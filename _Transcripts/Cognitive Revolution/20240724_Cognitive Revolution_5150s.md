---
Date Generated: October 30, 2024
Transcription Model: whisper medium 20231117
Length: 5150s
Video Keywords: []
Video Views: 1442
Video Rating: None
Video Description: Nathan hosts Riley Goodside, the world's first staff prompt engineer at Scale AI, to discuss the evolution of prompt engineering. In this episode of The Cognitive Revolution, we explore how language models have progressed, making prompt engineering more like programming than poetry. Discover insights on enterprise AI applications, best practices for pushing LLMs to their limits, and the future of AI automation.

Apply to join over 400 founders and execs in the Turpentine Network: https://hmplogxqz0y.typeform.com/to/JCkphVqj

RECOMMENDED PODCAST: Complex Systems
Patrick McKenzie (@patio11) talks to experts who understand the complicated but not unknowable systems we rely on. You might be surprised at how quickly Patrick and his guests can put you in the top 1% of understanding for stock trading, tech hiring, and more.

Spotify: https://open.spotify.com/show/3Mos4VE3figVXleHDqfXOH
Apple: https://podcasts.apple.com/us/podcast/complex-systems-with-patrick-mckenzie-patio11/id1753399812

SPONSORS:
Building an enterprise-ready SaaS app? WorkOS has got you covered with easy-to-integrate APIs for SAML, SCIM, and more. Join top startups like Vercel, Perplexity, Jasper & Webflow in powering your app with WorkOS. Enjoy a free tier for up to 1M users! Start now at https://bit.ly/WorkOS-TCR

Oracle Cloud Infrastructure (OCI) is a single platform for your infrastructure, database, application development, and AI needs. OCI has four to eight times the bandwidth of other clouds; offers one consistent price, and nobody does data better than Oracle. If you want to do more and spend less, take a free test drive of OCI at https://oracle.com/cognitive

The Brave search API can be used to assemble a data set to train your AI models and help with retrieval augmentation at the time of inference. All while remaining affordable with developer first pricing, integrating the Brave search API into your workflow translates to more ethical data sourcing and more human representative data sets. Try the Brave search API for free for up to 2000 queries per month at https://bit.ly/BraveTCR

Omneky is an omnichannel creative generation platform that lets you launch hundreds of thousands of ad iterations that actually work customized across all platforms, with a click of a button. Omneky combines generative AI and real-time advertising data. Mention "Cog Rev" for 10% off https://www.omneky.com/

Head to Squad to access global engineering without the headache and at a fraction of the cost: head to https://choosesquad.com/ and mention “Turpentine” to skip the waitlist.

CHAPTERS:
(00:00:00) About the Show
(00:00:23) Sponsor: WorkOS
(00:01:24) Introduction
(00:06:23) LLMs using LLMs
(00:09:38) Tool Use
(00:11:06) How to manage the breadth of the task
(00:14:51) Prompt engineering
(00:16:24) Sponsors: Oracle | Brave
(00:18:28) The importance of explicit reasoning
(00:21:16) The importance of breaking down tasks
(00:26:49) Multitasking fine-tuning
(00:31:49) Sponsors: Omneky | Squad
(00:33:36) Best models for fine-tuning
(00:36:41) The Platonic Representation Hypothesis
(00:42:02) How close are we to AGI?
(00:45:44) How do you know if youre being too ambitious?
(00:51:18) Best practices for generating good output
(00:54:33) Backfills and synthetic transformations
(00:56:59) Prompt engineering
(01:05:54) AGI, modalities, and the limits of training
(01:11:38) Compute thresholds
(01:13:02) Jailbreaking models
(01:16:09) Open-source models
(01:20:08) Solving the ARC Challenge
(01:23:20) How to Demonstrate Prompt Engineering Skills
(01:25:27) Outro
---

# From Poetry to Programming The Evolution of Prompt Engineering with Riley Goodside of Scale AI
**Cognitive Revolution:** [July 24, 2024](https://www.youtube.com/watch?v=wjaSyLHOUb0)
*  Hello and welcome to the Cognitive Revolution, where we interview visionary researchers,
*  entrepreneurs, and builders working on the frontier of artificial intelligence.
*  Each week we'll explore their revolutionary ideas and together we'll build a picture of
*  how AI technology will transform work, life, and society in the coming years.
*  I'm Nathan Labenz, joined by my co-host Eric Torenberg.
*  This episode is brought to you by Work OS. If you're building a B2B SaaS application,
*  at some point your customers will start asking for enterprise features like SAML authentication,
*  SCIM provisioning, role-based access control, and audit trails. That's where Work OS comes in,
*  with easy to use and flexible APIs that help you ship enterprise features on day one without
*  slowing down your core product development. Today, some of the hottest startups in the
*  world are already powered by Work OS, including ones you probably know like Proplexity,
*  Vercell, Jasper, and Webflow. Work OS also provides a generous free tier of up to 1 million
*  monthly active users for user management, making it the perfect authentication and
*  authorization solution for growing companies. It comes standard with rich features like bot
*  protection, MFA, roles and permissions, and more. If you're currently looking to build SSO for your
*  first enterprise customer, you should consider using Work OS. Integrate in minutes and start
*  shipping enterprise plans today.
*  Hello, and welcome back to the Cognitive Revolution. This is Nathan's AI voice clone,
*  powered by 11 Labs. The real Nathan is in Brazil this week to give a presentation on AI automation
*  at the Adapta Summit in São Paulo. And today's episode, featuring returning guest Riley Goodside,
*  the world's first staff prompt engineer at Scale AI, turned out to be a perfect prelude to that
*  presentation, which we'll share here soon as well. Going back to 2022 and into early 2023,
*  Riley became famous in the AI community for coming up with one clever prompting trick after
*  another. He was one of the first to put large language models into a read, evaluate, print loop,
*  or REPL, which most of us would now recognize as a precursor to AI agents. And I think you could
*  make a strong case that he had demonstrated the deepest, most practically useful understanding of
*  language models idiosyncrasies and outright weirdness of anyone in the world. Today,
*  our conversation reflects how much LLMs have continued to progress, even since GPT-4. As
*  models have undergone more and more post-training, the need for quirky tricks has declined. And as
*  Riley puts it, prompt engineering has become less like poetry and more like programming.
*  Meanwhile, in the enterprise context that Scale AI serves, companies are starting to move beyond
*  ad hoc chatbot interactions, and instead using the full range of best practices, including curating
*  gold standard examples, capturing reasoning traces, all sorts of retrieval, augmented generation,
*  fine-tuning, and anything else they can come up with. All to push language models to their
*  performance limits, with the goal of achieving human-level performance or better, and ultimately
*  saving serious time and money on routine tasks. It was a treat for me to dig into these topics
*  with Riley, and I was glad to find that our approaches are mostly in sync. For anyone building
*  AI systems, this episode is packed with practical value. And of course, I couldn't help myself from
*  sneaking in some questions about jailbreaking, the prospect for superhuman intelligence, AI safety,
*  and more along the way as well. As always, if you're finding value in the show, we'd love it if you'd
*  share it with a friend. Your support helps us continue bringing you conversations with the
*  leading minds in AI. The real Nathan will be back soon, but for now, he hopes you enjoy this deep
*  dive into the evolution of prompt engineering with Riley Goodside of Scale AI. Riley Goodside,
*  the world's first staff prompt engineer of Scale AI, welcome back to the Cognitive Revolution.
*  Thank you. It's great to be back. It's been a minute, and obviously a lot has happened.
*  In preparing for this, I went back to your Twitter feed, which was of course your original
*  claim to fame in the AI space with lots of super interesting examples coming out of the
*  Tex DaVinci 002 era. And I found you've been a little quiet on Twitter recently. I think the AI
*  community has certainly grown. There's lots of people doing that kind of stuff these days,
*  but what have you been up to that's had you quiet online in recent months?
*  Yes, there's a few reasons I've dropped off in my posting activity a bit. So the biggest reason
*  I've been quieter on Twitter is that I'm a father now. June of 2023, we welcomed our first child,
*  our daughter Felicity into the world. And it's been magical, but of course also time consuming.
*  So between that and working, it's left a bit less time for extracurricular posting on Twitter.
*  So not the total lack of progress since GPT-4 was introduced that has just given you nothing to talk
*  about? No, it's certainly not a lack of progress. I think there are other subtle factors at play,
*  though. So one, I think the other thing that's maybe a more mundane reason is just changes to
*  my situation personally at work. I think to some extent, my activity on Twitter was a campaign to
*  break into the AI industry and get me hired. It did that job. So I have a little less motivation.
*  Also, when you work for a company whose customers include much of the AI industry, you have more
*  people that you have to be sensitive towards. So it's harder to do some of the more reverent
*  material I guess I was known for earlier on. And I think the other thing too is really just
*  that I think maybe dominates in some ways are changes to prompt engineering itself.
*  I think this is maybe like a bigger topic that we could get into later in the podcast. But I guess
*  my TLDR teaser for it would be that I think modern prompt engineering is becoming more programming
*  than poetry and nobody really wants to do code review on x.com. We'll come back to that, but I
*  I'll leave it at that for now. Okay, cool. Yeah, that's interesting. Let's get to that very soon.
*  I think my comment on lack of progress since GPT-4 was hopefully understood as a joke. It was
*  meant to sort of allude to the sort of commentariat that's out. We've hit a wall. Nothing new has
*  happened since GPT-4. Oh, or GPT-4. It's all stalled out. That's definitely not my perspective.
*  As somebody who is an intensive user and increasingly seeing customers of scale,
*  presumably using language models in a lot of different contexts, what stands out to you most
*  in terms of the new capabilities that have come online? What do you think has really
*  been the biggest difference maker or driven most value over the last, say, year and a third since
*  we first got to see GPT-4 in public? I think a lot of the progress lately,
*  it's becoming maybe harder to describe, maybe a bit more diffuse across many different tasks.
*  One area of capability that I've been excited about for a long time really is use of REPLs and
*  the Chachibit code interpreter, as it used to be known. I think it's now advanced data analysis
*  and other projects that extend this idea even further like Julius AI of giving the AI an
*  interpreter environment to work in. I think there's a lot of progress that's been made and still a
*  lot of alpha to be found in increases to that capability. We're in this regime now, I think,
*  where LLMs could benefit a lot from knowing how to use LLMs. There are still things to know as a
*  user about what tasks an LLM is good for. It's not quite as much as it used to be. For example,
*  like GPT-3 would very reliably never say, I don't know. If you asked it a question that had no
*  answer, it would still just make one up and you had to remind it that saying, I don't know is an
*  option. That sort of knowledge is becoming easier, but it's still there. The things that you have to
*  understand that this is a classic example of a tokenization problem that an LLM would struggle
*  with. LLMs don't have that sort of, I don't know if you would call it situational awareness, but I
*  guess it's a form of that, of an advanced situational awareness of the circumstance that
*  they themselves are in as LLMs. I think that there's still a lot to be gained from just these kind
*  of bread and butter improvements of training on data that reflects usage of these features.
*  I think in some sense, when the internet was scraped to train, say, GPT-3, it was an internet
*  that didn't contain examples of chatbot dialogues as we see all the time today. Even just as you
*  think in pre-training, you learn more about how a chatbot behaves, scraping from the modern internet
*  than you did before. There was more that had to be built in post-training in order to flesh out
*  the fictional character of how a chatbot stereotypically behaves. That's very exciting
*  to me, that more of this data is disseminating through the culture, getting filtered. People
*  are picking out which dialogues are worth sharing and worth remembering and high quality.
*  The best parts of this are going to be fed back into the models, and they're going to have more
*  of this very practical skill that I think they're uniquely lacking and uniquely in need of being
*  able to use themselves and be able to use other LLMs and understand the limits of their
*  capabilities. I think code is the most promising avenue for that. In code, you can represent
*  understanding of a very wide variety of systems, and LLMs are one such system that you can have
*  code that uses LLMs, that code can be understood. I think that we're going to see a lot of lift just
*  from that recursive process continuing. That obviously suggests a focus on agents,
*  to put it plainly. I guess two questions I have there are part one is how would you characterize
*  the frontier of capabilities right now when it comes to tool use? You could break that down in
*  terms of how many tools can a language model be provided and still work well, or how complex,
*  maybe some tips for, or do we need few shot to get them to work well with tools? I think a lot
*  of people have seen this stuff, but I think very few people still have much experience in terms of
*  actually getting deeply hands-on with tool use. I think for tool use, it's often a case where
*  you want to have fine tuning, just because there's a lot of subtleties that go into using real world
*  APIs that you would need to communicate to the model. That can be done through long context,
*  it can be done through examples, and that's often a good way to get the data that you would want to
*  tune on. But I'd say that's a case where you're more likely than other tasks to see a need for
*  fine tuning to get the reliability that you would want for something that's going to call out to
*  other APIs. You can otherwise see issues with it forgetting just details of the semantics of how
*  some JSON structures to be called or so on. In cases like that where you have a very rigid
*  structure to your generation, it doesn't take many examples to help. Maybe to drill in a little bit on
*  fine tuning of language models for this tool use capability, how general versus broad do you think
*  people should be thinking of? Most of the fine tuning I've done has been single task, and that
*  makes my life pretty simple in the sense that I can just focus on the single task. I'm trying
*  to maximize performance. I'm controlling the environment in such a way where this model is
*  never going to be asked to do anything besides this task, and that makes the situation relatively
*  easy from an evaluation standpoint. If you're in a tool use domain, maybe you can narrow it down to
*  that super specific task where you're like, it just has to do the one thing, but inherent in tool use
*  is that you want a little bit more dynamism out of the system, or at least that's where my
*  intuition is at the moment. Then you have a challenge of, man, I'm starting with a base
*  model that a world leading company has created to be a very general purpose tool, and I'm going to
*  narrow it consciously or unconsciously through this fine tuning process, but I still want it to
*  be somewhat general. How do you think about managing, first of all, how broad or narrow
*  you should aim for, and then how do you actually keep things as robustly general as possible while
*  you're doing fine tuning? Yes, the progression I usually use is you start with a prompt,
*  right, just a sort of instruction prompt or MVP of how you'd want the task done,
*  continue on to including k-shot examples, add more k-shot examples until no more will fit,
*  and then start worrying about k-shot selection that doesn't even necessarily have to use embeddings,
*  just pick some method of selecting k-shots and find something that works, and from there there's
*  a lot of extensions going to rag and so on, but only once you've maxed out those options I'd say
*  you want to dive into fine tuning, both because they're easier and lower investment, but also
*  because it's not wasted effort. I think you get from the prompts and the especially expensive
*  long prompts that have wasteful amounts of context in them, you can get high quality answers that
*  would be useful in say k-shot selection or fine tuning, so you're not losing anything through that
*  work. But I think the thing that people forget throughout this whole process of refining from
*  like a prompt to a more advanced prompt engineered pipeline is decomposition, that at each step you
*  really just want to be asking yourself, is there any piece of this task that I could pull out and
*  make it easier and make it simpler, that I could delegate to a smaller LLM, that you could maybe
*  delegate to something that isn't an LLM at all, that can really help a lot with performance,
*  especially just digging into your data and I think using your intuition of like how could you fix
*  this, like how could you fix this one example, and make your data better just by tweaking your
*  data a bit and providing more context and generating more examples to tune on. I think people really
*  just neglect annotation really and labeling, they neglect just the need to put thought into
*  coming up with examples of the problem, both in the sense of doing the task well and having
*  high quality examples of their task being done, but also in correctly thinking about the distribution
*  of inputs, like what is a realistic input to this task, what needs to be demonstrated, and also what
*  are the edge cases. I think that's something that isn't emphasized enough, that you really want to
*  be considering what are the boundary conditions through which your high level task could break,
*  right, or where the output might be ambiguous or unclear to what you're looking for, and you want
*  to define those cases so that it can see every real world example as sort of an interpolation
*  of the examples that you gave it. So I think there's a lot of roads you can take that lead
*  to fine tuning, but they all converge on that last step. You could have many different ways that you
*  could produce high quality data to tune on, but they all collapse into the same approach at the end
*  if you get to that point, right, and you may not, right. There are many cases where simply
*  prompt engineering is the answer, and sometimes it's soda if you're willing to spend enough on it.
*  I think there was a great instance of this. I think this was at Microsoft, built a prompt
*  engineering pipeline that managed to beat, I think it was MedPalm, that was like a version of Palm
*  that was fine tuned for medical questions just by using a non-fine tune, a non-specialist model that
*  had a very complicated pipeline of prompt engineering on top of it, right. And I think
*  this is in some ways not always the answer you want to hear that it's going to be complicated,
*  that you're going to have this massive inference pipeline at the end, but for real world problems
*  that's often how it ends up, that simply having more examples will get you there faster.
*  I think one good intuition builder for this is that at the limits of k-shot selection,
*  the problem is always trivial, right. So if you have enough examples that you can find
*  this problem that you need to solve, then it just copies the answer, right. So you can think of
*  k-shot selection as a sort of pre-computation, and the space of what you could pre-compute
*  is very wide open. I think the computational approach of it, I think, is worthwhile of thinking
*  about what aspects of the reasoning and deduction that produces an answer are being performed in
*  each step, and how can we split those out? How can we make them more explicit? Hey, we'll continue
*  our interview in a moment after a word from our sponsors. AI might be the most important new
*  computer technology ever. It's storming every industry, and literally billions of dollars are
*  being invested. So buckle up. The problem is that AI needs a lot of speed and processing power. So
*  how do you compete without costs spiraling out of control? It's time to upgrade to the next
*  generation of the cloud, Oracle Cloud Infrastructure, or OCI. OCI is a single platform for your
*  infrastructure, database, application development, and AI needs. OCI has four to eight times the
*  bandwidth of other clouds, offers one consistent price instead of variable regional pricing,
*  and of course, nobody does data better than Oracle. So now you can train your AI models
*  at twice the speed and less than half the cost of other clouds. If you want to do more and spend
*  less like Uber, 8x8, and Databricks Mosaic, take a free test drive of OCI at oracle.com slash
*  cognitive. That's oracle.com slash cognitive. Oracle.com slash cognitive. This episode of the
*  Cognitive Revolution is sponsored by the Brave Search API. You may know of Brave as an alternative
*  to Chrome, but did you know that Brave has its own independent search engine powered by its own
*  20 billion page index of the web? The Brave Search API gives developers reliable and affordable
*  access to programmable web search, auto suggest, spell check, and more, with flexible plans for
*  all types of use cases from rag search to automated business intelligence. On top of that, it's up to
*  three times cheaper than Bing, all without compromising on quality, speed, or reliability.
*  Over 700 businesses, including Coheer, Chegg, and Kagi, rely on the Brave Search API, and a
*  recent survey showed that 94% of customers would recommend it to their peers. To start building
*  apps with the power of the web, sign up at brave.com slash API and get up to 5,000 free monthly calls.
*  The
*  mention of reasoning and mention of explicitness focuses my attention on the chain of thought or
*  the reasoning traces. By the way, I basically pursue essentially the same protocol that you
*  mentioned. I'm actually working on a, I think it'll probably be an upcoming episode on just
*  an introduction to AI automation best practices. What you articulated there is pretty much what
*  I'm trying to create flow charts, whatever to distill for people. I have found personally that
*  the quality of the reasoning traces in the examples is super important. And that is often an
*  overlooked piece when people go and do this because it is often implicit. If you take,
*  for example, the task of responding to a customer service ticket, what people will have is they'll
*  have the ticket that came in and then they'll have the response that was sent. But the sort
*  of internal notes, which usually does exist as a field in the ticket system, is often very
*  minimally filled out, if at all. And it certainly does not contain the actual thought process that
*  the person went through that's like, I'm going to do this because of this. And I noticed this. So
*  that's got me thinking this and getting that stuff out of people's heads and onto paper, so to speak,
*  is something that takes some social engineering sometimes. You got to go figure out who does this,
*  how do they do it, even interview them to try to pull that information out. But I have found that
*  to be a critical element to performance. I've done most of my fine tuning on GPT 3.5. We're now about
*  to see, I think, a whole set of options of next generation models coming online for fine tuning
*  as well. But at the 3.5 level, I found that if I just did inputs and outputs, it didn't seem to
*  grok exactly what I was trying to get it to do. And it was really important to have that explicit
*  reasoning trace there. So basically, I just wonder if you've seen the same or if you have any sort of
*  refinements on that summary. No, I think that's exactly right. That human produced text. If we
*  think of natural text that we find out in the wild, this text sometimes, it has sort of one mode of
*  behavior where it resembles a sort of a recording of our conscious awareness of the thoughts in our
*  heads, right? That you can see like reading something as being like playing moment by moment
*  thoughts that a person was having as they were coming up with these words. But there are violations
*  of that. Like a good one is calculation. Anytime you see in text something that says just casually
*  tells you what 57 times 125 is, you are getting data that isn't part of that flow,
*  right? It's the result of somebody stopping and pulling out a calculator and doing the math
*  and then resuming the transcription of their thoughts after that. And that shows up in a lot
*  of ways. That you see text that isn't always just what came to somebody's mind naturally is the next
*  thing to say. It's the result of experience. It's the result of seeing something in the real world,
*  possibly years of experience, history summarized or whatever. And that shows up in so many places
*  and in so many tasks and so many things that we think of as like demonstrations of a task being
*  performed. We're not really capturing all those pieces missing in the middle and attempts to
*  address this through the history of like attempts to address calculation errors in LLM's, right?
*  So it's very apparent that LLM struggle with calculation. And I think it's for kind of the
*  reasons that I was saying, that in real life like calculation summarizes over many steps
*  and we don't record those steps on paper. And if you let an LLM record those steps,
*  if you let it think longhand and go through the steps of like reasoning through the digits,
*  it's much more likely to be correct. Not perfect, but more likely. And getting that kind of thought
*  out of your answers is very important. And I think it's also a classic case for the power of
*  augmenting with synthetic data, being able to generate like chain of thought rationales for
*  particular answers. Especially, I think people don't appreciate always that there's a difference
*  between chain of thought that the model generates itself and say chain of thought that somebody
*  else generates. And that if you were to imagine that you were to prompt a model on some, you have
*  some data set of questions for it to answer. And then for each one, you ask it to think step by
*  step and it generates some rationale for its answer. If you were to tune on those rationales,
*  let's say you filter them to only the ones that lead to consensus answers or correct answers,
*  but consensus being a proxy for that, you're tuning on rationales that empirically led to
*  the correct answer for this particular model. That empirically, like when the model does this,
*  when it zigs this way instead of zagging, it lands in the right place more often. And so it's going
*  to learn these general reasoning steps that perhaps very idiosyncratically apply to this model
*  about how it specifically should do reasoning. And that's not always true if you have just even
*  reasoning steps made by some other model or especially reasoning steps given by a human.
*  They're not really going to capture all of the deductions that they were making that led to
*  things being decided. So I think the effort spent making that more explicit is rarely wasted.
*  Of breaking out your task into more sub-steps, annotating pieces of tasks. I think there's a lot
*  of forms the data of a task demonstration can take. If you put your mind to it, you can flip
*  fields around. So every English to French translation is also an example of French
*  to English translation. There's a lot of higher order transformations you can do your data
*  to create a synthetic pipeline for producing the data that's worth tuning on. I think maybe
*  a more concrete example of this, it was a paper where they were trying to show that models behind
*  fine tuning APIs can be tuned to be unsafe even if the data sets that you're tuning on
*  is monitored by another LLM to look for signs of unsafe activity. Because it's well known that
*  as long as you can tune a model, you can give it something bad to some examples of doing bad things,
*  it will do those bad things. So the defense against this is that model providers will have
*  filters that look at the data that you're tuning on and ask high level questions like,
*  what is the purpose of this? What are you attempting to achieve here with this fine tune? And is that
*  bad? So what they did to defeat this is they first came up with a text encoding method that
*  they verified that this particular LLM couldn't understand. And I think that they called it
*  Walnut 53 or something like that. And it was just literally like you'd permute ASCII characters by
*  seed 53 in NumPy to get like a permutation order of them. And then you apply that as a cipher
*  to the text. And they demonstrated that like the LLM without tuning could not understand cipher,
*  even when it was explained and given examples and they did various tricks. But they found that
*  they could get it to understand it through tuning. They created examples where a task is given in
*  this new Walnut 53 encoding. Then the LLM's response is to repeat the task in plain text
*  and then to complete the task in cipher text in Walnut 53. And after tuning on examples of this,
*  I think that they had a few other tasks in there too that may have been like pure translation,
*  things like that. But these were bridge tasks. Their true purpose is just to get the model to
*  the point that it could understand this particular encoding and then understand the payload, if you
*  will, of task demonstrations that have the model doing unsafe things and are encoded with a cipher
*  so that the filtering LLM can't understand them. I think this is a good case study in the sort of
*  problem that an LLM just can't do before fine tuning and how you would get it there,
*  of breaking the task up into easier steps and incrementally getting it to be good at each of
*  these smaller tasks and then composing them into the thing you actually want to achieve. So I think
*  in a fine tuning context that can work as well. You can like multitask fine tuning sometimes has
*  its benefits. There's trade-offs there too. But I think just that decomposition is really like one
*  of the most important and overlooked parts of it, of saying what are the pieces of this task that
*  if it were good at, it could do better on the rest. Because even if your high level task that
*  you're trying to achieve is hard to demonstrate, if there's some particular skill that it's missing
*  that isn't hard to demonstrate, it might be worth it to demonstrate it.
*  Soterios Johnson Interesting. Okay. That is a fascinating example.
*  So just briefly on multitask fine tuning, let's say I do have one of these skills that
*  a language model just can't do, whether it's using my private APIs because that's not in the
*  training set or some weird cipher along the lines of what you just described. And I want to fine
*  tune that in. But I also want to keep the generality. My goal is to have an in-house chatbot
*  where I would be able to say, hey, it's just like chat GPT or it's just like Claude, but it can use
*  our own internal APIs. Sweet. Okay, cool. Now, if I want to do that fine tuning, I can't just give
*  all the examples of every example can't be using my internal APIs, right? Because then I'm going to
*  presumably overfit and I'm going to start seeing the model start to want to use our in-house APIs
*  when it shouldn't in actual day-to-day use. Right? So is there any like best practice recipe that
*  you could point to that would be the sort of you handle your specific capabilities that you want to
*  add to the model? And then you also mix in some other data set of just like general chats or
*  something like what's the best practice for maintaining that generality while instilling
*  the new thing that you want it to know? Yeah, that's a great question. I think like the first
*  piece of advice I would give is avoid the problem if you can. The fine tuning does it. Wait for GPT-5.
*  That's one strategy. But more immediately, fine tuning has a cost. It's not free. And one of those
*  costs is that you lose more general skills. And there's also some more specific issues that show
*  up. There was a paper not that long ago that showed that fine tuning a model on any kind of
*  new information, like new factual information, will make it more likely to hallucinate in general.
*  Like that it would be more likely to make up just information out of the blue.
*  And logically, you can imagine why this is. The model has some understanding of what statements
*  are true or come from this great body of text that we think of as the real world, or like describing
*  the real world. And if you tune it on something that isn't in that body of knowledge, you're telling
*  it that new things are okay. The stuff that seemed weird to you in some deeply ingrained sense that
*  you learned during pre-training isn't necessarily wrong. So ignore that instinct sometimes. And once
*  you ignore enough of those instincts, you start to hallucinate. And I think that's like a good mental
*  model to keep in mind of what you're losing is the opportunity cost for tuning. For what you can do,
*  you mentioned a few strategies that are classic. One is mixing in more general data. The best
*  thing you can do, of course, is if you somehow have access to the pre-trained data, but you don't.
*  So you find some other similar source of chat data that you could mix in there. And that works well
*  for preventing some of the forgetting. If you're dealing with like an open source model where you
*  have full control of the weights, you can do like weight mixing. You can tune on your task and then
*  evaluate on some benchmark of both your narrow fine tuning task and some more general tasks that
*  you want to preserve. And you would determine empirically what mixture of the weights optimizes
*  both of those scores in the way that you care about. Another trick that I've heard anecdotally,
*  and I'm not sure if there's a paper for this or if it's just something I heard offhand once on a
*  Twitter thread, is when you fine tune on your narrow task, if you have the option, say like
*  Llama 3, you have both a base model and an instruct model. What the server's suggesting,
*  and they were saying that worked really well in practice, was tuning the base model rather
*  than the instruct model, and then taking the delta of the weights between the tuned model
*  and the base model and applying that delta to the instruction-tuned model. This is a very crude
*  outsider way of thinking about it, and probably wrong in the details, but my mental model of it
*  is the fine tuning comes first. You think the process of RLHF, you tune it into a particular
*  mode of instruction following before you put this finish of RL polish on it. Conceptually,
*  you can almost think of it as a way of closer to sliding it in under the polish, or not disturbing
*  what was learned through RL. I haven't actually tried that myself, but I've heard that it works.
*  Mad Fientist-Liepkowski Yeah, interesting. I think that sort of
*  weight Frankensteining, which is my umbrella term for those sorts of techniques, is super interesting.
*  I expect a lot more to come out of that, especially as we get deeper into the Lama 3 era and the Lama
*  3 400B era, but allegedly will be beginning very shortly. It seems like there's probably a lot more
*  that can still be figured out there in terms of how to just monkey around with weights in all kinds
*  of different ways and still recombine them in useful ways. That's a really interesting anecdote.
*  Hey, we'll continue our interview in a moment after a word from our sponsors.
*  Omnike uses generative AI to enable you to launch hundreds of thousands of ad iterations that
*  actually work customized across all platforms with a click of a button. I believe in Omnike so much
*  that I invested in it, and I recommend you use it too. Use Cogrev to get a 10% discount.
*  Hey all, Eric Torenberg here. I'm hearing more and more that founders want to get profitable,
*  do more with less, especially with engineering. Listen, I love your 30-year-old ex-Fang senior
*  software engineer as much as the next guy, but honestly, I can't afford them anymore.
*  Founders everywhere are trying to turn to global talent, but boy is it a hassle to do at scale,
*  from sourcing to interviewing to on-the-ground operations and management. That's why I teamed
*  up with Sean Lanahan, who's been building engineering teams in Vietnam at a very high level
*  for over five years to help you access global engineering without the headache. Squad, Sean's
*  new company, takes care of sourcing, legal compliance, and local HR for global talent
*  so you don't have to. With teams across Asia and South America, we can cover you no matter
*  which time zone you operate in. Their engineers follow your process and use your tools. They work
*  with React, Next.js, or your favorite front-end frameworks. And on the back end, they're experts
*  at Node, Python, Java, and anything under the sun. Full disclosure, it's going to cost more than the
*  random person you found on Upwork that's doing two hours of work per week but billing you for 40.
*  But you'll get premium quality at a fraction of the typical cost. Our engineers are vetted
*  top 1% talent and actually working hard for you every day. Increase your velocity without
*  amping up burn. Head to choose squad.com and mention Turpentine to skip the wait list.
*  What are your favorite models today and what are you most excited to fine tune? Last time we did
*  this, you gave us a great walkthrough of the stages of fine tuning. You did show goth and
*  the instruction tuning and the RLHF meme with explanation of how it worked and whatever.
*  I wonder if you have a characterization of the different models today. What's OpenAI as a series
*  best for in your mind? Where does Claude shine? Where does Gemini shine? And how do you think
*  that will potentially play out, especially as these fine tuning things come online? Is
*  there any heuristic that I should have for thinking about what to fine tune first?
*  Yeah, that's a great question. I think the main thing I'd want to emphasize here is
*  the best model is the one that does the best on your task.
*  So whatever you're using the model for, you really want to evaluate all of the reasonable options
*  because performance on different task domains is all over the map. You might find that one
*  model is good poetry, another one is good code, and they don't have to be the same model. So
*  it's worth testing. The leaderboards are a guide, but I think part of the strategy that we're really
*  emphasizing with our sealed leaderboards is breaking out particular domains. So we have one
*  leaderboard that's just for coding. We have another leaderboard that's precise instruction following,
*  and we explain on the website the different procedures we go through for making these
*  data sets. We have people coming up with role play scenarios where you do an act as if exercise
*  of imagining that you're in a certain professional role, coming up with tasks you would do in that
*  role. And then we have other people producing examples of those task demonstrations. We get
*  a diversity over the space of how the user would actually use the model. But I think having that
*  domain specificity is really necessary even just for the initial guidance of what model to pick.
*  And beyond that, I think asking around or even just looking at local law on Reddit has a good
*  place if you like smaller models and things like that. I think you'd be surprised at just how
*  fitly it can get. You would find that some models are much better than others at certain languages.
*  So if you need to work in a particular language, your ranking of which models are best could look
*  very different. And also I think in practice, you might run into just annoying issues.
*  And one model or another, you might find that once it writes technical docs in Spanish,
*  it sometimes just switches back to English. And then another model doesn't have that problem.
*  And so that's something that maybe doesn't show up on benchmarks, but it matters a lot to you.
*  So those are the kinds of things that I think people underestimate how frequent they are and
*  how little they show up in benchmarks. But I think you really want to use benchmarks as just
*  a guide to what to try and then to let data be your guide there. And also I think a lot of it is
*  a cost exercise as much as anything that you really want to think through what are your expected
*  volumes and how much are these things going to cost because things can inflate fast, especially
*  when you have L and consensus pipelines and so on. Is the difference in models today mostly
*  something that is a result of different post-training strategies? I'm thinking here of
*  this paper called the Platonic Representation Hypothesis, where I thought this was a really
*  striking paper. Basically, what they look at is the internal representations of concepts
*  within different models at different scales. And they show that as the models get bigger,
*  the representations appear to be converging. They become more similar as models get bigger.
*  So in other words, your smaller models are more different, your bigger models are more similar
*  in terms of the internal representations that they have for concepts. Obviously, taken to the
*  limit, you get something like the Platonic Representation, where it converges on reality,
*  and it's got some sort of compressed world model. Now, whether we ever actually get there or not,
*  maybe another interesting question I'd like to get your take on. But if that is happening,
*  and if all of the big leading developers today are presumably tapping into largely similar
*  giant pots of data, then one might infer that the reason there are different characters or different
*  strengths and weaknesses, why is one better at code versus poetry or what have you, is potentially
*  down to the post-training strategies and maybe also explicit trade-offs that companies are making
*  internally that where they may be saying, we want to emphasize this over this for whatever reason.
*  Is that how you would understand it? Yeah, I think that's right. I think the longer I use LLMs,
*  the more I see them as a sort of compression of text, a compression and an interpolation of the
*  training data. And that sort of interpretation naturally applies to the perspective that these
*  models are getting better largely because of post-training, because of the human demonstrations
*  that are going into them. And I think that's going to be increasingly true as we run out of room
*  in scaling laws. We're not there yet. I'm not entirely qualified to say exactly how close we
*  are, but my guess is we still have a bit of runway there. But I think the broader trend,
*  though, is clear. That scaling will slow down at some point, and the gains beyond that are in
*  post-training. But I don't see that as a major roadblock. I think that we don't even fully
*  understand how much room there is to grow in post-training. I think the space of things that
*  we could potentially be training models on is very wide open. I think maybe one of the clearest
*  demonstrations of that is recent video models. We've seen that the same strategies that predict
*  text can predict tokens that represent video, and this actually produces something that is realistic.
*  So I think we're going to find that there's a lot of things that can be turned into text.
*  It wouldn't surprise me at all if a year from now you start having models that just produce
*  executable binaries, or other forms of data that you wouldn't necessarily have to do a token
*  representation of an image. You could just start spitting out JPEG. And maybe those are impractical
*  or silly examples, or maybe technical reasons for any given one of these things why it's not worth
*  it. But I think in the general class, there are things that are worth doing.
*  Yeah, 100%. I might mind immediately there jumps to biological sequence-trained models and
*  generations. And those are still in the sort of GPT-2, maybe into the early GPT-3 kind of era.
*  Those have a long way to go, I would think as well. And that's going to get really weird,
*  is my expectation, because nothing makes the, like, can a chatbot help me build a
*  bomb feel more quaint than just the chatbot, like, actually just straight away out putting
*  a new virus sequence or whatever. And that is coming very soon, if not really already.
*  It's maybe still not quite there in terms of actual viability, but scaling laws seem to hold
*  there as well. So I guess most of the gains are coming from post-training. It seems pretty clear
*  that all the gains over the last year and change have come from post-training, or like the vast
*  majority of them, because we haven't seen, like, another order of magnitude scale up in model size.
*  In fact, prices have dropped precipitously, so there's been, like, presumably a lot of
*  efficiency gains under the hood. I don't know how many parameters we're dealing with these days,
*  but presumably, like, the models we're calling now have fewer than the 175 billion parameters.
*  So we haven't seen that scale up yet. I guess, first question, just to be clear, like,
*  you would expect that there is going to be another quantum leap with another scale up if we go from,
*  say, 10 or 15 trillion tokens for GPT-4 or LAMA-3 to, say, 100 trillion tokens. Like,
*  you would expect that that would be, like, a qualitatively different model that gets
*  spit out of the other end of that. Is that correct?
*  Yeah, it's sort of an irony in that we have these scaling laws that tell us how perplexed it will be
*  by natural text. But how that translates into actual skills is really anybody's guess. But
*  I think we certainly have only been surprised in one direction before.
*  Okay. So now coming back to today's models, let's say you have time and resources to do the
*  generations, to do the rag pipeline, to do the fine tuning, to iterate on it, to really put the
*  elbow grease in to make the thing successful. Is there any guidance that you could give people on
*  what is the limit of performance there? Another way to ask this would be, like, how close are
*  we to AGI? There's, like, a sort of state of, like, fine-tunable AGI, where it's, like,
*  if the definition is AI that can do the majority of work as well or better than a human,
*  people tend to think of that as, like, okay, just a single model doing it all. But if I were to
*  reframe that as for any given task that humans do, can we fine-tune? Can we find examples? Can
*  we fine-tune? Can we dial in the performance to get it there? How would you characterize the
*  frontier of what is possible today with all that extra work beyond the base models,
*  I don't mean base as in not post-trained, the models that were given by the companies and what
*  we can get to if we do all that work that we've been talking about to really focus in on a specific
*  thing? How could you characterize that frontier? Are there things you could say? These are
*  definitely out of bounds. Obviously, ARK has stimulated this conversation recently because
*  the models are not that good at ARK. Even with a lot of examples, they're still not that great,
*  maybe with fine tuning, but it's unclear. It seems like it's probably not going to get to that 85%,
*  even tuning GPT-4, although maybe, I don't know. If we were to do that elbow grease for every given
*  task of interest, how close are we to that AGI definition? That's what I'm trying to get at.
*  I think the definition of AGI that's out there, which is probably heavily influenced, I think,
*  by OpenAI's definition of systems that can do the vast majority of all economically valuable
*  human laborers like that. The issue I have with these kinds of definitions is that on the highest
*  level, this is a moving target. If you think of what is economically valuable work that humans
*  put out, before the Industrial Revolution, most, probably around half of all humans were involved
*  in farming. You were somewhere in the chain of agriculture. The number, I believe, is now
*  lay like 2% or something like that of all Americans who would work in farming. By that metric,
*  that's 48% right there of human labor that got automated by tractors and the other farm
*  equipment we've come up with. But when things like that happen, it changes what it is that humans are
*  doing. That we find other things to do with our time and economically valuable human labor becomes
*  something else. I think we are seeing smaller versions of that even now with, say, translation.
*  The LLMs are increasingly good at translation, transcription of videos. Those tasks are pushing
*  humans out of that work into other work. We'll see as humans get pushed out of work that's
*  automated, they'll move into other tasks where LLMs aren't as good. Our definition of what is
*  human labor will change. That's maybe a bit of a cop-out because you could still say,
*  okay, let's freeze it now at 2024 and say of all these things, let's do those. But I think even
*  there, it doesn't get us to the thing that I think a lot of people implicitly imagine when they hear
*  AGI, which is that humans are these fountains of new possibilities of things to move to.
*  When is the model going to be that? That's a slightly different definition. Maybe it is
*  the same definition, I guess, just applied more iteratively or recursively, I guess,
*  of saying that when will it do truly everything and that there's no task at all that we can imagine
*  that humans will do. I think we're a ways away from being able to think coherently about that,
*  of what does it mean to have no value in humans doing, say, philosophy, because all philosophy
*  has been figured out better by machines. I think at the point that we start to have to worry about
*  AGI, economic terms go out the window in some sense.
*  Okay. Just to take the other side for a second, is there anything that you would say,
*  how do you know if you're being too ambitious? If I want to say, okay, I've got this
*  task in my business and I've got a person doing it full time, they're doing fine, but the volume is
*  growing, they're going to have to hire two more people to do this thing, or maybe I can bring AI
*  to bear on the problem. Is there any way, any framework or whatever to get to good judgment on
*  is this going to work for a given task? I can throw a million examples at you and you could
*  evaluate them one by one, but is there any way we can abstract from that and say, okay, this is where
*  you're reaching too far? Any common mistakes or any overreaches that you would warn people against?
*  I think a good rule of thumb is LLMs can do tasks, not jobs. If you have something that you can
*  get down to a repeatable unit of a task, something where you can imagine the inputs and outputs laid
*  out as text on spreadsheet, that's potentially something that you can automate. I see a lot of
*  novice users of LLMs will ask them for a business strategy or something, what's an idea for a
*  startup or whatever. I can't imagine any LLM is going to give you a good idea for a startup,
*  anything like that, especially where it's current. You're not going to get that kind of originality.
*  I'd say that's probably one of the more common pitfalls is people asking for information that's
*  in this nexus of being recent and competitive. Writing a funny joke is maybe one of the
*  purer forms of this. The LLMs aren't going to be able to tell you a good joke, except in the sense
*  of maybe regurgitating one or applying something to a mold because humor changes so quickly.
*  The things that were considered world-class humor in the 30s probably wouldn't get very
*  many chuckles today. It's that competitive landscape of people trying to serve expectations
*  and trying to surprise people. That just isn't what we typically get out of LLM. Humor is probably
*  the archetype of something that LLMs aren't going to be great at. The less humor like it is, the more
*  chance you have succeeding. Something where you're not looking for it to be surprising and creative
*  in a way that nobody's done before, where you're implicitly in competition with everyone else that's
*  trying to do this task. That's good. I often say precious few eureka moments from AI systems.
*  On the flip side of that, the more routine it is, the more we know what good looks like,
*  the better chance we have of getting there. That narrows the scope to things where there is a best
*  practice or a standard of care or some reasonable consensus as to what is good. If you don't have
*  that consensus as to what is good, you're in trouble. Yeah, go ahead. Though to balance that
*  out, I will add that I do sometimes see sparks of these. Sparks of AGI. Maybe not sparks of AGI,
*  but sparks of connections that I feel confident are novel. I had an example a few months ago,
*  right in over here. It was on a YouTube video. I heard somebody remark very quickly
*  the name of the Python library adders, A-T-T-E-R-S, it was, quote, not a very nice thing to say to
*  somebody in Dutch. I wanted to know what did that mean? What were they referring to? When I posed
*  that question to Chagy B.T., it got it right. It explained that there's a Dutch insult called
*  Eter. I think it was E-T-T-E-R. I forget exactly what it means, but it passed or something like
*  that. It made that connection. Logically, it's not going to see that anywhere because it was in a
*  YouTube video unless they happened to transcribe that one video and then nobody was talking about
*  this video. It's not something that it could have found out there. I think you do see these
*  little reminders that it's not entirely missing novelty. Yeah. An interesting challenge there is
*  identifying the good ones. I remember the Google paper fund search where they set new state of the
*  art on a couple interesting, pretty esoteric, from my perspective, open math problems. One was
*  a packing problem, how to pack these balls or whatever into a space in the most efficient
*  possible way, that kind of thing. This has been something people worked on for a long time.
*  They were able to advance the state of the art by doing huge numbers of generations. The key that
*  they had in terms of an advantage is an objective function to score the little programs that the
*  language model was writing. Then they basically just aerated through keeping a couple of the best
*  highest scoring things and saying, hey, this is our best. Give me something else. They also did
*  have one interesting strategy for trying to make sure they didn't get too trapped until a local
*  maxima and try to make sure they would explore other parts of the space. But they were able to
*  advance the state of the art. It seems like a key thing there that they have though that we don't,
*  in general, have is an objective score on the problem. If you were trying to do humor and you
*  were like, okay, I see sparks occasionally of good humor from the language model. I don't want to
*  read a million bad jokes to find one diamond in the rough. I think the same problem, by the way,
*  applies for tons of things. People want to generate social media posts. They'd probably
*  be happy to spend 10 times more on tokens to get one thing or even 100 times more on tokens to get
*  one good thing if they could reliably actually select out the one good thing from the 100x more
*  generations. Is there any best practice or any tips that you could advise there for when like,
*  okay, I'm willing to pay up to generate tons of stuff, but now how do I narrow that stuff back
*  again to what's actually good? Do you trust the models to do a decent job of that?
*  To a point. I think maybe not for humor, but for a surprising number of tasks,
*  simply generating more and then taking the best of that through even imperfect or crude methods
*  can help a lot. A very basic way of approaching this is just generate multiple answers,
*  pass all of them back to a long context LLM and say, which of these is the best? That's
*  maybe a little too crude, but there's more sophisticated things you can do. But what I
*  would recommend most of the time is do comparisons rather than scores between different generations
*  that you have. And from the comparison, the wins, losses and ties, you can produce an ELO score and
*  use that to determine which one is the best. This can really help a lot. It's hard to overstate.
*  So much of whether an LLM does a good job or not is happenstance. And you want to just give it more
*  attempts. I think there was a paper that showed that you would get roughly equivalent performance,
*  I think, from doing 40 API calls to GBT 3.5 as you would for one API call of GBT 4. That's the
*  exchange rate. So intelligence has a steep cost, but it does keep going to some extent. You can
*  just keep generating more answers with GBT 4, rank them and take the best ones. And then from there
*  there's refinements to that process that can help a lot too. Coming up with better procedures
*  for ranking things. Trying to think how much I can share there. But even crude things do work.
*  Even things as simple as just asking the LLM which is best can help a lot. But wherever there are
*  indicators of quality in your domain, you should use them. So if you're using code,
*  like you're generating code, you could use unit tests or you could execute the code and see what
*  the results are. If you're doing translation and you want to know if this is a good translation,
*  back translate. So go from English to French, go from French back to English,
*  and then have a model assess is the English roughly the same as your original English or is
*  there some substantial difference that implies that a mistranslation happened. That's a
*  contrived example because you wouldn't be doing this translation, but apply to your own task.
*  I think so much of the work of making LLM-powered systems better really comes from setting up these
*  pipelines of ad hoc quality filters and checks and evaluations on your examples and making sure
*  that there is no bad data on your examples, that you're not putting bad demonstrations,
*  and that you're pulling in case shot examples that really match the structure of your task.
*  And the closer you can get to that structure, the better your performance will be. And often
*  that change, that structure is trivial. So a more concrete example of this may be
*  if you're doing RAG, if you're trying to answer questions about a document,
*  you are including context in your prompt that isn't in the form of a demonstration of your task.
*  It's just added context from the document. It's snippets that were embedded similarly to your
*  prompt. And there's all kinds of extensions like hide and things like that that go on and may have
*  more elaborate procedures for retrieving the right chunks and different chunking strategies.
*  But you're still making the LLM do a lot of work at inference time. That it's not just picking the
*  closest examples and interpolating between them. It's applying presumably novel question to all
*  these pieces of data. And that makes sense in a RAG context, but if you were fine tuning,
*  you would need to tune on actual demonstrations. So you would need to have tuning data that looked
*  like here's your input, which is some RAG chunks. Here's your question and your input being the
*  question in the RAG chunks. And then your output is whatever you get from those RAG chunks. And that
*  demonstration can be generated synthetically. So recasting documents into synthetic questions
*  is a powerful strategy. And because also I think the underappreciated benefit of doing a layer of
*  synthetic transformation is that it gives you an opportunity to do quality checks. To start
*  meddling with the sort of cached parts of the process, if you will, rather than trying to set
*  everything up perfectly so that it goes right in production. Yeah, those transformations backfills.
*  That's a really good tip. It's funny. I was doing early versions of that stuff in fine tuning the
*  never actually broadly released Pecstavinci 002 fine tuning in the summer of 2022. And you might
*  be doing the same thing at that time. But man, it was in some ways it was like way harder. The
*  models were way less capable. It took a lot more work to get anything to work. But in some sense,
*  I think that era really prepared me well for now because I feel like that's actually more when I
*  learned a lot of this stuff that we're talking about than today. It's like today the models are
*  so good at so many things. Like you can get tricked into maybe I could just tinker with the prompt on
*  my way to get there or whatever. And when I think back to my 2022 experience, I'm like,
*  this thing is going to do one thing, but I'm going to have to grind to get it there.
*  And if I'm missing data and I need 1000 examples or whatever, how am I going to create those? I
*  don't really have time to create it manually. That's where a lot of these synthetic transformations
*  and backfills and whatever became part of my practice. And it's interesting that they're
*  basically still the same core techniques are really operative now. It's just that we maybe
*  have a harder time seeing through to the need for them in some cases because the models just
*  off the shelf are so much better at so many different things. But they're still not good
*  enough to actually be production ready for many of the things that people actually want to
*  automate in their businesses. Yeah. I think that's probably a good segue also to what you were
*  talking about prompt engineering and how the profession has changed or rather how the profession
*  that showed up is not quite what was promised. There's a scale at least. Yeah. So are you still
*  a staff prompt engineer or are you now an AI engineer or how do you think of yourself and
*  what you're expecting? My title is still staff prompt engineer. It's anyone's guess whether that
*  will be a title that people have a couple of years of rebranded as AI engineer or things like this.
*  I think there's a lot of ways things can go. But I think the thing that's clearest is that
*  this image that was hyped up a lot in early 2023, particularly the job of the future narrative
*  hasn't come to pass. Most firms don't hire their own prompt engineers and there isn't
*  indeed for most companies, especially outside of tech, to be hiring full-time
*  prompt engineers on staff. And I'd say honestly, most of the demand for prompt engineering,
*  it's coming from within the AI industry itself. That right now the people who most need prompt
*  engineering skills are people who are preparing training data or not just preparing synthetic
*  data from a model itself, but just filtering and doing quality control. And the applications
*  of LLMs at a company like Scale or at any of the AI labs themselves are much more abundant than you
*  see in many other contexts. I think that's the piece that has surprised a lot of people. And
*  I never tried to lean into the promise that this was going to be a job in the future. That was never
*  something that I really believed in, in the sense that I thought everyone was going to do it.
*  One thing I used to say a lot, and I think I made this point on our last podcast, was I saw prompt
*  engineering as a skill something like being a typist. It used to be that people who knew how
*  to type could get a job knowing how to type. And that clearly isn't the case now. But everyone
*  still knows how to type. It's a skill that everyone has. And people just don't call themselves
*  typists, but they're still typing. I'm not even so sure if that's the right analogy now. I think
*  most of the tricks and things that characterize prompt engineering of say 2022 are less relevant
*  now. And they're certainly less mandatory. I think in 2022, there were many things that you had to know
*  right down to just really stupid things like not ending your prompt in a space
*  before you could really get started to get good results out of like GBT-3. And that's no longer
*  chat models are just much more user friendly. Many people get by just fine being completely
*  unaware of tokenization. And they run into gotchas and they get bad answers sometimes because of it,
*  but it's possible to not know. And that's probably the biggest explanation I'd say for
*  what's changed about prompt engineering. And as we were talking about earlier,
*  it's why my Twitter output of like prompt engineering, pips and tricks posts have
*  declined lately. Because I think at the same time though, I guess you would call it like folk prompt
*  engineering tricks of the things that fit in a tweet, maybe the best known ones being like,
*  let's think step by step and things like that. While those are less relevant and the ones that
*  aren't obsolete are at least not mandatory now, prompt engineering hasn't stopped flourishing.
*  It's moved into more complex areas and it's becoming more and more code heavy. It's becoming
*  more like programming than poetry. And it's also, I think, expanding into a lot of areas
*  where we're not really calling it prompt engineering as much. I think people would
*  debate maybe whether techniques like RAG are, if you squint a bit, RAG is arguably a form of prompt
*  engineering. You're choosing what goes into the prompt. And you have, of course, optimization
*  tools like DSPy. There's a lot of code and process being built up around like wrappers around LLMs
*  in a way that I honestly thought we would see sooner, but we're definitely seeing it now.
*  This proliferation of tools, I don't see any sign of that slowing down. I think that prompt engineering
*  has in some ways moved into less publicly visible task domains. We're now trying to solve problems
*  in a way that the solutions can be bottled back into the LLM. Even back in 2020, I sometimes got
*  the reply on Twitter of prompt engineering surely won't be a real thing because whatever
*  there is to know, you can teach the model to do that. And that's not literally true for a lot
*  of reasons. Maybe one day it will be like you'll actually have the model just using another model,
*  but that's not literally how anything works today. But metaphorically, it is how it works today.
*  That the extent that we have tricks for getting better output from LLMs, one of the best things
*  to use those tricks for is to produce better post-training data and thereby eliminating the
*  need for anybody to know that particular trick. And I think this is a good thing. We're going to
*  see prompt engineering continue on this frontier. I metaphorically visualize it as something like
*  the way the forest fire would move. The prompt engineering is the fire on the perimeter,
*  but any particular tree doesn't stay burning for very long. So I think the frontier will continue
*  or just keep moving. Yeah, that's funny. My version of that is the black hole that the models just
*  suck everything into and eventually nothing can escape. That sort of sketches out a implicitly
*  like a vision of the future that maybe you won't even comment on this, but I assume that a lot of
*  what is going on right now is creating the kind of multi-step, multi-app,
*  advanced reasoning traces for more agentic workflows and that those ultimately are likely
*  to get folded back into the models. And if I had to make a prediction of what is GPT 4.5
*  going to look like, if we are going to see a GPT 4.5, it would be yet another advance in the
*  post-training where a lot of these stumbling points that we see with agent workflows today
*  get addressed. They can try a new way. They have figured out that, okay, you got stuck here. Don't
*  do the same thing over and over again as we sometimes see today. And I think that could
*  probably work pretty well even without that next order of magnitude scale up in pre-training.
*  I often feel like the models today are smart enough. I'm not asking you to tell me all the
*  data that you're creating at scale, but I guess, is there anything that you would say,
*  I'm way off on that expectation for what we might see in the next half step of models?
*  No, I think that sounds about right. I think there's entire avenues of things that we could
*  train models on that we haven't really thought about much yet. And that's really exciting to me
*  because it means that once somebody has the idea of lifting up some half-forgotten format of text
*  and training an LLM on it, you can move into a new space very quickly. If you figure out DNA.
*  I think we're going to see a lot of progress from that kind of exploration of just trying out new
*  things to train it on. Maybe another great example of this is that there was a DeepMind paper not
*  that long ago where they distilled Stockfish into, where Stockfish is being a traditional chess engine.
*  And they created a chess AI by this procedure, which is really clever, where they took
*  essentially Stockfish's judgments of how winnable a board position is. So all the training examples
*  were just like all of the form of like, here's the position of a board. How likely is it do you
*  think that white will win? More or less. I'm lost in detail. But the tuning on that is enough that
*  given an actual position of the board, you can just say, what are all the legal moves you can make,
*  run all of those through the model, say which one's best, and then do that. And that produces
*  a pretty good chess engine. And so it shows that really that you can distill Stockfish's opinions
*  of what chess positions are good into an LLM that was really built to model language.
*  I think we're going to see a lot of those kinds of discoveries of that. The knowledge there is
*  in the corpus of all of these examples of all of this training data. And collectively, those imply
*  an understanding of how to evaluate chess positions. So I think we're going to see just
*  more of that. That is like we just do pre-training, like discovering a lot of this stuff
*  through happenstance. I think that's what characterized a lot of the 2022 era of LLMs
*  is that LLMs hoovered up everything. And then we had this period of exploration, where it's like,
*  wow, look at all the stuff that's in here. It can pretend to be Wikipedia. It can pretend to be the
*  news. It can write JSON and so on. These things weren't apparent at the beginning.
*  And I think that's what we're going to find new things to put in.
*  Yeah. I think for me, it's like, you can ask this question of, are things going to level off? Are
*  they going to level off? From my perspective, it's to not get to some definition of AGI,
*  where maybe we still don't have too many eureka moments coming from AI, but where they can do
*  a huge percentage of just the tasks that people get paid to do at work most of the time, most of
*  which are not eureka moments, but are doing a task and trying to do it reliably and consistently.
*  It seems to me like for us not to get there, things would have to level off really quick.
*  That seems almost impossible, even if we just imagine training on a lot more expert data or
*  pristine data, as I've heard your CEO refer to it. But then on top of that, maybe it does level off
*  at expert level. And then I'm like, nah, there are all these other modalities. That's where
*  I just can't see how it doesn't all come together because the stockfish example is a great one.
*  DNA that I've talked about many different episodes with models like EVO is another great one. I just
*  did another episode on predicting very small scale molecular dynamic evolutions where this dude,
*  Tim Diagnone, has had this super viral tweet where he's just simulating small salt solutions
*  literally just like saltwater, but observed that he was spontaneously seeing crystallization
*  happening in the simulation. And he's even trained this thing on crystals, but we just
*  trained it to solve the wave equation at any given moment. It's very similar to the stockfish thing
*  where it's like he has a computationally super intensive approach to solve the wave equation.
*  And he's just training the model to make its best guess as to what the real solver is going to do.
*  And that turns out to be accurate enough that he can run essentially the same simulations
*  at orders of magnitude speed up and start to see these things that would never have been possible
*  to see before. And it's crazy. The scales that they're talking about are like small number of
*  atoms. It's like picoseconds level resolution, but seeing these things like, oh my God, crystals are
*  forming in my simulation now. So when I see that, I'm like, man, there's a lot more modalities out
*  there besides there's a million different kinds of sensors in the world. And all of these things
*  seem like they're destined to find their way into the same ginormous pool of data. And with all those
*  modalities, then you put in like a Sora, good God, you've got intuitive physics, then object
*  permanence popping up. It seems like we are definitely headed for something that is at least
*  in some very meaningful ways, superhuman. That doesn't necessarily mean it'd be superintelligence
*  or it doesn't mean it would have no weaknesses, but it does seem like there's a pretty clear path
*  to me at this point to something that is in many ways and in many meaningful ways, a superhuman
*  system. Yeah, I agree. I think people have the impression of the data-centric view of AI,
*  of the hidden in the models is data, as they say. View is sometimes I think seen as like the
*  skeptical or conservative position on the capabilities, right? That it's the one that
*  jives with the worldview of these models are rising only to the level of intelligence that
*  we train them on and no further. Right, there's like a skeptical position that you sometimes hear
*  people advocate and so you're not going to see any progress beyond what we have now because this is
*  just like as far, this is as good as what humans can do and that's all we get is what we train,
*  what we get from training on that. I don't give much credence to that position I have of seeing
*  models as compressed data. In some ways it's really optimistic about what they can achieve because
*  I see this sort of fungibility between thought and experience. And I think we're seeing that theme
*  in a lot of ways, like all the way back to just the idea of generative pre-training, that the task
*  of token prediction and like just feeling out the vibes of what token should come next in a
*  statistical sense leads to something that resembles reasoning, right? That it resembles step-by-step
*  thinking and calculation and like all these other things that we could at least mistake for thought.
*  I think that pattern is going to continue, right? That we'll see things, more things like
*  the stockfish distillation example, we'll find that there's more and more kinds of knowledge and
*  experience that can be put into weights. And I think that's really exciting, like you said,
*  that even if scaling were to somehow magically stop, if a government comes in and says you can
*  only go up to this many parameters or whatever, there'd still be a lot of progress. I think
*  you just see a problem like training on better data, even on the pre-trained side, like just
*  knowing what to pre-train on is still very much a dark art.
*  Yeah. That just paper out of Google in just the last week or so I thought was another,
*  oh my God, this is a big advance. And even if it was the kind of, that was the sort of thing where
*  even if you discount how much you want to believe in it, you could discount it quite a bit and it
*  could still be like a pretty big deal. I don't know if you've studied that one, but for listeners,
*  if not for you, the idea there was that they took a small model and trained it on the same data that
*  they're considering training the large model on, and then look for data that is not yet learned
*  by the large model, but is learnable in the sense that the small model at least somewhat makes
*  progress on it. So it's essentially separating what the models can learn from what they're not
*  learning much from, and then selectively training the large model on the more learnable data.
*  And they report just your casual 10X efficiency improvement from just that one neat trick,
*  which is crazy too, because that compounds with many of the other things that you might think are
*  going to be great, but you could also apply that too. And it doesn't seem like it's a indirect
*  competition with other improvements. It's important, I think, to be clear, the compute thresholds today
*  are for a reporting requirement only, right? They're not actually telling you from the executive
*  order. They're not telling you you can't do it. They're just saying, don't let the government know
*  if you are doing it. So I've felt like that's a pretty good idea. And I've generally agreed with
*  the idea that, first of all, if somebody's doing multi-hundred million dollar training runs, yeah,
*  probably doesn't hurt for the government to at least have an awareness of who's out there doing
*  that. And then also, I can't come up with a better threshold. But the more you see all these just
*  efficiency gains coming from everywhere, it's, man, even that is, it's a pretty hard position to
*  really think, oh yeah, we can just set this threshold. And then as long as everything,
*  we know everything above that threshold will be fine. It does not, it's happening faster than I
*  would have anticipated that you take 10X out of the difference between 10 to the 25 and 10 to the 26.
*  It turns out to be quite a bit. It's 90%, which is, it's funny how that works. But anyway,
*  there's a lot happening. I think we both expect things to get pretty crazy. You mentioned DSPy
*  briefly. Is that something you use a lot? And in general, is there like a best overarching
*  automation system for the sort of work that we've been talking about through most of this 90 minutes?
*  DSPy, I've used it. I wouldn't say that I've used it a lot. And that's not really a reflection on
*  DSPy as much as like limited time that I've had on my backlog to get deeper into it to find more
*  use cases for it. But I am excited about the project. I think like there's a lot of good ideas
*  in there. And I think there are a lot of niches where automating prompt engineering makes a lot
*  of sense. On the dark art of prompt engineering, the jailbreaking side, I'm sure you're a,
*  in some ways, maybe you're like a Twitter spiritual successor might be Pliny, who is
*  jailbreaking every model in two seconds from the second that he can get access to it.
*  It seems like he's usually using the same techniques across a lot of different models.
*  And they basically just work. My question for you is, do you think that those techniques will
*  eventually be stamped out of the models through more reinforcement training or whatever? Or are
*  we headed for a scenario where the model itself just can't get that robust and we instead have
*  to have some sort of moderation layer or governing system on top of the model to control these sort
*  of jailbreak type strategies? There's a few questions in there. So first, regarding whether
*  you can do it entirely in the model through training, like better data versus like filters,
*  there seems to be increasing evidence that there are cases where you can't do everything entirely
*  in the weights. So Anthropic had a paper not long ago on many shod jailbreak attack, where you
*  basically repeat hundreds of examples of malicious prompts and responses into a long context model.
*  And this overpowers fine tuning based defenses against this, of tuning on adversarial examples
*  of it behaving correctly. That same paper, though, found that there are pretty reliable defense
*  against this, which was to simply add a suffix to the prompt, reminding the model that it's a safe
*  model, that it's clawed and that it's well aligned and all that. And this was remarkably effective.
*  I forget exactly what the numbers were, but it was very effective at stopping the behavior
*  that they were showing. And that's a very simple trick. So I'm sure you're seeing things like that
*  one today. But beyond that, I think we shouldn't trust blindly that there's going to be like a
*  tuning fix for all these things. I think there's very likely going to be a place for things like
*  content filters. There already is, right? A good example of this I know of like the token repetition
*  attacks. So it's trivially simple to have a filter on your API that just says, is the user trying to
*  repeat the same token over and over again? And if you have an LM, continue a prompt that has
*  too many repetitions of the same token, you can get into this mode where it will probabilistically
*  spit out pre-trained data. There is a paper that showed this by collecting lots of this data.
*  And indexing it all together. Well, so for that particular example, I wouldn't say strongly that
*  there's no way to do it in tuning, but it's hard and it's not worth it. You're much better off
*  handling this with filters on the input to protect against that particular issue and filters on the
*  output for tricks that try to get bottled to do it itself or filters for the copyrighted content
*  you're trying to protect. But it's all a cat and mouse game. I think that we spent a long time in
*  the regime of trying to do everything through tuning. And I think we're finding that there's
*  holes in that strategy, that there are some odd cases where it doesn't make sense to patch
*  everything the same way. And so I think we're going to see more of that.
*  There's a follow-up though, which is what, if anything, does that imply for the future of
*  open source? It would seem to suggest that we are either headed for a world where people are going
*  to say, hey, these models are too powerful to be distributed in the raw. They have to be somehow
*  contained in an envelope that keeps them from doing unwanted things. Or we may just say the
*  value of open sourcing them, which is certainly very significant, is just so high that we'll have
*  to live with the downside risks of that. Do you see any other way to not have to bite the bullet on
*  one side or the other of that debate? It would be really nice if there was some way to be like,
*  yeah, we can have the best of both worlds, but right now it seems like we're headed for having
*  to make a choice. Yeah. Once you release the weights, people can do what they want with it.
*  There isn't really any method that I'm aware of that you could have an open source model without
*  attempts to censor pre-trained data to make it, if you want to really squash the problem,
*  you can make it unaware of concepts. But that has downsides as well. So that's becoming, I think,
*  less popular and starting with llama 2 of filtering out just the concepts entirely from
*  the pre-trained data. So I think there's no free lunch there, but as to what are the solutions to
*  that problem, I'm not really sure. Yeah. One that this is just making me think of that you may have
*  seen is called Sofon and it's out of a Chinese lab, actually. It's a strategy for fine tuning
*  suppression. And this is not on large scale language models. It's on smaller scale,
*  like image generation models is where they started. So there's definitely some work that would have to
*  be done to generalize this. But as you of course are well aware, like the image models typically
*  work on a denoising principle. And what they tried to do is create a image generation model
*  that would denoise as they normally do, except in what they call the restricted domain, where
*  in the restricted domain, it would just output basically the null transformation. And so it would
*  essentially not denoise. And they crafted the loss function in such a way where it's like smooth
*  bottomed. So they fine tuned it with this combination of if you're outside of the
*  restricted domain, just do your normal thing. If you're in the restricted domain, you're supposed
*  to produce a zero and the last bottom, it has a smooth curve such that it's hard to fine tune out
*  of that local minima because the gradient in once you like converge on this kind of smooth bottom
*  loss function, the gradient is zero. And so if you're trying to fine tune out of this local
*  minima, like it's hard to know where to go. And they found that training these models in this way
*  created a model that is harder to fine tune to do the unwanted thing as opposed to just like
*  training from scratch to do the unwanted thing. So I thought that was pretty interesting. There's
*  like very few of these proposals flying around that I've seen. I'm also pretty interested in the
*  Dan Hendricks at all line of work around short circuiting where they take like representations
*  and essentially do internal classification. And they've actually just recently started a company
*  on this premise as well. Those are a couple of things that are on my radar. But as of now,
*  we don't have answers. The short circuiting, that's still more of a system kind of approach.
*  The SOFON thing is interesting in that it's fully baked into the model. And so you could imagine if
*  that were to be really generalized and scaled up, you could imagine something where you might make
*  a sufficiently fine tuning resistant model and not have to bite the bullet on these trade offs.
*  But with a long way to go on that. Anyway, I like to highlight that work because that flew
*  way under the radar. Zvi mentioned it to me in a podcast and I hadn't even heard about it at the
*  time. And it's out of a Chinese lab. So it's definitely one that I think deserves a little
*  more sunshine. Yeah, that's the first time I'm hearing of it too. SOFON. It's good. Or at least
*  it's super interesting anyway. We'll see how far it can be pushed. Okay. States-based models.
*  Are you a Mamba, Stan? And what do you think the promise of sub-quadratic architectures
*  is and will mean for the field as a whole? I'm really excited about it. I watch these sorts of
*  things as an interested outsider. I'm not really qualified to say much about architectural decisions
*  for experimental architectures for new LLMs, to be honest. But I have some familiarity with
*  states-based models for time series modeling. Before I got into LLMs, I was an ML engineer
*  working on a massively multivariate time series prediction. So they're near and dear to my heart
*  in that sense, but it's not something I've done much work with recently. So I'm excited, but I
*  don't really have too much to insightful to add there. Cool. Last one. What do you think the
*  prospects are for solving the Arc challenge? If we gave you a version that is no budget constraint
*  and just said, you just have to make it work and you can fine tune any of the models that are
*  soon to come online for fine tuning, like GPT-4.0 is in fine tuning beta now and Claude and Flash
*  are announced. All of the tools that we've talked about throughout this conversation, do you think
*  you can get there with Arc and create something that can actually hit that human level performance,
*  or do you think we're still just not there in some fundamental sense?
*  Yeah, Arc's really interesting to me. It's satisfying to me that it recapitulates the
*  pattern we see in human intelligence testing, where you see things like Raven's progressive
*  matrices, which is an IQ test that most people wouldn't recognize as what they think of as an
*  IQ test. It's a test that has no words. Every problem can be described as here's a pattern
*  that resembles wallpaper and there's a piece missing. What piece do you think is missing?
*  And then you have multiple choices. You can have all sorts of logic problems that are expressed in
*  this form. It's interesting that we're having something like that for LLMs. You could have
*  something that's like the other approach that you could take to intelligence testing, like the SAT
*  approach almost, of how much vocabulary do you know? How many things do you know about the world?
*  How much do you know about writing? How much do you know about music? And then you could test
*  everything out of the sun. But maybe this is not the right way to view the world. It's like a bit
*  of envy of the simplicity of physics, maybe. But it feels right somehow that there could be just
*  a simple task that captures this deeper notion of generalizable intelligence that we think is there.
*  But I'm unsure whether it's real. We spent a long time trying to think what are the grand theories
*  of intelligence, just armchair philosophy on how do humans think and trying to tease it apart and
*  capture that in symbolic AI and all the other attempts to AI over the years. And the thing
*  that worked is just making it know everything. There may be something irreducible about that.
*  There's a body of knowledge that has to be there for the thing that we think of as intelligence
*  to even be coherent as an idea. But its possibilities are wide open. I think the
*  fact that we can be sitting around just speculating this widely about the future
*  really says how little we know about this stuff. Yeah, that's maybe a great note to end on and I
*  think a very good reminder. Is there anything else that we didn't talk about that you want to talk
*  about? And this is if you want to share more about scale in general or eval stuff you're working on
*  there or the seal thing or product wise, basically floors wide open for anything that you want to
*  put some extra attention on. Okay, great. I'll say that scale is hiring prompt engineers. If you're
*  interested in prompt engineering, if really any of the issues we were talking about here today,
*  especially if you're interested in LN security and red teaming and jailbreaking adversarial
*  prompting, we're looking for people who can do impressive things in prompting. Reach out to me
*  on Twitter or through our scale job boards, but I'll do my best to make sure you get sent to the
*  right places. Anything people should do to demonstrate this? Anybody could say, oh yeah,
*  I love using chat GPT. How can somebody distinguish themselves? What kinds of things do you look for?
*  What stands out to you that's impressive so that people are not just yet another resume that's
*  like enthusiastic about chat GPT? Yeah, a lot of people are talking about Pliny. So things that
*  go viral. It's an art unto itself of like just seeing what's getting attention, what people are
*  liking. But that's a good way to get to the top of the stack. I think if you can let X, the everything
*  app sift through the quality ideas and let the good things bubble up. It's the avenue that worked
*  for me. So I'm a little biased. So take it with a grain of salt, I guess. This has been fantastic.
*  A lot of really good content here that I think is just going to be of super practical value to
*  people as they seek to use AI to actually automate work and get real economic value. I know you have
*  been hard at work figuring out which among these techniques is really worth it. And also happy to
*  say that I think our views of this definitely are converging on some sort of platonic approach today.
*  So that's been a great finding for me as well. I really appreciate the time. I think folks will get
*  a lot of value from it. For now, I'll just say Riley Goodside, the world's first staff prompt
*  engineer at Scale AI. Thank you again for being part of the Cognitive Revolution. Thank you so
*  much. It's been great. It is both energizing and enlightening to hear why people listen and learn
*  what they value about the show. So please don't hesitate to reach out via email at tcr at turpentine
*  dot co or you can DM me on the social media platform of your choice.

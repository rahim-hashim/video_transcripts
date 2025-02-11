---
Date Generated: October 31, 2024
Transcription Model: whisper medium 20231117
Length: 3308s
Video Keywords: []
Video Views: 1602
Video Rating: None
Video Description: In this episode, Nathan sits down with Paige Bailey, Lead Product Manager of Generative Models at Google Deepmind. In this conversation, they discuss what it's like to be a PM for an LLM as opposed to an app, defining ideal LLM behaviour, and reasoning - how do you distinguish real abilities vs pattern matching? If you're looking for an ERP platform, check out our sponsor, NetSuite: http://netsuite.com/cognitive

RECOMMENDED PODCAST:
Run the Numbers is a weekly podcast about financial metrics and business models, designed for ambitious people operating tech startups. It's a collection of things host CJ Gustafson (CFO at Partstech and writer of Mostly Metrics) has learned and thought about in the trenches as a tech CFO. Subscribe to listen on the platform of your choice: https://link.chtbl.com/runthenumbers

TIMESTAMPS:
(00:00) Episode Preview
(00:01:15) Introducing Paige Bailey
(00:04:21) Paige’s background at Google Brain and the Deepmind merger
(00:07:00) PM for a LLM vs being a PM for an app
(00:11:21) The development timeline and compute budget of PaLM-2 
(00:14:30) Paige’s role in the PaLM 2 project
(00:15:30) Sponsors: Netsuite | Omneky
(00:17:26) Defining desired capabilities for PaLM-2
(00:19:17) The amount of work that went into elevating PaLM 2 from PaLM 1
(00:20:28) Has Google lost its ability to ship?
(00:24:240) Paige's "eureka" moment seeing GitHub Copilot capabilities
(00:27:47) Competing PaLM 2 with other models 
(00:32:20) Grokking and the predictability of emergent capabilities
(00:37:30) Citizen scientists and the multilingual capabilities of PaLM 2
(00:39:29) Distinguishing real reasoning vs pattern matching
(00:45:51) Products using PaLM-2 that people should try
(00:50:35) Most exciting AI projects that you can try out
(00:52:29) Curriculum learning and successor to the transformer

LINKS:
PaLM 2: g.co/palm2
Duet AI for developers: https://cloud.google.com/blog/products/application-development/introducing-duet-ai-for-developers
Avenging Polayni’s Revenge: https://www.youtube.com/watch?v=BmyB-4S9QuY

X/TWITTER:
@DynamicWebPaige (Paige)
@labenz (Nathan)
@eriktorenberg
@CogRev_Podcast


SPONSORS: NetSuite | Omneky
NetSuite has 25 years of providing financial software for all your business needs. More than 36,000 businesses have already upgraded to NetSuite by Oracle, gaining visibility and control over their financials, inventory, HR, eCommerce, and more. If you're looking for an ERP platform ✅ head to NetSuite: http://netsuite.com/cognitive and download your own customized KPI checklist.

Omneky is an omnichannel creative generation platform that lets you launch hundreds of thousands of ad iterations that actually work customized across all platforms, with a click of a button. Omneky combines generative AI and real-time advertising data. Mention "Cog Rev" for 10% off.

Music Credit: GoogleLM
Music license:
HD0JLKNORIFN9NJX
---

# Google’s PaLM-2 with Paige Bailey
**Cognitive Revolution:** [August 29, 2023](https://www.youtube.com/watch?v=K-XYxLifpQE)
*  Part of the reason why we've seen such incredible adoption of models like Palm 2 and then also the
*  GPT-3 plus variants is because we've seen a really powerful increase in our ability to serve these
*  models efficiently. And then also distillation techniques to make the same kind of performance
*  that you might get from a model with hundreds of billions of parameters fit into a model with
*  perhaps a couple dozen. And that is really, really interesting to me because we don't want
*  to wind up in a world where the only people who have access to these incredibly powerful tools
*  are people who can afford to pay like a premium for accelerators. We should be trying to find
*  ways where we can have really, really super powerful models but with a much smaller footprint.
*  Hello and welcome back to the Cognitive Revolution. Today I am very excited to speak with Paige Bailey,
*  who was the lead product manager on Google's Palm 2. Now it's no secret that with the rise of
*  ChachiPT, Google, which had always been a leader in AI research both at its headquarters in Mountain
*  View and via its acquisition and continued investment in London-based DeepMind, made a
*  special push to respond by polishing and productizing its own large language model experiences.
*  With this in mind, I just knew that Paige had been through one of the most interesting experiences
*  of anyone on earth over the last year or so. What's it like to play a critical leadership role in a
*  mission-critical AI project at a company that has more AI resources, including data, compute,
*  and algorithm expertise, simultaneously has more opportunity and more to lose than any other company
*  in the world, and is fully focused on shipping AI as soon as possible? How do you pull the team
*  together and unite the work? How do you even organize the data and reserve the compute?
*  And what's it like to manage the development of a frontier language model in general?
*  These products have more surface area than any previously created, and with each new generation,
*  or should I say with each additional order of magnitude of pre-training compute,
*  we are finding all sorts of new, sometimes quite surprising capabilities. And then,
*  what's it like to work with the rest of Google as that same core technology is deployed across
*  dozens of products and begins to be customized for all sorts of specific purposes as well?
*  These were just some of the questions that I had for Paige, and her answers did not disappoint.
*  Comparing the project to the Apollo program, which is not really an unreasonable comparison,
*  particularly if you consider the incredible data and compute platforms on which Palm 2 was built,
*  Paige offers a truly unique perspective on the process of training a frontier
*  language model in 2023. We talk about her early AI eureka moments, her responsibilities as product
*  manager, how the team comes together to define how they want the model to behave, how many advances
*  seem to be happening ahead of schedule at Google right now, how we should understand models'
*  reasoning ability and the special opportunity that citizen scientists have to contribute to this
*  research, the AI products that she is most excited about, where the next breakthroughs might come
*  from, and lots more. We packed a lot into less than an hour, and it was super fun. As always,
*  if you're finding value in the show, we would appreciate a review on Apple Podcasts, Spotify,
*  or YouTube. And if you'd like to contribute to the show, you can follow me on Twitter, where I am
*  at LeBenz, and I've recently started sharing my draft list of questions a few days before recording
*  interviews. I leave the comments open so anyone can suggest additional questions, and I want to
*  give a special shout out and thank you to listener Dave Neuer, who has recently contributed some very
*  thoughtful questions of his own. Now, here's Paige Bailey, lead product manager for Google's Palm 2.
*  Paige Bailey, welcome to the Cognitive Revolution. Excellent. Thank you so much for having me,
*  Nathan. Yeah, I'm really excited about this conversation, because you have had probably
*  one of the most interesting last years of anybody on the planet, including your role as lead
*  product manager on Palm 2, which is, for the moment at least, the frontier model out of Google,
*  right? Google DeepMind. What's the deal there now? It's been merged. Is that merger fully done?
*  So yes, definitely. It's been an exciting year. Palm 2, you know, we announced it at I.O. If folks
*  are curious, they can go check out g.co. slash Palm 2, read the technical report, watch the video,
*  etc. It's incorporated into, honestly, dozens now, products and features across Alphabet's
*  product surface, which is really exhilarating. I don't think I've been prouder of anything in
*  my career than the work that the team did to kind of get the model ready, to get it tested and
*  instruction tuned, and then incorporate it into all of these great places. And then for Google
*  DeepMind, that is also something that is super, super exciting. So historically, we had had
*  many different research orgs throughout Alphabet, most notably Google Research and then Brain
*  Embedded within Research. I was part of Google Brain up until just recently. And then DeepMind
*  under Denis Eshabis, also doing phenomenal research work, really groundbreaking things like AlphaFold,
*  AlphaGo, like all of these super, super notable nature paper worthy research efforts.
*  So just recently, Sergey and all of the folks at Alphabet decided to take Brain, which was a part
*  of research, and to take DeepMind and merge them together. And so far, it has been amazing. It's
*  been so, so nice to have very open collaboration between researchers that had previously been
*  separated just by a result of being in a couple of different PAs. And I've personally seen dozens of
*  organic collaborations just spring up in the past few months. So if anything, it's just been
*  certainly the best thing from my perspective that Alphabet could have done for its research teams.
*  And it's also been just an incredible thing to be a part of, to be able to see all of these people
*  begin to work together when they've wanted to for a long time, or they've already been working
*  together for a long time just across PAs. Yeah, it seems like the intensity, the focus, the output
*  is kind of ramping up everywhere. I want to start off by just asking you a little bit about what it
*  means to be a product manager on a product like a language model, like a Palm II, that has such
*  insane surface area. I think a lot of people have a sense for what it means to kind of
*  manage a web product and talk to users and tinker and make iterative improvements.
*  But this thing is just so vast. I imagine it's quite a different experience.
*  Absolutely. And that's a great question. So I feel like my backstory, I started doing machine
*  learning engineering a long time ago. The first time I implemented a machine learning model was
*  in 2009 or 2010. So things have changed pretty rapidly. I'm also relatively new to the product
*  space. So I just became a product human a few years ago. Up until then, I was doing engineering,
*  either like developer programs, engineering sort of things with an alphabet or being a machine
*  learning engineer or a data scientist. And I think that helps you build an awful lot of empathy
*  for the researchers and the engineers who are building and deploying these models.
*  I also feel like I could never be a product human on something, anything other than a technical
*  product, whether it's developer tools or a model that's being built in research,
*  because I still get to program every day. And if I couldn't program every day, I would be a very
*  sad person. I will say that for large language models in particular, to your point, as you're
*  building them, there are so many things you have to take into account. So there's both the pre-training
*  data mixture for building a large language model or building a multimodal model. So you have to care
*  about things like compliance, but then also how the model might be used downstream. So all of the
*  ways in which users might be sort of asking questions or wanting to get feedback, those data
*  or data that sort of would address those questions has to be incorporated back into pre-training.
*  So you have to have a lot of intuition about how models will be used, or you have to be doing kind
*  of very rigorous data analysis on all of the deployment surfaces on which the model has been
*  deployed. Relatedly, you have to have evals to make sure that the model is kind of behaving in
*  the way in which you expect. And these could be anything from like responsible AI evals to
*  capabilities evals. So does it generate code well? Does it explain code well? Does it do security
*  vulnerability detection? Can it solve math problems, like all of these various things?
*  And then you also need to think about instruction tuning data sets. So once the model has been
*  pre-trained, how do you kind of fine tune it in such a way that it can give zero-shot answers as
*  opposed to few-shot answers? How do you think about deployments? So the different model sizes,
*  what are the constraints there in terms of latency? And that's also very, very related to how people
*  might be using it downstream. And then also considering things like RLEF or RLHF on how you
*  might incrementally improve the model over time. So it's an entire spectrum of things.
*  And in order to do it effectively, especially now, you have to be really, really invested in
*  all of the use cases in which your models are being deployed. I think it requires
*  a special kind of person to care about it because I am so impressed with other PMs that are so
*  effective at finance or design for websites or can place the button in the appropriate place.
*  But I am not one of them. And so the skill set that I've developed as an engineer, I think,
*  is useful in the sense of being a research PM, but it's not necessarily something that's for
*  everybody. Yeah, that's just a few considerations to take into account. I'd love to hear kind of the
*  maybe origin story of this project and a couple of different angles on that that you might unpack.
*  I was just talking to Vivek Natarajan from Medpalm2 and now Multimodal Medpalm yesterday,
*  and really struck by how compressed the timeline is on those projects. He always emphasizes we're
*  standing on the shoulders of giants with infrastructure and obviously prior research results as well.
*  I'd love to hear, not like into super specifics, obviously, but kind of how long was this
*  thing in the works? Was it basically concurrent with GPT-4? How does a project like this get
*  started? How do you decide, because this is obviously presumably one of the biggest compute
*  allocations Google is going to make, how do you decide how big the compute budget is going to be?
*  Do you have your sort of Palm2 moment stories where you got this thing back and you were like,
*  oh my God, this is actually next level? What's kind of the journey that you went on
*  to ultimately bring this thing out to release? It is a very, very significant compute allocation,
*  which means that you do have to kind of convince many different teams throughout Alphabet to kind
*  of okay the utilization of TPUs. That also falls into a lot of the product management questions.
*  So if you're building a model, how do you make sure it's a model that can be used by as many
*  different teams all at once and that it doesn't have any compliance concerns, that it doesn't have
*  any stickiness around data? All of these things are super, super important. But for the Palm2 story,
*  I think Google's been building generative models for a really long time and we've been announcing
*  them at IO for a long time. I think this is the first time that we announced one with like over
*  25 deployments already though at IO. So as an example, BERT, the original Palm, Palm2,
*  and now with Gemini, we're thinking increasingly about how do we get these models out into the
*  world? And so to your earlier point about standing on the shoulders of giants, being able to use
*  data sets that other teams have aggregated, open source data sets, data sets that might be different
*  preprocessing techniques for open source data, being able to leverage the model architectures
*  that folks have deemed to be the most impactful, and then really mobilizing this incredible team
*  across many different parts of research together to do the data aggregation, to train the model,
*  to figure out what architecture and what tokenizers should be used, to babysit the
*  model over time, because you do have to monitor it to make sure that it's continuously training.
*  It does like have problems every once in a while and you have to restart it or rewind or like go
*  back and like make sure that everything's going correctly and then doing the final stages of
*  polishing to make sure that it works well. So it really is just this massive, massive effort.
*  It feels an awful lot like working on an Apollo program to be training one of these models. That's
*  something that perhaps there's not a strong understanding of externally is that not only
*  do you need massive amounts of compute, not only do you need massive amounts of data, but you also need
*  a really strong team with a lot of expertise in different areas in order to do these things
*  effectively. So does that make you effectively a kind of manager or a information hub or like the
*  first user who is kind of responsible for like is this thing working well or not or maybe all of those?
*  I would not call myself a manager in the sense that there are TLS responsible for each of these
*  work streams and they do an incredible job of both defining the work that needs to happen and then
*  holding folks accountable or reviewing CLs. Though sometimes I review CLs, but I will say
*  being able to coordinate between all of the teams, making sure that they're all heading in the same
*  general direction. If one team comes up with an eval, making sure that we haven't included any of
*  those eval data in the pre-training data mixture and then also like being tied at the hip to whatever
*  latest version of the checkpoint we have to constantly be testing to make sure that we're
*  improving on all of the areas that we want to improve. Those are parts of the day job.
*  Hey, we'll continue our interview in a moment after a word from our sponsors. If you're a startup
*  founder or executive running a growing business, you know that as you scale, your systems break
*  down and the cracks start to show. If this resonates with you, there are three numbers you need to know.
*  36,000, 25,000, and 1. 36,000. That's the number of businesses which have upgraded to NetSuite by
*  Oracle. NetSuite is the number one cloud financial system, streamlined accounting, financial management,
*  inventory, HR, and more. 25. NetSuite turns 25 this year. That's 25 years of helping businesses
*  do more with less, close their books in days, not weeks, and drive down costs. One, because your
*  business is one of a kind, so you get a customized solution for all your KPIs in one efficient system
*  with one source of truth. Manage risk, get reliable forecasts, and improve margins. Everything you need
*  all in one place. Right now, download NetSuite's popular KPI checklist designed to give you
*  consistently excellent performance absolutely free at netsuite.com slash cognitive. That's
*  netsuite.com slash cognitive to get your own KPI checklist. netsuite.com slash cognitive. Omniki
*  uses generative AI to enable you to launch hundreds of thousands of ad iterations that actually work
*  customized across all platforms with a click of a button. I believe in Omniki so much that I invested
*  in it and I recommend you use it to use Cogrev to get a 10% discount. When you talk about all these
*  teams, one thing that I was really wondering about, because I've seen this writ small in
*  organizations that I help with AI, where sometimes it's like, you know, you try to do some AI task
*  automation, and one thing that can come to light is that the organization doesn't necessarily have
*  a clear sense of what it wants out of this task. Somebody's just kind of doing it, or maybe multiple
*  people are doing it. They might be doing it a little bit differently, and now when we're actually
*  going to evaluate an AI, it's like, well actually we never evaluated the people, you know, so we don't
*  really have a standard of what is good and people can disagree. How did you even think about the
*  process of, presumably as a team, coming together to say, this is how we want Palm2 to behave?
*  You could write obviously almost infinite instructions or, you know, wishes for how that,
*  for how such a big system would behave, but how did you guys think about even getting your arms
*  around that in the first place? So that's a great question. I think that there are many different
*  teams that might define personas for how they might want the model to behave downstream.
*  So as an example, the barred landing surface has a persona associated with the way that the
*  model is presented to a user, and you might have a different persona if, you know, you're providing
*  code assistance within an IDE, or you might have a different persona if you're, you know, the MedPal
*  model or any of these other domain specific models. So that's something that, you know,
*  we tried to create a general purpose instruction-tuned model that's generally useful
*  for kind of as broad a variety of use cases as we could, and then really each other team is
*  responsible for defining how they want that model to be a helpful tool for their users. So I will
*  say that a lot of work goes into that process, immense amounts of work, both for that as well as
*  for instruction tuning to kind of nudge the model towards certain behaviors. And I think alignment
*  work as well is one of the most interesting things that we do now as foundational model teams.
*  There's been great work from Alphabet and then from many other folks out in the industry. I
*  particularly love Anthropix papers on AI alignment. I mean, it's crazy. That's all basically in a year,
*  right? Because I think April 2022 is Palm 1, now Palm 1 publication, and May, I think, right, for
*  Palm 2 official kind of announcement. So in that window, you've got to figure out, okay, what's this
*  next generation going to look like? How much bigger is the data set? You know, what are we
*  going to augment on? You've got to do all the kind of experimental work to satisfy yourselves that the
*  giant training run is actually going to work. You've got to talk everybody into the compute and get all
*  that lined up. Wrangle the people, decide what model sizes should be, decide what kind of
*  domain-specific models should result, do the instruction tuning, help the PAs with the
*  deployments. It was an awful lot of work, but it was so, so energizing and I think empowering for
*  the team as well to be able to have Sundar and teams stand on a stage and say, guess what?
*  This model exists and also it is in over two dozen products and features already. Congratulations,
*  you're using it. So that's an incredible thing. And we've never been able to do that as Alphabet
*  before. Yeah, there's obviously been so much talk about, has Google lost its ability to ship or
*  is everything too bureaucratic there? This would be a pretty strong counterpoint, I would say, to that
*  narrative because this is not a color change to a button in Gmail, right? This sounds like a whole
*  layer across the entire company at this point with all of its bazillions of products.
*  Has there been a moment, I mean, I guess for starters, do you think that narrative was
*  ever true? Was there a time when there was kind of a shipping paralysis or was that all just kind
*  of nonsense? I've always been impressed with the number of features that we regularly ship and I
*  feel like perhaps they might be features within Photos or features within Gmail or updates to
*  algorithms within Search or whatever it might be. They might not be so immediately obvious to an
*  end user, but it's still incremental improvement despite not launching multiple new named products
*  all the time. So it's also interesting to consider the dichotomy of like, oh, well, Google's not
*  shipping, but also like, wow, Google ships a lot of stuff. They have like three chat apps or whatever.
*  It seems just like a little sort of cognitive dissonance. Like how do you wrap your brain around
*  it? My general sense is that narrative has kind of always been a bit overstated. And the big thing
*  that I kind of keep always in mind too, and I was telling people quite a bit, was like, you know,
*  let's see in the immediate wake of chat GPT, right? It was like, you know, where's Google on this?
*  They invented the technology. They should have been here, but I was kind of like, yeah, but keep
*  in mind also, it's only really recently become useful at all. You know, it's not like GPT 2 was
*  doing anything for anybody really. So it's an interesting artifact and it's cool to study,
*  but it doesn't like really move the needle for most work, right? So it's not really something that
*  would naturally have been deployed and it probably would have just kind of been weird, you know,
*  if you had put it in a bunch of products. So I was always kind of betting on you and the team,
*  not knowing anybody individually super well, but just feeling like the quality of the research
*  that I saw coming out suggested that there was not any systematic slowdown or weakness.
*  And we have, you know, we've been a machine learning first company for a very, very long time. So AI
*  integrated into pretty much everything that we do. But to your point, there were usually
*  models that were a bit simpler, easier to serve. And I think part of the reason why we've seen such
*  incredible adoption of models like Palm 2 and then also the GPT 3 plus variants is because we've
*  seen a really powerful increase in our ability to serve these models efficiently. And then also
*  distillation techniques to make the same kind of performance that you might get from a model with
*  hundreds of billions of parameters fit into a model with perhaps, you know, a couple dozen.
*  And that is really, really interesting to me, because we don't want to wind up in a world where
*  the only people who have access to these incredibly powerful tools are people who can afford to pay
*  like a premium for accelerators. We should be trying to find ways where we can have really,
*  really super powerful models, but with a much smaller footprint. So they can be served on a
*  CPU or they can be served really efficiently on a single accelerator. And that, I don't think that
*  would have been the case up until just recently. Yeah. It's amazing how much progress there has
*  been on that, you know, chinchilla scaling laws. And it just seems like it, at least for now,
*  you know, has kept going. Did you have any eureka moments, not in the sense of like discovery of how
*  to make it work, but just how well it was working? Like I have my sort of, I was a GPT 4 red team
*  participant. And at the time it was like a lightning bolt, you know, out of the clear. And I
*  was very into all the existing models, right? But the leap between what I had seen and that, at that
*  moment last fall was like, oh my God, everybody who I've talked to has had kind of a similar story,
*  but I wonder if you have a Palm two version that you would tell. So I actually think this happened
*  for me when I was working at GitHub. So when we were testing out copilot, like the very, the very
*  first instances of copilot, there had previously been, and I'm a nerd for developer tools. It's
*  like, they are, they are amazing, like hugest, biggest always fan of VS code. If you ever want
*  like pointers on creating an extension, I am happy to always give ad hoc advice. There had been tools
*  for code completions earlier. So something called IntelliCode, as well as other, other tools that
*  were available on the market, like tab nine, which was using kind of GPT two under the hood.
*  And you could get somewhat decent completions, single line, two to three line, dependent on the
*  language that you were using. You know, if you're using Python for GPT two based products, you are
*  probably getting pretty decent answers. If you are using Python within IntelliCode, you are probably
*  not getting decent answers because it did much better on C sharp and dotnet stuff. Looking through
*  that user experience and then seeing kind of what happened just out of the box with the copilot
*  extension, where you were getting like five, six, seven lines that were generally good lines of code
*  that were related to what you were asking. And even, you know, like text being able to help plan
*  out an itinerary for a weekend in San Francisco, it was bonkers. Like just, just thinking through
*  how this would impact developers long-term and sort of, you know, it was still early stages.
*  So like trying to do prompt engineering just in the context of the signals that you send to the
*  model, it was transformative. And all I could think was just like, all right, like this is,
*  this is going to be insane. This is going to impact everything that we do. And, and as soon
*  as that happened, I was just like, okay, like there's, there's building the model. That is the
*  only thing I want to do with my life, like making it much, much better at generating code, generating
*  math, because I really do feel those are the things that will move the needle the most for,
*  for progress going forward in the, in the generative model space.
*  I can relate to the copilot story. I'll, in the interest of time, I won't tell my version of it,
*  but I definitely recall a copilot where I was like, Oh, that would have taken me a long time
*  to figure out. It's funny. I'm just old enough to remember, you know, and was kind of a young adult
*  at the time when Google came out. And I remember people being like, this is incredibly next level.
*  And it does feel like we've kind of hit another thing where it's like, yeah, I wouldn't have wanted
*  to search for this. It would have been a bit of a struggle, but boom, you know, it just kind of
*  nailed it. There's kind of several frontier models, right? That are, that are out in the market today.
*  And I wonder where you think we are in this story. GPT-4 gets most of the attention because it kind
*  of came first and still kind of edges out the others on, you know, the leading benchmarks.
*  How would you characterize the comparison between a Palm two and a GPT-4? Maybe you could throw a
*  Claude two in there or a Lama two. Like, I'm not sure how you think about the relevant set of
*  comparisons. And also I'm really interested in how much do you think that matters? Do you guys think
*  about, you know, competing specifically with other models or is that less relevant to the
*  way you're approaching the work? I think that everyone is doing wonderful work in this space.
*  And it's very exciting to be here at the front lines for, for generative AI as it gets incorporated
*  into product. It's also really energizing to see so many open source offerings spring up and be
*  capable of being used for folks that are wanting to try out things within their projects, but then
*  they might not have their needs addressed by just a kind of commodity rest API. So I've
*  particularly been excited about the applications of Lama two, because you can do continued pre-training.
*  You can do more into the weeds style optimizations than you would be able to do with something that
*  you could only access via a rest API. I do know that we are focused on continuously improving
*  all of the models that we've built and making them better and better over time, both by improving
*  our data sets, by exploring these RL techniques, as well as building bigger and even more powerful
*  models like Gemini. And for folks who might not have familiarity, Palm two was kind of a text and
*  code based model. Gemini is multimodal from day zero. It's a superset of Palm two's capabilities.
*  There's immense potential impact for, for all of these models to have in the world. And I also
*  think that as people are selecting models for their use cases, they might want to explore
*  different latency approaches. They might want to explore, you know, different model size variants,
*  but there's certainly much more room in the space to grow. Yeah. It's easy to zoom out the kind of
*  leapfrog of who exactly, you know, passed who on what benchmark at any given time,
*  probably fades into the background. It doesn't matter if you try to adopt, you know, try to
*  envision the 2025 perspective. It's like all those considerations, you know, become kind of
*  footnotes in history pretty quick. It feels like it does feel like this wave is kind of, you know,
*  just tumbling over itself and the exact dynamics of that matter less. Alphabet sometimes feels like
*  living in the future, which is great in every sense that you can imagine, but can also feel
*  a little bit overwhelming in the sense that, you know, you have a model people in various places
*  are doing domain specific continued pre-training or they're optimizing it in some way, or they're
*  continuing to train it. So it gets bigger and bigger and more impressive, all of the things,
*  but you wake up one morning and you're like, oh my gosh, like this one version just surpassed
*  human level performance on this thing that we thought that would not have human level
*  performance for the next year and a half. And then, you know, you, you go to your next meeting and then
*  you look over and it's like, oh my gosh, like this just hit, you know, 10 full percentage points higher
*  on an eval just by adopting this one particular approach or like, oh wow, like RLHF moved the
*  needle 25% or whatever it might be. So it's just constantly kind of learning and experiencing these
*  new things. And I have never felt like the pace was so, the pace was so sort of somehow accelerating
*  still, even though it felt like it was a sprint, you know, it's basically been a sprint since like
*  December of last year, honestly. I am so excited. I don't feel tired. You know, we probably all should
*  feel tired, but like I feel so excited. Yeah. I'm in the same exact boat there, honestly, for the last
*  really two years since I've kind of became obsessed with all this stuff. I have in some sense been
*  working harder than ever. And in some other sense, I feel like I've had less trouble getting in gear
*  than maybe ever before, because I'm just inherently super motivated and curious to learn, you know,
*  what the next thing is that I can learn. I'm really interested in this phenomenon though,
*  of these kind of surprising moments of advance or threshold passing. One of the most interesting
*  results I've kind of gone back to over and over and over again is the grokking phenomenon. I'd
*  love to hear a little bit more about this kind of sounds like surprising, you know, and kind of
*  unpredictable and maybe even sudden, you know, advances in capability. That seems to me like a
*  really important question for the future of hyperscaling. We can kind of predict the loss curve
*  pretty smoothly, but we can't really predict when different capabilities will come online or even if
*  they will, or even really tell most of the time, like, is that something that has really
*  generalized in some meaningful sense or grok in some meaningful sense? Or, you know, are we still
*  in kind of stochastic parrot mode or somewhere in between a hybrid? I'd love to hear more about how
*  you think about that, having kind of, you know, had the inside view of watching the loss curve
*  drop and seeing where there's also these like periodic spikes in individual specific capabilities.
*  At the most recent ICML, there was a workshop kind of related to this around reasoning,
*  which I strongly recommend checking out. It also had a really powerful panel with
*  Simi Benjio and some others kind of walking through. There are papers that have proliferated
*  with assertions like, oh wow, GPT-4 can reason, or like this model can reason, and, you know,
*  we've unlocked it, guys, we've solved it. The reality is that when you actually start probing
*  a little bit deeper to check to see that, you know, there are these canonical examples, like
*  you have five blocks on a shelf, you want to move them around. If you even just slightly change,
*  you know, it's not blocks anymore. It's like cheese and an apple and like all of these other
*  things, and you change the terminology around like moving them around, then suddenly you realize like
*  the model isn't, like it's not reasoning at all. It hasn't learned anything to that effect. It's
*  just learned kind of pattern matching based on things that it's seen in all of the webpages
*  that it might have explored as it was being trained. So I do think there are still certainly
*  some capabilities that were not close to unlocking, and then there are others
*  where, you know, you experience these capabilities that you would have never imagined just by virtue
*  of the kind of data that you might have incorporated into pre-training. So examples of this might be,
*  you know, for source code, including source code, but also including diffs data, or including
*  perhaps commit messages whenever somebody was making a PR. And then suddenly by virtue of having
*  those data in various formats, you can ask the model, all right, well, tell me what I would need
*  to do in order to make a performance fix to this code, or tell me what I would need to do to sort
*  of migrate this code from one API to another, or one dot release for an API to another. And those
*  aren't things that, you know, somebody could sit at a computer and make an exhaustive list enumerating
*  potential capabilities of the model before it gets released. It's all stuff that we find out kind of
*  after the fact as people kind of test it, and then sort of see what it does. Like there was a, there
*  was another really compelling example just recently where, you know, we introduced new lens capability
*  within Bard. Someone decided to do the test where they sketched out something, like the design of a
*  website, and they fed it into Bard, and they said, like, hey, could you generate the code for this
*  website? And then Bard was able to do it. Like, whenever we were introducing lens capability, we
*  did not think, like, oh, wow, like, I bet you it can, like, take in images and generate websites.
*  It was just something that was kind of observed. Honestly, that's something that we were able to
*  do. Honestly, that's super cool. And it means that all of the people who are testing the limits of
*  what these models can accomplish and who are so creative and, like, pushing the boundaries, you're
*  all kind of helping accelerate research and helping us understand what we need to do in order to make
*  these models better, how we should be evaluating them, and then also sort of imagining even other
*  tasks that they might be able to accomplish over time. So it's really cool. For people at home, if
*  you don't realize it, like, every single researcher in the world is tight at the hip to social media
*  just kind of seeing all the cool stuff they all do, and that's all going into things that we need to
*  do to improve the models, how we might be evaluating them, how we might be improving instruction
*  tuning, and then also, you know, the kinds of data that we should be generating in order to kind of
*  improve those capabilities over time. I love that call to action for people, and I'm totally with you in that it feels like
*  the need for kind of citizen scientists, LLM explorers is huge, and I really encourage more
*  people, you know, if they have the curiosity to go for it. It's really not that hard, you know, in today's
*  world, you can just kind of, you can actually make meaningful discoveries right from an interface
*  and with, you know, a little bit of code, you can, you know, start to characterize that more systematically,
*  and before you know it, you've got something that is meaningfully contributing to the global understanding,
*  and, you know, there's a lot more global understanding that we still need, so I definitely
*  appreciate that encouragement for the audience. Especially multilingual examples, too. Like, one of
*  the other, you asked about a cool thing that we saw with Palm2 whenever it was first created,
*  one of the engineers on our team, Rohan Anil, who is also very much obsessed with code, so it's not
*  just me, he tested out a situation where he asked the model to generate some code and then to explain
*  each line of code in line, but using Malayalam, so using a different language, and it was able to do it
*  because we had kind of integrated multilingual capabilities within Palm2 as well. So that was
*  something that was super surprising, majestic to see. Yeah, it's a great word. OpenAI has said
*  something similar where in their original instruct paper, they basically, as I understand it, only
*  used English instructions, and then they were kind of surprised to see that it handles the instructions
*  in a lot of languages. So I want to just go back to the reasoning, grokking, statistical correlations
*  concept for a second, because it's still pretty confusing, right? There's like some things where
*  it definitely seems to be doing some reasoning. Maybe you would say, no, you don't buy that at all.
*  It's hard to believe that all this stuff is just purely paratree. How would you, you know, if you
*  had to give a very short summary for somebody who is going in and trying to do some of this exploration,
*  how would you orient them to what kinds of reasoning or the degree to which there's reasoning,
*  and how do you know when reasoning is kind of stopping and you're just entering into,
*  you know, statistical noise that may be confusing, confusingly like reasoning?
*  That's an excellent question as well. You know, how do you kind of spot when a model might be
*  fibbing or when a model might be sort of presenting itself as having the ability to reason,
*  but not necessarily having the capability innately? And I strongly, strongly recommend
*  watching that panel session. There's an additional talk from the same workshop
*  called Avenging Poliani's Revenge, which also quite gets into this. And it's a way to kind of
*  take a step back and be a little bit empirical about testing these capabilities, because the
*  likelihood is that, you know, as an example, again, the blocks on a shelf problem, usually these
*  questions are kind of formatted in the same way whenever people are testing out ability to reason.
*  It feels a little bit like SAT or ACT questions. So they've all been kind of crafted in the same
*  format with the same words, the same entities. You know, just as some people get really good at
*  taking standardized tests, the model gets really, really good at sort of giving the impression that
*  it knows how to reason and knows how to remove a block around on a shelf to solve a user's problem.
*  But the instant when you say like, no, it's not blocks, it's something else. It's not a shelf.
*  You're actually putting them on the floor. You're not trying to move them around. You're trying to
*  put them in different locations in space. Then suddenly everything falls apart. And it's because
*  this is still a reasoning problem. It's just outside of the context space that the model
*  understands. And that means that, you know, the model is just kind of reciting things that it's
*  learned by rote. It isn't necessarily kind of building the skills it would need in order to
*  sort of take what it's learned and apply it in a new context. Just as you might have kids that are,
*  or not kids, like just humans generally, I guess, that are really good at memorizing things,
*  but not necessarily taking what they've learned and applying it in a new context.
*  There was another really excellent takeaway from the Avenging Poliani's Revenge talk,
*  where a paper was sort of proposed saying that the models took so much prompting and sort of
*  correction in order to get the correct answer for reasoning. You know, like some grad students
*  saying like, oh no, that's not what I meant. Like you should do it this other way. That the author
*  proposed that the models are limited only by like what the grad students knew. So like if the grad
*  students knew how to accomplish a task, then they could prompt and kind of nudge the model towards
*  whatever outcome they desired, which isn't necessarily empirical and isn't reasoning.
*  It's just kind of keeping course correcting the model until it gets to the right location.
*  You know, that's still powerful that the models might be able to arrive at the right destination,
*  but it's not sort of getting them there by themselves.
*  Yeah, I'm kind of obsessed with this question right now. So how do you understand when you see
*  a phenomenon like that, where it can do apparent reasoning, and then with a perturbation, it kind
*  of can't do apparent reasoning anymore? Do you think that internally that is like, because you
*  can imagine different explanations for that, right? One would be it's all just paratree and here the
*  correlations worked out and here they didn't. Another one would be there is actually some
*  reasoning ability, but there's like a sub-circuit that is doing that, that is either getting
*  activated or not activated, depending on a context, or maybe is getting activated but
*  drowned out by other noise. Do you have any sense for how to conceptualize what's going on inside
*  of it? I know that's tough because we're still collectively working on cracking that, but I
*  wonder what your best guess is right now. I unfortunately have very little domain
*  expertise in that space. I do know that people are thinking about it very carefully, both by
*  building tools such that we can see what portions of documents are useful as models ask questions.
*  So Anthropic had a recent paper to this effect where you can see from either the pre-training
*  corpus or from something that you might include in the context window or in the prompt, what
*  particular words are most important and what placement of words are most important for the
*  model to make a decision. When you think about applying that at scale, everything gets very
*  tricky. But again, I'm not an expert in this space, so I would not be able to give you
*  a great answer. I would say that if you want to talk to some of the folks at Anthropic,
*  they have amazing intuition. In addition to the folks at Google DeepMind, it's a challenging
*  space. Reasoning is the thing that everybody seems to be pushing towards. How do we plan?
*  How do we reason? How do we break down this higher level problem into steps? And then that
*  kind of gets you the holy grail for these general autonomous agent things. How do you go from having
*  a natural language problem to decomposing it into steps and then generating code to accomplish
*  tasks or doing retrieval lookups to accomplish tasks? I don't think anybody in the world has a
*  definitive answer on that. Even Anthropic, I heard Dario the other day and it sounds like they've got
*  still more questions than answers too, which is amazing. Again, super exciting. There's never been
*  a more interesting time to work in computer science or work on AI. And if anybody tells you
*  that they've got everything figured out, then they probably haven't looked in enough locations
*  yet. And the number of interesting problems to work on only seems to be growing. I think you
*  recently tweeted that Palm2 is now in 38 products. I don't have the exact number for you, but it's
*  certainly in more than 38 products and features. And it's also been deployed in a variety of sizes.
*  We touched on this externally. Everything from small enough to fit in a mobile device
*  to so large that you have to serve it on a cluster of machines. So it's been really,
*  really energizing to see all of that great work happen from so many people.
*  So what are the products that you are most excited about that you think people should definitely go
*  try? One of the projects that I'm driving at Google DeepMind is our Code AI effort,
*  which is a collection of about 150 plus researchers and engineers that are working
*  on everything from code generation to code explanation to security vulnerability detection
*  to automatically applying performance fixes to source code migration to
*  generating source code to interact with tools and APIs dynamically. And being able to do that
*  general purpose autonomous agent thing that I mentioned before, which is you have a high level
*  task, you can decompose it into steps, and then you can sort of stitch together code in order to
*  navigate to accomplish tasks to assign yourself new tasks. So lots of really interesting work.
*  In this vein, so we have a product called Codi, which is sort of Palm2 with continued pre-training
*  on a lot of source code. This is offered as an API through GCP. I think a number of companies
*  are trying it out to see if it would work for them and for their IDEs. So if you're interested
*  in code completion, code explanation, all of these things, certainly give that a go. We're also,
*  we announced this at I.O. Duet AI for developers. So integrating machine learning models across the
*  entire spectrum of GCP products. So generating code within an IDE, but also the security
*  vulnerability detection, doing kind of rigorous analysis through logs, helping with DevOps
*  activities, doing autocomplete within the cloud developer console, some sort of Q&A that can help
*  you navigate cloud developer consoles, because they can get a little bit overwhelming with the
*  number of products that happen to exist automatically generating architectural patterns,
*  all of these things. That's particularly exciting. I would also love to have people kind of explore
*  things like MedPalm. The team has done amazing, amazing work. And there's tremendous potential in
*  the field of biosciences and all of the sciences really for these large language models tools,
*  and also for code generating tools. I feel like most scientific progress now is limited by the
*  reality that physicists, biologists, chemists, et cetera, most of their day job now is like,
*  I have all of this data, how do I munch through it? And they should not be expected to have PhDs
*  in all of their respective disciplines and also a PhD in computer science in order to be able to
*  further their research. So super, super excited about coding tools also being useful for these
*  scientists. And machine learning has also been integrated into Colab for Colab ProPlus users.
*  So the Codi API that I mentioned before has been kind of introduced within Colab to support code
*  generation, code completions, as well as code Q&A. And I believe error fixing is on the way.
*  It's quite a portfolio. I definitely think the cloud one in particular, I mean, all of these are
*  powerful, obviously, but one of my big theories is that any giant, you know, arguably possibly could
*  describe as, you know, way too complicated, bloated, over-featured, you know, impossible to
*  navigate. And by the way, no, you know, no sled on Google Cloud, like all the clouds, you know,
*  there's a bazillion features on all of them, right? It's just, it's a lot. I think those are
*  products that are going to stand to benefit the most because nobody can figure that stuff out.
*  Or, you know, nobody who's new and just like stumbles into Google Cloud today has a great
*  time. I don't think of like figuring out what they need to do with it. And this AI layer to kind of
*  smooth over all of that and like gently guide you toward the right place. Boy, I can remember
*  times I've needed that. Really interested in your thoughts on where the next leaps are coming from.
*  You mentioned multimodality, obviously being a big part of what Gemini, the next, you know,
*  the next big release is going to bring forward a couple other things that I would love to get your
*  thoughts on. We recently saw this tree of thought paper, which to me kind of suggests that, you
*  know, maybe there's a like deep mind brain, you know, obviously there's a literal organizational
*  fusion, but it seems like maybe also a fusion of approaches coming where some sort of planning
*  algorithm, you know, natively combined with the more fluid ability of the language model.
*  Is that something that you're expecting or excited about? There is tremendous potential
*  when you sort of get clever about when you call models or when you're using the capabilities of
*  a large language model, whether it's for code generation or for for answering in a natural
*  language way with other sorts of tooling or other sorts of software engineering in a performant way.
*  So a way in which this can manifest is, and there have been papers on this externally,
*  but something called execution feedback. So like say you're a large language model,
*  you give it a high level question, it generates some code, you can check to see if the code is
*  actually valid. You can even use like a large language model for this, or if you're
*  wanting to be a little bit more efficient, you could just use static analysis tools.
*  You can run the code, you can check to see that the output accomplished your task. If it did not,
*  you can kind of recursively apply the model such that it fixes the code before it runs again,
*  outputs an answer, and then you can verify. So that's not like saying, hey model, like just keep
*  going. It's actually trying to stitch these things together in a really efficient kind of clever way.
*  And then over time, if you have enough of those instances, so like the execution feedback with
*  the model like transforming at stage, then you can just incorporate that as training data,
*  and then the model understands it anyhow. But in the interim, like this kind of process of,
*  it's not just the generated pieces from the large language model, it's also the bits of
*  feedback that you get, not just from humans, but also from compilers, from execution, from all of
*  these other aspects. I'm super excited about that. That's the only way to get truly powerful systems.
*  Curriculum learning came to mind because I noticed you said that Codi was like continued
*  pre-training on code. I think OpenAI has said that their like instruct models were, you know,
*  intensively pre pre-trained on code. Seems like there's a lot to unlock there. And then also just
*  wondering if you're expecting a successor to the transformer anytime soon, or if that seems,
*  you know, impossible to imagine. I would not be surprised to see a successor to the transformer.
*  And I know a lot of very brainy people are thinking about it, both at Alphabet, but also external to
*  Alphabet, like Nomash's year, immense respect for him and the character AI team. And to the
*  curriculum learning piece, we did see tremendous gains when doing continued pre-training on Palm
*  2 with code, not just at code tasks, but also, you know, at math, at logic, at natural language,
*  even at so much so that there's a good indication that the more source code that you include in
*  pre-training data mixtures and the more math style data, the better it gets at all the things.
*  So that's definitely something that I would encourage people to test out is, you know,
*  as you're as you're doing continued pre-training, if you see that certain types of data or certain
*  kinds of data quality dramatically impact your downstream evals, that's something to consider
*  incorporating heavily or heavily waiting in the pre-training data mixture. Paige Bailey,
*  thank you for being part of the cognitive revolution. Thank you so much for having me.
*  This has been fun. It is both energizing and enlightening to hear why people listen and learn
*  what they value about the show. So please don't hesitate to reach out via email at tcr at turpentine
*  dot co, or you can DM me on the social media platform of your choice. Omniki uses generative
*  AI to enable you to launch hundreds of thousands of ad iterations that actually work customized
*  across all platforms with a click of a button. I believe in Omniki so much that I invested in it,
*  and I recommend you use it too. Use Cogrev to get a 10% discount.

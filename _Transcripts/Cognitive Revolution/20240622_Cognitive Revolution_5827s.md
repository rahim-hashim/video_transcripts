---
Date Generated: June 22, 2024
Transcription Model: whisper medium 20231117
Length: 5827s
Video Keywords: []
Video Views: 81
Video Rating: None
Video Description: Dive into the future of medicine with Google researchers Khaled Saab and Vivek Natarajan, discussing the breakthroughs in AI for healthcare. Discover how AI doctors may soon provide high-quality medical advice, enhancing global access to healthcare. Learn about the innovative use of large language models in medical applications and the potential for AI to outperform human doctors. Listen as we explore the significance of AI's role in healthcare and its implications for future medical practices, featuring insights from leaders in AI research.

SPONSORS:
Oracle Cloud Infrastructure (OCI) is a single platform for your infrastructure, database, application development, and AI needs. OCI has four to eight times the bandwidth of other clouds; offers one consistent price, and nobody does data better than Oracle. If you want to do more and spend less, take a free test drive of OCI at https://oracle.com/cognitive

The Brave search API can be used to assemble a data set to train your AI models and help with retrieval augmentation at the time of inference. All while remaining affordable with developer first pricing, integrating the Brave search API into your workflow translates to more ethical data sourcing and more human representative data sets. Try the Brave search API for free for up to 2000 queries per month at https://bit.ly/BraveTCR

Omneky is an omnichannel creative generation platform that lets you launch hundreds of thousands of ad iterations that actually work customized across all platforms, with a click of a button. Omneky combines generative AI and real-time advertising data. Mention "Cog Rev" for 10% off https://www.omneky.com/

Head to Squad to access global engineering without the headache and at a fraction of the cost: head to https://choosesquad.com/ and mention “Turpentine” to skip the waitlist.

RECOMMENDED PODCAST:
Byrne Hobart, the writer of The Diff, is revered in Silicon Valley. You can get an hour with him each week. See for yourself how his thinking can upgrade yours.
Spotify: https://open.spotify.com/show/6rANlV54GCARLgMOtpkzKt
Apple: https://podcasts.apple.com/us/podcast/the-riff-with-byrne-hobart-and-erik-torenberg/id1716646486

CHAPTERS:
(00:00:00) About the Show
(00:04:34) Introduction
(00:06:35) Flamingo
(00:11:50) Importance of data quality
(00:13:29) Amy: AI doctor
(00:18:44) Simulation Learning Environment
(00:23:26) Sponsors: Oracle | Brave
(00:25:34) Training the Agents
(00:27:29) Tens of thousands of data points
(00:30:35) How to incorporate new knowledge
(00:33:21) MedGemini
(00:34:51) Sponsors: Omneky | Squad
(00:36:38) Uncertainty guided search 
(00:39:29) Generalist models
(00:41:16) MedGemini, Gemini, multimodal, medical images
(00:44:57) Future work, integration, consolidation
(00:46:00) Cost of AI
(00:52:38) When will AI Doctors be Deployed?
(00:58:22) The Speed of Trust
(00:59:58) Societal Acceptance of AI Doctors
(01:02:06) Uncertainty-Guided Search
(01:06:02) Med-Gemini: Chest X-Rays and CT Scans
(01:17:38) AI Scientist
(01:20:01) What are the principles at play?
(01:22:58) What should we do about AI?
(01:28:24) LLM for democratizing access to care
(01:34:22) Final Message
(01:35:38) Closing
(01:36:45) Outro
---

# The AI Doctor Can See You Now, with Vivek Natarajan and Khaled Saab from Google
**Cognitive Revolution:** [June 22, 2024](https://www.youtube.com/watch?v=n_YEwSJAzXA)
*  Hello and welcome to the Cognitive Revolution, where we interview visionary researchers,
*  entrepreneurs, and builders working on the frontier of artificial intelligence.
*  Each week we'll explore their revolutionary ideas and together we'll build a picture of
*  how AI technology will transform work, life, and society in the coming years.
*  I'm Nathan Labenz, joined by my co-host Eric Torenberg.
*  Hello and welcome back to the Cognitive Revolution. Today I am thrilled to share
*  my conversation with Khalid Saab of Google DeepMind and Vivek Natarajan of Google Research.
*  This is Vivek's third appearance on the show, the most of any researcher, and for good reason.
*  As regular listeners will know, when I'm asked why we should be excited about AI,
*  my standard response is to point to the incredible potential value of AI doctors.
*  In a world where access to medical professionals is all too scarce, even in rich countries and so
*  much more in poorer parts of the world, the prospect that anyone globally one day soon
*  could have access to high quality medical advice from their personal device anytime day or night
*  for less than 1% the cost of current first world access, that is all simply too valuable to ignore.
*  And the good news is that Vivek, Khalid, and their colleagues at Google who focus on the
*  medical applications of the latest AI models have made extremely impressive progress over
*  the last 18 months, demonstrating that with a mix of techniques including strategic data
*  curation and filtering, repeated fine tuning, uncertainty modeling, and painstaking evaluation,
*  large language models can be effectively adapted to medical applications, including radiology,
*  diagnosis, multimodal understanding of medical records, and many more, often rivaling and
*  increasingly even surpassing human doctors' performance on the exact same tasks.
*  That is exciting stuff. But what's even more exciting about their work today, to me,
*  against the backdrop of continued hyperscaling and the prospect of an international AI arms race,
*  is how their results demonstrate the transformative value that we can already
*  achieve with current models, if people are willing and able to put in the hard work needed
*  to dial in and validate performance. Of course, it's undeniable that each new generation of model
*  brings greater capabilities and makes application development easier, but it's worth noting that
*  some of the human competitive results we discussed today are based on the Flamingo model,
*  which Google originally published more than two years ago now, in April 2022. And I was fascinated
*  to hear Khaled and Vivek tentatively forecast that they could probably achieve their vision of a high
*  quality general practice AI doctor, even if Gemini 1.5 Pro were the most powerful model that they
*  ever had the chance to build on. This to me strongly suggests not only that current models
*  are indeed in some sort of a sweet spot, where they're powerful enough to be extremely useful,
*  but not so powerful as to risk catastrophic harm, but also that we can afford to move with caution
*  through further orders of magnitude of scaling, confident that we won't be leaving all the value
*  we hope for on the table. In other words, there really might be solid ground from which to defend
*  my adoption accelerationist hyperscaling pauser position. While Khaled and Vivek are proceeding
*  very responsibly and methodically, cognizant of the fact that people generally need overwhelming
*  evidence before they'll be comfortable trusting AI systems in critical contexts,
*  I personally would advocate for a warp speed project for AI doctors, powered by 10 to the 26
*  class models, while the new sciences of interpretability and AI control are given time
*  to develop. In my wildest dreams, that might even be a joint project that we could work together on
*  with China. I'm really grateful to Khaled and Vivek for joining me and for the amazing work
*  that they are doing. I truly believe this technology will save many lives in the years ahead,
*  and I hope that by spotlighting it, I can help inspire others to work on high value applications
*  of today's technology, rather than waiting for further scaling to solve all of our problems.
*  As always, but even more so for this conversation, which I think is extremely important,
*  I would appreciate it if you'd take a moment to share the show with friends.
*  Know too that your feedback and suggestions are always welcome, either via our website,
*  cognitiverevolution.ai, or by DMing me on your favorite social network.
*  Finally, I'm still interested in connecting with AI engineers and AI advisors who are looking for
*  new opportunities. Earlier today, I collected all the responses I've received into a spreadsheet,
*  and soon I will be circulating that with a few friendly companies. So if you want to be part of
*  that, please ping me ASAP. Please enjoy this deep dive into the medical applications that are already
*  being built on today's foundation models with Google's Khalid Saab and Vivek Natarajan.
*  Khalid Saab and Vivek Natarajan from Google DeepMind and Google Research. Welcome back to
*  the Cognitive Revolution. Thank you for having us. Yeah, it's a real delight to be over here. I think
*  there are very few podcasts that I listen to in the AI space, and I can positively say that you're
*  the top two, Nathan. So yeah, real pleasure to be back over here. Thank you. That's kind of you to
*  say. And I don't know how you have time to listen to any AI podcasts, given the incredible terror of
*  first-party publications that you guys are involved with. So what we're going to do today is just pick
*  up where we left off a handful of months ago, and that is there have been at least five notable
*  publications that I've landed on that I want to walk through in terms of the results that you've
*  delivered, specifically in the application of large language models and the fine tuning and
*  adaptation of large language models to the medical domain. I think people are still largely
*  sleeping on what is out there in today's world, and so hopefully we can call them to attention on
*  all the great work that you guys have been doing, get into a little bit of the techniques, and then
*  for the second half we can get a little bit more philosophical and figure out how and where these
*  things should be used and where all this is going. How's that sound? Sounds perfect. Yeah. Cool.
*  The five papers that I have queued up are one on radiology, one on diagnosis, then you have the
*  most famous one, which is the med-Gemini, which is bringing the native multimodality to the medical
*  domain, an immediate follow-on extension that brings even more modalities to the gemini or the
*  med-Gemini family of models, and then one from just this week that is starting to look at the
*  interweaving of chemical structure and notation in with natural language as well. And I think that's
*  a super fascinating extension of all this work. So we've got a lot to cover. I think it's important
*  to flag as we go what the sort of base was on this, and we'll touch back on these different
*  base models later when we get to the philosophical section. But let's start with the radiology paper.
*  This one was based on flamingo, which was funny for me to read because I hadn't thought about
*  flamingo in a while, though that was one early for me when I saw the results from the flamingo
*  paper. I was like, okay, we're not just stopping at language. Basically, in that paper, you started
*  to compare the ability of a fine-tuned vision language model to do radiology reports against
*  what human radiologists can do. You want to summarize those results for us? Yeah, sure. So
*  again, I think the common strand among all the work that we've been doing over here is we're building
*  on the shoulder of giants in this field. And I think flamingo is one of the OG multimodal models
*  and papers. And it was probably one of the first to demonstrate few-shot capabilities in the
*  multimodal domain, generalizing beyond language. And so this work has been, I would say, a couple
*  of years in the making. And radiology is one of those spaces where I think a lot of the medical
*  AI research has been focused on for a long period of time. And I know that Dr. Jeff Fenton famously
*  had this quote on AI replacing radiologists, which has turned out to be a little bit infamous
*  right now. But I think he's not very far off. I guess the question of replacement of radiologists
*  is an interesting one. I was just with my wife's cousin not long ago who is a doctor and said that
*  in the hospital where she works, they often wait as much as 60 days to get a scan
*  read and get that report back. And I was like, man, 60 days, that's a long time. And she said,
*  yeah, we're all very frustrated by it. So in some ways, I think some of these replacement or
*  non-replacement questions, at least in the short term, are like, we have a massive shortage and we
*  need to just do something about that before we'd even start to worry about replacement.
*  Yeah. I think the results in the flamingo paper, I think, are for the first time showing that
*  for the clinically relevant task of report generation and not just classification of
*  pathologies, we are starting to have models that are approaching clinical utility. So I think that
*  was a really cool result. And obviously, the way we got over there was by taking, I would say,
*  a relatively modest and small visual language model compared to the sizes that we have today.
*  But bringing in a lot of high quality data, and again, a lot of it is not proprietary,
*  but rather open source. And again, credit goes to folks who have been behind this mimic data
*  repository who put together that. And so we utilize that one over there. And so when we combined
*  a very strong multimodal few-shot learner and fine-tuned that with high quality radiological
*  data, we start to see this very strong performance on radiology report generation and starts to
*  approach that of what radiologists can do. So I think that was a very cool result. I think it's
*  one of the first papers to show that. And since then, there's been several other papers, including
*  some of our own work, that has shown more progress over there. But I think the more
*  interesting bit in that paper, at least, was the human AI collaboration bit, because we had an
*  arm or a study over there where we showed that if we passed the AI reports to a human radiologist
*  and they did edits, then we... And when we look at the composite result or the composite system
*  results, those tend to be better than the AI alone or the human alone. And so that's the kind
*  of interesting nugget. And this goes back to something that I think Dr. Kurt Langloats
*  Stanford, who heads up the AME Group, he said that AI is not going to replace radiologists, but
*  radiologists who use AI will replace radiologists who don't use AI. And so this is one of those
*  first results that shows what he was saying is maybe not really hallucinating, but rather
*  he's speaking the truth. And so this is one of those first milestones towards that direction.
*  And again, there's been a lot of other incredible work in this space, not just from our group,
*  but from folks at MIT, Stanford, and beyond. But I think those were the two key or interesting
*  results over there in that paper. Yeah, it's striking to me that,
*  first of all, that I think it was April, 2022 that Flamingo was first published. It's striking
*  to me that is relevant even 18 months later. This paper, I believe, was either very late last year
*  or January of this year, but more than 18 months from publication of one paper to the other. That's
*  long shelf life for a foundation model these days. There's some interesting stuff in there too that,
*  and I think we've covered in probably enough different episodes, including some of the
*  past ones with you, where there are people like, if you're listening to this show, you're probably
*  well familiar at this point with the distinction between the narrow classification models of put
*  in an image and does it or does it not have this particular condition. Whereas here, what we are
*  getting out is a full natural language report of the sort that your radiologist would ultimately
*  provide back to a patient and their general practitioner. And there's some interesting
*  nuances there too around how data has to be manipulated and pre-processed. If you just train
*  on sort of naive reports, you have a lot of references back to history, which may not always
*  be available. And so you have to clean up that kind of stuff to teach the model exactly how you
*  want it to behave, which is to reason just from this thing and not to infer or hallucinate previous
*  medical history that it doesn't actually have access to. So some of those techniques, I think,
*  are increasingly well established. The question on data quality, it's one of those important things
*  again. So the last time we two were talking on a podcast, we were talking about mid-palm M and we
*  use the same data sets, but we did not end up using the cleaned up version of the report generation
*  data that we have, which did not have references to prior reports and things like that. And that
*  cleaned up version was curated by Dr. Pranav Rajpokar and others at Harvard. And there's this notion
*  that in some ways, progress is happening in silos between academia and industry, but that's actually
*  not quite true. I think academia does a lot in terms of investing in data sets and curating and
*  providing it and also creating benchmarks and beyond. And I think what we can do from an
*  industry perspective is releasing our frameworks and sometimes open source models that academia
*  can bring on. And so there's this already symbiotic relationship that has already, I think that's been
*  existing for a long period of time, but people sometimes tend to miss that when you look at
*  discourse on Twitter. And so that's maybe one of the things that I would stress on. And then again,
*  the importance of the right kind of data. And so we had missed that in the prior work on mid-palm M,
*  but then when we used a highly well curated cleaned up data set, and when you combine that,
*  even with a relatively small language model, that the performance can match up with larger sized
*  models and things like that. So I can never understand the importance of high quality data
*  over here. These are all building blocks of a recipe. And so it's very well possible that the
*  final outcome completely depends on how you combine them together. And so that's a lot of
*  the know-how and knowledge that you gain from working on these systems for a long period of
*  time. And then you know, okay, what are the ideal combinations of things that you can bring forth
*  together to make them more optimal? Yeah. And I think I'd also like to add to that. I think you
*  mentioned something interesting there where it took around 18 months from Flamingo to then
*  Flamingo CXR to come out. And there's this like general challenge now with generative AI on
*  evaluation, right? So we're not outputting a single label anymore. And so we can't use our
*  favorite metrics like accuracy. So I think evaluation is a big challenge now. And one of
*  the really cool things I thought about in the Flamingo CXR paper is that it really goes in
*  depth with doing the gold standard when it comes to evaluation, which would be evaluating these
*  model outputs with a panel of clinical experts. And that's what takes a lot longer is doing those
*  thorough evaluations, but they're necessary in this generative AI space. And especially in the
*  medical domain. In the medical domain especially. Yeah, that's a huge theme. And I think partly
*  applicable to the next paper as well, which is known as Amy, the headline of this. And this is
*  one that I've clipped one of the main figures from this paper and included in a number of
*  presentation slides anywhere where I'm trying to alert people to the fact that there are big things
*  happening in AI that they may not even have heard of. I pretty much always include the Amy result
*  at this point, because again, for those in the know, this is based on Palm 2. So we're still a
*  generation behind the latest and greatest that's come out of Google. But it's funny, right? Because
*  I always say to while it seems AI is moving so fast, it seems like it's old. But at the same time,
*  if you'd gone back to 2020 and dropped Palm 2 in, it would have been like absolute revelatory,
*  mind blowing. Even 2022 probably would have still felt that way. So Palm 2 is the base. And this one
*  is for me just an incredibly compelling result, which is that there is one major caveat, which is
*  that through a text only chat based interaction system, an AI doctor, if you will, the system,
*  Amy, can diagnose through a differential diagnosis process more accurately than the human doctors did,
*  human general practitioners, if I understand correctly. And I think that's evaluated probably
*  in multiple ways. But essentially, they come out ahead, the AI comes out ahead on all the dimensions,
*  right? Like it's evaluated as more accurate, the other doctors are giving it higher marks,
*  and the patients are even giving it higher marks in terms of how it scores on like, empathy and
*  making people feel heard and feel important. I can't get that one out of my head. What other aspects
*  of that result would you highlight for people? Yeah, I think in many ways, we were also surprised
*  by the progress on that one. And I remember a bunch of us after the Med Palm paper came out,
*  we were thinking about this kind of a task or a setup. And we were like just having a chat and
*  we were like, okay, how long before we are able to crack diagnostic medical conversations? So
*  the Amy project had two papers that came out. Like one was the Diagnostic Medical Conversations
*  paper, the other one was the New England Journal of Medicine case challenges. And so we were like
*  roughly having this discussion, okay, how long would it take for us to solve them? And I think
*  everyone was unanimous that it will take at least two years. And then literally six months down the
*  line, we had AI that was exceeding general practitioners on these case challenges, but also
*  on diagnostic medical conversations. And maybe the first thing I would highlight is,
*  this is a very different task in a couple of ways, right? So until this paper, we had a very well
*  curated vignettes that summarized very cleanly the clinical case descriptions and reports and
*  things like that, and presented that to the model. And then you're asking it to do a diagnosis. And
*  while that's a challenging task and has been a grand challenge in the field for decades,
*  it's not reflective of everyday clinical practice, right? So when you go to a doctor,
*  they have to, they'll first see you, they'll ask you about your symptoms and medical history and
*  things like that. And then they'll embark on this investigative journey. And then they'll ask you to
*  maybe do a few lab tests or give you some suggestions on interventions like medications
*  or things like that. And then gradually come to a differential diagnosis and a treatment planned
*  over a period of time. And so there is this decision making under uncertainty and like
*  efficient acquisition of new information. And I would say pretty much until this paper, I haven't
*  seen that in any field that we've shown that AI or LLMs are capable of doing that kind of work.
*  And so this kind of behavior is very different from what you see even with the general purpose
*  LLMs out there today, like Chan GPT or Gemini, in the sense that when you have a conversation
*  with them, ultimately at the end of the day, the way it's set up is for you to guide the conversation
*  and be the driver of the conversation. And the model is out there to assist you. Whereas in a
*  medical context, it's very different. The model has a task and a goal for sure, which is to help
*  you. But then the model has to drive the conversation and figure out the optimum plan in terms of asking
*  the right set of questions and helping you come in your care journey, basically. And so it's a
*  very different task. And to me, at least it was not clear and obvious that AI systems can be trained
*  to do that. But turns out we can. And I think the key reason behind that is the simulation
*  learning environment that we set up over there for diagnostic dialogue learning. And I think
*  Khalid can talk a lot more about that. But turns out when you do that with the progress in generative
*  AI, you can actually set up self play based systems that can learn over like several orders
*  of magnitude more data than any human doctor can possibly see, at least in the text realm and text
*  domain. And when you bring that power of simulation into the learning process, then you're starting to
*  see some of this magic starting to happen over here in the learning process. And so that's the
*  key thing. And again, I wouldn't want to over-hype the results too much. And so the last bit I would
*  state is I think the comparisons are not totally fair to human doctors because typically they are
*  not used to text based conversational interfaces. Rather, they're much used to doing it in person or
*  radio calls where you can use other cues to convey empathy and rapport and things like that.
*  And then the second thing is obviously AI systems don't tire. So every interaction,
*  they can bring their best possible selves, give you very detailed answers and things like that.
*  Whereas it's very possible that some of the doctors that we were working with in the course
*  of the study, they might be coming after a long day of clinical practice and they would be perhaps
*  a little bit tired. And it's those nuances that we also need to account for, but it is undeniable
*  that significant progress has been made over here. And Khaled, do you want to talk about the simulation
*  learning environment? Yeah. Yeah. Our goal here is to train an AI model to do diagnostic conversation.
*  And so that requires the model to try and get the information needed, like the patient, what's the
*  patient going through their symptoms. Once it understands those symptoms, it asks follow-up
*  questions on those. And then the final goal is to come to an accurate and confident diagnosis and
*  perhaps even a treatment plan. And when you have this goal in mind, you want to train an AI model
*  to do this. The first thing that came to our mind is, okay, the training data, right? Let's collect
*  training data on actual doctors interacting with patients in the real world and then transcribing
*  those and then training on those interactions. So we did that, but in the first version of Amy,
*  we saw it wasn't having the high quality conversations that we were hoping for.
*  And when we tried to dig into why that was, we saw that it's because the transcribed conversations
*  from the real world interactions weren't high quality because as we have conversations with
*  each other, unless like we're very well rehearsed, we're going to have some awkward pauses,
*  utterances, might be pointing to something. And so all those things add noise and a lot of the
*  information gets lost when we're transcribing those to text. We realized we had to come up with
*  something where we curate our own training data. And we were very inspired by a lot of the works
*  that show with these capable LLMs, you can actually curate high quality synthetic data.
*  And so that's where we came up with this multi-agent synthetic data framework where we had
*  one agent acting as the patient and we would give that agent like a patient profile. And then we'd
*  have another agent acting as the doctor and give that doctor-specific instructions. And then those
*  two agents go back and forth in a dialogue. And I kind of want to highlight two things here.
*  So with training data, quality is important as we've been mentioning, but also coverage of medical
*  conditions. So in a synthetic simulation environment, you can solve that with what we
*  call the vignette generator. So a vignette is like the patient profile. It describes what the patient
*  condition is, what the symptoms are, and maybe social history, medical history, family history,
*  and all that information you'd need. And so we generate tens of thousands of these patient profiles
*  using web search and other tools. And then so now that solves the coverage issue. So now we have
*  tens of thousands of patient profiles, right? And now we do this back and forth between the patient
*  agent and doctor agent, but then to improve the quality, we also have this third agent called the
*  critic. And so we give the critic instructions on what a really high quality dialogue is. And so the
*  critic gives feedback on those synthetically generated conversations. And then we integrate
*  that feedback to do another round of that back and forth generation of dialogues. And so that really
*  helped us scale the data coverage and improve the conversational quality and allowed us to train
*  Amy to see a lot more of these conversations. And I think that was one of the key drivers there.
*  Hey, we'll continue our interview in a moment after a word from our sponsors.
*  AI might be the most important new computer technology ever. It's storming every industry
*  and literally billions of dollars are being invested. So buckle up. The problem is that AI
*  needs a lot of speed and processing power. So how do you compete without costs spiraling out of control?
*  It's time to upgrade to the next generation of the cloud, Oracle Cloud Infrastructure, or OCI.
*  OCI is a single platform for your infrastructure, database, application development, and AI needs.
*  OCI has four to eight times the bandwidth of other clouds, offers one consistent price instead of
*  variable regional pricing. And of course, nobody does data better than Oracle. So now you can train
*  your AI models at twice the speed and less than half the cost of other clouds. If you want to do
*  more and spend less like Uber eight by eight and Databricks Mosaic, take a free test drive of OCI
*  at oracle.com slash cognitive. That's oracle.com slash cognitive, oracle.com slash cognitive.
*  The Brave Search API brings affordable developer access to the Brave Search index,
*  an independent index of the web with over 20 billion web pages. So what makes the Brave Search
*  index stand out? One, it's entirely independent and built from scratch.
*  That means no big tech biases or extortionate prices. Two, it's built on real page visits from
*  actual humans collected anonymously, of course, which filters out tons of junk data. And three,
*  the index is refreshed with tens of millions of pages daily. So it always has accurate up to date
*  information. The Brave Search API can be used to assemble a data set to train your AI models
*  and help with retrieval augmentation at the time of inference, all while remaining affordable with
*  developer first pricing. Integrating the Brave Search API into your workflow translates to more
*  ethical data sourcing and more human representative data sets. Try the Brave Search API for free for
*  up to 2000 queries per month at brave.com slash API. So just a couple of questions on exactly how
*  that works. Are you starting with the same base model for all of those different agents within
*  the system? They all start off as, in this case, palm two with just different prompting. And then
*  they do they like diverge then over time? Are you fine tuning the patient agent model distinctly
*  from the doctor agent model distinct from the critic? Yeah, we so yeah, we start off with a base
*  LLM. In this case, it was palm two. And there's some prompt engineering here to make sure that
*  the responses from the patient agent and the doctor agent are as we would expect. So we do some prompt
*  engineering there. And I guess the more capable your LLM is, the less prompt engineering you
*  probably have to do. I think it's still as possible to do this with some other LLMs, but maybe some
*  more effort would have to go in there. But the better instruction following your LLM is that the
*  kind of easier it is to set up these kinds of synthetic generation frameworks. But then to
*  answer your question, we train Amy. So after we generate those synthetic dialogues, we train Amy
*  for both the patient role and the doctor role. And so you can do this by having a different
*  instruction prompt. You're the patient, and then you train on the patient turns, and then also have
*  another instruction. You're the doctor now and then train on the doctor turns. So this Amy model
*  becomes better at both simulating the patient and simulating the doctor in this case. So then
*  as Amy gets better at playing both roles, we then generate the synthetic data again. And so that's
*  what we call the outer self-play loop, where we did this a few times. And yeah, we're using the
*  same model to do both roles, all three with the critic as well. It sounds like it's remarkably
*  not that much data. And maybe I'm not sure how many rounds of fine tuning, but again,
*  this sort of foreshadows some of the more high level discussion I want to get into a little bit
*  later. But tens of thousands of data points is obviously pretty miniscule in a world where
*  three was trained on 15 trillion tokens, right? We're talking like a very small fraction of kind
*  of pre-training scale. I don't know if you can share any data around like how many times you had
*  to turn that crank and what the sort of filter percentage was. If you had tens of thousands of
*  cases, did you have to run a million conversations to get the next 10,000 best out of those? Or what
*  is the enrichment kind of process look like in a little more detail? I think would be of interest
*  if you can share that. Yeah. So I think the key thing is we are not training the model from scratch,
*  right? So we are already building on top of Palm 2, which has seen roughly the same
*  order of magnitude tokens that say Llama 3 or a GPT-4 has seen. And so there is that base. And so
*  you don't have to reinvent all that over there. And I think the second useful comparator is perhaps,
*  okay, if you're trying to match and compare up with human doctors, like how many encounters do
*  they have over the course of their career? And if you were to do like back off the angle of
*  estimates, that comes out to be roughly in the order of like tens of thousands. And so you can
*  see that with AI systems and Carl mentioned tens of thousands of patient profiles, we can scale that
*  up very easily with net new data. And so you can cover a wide range of disease presentations and
*  symptoms and not just that, but also socioeconomic statuses, medication history, travel history,
*  and things like that. And very quickly, when you do this combinatorial cross, you can have like
*  millions, hundreds of millions of patient profiles. And then maybe the other interesting
*  bit over there is when you're doing the simulation, you can also simulate patient personalities. And so
*  you might have some patients who are very talkative, some patients who are very worried,
*  some patients who are a little bit adversarial in nature, and a human doctor has to deal with
*  all of them in a composed rational manner. And we would expect the same with the AI systems as well.
*  That's so you can start simulating a lot of variety over here. And there's a diversity over there.
*  And very quickly, when you do the math, and when you do the rollout of the conversations, that goes
*  into the order of millions. And we haven't stopped since the paper, obviously, like the checkpoint
*  was stopped at some point of time to do the study. But you can imagine the number of conversations
*  that we have easily going into like the hundreds of millions of realms and even beyond. But the
*  key thing is every time you're generating data that needs to add in net new information to the
*  model that it had not previously seen before, otherwise it would end up saturating. And so
*  the trick is how do you add that net new information so that the model is learning
*  something new and reducing its overall uncertainty in terms of solving this task? That's the key bit
*  over here. And specifically for this paper, I believe we had seven rounds of iteration of
*  the auto self play. And that's where we stopped. But again, like the project has not stopped,
*  we're just getting started. And so you can imagine a lot more work that's going on since that paper.
*  And this is now several months old now. Yeah. Okay. Two really interesting points there.
*  One, I think seven is maybe the most I've seen. There's been obviously a bunch of papers that have
*  demonstrated this self improvement via critic dynamic. And I feel like they usually top out
*  around five. So even to get to seven is going past what I've mostly seen. That's interesting.
*  Another interesting question is like, how do you think about this is top of mind right now,
*  because I just have been looking into this arc challenge that's just been announced for
*  these little like visual puzzles that today's language models can't do.
*  And there's a big debate as to is this something that you have to have if you're going to qualify
*  something as AGI or is it not necessarily so important? But the key question I'm wondering
*  about is the world changes, right? That was one of the big comments. Something like COVID pops up.
*  How do you think about incorporating new knowledge or new circumstances into something like this? Do
*  you have to go back and rerun all the loops and fold it in from the beginning? Can you just add
*  it into the eighth loop when a new disease pop or a new technique or whatever pops up onto the scene?
*  Facts in my experience, at least with like Laura low rank type techniques have been really hard
*  to get models to learn. Patterns of behavior seem to be a lot easier, but actual concrete facts.
*  Like I could not get a fine tuned GPT-3 to know my name. It would like know that I was Nathan,
*  would not know that I was Nathan LeBenz, even though I was trying to train it to write as me.
*  I could not ever get that data or at least in any reasonable timeframe, it couldn't get that
*  fact seemingly deeply learned. Okay. You've done all this, but something changes in the world.
*  How do you respond to that in the context of this sort of system?
*  Yeah. I think there are multiple tools at Artless Possible over here. I think one of the key things
*  with every round of self-play was the sampling of the patient vignettes that we had. It was not like
*  from a fixed, but rather we were also expanding that. In that sense, it was adding new knowledge
*  already, but we could do that in a more principled way. For example, if say a new COVID variant,
*  hopefully no, but if that pops up, then we can start doing that and we can add it to the fine
*  tuning mixture. Hopefully that can be learned well by the model already. But then I think this is a
*  nice segue into our latest work on MedGemini, where we are now starting to give these models
*  access to tools such as web search, which can real-time retrieve information.
*  And when you combine the ability to retrieve real-time high quality information with strong
*  and advanced clinical reasoning capabilities, then I think we're starting to get towards solutions to
*  the problem that you have outlined over here, which is again a very important and key problem.
*  But I think we have multiple tools at Artless Possible that can help us
*  address a lot of these challenges already. Yeah, I totally agree. We saw that there are
*  some interesting tricks to do to get LLMs to interact with tools like web search.
*  If the model isn't confident about something or doesn't know something,
*  it can generate questions and then use web search in order to fill in those potential gaps for
*  short-term updates and knowledge. But I do believe that we should probably do both,
*  always continue to do the self-loop we were talking about, self-play loop, where we continue
*  training on new information to have the model be more confident about the new incoming information,
*  but also for maybe a quick short-term if something came out the next day and it needs to know about
*  that to use tools like web search as well. Yeah, and maybe the last thing, and I think it's
*  perhaps the most important in the medical context, is this notion of scalable oversight that we are
*  building towards. And that requires models to have better inherent uncertainty estimates.
*  So that means more reliable behavior, such as when a model doesn't know about something,
*  then it needs to be able to communicate that back to the patient itself, but also maybe back off and
*  ask help from experts in the loop. And so that's the other kind of behavior that we are building
*  towards over here. And so that will hopefully enable more scalable oversight of these powerful
*  systems and allow us to safely deploy them in the real world. So that's one bit that we haven't yet
*  spoken about completely yet, because we still need to do some studies, but I think that's the
*  other missing piece of the puzzle over here. Gotcha. Hey, we'll continue our interview in a
*  moment after a word from our sponsors. Omnike uses generative AI to enable you to launch
*  hundreds of thousands of ad iterations that actually work customized across all platforms
*  with a click of a button. I believe in Omnike so much that I invested in it,
*  and I recommend you use it too. Use Cogrev to get a 10% discount.
*  Hey all, Eric Torenberg here. I'm hearing more and more that founders want to get profitable
*  and do more with less, especially with engineering. Listen, I love your 30 year old ex-Fang senior
*  software engineer as much as the next guy, but honestly, I can't afford them anymore.
*  Founders everywhere are trying to turn to global talent, but boy is it a hassle to do at scale,
*  from sourcing to interviewing to on the ground operations and management. That's why I teamed
*  up with Sean Lanahan, who's been building engineering teams in Vietnam at a very high
*  level for over five years to help you access global engineering without the headache.
*  SQUAD, Sean's new company, takes care of sourcing, legal compliance, and local HR for global talent
*  so you don't have to. With teams across Asia and South America, we can cover you no matter which
*  time zone you operate in. Their engineers follow your process and use your tools. They work with
*  React, Next.js, or your favorite front-end frameworks. And on the backend, they're experts
*  at Node, Python, Java, and anything under the sun. Full disclosure, it's going to cost more than
*  the random person you found on Upwork that's doing two hours of work per week but billing you for 40.
*  But you'll get premium quality at a fraction of the typical cost. Our engineers are vetted top
*  1% talent and actually working hard for you every day. Increase your velocity without amping up burn.
*  Head to choose squad.com and mention Turpentine to skip the wait list.
*  Okay. So with MedGemini, the part that sort of previews what you're describing there is the
*  uncertainty-guided search. And maybe just take even one step back and try to summarize MedGemini.
*  It's hard to summarize paper because it is a family of models, first of all, that you're
*  reporting on there with multiple different base models interested. You can maybe give a little
*  insight into why some of them are based on Gemini 1 and others are based on 1.5. I think there's
*  even a Flamingo one maybe still that is part of that mix. If one were telling a naive story of,
*  okay, here's Amy. This thing can have a chat interaction and it can do diagnosis. What comes
*  next now that there's Gemini and it's multimodal? You would think, geez, probably like a chat with
*  video chat or a chat with the ability to put in images, but I would have guessed that the next
*  step would still be this sort of like holistic patient-doctor interaction. And that's not really
*  what this paper was about so much. It's much more like a lot of different models, very narrowly
*  scoped and dialed into very particular tasks. A lot of different tasks, a lot of different
*  state-of-the-art results, a lot of different modalities, whether it's pathology, imagery,
*  or scans of various types, or even some genetic kind of information. And then with the extension,
*  also you've got 2D and even 3D scans. So just a ton of different stuff. I guess maybe why the
*  Swiss Army Knife approach there is one thing, and then we can get back into a little bit more of the
*  uncertainty guided search. Yeah. Again, great questions. So I think a good way to think about
*  Metgemona is it's like the analog to the Metpalm paper, but with obviously a much more capable
*  base model over here. And so if I were to summarize, okay, what is the key takeaway over here? I think
*  for me, it is the fact that now we have native multimodal understanding over millions of tokens
*  and million plus context windows. And that seems like a very big advance. And so in some ways with
*  Metpalm, the key thing that we relied on over there in order to capture the imagination of the public
*  and show how much progress we've made was the USMD analog. I think with Metgemona, maybe it was a
*  little bit difficult for us to say, okay, this is this one thing that it enables. And because
*  when you have multimodality over millions plus context windows, a lot of new things now become
*  possible. And so that's why maybe there's not just this one thing that you can say, oh, this is the
*  one thing that's happening. But rather it's like a huge array of possibilities that now suddenly
*  becomes feasible and possible. And so maybe that's the takeaway for me. It's hard to distill and say,
*  oh, yeah, this is only this one thing, but rather it's like a platform that enables a lot more new
*  things over here. And coming back to the specifics, right? Like, why do we not have a generalist model
*  anymore? I think it's also a little bit of an evolution of our own research theories and like,
*  which way we want to build towards. And so I think this time last year, we had not yet demonstrated
*  the idea of a generalist model in medicine. There were a few examples of that in robotics and maybe
*  in a few other domains, but that still felt like something that no one had demonstrated yet. And so
*  it was interesting to do that. And we did that with Matt Parma when we showed the capabilities.
*  But then when like over the course of last year, when we were trying to think about, okay, how do we
*  deploy this in the real world and enable people to make use of them? We realized that there's a lot
*  of trade-offs that you need to make over there. Trade-offs in terms of the kind of data that is
*  brought into the mix, what tasks you're optimizing for, what is the latency and
*  throughput requirements. And that in turn ties back to the size of the models that you're serving.
*  And so it felt like this generalist approach where you're trying to cram everything into one model,
*  which in turn invariably means like the largest models in nature. Sometimes the cost is not worth
*  it for specific applications. And so what may be like specific applications or demand is like
*  trade-offs. And so you need to be able to provide a menu of options over here. And so that is why we
*  stepped back from this notion of building one generalist model to do everything over here,
*  because it felt like from a research perspective that we showed that challenge is no longer like
*  out there, but rather it's possible to solve. But from an application and real world deployment
*  perspective, what is really needed is an area of specialist models and develop with different
*  constraints in mind so that we can easily deploy. And so that's a goal over here. And so some
*  applications might demand not a lot of reasoning capabilities, not a lot of multimodal capabilities,
*  but rather a very low latency and high throughput. And for that we have the smaller size models.
*  And then some would demand advanced clinical reasoning, million plus context windows and so
*  for them, we have many options as well that are catered to that. And that's a reason over here.
*  Yeah. And I agree with everything that you said. And I'll think about the MEDGEMINI paper as our
*  first exploration to seeing how well GEMINI can do in the medical field and how should we start
*  thinking about specializing GEMINI to the medical field. And so in this first exploration,
*  we definitely wanted to look into textual reasoning, like what Medpalm and Medpalm2 did,
*  and then also advancing the techniques over there. And that's where the web search and
*  agentic framework came in. But then also because those GEMINI is a multimodal first language model,
*  we wanted to look into how do we specialize it for things like medical images. But then what was
*  really interesting is during this exploration, we had this breakthrough in GEMINI of having the
*  one million and now two million context length. And so we also wanted to start thinking about,
*  okay, how can we start exploring how to leverage that for the medical domain?
*  So GEMINI has all these amazing things, but we have all these ideas on how we should specialize
*  it to the medical domain. First, what works best, right? And how well does it do? And so
*  let's first report on a broad range of benchmarks. And that's what that paper mainly focused on.
*  And then we showcase some of the qualitative aspects, like having multimodal conversations,
*  which is also a very important part because just having a task, like just one question, one answer
*  is very helpful. But the ability to interact and have follow up conversations is what really,
*  I believe, has some clinical translation to the real world and utility. So we showcase some of
*  those qualitative things. And then with the long context, we were looking at new tasks, like if you
*  have multiple EHR logs and visits, some things that's extremely long that couldn't fit into the
*  context window previously, how well would GEMINI do in processing that and being able to look up
*  specific conditions or details in the history of the patient? And then also things like surgical
*  video and having conversations with a surgical video and then asking questions across 12 different
*  genetic papers. And it was just look at all these things that GEMINI could do. And these are the
*  techniques that worked really well for specializing GEMINI. But then again, you're also hitting at the
*  point of why not an AMI-based style paper? And that's definitely something that we're thinking
*  very hard about. It's just that requires more rigorous evaluations with clinical experts and
*  takes a bit longer. And that's why the first paper was more benchmarks, qualitative examples,
*  and we're working hard on the more rigorous evaluations with clinical experts.
*  Yeah. And maybe just to add onto that, I think we're at the stage right now where maybe our
*  evaluation setups and benchmarks are no longer as keeping up with capabilities advancements.
*  And doing that in a rigorous manner takes time. And so we still have to rely on imperfect measures
*  like existing benchmarks, but that clearly don't capture the set of capabilities. And sometimes you
*  say, oh, look at this on this benchmark, say on MML, you just got 0.6% improvements, but that's like
*  just one tiny fraction of the capabilities of the entire system. And how do we showcase that? So
*  that's an open challenge for us as well. We've resorted to doing a mix of quantitative evaluation
*  on benchmarks plus like qualitative demonstrations. But clearly I think we need better measures of
*  progress over here than what we have right now, which is largely static benchmarks driven at this
*  point of time. And that's true, I think overall for the field, but definitely for progress in the
*  medical domain. Yeah, that makes sense. So I think one takeaway from that is we can stay tuned for
*  future work that might start to consolidate this. This is the proliferation phase of look at all the
*  many different things we tried and we can expect a consolidation or maybe integration is probably
*  a better word phase to follow that in the not too distant future. Maybe that's what we should
*  expect in general is to tick tock like new fundamental or new level of scale or new foundation
*  model or whatever kind of comes out. Now it's, hey, we got to go broad and just try this thing on
*  50 different things, see in a very broad way, can we characterize it? And then we can bring all that
*  into some form factor that would actually be intuitively usable for whether it's a doctor in
*  the field or even a patient or whatever. And that does make a lot of sense. And I think also certainly
*  the doctors will probably want to see that sort of detailed breakdown as prior work or qualifying
*  work before they would be ready to trust such a system. One thing that you had said that caught
*  my ear a little bit was cost. And you had said for some things it might be too expensive. I
*  am of the opinion, and I would even say this outside of medicine, that people are overly
*  worried about the price of their AI products today. I hear this fairly often from people
*  that are building general purpose AI assistant type products. And I'll say, why aren't you using
*  just the very best model available and just stuffing whatever context in there that you
*  need to make it work? And sometimes they'll say, well, it's too expensive. The product would have
*  to be $500 a month or whatever. And I say to that, give me something that works and I'll pay the $500
*  a month. It's still probably often like order of magnitude cheaper than what it's replacing,
*  even if it were $500 a month or whatever. And on top of that, obviously we have these dramatic
*  price drop trends that showed no signs of stopping. Gemini Pro 1.5 is $7 per million
*  input tokens. So it seems like the cost is ultimately not going to be that much of an issue,
*  but maybe I'm missing something. How are you thinking about the cost? What is the current
*  concern and where do you see that going? Yeah, I think the trends are overall in the right
*  direction, as you say. I think the cost per token is going down dramatically and it's
*  probably going to continue that way as we do more of this hardware software integration over here
*  across the entire stack. And I think 1.5 Pro is great, but Flash is, I think, hitting the sweet
*  spot in terms of capabilities versus surprising trade-off. And you can go even further lower for
*  on-device stuff like the nano models. And so I think all that's great, but maybe the one key
*  thing is, at least at Google, and this is something I got used to it over a period of time by being
*  over here, the tendency is to not just aim for the top 1% of the population, but rather think
*  about it at a billion user scale and at a global scale. And for a large part of the world,
*  in addition to, I guess, the high amount of utility that you get from different kinds of Google
*  services, it is attractive that these services are, at the end of the day, free to access.
*  And so there may not be like $500 per year would seem not so high for the UMI and Khaled over here.
*  We're very fortunate to be in California, probably the best place in the world to be in,
*  at least as far as AI goes. But for large parts of the world, in India and Africa,
*  that's a no-go, simply. So how do we bring these technologies sustainably out there in the real
*  world? In a very affordable manner. And I think that requires us to go down even further below,
*  because one thing that we can end up doing over here is we can build up technologies,
*  but then the pricing is so terrible that it becomes a barrier for 99% of the people to access.
*  And that's completely the non-goal over here. I think what we really want to do at the end of the
*  day is to leverage the advancements in technologies to not amplify existing disparities in care,
*  but rather really enable people at planetary scale to have access to the best possible
*  healthcare possible. And that requires us to continue pushing the boundaries over here in
*  terms of cost and access and things like that. And again, I would just caveat that we're still
*  very early over here. I think we'll make fundamental technological advancements a lot more before,
*  say, overcoming challenges on the regulatory side to deploy these things. And also in general,
*  generally speaking, the societal acceptance of such technologies. But I think it's important to
*  not accept the status quo. I think we can do a lot better and we will do a lot better over here.
*  Yeah. And especially if we think about our text-based systems, I guess the cost is definitely
*  would change depending on if we're having conversation with text versus conversation
*  with a video or audio. And that would drive the cost up. And just with text alone, I think
*  as we show in Amy, you can do so much. And I've been lucky to be able to interact with Amy. And
*  it's a really amazing experience with the way it follows up and asks you questions. If you're
*  having some kind of worry or condition you're not too certain about, I think that the comparison
*  here to make is chatting with something like Amy versus doing your own research or talking with a
*  clinical expert. And that cost alone, like with the text base is already dramatically less. And
*  just excited to try and democratize it. Yeah. I certainly share that vision and the excitement
*  for the broad accessibility of this technology. It literally is my first go-to answer whenever
*  anybody's just broadly skeptical of what's going on in AI. Like, what are we going to do? Just put
*  all of ourselves out of work or whatever. And I'm like, Hey, AI doctor, let's start with that.
*  A lot of people can't see one, have to take off work, travel a long way, make real sacrifices.
*  If they can do it at all, this could be a total game changer for a lot of people. So I certainly
*  share that. I'm just wondering about the path. I mean, and I'll maybe ask it from the other end.
*  The first question is like, why not pursue the Tesla strategy of, because it does seem like
*  there's something weird too with all these systems where self-driving cars are probably
*  the number one example in my mind, but AI doctor probably not too far behind,
*  where it's not enough for it to be similarly effective or even a bit better than the human
*  provided service. It has to be like 10 times safer, it seems like for self-driving cars
*  in order for them to be like accepted. And we might even be closing in on that or soon to be,
*  but until it gets to the point where it's like totally undeniable, people are just not quite
*  ready to embrace the technology. The Tesla strategy, that's just make an expensive
*  version first and use that to subsidize the kind of development of bringing the cost down.
*  Google has enough resources that maybe it doesn't even need to go that route.
*  Asking the similarly provocative question from the other end, I feel like a lot of people around the
*  world literally can't do better than Amy today. And so I wonder, at what point does it become like
*  almost a societal or global obligation to actually deploy the technology, even if it isn't
*  10 times better than the best doctor? I think we suffer a lot of times from
*  weirdness in our comparison. This isn't necessarily as good as the care that I might get at Stanford
*  Medical Center, therefore it's not fit for anyone. When in reality, it's like, that is not scaling,
*  this could scale. And I feel like a lot of people around the world would be very grateful
*  to have it. I'm sure that's something you guys talk about internally. At what point does this
*  hit a point where it almost becomes like a moral requirement that we put it out into the world?
*  Where do you think we are on that journey? Because at some point we're getting there,
*  right? I can't imagine the 2027 where you guys continue down this path and we don't have something
*  that would be like almost a moral imperative to deploy. How close do you think we are to that?
*  How do you think you approach it as you hit that threshold?
*  Yeah, before you answer, I wanted to share something. When I first joined Google last year,
*  I remember we were in a summit and I asked this, I just raised my hand. I'm like,
*  these LLM services are free, people are using them. Why can't we just have the same thing,
*  but for these AI doctor type models? And I guess I learned a lot from that answer. But I was also
*  thinking in the same space, but the medical space, it just has so many subtleties when it comes to
*  FDA regulations and the way you need to evaluate things. But I just wanted to point out that I was
*  also thinking that too. I just wish it was that simple. Yeah, honestly, I would say it's probably
*  the single biggest question or dilemma that keeps me up at night these days. We are in a very
*  privileged position that we can build out such powerful and capable technologies that can have
*  such societal level impact. But the key thing is to do that in a safe and responsible manner as well.
*  And I think one of the challenges being able to communicate progress, but do that in a responsible
*  manner. And so a lot of the progress that we've been communicating have been capabilities,
*  advancements over here. And we've tried to make sure that when we put out our papers or whatever
*  products, we add the necessary disclaimers over here that capability does not mean reliability
*  in the field. And there needs to be more evidence that we need to accrue to show that actually these
*  things are really better than the standard of care. And that requires us to do control studies by
*  integrating them into real world clinical workflows and putting them as interventions
*  in people's care journeys. And we are definitely doing that. And we hope to announce something
*  very soon, like the kind of work that we're doing in this space. But as a matter of fact,
*  as things stand today, we don't have enough data to say that these things are meaningfully
*  improving the standard of care. Yes, every now and then on Twitter, there's a post that goes
*  viral saying, oh, I use Chagybd to diagnose my condition, and this is much better than doctors.
*  But like, how much can you rely on anecdotes? For regulatory agencies, we convinced on that.
*  I don't think so. I think you need to be more rigorous. And there is a well-defined
*  process of doing that. And I think in some ways, the way you develop and bring forward these
*  technologies into the real world is not too different from how we bring drugs into the market,
*  for example. And there's a well-established process where you first evaluate things in
*  simulation, which is in vitro in the lab settings. And then if things look promising, you
*  progressively step through different phases of clinical trials. And then you finally bring it
*  into the market. And obviously, it's a very painful process. It takes years, costs a lot of money.
*  But there's a reason for things being set up that way. And that is primarily to ensure the safety and
*  well-being of the patient at the end of the day. So in many ways, we are embarking on a similar
*  journey. And so with, for example, the AME papers, we showed it in simulation with patient actors,
*  not real patients themselves, that this thing works. And so now the next step for us is to do
*  them do the actual clinical trials kind of thing, put them into real world clinical workflows,
*  put them as interventions into patients' care journeys, and get the data readouts.
*  And if that looks promising, and the first thing over there, perhaps to check is not even
*  the efficacy of the system, but rather the safety of the system. And once we are confident about
*  that, then we can gradually step up the kind of capabilities that we expose and take them through
*  these different phases. And I hope it doesn't take us 10 years, but rather it takes us much
*  smaller than that, the amount of time over here. But once we do that, I think then we will have
*  enough rigorous data to say that, yes, this thing now can be safely deployed in the real world.
*  Because the other thing that I would really personally hate is, like, I come from parts of
*  the world where, like, we don't generally have access to the best resources, right? And we're
*  almost always further behind. But I don't think it's also ethically the right thing to do to take
*  unproven technologies and untested technologies and dump them in those parts of the world. So I
*  think it's very important to test the safety and efficacy of these systems. But it turns out the
*  challenges to test the safety of these systems, you need oversight. And oversight necessarily means
*  availability of doctor resources to immediately step in when something goes wrong. And so imagine,
*  if you have an interaction with a patient, like Amy having an interaction with a patient, and it's
*  maybe it's something that's incorrect, there is a liability over there. And so the only way to ensure
*  patient safety is a doctor overseeing that entire conversation and immediately stepping with a phone
*  call or something like that and saying, oh, this thing has gone wrong. This is not the right thing
*  to do, because otherwise it can even have, like, life and death consequences. And so that's a
*  challenge. And so even testing the safety of the system requires resources, medical resources.
*  And I think as things stand today, those kind of resources are available only in the western world.
*  And so that's why we are partnering up with well-resourced CATL reorganizations to be able
*  to test the safety of the system first. And then once we have promising data readouts,
*  then we can step up through the process over here. But I guess the key thing in healthcare overall is,
*  I guess there are two things. One is there are clearly no shortcuts. I think if we end up taking
*  shortcuts, then we are going to set the field back by several decades. So it's important to do things
*  the right way. And then the second thing is everything in healthcare moves at the speed of trust.
*  And so the more trust we can build up in the system with all these different stakeholders,
*  whether that's the patients themselves or the doctors, and also folks like in the regulatory
*  agencies, I think the better it is. And it may be a little bit counter-intuitive, but I think doing
*  things the right way to accelerate and get us sooner to the future that I think we all envision
*  over here, not by taking shortcuts. Yeah, it's funny. I feel like AI scrambles so many
*  different debates. And even my own perspective, I feel is weirdly scrambled. It's like I feel alien
*  to myself sometimes when I think about how I mostly for most of my life, I've thought about
*  technology and regulation versus how I think about it now. And I do feel I find myself in
*  this weird place where I'm like, I actually am afraid of just full pedal to the metal AI scaling,
*  let's make the very most powerful systems that we can. And on the other hand, I'm like,
*  but I do want my AI doctor sooner rather than later, even if it's only on par with the human
*  equivalent or only slightly better. It does feel like waiting until it's that 10X better
*  leaves a lot on the table, but that might just be the only way to achieve the trust that you
*  talked about. And that is a great sound bite that things move at the speed of trust in medicine is
*  definitely an important insight for technology people to keep in mind. Yeah, maybe one quick
*  thing I'll also add in is the other thing that's also not very obvious to me yet is societal
*  acceptance of such technologies like this quote unquote AI doctor. It's very obvious that
*  as we keep progressing capabilities, we'll have superhuman AI diagnosticians. But the key question
*  to ask is do people really want that? And to me as things stand today, and beyond like the Twitter
*  bubble that we live in, the answer to that is maybe not obvious to me, because for most general
*  people's interactions with AI systems, it's actually quite terrible. Like I was talking to
*  my mom the other day and she doesn't use charge you pretty regularly. And the only places that she
*  has encountered AI are every time she's trying to call up an airline or a travel agency, and there's
*  a weird AI wall that prevents her from getting to the human and getting things done. And so for many
*  people like that, the experience with AI, and a lot of it is AI from the previous generation,
*  and even things like Alexa or Google Home, they're not the best. And so the expectations that
*  people have from AI are maybe quite low at this point of time, and the trust they have in AI
*  systems is also quite low. And that's primarily because again, in San Francisco, in Silicon Valley,
*  and maybe in the Twitter bubble again that we live in, technology tends to diffuse very quickly.
*  But then in the real world to diffuse at scale, at billion user scale, it takes a long time. It
*  takes decades. And I would not be surprised that it might only be like one tenth of the population
*  that has seen the GPT-4 or a Gemini yet, and we're still so far away from real diffusion and
*  adoption of this technology at scale. And so that's the other key thing. For such a technology to be
*  really useful and helpful, it requires that adoption at scale. And we are nowhere there
*  yet in terms of societal acceptance of such technologies. Yeah, that definitely is going
*  to take time. I have similar conversations with my parents as well, not infrequently.
*  And it is striking. A lot of times they'll be like, oh, I tried. My mom is Gemini advanced or
*  Google One subscriber or whatever. And she said, oh, I tried asking Gemini to plan me a trip and it
*  didn't do very well. And I was like, oh, yeah, you probably, they've got something coming for that
*  for one thing, but also you might want to go to a specialist thing and it needs to tie into APIs.
*  And so there are a lot of things where even just to select the right tool in today's world is not
*  easy. I just want to go quickly through a couple final things here and then get back to this
*  question of like, where are we going hyper scaling versus domain specialization? I think that might
*  be like the most important question for the big picture over the next couple of years.
*  I guess just briefly on the uncertainty guided search, because we had teased that up and hadn't
*  closed the loop on it. That would seem to be, first of all, if I understand it correctly,
*  it's basically just like you run the generation multiple times, see if you're getting a consistent
*  answer. I don't know if you're looking more deeply at like perplexity scores or something like that,
*  but basically saying, do we appear to be confident here in what we're saying, or do we have enough
*  uncertainty that we need to go acquire more information? That would seem to be also a basis for
*  a flag up to a human oversight or even just a disclosure to the user that this is off the
*  happy path here. Any more that you would want to highlight on the uncertainty guided search?
*  Yeah. So I think two things that we realized we had to get right for this to work, because if you
*  just use web search where you just tell Matt Gemini for each question, generate some search
*  queries that will help you solve the question, and then you go and you fetch those search results and
*  then add it to the input, then in fact, sometimes you might confuse the model because you might be
*  getting some irrelevant facts or the more information you're giving the model, the more
*  possibilities of something going wrong or it latching onto something that's incorrect.
*  In order to really get that right, there were two parts there. One was generating the search
*  queries, and then two is how do you integrate the search results? In order to generate the
*  search queries, we realized we had to do it in a way that was very specific to what the model
*  was confused about, not just about the general question itself. The way we did that was by
*  telling my Gemini to generate search queries by looking at conflicting responses.
*  As you were saying, we generate multiple responses, and then when we had a lot of conflicts or
*  disagreements among the responses, we would get those conflicting responses and then from
*  the conflicting responses generate search queries. So the search queries are targeting
*  what the model is specifically confused about. So that was the first part.
*  And the second part with how to integrate the search results, that's where we saw the self
*  training helping where in the training part of that algorithm, we train with search results in
*  the context so that met Gemini was used to seeing search results. And in the training,
*  met Gemini would know what the right answer is. So it also learns how to just extract specific
*  parts of the search results and not over rely on them. Those two, I think, were the key ingredients
*  to getting it to work well. Cool. Yeah. Those are good tips. That makes sense as to why it wouldn't
*  just be a token level perplexity indicator, but like an actual contrast of full responses. So
*  that's interesting. Yeah. Maybe one thing. I think an incredible amount of work. And I think
*  Carla's wife, Kirsten, has a video of the amount of effort that Carla put in over like a three month
*  window. He's coding up at gas stations and things like that. But yeah, in some ways, I think the
*  work that we did over there was maybe not the most optimal, I would say. Ideally, we wouldn't have to
*  regenerate every single time. And we would rather have the model produce its own verbalized uncertainty
*  estimates. And so we're moving towards that. And then the other thing is, again, it's like the baby
*  steps of an agent framework that is being put over here. And search is one of the tools that the model
*  will have in sarsenal, but it'll have a lot more, including the ability to talk to maybe more
*  specialized systems. So that's where we are building towards. So there are like hints and clues of what
*  we are doing over there. But I guess for this specific paper, a lot of it was optimized towards
*  doing well on the benchmarks. And so that's why we have that specific instantiation of the technique
*  and the approach over there. Gotcha. Cool. I think this is something that feels to me to be
*  much underappreciated when people talk about, are we going to run out of data? For one thing is
*  obviously the big topic recently, and that tends to focus attention on high quality text data.
*  But then I'm always like, man, there's a lot of other modalities out there. And a lot of that stuff
*  is just massive deposits of data that have not been tapped into when you think of all the
*  think of all the x-rays and the MRIs and the pathology tissue imagery and even just the chemical
*  information itself. I guess the last two, one is an extension of med-gemini getting into even more
*  modalities. I'll just read a quick quote from that one because of a couple of notable things.
*  Chest x-ray report generation across two separate data sets by an absolute margin of 1 and 12%
*  where 57% and 96% of AI reports on normal cases and 43 and 65% on abnormal cases
*  are evaluated as equivalent or better than the original radiologist's reports.
*  So basically with this one, with these 2D chest x-ray type things, we do seem to be hitting the
*  point of basically clinical utility. It's hard to read that another way. And then there was another
*  quote that I pulled out. This is the first ever large multimodal model-based report generation
*  for 3D computed tomography aka CT scans with 53% of AI reports considered to be clinically
*  acceptable. So those are pretty notable results. And I, again, just think, man, as we start to
*  integrate these other modalities of data into potentially even the pre-training mix, if I
*  understand correctly, all this stuff is done in kind of a post-training scale such that the models
*  have seen whatever they saw on the internet, but they weren't really concentrating on CT scans,
*  for example, in pre-training. You're bringing a relatively modest data set to this, creating
*  these distinct encoders, basically creating a framework to add all these different new modalities
*  in after the bulk of training is done. Do you think that it continues to be that way or do you
*  think that where we're going is more like CT scans and all this stuff just get dumped into
*  the pre-training mix and it all is just native at some point in the future? Like natively multimodal
*  means like literally all the modalities in say a year or two. Yeah, I think it's an open question
*  for me. The path I would like to see is again, like more generalized encoders. So I wouldn't
*  want to see hundreds of 2D encoders and hundreds of 3D encoders, but rather I would want any 2D
*  modality to be processed by one single encoder, regardless of whether that's a natural image or
*  a medical image. And same with 3D, right? I would hope that we have encoders that are able to
*  process videos and 3D medical images equally well. But as things stands today, that is not the case.
*  You do get quite a bit of boost when you have specialized encoders. And I think that's where
*  maybe also the question or the challenge of whether you throw that into the pre-training mix or
*  whether you do adaptations or post-training also comes in. So if we have generalized encoders that
*  are shown to work well across different types of data modalities, then I can imagine a lot of this
*  data starting to be mixed up with the pre-training mixtures. And then you don't have to maybe do a
*  lot of the specialization or the adapters or the post-training work that you do. But if we don't
*  get there, then maybe the specialization route would hold on for a little bit longer. So I think
*  that's the interesting question that needs to be answered in the next few months. So can you,
*  for example, train a 3D encoder that does equally well on 3D medical imagery like CT scans or OCTs
*  or MRIs or whatever, and also video data, for example? And if you're able to start showing that,
*  then you can reduce the need for specialized encoders. And that in turn makes a lot more
*  things feasible at the pre-training space. Because, yeah, again, if you imagine the different stages
*  of model development, pre-training is the most general catch-all. And then you gradually have
*  a narrowing of the funnel with more specialization. And so the more general purpose encoders that you
*  have and the more you can show that those general purpose encoders can interpret a lot richer
*  modalities of data, the more you can start throwing interesting mixtures over there.
*  But we are not there yet right now. Yeah, I agree. It would be nice to move to just general encoders
*  that can really capture everything really well. But I would also argue that for something like
*  the medical domain, it is definitely worthwhile to put in more resources into that specialization
*  piece. And then even if we have these really broad and good encoders that work very well
*  for the medical domain and we don't need the specialization, I think we would still need
*  specialization for how we want the models to behave in a clinical context. So like the diagnostic
*  conversation and how to follow up with the patient and things like that. So the behavior
*  piece, I still see that as even if we solve the encoder piece that we would need that specialization.
*  Yeah, that makes a lot of sense. Okay, so the last paper on my list is TX-LLM. This is another
*  interesting one where again, essentially more modalities. This time, if I understand correctly,
*  representing chemical structure basically just as text tokens in the way that any former pre-med
*  student can recall the Cs and the Hs and the Os and the way that those are laid out in a string
*  to represent a chemical. The interesting finding here is that you can weave those into training data
*  alongside other text and that lo and behold, this is obviously becoming a recurring theme.
*  The model learns how to deal with that kind of stuff too and seems to be developing a sort of
*  a set of higher order concepts. This is like the remarkable finding of interpretability that
*  the models are representing these higher order human recognizable concepts, love, justice,
*  fairness, unfairness, whatever as a means to predicting the next token. It seems like here
*  there's something similar happening, but what I find so fascinating about these other modalities
*  being woven in this way is that probably in a lot of cases, we don't even know what those higher
*  order concepts are. So I guess my expectation for this sort of work is that it's a remarkable
*  first step that we can weave this stuff in and then we can start to get these guesses out.
*  But I also see interpretability being turned on these models and doing this sort of
*  sparse autoencoder type work to identify what are the internal concepts and then actually
*  discovering new concepts about the world that the models have actually learned as a means to
*  next token prediction that we didn't even have coming in. Is that how you understand what's
*  going on here? Is that where you see things going as well? Yeah, maybe I'll take a step back and
*  explain the motivation of this work a little bit more in detail. So I think if you look at
*  scientific history and if you look at scientists like Alexander Fleming or Jonas Salk and others
*  who've discovered penicillin and the polio vaccine, they used to all be like practicing
*  clinicians and so they would see patients during the day and then use those insights and come back
*  at night to do the laboratory experiments. And so in many ways, obviously our primary mission is to
*  build out medical superintelligence that can democratize access to healthcare.
*  But the process of doing that naturally feels like trying to encode the biomedical universe.
*  And that means data from across the entire biological stack and so starting all the way from
*  like subcellular molecular measurements, gna sequencing, RNA sequencing, protein data,
*  all the way up to medical imagery, EHR, clinical and population health level data.
*  And so when you start encoding that at scale and train these models to learn useful representations,
*  then these models can start doing interesting things. And the overall composite system that
*  you have or you probably will end up having is like a hybrid AI physician scientist. And so this
*  model is not only going to help us fundamentally democratize access to healthcare, but it's perhaps
*  also going to help us improve our understanding of human biology, help maybe design better therapies
*  and really help scale personalized healthcare to everyone. And so that's like the broader,
*  longer term vision over here. And you're seeing specific instantiations of this overall composite
*  system through the work that we did on Amy and also this one. And I think in this one, again,
*  this is a little bit of an older work. And so a lot of the techniques that we were used are from
*  like the Met Palm era, if I may use that word. And so like all the data is textual data in there.
*  And the model was not necessarily optimized for conversations. It was just like instruction tuning
*  at the end of the day. But the interesting result is the fact that you can possibly have a single
*  journalist model that you can use across the entire therapeutics drug discovery pipeline over
*  here. And so that includes tasks at the discovery slash target identification phase, all the way up
*  to clinical trials and things like that at the final stages of the pipeline. And so it was
*  interesting. I think there are some things where we are still much further behind state of the art
*  specialist models, but then there are other things where we are already very good. And the interesting
*  thing is this transfer learning that is happening between different therapeutic modalities and
*  learning of interesting representations. I wouldn't say that we've done enough work in terms of
*  uncovering what sort of unique insights that this models are learning. So there's a little bit more
*  work to be done over there, but I think the results are promising. And then I guess maybe one other
*  paper that I would want to talk about is the work that we're doing a little bit on the biomedical
*  discovery slash genetic discovery side of things. And so over there, it's not the inherent representations
*  that these models learns themselves that we are using for discovery, but more rather the
*  generative outputs that these models produce. And so if you just generally think about LLMs and
*  modern multimodal language models by training on a lot of data and especially scientific literature
*  and things like that, they are already encoding more knowledge than any human can and any scientists
*  can. And obviously hallucination is a big challenge with these systems, but the flip side of
*  hallucinations is creativity. And fundamentally for advancing science and discovery, you need
*  creativity. And so the idea over there is can we tap into that ability and capability of these
*  systems? Right. And so in very preliminary work from late last year, we showed that you can use
*  these models to identify causative genetic factors of different kinds of rare diseases. And so
*  specifically the work that we did in collaboration with some awesome collaborators at Stanford
*  was that we use these models to come up with a hypothesis for hearing loss phenotype in mouse.
*  And then the collaborators did like CRISPR knockout experiments to validate the hypothesis.
*  And so that itself, the data is very promising. And since then we've used it to also look at human
*  variants of unknown significance, because again, rare diseases and undiagnosed diseases are a huge
*  challenge. And the more we can get at in terms of identifying causative genetic factors, the better
*  we can in terms of providing care to such people. And so to me, that's one of the most exciting bits
*  about the kind of systems that we are developing. I mean, we focus quite a bit on the clinical
*  aspects over here, like diagnosis and treatment management. But for me, the other exciting bit
*  is in general, the fundamental understanding of human biology, the fundamental understanding
*  of causative mechanisms of diseases and being able to then design better therapies and things
*  like that to really just scale personalized healthcare. So that's where we are stepping
*  towards over here. And this is why it's an honor to work with Fivik because he's an ambitious
*  visionary in the field of medical AI and there's no shortage of amazing things to work on.
*  And you're too kind.
*  Yeah, that definitely resonates with me. It seems like we're headed for,
*  a singularity might be like a little strong, but I am struck by just how on track we are for a lot
*  of the like late 90s, early 2000s, Kurzweil style predictions, and also how timely they have been.
*  We're not that far off from the curves that they drew in those books 20, 25 years ago now.
*  It seems like in addition to the foundation models and learning these new modalities, whether it's
*  genetic sequences or all these different scan type modalities, we're even these chemical
*  notations, they're also going to be trained to use the specialist tools. So if I just try to project
*  a little bit out into the future, it's not only that the core models get better and that they get
*  this more agentic post-training finishing to be able to recover when they run into obstacles and
*  come up with a new approach to try to accomplish their goal, which a lot of times these days,
*  I feel like they are smart enough to do it, but they just don't quite have the pattern of behavior
*  that I need them to have to get over humps on things. But then in addition to all that,
*  they're also going to have Alpha Fold 4 to call on when they need to, and they'll presumably be
*  trained to use all these. And there's obviously a version of that for material science, and there's
*  a version of that for basically everything under the sun. So it seems like we very much are on track
*  to the AI scientist. And I guess I both am very inspired by that and a little bit fearful of it,
*  just because I do think these things seem like they are on track to become more powerful
*  than any of us individually certainly are. Maybe not necessarily to overwhelm the collective in the
*  next couple of years, but definitely I would not bet on myself to go head to head with the AI scientist
*  and try to discover it over the next couple of years. I guess, is that your expectation? And if so,
*  how do you feel about it? No, I think I share your sentiment. This repeated joke on Twitter
*  right now where people say, oh, we were promised flying cars and then we got 280 characters.
*  It feels like we were promised flying cars and we got much better, which is GPT-4 slash Gemini
*  style AI agents, Alpha Fold kind models that can do protein structure prediction, self-driving cars,
*  progress in AR, VR, Vision Pro, and things like that. And taking a step back, I would say that
*  the technological progress that has happened over the last decade definitely has been quite
*  incredible. And it feels like multiple different technologies are converging and we're going to be
*  accelerating quite a bit. Again, at the end of the day, I think the key thing is how do you
*  wield such powerful systems and technologies? And so what are the principles that play over here?
*  And with any kind of technology, there's always dual use capabilities. It was true
*  like 5,000 years back when man discovered fire. It was true when we discovered the steam engine.
*  It was true when we discovered electricity. It was true when we discovered nuclear energy.
*  And I think it's the same as well as we now advance with the AI capabilities. And if you look at
*  what has happened in history, obviously there would be concerns with such powerful technologies,
*  but we've ultimately as a society figured out a way to use these systems in a manner that benefits
*  optimally a lot of people. And I would expect that to be no different over here. Obviously,
*  there's going to be a lot of discussions, a lot of churn, and a lot of societal level questions
*  that need to be answered before we get there with AI. But I'm hopeful in humanity for sure.
*  I think we'll figure out a way. Yeah. And perhaps, I think one to get there to that AI scientist
*  vision and to make progress there, perhaps one key blocker is building a simulation environment to
*  test hypotheses. Because right now, as Vivek was describing, the LLM gives us a hypothesis. We have
*  to go to the wet lab and do testing, and that takes months. And so if we can improve simulators,
*  biological or whatever domain, then we can have that iteration loop be much faster and try out
*  many more hypotheses. And I think that would be a key breakthrough there as well. Yeah. Maybe one
*  final quick thing over there is engineering the right amount of safety in these systems.
*  And obviously, we have this AI physician scientist vision. But the key thing that we've
*  been stressing on is always having the expert in the loop to be able to validate or control the
*  kind of experiments that are being run. And so we are not trying to, for example, integrate the
*  system with, say, a robotic process automation lab environment, because we currently don't,
*  I think, have a very good handle on how to safely control this. So it's about doing things in a
*  manner where you're very clear that the development is happening with safety first and foremost as
*  paramount. And obviously, we will figure things out. We'll get better at simulators. We'll get
*  better at controlling these systems. And that will help us in turn accelerate progress further. But
*  yeah, the key thing is having the expert in the loop right now. So last kind of big
*  topic I wanted to bounce off you guys is my own position. And I always say we need to be more
*  focused on what is first before we can jump to what ought to be done about it. And almost
*  everything I've done in this process of making this podcast has been trying to just get really
*  clear on what is what's why is it working, all that kind of stuff. But at this point, we've got
*  legislation proposed, and there's definitely a shift toward what should we do about it. So I'm
*  trying not to shirk my duty as a commenter and at least have some go to answer. My answer right now,
*  if people were to just say, Hey, Nathan, what do you think we should do about AI broadly? I use this
*  phrase that I described myself as an adoption accelerationist, hyper scaling pauser. And what I
*  mean by that is basically that I'm really excited about the AI doctor and the AI coder and like all
*  these different applications. But I am worried about creating something that is genuinely super
*  human. It does seem like that's quite plausible to arrive with a few more orders of magnitude of
*  scale. Obviously, nobody knows that could totally flatline and not work, or it could work faster than
*  people expect. And maybe it's here in it seems like we are hearing increasingly 2027 expectations
*  from people. I'm not when I say pause, I do mean genuine, like, pause in the sense that I don't
*  think we need to stop forever. I do think that we are making incredible progress on interpretability
*  and control. And that line of research is actually going much better than I had expected it to go
*  18 months ago. But it does feel like it's maybe still struggling to keep up with just like the raw
*  scaling drumbeat that's happening. So what I wanted to ask you is, okay, if that's my
*  recommendation, is that a coherent position? And when I say is that a coherent position,
*  it means can I have my AI doctor without like too much more scaling? I think right now I say
*  we're in the sweet spot where GPT-4 and you know, Gemini 1.5 are like, powerful enough to be really
*  useful. Probably the next generation still is in the sweet spot where they're powerful enough to
*  be really useful, but they're not so powerful that I like, I have to worry about major accidents
*  happening or just like overall systems level stuff getting out of control. But then the question
*  becomes, can we actually get what we want from that level of power? You can answer this in any
*  number of ways, but ways that I was thinking of putting the question very specifically would be
*  like, if Gemini 1.5 Pro or if we imagine a Gemini 1.5 Ultra or whatever was like the best language
*  model that you could have, do you think you could still achieve your vision of the AI doctor
*  with all of the sort of post-training optimizations, validations, elbow grease that
*  you're putting into it? Or do you think there is something fundamental that still is yet to be
*  unlocked that needs the Gemini 2 or Gemini 3 actually get there? Yeah, maybe I'll say a couple
*  thoughts. I think maybe the idea of superhuman intelligence, I don't know why we necessarily
*  should be maybe scared of that because in a lot of ways the tools we have now are already in some
*  ways better than humans. Like just our calculator can have better at doing calculations than a math
*  PhD or a computer might be better at recalling certain things or having larger memory. And so
*  our tools are already superhuman in a lot of axes. And so I don't necessarily, as long as
*  those tools are fully controllable by us and we're able to use them to benefit humanity,
*  I think that's a great thing. For me, maybe it's because I'm an AI researcher, but it's easy for
*  me to put both hats on where one hat is, wow, these AI systems can already do amazing things
*  and the results with Amy are pretty mind-blowing. And I think there's no argument that the pace of
*  AI improvement is incredible. But at the same time, it's easy for me to switch that hat and go, wow,
*  these AI systems still have so much to improve on. And hallucination is the first thing that
*  comes to mind, but it is a serious issue. And even with Amy and AI doctors, I think that is an issue
*  that at least keeps me up at night is like, how do we fix this hallucination issue? And so I think
*  that we can do a lot with Gemini 1.5 and to benefit humanity. And if it did pause at that,
*  we can still have a lot of benefit with building Amy on top of Gemini 1.5. But to really solve
*  issues that keep me up at night with hallucination, especially in those settings, I think it is needed
*  to continue improving these models because they can fail on very basic things as we see on viral
*  posts on Twitter that show a very concerning lack of reasoning. At the same time, they do
*  amazing things. So I think we do need to improve those concerning error modes. And I'm not, of
*  course, it's an open problem. I don't know if scaling is the solution, but I think we need to
*  keep thinking hard in a research sense about how to close those gaps when it comes to those
*  concerning reasoning errors. Yeah, I'm very, very confident you'll solve hallucinations.
*  I think I tend to agree with Khaled over here. If you day to day interact with these systems,
*  you simultaneously feel like these are the smartest systems that you've ever seen and also
*  perhaps the most stupid ones in some ways. And maybe to answer your question very directly,
*  do I think we can build some sort of a system that can democratize access to care with
*  where current LLMs are today? I think that is possible. And I take a lot of inspiration from
*  how self-driving cars and Waymo has evolved. And we don't have AGI for sure, depending on the
*  definition, but we have self-driving cars that are functioning and are perhaps the most magical
*  experience that AI has to offer. They have shown the way. And the key thing is, again, it's not
*  something that happened magically, but rather a lot of systematic development, investment and safety
*  in simulation in overall systems engineering. And I think for us to get to a system that can
*  democratize access to care, we will need the same kind of thing. And the real thing is challenges
*  such as hallucinations, but also dealing with the long tail that you see over here. And that
*  ultimately comes down to the kind of data that you can bring forth to be around these systems to learn
*  and experience from. And also how do you actually train these systems? And over there, I feel like,
*  again, we still don't have the best possible handle. We need to get better at things like
*  process supervision to really improve the overall reasoning process towards solving a given task.
*  And so, yeah, I would say if I were to have these base capabilities as we have today,
*  we can definitely build it, but it'll take us a bit more time. And so if we have more capable
*  systems, it will take us a little bit more time. And that's one of the maybe the best parts about
*  working at a place like Google, where we can continuously integrate the advancements that
*  are happening in base capabilities and build out on top of them. And if at any point of time
*  progress stalls, that's fine. We'll keep pushing the vision. But the fact that we're able to do
*  this, I think allows us to perhaps get to the overall vision and the place that we all want to
*  go to sooner. So I think that, I think that checks out to me. My intuition was that I think you guys
*  can get there. Even if there's, it's not that the base model wouldn't necessarily get better,
*  right? Obviously, all these things suffer from major definition problems, including what is AGI
*  and what kinds of super intelligence and even just what's good enough to use. If we're defining a
*  pause hypothetically as basically you can only train foundation models at the general flop
*  scale that they've been trained or maybe one more or of magnitude beyond that, there is still
*  a lot of low hanging fruit in terms of just like all the different techniques that have proliferated
*  over the last couple of years. I don't think any single system has integrated all of those
*  techniques into one single model or one single system at this point. So that feels like we have
*  probably a couple of years worth of work just to integrate all those different techniques.
*  And then a lot of work of the sort that you guys are doing to really dial in performance. And it
*  does feel like we're pretty much to the point where it can happen even without like massive
*  further scaling. Now, I will also agree with you that it probably is undeniable that it would
*  get there faster. And that's maybe where my adoption acceleration is hyper scaling,
*  pause or position becomes at least partially incoherent. But I do love the work that you
*  guys are doing because I think we are headed. I don't know if you feel this, but to me, it feels
*  like we are headed for a, especially last week, we had the either the situational awareness
*  manuscript published and there's this sort of prophecy, which might in some ways become like
*  a self-fulfilling prophecy of an AR arms race with China and this like race to scale scale and the
*  trillion dollar data center and whatever. And that feels to me like a recipe for an unstable world.
*  And I'm like, man, is there any way that we can avoid an AI arms race with China?
*  I would really like to avoid an AI arms race with China. And I think that the work that you guys are
*  doing is so important in that it demonstrates how much value there already is. In some cases,
*  even from a spring 2022 model, but certainly from the latest models, how far those things
*  can really take us and how much the practical utility depends. Not to say it doesn't depend
*  at all on further scaling, but certainly even in the absence of further scaling or even with a
*  model that's now two years old with focused attention, with a commitment to really dialing
*  in the performance, you can get so much value. And I think that is something I want people to
*  pay a lot more attention to. The fact that we already have a lot of power and we're still
*  figuring out how to wield it effectively in these high value domains. And that's the big,
*  obviously, I just want the AI doctor too, but in the sort of big picture of AI and the dynamics,
*  and are we going to race with China to some unknown super intelligence as fast as we possibly can and
*  try to achieve decisive advantage over each other? Oh my God. I think it's really helpful to keep in
*  mind that the AI doctor doesn't necessarily depend on that and that it could be with this level or
*  maybe a little bit more or whatever, but also it's just dedicated work of people that are really
*  committed to the problem that is going to make, and maybe even more and probably more so than the
*  next level of scale. Because the next level of scale in all likelihood is going to be smarter,
*  obviously, and can maybe do some more really crazy things, but you're still going to have that
*  problem of, as you said earlier, behaviorally, you've got to dial it in. Reliability wise,
*  you've got to dial it in. A lot of the same problems are still going to be there, even if
*  the model is incrementally more capable just because of scale. So I love what you guys are
*  doing. I really commend it. I think people should be much more aware of this line of work, and I
*  appreciate all the effort and all the great results that you guys are delivering.
*  That might be a good note to end on. Is there anything else that, and I appreciate all the
*  time that you've given today too, not just today, but in your third appearance Vivek,
*  anything else you want to touch on before we call it for today?
*  No, I think I completely agree with what you said. I couldn't have summarized it any better,
*  I think. Perhaps the only thing that would change if progress plateaus is what sort of
*  modes exist for businesses that are built or the go-to-markets and the commercialization strategies,
*  but that doesn't distract from the fact that the kind of things that we envision are truly
*  possible. It'll just maybe take a little bit longer or take a different path. So in that sense,
*  I think that's very exciting to know that such things are no longer in the realm of science
*  fiction. And to me again, it's a real privilege to be able to go deep and talk on specific topics
*  with you. And I think you are an awesome communicator of AI progress. And this is perhaps,
*  as I said, the best podcast over there. And the key thing for maybe a lot of the people to know
*  is, yeah, I think it comes down to the fact that we need to have like rational optimism
*  about these things. And I think you perhaps more than anyone else manage to strike a balance,
*  I think. And so that's the key. I think we need everyone. We can keep doing work, but if it's
*  projected or hyped up in a different way, then I think that's also quite bad. And yeah, I really
*  hope you keep doing this. Yeah. And Nathan, I totally agree with what you had said earlier.
*  Like for me, it feels like it's our responsibility to try and bring this amazing technology to where
*  it's something like healthcare or an AI doctor and democratize access to a lot of people for
*  good quality healthcare. And yeah, it's been a pleasure also listening to your podcasts in the
*  past. Actually, funny story, you might be one of the reasons why I am here at Google, because I was
*  listening to the Medpalm talks, the podcasts that you had, and I learned a lot about those papers
*  through your line of questioning. And I think that allowed me to maybe impress Vivek a bit to
*  get into. I didn't know that actually. Yeah. Yes. And so thank you for democratizing AI education
*  and doing this and giving us this opportunity to talk more about our work. Cool. That is awesome
*  to hear. I really appreciate it. Khalid Saab and Vivek Natarajan, thank you for being part of the
*  cognitive revolution. Thank you. Thank you. It is both energizing and enlightening to hear why
*  people listen and learn what they value about the show. So please don't hesitate to reach out via
*  email at tcr at turpentine.co or you can DM me on the social media platform of your choice.

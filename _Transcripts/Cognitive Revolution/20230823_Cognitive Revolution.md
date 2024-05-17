---
Date Generated: April 03, 2024
Transcription Model: whisper medium 20231117
Length: 4937s
Video Keywords: []
Video Views: 1210
Video Rating: None
---

# Google’s Multimodal Med-PaLM with Vivek Natarajan and Tao Tu
**Cognitive Revolution "How AI Changes Everything":** [August 23, 2023](https://www.youtube.com/watch?v=2RMpqheYKlw)
*  If you look at medicine as a discipline, it's inherently multimodal in nature.
*  Doctors and clinicians routinely interpret data from all sorts of modalities ranging from
*  clinical text to imaging to lab records and lab tests and vital signs and census data.
*  We like to set the bar high and we like to go after the most ambitious problem. And for that,
*  the most ambitious version of the problem felt like building a journalist biomedical AI agent.
*  It's no longer a science fiction to think that that is possible.
*  Hello and welcome to the cognitive revolution, where we interview visionary researchers,
*  entrepreneurs and builders working on the frontier of artificial intelligence.
*  Each week, we'll explore their revolutionary ideas and together we'll build a picture of how
*  AI technology will transform work, life and society in the coming years. I'm Nathan Labenz,
*  joined by my co-host, Eric Torenberg. Hello and welcome back to the cognitive
*  revolution. I am super excited about today's conversation about Google's new multimodal
*  MedPalm M model with returning guest Vivek Natarajan and lead co-author Tau Tu.
*  This paper, published just a few months after Vivek was here to discuss MedPalm 2,
*  extends Google's insane run in generalist medical AI by training a single system that accepts not
*  just clinical text, but a wide range of medical imaging and even genomics data, and trains it to
*  perform 14 distinct medical tasks, of which text only medical question answering is just one.
*  The headline from this work is that this single model sets new state of the art performance
*  records across a number of tasks, while also coming close in a few more, all with a single
*  set of model weights. For radiology report generation specifically, the AI output was
*  preferred to that of a human radiologist more than 40% of the time. The promise for society over the
*  next couple of years is no less than an AI doctor in everyone's pocket all around the world. One
*  that can not only understand patient language and images, but also incorporate and interpret
*  new things like genomic data in superhuman ways. The insights from this conversation were, for me,
*  many. I talked with Vivek and Tau about how predictable such incredible progress has
*  recently become. The many different tricks and best practices that go into training a large scale
*  model like this. How quickly and efficiently they can conduct this work as they stand on the
*  shoulders of giants at Google. The extremely promising generalization that this system is
*  already showing. How much low-hanging fruit remains available to improve future models
*  performance. How Google's strategy of building comparatively narrow specialist systems drives
*  value while also promoting safety. The path to clinical testing and deployment of generalist
*  medical AIs. And lots more along the way as well. If you've got any doubts about AI having major
*  impact on humanity over the next few years, I think that after listening to this conversation
*  and considering not just where we are today, but how consistently we are moving forward and how
*  much room we clearly have left to run. I think that those doubts will pretty quickly fade away.
*  As always, if you're finding value in the show, we would appreciate it if you'd share it with
*  friends and post a review to Apple podcasts, Spotify or YouTube. And of course, I always
*  love to hear from listeners. This last week, I got LinkedIn notes from a London based growth equity
*  investor who said that he listens to the show in order to better understand the edges of AI leaders
*  understanding of AI systems. And also from an intelligent automation leader at an iconic
*  American manufacturing company with over 50,000 employees who said that he'd watched the AI scouting
*  report on YouTube multiple times. It is both energizing and enlightening to hear why people
*  listen and learn what they value about the show. So please don't hesitate to reach out via email
*  at tcr at turpentine.co or you can DM me on the social media platform of your choice. Now onto the
*  show with Vivek Natarajan and Tau Tu, authors of Google's new multimodal Medpalm M. Vivek Natarajan
*  and Tau Tu from Google, authors of multimodal Medpalm. Welcome to the cognitive revolution.
*  Pleasure to be back over here, Nathan. And I'm looking forward to this one with Tau.
*  Yeah, same thing. My first time doing a podcast.
*  Well, I, you know, I take pride in having a lot of first time podcast guests who are doing
*  great work on the show. So welcome to, you know, proud tradition for me. You guys have been
*  really on a tear at Google of late with, you know, an incredible series of papers
*  specifically focused on the medical use case with Medpalm, Medpalm 2 and now multimodal Medpalm.
*  And it hasn't even been that long since our first episode. You know, just a few months have passed
*  between when it was like, okay, we sort of achieved with Medpalm, you know, maybe whatever,
*  six to eight months ago, we achieved kind of passing level on the licensing exam to with Medpalm
*  2. Oh, we achieved expert level question answering. And now with multimodal, you are incorporating all
*  these other types of data, imagery, and, you know, even genetic information. So it's really
*  just incredible how fast this is moving. And yet at the same time, like I kind of wasn't even
*  super surprised by it because it just feels like you're on such a consistent role at this point
*  that these things that were once unthinkable are now almost expected. For starters, like, tell me
*  what's that? What is that like? Like you're working at this kind of critical point, I feel
*  like in human history and all these milestones just keep falling one after another. Yeah, I think
*  the key over here is we have been building on the shoulder of giants over here at Google. And so
*  in many ways, all this started off at the transformer revolution back in 2017. And then
*  more recently with the Palm series of work and the underlying infrastructure that allows you to
*  train large models effectively and efficiently at scale. So I think that helps a lot. And then the
*  second thing is at least on the medical side, again, my team at Google, we've been around for
*  several years now and you've had quite a few successes, but also a lot of failures. And we've
*  learned from that. What helps is we also have like a very nice and strong interdisciplinary team that
*  really understands medicine and health care. And so that in turn helps us, you know, motivate and
*  frame problems in an appropriate manner and then go after them. And so I would say this is just in
*  many ways, you know, the foundations have been there and around for a long period of time.
*  And this just feels like, you know, surfing the wave, like it's just the right place at the right
*  time, given all the foundations that exist. And we're just incredibly lucky and fortunate to be
*  part of it. So let's characterize this system a little bit, you know, starting with the inputs,
*  I suppose, probably the natural place to start. Previous systems have been all text. This system
*  accepts a lot more different kinds of inputs. So tell us about the new types of inputs that it
*  accepts and how you selected them. I think the motivation for this is fairly clear. If you look
*  at medicine as a discipline, it's inherently multimodal in nature. Doctors and clinicians
*  routinely interpret data from, you know, all sorts of modalities ranging from clinical text to imaging
*  to, you know, lab records and lab tests and vital science and census data. So doctors and, you know,
*  human clinicians are remarkably proficient at doing that. And I would say that that is required
*  to like really understand the context of a patient, you know, the context of the healthcare system as
*  well. And that in turn helps you provide care more effectively. So if we want to be using AI
*  in such scenarios and such situations, then these models do need to be multimodal in nature.
*  And that's what we are building towards. And now how exactly do you do this? How do you make,
*  you know, large language models multimodal? I think there are a variety of approaches where I
*  think the trade-offs are like, how much data do you have? How much compute do you have? And I think
*  many people have proposed a lot of different ideas. But for us, I think in many ways, we like to set
*  the bar high and we have, we like to go after the most ambitious problem. And for that, the most
*  ambitious version of the problem felt like, you know, building a generalist biomedical AI agent
*  that just with the same set of model weights, the same set of parameters can solve a bunch of
*  different biomedical tasks, can encode and interpret a bunch of different biomedical modalities. And so
*  this has been something that has not been previously done before. People have shown the
*  concept of a generalist agent in other domains. DeepMind famously, I think a couple of years back,
*  showcased to Gato, which I think 600 different tasks, spanning a variety of modalities,
*  actions, observations and beyond. And they showed that the same model could not only like, you know,
*  chat with you, caption your images, but also be used as the policy model for a robot that, you know,
*  stacks blocks the policy model for an agent that plays Atari games. And so that was impressive.
*  But I think there are unique challenges in medicine just because of the nature of the data
*  and the nature of modalities that you're dealing with. And so in that sense, while there has the
*  worst precedence, and again, we built on top of another system known as Palm E, which was more
*  recent, but very similar in flavor to Gato, the fact that, you know, there are unique challenges
*  inherent in medicine and biomedical data. So that was, I would say, the uncertainty associated with
*  this. Yeah, I think to answer your question directly, we included data from dermatology,
*  pathology, chest X-ray, mammography, and also genomics, in addition to clinical text. All the
*  modalities converted into an image that is digested by the model. Most of those images,
*  I have like a reasonable, you know, intuition for what they are, right? I can picture and I assume
*  listeners can picture an X-ray and, you know, can probably, we did an episode actually about
*  virtual tissue staining, which was fascinating. And, you know, if anybody heard that, then they
*  certainly should have a memory of kind of what a pathology, you know, image from a tissue on a
*  slide under a microscope would look like. As I was going through this, I didn't have an intuition,
*  though, for the genomic data. There sounds like there's a little bit of kind of a trick or
*  something, you know, maybe it's standard in the field, but I wasn't familiar with representing
*  genomic data in image form and kind of had no intuition for how that would work.
*  Yeah, so we had brilliant collaborators from the genomics teams at Google. So they have
*  developed deep variant model, which is the state of the art variant calling model used in the field.
*  So what they did is they converted in the genomic sequence into a 3D tensor that can be
*  digested by inception type of vision network. So we borrowed the idea from their model, and then
*  we did some reshaping in order to make the image compatible with our vision transformer encoder.
*  In our team, I think, getting back to again 2018, 2019, the genomics Google health team has been
*  building out the system known as deep variant that's used for variant calling. The way they
*  did this was actually cast that problem into an image classification problem, because back then
*  that's what deep learning models were really good at. We were very good at computer vision, and I
*  think LLMs did not just yet catch up. And so the first version of these models used inception systems
*  and later on Resonance as well. And so this clever encoding of genomic signals and data in the form
*  of image representations helped with that task. And the models were actually really good. And so
*  if you look at the performance of these systems, they are really accurate. And so the FDA runs a
*  challenge known as precision FDA challenge. And I think for a couple of years, I may not be getting
*  the details right, but this system won the challenge. And maybe another bit of detail over
*  here is more recently, so there was this effort from a bunch of researchers at Stanford led by
*  Professor Yuan Ashley. And they had this system that set a world record for sequencing, variance
*  and calling out what might lead to a particular disease. And they set the world record for that.
*  And so one of the key components in that system, in addition to all the innovations that's been
*  in general going around like really fast real time sequencing, has been this way in calling system
*  that really helps in improving the accuracy of the reads that you have. And so that was like
*  something that was celebrated. I think it was published in the New England Journal of Medicine.
*  And so this component, this variant calling system was a key part of that.
*  If I understand correctly, then it's genomic data that is encoded in an image. And then the output of
*  that is like a sort of, I guess it was more of a classification originally, like this is a, you know,
*  unusual sequence, or this is a sequence that is, you know, likely to be problematic because it's
*  unusual. But now you guys are doing that in a much more holistic way, right? Like now it's not just
*  a classification scheme. So did you essentially recreate that capability in the course of this
*  palm fine tuning that you didn't like actually bring any weights or anything right from that prior
*  work? Yeah, that is correct. So all of this was trained from scratch in addition to all the other
*  tasks that we had in medical imaging and doing medical quest answering from text and beyond.
*  I think one of the nice things about the generative setup that we have with large language
*  models is everything can then be framed as a generative task. And so even classification
*  problems, which were previously, you know, you were outputting a vector and coding probabilities
*  of different classifications. Now you can just have a language model and say, well, I think this is a
*  suspected variant, or I think this is like this disease in dermatology or whatever. So it just
*  unifies everything and provides language as a common grounding. And we can get into this in more
*  detail, but that gives you a lot of advantages. We didn't really build on any previous specialized
*  model weights. So what we did actually build on was the weights from the PUM-E model,
*  which is the backbone of vision language foundation generalist model that was originally
*  designed for robotic tasks. Yeah. And maybe very quickly to add to that, that did not have any
*  medical domain fine tuning. So it did not see any dermatology images or these genomic variant
*  images and any medical text. And so when we looked at the out of the box performance, and that was
*  one of the baselines that we compared to as a generalist model without any medical domain fine
*  tuning, the model was not very good at all. And so that in turn shows the importance of medical
*  domain fine tuning, medical data and medical specialization. If you want these kinds of
*  systems. Yeah, that's super interesting. So PUM-E was basically to help robots move around the
*  kitchen and like pick up, you know, objects and follow directions. Right. So yeah, it's amazing
*  how all this stuff is kind of just, I don't want to say easy to recombine, but I want to hear a
*  little bit more about this, your kind of successes and maybe some failures too, because just the pace
*  at which you guys are coming out with these results, it feels to me from the outside, like
*  everything's working. Hey, we'll continue our interview in a moment after a word from our
*  sponsors. If you're a startup founder or executive running a growing business, you know that as you
*  scale, your systems break down and the cracks start to show. If this resonates with you, there
*  are three numbers you need to know. 36,000, 25 and one. 36,000. That's the number of businesses
*  which have upgraded to NetSuite by Oracle. NetSuite is the number one cloud financial system,
*  streamline accounting, financial management, inventory, HR and more. 25. NetSuite turns 25
*  this year. That's 25 years of helping businesses do more with less, close their books in days,
*  not weeks and drive down costs. One, because your business is one of a kind. So you get a
*  customized solution for all your KPIs in one efficient system with one source of truth.
*  Manage risk, get reliable forecasts and improve margins. Everything you need all in one place.
*  Right now, download NetSuite's popular KPI checklist designed to give you consistently
*  excellent performance, absolutely free at netsuite.com slash cognitive. That's netsuite.com slash
*  cognitive to get your own KPI checklist. netsuite.com slash cognitive. Omniki uses generative AI to
*  enable you to launch hundreds of thousands of ad iterations that actually work customized across
*  all platforms with a click of a button. I believe in Omniki so much that I invested in it and I
*  recommend you use it too. Use Cogrev to get a 10% discount. And you know, that probably isn't quite
*  literally true, but when you set out to do this project a few months ago, were you guys like
*  pretty confident that this was going to work and get basically here? Or did you actually have,
*  doubt in your heart of hearts that, hey, maybe this still won't work? I would have been betting,
*  I think if I was you, I would have been betting on it working pretty well. But I'm wondering,
*  if there's actually more uncertainty in what is possible when you're in the trenches doing the
*  work. I think at a high level, you are right. The fact that systems such as Gato and Pami and
*  Flamingo and various others existed, pointed us that this thing is doable. But I think it always
*  comes down to the details and the devil is in the details. The other question is, okay, from
*  like a scientific perspective, it is interesting to build a journalist agent that can broadly be
*  competed at a bunch of different tasks. But then the other question is, okay, like if you're looking
*  forward, what is the utility of this? And today we have a lot of specialist systems. For example,
*  there's a highly accurate mammography breast cancer screening system that's being used in
*  clinical trials across the world. And so if you want to use this journalist agent, you need to
*  be able to perform at that same level. And so that's kind of the key question. Okay, from a
*  scientific perspective, it's interesting. But you also have to think about the utility. And so that
*  was the other question that we were trying to answer. So A, can we make this journalist agent
*  perform at the same level as these narrow specialist models that you have, which have
*  been really customized and fine tuned with a lot of effort, with a lot of compute, with a lot of
*  brain power, and make it reach the same level of performance? And then the second thing is,
*  the other hypothesis is, as you start training these journalist agents to encode a lot of
*  different biomedical data at scale, can you see interesting phenomena such as positive
*  trust transfer or combinatorial generalization that emerges as you use language as a common
*  grounding to interpret different modalities and solve different tasks? Can you do more
*  effective few-shot learning? Can you do more effective multimodal reasoning? And so I think
*  those are the other things that we were hoping we would see. But then one of the difficulties with
*  systems, especially at this scale, is, I mean, you may have hypothesis, but then you have to build
*  out these systems first. And that often takes a lot of compute. And again, I can tell you more
*  about all the details that went into it, all the norms that he had to tune to make the system
*  really work. And so if you get like some of these details wrong, then you won't get what you expect.
*  And so that's maybe where always the challenge and the uncertainties. Yeah, I think for us,
*  it's a continuous learning process, even like now, when the paper is out. Like Vivek mentioned,
*  there are different options of the model, foundation model choices for a biomedical
*  journalist model. For example, POM-E and also Pardly, which is also by a large foundation model,
*  vision language model by Google. I think the choice of model can also depend on what the
*  data set we have and importantly, what kind of tasks that we want the model to perform.
*  So there are some pro and cons to different model architectures. And maybe we can come back to that
*  later. So I think one thing that I do want to highlight is so for the MEPOM-M, we
*  did not really fine tune the model with multiple images during training. I think this is something
*  certainly is important for a lot of biomedical applications, especially if you want to look at
*  a longitudinal change. Yeah. And maybe just to add a quick detail over there is the reason for doing
*  that is mostly compute reasons, because if you have multiple images, then you have to encode them
*  and get the representations. And so that adds a little bit more compute. And so if you can
*  teach the model, the notion of like an image without actually giving it a real image,
*  then that just makes it practically more efficient to train. And so we decided to use that regime.
*  And then if you look into the paper, we show that that is actually quite effective. And so even if
*  you don't give the model an actual image, but then just use these tags for an image in the few
*  short instruction, that is still useful enough for the model to understand the context. And in turn,
*  the model can generalize to scenarios where you start giving the model actually multiple images,
*  such as multiple views of a chest x-ray, multiple views of a mammogram, or like previous cases of
*  your radiology images or whatever. And so that was one of the tricks again that we used. And so
*  ultimately, I think these days in many ways, training large language models, foundation
*  models, multimodal models, it just comes down to assembling a reasonable bag of tricks and putting
*  them together in such a manner that you're not using a whole lot of compute. And based on the
*  data, you can end up building a system that's hopefully well optimized for a task that you
*  want to be solving and you care about. So there's not a lot of, I would say, secret new knowledge.
*  It's all about putting these tricks together in the right way, in the right format. And then once
*  you start putting all of them in, they start accumulating. And that leads to these outsized
*  improvements. And I think that's true for not just this work, but also Palm-E, Palm,
*  and also for other systems outside GPT-4. I think people who build that, they'll also tell you the
*  same set of things. Yeah, there's certainly a lot of know-how that seems to accumulate in these
*  leading organizations. And certainly, this is not really the topic of today's conversation,
*  but if one is looking for moats, the incredible know-how that the team has that applies all these
*  little detailed, nuanced tricks in the effective way, it's a pretty good place to look.
*  Tell me about the team, actually, because there's 50 or so authors on this paper,
*  and I believe the two of you are the first and the last name listed in the author role.
*  How does the team, take me through the whole thing, maybe. How does a project like this at Google get
*  decided upon in the first place? How does a team get assembled? Presumably, this is not a specific
*  unit of hierarchy within Google. I imagine it must cross all sorts of organizational lines and
*  different kinds of expertise. So I'd love to hear how you bring a team like this together,
*  and what the roles are, and who manages it, because it sounds pretty complicated.
*  I think one of the nice things about working at Google is the fact that, in many ways,
*  organizational boundaries and hierarchies do not exist. So again, there was no real
*  top-down mandate that you have to do this. It's more like a bunch of researchers getting together
*  and feeling that, oh, this is tractable and possible, and we should do this. And then,
*  the right set of people with the right expertise just coming together, working together
*  for a period of time with intensity, with a collective spirit, and then that happens.
*  And then the other thing is, again, when you want to do these things the right way, especially in
*  the medical domain, there's a lot of details, say, around data set access, around policy and legal,
*  and typically, when you're writing these papers, you tend to ignore those contributions
*  when you're considering who should be a paper author and who should be not. But we don't believe
*  that. We believe that that's also an important part of doing things the right way, and their
*  contributions of, say, people who are providing program management support or product management
*  support are equally as important as the machine learning researchers and engineers and the
*  clinicians who are helping frame the problem and build up the systems. And so, in that sense,
*  when you want to do things the right way, where you want to ensure that the data sets that you're
*  using, you have the right licenses to it, there's no copyright violations, and you can use them
*  onward and so on and so forth, it quickly requires a village to start doing these things the right
*  way. And so, that is what we try to ensure and stress. And so, in some ways, ensuring that people
*  are acknowledged and included in papers is the least we can do because that work is equally
*  important. Yeah, I think that is why you see papers with a lot of authors, because it's really
*  a cross-functional effort, especially when it comes to medicine. And then the other thing is,
*  again, we are not doing this in vacuum. We are not training these models from scratch,
*  but rather we are building on top of the authors of Palm and PalmE. So, for example, you can see
*  Pete Florence and Danny and Akansha Chaudhary on this paper, and they've been incredible sources
*  of support for us, bouncing off ideas, telling us what to do, what not to do. And they all care
*  about the medical domain, but maybe they don't have the time to push deeply on this. And so,
*  it ends up being a very nice collaboration. And so, that's why you see a big author list, basically.
*  Yeah, one thing I want to add to that is we also received tremendous amount of help from our in-house
*  clinicians, which is critical to do any biomedical applications, because we need fast and accurate
*  feedback for us to be able to do model iterations and give us directions. I think in the Map Palm
*  in particular, we are working with radiologist Chuck. So, he has been providing tremendous
*  insights on the model readings on the chest x-ray images. I think we use him as a
*  successful metric, like his input. Yeah, maybe another quick detail is actually
*  Chuck helped craft the prompt for the chest x-ray task. And so, if you look at it, it's very detailed
*  and it's like crafted as if how radiologists would actually interpret an image, like look at
*  different parts, how you collate the findings and summarize the findings and what you should look
*  for. And so, it's very detailed. The nice thing is we have models today that can follow such language
*  instructions to a high degree of accuracy. And the other thing is we have clinicians who can then
*  help us craft these instructions and provide the human intuition in language form. And so, yeah,
*  that's just the best of both worlds being together and helping push things along over here. And maybe
*  the final thing I would add is the incentives are also different over here. It's not a zero-sum
*  game anymore. And also, science as an endeavor, especially in AI, the way it has evolved, it's no
*  longer, I think, an individual doing brilliant things like say Einstein did in physics like a
*  hundred years back, but rather like groups of people coming together and building awesome stuff.
*  And the more we are able to empower groups of people to come together and build things fast,
*  but also effectively, I think the better it is. And ensuring that the mechanisms for that exist
*  is great. And I think in many ways, I think DeepMind and OpenAIR, they set the standard over here for
*  that. And we just hope they replicate because I think that's going to be the future for AI.
*  And so, there's no need to play zero-sum games over here. We can be very generous with inclusion
*  and authorship. And so, that's I think one of the benefits of being in industry, say,
*  was as an academia, but that's a little bit more challenging. So, the breakdown is like,
*  it's kind of everybody that's involved in all these roles. So, you've got like literal
*  doctors that are also Google employees that are providing the expertise. You've got legal,
*  that's handling all the kind of licensing and whatnot, as you said. You've got infrastructure
*  engineers. You've got people that focus specifically on like data set preparation.
*  How many at the end of the, once all these other roles are carved out, how many like down the fairway
*  ML researchers are on this project? It's hard to put a number exactly on that. I would say it's
*  probably eight or 10 maybe who have like strong and deep ML expertise. But also, one of the nice
*  things is we have people who are fluid. And so, like someone who, for example, is doing infrastructure
*  is not only doing that work, but they also tend to be equally competent at like training models and
*  building models at scale. So, the roles are kind of fluid in that sense. Like once people come onto
*  the project, they'll just do everything that takes to like make it succeed. Yeah. And also,
*  one detail of that. So, compute is always like a resource. So, not multiple people can round
*  experiments simultaneously. So, that's something you have to plan ahead of time, especially when
*  you're training the bigger models. This pathways framework, right? This is the, when people talk
*  about POM, the P in POM stands for pathways. And I don't really know what that is. If I took my best
*  guess, it would be like, it sounds like it's a framework for tapping into compute. Google has
*  its own chip, the TPU, which is kind of an alternative and proprietary AI focused chip,
*  as I understand it. That's not, doesn't do all the graphic stuff, but is specifically optimized for
*  AI workloads. What is pathways? And tell us about the process of compute. Like from the outside,
*  one would maybe imagine that like compute is effectively unlimited at Google, or at least for
*  projects like this, but it sounds like maybe not so simple as that. I think pathways was kind of
*  like Jeff Dean's dream and vision and many others have worked on it, including Akanksha, who's a
*  co-author on this paper. At a high level, it's a large scale ML orchestration system that allows
*  you to train giant multitask multimodal models on like, you know, thousands of accelerator chips,
*  which in Google's case more often than not turns out to be TPUs that are optimized for this.
*  We could probably spend like another full episode, you know, talking about pathways and the magic
*  behind it and infrastructure and everything that goes into it. But I think at a high level,
*  what is happening is, you know, if you look at, you know, large language models today,
*  they have this transformer base and transformers are mostly a lot of matrix multiplications,
*  MacModes, and the combination of Jack's XLA, which is short for Accelerated Linear Algebra,
*  it's a compiler that allows you to port code written in Jack's to multiple different accelerators
*  and distribute the code across them. And that with TPUs that are optimized for AI workloads,
*  it turns out to be like really magical because they're really optimized for
*  doing the computations effectively and also the communications that you need to be able to do
*  when you're training these systems at scale. And when I say communications, it means, you know,
*  splitting out the models, passing along activations and gradients between them,
*  and so on and so forth. And so that system as a whole is really well optimized. We can go into
*  a lot of details of, you know, what makes Jack's really special as well from a developer perspective,
*  like for example, the NumPy interface that allows you to, you know, hack things at a low level,
*  or, you know, stuff like AutoGrad and just-in-time compilation that we have, or auto vectorization,
*  all those sorts of features that, you know, make Jack's really good system. But like if you were
*  to just, you know, zoom out and look at it from a high level, it's just the effectiveness of that
*  framework and the co-optimization with the hardware that allows you to train these transformer models
*  really, really effective at scale with the kind of compute that you have access to at Google.
*  We did an episode with a couple guys from Mosaic ML not too long ago, and they've got a lot of
*  different things to bring to the table. But one big value driver of that company is, hey, we give
*  you a really high level abstracted way to think about defining what it is you want to do with the
*  data set and an optimization, you know, target, and then you can kind of hit run and all the stuff
*  below that of coordinating the different devices and making sure that the data flows as it needs
*  to flow. You really don't have to worry about that. And obviously, you know, that company's had a
*  good outcome since the time that we had that episode. So it sounds like Pathways is basically
*  the internal Google version of that, such that today, and this is like, you know, very, you know,
*  I get why you're saying standing on the shoulders of giants, because if you had to do that every
*  time, obviously, you'd be probably 100 times longer in delivering a project like this. But
*  it sounds like you get to work at a pretty high level. If I understood correctly, it even sounds
*  like it's hardware versatile or agnostic as well, right? Like it could be TPUs, but it could be
*  something else. And you don't even have to worry about that from the high level. Yeah, that is
*  right. And I think that's where the flexibility of Jax kind of helps. So you can, you know, work
*  using this Jax Numpy interface that gives you low level hackability. But then you can also zoom out
*  and use, you know, depending on the project and the choice that you make, like with Flax or Pax,
*  which is more optimized for using this pathway systems and for, you know, architecting models
*  and annotating them such that, you know, the model can be with effective model and data parallelism,
*  be effectively mapped onto the physical hardware that you have for training. So there's all these
*  layers of abstraction that you can work with. And more often than not, because of how the system
*  has been architected, you don't have to worry about these details, especially for, you know,
*  me and Tao and others, we were working on this. We are, you know, more in the applications realm
*  and the product realm. But then sometimes when you are training these models at scale, you would,
*  for example, run into spikes and losses, or you may run into non determinism or stuff like that,
*  where, for example, you need to maybe be able to be zoom in and like, you know, be able to read on
*  certain steps and you want to have determinism for that. Or you may want to, for example, ensure
*  that the data set, the batches that you're using, they're all deterministically shuffled so that,
*  like, you can recreate that checkpoint and stuff like that, that, you know, helps with debuggability.
*  So all those features exist. But then again, the nice part about this being a collaboration is we
*  can very quickly, for example, as a concha, who's been doing this for several years now,
*  about all these details. And that helps us, you know, move really fast.
*  It sounds like the actual project here might not even be like that many lines of code,
*  like the core sort of model training loop is maybe able to be somewhat simple there. You know, dare
*  I imagine it might even be elegant if you are kind of, you know, you've got obviously giant
*  data set that you had to assemble a lot of work there. You've got this tower of computing
*  management that, you know, already exists. And then you're kind of bringing those together.
*  Am I right on this, that it's actually not maybe that much code that kind of pulls together a
*  giant data set and a giant pool of compute now that all those pieces are in place?
*  We train the model on each single task individually with the uncertainty that we don't
*  know if we are mixing all these things together, it would maintain the performance that we get from
*  training them separately. So we started out doing a lot of experiment on each task individually,
*  and also figuring out the best setup. I think Vivek mentioned that we use this text only one shot
*  exemplar as a way of giving the instruction and an example for the model to know how it should
*  craft its response. So there's a lot of experiments to be done on each different
*  data sets. We also tried different setup in our task mixture. For example, for the chest x-ray
*  generation task, we have Chuck providing us very detailed instructions on how the model should
*  write the report. But for other simpler tasks, for example, classification on the
*  monography, we didn't have that. So I would say it's a lot of trial and errors. And when you're
*  actually putting all these things together, the immediate question that we encounter is how do we
*  address the proportion of each task? So because the data set varies in sizes, if the model only
*  has the same size, then the same task would be done on each of the different data sets.
*  So if we were to do a lot of design choices, we would have to run a lot of
*  experiments on the same data sets. So for example, if we were to run a lot of design choices on the
*  majority of the chest x-ray, would that be very biased towards this grayscale image that probably
*  would degrade the task performance on the genomic images? So there are a lot of design choices and
*  this system is fairly mature. But when we assemble everything together, we encounter the gradient
*  instability. So we have to apply some clever tricks to stabilize the gradient for the model to be
*  trained properly. Yeah. So maybe just to summarize, perhaps the number of significant lines of code
*  is not that big. And given, especially we have existing models that we can fork off and build
*  over here, and the infrastructure is already fairly robust. But then getting the model to
*  actually train and behave well and the number of choices that are highlighted, and I think that's
*  still a very small compared to the actual number of details that we had to go through over here.
*  Yeah. The number of experiments that we had to run and manage to get these details right,
*  and then transfer that over to when you're training up, say, the 64 or the 84 billion model or the 540,
*  562 billion model that you have. That is, I think, where the bulk of the work is. And then the other
*  big part of the project is obviously the human evaluation, setting up the infrastructure for that,
*  the user interface for that, and doing all the studies around that is where I think the other
*  area where a lot of coding and software engineering comes into the picture, in addition to the clinician
*  inputs and everything. Yeah. So the model behaves kind of different when it's small scale versus
*  large scale. I think when I look back on the experimental log, I think I ran 300 experiments
*  in the past four months to do this paper. So in practice, as you're doing this, there's three
*  model sizes that are reported on in the paper. And I think it's interesting to note also that these
*  parameters are kind of now being summed. As I'm reading through, I'm like, okay, we got the palm
*  8B, and then there's the vit 4B. Vit is the vision model. So those come together and they become
*  palm E12B. And I do find it pretty interesting, I don't want to over-interpret something like this,
*  but the fact that these parameters are now just being kind of summed, even though it was like
*  a language model and a vision model, and now they just kind of merge and now they're all working
*  together. I mean, it's amazing how well these things kind of snap together in all kinds of
*  reconfigurations. But when you're doing this in practice, are you starting with the 8 plus 4
*  equals 12B model? And that's where your 300 experiments are running. You're like, I'm going
*  to kind of set up. So if I'm taking myself through your, imagine this was what, a six-month project,
*  you kind of start off by saying, I'm going to take this, we got to get the data set, obviously,
*  together. And we already have this giant compute management stack that I can build on top of.
*  But the first thing we got to do is take a small one, run one task at a time, make sure it's working,
*  tune some hyperparameters, what's the learning rate, where are these instabilities coming in,
*  iron out those kinds of details. Okay, now each individual task seems like it's working.
*  Now let's try running multiple tasks. Let's experiment with the mix. And on and on you go.
*  This does seem to be one of the huge things that has also proven to be pretty general is the idea
*  that you can generalize. I mean, you can't fully generalize, right? I always go back to the GPT-4
*  technical report on this because they show that insanely smooth curve that predicts the loss
*  of systems as they grow. And they ultimately predict GPT-4 loss. I think with the biggest
*  model used to predict it being only one 10,000th the size of the final GPT-4 model. And so the loss
*  becomes incredibly predictable, which is insane how smooth those curves sometimes are. But then
*  you do still have this kind of, but so what kind of question, what is that actually going to translate
*  to in terms of behavior? We can maybe say what we think the loss is going to be, and we might even
*  be right, but does that mean it's going to be able to do these kind of generalizations that we
*  kind of hope for, but don't really know? So tell me a little bit more about that story. I mean,
*  fill in some more of the gaps as to what your researcher experience is like beyond what I
*  just imagined. What you outlined is spot on for text only large language models in the sense that
*  from lower sizes of models, you can start predicting to a pretty high degree of accuracy
*  what the loss would be for a large model. But then as soon as you start going into multimodal
*  realms where you're trying to bring in different building blocks together that have been optimized
*  separately, and now you're trying to fuse them together, then I think that becomes far more
*  challenging. You lose some of that predictive power. And it also happens that depending on the
*  datasets that you're training on, how you scale up these components together matter. And right now
*  we're only dealing with vision and language, but you can in the future imagine so many more
*  different modalities that will have their specialist encoders. So if there is say some
*  amount of mismatch in the capacity, and it is true that in both Palm E and in MedPalm M, there is
*  actually a giant mismatch, especially as we scale up the models. And that's why I would say we don't
*  see the expected gains in performance on some tasks that you might expect, because the language
*  capacity has been scaled in a very disproportionate manner to the vision capacity. And so the vision
*  in turn ends up being a bottleneck. And that in turn limits the overall model performance on some
*  of these tasks. So I would say that's maybe one of the challenges that you encounter as soon as you
*  start going into multimodal realms. Things become much more uncertain. Then you're trying to like,
*  you know, the only way out of this is actually just to experiment and see what happens.
*  There are multiple components in the multimodal system, the vision encoder, the language model,
*  but most importantly, there is alignment layer. This alignment layer projects the image token into
*  the same space as language. That's why Palm E has this flexibility to construct these multimodal
*  sentences, that is interleaved text and image tokens, and can be processed uniformly by the
*  language decoder. So when we think about scaling, on some of the classification tasks where the
*  language capacity is not really needed much, I think we didn't really observe a gain when we
*  scale up the language model. And also another source of variability is this vision encoder,
*  vision transformer, was pre-trained on natural images. So they have not really seen much medical
*  image, which has a complete different distribution than the natural images during the training. So
*  the transfer learning on the vision encoder can also result in the bottleneck from the vision side.
*  So I think to properly study the effect of scaling, we kind of need to isolate each component
*  separately. And that requires a lot more large-scale medical data, because we first need to demonstrate
*  that we can actually adapt the vision encoder to medical domain well before we even connect it into
*  the language model. So I think a lot of things you can only know after you do the experiments. So it's
*  really hard to predict and borrow the knowledge that we have gained from the language model domain,
*  because for language model, even though you are switching from medicine to law, the text token
*  is still in the same domain. It's just a different context. So there's a number of fascinating things
*  there. One, just to make sure everybody's clear on the results. Going through the paper, I was
*  definitely struck by this, that the mids, there's three tiers of model. There's the 12B, the 84B,
*  and the 562B. And one would naturally expect that the 562 would be the best, because it's the biggest.
*  But in reality, it wasn't really so clear. It seemed like it was kind of more or less even between
*  the middle size and the largest size. And if I understand correctly what you're saying,
*  the understanding of that result is that vision model, because across the two, the medium and the
*  large, the language part of the model, the palm part got bigger, but the vit part did not get
*  bigger, because the biggest one there is the 22B. So the idea is that if you're basically limited by
*  the power of that, not only because of its just general size, but maybe even more to the point
*  that it didn't have much in the way of medical content in its pre-training. So you're kind of
*  starting from something where you had basically very limited knowledge on that side of the
*  overall system. Yes, that is correct. And that ends up being the bottleneck. And so a good example
*  of these, like the bottleneck over here is in the classification tasks, where the output for the
*  language model is something very simple, like saying, for example, oh, this dermatology image
*  has evidence of eczema, for example. So the space of tokens that the model needs to generate is
*  fairly limited. And so there's not much scope for language understanding and reasoning. But then to
*  really do this task really well, you have to understand the image, look at patches and signs
*  and pathologies of different presentations of diseases. And that in turn requires a very
*  powerful vision encoder. And so that is why this ends up being a bottleneck, say if the model is
*  too small or it's not been trained properly or has not seen enough medical domain data. And so those
*  are the tasks where you see the gap really become small between, say, the 84B model and the 562B
*  model. Yeah. And also a practical constraint in training all the tasks simultaneously is all the
*  input image needs to be in the same shape. That certainly creates some bottleneck for the
*  ChessX3 report generation, because the image size that we fit into the model is fairly small
*  compared to most of the state of the art ChessX3 report generation specialized model that they would
*  use. These are all details that matter. And so in the end, I think that what we have shown so far is
*  that is why we call this a proof of concept. But I think there are all these little knobs that you
*  can tune and we know how to tune them that I think is significantly going to improve the
*  performance of these systems. So hopefully the next iterations as we have over here,
*  where we can, for example, adaptively process images at different scales with different
*  resolutions, change the number of tokens that you have for the different modalities, that's going to
*  make a lot of difference in addition to just purely improving the language model capacity
*  and the vision capacity and bringing in more data. Yeah. It sounds like we're now at the end of the
*  paradigm just by a long shot. Just roughly speaking, how much data and how much compute
*  are we talking here? I've looked at the range of fine tuning relative to base model.
*  And these days that range is pretty huge where on the very low end, a few dozen examples
*  can fine tune your... It's almost like you get down to few shot territory. There's a spectrum
*  from few shot up to pre-training and you can be fine tuning in a pretty wide... Several orders
*  of magnitude are in that fine tuning bucket. So was this something where it was like 1% more compute
*  relative to all that had already been poured into the models that you started with or 10%
*  more compute relative to the base? How do you think about the relative compute investment?
*  So there are two things. One thing is purely in terms of the number of tokens that you have,
*  and I'm clubbing in image tokens with text tokens. I would say that's not a lot. In aggregate across
*  the benchmark, the number of samples that we had was roughly in the order of 1 million. And then
*  if you were to take on average maybe 10, 20 tokens per sample, then you're probably ending up with
*  like 20 million tokens or something like that. That's very small in general compared to the
*  billions of tokens that go into training the base model. Yeah. Palm is like a trillion-ish tokens.
*  The original palm, if I recall correctly, is order magnitude trillion. That's right. So I think the
*  paper, they say 760 billion. I think one thing to add because the image, one image will be converted
*  into 256 tokens. So I think the 20 tokens of the convention is probably only on the text side.
*  Yeah, roughly somewhere. Depending on the exact data, 1 million into 20 or 200,
*  and you get that number of tokens, but it's still fairly small. Then I think in terms of compute
*  training these models, I would like to think it's more in the one to 10% realm of training the base
*  model. One of the factors that come into play over here is also the more chips that you have access
*  to. And we are training with TPU V4 chips over here. The faster your speed of iterations are as
*  well. And so in that sense, that is maybe something that's disproportionate between the base model
*  and the fine tuning that you can do in the sense that we may end up for different reasons for access
*  because we have access to different kinds of compute. We may end up having a different
*  chip configuration or the number of chips that we end up using. And so that sometimes plays a part
*  and that in turn also impacts the iteration speed over here. But I think the order of magnitude is
*  roughly between one to 10%. So how fast is that cycle time? I guess I'm interested in that on the,
*  when you're running your 300 experiments, I mean, a 12B model, if I had to guess, I would guess that
*  you have kind of discretionary access to that level of compute and like probably don't need to go,
*  reserving or anything. And I would guess those also return by the time you come back with a new
*  cup of coffee, or is it maybe not quite that fast? I think on average it takes a couple of hours to
*  finish training with the 12B model. So it's fairly fast. And sometimes I don't have to run
*  the experiment like to the end to be able to know if I want to make any change. That completely
*  depends on the number of chips that you have access to. So if you don't have enough number of
*  checks, for example, if you have say one tenth the number of chips, then that two hours will become
*  like two weeks. So certainly there's easy knob that we can like turn is turn off the data parallelism.
*  So basically running multiple copies on different segments of the inherited set,
*  that's going to give us significant improving efficiency. Yeah, this is a good point because
*  I think people are aware of the fact that this is a parallelizable process, but the way you're
*  parallelizing here with data parallelism is you're essentially, while still in the training room,
*  people have a little bit more intuition for this in the inference side of things, but still in the
*  training process, you're basically saying, I'm going to copy the model a number of times. We will
*  run the training process itself in parallel. And then there's, you kind of collect all the gradients
*  and all the adjustments you want to make to the weights. And then you basically just sum those,
*  right? And kind of the next round starts with like the sum of all those gradients found across all
*  the different copies. So it's pretty much, I guess there's maybe some loss of efficiency there in the
*  sense that all these different gradients, if you did them sequentially, maybe they would kind of
*  approach the goal a little bit faster. But the dominant effect obviously is that the parallelism
*  speeds it up, roughly speaking, by how many copies you have, I guess, right? If you're going to do now,
*  okay, I've done a ton of experience, it's time to really start to do the experiments on the big model.
*  Is that now a few days to run one round of the 562? I'm really interested in how fast
*  you can iterate because that seems like it's going to be a huge driver of how fast you're going to
*  solve all these other little remaining issues that we've been, you know, touching on.
*  With the compute that we have available, it's on the order of weeks.
*  That's incredible. Everything is kind of going, you know, exponential at the same time. And just
*  also the iteration cycle dropping to, you know, hours for significant scale experiments, and then
*  weeks for like the full palm E562B scale. That's probably an underappreciated
*  fact of the entire progress. It's just like you're able to run so many more experiments than people
*  could run a couple of years ago. But maybe one detail over here is as you scale up these models,
*  the other factor is more often than not, you're not going to be able to fit them onto a single chip.
*  And so there is model parallelism that comes in. And so now you're sharding the different parts
*  of the model across different chips. And then in addition to that, you have data parallelism.
*  So it's like a 3D mesh in many ways. And we like to call that a mesh system over here.
*  And Pax is the framework in which we define the mesh for the model. So that's another factor,
*  because as you're scaling up the number of chips that you need to like efficiently run these
*  training workloads also increases quite a bit. And that adds in. So we have to take all those
*  factors into account when we are training these systems. But in general, I think you are right
*  that the progress in terms of what the hardware and the frameworks that we have allows us to like
*  do things in general more fast than before. But then if you're like scaling things up,
*  then that is an effect that is pushing you in the opposite direction. So maybe the speed doesn't
*  change that much because while you're getting better hardware and software, you're also scaling
*  up these models. And in turn, that just increases your training time. I would also add maybe a
*  couple of other things. One is the fact that now I think there is generally going to be a push
*  towards more compute efficient approaches to like scaling these models, particularly in the
*  multimodal setting. And so the more we can, for example, make use of specialist encoders that
*  have been like really well-tuned for tasks such as in the VIT22B that has been trained on like,
*  I think close to a billion images and craft that into a language model like POM that has been
*  trained separately, but again on like a trillion tokens. And if you can figure out like, you know,
*  compute efficient ways of doing that crafting process, I think that is going to be incredibly
*  impactful because in general, there's a lot of competition for compute and you can, and the AI
*  is like, you know, such a broad general purpose technology and you can see so many different safe
*  and beneficial use cases spanning not just, you know, biomedicine, but also like energy and
*  climate change and beyond. And so people would want to like, you know, make use of these systems.
*  And so that there isn't done like contention for resources. The underlying message is even
*  at places like Google, efficient approaches will trump out. And so that's something we hope to
*  build and maybe Tao can say more on this. Yeah, please do. One question I specifically did have
*  on that efficiency point is the approach here is an end-to-end fine tuning, right? So all
*  562 billion parameters are subject to change. There's also kind of another class of approaches
*  that seem to be have their, I'm sure pros and cons in all sorts of different, you know,
*  nuanced ways, but from a compute perspective, these kind of like bridge or adapter structures
*  are also often like quite effective. So did you guys consider doing something like that where you'd
*  say, Hey, instead of, you know, messing with all 562, why don't we just, you know, layer, insert
*  another 10 B at the end and kind of, you know, do the last kind of adaptation of the weights or
*  whatever. I mean, obviously simplifying there, you know, we've seen a lot of those things work. So
*  did you consider an approach like that? So we actually tried even in our end-to-end fine tuning
*  where you can freeze the language model and only tune the vision or do only freeze the vision
*  until the language model or freeze both vision and language model and only tune the alignment there.
*  So there are different choices. I think I ran some experiments when I freeze the language model and
*  only tune the vision and alignment. And I think what I've seen preliminary evidence is I think
*  the convergence rate is slower. So it takes longer time for the model to reach the performance that
*  I get when I fully fine tune everything. But it does generally kind of work. Yeah. I think in the
*  Palm E paper, they also did the frozen language model version. I think this is also some experience
*  that we have gained over the development of a Metpum. For Metpum one, we did prompt tuning,
*  which is a efficient parameter and data efficient tuning methods. And then for Palm two, we did the
*  full end-to-end fine tuning. So I think empirical, the evidence that we have observed is actually
*  full end-to-end fine tuning gives you the best performance uplift provided that you have at least
*  a reasonable amount of data. Yeah, I think that's right. And it's also true even when you compare
*  like low rank of procedures such as LoRa for fine tuning. It turns out that if you can do
*  end-to-end fine tuning without using LoRa with the same data, then I think convergence is faster in
*  model quality also turns out to be generally faster. That's our empirical evidence at this point of time.
*  So even though people like to say LoRa is, for example, more computer efficient, in terms of
*  number of cycles that you spend optimizing with that approach versus say an end-to-end fine tuning
*  approach, it may turn out that the compute is actually kind of the same. The other thing that
*  jumped out to me is, if I understand correctly, this is the original Palm that this is based on,
*  right? As opposed to Palm two. I guess if I had to guess, that's maybe just the function of the
*  fact that Palm E was based on Palm. And so you're kind of building on, but there's a
*  couple of different tracks here. I'm going to go ahead and title your next paper now,
*  multimodal MedPalm two. So when can I expect that one to be dropping?
*  Yeah. So based on the learnings that we had from the MedPalm M paper, I think we are exploring
*  different approaches where we can achieve the same journalist biomedical AI. I think one example is
*  what Vivek had said. We take a more modular approach. We have these modalities with
*  encoders that might be small, like a CNN resonant. And then we find ways to combine them with a
*  shared language model. And we can take any state-of-the-art language models that we have
*  and potentially get even better performance in terms of, for example, instruction following,
*  and also augment the language model component with stronger conversational capability. So we
*  might be able to unlock new capabilities for this biomedical journalist AI system.
*  So maybe in addition to that, I think the architectural details, there's definitely a
*  lot of low-hanging fruits in terms of how we approach the training as well as the components
*  that we're using to, you know, architect the overall system. But then the other question is
*  in general around utility and what capabilities that you're targeting with this channel system.
*  And so we're also broadly thinking about that. And so in that sense, we would want to have
*  the next version of the system not only be better than what we have today on the multi-bed bench of
*  tasks, but we want to expand that bench of tasks that we are considering to maybe include more
*  different kinds of medical imagery or more biomedical data, such as data from different kinds
*  of genomic sequences, like proteomics. And so there's so much rich variety of data and tasks
*  that we can start bringing into the system. And then again, the approaches are also,
*  there's I think a range of approaches ranging from tool use to adapter or grafting or bridge
*  approaches to training these generalist agents with like end-to-end fine tuning. And so the
*  opportunity is there, but I think ultimately it comes down to what problem are you solving
*  with these systems. And I think that's the root problem that we, or the root question that we
*  first ask before we embark on these giant model training runs of these giant projects.
*  It seems like it's basically, can we create an AI doctor? I mean, is it as simple as that,
*  or how would you frame the motivation for the next system at this point?
*  It's no longer a science fiction to think that that is possible. I would still say that we are
*  very, very early, not just in terms of the technical development, like architecting the
*  system and the model as a whole, but definitely in terms of like validating these solutions,
*  verifying them, trialing them in real world settings. But for me, the most exciting part is
*  it feels like that is all imminently possible and doable. And that all seems science fiction,
*  maybe even just a few months back. But now I think that's all possible within a very reasonable
*  timeframe. And so I think that is the most exciting aspect. And maybe one of the other things is
*  again, like doctors today do a lot of different things and hopefully we'll be able to build AI
*  systems that can be effective teammates for them, effective assistance for them, like make a lot of
*  the tasks that they do and take a lot of their burden off them, like the administrative tasks
*  and everything. But then the other impressive thing is, for example, these models can start
*  doing things that maybe clinicians are not trained to do. Clinicians are not trained to interpret
*  genomic data, for example, but the scale at which we are able to measure fundamental genomic data
*  from individuals at scale today, that the cost of it is going down even faster than Moore's law.
*  And so that is going to be a signal that we want to be able to repeatedly tap into in the future.
*  And so we can have these AI systems in some ways actually be better than say human doctors today
*  on that front, like new modalities of data, new signals that we are going to be able to measure
*  with a high degree of precision. These models are going to be able to make sense of that.
*  And so in some ways, that's actually superhuman capacity and superhuman capacity to provide care.
*  And then maybe the last thing I would say is also as you start training these systems at scale with
*  such diverse biomedical data, the hope is in the process of doing that, you're going to be able to
*  also fundamentally transform your understanding of human biology, of disease mechanisms, of disease
*  trajectories. And hopefully that will lead to new insights such as potential new biomarkers
*  or different causative gene variants for say certain diseases that have been longstanding
*  grand challenges or designing of new therapies. And so in some ways, you're also building out
*  AI biomedical research scientists or research assistant or something like that. And so the nice
*  thing is I think the base components of these systems, they can lead to all these different
*  applications. And so I feel like that is the most exciting aspect over here.
*  One of the things that really jumps out in the paper is this notion of emergent capabilities.
*  I'd love to just hear your comments on emergent capabilities. I also want to hear a little bit
*  about the next generation of validation, because you guys have done a lot of work through multiple
*  papers on creating these benchmarks and being very systematic. But it seems like maybe not
*  quite yet with this one, but probably the next one, I'm wondering at what point does it go to
*  like more of a clinical trial type of modality as well, where you'd say, look, I mean, we can
*  characterize this thing a hundred ways. But at some point it is time to be like, let's give it
*  to people and see if they end up healthier than they were if they didn't have it. And that seems
*  that time has got to be close at hand. So emergent capabilities and then kind of
*  actual field clinical trial style validation. Yeah, I think Tao and I, we had a lot of debate
*  about using the word emergent capabilities in the paper, just given the wider debate in the
*  community with the Mirage paper, for example, coming out. I don't know if Tao, you disagree
*  with this from me. Emergent capabilities are just something that you did not predict would happen
*  or exist in the model that you're building. It's maybe less about model scales per se,
*  or whether there's a continuous or discontinuous improvement in performance on some of these tasks
*  or capabilities that you're looking at, but more about what unexpected new things are you seeing
*  over here. And so maybe Tao can talk more about the TB example that we had in the paper.
*  I think one interesting findings that we had from this journalist model is when the model was
*  trained on trance-electrode images and with 14 prevalent clinical observations, such as
*  the enlargement of heart. But it's not, so TB is not pathology label that we specifically trained
*  the model on. But when we present another trance-electrode image, which is acquired from
*  a different center, and the major pathology is the TB, and then we prompt the model asking
*  if there's any abnormality in the image and ask the model to generate explanations. So in this case,
*  describe the findings in the image. The model was able to actually characterize the correct
*  lesion type, which is cavitary lesion for tuberculosis particularly, and also be able to
*  identify the correct location in the image where the lesion is. But we also showed the caveats of
*  the model because the model cannot really characterize every single lesions in the image.
*  There might be some omissions, but we are excited that the model can actually identify the correct
*  location of TB and also the right lesion type. I think that's the benefit of the model probably
*  have seen like vitrature on the TB and now it was able to generate reasonings conditioned on the
*  visual input. Maybe I'll quickly add a couple more things. One is, I think we showed this in the paper
*  as well, is the number of examples that you need to actually teach the model the concept of TB.
*  We show that that's actually zero for us because we're just able to like provide a language
*  description of it. And so I think that is again coming down to the power of language where you
*  mapping everything to language means you can start describing you know signals and other
*  modalities information and other other modalities just through language. And you know that really
*  helps a lot with this kind of few short learning. Maybe the other quick detail I'll point out is this
*  definitely seems to be like an emergent capability because when we looked at the 8B model that was
*  not capable of providing any sort of explanation or description over here. But as soon as you start
*  you know having a model that has more capacity to do nuanced language reasoning and so both with the
*  64B and the 562B model that we have we see the ability to not only like you know make predictions
*  about the presence or absence of TB in image but also actually describe it to a degree that
*  a radiologist would say is fairly accurate. So let me unpack how that works as I understand it.
*  You tell me if I am getting anything wrong here. The finding is you had 14 different types of
*  radiology images that were used in training. Basically for each image there might be 14
*  different pathology labels, different conditions that you might find in the chest. That's the
*  problem with clinical significance. There's 14 labels on the images that you're using in the
*  training tuberculosis not one of them. But you find that nevertheless when presented with an image
*  showing tuberculosis in the chest x-ray the overall system can identify that and not only that but can
*  identify the specific location in the image where it is found. So that's pretty amazing you know
*  emergent capability per your definition of things you didn't predict. And I guess what's happening
*  there is the language portion of the model understands you know has enough information
*  about tuberculosis such that it is able to effectively interpret the image as it is projected
*  into language space in the form of 256 tokens. I'm always fascinated by the fact that these
*  projections end up in a place in language space that no actual language can access.
*  But it must you know it is obviously communicating or you know transmitting
*  information about like what is seen where in a way that you know it's also interesting to notice
*  pictures worth a thousand words here we've managed it with 256 tokens.
*  Enough information is there and there's enough understanding of that information. So essentially
*  it's kind of like the image portion is to the language because it's in this language space.
*  Right I almost imagine it like I don't like to anthropomorphize too much but it's almost like
*  it's whispering into the language parts here you know. In this you know portion you see this thing
*  and in this portion you see this thing and all this kind of just visual data somehow in language
*  space is enough. And then the model from there can kind of take it and be like all right well
*  if you're telling me that then that sounds like tuberculosis. I mean that really is pretty
*  incredible and I have to say the labeling that an emergent capability seems very reasonable to me.
*  I don't know what else you'd really be looking for if you're looking if you know
*  what I mean tell me I guess what's the debate on that you know is there what's the case that
*  that is not an emergent capability or that that term is maybe just that the term is more trouble
*  than it's worth. Yeah I personally I just think that's a buzz like word. So what would you say I
*  mean or how would you how do you think about the I mean is that a surprise to you when you found
*  this result were you guys surprised by it? So I am not like surprised by the model was able to
*  identify TB even though there's a chest x-ray image that is acquired from a different
*  like center it's still chest x-ray so somehow I think this image is still in distribution
*  even though it's a completely different medical concept. I think I would be rather excited if
*  actually we are doing like the additional analysis for example presenting the model with the
*  founders image that was not looking closely like any of the images that we put in the training and
*  see if the model can actually characterize the image purely based on the language knowledge that
*  it has accumulated during training. I have high expectations so I want this to be as good as
*  possible. Yeah maybe just quickly summarizing that I think what we have shown so far is interpolation
*  within the distribution of what models trained and a lot of people still like to call that as
*  creativity or intelligence. I know that Demis likes to call it like you know level one of
*  creativity or intelligence but I think what Tao is saying is he's more excited or interested to see
*  if the model can extrapolate out outside of the space of distribution that it's trained on and
*  so once you start giving it out of distribution examples like a fundus image for example can it
*  still you know start doing these novel multimodal reasoning in that space. The early evidence I
*  would say is promising but I think we still have ways to go over there so hopefully more soon.
*  So then going back to the clinical trial concept for a second how close do you guys think you are
*  to running not a sort of task level evaluation but a more kind of system level evaluation?
*  Definitely not just us within this room over here in this virtual room for this podcast who are well
*  placed to answer that but also like us just within at Google are probably also not well
*  placed to answer that. I think that's actually a broader question around how we regulate these
*  more generally capable AI systems because the way in which we typically regulate you know AI systems
*  as medical devices as software as a medical device is we assume that they only go at certain tasks
*  so they are the supervised systems that for example can only do this one task and that you know we know
*  the bounds of their capabilities but that also allows us to like you know put numbers around
*  their effectiveness and verify and validate them appropriately. But then as soon as you have like
*  these generally capable systems then the interactions that you can have with that system just explodes
*  and we don't have a reasonable method or like you can't basically retrofit the framework that you
*  had for regulating say supervised classification systems or single task systems into this framework
*  of generally capable AI systems and so that doesn't exist today and I think that needs to come into
*  the picture and so it's a conversation that's ongoing with you know people who have broad
*  regulatory expertise say with the FDA with the EU and different parts of the world but as things
*  stand today we do not have that I think what you suggest is actually a very reasonable approach to
*  take and maybe that is the approach that we go down the route of where for example we give a
*  generally capable system such as MedPalm to like a doctor or put it in the hands of people and then
*  we run a control trial and look at health outcomes say after six months a year and see if like you
*  know people are just more healthy and feel like better about themselves and beyond and maybe that's
*  the way to go over here but right now as things stand that's not how you know we are supposed to
*  be regulating these AI systems because the FDA definition of what an AI system no longer fits
*  with what we are building today. So do you think that you're blocked by current regulation from
*  doing something like that or is it more that you you know not you obviously but like Google as an
*  institution wants to make sure that it has a you know a regulatory regime to fit into
*  because you could imagine like one attitude might be hey there's no you know specific law against
*  this we're going to try and do it but another might be like we want to make sure that there's
*  like a law that says how to do it before we do it. With MedPalm 2 we are rolling out the model first
*  to trust it on test users to gather feedback that can in turn inform our model development to make
*  it more safer and effective so I would say it's like evolving we are also like learning navigating
*  along the way. What happens if you ask it questions that are not at all about medicine or you know
*  about something that's like I imagine you know in the mature version you would want it to like refuse
*  to be your lawyer right you would want it to refuse to do all sorts of things that are not
*  kind of in its wheelhouse. Is that an aspect that you have developed at this point or is that just
*  kind of like left for future work? I think that's a question general to all the like AI systems even
*  the general purpose of language models how to put on guardrails around its response. In MedPalm 2
*  testing we actually presented the model with a set of adversarial questions that with the intention
*  to break MedPalm 2. So there's a lot of work that's needed in order to basically put these
*  different guardrails around the model so it doesn't generate bias response or even amplify the health
*  inequality that was present in the training data. Yeah and maybe a couple of you know just
*  broader points. One is you know the safety and alignment question that's very important for the
*  generally capable agents and systems that we are building today but I think one of the nice things
*  about working in domains such as biomedicine fair for example maybe you're building a bot for primary
*  care triage or you know you know bot that helps with chronic care management. The domain is
*  constrained and that in turn you know makes the safety problem and alignment problem more tractable
*  say compared to a general purpose chat bot such as GPT-4 or bot that is supposed to talk to you
*  about philosophy or music or poetry or whatever and so just because of the broad range of capabilities
*  and the domain being unrestricted it becomes a lot more challenging whereas for us I think there are
*  approaches that will be intractable for safety and alignment if you had a general purpose chat
*  bot that become a lot more viable once you have like constraints over here. So I think that is
*  going to be one like one direction that we are going to take technically to do more safety and
*  alignment stuff where the the work that we do over here is going to be very domain specific but that
*  in turn will allow us to you know proceed with guarantees around these systems and enable more
*  of these you know clinical trials and regulatory conversations with safety as front and center.
*  Coming back to the other question that you had are we like you know blocked by regulation?
*  I would say a couple more things. I think it's not necessarily true. I think there's still a lot of
*  work still to be done on the base model capabilities and on safety and alignment of these systems and
*  that can you know happen in parallel to the question around how we regulate these systems
*  and then the other thing is it's just such a transformative technology such you know a pivotal
*  moment in history as you you know mentioned in the beginning of the conversation that I think
*  it's okay for us as a society to take time and have deliberate conversations thoughtful conversations
*  before we come to a conclusion one way or another on how we like use these technologies and so
*  in that sense I think it's more important for us to get this right rather than just being fast
*  over here and hopefully that happens with a degree of urgency given all the potential.
*  You had mentioned you know a kind of deep personal motivation around having grown up in a place in
*  poor part of the world in India where access to medical care is just not you know what obviously
*  you would hope it would be. How far do you think we are from really changing that in a fundamental
*  way? I mean you said it's a transformative technology but it seems to me like we're not
*  many years away from just radically democratizing access to quality medical advice if not care
*  but advice is often worth a lot you know as a precursor to care. So I mean you know you said
*  it's not science fiction like are we really looking at like a three to five year time frame to
*  put a genuine AI doctor into everybody's hands around the world? So for me personally right I
*  think you know I grew up in you know parts of the world where you know for most people going to see
*  a doctor was simply not a possibility. Oftentimes that meant walking 30-40 miles in extreme heat,
*  giving up days wages, going without food and as such you know I knew many people who did not see
*  a doctor in their entire lifetimes and that meant like for example not detecting diseases earlier or
*  dealing with the burden of like chronic diseases and overall like lower life expectancy and quality
*  of life and for me personally I've always wanted to do something about this. This goes back a
*  decade now in terms of like the motivation of you know doing something about democratizing access
*  to high quality healthcare. I'm pleased to say that I think the arc of progress in technology and AI
*  in particular especially in the last couple of years allows us to dream of that future where you
*  know world-class healthcare is democratized to billions of people worldwide and we put a world
*  class AI doctor you know directly accessible in the pocket of billions of people worldwide.
*  So in that sense I think AI is you know truly transformative because I don't think there's
*  another industry where the biggest problems of that industry are immediately solvable by AI today.
*  For example the biggest problems in healthcare are a access to healthcare,
*  b cost and c quality and all these things can be radically improved by AI today and so I think that
*  is immensely exciting for all of us working in this field because we see this opportunity and
*  that is not just true for like places like India or Africa for example but also like you know
*  solving different there are different challenges in places like the UK and EU and the US but again
*  all those problems can be solved by AI today that just feels like you know the opportunity of a
*  lifetime for and that just excites me and Tao and all of us are working on this not just at Google
*  but in you know in the wider space at large. Tao any other closing thoughts you want to share?
*  I won't share like my like personal motivation of course I share what Vivek said to make the
*  medical care accessible to billions of lives but coming from a neuroscience background I have
*  always been intrigued by exploring the mutual benefits between AI and human intelligence.
*  I think that what got me excited working at Google and especially working on this medical
*  assistant job because I think it empowered me to do the things that I have dreamed of
*  which is that I want to use AI to accelerate scientific discovery. This multimodal map is
*  providing tools for us to tackle problems like that. We can leverage the language capacities
*  like the language has seen all the let's say PubMed articles or the biomedical research and
*  if we can leverage that knowledge and help us to discover let's say new genetic biomarkers for
*  upfamers or Parkinson's that would be awesome. Yeah it's a huge vision at some point it starts
*  to seem like even the AI doctor in your pocket is maybe too small of a vision relative to the
*  potential so it's good to point out that it's not just operationalizing and scaling what we can do
*  but it's also kind of changing what we can do. Super fascinating to learn all about this new
*  system and I hope we can do it again in a few months when multimodal MedPalm 2 comes out or
*  whatever the next big milestone is because you guys are certainly on a roll and I think it's
*  one of the most consequential efforts going on in the space today so in conclusion Vivek Nadarajan
*  Tao too thank you for being part of the cognitive revolution. Yeah thank you so much for providing
*  us the platform to talk about our work and also sharing more of our vision. Yeah thank you Nathan
*  we really enjoyed the conversation. It is both energizing and enlightening to hear why people
*  listen and learn what they value about the show so please don't hesitate to reach out via email
*  at tcr at turpentine.co or you can DM me on the social media platform of your choice.
*  Omnike uses generative AI to enable you to launch hundreds of thousands of ad iterations that
*  actually work customized across all platforms with a click of a button. I believe in Omnike so much
*  that I invested in it and I recommend you use it too. Use Cogrev to get a 10% discount.

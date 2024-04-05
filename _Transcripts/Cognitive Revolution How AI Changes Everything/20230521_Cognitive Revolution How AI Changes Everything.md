---
Date Generated: April 03, 2024
Transcription Model: whisper medium 20231117
Length: 5135s
Video Keywords: []
Video Views: 3202
Video Rating: None
---

# Google’s Med-PaLM and Med-PaLM2 with Vivek Natarajan
**Cognitive Revolution "How AI Changes Everything":** [May 21, 2023](https://www.youtube.com/watch?v=nPBd7i5tnEE)
*  It just feels like the opportunity of a lifetime,
*  impacting the world in a safe and beneficial manner.
*  It's leveraged technology and AI to
*  improve the health of millions of people and
*  help people reach their true potential.
*  Hello and welcome to the Cognitive Revolution,
*  where we interview visionary researchers,
*  entrepreneurs, and builders working
*  on the frontier of artificial intelligence.
*  Each week, we'll explore their revolutionary ideas,
*  and together we'll build a picture of how
*  AI technology will transform work,
*  life, and society in the coming years.
*  I'm Nathan LeBenz, joined by my co-host, Eric Tornberg.
*  Welcome back to the Cognitive Revolution.
*  Today, we're closing our short series on AI and
*  Medicine with Vivek Natarajan,
*  AI researcher at Google and one of
*  the lead authors of the groundbreaking
*  MedPalm and MedPalm 2 papers.
*  In this conversation, we'll track
*  the amazingly short timeline that the field has taken
*  from just better than chance performance
*  on medical licensing exam questions,
*  just two and a half years ago,
*  to expert level performance that
*  Google is now beginning to commercialize today.
*  We start with an overview of
*  the foundation models that Vivek and team were building on,
*  Palm, FlanPalm, and Palm 2,
*  before diving deeply into the details of MedPalm and MedPalm 2.
*  The techniques used to develop MedPalm are of high interest
*  given their data efficiency and conceptual generality,
*  and the pains that Vivek and team have taken to
*  validate its outputs,
*  which go beyond benchmarks and endeavor to truly
*  understand the utility and shortcomings
*  of specialist medical models,
*  are instructive for anyone
*  developing AI systems for high stakes use cases.
*  While Vivek and his co-authors described MedPalm as
*  inferior to clinicians as recently as last December,
*  today, Google describes MedPalm 2 as
*  outperforming human clinicians on
*  eight out of nine dimensions evaluated.
*  As Vivek says in our conversation,
*  the trend is obvious and it's
*  hard not to be excited about the potential.
*  For Vivek, who grew up in rural India,
*  where access to healthcare often came at great cost,
*  if it was available at all,
*  the imperative to not just develop such systems,
*  but to deploy them broadly so as to
*  equalize access to medical expertise is deeply personal.
*  Toward the end of the conversation,
*  we turn to Google's business plans with
*  the newly announced MedPalm API and we
*  imagine what might be in store as
*  medical AIs become ever more capable and also multimodal.
*  One note before we get started,
*  last time I invited anyone who might be
*  interested in attempting to reproduce
*  some recent LLM benchmarking results to reach out to me.
*  One person already has and we are
*  beginning to collaborate on a project.
*  With that success in mind,
*  I'd love to invite anyone who'd be interested in
*  reading drafts of my AI analysis mega threads to reach out as well.
*  I have a number of drafts in progress and would
*  love to get some feedback from interested readers.
*  You can contact us at our new email,
*  tcr at turpentine.co or just DM me on Twitter where I am at LeBenz.
*  Now, I hope you enjoy this conversation with Vivek Natarajan.
*  Vivek Natarajan, welcome to the Cognitive Revolution.
*  Great to be here, Nathan.
*  Congratulations on an amazing run of papers.
*  You are one of the project leads,
*  lead authors on the MedPalm series of papers,
*  which has announced some incredible progress
*  several times over the last year.
*  Most recently with last week's Google I.O.
*  where you guys even are starting to
*  announce some steps toward commercialization.
*  I'm really excited to get into all this with you and dig into how it happened,
*  the brief history, the techniques that you guys are using,
*  the progress that you've made,
*  and especially really want to give our audience a sense of the pains that you've taken
*  and the ways in which you've sought to validate the performance of the MedPalm model.
*  Maybe just for starters,
*  can we go back to the beginning and tell the story of Palm,
*  where it came from, then on to like Flawn Palm and then to MedPalm.
*  You've been at Google this whole time,
*  and it's amazing that this has all happened in just like a two-year timeframe.
*  I think you're spot on that the progress has been kind of the exciting,
*  and especially the implication in settings like healthcare and medicine.
*  I think that's quite profound and it's, I think,
*  generally for me personally the most exciting time in history,
*  with all the progress that's happening over here and the possibilities I'm looking at.
*  I think if we were to look at where we are today,
*  I think many people have mentioned this,
*  but I would say it all goes back to 2017 with the Transformers people.
*  The emergence of a general purpose architecture that is highly optimized
*  for the kind of hardware that we have today in GPUs and GPUs,
*  and can guzzle up data at scale,
*  that has enabled, I would say,
*  whatever progress and breakthroughs that we have seen so far today and everything.
*  And since then, we have seen various different LM architectures
*  emerge different styles and code decoder.
*  But the key has been the transformer,
*  a lot of the emergence of that architecture.
*  And if we look at it,
*  there hasn't been maybe much of a change in the transformer architecture itself.
*  In many ways, people have kind of frozen that architecture,
*  and all the work is happening around it in terms of data and scale and computer and everything,
*  and applications.
*  But over six years, and six years is a very long period of time in AI and deep learning,
*  the fact that this architecture has kind of remained static,
*  I think that's testament to that original paper.
*  And there are no amount of praises enough for the work that, you know,
*  Ashish Rasswani and others did.
*  So, yeah, so we have the transformer building block.
*  And then I would say the next big thing or breakthrough was GPT-3,
*  undoubtedly from OpenAI,
*  and showing that decoder-only transformers trained on internet scale data,
*  using this very simple next word, next token prediction objective,
*  can do some amazing through-shot learning.
*  Albeit in natural language processing, I think that was a very big tool as well.
*  And Palm kind of like followed up on that.
*  In many ways, the recipes are similar, the architectures are similar.
*  And I think it's probably just specific details that changed.
*  But like in terms of the studies, I would say both of them are roughly very comparable.
*  The results are kind of the same.
*  It's just two different systems.
*  And I guess besides transformers and decoder-only large language models
*  and the emergence of that, the third big thing was alignment and RLHL.
*  So we had language models before.
*  I think people remember Microsoft Day,
*  or the fact that it was released on Twitter,
*  and then a day or two it went wild and crazy.
*  And but now we have like GPT-3, GPT-4, and many other language models out there.
*  And while there have been some incidents of, you know,
*  models producing unexpected things,
*  for the most part, I think the experience has been that of delight
*  for most people, right?
*  And that is all down to alignment with reinforcement learning,
*  with human feedback, the fact that we can control the outputs of this model
*  and ensure that they are behaving in a way that is expected and see it.
*  And, you know, just invokes delight in people.
*  So I think these three things are kind of like what has led to where we are today
*  with these large language models like GPT-3, GPT-4, and Palm and Palm II.
*  And I would really say the work that we are doing in medicine
*  with large language models generally is just building on the shoulder of these giants
*  that's happened over the last five years.
*  Palm in particular, and I just want to quickly layer these on
*  because I do think the intellectual history of this,
*  because it's so brief, it's worth kind of, you know,
*  highlighting the key chapters, which you did a great job of there.
*  We'll just add in a couple, you know, myself as well.
*  So the Palm model, 540 billion parameters.
*  I've always wanted to ask this question.
*  It seemed like there's maybe like parallel kind of research paths going on there
*  where if I had to interpret from the outside, it seemed like Google sort of saw 175
*  and was like, all right, we're going to do that one better.
*  And then at the same time, there was kind of the Chinchilla line of,
*  you know, research suggesting that maybe didn't even need all those parameters,
*  but they kind of both came out in a similar time frame.
*  Is that kind of what was going on in Google at the time?
*  Yeah, this is my personal opinion because I wasn't involved in both of those studies.
*  I think you are accurate and that's because we want to have these explorations, right?
*  And in terms of scale and what is optimal with respect to model size and data and
*  compute and everything. And I think both those studies were helpful, useful data points.
*  And that I think is influencing the next generation of these models that we are seeing
*  that are again, I think incredibly that seemed like more powerful than I guess.
*  So yeah, I think those explorations are both good and that's possible.
*  Let us basically say you have like swimming town, but researchers exploring all these avenues.
*  One highlight, by the way, from the Palm paper, I consider this to be one of the great sort of
*  buried leads in publishing history. There's a quote, I think it's on like, I've tweeted about
*  this thing, it's on like page 44 or something where it says, Palm outperforms the average human
*  on the big benchmark. And I was like, wow, you know, that's quite a claim to have sort of,
*  midway down this paper, not at the expert human level, we'll get to that, but already above the
*  average human level. I was watching this stuff very closely because I've been using open AI's
*  products extensively and really understanding them. And of course, everybody has this question of like,
*  is Google keeping up or they're behind? How does their stuff compare? So I was looking for these
*  little clues in the data coming across some of these gems. When Palm gets done, is it a matter
*  internally of Google of like, how does it work from there? Like there's been all these kind of
*  spin-off projects, right? You've got first, maybe more, not even necessarily a spin-off, but kind of
*  a continuation as Fawn Palm where we get to the instruction tuning. And then, you know, you've got
*  the med and the embodied, you know, for robotics. And is it, how much like infrastructure do you guys
*  get as like other product teams? Do you get a model that's kind of ready to be served up or
*  ready to be, you know, tinkered with in a way that like I as an open AI customer, you know,
*  convenient access, or are you wrangling like your own kind of server infrastructure, you know,
*  it's more like here's the weights, you know, good that you guys can, you know, do what you want to
*  do with it. Yeah, I can't really talk too much about the internal policies over here. And I think
*  it really is depending on which application I'm product team or whatever research that we're
*  doing over there on top of these models. One thing I would say is that the infrastructure is also
*  constantly evolving, ensuring that both training and influences are optimized for taking care of,
*  especially as we scale up these models on both sides, and they mean actually quite different
*  things. So the software is evolving, the hardware is also evolving, but on longer time scales.
*  So it's not a static thing that you take on and build, but rather probably get these set
*  up model weights and then these libraries and then you figure out, okay, what to how to make
*  best use of it. And then three months down the line, maybe you see something even better. And
*  then you figure out, okay, should I continue with this one that I've built on? Or do I transfer
*  everything that I've done onto this new system? That seems even more better and promising. And so
*  that's kind of the question that we angle with all the time. So,
*  all right, it's not something that I would say is static. And definitely,
*  that is true for the models themselves, but also the underlying infrastructure and everything that
*  we use for training models. Yeah, interesting. Everything kind of advances on all fronts. I feel
*  like whenever I say this to somebody who's involved with research in a very deep way,
*  they say, well, no, that's not quite true, but it always kind of feels to me like everything is
*  working. It just seems like people are putting out so many papers. There weren't that many times,
*  there's not that much time left for things that didn't work in the calendar, it seems almost.
*  I think sometimes I am surprised that the infrastructure, the way that it is put together.
*  There are a lot of amazing engineers at Google and legendary engineers who have been
*  with us for about 10, 15, 20 years. But sometimes I'm just surprised that this works because it
*  feels like sometimes it's just taped together and the system could crash and burn anytime.
*  So, that aspect is there. But I think the other advantage being
*  internal to Google, instead of being like a customer that is interacting with these models
*  through an API is that you get to see them at some point. And you can then go and deeply influence
*  it. So, you see the raw form. So, I think that helps quite a lot, especially in domains like
*  medicine, where you need that specialization because of the nature of the domain and the data
*  that you are using. So, perfect transition then to Flaunt Palm. So, that's the instruction tuned one.
*  If I understand correctly, no RLHF in that model, right? Just kind of example-based instruction
*  tuning. And yet, at the time, state-of-the-art performance on the US MLE medical licensing exam.
*  We've covered this a little bit over the last couple episodes, but could you maybe just give
*  us a little bit of a sense for what that exam is like? Who takes it? How do they study for it?
*  The kind of depth of knowledge that it requires and maybe what a passing score looks like on
*  an exam like that. So, I believe this exam, if you're training to be a medical doctor
*  and want to practice in the US, you need to pass this exam. And there are different steps
*  over here. And the kind of persons that we generally see is pretty large
*  veneer with some description, some it could be symptoms, it could be patient metadata,
*  it could be other necessary information. And then you will have to use that information with
*  anything else that you know and deduce and answer on reason and retrieve a proper knowledge and
*  then come up with a final answer that is required over here that often has considerable ambiguity
*  and sometimes to come with the right answer. You may have to do this process of elimination
*  because you have these multiple choice answers. So, I would say a good chunk of questions are
*  like that. Some of them are more direct where they basically test your knowledge retrieval.
*  I would say simpler. And these questions typically tend to occur in step one, although I may be wrong
*  over here because I think that's the easier one. So, I would say yeah these questions are quite
*  challenging for humans because they test a lot of different aspects, especially knowledge retrieval
*  and then reasoning and using. And at the point of time when we were building out these systems or
*  like evaluating these systems on these benchmark datasets, they seemed like a good challenge for
*  AI as well or the kind of models and AI systems that we had at that point of time given where the
*  scores were on these systems and given the abilities of these models. But now when I reflect
*  back on it, I do think that the kind of AI that we have today, the kind of intelligence that we
*  that it is, for that maybe this is not the best measure. And so probably need to think about
*  something else. Hey, we'll continue our interview in a moment after a word from our sponsors. I want
*  to tell you about my new interview show Upstream. Upstream is where I go deeper with some of the
*  world's most interesting thinkers to map the constellation of ideas that matter.
*  On the first season of Upstream, you'll hear from Mark Andreessen, David Sacks,
*  Balaji, Ezra Klein, Joe Lonsdale and more. Make sure to subscribe and check out the first episode
*  with A16Z's Mark Andreessen. The link is in the description. Omnike uses generative AI to enable
*  you to launch hundreds of thousands of ad iterations that actually work customized across all
*  platforms with the click of a button. I believe in Omnike so much that I invested in it and I
*  recommend you use it too. Use Cogrev to get a 10% discount. But regardless of that, I think this
*  was a very useful measure of progress and showing that these models can first reach passing score
*  and now reach performance close to the level of expert test takers. I think that's great. And so
*  when I say passing score, it's typically around 60%. And then when I say expert or test takers,
*  I think it's in the top quota, 85%-ish score. And one thing I would want to verify is we evaluate
*  this on a data set that has presentative USMLE style questions, but it's not actually
*  like an exam that we take from the board and then evaluate it on. So it's a representative data set.
*  I think you can roughly equate performance, but it's not the same as saying, well, this AI system
*  has passed USMLE. And so in our papers and all the media articles that have been written about it,
*  we've been very careful in saying that this is not equal to passing the USMLE. Rather,
*  representative questions is what I want to miss. Is that a step that you take to make sure you're
*  not seeing memorization sort of artifacts? Or why not just use the actual USMLE questions?
*  Yeah, I think it could be useful. But what we are maybe more interested in not passing the USMLE,
*  but rather in these models being actually useful in real-world clinical settings applications on
*  both news. Also, if you look at it both in the original Micron paper and the Micron paper that
*  you have, we've decided to focus on grounded use cases, which is what sort of questions
*  people who have medical information needs ask, typically in the context of search engines. And
*  we are trying to evaluate our systems and benchmark it against other LLMs as well as,
*  let's say, maybe physicians. So we want to be more use case grounded. And I think the USMLE,
*  this is my personal opinion. It was worked from a PR perspective to show that these AI systems can
*  get a lot of it. And it's got multiple other systems that have shown that. But that is not
*  necessarily a good indication of real-world utility, especially in medicine, the kind of
*  challenges that you face. Yeah, that makes sense. So it's essentially another example in the
*  increasingly long list of examples of benchmarks that, in this case, it's a human-focused benchmark
*  as opposed to an AI-focused benchmark. But nevertheless, it's sort of, while indicative,
*  falls short of a standard that is maybe more aligned or close to what is actually practically
*  useful. And as you start doing these deeper evaluations or start probing these models and
*  settings that are more reflective of real-world use cases, you start to see these gaps. I think
*  that was best reflected in the Met Palm paper where we showed that Zan Palm, the model that was
*  instruction fine-tuned using Palm, that did great on the USMLE instead of the other that kind of
*  time by a significant margin. But then as soon as we started giving it consumer medical style
*  questions and had that evaluated by re-inexpected physicians and also by non-expertly people,
*  we started seeing that there was several gaps on multiple different axes pertaining to
*  factuality, bias, reasoning, recall of knowledge, and even along axes such as utility and
*  helpfulness. And so it became very apparent to us that passing these benchmarks or getting
*  straight-of-the-art performance on these benchmarks, which are kind of narrow and limited,
*  is not the same as real-world utility and actual workforce. And I think the story, again,
*  kind of repeats itself with Met Palm 2 as well, where we're building on top of Palm 2. And that,
*  again, on a bunch of different benchmarks, the state-of-the-art M has been used in many different
*  applications already. And that's particularly impressive on Monteligro, DAS, code generation,
*  other stuff. But then when we do this side-by-side comparison with Palm 2, it's a great general
*  purpose model. And then Met Palm 2, which is fine-tuning specifically for use in the
*  medical domain, we see significant improvements again on all these axes and particularly on
*  evidence of like good medical reasoning or incorrect medical reasoning. We see this like
*  almost a 9x improvement once we do this fine-tuning. So that shows the importance of specialization
*  and also that shows the limitations of benchmarks that we are using.
*  General purpose systems, it's very hard to evaluate. Narrow systems, where the
*  use cases are well-defined and the intended use is very well-defined. It's much easier to evaluate.
*  But general purpose systems, I think you need to go deep into the intended use on the actual work.
*  Yeah, I think I would put that on a poster because that's definitely a big theme that keeps coming
*  up in all these conversations that I'm having and just my own work as well. Like,
*  validation of language models is really hard. GBT-4 is only preferred to 3.5 by like a 2 to 1 margin.
*  70-30 is what they report in the technical report. And so often, the sort of initial quantitative
*  measure that you might get, if you just look into the chain, just read through the chain of thought
*  that it's spitting out, you kind of realize that your initial take on the entire situation
*  was just kind of flawed. And I've seen that so many times. So you kind of alluded to it with
*  labels, but I wonder if you could just give a little bit more intuitive sense for,
*  okay, you've got this flan poem, it's instruction-tuned, it's basically hitting
*  better than ever USMLE performance or USMLE grade question performance,
*  but you're finding that these things are falling short. If I'm a user of that, how is that falling
*  short? And then from there, we can get into how you started to overcome that with the Medpalm
*  project specifically. At least with the Medpalm, one critical assumption that we know was that
*  given the palm model and the flan palm model were trained on internet-scale data, we assumed that
*  the knowledge required to kind of do well in the benchmarks that we were running on, and these
*  included these USMLE-style questions, but also the medical information, consumer medical questions,
*  and data sets as well. We assumed that the knowledge was already encoded in the weights
*  of the model. And so the challenge was to be able to prompt or elicit the right response from the
*  model given this domain, teach the model how to maybe reason more about it, think more critically,
*  do a better deduction and reasoning, think like a technician basically, if at all possible.
*  But the assumption was the knowledge was there. And the second thing was that we could
*  teach the model that sort of behavior without investing into a mystery. So that is what led
*  us to using the techniques that we ended up using, which I'm sure you want to talk about next,
*  which was instruction from Tim. So the goal was to basically, okay, you know everything that you
*  need to do over here. I'll tell you how to use that information to come up with the right answer and
*  move along with this process. I would definitely encourage everybody to look at, I've tweeted some
*  of these graphs and they're obviously in the papers, but I think you guys have done a really
*  nice job with both kind of the validation scheme conceptually and also some of the figures just
*  really make extremely clear what is going on. And that's something I think to be celebrated,
*  praised. I can still kind of picture the original Medpalm graph where it sort of shows
*  side by side the rate at which clinicians and Flanpalm and Medpalm in comparison kind of do
*  the right thing, so to speak, and then also like do something wrong. And so there's like multiple
*  different right things like retrieving the right information, demonstrating that you understand
*  the question, and then there's ways to get it wrong too, like have bad, recall bad information
*  or have something that's omitted that could have been important. So you've got kind of these
*  multiple ways to be successful and ways to be problematic. And I think it's just such an
*  important understanding for everyone that those are not mutually exclusive. So I really like about
*  that graph that they add up to more than 100%. And it's just so critical to kind of understand
*  that like these complicated responses, that's true for the doctors as well, right, as the AIs.
*  Everybody can be both kind of wrong and right at the same time. So I think that's really
*  important insight and very well captured in those graphs. So I guess I kind of,
*  the Medpalm paper sort of answers my original question in terms of like how, what kind of access
*  do you guys have? Because you are taking this very like data light approach. And I'm very curious
*  about how you understand the idea that like maybe few shot prompting couldn't work for this, it
*  didn't seem like it was going to get you where you want it to go. And so you ended up with this
*  soft prompt technique that I guess, first of all, I should just ask you to explain like what soft
*  prompting is, but it's amazing how little data requires. And I'm really interested to understand
*  that juxtaposition against few shot prompting. Yeah, before I go into that, I'll quickly say
*  I've created a lot of the illustrations and figures that we have in the Medpalm paper.
*  Dr. Shekhar Fierzi, who is one of the co-authors on Medpalm, is brilliant at this.
*  And then the evaluation rating and rubric is, it's just possible because we have
*  those amazing interdisciplinary team at Google and that allows us to like think critically
*  and holistically about this entire problem and actually get those settings and workflows. And
*  again, a lot of credit goes to Dr. Alan Karthi, who is also reasonably famous on Twitter. You don't
*  want me to say anything more than that. Yeah, and then going into what you actually asked about
*  which is soft prompts. Yeah, so again, just repeating what I said before, the assumption was
*  the knowledge was encoded or the knowledge that was needed was already encoded in the rates of the
*  model. And so it's more about teaching the model how to elicit out that information in the right
*  way and music wants to answer the question and then more stylistic aspects around like how to
*  convey that information. And for example, if you look at how clinicians respond to answers,
*  they wouldn't say something objectively. They wouldn't say, oh, you 100% have this or you 100%
*  don't have this. Rather, there will always be a degree of uncertainty that has been located.
*  You may have this, but you need to do this additional thing or you may have this, but I need
*  these follow-up tests or I need this additional information. And so if you want a model to be
*  used in such settings where you're providing medical information, you also want the model
*  to learn that behavior. And so that is, I think, somewhat orthogonal to having the knowledge.
*  So you can be like a very smart student and you can learn all these books about medicine and have
*  all that knowledge encoded in your brain. But then if you can't apply it in a way that's actually
*  useful, then that's no use. I would say there's no point in like, you know, studying all that
*  information and everything. And so the goal of the soft prompting at a high level was kind of like
*  doing two things. One is in this vast space of knowledge that is encoded in the weights
*  of the model, showing the light to which section of knowledge that we need to actually use.
*  So it's like, if you think about this parameter, the model knowledge space as like a huge library,
*  then this very specific section might be about medicine. And so like basically shining a light
*  on that and telling them, this is the information that we need to use. And then secondly, it is more
*  about the stylistic elements around like how to convey information, how to convey uncertainty,
*  and then how to ensure that your answer is more complete and there's less hubris in your answers,
*  maybe. And so those are the stylistic elements that I think we were trying to get at with like
*  a soft prompt conditioning. And to do that well, you need expert demonstrations. You want to be
*  able to learn that from actual relations and learn from how they actually write out these answers to
*  these medical questions when asked by patients and non-expertly users and so on and so forth.
*  So yeah, we work with our internal team. It was again a pretty diverse team from a bunch of
*  different countries, all expert trained, and then we collected responses from them, the styles in
*  which they would write out these responses to these questions. And then we use that to further
*  fine tune and align the model. But then the specific method of fine tuning, as you said,
*  was all this instruction prompt tuning where this is the soft prompt vector that we are
*  basically learning through gradient descent. And the nice thing about that is it does not necessarily
*  mean anything as in like these are not tokens corresponding to language words or anything,
*  but it's kind of in the same space. So it helps with the conditioning and anchoring
*  of the subsequent words that's generated over there. And yeah, because again, you're
*  like learning only like an order of a million parameters, it's very fast. And so, and it's also
*  very data efficient. So pretty much in a colab, as long as you have the right number of tips to train
*  like and the amount of data that we use, the amount of expert demonstrations that we used,
*  which was actually not that big in order for a few thousand examples, maybe even less than that,
*  actually. So once I put it in the paper, it took a few hours. And so it enabled like real fast
*  iteration over here. One of the other things that I would maybe very quickly point out is,
*  I think the ability to like perform well with only prompt tuning, that's also an emergent property
*  of scale. So we've seen that smaller models because they don't encode enough information
*  in their weights. They're also not that effective with prompt tuning, whereas larger models just
*  because they encode all that information. And what we actually need is guidance on how to
*  use that information appropriately. With prompt tuning, they become even more effective. And so
*  that's why we decided to use it. So a small amount of data, we wanted to move fast, so
*  like not be blocked on the compute. And then, yeah, that just made prompt tuning a very natural
*  strategy. That's fascinating. And I think you explained it well, but I just want to dwell on
*  it for a second more, because I think it is such a profound trend that kind of keeps popping up again.
*  And there's a couple of things I'm not super clear on, and I'm not great with like linear
*  algebra theory, but is this a... Let me just try to describe the setup. You tell me if I get it wrong.
*  So first of all, you've got flan palm, it's frozen. The whole block of it is not going to change
*  during this exercise, but you're going to fine tune instead just this very small auxiliary,
*  would you even call it a model? Is it ultimately like a prefix or is it a matrix that sort of
*  transforms the input? What is the nature of the way that the thing that you're learning interacts
*  with the runtime input? Yeah, it's more of a prefix to the hard prompt that comes up, or the
*  encoding of the hard prompt that comes up. And so essentially it does is a test conditioning and
*  anchoring, I would say, and that enables a few different kinds of transformations and we can
*  build that. But what it essentially does is like, as I again said, it doesn't impart any
*  net new knowledge to the model, but rather it just helps with this conditioning and teaching
*  the style of the domain. And so that is all what we need over here. And so that is what we all
*  worked with over here. And so, yeah, I mean, we debated this whether to call that a new model
*  or not, but the fact that you do have a million additional parameters and that actually bigger than
*  most models we were training even like two or four years back. You thought, I know it's okay,
*  it's fine. I mean, this model does have a new parameter, so let's just do it in the name.
*  I think that helped. Yeah, I mean, I think this idea has been around for a long period of time,
*  like adapter networks, even like things like film, for example, and vision and medical and like
*  visual question answering. The difference is where you're applying it and how you're applying
*  it. But the idea of like these adaptive rates and keeping like a big chosen model and using
*  that as conditioning has been around for a long time. Yeah, you mentioned the visual question
*  answering. We had the authors of Blip, Blip 2, and most recently Instruct Blip to talk about that. And
*  that was probably the first place where I really started to see how powerful and kind of generally
*  applicable this is likely to be. This is another great example. So the setup is you've got your full
*  Flan Palm frozen model. Now you're running a small number of examples. Does the paper say,
*  are we talking like double digit number of examples? Like how few are we talking here?
*  I think it's low triple digits. The scores that we reported in the paper,
*  actually just trained using multiple digits. So that's insane in and of itself. It's pretty small.
*  I mean, it's also not insane. It is consistent with, it's insane and it's consistent with
*  stuff that I've seen too, like just fine tuning as a retail customer of open AI.
*  You don't often need, or often you don't need like that many samples. I think they recommend 500 is
*  kind of a starting point. So it's pretty consistent with that general guidance.
*  You're now setting up prompts and expert written, grade A, best you can find examples.
*  And then just doing a pure still next token prediction loss function and just modifying
*  like this prefix instead of modifying the whole model, just this sort of prefix, which exists
*  in the language embedding space, if I understand correctly. And so in that sense, we can sort of
*  think of it as like, we have, you know, it should be meaningful to us in some way,
*  like language is meaningful, although it's this sort of like dark region of this space that we
*  can't actually directly access with language. I think that is spot on. So you have these
*  prefix tokens and representation that is in the language space. And then we just have that and
*  then have the representation of the hard tokens and together. So I would think about these soft
*  tokens as more abstract condition. And then those hard tokens are instructions that you have as more
*  hard constraints on the model as to what will generate next. And together.
*  One other way to think about this is I think these soft prompts, they kind of give you a
*  general idea of how to answer, whereas the instruction for the guidance specific question
*  or that context gives you a more specific and detailed instruction that is. So it's a combination
*  of a general instruction and a very specific instruction. And you use that together to come
*  up with a final answer. I think you raise a very good point. And I think if I were to have a little
*  bit more time, that's what I would be spending my time on, which is to see what is there even a human
*  interpretable notion of what is actually being learned in the soft prompt vectors. We haven't had much time
*  to do that study, but I think if we can see, okay, like are there some clusters emerging over here
*  in these vectors that we can anchor with specific tokens in language? And if they are interpretable,
*  I think that'll be amazing. Or if someone who's going to listen to this and they want to do this,
*  this might be different from what we heard from the blip squad. It didn't sound like they found
*  much there that was, and I don't necessarily know how harder exhaustively they looked either,
*  because they've been busy publishing paper after paper too. But at least the preliminary
*  exploration that they did, it did not sound like they found anything where they were able to say,
*  in their case, it's image. So if a picture is worth a thousand words, they were not able to
*  give me the thousand words that the picture represented. So one thing I hadn't maybe
*  understood there is, so there's the soft prompt that's the general some sort of position
*  in language space that we can't access directly through words. But two things, like that's followed
*  by explicit instructions, like answer this question in such and such a way. Okay, that's interesting.
*  So it's not a substitute, it's an and. Okay. And then all that is ultimately interpreted by the
*  model as language, right? There's no separation really between how that's then processed through
*  the layers of the model. There is a difference. I think that is interesting. I think image domain
*  is a little bit harder to understand explorations. I think in language, there's a possibility that
*  we'll have something interesting. Again, even if you don't end up finding that's also fine.
*  I think we have at least that in the surface in terms of understanding how these models work.
*  I wonder, you probably didn't have time to do this either, but I wonder if there could be like a
*  curriculum sort of approach to this, where you might have like multiple soft prompt prefixes that
*  are like bedside manner, you know, upgrade, you know, relative to like clinical, you know,
*  detail upgrade, anything like that explored? I don't want to say too much, but that would be
*  there in some upcoming work. It's not directly using soft form vectors because in Metmum 2,
*  we kind of moved away from that. And primarily that comes down to having a more compute-optimum
*  model and having more data. But we are exploring that direction in a slightly different manner,
*  which enables us to control the outputs of these models according to the different axes that you
*  talked about over here, bedside manners, factuality, safety and other stuff. But it's more dynamic and
*  at runtime, or we're definitely doing that because as you can imagine, you may want to have that
*  control and different end users may want to like, you know, have different outputs on the one of
*  them. So they may want to like, you know, a button or a knob that you can change and you're
*  giving it slightly different responses. You want to give that control to users. Yeah. Exploring the
*  latent space of text with these sort of abstract, well, it sounds like you're doing it a little
*  differently, but yeah, very interesting. Layperson evaluation. That was the other thing that I wanted
*  to get into. I think there's everything that's old is new again. Like, you know,
*  if language models in like 2020, 2021, we're sort of, you know, international contractors,
*  you know, picking A versus B. And now we've kind of shifted dramatically up market from what I
*  understand with like scale AI has, you know, dozens of PhD, you know, evaluator positions on
*  their website last day checked. You also have like the, you know, expert evaluator, but then
*  you circle back to the layperson evaluation. So tell me what you learned from what motivated that
*  and what you learned from that. I think it's helpful to think about LLM's platform technologies
*  having a spectrum of use cases. And that means spectrum of end users or, yeah, would be interacting
*  with the model in very different ways. And even in medicine and life sciences, you may end up having
*  not just doctors and clinicians, but also like people who are maybe more on the administrator
*  side, or maybe more people who are medical researchers or life sciences researchers.
*  And then definitely non-expert lay users who are simply searching for medical information online.
*  They maybe typically do it a search engine and they may want to do the same with
*  or a last language model as well. So when you're doing these evaluations and,
*  and if you look at question answering itself, it's just a very broad topic and anything pretty
*  much can be framed as an instruction slash question and then answer rate. And so that basically
*  subsumes any test. You want to try to cover as many evaluations as possible. And we thought one of the
*  most important applications would be where you directly have these models interacting with end
*  users for their medical information needs. And this is a little bit of my own personal opinion,
*  or, but for me personally, and then for a lot of us in the MedFarm team, access to health care
*  metals a lot. I personally grew up in parts of India, going to see a doctor from most people
*  in the nearby towns and villages with me, you know, walking 30 miles in extreme heat or giving
*  up on a day's wages, going without food. And so that was simply not an option for many people.
*  And that would in turn mean many people would actually go their entire lifetimes without seeing
*  a doctor. And that in turn meant like adverse, even succumbed over a lifetime and in turn
*  translated to that, you know, lower life experiences, all sorts of things. But now with
*  these technologies and the arc of progress over here in technology and AI in particular,
*  we can now start imagining like a pocket world class, or general public general practitioner,
*  or that is scaled up to billions of people and in turn helps us make space
*  like mobile test object everyone. And so this for me personally has been a dream for a long
*  period of time or like my undergraduate thesis back in 2013 was an app called last doctor anytime
*  anywhere and that was reducing non deep learning technologies did not work really well. But now I
*  feel like we can realistically start thinking about like really putting a word class
*  general practitioner into the pockets of like millions of people worried about and so on the
*  medical information needs. So that kind of is the, I would say, the subtext of this evaluation,
*  although the other people, this is mostly my personal opinion and other people in that different
*  take over here. But the fact remains that non expert users are going to be interacting with
*  these systems. And one aspect that we have seen is the more you know, the more you generally
*  tend to get out of these systems. And sometimes the less you know, the more harmful or unsafe
*  these systems. So you want to ensure that when people who are not experts are exposed to these
*  systems, it doesn't act in a way that affects their well being or whatever. So that is kind
*  of the underlying subtext of this evaluation. And so we wanted to directly understand from such people
*  who are looking for medical information, whether they found it useful,
*  useful, directly addressing the intent of what they were getting at. The interaction was useful
*  at all or not. And I would say we were barely stretching the surface over here. There's a lot
*  more to be done. But I think padding that sort of evaluation without some experts on axes around
*  like factuality, medical reasoning bias, I think that's going to help us get where we want to. But
*  again, very early days over here, a lot more studies on the way better evaluation.
*  I love the vision of that too. It's the simplest one I find to just come back to always when people
*  are like, you know, why don't we just forget about this AI stuff? Or you know, isn't it going to be
*  more trouble than it's worth? I'm like, I think the people that don't have access to doctors are
*  really going to want to have a word about that. And by no means my you know, regular listeners
*  will know that I have my deeply held concerns about the general AI future. But that is such
*  an incredible promise that I really want to keep my eye on the ball with that as well.
*  So in this process, I can imagine you could run it different ways, right? You could run it in,
*  for one thing, multiple languages. You know, your background, obviously, I'm sure
*  you know, multiple languages would be a critical component to actual deployment. And then I can
*  also imagine like, asking laypeople to just evaluate outputs, versus kind of giving them
*  some ability to like interact with the system, phrase the questions in their own way, maybe even
*  have like multi turn interactions. Yeah, tell me a little just a little bit more about how you kind
*  of approach that in terms of the languages and sort of how, you know, how much the individuals
*  actually got to kind of explore. So I think the evaluation was kind of informed by the capabilities
*  of modern and automatic palm paper. And if you look at it, palm wasn't necessarily optimized for
*  multilingual applications, whereas palm 2 has been a step change on that phone.
*  Also, all the evaluation so that I show that. And then again, with respect to interactions and
*  multi-term conversations, palm wasn't optimized for that. That's more the Lambda system.
*  Yeah, Lambda actually does impressively well on those things, but we were building on that system,
*  format palm. So yeah, I would say basically the capabilities of those systems and the desire to
*  keep the evaluation simple and scalable while giving us enough data. That's what I think
*  informed the process that we made. But I think as we are improving the capabilities of the systems
*  to interact, engage in dialogue, answer questions in different languages, and all that is coming
*  very rapidly. And yeah, it's just that for the first version of the paper, we wanted to keep that
*  simple and not have any feature keep, which as you know, can take down many conflicts.
*  But now as we are opening up these models more broadly, or hopefully with different kinds of
*  collaborators in academic settings and medical research settings, we can do these studies as well
*  and understand the capabilities of the limitations of these systems.
*  So that's a perfect transition, I think, to palm 2 and MedPalm 2. And just as a quick refresher too,
*  the timeline on all of this is just insane, right? Palm, if I remember correctly,
*  first paper was April of last year, April 2022. And then Flandre Palm is maybe like August,
*  September-ish 2022. You then follow up with MedPalm in December of 2022. And then now we're in
*  the middle of the year, and then Palm 2 and MedPalm 2 announced like whatever a month ago,
*  and kind of paper just released on the archive server this week. So ever so slightly over a
*  year from kind of first announcement to this announcement, which just everybody should
*  ponder that for a minute, definitely didn't take long. So you kind of, if I understand correctly,
*  there's a new base model is essentially the core shift. And then it sounds like you've also,
*  though, shifted your methods. You said it is not, I don't have any insider information,
*  but it certainly sounds like it's probably fewer parameters, more intensive training,
*  that obviously leads to more efficient inference. And then that opened up different techniques. So
*  can you tell us about the different technique that you use to customize to the medical domain
*  this time around? Yeah. Again, without too many details over here, the fact that this model was
*  maybe more compute-optimal and allowed us to go into and find training more efficiently,
*  or we just decided to go with that one. And coupled with the fact that we now have a little
*  bit more data, not a lot more data. I mean, if you still look at it, or like MedPalm,
*  they were using mostly the Genesys, and then again, the expert demonstration set
*  numbers in a few hundred. So it's just the order of a million tokens, not that big, but
*  just the fact that now you have a more efficient model that you can value with, we decided to do
*  fine-tuning and update all the weights of the model. So I think that is basically the key difference
*  switching over to a more powerful base learning and then doing this end-to-end fine-tuning because
*  the model is all simply more efficient to train and find you. And so the output of this is
*  amazing. I mean, you've got now 85% accuracy on the same question set right then. This is
*  the USMLE-like questions, which is basically expert level. We don't have too many people that
*  can outperform that, if I understand correctly. Yeah, I think that's likely in the top corner of
*  doctors that take these tests. But again, I would say we should not anchor too much on this.
*  I think by now we should not be surprised that these models are solving these tasks or these
*  questions as well as they are right now. One hypothesis that has been there in the community
*  for a while, and I mentioned that on Twitter, is whether these questions or these benchmarks are
*  contaminated in the training data. So that was a concern for us because if that's the case,
*  then these are definitely not a true measure of progress. And so we explicitly spent time to see
*  how much overlap there is. And so it was not done in a hand-wavy manner with some other papers I've
*  done. And there is definitely some overlap, but it's a very small percentage and for most data
*  searches, less than 10%. And then the performance difference between
*  performance on the data with overlap and without overlap is, I would generally say not statistically
*  significant. So that was reassuring in the sense that this is not simply a case-in-the-all
*  memorization, but rather there is something more powerful emerging in these models. So that is great.
*  So that is definitely one measure of progress. But as I keep saying,
*  that is not the end goal over here. The end goal is real-world data availability. And for that,
*  we need extensive validation in real-world applications and workers. Well, we're not at the
*  end of your validation effort just yet, but maybe before getting to that, do you have a sense for how
*  much performance boost there is from say, for example, if we just had Palm 2, let's say we had
*  Palm 2 and we just used our best prompt engineering versus like, I don't know, you didn't ultimately
*  go with the soft prompt approach for MedPalm 2, but versus a soft prompt approach versus a full
*  end-to-end fine tuning approach. How much difference does that make? Can you quantify that?
*  Yeah, I think this has been the subject of quite a bit of debate, whether you can take a model,
*  large LLMs such as GPT-4 or Palm 2 or other books, and then use them with simple prompting strategies,
*  or do you need some specialization? And I would like to think anytime you do gradient descent and
*  update parameters, that is specialization. And so whether you use prompt tuning or prompt tuning,
*  those are both in the same category for me personally. So that has been like some sort of
*  recurring debate, both internally, but also with some folks that are really now in respect to
*  OpenAI and Microsoft. And our take and my take over here has been that you would benefit a lot
*  from fine tuning. And that again comes across not on these benchmarks, because as you can see,
*  GPT-4 with simple prompting performs really well. Palm 2 performs really well. But then when you
*  start doing these real-world evaluations and this multifactorial evaluation, that you granularly
*  check actuality, possibility of bias and harm, evidence of recall, reasoning, and all those
*  aspects over there, that is when using the gaps. And so even if you have a very general purpose
*  model that seemingly has all the knowledge in the world, it may not necessarily know how to act in
*  settings and real-world application scenarios and so on and so forth. This effort came across as a
*  brain moonshot program. So moonshots are basically a program where it's a more bottom-up thing,
*  where a group of researchers across the company, across Alphabet, all kind of think, oh, this
*  thing should exist in the world. And then they come together to build it up. And so that's why
*  if you see the team is an interdisciplinary team spanning health, AI, brain, deep mind,
*  and other research organizations at Alphabet. And the thesis we had that these models such as
*  Palm 2 and other vision models or foundation models, they are very strong building blocks.
*  They have general reasoning capabilities and they have a lot of knowledge encoded in them just
*  because of the state of data that they are trained on. But now the next step that is needed before
*  they are really applied in medicine and in clinical settings is sending them to medical school.
*  And that means not just training them on specialized medical data and purposes, but also
*  exposing them to real-world interactions in settings and allowing them to learn from feedback.
*  And so that was the tagline of this moonshot, sending foundation models to medical school.
*  And so that is how medical school works. And so that's how we can build a model.
*  MedPalm 2 and other models that we will soon have or has emerged. And so the core idea of the core
*  thesis over there is you can have a general purpose model such as Palm 2 or Z54 that has
*  very strong intelligence similar to a human. I mean, we are generally intelligent. We can
*  pretty much learn anything that we want to. But without that specialization or years of training,
*  you don't actually get good at it. And medicine is a very specialized endeavor. And so you need to
*  spend time learning about the domain, the etiquettes, the safety, the nuances, and how
*  to interact with fellow doctors and the patients and other people in this setting. And so that
*  requires specialization. And so fine-tuning is one sort of specialization over here. And that's how
*  you should think about it. But then there are other ways to do the specialization.
*  RLHF could be one way, but then there are others that you can do. So that is the core thesis that
*  we have. You can have a very strong general purpose system, but that's not enough. You need
*  this expert specialization, especially in this domain. So again, the results are pretty arresting.
*  And I've just got the graph up here again from the most recent paper. Another outstanding
*  graph, I would say. Two parts. One just shows, again, the up and to the right curve of going back
*  to just two and a half years ago in December 2020 when GPT-Neo was the best on this US MLE
*  style question with 33.3%. And then it's just up and to the right until the point where Medpalm 2
*  is at 86.5% expert level. But then on the other side of this graph, it's a comparison between
*  really showing the share. You've got nine evaluation dimensions. And for each of these
*  evaluation dimensions, it shows how often is Medpalm 2 preferred, how often is the human
*  physician response preferred, and then how often is it evaluated as a tie. And you've got Medpalm
*  preferred to the physician in eight of nine dimensions. And just eyeballing the thing,
*  to me, it really looks like seven of those nine dimensions are pretty clear cut for Medpalm 2.
*  I should say Medpalm 2. It's not that close. So those dimensions are better reflex consensus,
*  better reading comprehension, better knowledge recall, better reasoning. All four of those.
*  We're talking, let's say, an average of 70% of the time Medpalm 2 is preferred. That's a way bigger
*  and then 10 to 20% of the time is a tie and only 10% of the time you have the physician preferred.
*  That's a way bigger ratio just for comparison in terms of preference than GPT-4 has to GPT-3.5.
*  So it's a substantial difference. I'm always shocked by how close those ratios are. GPT-4 right now
*  versus Claude V1.3 is like six to four. It's even a little bit closer. So in general, we're seeing
*  not huge ratios. This ratio of seven to one with two going to tie across all those core dimensions
*  is a big deal. You don't want to over anchor on it, but I'm starting to anchor on it when I see
*  these kinds of graphs. And then the other five just for completeness. The one that the physicians
*  are preferred on is having how often do they have inaccurate or irrelevant information. Medpalm 2 is
*  judged to commit that mistake a bit more often than the doctors, but then omits information.
*  Medpalm 2 dramatically preferred extent of possible harm. Again, Medpalm 2 dramatically
*  preferred likelihood of harm. Again, Medpalm 2 dramatically preferred. And then finally a tie
*  basically on evidence of demographic bias. So that is a big deal. I guess to bottom line all of that,
*  in the original Medpalm paper, there's this line that says, it's still Medpalm still remains
*  inferior to clinicians. And as I look at this chart, I'm like, is that statement still true?
*  Or do we now have to kind of reckon with the fact that like, this appears to not really be
*  inferior to clinicians, at least on this, you know, question answering domain. I think the
*  qualified that you added at the end, at least in this question, answering domain in this data set,
*  this setup, that is what we observe. But I would still like to think that generally,
*  despite all the progress, these models are not saturated to be used autonomously. We should still
*  have expert divisions and norms. And I think there are limitations of this physician
*  response generation as well, because if you think about how physicians produce answers, right,
*  or they are biased towards delivering information in a succinct or manner, because they generally
*  just constrain for time. So in that sense, I think that bias might be creeping in. And so
*  in additional studies, what we want to do is be more deliberate. So in this one, we were deliberate
*  and we did ask our physicians to use whatever sources of information that they thought was
*  necessary. But even then, I think this natural bias might be there. And so we're trying to
*  remove that confounder and the additional evaluations that we hope to do soon, where
*  we want physicians to be the best possible version and also explain the situation as to how
*  their answers might be used or how the model answers might be used. So while, I mean, these
*  results are great, I think there are these limitations. And so I wanted to call that out.
*  And I think that requires further validation. But to me, what this shows is even though these
*  systems are maybe not yet ready for use without any sort of supervision by expert humans in the
*  loop, they could actually be already very valuable in terms of augmenting our clinicians and doctors.
*  So you can imagine these e-concert scenarios where doctors produce the gist of the response
*  to patient query. And then these models kind of like come in and complete it and make it more
*  their user-friendly, like extreme terms that maybe they're still to pass. And so those kind
*  of things, for example, I think these models might already be ready. And that could again have like
*  a pretty big impact. And more broadly, the way to think about these things is cases where it's easy
*  to verify the solution. I think by an expert human, I think that is where these models will,
*  I think, immediately shine. And as long as they verify, that verification doesn't take most time.
*  So if the model produces something, instead of you as a doctor having to write out that entire
*  thing, you kind of just edit and correct the model that is necessary. And hopefully that brings down
*  the time for you to generate the documentation from like 10 minutes to two minutes along with
*  the model. So I think those are the scenarios that we are immediately looking for. But as you can,
*  as you are saying, it's hard not to be excited because the trends are kind of like obvious
*  in terms of being able to do more autonomously. But I would still like to think that two things.
*  I think for the foreseeable future and parts where there's maybe not really a shortage of doctors,
*  I think these systems are going to be like a co-doctor, which is going to maybe listen
*  into conversations and look at the information that got out of the patient more holistically,
*  maybe interpret information such as genomics, for example, which most doctors don't understand
*  really yet, and then surface information. And then the doctor ultimately decides how to use
*  that information or to help the patient at hand. So I still think that is actually going to be the
*  scenario for the foreseeable future. But then as I had a year before, there are parts of the world
*  where billions of people have medical information needs. And right now the standard of care is
*  like nothing. And so we can instantly do something pretty profound over there. But
*  I think that again requires responsible innovation validation before we get over there. I don't think
*  we can just go out there and just acquire these systems. I think there's still a lot more work to
*  do. I definitely want to come back to the commercial path that you're really now beginning on. And
*  it's amazing again, just how fast this has all happened. But maybe as a bridge to that too,
*  my qualifier in this question answering domain, the obvious next step that's maybe the busiest
*  trend in AI right now would then be multimodality. And so what is Palm2 promised for us there? And
*  do we think that we're headed for MedPalm2 plus or whatever that can sort of
*  ingest like scan data or look at images of wounds? It seems like this has got to be the next frontier.
*  Right? Yeah. Again, I don't want to give too much over here, but that's kind of obvious. Medicine as
*  an endeavor is inherently multimodal. All the data that we are dealing with, it's non-testing
*  language and text format, but lab records, EHR, scans and images, genomics data.
*  And I think one of the most interesting trends that maybe people don't appreciate enough is
*  biology and medicine is kind of like the largest data generating flywheel on Earth today. And
*  that is higher than pretty much any other domain. And I think the implications of that are quite
*  profound because here that means the most obvious way to make use of that data is through AI because
*  no human is going to be able to do. I think we kind of like gave up on that dream like 10, 15 years
*  back. So it's not even true, but like we need AI to make sense of all the data for us. And I think
*  it's going to enable two things. One is as you start integrating this data, it's clear. And all
*  this is going to be multimodal data. I think a lot of different hypotheses are going to emerge in
*  terms of our understanding of human diseases or disease mechanisms or what sort of or how to do
*  like biomarkers and diagnosis and what sort of threat you're taking to actually supply.
*  So there's going to be fundamental bio-medical discovery that that is going to enable as we
*  start doing this next year. And then the second thing is you're going to leverage that with these
*  systems to really scale up precision medicine to billions worldwide. That just seems like an
*  inevitability at this point of time. So I do believe that we are at this very early stage of
*  an exponential curve over here in bio-life sciences and medicine. And the end goal over here is just
*  precision medicine at scale. And beyond that is just simply advancing the human potential and the
*  kind of things that you gain. And that's probably all going to happen within 15, 20 years, although
*  in the next few years it's going to be interesting how this goes out.
*  Yeah, 15, 20 years seems like a long time given the December 2022 present graph in the current paper.
*  Do you think there are any fundamental breakthroughs required to achieve this
*  vision? Like when I scan the landscape, I'm sort of like all this soft prompting stuff, all this
*  multimodal injection, going back to the Flamingo paper and a million other things, Blip 2,
*  Face Meta's recent ImageBind release with five, seven different modalities just in the last couple
*  weeks. It doesn't seem to me like we're really missing any key pieces to get to the point where
*  the systems really should work. That's not to diminish the amount of actual field testing,
*  rough spot identification and sanding down. My company Waymark, we make video scripts for small
*  business commercials and we still find plenty of rough spots to stand down. So I appreciate the
*  fact that you're dealing with a thousand X bigger and maybe 10,000 X bigger and
*  you know, thousand X more critical domain than we are. And there's probably a correspondingly
*  million times as many rough spots. But when we find those rough spots, we sand them down and then
*  that pretty much does work. We patch training data, we sort of do a variety of different things like
*  tweak our instructions, and we basically can get over most of the problems that we have.
*  Do you think that we're basically there subject to sort of refinement, engineering,
*  validation, you know, field testing and like deployment? Or do you see conceptual things that
*  feel like they're not yet there? I think it depends on what you exactly want from those systems.
*  If you want like human style intelligence, I don't think we understand human intelligence well enough.
*  And so these models are not going to be that. But I think these models are fundamentally a very
*  different kind of intelligence. And that means the kind of things that they do is also different
*  from what we do. It is their ability to actually deal with information at scale. And if you're
*  thinking about that, so I think other people have just mentioned this, right? I think once you,
*  so people have said this, like these models are simultaneously smarter than us and dumber than us.
*  And I think that just is because this is a different kind of intelligence. And so if you're
*  okay with that, and thinking about how to use that intelligence to augment us in our pursuits
*  and endeavors, whether that's in medicine, whether that's in science, then I think most of the
*  components do already exist. I would still say there are some technical challenges for sure that
*  as in as in when we train these models across modalities, we see, or like for example, even
*  combining vision and language, I do get a sense that our language models have become very, very
*  powerful. That is kind of obvious with GPT-4. But the vision models, although there's been some
*  really incredible breakthroughs with the Meta segment and a bunch of other stuff on the way,
*  I maybe get a sense that despite scaling both the model and the data, we are maybe not there yet.
*  It's not that powerful and that becomes more apparent in medical settings when we are dealing
*  with these scans where to interpret them accurately, it's like finding a needle in a haystack.
*  So your representations have to be kind of like really spot on. And then again, the volume of
*  information that you are dealing with is also much bigger. And that has implications on the size of
*  the model as well. And then I'm just talking about vision and language over here. Now you think about
*  fundamentally completely different modality. And if you want to model that separately and well,
*  again, you have to deal with the architectural choices, the encoding choices that you make over
*  there. Same with genomics, it's very different. So there's a combinatorial explosion that happens
*  when you start modeling and try to think about optimal encodings for these different modalities.
*  And I would say while we kind of have a good space of solutions to explore, we haven't arrived at the
*  right design choices yet. And I think that is going to take quite a bit of exploration in the
*  next year, year, maybe two years to get over there. And I think the second thing is also generally
*  around this architecture. There is, I think, this question of whether do you want to throw
*  everything at this one single model that can process pretty much anything? Or do you want to
*  maybe compress that model down and have a lot of specialist models that you can folk off to,
*  to form a study maybe and train these systems. And I think there have been
*  illustrations of that, like hugging is has something. So we still don't know the trade
*  off over there. I don't think anyone has done a comparative study. So I think those two places
*  for me, it still seems right for exploration and research. As you said, I feel like if we accept
*  that we're not looking for human-style intelligence, but like something more complementary,
*  that is going to make sense of all this data at scale for us, then I do think most of the building
*  blocks are there for us. And we will find out pretty soon if it's enough or not. But I do think
*  that once we get this right, it's going to be very useful. So then let's talk a little bit about kind
*  of a business plan. With this last Google IO, there's now the notion of Medpalm API. And I
*  understand that this is available on a limited basis right now to kind of trusted testers and
*  researchers in the academic community. Can you tell us what it is? Are we now in a multilingual
*  chat style modality that these folks can start to explore? No, I think the model is still optimized
*  for mostly single term use cases and settings. So we've done development of Medpalm with certain
*  applications in mind. But as I said before, this is a platform technology. And I think once you
*  give access to people, they're going to find creating those cases of it. And so that is kind
*  of the goal. But then again, it's important to do this responsibly, because we know that these
*  systems can be useful or not useful depending on the end user. So you want to do this in a setting
*  where this feels safe. So that is why we're having this trusted test program or cloud where
*  we are exposing it to a bunch of people with spectrum of use cases in the medicine and life
*  census domain and hoping to gather more feedback. And we'll use that feedback to iterate and enter.
*  And hopefully it gets to a stage where we feel it's safe enough to more broadly expose the system.
*  But I think the value proposition is very clear and the opportunity is very clear.
*  Hopefully if things go well, all that happens. Yeah, I guess is there a vision of like a consumer
*  product? I mean, it sounds pretty straightforward to imagine. Not straightforward, but I imagine
*  there will be no shortage of people who need to process medical data for medical systems or for
*  insurance companies or all that kind of stuff is going to be probably less controversial,
*  easy to attach revenue to and just like pure everybody's going to win. Or it seems like things
*  might get a little bit more controversial at a minimum would be an actual consumer facing
*  application. And then a theme we've heard a couple of times, or maybe if it's a theme, but certainly
*  a theme of speculation anyway, is that there may be some sort of leapfrog type dynamics
*  because maybe you can't or you don't want to deploy something like this direct to consumer in
*  the US. But maybe for very good reasons, you might want to do it in your hometown in India where
*  it's kind of this or nothing. So how would you kind of sketch that path forward for us?
*  Yeah, I really don't know if I have all the answers over here to be honest. I think we all see
*  the potential for this technology. And I think we all agree that there's a spectrum of these cases.
*  And some of them are obvious where we can deploy into workflows and settings where there's not much
*  risk involved. And the upside is very clear and obvious. And that's going to have a lot of impact.
*  So these workforce style settings, documentation, generation and everything, I think that's going
*  to happen very, very fast. The middle ground is mostly going to be scenarios where you do actually
*  have an expert in the loop or that you can fall back into. But even that scenario, I think would
*  need verification, validation, evaluation studies, or data sufficiently well powered
*  before we can start doing that. But again, that is I think going to happen
*  fairly rapidly. There is more shortage of interest from folks in the healthcare,
*  medicine, to do these kind of studies. Yeah, the last application that you mentioned,
*  like direct to consumers. Yeah, I think that is the one that I am maybe less clear on. Honestly,
*  it could go anywhere over here. And there's again, my personal thing, but I'm pretty sure people are
*  already using GPT-4 for medical information needs. And so the genie is kind of like already out of
*  the border. And so it's unclear to me whether there's going to be a clampdown over it or whether
*  there's going to be some other form of regulation that comes in. I think we're going to find out
*  very soon. There's a lot of discussions and noise happening. The value prop is clear. I just don't
*  know who does it and where and how. That is a good question. Yeah. Well, Google is quickly coming out
*  of its shell in this space and certainly seems like you guys are going to make a big impact along
*  with a couple of others, obviously, who are helping lead the way. But the quality of this work is
*  obviously extremely high. One kind of random question I want to sneak in before the end,
*  and then I've got just kind of a couple closers for you. And I appreciate all the time. This has
*  been extremely illuminating and fun for me. But there's been some debate a little bit lately
*  around narrow, more trusted data sets versus these sort of super broad data sets. I just saw a company
*  launched in the last few days that says that they train only on the kind of trusted data that they're
*  able to license or partner for. And my implications seem to suggest that pre-training on the internet,
*  you learn all this crap, some of it's wrong, that could be a problem. That kind of rings
*  plausibly true to me. But then I also wonder, and I was talking to our last guest on the show,
*  Neil Kostel, about this. It seems like there is also some sort of inherent breadth to medicine or
*  like just deeply contextual nature. So examples that he gave were like, if a patient says they
*  eat cereal, that probably also means they consumed milk. And if you don't have that kind of general
*  common sense, you may struggle. Or very Silicon Valley take, but he was like, if the patient said
*  they went to Burning Man, they probably inhaled a bunch of dust. And you might want to know that.
*  As you're trying to engage with them. So do you have a point of view on that? Like this general
*  pre-training does seem like it may have pros and cons. What do you think? So I think it goes back
*  to how we did this work. We did not decide to initialize our language model from scratch and
*  training only on medical domain data. And the reason for this is the fact that I've been training
*  on internet-scaling data, even though that objective seems very simple at a high level,
*  by doing this at this scale, you are basically inputting a very complex multitask objective
*  over here. And so that means to do well on this task and predict next words accurately. You need
*  to not only understand syntax and semantics, but also medicine, physics, biology, chemistry,
*  and everything. And so as a result of doing that and with models that have sufficient number of
*  parameters and good enough architecture, we do see emergence of these reasoning capabilities
*  in these models. And so you want to build on top of that substrate. It's clear that as you do that,
*  pre-training becomes important as well. And you can get a quality is important and you can,
*  I think, filter out a lot of the stuff that we think of as toxic or harmful and still end up
*  with a sufficient number of tokens where you can train these models. But it's not a perfect process.
*  But I would say that you do need that to have this emergence of reasoning and
*  common sense reasoning in these models. And that is the substrate that you want to build on top of.
*  And for example, even engaging in dialogue and conversations. If you're training purely on
*  biomedical text or scientific text, I don't think you're going to be able to have a normal
*  conversation with an end user who's looking for a very simplified explanation of terms. You're
*  probably going to talk to a scientist who only understands complex terms and that's going to be
*  useful for, not going to be useful at all for an end user. So you want to build on top of the
*  scale of things. And then the second thing about medicine is the fact that I think we should not
*  underestimate the power of the internet scale data and the amount of information that is in
*  COVID-19. So if you're looking for rare diseases, conditions, symptoms, it's very likely that someone
*  somewhere would have posted about it on some social media forum. And so I think it's useful
*  to have that indexed and represented some way or another. And then the challenge is, okay, how do I
*  elicit out that information when needed, given the context? So that is how all this work on fine
*  tuning and alignment and everything actually here. But I generally do believe, and this is not just
*  true with last language models, but over a period of four years that I've been working on medicine
*  and health, we have seen that as you scale up these models with more diverse data, the reliability
*  of these systems improve, the calibration improves, the auto-distribution performance improves, and
*  we've done very rigorous studies in many different modalities, imaging, records, and now last language
*  models. And the alternative of not training on internet scale data is small scale data sets.
*  And that is by definition biased. That is not going to perform well when you take it to a new
*  setting where it has not seen that kind of data before. So I think this is absolutely critical.
*  But then the work on alignment and ensuring that the model is performing in a safe manner is also
*  critical. AI tools that you like, like products that you would recommend that the audience check
*  out, what are you using? Yeah, I think this is where, since because I am so close up within
*  the Google ecosystem, I don't actually get a lot of exposure to other AI
*  tools necessarily. So my response is not going to be great over here, but I do enjoy these new apps
*  that can do this new like avatar generation, stuff with images and all those things. I think that is
*  in the industry. I would also give, put in a plug for music in them or in ULM from Google that can
*  do interesting stuff. Oh, you can have everything on with it and it doesn't lose a place. And
*  as someone who has had a keen interest in music, but is not particularly skilled at it, I find
*  those sort of tools to be, they can have potential in like allowing me to explore the space more
*  broadly. I was just, got my hands on that for the first time earlier today. And we might even have a
*  futuristic classic reggae track about AI. That was my prompt as kind of theme music for this episode.
*  So that's a very timely recommendation. Okay. Second one. So let's imagine a hypothetical
*  situation. A million people already have the Neuralink implant and the safety profiles like
*  generally looking good. I usually say like, imagine it's kind of like COVID vaccines where
*  it's like by and large, most credible sources seem to agree that it's appears to be safe.
*  That doesn't mean, of course, nothing could go wrong or there's no doubt about it. But
*  if you get one, then you can communicate directly from your brain to all your devices. Would you be
*  interested in getting one? Yeah, I think it's a good question. I need to think more carefully
*  about the potential applications over here and what benefits it does have for me.
*  Again, I think this is one of those trends, which is obvious in terms of like how our interaction
*  with technology and AI has evolved over the last few decades. We're making it simpler and simpler,
*  more efficient. So you've been controlling GUIs to know language. And I think the next obvious
*  to you is neural interfacing. Yeah, I think the question is, can I keep up with that piece
*  of interaction that might happen as soon as I have this high bandwidth channel? And what are
*  the kind of new things that I can do now with that, which I couldn't do before? I haven't maybe given
*  deep thought on that one to give you a direct answer right now. But as someone who likes to
*  explore new things, I think that it could be fun. And I see that happening. But I do think that we
*  are going to probably invasive ones are not going to be what is going to become popular. I think
*  we're going to make progress towards one this way interfacing technologies as well.
*  And that may be maybe a longer time still out there than what New Link has right now. But I think
*  that is also very obvious. The trends are obvious there. Yeah, there's been pretty visible progress
*  on that just in the three months that I've been asking this question. So may have to update it
*  to a V2. Okay, so last one then, just zooming out, you know, as big picture kind of wide lens
*  as you can. What are your biggest hopes for and fears for society at large, as we enter this
*  seemingly likely to be transformative AI era? It just feels like the opportunity of a lifetime.
*  I have impact in the world in a safe and beneficial manner. And
*  leverage technology and AI to improve the health of millions of people and help people reach their
*  true potential. I think there's a very good chance of that happening. Given a sufficient enough
*  time scale. My hope is just that the wider community over here, everyone who's in
*  positions to influence over here, that people will train these models, but also policy makers,
*  regulators and users of these systems and so on and so forth. We kind of like work together
*  in a collaborative manner and we ensure that everyone pulls together in the same direction
*  in a fast and bold manner, but also in a safe and responsible manner. And I think if we are
*  able to achieve that, I don't know what the odds of that out or could be that that doesn't happen.
*  I think the future is very bright. The arc of technology is such that I think we've had
*  generally technologies that are dual use, whether it's fire, electricity, or automobiles and so on
*  and so forth. And humanity as a whole has always until now managed to make safe and beneficial use
*  of these technologies while being able to constrain elements of society that want to use this
*  in their face. So I remain very optimistic about doing these and making use of AI and
*  yeah, just use it to do incredible things. Vivek Natarajan, thank you for being part of the
*  cognitive revolution. Thank you so much for having me. Amnaki uses generative AI to enable you to
*  launch hundreds of thousands of ad iterations that actually work customized across all platforms
*  with a click of a button. I believe in Amnaki so much that I invested in it and I recommend
*  you use it too. Use Cogrev to get a 10% discount.

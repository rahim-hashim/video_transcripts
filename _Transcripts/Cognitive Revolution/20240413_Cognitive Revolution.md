---
Date Generated: April 14, 2024
Transcription Model: whisper medium 20231117
Length: 3699s
Video Keywords: ['Descript']
Video Views: 699
Video Rating: None
---

# Data, data, everywhere - enough for AGI?
**Cognitive Revolution How AI Changes Everything:** [April 13, 2024](https://www.youtube.com/watch?v=IdCWaWupMrk)
*  Oftentimes, people's conceptions of AI progress seem to be more so derived from aggregating
*  the sentiments of the crowd than any core ground-up framework.
*  This is something often I do as well, but we want to avoid reducing AI as a concept
*  to an index that we're sort of longer, short, bearish, and bullish, overpriced, underpriced.
*  Because doing so makes our models of the AI space sprout in other people's opinions of
*  Rather than in any facts of the case, it's becoming awfully clear to me that these models
*  are truly approximating their datasets to an incredible degree.
*  What this manifests is, trained on the same dataset for long enough, pretty much every model
*  with enough weights in training time converges to the same point.
*  Improvements in data quality and improvements in algorithmic architectures can be viewed as
*  reducing the scale requirements to reach this human level performance in generality
*  across a large range of tasks.
*  Hello and welcome back to the Cognitive Revolution.
*  Today we're diving deep into one of the most critical questions in AI.
*  If we think that we can build some form of AGI by simply scaling up the current paradigm,
*  is there enough high-quality data in the world to get us there?
*  Joining me on this journey is Nick Gannon, Master's Degree Data Scientist by Day,
*  AI Scout by Night. He conducted extensive research to gather the numerous numbers that
*  we'll be discussing over the next hour.
*  We begin by extrapolating the trends set from GPT-2 to GPT-4 to set a budget for a hypothetical
*  GPT-5. Then we consider the total data volume generated across domains like email, social media,
*  YouTube, genomics, and astronomy, attempting to determine just how much of humanity's raw data
*  output would need to be high quality to achieve this ultimate goal.
*  We also work backward from the scale of compute that we might expect to have in the future,
*  asking how much data we'd need to use it all effectively.
*  As you'll hear, this episode is full of interesting numbers and useful comparisons.
*  Our goal is to help you anchor your AI worldview to realistic ranges for the key AI inputs of data
*  and compute, enabling you to better contextualize the growing volume of new research, data sets,
*  and models that you'll have no choice but to process with increasing speed going forward.
*  While following the many order of magnitude calculations that we work through,
*  will likely require more focus than our typical episode, I personally believe the extra effort
*  is worth it. In a world where the White House has set 10 to the 26th flops as the threshold for
*  reporting training runs, I think anyone seriously tracking AI progress should actively build
*  intuition around key reference numbers. As always, if you value this work, we appreciate
*  it when you share it with friends. And for this experimental episode in particular,
*  we especially request your feedback, either via our website, by DMing me on your favorite social
*  network, or if you loved it, via a review on Apple podcasts or Spotify. I don't see anyone
*  else doing quite this kind of work, but is that for good reason? Or would you like to see us
*  invest more in these high level guides? In any case, your input will shape our future decisions.
*  Now, without further ado, here's my discussion about the scale requirements for AI training data
*  with Nick Gannon. Nick Gannon, welcome to the Cognitive Revolution. Thank you. So we are here
*  to talk about data. And I've been really intrigued by some of the analysis that you've brought to
*  bear on this question of what data exists, what's out there, are we going to run out of it? What are
*  the different modalities? So this is a scouting report episode that really just tries to get our
*  arms around the scope, the scale, and the nature of data to the best of our ability. And I really
*  appreciate all the work that you've put into trying to answer these questions. I'm excited to
*  learn a lot from your analysis. Yeah, absolutely. Yeah. Thanks for letting me share. So diving into
*  here, the general premises, what are the data requirements to brute force your way to systems
*  that are as generally intelligent as humans across essentially all cognitive tasks?
*  Oftentimes, people's conceptions of AI progress seem to be more so derived from aggregating the
*  sentiments of the crowd than any core ground up framework. This is something often I do as well,
*  but we want to avoid reducing AI as a concept to an index that we're sort of longer, short,
*  bearish, and bullish, overpriced, underpriced. Because doing so makes our models of the AI space
*  crowded in other people's opinions of AI rather than in any facts of the case. So instead of this
*  AI perspective of crowd sentiment analysis aggregation, it makes more sense to live within
*  an explanatory paradigm to explain the current state of affairs. In AI, the current paradigm
*  that sits at the core of the hyper scales being open AI, deep mind, and enthrotic is the scaling
*  hypothesis of intelligence. And Ilya puts a pretty well outlining two fairly simple premises for the
*  scaling hypothesis that sort of underlies the AI strategy of these three firms. Premise one being
*  really just this if brain bigger than brain smarter premise. And the second one being there is
*  functional parity between biological and artificial neurons. And this is like a substrate independence
*  of intelligence. There's nothing necessarily unique about fleshy wires or anything along these
*  lines. It doesn't need to be carbon basic and silicon. If premise one and premise two hold,
*  then human level AI systems are not only tractable, but a very doable engineering problem. It is
*  examining data through this reference frame of scale that gives it the most grounding and how
*  we should go about approaching this that allows us to take API like extremely literally even more
*  so than taking it seriously where we start planning for the world that we are walking into
*  where we've got systems that are as generally intelligent as humans across essentially all
*  cognitive labor. Jay Becker has a really good quote on the role of data to be played here.
*  Jay Becker for context has an awesome blog. He works at OpenAI and essentially builds distributed
*  clusters and large systems at scale. He's got a quote says, it's becoming awfully clear to me
*  that these models are truly approximating their data sets to an incredible degree. What this
*  manifests is trained on the same data set for long enough, pretty much every model with enough weights
*  in training time converges to the same point. And this is a very extreme interpretation of
*  the scaling hypothesis where improvements in data quality and improvements in algorithmic
*  architectures can be viewed as reducing the scale requirements to reach this human level
*  performance in generality across a large range of tasks. Yeah, just to zoom out for a second,
*  the core question right now is, can we just keep scaling? One of the key questions seems to be,
*  is there enough high quality data? The leaders at the labs seem to be pretty clear on their belief
*  that there will be enough data or that they can figure it out one way or another, create it if
*  they have to, but across the board, nobody has shown much concern of the SAM-A, GDB, Ilya,
*  Demis, Shane Legg, Dario set. Nobody there that I'm aware of has shown much concern about lack of data
*  being a fundamental barrier. And on the contrary, pretty much all of them, I can recall quotes
*  for where they're like, yeah, we'll be fine. We'll be able to get over that. So that's the paradigm.
*  How far does it hold? They seem to think it's going to hold. Now we can actually go out and
*  look at how much data there really is. What is the data we actually have? Yeah, absolutely. And so
*  going back to GPT-3, GPT-3 was trained on roughly one trillion tokens or 600 gigabytes of text.
*  In a lot of numbers, our ultimate goal is to be in the correct order of magnitude.
*  Honestly, our confidence interval, we would like to be smaller than an order of magnitude ultimately.
*  Along these lines, the GPT-4 training is estimated to be somewhere around 10 trillion words or 10
*  trillion tokens. And this 10 trillion data point number is something that we're going to anchor
*  against going forward. And it comes from many places. Probably the most influential is semi-analysis
*  research, where he estimates GPT-4 to be 16 head MOE, 111 billion parameters per head,
*  1.8 trillion parameters total with an additional vision encoder with cross-attention trained on
*  another two trillion image tokens. So giving these GPT-3 and GPT-4 estimates, current scaling trends
*  suggest that GPT-5's data set is going to be somewhere in the hundred trillion byte, or we can
*  think hundred trillion word territory. And if we look at Chinchilla scaling laws, if we're going up
*  910x on the increase in data set size, that would be akin to about two orders of magnitude increase
*  in the amount of compute that we're going to be using, which does fall in line with the compute
*  trends that we're seeing as well. And it is also worth noting that Chinchilla optimality is no
*  longer in fashion and everybody essentially trains significantly past Chinchilla optimality
*  with really high token per parameter counts to minimize inference latency and inference cost.
*  To add a couple more caveats to these GPT-5 training set estimates, it's worth diving into
*  some of the algorithms that are likely to be central features. So the pre-training context window size
*  can have a large impact on the data to compute ratio. And it seems likely that GPT-5 will be
*  trade with something that looks like ring attention, a mechanism to allow context window sizes to get
*  to this sort of one to a hundred million token context window with perfect needle in a haystack
*  recall. It's speculated that this is likely what Gemini 1.5 is using and also what Claude Opus is
*  using to get that really long retrieval performance. And to illustrate the computational
*  savings that you get from ring attention, because it's not approximate, so you still do have to pay
*  this quadratic compute. If you have a one terabyte model with roughly a trillion parameters, if you
*  were to pre-train it on a fixed data set size at 4k token context window, and then you're going to
*  pre-train it on a million token context window, it would actually be 5.6 times more compute for
*  the million token context window. Intuition for why this would be the case is attention's
*  flop contribution is being offset by the dramatic increase in tokens per batch. So we can think we
*  have this 4k squared value in the numerator, and then you've got this divided by 4k, and then we're
*  changing that to a million squared in a numerator along with a bunch of other variables, number of
*  layers, things along these lines, but you're dividing by a million. So it takes the byte out
*  of that 256x and intuitively, if you're batching at a million tokens, you just have way fewer batches
*  as you're going about this pre-training process. And so we can look at this sort of variable as
*  being a downward force on the data requirements that we would need to train something like
*  GPT-5. You've actually spoken to this in your Mamba work where some of these algorithmic developments,
*  it's pretty astonishing that anybody is publishing them at all. This feels like a secret that if
*  somebody went to DeepMind and asked for 10 million dollars, they could likely be given 10 million
*  dollars just for DeepMind to have the option to have a couple months before everybody else figures
*  out an algorithmic secret. So it's definitely shocking that any of this is publicly disclosed
*  in the west of the hearts of all of the academics of the world for doing that. In further caveats to
*  these GPT-5 data requirement estimates, the scaling laws for MOE are different than Chinchilla
*  optimality. MOEs were dealing with highly sparse decoder-only transformer models, and they're sort
*  of the elected successor of dense counterparts because they're vastly more compute efficient
*  across just a really wide range of compute budgets. And we look at the MOE of GPT-4 on a forward pass,
*  it's likely of the 1.8 trillion parameters, maybe only 270 billion of those parameters are actually
*  being activated, allowing us to reap a lot of these benefits of scale without paying this really high
*  latency cost. But on the other side of that, there is no free lunch. And so while the MOEs
*  still follow scaling laws, meaning cross entropy of log loss and log complexity decreases on a
*  range of test sets, linearly as a function of log data and log parameters and log compute,
*  the slope is a little less slopey. Okay, a quick recap of that because there's a lot there.
*  Starting off with the amount of training data that is going to be potentially thrown into a GPT-5.
*  One trillion was the number for GPT-3, that is 10 to the 12th. So 10 to the 12th tokens for GPT-3,
*  10 to the 13 or 10 trillion tokens for GPT-4. And you're estimating that would go up another 10x
*  with GPT-5 to 100 trillion tokens of training data or 10 to the 14th tokens. And to get an intuition
*  for why it would grow by a factor of 10x, it seems like that's based off the budgetary observation
*  that the compute budget is going up 100x per generation. Right. So let's imagine that they
*  100x the budget. We have estimates of flops and we also have estimates of dollars. GPT-3
*  trained from scratch for under a half million dollars was a mosaic claim from a little while ago.
*  Estimates of flops on GPT-4 are somewhere in the 10 to the 24, 10 to the 25 range. We don't know
*  exactly. And that is mid tens of millions of dollars compute budget. So if we're then imagining
*  100xing that, we're getting into a billion to a couple billion run size. So that basically tracks
*  certainly Nvidia's revenue seems to be on the order of magnitude, suggesting that people are doing that.
*  Meta's announced purchases would allow them to go in that direction pretty soon if they wanted
*  to. So, okay. Billion dollar training run 100x compute 10x the data size. And why does that 100x
*  compute translate to 10x the data size? The chinchilla training laws say that for a given
*  compute budget, you're going to expand both the parameter count and the token count. And when you
*  expand both the compute required is the multiplication of that. So if you make the parameters 10x
*  bigger and the data 10x bigger, then your compute budget gets 100x bigger to expand both of them
*  in parallel. It's also really good note that the shift in overtraining seemed to be really associated
*  with llama because they trained llama to seven B up to two trillion tokens, which was like, oh, wow,
*  you're taking the parameters way down, but still doing a ton of tokens because the models can learn
*  past the point of optimality. And especially if you want to make something that people can run on
*  their laptops or whatever, which obviously was a big part of that whole program. Then you take this
*  100x compute budget and maybe you say instead of going 10x and 10x on either side, maybe I'll do
*  20 and five. That does lead you to something pretty dense. And then finally, with the ring attention,
*  the much bigger context window requires much more compute to compute all the attention. But
*  because you are running the data through in such bigger batches, you are not making as many updates
*  to the weights. Okay, cool. Hey, we'll continue our interview in a moment after a word from our
*  sponsors. Omniki uses generative AI to enable you to launch hundreds of thousands of ad iterations
*  that actually work customized across all platforms with a click of a button. I believe in Omniki so
*  much that I invested in it and I recommend you use it to use cog rev to get a 10% discount.
*  So basically, with all that said, we have to see our way to 100 trillion high quality tokens.
*  Yeah, absolutely. So diving into how much data we currently have at our disposal in the year 2020,
*  estimates were that we created about 64 zettabytes of data, which if we converted everything to text
*  to be somewhere between 60 and 100 sextillion words, which is an almost meaninglessly large
*  number. And really, almost all of this is just copies and copies of copies. You'd think of
*  Netflix video or a YouTube video as being pre-stored segments or chunks of video
*  that are streamed from some CDN node that happens to be closest to you.
*  So the 2020 headline super high level number is zettabytes 10 to the 22. That is all data. That's
*  like global storage. So our hundred trillion words by comparison is 10 to the 14. So we're talking
*  one in 10 to the eight, aka one in 100 million parts of this raw data would have to be
*  high quality text for us to see our way to the theoretical GPT-5 training data scale.
*  This data just includes everything. It clocks in at about 13,000 times more words than all of the
*  humans have ever said collectively through the history of email, about a hundred billion humans
*  that have lived thus far. It's the continual monitoring logs of edge computers, such as electric
*  toothbrushes. It's the 333 billion emails that are sent each day, the vast majority of which are like
*  the same emails being sent to all of us. So one in 100 million parts of this raw data
*  would have to be high quality text. I would say that's feels safe as much as there's a lot of
*  log data and a lot of garbage out there. It does feel like if only one in 100 million parts of
*  total data has to be good, surely that much is good to put them in scientific notation as well.
*  So there's 10 to the 11 emails sent per day. Assume 300 tokens per email. You're already up to
*  10 to the 14. Assume 300 days of the year. You're up to between 10 to the 16 and 10 to the 17.
*  We need to get to 10 to the 14 of high quality. So if one in 1000 emails is high enough quality,
*  then email traffic would contain enough data to do the job. Obviously, you've got major access
*  questions on something like email, but yeah, again, it seems like you can start to wrap
*  your head around why people would not be too worried because there's just a ton flying around.
*  So we have orders and orders of magnitude, more data than we actually need. And the current trends
*  seem to suggest that the amount of data being generated by the world doubles roughly every
*  three years, meaning about half of the data that has been generated the last three years.
*  And it seems that this is going to continue if not accelerate. Let's get a little bit more of a grasp
*  on what this looks like with a little bit more granularity. There's a great research paper called
*  Big Data Astronomical or Genomical that dives into a couple domains, including astronomy,
*  genomics, YouTube, Twitter. And it also touches on other things like particle physics data
*  accumulation. Apparently the Large Hadron Collider creates quite a bit of data. So Twitter can serve
*  as a great microcosm of sort of mediocre quality text data on the internet. And estimates suggest
*  that about 33 terabytes of text are being generated per year. And this is about a billion tweets a day,
*  most of which is probably executed by bots, spamming people. And this is enough to train a model
*  about double to triple the size of GPT-4. Okay. The Twitter one was a billion tweets a day,
*  say 100 tokens per tweet were at 10 to the 11, 300 days, three times 10 to the 13 would be the
*  total volume of Twitter for a year. Yeah. So that's three times GPT-4 and would be about a third of the
*  way toward this hypothetical GPT-5. So, wow, it's interesting. The relative scale of email versus
*  Twitter is shocking. One one thousandth of email over a year would be enough for GPT-5, but you need
*  three times Twitter to get to GPT-5. And that also goes to show, I mean, OpenAI has a data acquisition
*  team that they've been fairly public about where they're just like looking for all kinds of data
*  and trying to partner with, whether it's governments that have their own data sets of
*  their particular language, or really they're open to a lot of things. It's not necessarily easy for
*  them to get to the scale that they want to get to. All this stuff is locked up in other people's
*  systems. And so the question is, who knows where it is, how to tap into it, how much do they need
*  to be compensated to potentially share it. But one in a hundred million parts definitely suggest that
*  we'll get there to get to GPT-5. Okay, cool. In terms of our target, we've been conceiving of this
*  largely in text. And it's also interesting to think what other modalities might be bolted on there.
*  A lot of this overindexes on text, but that's largely just because it's easier to think about
*  all of these estimates in a single modality, even though this is very much a story of many modalities.
*  Okay, cool. So let's get back to the story.
*  Yeah. So we have astronomy and YouTube data, which are roughly on the same scale of one to two
*  exabytes. And so exabytes, if we were on the terabyte scale for dealing with Twitter,
*  we're 33 terabytes. We skipped had a scale and we went straight to exit scale. So we skipped
*  essentially four orders of magnitude in there. And for YouTube, this essentially means we've got
*  500 million hours of uploaded content every year. And remarkably, we have about
*  that equivalent in images of space. Hubble and James Webb are certainly pulling their weight here.
*  So if you did just want to go straight YouTube, it does seem like that's a honeywell that will just
*  keep giving and giving for a good long while. And then genomics data, you have about 40 exabytes
*  of genomics data being stored every year in almost none of it is actually being utilized.
*  So I'll trust folks are familiar up through Giga, which is a billion. So a gigabyte is a billion
*  bytes, a terabyte, Tera for 12, Tera is 10 to the 12, a peta is 10 to the 15,
*  and an XA is 10 to the 18. So the scale of both YouTube and as it turns out, astronomy at 10 to
*  the 18, that is four orders of magnitude bigger than our 10 to the 14 target, 10 to the 14 target
*  corresponded to a billion dollars in compute. So if you actually said, what would it take to scale out
*  to all this raw astronomy data? Talk about your universal function approximators. Here's all the
*  stars, figure out what's going on. Now we can start to be maybe a little fast and loose on which
*  scaling laws we're going to use. If we're going up an order of magnitude of data, we're also presumably
*  going up an order of magnitude in params. Therefore, we're going up two orders of magnitude in compute.
*  You'd be talking about taking the budget up 10 to the eight, which would be 10 to the eight
*  billion dollars. So you're talking a hundred quadrillion dollars, which is a thousand years
*  of global GDP at present. So that's probably a bit out of reach. We're going to need some filtering
*  techniques to do that. But it is also really interesting just from a YouTube standpoint,
*  those are bytes and you can definitely get a pretty good discount from pixels to tokens.
*  Obviously it depends on how well the model works and the nature of your images that you're looking
*  at. But I'm been doing a bunch of stuff recently with GPT-4V and the new Claude multimodal, which
*  by the way, the new Claude Haiku is insane. It's so much cheaper and faster. And for my use cases,
*  it largely seems to work roughly as well. If I was looking for a tumor in an X-ray or whatever,
*  I don't think I would take it to Claude Haiku, but for this, is this an appropriate image to be
*  used in a certain context or whatever? It's like totally handling that stuff fine. But I guess I
*  know GPT-4V best there, a low res image is billed at 85 tokens and a low res images, maybe 256 by 256.
*  So you're looking at, let's call it 50,000 pixels, each of which is basically a byte of information.
*  That means you are going down a thousand X pixel to token compression. So now let's do that again
*  on the YouTube side. YouTube at 10 to the 18 bytes. If we were to try to compress that to
*  tokens at that thousand to one ratio, we'd be at 10 to the 15 tokens, which would be 10X the
*  tokens of our 10 to the 14 GPT-5 target. And that's the annual upload to YouTube. So that would be
*  if you wanted to do all those YouTube tokens following a chinchilla scaling law,
*  you would be 100Xing past our hypothetical GPT-5 budget. So then we'd be talking
*  hundreds of billions of dollars of compute, which it's funny. That's like on the balance
*  sheet for the world's biggest tech companies. That's like the size of cash and cash equivalents,
*  Google, Microsoft, Apple, Meta, balance sheet. It's crazy to think that, I mean,
*  it is in scope for those guys. Obviously a lot of engineering is going to go into,
*  they're going to need to buy a lot of chips, but they could just raw crunch all of YouTube.
*  If it really came to that. Okay, cool. So we got 10 to the 14 target. We got 10 to the 18 from
*  astronomy. We got 10 to the 18 from YouTube. Apply token deflator. We would get 10 to the 15
*  tokens from YouTube. All of YouTube on a chinchilla scaling law basis would be estimated at a hundred
*  billion dollars to train on that scale. But again, another way to think about that is 10% of the
*  tokens of YouTube would have to be good in some sense to get that same level. Okay. Useful data
*  points to have in mind. I will, I'll be referring back to this often. Let's just maybe start it over
*  at the top of the genomic section. Yeah. So moving on from astronomy and YouTube data, we move up
*  in order of magnitude for genomics data in the rate of growth in the genomics data space,
*  certainly outpaces a lot of these other spaces where we're seeing about a doubling in the amount
*  of genomics data generated every two years. And so right now we're generating about 40 X of bytes of
*  genomics data a year, which definitely gets us to this point where we're a million X, the amount of
*  data required to train GPT-4. So that's interesting for genomics specifically coming in at 40 X of
*  bytes, four times 10 to the 19. It is kind of crazy that that's that much bigger than YouTube size of
*  human genome is 3.4 gigabases. We each have 3 billion bases. So in the raw data, we each have
*  three gigabytes. So to get to X of bytes from gigabytes, you basically got to be doing a billion
*  sequences a year. I don't think we're sequencing a billion humans a year, but you think about all of
*  the other things that are constantly being sequenced and that seems not crazy. So just as
*  another anchor on this, I looked up the size of the data set that is behind the recently released
*  EVO model. They're open sourcing a 300 billion token training data set, which consists of 2.7
*  million publicly available prokaryotic and phage genomes. This is kind of crazy because
*  they don't get here to the organisms with nucleus in their cells. This is all prokaryotic and phage,
*  and that gets you to 300 billion tokens. So genomics projects hit 10 X of bytes scale,
*  10 to the 19. That's a billion human sequences. So it's like high end kind of what genomics data
*  look like. That's all healthcare data, including like imaging, whatever is even like a lot bigger
*  than that. That gets up to 10 to the 21 just raw bytes of data. Presumably a lot of that is imagery.
*  Low end from the EVO paper, 300 billion tokens, all prokaryotic and phage is used to train that
*  7 billion parameter model, which is ostensibly developing some sort of life or cell model,
*  which is something I really am eager to understand better. And if you're listening at this point
*  and you're somebody who knows a lot about that, then definitely ping me because I want to do one
*  of these for that as well. I've been actively pinging people and DMing to try to find the right
*  scouts for the intersection of AI and biology. But again, 300 billion tokens curated just from
*  prokaryotic organisms. Two trillion was the amount of image data added to GPT-4 to get to that vision
*  understanding. So it seems like, again, a pretty clear path to the scale of data that would be
*  needed to certainly add a DNA modality. And this is where this stuff starts to get like really
*  trippy is when you start to think about adding modalities on the native on par basis that
*  humans just have no intuition for. For all the tools and understanding we've developed of DNA,
*  we cannot natively speak DNA. Nobody can do that. And there's now both a proof point to believe
*  that models are starting to do that, even at 300 billion tokens, and then a path to easily scaling
*  that 10x, which is the same size of image data set that got us to GPT-4V. So you think, huh,
*  it seems pretty realistic that you could just add some sort of native sense for DNA
*  into a language model. I imagine the curriculum learning aspect of that would be like quite
*  important. A big part of how OpenAI has been so successful with their multimodal stuff in general
*  has been recaptioning. There's this process of refinement where they are creating better and
*  better captions for the images and much more tightly aligning the vision and language spaces
*  that way. And I imagine there would be definite need for tricks there as well on the DNA side,
*  to really make use of that. You would presumably need to annotate it in all sorts of ways. I mean,
*  you'd want proteomic data or regulatory RNA data as well. But if you started to interleave all those
*  together, especially with some sense of health outcomes, I started to think about putting that
*  stuff interleaved with like scan results. It sure seems like you could get to an integrated system
*  that speaks biology as well as language and image. And I've not even been talking at the level of
*  theoretical GPT-5. This is the level of vision that already exists in a GPT-4 was the 2 trillion.
*  So moving on to areas outside of genomics and astronomical, this planet is really dripping in
*  data to a large degree where there's 600 GPT-4s worth of pre-training data in the world data center
*  for climate. The way that they actually go about accruing weather data is definitely very cool.
*  They're scraping just four quarters of the planet. And DeepMind certainly has a cool paper where
*  predicting hundreds of weather variables 10 days in advance to 0.25 degree accuracy in under a minute.
*  It's just a lot of infrastructure from the entire world. Satellite imaging data in sensors on
*  aircrafts, in ships, in buoys, in hydro-mediological radars and weather stations and
*  radios nodes on weather balloons. And they just, they hold nine yards. They're just taking it from
*  everywhere. That's wind, temperature, humidity, pressure, just a lot of different ways of attacking
*  this. Does it say in that paper how big that data set is? Claude 3, Opus, tell me what is the size
*  of the data set in this paper? Okay. Apparently it does not say. Claude can't find it, but 37 years of
*  weather data. Moving on, there's another several hundred GPT-4s worth of training data in the US
*  Census Bureau. Apple Vision Pro has just a remarkable mechanism to accrue data. There's
*  blockchain data. Really the whole financial sector has a remarkable amount of data. In the financial
*  sector, one of Jeffrey Hinton Lost Protégés, Peter Brown, who is actually Hinton's first advisee,
*  has allegedly been accruing a really large number of H100s. And he currently runs
*  Jim Simons' hedge fund, Renaissance Technologies. Renaissance Technologies, having had their premiere
*  fund return about 37% a year, every year for decades. And there's definitely an interesting
*  element where we are starting to have people to a remarkable degree using AI to essentially win
*  the financial markets. And they appear to be increasingly using larger amounts of compute
*  as they're doing it. And then moving on to the size of the internet, the amount of pages indexed
*  by Google at any one point in time oscillates roughly around 50 billion pages. In estimates for
*  the unindexed size of the internet range anywhere from 25x the index size to about 2,000x the index
*  size. And when examining what is the unindexed internet look like, try to find an old tweet.
*  And you'll find it's just not indexed on the internet and it's not going to pop up. And this
*  is the sort of stuff that's lost in the ether where it is accessible in theory, but it's just
*  not searchable. And it's also worth noting the massive error bars here. So we're 25x to 2,000x
*  larger than the index internet. And it's sort of asking like, how big is the unobservable universe?
*  Well, it's at least a little bit bigger than the observable universe. And it could be a lot of bit
*  bigger, but it's really tough to calculate. Hey, we'll continue our interview in a moment
*  after a word from our sponsors. The tech world turns to the Brave browser for its unbeatable
*  privacy protections. But did you know that Brave also has a private ad platform? Brave Ads offers
*  first party targeting and it's been cookie list since day one. So you can relax while third party
*  tracking cookies disappear from the web. Today, millions of people turn to ad blockers to avoid
*  being tracked and pestered online. But Brave's new ad model aligns incentives for users and
*  advertisers. Users earn rewards for viewing ads, which they can save, spend, or pass along to their
*  favorite creators. And advertisers score points for respecting user privacy, generating ROI without
*  invasive tracking. So whether it's high impact announcements on the new tab page or keyword
*  targeted ads in Brave search, Brave offers diverse private future proof ad formats for all your
*  business goals. Join the future of advertising at brave.com slash ads. Mention MOZ when signing
*  up for a 25% discount on your first campaign. Today's podcast is brought to you by Plum. You've
*  probably noticed by now that the AI features in your favorite products kind of suck. They're cool
*  the first time, but pretty soon you're underwhelmed. That's because truly great AI features require
*  complex pipelines and rigorous testing that most startups simply don't have the time or tooling to
*  get right. That's why Plum created a collaborative AI app builder that's purpose-built for product
*  teams. Your users deserve better than a glorified GPT wrapper. Blow their minds with Plum. Check out
*  useplum.com. That's Plum with a B for early access. Hey all, Eric Torenberg here. I'm hearing more and
*  more that founders want to get profitable and do more with less, especially with engineering. Listen,
*  I love your 30-year-old ex-fang senior software engineer as much as the next guy, but honestly,
*  I can't afford them anymore. Founders everywhere are trying to turn to global talent, but boy,
*  is it a hassle to do at scale from sourcing to interviewing to on the ground operations and
*  management. That's why I teamed up with Sean Lanahan, who's been building engineering teams
*  in Vietnam at a very high level for over five years to help you access global engineering without
*  the headache. Squad, Sean's new company, takes care of sourcing, legal compliance, and local HR
*  for global talent so you don't have to. With teams across Asia and South America, we can cover you no
*  matter which time zone you operate in. Their engineers follow your process and use your tools.
*  They work with React, Next.js, or your favorite front-end frameworks. And on the back end,
*  they're experts at Node, Python, Java, and anything under the sun. Full disclosure, it's going to cost
*  more than the random person you found on Upwork that's doing two hours of work per week but billing
*  you for 40. But you'll get premium quality at a fraction of the typical cost. Our engineers are
*  vetted top 1% talent and actually working hard for you every day. Increase your velocity without
*  amping up burn. Head to choose squad.com and mention Turpentine to skip the wait list.
*  The other thing that we didn't cover is code, and that's probably one that we should at least look
*  at for a second. Just pulling up the big code data set from Hugging Face is 6 terabytes raw,
*  3 terabytes, they say, near fully deduped. So 3 times 10 to the 12, this code data set
*  is 10 times bigger than the genomic data set used in Evo hanging out on Hugging Face deduped.
*  That would be 30% of GPT-4, 3% of GPT-5. That's an area where you can really generate an unbelievable
*  amount of stuff. And then even in the synthetic data space, we're seeing a remarkable growth rate
*  in the synthetically generated data from GPT in Claude in Gemini where quick market sizing,
*  we could estimate GPT to have maybe 25 million daily active users, maybe 15 queries per day per
*  user, which is potentially an overestimate, but I'd probably query GPT 40 to 60 times a day on
*  the average weekday. And if we estimate about a thousand tokens per response, we again get to this
*  sort of team to 45 trillion generated words by ChadGPT, which again is enough to train a couple
*  GPT-4s. And so you were speaking about this earlier, the degree to which nobody seems to be
*  particularly concerned about the amount of data that we have. It comes up and then there's a sly
*  smile that goes across the face of the AI researcher and they say, don't worry about it.
*  We've got it figured out. And it might be synthetic data. It could be these huge,
*  honeywells of data elsewhere, but it definitely does seem like at first glance, there is just a
*  lot at our disposal. Okay, great. Well, let's do a quick recap of the bullet case.
*  I find the bullet case pretty compelling. The bullet case is GPT-5 would need 10x more data than
*  GPT-4, which would correspond to a hundred X bigger training budget, which is like a billion
*  dollar or a couple billion dollar training run. And 10 to the 14 or a hundred trillion tokens
*  is the target. Basically that's one in a hundred million parts of all the data
*  that we're creating. That would be one in about a thousand of all the email volume. It's roughly
*  on the same scale as all of Twitter for a year. And other modalities seem to also be like pretty
*  accessible. YouTube tokenized even with a thousand to one pixel to token compression ratio
*  is 10 times that target with just one year's worth of data uploaded. So 10% of YouTube would have to
*  be good for that to hit some sort of parody. Astronomical data, it's just a kind of, you know,
*  ridiculous amount. Genomic data, another kind of ridiculous amount. And we already see that not
*  huge amounts are starting to work. 300 billion tokens uncompressed in the EVO paper as compared
*  to 10 to the 12, which was the scale of image tokens in GPT-4. So the benchmark of two trillion
*  tokens to add a modality that seems like all the usual suspect modalities would have plenty of
*  data available. And then synthetic data was the last thing that we mentioned where basically chat
*  GPT is like generating more data than it was trained on. It's already generating more than
*  it was trained on and it's approaching generating as much as GPT-5 would need to be trained on.
*  Obviously quality there becomes the question, right? The bull case is that just the scale is so big
*  that surely these small fractions of these holes are good enough to work. That's honestly most
*  compellingly obvious on these other modalities where we just can't interpret them natively very
*  well. Any sort of being able to see DNA, so to speak, would be potentially game-changing,
*  but the bear case presumably has to start with quality. Okay, sure. There's all that stuff,
*  but how confident are you really that the fraction that you need is actually going to be of the
*  quality that you need to get there? So let's tackle that. Time for the bear case.
*  Yeah, absolutely. So a research paper from Epic AI called Will We Run Out of Data does outline a
*  little bit more of like the taking us back to reality, like how much of this data is usable,
*  at least insofar as it's high quality text data. And Epic AI suggests that we're actually going
*  to run out of high quality text data between 2024 and 2026. And they claim the amount of high
*  quality data to be roughly on the order of 10 trillion words. So the amount of high quality
*  text data is roughly akin to the amount of data used to train GPT-4. Data finesses, books, news
*  articles, scientific papers, Wikipedia, filtered web content. Just to sort of sniff test this number,
*  the amount of words of text in the Library of Congress is about 10 trillion words or, you know,
*  10 terabytes of data. So if getting into the Library of Congress's storage is some sort of
*  litmus mechanism for, are you a high quality text token? It does seem fairly reasonable.
*  On the one hand, we've got plenty of data. And on the other hand, most of it seems to not necessarily
*  be of high quality. And certainly here, we are over indexing on the idea of text tokens, where
*  building human level systems could very much, even if not more so, be a function of vision or
*  other modalities. But it also makes the estimates a little bit more consumable to reduce it down to
*  a single modality. Yes, if we were to brute force our way to the largest training run,
*  we could feasibly do. And this is a little bit of the Carl Schulman perspective, where the max
*  scale of a training run that we could get is something on the order of $1 trillion or 1%
*  of gross world products. Investments like this are, they're precedented, but they're very uncomp.
*  The primary anchor point would be the U.S. during the Cold War Apollo program was spending about 2.2%
*  of GDP on the Apollo program, meaning it's not completely out of the discussion to be spending
*  1% of global world products on just a very large training run. But if we moved up in order of
*  magnitude, it would fall out of feasibility. And furthermore, Apple's revenue is closing in on $400
*  billion. So this could be a degree to which we say like, the numbers are sort of there for this to
*  be just like the final attempts of brute forcing it. If there was no major algorithmic development,
*  we can just throw like 30 aircraft carriers of money at it or 10 international space stations
*  of money and see if we can't build this thing that's as generally intelligent as the human brain.
*  More than likely, if you were to get going to go about doing something like this, it would probably
*  be the Defense Department's dollar. Their current budget is about $800 billion. If that was siphoned
*  into chip fab production over the course of a half a decade to a whole decade, it does seem
*  very feasible. And certainly plenty of headlines recently about Sam Altman, allegedly speaking to
*  investors in the Middle East, about $7 trillion. I didn't see any quote that was like Sam said,
*  I would like $7 trillion. It was a lot more rumor mill. But there is evidence of Sam Altman,
*  even as far back as 2015, having discussions with the Secretary of Defense about the role of AI
*  and the role of compute in a national security context. It does seem if you were going to do
*  a trillion dollar training run, and you were going to have a cluster that was going to be able to
*  run this large pre-training, it would likely has to be in the United States. And really,
*  it does seem like the only two parties that could feasibly execute a training run at this scale would
*  be Xi Jinping and Joe Biden. So if Sam Altman were to get this $7 trillion and was able to do
*  a trillion dollar training run, and maybe it's Google, maybe it's another player, looking into
*  the investment side, like when would it happen and how much data would be needed for a training
*  run of this scale? So GPT-3 was roughly on the order of about $5 million. And most estimates
*  for GPT-4 is pre-training or somewhere between 50 and 100 million. And like all the bells and
*  whistles, I'm sure it's far more than that. There's plenty of R&D, plenty of side experiments going
*  on, but this is just like straight GPU costs for the singular pre-training run. In following these
*  investment trends out, where you're moving up in order of magnitude every two years or so,
*  we see this sort of trillion dollar training run coming somewhere in the early 2030s, if we're
*  following this investment trend starting in 2012 and going through to 2024 thus far. And so the
*  intuitions for how much data we would need would be anchored in sort of three different but core
*  trends. One is this investment trend where the most expensive training run, the cost of that is
*  doubling about every two years. And then we also have Moore's law, the compute trend that we're
*  seeing this doubling of transistor density every two and a half years. And in some sense, Moore's
*  law is dying, but in the less parochial sense, it's very much still alive, where we're interpreting
*  the spirit of Moore's law to be something closer to the sort of Kurzweilian law of accelerating
*  compute, where we don't really care about transistor density, we care about the amount of operations,
*  the second that we can do. And then third, there's algorithmic developments where since 2012,
*  we're seeing a doubling of effective compute about every nine months. And what we mean by compute
*  efficiency or effective compute is essentially the amount of floating point operations or the
*  amount of operations per second required to get a 90% on test set x, y and z that is coming down
*  cutting in half every nine months. And this is just a testament to better strategies and all of
*  the algorithmic developments, we have more dollars going to compute, we have more compute per dollar,
*  and we have more effective compute per compute. So in this sense, we can expect our trillion dollar
*  training run to be somewhere between 2029 and 2033, requiring about 85 quadrillion data points,
*  which is a lot of data. But if we're going to take the non tokenized version of YouTube,
*  it's not even a single year of YouTube. And just to give us a couple of anchoring points here,
*  most estimates put the processing of the human brain at about 11 million bits per second,
*  implying that the human brain processes about two to three quadrillion bytes over a 70 year
*  timeframe. And in this sense, the data processed by the human brain is about two to 300 x the scale of
*  GPT-4s training data. And what we would need for this trillion dollar training run would be about
*  8500 x the scale of GPT-4s training data. And so from the scale perspective, this human level
*  performance on cognitive tasks, it does seem quite reasonable if it's truly a story of data,
*  that it would be as we're approaching the amount of data that the human brain processes, that's when
*  we would start to get performance levels akin to that of the human brain on cognitive labor tasks.
*  And yes, we've got 85 quadrillion data points that we need to come up with for our trillion
*  dollar training run. And that would be about point 00013% of the data that was generated or
*  replicated in the year 2020. And then variously, we've got this epic estimate that suggests that
*  we need 8500 x more quality tokens of text data to build this full corpus if we were going to do
*  it exclusively in text. You're coming at it from a top down and a bottom up. The top down idea is
*  largest conceivable training run would be a trillion dollar training run. That would be
*  1000 times the budget of the 1 billion that we've estimated for GPT-5. You can split the
*  compute budget across increases in your parameters and increases in your data size.
*  If we have 1000x compute budget, maybe we could do 10x parameters and 100x data size. So from the
*  10 to the 14 tokens that we had for GPT-5, you get to 10 to the 16 target tokens. Now,
*  what do we actually have? Well, we know we have 10 to the 13 because that's what GPT-4 was
*  trading on and that's what the Library of Congress contains. We've pretty clearly established we can
*  probably get to 10 to the 14. 10 to the 16 though does seem like that could be kind of a lot.
*  Then there's also the estimate 10 to the 17th with my back of the envelope I got to 10 to the 16.
*  We're within an order of magnitude. But that definitely matters when it's that last order
*  of magnitude. How do we get to that one more order of magnitude out of there?
*  Yes. So essentially we're saying, okay, we're spending a trillion dollars. We're getting
*  more compute per dollar and then we're also getting more compute per compute. So the effective compute
*  is increasing. Okay. So that last order of magnitude basically comes from compute also
*  getting cheaper. Certainly a reasonable prospect. Now it's also important to keep in mind that is
*  how did we pick the starting point here? We basically picked the biggest training run that
*  seems like economically somewhat plausible and then said, assuming that compute continues to
*  get cheaper and we're maximizing the value of that budget, then to really do that you would
*  need something like 10 to the 17 tokens, which is 10,000 times GPT-4 and a thousand times our
*  target for GPT-5. So yeah, if it does take a trillion dollar worth of compute, it does seem
*  like we may struggle to get to that quality of data. Then you'd have to either be synthesizing
*  a lot of it, which may work. Clawed 3 certainly has changed my thinking about how viable this
*  refinement process really can be. I still am uncomfortable with the notion of just having
*  AI self-critique to the singularity, but the quality of Clawed 3 definitely suggests that they've
*  got that top spinning pretty tightly. It's not totally crazy to think that you could
*  generate data on the scale that we're talking about here. Definitely in code, there is the
*  opportunity for this kind of self-play, create, modify, actually run it and validate on the fly
*  in ways that you could really generate an unbelievable amount of code.
*  Yeah, totally. I do champion code is like the best sorts of synthetic data sets like AlphaGo
*  and AlphaZero and AlphaGR, the whole Alpha series, the mechanisms that they've created
*  to determine how to do Monte Carlo tree search at inference time and how to do synthetic data
*  generation and then self-play and how those work together to create the only data sets that we have
*  that are actually capable of generating superhuman performance in systems. And if the goal was to
*  create systems with superhuman performance, we have to throw most of the human generated data
*  in the trash. We start over with just Alpha geometry like systems, but we scale horizontally
*  where you've got an Alpha geometry in an Alpha fold for every game that could be played. So
*  really anything that you could put an ELO score on like chess could be constructed into an algorithmic
*  architecture that's value network Monte Carlo tree search, focusing on self-play and then updating
*  and then self-play and then updating. And then if you would like to do reasoning, the closest thing
*  that looks like reasoning right now is Monte Carlo tree search at inference time, which is
*  known Brown's work. If we let the model sink for a while, can it essentially play as a neural network
*  that has 10,000 X more parameters? That's really a way to hack your scale by just thinking more
*  about the problem. Those are a lot of the elements that are going to be zeroed in on.
*  Yeah, that self-play stuff, man. My kind of final thought on that was just can GPT-5 create a coding
*  problem that even GPT-5 can't solve? The answer is probably yes, but also in a way that kind of
*  leads you to superhuman coding in a pretty likely way, right? It's definitely easier to specify the
*  problem that it is to come up with the solution. So could GPT-5 create demanding coding problems
*  that itself then could then try to solve and then train on the ones where it's working and whatever
*  that formula seems like it is almost sure to work. Yeah, recursive self-improvement just seems like
*  a tipping point where at some point RSI starts working and it was clear it wasn't even close
*  to working the GPT-3 and the GPT-4. You see the glimpses, but ultimately I don't think it would
*  work. I've seen a number of papers where there has been this change between 3.5. A lot of times the
*  self-critique and attempt at self-improvement loop makes it worse. And then with GPT-4, it'll get
*  better, but it'll plateau after three to five rounds. That's been the thing in program improvement
*  and also like chemical reaction improvement. It levels off on three to five cycles, but notably
*  that's not involving any retraining. So it seems that's when the loop really could start to be
*  closed in a true takeoff sort of way. All right. Well, it's a pretty nice journey that we're taking
*  people on here because from the bull case of there's so much data, only this small amount should work.
*  We've got all these different modalities. These things should be able to do all these different
*  things in an integrated way. But on the other hand, wait, we don't have an obvious path to
*  a thousand X that if that's what it were to take. And so then the question becomes,
*  can we actually create a curriculum that gets the right grokking going on early enough in the cycle
*  that you get the superhuman capabilities that you either hope for or fear? This has been cool.
*  I'll walk around now, like doing these sorts of numbers more. And I think more people would
*  do really well to be able to do that kind of quick sanity checking on order magnitude basis. So
*  hopefully we'll help people do that for now. Nick Gannon, thank you for being part of the
*  cognitive revolution. Yeah, thank you. It is both energizing and enlightening to hear why people
*  listen and learn what they value about the show. So please don't hesitate to reach out via email
*  at tcr at turpentine.co or you can DM me on the social media platform of your choice.

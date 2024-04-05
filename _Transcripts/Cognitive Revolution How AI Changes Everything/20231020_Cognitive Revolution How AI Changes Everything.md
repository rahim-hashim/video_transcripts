---
Date Generated: April 02, 2024
Transcription Model: whisper medium 20231117
Length: 3790s
Video Keywords: []
Video Views: 532
Video Rating: None
---

# The Future of the Transformer Pt 2 with Trey Kollmer
**Cognitive Revolution "How AI Changes Everything":** [October 20, 2023](https://www.youtube.com/watch?v=2QGQWWA3mVU)
*  No less than Imad Mostak from Stability said, brilliant researchers like this literally knock
*  10% off of global training compute needs with these improvements, which are impossible to predict.
*  10 million tokens starts to give you the opportunity to put like whole bodies of
*  literature into a single token, right? I mean, the great Gatsby famously fits into
*  Claude's 100K. Now you're talking perhaps about 100 books with full attention
*  considered for the next token generation. If this allows the models to make those connections at
*  such huge length, this could be where you could start to see tipping into superhuman performance
*  of like learning things that experts don't know. Hello, and welcome to the Cognitive Revolution,
*  where we interview visionary researchers, entrepreneurs and builders working on the
*  frontier of artificial intelligence. Each week we'll explore their revolutionary ideas,
*  and together we'll build a picture of how AI technology will transform work,
*  life and society in the coming years. I'm Nathan Labenz joined by my co-host Eric Torenberg.
*  So then the next one is think before you speak is the name of this paper. And training language
*  models with pause tokens. So think before you speak training language models with pause tokens.
*  This comes out of Google and again Carnegie Mellon collab. And this was, I guess, a student from
*  Carnegie Mellon who's interning at Google. It's amazing how many of these papers are like
*  couple month processes. And you know, you can do this kind of stuff in the context of a summer
*  internship these days. Amazing. So what do they do here? They start off with an observation,
*  which is a pretty simple one on some level. I'll quote this from the paper. Language models
*  generate responses by producing a series of tokens in immediate succession. The K plus one
*  token is an outcome of manipulating K hidden vectors per layer, one vector per proceeding token.
*  What if instead we were to let the model manipulate, say, K plus 10 hidden vectors
*  before it outputs the K plus one token. So basically just like, especially in the early
*  going, but you know, kind of any time, you only have a certain amount of computational space to
*  move information around. And maybe that's just not enough or maybe more could be beneficial.
*  First thing that comes to mind for me when I hear something like that is, I think that's a lot of
*  what's happening in the chain of thought type prompting. You know, certainly that's been
*  hypothesized that like, by giving the model, you know, time to think, you give it time to kind of
*  work its way through things and, you know, hopefully summon the right reasoning.
*  And then you get better results. So certainly empirically, we see that you get better results.
*  Well, this is now saying, okay, what if we just gave it extra space, but we didn't make it do
*  anything with that extra space. I'm not asking for reasoning. I'm just giving it a pause token
*  that it can just literally put a pause in when it feels like it needs to, you know, and how exactly
*  that gets decided is a bit of a black box. And that's, you know, there's some trade offs here,
*  I think for sure. But give it that opportunity to just take a pause when it needs to. Now it can just
*  process information a little bit more. It could, you know, potentially do a couple of pause tokens
*  in a row if it needs to. They suggest, you know, what about 10, K plus 10? So 10 extra
*  vectors that it can kind of manipulate and move information back and forth between.
*  Does that give us the opportunity for better performance? And obviously, you know, this makes
*  the research roundup because indeed they show that they are able to improve performance on this.
*  So first thing on this, I was like, well, I saw that one coming. There's the first thing
*  we covered a little bit of the backspace paper on a couple earlier episodes. That was a Stanford one
*  where they had shown that, and this kind of combined some concepts from the last one too.
*  In the backspace one, when they got out of distribution, as measured by like not having
*  high confidence on any next token, then they started to train the model to use the backspace
*  to go back and be like, well, we kind of, we must have gotten off the rails here a little bit because
*  now we're not confident of what to do next. So let's instead go back, try that one again,
*  maybe make a different prediction this time. And then maybe that will lead us towards something
*  where we can feel more confident. When I saw that, it was like, well, it seems like you could
*  probably have a, you know, if you can go back one, you could probably just add a padding one too,
*  and just kind of quietly think to yourself. Sure enough, 60 days or so later, here's the publication.
*  Was this inspired by that? I'm not sure. It was kind of on the border where like it,
*  there was just enough time for them to have done it, you know, in response to that. But I would guess,
*  honestly, they probably had the idea before. So it's probably independent, you know, kind of parallel
*  lines of thinking. So it was like, okay, cool. You know, that's good confirmation, you know,
*  that I'm starting to build some intuition about this kind of stuff. But then as I think about it
*  more, I'm like, boy, do I like this? Do I not like this? I like chain of thought in that I can
*  at least read what it's outputting, you know, and when I can read what it's outputting, then I can
*  be like, well, if the reasoning is wrong, then no wonder the answer is wrong, you know, so I can kind
*  of maybe go back and coach it on the reasoning a little bit more. Here, if you're just using these
*  pause tokens, which is what they're kind of doing in the experiments, they show that, you know, it
*  works. But you've kind of lost the step in terms of interpretability, because now you don't have
*  this reasoning that you can examine. Instead, you just have this pause. And like, yeah, it improves
*  performance. But what's happening there? We don't really know. We just, you know, again, we're back
*  to, well, we can try to look at the activations and figure it out that way. But you know, it
*  certainly is nice to as a practitioner, definitely, to see this kind of reasoning that you can audit
*  and, you know, kind of get comfortable with seems to be approaching the problem in the right way.
*  Now, like many things, of course, not mutually exclusive. They do show that this it works.
*  It works better if you incorporate it into pre training as well. So there's kind of a, you know,
*  going back and like synthesizing some data, adding pauses into kind of show, you know, at some scale,
*  when pauses are appropriate, that helps it even more. And then I don't see any reason you can't
*  use both of these techniques together, you know, you could have the pause, and then the chain of
*  thought, right. So one thing that I do sometimes worry about a little bit with chain of thought,
*  there's actually multiple worries with chain of thought. One is that there has been some research
*  that shows that it's not always super faithful. You know, that the which is to say, like the
*  answer that you ultimately get is not always as determined by the reasoning as it may seem,
*  or as you may wish. So that can be a little bit complicated, you can't just totally naively trust
*  the reasoning output. So maybe here, you could do something like first pause, and then reason,
*  because I've often kind of thought, well, geez, if my if I force it to give an answer immediately,
*  and that's subpar, and then I, you know, can get better performance by reasoning. Well, don't I
*  still have a little bit of a problem where I'm like, it's immediately reasoning, you know, what
*  if it's not reasoning, right, you know, and I think again, I don't want to analogize too much
*  between human and AI. But in this case, I do feel similarly, right? If I'm
*  banned forced to answer some question, you know, okay, wait, it certainly be advantage if I could
*  think it out. But the same kind of thing, if you're like, you must begin reasoning immediately,
*  you know, I'd be like, can I just think quietly for a second, then explain my reasoning and then get
*  to an answer. So now we've kind of got the ability for the AI to do something similar.
*  I don't see any reason you couldn't train for first the thinking pause, then the chain of thought,
*  hopefully now your reasoning becomes better, hopefully becomes more relevant, hopefully becomes
*  more faithful. And then, you know, maybe get the best of both worlds with kind of combined tactics,
*  you get the you know, the best possible accuracy. How do they train for the pause tokens to output
*  pause tokens? Do they pick situations like with a backspace paper where it's not that confident,
*  and then they say that's a situation you should output a pause token? Or do they have some other
*  method? Because that seems like a hard thing to put in the data. It's not like automatically in
*  the data. Yeah, it's definitely not automatically in the data. So they do it with pre training and
*  also with fine tuning. It works best with the with both pre training and fine tuning, although you do
*  get some lift. Well, it varies, I guess across data sets. When you do both, it's like clearly the
*  best. In some cases, it seems like depending on the data set, it seems like in some cases,
*  just fine tuning makes it better. And in some cases, it makes it worse, because it makes it
*  better more than it makes it worse. But there are a couple of data sets where just doing it the fine
*  tuning stage does make it worse. I'm not immediately seeing how they're preparing the data.
*  Is there, I guess they could just train to always start with 10 pause tokens.
*  Yeah, it looks like it might actually be as simple as that. Because in the inference,
*  it says during inference on the downstream task, we append M pause tokens to the prefix. And as
*  always, we ignore the output of the model until the last pause token is seen. We term this pause
*  inference. So at least when they're testing it, it looks like they're presenting these benchmark
*  questions. And they've got grade school math and common sense and Web QA. And there's like
*  eight here just in the one graph of results. It seems like for those, these are just straight up
*  questions you're supposed to answer. And so they just say, okay, you're going to definitely pause
*  and use these extra tokens. And then it looks like it can add more pauses. And it's still not quite
*  clear how it's learning when to do that or not. You could easily imagine kind of setting up,
*  certainly at the fine tuning scale, a data set that just shows when you would want to pause.
*  There's more work to do, I would say, to generalize this beyond the current set of benchmarks that
*  they're running it on. Because here, they're basically just saying, we're in benchmark land,
*  we're in question answering land. We're just going to give you some pause tokens
*  at the start of your answer and see how you do. And okay, cool. It helps. But when to pause
*  doesn't seem like it is something that the model has fully learned here.
*  And so, yeah, but you can imagine also scaling this up.
*  Yeah, obviously you can imagine probably GP for helping you scale it up, annotate these
*  examples with where thinking breaks would be inserted. I bet it would do that perfectly well.
*  And then next thing you know, it can kind of learn when to do the pause breaks. I would
*  know that pretty well. Again, we've seen that with the backspace. So I would expect that something
*  similar would be possible here too. Yeah, there's one section on appending versus
*  prepending the pause tokens. So it does seem like this is still kind of in the manual
*  manipulation realm as opposed to a fully learned tool or technique that the model can use
*  at its own discretion. Also, again, this was a presumably a PhD candidate
*  working as a student researcher at Google, who's the first author on this paper. So
*  plenty of additional muscle there to take the ball forward a little further.
*  Okay, so that's think before you speak. Next, analogical prompting. This one kind of surprised
*  me honestly, but the more I thought about it, the more it started to make sense. So
*  analogical prompting is presented as yet another improvement in how to just get the most out of the
*  current language models that we have. They compare this explicitly to few shot chain of thought
*  and find that it can beat few shot chain of thought. So this might be the new best
*  prompting technique. And it's also easier to do than some of these other prompting techniques.
*  What they do this time is they ask the model, first they present a problem, then they ask the
*  model to recall relevant examples, and then solve the initial problem. And that's in contrast to
*  few shot chain of thought. Few shot would be, here's a couple of examples, chain of thought
*  would be think step by step, et cetera. Few shot chain of thought would combine both of those,
*  where you have examples and the examples show the reasoning that you want. Here, you're able to just
*  say, here's the question. It's on the model itself to recall the relevant examples and to then cycle
*  back to solving the original problem. So the fact that this gives better performance, initially I
*  was like, wow, that seems weird because since you're relying on the language model kind of a lot,
*  right? When I give it few shots and I show the kind of reasoning I want, then I feel like I'm
*  doing my part. I'm guiding it to where I want it to go and showing it how I want it to behave.
*  Here, it's responsible for generating the examples. This is not a tool used. There's no database here.
*  It's just generating the examples with the same kind of generation as always. And yet, at least,
*  again, we'll see as this gets into the wild, but this is somehow better than chain of thought.
*  How would I understand that? So what I came up with was maybe the right way to think about this
*  is heuristic recall. Maybe what it's doing is it's sort of... And we have got all these results,
*  right? That have this kind of high level conceptual middle layer sort of understanding.
*  Maybe what it's able to do when you say, find relevant examples, is it's able to kind of
*  load this problem into some high level of representation. It's maybe able to do a better
*  job than you are, at least for this particular problem, based on these high level,
*  quite decoupled conceptual representations. Based on that, it seems to be able to then zero in on
*  a really relevant canonical example. And it's seen examples of so many things, obviously,
*  right? That it has a lot there to draw on. So it seems like it's better able to pick
*  the most useful example than your few shot example, especially as you then take that to
*  the diversity of whatever you're trying to do. So if it can locate a better example,
*  and it's kind of memorized or learned the heuristic that solves that canonical example that
*  it's able to load into place, then it essentially could get better few shot loaded from its own
*  memory for this particular challenge than the hard coded few shot that you try to cook up for it.
*  Try as you might, right? So I almost think of this as kind of self-rag,
*  rag being retrieval, augmented generation. And I think I'm going to do another episode on kind of
*  the state of rag maybe in the next week or two as well. But the classic rag setup would be,
*  you have a database, the query, the question, whatever gets sent into the database to find
*  relevant stuff, that gets loaded into context. And then you proceed from there with the benefit
*  of whatever was retrieved out of the database. This is like treating the model itself as the
*  database and saying, you could embed that and go hit some vector database that has a ton of examples.
*  But the model itself kind of represents all those relevant concepts and can generate
*  relevant examples. And then once it has the most familiar kind of happy example,
*  then it can apply the same heuristic to the question at hand. And it works better.
*  Wow. Okay. This is across a number of different models. So yeah, basically it seems like up to
*  the frontier models, this still helps. It's not like a dramatic change relative to other
*  prompting techniques. It is a pretty dramatic change relative to just zero shot, nothing.
*  This is probably most competitive with a good rag implementation. Because I've been building some of
*  these types of systems. I built a first version of a prompt coach for executive assistance recently.
*  And I just did a few shot chain of thought implementation there where this is kind of
*  a meta prompt where the idea is like, the executive assistants don't necessarily have a ton of
*  experience prompting. They may do wrong things. So can we identify things that they're doing that
*  are suboptimal and provide feedback on how to better prompt the AI for better results?
*  It's a little bit like the improver, except we're trying to improve the human's prompts to the AI.
*  My few shot chain of thought is just like, okay, here's a number of prompts, whatever. I just
*  grabbed some random ones. I wrote critiques of these prompts that had these various shortcomings
*  and showed what kind of feedback I wanted. And the system kind of works. And then I written out
*  what are the next things I would do if I wanted to improve this further. And I was like, I think the
*  best performance that we could probably get to would be with a rag setup where I would,
*  instead of using the same examples for every prompt, I would go get specific examples that
*  are most relevant to this. And then we could show, and how big does that database have to be? I mean,
*  that's where it starts to get a little bit scary, because I don't want to have to write a thousand
*  of those by hand. And that might not even be enough. I don't know. My few shot examples, just
*  four or five, that was manageable enough. But a thousand, that's a different scale of project,
*  for sure. Of course, I'm going to have GPT-4 help me, but it's, we'll actually use Cloud Instant for
*  that, interestingly enough, because it's quite a few tokens. We need the long context window.
*  And the Instant is really good for the responsiveness and seem to be performing
*  almost as well as Cloud too. It was like at 10% of the cost and a lot faster.
*  I decided to go with the cheap one. But anyway, this now starts to suggest
*  maybe a different approach where maybe I don't have to do this whole rag setup and have a thousand
*  examples and go find the most relevant examples. Maybe I can just have the language model recall
*  the most relevant examples and then have it go from there. If there's one thing that that's
*  probably not going to work on quite yet, it might be meta-prompting, because it certainly has seen
*  the types of questions that are being asked in this study, which are grade school math again,
*  and that kind of thing. When you flip over to improving prompts, depending on the training data
*  cutoff or whatever, has it seen huge numbers of prompt coaching in its training data? Maybe it
*  hasn't. If it has, it's probably because they've consciously baked that in as opposed to it being
*  out there on the internet as of the training data cutoff. That does seem like something that
*  Anthropic might be a little head on, because they do have this constitutional approach where
*  there is this more iterative internal sculpting. Obviously, OpenAI has a lot of that too. But
*  anyway, that's my next test on my prompt coach is to see, hey, maybe I can skip this whole
*  complexity of the rag setup by just having the AI itself recall the most relevant example.
*  Heuristic recall is my own name for this, because once it has that example and it knows how to solve
*  that problem, then we move pretty smoothly into applying that same heuristic to my particular
*  challenge. One of the examples that they show in the paper is finding the area of a square or
*  something like that. You can think about this. It's fascinating. It's weird, but again, it has
*  a certain logic. You can see how this would make sense for yourself. If you're like, okay, I'm a
*  middle school math student. I've been presented with a find the area of this square. What am I
*  going to do? Am I going to look at four other math problems with reasoning and be like,
*  now I understand what to do? Not exactly. Not if none of them are finding the area of a square.
*  What I'd really do is be like, okay, how did I find the area of a square? Let me recall that.
*  Let me recall the simple example. Now I'm going to apply that to the particular numbers and
*  details of this particular problem. It does seem like a little bit more human-like behavior
*  because that is more like what I would imagine myself doing internally if I was trying to solve
*  a similar problem. I'm going to look for the one that is most analogous, recall how I did it,
*  and then proceed in the same way. That's available for free everywhere you want a prompt right now,
*  by the way. That's crazy. It's interesting that performs better than giving it a few
*  shot examples. It just seems like another data point of just because you don't find something
*  in the model with an IE prompt doesn't mean it's not in there somewhere and that there's some work
*  to coaxing out the full capabilities of the models. Yeah. Another little tiny detail of this is they
*  seem to be using Markdown for the instructions. I just saw some chatter online the other day from
*  a couple of people that are definitely super knowledgeable who said that Markdown works best
*  for OpenAI because that's how they tend to train stuff in their own processes and XML tags seem to
*  work best for Claude. That is something that Anthropica officially recommends is use XML tags.
*  Just another little footnote, Markdown for OpenAI, XML for Claude. Your mileage may vary on that,
*  but this is showing the Markdown format. Even for GBT4, you're squeezing out a couple more
*  percentage points on these math benchmarks. Pretty incredible. It works almost across the board.
*  I think they show one thing basically where it's not the very best. In that case, it's like 0.4
*  percentage points lower than the chain of thought. But in every other thing that they show, it's a
*  couple of percentage points as much as like 5 percentage points higher. Yeah. Go improve your apps.
*  I believe in Omniki so much that I invested in it and I recommend you use it too.
*  Use Cogrev to get a 10% discount. All of these things, I said earlier, we're climbing a level of
*  impact, conceptual importance, perhaps whatever. Now we're getting to a couple of things toward
*  the end that I think are definitely pretty interesting, pretty notable. There's two
*  papers that specifically speak to the possibility of much longer context windows and they do it in
*  quite different ways. The first one is called Streaming LLM. This is a paper out of Meta.
*  The supervisor, Mike Lewis, you'll see his name on quite a few of the big Meta papers.
*  Basically, what they do here is they manage to extend not the context window exactly,
*  but the length of text that the language models can handle dramatically with just a relatively
*  superficial change in a way that applies to all the existing open source models. They're able to
*  show that this technique can be quickly retrofit to Blamma and all the other, I mean, all but like
*  a lot. They've shown multiple different major open source models that they apply this technique to.
*  It works across these already existing trained models out there in the wild today.
*  What are they doing? It starts with this observation that it's another one of these things
*  where you're like, wow, that is a pretty simple observation. I'm kind of surprised nobody noticed
*  that before, but you made a lot of hate with it. The observation is that there's this,
*  they call it attention sinks, but let's just start with the purely observational.
*  What they find is that as language models are making their predictions, the late tokens,
*  often they attend to tokens that are very close to them. Often, just one of the words immediately
*  prior, which makes total sense, right? Because if you're just thinking, okay, I need to predict
*  the next word, well, the most important words are going to be the ones that just came immediately
*  before just for even simple things like part of speech and just general continuity. You're going
*  to see this intense attending to the immediately preceding tokens. Then you see random, but not
*  that much attending to things that are farther back because most of the time, and again, just
*  kind of sanity checking yourself, if you were going to try to predict the next word in a paragraph,
*  you'd be looking at those last few. You'd be maybe read the whole thing, but a lot of the
*  details in the middle paragraphs, they're probably not super hingey for what that next word is going
*  to be. There's not a lot of attention into these middle things, although key things do matter.
*  Then there's a lot of attention for many tokens. There's a lot of attention to just the very first
*  tokens in the sample. Why is that? It doesn't seem like it's super influential,
*  but what's going on? The hypothesis that they come up with is that
*  because of the mechanism where the sum of the attention for a given token across all earlier
*  tokens has to sum to one, that's a constraint of just the way everything is calculated in the
*  computation, the attention has to go somewhere. If there's nothing for a given token that is super
*  relevant, still the attention has to go somewhere because it's required to sum to one.
*  They hypothesize that these intensive attentions to the very first tokens are what they call
*  attention sinks. In other words, you've got to have this thing sum to one, but there's not really
*  much here that seems super relevant. Just put it at the beginning and then we can somehow, some other
*  part of the network can not pay too much attention to that. Not to use attention in different ways,
*  but I am. We're talking here about the proper attention mechanism. I'm just saying downstream,
*  it seems like that high level of attention paid to the first few tokens is somehow accommodated for
*  in such a way where it's expecting that and it's fine downstream performance-wise.
*  Is say, well, what if we, and there's been a lot of different techniques over time that have tried to
*  figure out, well, how can I have an ongoing, how can I have a long running conversation with a
*  language model? Especially when it was 2,000 tokens limit, you'd hit that limit pretty quick.
*  Now with GBT-432K, with Claude 100K, you don't reach it super quick, but it's still nowhere
*  near enough to have a super long running dialogue. People have tried various things.
*  One thing that folks have tried is a sliding attention window where you basically just only
*  look back and tokens and everything before that, you just forget about. That doesn't work for
*  some reason. I don't think it was necessarily clear before this why that wasn't working.
*  I'm sure it's entirely clear even still with this, but as an empirical matter, what they find is that
*  if they keep the first however many tokens, which they now call the attention sync tokens,
*  and they experiment with some different things where they even just put some padding there,
*  put some empty stuff so that there is this designated place. Again, this is another thing
*  where if you can just do it, but if you do it with pre-training, then it will work even better.
*  I don't think we've seen the end of this, but keep those early tokens, those attention sync
*  tokens there at the beginning, and then do the sliding window. Now it works. Now you can basically
*  keep essentially the same level of model performance way beyond the actual context window that you have.
*  Somehow the ability to put this extra attention that doesn't really have any other natural place
*  to go back to these early starting attention sync tokens that don't change allows the models to stay
*  coherent, where otherwise what had been observed is as soon as you get past and start to drop some
*  of those early tokens, the thing blows up and doesn't work anymore. Now it kind of
*  stays coherent. You're still dropping, as you get to a long enough thing, you're still dropping
*  the middle stuff. So if you have a 32K model and you've got 40K worth of text, you've got the
*  initial attention sync tokens, then you're skipping 8,000, and you're just looking at the last 32,000.
*  But the ability to not have to force everything into that window and continue to put some stuff
*  toward the beginning into the attention sync allows it to basically stay consistent perplexity
*  score for super, super long transcripts. And we're not talking about a small difference in
*  transcripts here. We're talking going into millions of tokens. This goes a long way.
*  So it is a little confusing. I think I want to understand this a little bit better. Notably,
*  it seems like the perplexity is staying basically flat. It does not seem like it's getting better.
*  And I think that's consistent with the general understanding that, okay, for any given time,
*  we are only looking back at our 32K or our 8K or whatever our attention window is. So anything that
*  is being dropped before that, we're not able to take advantage of. So we're still kind of operating
*  at a 32K or an 8K capacity, but we're able to slide that window out into the future.
*  This could create some odd experiences for users if you're like, well, I had some interaction about
*  this particular topic. Is it still in window or is it now out of window? That could be kind of weird.
*  You could have some situations where it's like remembering, remembering, forgetting
*  the perplexity score as measured on these super long text things, doesn't show a pain point there.
*  It's just kind of humming along at consistent whatever perplexity it can achieve with its 8K
*  or its 32K look back, that's what it can do. And it can just now continue to do it on a rolling basis.
*  But from a user standpoint, that might be somewhat weird if all of a sudden something you did just
*  know about now you no longer know about. So I don't think this is exactly the form in which
*  this is going to hit production. But I do think it could be a pretty powerful
*  aspect of something that I think could start to look more like a next generation system.
*  Why do you think the beginning tokens are such more effective attention sinks than just
*  whatever tokens are at the beginning of the sliding window?
*  I don't know. It's odd. Maybe they just don't look like a beginning. That's kind of the best
*  thing I can come up with. I mean, I do think you could say their hypothesis was pretty minimalist.
*  It was just they were phrasing questions slightly differently. Like why would the attention sinks
*  be at the beginning? And the answer was, well, the beginning is the stuff that all downstream
*  tokens can see. So that's a natural place for that to go. So if you start with the notion that
*  you need an attention sink, then it seems reasonably intuitive that it would be at the beginning.
*  Why the attention sink behavior doesn't roll with you as you roll the context window through a long
*  text. I don't have a great intuition for that. And I was trying to come up with something. And
*  I think that's the best I came up with. Just that maybe it doesn't look like a beginning.
*  And maybe things that look like beginnings are kind of what it's looking for when it's doing that.
*  And if you're kind of right in the middle, maybe it just gets straight up confused. This may be a
*  reflection of kind of how things are pre-trained. It does seem consistent across these models.
*  So they've published, I believe they've already published the code. They have published that,
*  they have published that, yeah, the code is out there on GitHub. So this is a framework
*  that you can apply to existing language models. And they show that they are indeed applying it to
*  Lama2, LongChat, a few different ones in here. It seems like it's a lot of Lama2. This is out
*  of Facebook, but there were others that were not like Falcon, MPT. So quite a diverse set of
*  different existing open source models that they've done this for. And it seems to work
*  comparably well, basically across all of them. The perplexity looks pretty similar. It looks
*  pretty flat. I was thinking, maybe it has something to do with how they're trained,
*  the way that the text is run through them. If it's always kind of chunked in ways where it's
*  like starting with something that kind of looks like a beginning, then you could kind of understand
*  this behavior where it needs the thing to look like a beginning in order to use it that way.
*  I would be curious if there's a model, and I don't know, people don't really
*  disclose their full pre-training mix super often. But if we could find a model where
*  they specifically start in the middle in pre-training, and just kind of take random
*  starting points that could be mid paragraph, mid sentence, whatever, and just try to chop it up
*  very noisily like that, maybe that could be a way in which the rolling window could work better.
*  And then maybe you wouldn't even need the attention sync dedication tokens. Maybe that
*  attention sync behavior could roll. But I don't know of any models like that. And I don't even
*  know that we would know even for these models that they study, because often that level of detail is
*  just not disclosed. That's my best guess as to what is going on there. And again,
*  this works on existing models, right? So now we're not far at all from people being like,
*  oh, hey, I'll take my llama to whatever and just apply this framework. And now you can have running
*  chat long lived as long as you want. You don't hit that hard. The kind of user experience trade-off
*  would be today you hit a hard end, and it's the end. You got to start over. Next generation,
*  with just applying this, now you can run forever, and it'll at least stay coherent,
*  but you're going to have amnesia for stuff that has now rolled out of the window. But it's not
*  catastrophic amnesia where you get totally insane right away, but you may have these kind of
*  weirdnesses where you're like, when is that thing in or out? And how is that affecting me? And
*  it definitely could create some strangeness. But again, I think there's a synthesis of almost
*  all of these things coming. Again, keeping in mind that you can train a GPT-4 model in a week if
*  you're an inflection. Once you get all your stuff online, combining a lot of these techniques into
*  one is, I think, into one model is definitely not too far into the future, and certainly doesn't
*  feel like science fiction at this point. So one more paper, and then I'll kind of sketch that out.
*  So the last paper, ring attention. This one is the deepest tech. It's really at the intersection
*  of hardware and algorithm. And no less than Imad Mostak from Stability said that the researchers,
*  he's like, brilliant researchers like this, literally knock 10% off of global training
*  compute needs with these improvements, which are impossible to predict. And I honestly don't even
*  think that's necessarily an exaggeration. But for one technique to potentially chop off 10%
*  of global compute needs means that probably just a lot more is going to happen. I don't think we're
*  going to make any fewer H100s instead. Just more is going to get done with them. So how does this
*  one work? I caveat this one by saying I'm definitely not a big expert here. But one thing that is
*  interesting to know about transformers, particularly, and more generally, like models
*  in general, is you can represent them in different ways. And that could be like, obviously,
*  you could represent them in code, which is how they're ultimately kind of represented. You can
*  represent them in linear algebra notation. You can represent them in diagrams. And different
*  representations have very different tradeoffs in terms of the intuition that they help you to
*  develop on the one hand, and then the actual compute efficiency on the other hand. So I think
*  Anthropic has made great use of this in some of their research work, where they're like,
*  nobody would compute with this representation. But we find this representation to be the most
*  intuitive for how we want to think about what is actually happening in the transformer. So we're
*  trying to decoupling how does the machination actually happen, subject to the hardware and
*  the RAM and the layout and all that stuff, from the way we want to organize our thinking about it
*  in our heads for intuition building purposes. So just separating those, for one thing, is a pretty
*  important conceptual move. And what these guys have done is they have restructured the computation,
*  seemingly identifying that the current bottleneck can be worked around. Now there's going to be,
*  of course, some next bottleneck. But the next bottleneck seems to be a much more appealing
*  overall bottleneck. So they are restructuring the compute. They're notably, this is not a shortcut,
*  it's not an approximation. This is still fully literal attention computed to the same level
*  of precision with no shortcuts. It's just a more efficient way of structuring that compute. And
*  basically it amounts to passing different things back and forth between devices instead of other
*  things that used to be passed back and forth between devices as all this kind of information
*  is flowing. Because you've got the parameters of the model itself, you've got the data that's
*  being represented and flowing through. If you're doing training, you've got to keep in mind all the
*  gradients as well. If I tweak these things, how is that going to change so you can do the
*  back propagation? So you've got huge memory requirements and also huge data passing requirements
*  between devices. So by optimizing this in a new structure, basically, here's a couple of key
*  quotes. Ring attention lets you scale context length linearly with device count, breaking free
*  from memory constraints. Scaling context doesn't mean a quadratic increase in flops per data set.
*  For the GPU rich, you can go from 4,000 token context to 10 million token context on a 175
*  billion parameter model for 150 times the training compute. What is that? That's a 250
*  increase in the context length, which we've all been kind of taught, well, attention scales
*  quadratically. But with this reorienting of how things get passed around, it costs you 150
*  times more compute, which is not even the 250x that you're getting in terms of the expansion
*  of the window and certainly nothing like 250 squared. So it does cost more to train a 10 million
*  token thing versus a 4,000 token thing, but only two orders of magnitude more. And it's not like
*  running away with a quadratic function. Then they also say for the GPU poor, if you have just
*  eight GPUs, then you can expand your context by eight at just two times the cost. So if you were
*  going to train a 4,000 token context window on eight GPUs, now you could train 32 and it would
*  only take you twice as long. That's a pretty huge difference in terms of utility between a 4x and a
*  32 for just 2x the compute. And again, not an approximation, right? This is the full attention
*  every token to every token. So what I think is really incredible about this is, you can only
*  put so much into the current token limits that we have today. And that's important at runtime,
*  certainly, because you can only pack so much in there. Beyond that, it just can't handle it.
*  I think it's also probably pretty important at the training layer. And I recall Illya from OpenAI
*  giving this example of like, I think maybe you even mentioned this in one of our earlier
*  discussions about the mystery novel, where it's like, you have maybe hundreds of pages,
*  thousands, it could be an epic, right? You can have thousands of pages, all leading up to,
*  and the person who did it is blank. And if you could only have read the last chapter,
*  you're going to struggle. If you've read the whole book, you can do a lot better.
*  So the longer the window is, the more opportunity there is to, yes, infer effectively, but also to
*  just learn connections between things that are potentially quite remote from each other.
*  10 million tokens starts to give you the opportunity to put whole bodies of literature
*  into a single token, right? I mean, the great Gatsby famously fits into Claude's 100k.
*  Now you're talking perhaps about a hundred books, a hundred books, all being with full attention
*  considered for the next token generation. Now, would you run that at runtime for inference?
*  Like probably not. I think it's probably more impactful for training. If I really want to get
*  into science, if I really want to start thinking about how can I use language models for a book,
*  understanding DNA interactions, things that are really data heavy or where there's just so many
*  possibilities for connections that are just not obvious, then the 32k or the 100k is still just
*  not enough to do that. You need more than one great Gatsby worth of stuff to start to draw these
*  really far-flung, non-obvious connections. But at 10 million, and there's no rule here that says it
*  stops at 10 million. It's just that that's the one example that they gave. At 10 million,
*  you can start to load up really pretty serious amounts of data. And my guess is that of all the
*  things we've talked about today, this would be the thing that would start to drive overall lower
*  perplexities. When we talk about the sliding one, even with these attention sinks, the perplexity
*  is basically flat. That just means model confidence, the performance is basically flat,
*  but that's rolling. Now you really allow it to learn from 10 million tokens at a time.
*  There's just so much more input there that it can learn from, so much more opportunity to make
*  huge, different, long distance connections between things. It seems to me like this could be a huge
*  unlock. And again, to put that at two orders of magnitude, let's say you've got your GPT-4 today,
*  and we know that again, I keep coming back to that maybe that takes you a week, two orders of
*  magnitude up from that would be a hundred weeks. That would be two years. There are a lot of H100s
*  getting shipped. We're not necessarily that far from being able to train a GPT-4. It starts to
*  get it to be a different class of thing, I think, at 10 million tokens per thing for it to learn from.
*  That's just so ridiculous that this feels like the thing where maybe you could see your way into
*  superhuman performance. Just because I can handle the whole great Gatsby, I can remember what I read.
*  I would put myself up against the language model for making that guess as to who done it at the
*  end of the mystery murder, but you now give me 10 million tokens. I can't hold that. I can't do
*  100. I cannot do anything analogous to full attention for a 10 million token thing.
*  And so if this allows the models to make those connections at such huge length, it seems like
*  this could be where you could start to see tipping into superhuman performance of learning things
*  that experts don't know. And if you're learning things that experts don't know, now you're really
*  into a whole new era. That's probably the biggest threshold that everybody's wondering if and when
*  we might cross. And I would say there's a decent chance in my very subjective estimate that
*  this could be the thing that could unlock the ability to learn things that experts don't know.
*  Yeah, the paper seemed really cool. And I mean, I know for me personally, it'd be amazing to be
*  able to load in an entire script and ask it, are there any logical inconsistencies? What
*  holes can you see? What should I work to improve? Which isn't possible right now with
*  this current size of the context windows. I also wondered, I just glanced at the paper last night
*  after you sent it. It seems like the key breaks the context up into these blocks.
*  And then the key value pairs get passed around the full ring of all the different blocks. So you still
*  calculate the full all to all attention. No shortcuts is my understanding. And I think
*  that's what you just said. Yeah, no, that's my understanding too. It's just less memory. I think
*  memory has been the current bottleneck with previous approaches. And now I'm not actually
*  sure what the next bottleneck becomes, but you know, they're getting around this
*  memory bottleneck. But I also do wonder if you really need to pass the key value around the
*  entire ring. If each block could only see its neighbor, then each layer, each block, its field
*  of view of the input grows exponentially. So I do wonder how much you really do need to pass it all
*  around the full, the full ring and how much you could just do attention somewhat locally in blocks.
*  And then each layer, each block would see more. Cause like when I read a novel, I'm not thinking
*  how much does this word the compare to like this word, you know, the name Justin 18 chapters earlier,
*  but you build up almost hierarchically each section of the, of the context.
*  And again, there might be a difference here between training and inference. If you're trying to get a
*  model to learn things that experts don't know, then kind of by definition, you have to like crunch a
*  lot of shit, right? Because you don't even really know what you're looking for, but at runtime,
*  yeah, you don't, you know, there's probably a lot of shortcuts that you could take.
*  So, you know, here's kind of my sketch for where this might be going, you know, just based on all
*  of these results, like what does the language model look like? And by the way, we're, you know,
*  we touched briefly on multimodality and vision toward the beginning, but this is not even to say
*  like everything, but just kind of the stuff that we've, you know, marched through today.
*  How does that end up looking if it's all kind of combined into, you know, a single system that,
*  you know, that has all this stuff? I mean, for one thing, it might be just way more capable if this,
*  you know, 10 million or whatever type of learning does allow it to learn, you know, more, a more
*  nuanced representation of the world, then you might just have straight up higher capabilities.
*  My guess is though you probably end up running it with a smaller kind of, you know, more manageable
*  inference window most of the time. From the paper of the attention things, it seems like you can
*  vary attention kind of on the fly. You know, they're like padding a few more tokens here,
*  whatever it seems like. We may be looking at something in the not-too-distant future where
*  there's a ability to adjust the context window depending on exactly what you're doing. And
*  sometimes you may need it to be longer and sometimes you may be fine with it kind of rolling
*  because I'm not, you know, if I'm having a single long running dialogue, I'm not going to be like,
*  you know, if I'm having a single long running dialogue with my AI, you know, assistant,
*  most of the time I don't need the way old stuff, but occasionally I do. And, you know, that might be
*  something that could be kind of used dynamically on the fly. The thing that I think is kind of
*  most interesting though that isn't quite here yet, but really is I think strongly suggested,
*  is some sort of retention built into the transformer. You know, trying to combine these
*  ideas, you've got these attention things at the beginning, then you can kind of skip a bunch of
*  stuff. We've seen that you can like have a pause token that allows you to think more and kind of
*  just represents like more ability to kind of process and store information. Then there's the
*  backspace. We could, you know, we get out of distribution, we're not happy about something.
*  We can back up. It seems like the rolling window probably is the way, but that there's some sort
*  of like highly compressed historical record that kind of comes to represent and allow you to retain
*  information from stuff that is no longer in the context window in a way, kind of like what you're
*  describing where it's not necessarily every word, but it's like a higher level of representation
*  that you can carry forward with you. It doesn't take that many tokens, but is like beyond the,
*  you know, in the way that the pause is like beyond a token and just kind of represents
*  space to store stuff or to process stuff, a place to store stuff that is kind of the historical
*  record. That seems to be the next big thing that I'm really looking for that all these other kind
*  of tools and techniques would start to be able to take advantage of. And you can even imagine the
*  real self-rag would be like, okay, you know, I've got these attention tokens at the beginning. I've
*  got like these sort of historical compressive representations of like history. Now I've got
*  like the conversation we're currently having loaded into memory. This is starting to sound like a lot
*  more, you know, like what I feel like I experienced on a day-to-day basis. And then I kind of imagine
*  like, oh, I'm attending now to this like slice of history, right? There might just be one or a
*  couple of tokens in terms of its size of representation, but which then corresponds to,
*  you know, the real self-rag would be, and here's the whole history that underlies that. So that,
*  you know, we see the pause, we obviously seen many tool uses, but can you imagine something where
*  as this history gets kind of compressed and added in on a padding basis toward the beginning,
*  you could also start to identify, hey, I need that section of history in more detail for this
*  particular thing. And I can see that because I can see the meaning, not necessarily at the token
*  granularity level, but then I can call up the token granularity level, load that into my current
*  context and, you know, get the granularity that I want based on recognizing that some
*  portion of previous history, which has been compressed into a few tokens worth of space,
*  is what I need to, you know, to draw on to do the current thing. Honestly, that does not feel far
*  off. It feels like, you know, if we're sitting here six months from now and we haven't seen
*  something like that, I would be quite surprised. You know, a version of it sort of was the retnet
*  paper, but it notably was like, there's a change to the architecture there and we'll see how well
*  that generalizes. But what I'm kind of describing here seems like something that you could have
*  even without, you know, any kind of additional fundamental architectural changes, but just like
*  a training for this kind of compression for future recall that, you know, you could still kind of
*  attend to in the normal way, pluck it out as needed, not even necessarily have to go to the
*  database all the time to have like the conceptual backing, but the ability to go to the database
*  sometimes when, you know, that seems like it's super relevant. So you're saying like, like a
*  memory just in language that you could then treat as like a database that you can recall certain
*  slices from it. You don't, you're not even saying like some hidden state in latent space, like,
*  you know, the old LSTMs that it's also carrying forward.
*  Yeah, no, I sort of like that. So like by analogy to the pause and by analogy to the backspace,
*  every so often, I think you could train the model to represent some token that would be like
*  a memory token that would represent the high level conceptual content of that memory
*  that then could just be included as context, but super efficiently
*  and not have to take up a ton of tokens, not have to have token level resolution,
*  but which would kind of, it would be in still the same latent space as the model is operating,
*  but not necessarily accessible via direct tokens, but only sort of the kind of thing,
*  kind of like the pause where, you know, this gives you an extra space to like put manipulative
*  do stuff with data here that the purpose of it would be to say, I want to kind of summarize
*  this not in text, but in some representation in the space that I can come back to later,
*  super efficiently at like high conceptual meaning, but like low resolution in terms of the actual
*  exact language that was used. Very cool. We know that we're not at the end of history.
*  And that's kind of, if I had to guess what would be the next big thing that would unlock a ton of
*  stuff, it would be that kind of, you know, it seems like we're so close to all those pieces being
*  there with the rolling and, you know, with the pauses, with the backspaces, with the like kind
*  of version of self-rag that we're already seeing. Imagine that self-rag thing had these memories
*  that it could go back to, you know, as well, right? So now it's not just looking at its own
*  pre-training, but like also the conversation that you had and able to say like, it looks like,
*  you know, on this slice that represents this whole exchange, you know, it looks like that is where
*  this was kind of, you know, covered. And so maybe that's enough. Maybe I have to go deeper into the
*  actual transcript, but either way, you know, to be able to, to compress and kind of, you know,
*  in a way that I think would start to represent, would start to look more like what we're doing,
*  right? Because as you said, you're not keeping every word of the novel in mind, but you have
*  these kind of vague associative high level, more representational, not token by token sort of things
*  that are like much more easy to recall. And of course you don't have the actual, you know,
*  token by token at your command. But, you know, that's another reason I think superhuman performance
*  definitely cannot be ruled out because if we can figure out the high level of representational
*  thing that's more like our kind of loose, but like really relevant memories, then it'll be
*  way easier to connect the computer's version of that to the actual raw transcript
*  than it is for us, you know, to go back to our, you know, raw transcripts, which, you know,
*  obviously we just basically usually don't have. Yeah. That's where I think this is going. That's
*  super confident, but I'd, I bet we see some of this. It makes sense to me. And it feels like,
*  I mean, if we figure out that recall element and then add in some planning algorithm
*  and a little bit of scale, more scale, major breakthroughs.
*  Yeah. The timelines are not necessarily very long. I think it's more I think about it,
*  the more it does seem like the next couple of years could get really, really crazy. It's been
*  fun. Any concluding thoughts on your end? No, this is very fun. And, you know,
*  that I'm working all day. This was a great way to catch up on what's been happening.
*  Well, that's the goal. It's too much for any person, you know, and this is by no means
*  everything, but trying to give the, you know, that kind of middle depth where hopefully people walk
*  away with some real understanding and, you know, some, you know, some real food for thought,
*  but can hopefully do it, you know, in a compressed way that, that allows people to get a survey of
*  increasingly crowded and noisy landscape. With that, I'll say Trey Colmer, thank you for being
*  part of the cognitive revolution. All right. Have a great day, man. It is both energizing
*  and enlightening to hear why people listen and learn what they value about the show.
*  So please don't hesitate to reach out via email at tcr at turpentine.co or you can DM me on the
*  social media platform of your choice. Omniki uses generative AI to enable you to launch hundreds of
*  thousands of ad iterations that actually work customized across all platforms with a click of
*  a button. I believe in Omniki so much that I invested in it and I recommend you use it too.
*  Use Cogrev to get a 10% discount.

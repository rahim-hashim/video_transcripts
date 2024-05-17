---
Date Generated: April 03, 2024
Transcription Model: whisper medium 20231117
Length: 4629s
Video Keywords: []
Video Views: 917
Video Rating: None
---

# OpenAI Fine-Tuning Update, Acceleration Debate, and Bundling AI
**Cognitive Revolution "How AI Changes Everything":** [September 26, 2023](https://www.youtube.com/watch?v=o6mOZ-AOptU)
*  somebody, you know, friend of a friend reached out to me with a legal question.
*  I'm like, I'm really not qualified to answer this, but I am qualified to put it into chat.
*  If you see if they were one company, they could have avoided this whole mess.
*  Um, and I spoke to Emil Michael, the chief business officer at Uber.
*  And he was like, yeah, I tried to get us to acquire them to merge because they
*  just didn't make sense.
*  But Travis said we got to kill them.
*  And that Lyft was like, we hate Uber.
*  So businesses just are irrational at the end of the day.
*  And the fact that there's funded by VCs who, and they all have take over the world
*  visions, it's challenging for people to be in a spot of like, hey, you play this
*  niche or hey, you collaborate with this competitor.
*  Hello and welcome to the cognitive revolution, where we interview visionary
*  researchers, entrepreneurs and builders working on the frontier of artificial
*  intelligence.
*  Each week we'll explore their revolutionary ideas and together we'll build a picture of
*  how AI technology will transform work, life and society in the coming years.
*  I'm Nathan Labenz joined by my cohost, Eric Torenberg.
*  Let's kick it off with a GPT 3.5 turbo fine tuning update.
*  Let's do it.
*  It's been just a couple of weeks since the last episode where we covered it in
*  the immediate wake of the release.
*  And you know, it is interesting.
*  I had had, as I mentioned then, you know, explore fine tuning llama two on my to-do
*  list for a little while and then kind of said, yeah, I'd probably scratch that off
*  and do the 3.5 fine tuning instead.
*  And they do make it super easy.
*  You know, I probably at this point in time, wouldn't have still gotten around to
*  doing the llama to fine tuning.
*  Not because it wouldn't have been interesting, but you know, just, okay, even
*  if you do it and you get it to work, then you still have the inference problems that
*  we talked about, you know, where it's like, okay, how am I going to host this?
*  And what kind of load can it handle?
*  And do I auto scale up or down?
*  Who's got a good solution for that?
*  There are solutions, you know, coming, but they're not mature.
*  In contrast, OpenAI just makes it so easy.
*  If anybody, you know, if you've used the previous version of their fine
*  tuning, it's very similar.
*  This time around, they have both the prompt and completion format, which is
*  the old format.
*  And now the primary one is the chat format.
*  So you get to set up your kind of system message, you know, who you want the AI
*  to be, what its job is, and then from there, it's kind of a back and forth
*  between user and assistant.
*  You can set up a couple of examples of the task that you want it to do.
*  And next thing you know, you're, you're kind of off to the races fine tuning.
*  What has been really interesting though, is using GPT-4 to create the
*  data set for 3.5 fine tuning.
*  And we kind of came to that in a couple of steps, but again, I'm doing all
*  this for Waymark, right?
*  So my goal here is we already have a product in market.
*  It works really, you know, relative to anything in the, you know, not
*  too distant past, like amazingly well.
*  You can just tell it what kind of video you want.
*  It will make you that video.
*  Next thing you know, you're watching that video complete with a script, images
*  from your business loaded in, you know, to compliment the, the narrative and
*  even a voiceover layered on top of that.
*  And that all happens, you know, in kind of 20 to 30 seconds.
*  So pretty cool, but obviously, you know, there is still room for improvement
*  in all of these things.
*  Our scripts are often not quite as good as we'd like them to be.
*  And sometimes we see like wonky images chosen where we're like, Oh God, you
*  know, we really rather wish you had to pick something else.
*  And sometimes the voiceover, you know, it's usually well written and like apt,
*  but sometimes it doesn't quite sync up just right with the, you know,
*  the timing of the scenes.
*  And so, you know, there's obvious opportunity for improvement.
*  So it's like, okay, we got a new model.
*  And per what open AI said, as soon as you find tune it, it's available immediately
*  for use and you have the same rate limits as you have with the normal models,
*  which are high, meaning I don't have to worry about scalability at all.
*  I don't know if we're about any hosting complexity, assuming that's true.
*  Spoiler seems to be pretty true.
*  So I'm like, yeah, now if I can just make the model better, I didn't have to deal
*  with any of these other problems.
*  And I can just hand something right over to our development team.
*  That could be a drop in replacement.
*  So what you had before just, you know, switch this model out for this new model
*  ID, everything gets better and that could happen with almost no work from the rest
*  of the development team.
*  So that's like a huge attractor to, okay, let's do this now instead of kind of
*  having, you know, one or two on our to-do list and, you know, maybe getting
*  to it when we have time.
*  So first round we did was, you know, kind of the same thing we'd done before.
*  We just took inputs and outputs.
*  Here's the setup, you know, and our setup is typically here's kind of the structure
*  of the video, here's a profile of the business that also can start to include
*  what are the images available.
*  We represent those as text, just as image captions, starting to use some aesthetic
*  evaluation as well, so we can kind of bracket like these are the, you know,
*  super high quality images.
*  These are the medium ones.
*  These are the low ones.
*  Sometimes all they have are low ones.
*  So, you know, we've got to use what we can.
*  And then here's the user's runtime instruction.
*  You know, typically these are small businesses, so they might be saying,
*  I'm opening a new location or I've got a sale this weekend, or I'm hiring for a
*  particular role or whatever, right?
*  They've got all sorts of different things and it's a long tail, you know, as you
*  might imagine with all these kind of different idiosyncratic local businesses.
*  So we tried the prompts and completions and, eh, not that great.
*  Not that great.
*  Why is it not that great?
*  Um, just not as good.
*  Didn't seem quite as good.
*  I don't know.
*  You know, it just wasn't quite there.
*  So I took a walk and I was thinking, all right, GPT-4 by the way, does this task
*  pretty well with a couple of examples?
*  Do we need just more data?
*  Well, we already have like a decent amount of data.
*  I mean, I don't know.
*  It's our data set is reasonably small.
*  Like it's, you know, we've used anywhere between a hundred and a thousand scripts
*  for most of our fine tuning processes.
*  That's not like big data, but that's always kind of worked.
*  You know, for the last however many rounds.
*  So GPT-4 can do it, you know, it seems like, okay, we can get more data from GPT-4,
*  but is, you know, is that really going to move the needle all that much?
*  And then what I landed on, you know, just to get away from the keyboard a little bit
*  and really think, okay, what, what would really help here?
*  And what have I seen in the research that people seem to do that was pretty effective
*  came up with the idea of let's train 3.5, not just on GPT-4's output, but actually
*  it's reasoning that leads up to that output.
*  So we moved from instead of just asking GPT-4 to do the task, which by the way,
*  it can do well just straight away, you know, with a couple of examples,
*  anybody can just do it.
*  We then moved to asking it to first analyze the task, explain its reasoning,
*  you know, classic kind of step-by-step chain of thought.
*  And we're still in the process of refining that, you know, exactly how do we
*  want it to reason about this?
*  But immediately, even though GPT-4 didn't necessarily obviously do any better
*  with the chain of thought, so in some sense, it kind of seems like a waste.
*  We were able to generate a still modest size synthetic data set using the chain
*  of thought approach on GPT-4, then take that output, go over to 3.5 and run the
*  fine tuning now where the data set is not just inputs and result, but inputs
*  and then analysis, reasoning, breakdown, coming up with a strategy and then the
*  result, and that works a lot better.
*  And I think this really suggests that this loop is going to become super
*  common where basically if you have, and we can talk about the cost and time
*  savings on this too, because both are substantial, but if you have a prompt
*  that works with GPT-4, even if it's kind of a lot of tokens, you know, in our case,
*  we're starting to get close to maxing out the 8,000 token context window
*  with just two examples.
*  So we've got boilerplate instructions that adds up to like a thousand words
*  by the time you say everything you want to say, then a couple of examples.
*  Those are each, you know, let's say 2,000 tokens and we'd leave 3,000 tokens at
*  the end and you know, you're starting to max that out.
*  That is cost-wise like 30, 35 cents per.
*  So it starts to be a little bit prohibitive for production.
*  And it's also slow.
*  I mean, typically over a minute, sometimes over 90 seconds, typically
*  in that kind of 60 to 90 second range.
*  So you're waiting a long time and you're spending a lot on it,
*  but the result is good.
*  If you are in that position, what this really suggests is that you can add that
*  chain of thought element to the GPT-4 approach, even if it's not obviously
*  adding anything in terms of GPT-4's quality of output.
*  And then when you go to fine tune on the 3.5, notably we're also
*  cutting out those examples.
*  So our token count drops from the, you know, up to 8,000.
*  The limit on the 3.5 one is 4,000, although they do have 16,000 coming,
*  but the limit is 4,000 there.
*  So we cut the two examples.
*  Now we just have the instructions, the inputs and the outputs are, you know,
*  just the one case that we're actually concerned with.
*  And it basically learns to do that reasoning, maybe not quite as well
*  as GPT-4, but like very well.
*  I think this implies a lot about kind of where things are going.
*  We've already seen a huge trend toward using synthetic data in training
*  for all sorts of reasons.
*  Our last episode with Zico, Coulter and Andy Zavik talked about that, you know,
*  decent amount where it's like, you know, the whole problem of jail breaks stems
*  from the fact that the model is trained on like all this crazy content that
*  includes all sorts of toxic and hateful and, you know, anything you might imagine.
*  And so we kind of have to try to paper over that.
*  What he suggested was, well, why don't we start trying to train our
*  models with out all that shit, or at least with a lot less of it, you know,
*  that maybe that problem would be much less severe.
*  We wouldn't have to paper over as much stuff if we could just not have the
*  models be exposed to all that, you know, internet sludge in the first place.
*  People are starting to work on that.
*  And this just goes to show how easy that is starting to be,
*  at least for narrow use cases.
*  Now I'm still building, of course, on like all the pre-training and all the,
*  you know, there's very much on the shoulders of giants here, but I can take
*  GPT-4 with just two good examples, have it generate a hundred examples with
*  chain of thought.
*  Now I can go move that to a 3.5, get it to work with, you know, half or
*  fewer of the tokens, the cost of that is like also like a third.
*  So you're, you know, in the ball, probably not quite, but like in the
*  ballpark of a 90% cost reduction.
*  Latency is also much better.
*  It's like often under 10 seconds.
*  Sometimes it seems like it kind of varies by just probably the load on
*  OpenAI systems, but under 10 seconds, often up to into the twenties,
*  sometimes if it's more slow, but you know, basically the slowest ones with
*  the 3.5 are about at the same level as the very fastest ones from the GPT-4.
*  And this whole thing can be run pretty quickly.
*  Another really interesting data point on this, just from our experience of
*  over the last couple of weeks of really getting into it is we have
*  these data sets that we've created of like what good videos look like.
*  But here we didn't have the chain of thought because we never needed it.
*  Right.
*  We never, there was never any time or place where anybody was like, I'm
*  going to sit down and write three paragraphs about how I'm making this
*  video, just, you know, just do it.
*  Right.
*  So that all just is internal to the human's heads who made those videos.
*  So we didn't have that, but I wanted to run the fine tuning on it.
*  So I had to have GPT-4 create it.
*  Now I could have taken the existing videos and generated the chain of
*  thought for that, and we might still do that, but we found that the, just
*  asking GPT-4 to just do the task with chain of thought straight away was two,
*  at least, you know, first approximation, roughly as good as the human work
*  that we were doing anyway.
*  So instead of like, kind of, you know, re-plumbing everything and generating
*  just the chain of thought, I just kind of said, well, hey, GPT-4 just do the
*  chain of thought and do the video, just do it all.
*  And then we'll just train on that.
*  And I don't think that's probably where we'll end up, because we do have a
*  dataset that we probably trust a little bit more, and I think we can refine
*  still further from there, but if you don't have a dataset, you know, if you
*  just have a prompt that works, then, you know, this, this cycle of use that
*  prompt to generate a dataset with that kind of how you're going about it, not
*  just what you do, but how you're kind of planning and thinking about it, and
*  then what you do, port that over to 3.5, run the fine tune.
*  The fine tune typically takes minutes.
*  The model is indeed available to use typically in seconds after.
*  I've seen a few errors where, you know, the model gets done and I go ping it
*  immediately and it's like, sorry, not ready yet.
*  Typically the next time I ping it, it is ready and it's ready to go.
*  And then you've got, you know, just the, you know, the full scalability
*  and responsiveness of 3.5.
*  It is, I think, going to be a hit product for them if it's not already.
*  And definitely suggests, you know, that just there's so much opportunity.
*  Now, now that we have language models that are good enough to generate a lot of this
*  data training on synthetic data is just going to be, you know, such a, an obvious
*  win in so many cases, you know, data provenance issues too is another one.
*  You know, open AI probably is not going to get away with saying, well, we just
*  use synthetic data from GPT-4 because then people are going to be, well,
*  how'd you train GPT-4?
*  So there's kind of that, you know, regress that they may have to defend.
*  But in another context at Athena, which we've talked about many times, I, you
*  know, there's kind of this question of like, well, geez, what are we going to train on?
*  You know, forget about what open AI is going to train on.
*  Maybe, you know, we're using the API.
*  They're not going to train on our data, but what if we want to train on our data?
*  What if we have clients who have somewhat sensitive data, you know, what if their
*  executive assistants are using somewhat sensitive data or just personal information
*  in prompts and now that becomes part of our data set, would we train on that?
*  Hey, we'll continue our interview in a moment after a word from our sponsors.
*  If you're a startup founder or executive running a growing business, you know, that
*  as you scale your systems break down and the cracks start to show, if this resonates
*  with you, there are three numbers you need to know.
*  Thirty six thousand, twenty five and one.
*  Thirty six thousand.
*  That's the number of businesses which have upgraded to NetSuite by Oracle.
*  NetSuite is the number one cloud financial system, streamline accounting,
*  financial management, inventory, HR, and more.
*  Twenty five.
*  NetSuite turns 25 this year.
*  That's 25 years of helping businesses do more with less, close their books in days,
*  not weeks and drive down costs.
*  One, because your business is one of a kind.
*  So you get a customized solution for all your KPIs in one efficient
*  system with one source of truth.
*  Manage risk, get reliable forecasts and improve margins.
*  Everything you need all in one place.
*  Right now download NetSuite's popular KPI checklist designed to give you
*  consistently excellent performance, absolutely free at netsuite.com slash cognitive.
*  That's netsuite.com slash cognitive to get your own KPI checklist.
*  netsuite.com slash cognitive.
*  Omniki uses generative AI to enable you to launch hundreds of thousands of ad
*  iterations that actually work.
*  Customized across all platforms with a click of a button.
*  I believe in Omniki so much that I invested in it and I recommend you use it to.
*  Use cog rev to get a 10% discount.
*  How do we probably want to take some steps to like make sure that that.
*  Information is kind of cleaned up or like, you know, sort of anonymize somehow,
*  or, you know, sometimes they use the term de identified, but are we really experts
*  in that?
*  No.
*  And, you know, we don't really want to get caught making a huge mistake.
*  So based on this experience, I'm kind of like, maybe we can just, you know, make
*  the kind of policy now that like, we just won't train on client data and instead
*  we'll just train on synthetic data that, you know, is maybe looks like client data
*  or, um, inspired by client data, but never actually having to use the client data
*  in the training process at all.
*  So I think those are my kind of big updates.
*  Let me know what questions you have, but bottom line, 3.5 fine tuning is a great
*  product experience.
*  It's really easy to use.
*  It runs quickly.
*  The models are very scalable.
*  Once you have them.
*  Biggest insight from the process is training on chain of thought can get you
*  really good performance much better than you get just by training on the work
*  itself and the synthetic data approach, you know, generating from GPT four or
*  whatever, and then feeding that into the smaller model really works.
*  Give a shout out to, to former guests and friend of the show, uh, human loop.
*  Cause I'm using that for this process.
*  And I think they've done a really nice job of anticipating what this loop is
*  going to look like and building the tools to make it pretty easy to do.
*  Um, at the, you know, as of two weeks ago, I was kind of thinking, all right,
*  how am I going to code myself a loop here to do this?
*  And then I got back into human loop, which I have been using throughout, but
*  I hadn't used every last feature and until recently, and as I looked into that
*  more, I was like, yeah, these, these guys have definitely done a really nice job
*  of anticipating what kinds of.
*  Loops people are going to want to create.
*  You can go in there, you know, track every little aspect of everything you've done.
*  Make corrections.
*  You know, if you have something it's like, okay, this was wrong.
*  I want to fix that or kind of modify how it's, you know, reasoning through this.
*  And then use that in the next batch of training.
*  You can kind of have what the model did, your correction on top of it.
*  And then, you know, just by layering on those little corrections, again, just
*  improve performance so much.
*  So I think all these apps are going to start to get pretty good.
*  I would say ours at Waymark.
*  It's already among the best in terms of just reliably doing a pretty good job,
*  you know, and giving you something that you would have a decent chance of
*  actually wanting to use a lot of room for improvement.
*  And I think we will see a lot of that improvement come online over the next
*  few weeks to a month as we do another kind of 10 iterations, probably on the
*  fine tune model that powers it.
*  And it's exciting, you know, for this is a great instance too, of just kind of,
*  you know, what do we, what do we want to accelerate and what do we want to slow down?
*  I'm all for accelerating this kind of stuff, making 3.5 work well and scalably
*  and, you know, responsibly for users and just make all these apps in our
*  daily lives so much better.
*  That is to be accelerated in my mind.
*  And notably, I don't think we really even necessarily need GPT-5 to do our task.
*  You want to do medical work.
*  You want to get into science.
*  You know, you want to think about advanced cybersecurity type stuff.
*  You know, GPT-4 can, you can hit its limits, but for the kind of script
*  writing we're doing, I'm not even sure, you know, that there's that much more
*  improvement left beyond what we can get from kind of a GPT-4 based system.
*  So very cool.
*  Definitely fun learning experience.
*  And that's what I've got to report.
*  There's a few questions that stem from that, but just to close the last loop.
*  So in your dream world, what we would accelerate is the, the applications that
*  we've just been talking about, but what we would slow down is sort of new versions,
*  you know, GPT-5 basically.
*  How would you delineate what's your policy for what you want to slow down or?
*  You know, the leading model developers have, I think, put a pretty good position
*  out, which is that they think systems more powerful than GPT-4 deserve special
*  scrutiny and they've committed to, you know, a few different ways of doing that,
*  including having third party independent auditors or red teams look at them and
*  try to assess the risks.
*  And the sort of talk of licensing also, I think is often willfully or not, but
*  often it seems sometimes willfully kind of mischaracterized as like, oh, you're
*  not going to be able to do anything on your laptop anymore because big brothers
*  can be watching you.
*  And they have been very clear that they want that to apply to systems more
*  powerful than GPT-4 as of now.
*  And it's presumably a sliding scale.
*  You know, if we get to GPT-5 and that's safe, then, you know, maybe it's, maybe
*  that gets edited to be, you know, systems more powerful than GPT-5.
*  But I do think, you know, some of this stuff with the, like the synthetic data,
*  I just think we need a little bit of time to develop some better techniques before
*  just more raw scaling.
*  And it's possible that within some of the leading labs, they have developed some
*  of these techniques and we just don't necessarily know about them yet.
*  But, you know, cleaning the data is just one obvious thing that we can now do
*  pretty well and pretty efficiently with the language models that we do have to
*  try to create data sets that are just not so problematic in the first place.
*  The biggest risk that people tend to identify is pandemic, you know, that, that
*  a language model and, you know, Anthropic had a Senate testimony thing about this.
*  They've worked with some, some leading biosecurity people and they've kind of
*  said, yeah, it's not quite there yet, but, you know, and they don't even like to
*  talk about the details of the work.
*  But they have some extremely credible people that, you know, like MIT professors
*  involved with it.
*  And they basically say, you know, there's a number of things that you would need to
*  do to create a new pathogen.
*  And language model can't do all those things, but it can do some of them and it
*  can like kind of help you figure out what those steps might be.
*  You know, the problem right now is like that information is in there because it's
*  just been trained on everything.
*  And, you know, you try to RLHF it to not happen, but then you got things like the
*  universal jailbreak that show if it's, especially if it's open-sourced, but even
*  if not, but definitely if it's open-sourced, like you can get that out and you can have
*  kind of a cascade of things where somebody might just be like a free speech absolutist
*  and say, well, I'm going to, you know, figure out a way to take off this kind of
*  refusal behavior and somebody else, you know, comes along.
*  It's not just like one person's going to do all these steps, but you do see this
*  kind of proliferation loss of control.
*  And then, you know, if the model is capable enough and the information is in there,
*  if you are open-sourcing something, it's out there.
*  So I think up to around GBT four, we're going to be reasonably confident.
*  It's not going to like design a pathogen.
*  GBT five very well might have, you know, pathogen designing capabilities.
*  And I would much rather we get to a place where we like know what the data set is
*  and know that it doesn't have exposure to certain kinds of super sensitive stuff
*  before we build it.
*  And I think it is increasingly, you can kind of see a path to that.
*  Are we going to take that path or not?
*  It does seem like, you know, open AI seems to want to.
*  Anthropic is definitely all about that.
*  Google, I don't deep mind.
*  I don't really know, but they've been leaders in science, you know, with things
*  like Alpha Fold and many others.
*  So clearly they have awareness.
*  Meta's, you know, probably the biggest wild card there right now where, you
*  know, the scuttlebutt is that they are training a GPT four, going to open source
*  it, you know, don't care what anybody thinks, you know, we'll, we'll learn a lot.
*  If they do that about, did they take any extra precautions?
*  You know, did they, did they filter the data set?
*  You know, if they are going to go down that path, I would love to see some
*  additional foundational thought being put into this.
*  That's not just like, Hey, maybe we can pay for it over, but maybe in fact, we
*  can find a way to not have this be part of the models capabilities in the first
*  place and nobody really, you know, that would not compromise anybody's
*  utility really at all.
*  You know, I mean, there's maybe a few biologists that would get a little less
*  value from something that didn't have access to certain information.
*  And maybe you could have, you know, if we're operating in a world where there
*  are going to be rules, maybe there could be rules around, you know, bio aware
*  language models versus non bio aware language models and, you know, maybe
*  similar for some other domains too, but we just need some time to figure that
*  stuff out.
*  And so yeah, that's, that's what I would like to see us take a breath on.
*  Meanwhile, we can have all the cool apps we want, uh, with the, you know, and
*  increasingly affordably and responsibly with the 3.5 fine tuning loop.
*  Well said.
*  And anything that came up for me when you were talking is this idea, the sort
*  of question going around now of like, where is it going to be sort of copilot
*  for X versus where is it going to be just like doing X directly, replacing X,
*  taking the human out of the loop, obviously in regulated industries, you
*  know, you're going to need the human in the loop, but what are the, you know,
*  outside of that, where the spaces where it's copilot for X verse, you know, X
*  directly and kind of on what, what timeframe.
*  Yeah.
*  Great question.
*  I mean, I, I currently divide the modes of using AI into two, and I think there's
*  kind of a third one coming.
*  One being copilot.
*  And I described that as you as the human are the primary agent going about your
*  business and the AI is there to assist you answer your questions, you know, do
*  the menial tasks increasingly can do like pretty significant chunks of work.
*  I've been coding quite a bit over the last couple of weeks as I've been
*  getting into this whole fine tuning loop.
*  And I basically don't write any code by hand anymore.
*  Almost at all.
*  I pretty much always take some existing code, whether that's something that I
*  previously wrote or something from some documentation somewhere, go to GPT-4
*  with it and say, here's what I have.
*  And here's what I want.
*  And I just try to force myself and it, you know, it helps force you to do it
*  or because it rewards it, but you really just try to think through like, what is
*  it that I really want?
*  But that's still copilot mode because I'm basically doing that like one
*  bit of code at a time.
*  You know, it's, it's able to be more and more helpful, but I'm still going to it
*  with like, okay, next I want to do this class and I want to base it on this one.
*  And I want to borrow the caching pattern from over here.
*  And you know, your job is to come up with a new thing.
*  It's remarkably good at that.
*  I would say, you know, last time we talked about coding, I said, you know,
*  that's where I use it the most, but just over these last couple of weeks, getting
*  into it more intensively again, for a sprint, like I would say it is safely
*  a multiple X speed up on my ability to get projects done, just much less likely
*  to get stuck on something I don't know.
*  Much less likely to have some really stupid like typo or whatever, you know,
*  kind of unobvious mistake, you know, confuse me for a while because the AI
*  just doesn't make those kinds of mistakes very much.
*  Uh, not to maybe say never, but you know, not very much.
*  So I'd say it's a multiple speed up, but we're still in co-pilot mode there.
*  The other mode that I talk about is delegation mode.
*  I borrowed that word from Athena because their whole thing is about delegation
*  and the transformative power of delegation.
*  And in delegation, I kind of think like the core difference is you're trying to
*  get the AI to do the work at a level where you have enough trust in it,
*  that you at least don't have to review every single thing it does.
*  You're probably still going to have some sort or form of review in most cases.
*  Whereas I'm coding in co-pilot mode, I'm looking at all, you know,
*  I'm watching it write the code.
*  I then typically go run the code immediately and that, you know,
*  I may find an issue, I may come back with a bug.
*  If I do come back with a bug, I literally just copy and paste the bug, you know,
*  message right in and say, you know, Hey, I hit this issue.
*  Often it can help.
*  Often it helps, you know, pretty much immediately, not always, but, you know,
*  it takes, again, just tons and tons of time out, but I'm driving.
*  Whereas in delegation mode, it's like, okay, you know, I've used this example
*  a lot of times, like good news, bad news, good news.
*  We got a thousand applications for this new job.
*  Bad news.
*  Nobody has time to read them all.
*  Good news.
*  Good news.
*  I can create a prompt that can, you know, that I can validate on probably the first
*  10 that takes me about the time it might take me to read through 50 to a hundred.
*  And then I can achieve like 90% time savings, not necessarily to, definitely
*  not to like make the hiring decisions, but at least to like separate the bottom
*  half from the top half, or maybe the top 20% from the bottom 80%.
*  And the real key there, or where I would say you're getting into delegation mode
*  is where you're confident enough that that bottom 80% or whatever is something
*  that you can in fact, be comfortable letting go of without actually reading those.
*  You know, then you might just look at the top 20% or the top 10 or whatever.
*  So you're still going to have typically a human in the loop if it's anything
*  important, but you can save a ton of time.
*  And again, my, my key distinction for delegation mode is you aren't planning
*  to review all the work, so you want it.
*  You need to get to some standard, you know, and satisfy yourself that the work is
*  good enough that you don't have to review every bit of work.
*  Rachel Woods has a good, uh, three tier hierarchy for this.
*  She's got these kind of tiers where it's like work that just needs to get done,
*  good enough work, and then like great work.
*  And she's like, you know, work that just needs to get done.
*  That's the first thing you want to delegate to the AI and put into some sort
*  of automation work that's like just good enough, you know, could be borderline,
*  but often, you know, you can get there.
*  Great work, you know, insights, strategy, you're not going to delegate that stuff.
*  So at most you're going to be in kind of copilot mode.
*  Maybe you get, you know, some ideas from AI along the way, but you're going to be
*  the one that's judging whether those ideas are good or not.
*  What is the standard?
*  Do we need, we've talked about this in the past too, right?
*  Do we need breakthrough insights or do we need like reliable, consistent execution
*  of a given standard or a given rubric or a given, you know, protocol against some
*  like fairly predictable data?
*  Those are the two modes as they exist today.
*  And what's coming soon perhaps is the rise of agents, which kind of sit in between,
*  you know, that that's like, I think of those as kind of the bridge between the
*  copilot mode where you're driving and the delegation mode.
*  And the dream is like, you can delegate something in real time and it will be
*  reliable enough to do it for you without you having to supervise every step.
*  But you also like, hopefully don't have to spend a ton of time, you know, creating
*  scaffolding or creating a rubric or, you know, validating in the way that you do
*  pretty much have to do today if you want to get something set up for a delegation
*  style automation.
*  So all that was in your question of like, okay, what is, you know, copilot for what
*  versus doing what, you know, it's an incomplete account too, because when I
*  think about myself, you know, I'm like, it's also a huge question of who the user is.
*  I've had instances in the last couple of weeks where somebody, you know, friend of
*  a friend reached out to me with a legal question.
*  And I'm like, I'm really not qualified to answer this, but I am qualified to put it
*  into chat GPT.
*  So it's like, it's a weird in between case in that one, right?
*  Where I'm like, I never called the lawyer that I might have otherwise called because
*  I have a pretty good sense for what GPT four can and can't do.
*  It's pretty sure it would be like solid on this one.
*  And, you know, I got good enough information that for my purposes, like I was able to
*  move forward and kind of basically tell this friend of a friend that I think they need
*  a new lawyer. But the what is that?
*  Is that that's not copilot for lawyers.
*  You know, that's copilot for me, but it is perhaps replacing a call to a lawyer or, you
*  know, the more maybe optimistic take and possibly true take, I don't know, is maybe I
*  just never would have done that.
*  I would have just told this person like, sorry, I can't help you at all.
*  And they would have had to go, you know, figure something else out.
*  So maybe it's just like purely expanding the pie and no, you know, no lawyers were
*  harmed in the in this use of chat GPT.
*  But definitely there are plenty of situations.
*  I've done a number of contract reviews recently to just get, you know, whatever, some
*  independent, somebody sends me an independent contractor agreement.
*  Hey, Claude, GPT-4, does this look standard?
*  Anything of concern here?
*  If both of them say there's nothing of concern.
*  I'll sign it, you know, if because I've, you know, I've seen enough to know that
*  they'll flag stuff and usually they flag something, you know, they'll flag something
*  anyway. So the things that they flag, if they're reasonably consistent and they seem
*  fairly normal and they, you know, they don't they don't seem to be of particular
*  concern. Like, again, I don't need to probably in the past would have read it myself.
*  So, again, it's it's more copilot for me than copilot for a lawyer, but it does sort
*  of substitute.
*  I don't know, man, it's everything everywhere all at once to deny displacement at this
*  point is.
*  Definitely head in the sand, you know, there are it is clear that there are calls to
*  experts, lawyers, doctors, whatever that would be made and would incur billable time
*  that are just not made because you can get what you need directly from the AI.
*  That's not enough yet to say, you know, that those jobs don't need to exist, you
*  know, certainly far from it for some of the most, you know, sensitive jobs that are
*  out there. But to say that there's like not displacement happening is, I think, just.
*  Denial, really, at this point, it's interesting.
*  I just had Sam Lesson and Seth Rosenberg on the VC podcast.
*  They were debating the whole time around whether value will go to all incumbents or
*  some startups, et cetera. But at the end, they both agreed that, you know, costs
*  going down is going to radically increase demand.
*  And thus, they were very bullish on unemployment.
*  And I wanted to bring up the tweet that you had around, you know, tell that to the
*  farmers, et cetera, like, you know, employment for who.
*  And, you know, there's a big question around, like, to what degree will the displacement
*  happen and on on what timeline and the new jobs that are enabled.
*  Who will be able to do that and will enough people be able to transition into whatever
*  these new jobs are demanding?
*  And I think these are all these are all these are all big questions.
*  Yeah, it seems to me like we are definitely headed for some significant disruption.
*  How concrete would you be willing to get in sort of a prediction?
*  I want to be thoughtful about what I would want to get concrete about.
*  You know, one data point where I was a little hesitant to get concrete a year ago, this
*  was in the GPT-4 red teaming time.
*  I was like, holy shit, you know, this is going to be huge.
*  And because it was just immediately so useful to me, you know, and for this stuff like
*  medical to just you name it, right.
*  I'm just using it for everything.
*  So I'm like, OK, this is going to be huge.
*  And I was talking to a friend about it and they're like, well, you know, how big do
*  you think the market size is going to be?
*  And I was like, well, I know that's tough because first of all, they just keep dropping
*  the prices, you know.
*  So like when you keep when you see 98 percent price cuts or whatever from one year to
*  the next, like that is kind of tough, you know, from a market growth standpoint.
*  So I kind of hedged on that.
*  I was like, I don't I don't know that I would bet on the, you know, the revenue
*  directly attributable to LLMs as like the metric that I would want to bet on.
*  And so we ended up like not making a bet at that time.
*  Now, I would say safely that open eyes revenue growth has significantly exceeded my
*  expectations, even having seen GPD for at that time.
*  I think they did something like high 20s, million revenue last year in all of 2022.
*  And now they're at a billion annual run rate, which is to say, you know, 80 low
*  80s million per month.
*  So they've scaled from end of last year, you know, maybe.
*  Whatever they could have been at four or five, they're at like 15 to 20 X in nine
*  months and think too about how many tokens that is.
*  80 million dollars a month when the retail price of GPT 3.5 turbo tokens is
*  two dollars per million.
*  So obviously they're serving different models that, you know, that's the lower
*  price, although they're also serving a lot of free tokens, too.
*  So, you know, maybe just to take a totally naive, you know, okay, 80 million, two
*  dollars per million, 40 million times a million, 40.
*  Trillion tokens per month they're generating.
*  5,000 tokens per month for every human on earth is kind of roughly what that.
*  Backs out to that's definitely growing faster than I thought it would.
*  And I was pretty sure it was going to grow, you know, quite a bit.
*  So, yeah, I don't know.
*  Maybe we should think a little bit more and do this on another episode.
*  And I, I will definitely be happy to put some guesses on, but the metrics are tricky.
*  One of the things that people are speculating they might, uh, deliver at
*  their upcoming developer conference is another price drop.
*  Uh, so they're not maximizing in, you know, conventional sense, I don't think.
*  And it is a little tough to kind of figure out exactly, you know, what you
*  would want to predict as a result as, as hosts, you know, I have to make a prediction.
*  So I'll, I'll punt on it, but I won't, uh, I won't dodge it indefinitely.
*  You know, synthetic data based on client data or inspired by client data, as
*  opposed to client data itself, does that solve the problem for the client?
*  You think, is that something that people would be, would be happy with?
*  Or is that kind of a loophole or workaround?
*  I think it probably is contextual.
*  You know, nobody wants their phone number coming out of a, you know,
*  of a language model, right?
*  So that type of kind of very explicit, you know, this is obviously your data
*  and it shouldn't be here is pretty easy to avoid.
*  So yeah, you can just like change up all the phone numbers, you know, change up
*  the names, you know, the old dragnet names have been changed to protect the innocent.
*  I think you can definitely go clean up that kind of stuff.
*  Pretty simply conceptual stuff is a little bit trickier.
*  There has, I need to do a little bit more reading on this, but there has been
*  some recent research that showed that it only took like very few examples.
*  Maybe as few as just one example, in some cases for a model to essentially
*  memorize a certain text, what exactly, you know, does memorization imply
*  understanding or whatever.
*  But if you had conceptual IP and it's not the kind of thing that's like so
*  obvious as a phone number or, you know, an address or whatever, and then, or a
*  price, you know, of an item or, you know, your code, right?
*  I put code into chat GPT all the time, right?
*  So I don't really want my SQL schema to be in the training set, but they could
*  fudge that around pretty easily.
*  I would think, but more conceptual stuff that's like, how is this done?
*  You know, do we have kind of a, a certain secret sauce that kind of constitutes
*  a sort of intangible IP and might that still get through some of these things
*  into a model's conceptual understanding such that, you know, other people
*  interested in the field could kind of indirectly get access to your, you know,
*  hard won specialized knowledge.
*  Tough.
*  I, you know, it's, it's really hard to say.
*  I, it seems unlikely that that would happen, but I certainly wouldn't say
*  you have nothing to worry about.
*  You know, if you have, I'm trying to think of a good example of this, right?
*  There's just process chemistry.
*  I studied chemistry in college and there's like the reactions, you know,
*  and there's like the molecule and you know, you could sort of say, okay, if we
*  don't tell them what the molecule is, you know, they don't know what it is.
*  They'll, they can't reproduce the drug.
*  There's also a lot of stuff that is just kind of known and developed or along the
*  way of, well, how exactly is this done?
*  How fast do you heat it up?
*  You know, at what, you know, how gradually do you add this other thing in?
*  And a lot of this stuff is just kind of learned by trial and error and is kind
*  of a, you might look at somebody's notebook and say, well, there's not really
*  anything like super special here.
*  You know, they're just kind of recording how they did a certain thing and it
*  seems, you know, fairly innocuous in and of itself, but if you're like a big pharma
*  company and you've got like all this kind of process, you know, knowledge that's
*  kind of represented in all these notebooks, I wouldn't just hand that over
*  to open AI for training.
*  That's for sure.
*  You know, I might, I'd be very interested in what that might do for me, you know, to
*  train my own model on, on that kind of specialized knowledge, but I would be
*  reluctant to, you know, have anybody else get their hands on it because in some
*  ways it becomes more valuable perhaps in the language model than it is even in
*  the notebooks.
*  You know, these notebooks are not, uh, from what I've seen, you know, there's not
*  a lot of time spent one scientist reading another scientist's notebook.
*  Uh, but if the AI could read all the notebooks, then it might just have some
*  insights that, you know, are not obvious to perhaps anyone.
*  So yeah, I think a lot more needs to be kind of figured out there.
*  So far it's been pretty superficial, but more conceptual stuff is harder to say.
*  And so that's why opening AI, you know, has kind of had this very consistent
*  message recently of like, we don't train on your data.
*  We don't train on your data.
*  We don't train on your data.
*  And I, and I don't even the synthetic thing, you know, I'm not sure would get
*  around it for some of this fuzzier kind of de-localized information.
*  Let's, uh, let's get into some AI bundle talk.
*  Yeah.
*  So, okay.
*  This is, um, possibly a good idea, possibly not a good idea, but I wanted to
*  bounce it off of you and for context, it stems from the fact that as a customer
*  of AI services all over the place, I am constantly running into a, just like
*  an increasing number of services that I think are like awesome and, you know,
*  potentially worth paying for, and then also like an even longer tail of services
*  that are potentially, you know, worth paying for, or, you know, kind of something
*  I want to pay for once maybe, but not something I'm like going to be a power
*  user of this is.
*  Coming to the four very much at Athena again, you know, a thousand plus
*  executive assistants serving a thousand executive clients all over the place.
*  A lot of different needs, you know, a lot of different contexts, a lot of different
*  tools that would be helpful in that circumstance.
*  So one of the skills that I'm trying to teach folks is product scouting.
*  Just how do you go out there and figure out, is this good?
*  Is it bad?
*  Does it add anything to, you know, kind of base GPT-4 what's worth paying for?
*  And it's tough and it's also tough on the app developer side.
*  So as you know, putting on my way market, then I'm like, man, we get a lot of
*  traffic from a lot of people who.
*  Don't really, they're not like power users of our app, right?
*  We help small businesses make marketing videos.
*  We sell to big companies that do a lot of that.
*  So like cable companies, TV companies, you know, you spectrum, Fox, gray TV,
*  et cetera, they have dedicated sales teams that go out and sell video advertising
*  all the time.
*  And so they need a lot of video creative.
*  And so they're a natural kind of long-term customer for us.
*  But then the small businesses themselves, even today are not like making a video
*  every day, you know, no matter how easy we make it, they're just not going to
*  make that many videos.
*  And, you know, we offer just like so many retail SaaS businesses.
*  And it's kind of putting us in this weird position where we want to show the
*  product off.
*  We want to give that demo without requiring payment, but we figure we're
*  paying about 15 cents for all the different AI services that we're using to
*  serve one random new user, whether or not they pay us anything.
*  And then our lowest price point.
*  Well, we've varied it over time, but you know, you, you see a range of
*  things that we're paying for.
*  Well, we've varied it over time, but you know, you, you see a range of lowest
*  price points out there, but typically they're like at least 10 bucks, often 20,
*  often 30, sometimes more.
*  And so you're kind of in this weird spot where you're like, okay, I need to get
*  one person to sign up for a $30 a month subscription to cover 200 people just
*  trying the product.
*  And then I can kind of break even on that.
*  But it doesn't really feel like super fair or awesome for anyone.
*  And I think Waymark has really good customer retention metrics at those
*  like high-end enterprise customers.
*  But like many AI apps, we see a lot of people try the product.
*  A lot of people just bounce, obviously, you know, they're not ready to pay the
*  30 bucks or whatever.
*  Then a lot of other people do pay the 30 bucks because they're like, I love that.
*  I want that.
*  And we don't want them to download the thing that they created until they pay us
*  something.
*  But then a lot of those people will just quickly cancel because they're like, I
*  only wanted the one thing.
*  I don't want another subscription.
*  You know, this sucks.
*  So I got pain on both sides, right?
*  As a customer of AI products, I like have a proliferating set of things that I
*  value in.
*  And, you know, the bill is adding up and it's ridiculous, you know, to try to
*  imagine buying all the things that I might want to use just to, you know, go
*  down my, my power rankings a little bit.
*  Chat GPT, 20 bucks a month, retail, 60 bucks a month.
*  If we're going to buy the recently announced enterprise edition, 60 bucks a
*  month is the highest AI platform price that I've seen so far.
*  Windows Co-Pilot, 30 bucks a month.
*  Google Duet, 30 bucks a month.
*  Perplexity Pro, 20 bucks a month.
*  Cloud Pro, 20 bucks a month.
*  GitHub Co-Pilot, $10 if you buy it for yourself, $19 if your company buys it for
*  you.
*  Repli Ghostwriter, $10 per seat.
*  And those are just like the literal, you know, the top, top tier of things that I
*  use repeatedly every week.
*  So you add those up and even leaving the enterprise price off of, of chat GPT, you
*  know, and I'm just figuring I'm only going to buy one of Windows or Google Suite.
*  I'm still at 110 bucks, you know, for kind of the other four of seven of those things
*  or whatever.
*  That's adding up to quite a bit.
*  And Waymark notably doesn't see a cent.
*  So this got me thinking, is there an opportunity here to create some sort of
*  cable bundle like bundle and who exactly should sell it and how it should be
*  governed?
*  I mean, there's, I think a lot of little nuances to how this would work
*  inevitably, right?
*  Certainly cable bundles are not without their drama as we've seen lately too.
*  But if I'm paying a hundred bucks a month, it seems like what I really want and maybe
*  could get would be like a little bit of all the different AI apps that are out there.
*  So instead of having to kind of decide like, do I want to subsidize the next 200 free
*  users for this given app by like paying the 30 bucks, even if I don't really intend to
*  be a power user of this app.
*  Maybe there could be some other way where if I'm subscribed to a bundle, I can kind of
*  get access to all these things, at least in some limited fashion, right?
*  So I could kind of pop around the web and like make a Waymark video and then maybe make
*  like a gamma slide deck and maybe make another one in a couple of weeks.
*  But I'm never going to become a power user and I don't want the $30 per month level.
*  How could that look?
*  And it does seem like there's something there that really could make sense.
*  You know, if I'm a customer and you said, hey, your bill is adding up for a hundred
*  bucks, we'll curate for you, you know, a hundred going on a thousand apps and you'll
*  get at least baseline access to all of them.
*  Presumably, you know, there would be higher tiers for many of these things beyond kind
*  of what would be included in the bundle.
*  But those would be for like the real power users, you know, that are not going to just
*  make one off things here or there.
*  I think that would be very compelling to me as an individual customer.
*  And then I think about it from the Waymark side and I'm like, I don't know what our
*  share of that bundle would be.
*  We're more like the ESPN classic than the ESPN, you know, in the cable bundle
*  hierarchy. But, you know, we've got a cool product and it's something that a lot of
*  people do need every so often.
*  You know, a lot of people do have very good experience of it.
*  And then they're just like, I just can't get over that thirty dollar hump right now.
*  And we can't really lower that price that much because we got it.
*  That person has to cover the other 200 people.
*  So what I would definitely take, you know, is like some small share of this bundle
*  just to be a part of it.
*  And, you know, you can imagine complicating that in any number of ways.
*  But even if I were just to say, OK, let's say that bundle is 100 bucks.
*  Let's say Waymark gets one one thousandth of that bundle.
*  We get 10 cents per user that they sell.
*  If they go sell a million users, then that is one hundred thousand dollars a month in
*  revenue for Waymark.
*  That's a million dollars a year.
*  So every million they sell of those bundles is a million dollars to Waymark and, you
*  know, and potentially hundreds of others of long tail, you know, kind of episodic,
*  you know, yeah, it'd be cool to use this, but I don't really want to subscribe to it
*  right now sort of apps.
*  Then we could serve an audience that we just never really could otherwise serve, you
*  know, that million people when they need Waymark, they could have it, you know, and
*  we would feel like we're not getting cheated.
*  You know, we would we would also feel like we don't have to pressure every user to
*  sign up that we're pressuring.
*  But, you know, we're gating, we're like putting calls to action, you know, we're
*  trying to do all the things that SaaS apps do to get people to subscribe.
*  It feels like we could really, you know, be more like, hey, just have at it, have fun.
*  Have fun.
*  And then if you're going to make more than five this month or whatever, then then
*  you can, you know, maybe subscribe to a higher tier plan.
*  And I don't even think that would cannibalize much of our business.
*  And from what I hear from other app developers, this problem is very widespread.
*  And I think you've probably heard some of this in your, you know, VC talk as well.
*  Right.
*  All of the app developers that I talked to, at least have a lot of people
*  interested, you know, a lot of traffic as people just kind of explore new stuff all
*  the time, typically they are doing pretty well in new customer signups too.
*  But the retention sucks.
*  And so it's like, man, you get into this high churn environment and that's just
*  not a great dynamic to be in.
*  I don't know.
*  I feel like I like it on both sides.
*  There would obviously need to be some sort of market maker in the middle.
*  Who would do that?
*  You know, could it be open AI?
*  Maybe.
*  Could it be a more neutral kind of editorial type of body?
*  You know, a wire cutter type of thing where we don't, you know, as wire cutter, we
*  don't make any of these products, but we just have an authoritative credible voice
*  of what is in and you know, what is good and what's not good.
*  I could also see that.
*  I don't think open AI is going to be like super keen in the short term to take on all
*  this editorial, but I could imagine them creating a more sort of, you know, rules
*  based system where you might imagine something that's like, you get in based on
*  an initial review and then you stay in based on like some amount of usage or, you
*  know, or also like payments could be sort of what they really don't want to do.
*  Presumably is do all the negotiation with a thousand different apps as everybody's
*  like, yeah, whatever, but they could easily do like a take it or leave it sort of deal
*  where it's like, you're at this scale, you have this many users, you know, that puts
*  you in this tier, you get this percent.
*  And that's that, right.
*  And we have room for how many companies and, you know, maybe as the bundle
*  subscriber base grows, I mean, we've got what probably 50 million cable
*  subscriptions still in the United States.
*  So like a million cable bundles is small, you know, at a more mature state, if it
*  became 10 million AI bundle subscribers, I don't necessarily think way marks share
*  would even necessarily grow proportionally instead it might be like, now we go from
*  a thousand apps to two thousand apps and you guys all get more, but not as much more
*  as the whole thing has grown because we're going to expand, you know, all the
*  different things that we can include.
*  Obviously a lot more things are coming on all the time as well, which would make
*  that a natural progression.
*  I don't know.
*  Why doesn't this work?
*  You're the, you're the VC.
*  What's, what are the holes that you see in this theory?
*  I totally get how it makes sense from the developer perspective, the user
*  perspective, and my natural inclination is to sort of look at other industries.
*  And think about where things like it have happened or things like it haven't.
*  And we, you know, we sort of alluded to, to, to, to cable and sort of the, the
*  strength of, or the durability of, of that bundle, despite people's expectations.
*  Otherwise, and Ben Thompson writes a lot about how people under appreciate the
*  economics of the bundle and why it makes sense for so many people.
*  I go to SAS, right?
*  So companies have a whole suite of SAS products that they pay, you know, X
*  amount a month, and wouldn't it be easier if they just paid a bundle in terms of
*  access to all of them and maybe in some cases that exists, but I don't see that
*  sort of like super widespread.
*  I think it's just the cost of coordination such that on the producer side, such that
*  it would make sense for every individual company instead of, you know, the
*  individual companies trying to own the customer relationship directly and then
*  use that as a wedge to expand into, you know, multi-product themselves.
*  I wonder if that's what might hold that back here is just companies not wanting
*  to be intermediated between them and the customer, and then also thinking that
*  they will not just occupy their, their spot, but that they will occupy the other
*  spots within that bundle and they'll become competitive.
*  But you can still have a lot of competition within the bundle, right?
*  I mean, when I think about my cable bundle, there certainly is plenty of
*  competition within that seems to be, you know, pretty fierce.
*  And you also, I think, I mean, this is very different technology, right?
*  So in the case of cable, you, you know, historically, you basically just had no
*  other choice to do it.
*  If you're a producer of, of content or very few other choices, you know,
*  bordering on no other choices.
*  And so, you know, you might have wished that you could go direct to the consumer,
*  but you just really couldn't now with, you know, content being delivered over
*  the internet, obviously lots of people are trying that in various ways.
*  And, you know, we've got everything plus the, you know, the content, uh, industry
*  decided to add plus everything and the AI industry is adding pro to everything.
*  So they're doing that.
*  It seems like it's kind of working for some of them, but, you know, probably
*  again, kind of a power law type of thing where it's obviously going to work for
*  Disney because they have the gravity to command that type of, yeah, I'm going
*  to buy it and it is what it is.
*  Few have that, you know, I've not subscribed to discovery plus, or, you
*  know, whatever other pluses there might be, I see, you know, CNN plus obviously
*  it was not a super well received.
*  So in any event though, in this case, you kind of would much more easily be able
*  to own the customer relationship or at least have it not like totally, you
*  maybe would have it like partially mediated by the bundle.
*  You'd have to have some, you know, log in with or connect with, you know, again,
*  we have that in cable too, right?
*  I go to ESPN.com.
*  I want to watch something on the website.
*  You connect with your, you know, cable provider or what have you.
*  So some, some version of that is maybe still needed to, you know, just
*  manage the logistics, but then once you're logged in, presumably the app
*  would like know who you are, you know, be able to see what usage you're doing.
*  You know, if you're Waymark, you're going to be creating a business profile.
*  And, you know, we're going to have a pretty good sense of who you are.
*  If you're using the app at all, you know, kind of regardless of who
*  owned the billing relationship.
*  And I honestly think, you know, for us, like, we want to own the
*  billing relationship with our best customers, but we really don't
*  necessarily want to own it with our worst customers, you know?
*  And it's not to say that those customers are bad people, but just that they're,
*  you know, not long-term subscribers to whatever, you know, $30 a month video
*  creator, especially when we don't lock them into anything.
*  So you just see this be so often.
*  This is like, yep, create, download and cancel.
*  It's like, it wasn't really, you know, that wasn't, that wasn't something
*  like people were disappointed with the service.
*  That was their plan the entire time.
*  You know, they're not, they're not coming back later and saying,
*  I don't like this anymore.
*  So I don't know.
*  Yeah.
*  I mean, I still feel like I'm, I'm still bullish on the bundle.
*  Say more about the, the SAS.
*  Why isn't this more prevalent at a company level for sort of SAS
*  products to SAS tools, either via some sort of wire cutter thing, or just
*  the company's coordinating, you know, one company coordinating.
*  Maybe churn isn't so high in general.
*  You know, I think maybe SAS historically has more of a stickiness to it.
*  I mean, you know, the magic of AI from a user standpoint kind of cuts the other
*  way from a retention standpoint, I can use waymark with no learning curve, no
*  time spent, and I'm not really forming like a sense of, Hey, I've invested in
*  this or, you know, I've learned how to use it.
*  I don't want to go have to learn another thing.
*  We've taken the learning part totally out of it.
*  So that could be one reason, you know, if, if people are happy with their.
*  Retention and they're like, yeah, I don't have, you know, if you, if you simply
*  don't have a lot of people trying your product that you like, you know, would be
*  happy to kind of take 10 cents a month from, you know, cause there may be only
*  going to show up one every, you know, 24 months anyway, then maybe it's just
*  not appealing to you.
*  And so much SAS is kind of that way where you're like, you know, you're
*  onboarded and you're, you know, trained and all this kind of stuff.
*  That's the first thing that comes to mind for sure.
*  Just the ease of flipping into and out of all these products.
*  Like I can get value super quick, but I also know that I can go get value
*  anywhere else, you know, super quick too.
*  So I just can't, I'm just not forming and, you know, don't have time to form
*  attachment to these products in the way that maybe a couple of years ago, you
*  know, I really had to sit down and learn to use it and therefore, maybe I'd
*  stick around a little longer.
*  Yeah.
*  I mean, to go back to the cable thing for a second, it's like, from a user
*  perspective, at least it's like, Hey, I really just want to watch ESPN or
*  whatever this channel, I don't need this entire sort of collection of things.
*  And it's probably, it might be cheaper for me to just, just get the, get the
*  one that that's when people want it to be unbundled, they want it to be bundled
*  when they think it would be cheaper to get the aggregate they, and either, they
*  either want the aggregate or they might want the, the aggregate and there's some
*  like variability in there.
*  And so I understand here why people would want, what users would want the
*  aggregate or the collection, the bundle.
*  And the question is, is it in the company's incentives to be a part of this bundle?
*  And more so than that, whose incentive is it to form the bundle?
*  This is sort of the, to form, maintain, you know, keep up, upkeep, be accountable
*  for, in theory, whoever does would own a customer relationship.
*  So that seems it'd be very strategic for someone to do so, but would they let
*  other companies be in the bundle and also let them own the customer relationship,
*  as opposed to try to just build competitors?
*  Yeah.
*  Like you said, you know, maybe, maybe it's an open AI or, or a new company like
*  Wirecutter, but I don't know how many companies would be incentivized to do
*  such a thing where they include their competitors in a bundle.
*  Yeah.
*  One.
*  So I don't know how realistic this is either, but I was kind of thinking, you
*  know, there's these really interesting moves that the leading AI companies are
*  making where, you know, they're competing with each other, but it's honestly not
*  very hard competition right now, relative to what it probably could be.
*  There are nascent collaborations, you know, with things like the Frontier
*  Model Forum, there are just generally people like saying nice things about
*  each other, you know, up until pretty recently, and even still to some degree,
*  there's like a lot of knowledge sharing in the form of just publishing research.
*  And maybe above all, there's this most, most tangibly and maybe most
*  relevantly, there's this part of the open AI charter where they say that.
*  If another credible organization is like getting close to AGI, then they will
*  work with that organization as opposed to racing that organization because they're
*  really afraid of these race dynamics.
*  So we're in like a much more mundane moment right now for how long who knows,
*  but certainly at the moment, you know, like neither Claw 2 nor GBT4 are
*  sufficiently close to AGI as to have triggered that clause, but I do wonder if
*  there's, you know, given all the movement that they are making to like try to kind
*  of set up these collaboration forums and try to, you know, agree on some regulation
*  framework, seemingly as well.
*  I do wonder if like a commercial agreement like this could be appealing in a way that
*  it wouldn't be if it's just two content, you know, owners duking it out, right?
*  Because here they do seem to have a real kind of principled worldview that's like,
*  the last thing we want to do is get into a cutthroat race, you know, against each
*  other to the point where we're both, you know, or multiple parties are incentivized
*  to cut corners on safety, right?
*  They've certainly paid a ton of lip service to that.
*  I tend to think it's pretty sincere.
*  So if that is the case, you could almost imagine the Frontier Model Forum,
*  I think this would end up being a separate thing because this would be like, you know,
*  people are already cynical enough.
*  I don't think they would.
*  There'd be an infinite amount of cynicism in response to the literal Frontier Model
*  Forum doing it.
*  But something like the Frontier Model Forum, you know, the same companies could say,
*  hey, we've all got kind of some strengths and weaknesses.
*  You know, the pie is growing extremely quickly.
*  Let's not compete for every subscriber because we know that probably people are not
*  going to want to subscribe to everything unless we can make it just really compelling
*  and easy for them to subscribe to everything.
*  And then, you know, if we could kind of agree on some rules based way to divide up
*  that revenue, then that could be just good for everyone, right?
*  It takes pressure off of us.
*  We don't have to worry that they've got a slight edge or they're releasing their
*  thing before we do.
*  I mean, the moment earlier this year where Microsoft is racing to get their big thing
*  out and then Google's trying to get ahead of them, they get ahead of them by like one
*  day and have some terrible announcement.
*  You know, that is a pattern we really don't want to get into in the GPT-5 plus era.
*  So anything you could do to kind of say, hey, you launch this week, we'll launch
*  next week, we'll launch next month, whatever, it'll all be fine because, you
*  know, it's just all these launches make the bundle more compelling.
*  More people sign up.
*  We all get revenue.
*  You know, maybe we kind of compete on the margins for users, but not necessarily for
*  like that more discreet payment decision moment.
*  I could see that being pretty cool.
*  And, you know, there's a long list.
*  Let me just give you a, I give you like the anchor tenants in my bundle, but here's
*  just more, you know, things that I would like to have in a bundle that I either have
*  paid for and canceled or like, you know, was at least tempted to, or maybe I'm still
*  paying for without realizing it.
*  So Dolly, I get that with OpenAI.
*  Mid Journey is its own subscription.
*  Playground AI is, has a super generous free tier, as we may recall from our very
*  first episode, but obviously also as an upsell Lexica, same deal, stable diffusion
*  from stability, you know, has its own kind of pricing for its usage.
*  That's just five image creators.
*  There's a ton of niche ones too.
*  Like I follow this, this guy Levelzio.
*  Who is like a prolific individual kind of solopreneur who's put out multiple,
*  pretty cool AI apps.
*  And, you know, he's also at this kind of price point and he does well for himself.
*  Probably could do maybe even better in a bundle.
*  I mean, I don't know.
*  He's been among the most successful, but I think it could even make sense for
*  somebody like him, but he does these very niche ones, like put yourself in this.
*  He was in that before other people were.
*  So, you know, you could do have a bunch more just like a, you know,
*  just in the image category.
*  Agents type stuff is coming up all over the place.
*  We've had three different agent companies on the show.
*  Text to speech is another one where I've got live accounts with WellSaid Labs,
*  PlayHT, former guest, and Eleven Labs.
*  That's just in voice.
*  You know, then you got all these creative tools, Weymark, Gamma,
*  Tome, Jasper, et cetera, et cetera.
*  Every single one of those is like, has a $20 plus per month.
*  Tier.
*  And they're all like super useful, but they all have this kind of dual problem
*  of like the friction of paying.
*  And then also the fact that I just don't do it that often, you know, gamut.
*  It's an awesome way to create a great visual presentation.
*  I don't create that many.
*  I created one for the AI scouting report.
*  I've created another one for like an AI task automation primer.
*  Not that many Khan Academy too, you know, tutoring.
*  I signed up for that thing.
*  I since canceled it.
*  I don't, I'm not looking for algebra, you know, tutoring on a daily basis.
*  So, you know, at some point you just gotta like keep the credit card clean.
*  I feel like easily there are, you know, $500 worth of apps that I would be like,
*  yeah, if I subscribe to everything that I occasionally use, it comes out to a ton.
*  80, 90% of those are probably not worth it.
*  And kind of in the same way as the cable bundle, I sort of imagine subscribing to
*  this thing where I'm like, yeah, okay, whatever that price is.
*  Well, if I just went and bought chat GPT pro by itself and also copilot by itself
*  and also perplexity pro by itself, I'm basically there.
*  So I'm basically just buy the bundle and like get a hundred other things too.
*  It does feel super compelling.
*  You want to be an equity investor in my new, uh, AI bundling AI bundle.co.
*  I think it's going to be hard to, to coordinate.
*  I mean, think of something like ride sharing.
*  Like Lyft and Uber, those companies should have merged, right?
*  Like those companies were offering the same product basically, and they were
*  fueled by venture dollars to inefficiently offer the same product.
*  Basically they were both running each other out of business more or less.
*  And venture subsidized rides.
*  So they diluted, I don't know, did they both dilute like 80% 90%?
*  I have no idea, but they both diluted a crazy amount because they took so much
*  money and if they were one company, they could have avoided this whole mess.
*  Um, and I spoke to Emil Michael, uh, the chief business officer at Uber.
*  And he was like, yeah, I tried to get us to acquire them to merge cause they
*  just didn't make sense, but Travis said we got to kill them and that Lyft was
*  like, we hate Uber, so businesses just are irrational at the end of the day.
*  And the fact that there's funded by, by VCs who, and they all have take
*  over the world visions, it's challenging for people to be in a spot of like,
*  Hey, you play this niche or Hey, you collaborate with this competitor.
*  When everyone's trying to dominate market share, it's hard to get them to agree to
*  a bundle long-term when they would just go on getting one increasing pies of this
*  bond.
*  Now you do see some major players collaborate, but there are a lot of times
*  where they don't, even though it would be much better, not only to the user, the
*  customer, but also to themselves.
*  It would cement cement themselves.
*  I see the example of levels, et cetera.
*  There are obvious examples where it makes sense.
*  Yeah.
*  Even in situations where it makes sense for all parties, sometimes pride or, or
*  just the narrative that they told or believed themselves prevents them from,
*  from doing it.
*  So I'm color me a bit dubious though.
*  I would like it to happen.
*  And I think, I think it's a creative idea.
*  Yeah.
*  You can almost see in the Lyft and Uber example, and also if you visit the sling
*  TV pricing page, you can see kind of an alternative vision of this, which I think
*  is maybe more likely for the reasons that you're describing what they have done.
*  The sling TV pricing page is the orange pack and the blue pack.
*  And basically they're kind of, you know, just two different content alliances that.
*  You know, I've kind of clustered around some core pieces.
*  So you could kind of imagine a version of that.
*  It could be like the open AI bundle and the anthropic bundle, you know, or maybe the
*  open AI Microsoft bundle, you know, is kind of one axis and then the anthropic
*  Google bundle on the other axis.
*  And then, you know, each one could kind of have a bunch of, you know, smaller players
*  that are kind of in their ecosystem.
*  You can imagine like to be in our ecosystem, you have to use our models.
*  That sounds a lot less awesome to me for most people involved, but I could see how
*  certainly the folks at the leading companies right now do feel like they're kind of.
*  If not taken over the world, you know, certainly in a very privileged position
*  where they're going to get to call a lot of shots and yeah, if they don't want to
*  cooperate, you know, certainly it's going to be very hard to make them.
*  The other thing I think could be also pretty interesting about this is I think you
*  could get a lot of people to buy the bundle, particularly if a lot of the app
*  developers, and maybe this would end up being like something you have to do or,
*  you know, but again, you don't want to end up negotiating too much or it's just
*  going to be way too much friction.
*  But I can also see something where it's like, Hey, you know what?
*  At Weymark, we don't give away the AI experience anymore.
*  You got to subscribe to the bundle.
*  And if you did that and all of a sudden, all these like apps that are currently
*  kind of out there for free ish, you know, for a little or whatever, then maybe each
*  one, you know, kind of serves as like a point where it's like, yeah, another
*  reason to get the bundle.
*  That would be a very different dynamic from say a cable where, you know, I don't
*  get to see what's on, you know, Discovery Channel haphazardly and then decide to
*  buy it, I guess, maybe out of home or whatever.
*  But like, you know, I don't have that kind of quick taste of this one random thing
*  that I want that then like leads me into the bundle from like a thousand different
*  directions, you know, more kind of distributed high surface area, more touch
*  points away might have, you know, more, more ways in to the bundle as well.
*  You know, I'll maybe remain hopeful.
*  I think it's funny.
*  This is kind of the classic, like the market can remain irrational longer than
*  you can remain solvent, you know, or companies, you know, don't necessarily
*  always act rationally, certainly undeniable fact, but if that's the biggest
*  reason it won't happen, then at least it feels like there's maybe some chance
*  that it could, that's a good note to wrap.
*  Cool.
*  Well, let's see if we can go talk anybody into it.
*  Nathan, always a pleasure until next time.
*  It is both energizing and enlightening to hear why people listen and learn
*  what they value about the show.
*  So please don't hesitate to reach out via email at tcr at turpentine.co, or
*  you can DM me on the social media platform of your choice.
*  Omnike uses generative AI to enable you to launch hundreds of thousands of ad
*  iterations that actually work customized across all platforms with a click of a button.
*  I believe in Omnike so much that I invested in it, and I recommend you use
*  it to use Cogrev to get a 10% discount.

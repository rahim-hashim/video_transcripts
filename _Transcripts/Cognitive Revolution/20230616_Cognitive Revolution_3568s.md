---
Date Generated: April 03, 2024
Transcription Model: whisper medium 20231117
Length: 3568s
Video Keywords: []
Video Views: 714
Video Rating: None
---

# Your Model, Your Weights with MosaicML's Abhi Venigalla and Jonathan Frankle
**Cognitive Revolution "How AI Changes Everything":** [June 16, 2023](https://www.youtube.com/watch?v=5_qAuSQGLHQ)
*  Who's training these models?
*  Everybody.
*  Really the question you should ask is,
*  who has interesting proprietary data?
*  Everybody.
*  I mean, as Abhi mentioned,
*  there's a model size for everybody.
*  There's a good entry point for everybody.
*  And at the end of the day,
*  it's everything from small startups
*  for whom the model is their main product.
*  Companies like Replet that are very tech forward
*  and AI first and recognize the power of this
*  to the kinds of companies that if I mentioned them,
*  you'd say, wow, that's a really big, boring company.
*  They're doing AI?
*  Yeah.
*  I mean, they have amazing data.
*  This is how you activate it.
*  In the old days, you know,
*  you used to say like data is your mode.
*  And then in the past year or so,
*  there's been like this new kind of way for it.
*  Well, actually training the model so hard,
*  maybe that's the mode.
*  And I said, what's next thing is like,
*  we're making that easy again.
*  So it's almost like making it more training boring again.
*  Hello and welcome to the Cognitive Revolution
*  where we interview visionary researchers,
*  entrepreneurs and builders
*  working on the frontier of artificial intelligence.
*  Each week we'll explore their revolutionary ideas
*  and together we'll build a picture
*  of how AI technology will transform work, life
*  and society in the coming years.
*  I'm Nathan LeBenz joined by my cohost, Eric Tornberg.
*  Hello and welcome back to the Cognitive Revolution.
*  Today we're talking to Jonathan Frankel and Abhi Vinayagala,
*  chief scientist and research scientist at Mosaic ML.
*  In today's world of AI hype,
*  it seems like almost any project has at least some chance
*  of going viral on Twitter.
*  A few of those will prove deserving and enduring,
*  but most will quickly fade away.
*  To make headline news repeatedly, however,
*  as Mosaic has done over the last year,
*  is something that only truly top-notch organizations can do.
*  Mosaic specializes in creating custom,
*  proprietary language models for corporate clients.
*  They were the first to offer GPT-3 quality models
*  for $500,000 in September of 2022.
*  And they were the first to train stable diffusion
*  from scratch for under $160,000 in January of this year.
*  They then turned around and did it again,
*  announcing stable diffusion for under $50,000 in April.
*  One funny note from the conversation,
*  at one point you'll hear Jonathan give me
*  a bit of a hard time for quoting the $160,000 number
*  instead of the latest $50,000 number.
*  I went back and checked and it turns out
*  that they announced that additional price drop
*  in the few days between when I prepped for
*  and when we recorded this episode.
*  Just goes to show how fast things are moving.
*  Most recently, Mosaic has released
*  their own open source models,
*  as well as an inference service that allows you
*  to use their servers to power your applications.
*  According to LM-SYS.org,
*  a leaderboard that collects human evaluations
*  on blind head-to-head language model comparisons,
*  their MPT-7b chat model is currently
*  the number nine rated chat model in the world.
*  Now that's already an impressive accomplishment,
*  but what's even more impressive,
*  when you remove the OpenAI, Anthropic, Google,
*  and Llama derived models from the list,
*  it turns out that MPT-7b chat is actually
*  the number one rated open source model
*  that is available for easy fine tuning and commercial use.
*  Additionally, their release of the MPT-7b Storywriter
*  65k plus model, which allows actually even more
*  than 65,000 tokens of context,
*  legitimately shocked much of the AI world
*  and set a new standard for long context models,
*  which are already quickly becoming the norm.
*  We'll talk about the alibi technique
*  that they used to achieve this.
*  We only had an hour for this call.
*  As you'll hear Jonathan say,
*  demand from Mosaic ML services is through the roof.
*  They are reaching the point where they're making
*  tough choices between serving additional customers
*  and conducting additional research.
*  Obviously that doesn't leave a ton of time for podcasting,
*  but I still think this episode is a great window
*  into who is training their own language models,
*  why they're going that route,
*  what they're using them for,
*  and the techniques that are powering this trend.
*  Before jumping into the episode,
*  a quick thank you to everyone who has shared
*  the cognitive revolution with friends
*  or posted a review online.
*  We're now up to roughly 25,000 unique monthly listeners,
*  and I am having a ton of fun sharing
*  all of these conversations
*  and everything I'm learning from them with all of you.
*  Now, I hope you enjoy this conversation
*  with Jonathan Frankel and Abhi Venugala of Mosaic ML.
*  Abhi Venugala, Jonathan Frankel,
*  welcome to the cognitive revolution.
*  Hey, it's great to be here.
*  Really excited to have you both.
*  As you know, I've been a close watcher of
*  and big fan of Mosaic for a little while now,
*  and you guys have built an awesome platform
*  and made a bunch of news recently
*  with a number of product and model releases
*  in the LLM space.
*  So I've got a ton of questions
*  and thought we could maybe kind of structure things
*  by starting first with what I believe
*  to be kind of the foundational layer of the business,
*  which is the custom large language model training.
*  Then I kind of want to get into the new inference side
*  of the business as well.
*  Definitely want to make sure we get to the 65K model
*  that you guys recently released,
*  because I think that's super interesting
*  and even want to dig in a little bit to how that was done
*  and some of the new techniques that you have
*  I'm sure not only applied, but refined in practice.
*  And then if we have time,
*  we can even get into some bigger picture stuff.
*  How's all that sound?
*  It sounds great.
*  Cool.
*  So I guess when I think of Mosaic,
*  what I have kind of understood you guys to be
*  up until recently is the go-to place
*  for presumably larger businesses,
*  although you've done impressive work
*  to bring the kind of entry point sticker price down,
*  but presumably mostly larger businesses
*  that want to create their own custom large language models,
*  I think usually from scratch.
*  So the first thing I wanted to just kind of sanity
*  check myself on is do I have that right?
*  And then we can dig in a little deeper
*  to like who those companies are.
*  Yeah, no, totally.
*  I think you got it right.
*  And I think we've sort of been expanding
*  from that initial position,
*  like recently in the past while they're set up.
*  But yes, we started off as a kind of help people
*  build their own custom models,
*  whether it's large language models or diffusion models,
*  originally, even verb models
*  and out of the rest of the 50s, even back in the day,
*  really want to help people who have valuable proprietary data
*  turn that into valuable models that they own
*  rather than necessarily leverage APIs and such.
*  One way we've expanded from that is try and make it
*  even, even easier for people to build these custom models
*  so they can start from like pre-trip checkpoints
*  and kind of our recently like MPT models
*  that we released out there.
*  Or show these like public checkpoints
*  where it's already a pretty good language model
*  and you just are on top of this and continue.
*  And finally, like the last one that we thought is that
*  every person who trains models with us
*  wants to deploy them from the press.
*  So we figured, well, we should probably help them
*  with that too.
*  So that's also what we're trying to do.
*  So we're really trying to help end to end people
*  go from the data to these kind of private models
*  having points that they own.
*  Let's unpack that a little bit more.
*  Who in today's world is building, you know,
*  a custom large language model and you know,
*  how big are these models that they're building?
*  We could talk about that in terms of parameters
*  or like token count on the training side.
*  You've kind of answered already,
*  but I was kind of curious to what degree you're seeing
*  people use a combination of like open source data sets
*  versus just, you know, how many of these customers
*  actually have enough of their own data
*  where they don't even need, you know,
*  any of the kind of standard data sets.
*  Yeah, for sure.
*  I mean, like I think we have a very wide spectrum
*  of customers.
*  We have people concerning, you know, training, you know,
*  sub-billion parameter models to, you know,
*  like in the single digit billions of parameters
*  and some even going well beyond that.
*  You can see some of our customer stories
*  like Reflet recently, they've turned like a really powerful
*  three billion parameter model that actually
*  can summarize that for like the first of code version, right?
*  So kind of like out punching for its subway class.
*  We really focus a lot on kind of efficiency in this way.
*  We want people to be able to produce things
*  that are smaller, you know, cheaper for reference,
*  cheaper for training that still match the quality of the need.
*  Now in terms of data, you know, this is,
*  this is the thing I've really focused on nowadays,
*  which is that sometimes customers come
*  with a lot of pre-trained data.
*  You know, they may have across all of their like, you know,
*  customer interactions or like, you know,
*  all logs and stuff, maybe tens of billions of tokens.
*  But they want the model to also start
*  with a general knowledge of the world, right?
*  So there's a good amount of research doing that.
*  You know, like what are the data mixes that want to do?
*  They actually spent a lot of time curating the data
*  for the team models that we released.
*  But yeah, I would say like, I would expect customers
*  to have a mix about public data.
*  I'll throw in one more thing, which is, you know,
*  to put a really fine point on answering your first question,
*  who's training these models?
*  Everybody.
*  Really the question you should ask is,
*  who has interesting proprietary data?
*  Everybody.
*  I mean, as Abhi mentioned,
*  there's a model size for everybody.
*  There's a good entry point for everybody.
*  And at the end of the day, you know,
*  it's everything from small startups
*  for whom the model is their main product.
*  Companies like Replet that are very tech forward
*  and AI first and recognize the power of this
*  to the kinds of companies that if I mentioned them,
*  you'd say, wow, that's a really big boring company.
*  They're doing AI.
*  It's because yeah, I mean, they have amazing data.
*  This is how you activate it.
*  So it really is everyone and everybody,
*  you know, trying to train these models.
*  Yeah, actually you're reminding me of something
*  that I've thought of a lot, which is the kind of,
*  in the old days, you know,
*  it was to say like data is your mode.
*  And then in the past year or so,
*  there's been like this new kind of way for it.
*  Well, actually training the model so hard,
*  maybe that's the mode.
*  And I said, well, the next thing is like,
*  we're making that easy again.
*  So it's almost like making it
*  and not training boring again.
*  You know, like we're bringing it back to a position
*  where actually the proprietary data
*  is what makes your model so much better.
*  Can you expand a little bit on just kind of use cases?
*  I mean, obviously, you've got some names on your website
*  and then I'm sure, you know, lots more customer names
*  that maybe you can't disclose.
*  But if you can kind of abstract away from, you know,
*  the sort of identifiable details
*  of some of these customers,
*  I think people are really curious about use cases.
*  Like, are we building chat type agents
*  to like help enterprises interact with their customers?
*  Are we doing like task automation back office?
*  What's that kind of breadth and mix look like?
*  You know, the boring answer is
*  it's a little bit of everything.
*  But I think the main thing we see,
*  especially with big enterprises,
*  kind of I can really sum it up as two tasks,
*  extraction and summarization.
*  Those seem to be kind of the core workhorse tasks
*  that people want to get done.
*  You've got a huge amount of information.
*  You may get there because, you know,
*  a new court case came out
*  and it's a hundred something pages long
*  and you want to understand what it's about right away.
*  You may get there because you're using something
*  like land chain and a vector database
*  and you pulled up a bunch of really relevant documents
*  and you have a lot of information
*  that is relative to some question.
*  But at the end of the day,
*  you really want to extract out the relevant piece
*  of information or the relevant passage
*  where you want to get a summary
*  and get useful information out of it.
*  I think for a lot of our enterprise customers,
*  it's as simple as that.
*  For a lot of other customers,
*  they are looking at some specific application.
*  We certainly have customers who care a lot about chat.
*  I wouldn't say it's anywhere near the majority,
*  but we certainly have some folks
*  who either care about chat as their main application
*  or care about chat as a good user interface
*  on top of one of these systems.
*  And then of course you have customers like Grapplet
*  that are doing something that doesn't really fall cleanly
*  into any of these categories.
*  It is genuinely useful.
*  The models are as multipurpose as any other language model,
*  but those are really at the end of the day,
*  those are kind of the boring useful things
*  that honestly these models are best at.
*  And then both things with a model
*  doesn't have to be perfectly right.
*  We're getting in the right direction
*  or just try to get useful information
*  out of some data you already have
*  is the most important part.
*  And you're not about to make an important medical decision
*  on the basis of a summary
*  that your model gives you for example.
*  There's still a human decision maker in the loop
*  to make sure that the information is acted upon
*  that is in an appropriate way.
*  Yeah, I think that's great grounding.
*  There's so much stuff going on in the corporate world
*  that is ultimately not necessarily super flashy,
*  but there's just a ton of value to unlock
*  because of how much of it there is
*  and how much more cheaply you could do it,
*  or potentially also like how much more you can scale it
*  versus what you could do in the past.
*  I wonder if you could comment on that.
*  I see a lot of in the context of like task automation,
*  sometimes it's like, I have this task,
*  I do it today in a human powered way,
*  and it's that can be slower and more expensive
*  than I'd like, so maybe I can take time and costs out.
*  But then the other thing that people often kind of
*  quickly turn to once they start to wrap their head
*  around this is like,
*  maybe I can scale previously unscalable processes.
*  So if it is this kind of extraction and summarization
*  are the main things,
*  how much of that extraction and summarization
*  do you think in the pre-language model era
*  was done by humans versus just like not done at all
*  because nobody could get to it?
*  Yeah, I would say I'm much more excited about the water.
*  And that's also where I think customers
*  are probably excited too.
*  One thing I think about a lot is actually in the context
*  of some of our work in our open source repos,
*  lots of times when people use it, they have questions,
*  right, they're like, oh, how do I actually like,
*  use the script, like what should I be doing?
*  What's the workflow?
*  And right now I think the best that humans can do
*  really is to write like documentation, right?
*  Or like write FAQs and stuff like that.
*  But there's no scalable way to say like,
*  have someone next to you as a support person
*  helping you through it, right?
*  But with these models and stuff,
*  we could actually build some system, right?
*  It seems like we can actually build higher
*  and higher quality interactions with people.
*  Like previously, like as we said,
*  just could not be done.
*  So the cost and scalability of like having,
*  one person for every customer.
*  So I think that's where it would be most exciting.
*  Not necessarily like replacing, you know,
*  things that are done today,
*  but enabling new things that can't be done today.
*  Yeah, I certainly see that in some of my task automation work.
*  It quickly becomes like, geez, we could do 100X,
*  you know, of this.
*  And some of these things are just every,
*  almost every business has certain use cases,
*  like often it's like scaling outbound recruiting outreach,
*  you know, how are we gonna get, you know,
*  to all the candidates we'd like to get to?
*  Most companies just don't have the resources
*  to do as much of that as they would like.
*  And we're starting to see that kind of thing turn out.
*  It's gonna interestingly lead to some probably
*  different dynamics in terms of how
*  that communication actually works
*  and like what it takes to break through and be effective.
*  But we're in this interesting moment where it's like
*  the early adopters are getting these kind of early benefits
*  and then, you know, presumably there's gonna be
*  a new equilibrium on some of these things.
*  Digging a little bit deeper still into,
*  why does somebody come to Mosaic?
*  Because I can imagine, okay, I'm an enterprise.
*  I've got these, probably at the end of the day,
*  fairly mundane, you know, information processing objectives.
*  I could go to like an open AI and, you know,
*  they also make it pretty easy to do fine tuning
*  with just like, you know, supervised input, output,
*  pair, paradigm of fine tuning.
*  What is the main reason that folks say
*  I don't wanna go with them?
*  I instead wanna work with Mosaic.
*  Is it like control of data, cost?
*  I mean, you're gonna say all of the above again,
*  but give me a little bit more than just the all of the above
*  because I kind of know what the suspects are,
*  but I wanna know like what the mix is and what you're seeing.
*  Hey, we'll continue our interview in a moment
*  after a word from our sponsors.
*  Omnike uses generative AI to enable you to launch
*  hundreds of thousands of ad iterations that actually work,
*  customized across all platforms with a click of a button.
*  I believe in Omnike so much that I invested in it
*  and I recommend you use it too.
*  Use Cogrev to get a 10% discount.
*  Yeah, totally.
*  I think I'll focus on like kind of two customer profiles
*  seeing one is the type of customer often startups
*  where they wanna build a new product or like experience
*  that truly cannot be done any other way
*  than to produce a custom model.
*  You know, they either have to train like a really custom
*  domain like coding model, or they need a model
*  that handles multiple languages or basically like things
*  where it's like, you know, they've tried the APIs,
*  it's not quite good enough, or it's not cost effective enough
*  and they really need to have their own custom model.
*  And so for them, it just makes sense, you know,
*  well, if I need to build an element house, you know,
*  I need to get the computer, I need to get the engineers,
*  they're all researchers, it's a really expensive
*  and honestly today pretty hard to find group of people
*  to build something or kind of like the other option
*  that you can just go to Mosaic and you build them
*  and a very small team, right?
*  You can actually build these custom models for yourself.
*  I would say that's like one type.
*  Another type are people who actually are like our users
*  and that means API providers like OpenAI, Cohere,
*  others, right?
*  Where maybe they build the first version of the product
*  on top of these APIs and it's going great, you know,
*  they've still users, you know, they're getting lots
*  of revenue, that's fantastic.
*  And now sort of like, okay, now it's an optimization
*  question, right?
*  Like, can I potentially build smaller models
*  or custom models myself and deploy them for cheaper, right?
*  And that's like part of what we're talking about
*  in this inference strike.
*  We're basically trying to very clearly separate,
*  you know, the costs of training the model
*  and the cost of deploying the model
*  and there's like only a small team.
*  It's actually very, very close to the actual inference
*  to EU comes to the power.
*  Whereas opposed with OpenAI system, right?
*  You know, you're paying for the particular thing
*  and the particular cost actually goes a lot
*  when you find it.
*  So I think like, for instance, some of the fine tune models
*  they cost six X as much when you go from like
*  the base model to fine tune.
*  With those, there's no such thing like that, right?
*  We're very explicit about, you know,
*  here's like the compute costs and cost power.
*  It doesn't matter what weight you're putting on
*  be it the base models or the models and so on.
*  So that's where I think like we're trying to be
*  a bit more transparent in all of this
*  and like passing those data to customers
*  and, you know, give them a lot more flexibility
*  than you'd get with the actual design of the new BS.
*  You want to say anything?
*  Yeah, I'll throw in, I think, you know,
*  from the big enterprise perspective,
*  it's really three things.
*  You know, it is customization control and costs
*  and they love that they all start with C.
*  That was convenient.
*  On the customization side, a lot of folks,
*  like enterprises have huge amounts of data
*  that you can't put into a few input output pairs.
*  You know, we've had plenty of customers come to us and say,
*  I have several hundred billion tokens
*  or I have over a trillion tokens worth of data.
*  There's no other way to get that data into your model
*  beyond, you know, doing a lot of training
*  potentially from scratch.
*  A lot of customers come to us and say,
*  we, you know, we want to customize the pre-training data
*  for the model fundamentally.
*  They look at, you know, open source models
*  and they say, well, I don't like that data set.
*  I want a little more code.
*  I want a little more of this.
*  We basically have a menu at this point
*  of what's available open source
*  and how they want to put it together.
*  With any of the big APIs, you have no idea
*  and that's part of the secret sauce.
*  You have to hope that the thing you're worried about
*  just isn't in that model.
*  On the control side, we can do it
*  within their cloud VPC such that the data never leaves.
*  We can do it on cloud if they want to.
*  And they own the model weeks when they're done.
*  Not just, you know, not just an API to the model
*  where they can rent their own model forever,
*  but they actually own the model.
*  If they want to take it and serve it another way
*  or open source it, we're fine with that.
*  That's, you know, that's up to the customer, not to us.
*  And, you know, Abby, I think has covered
*  and so they mentioned the cost side.
*  It's just cheaper to train a domain specific
*  pre-billion parameter model than it is, you know,
*  even to try to fine tune in many cases
*  a gigantic, you know, I guess 1.6 trillion parameter model
*  from what I've heard, especially if you're going to do it
*  on more than a few input output pairs.
*  So that difference really matters.
*  I've done a lot of fine tuning on the OpenAI platform
*  in particular, and I've had some things
*  where it's worked really well for me.
*  And then I've had other things
*  where it hasn't worked so well.
*  Where it's worked well has been,
*  I have like a very defined task
*  and I'm kind of dialing it in.
*  I have a certain format requirement.
*  I have certain like length, you know, output requirements.
*  And I, you know, typically find it doesn't take
*  that many examples to get there.
*  But then I've also tried like trying to train it
*  to write in my voice.
*  And that hasn't worked so well because, you know,
*  I only have so many tokens for one thing,
*  and it sort of kind of learns who I am,
*  but it's like still madly hallucinating, you know,
*  after at least the sort of data set that I'm able to muster.
*  It sounds surprising to me on some level
*  that there are this many established companies
*  that are already this far
*  in their large language model journeys.
*  And I see, you know, like everything's kind of happening,
*  you know, all at once.
*  Or we've got reports of like people banning Chaggpt at work.
*  And then we've got reports of other people
*  like if you don't learn to use it by, you know,
*  July 1st, you're fired.
*  I just saw a story like that the other day.
*  But I am surprised that people are kind of
*  seemingly moving on to like next generation, you know, already.
*  So I'm curious about that.
*  And I'm also curious about like the nature of the models
*  that they create.
*  Like, are they creating these models
*  that sort of have a very particular point of view
*  on the universe?
*  Yeah, we saw, I don't think this is your customer,
*  but like Wendy's, you know, has like fresh AI.
*  And I'm wondering like,
*  do those AIs like know about a Big Mac, you know,
*  or do they have like just no conception of like what exists,
*  you know, outside of kind of their, you know,
*  corporate knowledge base kind of universe?
*  There's a lot there, but I'd love to hear a little bit more
*  about just kind of the color commentary
*  of the sorts of journeys that people are on
*  and the nature of the models that they're creating.
*  Yeah, so I think, I don't know,
*  let me just go to the first question.
*  Yeah, that the number of companies
*  that are building Ellens.
*  No, I think we were also like, you know,
*  pleasantly surprised by the number of companies
*  that we found like since I'd say last winter or so,
*  like when we really started doing this alone after.
*  And in the beginning, I think it was mostly startups,
*  but especially since the Cap2BT explosion,
*  like a lot of like, basically once the world like realized
*  this is possible, we've seen many, many more
*  companies that want, they basically want like a
*  Cap2BT internal that they can use,
*  one that they can trust,
*  one that they can actually control,
*  like, you know, the data that's coming in,
*  you know, the recency, one that which, you know,
*  they're even internal like employees can use safely, right?
*  As opposed to some of these reports of like, you know,
*  confidential data leaking into the Cap2BT system.
*  So yeah, I think it's, even if they're not like super
*  far on the journey yet, they know right away
*  that they're gonna have to develop some kind of
*  proprietary system, not necessarily just.
*  Yeah, so I can't speak too much like what exactly
*  our customers are doing, but I will say it's,
*  it's not too diverse in that way yet.
*  It's not like people are ripping out parts of Wikipedia
*  and trying to control things like that.
*  I think right now a lot of it's just sort of,
*  how do we incorporate our proprietary in addition to like,
*  you know, general knowledge?
*  A lot of it is, you know, like making sure there's no
*  harmfulness, you know, no toxic hate here,
*  that kind of stuff too.
*  Some of it is even just like, how do I incorporate,
*  you know, things like long context length
*  or long form documents, which you couldn't do
*  until very recently, like, you know, on the APIs.
*  Of course, Centrafic now has like this 100k support as well.
*  And we're really excited about that and the possibilities,
*  but I think most things haven't added it.
*  I'm not sure I've seen too much of like the kind of like
*  pruning away that you may be talking about.
*  Maybe, do you want to comment on that?
*  Yeah, I think what we tend to see is that all of our
*  customers want to mix some open source data
*  in their internal data.
*  You know, if you were to just train it on your internal
*  knowledge base, that model is going to have a pretty
*  limited understanding of the world.
*  And, you know, the knowledge base may not even be
*  in very clear prose in a lot of cases.
*  So a lot of customers are mixing together open source
*  data since they think they're a good fit
*  with their own internal data.
*  I do also want to kind of, you know, popping up one level.
*  I think you're framing this as, do you use GPT for,
*  and I think that's a false dichotomy.
*  What we're seeing for a lot of our customers is that
*  the answer is yes.
*  There are certain use cases where GPT-4 is both great,
*  you know, and, you know, allowable.
*  There are a lot of use cases where either GPT-4 simply
*  can't be used in those cases, there's sensitive data,
*  or, you know, there are a lot of cases where it's just
*  not effective because we need to know about internal
*  business processes that it simply hasn't been trained on
*  because that's internal documentation.
*  So what we see with a lot of our customers is,
*  are they using GPT-4?
*  Are they using us?
*  Yeah.
*  And, you know, these are different tools
*  for different use cases.
*  But I don't think we're trying to say replace GPT-4
*  with Mosaic ML.
*  We're trying to say there are a lot of different ways
*  to solve these problems and a lot of different tools
*  to do it.
*  Yeah, I think that's a good call out.
*  And it's almost one of my mantras these days too,
*  is like, it's never in AI right now, either or.
*  It's always kind of both.
*  And, you know, that extends to like societal impact
*  questions as well as kind of, you know,
*  which models and tools are people going to use.
*  So I totally, that totally makes sense to me, you know,
*  that it's not all one way or the other.
*  So not that, so it makes sense what you're saying there
*  with kind of the mix of data.
*  It makes sense then why you have these kind of checkpoints
*  that are like a base to build on,
*  like no need to rerun that sort of, you know,
*  Wikipedia pre-training time and time again,
*  if you can kind of embody it and have the ability
*  to branch off from there.
*  When you do that fine tuning,
*  are you continuing to mix in, like, what is the curricula?
*  It seems like we're kind of moving toward this
*  like curriculum model where there's kind of this general,
*  you know, knowledge base, you know,
*  that is the checkpoint and you're laying
*  on the proprietary data.
*  Are you still mixing in the open source data
*  or do you just like, just kind of pre-train on their data
*  and that works out okay?
*  I don't really have a sense for if you can make
*  that kind of shift from like data set A to B
*  and it all works out okay,
*  or if you kind of have to continue to bring, you know,
*  some of the base forward into the continued pre-training.
*  Yeah, I mean, I think the first thing I would,
*  I would mention here, you know,
*  I'm going to be really picky right now.
*  I hate the word fine tuning because when you show up
*  and you say, I want to fine tune on 200 billion tokens,
*  I don't know, there's nothing fine about that.
*  It's as hardcore as pre-training, if not more so.
*  What we tend to see is kind of a mix of things.
*  If they're going to build on one of our checkpoints,
*  you know, you do continue to mix in some open source data
*  and create the right mix.
*  It may not be the exact same open source data,
*  but often, you know, if a customer doesn't have
*  the right representation of data anyway,
*  simply training on a specific subset of the data
*  they want the bottle to eventually know
*  will be catastrophic for getting.
*  And so you do want to make sure that you've got, you know,
*  a good mixture of both, you know, some more generic data
*  and some more domain specific data.
*  I think this is in some sense a question as old as time
*  when it comes to transfer learning and fine tuning.
*  There are papers from the BERT era,
*  which was so long ago, you know, three years ago,
*  that were all about this question of
*  how do you fine tune properly?
*  And, you know, a paper called Don't Stop Pre-Training,
*  which, I mean, should tell you the whole story there.
*  So there are a lot of different, you know,
*  there are a lot of different approaches to this,
*  especially when you get into instruction fine tuning
*  and RLHF, you are doing a different task.
*  And so you do want to change the nature of your data
*  and probably don't mix, you know,
*  for example, instruction following
*  and just normal continuation of natural language.
*  But all this is really, I think the bottom line is
*  all this is science yet to be done.
*  We're experimenting, our customers are experimenting,
*  we're doing things that seem intuitive,
*  we're trying to test everything rigorously,
*  and we're all learning every day.
*  A lot of the best questions like this
*  haven't even been answered in a really rigorous way though.
*  Yeah, so basically no sharp line between continued pre-training
*  and fine tuning in many instances anyway.
*  And yeah, starting to see too, like some of these,
*  what had been understood or at least introduced
*  as kind of late stage training techniques
*  are also being backported into the pre-training, right?
*  Like we're seeing just from the last week, I think,
*  like pre-training with few shot, you know, structure
*  as kind of an earlier thing,
*  that could probably cite several examples,
*  but I won't waste your time.
*  But yeah, it's interesting that both
*  are kind of blending together and the techniques
*  seem to be kind of going both directions
*  at the same time as well.
*  Yeah, I think especially once we start getting to this,
*  the situation where like we just kind of few shot the models,
*  I mean, few shot prompt the models,
*  even like the loss functions that we're using
*  for fine tuning and pre-training are exactly the same, right?
*  We're effectively just giving sequences
*  and saying please match the sequence,
*  please auto-computer, right?
*  And so previously, I think some of the distinctions came from
*  like, oh, fine tune time, I'm gonna add a new head,
*  you know, I'm gonna add a new class of fusion head
*  or an LNF or something.
*  Now all of that's kind of at the window
*  and we're just continuing to train the original mates
*  with new like four minutes effective.
*  Yeah, the great convergence.
*  It is fascinating that, you know,
*  obviously the architectures have kind of unified,
*  but also the, you know, the loss functions,
*  you know, kind of converging to the same thing.
*  Man, that is crazy.
*  Are there any, so what I wanted to ask specifically
*  about life sciences,
*  because one of my personal goals is to have no major
*  blind spots in my understanding of the AI landscape
*  and I, you know, can't quite ever achieve that,
*  I don't think, because it's moving too quickly.
*  But I realize in looking at some of the stuff
*  on your website that that is kind of a gap
*  in my knowledge right now.
*  What is a language model,
*  maybe it's not even language models that you're training
*  but I had kind of understood it is, I think,
*  language models in the context of the life sciences.
*  What does that look like?
*  Yeah, so I think, you know, we've done a bit of work,
*  you know, kind of on biomedical language models
*  in the past.
*  We worked together with a team from Stanford,
*  this year our team, to build a, I think, biomedal.
*  And that was just like late last year,
*  where basically we wanted to have a model
*  just custom domain data,
*  which was, I think, like PubMed papers, basically.
*  So that you could actually ask the questions about like,
*  you know, medical diagnosis and things like that
*  and have it actually in a server.
*  And you're seeing like a very similar trend happening
*  at Google right now, I think,
*  but they're Med-POM models, they're Med-POM and Med-POM2,
*  where they're actually able to like,
*  kind of put them head to head with physicians
*  and actually see like, oh, could this be an augmenting tool,
*  you know, that like, you know,
*  helps you diagnose patients, helps you like respond to them,
*  you know, and stuff like that.
*  So that's like one part where it is just genuinely
*  like language models,
*  but you're not like biomedical language.
*  There's another sort of direction,
*  which, you know, we haven't gone too much into yet,
*  which is sort of like genomics or like, you know,
*  kind of use more chemistry kind of applications
*  where, you know, like protein synthesis
*  and like amino acid-chains stuff
*  are also just like sequences, right?
*  And especially with something new,
*  like support for long context,
*  can we help people in those domains too?
*  Basically turning transformers
*  for like protein sequences or something like that.
*  I think that's like a really exciting question.
*  Cool, any other customers or kind of, you know,
*  perhaps surprising language model use cases
*  that you would highlight?
*  I mean, I don't know.
*  I personally still find every use case of language models
*  a little bit surprising.
*  Fair.
*  It's still new and so everything is new and interesting.
*  And honestly, our customers are really creative.
*  So I think there's a lot of really cool multilingual work
*  that we're seeing happening where, you know,
*  existing models are okay at doing multilingual stuff,
*  but if you really want a model
*  that's focused on a particular bilingual scenario,
*  that seems to be incredibly popular right now.
*  You know, languages that I would not have chosen
*  if I were trying to build say a five language
*  or 10 language language model.
*  So I found that to be really cool
*  and really exciting so far.
*  I hope our customers will talk about that at some point.
*  I want to talk about another place for them,
*  but we've seen some really awesome applications
*  in that area and it has to be exciting.
*  It's not something I thought that much about.
*  It puts a lot of pressure on the tokenizer,
*  which is kind of interesting.
*  It's something that I've always been very fraught subject,
*  but it's cool to see all that activity
*  and to see that we've reduced the barriers to entry
*  such that, you know, these applications are now within reach.
*  You can build an LLM for an interesting language pair
*  that certainly nobody would have picked right off the bat.
*  Yeah, that tokenizer,
*  it's been interesting research this week, you know,
*  that has been billed as maybe the beginning of the end
*  of the tokenizer.
*  We'll see if that pans out,
*  but I've seen also the like, you know,
*  one character from like a Hindi script, for example,
*  might be in fact like eight tokens
*  because of the way it's all kind of broken down
*  under the hood.
*  And that is definitely something for listeners.
*  If we want to go down that rabbit hole, you know,
*  check out how certain like Indian language alphabets
*  get tokenized.
*  It's quite gnarly.
*  I want to move on to the inference business,
*  which you guys have just introduced in just a second,
*  but just a little bit more calibration on kind of this data.
*  You know, people have these, you know,
*  hundreds of billions of trillion tokens.
*  It sounds like it's often kind of raw.
*  How raw can it be before it becomes like a problem?
*  And then like, how tight did the resulting language models
*  kind of stay to that knowledge base versus like,
*  do they start hallucinating like plausible products,
*  that these businesses might have?
*  Or, you know, I imagine that same problem must exist, right?
*  Yeah, I mean, I think to a first approximation,
*  your model is what you put into it.
*  If you train a language model on a web data set
*  that has a bunch of advertisements in it,
*  your model will learn to start spitting out
*  advertisements of its sentence.
*  You know, that sort of behavior is definitely in these models.
*  And so the data needs to be reasonably clean.
*  You can't just shove everything in there.
*  Not all tokens are created equal,
*  but to your first approximation,
*  all tokens are created equal.
*  You have to do a lot of work
*  to get a high enough quality data set
*  that you start to see this matter.
*  You know, this is why we place such a high-frequency
*  amount of things like Wikipedia,
*  or things like code that, you know,
*  tend to be relatively well curated,
*  all things considered from the beginning.
*  And so just, you know, punch above their weight,
*  token for token with other data sets.
*  But if you're gonna pull data from the web,
*  level data from your internal use cases,
*  do a good work on that data to clean it up,
*  can be really, really important.
*  And, you know, I imagine, you know,
*  models like all models like, you know, TGT-4,
*  that was the lion's share of the work in some sense.
*  Once you have a good system down for training a model,
*  you know, data is a never-ending problem.
*  And to address the other question,
*  how do you make sure that the company's products
*  are represented faithfully and they don't like losing things?
*  I think this is where, like,
*  long contexts can really help, right?
*  More you can kind of shove into that initial props
*  to the model.
*  It's going to tend to that rather than whatever memories
*  are struck away much more, you know, attentively.
*  And that way you can kind of ensure like,
*  hey, here's a list of actually, you know,
*  June 2023 products, you know,
*  please refer only to these.
*  I think that's a lot more, you know, reliable
*  and potentially gonna retrain every so often
*  so they have to do.
*  So really investigating our research
*  in lots of different ways to incorporate both long contexts,
*  potentially in the future retrievable as well,
*  to make it so for enterprises
*  they can actually trust these models to come.
*  How often are the customers able to kind of use something
*  that comes out of the, you know,
*  kind of bulk pre-training process versus layering on
*  some sort of finishing instruction tuning or RLHF?
*  I think for most enterprise applications,
*  you have to go through some kind of like this after training
*  or polishing.
*  I think especially, you know,
*  you can even tell from API providers,
*  they usually have a lot of this kind of
*  either instruction tuning or RLHF or something like that
*  so that you can actually speak to the model naturally
*  rather than like kind of prompted very specifically
*  to do what you want.
*  I think we offer, you know, especially on our
*  was like infrastructure service,
*  like instruction tuning models mostly.
*  If you go general, obviously you can start with a base
*  and like, you know, however you wish.
*  But my gut feeling is that the instruction tuning models
*  are a little bit more useful.
*  Yeah, makes sense.
*  I was kind of, from that I'm kind of inferring also like,
*  what the pattern of use is, where, you know, again,
*  in like some of the very highly tailored, you know,
*  fine tuning, which is, you know,
*  genuine just like few, you know,
*  example fine tuning that I've done,
*  it doesn't necessarily need to be instruction tuned
*  because it's in such a controlled environment.
*  You know, there's a high degree of kind of developer
*  architecture that surrounds what the inputs
*  are even gonna be.
*  But it sounds like there's also a pretty good mix of
*  companies just kind of creating these things
*  and then making them available to their internal users
*  to say like, now you can use this whenever you want.
*  Is that fair conclusion?
*  Yeah, no, I mean, I think in terms of evaluation stuff,
*  that the best place to put data is on one of people,
*  like internal ones and just like see how they use it.
*  I think as you're saying, right, you know,
*  especially if you're fine tuning,
*  if I could have a lot of data,
*  if you go input output format,
*  maybe it's good enough to start from the base
*  versus the instruction tuning model.
*  I don't think there's like any capabilities
*  to start from tuning.
*  It's really just this kind of like massaging
*  of input outputs so that you can talk to it
*  as you go to your friend or something.
*  But yeah, so like, you know, a common path that might be,
*  you know, if you start from like a base model, right,
*  either one are pre-trained ones or one that you build yourself,
*  you deploy it in what was a different,
*  so we have a nice little play back where you can actually
*  talk to it and kind of like investing how it's doing
*  based on how that performs, you know,
*  you share that out with your employees.
*  Then you build a fine tune model
*  and then you implement the next one, the next one.
*  And it's really an iterative process to get the model to,
*  and where you have to be more,
*  you know, more actually comfortable performing.
*  I can say we're pretty well locked up
*  where we're pretty much at evaluation.
*  We started off with kind of these academic demographics
*  and we have some blockbusters along,
*  and we have to do really fast evaluation
*  of these kind of context learning tasks,
*  but we have to graduate beyond that.
*  These models are getting so good that effectively,
*  it's hard to even treasure circle
*  because of these nice little tasks.
*  So interactive evaluation, automated evaluation,
*  all of these stuff.
*  I think so.
*  And if I understand correctly,
*  that's kind of frontier right now.
*  Like most clients are not, for example,
*  like red teaming models yet, it sounds like,
*  but you see that as a, the kind of thing that more
*  we'll start to do in the not too distant future.
*  I see this as something that we're gonna provide
*  as a service to our customers.
*  At the end of the day, you know,
*  we are the one stop shop for, you know,
*  making sure that you get a good model
*  all the way from data to training to inference.
*  A big part of that is making sure that the model
*  you've got out there is something you're proud of.
*  So we invest a lot of resources when we work with customers
*  to make sure they're evaluating their models carefully.
*  Red teaming is a part of that.
*  And so, you know, I can't make any promises
*  about a mosaic and middle evaluation product.
*  You're not gonna announce that today,
*  but you know, you should keep your eyes out
*  in an not too distant future,
*  because we're gonna work on that.
*  I'm always very interested in the, you know,
*  the kind of red teaming risk mitigation side of that
*  in particular, but obviously,
*  confirming that it does the, you know,
*  the happy path, you know,
*  effectively is also super important.
*  Let's talk about the inference business.
*  You guys have layered on an inference platform
*  to the business, and it's interesting
*  because you both have like open source these,
*  you know, foundation models.
*  People can go do whatever they wanna do with them.
*  Obviously you don't see that as a threat
*  to your ability to build a good inference business.
*  So I'd kind of love to maybe just start
*  with like the pitch for, you know,
*  the practical kind of way that people understand,
*  even though this model is right here
*  and I could go do it, you know,
*  what is the calculus that ultimately leads them
*  to choose you?
*  And then I'd love to dig into like the pricing
*  a little bit more and kind of understand
*  the cost structure to the degree
*  that we can do that as well.
*  Yeah, absolutely.
*  So I think kind of like starting at the basics, right?
*  So you've got something that's open source model,
*  it's like off the hub, it's up the stuff.
*  Why not just try and like spin up a GPU cell phone server?
*  And I think there's a lot of learning that happens
*  once you actually start to try and do this
*  and like serve it on API to, you know, many, many customers.
*  You realize that like kind of, you know,
*  the libraries that you have today, you know,
*  it's easy to like serve one customer,
*  but very hard to serve many, right?
*  And you need batching, things like, you know,
*  lower precision weights, you need things
*  like multi-processing and auto-scaling and stuff like that.
*  And tuning all these things is quite difficult,
*  especially as you have these very, very large models.
*  So the challenges I would say is that when it comes time
*  that you actually want to serve say
*  a 30 billion parameter language model,
*  you find there's very few existing solutions
*  that can actually achieve the type of performance
*  or latency that you expect from like an opening
*  or here and stuff like this.
*  So that's like one thing,
*  is that we want to simplify all the infrastructure
*  the same way we simplify the training.
*  And in terms of the cost side of it,
*  are there any particular questions I could answer?
*  Yeah, so I study this somewhat obsessively.
*  So just looking at the pricing page,
*  I noticed that it is five one hundredths of a cent
*  per 1000 tokens for the new MPT 7B instruct model,
*  which I gather is kind of the new
*  like mainline workhorse based model.
*  And, you know, to put that pricing a different way
*  at 20,000 tokens or 40 pages, you've now spent one cent.
*  So you've got quite a bit of room to run there
*  before you're spending much money.
*  Where does that money go?
*  Like, I don't know if this is something
*  that you can even characterize this way.
*  On some level it could be,
*  but it may be so many layers of abstraction.
*  But like, do we have a sense for,
*  if I spend one cent on 20,000 tokens,
*  how much of that one cent went to electricity?
*  How much of it went to buying GPU cards?
*  How much of it went to, you know,
*  I don't know if you guys use like AWS or multiple clouds
*  or even run your own data center.
*  So that'd be interesting,
*  but like how much of it goes to data center management?
*  Well, without going into too many details of the exact numbers,
*  I can help build up kind of the stack of everything
*  that goes into that file cost there.
*  So, so let me say, you know,
*  we deploy anywhere on any computer,
*  so you could bring your own GPUs that you have,
*  if you have your own, you know,
*  this account or Oracle account,
*  you could rent the computer directly from us
*  and we have some preferred partners,
*  mainly Oracle right now,
*  where we like rent a lot of these GPUs.
*  And so as you build up towards like that cost per serving,
*  what you're really trying to figure out is
*  to satisfy a given workload,
*  let's say you need to satisfy like 10 requests per second,
*  keep or something,
*  and you need to figure out any of the particular model sizes,
*  say like a BTU set of a comparable model.
*  You want to figure out how many GPUs
*  can satisfy that thing,
*  and then you're basically renting those
*  and running them full time 24 hours a day.
*  So that's the thing about inference, right?
*  Is that you have these servers that are basically running
*  all the time with non-stop certain requests.
*  And so it's funny, you know, sometimes training,
*  at least, you know, the job finishes at some point,
*  but inference is running forever.
*  So building up towards that,
*  like, you know, one cent cost per hour, right?
*  You're paying a certain charge rent from GPUs,
*  and that both amortizes the cost of the GPU,
*  usually over about three years or something,
*  plus the electricity is being used for the data center.
*  But for most people,
*  that whole cost gets packaged up
*  into like the rental price per hour, right?
*  So maybe like just putting a number out there for it,
*  and they 100, it costs $2 per hour, right?
*  Maybe to your data center provider,
*  it costs them only like a dollar to actually run the whole thing
*  because they've got such a comprehensive scale.
*  But that's like the first part, right?
*  So the price per hour.
*  Then on top of that, you know, mosaic platform service,
*  you know, we have a few ourselves,
*  so we put on top of that.
*  But finally, when you're an enterprise customer,
*  you basically just pay per hour of costs.
*  So we help you figure out
*  where your request work will come to GPUs.
*  We help kind of point you towards the right GPU types
*  that you want as well.
*  Not necessarily A100s, which are really powerful,
*  but a little bit of overkill for sharing workloads.
*  Maybe you want A10s and so.
*  And we help break that down effectively
*  into a price gap.
*  And so then finally,
*  when it comes to your single request rate,
*  what we're saying basically is that that one request,
*  you know, if it was happening coincidentally
*  over the course of a month,
*  it breaks out to only have a little bit, one cent
*  versus like the monthly cost, maybe a few thousand dollars.
*  So as it stands today,
*  can I come and buy like on sort of an API basis,
*  like one call against that new instruct model?
*  So you have both a kind of pay per use,
*  pay per token model.
*  And, but it sounds like more of the business is ultimately,
*  because people have their own custom models, I guess,
*  they can't use shared infrastructure anymore, right?
*  When they've got custom models,
*  cause you don't want to be like,
*  you have too much load, you know, cold start problems.
*  So you're more often selling compute
*  on a dedicated capacity basis.
*  And the value add is helping people understand
*  what dedicated capacity they need
*  so that they can, you know, spend efficiently.
*  Yeah, exactly.
*  So we have two ways,
*  two pathways for their inference service.
*  The first is the starter series,
*  where there's a list of supported models
*  that are basically models we build,
*  open source models that can just pay per use, right?
*  So you can match that as kind of like shared service,
*  like you have the providers out there.
*  So I think that's maybe like the place
*  where you got like the one set for 40 pages, right?
*  That's kind of a starter, you set in the model.
*  Then once you train your own custom models
*  and you want to deploy them,
*  that's where you're going to transition
*  to the enterprise service,
*  where you're going to not be paying for requests,
*  you're going to be paying this, like, as you said,
*  dedicated capacity that will help you figure out.
*  And for there, it's like really, you know,
*  basically a cost per hour.
*  And then that can satisfy a certain workload.
*  And so do people, they buy that through you
*  in a way where they don't even,
*  like, do they know like,
*  oh, I'm deploying this on AWS
*  and it's kind of a transparent model,
*  or are you like reselling the underlying cloud compute?
*  It is fully transparent, right?
*  Like I think one of the core features of Mosaic
*  is that we will run the workloads wherever is required,
*  you know, based on your security constraints,
*  based off your existing like contracts that you may have.
*  And it's like, partially you can rent it through us,
*  but it's just an option, right?
*  So we train ourselves just like all other computers.
*  Gotcha, okay, cool.
*  So if you had to estimate,
*  going back to that original question,
*  if I rent GPUs by the hour, let's say on AWS or on Oracle,
*  what would you estimate their stack kind of looks like
*  in terms of how much of their per hour cost
*  goes to electricity?
*  How much of their per hour cost
*  goes to buying the physical hardware?
*  I mean, I think the simple answer is, you know,
*  that's their internal numbers and you don't know.
*  And I don't think it's a good kind of
*  for us to speculate on that.
*  I would guess that the electricity
*  is probably a relatively small amount
*  compared to the hardware,
*  but that's just a complete guess.
*  And, you know, happy to refer you to our friends in Oracle
*  if you wanna ask them.
*  Yeah, all right, well, we might take you up on that.
*  This is something I definitely am trying to triangulate on.
*  Because ultimately, you know,
*  some of this stuff goes on the edge eventually, right?
*  And then it's like, you have no marginal cost
*  of device arguably, and you know, it's just electricity.
*  So I'm trying to kind of scout out a little bit to some,
*  then not that that's gonna be the end all be all,
*  but there's some part of the future
*  that kind of ends seemingly at like
*  marginal cost of electricity.
*  So trying to kind of sketch out to like what that is.
*  And it isn't super easy to figure it out.
*  Anything else we should cover on inference?
*  And then my next thing is to switch gears
*  and go to the new 65K context window model.
*  The only thing about it, as I said,
*  is that Grange said, please reach out
*  because I think we have very competitive pricing
*  and a lot more transparent model
*  than some of the other eight-gap products out there.
*  So we want to build customers for them.
*  Yeah, so it's not.
*  And I vote their own on that.
*  If you want to do better, reach out and get a safe fee
*  because we're definitely getting,
*  as our research team is learning,
*  we are getting booked up very, very quickly.
*  Certainly, you know, it's,
*  we're making hard choices between research
*  and customers right now because there's so much demand.
*  Yeah, I'm not surprised by that at all.
*  Following your trajectory, you know,
*  from $500,000 GPT-3 quality, you know,
*  however many months ago to the more recent, you know,
*  stable diffusion for like, I think it was like 150K or so.
*  And now all this new stuff as well.
*  Like I would expect the phone is ringing off the hook.
*  Less than 50K.
*  Gotta get that number.
*  Oh, less than 50K.
*  Yeah, okay, thank you.
*  I think we crossed the price tag a few times.
*  So it's changed a bit.
*  Yeah, you guys are hard to keep up with.
*  There's a lot of releases.
*  So, okay, let's talk about this.
*  One of the aspects of the recent set of releases,
*  the story writer model, 65,000 token window
*  extends even beyond that.
*  So I understand, you know, I've read the paper a little bit.
*  I'd love to get a little bit better intuition for,
*  it seems like this alibi approach
*  is kind of the heart of the upgrade there.
*  And what we're doing essentially is replacing
*  the original old school positional embedding scheme
*  with a new, seemingly more intuitively justifiable
*  principled positional embedding approach.
*  But it still seems like the model like gets big still,
*  right, like to have that long token window,
*  you still like, attention still like scales
*  with the square of the context window,
*  do I have that right?
*  Nothing has changed about that, has it?
*  Yeah, no, 100%.
*  It's still the same amount of work as before.
*  We were just seeing that positional embedding
*  and they're placing a bias in the kind of attention.
*  But yeah, so I think some of the nuances here
*  is that that quadratic portion of the attention
*  is actually not as big as many people might think.
*  You know, for a lot of very large transformers,
*  you know, like if you're training them with the context
*  of like say 2K, you actually want the work being done
*  that kind of attention dot product.
*  So it can be less than 10% of the real work of the network.
*  So yes, as we're stretching out the context
*  and I've got from 2K to 4K to 8K,
*  yes, we're stretching it 10%, a lot, lot bigger
*  that piece of the pie.
*  It's not like a ridiculous technology.
*  You know, as a kind of point in the sand,
*  when we trained our story writer model,
*  it's 55K context window, right?
*  So we had the base model,
*  then we're fine tuning the small context.
*  The kind of work done for token went up by that 4X.
*  So you can think about like the cost to train,
*  say like a couple billion tokens was 4X larger
*  for that context window,
*  then it would have been a 2K context window.
*  So yes, it is bigger, but it's not like ridiculous.
*  So from two to 65,
*  and it's actually even bigger than that, right?
*  Cause you allow it to go.
*  Yeah, so at inference time, you can actually kind of,
*  you can technically go to any infinite context,
*  but practically speaking, you know,
*  maybe like 2X more than it's been trained for, but yes.
*  So how does that,
*  so how can you have an infinite context?
*  Is something just getting truncated eventually there,
*  or you're like rounding at some like distance,
*  you're rounding down to zero?
*  Cause otherwise, traditional, you'd have,
*  that would mean an infinite by infinite matrix, right?
*  Yeah, no, absolutely.
*  I bet the infinite is definitely like has a lot of aspects
*  that are like, you know, your hard roll around of memory
*  at some point, so it's not really,
*  and eventually you'll get tired of waiting as well.
*  So that's not quite infinite.
*  But what has happened with Alibi
*  is that there are these kind of slopes,
*  biases that are being at,
*  you can imagine like there's a slope from negative one to one
*  from like the zero position always to end one.
*  And when we go out to like a very, very long context window,
*  all we're doing is stretching that slope out
*  cause it's a continuous slope
*  to whatever kind of target inference context
*  like that we want.
*  So we trained with 2K and we can work with like,
*  you know, negative one to one across 2000 tokens.
*  And then for the time we're going to do 4K
*  and then we just stretch it out farther.
*  So the bias being added,
*  it's basically more of a good way.
*  So in the 65K model that you have released,
*  is there like, there is still some sort of hard cap of like,
*  this is the max number of tokens that this thing can handle?
*  No.
*  Not really.
*  But in the model, you can see on the home page as well,
*  the config, we have the max SQL slope of 65K.
*  But you can totally adjust it.
*  So you download the model,
*  you change that one line to config,
*  and then when the model is instantiated,
*  it will just create its alibi bias
*  to whatever SQL slope you wish.
*  And you will be able to use inference up to say like,
*  130 or something like that.
*  Yeah, I think the only two limitations
*  that you'll encounter with alibi,
*  and this is why we love alibi,
*  is number one, you'll just run out of memory.
*  That is your first limitation.
*  So, you know, if you need a bigger beefier GPU
*  with more RAM to do this,
*  or you need fancier parallelism or fancy caching
*  or things like that,
*  the only other limitation is, you know,
*  that past a certain point, you know,
*  empirically, if you've trained at a certain context window,
*  alibi doesn't seem to extrapolate that well beyond about 2X
*  whatever the context you trained on.
*  So you'll run into kind of algorithmic issues there
*  where the model, you know,
*  the quality of the outputs will start to degrade
*  if you get much longer than that.
*  But otherwise really, you know,
*  alibi can just keep going to whatever amount of memory
*  you have signed for memory,
*  and that can give you a longer sequence.
*  So I'm still a little bit lost,
*  and this is one thing I do where I just like,
*  fixate on things and keep asking questions,
*  and so I try to understand it,
*  or until I eventually hopefully understand it.
*  I've got finite parameters,
*  but in principle, you know, if I had infinite memory,
*  I could go to infinite tokens in the context window.
*  How, what, can you unpack that transformation
*  of these like finite learned parameters
*  into that infinite attention,
*  you know, approaching infinite attention matrix?
*  Totally, yeah.
*  So maybe the best way is we could start with
*  something that's close to a transformer,
*  something that just has no position knowledge at all, right?
*  So you have all the learned weights,
*  which are like the word embeddings
*  and the weights of all the matrix multiplies and so on,
*  but nothing for the attention matrix, right?
*  And so as you feed in tokens
*  and you kind of save their capabilities,
*  you can always keep attending to more and more and more.
*  It's just that there'll be no position like information,
*  so you're looking at a bag of words,
*  you're looking at like a whole jumble of words
*  and your next token's attending to them,
*  but has no idea which one came first.
*  So that model, you could stretch out to any class
*  and do which, right?
*  There's no learned parameters going on
*  with the attention now.
*  The one thing that Alibi happens is that it's this bias
*  that is set up at initialization that can be stretched
*  and it's not learned, it's like a fixed set of slopes
*  that go from like negative K to like K.
*  And so that's the kind of matrix
*  that you can basically adjust dynamically at different times.
*  Say I wanna stretch this out over a thousand positions
*  or over 2,000 positions or over 100,000 positions.
*  So that's what it says.
*  So the Alibi kind of mechanism
*  is not like a learned mechanism
*  and that's what makes it possible
*  to use whatever sequence it wants.
*  Yeah, I think to get to the heart of your question,
*  the attention weights are shared.
*  So for each position, for each encoded token,
*  you're using the same attention weights.
*  You've got parameter reuse.
*  And so technically your sequence doesn't matter
*  and you can just keep reusing those same attention weights
*  for any token that you have.
*  In the same way that a convolutional network,
*  in many cases can be completely agnostic to resolution
*  because you're just doing the same convolution
*  across multiple different positions in the image.
*  So that's why fundamentally there's no issue
*  doing an infinite sequence like,
*  other than running out of memory,
*  you need somewhere to store the activations,
*  but a finite parameter model,
*  you're just reusing that same fixed number of weights
*  over and over and over again at every sequence position.
*  Anything else we wanna cover on the 65K,
*  anything on the flash attention or other enhancements there
*  that you think people ought to know about?
*  One of the models 65K,
*  we showed some demonstrations that,
*  pretty cool, great gaps,
*  writing out a blog afterwards.
*  But I'd say one focus coming up soon
*  is for gonna be something on performance.
*  Basically making sure that,
*  it doesn't take like minutes to write.
*  I think one really impressive part of playing the game
*  is recently released is that,
*  the model actually writes quite quickly.
*  And you'll probably see some content per month
*  breaking down how to actually use long context windows
*  and where it gets faster and slower.
*  So it turns out reading is a lot faster
*  than writing these transformers.
*  You need to fit in 65K of context into the input
*  and that will go relatively fast.
*  But then to generate every token out,
*  it's gonna take some time.
*  So you'll see a lot of improvements for this
*  in the coming weeks and months of this,
*  as well as potentially seeing
*  architecture features that make you very...
*  I think I'll throw in perhaps,
*  as we get into the last word,
*  keep your eyes out on things that are coming from us.
*  We've released a lot over the past couple of weeks,
*  and that cadence is not gonna be slowing down at all.
*  We'll be able to have a lot more work
*  that's gonna be churning out over the next days,
*  weeks, months.
*  So I hope we'll be having these conversations a lot
*  over the next while.
*  MBT-70 and stable diffusion for less than 50K,
*  those are kind of the more baselines
*  that we're gonna be crushing over the next little while.
*  Well, that's a great teaser.
*  I look forward hopefully to a part two
*  in the not too distant future.
*  And it sounds like you'll have some exciting new stuff
*  to help us break down and understand.
*  But for now, Avi Venegala and Jonathan Frankel,
*  thank you for being part of the Cognitive Revolution.
*  Thank you so much for having us.
*  Thanks so much.
*  Omniki uses generative AI
*  to enable you to launch hundreds of thousands
*  of ad iterations that actually work,
*  customized across all platforms
*  with a click of a button.
*  I believe in Omniki so much that I invested in it,
*  and I recommend you use it too.
*  Use Cogrev to get a 10% discount.

---
Date Generated: April 03, 2024
Transcription Model: whisper medium 20231117
Length: 5631s
Video Keywords: []
Video Views: 995
Video Rating: None
---

# Keeping the AI Revolution on the Rails with Shreya Rajpal of Guardrails AI
**Cognitive Revolution "How AI Changes Everything":** [May 23, 2023](https://www.youtube.com/watch?v=97plVwe5hxI)
*  it's insane to see just the amount of activity and excitement around the space. There's people
*  training and fine tuning deep learning models that weren't even in the space a few months ago.
*  That's really awesome. I had people who were like, I really like guardrails, I really like opening
*  eyes, but it's just too expensive for what I'm trying to build. Can you make this work with
*  an open source model as an example? I do think that we're going to see a lot of that proliferation
*  happening with great performing models from different price points, different latencies,
*  different providers, etc. Hello and welcome to the Cognitive Revolution, where we interview
*  visionary researchers, entrepreneurs, and builders working on the frontier of artificial intelligence.
*  Each week we'll explore their revolutionary ideas and together we'll build a picture of
*  how AI technology will transform work, life, and society in the coming years.
*  I'm Nathan Labenz, joined by my co-host Eric Tornberg.
*  Hello and welcome back to the Cognitive Revolution. Today my guest is Shreya Rajpal,
*  a former machine learning engineer at Apple and founding engineer at Predibase, who is now best
*  known as the creator of Guardrails AI, a new Python library that allows developers to add a layer of
*  output validation and correction to their code. As anyone who's spent time building AI-powered
*  products over the last two years will attest, validation and even more so reliability are key
*  challenges. LLMs simply don't always follow instructions and sometimes go entirely off the
*  rails. Better models have helped tremendously, it's true. GPT-4 can follow instructions far more
*  reliably than earlier models and Claude V1.3 is also very impressive. But with this elevated
*  capability also comes expanded developer ambition and so it seems that for the foreseeable future
*  the problem of LLM reliability will remain both critical and ubiquitous.
*  Shreya's work tackles this problem in many ways and at multiple levels. Super practically,
*  Guardrails can ensure a reliable interface between language models and more traditional
*  deterministic software systems. Validations like, did the language model return data with the right
*  type and format? Or, did the model choose a value from the list of allowable values that we provided?
*  These are very familiar questions for developers and are still powered in Guardrails by traditional
*  code. But at the same time, and for me this is clearly the more novel, exciting, mind-bending
*  and potentially risky use case, frameworks like Guardrails allow developers to ask and answer
*  entirely new kinds of questions. Assessments of things like the quality of a summary or translation,
*  or whether a given piece of text contains any redundancies, inconsistencies, or gaps in logic,
*  these are the sort of things that until recently developers simply had no way to validate.
*  Thus, for product and engineering teams around the world, Guardrails is both a solution to a
*  very practical problem at hand and a sort of introduction or bridge to an emerging paradigm
*  of AI-first software development that goes well beyond the copilot-style autocomplete
*  or even chat interfaces that we've recently seen, and begins to use AI functions not just as
*  development tools, but as components of the production technology stack itself.
*  Talking to Shreya really reinforced for me just how early we are in LLM's impact on the software
*  industry. The core AI capabilities needed to transform software, as far as I can tell,
*  mostly already exist. What remains, though, is the work of reimagining not only how software is
*  built, but how it functions now that intelligence can be baked in at any point. Personally, I believe
*  that this paradigm shift could ultimately unlock bigger productivity gains and more user value
*  than the current generation of tools that increase developer speed, but don't yet attempt to change
*  the kind of software that they're building. At the same time, this is also something to be
*  approached with real care and caution. The delegation of AI output validation to other AI models
*  is not a step to be taken lightly or taken for granted. I hope you enjoy this thought-provoking
*  conversation with Shreya Rajpal of Guardrails AI. Shreya Rajpal, welcome to the Cognitive Revolution.
*  Yeah, really excited to be here. Thanks for inviting me.
*  My pleasure. This is the first time that I've invited a guest. Basically, as soon as I got off
*  the call recording a previous episode, it was Matt Welsh, CEO of Fixie.ai, who mentioned your
*  new project, Guardrails AI. I was immediately like, okay, I have to learn everything I can
*  about this. I'm really excited to dive into it with you. I guess let's start with
*  what made you say a couple months ago, I need to build a system to help people keep their
*  language models on the rails. Yeah, I was really solving my own pain points and my own problems.
*  I had been, end of last year, I'd kind of been doing some tankering on my own where I was building
*  some applications. Even as I was building them, I was like, yeah, this is really cool. I think it
*  was nothing very exciting, like what you're seeing on Twitter about chatting over proprietary
*  documents, et cetera. I was building that and I realized, yeah, this is pretty cool. I can see
*  the potential with this. Even as I'm kind of like, as a developer, testing it out, I can tell that
*  it doesn't get me reliably the desired experience that I want to achieve. I think it was this big
*  problem where these language models are really potent and they're really powerful, but they're
*  also inherently very stochastic and very hard to control. What makes this very interesting is that
*  unlike traditional machine learning, how this is different is that as a developer, you haven't
*  really trained the model, so you can't just throw more data at it, make it work really well for your
*  use case. Then separately, the only knob you really have as a developer is here's this prompt. If you
*  wanted to maybe do something or not do something, how developers typically deal with that is just
*  adding a lot of verbiage in the prompt and maybe a lot of exclamation marks, et cetera, to make it
*  listen to you. That just seems woefully inadequate. Guardrails is this idea of a
*  specification framework where as a developer, you know what the right output for an LLM looks like
*  and you're able to decompose that and individually validate and verify each component of that output.
*  If any of those components fail and if any of those quality criteria that you impose on it fails,
*  it gives you a set of tools to address that in a very extensible manner. I was building this and I
*  was like, yeah, I know what responses I want a user to be able to get from this thing that I'm
*  building and how do I ensure that I'm always able to do that for a wide variety of scenarios.
*  That was some of the inspiration. It also, it's spent some years in autonomous systems and
*  self-driving and it's a similar problem there as well where you have this really powerful,
*  deep learning based perception model that often feeds into this more rule-based decision-making
*  system and how do you essentially ensure that the interface between that stochastic system and
*  that deterministic system is robust and not brittle whenever the perception system maybe doesn't do as
*  well. The idea was to, it was inspired by some techniques you'd kind of see there, but built
*  for language models and built in a very extensible way so that it's not very government-specific.
*  That was some of the inspiration. As much as possible, I love to get super concrete on these
*  things. This is clearly a pain point that a lot of people have. The project has gone on its own
*  little rocketship ride of GitHub stars with 1,200 as of last check at the time of this recording,
*  but probably a lot of people listening also could use a little bit more of a concrete example of
*  what kind of thing are you looking for and how is it failing and then can you tell us maybe a
*  couple of those and then how does the guardrails come in and save the day in those instances?
*  Yeah, absolutely. I love that question. I love digging deep into the details, so I'm happy to
*  do that. I think when I was prototyping guardrails, my favorite kind of prototype example was that I
*  have this Chase credit card agreement, which was my own credit card agreement, and I want to extract
*  what are the key terms, et cetera, from that credit card agreement, get a nice JSON out of it.
*  As a user, I know that if I'm extracting something like an interest rate, it must always be a number,
*  it must be maybe a percent sign, and what is a reasonable range for that? If I'm maybe
*  extracting the name of a specific fee and I want this name to be presented somewhere, I know that
*  the name should be very concise, it should be very robust, et cetera. I think one of the common
*  failure points, et cetera, there is that if I want to extract this information and then it needs to
*  be maybe added to some downstream data sync, it's hard to do that reliably, consistently from an
*  LLM because an LLM doesn't reproduce, essentially. In this structured data extraction setting,
*  I could essentially enforce constraints of what I want each extracted entity to look like. For
*  example, the interest rate must be a number, it must be within this range, there must be a description
*  with each interest rate and the description needs to be some length or some needs to be relevant to
*  whatever the entity that it is coming along with. I think all of those constraints are what I want
*  to impose on this JSON structure. That was a use case that I was prototyping it. I have a ton of
*  examples on my documentation, but one of my favorite ones is Text2SQL. In Text2SQL, it's a
*  wildly different domain, but a lot of the same ideas apply, which is that you want correctness
*  from any generated SQL query. The idea is that as a user, you want to be able to ask natural language
*  queries over your data and get a SQL query that you can maybe execute. A lot of the ideas are the
*  same, which is that you need to be able to, what are the constraints you want to be able to impose
*  a priority on that SQL query? It must actually work for my database, for the environment that I
*  want to execute this query in. Other constraints, you may not want to return results from any
*  specific tables. Some tables might be private, and if you want to say as a customer, you never
*  want to be able to query those tables, you can filter those out. You can add things like only
*  support these specific SQL predicates. If there's any drop predicates or maybe update or insert
*  predicates, you want to be able to filter those out. The idea is that as you're setting up this
*  text to SQL task, you can add all of those constraints. How Godreal solves this problem is
*  it takes your database schema and sets up a SQL sandbox for essentially any SQL query that is
*  generated. It's executed in that sandbox to make sure that it's executable. If it's not executable,
*  you take all of those errors for why the SQL query fails to execute and wrap those errors into
*  something, send it back to the large language model, correct itself, and get something that
*  actually works for your specific database. Then you can add other constraints and other restrictions
*  on top of that, like filtering out specific tables, filtering out specific predicates,
*  etc. I think just this idea of here's a question, here's a task I want this large language model
*  to solve, but as a developer, I have some domain expertise for what correctness means to me in this
*  task and how much I care about that correctness. If it's incorrect, then this query is totally
*  useless to me, or if it's incorrect, I just want to know about it and maybe post-hoc I'll handle it.
*  I think that is the main idea, and Godreal takes that and allows you to basically think of that
*  as a developer. Hopefully, that was a little more grounded in terms of female-specific examples.
*  It's fascinating. One of the things I want to explore the most in this conversation with you
*  is the, seemingly, we're opening up a spectrum or a dimension, if you will, where we can go from,
*  on the one end, explicit errors, like the errors that we are used to as developers in code,
*  and that could be starting with a syntax error, up to more meaningful errors,
*  like, but that could still be found through traditional software messages, like,
*  this variable doesn't exist, or all sorts of things like that. But then you've got a whole domain of
*  correctness, which code has never really accessed before, and that is, what are you trying to do?
*  Does this appear to be a reasonable approach or output from a much more semantic or, dare I say,
*  intelligent point of view? But I find myself a little confused or a little bit lost in that
*  space, and I see that you're covering it in a really interesting mix of ways. In the library,
*  in the validators, there's a mix of validators. So maybe walk us through, tell us how you think
*  about that, I guess, and again, maybe some examples of different validators that sit in different
*  parts of that space would be helpful to help people understand what I'm talking about.
*  If it's already clear. Yeah, I think that's a very, I think that was kind of like one of the very
*  exciting things about the library as I was building this out, which is that the general
*  framework works even outside of things you can't maybe use an assert statement to verify or
*  something. It's really extensible as a framework where you can have a mix of large language models
*  and maybe some rule-based heuristics, some programmatic checking, as well as more traditional
*  machine learning models that are very maybe high precision classifiers, etc. And you can ensemble
*  all of these techniques together to get something that is greater than the sum of its parts and
*  much more robust and much more reliable compared to just using a pure large language model.
*  So as an example of that, I last week added a bunch of guardrails for summarization. So if you're
*  summarizing multiple documents and maybe generating an aggregated summary from that,
*  there's a bunch of requirements that you may have in order to ensure that that summary is accurate,
*  that summary is concise, it's not redundant, etc. And so how guardians kind of thinks about
*  this general problem of correctness when assert statements aren't sufficient is to really break
*  it down into either a smaller ML task or into smaller verifiable heuristics, etc. And tries to
*  get an aggregate assessment of how well this works. Hey, we'll continue our interview in a
*  moment after a word from our sponsors. I want to tell you about my new interview show, Upstream.
*  Upstream is where I go deeper with some of the world's most interesting thinkers
*  to map the constellation of ideas that matter. On the first season of Upstream, you'll hear
*  from Mark Andreessen, David Sachs, Balaji, Ezra Klein, Joe Lonsdale, and more. Make sure to
*  subscribe and check out the first episode with A16Z's Mark Andreessen. The link is in the
*  description. Omnike uses generative AI to enable you to launch hundreds of thousands of ad iterations
*  that actually work customized across all platforms with a click of a button. I believe in Omnike so
*  much that I invested in it, and I recommend you use it too. Use Cogrev to get a 10% discount.
*  So in the case of summarization, what that looks like is if you essentially want to
*  figure out if the summary is faithful to the original source text, how you can do it is
*  basically look at each sentence in the summary and then essentially do something like a similarity
*  matching based on which parts or which passages or sentences it's most similar to in the source
*  text, which allows you to do much more fine-grained attribution and figure out where is the sentence
*  that it's generally coming from. The other cool thing that you can do on top of this is that you
*  can assign thresholds. So as a developer, you can do some experimentation, figure out what is my
*  appetite for how varied I want these sentences to be from the original source text, and then set a
*  threshold. And then any sentence that is below the threshold in terms of similarity score,
*  you can essentially filter out and not infuse that in the summary. So that allows you to,
*  I think it's just this way of thinking about text outputs, which may seem like a single unit,
*  and it basically breaks them down into smaller chunks and independently tries to verify that.
*  So I think other techniques you have in summarization specifically is make sure that
*  there's, I want the summary to be concise, so make sure there's no redundant information.
*  So essentially within the generated summary, essentially make sure that each sentence is
*  diverse enough from other sentences within that, and if that's not the case, maybe filter out
*  sentences that are too similar to each other, et cetera. So yeah, I think the cool thing about
*  LLMs, it's like we are looking at a lot of the first order benefits of that, where you can use
*  this and do a bunch of really insane tasks. But I think the second order benefits are that you can
*  really use these models as verification systems in an optimum cells. So you can use a large language
*  model within a validator to verify and validate whatever you're getting is correct, or you can
*  depending on your access to data and your latency requirements, et cetera, maybe train a smaller ML
*  model that can do this for you, but truly bring together a bunch of these different
*  verification strategies and you'll get something that's more robust. So that's the philosophy
*  behind how Guardrails tries to add guarantees around what traditionally seemed like harder
*  problems to, harder ML problems to verify. Yeah, that's really interesting. I'm
*  mapping this onto my own use cases here in real time. So I'm wearing my Waymark swag today.
*  Waymark is in the video creation space and we have, it's a multi, excuse me, a multimodal
*  problem, right? Where we ultimately take in some minimal information about a business and then ask
*  the user to tell us what they want to create. And then on the other end, provide a ready to watch
*  video. We kind of do that with like an ensemble of different models working together, but the core
*  one is the language model that writes the script and kind of gives the direction for what the visual
*  assets should look like and all that sort of stuff. And I mean, for one thing, boy, we've come so far
*  in a year. It was just a year and a half ago, basically, that we got the very first fine tune
*  GPT-3 to do the task at all, with any sort of like, it wasn't good, but it would at least respect
*  the nature of the inputs and outputs. And now today, GPT-4 can basically do it zero shot and
*  respect the outputs. And then 3.5 turbo kind of not really reliably, but then I think, geez,
*  it is like 20 times cheaper. So I guess I'm interested in kind of what do you see the value
*  drivers being for this sort of thing? To some degree, maybe like there's no other way to do it.
*  But as I'm kind of running through my head, I'm like, so on some of these things like GPT-4 is
*  pretty reliable at this point. So people might want to do it for cost savings or they might want
*  to do it for, I don't know, I guess a lot of different reasons, but cost savings and
*  latency are actually one. I would see like benefits to that potentially if I could move
*  to a little bit of a less reliable model, but still like know that my stuff is going to render
*  in the right way for our users. So what are you seeing in terms of like the value drivers from
*  your community? Yeah, yeah, I think that's a really great question. So I think there's two aspects of
*  it. So cost and latency, maybe being able to use like open source models or like cheaper models
*  with like the same level of reliability, etc. I think like that is like one aspect. But the more
*  interesting aspect for me is, you know, like what is the task that you're truly using this model
*  for? So, you know, like Waymark, there's a lot of use cases where you're using these models as maybe
*  writing assistants or to, you know, like help you. One of the ones, one of the products I enjoy using
*  is like Notion AI Assist, I think it's what it's called, where you draft a little bit and, you know,
*  it helps you like maybe shape up an outline, etc. So I think for those use cases, the creativity
*  of a large language model is actually really good, and it's a desirable trait. But I think at the
*  same time, there's this whole other space of use cases that are, you know, like where that rely on
*  the world model that is, you know, like ingrained in these large language models. And, you know,
*  it uses these large language models as like software instruction to do more general purpose
*  reasoning. So I think there's a wide variety of those use cases that are seen. So for example,
*  one of them is that use an LLM to basically, you know, as like an AI receptionist, essentially,
*  where you're a small business owner, and you instead of, you know, leading to higher
*  receptionist, you can use a large language model and anytime you get calls, it, you know, figures
*  out scheduling, figures out who's available, etc. So that's a very powerful capability of that model
*  where, you know, creativity is maybe not as good a thing, right? Like you wanted to maybe stick to
*  some desired workflow that you want to be able to ask, you want to make sure that maybe you don't
*  ask for private information, if you know, like a customer is calling, etc. So I think like where
*  guardrails is like most useful is within those constraints where you use the LLM, not just as a
*  text generator, but as like a software instruction, really. And when you're using it in that capacity,
*  that is when like reliability becomes most useful. I think over the weekend, I shared something that
*  a community contributor had built using guardrails, which was, you know, this GitHub action called
*  auto PR. And what auto PR does is it, you know, takes a GitHub issue and then automatically creates
*  a code request from like GitHub issue, like for your code base. And that is, you know, that is one
*  of those use cases that has like a bunch of really strict constraints, right? Like this files must
*  exist, the code, the diffs that are generated must be valid for those files, etc. And those constraints
*  are pretty hard to enforce, like without having some validation frameworks such as guardrails and
*  pop-up it. So I think like for a lot of those use cases, you know, like creativity is like not as
*  nice a thing and you want like more reliability. And I think like it's still like such a powerful
*  use case of this model that it would be, yeah, we would be kind of under like under utilizing
*  their capability if we don't build software such as that, you know. Yeah, it's like it's a mix of
*  both. I think even with a lot of the creative use cases, I've kind of found that there's still like
*  a bunch of constraints that, you know, people implicitly have that, you know, right now the way
*  to do it is like via prompt tuning or prompt iteration, but truly being able to, you know,
*  like encode these constraints and like maybe only like instead of like manually having to do this,
*  you know, like have a validation that runs and then, you know, only do it like when needed is
*  like also a pretty nice workflow where you, for example, you might not want any profanity in like
*  scripts that are generated or you might, if you're creating like video content for someone,
*  you might not want to mention, you know, like peer products or like competitors,
*  et cetera. And so I think like those kinds of constraints are also useful even with freeform
*  test. So it's, yeah, it's a mix of both. It sounds like though you are most excited about
*  something that could not be achieved in traditional code. And I still kind of really trying to find
*  that line or like, I guess there's maybe just a lot of overlap. A lot of times when I get to these
*  kind of puzzling moments as I study different aspects of AI, I end up kind of finding that it's
*  like sort of both in the end. And there's probably a lot of truth to that here too. I'm thinking,
*  okay, so we're in the GitHub, not whatever, the automatic pull request, auto PR was called, right?
*  I saw this. It is cool. And super technical to some degree, those responses could be validated
*  presumably by like existing libraries. Like I'm sure, you know, the Git package itself has like
*  some way to sort of say, you ain't got your shit together. So, you know, this is not going to work.
*  And I think that's kind of what a lot of people are like naively doing is, you know, just kind
*  of implementing that stuff on a case by case basis. Like at Weimark, there is no standard,
*  nobody else has our video standard. Like we totally define it and own it. So, you know,
*  it was up to us to figure out how do we represent that in text and then like what validation
*  comes back from that. So I think one thing we could maybe have tried to do is,
*  you know, we did this before you'd launched the project, but I kind of wonder like if you're
*  advising us, you know, and we were maybe a little earlier, how would you think about like what points
*  of validation we might, you know, ought to do through guardrails? Like should we be thinking
*  about structure or should we be thinking like, does this copy like satisfy the user's prompt?
*  Or, you know, I guess there's probably a lot of room in between, right? Those kind of stake out
*  the like most rigid versus most kind of semantic, you know, desires or requirements from the model.
*  It seems like you're more interested on some level and the semantic side, but that there is
*  this kind of like fundamental interface with computing where it gets like very
*  syntactic as opposed to semantic as well. I think it's a good question. I do want to say
*  before I say this, like I want to preface this by saying that like generating something and getting
*  outputs, you know, getting feedback from the end user about, you know, is this good? Is this like,
*  does this meet your original criteria? And doing a more like qualitative assessment,
*  taking that feedback and, you know, going back to the drawing board. I think that's a very valid
*  way of doing things, right? Like I think for a lot of domains, you know, like getting that human
*  feedback and getting that human input and write off is like essential before you can like really
*  think that this output is correct and is valid for, you know, whatever use case you have. But I
*  think like for like in the guardrails world, there's basically this idea that, you know,
*  maybe some parts of that human feedback can be done by a combination of, you know, traditional ML,
*  heuristics, and maybe more large language models in the loop, right? And if you are able to,
*  you know, like take some of that, encode whatever that qualitative criteria is into, you know,
*  like codify it into something that is more specific, what you're then able to do is,
*  you know, like generate specific like failure error messages, etc., that help the model
*  output correct itself, right? So in terms of like maybe how that would like, I obviously don't know
*  as much about remark, but what that might be helpful in is, you know, like maybe doing the
*  number of like back and forth you have to do with your end customer, because you're just able to
*  take some of their constraints, you know, run those programmatically, if they're wrong, like automatically
*  create like new prompts that, you know, tell the large language model why previous outputs are
*  incorrect and get it to correct itself. So I think this is like one of the net new capabilities
*  that we have, you know, with large language models that didn't exist previously, which is, you know,
*  their, their understand, like the ability to get them to like self heal or self correct themselves,
*  if you give them enough context. And that is where like guardrails, like I think a lot of the
*  frame, a lot of the like core functionality for guardrails, you know, like, like really harnesses
*  that. Right. So what, how it, how it functions under the hood is like, it's really good at, you
*  know, figuring out like what the relevant context is, you know, like packaging it up nicely,
*  automatically creating a new prompt from for you, reaching, like getting a new response from the
*  large language model, merging that new response, you know, with the old response that you had,
*  because it only it's very efficient, it only we ask like things that are wrong, not like your whole
*  previous output, etc. So it merges all of that together. And then, you know, you're then like,
*  that is your corrected validator response. Sorry. So I think that is the world where like
*  guardrails is most useful. And like with that said, it is very domain specific, right? Like
*  there are domains where, let's say something like any text that is generated must be funny.
*  Now that is something that is like next to impossible to validate. And I can't imagine
*  like writing a validator that maybe assigns like a scoring function to humor, right? Like that's just
*  very hard to do. And so you can't do that. And you need to have like a human group.
*  Maybe there's like some other domains, right, which have like very high stakes and very high
*  cost to like getting something wrong. But even if like maybe you can do some pre scoring, etc.
*  The actual like human, you know, confirmation that this output is correct is like essential
*  before you can do another like iteration with the large language model, etc. So there are those
*  domains where, you know, this re asking strategy doesn't work. But I do think just this idea
*  of, you know, like taking what is correct, like what is correctness, or what does, you know,
*  like an aligned output mean in your use case and trying to like codify some of that is useful,
*  both in terms of, you know, like prompting the large language model that allows
*  guardrails to construct like prompts that are, you know, more effective at getting you what you want.
*  And then it also allows you to like post hoc validation and this, you know, like a loop of,
*  I want to systematically programmatically handle, you know, failures as and when they arise.
*  And, you know, maybe that involves like re asking that involves like filtering any like incorrect
*  output, etc. I think this is a very powerful framework to like require less human supervision.
*  And, you know, like take a lot of that pain away of like, maybe going into chat, you know,
*  writing, like, okay, this doesn't work for this reason, or trying to get something else.
*  So that's that's the world in which like that's a hypothesis behind guardrails.
*  Maybe it's just because we all have agents on the brain. But as I'm listening to you describe that,
*  I'm really going to this agent, you know, moment that we're in and sort of really when you dig into
*  these agent systems, it's usually like, you might think of it more classically as like a multi agent
*  system. In many cases, like it's the same language model playing the role of different agents.
*  We're seeing all these examples where it's like a simulated town where, you know,
*  GPT-4 plays all the people, or, you know, a research agent where there's like a planner
*  and a coder and a, you know, retriever that all kind of work together and have their own
*  prompts, and they're all kind of scaffolded together. And then, of course, you know,
*  these things fail a lot, because they are, you know, there's some probability of being wrong at
*  any given point in the chain. And then you're only in the naive implementation, you're only kind of
*  as strong as the weakest link in the chain. So in a sense, I guess what I'm learning here is like,
*  this guardrails paradigm is like connective tissue between the different roles in a like multi agent
*  system. And I should probably accelerate how quickly I think that these agents are going to
*  start to work. I think it's a it's a yeah, agents are very exciting. Like I think I've been thinking
*  about them a bunch and trying to think about like, you know, how do you how do you make them
*  more effective, more reliable. I think the interesting thing about agents versus how
*  guardrails works is guardrails is, you know, essentially, the main problem that is solved is
*  like, I want to add constraints on this output so that it works for my use case, right? It works
*  for what I wanted to work on. But essentially, it gives developers a lot of agency to think about,
*  you know, like their specific the specific problems that they're solving, you know, what
*  correctness means to them. I think like contrasting that with the with Asian frameworks,
*  where, you know, a lot of the goals of agents and a lot of the the tasks of agents are like configured
*  autonomously, like by a large language model itself. So you're in this like interesting setting where
*  the the involvement of a human or a developer in terms of, you know, like your ability to kind of
*  like enter something like an agent framework and like add guarantees, etc. You typically like with
*  the agent framework that exists today, you typically don't have access to that fine grain
*  level of like a task execution or goal setting, right? Because you're not the person who's
*  configuring these these agents themselves. So I think like there's this. So I think like that is
*  the gap between like how agents operate today versus, you know, what what humans would ideally
*  like to have like ideally, if you're if you're a person who wants to, you know, like employ a
*  bunch of these agents, and you know, maybe do research for you, etc. You want to be able to say,
*  you know, like, this is the set of allowable things that you're able to look at. But also,
*  you want you want that to be configured dynamically based on like where agents are operating.
*  So I do think that like, so that is the context. And if I were to summarize into like what that
*  means for, you know, agents, I do think like constraints are essential. And like, correctness
*  specs are essential, right? It's the only way to think about like, how do you how do you assess
*  what these large language models are doing? Like you can stream them and you know, you evaluate
*  them at each step to make sure that they're not going off the rails. But like, how do you do that
*  dynamically when you're not the person who's, you know, creating these agents setting their goals,
*  etc. I think like that is the key problem to solve there. So yeah, it's a problem I'm very excited
*  about. And I think it's a problem that you're willing to get solved before these agents are like
*  employable before you can truly use them, you know, outside of just like seeing how exciting
*  they are. Yeah, I guess like for agents, you know, I'm always very curious to see people's
*  use cases for like for waymark specifically, you know, where once again, we're like in this domain
*  where, you know, there's like constraints and there's like a finite scope of like what you want
*  the large language model to do, etc. If you like looked at some of these agents and you know, like
*  thought about like, what is something that you would want to, you know, like add into
*  what part of, you know, the waymark stack could be aided with like agents?
*  Yeah, it's probably not such a great fit. I don't think for the waymark product experience because
*  we do have a lot of structure. I kind of think of these things as
*  this is, I'm still working out this framework, but I talked about this with Matt, actually,
*  and this is part of what led to him mentioning your project. So we kind of bring it full circle,
*  but I kind of think of different, I don't know if this is a spectrum or a binary or multiple
*  categories or what exactly, but in terms of like how we interact with AI systems, there seems to be
*  a like real time co-pilot mode where you are doing stuff as a human and the thing is like there to
*  kind of guide you, shepherd you, whatever. And then there's things where you're kind of ultimately
*  delegating more because you really don't want to do it. You know, you don't want to be the person
*  in the driver's seat or the entity in the driver's seat. You want to put the AI in the driver's seat,
*  let it do it, and then look at its work once it's done or have some other sort of way to like
*  circle that back into your life. And those workflows right now are largely done with
*  like integrations, you know, various kinds that could be code, no code, you know, Zapier, what
*  have you, with way markets code. And it's a pretty guided experience where like, you know,
*  you are delegating the task of writing a script, you know, choosing all the assets for your video,
*  etc. And then what you get to do is watch the output. So there's so much structure there that
*  it doesn't feel like we really need an agent to like come in and, you know, mix it up too much.
*  But I do see the agent as sort of the bridge between these two modes where you're like in
*  real time, I sort of want to send something off. So if I'm in ChatGPT Plus today, I can like
*  use a plugin perhaps to look for flights. But I really more might want the thing to be like,
*  go book me the flight for, you know, whatever date like subject to my preferences. And ideally,
*  like it would kind of figure out all the downstream mess of that. So where I think this is
*  actually really relevant for me. So I'm also working with a company called Athena, which is
*  in the executive assistant. So I also talked about this with Matt. And, you know, they have those
*  kinds of things all the time, where, you know, a human today is like responsible for executing a
*  lot of web tasks, you know, for a client. And there's kind of, you know, different aspects of
*  the cognitive work there. One is like, understanding what's going on, like translating
*  the language to and from the client, like you got a request, right? What does it mean?
*  Understanding what it means. And then the other part is like being able to like actually hit the
*  right buttons to make it happen. And ideally, we delegate that whole thing. But the agents,
*  you know, that's where we are kind of testing like along with everybody else, we've kind of found,
*  yeah, we may have AI that can understand the request, you know, parse it effectively,
*  you know, ask the right follow up questions, you know, at least suggest some pretty good follow
*  up questions, demonstrate a really robust understanding of like what the human wants.
*  But we're falling down very much still on like, how do you actually, you know, hit the right
*  buttons, check out, I mean, God forbid you have to like do a payment, you know, process,
*  or like log into something. Like two factor authentication does still work as a deterrent
*  to AI login for the time being, at least. Yeah. Yeah. I think that's kind of been like my
*  experience and my exploration as well, which is that there's, you know, there's this like, there's
*  this interesting like wedge where agents can be useful, but in order for that wedge to succeed,
*  you need this notion of like grounding, right? Of like being able to like figure out like,
*  okay, here's how it understands what I'm saying, but like at each step of that execution,
*  you need validation. So I think this idea or the problem by way, book me a flight is like very
*  interesting because book me a flight, like given my, given my schedule and given my budget and
*  where I'm trying to go, right. And that translates into maybe like some constraints that are then
*  grounded, like based on your calendar or based on your, you know, based on like where you're
*  trying to go and like what flights are available. And so I think like validation at each like
*  decision that the large language model makes and each action that it makes like becomes, you know,
*  more important for these things to succeed. But at the same time, like, you know, having, having
*  worked in like the self-driving world a little bit, like part of it is like, are they able to
*  do it? And part of it is like, can a human, you know, this is like trust deficit, right?
*  Where even if, even if these agents were perfect, there'd be this trust deficit between how much
*  people are comfortable, you know, delegating. And so even in terms of like building that,
*  you need, you know, like, you need this like verification system essentially that makes sure
*  that each step of the way you're able to kind of like have control and have some oversight and do
*  like how they execute themselves. So I think those frameworks would be kind of like essential
*  before we're able to see their adoption outside of, outside of like demo use cases.
*  Yeah. It's funny that you say that. I would actually take the other side of the bet there
*  when it comes to the human behavior. I mean, if I understand you correctly, you're saying people
*  won't want to trust these systems unless there's good guardrails in place. I think of you as saving
*  people from themselves because I think people are going to be much more quick to just kind of go
*  ahead and be like, yeah, it seems like it works. And why, you know, what's the worst that could
*  happen, right? And I think we may find out, especially, you know, in a future world that
*  the worst could be potentially quite bad. But I do kind of expect that behavior.
*  We, I just recorded an episode of it, a medical school professor at Harvard, Zach Kahane, who is
*  just written this book, The AI Revolution in Medicine. And, you know, this is exactly,
*  I think, the kind of system that he's looking to figure out how to implement into clinical practice,
*  right? Something to kind of help, you know, for now, it's like, of course, the human is in the loop.
*  That's the official recommendation. But even then, you know, it's just so easy to get lazy. It's so
*  easy to kind of be like overly trusting, especially when the models are getting so good.
*  It's fascinating that you can get better performance just by kind of
*  pointing the model at itself. That's one of his big findings was our recurrent theme is that
*  GPT-4 is better at evaluating text than it is at generating. And so, you know, he's starting to
*  develop some of these like self-critique things totally on the fly, like in the context of,
*  you know, just exploration in clinical setting. Yeah, I think this, that's part of like what
*  cardrails like the validation system is also based on, which is that, you know, like it's almost
*  like trust would verify, like you get to generate something would maybe, you know, have it even if
*  you are doing large language model based evaluation, maybe, you know, like have a separate stuff that
*  does evaluation separately so that you have, you know, that additional layer of security.
*  And ideally, this is, you know, back from machine learning, but like the more diverse,
*  you know, evaluators you have, the more kind of like guarantees they're going to be. So just like
*  ensembling is a technique that, you know, I'm pretty bullish on in this space. It's like,
*  what's going to get us that confidence? But the medical, like AI for medicine or medical
*  assist is so fascinating because it's back to, you know, like reminds me of like, once again,
*  like self-driving where, you know, like with the autonomous vehicles that are out there today,
*  maybe like Tesla, FSD, etc. The idea is like, okay, you're still supposed to be very alert,
*  you know, you're not supposed to take, you know, maybe your hands off the wheel or something.
*  I don't have a Tesla, so I don't know. But even within that, you know, there's this expectation
*  that a human should always be, you know, aware and like present, etc. Right. But like as humans,
*  it's so easy to get lazy. And so one of the really, one of the things I'm really excited
*  about in this space is like good, you know, interface design so that like we are able to like
*  get human involvement when it's most needed and like not, you know, like if you're always
*  notifying them, like, hey, pay attention, pay attention, like maybe that, you know,
*  ceases to have an effect. Right. So it's this idea of like, okay, how do we build this balance
*  between like when human involvement is necessary versus like, you know, when we can like maybe
*  offload some of that, do that, you know, more programmatically or more with code. I think
*  like figuring out that balance and figuring out the interface to surface that balance or surface
*  that like division of responsibilities to the human. I think like that is very, very exciting.
*  I'm very, very excited to see like how that evolves. I don't know if it's Tesla either,
*  by the way, but a neighbor of mine does and has the full self-driving package. So knowing that
*  I'm as obsessed with AIS, I am, he was gracious enough to take me for a ride. And first of all,
*  it works way better than people I think commonly realize. Like I got into the car in front of my
*  house. He put his finger on the screen, like, we're going to go here and hit the drive button.
*  And the car drove, like it was not a lot of fuss between just, you know, map, go, and you're
*  riding. But when you talk about like the reminders, that's something I think they've really put a lot
*  of engineering into as well. Like there's like three progressions. I haven't spent a ton of time
*  with it, but there's a couple of, I think it's three levels of first, there was a little maybe
*  visual indicator that like you haven't done anything to the wheel in a while. There's a
*  camera also that watches you from the roof of your mirror in some versions. But then after that,
*  it goes to a little sound. And then after that, it goes to a warning and it's like, we're going to
*  pull over if you don't keep your eyes on the road. So they're pretty far along in that. And I thought
*  that was a really remarkable experience because it is a very delicate balance, so easy to tune out.
*  Obviously they have the hammer there eventually of like pulling over. And eventually they also
*  will kick you out of the program if you pull over too many times. He said, you know, if you're truly
*  sleeping at the wheel, they'll retract your access to FSD ultimately. But it is a fine balance,
*  right? Because you can start to tune these things out. So I mean, how many warnings do we tune out
*  crazy? So the next big thing that's kind of jumping to mind is, okay, you've got this
*  developer, like what is right to me? But the pattern seems to be very quickly like,
*  well, why can't an AI just do that? So I start to then think like, is there a version of this
*  that's like a plugin? Like you've created a spec and I'm trying to envision what is it like to use
*  a computer, you know, a year from now as kind of the tooling and the plumbing all matures.
*  One good candidate would seem to be like, it's a chat interface that you can like access the world
*  through and delegate stuff to little agents that go, you know, do stuff and report back. It sure
*  seems like a GPT-4 central process could like use the guardrail spec or something similar
*  to, you know, kind of insulate itself from problems as it like delegates things off to the side. So
*  do you, I mean, first of all, do you see that as realistic and do you have a point of view as to
*  kind of how the computing experience might evolve in light of that? That's a very, very good question.
*  I think I can go in like a bunch of directions like in my answer, but I think like my core belief
*  like for that in that whole space is I think like humans will be very essential in the loop.
*  And so it will be very hard to automate like all of this away, right? I think primarily because
*  even what correctness means like very different things to different people in different contexts,
*  right? And so one common thing as an example is like profanity filtering. Profanity filtering is
*  like one of the things that like most people can get consensus on is like they leave these,
*  if you're generating facts, like make sure it doesn't have profanity. But I also chatted with
*  people who are building, you know, like chatbots where authenticity, where the chatbots are,
*  you know, interacting with like certain audiences and like authenticity is essential, right?
*  And so if the chatbot is trying to imitate someone or like be in the likeness of someone
*  who does use profanity, then, you know, filtering out that profanity is actually detrimental to
*  the user experience that they're building. I think it is very hard to figure out like what
*  those constraints are on a global level. And so I think like having, you know, humans and domain
*  domain experts like be involved to developers to kind of figure out like, you know, like think
*  ground up from what they're building, what they're doing. For users to even think about,
*  you know, like what is their desired experience? I think like those inputs will like continue to
*  be very important. And like there would need to be like some way to configure, you know,
*  those inputs or those criteria or just that experience that like a user or developer wants.
*  So I do think that like, I guess like offloading this entirely to the model or to like a provider,
*  you know, is like going to be hard to be able to achieve like the cause of that just because of
*  that constraint. But in terms of like what the programming experience, what the developer
*  experience would look like, I think one way, and this is like purely hypothetical, I'm, you know,
*  not making bets on this at all. But like one way is to like really start thinking like almost
*  configuration first, right? Like there's like a configuration system that allows you to like,
*  you know, tune the outputs that you want to see from these LLMs. And even if the underlying
*  machine learning model stays the same, like how that model is like validated, corrected,
*  like how the outputs of that model are post-processed, like that is all what you
*  can configure. And so when people are working with large language models, you know, it's not
*  just text, it's also this configuration that they kind of pass it in every time. And this is like,
*  I'm an engineer and so, you know, all of my empathy goes to like engineers whenever I'm thinking of
*  like building systems, et cetera. So especially in engineering, like this is a pattern that I do
*  think will be like very important where, you know, the prompt isn't sufficient by itself, you know,
*  and just choosing the LLM and choosing, you know, temperature or something isn't sufficient by
*  itself. But it's, you know, this configuration framework of like, how do I want this output to
*  be like, and even like, how do I want my input to be, you know, like processed or formatted, et
*  cetera. So there is like one pattern that I can see emerge. Yeah. Yeah. Security also jumps out to
*  me as like a big driver here because as I was thinking about, you know, where would I use this
*  and all the things that I've done, I'm kind of like, increasingly I see like GPT-4 just running
*  pretty well and giving me like the format that I want. Certainly it has, you know, plenty of errors,
*  but it very rarely goes like, you know, totally off the rails, so to speak. There are a lot of
*  vectors that are as yet totally undeveloped that seem like they're going to come online and cause
*  a bunch of problems. So having this sort of SLA guarantee layer, validation layer, you know, seems
*  really smart in light of like prompt injection for one thing, like as users get more, you know,
*  generally sophisticated and kind of, you know, savvy in their adversarial, you know, attempts, like
*  you gain a lot by having something like this like implemented ahead of time. Similarly, you know,
*  we've seen some really interesting things even in Bing where a user will change or, you know,
*  not even a user, right? This is where it starts to get weird, like a site owner. We've just begun to
*  see like what the SEO people are going to do in the AI search era. So, I mean, the battle between
*  search and SEO, the arms race there, I think is going to be made to look pretty pale in comparison
*  compared to what is going to happen now that you can like try to trick the language model at
*  runtime with whatever kind of content. Then there's all these like, you've got model risk too
*  where you really probably do want to, as awesome as GPT-4 is, and my general strategy right now is
*  like use it for everything, you know, get the quality to an acceptable level and then think
*  about, you know, maybe taking out cost or taking out latency opportunistically or as necessary or
*  what have you. But that's going to come in due time too. And then people are going to be like,
*  well, you know, what about like, I heard like Alpaca, whatever was just as good and, you know,
*  we can just sort of drop that in there. But now you're just in a world where you have no idea
*  what's going on, right? I mean, your open AIs, your anthropics, like they have a certain SLA.
*  And I think one huge misconception that people have is like that that SLA sort of is an inherent
*  property of language models when in fact like it's not at all. And they've worked really hard to get
*  to the level that they have. And like, you know, you definitely cannot take for granted that your,
*  you know, bootlegged llama fine-tuned on whatever is going to be, you know, anywhere as safe or
*  friendly to users. I don't know, I'm going on and on, but that seems really important, but it's all
*  that stuff is just starting to kind of emerge from the mists. I guess how much did that motivate
*  you? Do you see other things like that? What do you make of all that kind of emergent security
*  stuff that you're kind of helping people get in front of? Yeah. Yeah. I think security is, you
*  know, a big, big operational risk of, you know, working with these models, especially like prompt
*  injection. I think we all kind of, you know, when Bing chat was released, I think Sydney and York
*  saw how easy it was to kind of manipulate these models in like specific ways. So yeah, I think
*  like my, like how I think about this is very okay. Like how do you decompose the problem? Right.
*  I truly think that this isn't a problem that will be solved by machine learning specifically. I think
*  like, you know, a lot of what opening has managed to achieve is, you know, built on like scaling
*  laws where, you know, like as you scale the data, et cetera, you just kind of start to see and scale
*  the models, you start to see, you know, emergent properties. But this is, you know, just from like
*  all of my experience working in machine learning, like there's, these are fundamentally stochastic
*  systems and it's very hard to like, there's a, there's a big long tail of, you know, like
*  what these stochastic systems like can't have guarantees for, right? Like you cannot have
*  guarantees or you cannot have data points for all of the different exciting and weird ways that
*  people are going to use these models. And so as a consequence, it's very hard to like add that
*  validation like from the model piece itself. And so security becomes, you know, an essential thing
*  because that isn't something that you can leave like up to the stochastic system, right? You
*  essentially need to have like more determinism like around it. And so my way of thinking about
*  is to kind of like break it down into like, okay, the model is stochastic. Like what can we do
*  around the model that then adds that, you know, those like, those like watertight guarantees.
*  So for prompt injection, for example, like the things that would be exciting to me are both like
*  on the input and output side, right? You sandwich the LLM API call with like, you know,
*  input validation, output validation to essentially ensure that you have like multiple layers of
*  security that, you know, make sure that your model isn't behaving in ways that you don't want it to.
*  So some of the ways I like, you know, familiar with like some of the more exciting, like
*  new developments in, you know, like protecting against prompt injection, but also, you know,
*  on the output side of things, like I think a lot of those corrections are like an input validation,
*  but like on the output side of things, if you know that there's behaviors that you don't want
*  this large language model to exhibit, it's possible to do that, you know, as like secondary checks on
*  in terms of output validation, right? If you want, for example, if you have like known patterns of,
*  you know, prompt injection that people tend to follow, you can do that on input validation to
*  essentially make sure that, you know, there's not your only, you're almost like gatekeeping,
*  like queries and interactions that users can have to the set of things that you can kind of support.
*  So I think like solving, it's back to this problem of like kind of what are the,
*  like decomposing this whole problem of security into, you know, specific domains, specific
*  applications, and then for those domains thinking about like, what is the, just like what is the end
*  goal that I want my users to have? And then, you know, like adding constraints to filter out like
*  everything that is outside of that goal, that is not kind of related to that goal. So like I would
*  be very surprised to see if we, for example, like chat with a bunch of teams who have been doing
*  this and like, I think that's a common design problem, right? Like where you can't simply rely
*  on the LLM, like there's a reason, for example, like we don't have like end-to-end machine learning
*  systems, right? Like you kind of have like some subcompetent machine learning and then some
*  checkpoint that has like either human or like a more deterministic, you know, component like
*  verifying or validating the output of the machine learning system and then like another downstream
*  thing that may be machine learning, but decomposing it and, you know, like adding
*  different layers of security on either end of like the ML system is like, yeah, the pattern that
*  most people when they try to like production systems, what kind of like see happen.
*  Security in depth, defense in depth is definitely, I think, going to become really important. Another
*  version of this too is models talking directly to other models in vector
*  form seems like it's going to become a huge trend. We had the authors of Blip 2 on the
*  show a while back and, you know, that I think of that as such an emblematic
*  foreshadowing of what's to come where they're able to take a frozen vision model and a frozen
*  language model and very quickly train a connector model that essentially converts the encoding
*  of the image to something in some unspeakable, literally unspeakable thing in the language
*  embedding space in a way that then allows you to have like dialogue with the language model about
*  the image. I actually love that. Yeah, sorry to interrupt, but I love that example because this
*  like literally is like research that I've done, you know, in my masters and that, you know,
*  it worked with some collaborators and I have a paper about this that does like these kind of
*  joint embeddings in language, in vision space for, I think we did this in the fashion domain where
*  you have some fashion embeddings and then some texts associated with it. How do you project it
*  into a single space or into a single like, you know, projection space so that you're able to like
*  figure out similarity between, you know, like essentially like using language, figure out
*  like what are some more images, et cetera. So it's a, yeah, it's a body of work that is like
*  pretty interesting and like opens up like so many cool capabilities. I mean, the fact that that's
*  going to work seemingly across, you know, I'm still educating myself on this, but I really
*  just see so many examples of like even just simple linear maps from one space to another
*  that people are kind of able to, you know, now bridge these different encoded or latent spaces,
*  whatever you want, you know, embedding spaces. I think that's going to be
*  a huge trend that will bring a lot better performance out of a lot of systems
*  because like, why would you go through this natural language bottleneck if you have the,
*  you know, a much richer representation of an image or for that matter, a medical scan or,
*  you know, a sound or whatever, like you have the sound of the bird in an audio file.
*  You're not going to project that down into language long-term, you know, and be like
*  a sound of birds is heard or whatever, and then feed that into the, you know, the language model.
*  You're going to figure out how to represent that in the language model space, but in like a way
*  that is truly unspeakable that I just see so much force going in that direction. But then the obvious
*  worry there is like, well, now you've opened yourself up to God knows what, you know, like
*  the space of possibility there is so vast, it's totally untestable. It's like incomprehensible on
*  the input side. So what can be done about it? I think, again, this is like a really good answer.
*  Start validating your outputs, people. This is really important. And it's only going to get more
*  important. Like you could, I think one thing people are probably really underestimating is
*  they can create a system today that behaves pretty predictably and the world underneath it is going
*  to change in such a way that it may start to expose their vulnerabilities over time. I mean,
*  in some sense, software kind of always works that way. You know, we've seen like windows patches way,
*  you know, way downstream after launch, but I don't know, this seems a little bit different.
*  Yeah, I think it's a very interesting point. I do think, I think it's like this fundamental idea of
*  like, you know, more sensory, like input from more sensors, if you're able to have that and code that,
*  I think that just leads to like better performance. And it's also like going back to this idea of
*  like grounding that I was talking about earlier, like you have like some amount of system that
*  like projects it in some space. How do you make sure that that projection is correct or not? And
*  if you have this idea of grounding where you have like, you know, this other sensory input that is
*  also supposed to be projected in something, you can use that as like a, as we like, you can use
*  that as like self correction or like self verification systems. Right. So we kind of like
*  saw this like while I was a, you know, driveway, I was just a software instructor that I worked at.
*  I think we had this where the performance with using just LiDAR versus using, you know, like if
*  you have cameras in the, as part of your inputs as well, in addition to LiDAR, you just kind of
*  like have better, a better understanding of the state that the car is in and you're able to,
*  you know, kind of like have better, just make better decisions overall. So I think it's a,
*  in my opinion, I think it's a net positive thing because it allows us to also like enforce these
*  car drives, you know, across like multiple dimensions, right? Because it allows us to
*  kind of figure it out, like where things might break down and then add like checks and systems
*  there in place. So yeah, I'm excited to see a world where we can have like all of these vectors
*  embedded in the same space. And there's a lot of like interoperability between them.
*  So essentially you're describing a validation step that is in coherence of
*  like semantic interpretation of different input signals. I'm trying to think of any example of
*  that that I've seen in the wild, like as you're pointing to one in the self-driving car area.
*  Maybe I want to just kind of throw a few other kind of safety control, etc. sort of paradigms
*  at you and just have you react to those not in a like better or worse sort of way. I mean, I think
*  obviously again, defense in depth, like there's a place for probably all of these. And
*  different things maybe in just kind of comparing and contrasting some of these other approaches to
*  what you're building. Again, it can help enlighten people as to how you're thinking about it and how
*  what kinds of use cases your project is best suited for. So I've got a handful. One is the
*  like most people listening to this would be most familiar with OpenAI, obviously. So
*  their moderation endpoint, which briefly you can like take an output bump it up against the
*  moderation endpoint. It gives you like a flag of, hey, you might have one of these like finite
*  number of problematic content types. And then I believe you can really do with that what you will
*  still. I don't know that they even enforce any particular action downstream of the moderation
*  endpoint. But essentially you're classifying stuff into one of these categories. That's
*  obviously pretty simple. So where do you think that kind of falls short?
*  I think it's great. I think it's very finite in scope. So if you were to take something like that
*  and then expand that out into any use case that you want to verify or validate, but that is like
*  at least programmatically verifiable or verifiable with the machine learning model,
*  flag specific things within that output that may be problematic with that. And then also allow you
*  to configure how you want all of those invalid outputs to be dealt with. I think that is how I
*  think about CardRail. So moderation. So if you think about moderation, I mean, specifically like
*  profanity filtering, it's like one of the validators out of like a number of validators
*  within the library. So you take some LM output, you give it to that profanity filtering validator,
*  it'll tell you whether there's profanity or not in your LM output. And depending on how you
*  configure that validator, it will also like correct that for you. So for example, generate that text
*  without profanity or maybe just filter those sentences that have profanity in there. But you
*  can just take that pattern and apply it across a bunch of other use cases. So if there's code that
*  is generated that maybe is incorrect or is not executable, you can do the same thing for code.
*  If there's like summaries that are generated from some source text, but those summaries are
*  incorrect or invalid for some reason, you can do that. If there's structured data that you've
*  extracted, which is like specific parts of it are incorrect, you can basically apply that same
*  paradigm. So it's taking that moderation and fine, but you know, making it like a very general,
*  very sensible thing that you can use. In practice, what do you see people doing most to fix on fail?
*  Like you gave a number of different kind of choices there where one could be like, you know, pop an
*  outright error. The other could be like rerun the whole call and just like hope for better the
*  second time. But you're getting pretty granular in between as well with like maybe just fix a little
*  bit or like snip the profanity. How do you, how would you like advise people to think about
*  which option they should take in that moment of a problem? And what do you see people actually
*  like doing today in the community? I think that's a hard problem to answer because like,
*  I can't tell people what their, I guess what their pain tolerance is like for their applications,
*  right? Like I think fundamentally, you know, there's like some cases where you're like, oh yeah,
*  if this doesn't pass, like this LLM output is of no use to me, right? And so I wanted to either be
*  corrected or just like filter it out. I can't use it in this like in between state. And so re-asking
*  is like one of the things that was, that is pretty valuable. Like it allows you to, you know, kind of
*  just from the user perspective, it's like a single, like, I don't want to say one shot because
*  it there's like, it's an overloaded term because you know, ML one shot, et cetera. But like,
*  it's like from a user perspective, it's a single API call that, you know, like on the back end might
*  make, you know, like multiple API calls, et cetera, to the large language model, but like give you
*  like either a corrected output or it'll tell you like, hey, this is just like incorrect and
*  you can't handle it. So, so who are very important use cases or very high stakes use cases where if
*  a validation check fails, you can't use it. I think like re-asking is probably the most effective
*  thing that I see people use a bunch. I think like filtering is another one. So specifically for like
*  some variation or for profanity, et cetera, if, you know, there's like some sentences that don't,
*  you know, aren't information dense or that have profanity, you would be able to, you know,
*  have like that granular control of like filtering out those specific things.
*  And I think like another one, which is like the default setting if you're using guardrails is like
*  a no-op. So essentially you would still run all of the validations on an LLM output, but you would
*  only like, if validation fails, you wouldn't do anything. You would just like return the output
*  as is to the user. So same as if they were using an LLM without guardrails, but it would just like
*  log everything that went wrong. And, you know, you can access that log and like figure out,
*  you know, do I want to like, do I want to iterate on my model or my prompt or something,
*  you know, using that. So I think those are probably some of my favorite ones, but like there's also
*  like raise an exception or like deterministically fix it if it's possible to determine deterministically
*  effects. So yeah, there's a bunch of, there's a suite of options within the framework.
*  Open AIs, we'll go with Open AIs first. They also recently with GPT-4 launched this
*  eval's library. I'm sure you've studied that a little bit. I guess my surface understanding is
*  that's more of like a bent, architected as like a benchmarking suite versus like a runtime aid,
*  but maybe, you know, what, what have you learned or what, what did you think was smart in the
*  eval's implementation or approach to validating language model outputs?
*  Yeah, yeah. I think my, my, I like eval's, I think my interpretation is the same, which is that it's
*  like this offline, you know, benchmark that allows them to internally test out how well,
*  you know, their LMs are doing for tasks that people care about. And so I think like one of
*  my favorite things about it is just the, I guess this is maybe not technical, but maybe more from
*  like a product or go to market standpoint. I really like how they, it's almost like this rate
*  of crowdsource, like how people want to use their large language models, right? Like all of the ways
*  that people are using it and like all of the ways that it's going wrong, take that and almost make
*  it part of like a training data set or your evaluation framework so that the models themselves
*  are, you know, are trying to serve those use cases better. So I think that's probably my favorite
*  thing. I see like other folks use it to just like scour through it and maybe figure out, you know,
*  interesting prompts that they can borrow. So I've like seen some people do that,
*  which is pretty interesting, which I think is like a nice way to like mind that library. But yeah,
*  that's probably the, I see it as a totally different framework basically.
*  I thought it was a nice touch also that they tied or essentially created a separate lane for GPT4
*  API access for folks who contributed to the, to the eval library. How about like Anthropics
*  constitutional AI approach? Again, it seems like there's a certain, that's obviously a training
*  protocol as compared to a runtime validation, but do you see commonalities there or have you taken
*  inspiration from their approach? Yeah, the constitutional AI stuff is interesting, but
*  I think it's back to like some of the, some of the things I said earlier, which is that like
*  it is essential to have like deterministic checks, right? Deterministic post-hoc validation,
*  because like just by training itself, like the models are not super sufficient. So I think like,
*  yeah, I think like runtime verification, runtime validation is like the most exciting kind of
*  problem to me. So that's how I think about it, but it is pretty interesting. I think this other
*  aspect of it is just like configurability, you know, so also a similar theme that I touched on
*  earlier, but being able to configure, you know, like what, what correctness means to you and like
*  enforce that specifically rather than, you know, having it is globally understood and read the
*  bottom, like standard of correctness. So I really like that world where, you know, like developers
*  like have that agency to configure what that means to them. So I think that's also being to do that
*  in this post-hoc setting where you don't have to go and train a model every time your definition
*  of correctness changes or every time your use case changes, I think is like, you know, it like
*  opens up access to a much broader audience. Yeah. I feel like there's a, there's an opportunity though
*  to sort of bring the constitutional critique to runtime. I listened to the, the guy, his name is
*  escaping me right now, but one of the authors, one of the lead authors on the diplomacy paper,
*  the Cicero model that came out of Metta, he was describing a general strategy of like,
*  how can we bring more compute forward to runtime? Like the old systems of like, you know,
*  deep blue and chess was like super intensive, you know, compute at runtime to the point of being like
*  borderline, largely a tree search more so than an AI or as we think of it today anyway.
*  But like with our language models, you know, it's not been quite as obvious how to do that.
*  And it seems like, again, this sort of framework of rather than lean on all that
*  embodied compute and training, like bring some of it somehow more forward to runtime and,
*  you know, apply like all these checks that essentially like the more compute you can spend,
*  like the more likelihood you have of getting like really good output essentially is his mega,
*  you know, observation. You talk about like deterministic, but some of these things,
*  they're not, they're still not really deterministic, right? Like if I, the more I critique,
*  like I still have this kind of inherent, you know, it's layered non-determinism, right? More than,
*  which hopefully kind of limits my problems, but still there is some like, in most cases,
*  right? There's still some amount of stochastic stuff that is not like reduced.
*  I think that's a very good point. And I should clarify, you know, the, I should not qualify,
*  I should qualify what determinism means. So I think there's essentially different ways to like
*  evaluate or to validate outputs, right? And I think like, basically one of those ways is, you know,
*  like taking an LM output, creating a new prompt that, you know, asks GPD core again, like, okay,
*  is this output correct or not? Giving these criteria and maybe give me like a yes or no,
*  or like maybe some binary response that allows me to assess this, right? And that is like one
*  way of doing validation that is not deterministic at all, but it is, you know, like additional layer
*  of security. But I think like the, there's also like a bunch of other techniques and like,
*  yeah, other like validation rules that people can use. So some of them are more kind of like rule
*  based or heuristic based. Some other of them are like, you know, not using LLM APIs, but using,
*  you know, like maybe smaller, high precision models that are, you know, like trained on like
*  subsets of data. So even if they're not deterministic, they're like trained on your own data. And
*  because you have control over the model, you can, you know, maybe do things like set random seeds,
*  et cetera, so that you essentially get, even if it's an output that is, you know, like generated
*  by a machine learning model, it's an output that you have control over and you can control its
*  randomness on, right? Either in terms of like changing the seed or changing some of the parameters
*  or just like being able to like generally work from more training data added. So that, both of
*  those frameworks are, you know, like one is like purely deterministic and then one is also like
*  more, more deterministic in terms of, you know, being able to control randomness. So when I say
*  deterministic, I'm truly referring to, you know, like an ensemble of like all of these techniques.
*  And so some of them are, you know, basically all of the mapping in terms of like what their randomness
*  kind of looks like. But that was a good, that was a good like little cash. Yeah.
*  One obvious question from a developer standpoint is what overhead does this create? And,
*  you know, you could measure that in a number of ways, right? Like token overhead, which is
*  cost overhead, maybe like complexity, overhead, latency, you know, increase. And then maybe some
*  just tensions also in a product experience. Like I think about the Bing experience where
*  fascinating, honestly, that one of the biggest corporations in the world went with this as their
*  approach. They spit out the token, you know, in a streaming token by token way, and then retract it
*  from you if they determined that it went off the rails. So like, I mean, that is crazy to me that
*  Microsoft like launched with that paradigm. I do get why, of course, because like people don't
*  want to sit there and wait for the whole thing to be generated before they can start to see
*  what's happening. There's a really powerful draw to the streaming experience. So much so that,
*  you know, Microsoft did this, but like, it's crazy that, you know, these, the biggest corporation,
*  one of the biggest corporations in the world is willing to knowingly like set up a system where
*  they're going to sometimes emit some, you know, toxic content or whatever. And then, well, just
*  kind of swipe that from you. We're in a brave new world for sure. So yeah, I guess, you know,
*  all those dimensions, how do you think about kind of overhead and, you know, again, how would you
*  kind of guide developers toward minimizing that overhead? Are there things that could be done in
*  parallel? Or, you know, what's, what's kind of the smart version of this so that, you know,
*  because a lot of people are going to be like, okay, yeah, but the CEO says we can't wait for that.
*  Yeah, I think that's really, it's a really good question, honestly. Interestingly, before I,
*  before I start, you know, talking about how I think about overhead, you would be surprised by
*  how for specific applications, like if you're not in the chatbot world, like how comfortable people
*  are with latency, as long as, you know, if they're getting like high quality output at the end of it.
*  So I, when I was kind of initially building this, like latency was a concern and like some of the
*  design decisions that we need, you know, support that hypothesis, like re-asking, for example,
*  you know, there's not piecemeal re-asking, like aggregate stuff, and then we ask, so it's a one
*  shot kind of like request. But people are pretty okay waiting for, if they're in this world where
*  correctness matters to them, people are pretty okay, you know, like tacking on some additional
*  latency in order to have that correctness. But with that said, I think like overhead is a pretty
*  important question. I've actually found like token overhead is an interesting one because I found like
*  this interesting balance between, you know, like how efficiently can you like write a prompt if
*  you're using the structured prompting strategy that Godreel offers versus how efficient are
*  your prompts when, you know, everything is in words, right? And so like for some use cases,
*  interestingly, I have seen that like being able to structure your prompts, you know, even if you
*  would think that it's more tokens, it's actually more efficient because like all of that structure
*  and all of that, those constraints, you know, which are like now maybe in symbols or in some
*  domain specific language end up, you know, being represented in like words, which is way more,
*  you know, just way more expensive in some cases, right? And that's a similar, like I've seen that
*  with complexity as well, where if you're trying to get your LLM outputs to be like structured in
*  some way or to be, you know, to have some behavior, et cetera, right now, the only way to do it is,
*  you know, to like prompt it yourself and like do a bunch of prompts, et cetera. But Godreel's kind
*  of like abstracts some of that complexity and some of that, you know, some of that exploration that
*  you have to do away from you, right? Because here's this like, here's this DSL that like is tested
*  and like works across a bunch of these LLM providers. And you essentially as a developer,
*  you don't have to think about like, how do I write a prompt that will give me this output,
*  that structure this way? Like I just, you know, I just write it in this like known way. And that,
*  you know, is like almost easier in terms of development. Like I have tweeted this some time
*  ago and also talked for my Twitter, follow me at Shreya R if you don't already. And I basically
*  talk about Godreel's and NAI all the time there. But I tweeted this, which is that like, even if
*  you're in this setup where you don't care about validation, if you just care about like getting
*  structured outputs, like it's a pain to kind of like think about how to do that. Right. So just
*  use Godreel's for like getting those structured outputs across like elements. And like, it's just,
*  it's useful in and of itself, right? Because you don't have to like write prompts and like iterate
*  on prompts, et cetera. So- I hope people understand a little bit more like that complexity that you're
*  taking out and how you're doing it on the just first question of like, can I get the desired
*  format back? Yeah, good question. So I think how Godreel's kind of like the entry point for
*  developers is like creating this spec, which is, you know, a markup language where you're able to
*  specify here's my, here's like an output schema. Right. So if you, if you, if I want an output,
*  here's, you know, like all of the different components that I want in that output. If that's
*  a JSON that you're able to kind of configure that if it's, you know, just a string with like some
*  additional validation on top of it, like it's just an equal string that you're generating.
*  And you want some additional validation, you're able to kind of configure that. Right. But in this
*  case where, but that is like totally separate from your prompt. That is just you thinking about like,
*  what is the output that I want? And like, how do I write that output in like a schema definition
*  perspective in the real? So Godreel's basically has real specs, reliable AI markup language.
*  That's the specification framework. And so in a real spec, in addition to the output schema,
*  you can also have like a prompt separately. And then all you need to add on the prompt essentially
*  is like the high level task description, right? Because everything that describes like, make sure
*  my output is this way and make sure my output has these constraints and make sure my output is
*  formatted that way. All of that you do in a schema, which is like a specific, like it's a programming
*  language. Right. So you can think of it in terms of like, if you can write like XML or you can
*  write markup, you can write that and you don't have to convert that into English and then, you
*  know, do a bunch of experimentation to make sure that your LLM API will like understand what that
*  means. So like it allows people to like, basically, yeah, it allows people to only think about like,
*  the pain of prompt engineering essentially goes away a little bit and it allows you to think about
*  like interacting with these LLMs in a more programmatic fashion to some degree. So that's,
*  you know, that's the complexity that gets, that guardrails kind of takes on. So one of the
*  exciting things about that is that the contract between the user and guardrails is basically the
*  spec, right? And then it's guardrails' job to translate that spec into a prompt. So the user
*  gives, you know, like a high level prompt and everything, but, you know, the output schema
*  definition is translated into a prompt based on guardrails. So if you work with these LLMs,
*  you would know that, you know, they basically like change, the version internally gets updated,
*  like all the time. And as part of like the behavior of the large language model changes,
*  right? And I've experienced some of that as I've been building this library, but you would
*  essentially kind of find that like, even if the model version changes, as a developer, you have
*  the same real spec and then guardrails just like compiles that real spec into different prompts,
*  depending on what is most effective for a specific LLM. So I think that is also, you know,
*  like from a developer point of view, you don't have to wrangle like model version updates and
*  like model quality issues to some degree. That sounds really useful. I was just doing some
*  stuff yesterday where I'm doing some task automation and I used the format trick,
*  right? Everybody kind of who uses language models much comes across the format trick,
*  use this format in the response. As far as I know that came out of OpenAI,
*  far as I've been able to track that back through Riley Goodside, you know, who like very much
*  popularized it, he attributes it to Boris Power who's at OpenAI. Before that, I don't know,
*  maybe Boris just came up with it on his own. But I do run into this stuff where I'm like, well,
*  how intricate do I really want this format to be? A lot of times I'm just like use this format,
*  just like XML open tag, content, XML closed tag. That way I can at least kind of easily just use
*  a regular expression, just kind of parse out whatever's within those tags. And then if it
*  has a prefix or a suffix or, and I hope this was helpful to you, you know, whatever, I can like
*  get rid of that cruft and have what I want. But then I usually haven't gone that much farther
*  than that because I'm like, then I'm getting into like hand coding XML and like the playground or
*  whatever, and that's not great. So right off the bat, I think that is maybe something we
*  under emphasize at the beginning of the conversation is just like, there's just a
*  straight convenience factor associated with, at least from a developer standpoint, being able to
*  write something in a little bit higher level abstraction and have the thing kind of translate to
*  a more detailed prompt that will get you the parsable result that you want.
*  No, yeah, totally. I kind of found that as well. When I was doing a lot of my prototyping,
*  I prototyped it with GBD3. And then I had a similar experience with having anybody who's
*  worked with GBD3 and 3.5 knows that, you know, you have like, here's the upgrade we're looking for
*  and hope that was helpful, etc. All of these statements, right, which are like,
*  just give me the JSON, which is what I want. And then I think with guardrails, since release,
*  I've had a community contributor actually push this effort to add instruction tags and do a
*  bunch of experimentation to make sure what works well with GBD3.5. And so from a developer's
*  standpoint, you write like one spec and then depending on if it's GBD3 or 3.5, you know,
*  and basically like compiles a little bit separately so that, you know, it just works.
*  Like I think even with GBD3.5, I've had a bunch of people testing it out and they just get the
*  thing that they're looking for without a lot of that extra, you know, filler text that maybe that
*  makes it not work as well. Yeah, it's interesting that you are also then translating that to
*  other models, which the angle that I was going to mention a second ago was,
*  it seems like there's a dynamic here where, as people kind of try to think about like, where's
*  all this going? You know, how is the market going to shape up? Who's going to lead? Are we going to
*  have like one AI to rule them all? Or is it going to be, you know, many, you know, or so an
*  oligopoly of large language model providers? Oh my God. So where's this all going?
*  One force that I see kind of pulling everybody in line with OpenAI is just the fact that all of
*  these things are getting developed against OpenAI's state of the art behavior at the time,
*  almost like across the board. And so then if you're a different language model, large language
*  model provider, you know, if you're an anthropic or a cohere or a, you know, Google or a, you know,
*  alpha out of Europe or like whatever, then it seems like you have a really strong incentive
*  to basically try to be as much like OpenAI as possible when it comes to like supporting all
*  these things. But then that kind of just sounds like, well, then how are you going to compete on
*  that? Right? If you've got to expend all this energy to basically just make sure that like people
*  even can switch to you without things that they're kind of currently assuming will work, breaking,
*  you know, that's not a great position to be in, you know, to be spending all your time just like
*  trying to catch up in that way. But I don't know that there's any way around that for other
*  providers. Do you see that dynamic similarly? And does this experience like lead you to think that
*  we may see kind of concentration if not necessarily providers, at least in terms of like
*  how language models behave? Yeah, I think that's a really great question. I do think I'm pretty,
*  like I personally believe that there would be a big diversity in terms of model providers. I think
*  like we are in this almost, it's kind of insane to see just from like, I've worked in a mall my
*  whole life, but or my whole adult life, but it's kind of insane to see just the amount of like
*  activity and excitement around the space. Like there's, you know, people training and fine tuning
*  deep learning models that, you know, weren't even in the space like a few months ago. And that's
*  really awesome. And that just that amount of like demand like makes it so that there's, you know,
*  more need and more providers that will come up. I had like people who were like, oh, I really like
*  guardrails, I really like opening eyes, but it's just too expensive for what I'm trying to build.
*  And so I can you make this work with an open source model as an example. So I do think that
*  we're going to see a lot of that proliferation happening, you know, great performing models from
*  like different price points, different latencies, different providers, etc. So I'm pretty,
*  pretty excited about that world. I think the other interesting aspect of this is that like,
*  because a lot of this was unlocked by opening, I were in this space where people are, you know,
*  building these frameworks, etc. around what is the most performant provider, what is the most
*  performing model. And because like those frameworks are maybe like indexing too high,
*  highly on OpenAI, like there's, you know, this incentive for other model providers to, you know,
*  offer interoperability for those specific functionality. So I do think that like,
*  the standards are evolving at the same time as like the models are getting better. So there's
*  this like interesting kind of dynamic between them. So at least for the foreseeable future,
*  there's like this big incentive for other model providers to also, you know, provide similar
*  functionality or at least not have regressions, right? So that incentivizes people to, you know,
*  switch over to them for a variety of reasons. But I do think that like, just the pace of innovation
*  means that, you know, there will be some, just like a more level playing field at some point,
*  and then it'll be very interesting to see like, what are the specializations that different
*  different model providers offer, or even like the different open source models,
*  like what that specialization is. Okay, here's my three quick, you can answer this as quickly
*  or not at all, whatever it is you want. But I typically, if there's time, I usually ask these
*  three final questions. One is favorite AI apps, experiences, tools, whatever that you are loving
*  that you would recommend to others. I'm going to be very basic and say copilot. I think copilot
*  is awesome. I have, I use it extensively. And I recently like, had to set up my dev environment
*  from scratch and wasn't like, didn't have copilot. And I was like, what am I missing? What is,
*  why is my, why am I coding slower? So yeah, definitely copilot.
*  I can totally relate to that. When they went paid and it stopped working, I was like in a panic
*  until I realized that I could just pay for it and make it come back. But yeah, it was like,
*  I'm not going to be doing this without this now. That's like, not to be endured. Okay, second one,
*  hypothetical situation. Sometime in the future, a million people already have the Neuralink
*  implant. If you get one, then you can control your computer devices with your thoughts.
*  Would you be interested in getting a Neuralink implant at that point?
*  I would not. I can imagine that like, I don't know, as like a, as a weird like strawman,
*  what if I'm in like a presentation or something and I'm computer, you know, controlling my laptop
*  in my brain and I get distracted, right? Like, does that mean that my slide deck now is on like,
*  whatever I'm distracted by? Like, I think there's, you know, like there's, again, like having
*  guardrails and like having layers of security between, you know, thinking versus like something
*  being executed on a different system. I think it's important to kind of have like some, some
*  filtration mechanism there. So I would stay on it, but I would be very excited in that role. Like I
*  would, yeah, I would like, I would, I would like inhabiting that role, even if I'm not actively
*  participating in it. Great answer. I love it. Final one, just zooming out, you know, as wide
*  as you can, you know, and thinking as far in the future as you have any sense of what might happen.
*  What are your biggest hopes for and fears for society at large as this AI moment continues to
*  unfold? I think it's a great question. Let's see, I think my biggest concerns, once again,
*  I don't think I'm very, I have any special insight here, but I do think like job displacement is
*  something that I think about quite a bit. And thinking about, you know, like, what are the,
*  you know, just like, what are going to be the, what is the, what is the amount of work, you know,
*  that would still be valuable in this future where a lot of knowledge work can maybe be at least
*  assisted or like a lot of knowledge workers can be made like more efficient, right. And then,
*  then what they are like today. So what does that mean for the future of work? I think that is
*  something that I think about. And let's see, I think a hope is that I am able to live a life where
*  I just don't have to do any of these like mundane things that end up taking so much of, you know,
*  our parts of life. So in the future, like maybe I don't have to do my own taxes and we, you know,
*  I don't have to book my own flights. I can just say like, book this flight from me at this date
*  and just find me the best place, et cetera. So being able to, you know, like automate away a
*  lot of those parts and then just do like whatever fun parts of life are, I think that would be
*  something that I'm excited about and hopeful for. Yeah. Go check out the package. If you're building
*  with large-diamond models and if you're facing like any issues where you're like, I was just
*  working and it's not working anymore. How do I, how do we kind of fix that? Check out guardrails.
*  And yeah, follow me on Twitter. Yeah. It's a beautiful vision. We can all hope for it.
*  Shreya Rajpal, thank you very much for being part of the cognitive revolution.
*  Yeah, absolutely. Thank you again for inviting me. I really enjoyed spending my afternoon
*  chatting with you. Amnaki uses generative AI to enable you to launch hundreds of thousands of ad
*  iterations that actually work customized across all platforms with a click of a button. I believe
*  in Amnaki so much that I invested in it and I recommend you use it too. Use Cogrev to get a 10% discount.

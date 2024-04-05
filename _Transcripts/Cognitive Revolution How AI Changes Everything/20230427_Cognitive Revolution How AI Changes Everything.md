---
Date Generated: April 03, 2024
Transcription Model: whisper medium 20231117
Length: 4866s
Video Keywords: []
Video Views: 2118
Video Rating: None
---

# The Great AI Implementation with Raza Habib of Humanloop
**Cognitive Revolution "How AI Changes Everything":** [April 27, 2023](https://www.youtube.com/watch?v=EKKJrRWOU30)
*  RHF is like sex in high school, right?
*  Everyone's talking about it, but almost no one's actually doing it.
*  I'm not a connoisseur of too many things in life, but one that I might claim
*  connoisseurship of is AI analogies.
*  I'm very optimistic about the rate of progress.
*  So I kept making predictions.
*  I thought, oh, that will take this many years.
*  And again and again, I've kind of been beaten down to the point that I've kind
*  of learned that this progress seems to be happening a lot faster than most might expect.
*  I already have a prosthesis.
*  It's my phone and I'm glued to it all the time.
*  So it's only one step further.
*  But I'd want to be confident that I'm not, you know, opening up literally my brain to
*  some like advertiser model.
*  Spending time in an interactive environment, I think gives you a much better intuition
*  for the capabilities of the models than just looking at benchmarks or, you know,
*  numbers on test sets.
*  Obviously, those quantitative measures are valuable and important, but you gain
*  something qualitative and different through interactive, almost play with the
*  models that I think is hard to gain if you haven't just spent some time with them.
*  Yeah, preach.
*  Hello and welcome to the Cognitive Revolution, where we interview visionary
*  researchers, entrepreneurs and builders working on the frontier of artificial
*  intelligence. Each week, we'll explore their revolutionary ideas and together
*  we'll build a picture of how AI technology will transform work, life and
*  society in the coming years.
*  I'm Nathan LeBenz, joined by my co-host, Eric Thornburg.
*  Before we dive into the cognitive revolution, I want to tell you about my new
*  interview show Upstream.
*  Upstream is where I go deeper with some of the world's most interesting thinkers to
*  map the constellation of ideas that matter.
*  On the first season of Upstream, you'll hear from Mark Andreessen, David Sacks,
*  Balaji, Ezra Klein, Joe Lonsdale and more.
*  Make sure to subscribe and check out the first episode with A16Z's Mark Andreessen.
*  The link is in the description.
*  Hi friends.
*  Our guest today is Raza Habib.
*  Raza has a PhD in machine learning from University College London, during which
*  time he also worked at Google AI as a research intern, but at present he's on the
*  front lines of LLM implementation as the CEO of Human Loop, a Y Combinator backed
*  startup that helps companies of all kinds, small and large, across a wide range of
*  industries, bridge the gap from API access to successful LLM deployment.
*  Like many things, but even more so, LLMs are easy to learn, but hard to master.
*  It may take just a few minutes to get a starter prompt working reasonably well,
*  but for companies looking to build LLMs into their products or to use them to
*  automate internal process, most of the work remains in the form of capturing and
*  studying data, collecting user feedback to identify failure modes, monitoring
*  performance on an ongoing basis, and running experiments to quantify and
*  compare LLM performance.
*  In my experience, it's more extreme than 80-20, maybe more like 90-10 or even 95-5.
*  Human Loop exists to make this process easier.
*  Now, full disclosure, I am a Human Loop customer, but there was no sponsorship or
*  other consideration attached to this interview.
*  I simply wanted to hear what Raza has learned in the process of helping so many
*  different companies on their LLM implementation journeys.
*  And he did not disappoint.
*  As you'll hear, he shared a bunch of concrete examples of customer use cases,
*  practical challenges that people are facing, and the strategies that they're
*  using to overcome them.
*  If you're a regular listener to the show, first, thank you.
*  I continue to be amazed by all the great feedback we receive, and I'm always
*  honored when someone tells me that they heard about the show from a friend.
*  But second, over the last few shows with Riley Goodside, the world's first
*  staff prompt engineer, and also Alex Albert, the creator of jailbreakchat.com,
*  you've now got a pretty good overview of hands-on LLM use and of prompting in
*  particular.
*  So with that in mind, if you'd like to test your own prompting skill or nurture
*  your inner red teamer, you might be interested to participate in the upcoming
*  hack a prompt competition.
*  This is a beginner friendly competition that challenges users to trick the AI
*  into saying specific things.
*  I'm a big believer in the importance of such crowdsourced testing.
*  And for me, it's actually quite fun to mess around with AI models in this way.
*  So I encourage you to check it out either by searching hack a prompt 2023, or using
*  the link, which we'll have in the show notes.
*  This competition is sponsored by a who's who of AI companies, including human
*  loop, and there are some $40,000 worth of cash and AI credit prizes available.
*  The competition begins on May 5th and will run for three weeks.
*  After which we'll have the organizer, Sandra Schulhoff, who is also the
*  creator of learn prompting.org on the show as a guest to talk about the results.
*  Now, without further ado, I hope you enjoy this conversation with Raza Habib.
*  Raza Habib, welcome to the cognitive revolution.
*  It is a pleasure to be here.
*  Thank you, Nathan.
*  Super excited about this.
*  I think this is as we're just talking kind of a bridge from our prompting week to
*  our medical week coming up.
*  You are the founder and CEO of human loop, a Y Combinator company that is building
*  tools to help people maximize the value that they get from language models.
*  Just looking at your website, find the prompts users love and fine tune custom
*  models for higher performance at lower cost.
*  So I really am excited to just dive in with you and look at like, what are people
*  doing today?
*  How's it going?
*  What are the struggles?
*  What are the tools that you're using?
*  What are the struggles?
*  What are the tools that you're building to help them overcome those struggles?
*  And obviously we can get into where we're going in the near future as well.
*  But for starters, just tell us a little bit about like your customer base and your
*  business.
*  Yeah, absolutely.
*  So I think I think you're exactly right.
*  Human loops dare to try and help developers and founders build products with large
*  language models to bridge that gap between here's access to this really smart API to
*  a model and actually turning that into a useful, usable product.
*  And it turns out that there's many steps along that path.
*  It's not as straightforward as it might seem at first.
*  So our customer base tends to be developers, founders at sort of startups,
*  increasingly actually founders at larger startups.
*  We keep getting messages from the CTO of like reasonably large companies being like,
*  don't tell anyone.
*  But me and two others have been working on this side project for the last three
*  months. And we think it might change everything.
*  Can you help? But predominantly it's people who are technical, who are looking to take
*  the API and build a useful product with it.
*  That's our customer base.
*  And the use cases are really broad.
*  We've got people doing coding assistance and code generation.
*  We've got marketing copy generation.
*  We have slightly more rogue use cases like, you know, Disclaimer Nathan is one of our
*  customers and they use it as part of a workflow automation tool.
*  So there's a wide range of applications that we see, but a core thread of workflows
*  and problems that people face, which typically are at the early stage, a lot of
*  experimentation and prototyping.
*  Large language models are stochastic.
*  They require instructions.
*  So finding the right prompts, figuring out how do I mold my problem into a format the
*  models can understand.
*  Evaluation is another sort of big key problem area people have.
*  So the tasks that people are trying to do right now are much more subjective than you
*  might have done in the past.
*  And so trying to understand if I generate an email or if I'm doing marketing copy or
*  reading a job description, you know, what does good look like?
*  And understanding how to monitor that at scale is a challenge.
*  And then customization and improvement.
*  The models make things up.
*  They don't know about company private data.
*  So how do I get the model to understand my context, my company, be customized to my
*  users?
*  And those are kind of the three big problem areas that we see people having and that we
*  help them solve.
*  Molding the problem to a format that the AI can solve.
*  I think that's such a huge concept that people who have kind of tried chat GPT are not
*  quite reckoning with yet in terms of the depth and really the degree to which problems can
*  be fit to, you know, a format that AIs can solve them.
*  Definitely kind of to me there, it sounds like a lot of your customers are building for
*  themselves. Like, how would you break it down right now between customers of yours that
*  are building applications that they're offering commercially to, like, you know, third
*  party users versus folks, you know, you can kind of mention the like CTO.
*  And it is fascinating that, like, at the executive level, these tools are so accessible that,
*  like, where, you know, a lot of these leaders probably haven't coded all that much for a
*  while. They can still dive in.
*  Yeah, it's interesting. I don't want to know names, but it's, you know, it's companies you
*  would have heard of. And it's the CTO plus like two or three really strong engineers.
*  And they're trying to figure out what the limits are.
*  I mean, we know some examples, right?
*  So like HubSpot, Darmesh was like actually, you know, in the room with his engineers trying
*  to figure out how to make this stuff work.
*  And there's many examples like that.
*  I guess it's a spectrum.
*  So the larger the company, the more likely it is they're building for themselves.
*  Right. And so big companies come to us and they want to do two things.
*  They want to build applications or they want to add LLM or AI features to their products.
*  And they also want to automate internal processes.
*  Right. Those are the two areas.
*  And then smaller companies tend to be building products with third parties.
*  So if it's a startup, it's almost certainly using the LLMs as part of their product.
*  If it's a large enterprise, you see a bit of both.
*  Yeah, interesting. Those two modes.
*  Thinking a lot about just kind of the the mode of human AI interaction or the various
*  modes. And I'm kind of working this framework, which I keep adding dimensions to.
*  But the I think the first dimension that I think the most about is like real time
*  co-pilot style chat GPT style interaction where you are kind of doing your thing
*  and the AI is helping you.
*  And then on the other extreme of that access, you have kind of highly structured
*  workflows that have kind of designed architecture of routing information in such a way
*  that you can take advantage of AI capabilities as like one step or one of your multiple
*  steps within automated workflows.
*  And maybe it's worth giving a concrete example of each of those just to help people hang
*  their hats on. So on the one end, you might have something like GitHub co-pilot that's
*  sitting over your shoulder. It's watching the code as you write and it's generating
*  suggestions for what you might have.
*  It's quite open ended. On the other end, you have something like copy AI where you put
*  in a set of bullet points and you hit a button and it generates you marketing copy and you
*  have very little parameters for control as the end user or chat GPT maybe lives on the
*  end closer to co-pilot as well or something very open ended that you can interact with
*  and get very different outcomes.
*  So it's interesting that you have both.
*  If I understood correctly, it's kind of the startups tend to be building this some sort
*  of more opinionated view on essentially a language model service.
*  And they're using your tools to try to figure out how to make that perform well for kind
*  of the uninitiated, right, the person that's not super AI savvy.
*  And then is it a spectrum or do you see it as more of a binary where the other side is
*  like, OK, I want to potentially automate first line responses to email tickets in my
*  CS system.
*  So it's a good question. I think it's all about the user experience.
*  And I think it's about thinking about different types of UX that work for AI or that work
*  for elements. I think that if you look at the breakout successes and I get a co-pilot
*  chat GPT being by far and away the biggest.
*  But there are others right.
*  There's copy. I there's writer.
*  There's there's a whole bunch of other things.
*  But if you look at those two co-pilot and chat, you'll be very different novel you access.
*  But I think they're successful because they've cracked some kind of UX insight as well as a
*  modeling insight. So in the case of chat GPT, I think the reason it's so much more
*  accessible and so much more appealing to people than the original opening models that were
*  accessible through the playground is that the interface is fault tolerant by design.
*  If you go to interact with something in chat and it doesn't get it exactly right the first
*  time, you don't immediately give up.
*  Right. You're in a conversation with someone you don't expect.
*  Your expectation is not for it to be perfect first time.
*  Whereas the original UI that I think OpenAI exposed in the playground, which was this text
*  box that you go and you put text and you hit enter.
*  I think a lot of people bounced off that without giving it the time to discover its
*  boundaries. And so they would come and they would like put something in and it didn't work
*  first time and they go, oh, this is crap.
*  It doesn't work.
*  And so I think like the model was a lot better.
*  Right. Like, let's not pretend that GPT 3.5 or 4 wasn't significantly better.
*  But I do think that part of what makes those chat experiences work so well and be so
*  popular for people is they're very fault tolerant and they give you a chance to correct
*  the model and have a few tries to get what you want.
*  There's just a spectrum of different UX experimentation going on right now.
*  So in some cases, you know, you don't want someone to have to think about the fact that
*  they're interacting with an AI model.
*  They have a job to be done and you want to give them the shortest path to achieving that job
*  to be done. So it makes sense to put a lot of rails on it.
*  In other cases, you need more complexity, more generality.
*  You're trying to answer a complicated question or solve a research problem or whatever it
*  might be. Chat makes a lot more sense in the GitHub copilot case.
*  Like latency was super important.
*  And so having a chat type interface is it requires context switching.
*  It requires some way of knowing the code you're looking at.
*  And it takes a long time to get a response from these larger models.
*  Whereas having a model that sits over your shoulder, can see your code, knows your context
*  and just occasionally makes a suggestion turns out to be really useful.
*  And so I guess I wouldn't like my mental model isn't like a binary spectrum from like
*  everything's on rails to everything's free.
*  It's more we're exploring this space of quite novel user experiences where at the very
*  early stages of doing this for AI models and we're starting to discover some of the things
*  that work and don't work.
*  Do you see the human loop tool set as inherently.
*  More geared toward the narrow.
*  You know, kind of guided use cases, it seems to me like that's probably what more of
*  your customers are focused on as opposed to the much more kind of open ended, you know,
*  free form experience.
*  I think this I think there's some there's some truth to that, for sure.
*  It's people who are trying to figure out how do I build a particular feature or product
*  and do that in a way that's robust and kind of has reliable results.
*  I guess there's like two parts to it, right?
*  There's the like prototyping playground type environment that I think lends itself a lot
*  to customization.
*  But there's also these tools around understanding like how well is my model working?
*  What is it actually doing?
*  Is it performing well?
*  Understanding the inputs and outputs and the data that flows through, which is, I think,
*  like infrastructure that you're going to need, irrespective of the generality of the
*  problem. And in some cases, the more complex or more kind of free rein you give the
*  model, the more important is to understand how well it's working and where it's breaking
*  and where it isn't.
*  Let's maybe take a minute and just kind of run down the product and what it is, because
*  I think that's also a great way to think about all the challenges that people are
*  encountering. So I, as you mentioned, I'm a customer of Human Loop in my capacity as
*  an advisor at Athena, which is in the executive assistant services space.
*  And we're trying to figure out, you know, and it's a target rich environment.
*  Like, what are all the things we can use?
*  You know, especially now at GPT-4 quality, there are so many applications.
*  And interestingly, one of the things we're kind of noticing is like a lot of them don't
*  even take that much prompt engineering to work, especially if we have a literal human
*  in the loop, which for now, you know, we always do.
*  When I was like, OK, I need something like Human Loop.
*  I went out shopping and I was like, OK, I want a neutral playground because I, you
*  know, as much as I do think OpenAI is awesome, I don't want to be entirely locked into
*  them. I definitely want to be able to flip over and try Claude and stuff.
*  I also really want to keep the history of my usage, which was something that OpenAI
*  is really moving away from with their like, you know, we don't keep any of your history.
*  It's a 30 day and delete, you know, kind of policy.
*  It's kind of the opposite of what I was looking for, because we have a thousand executive
*  assistants working in all these different contexts.
*  We want to be able to see and know, you know, what are they doing and how is it working
*  and can we coach them? Can we detect patterns?
*  You know, whatever. There's so much for us to learn about just our own operations there.
*  So I was really looking for history, you know, looking for a way to kind of graduate from
*  a playground, like interactive exploration type experience to something that I could
*  then build into workflow. So I wanted like the flip from the playground to the API mode,
*  which you guys offer. And then I've even gotten into, you know, all the advanced features
*  yet in terms of like running experiments and collecting feedback.
*  So, you know, it was those kind of first anchor things that led me to you.
*  Comment on those kind of stuff, on those kind of features as much as you'd like.
*  And then I really want to get into, you know, kind of what is the frontier for me, which is
*  like this feedback, experiments and tools as well, which you have available to.
*  Omniki uses generative AI to enable you to launch hundreds of thousands of ad iterations
*  that actually work customized across all platforms with a click of a button.
*  I believe in Omniki so much that I invested in it and I recommend you use it to use Cogrev
*  to get a 10% discount.
*  We saw this like repeated pattern of basically people struggling with the complexity of
*  managing a lot of different versions of prompts and trying things out and it being highly
*  experimental and there being also like knowledge being built up through that experimentation.
*  Right. When people do prompt engineering and they interact with the models, they start to
*  implicitly build up intuitions about what does and doesn't work.
*  And then that knowledge was being split between the open AI playground and Excel spreadsheets and
*  GitHub code. And there wasn't like an easy way to manage the prompt experimentation and that
*  experience. And so that's part of, I think, what you've been using very heavily, which is we have
*  something that looks a little bit like the open AI playground.
*  There's a chat version and a completion version, but it's multi provider and it also has a few
*  other kind of key differences, which is it allows you to map the same model across multiple
*  inputs simultaneously.
*  And this is like a key thing when you're trying to develop something that's going to work, not just
*  for the one instance you're looking at right now, but you're trying to see, OK, is this going to
*  work in general and robustly?
*  OK, maybe you don't look at a huge test set all at once, but at least having 10 or 20 use cases
*  that you can say, OK, I'm going to prototype a sales generating email or I'm going to prototype
*  something and I'm going to test it out at all these different inputs and make sure it least works
*  for those. And so we see this sort of interactive environment where people will be product prompt,
*  like creating a prompt template and then trying it out on a lot of different things at the same
*  time and seeing how well does that work.
*  And they typically then graduate from there, as you said, to deploying that as an API endpoint and
*  using it in production or as part of a product.
*  And at that point, I think the core challenges are how do I go from quite good performance to
*  robust and good enough that I trust this in production and even upstream of that, how do I even
*  know if it's working?
*  Because these things are so subjective, it's really difficult to to understand those bits.
*  And so those are I think that's when human really comes into its own.
*  I think that the early prototyping parts are best in class and people use them, use them.
*  I think they add a ton of value.
*  But in the journey of going from idea to robust deployed application, being able to understand how well things are working and to take actions to improve them.
*  That's the that's the really critical component.
*  Could you run down a handful of actual tasks like, you know, I'd love to just hear a parade of kind of across different types of businesses, different sectors.
*  What are the sort of object level?
*  So early on, the majority of people, I think when GP3 came out, we're doing writing assistance of some form, right?
*  This was the first, you know, obviously, this is the first thing people think of.
*  So you have like marketing writing assistance, sales writing assistance, fiction, et cetera.
*  Right. So companies like Sudo Write, Copy AI, Jasper, et cetera, different varieties of I want to overcome this blank page problem and I want to write more quickly and better.
*  And there's a whole range of use cases there.
*  Then you have people kind of doing various forms of like knowledge work automation.
*  So you have a lot of different legal use cases, people doing contract review, summarization, question answering, extracting things from documents.
*  That's like another very large bucket that we see a lot of usage in.
*  Then various forms of like process automation.
*  So we mentioned like sales email writing.
*  Right. But within sales, it's just a lot of mundane tasks that people do.
*  I have a meeting, I have the transcript, I need a summary, I need to populate this in my CRM, et cetera.
*  So there's like a lot of people, I think, building in that space.
*  We see a lot of use cases for in the medical domain, typically around just removing some of the grunt work.
*  So doctors have to do like a significant amount of paperwork around insurance claims and filling out forms in the right way and summaries and things like that.
*  So we've seen quite a few companies building in that space.
*  Code writing is another one.
*  Right. So GitHub Copilot is just one of many different ways you might try and build code assistance.
*  And so we've seen a few varieties of those, whether that's people doing natural language to SQL so that business analysts can query their own databases or it might be people building an entirely new IDE from the ground up.
*  One of our companies is a company called Cursor.
*  And they're trying to reimagine like what would an IDE look like if I started with an LLM on day one?
*  And that's another use case.
*  And I could go on. There are so many applications being built now.
*  There's a real Cambrian explosion.
*  Yeah, that's amazing. How do you even think about kind of characterizing?
*  All of those tasks in terms of like.
*  The impact that they make on people.
*  Do you think of them in terms of like minutes saved, you know, doing doing it manually or, you know, as a human versus kind of the LLM obviously takes whatever its latency is.
*  And then you have some, you know, review overhead.
*  What's your framework for that?
*  That's a great question.
*  I don't know if I have a framework, but I can tell you kind of just off the cuff what comes to mind, which is it feels to me that there's sort of like the V not version of using AI or LLM, which is like I'm going to use this to do an existing task a little bit faster or to automate something that someone was already doing.
*  This is the version that I think teachers worry about.
*  This is the sort of cheats on exam version, right?
*  Like lets me do what I was doing before, but a bit better or a bit faster.
*  And I think there's the interesting version, which is like I now have an assistant that lets me do things I couldn't do before or to push what I was able to do a little bit further.
*  And here I think of like some of the more advanced coding tools as being really interesting.
*  So I've seen quite a few examples now of people using languages they're not familiar with because the coding assistant is good enough that they can move across code base.
*  So I've seen I've been speaking to friends who maybe would be back end engineers, but have found themselves able to contribute a bit more elsewhere.
*  Or, you know, I've got a tool myself that I kind of built for personal use where when I'm taking notes, it tries to critique and extend what I'm writing.
*  So it's not like actually taking a set of bullet points and filling it out, but it's doing something more like what a colleague or friend might do, being like, have you thought about this?
*  And I feel like that actually allows me to do things I wouldn't have been able to do on my own.
*  So there's a bit of a spectrum. I'm personally more excited about the tools that give people more capabilities than they would have had previously.
*  But I think there's a lot of value in both.
*  But there are large cost centers.
*  One of our customers is doing a huge amount of customer service automation.
*  They've got several hundred thousand customers.
*  And so customer success is a big cost for them.
*  Being able to accelerate those people and reduce headcount there is is obviously valuable.
*  On the other hand, you have customers who are augmenting lawyers where it's less about reducing headcount and more about letting the same person do the work better and leverage the tools in that way.
*  Is it a particular tool that you use for the critique of writing?
*  I built my own.
*  If it's something I could try, I'd be interested in trying it.
*  If it's too bespoke, then maybe it's hard to share.
*  But that sounds really I have not had a lot of success with the writing tools on the market today.
*  But I mostly just, you know, if anything, I'll ask for a little bit of kind of help clarifying, simplifying from GPT-4 directly.
*  But that does sound like an interesting UI or UX maybe is a better level of which to think about that.
*  Yeah, it's interesting.
*  I think it depends what you're looking for.
*  And I think a lot of the early success of certainly writing assistants and kind of the marketing space are around getting to either around brainstorming, come up with more ideas or they're about volume of kind of not necessarily like super high quality content.
*  Right. You're not trying to write something.
*  Yeah, you're throwing it all into an optimizer anyway.
*  So yeah, you're not trying to win a Pulitzer Prize.
*  You're trying to produce like a large volume of like medium quality content.
*  Whereas when I'm writing notes for myself, I'm trying to produce a small amount of stuff that I'm going to find useful.
*  So I guess the use case is probably slightly different.
*  Yeah. OK, that's really interesting.
*  And then what you didn't kind of speak to as much there, which I imagine must be a significant part of the business, is this kind of scaling things that were previously unscalable.
*  So this is as we're looking through, again, like the Athena client base and looking for examples of people that have done great things with AI tools already.
*  One that we see is like the ability, you know, almost all of our clients are like recruiting in some way, shape or form.
*  So what we've seen there is like the ability to scale recruiting workflows that you would previously delegate to a person.
*  But now you can kind of systematize, probably honestly do better like profile evaluations even then, you know, the human was able to deliver in many cases, but certainly at way more scale,
*  like the ability to kind of bring some of these functions where people maybe used to use a firm or whatever in-house and do it for like a one, two percent of the cost is kind of insane.
*  So I guess the question there is like, do you see a lot of that kind of activity?
*  And then also really interested in like, how do people wire that up?
*  Like, are people using Zapier in your experience?
*  Or are they like, you know, stitching stuff together themselves out of Google Sheets?
*  Like, where are the actual API calls coming from?
*  So the majority of our customers are integrating the APIs into some form of front end product.
*  So they have some UI that they're building where they're going to be making a call to HumanLoop to call the model.
*  And as part of that, we're going to log the data that flows through as well so that they understand how well things are working.
*  We do have some people who are doing more low code, no code automation.
*  Typically, we've seen people use bubble quite a lot for this, actually.
*  And then some use of Zapier as well.
*  But the majority of our customers are not on that kind of no code, low code end of the spectrum.
*  They're closer to I'm integrating this into a product and I'm going to be using HumanLoop as the backend, the way to understand how well things are working.
*  The way to build my data sets to fine tune and improve stuff.
*  But the user experience and the product is being built by them.
*  Do you think that's a reflection of like the general market of, you know, LLM usage?
*  Or is that just, you know, maybe more of a reflection of like you're in the YC network and so you're sort of wired into product building companies?
*  And so, you know, in some sense, it's impossible for me to know, right?
*  Because I've only seen the sample of the market that I've seen.
*  Well, actually, maybe that's not true, because we do get like we get a huge amount of inbound, right?
*  And we don't, you know, we narrowly focus on builders and founders and engineers.
*  We don't build for everyone.
*  There definitely is a large volume of people looking to do no code, low code automation.
*  And, you know, I think that HumanLoop is probably not like being built for them.
*  So some of them end up using it anyway, because they love how they love the playground and they love that kind of experience.
*  But we see less of that because it's not what we've optimized for.
*  Let's start with maybe evaluation.
*  You've gone through this process of kind of experimenting.
*  You're in the playground.
*  OK, you got something that's like worked for your however many different examples you could kind of think up on the spot.
*  By the way, I find that also pretty effective as like a teaching paradigm for like intro, you know, to what the hell's going on here in the first place.
*  You know, let me run this.
*  And I've done things like I'm going to put Kobe Bryant, Santa Claus and, you know, Joe Biden in like the three.
*  And then we'll see how, you know, just a simple prompt like varies with those variables.
*  And that definitely like helps people grok, you know, what a language model is.
*  I think for companies adopting LMS for the first time, or even academics coming to this from other parts of machine learning,
*  spending time in an interactive environment, I think gives you a much better intuition for the capabilities of the models than just looking at benchmarks or, you know, numbers on test sets.
*  Obviously, those quantitative measures are valuable and important, but you gain something qualitative and different through interactive, almost play with the models that I think is hard to gain if you haven't just spent some time with them.
*  And that's partly why I think these playground environments, these REPL style environments are very important.
*  Yeah, preach on that point.
*  I think that is so, so important.
*  I mean, good God, I see so much misunderstanding that could be remedied with just a little play.
*  Yeah, I mean, like you see, you know, a silly example of this is Noam Chomsky wrote an op-ed in the New York Times, basically like outlining all the reasons why LMS would fail and giving a bunch of things that he thought LMS would never be able to do, which they can already do.
*  All of the examples he gave, you can just shove into the playground and run it and it works.
*  Like literally the concrete examples, not even versions of them, but specifically the ones he gave.
*  And you just think like, how hard would it have been to just try?
*  Yeah, I know it's baffling.
*  I find that so true.
*  Okay, well, maybe leave that aside.
*  So we're using HumanLoop, we're doing the playground, we're actually, you know, making progress, getting somewhere.
*  And now you've got this challenge in implementation of evaluation, which is connected to feedback.
*  So how do you think about that?
*  When for context for users, I find this particular stat kind of insane.
*  In the GPT-4 technical report, they report a 70-30 preference ratio for GPT-4 over 3.5, which to me, given the qualitative difference in capability and
*  the 10th to the 90th percentile on the bar exam and all that, you know, stuff, that seems like a pretty low ratio.
*  So that suggests to me that like evaluation is hard.
*  And it's probably something that a lot of people are kind of diluting themselves and, you know, seeing patterns that aren't there.
*  I mean, this sounds just like a total mess right now.
*  Yeah, it's certainly tricky.
*  It's especially tricky for the tasks that are more subjective in nature, where actually, okay, maybe you can you can sort of assess the quality, but in
*  some sense, the correct answer is what your user says the correct answer is.
*  If you are a writing assistant or something like that, then that's much more subjective.
*  There are more concrete examples.
*  If you're writing code, then obviously it needs to run.
*  And you're generating an SQL query.
*  Maybe it's easier to have an objective metric of success.
*  But even for question answering or summarization, like a lot of the tasks that people are doing, pure objective evaluation is quite hard.
*  And so within HumanLoop, there's the option both for quantitative evaluations, you can define metrics, etc.
*  But we also give you the tools needed to capture human feedback, both internally, but most importantly, from your end users.
*  And so the way that works is we have a feedback API.
*  And so every time you sort of log to HumanLoop or you use our generate call, we return you a unique ID for that session.
*  And then you can capture different types of user feedback from people interacting with your application to get a sense of how well things are working.
*  And typically, we see people get success with three types of feedback, sort of explicit votes.
*  So things like you might see in chat, GPT, thumbs up, thumbs down.
*  Those are useful, but you get a small proportion.
*  The vast majority of people don't touch those buttons and you're getting a kind of more extreme skew.
*  Implicit signals of feedback.
*  So people look at the actions people take within their applications.
*  If I generated a sales email, did they send it?
*  Did they copy the marketing copy and use it somewhere else?
*  Did they hit the regenerate button?
*  Right. If the person sitting there generating again and again, it's probably a sign that things didn't work the first time.
*  So those signals get logged as well as like senses of how well things are working.
*  And the final one is sort of textual corrections.
*  So if you're generating text that the person can edit and they edit it before using it,
*  then capturing that can be a really useful signal for figuring out what went wrong or how you can improve it later.
*  Whether that's inspecting manually or just fine tuning a model on corrected results.
*  People can define their own feedback types, but those three categories of kind of explicit actions and
*  corrections, kind of votes, actions, corrections are the ones we see people getting the most success with sort of in practice.
*  And then we give you an aggregated view of like, how is that varying over time?
*  And that allows you to kind of get a sense when you make changes.
*  You know, we saw this for a lot of our customers when they made the switch from GPT-3, TextAVinci 2 to 4 or 3.5 when it first came out.
*  They could just see their user satisfaction charts just jump up almost overnight.
*  And I think the vast majority of people who didn't have tooling like this didn't really know.
*  Like we changed the model. Did it get better? Did it get worse? Seems better.
*  But like, how do you know if it's actually working better for your customers?
*  And having that feedback both gives you this like high level view of how well things are working, but then allows people to take more granular interventions.
*  So something else that we see people doing is they will filter for the failure cases and then manually inspect some handful of those to understand, OK, what went wrong?
*  Was it the data lookup that I did? I grabbed the wrong context information.
*  Is the prompt sort of wrong in some way? Can I tweak that?
*  Is the model just like not capable at this task?
*  And they will do this loop where they'll kind of filter for examples that didn't work that well, reopen them in an interactive environment like the playground, form some hypothesis for what went wrong, take an intervention and redeploy.
*  And because they have all the monitoring and the metrics in place, they're able to see what the impact of that was.
*  Or HumanLoop also allows you to run a direct comparison experiment.
*  So for some subset of users, you know, be running an A-B test or multivariate test, we are seeing, OK, did this change result in an increased performance or not?
*  And so we see people run that loop quite often, even before their fine tuning models.
*  Like they do it when they fine tune as well, and we can maybe chat about that.
*  But this process of like understand how well things are working, find some of the edge cases, find the things that are going wrong, fix them, repeat is a very common workflow we see.
*  Yeah, and the iteration time on that can be, you know, down to minutes in theory, right?
*  In some cases, because you're literally just giving a slightly incremental instruction or whatever.
*  I have a ton of different follow up questions that are coming to mind that I want to ask.
*  On the nature of feedback, would you include something like generating multiple outputs and then kind of asking the user which they prefer as like an implicit?
*  Or is that just something that you don't see that much?
*  Because I know Anthropic does that in their loop, and it seems easy to be like, I like this one more than that one.
*  So we see that when people are doing internal evaluation, that's very common.
*  In fact, I don't think so. Anthropic does this like binary selection.
*  OpenAI does ranking of the generated outputs.
*  We have other customers who are building custom models and they'll they'll do preference as well.
*  But that's kind of a sucky user experience, right?
*  And so when people are collecting in production data, they tend not to want to generate multiple options and get the user to pick one.
*  Some companies have done this or experimented with it.
*  I know that like AI Dungeon was doing this for a little while, where when you generate it, they would generate a few options and ask you to pick.
*  Choose your own adventure. It's the purest form.
*  But in a choose your own adventure context, I think it's okay.
*  But for most applications, it's not really what the user wants.
*  And so people are more reticent to do that kind of sort of preference gathering in production.
*  But for internal evaluations, we see it a lot.
*  That's fascinating. I kind of don't.
*  I don't know. To me, it seems like an OK experience.
*  This is something that we're considering at Weymark, where we're making video content for users.
*  And it's a cool experience that we have right now, where you basically find your business online, give like a very sort of Dolly like
*  short prompt on what you want to see a video about.
*  And then we return a fully formed composition for you.
*  But I've been kind of thinking like, well, what's better than one fully formed composition?
*  You know, maybe two or even potentially more than that.
*  You know, if you watch Mad Men, right, they like have multiple pitches come through.
*  So if there's some way in which it can kind of echo what it feels like to be a big company.
*  What do you think is what do you think is bad about that?
*  I think it's very context dependent, right.
*  So I think in that case, it's maybe not so bad.
*  And I think it'll be fine.
*  So two things come to mind. One is context dependent.
*  If you're doing something like code generation or text completion or in GitHub copilot, like I don't necessarily want to choose between a bunch of different pieces of code.
*  Like I want a completion that's kind of good.
*  Maybe I can tap between a few.
*  But generally speaking, I want it to work first time.
*  But the other thing is just like the goal that the developer has in mind.
*  So I think that like with the preference data, they're planning to fine tune the models with RLHF on this preference data.
*  And so like, then I think it makes sense to have it in that format.
*  Whereas where a lot of what a lot of our customers are doing is like they're trying to do monitoring or evaluation.
*  They want to know, like, for the parameters that I have at the moment and the setup I have, like, is this working well?
*  Is it causing problems?
*  Are my customers, you know, getting success when it's going wrong?
*  Like, why? And there, I think like a single evaluation is fine because you're evaluating the system.
*  It's not the same model.
*  So it's a little bit of what you're trying to do in a little bit of the context.
*  I think in some UXs, it'll be fine and some it won't.
*  Yeah, I also had a similar kind of thought on like, I wonder, maybe just have a take on this.
*  Why do you think people don't make a more explicit trade between like feedback and access?
*  It seems like that that is almost like the AI successor to like the ad driven model, right?
*  The free at least for a while, like the free version is based on you have to like help improve the product.
*  But I don't see much of that.
*  Do you have a sense for why that wouldn't work or why people don't don't make that trade with the public more often?
*  The honest answer is no, I don't have I haven't thought about it that much.
*  I don't have a strong view there.
*  My suspicion is that people are quite happy to give this feedback anyway.
*  And a lot of it is implicit.
*  And so maybe maybe you don't need to make the trade because you're getting a lot of that anyway.
*  From what I've heard, it seems like the rates are usually fairly low.
*  Like you had said, you know, the kind of thumbs up, thumbs down, people don't hit too much.
*  The rates for explicit sources of feedback are definitely quite low.
*  So if you're if you're clever enough to structure it in in a smart way, then you can kind of work around this problem, certainly.
*  But yeah, I don't know.
*  There seems to I feel like there's some sort of inconsistency here where like the received wisdom, which seems
*  to check out to me is like, you know, the fast like the best RLHF cycle wins in probably a lot of domains.
*  And yet people are not pushing as hard as they could to.
*  Build that like data engine and really getting it to turn over as fast as I think a lot of this probably comes to stage as well.
*  So I think like, you know, I saw in the in the notes, one of the questions you were going to ask me about is about fine
*  tuning and whether a lot of it's happening and the you know, so are people fine tuning a lot?
*  And the answer is like in general, not that many.
*  But the people who are fine tuning tend to be the ones who are further along or slightly more advanced in their journey around building
*  LLM products. And I think a lot of this has to do with sort of like what is the low hanging fruit to improve things?
*  And early on, you can probably get quite a lot of juice out of prompt engineering, which has a very fast feedback loop.
*  And so like if you're spending all of your time making those kinds of changes, then maybe this feedback data isn't yet that valuable to you.
*  And when you get to the point where you're now thinking about actually fine tuning custom models and going a little bit further ahead, then I think, you
*  know, then it starts to make a big difference.
*  And I think the majority of people are still in that first camp.
*  And and I think the reality is it'll stay a bit of both going forwards.
*  But I suspect it's a maturity question.
*  Right. So I think about companies, you know, one of our there's a YC YC company called Find perplexity is another example, but I know the find
*  guys quite well. And they're building LLM based search for developers.
*  So kind of think like the best version of Google married with Stack Overflow.
*  You put a query in and it actually generates you answers with code snippets, etc.
*  They make heavy use of fine tuning and feedback.
*  And they've been able to get substantial model improvements as a result of this.
*  So they're probably have the best and best in the world model now for this task because of that cycle they've been running.
*  But they also have significant machine learning expertise at the time that they were doing this.
*  All of this stuff was really hard. Right. Like Human Loop didn't exist yet.
*  I don't think there was that many other tools around fine tuning.
*  And so I think for a lot of people, fine tuning is a little bit novel, a little bit scary.
*  They're concerned about what happens when the next model comes out.
*  But also they just have so much ground, like so much juice still to get out of prompt engineering that they haven't got there yet.
*  So I think maybe what you're suggesting will come true in the future.
*  I think like my prediction is and I think this is a fairly contrarian take.
*  There will be a lot more fine tuning in the near future.
*  Yeah, that's really interesting.
*  And the other big thing that's just kind of changing in this moment right now is both called this kind of the stable diffusion moment
*  for language models and kind of until you had that, if you just looked at what you could buy straight away with now GPT-4,
*  even before that, 3.5 versus what you could fine tune given the available base models or open AIs,
*  fine tuning is still just the original DaVinci.
*  It was the best thing that they were offering to the public.
*  And that comes also at like now, good God, like 100 times more expensive than turbo.
*  So that like relative capability of the off the shelf versus like what was available to fine tune seems like it's probably also kind of part of what's held the fine tuning back.
*  But that seems like it's flipping literally right now, right?
*  Because we're seeing this stability and a bunch of other models that are pretty like the Lama class of model,
*  even if not Lama exactly, but like densely trained, pretty inference efficient, but strong open source RLHF model or libraries coming online.
*  Yeah, I mean, my assumption is we're at the very early days of this, right?
*  So like one of the questions we get asked most is around privacy and private deployments and people being able to have their own models.
*  And there's a big fraction of the world that will happily use a third party API,
*  but there's also a big fraction who really don't want their data leaving their servers and for whom like a custom fine tune is the only option.
*  And so like there's definitely a strong like demand for this.
*  And increasingly, there are good open source models coming out.
*  I think the first batch of open source models, in all honesty, just wasn't that good, right?
*  So like OPT and Bloom were unfortunately, like significantly behind the equivalent closed models.
*  But that gap is closing, right?
*  Lama is not a permissible license, so you can't use it for commercial purposes.
*  But it is a model that is out there that is performant, right?
*  It's very competitive with the best closed models.
*  And I imagine it's just a start.
*  I think like large language models are somewhat different to the image models.
*  They're harder to train.
*  They require a lot more scale.
*  The models are bigger.
*  I don't think it's going to be as easy as it was for stable diffusion where you can have a four gigabyte model or it's very quickly people had running on phones and laptops, et cetera.
*  The smaller versions of large language models are not as good.
*  They are harder to train.
*  I think there's going to be is not going to be as fast or, you know,
*  but I also don't think that for GPT-3 level models, we have to wait that long for there to be a lot of open source alternatives or a lot of competition in the marketplace.
*  I think if you want the biggest, baddest, best LLM, you're probably still going to be going to OpenAI or Anthropic for a while.
*  But you don't necessarily need that for a lot of use cases, especially if you fine tune.
*  And the main, you know, one of the main reasons we see people fine tuning is, you know, cost and performance.
*  So they're looking for smaller models that can do equally well or better on the tasks that they care about.
*  So what role do you envision yourselves playing at HumanLoop in that future, potentially, you know, coming soon wave of fine tuning activity?
*  Like, do you run the fine tuning processes?
*  I don't expect you're going to say you would like host models, but like, I'm going to have all these kind of like the full of the full stack of problems.
*  If what I've got is like a downloaded, you know, instance of.
*  Stability LLM or stable LLM and a dream, right?
*  So like, what parts of that do you feel like are natural for you to help with?
*  At least early on, I imagine that we will partner with people to help with this.
*  So what we do a really good job of is we have all of that infrastructure in place that captures the data that you would need to make sensible decisions about fine tuning and improvement.
*  We have that evaluation data, the feedback.
*  So it's very natural and we already have fine tuning integrations with the large language model providers that have these APIs.
*  Right. If you want to fine tune GPT-3 and do that well, HumanLoop makes that a very painless process.
*  And so I imagine like partnering with others who have similar APIs and increasingly doing that initially.
*  Because I think to do that well is probably its own entire company to start with.
*  And maybe over time we do more and more of that.
*  But at least, you know, in the early days, in the same way that we don't really want to own the model right now, I think that's a, you know, a big and separate problem.
*  I don't think we probably want to own the fine tuning process initially, but that might change over time.
*  Tell me a little bit about where you think RLHF is today in terms of like.
*  Who should use it? You know, at what scale does it start to make sense?
*  I think there's a lot of expectation that everything is going to be smooth with RLHF.
*  And I think you have an interesting kind of, you know, maybe not so fast take on the difficulties of implementation there.
*  The non-PC version of this is like, I don't know, RLHF is like sex in high school, right?
*  Everyone's talking about it, but almost no one's actually doing it.
*  And we get asked about it a lot.
*  And I think like it is true that RLHF leads to much more performant models, right?
*  The gap between the RLHF GPT-3 models, if you look at the sort of reports or the anthropic ones and the ones that are not, is large.
*  So there is a big performance gain to be had through RLHF.
*  Some of that is just making the models like easier to use, right?
*  So it's not necessarily even about increasing the capabilities of the base model.
*  But it's about making them more aligned with what the user wants out of them.
*  That said, for a lot of the tasks that people come to us and practice, where they're looking to do some specific thing,
*  and they don't need the full generality of the model, and they have a data set,
*  supervised fine-tuning is more than sufficient for them to get good performance.
*  And it's a lot easier.
*  And so in general, you know, I'm pro-RLHF as a concept, and where, you know, it makes sense to do it.
*  If you have a big enough problem.
*  But my advice is always to like, try to find the simplest solution to what you're trying to do first.
*  And only if that doesn't work, go for more complex or harder things.
*  And so if people are thinking about, you know, basically an order of complexity,
*  I think you have prompt engineering, which is like very straightforward and very accessible and very fast,
*  has some limitations to how far you can take it.
*  You're never going to get a 10x latency improvement through prompt engineering, right?
*  Supervised fine-tuning is a little bit harder, it's more involved.
*  But you can get gains that you couldn't get through prompt engineering,
*  because you can get big, you know, cost or latency improvements
*  that are just never going to come through prompt engineering alone.
*  And RLHF can give you significant performance improvements on top.
*  Pick the, you know, the appropriate tool for the job.
*  Like how complex do you actually need this to be?
*  What is it that makes the RLHF so much more challenging in your experience?
*  It's a multi-stage process, right?
*  You're first training this reward model.
*  You've got to get all of this annotated data.
*  You've got to make sure you do that process correctly.
*  You're then training a reward model on that.
*  So you have another model to train.
*  And then after that, you're doing that, you know, you're doing an RL step.
*  So there's just more places for things to potentially go wrong.
*  There's more complexity to handle.
*  If you look at the kind of appendices of the Instruct GPT paper,
*  there's a lot of nuances and subtleties that you have to get right to make this work robustly.
*  Whereas supervised fine-tuning is pretty straightforward.
*  Relatively speaking, right?
*  You just need a data set, not even necessarily that larger data set
*  for some of these large models.
*  I was speaking to a founder last week who has been auto-generating tests.
*  He hand wrote 50 examples and fine-tuned DaVinci 2 on that.
*  And now he has a pretty good model.
*  And 50 examples is not that many for him to be able to get, you know,
*  a pretty reliable fine-tune.
*  With more examples, he could probably do it with a smaller model.
*  To do the equivalent with RLHF would have been really hard for him
*  and probably just not the appropriate tool.
*  How does that actually cash out in terms of failure modes?
*  Is it that people can't make the process work because it's too intricate
*  and there's just too many parameters to wrangle?
*  I mean, I've heard that kind of account in the past.
*  But then you also see these mode collapse type reports.
*  And there's this sense of like,
*  you kind of have a lot of dark matter in terms of other domains of possible,
*  possibly much worse model performance as a result of the RLHF.
*  What do you see there in terms of how it actually goes wrong for people?
*  I mean, it's more the more of at least from our perspective,
*  it's more the former than the latter.
*  It's just like very hard to actually get it to work reliably.
*  Do you even get the model to learn what you want to do at all or to do it robustly?
*  Small changes in the reward model can have quite big impacts.
*  Reinforcement learning in general is just a lot more finicky than supervised learning.
*  RL is harder.
*  And that was my experience even as a researcher.
*  Every time we got rid of an RL component,
*  everything seemed to just be a little bit more robust or a little bit more reliable.
*  So it's more that in terms of things like mode collapse.
*  So the RLHF models, I think are in some sense is less capable than the base model
*  conceptually or in some ways.
*  But they're much easier to get to work.
*  I think a lot of what you're doing is figuring out how do I
*  get the capabilities of this model to be easy to access.
*  People like Riley, who I think you had on the podcast recently,
*  are wizards at taking the base model and having spent a long time playing with them
*  can figure out the right way to prompt them to get the output they want.
*  The nice thing about the RLHF models is you don't have to do that as much.
*  I think you mentioned this earlier.
*  You can more reasonably expect an instruction and natural language
*  to get you the outcome you care about.
*  You are sometimes paying a little capability cost.
*  Certainly the people who tell us they use the models for more creative tasks,
*  like natural fiction writing assistants or things like that,
*  they use the base models where they can.
*  They prefer them to the RLHF models because they get a greater variety of output.
*  My kind of working theory on this agent moment,
*  which you said at the top is obviously all the rage right now
*  and yet mostly they don't work.
*  My sense is that the RL paradigm is a pretty good fit there
*  and that there's just going to be a ton of what didn't work
*  and then very concretely what did work in terms of
*  CODIS policy style API calls generated or what have you.
*  So I guess a two-part question there.
*  How quickly do you think that that's right?
*  Do you think that paradigm will kind of lock these little
*  code generator agent models into form over the not too distant future?
*  And then how does Human Loop think about playing in that space?
*  You have the tools offering, but it's been a minute since we talked about that.
*  So it's maybe worth just mentioning what tools are in Human Loop.
*  One of the problems that a lot of the companies that we work with face
*  is figuring out how to get private company information into their models.
*  And so tools in Human Loop are basically APIs that take text as input and text as output
*  and they're used to augment the models with extra information.
*  So for example, we have a tool that accesses the Google API or the SERP API.
*  So if you do a factual query, it can look up from Google
*  or you might connect Wikipedia or something.
*  It can pull that information from there
*  and include that in the context of the model to help you get a more factual response.
*  And Google and Wikipedia are public sources of information,
*  but increasingly people are connecting private sources.
*  So they'll connect a database or they'll connect an FAQ or something like that
*  and give the model access to that at inference time.
*  So when someone comes and asks the question, the model can pull information
*  or we pull information into the model's context and allow the model to use that.
*  So tools are essentially a way to add extra information to the model.
*  Which is slightly different, I think, from some of the other ways
*  that sort of tools have been used up for now, where people have the GPT-3 plugins,
*  for example, allow the models to take actions.
*  Human Loop doesn't let you do that yet today
*  because we haven't found it yet to be reliable enough.
*  So we're very excited about it in the future,
*  but we see less of that up till this point.
*  In terms of will RL just fix the agent problem, my suspicion is no.
*  I basically think that the issue with agents is that you start with a core module
*  that has some reasonably high probability of error, I don't know, 85 or 90% accurate,
*  and then you chain these things together.
*  And so the longer the chain gets, like 0.85 or 0.9 to the power n,
*  as n gets large, that thing tends very quickly to zero.
*  And so your probability of it working decreases rapidly with the number of steps in your chain
*  and you're essentially running open loop control.
*  You have a system that's getting no feedback as it goes,
*  and so if it makes errors, the errors compound.
*  So I think that probably the solution will actually be some form of feedback mechanism,
*  not necessarily human feedback,
*  but some way for the models to heal their agents or heal their chain.
*  So if it goes wrong, there is some other mechanism, another model maybe,
*  that is able to look at that and go, no, that bit's wrong, try again,
*  or here's what you might have done.
*  Because I think you need some way to course correct.
*  Without course correction, I just don't see how agents become reliable.
*  Yeah, I mean, I think those kind of work together though.
*  Like the multi-agent system is definitely...
*  When people talk about agents, a lot of times you dig into these things,
*  it is kind of a...
*  It might be a single language model, but it is kind of powering
*  some sort of multi-agent configuration or ensemble or something.
*  And I think you need that.
*  I think you need that for it to have a chance of working to make it robust.
*  Some people may be getting these working.
*  We certainly see a lot of people chatting about it on Twitter
*  and posting very cool demos.
*  From the production side of seeing people actually put these things into production
*  and speaking to people who are trying to do that,
*  we just hear again and again and again that they try and they don't quite succeed yet.
*  But what do you think I'm missing about this?
*  Because what I kind of imagine happening with this feedback loop is,
*  basically, what's the most automatable sort of feedback
*  is whether the code executed successfully or not, right?
*  And then on the far end is like,
*  do you prefer this sonnet or that sonnet is probably the hardest.
*  Interestingly, visual art gets very comparatively close
*  because you can make that judgment often in a fraction of a second.
*  But nothing works at the speed of the code worked or not.
*  So it seems like there's this kind of very natural,
*  pretty substantial data set that's going to kind of just accumulate in the logs almost,
*  maybe not super useably automatically, but with the help of human loop, that stuff shows up.
*  There's only so many APIs.
*  There's only so many ways to call the APIs that are right.
*  Obviously, you do have the world is shifting and this is never a done problem
*  because people change their APIs.
*  Although I think it's going to become on the API providers to come up with a way
*  to make sure the language models continue to work before you know it.
*  No, I don't disagree.
*  Right.
*  So as I said, I've been talking about agents and we've been talking about them in human loop
*  for like well over six months now.
*  We are very excited about it conceptually.
*  I assume that it'll be a key part of this in the future.
*  I guess I'm just giving you the perspective.
*  I think given how hyped they are at the moment,
*  I'm just giving you the perspective we're hearing from our customers
*  who are trying to build with them.
*  And the most common perspective we hear is we've tried really hard.
*  It works 80% of the time, which is not good enough for our production use case.
*  Yeah, that's definitely consistent, I'd say, with what I've seen as well.
*  We've had two CEOs of agent platform product companies on the show.
*  And notably, neither one is quite scaling just yet.
*  One is not even really quite released and the other has kind of a demo, but is definitely not
*  hitting that inflection point in usage just yet, I don't think.
*  Yeah, it does feel like it's going to be another wave that's kind of on us before we know it.
*  Do you think we'll get out of, if you had to guess, end of 2023,
*  are these problems largely solved and we have agents doing our online bidding?
*  I'm very optimistic about the rate of progress.
*  And part of that comes from kind of having course corrected a bit.
*  So, you know, I've been in the field of machine learning and I did a PhD in it
*  for now, I guess, like six or seven years.
*  And I've consistently been too pessimistic and how quickly I think things would get done.
*  So I kept making predictions.
*  I thought, oh, that will take this many years.
*  And again and again, I've kind of been beaten down to the point that I've kind of learned
*  that this progress seems to be happening a lot faster than most might expect.
*  So that's not a super reasoned answer, I suppose.
*  But my intuition is that, yes, these things will get solved very quickly.
*  Yeah, I've honestly kind of had the other experience where I've been an entrepreneur
*  for pretty much my entire career and I've always underestimated how long different changes will take.
*  And I may be proven to have done that again in terms of like,
*  how quickly AI implementation can happen.
*  But AI, just raw capability progress is the one thing that has found the other side of that for me.
*  I've always been like, oh, by this time, there's no way you won't have this awesome experience.
*  And then people just kind of live with the status quo a lot longer than I anticipate.
*  But this has been the one exception.
*  There's the point where we get the capabilities and then the point when that gets into products.
*  And the thing that part of what made us go and build Human Loop is that gap felt too big to us.
*  That actually we could see that the model capabilities were far exceeding what was
*  actually being productized or built for a long period.
*  And I think that turns out to be because productizing these things is harder than
*  just having a model API.
*  But yeah, so I think there will be a gap between when these things get solved in research and
*  when people figure out how do I make this useful and actually productize it.
*  This kind of anticipates one of our typical closing questions.
*  But I've asked a ton of extremely smart and very plugged in people now what applications
*  they use that they would recommend to the audience.
*  And you can answer that one.
*  You probably have a good answer.
*  But honestly, surprisingly, most people haven't named that many things.
*  They've largely been like, well, I use ChatUpt.
*  And then we certainly hear a lot of copilot.
*  And then we hear that's about it.
*  There's a little bit more.
*  Certainly, some people are into the art.
*  Occasionally, somebody would be like, there's a spreadsheet plugin that's killer for me
*  or whatever.
*  The names of applications that people name, it's honestly very few.
*  Are these AI first products just too far behind the incumbents to overcome them before
*  the incumbents can layer on the AI?
*  Is it just that the amazing UX and UIs?
*  Of our future haven't really been discovered or invented yet.
*  How do you see that playing out over a couple of years?
*  So I just think it's very early.
*  I think you're right that most people are not using that many AI products.
*  If I think about my day to day usage, I use various forms of coding assistant quite frequently.
*  I use the human loop playground a lot.
*  For me, it's mostly replaced ChatUpt usage, but it's probably similar to what people are
*  using ChatUpt for.
*  I have various forms of summarization assistant attached to all of my sales calls that are
*  creating transcript notes for me that I use pretty frequently.
*  I'm probably using that four times a day or something.
*  In terms of volume of usage, I'm using new search engines.
*  When Perplexity had BirdQL, I was using that all the time, their Twitter search, because
*  it was insanely better than a terrible Twitter search experience.
*  Unfortunately, it's not available anymore.
*  So I'm increasingly seeing them.
*  But I also just think that the current wave of applications only really started getting
*  built four or five months ago.
*  To be looking around and saying, where are all of them seems a bit premature to me.
*  We haven't had this for that long.
*  But I guess there's a second question, which is, is this more a sustaining innovation that
*  will help larger companies or is this more disruptive where startups end up winning?
*  I thought about this a fair bit.
*  I think the answer is almost certainly both.
*  I think in established categories where you have a big player that's winning, integrating
*  these features very quickly, I think happens very naturally.
*  If you're one of the large contract review providers or you're a HubSpot or Salesforce
*  and you have a CRM or something like this, then adding automated extraction of notes
*  and adding summarization and all these kinds of features, I don't think is that difficult.
*  And obviously enhances the product and they have the distribution channels and they're
*  going to get more user feedback.
*  They probably win there.
*  But I also think that there will be entirely new categories created or new styles of product
*  that weren't possible before.
*  The people who ask, what does the IDE look like if we build it from the ground up today?
*  Or someone who's building an educational assistant.
*  What is the next version of a language learning app look like?
*  I'm sure all of the big successes right now are rethinking their products and maybe it'll
*  work as an add-on, but maybe something new built from the ground up will replace that.
*  And then there's just the UX experiences that people haven't thought of yet because this
*  stuff is so new.
*  I think we're still in that stage of plays on the television.
*  We've taken stuff from the old paradigm and slotted it in.
*  I don't think we've fully thought about what does this let us do that we really just
*  couldn't do before because it's so early.
*  Yeah, that's a good analogy.
*  I'm a collector of AI analogies that I think...
*  I'm not a connoisseur of too many things in life, but one that I might claim connoisseurship of
*  is AI analogies.
*  And I like that one.
*  I haven't heard it before.
*  But what I like about it is the big difference between the play on the TV and the modern TV
*  show is just a ton of cuts, all these different things integrated together with a whole tool
*  chain into a final product.
*  And that is really where we're still very much figuring it out.
*  So I think that's a very good image.
*  I'm always very suspicious of what is sneaking into this analogy that's actually going to
*  mislead me.
*  So I'll have to report back if I come up with any concerns, but I do like that image a lot.
*  What I would say is that I think the incumbents that don't adopt this technology will fall
*  behind.
*  So I do think for a lot of companies, it is a sort of adopt or die type moment.
*  If you are a legal tech company and you don't start adding these things, if you are a CRM
*  company, you don't add these things, someone will and I will give a much better product
*  experience as a result.
*  I just don't think it's that hard for them to add them.
*  And the large enterprises seem to have been remarkably fast to adopt relative to previous
*  technology waves.
*  I mean, this whole thing has been led in some ways by Microsoft.
*  Who has been faster to add LLM features than Microsoft?
*  Nobody.
*  Replit, they would point out, is right up there as well.
*  Replit is definitely up there.
*  Replit is definitely up there, but smaller products we'd to be adding it to.
*  And I just guess you expect Replit to do it.
*  Replit adding these things is great, but I expect fast moving startups to do it.
*  Yeah, your point is very well taken.
*  I've rippled on the brain today because I've got a big announcement that I'm excited to see.
*  Oh, fantastic.
*  What they're adding to an already exciting product.
*  But you're totally right.
*  That Microsoft could lead in this space would previously have been unthinkable.
*  It's certainly something we're starting to see at Human Loop as well.
*  Increasingly larger companies approaching us because they want to implement LLM features.
*  They've started to try in-house.
*  They're seeing the same pain points that others had.
*  How do I prototype?
*  How do I handle prompt management?
*  How do I evaluate?
*  How do I make this better over time?
*  How do I fine tune?
*  And they're starting to look for solutions.
*  But that's fairly recent, I would say, more over the last couple of months than previously.
*  Do you see consultants?
*  What do you think is the role of...
*  OpenA has this partnership with Bain.
*  Do you think that's going to work?
*  There are all these big companies that presumably can do process automation at a minimum
*  and maybe don't have that plugged in CTO, that HubSpot and some other...
*  More tech-forward companies have the benefit of employing.
*  Are Bain consultants coming to you and bringing Fortune 1000 projects to Human Loop?
*  I can neither confirm nor deny.
*  I guess OpenAI doesn't want to do the sales part of this.
*  I think they're sincere in their objective being to build AGI.
*  And so I think they are encouraging an ecosystem to develop on the tooling side.
*  They're working with partners on the sales side.
*  I think so that they can maintain their focus on what they see as the thing that they do best,
*  which is pushing the boundaries of AI.
*  So I think insofar as they're working with people like Bain,
*  Bain is going to be better at enterprise sales than OpenAI is, almost certainly.
*  And I think they're choosing to partner rather than try to do everything,
*  which to me seems like a very smart strategy.
*  Yeah, especially when you have the thing the whole world is clamoring for.
*  A channel partner can really add a ton of value.
*  What we can offer from in terms of perspective at Human Loop is I suspect we have seen more people
*  try, succeed and fail at getting applications into production than I suspect almost anyone
*  other than maybe OpenAI.
*  And that gives us some insight, hopefully, into what applications are actually being built.
*  And we discussed that a little bit.
*  And also the challenges people have around reliability, factualness, evaluation,
*  experimentation that I think almost everyone will face when they do come
*  to actually try to productize this.
*  And that's what Human Loop is there for.
*  We're building the tools that bridge that gap between I have access to the GP4 API,
*  I have access to an LLM, and I actually need to make this robust and understand
*  how it works in production.
*  And yeah, I think it gives us a unique perspective.
*  And some of it really is just having the right workflow to iterate very quickly.
*  In fact, actually, probably that's the thing that I would say is the most important.
*  Because a lot of this requires trial and error, it's difficult to kind of get it right first time.
*  Having a really fast iteration cycle to be able to try something, understand how well that worked,
*  and go again, whether that's fine tuning, whether that's changing the prompts,
*  whether that's rethinking the UX a little bit.
*  I think that really makes a big difference about whether or not you get to success.
*  And I guess the people who don't get there tend not to set up robust evaluation systems.
*  So they don't know whether as they're making changes, things are actually getting better or worse.
*  And if you're kind of changing a lot of stuff flying in the dark,
*  you're not actually going to make progress.
*  And so yeah, I think really robust evaluation and fast iteration cycles have been the things that,
*  if I was to have to extract principles that I think make this stuff work well.
*  I'd love to hear just how you think about guiding people up the curve of scale and sophistication
*  of evaluation. Because those things I think are very much like,
*  ideally should be working in tandem for people, but maybe not always are.
*  Yeah, so I think the typical journey we see is people start in something like the playground
*  with a handful of test cases. And the question they're really just trying to answer for
*  themselves is like, is this even feasible? Like, can I get the model to do this task?
*  And they don't really know yet. And so they spend some time iterating with that.
*  Usually they're convincing themselves yes or no on that question. Like, can I, you know,
*  is this something that's within the capabilities of the model? Maybe experimenting with a bit of
*  prompt engineering. Typically at that point, they'll go and actually wire this up into some
*  kind of product. They might have like some kind of internal evaluations. We typically see people
*  also will hook this up to something like a streamlet app or just a very simple UI to collect a little
*  bit more volume of internal evaluation. And there they're looking at maybe like hundreds to
*  thousands of examples, just trying to get some quantitative metrics on performance.
*  Some of the startups skip that step entirely. So this is like, you know, that step is more
*  common amongst the larger companies. The startups typically, once they've kind of got satisfaction
*  that it works like 80, 90% of the time, will typically just deploy it. And then we'll use the
*  in-production data as a way to understand how well things are working and then iterate very fast.
*  And by the time you have like a few hundred interactions per day, which is not that many,
*  because people are often touching the models in multiple places, you start to have enough
*  signal to start actually driving decisions. So you don't need masses and masses of data,
*  but you do need some usage. You do need some people coming through the app.
*  And most have a lot more than that pretty quickly.
*  I already did the kind of version of products you'd recommend if you want to throw any
*  else out there. Mems are a good example here, right? So I think like rethinking what a note
*  taking app looks like if you try to put LLMs everywhere, self-organizing system for notes,
*  where you just dump everything in and it tries to figure out where things belong. I don't think
*  people think of that as an LLM product, but it's obviously very AI driven in the background.
*  I think that's a cool one. I'm a big fan of the new LLM search engines. I think
*  find is really cool. I use cursor all the time, which is like that ID product I was telling you
*  about. So I'm a big fan of that. They've got an integration to VS code. The ones we all already
*  know about, like GitHub Copilot, everyone in our team uses that pretty frequently.
*  As I say, I do end up using the human loop playground a lot. I now prefer it to the
*  OpenAI versions or chat GPT. And so that's where I live. And also I think it's important
*  for us to use the products ourselves to improve them. So that's another one I'm using pretty
*  frequently. I have a note taker that goes to all my Zoom meetings. I get transcripts and summaries
*  from that. So I use Fathom for that. But I think there are many others, Firefly and others. I don't
*  know if they also have those AI summaries built in. What else do we use pretty frequently? I mean,
*  we also use just the raw GPT 3.5 and Cloud models in our Slack quite a lot. So we have a Slack
*  channel and also individual access to Slack with those models built in. And just having them there,
*  where you're working most of the time, means we end up using them more than I think if we had to
*  go to the playground or go to chat GPT. Okay. Quick hypothetical situation. Let's imagine
*  that in a not too distant future, 1 million people already have the Neuralink implant.
*  If you get it, just like everybody else, you get now the advantage of thought to device
*  direct communication. So you can record your thoughts as text or use a UI. Would that be
*  enough for you to consider getting an implant yourself? Has it been safe for those first million
*  people? Yeah. Let's say we're in COVID vaccine safety, where you've certainly got some noise
*  around it, but the general data suggests that it's overwhelmingly safe. It's a difficult one
*  to answer because I feel like whether or not I say yes depends so much on the political context
*  around the technology. And I feel similarly with AI. We're building this very powerful, potentially
*  hugely positively transformational technology. But in order for it to be positive, we need to
*  make sure that everyone gets a say in how it's used and it's democratically controlled and
*  et cetera, et cetera. And I think I would feel similarly about something like Neuralink.
*  Like if the right safeguards were in place, then I would seriously consider it. I already have a
*  prosthesis. It's my phone and I'm glued to it all the time. So it's only one step further.
*  But I'd want to be confident that I'm not opening up literally my brain to some like
*  advertiser model driven, concentrated, like do I want Facebook or Google or whatever large tech
*  company to have direct access to my brain? Probably not. But if all the right safeguards
*  were in place and we had the right political structures in place, I'd be very excited
*  about the technology. Brilliant answer. I think the distinction there between medical safety and
*  social contextual safety is a very sharp one. That's also a perfect transition to
*  typical final question, which is just zooming out as far as you can. We've spent all this time
*  really on kind of the current margin of implementation and the struggles and the
*  triumphs and the tools around that. But zooming way out, what are your biggest hopes for and fears
*  for what AI is going to mean to society over the next handful of years?
*  So on the hope side, I really hope that it augments people to be able to achieve stuff
*  that they couldn't do before. So I really hope that we accelerate the progress of science.
*  The volume of literature being produced is way beyond what anybody can read in full. It's
*  probably lots of connections to be made. If we can make progress faster in medical research,
*  in other parts of scientific research, we've got diffusion more quickly, whatever it might be.
*  I think that would be a hugely positive and exciting win. And we've seen early signs of
*  this from DeepMind Alpha Fold and things like that, where it seems plausible that we can
*  accelerate scientific progress with AI. I'd also be really excited about increasing access to
*  education. So whether this be even just in the rich world, giving more people access to more
*  personalized educational experiences, which I suspect what will happen first, but also if
*  we can reduce the cost of education far enough and figure out ways to give more people access to it.
*  That's a really exciting vision to me. Personal tutoring is one of the educational interventions
*  that seems to have the largest evidence behind it, but it's very expensive to scale with humans.
*  What does an AI version of that look like? And that could be very exciting.
*  I think freeing people from work they don't want to do is also something I'd be very excited about.
*  And I think a lot of us spend time doing just drudge work as part of our day to day.
*  I'm less excited about the potential for misuse. I think it could concentrate political power.
*  I do think there are challenges. You mentioned earlier using AIs for screening CDs. It always
*  raises a red flag in my mind when you give autonomous systems these decision-making
*  capabilities that have big effects on people's lives. Can we make sure that we don't bake in
*  political or social biases and then scale them and systematize them worse than they even are now?
*  I think there are risks, but I also think there's potential huge upsides. I'm very excited about a
*  world in which software is generally smarter and works a bit better and is easier to produce.
*  One thing I'm just excited about is lowering how hard it is to build software products. I think
*  there's lots of places where we could have good software, but the markets are small. It's not
*  interesting for a company to be built around it, but it could improve some people's lives.
*  The cost of producing software is going down dramatically.
*  Many big benefits, education, healthcare, science improvement, definitely risks as well,
*  even before we get to anything that resembles AGI. Excited, but cautious.
*  Raza Habib, thank you for being part of the Cognitive Revolution.
*  Thank you for having me.
*  Amnaki uses generative AI to enable you to launch hundreds of thousands of ad iterations that
*  actually work, customized across all platforms with a click of a button.
*  I believe in Amnaki so much that I invested in it, and I recommend you use it too.
*  Use Cogrev to get a 10% discount.

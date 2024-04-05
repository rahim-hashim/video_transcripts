---
Date Generated: April 03, 2024
Transcription Model: whisper medium 20231117
Length: 3826s
Video Keywords: []
Video Views: 2303
Video Rating: None
---

# The AI Assistant Revolution with Flo Crivello of Lindy.AI
**Cognitive Revolution "How AI Changes Everything":** [March 22, 2023](https://www.youtube.com/watch?v=tGKULKTsapA)
*  and he, Napoleon, had the highest material of all,
*  he had aluminum.
*  I'm drinking La Croix right now,
*  and aluminum has become so cheap,
*  we literally throw it away.
*  I'm literally drinking in aluminum,
*  and then I'm going to throw this away.
*  This would have been unthinkable.
*  I think it's going to be the same thing with code,
*  where it's like an app today costs of
*  the order of 10 to $100,000 to build.
*  While rapidly approaching a world where an app costs of
*  the order of one or 10 cents to build.
*  When that happens, you basically start having disposable apps.
*  You basically start building an app just for
*  this one session that you have right now.
*  That's basically what Lindy is doing.
*  Hello, and welcome to the Cognitive Revolution,
*  where we interview visionary researchers,
*  entrepreneurs, and builders working
*  on the frontier of artificial intelligence.
*  Each week, we'll explore their revolutionary ideas,
*  and together, we'll build a picture of how
*  AI technology will transform work,
*  life, and society in the coming years.
*  I'm Nathan Labenz, joined by my co-host, Eric Torenberg.
*  Omniki uses generative AI to enable you to launch
*  hundreds of thousands of ad iterations that actually work,
*  customized across all platforms with a click of a button.
*  I believe in Omniki so much that I invested in it,
*  and I recommend you use it too.
*  Use Cogrev to get a 10 percent discount.
*  Our guest today is Flo Crivello,
*  founder and CEO of Lindy,
*  an AI assistant that aims to put your life on autopilot,
*  online at lindy.ai.
*  One of the smart, but already increasingly mainstream takes
*  in AI right now is that the next big thing will be actions.
*  That is, taking the AI paradigm beyond generating
*  inert text and allowing models to use tools
*  to take actions and ultimately get things done.
*  There are a number of ways to go about doing this,
*  but they all involve using a language model
*  to bridge the gaps between a user's request,
*  typically specified in natural language,
*  and an action space, which could combine APIs, web browsers,
*  other software applications or interfaces,
*  and eventually even robotic controls,
*  all while taking into account the user's history
*  and preferences, which unfortunately for developers,
*  tend to be spread out across email accounts,
*  Slack conversations, calendar history, and much, much more.
*  Now, people have imagined AI assistance seemingly forever,
*  at least from the Jetsons to her,
*  but recently they've become a central focus.
*  ChatGPT broke through to the mainstream in part
*  because of its accessible chat assistant style interface.
*  And in the context of AI safety,
*  assistance have been described as a laboratory for alignment.
*  To state the obvious, economically,
*  an AI assistant that really works
*  will be incredibly valuable technology.
*  Indeed, Flow talks about Lindy as a virtual employee,
*  and with such a big prize to be won,
*  he'll surely face competition
*  from some of the biggest companies in the world.
*  Alexa and Google Assistant are already in millions of homes,
*  and Siri is rumored to be due for an update in June.
*  Still, Lindy is no hackathon project.
*  It's a serious effort with a dedicated team,
*  backed by real resources and critical connections.
*  Flow has raised $50 million,
*  and his team was building on GPT-4
*  for a month prior to launch.
*  They've got a level of ambition
*  that sometimes creates life-changing products
*  and generational companies.
*  So while Lindy is being announced today,
*  and currently still in very limited beta,
*  in keeping with our goal of helping listeners understand
*  and where possible experience the near-term AI future,
*  we did get Flow to agree to prioritize anyone
*  who mentions the cognitive revolution
*  when signing up for their wait list.
*  One note, Flow does give me a screen share
*  to give a demo of the product during this interview,
*  and while that part of the conversation
*  doesn't go on for very long,
*  and I think you should be able to follow it
*  from the audio alone,
*  we do have video available on YouTube,
*  and you can also watch some flashy demo animations
*  on their site at Lindy AI as well.
*  Now, I hope you enjoy this preview
*  of the AI Assistant future with Flow Cravello.
*  Flow Cravello, welcome to the cognitive revolution.
*  Thanks for having me.
*  Really excited for this conversation.
*  You are launching something new,
*  and I think it is something that is going to,
*  you know, you and then others who are exploring this space,
*  I think are going to really change the way
*  that people use computers by harnessing the power of AI
*  and making it useful for practical everyday tasks.
*  So tell us about what you're building,
*  what you're launching, and let's get into it.
*  Yeah, so we're building Lindy.AI.
*  So it's an AI assistant that can basically do stuff for you.
*  Like you can think of it as that GPT
*  that can also use your applications and access your data
*  in order to automate your work.
*  So it can own your calendar, own your email,
*  book travel, send contracts, scrape the web,
*  help you prospect, help you recruit,
*  and all of that kind of stuff.
*  So we've basically trained a large language model
*  to be able to use tools and to train itself
*  on how to use tools based only
*  on the documentation of these tools.
*  So we literally just feed it to the human documentation
*  of an API, like the Stripe API or the Slack API,
*  and then it's just knowing how to use the API.
*  And then we can give it a goal,
*  and it figures out how to use which APIs when
*  in order to fulfill its goal.
*  So for example, if I go like,
*  help me find half an hour with this and tomorrow,
*  it's going to first hit up the Google Calendar API
*  to find my calendar and my availabilities,
*  and then it's going to compile an email
*  and hit the Gmail API to send you
*  these availabilities by email.
*  And then once you reply, it's gonna hit the GCal API again
*  in order to put that time on both our calendars.
*  So that's the idea.
*  We're actually gonna do the screen share,
*  and this will be available in the video version
*  of the podcast.
*  So if you are listening, you can still listen along,
*  and hopefully it will be clear enough.
*  But if you really want to see the thing in action,
*  then flip over to the video version,
*  and you'll actually be able to see a preview
*  of this product, lindy.ai.
*  Here I have a sort of like big text field in the center.
*  It's funny, actually, the first good name
*  for the product was Google.
*  It's like Google accepted that stuff for you.
*  And I'm gonna type, find me Ben Software Engineers
*  in San Francisco.
*  So I'm actually already using lindy for hiring quite a bit.
*  It's really, it's making it 50x easier for me.
*  So it loads a little bit, and then it asks me,
*  hey, you're going to use some prospecting credits.
*  And then now it just showed me a list of software engineers.
*  And if I click, there's name, current role, LinkedIn.
*  And if I click, I see actual software engineers.
*  So this guy works at Sprite,
*  this person works at AdSana, and so forth.
*  And there's a little bit of debug information here.
*  None of this UI is hard coded.
*  Basically, the AI has UI components
*  that it just mix and matches
*  in order to do its job at any given time.
*  So now I can follow up with these candidates,
*  and I can be like, craft them a recruiting email
*  to join lindy.ai, a startup building and AI assistant.
*  Or I could be like, draft them a recruiting email
*  based on this JD.
*  And here I could paste a Google Docs link or a Notion link.
*  And it would read the JD
*  and draft the recruiting email based on that.
*  Or I could go like, personalize the recruiting email
*  for these people.
*  And boom, it sends the email,
*  and I can just customize it here.
*  Again, this UI is basically built by the AI at runtime.
*  And I can send the email.
*  I'm just going to cancel here
*  because I don't actually want to send this email.
*  You can also ask Lindy to help you with recurring tasks.
*  So for example, here, and this one is a prototype.
*  I can be like, before my meetings,
*  send me the Zoom and attend these LinkedIn
*  and summary of our last interactions.
*  And it's going to create this automation,
*  which is that five minutes before every meeting,
*  it's going to grab the Zoom link,
*  grab my emails with these people,
*  grab my meeting recordings with these people,
*  and grab the LinkedIn of these people,
*  and then send me a summary of all of that on Slack.
*  Back to real demo, again,
*  can grab the meeting recordings
*  because it's currently already joining my meetings.
*  So it joins my meetings.
*  I can see my list of meeting recordings here,
*  and I can click on any meeting.
*  I see the, like it takes notes for me.
*  It summarizes the meetings,
*  and then I can chat with it about my meetings.
*  Like, what was the meeting about?
*  What did Flo think?
*  What was the particular way of the meeting?
*  Or I can go like, hey,
*  can you update my Salesforce based on this meeting?
*  Or can you create tasks on linear based on this meeting?
*  And so on and so forth.
*  So, you know, it's basically like an AI employee.
*  And so just like an AI,
*  just like an employee,
*  you can talk to it however you'd like.
*  You can send it emails,
*  you can talk to it on Slack,
*  or you can invite it to your meetings
*  and collaborate with it however you'd like.
*  Boy, there's a lot here that I think is fascinating,
*  and I'm excited to unpack.
*  For one thing, I see that you had a monologue
*  that went longer than the recommended max of 230.
*  That sounds like the sort of AI coaching
*  that I also need as somebody who has more than once
*  gone beyond the maximum monologue recommended length.
*  So I think that's funny right off the bat,
*  we're seeing these kind of coaching type interactions,
*  you know, coming back to us from our AI assistants,
*  like in some ways, you know,
*  they already know better than we do.
*  But let's kind of just, you know,
*  unpack a lot of what we just saw,
*  because you showed a lot very quickly.
*  First thing that I want to understand is just,
*  how does this thing handle my accounts?
*  You know, because I've experimented
*  with some similar paradigms,
*  even going back to the GPT-4 red teaming days,
*  you know, one of the first things I thought was,
*  holy moly, like this thing is so smart,
*  it might be able to sort of use itself as a tool,
*  you know, it's so good at coding,
*  maybe it can even like break down problems
*  and sort of delegate the solving of those problems
*  to itself recursively, and who knows what it might,
*  you know, be able to accomplish then.
*  What I found was one of the biggest challenges practically
*  in getting that to work was just,
*  everything is protected by authentication,
*  and you know, it's hard to,
*  especially if you're just kind of, you know,
*  one person like I was at the time exploring something new,
*  it's hard to get enough stuff connected
*  to figure out all that like security logistics
*  to actually get something to work.
*  So obviously in your demo there, you had stuff set up,
*  but what is a new user experience
*  and how are you thinking about that,
*  both from like a user experience standpoint,
*  and ultimately obviously security is gonna be critical
*  to this application as well.
*  So it's a little bit like onboarding an executive assistant,
*  like when you start working with an executive assistant,
*  you hand over to them the credentials
*  of whatever tools they are going to need
*  to get their job done.
*  So here it's actually more secure than that
*  because you don't give the AI your password,
*  you just owe us with Google or Linear or Osana
*  and so on and so forth.
*  So, and we make you owe us with them
*  on a just in time basis.
*  So the first time you ask it,
*  hey, help me find time with this,
*  and maybe like, look, I need your calendar
*  and your email to do that.
*  And then you connect with Google and that takes two clicks.
*  Yes, it's funny what you say about recursively calling
*  itself because that is something that it does.
*  So the way it works is that it basically writes code.
*  And I'd love to get back to that
*  because I think it's insanely interesting the fact
*  that it writes a one time piece of code for this.
*  But when you ask it to do something,
*  it writes a piece of code to fulfill the tasks
*  that you ask it.
*  And in that code, it's got functions to call itself back.
*  So for example, in the example that I just gave
*  of summarizing your last interactions with someone
*  is going to write a piece of code
*  that's like hit up the Zoom API to grab the recordings,
*  hit up the Gmail API to grab your emails to this person,
*  and then call myself back to summarize these pieces.
*  Again, like to go back to the code thing,
*  I always compare the moment we're into it.
*  I think like that's why like the name of the podcast,
*  the Cognitive Revolution is very apt.
*  It's striking the parallels between this
*  and the Industrial Revolution.
*  Like the Industrial Revolution made some goods so cheap
*  that we could now have single use goods.
*  Like we have like big pens, like disposable big pens
*  and like solo write caps that you use only once
*  and throw away.
*  Like that was unthinkable before the year 1700.
*  Like a cap was probably like the equivalent
*  in today's dollars of, I don't know,
*  like $500 or something.
*  And now you have like caps that are like five cents, right?
*  There is this crazy story of Napoleon at some point
*  had a bank account with a bunch of world leaders
*  and the lower leaders had like silver cutlery
*  and the higher leaders had gold cutleries,
*  the higher leaders had platinum cutleries
*  and he, Napoleon had the highest material of all.
*  He had aluminum.
*  And I'm drinking La Croix right now
*  and aluminum has become so cheap,
*  we literally throw it away.
*  I'm literally drinking in aluminum
*  and then I'm gonna throw this away.
*  So this would have been unthinkable.
*  So I think it's gonna be the same thing with code
*  where it's like an app today costs of the order
*  of 10 to $100,000 to build.
*  While rapidly approaching a world
*  where an app costs of the order of one or 10 cents to build.
*  And once that happens,
*  you basically start having disposable apps.
*  You basically start building an app
*  just for this one session that you have right now.
*  And that's basically what Lindy is doing.
*  You give it a use case,
*  it's going to build a one-time app,
*  it's going to write the code for that app
*  for that one session and then when you're done with it,
*  it's just going to throw the app away.
*  That is fascinating.
*  I've done that a couple of times already.
*  We're just to date the recording of this podcast.
*  We are at GPT-4 plus seven,
*  as I've started marking everything
*  from the date of GPT-4 release.
*  And it has been kind of amazing to just,
*  a couple of times when I had a particular need,
*  whether for a little data analysis
*  or like make me a little chart out of this data,
*  GPT-4 can do that straight out of the box
*  for some basic things.
*  It obviously does not have all of the authentication
*  and sophistication, let alone like the sort of recursive
*  or access to a runtime.
*  So there's a lot here that you are adding on
*  to the kind of core functionality.
*  But even just with the base, I see some of that potential.
*  I'd love to hear like use cases that you see
*  for these kind of one-off single use applications,
*  maybe how that kind of compares to the example you showed
*  where it was like setting up an automation
*  because that's not a single use, right?
*  That's like an ongoing thing.
*  And then I also really wanna kind of get into
*  the sort of consumer versus business paradigm
*  here a little bit.
*  And just thinking about that, I kind of wonder like,
*  is this something you think individuals will use
*  kind of on an ad hoc basis and do whatever they need to do?
*  Or do you see this getting into business
*  and kind of becoming part of process as well?
*  Lot there, so take your time.
*  The first ones that Lindy does very well
*  is anything that you would give to an executive assistant.
*  So the few very big ones are gonna be emailing,
*  calendaring, contract sending, prospecting, recruiting.
*  So emailing, for example,
*  when you wake up in the morning with Lindy,
*  you open your inbox and Lindy triages your emails for you.
*  She tells you, hey, those emails are like really important
*  for you to look at right now.
*  And she pre-drafts replies to the emails
*  based on not only your voice,
*  but your voice for that particular recipient.
*  So she learns how you speak to each person.
*  You probably don't speak the same way to your wife
*  as you do to investors, hopefully.
*  And so she's going to draft the email.
*  And so you open your inbox in the morning,
*  the emails are pre-drafted and you can review them.
*  You can edit them if needed,
*  and then you can send them away.
*  So that's one example.
*  Calendaring, she can manage your entire calendars.
*  And you can be like, again, find me time with Nathan.
*  She can handle conflicts automatically.
*  She handles arbitrary preferences.
*  So I can be like, hey, I don't want any meeting on Friday.
*  So I don't want any meeting before 11 a.m.
*  That's my focus time.
*  And she's going to respect the preferences.
*  So those are some of the very big use cases
*  that it handles quite well right now.
*  It's basically replacing an executive assistant
*  for a lot of people.
*  Regarding the consumer and professional thing.
*  Look, I think we're basically seeing
*  a new type of computing.
*  I think of this as the next operating system.
*  And it's funny, it's actually an inverse operating system
*  because normally an operating system
*  leaves on top of your hardware
*  underneath your applications and data.
*  This leaves on top of your applications and data.
*  And so you just start using this
*  instead of using a lot of your applications and data.
*  And it just patches together all of your applications
*  and data to do the work that you want to do.
*  So at the end of the day, I think this is just how people,
*  regardless of whether they're consumers or professionals,
*  I think this is just how people are going to use
*  their computers moving forward.
*  I think that the computing experience of the future
*  is not you doing work on a computer.
*  It is you having a conversation with your computer.
*  And since the computer works with you to do the work
*  or even does the work for you.
*  Yeah, that certainly is the dream.
*  And it seems like it's becoming a possibility
*  rather than just a dream extremely quickly.
*  Could you tell us a little bit about
*  how you decided that this was the moment
*  to pursue this dream?
*  I mean, in some sense, this goes back to the Jetsons, right?
*  Or like kind of post-war science fiction,
*  or even to some degree,
*  like wartime pre-war science fiction.
*  And it's always been kind of like one day,
*  maybe we could achieve this.
*  It seems like now, again,
*  like everybody's kind of got the sense
*  that this is coming into focus.
*  What gave you the confidence to set out to build a product?
*  And how are you thinking about this moment that we're in
*  where presumably you're going to see a pretty healthy
*  amount of competition from other startups,
*  but even more so probably like,
*  there's rumors of a new Siri, Google Assistant,
*  is going to get a lot smarter.
*  We have to imagine.
*  So how are you seeing your place in the landscape
*  and the kind of opportunity to carve out a niche
*  for yourselves with this business?
*  So how I decided now was the time,
*  I mean, I feel like,
*  and perhaps the audience knows that as well,
*  like it's very obvious, right?
*  When you're close to it, it's so obvious
*  that like there is something unprecedented
*  going on right now in AI.
*  I have been following AI.
*  I think I started to follow it up close
*  more than 10 years ago.
*  Like the image that moment sucked me in,
*  like for a lot of people like CNNs and RNNs started to work.
*  And I, at the time I was a software engineer
*  and I followed some AI courses on Coursera.
*  And it was super exciting,
*  but I couldn't come up with killer use cases back then.
*  And I kept following along and I actually got really excited
*  and I almost started a startup in this field
*  when GPT-2 came about.
*  And I wanted to start something in enterprise,
*  so GPT-2, I played around a little bit with it.
*  I did some experiments and still it didn't feel quite ready just yet.
*  And then GPT-3 came about,
*  ChetGPT came about very recently.
*  And when you start playing with these products,
*  you get very good results very quickly.
*  And then you're like, okay, now is the time when actually
*  this is starting to become very viable.
*  Regarding the competition, I'll say a few things.
*  One, I don't think too much about the competition.
*  I have so many minutes in the day,
*  so I try to spend them thinking about my customers
*  and not too much about my competitors.
*  I think it's Jeff Bezos who said,
*  your competitors aren't giving you any money anyway.
*  So why think about them?
*  I also think it's going to be such a huge market
*  that it's just going to be the model of all markets.
*  I think there's going to be many winners into this space.
*  I also think the Google Assistant and Series,
*  generally one handicap that these incumbents have is speed.
*  I think it's Reid Hoffman who said,
*  we are driving at night on uncertain terrain,
*  it is the fog and no one can see very far along.
*  And no one is exactly strong in that kind of environment,
*  but I think that huge companies are even less strong.
*  I think startups thrive
*  in this kind of chaotic environment.
*  So I think startups are going to have an advantage here
*  structurally to play in this kind of environment.
*  How do you think that plays out in practice?
*  Like, are there obviously the speed factor
*  and just kind of the willingness to ship
*  without a million sign-offs and all that?
*  Everybody's familiar, I think, probably with those dynamics.
*  Do you see specific features or use cases
*  or kind of paradigms that you think you
*  or startups in general are better able to embrace
*  as compared to say a Siri or a Google Assistant?
*  Yes, I think so to go back to your question earlier
*  about customer or professional.
*  Although I see this eventually as a universal new kind
*  of computing paradigm, right now we are focused on
*  the sort of again, executive assistant use case
*  for busy professionals.
*  You have too much to do, you have too little time,
*  too many meetings on your calendar,
*  we help you put order into this chaos.
*  That is something that Google Assistant or Siri or Alexa
*  can't do, they are consumer products.
*  And these companies are so huge
*  that they have to cater to a universal audience
*  from day one, right?
*  It's the same reason why, look, Apple has FaceTime
*  and they've actually been fleshing it out.
*  Now you can send FaceTime links in your calendar invites
*  and all of that stuff, but Zoom is still a formidable company
*  because they are focused on the B2B professional use case,
*  which Apple structurally cannot go after.
*  Yeah, I think that is one example of an instance
*  where startups will have an advantage.
*  It's not one specific use case,
*  it's more the ability to focus on any use case,
*  just as having to cast such a wide net.
*  I think that's one.
*  Yes, to your point like the bureaucracy
*  and the legal rounds of review inside companies
*  are another thing.
*  I also think generally, yeah, startups can be more nimble,
*  they can change direction, they can make more experiments
*  and they can take more risks.
*  You can just allow yourself to release a product
*  that is slightly more rough,
*  where on the edges slightly less ready
*  and you don't risk what happened to Google
*  where it's like they released it or they announced it
*  and there were issues and they lost billions of dollars
*  of market cap overnight.
*  That's not a risk for you as a startup.
*  So let's talk a little bit about how it all works.
*  I mean, you've given us a little bit of insight into that,
*  but I'd love to kind of understand one of the big themes
*  that we've heard in talking to different entrepreneurs
*  and builders is this kind of constant advancement
*  of the model and there's then also the question of
*  how do we think about using like the best available model,
*  which right now is pretty clearly GPT-4.
*  I need to spend a little more time with Claude V1.2 as well,
*  but I think it's safe to say GPT-4 is ahead for the moment.
*  So it can do more and more stuff.
*  Then you may also think, geez, that could be expensive
*  or there may be some things that it can't do
*  that we need to train our own models to do.
*  So we may have sort of a mix of models.
*  So I'd love to hear kind of your thoughts
*  on the mix of models first.
*  And then I also want to talk about like memory
*  and client profiles, but we'll come back to that.
*  So tell me first, how are you thinking about
*  what models to use?
*  Is it a mix?
*  Are you training your own?
*  The criteria we use here to make the decisions
*  or the quality of the responses,
*  that's our single only criteria.
*  And I really insist on the single only criteria.
*  We don't care about the cost, for example.
*  So right now that's the guidance I've given as a team.
*  It's like, ah, like GPT-4 is so expensive.
*  And I'm like, I don't want to have this conversation.
*  We're not talking about costs in this room.
*  Right now, let's, because most lies on your side.
*  I think the cost of these models has been divided
*  by 20 over the last year.
*  Like this is not a problem.
*  So right now, Lindy is costing us a pretty penny
*  to serve the customers.
*  It's dozens of dollars per month per customer.
*  And that's just okay with me.
*  I don't really care about that just yet.
*  With that said, so right now, yes, GPT-4 is head
*  and shoulders about everyone else.
*  And we've tried pretty much everything out there.
*  But it is often surprising to people
*  to what extent you can actually get better results than GPT,
*  at least GPT-3.5 on at least one narrow use case.
*  If you build your own model based on that one use case.
*  To your point, I think the landscape is changing
*  super rapidly right now.
*  And so what we've had to build is we've had to build
*  the infrastructure to be model agnostic
*  and be able to swap out the model super quickly
*  and retrain new models very quickly
*  once a new open source option out there starts working.
*  Right now we mostly run on GPT-4,
*  but we also all building and fine tuning our own models.
*  And they are getting better very rapidly on our benchmarks.
*  And so eventually I think we're gonna have a mix of GPT-4
*  and our own model.
*  And again, purely for quality reasons.
*  So we have a ton of data that we have collected
*  through a lot of means.
*  And we're using that data to fine tune our own model.
*  And that actually makes it almost as good
*  and I think soon better than GPT-4 again
*  for our one specific use case.
*  I think what you said there about not caring about cost
*  right now is definitely, seems to be a trend
*  and is definitely one that I subscribe to as well.
*  It is crazy to think that just six months ago,
*  I believe it was August of last year,
*  was when the cost of like the mainline models
*  dropped from six cents a thousand to two cents
*  a thousand tokens.
*  Then they dropped that further down to 0.2 cents
*  per thousand tokens and then reintroduced,
*  higher price point with GPT-4.
*  That difference is a, right now it's a basically a 20X,
*  the structure being a little bit different
*  where GPT-4 has a different price for input tokens
*  versus output.
*  But it is interesting to hear that basically,
*  yeah, just pay up for the 20X difference.
*  All we care about is quality and we kind of have enough faith
*  in price drops continuing slash our own ability
*  to engineer stuff that it will resolve itself over time.
*  I do think that makes a lot of sense,
*  but it does take some conviction about a view,
*  point of view of where the world is going.
*  And conviction and money.
*  But it's not a tough decision to make really.
*  It's, I mean, it's, when you look at that curve,
*  it's so smoothly going down.
*  And so it's never bet against Moore's Law
*  and here it's even more than Moore's Law.
*  It's an order of magnitude even faster than Moore's Law.
*  So the question really, and that's a little bit
*  of a mouthful, but does cheap get better faster
*  than good gets cheaper?
*  I will bet, and so far history has always proven that out
*  is that good gets cheap very fast
*  and cheap doesn't necessarily become good.
*  Yeah, that's interesting.
*  So how much easier has GPT-4 made your life
*  in building this product relative to 3.5?
*  A lot easier.
*  It's pretty shocking the improvement.
*  I think the bigger context window alone is a huge deal.
*  You used to have to hack your way around the context window
*  and summarize and embed and fine tune
*  and do a bunch of crap to not have to deal
*  with the context window.
*  And the context window is still a constraint
*  but much less of one.
*  It's really not something you have to worry
*  about nearly as much.
*  So that alone is a game changer.
*  You also need to do a lot less prompt engineering for GPT-4.
*  GPT-3 and GPT-3.5, you had to coerce them
*  into giving you the output that you expected.
*  And so lots of prompt engineering is like,
*  you are like a smart assistant.
*  You don't want to do XYZ.
*  GPT-4 works out of the box a lot more often.
*  It works full shot.
*  You just ask me to do something
*  with zero prompt engineering around it
*  and it just works a lot more often.
*  So it's made a pretty dramatic difference.
*  I would say the only downside so far of GPT-4
*  has been the speed of it or lack thereof.
*  It's pretty slow.
*  The generation is quite slow.
*  And so you may have noticed during the demo just now,
*  it takes a few seconds for it to answer.
*  Oh, well, it's not the end of the world
*  because the way we think about it is like,
*  even if the model takes 30 seconds to answer,
*  which it doesn't, even if it took 30 seconds,
*  that would still be way faster
*  than a human executive assistant.
*  So I think that in a lot of ways,
*  the product is superhuman as an executive assistant
*  out of the box.
*  It's available 24 seven
*  and it then stills in like 10 seconds or less.
*  Yeah, so one of the things I think in many respects
*  that is gonna undeniably be true,
*  for one thing, there just aren't that many
*  executive assistants out there that know how to code.
*  Although they can increasingly figure that out
*  with GPT-4 as well, perhaps.
*  But one thing that a human teammate is going to do
*  that I think you're also working toward,
*  but it's not quite clear to me
*  exactly how you'll accomplish it yet
*  is really getting to know you over time
*  and knowing your tendencies, preferences.
*  You mentioned kind of relationships
*  and talking to different people in your life
*  in a somewhat different way, a different voice.
*  What I see out there in the world right now
*  is kind of the default paradigm would be like,
*  we embed all your stuff and then at runtime,
*  when you ask for something,
*  we kind of translate that to a database query
*  against the embeddings.
*  And then we pull out stuff and rank,
*  and then we take whatever kind of pops up
*  to the top of that ranking and stuff that
*  into the context window for the language model
*  to kind of use that information
*  to inform what it's gonna do.
*  And I think that makes a lot of sense,
*  certainly for things where I have like just tons
*  of content sitting around,
*  or for companies who have like internal
*  knowledge management systems already
*  that they might wanna layer a chat onto
*  that makes a ton of sense.
*  Are you doing that?
*  Or it sounds like you may be doing something
*  a little bit different,
*  because you said like the model writes code to search.
*  It sounded like you were talking about
*  like just searching my Gmail directly, for example.
*  So how do you think about kind of ingesting
*  all this content, embedding it,
*  trying to have a semantic search
*  versus using like the many search APIs that exist,
*  or maybe it's a combination of both?
*  So we do a mix of three things.
*  There's basically, there's two kinds of things
*  that the model needs.
*  It needs your preferences and it needs your data.
*  And we do three things to get those.
*  So for the preferences, it's funny actually,
*  this is an example of a time when GPT-4's context window
*  really helped, because at first we were like,
*  oh, let's do what you just described.
*  Like let's encode your preferences in a vector database,
*  and it put them when you give something,
*  it's like, hey, like, help me find time with this.
*  And then vector self against your preferences.
*  They said, don't find time on Fridays.
*  And so I'm going to inject that into the context window.
*  And then we took a step back and we were like,
*  wait a minute, you guys,
*  like 32,000 tokens context window?
*  Like how many preferences do people have?
*  Like you're not gonna have like 30 pages of preferences
*  to give to your assistant.
*  Like, let's just stuff all of that up in the context window
*  and we'll deal with all of that later
*  once you really have too many.
*  And that works really well.
*  So that's the, that covers the preferences.
*  Then the two other things we do all for your data.
*  So for example, if I go like write an email to Bob
*  about this report that I just wrote in Google Doc
*  or whatnot, there's two ways that Lindy
*  is going to pull this data.
*  One is using what we call a context injector
*  that leaves upstream of the code generation model.
*  So the context injector takes a prompt from the user
*  and tries to figure out what questions it needs to answer.
*  What context does it need to fulfill this prompt
*  and where can it find this context?
*  And then it pulls this context from these sources
*  and injects them into the prompt.
*  So it sorts of hydrates the prompt.
*  So for example, if I go like send an email to John,
*  suppose I literally just say that, send an email to John,
*  the context injector is gonna go like, who's John?
*  Like, so that's the first question, who's John, right?
*  How am I going to find that out?
*  It's like, okay, like I have all of these sources
*  of information, I have his contact, I have his calendar,
*  I have his email, and I'm gonna use a mix of all of these
*  to find out who John is most likely.
*  And so if I always work with the same John day in, day out
*  and email him, he's gonna be like, okay, this is John.
*  So that's the context injector.
*  And then even without the context injector,
*  the last thing we do is that the code generation model,
*  yes, is also able to write code
*  to pull this context at runtime.
*  So if I say again, write an email to John
*  following this Google Doc, the Google Doc thing
*  is probably gonna be handled at the code generation phase,
*  and the code is gonna be like, hey, I'm gonna hit up
*  the Google Doc API, pull this Google Doc, summarize it,
*  and then send an email to John about it.
*  So that's the last part of how we inject this context.
*  And then do I imagine correctly also
*  that you're kind of building your own profile
*  of each user that kind of lives in its own place,
*  like in your database that didn't exist otherwise?
*  Yes, so we connect to all the sources of data
*  that you'll feel comfortable connecting us to.
*  So your email, your meetings, your documents,
*  all of that stuff.
*  And then, yeah, I mean, it basically knows you better
*  than anyone, and it can use all of the data
*  to personalize everything.
*  I wanted to highlight that privacy obviously is one.
*  So we've actually laid out seven constitutional principles
*  and privacy is one of them.
*  It's actually funny, the etymology of the word secretary
*  is secret.
*  So this is a person that can hold your secrets.
*  So we take that super seriously.
*  Lindy never leaks information, and we as a company,
*  or not in the business of selling this information,
*  we will never do ads, for example.
*  What we do is we charge you money for access to Lindy,
*  and so that aligns the incentives quite nicely,
*  and we take the privacy super seriously.
*  Yeah, that'll definitely be an important selling feature
*  to continue to emphasize, I'm sure.
*  The constitutional principles, I also
*  think are really fascinating.
*  I mean, it's kind of a, on some level,
*  it's like a company core values type thing,
*  and that is fairly familiar.
*  But I couldn't help but also call to mind
*  Anthropix recent constitutional AI publication,
*  where they basically spell out a small,
*  I think it was just like two pages worth of guidance for,
*  here's what we want our AI to be,
*  here's how we want it to treat people,
*  we want it to be helpful, honest, harmless.
*  And then they've devised this sort of
*  self-correcting mechanism whereby they're able to use
*  the model to critique its own performance
*  according to its principles and suggest improvements,
*  that ways it might've been better and more in line
*  with its principles.
*  Is that kind of a paradigm that you're developing
*  internally as well?
*  Like how deep does this constitutional concept run?
*  Yeah, 100%.
*  It runs super deep.
*  So we wrote down these principles,
*  we put them on our homepage as a way for everybody
*  to be able to review them and for us
*  to hold ourselves to them.
*  And then we use them at every level of the company.
*  So we use them when we make high-level strategic decisions,
*  is that aligned with our principles?
*  We use them when we make lower level product decisions,
*  like, hey, what do the principles say here?
*  And then, yeah, we use them when we train the AI.
*  So we fine tune the AI on data, we RLHF it,
*  we RLAIF it, and we use these principles
*  to do each of these things.
*  One thing that I thought was really interesting
*  was principle number five, comfort with ambiguity,
*  which has historically been a tough one
*  for any computer system, obviously,
*  with the language models, we're getting a lot of progress
*  coming our way for free, so to speak.
*  But I thought you had some really interesting comments
*  when we were speaking about this,
*  about how you want the tool to be able to do things for you.
*  You really wanna get stuff done,
*  but you also have to be mindful of context
*  and understand how confident are we
*  that we're about to do the right thing?
*  And what would be the cost of making a mistake?
*  Tell me about that part of the paradigm.
*  Definitely.
*  So the image we always use internally
*  about this comfort with ambiguity
*  is we say that Lindy texts a message to Garcia.
*  And taking a message to Garcia, that's an essay,
*  it's like a very famous essay,
*  it's about some rule between the US and Cuba,
*  and there was an American general
*  who wanted to get a message to the head
*  of the Cuban intelligence
*  who was hiding somewhere in the mountains, Garcia.
*  He takes a letter and he goes to the soldier
*  and he hands the letter to him maybe like,
*  take this message to Garcia,
*  and the soldiers asks, who's Garcia?
*  And general takes a letter back,
*  goes to the next soldier,
*  takes this message to Garcia,
*  and the soldier asks, where is Garcia?
*  And then the general takes the message back,
*  goes to the third soldier
*  and goes like, takes this message to Garcia,
*  and the soldier goes, done.
*  That's what we're aiming for.
*  So again, the other concrete example
*  I gave just earlier, applies here, like send an email to John.
*  You don't want your assistant to ask you who John is
*  if you're meeting with John day in, day out.
*  Now, one of the other funding principles is reliability.
*  Like, Lindy doesn't screw up.
*  And so there is a little bit of a tension
*  between reliability and compared with ambiguity.
*  If you take too much initiative,
*  you may screw up from time to time.
*  And so given the choice between both of these principles,
*  reliability always wins.
*  We never sacrifice reliability.
*  And the top heuristic that we use to decide,
*  hey, can you feel comfortable to do this or not?
*  There's two factors that we use.
*  We use perplexity and we use the stakes
*  of the decision that Lindy is making.
*  So the perplexity is, hey, how certain are you
*  that this is the right thing to do?
*  And then the stakes is assuming you screw up,
*  how bad is it?
*  So for example, like I will take the initiative
*  to send an email and fire John.
*  It's like, whoa, whoa, whoa.
*  Assuming this is the wrong thing, how bad is it?
*  It's pretty bad.
*  If you're firing someone,
*  you're not supposed to fire them.
*  It's pretty bad.
*  So we use both of these factors
*  and Lindy uses both of these factors
*  to decide whether to move forward
*  or whether to ask for confirmation.
*  One other heuristic we use generally is,
*  is the action that you're taking read only
*  or is it read right?
*  Like read only action is like,
*  I'm going to go ahead and search his email.
*  Or for example, if I go like,
*  hey, find me a way, I'm moving apartments right now
*  and I have cats, but I'm moving.
*  And so I would ask Lindy,
*  find me a way to move these cats.
*  And like, you know, I'm going to take a plane,
*  like what are the requirements?
*  Lindy could also go like,
*  I'm also going to research online options
*  for cat moving companies, right?
*  So like there's no risk involved in that.
*  Read right actions.
*  Oh, I'm going to send an email on your behalf.
*  I'm going to make a purchase.
*  I'm going to do all of that stuff.
*  For read right, basically Lindy always asks
*  for full confirmation.
*  Interesting. Okay.
*  So I was going to ask first of all,
*  about just the confidence when it comes to moving forward
*  on a particular action.
*  Is that something I had,
*  I haven't actually had a chance to dig into this yet,
*  but I had heard somebody say that with GPT-4,
*  OpenAI was no longer returning the log probs for,
*  like the top, you know,
*  historically they've returned the log probs
*  for like the top five most likely tokens at least.
*  So you could kind of see what the, you know,
*  the leading options were via the API.
*  That's how I would assume you would do something like this,
*  assuming you're using GPT-4,
*  but I had heard that that function
*  maybe wasn't there anymore.
*  So do I have that wrong or is there another strategy
*  that you're able to use?
*  No, that's right.
*  That is another downside of using GPT-4 for us.
*  My hypothesis is that OpenAI is removing this
*  in order to remove the ability of competitors
*  to distill their models.
*  Cause you can use this perplexity to actually
*  kind of build your own GPT-4 out of GPT-4.
*  And I don't think OpenAI is too happy about that.
*  It sucks though.
*  Well, our kind of use case,
*  it really sucks that we don't have access
*  to this information anymore.
*  And that's another reason why we are looking
*  into building our own model.
*  Yeah.
*  So for the moment,
*  what else do you have available to you
*  in the absence of the log probabilities?
*  Well, we've trained another complexity model.
*  Just takes a prompt as input and the context
*  the action that you're about to perform as output
*  and tries to figure out like,
*  hey, like does this really follow that with high certainty?
*  And we're training that model right now.
*  Gotcha.
*  Okay, cool.
*  That's interesting.
*  And then on the action side,
*  the main approach is just to present the action
*  to the user for confirmation,
*  which is, it makes a ton of sense, obviously.
*  Do you think there's potential there also
*  for like a sort of ensemble of models
*  where like, it sounds like similar to the,
*  the perplexity side,
*  I could imagine you having kind of a,
*  good judgment model that comes in and says,
*  is this a good idea or should I hit the brakes
*  before the kind of more base action model does its thing?
*  Yes and no.
*  We do compose models together,
*  but all right, there are agents and workflows together,
*  but that's perplexity and that guardrails is,
*  yeah, it's just something that's present
*  every step of the way.
*  It's just like, we constantly apply guardrails
*  and we have many of them.
*  And again, not screwing up and reliability
*  is one of our top priorities.
*  We do though, again, we do compose models and workflows,
*  which I think in a really cool way.
*  So for example, you can go like,
*  hey, when I ask you to send a contract,
*  I want you to do that via DocuSign,
*  because there's like a bunch of alternatives out there.
*  So go to DocuSign, generate the contract,
*  I have templates and then send them by email.
*  That's what I mean by send a contract.
*  So now I can be like, hey, send an NDA to Bob, right?
*  And then I can go like, hey,
*  when I ask you to onboard a vendor,
*  what I want you to do first is send them an NDA, right?
*  And so basically is that onboard a vendor workflow
*  now uses another sub workflow, which is send a contract.
*  And you can end up building an entire constellation
*  of workflows like that.
*  Very interesting.
*  So how, kind of two-part question then next,
*  how far do you trust this today?
*  Like, would you say go book me a flight
*  and just be confident you're gonna get,
*  you know, a flight that's gonna satisfy your need?
*  You know, what kind of percent hit rate
*  do you think you would have on something like that?
*  And what about actions that kind of can't be taken via API?
*  I actually don't know if you could like,
*  no, you can search for flights via an API,
*  but can you buy a flight via an API?
*  And you know, whether you can or can't,
*  what happens when you need to like execute
*  a transaction online that you just can't do with,
*  you know, kind of generated code?
*  I trust it quite a bit because I think we are doing
*  a pretty good job with the guardrails.
*  And it's asking me for confirmation before doing anything.
*  And it's doing a pretty good job
*  at taking my preferences into account.
*  So yes, I do trust it to like book flights.
*  Hey, Miami to SFO is going to send me options.
*  I'm gonna be like option two,
*  and then this is going to take care of everything else for me.
*  That's amazing.
*  The API thing, first of all,
*  you would be shocked to see how much you can do via API.
*  You can really do most things.
*  From time to time,
*  we will run into something that you cannot do.
*  And we all building that's not available quite yet,
*  but we're working on that.
*  We are building also a web browsing agent.
*  So we all gonna have that full back where it's like,
*  hey, if you need to use the web and not an API,
*  you will be able to do that.
*  And we'll making fast progress on that as well.
*  You showed a little bit of the product
*  and the user experience earlier.
*  How do you think that evolves?
*  Does it kind of stay like a single text box
*  that you can kind of interact with anywhere?
*  Or what is the, are we going full her here?
*  Or what do you kind of envision
*  my procedural daily use of this tool being over time?
*  Yeah, I think it's going to be,
*  I think it's going to have a lot of front ends
*  and a lot of incarnations.
*  And we actually view it as one of our key reasons to exist
*  as a company to build these front ends.
*  We basically want to be to large language models
*  as the PC was to the CPU, right?
*  It's like, look, like the PhDs did it.
*  Like they give us this amazing thing
*  that works really well.
*  It is not an end product.
*  It's a miracle really that large language models
*  are so usable today with just a text field,
*  but they can go so much further than that.
*  If you give them, if you package them up,
*  you give them access to the right tools,
*  the right applications, the right data,
*  and you give them the right front ends.
*  So yeah, we don't think of ourselves
*  as building a text box.
*  We think of ourselves as building that holistic product
*  with all of these front ends.
*  So yes, you will be able to send it emails,
*  talk to it on Slack, invite it to your meetings,
*  send it voice emails.
*  Eventually we do want you to be able to give it a phone call
*  and it will actually respond to you.
*  So to answer your question, it will, yeah,
*  it will do all of these things for you.
*  You don't have to answer this question,
*  but just calling back one of our earlier episodes
*  that we did with the founder and CEO of Replica,
*  what's your stance on erotic role play with Lindy?
*  That's not a cool job to be done.
*  We'll have to, we'll maybe see what jail breaks
*  your early users might be able to pull out of it.
*  In all seriousness, you do lean on the safety work
*  that OpenAI has done under the hood.
*  It'll be interesting to see too how people choose
*  to use something like an OpenAI,
*  which for all the jail breaks and whatnot
*  that we have seen online, they've done a lot
*  to bring it under control and have made a ton of progress
*  versus just this last week also,
*  we had the sort of llama release from Facebook
*  and then the alpaca fine tuning of that
*  coming out of Stanford.
*  And then there was this brief moment where it was like,
*  oh, it's just like text of NG003.
*  And then it was like, oh no, it's not.
*  We're taking it down based on feedback from the community
*  of like problematic uses.
*  I don't know if there's a question there,
*  but I wonder about the degree to which training
*  your own models opens up like a whole can of worms
*  in terms of safety and edge cases and just blind spots
*  that you maybe don't have to worry about as much
*  if you use such a well-established provider.
*  Any thoughts on that?
*  It does open that kind of windows.
*  And to me, that's like a whole other broader conversation
*  around AI safety, which is like, look,
*  I'm very happy that OpenAI is taking safety seriously enough
*  though even them, they can't really stop jail breaks
*  from happening and they happen all the time.
*  And even if OpenAI was doing a perfect job,
*  which they are not, you can't really stop other people
*  from building their own models.
*  And so whether we want it or not,
*  we are gonna have these models out there
*  and we are gonna have them do basically anything
*  any human wants.
*  So I do think that is something we're gonna have
*  to grapple with as a society.
*  Yeah, no doubt it's coming at us quick.
*  Other things obviously that we're gonna be grappling with
*  in the wake of GVG4, OpenAI along with a professor
*  from Penn and another researcher, I believe
*  from Open Research published a study
*  of the anticipated labor market impacts
*  of large language model technology.
*  You can kind of read their charts and estimates
*  in a few different ways, but to me,
*  one big bottom line is that it seems like
*  they're kind of setting a lower bound
*  of like 25% of all work is kind of what they
*  would seem to suggest as like the minimum amount of work
*  that language models could ultimately take on,
*  especially as they're equipped
*  with all the surrounding tools which you are building.
*  So I'd love to hear maybe your thoughts first of all
*  on like how do you assess that report?
*  Does that like 25% number seem like low, high?
*  And what do you think it's gonna look like for us
*  to adjust to this world where we have virtual employees?
*  As awesome as that sounds, a lot of people are pretty worried
*  about what that's gonna mean for society.
*  I think there's two time horizons, right?
*  There's like the next five years or so
*  and then there's like AGI and ASI, right?
*  AGI and ASI all bets are off.
*  Like I can't comment on that.
*  Like no one knows what's gonna happen.
*  Certainly I think it's gonna be quite disruptive.
*  In the meantime, I'm not too worried about job losses
*  because that's just something people have been worried
*  about forever and I think it's just a failure
*  of imagination for humans to realize like human needs
*  and wants are infinite.
*  And as you free up humans,
*  because now some tasks are automated,
*  you actually free them up to do other things
*  that only them can do.
*  And so look, I think something like 90%
*  of the active population in the early 1900s were farmers.
*  Today it's something like 5%.
*  So it's a huge transformation
*  and there is very low unemployment at least in the US.
*  So not a huge concern.
*  I think it's Mark Andreessen who's very fond of saying,
*  every quarter I believe there's some official numbers
*  that come out with the unemployment numbers.
*  And so it's always like a net number.
*  It's like this quarter, X thousand jobs will last
*  or created, but it's always the net number
*  that makes the headline, but the gross numbers are huge.
*  It's always like millions of jobs created
*  and millions of jobs lost.
*  And then there's like a tiny difference.
*  That's like the net result.
*  And so I think that the bottom line here for me
*  is that economies are a lot more resilient
*  and elastic and dynamic than people realize
*  and they can reconfigure themselves extremely quickly.
*  So I'm not worried about that.
*  Actually, I'm very excited about our growing the GDP by 20%
*  and making people 20, 30, 50% more efficient.
*  So one thing that's not there,
*  I wonder if you have a take on this,
*  is the sort of Kane's vision from 80 years ago
*  or whatever now, where maybe even more,
*  where he famously projected that by this point in history
*  we'd all be working a lot less, right?
*  The idea was supposed to be that we'd enjoy
*  our like material comforts
*  and maybe only have to work a couple hours a day.
*  I think it was like 15 hours a week or something,
*  which was kind of the long range forecast.
*  Obviously nothing like that has happened.
*  It doesn't sound like you foresee that either.
*  Like it sounds like you more see people continuing
*  to work hard for the foreseeable future,
*  but just being more productive
*  because they're able to delegate more stuff to AI.
*  Is that right?
*  No, I think Kane's wasn't too far off.
*  Like it's, I think it was just too early
*  to find to eager in his predictions.
*  But if you look at hours worked per year,
*  per person in the US,
*  it has been going down steadily over the decades.
*  I think we work 30 or 40% fewer hours now
*  than we did a hundred years ago.
*  So no, I think that's also part of the solution.
*  Like at some point, perhaps you reach decreasing returns
*  and perhaps you're like, look, you know,
*  we are actually filling up most of our needs
*  and a lot of people are actually deciding to work less hard
*  in order to have less and just to have more time.
*  I think that is going to be part of the solution.
*  Well, I'm hoping for some of that.
*  It definitely seems like more leisure would be a good thing.
*  And, you know, I'm personally very much looking forward
*  to the era of robot servants,
*  both digital and, you know,
*  potentially even domestic robots and who knows what else too.
*  So I know you're super busy.
*  You've got a launch that you're doing
*  and I appreciate you coming on to talk to us about this.
*  Just a couple of kind of closing questions.
*  One is how do people find you?
*  How do they find the product?
*  Like, how do they sign up?
*  And then, you know, we're going to do a little,
*  as the episode releases, we'll do a little promo online
*  where we can get a couple of people off the wait list
*  and into early access.
*  But just for the general audience,
*  like where do they go to sign up
*  and what do you think the timeline is
*  to really ramp up the user base?
*  So you can go to lindy.ai to sign up to the wait list.
*  Right now it's a very limited private beta,
*  but yeah, any Cognitive Revolution listener,
*  go there and say in the notes of the form
*  that you're coming from Cognitive Revolution
*  and we're going to prioritize you.
*  The timeline is we are onboarding new custom models
*  every week and I think we will reach general availability
*  sometime this year.
*  Sometime this year it could be obviously, you know,
*  next month or it could be nine months from now still.
*  What do you think are like the big things
*  that you need to iron out or the sort of,
*  do you have like a short list of kind of key problems
*  that you need to solve
*  before you can go really wide with this thing?
*  Definitely, I think that the reliability of it
*  is one thing that right now it's working well,
*  but to me it's very similar to self driving
*  where it's like, you know, there's like one fatality
*  every million miles or whatever.
*  So look, you actually need a lot of data.
*  You need like three million miles
*  or maybe I'll pay a factor of like 100 here
*  to know whether you're actually doing a good job.
*  So here it's the same thing.
*  We need a lot of data before we're actually comfortable
*  putting that in the hand of a lot more people.
*  We're also just learning so much and so fast
*  about what people want to use this kind of system for.
*  And so as we're learning, we're adjusting our plans
*  and we want to make sure that we've built and crafted
*  an amazing medical product before we put it in the hands
*  of the general population.
*  What AI tools are making an impact in your life today?
*  Like stuff that anybody can go try,
*  but that you have found yourself going back to?
*  Apart from Lindy, you know, GPT-4,
*  chat GPT are pretty huge for me.
*  The reveal blog post that I'm releasing
*  as part of this announcement was written with GPT-4.
*  I recorded my, I'm not a terrible writer,
*  but I just hate it and it takes me a long time
*  to write one thing.
*  It takes me like four or six hours every time.
*  This time what I did is I just recorded myself
*  and I rambled for like 15 or 20 minutes
*  in the most unstructured way imaginable.
*  And then I transcribed this using whisper
*  and I fed that to GPT-4 with some lightweight guidance
*  on like the style I'm going for,
*  which is colloquial, minimal, simple.
*  And I'm like, write a blog post with this guideline
*  according to that transcript.
*  And it did it almost first shot.
*  And it took me only half an hour to write that blog post
*  instead of six hours.
*  So that's a huge one for me.
*  There's also that, I think there's like YC search
*  or something like that.
*  It's like some people, it's like a Heroku app.
*  It's like some people indexed and embedded
*  all the YC videos and blog posts
*  and now you can search them, which is pretty awesome.
*  So you can be like, how should I think about hiring
*  or how should I think about remote?
*  How should I think about co-working spaces?
*  And you get distilled startup wisdom in like five minutes.
*  So like that one's been pretty awesome.
*  What else do I use these days?
*  I use whisper quite a bit.
*  There is a whisper rap that's called the Mac whisper.
*  And that's the 80 that just think
*  it's a really well-built product.
*  And I use it quite a bit for voice memos
*  and recording myself.
*  Interesting.
*  You're pretty consistent.
*  I mean, whisper is one that hasn't come up a ton
*  but is awesome.
*  But it is interesting.
*  We're in this moment where for all of the insane
*  proliferation of apps and you know, Ben's Bites
*  is dropping dozens per day on people still.
*  In this show, when I have asked people what they use
*  it has been pretty consistent that like the main thing
*  is kind of chat GPT.
*  And there aren't, you know, there's been mention
*  of a number of other things
*  but mostly it's people are like,
*  yeah, mostly use chat GPT.
*  And then, you know, maybe one or two other things as well.
*  So I wonder what ultimately that means.
*  It doesn't seem like it bodes super well
*  for the like first wave of applications anyway.
*  But obviously the second wave, you know
*  the more of the kind of thing that you're building
*  there's just a lot more to it than most of the stuff
*  that we've seen so far.
*  So I do think that will probably change, but I don't know.
*  It is interesting.
*  It doesn't seem like there's maybe that much room
*  for like a thousand AIs in most people's lives.
*  No, I think to your point, and this is one area
*  where AI applications diverge from commonly received
*  startup wisdom.
*  It's that I think a lot of these AI applications
*  are a bit too narrow.
*  So again, it's like why is this still thing?
*  It's like one tool to search YC videos.
*  If you look at product hunt, there's like hundreds
*  of like AI tools coming out every week right now.
*  People don't wanna have to manage hundreds of tools
*  and hundreds of plugins and hundreds of links.
*  Like they want one big tool.
*  And so I think right now chat GPT is the one thing
*  that comes closest to this one big tool.
*  But I think again, tools like Lindy
*  are certainly another attempt to create something
*  that is very broad and general purpose.
*  Is there a limit on what this type of thing can do?
*  You're positioning it for starters as kind of a AI assistant
*  but is it also gonna become like an AI accountant
*  and an AI lawyer for you as well?
*  Is there any limit on how much this thing can do over time?
*  I think of it as like Amazon or Craigslist, right?
*  And like these things are getting unbundled, right?
*  Like Amazon's vision was the everything's tool.
*  We sell everything.
*  But at the end of the day, we're not saying like
*  this is literally going to kill all software, right?
*  Like yeah, there was going to be point solutions
*  for very specific needs, just like Amazon does like,
*  there's also Xelo if you wanna buy a house
*  and there's like platforms if you wanna buy a car
*  and there's platforms if you wanna buy a dress
*  and so like, you know, and furniture.
*  There's like some verticals have like very specific needs
*  and I'm gonna use these verticals when I buy a car
*  or a house or a dress or like some furniture
*  but buy in large for everything else I use Amazon.
*  So that's my mental model here.
*  Lindy is Amazon and sure, you know,
*  like when you're gonna want to prospect,
*  you're gonna use a CRM or like ZoomingFoo and whatnot.
*  But I think people are gonna have one big text field
*  in which they type whatever stuff they wanna get done.
*  Okay, here's a hypothetical question.
*  Let's imagine in a world not too long from now,
*  a million people already have the Neuralink implant
*  in their skulls.
*  Now, if you get one, you will be able to think
*  and communicate directly via your thoughts
*  with Lindy and, you know, the computer in general.
*  You'll have essentially thought to text.
*  Would you be interested in getting one in your own head?
*  Not at first.
*  The privacy and the security issues here are problematic.
*  So I think I would wait a very long time
*  before getting something implanted into my skull.
*  Probably 10 years or more.
*  Yeah, you only have one skull,
*  but answers on that have also been surprisingly varied.
*  There are some early adopters among our previous guests.
*  Okay, last question.
*  You're setting out with a really ambitious vision
*  to build what you hope will be like a big part
*  of our future lives, certainly our computing lives.
*  If you could zoom out even farther than that,
*  what are your kind of greatest hopes for
*  and greatest fears for the next handful of years
*  as AI permeates all parts of society?
*  I do hope we can get people rid of mini-ill work.
*  I think we're seeing so many humans right now.
*  Humans are AGI, right?
*  We're seeing so many humans do work
*  that they shouldn't be doing, that robots should be doing.
*  Like mind-numbing data entry work and stuff like that.
*  And like you shouldn't have to spend time
*  going back and forth to find time.
*  And playing with people's schedules.
*  Like that should be the job of a robot.
*  So I'm very hopeful for that for sure.
*  Any big fears?
*  I think misinformation can become a problem.
*  Mostly I have my side
*  to over the very long-term existential risks.
*  I do believe there is a low,
*  but non-zero percent chance
*  that things go very wrong with AGI.
*  Would you venture any remedies, prescriptions,
*  regulations, guidelines?
*  And do you have any sense for how we can minimize that risk?
*  That's very uncharacteristic of me,
*  but I think we need regulation.
*  We don't trust private sector to self-regulate
*  for basically anything that is touching safety.
*  Airlines are extremely regulated,
*  banks are extremely regulated,
*  buildings, when you build a new house,
*  that's extremely regulated for safety reasons.
*  Is this the same thing with AI?
*  Well, it's gonna be an interesting few years
*  to say the least.
*  And looking forward myself to getting off the waiting list
*  and getting into Lindy.ai,
*  the AI assistant, Flo Crivello, founder and CEO.
*  Thank you very much for being part
*  of the cognitive revolution.
*  Thanks a lot, Nathan.
*  Omniki uses generative AI
*  to enable you to launch hundreds of thousands
*  of ad iterations that actually work,
*  customized across all platforms
*  with a click of a button.
*  I believe in Omniki so much that I invested in it,
*  and I recommend you use it too.
*  Use Cogrev to get a 10% discount.

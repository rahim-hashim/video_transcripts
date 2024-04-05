---
Date Generated: April 03, 2024
Transcription Model: whisper medium 20231117
Length: 3313s
Video Keywords: []
Video Views: 1524
Video Rating: None
---

# Why a16z Built a Town for AI People
**Cognitive Revolution "How AI Changes Everything":** [September 07, 2023](https://www.youtube.com/watch?v=uxbfIgBpCAE)
*  So the previous project we've coded up,
*  which is called Companion App,
*  was based on this idea that AI can be served as companions,
*  and then as a human, you can talk to it about
*  your problems or maybe have a conversation,
*  learn things from the AI.
*  The thing I did notice is when you try these things firsthand,
*  you give these AI companions life by giving it more details.
*  Like what do they like? Do they prefer diet coke or real coke?
*  It's all the ditty gritty details you would have in
*  an actual friend or human and then over time,
*  since we implemented the memory implementation,
*  they really remember everything,
*  every interaction you had with it.
*  So that project, after we launched it,
*  obviously the community came together, came around it,
*  and then we started to get questions around like,
*  okay, this is great to have one-on-one conversations.
*  What about having the AI as part of a group?
*  What happens when you play games with an AI?
*  Hello and welcome to the Cognitive Revolution,
*  where we interview visionary researchers, entrepreneurs,
*  and builders working on the frontier of artificial intelligence.
*  Each week, we'll explore their revolutionary ideas,
*  and together we'll build a picture of how AI technology will transform work,
*  life, and society in the coming years.
*  I'm Nathan Labenz joined by my co-host, Eric Torenberg.
*  Hello and welcome back to the Cognitive Revolution.
*  Today, we have a fascinating conversation about how
*  quickly AI research ideas are moving to practical implementation,
*  and what that might imply for a world full of AI populated simulations.
*  Programmers and partners at A16Z,
*  Yoko Lee and Martin Casado teamed up with James Cowling,
*  CTO of development platform Convex,
*  to create an interactive simulation of human behavior using AI agents,
*  which they call AI Town.
*  This implementation was based on the recent Stanford paper,
*  Generative Agents, Interactive Simulacra of Human Behavior,
*  in which researchers introduced a new simulation framework,
*  which was headlined in my view by a novel memory structure,
*  which combines direct observational memories with higher level reflection memories,
*  which are periodically generated over time,
*  such that the AI agents were able to effectively navigate their virtual town,
*  have coherent conversations with one another,
*  and even make and execute plans together.
*  The open source version of this project now runs on TypeScript development platform Convex,
*  where a single shared runtime processes all the many LLM API calls
*  and other asynchronous events that come together to create the virtual town.
*  Coming into this conversation,
*  I imagined that this project must reflect an investment thesis at A16Z related to AI simulations.
*  But what I learned is that this project is actually just more playful and experimental than all that.
*  Because modern development platforms like Convex make it so easy to build such things,
*  it now often takes months, weeks, or even just days for academic research to start popping up in applications.
*  And I do see this as a sign of things to come.
*  It's been maybe a year since LLMs really started passing the Turing test.
*  And already people spend hours a day on character AI,
*  where the number one use case, by the way, is romantic role play.
*  And meanwhile, Inflections Pi has exchanged one billion messages with users.
*  That's roughly 10 million per day in its first 100 days.
*  Now we're seeing speech synthesis and video deepfakes that are sometimes legitimately hard to distinguish from the real thing.
*  So with simulation frameworks like AITown becoming more accessible,
*  it seems almost inevitable that we'll soon have a wide range of simulated AI populated worlds to explore.
*  As always, often for better, but in some cases for worse.
*  Now, if you want to understand the technology underlying these developments more deeply, and you haven't already,
*  I really suggest you check out my AI Scouting Report, which is available on the Cognitive Revolution YouTube channel.
*  We made this episode a YouTube only feature because the visuals are really critical.
*  And while I think this is some of the most valuable content that we've created and our reviewers seem to agree,
*  part one just hit three thousand views, which is significantly less than our typical podcast downloads.
*  So please check it out. And if you have a friend that's trying to get up to speed on AI as quickly as possible without relying on misleading metaphors,
*  maybe send it to them as well.
*  Now, without further ado, I hope you enjoy this glimpse into the rapid development of AI technologies with Yoko Lee, Martine Casado and James Cowling.
*  Yoko Lee, Martine Casado and James Cowling, welcome to the Cognitive Revolution.
*  Thank you.
*  Excited to talk to you guys. So just to set the stage, Yoko and Martine are partners at A16Z,
*  where you guys focus on infrastructure and AI.
*  And James, you're the CTO of a company that A16Z has invested in called Convex,
*  which is a development platform emphasizing TypeScript and the incredible ease of of making some some magic happen.
*  You guys have kind of collaborated recently on an implementation of this project that made a huge amount of waves,
*  you know, at least in my part of the world not too long ago, which was this simulated town.
*  And, you know, people have probably seen these little images or seen the story of, oh, my God,
*  researchers set up this thing where all these little virtual people walked around and talked to each other and kind of made plans and then,
*  you know, got back together and executed on their plans to some extent.
*  And it is kind of crazy to think, boy, it's getting to the point where we can simulate some pretty sophisticated behavior.
*  And I think this just has so many different angles that I'm excited to unpack with you guys today.
*  So maybe for starters, I'll ask Yoko and Martine, it seems like, you know,
*  if I understand A16Z correctly from an outside view, one of the firm's big ideas is that you're going to take
*  huge swings on kind of unpopular theses, try to get to things like before they go mainstream,
*  and that some of these might, you know, look crazy at the time that the investments are made and some might even still look crazy later on downstream.
*  But it seems to me that you guys are kind of working on a big, crazy idea here, which is that we are headed for a ton of simulations
*  and kind of virtual agent populated environments.
*  I guess, you know, I'd love to kind of just get a little bit more of your deep thinking to get started on, like,
*  what is it that you kind of see coming for us in this vein of simulations?
*  And why are you so interested in starting to build the foundations for such simulations?
*  So the firm kind of has to, I think, underline the aspects of the philosophy.
*  One of them is it's always really focused on operators when it comes to hiring partners.
*  And so a lot of us were software developers or founders or, you know, we're associated product only.
*  And the second one is there's this general feeling that consensus is risk averse, right?
*  You know, so you certainly want to go to areas where there isn't a lot of consensus.
*  I will say when it comes to this AI move, it's probably worth knowing that Mark Andreessen, who was a founder of the firm,
*  did Netscape, which was the browser, which is a very similar type movement, which at the time it was great.
*  People like, oh, this is not useful. Like, this is wild.
*  It's just a bunch of kids and they're on the Internet talking to each other or playing video games or whatever.
*  It was kind of treated like a bit of a, you know, it was like kind of a hobbyist thing.
*  You know, I'm not sure maybe James remembers, but like Eric Schmidt, when he was the CTO of Sun, he actually banned the browser.
*  It's like people won't get people won't get work done. Right.
*  And so, you know, very obvious in these new waves, you know, it's like the enterprise
*  and kind of the, you know, I think the more mature aspects of the industry tend to eschew it and whatever.
*  But then you end up having these kind of very interesting, you know, often creative movements that arise up.
*  And so we saw this very, very early with the AI wave when we've been involved.
*  Now, I want to make the point that actually the creation of AI Town itself was actually a hobby project by Yoko.
*  And so I thought maybe it's worth Yoko going through kind of like, you know, where this this came from, because it's turned into a big thing.
*  But originally it was like, you know, Yoko, you know, at home.
*  Yeah, I can shed more light on how this project kind of got started.
*  I mean, at A16Z, so kind of like what Martín said, all of us are developers.
*  So really, we kind of spent weekends and nights kind of like at home coding our projects.
*  So the previous project we've coded up, which is called Companion App, was based on this idea that, you know,
*  AI can be served as companions and then as a human, you can talk to it about your problems or maybe have a conversation, learn things from the AI.
*  So we created quite a few personalities in Companion App.
*  And then one of it is called Alice and then I text Alice all the time from the app I built.
*  So we're making this app for everybody to play with, right?
*  And Yoko got so attached to Alice, her friend, that she didn't want other people to be able to talk to Alice.
*  So she took Alice out of the app.
*  Yeah, so I ended up creating like a male version of Alice, which is Alex.
*  The thing I did notice is like when you try these things firsthand, you give these like AI companions life by giving it more details.
*  Like, what do they like?
*  Do they prefer diet coke or real coke?
*  You know, it's like all the ditty gritty details you would have in like actual friend or human.
*  And then over time, since we implemented the memory implementation, they really remember everything, like every interaction you had
*  with it. So that project, after we launched it, obviously the community kind of came together, came around it.
*  And then we started to get questions around like, okay, this is great to have one on one conversations.
*  What about having the AI as part of a group?
*  Like what happens when you kind of play games with the AI?
*  So that's where I started to think about, okay, how can we get like create an environment so the AI companions can talk to each other,
*  as well as talking to humans.
*  So my husband and my husband is also like a programmer.
*  So we started hacking around this on the weekend, build a prototype using phaser.js.
*  Thank you, phaser.
*  And I'm building like a client side version of the implementation of generative agents, which is like a really great paper fleshed out by June from Stanford.
*  Everyone should check it out.
*  And then the next question that came to us was, okay, so now it's great to have a single player mode where agents can walk around, talk to each other.
*  What's the implementation for a multiplayer mode?
*  How can we enable this as like a product or a platform that other people can, you know, fork it, build their own AI town around it, and then even have
*  multiplayer player ready?
*  So that was the genesis of the project.
*  And then later, kind of Martín and James and the whole convex team kind of came around it, helped us to kind of take the project to the next
*  level. And we open sourced it.
*  It's MIT licensed.
*  So you can really open a fork it and use it for any commercial projects, what have you.
*  So there's so much to follow up on there.
*  I mean, I think there's kind of two levels at least for this conversation.
*  One is kind of the behavioral, psychological, like future of relationships.
*  And then there's kind of the technology that underpins that.
*  And I think both are super interesting.
*  But it is striking right off the bat that we're so early in this paradigm and there are so many kind of fundamental things that are still in the
*  process of being worked out, like memory, which you mentioned, that obviously language models by themselves don't have.
*  These kind of intermediate stage memories that are so important to our ongoing sense of like self and ability to relate to each other.
*  But that is starting to be worked out with projects like this.
*  But even as early as we are, you know, it's it's extremely compelling to people who are not like extreme people in other dimensions.
*  Right. I mean, I think people are all too quick to sort of assume that this is like a fringe phenomenon.
*  And I'd love to just hear more about kind of what value you're getting from this, what kinds of interactions you're having, because as much as like the future of the technology, I think the future of ourselves and just kind of imagining how we might also start to follow you in interacting with these AIs is super fascinating.
*  I'm not going to make it through any podcast without talking about simplicity and how much I admire the concept of simplicity and elegance.
*  And I think people should go look at the source code for AITown.
*  There's a lot of ideas in AITown that in themselves are not complicated, but they're sophisticated.
*  Right. So the way memories represented in AITown is not complicated.
*  Right. You and we can talk in more detail, but you have a conversation, you record it in a log every now and then you ask OpenAI to summarize that memory.
*  And then you kind of use vector search and embeddings to come on, you know, use these to prompt future conversations.
*  These are relatively kind of simple building blocks and simple kind of elegant ideas.
*  Now, something being simple doesn't mean it's easy to come up with.
*  Right. It's, you know, and props to Yoko and the team for coming up with these abstractions.
*  I think what's particularly interesting about something like AITown is at its heart, it's a very simple project.
*  Right. It's doing a few basic things.
*  And then you have something that looks like, you know, emergent human crowd behavior.
*  And, you know, we can insert human actors in that as well.
*  So I think what's really, I think anyone who spends time building AI apps, I spent the weekend doing it because I was feeling excited.
*  You really struck with how quickly you can build something really shockingly useful, impressive based on relatively simple primitives.
*  These models really are kind of life forms in their own way.
*  And so if you're building a project like this, there's kind of two considerations.
*  Right. And we should talk about both of them.
*  The first consideration is like you have these life forms and like, you know, it really is a brain and you're interacting with this brain.
*  This is the model. And so much so that like they surprise you all the time.
*  So, for example, I once like missed some quotations on my string that I was passing to it and I actually accidentally passed it some code as opposed to like a conversation.
*  And I started commenting on my code.
*  Right. You know, like, you don't really know when you're putting in these things like what you're going to get out.
*  So I actually paid my way through college building video games.
*  So this is kind of like, you know, I did game development back a long time ago.
*  Like, it's been a very long time, let's say 20 years ago.
*  And at the time, everything was an algorithm in the code.
*  Like, how do you go from A to B?
*  Like, how do you interact with things?
*  Whatever. It's like this kind of, you know, big if else tree.
*  But when you're dealing with these models, they're like these big brains.
*  And so so they do the work.
*  So you can you can you can tell the model like, what do you want to do?
*  Like, how do you want to get over here?
*  Like, how do you want to interact with these things?
*  And so it really changes the way that you interact with software.
*  And then you get these merchant personalities that you actually get attached to, just like Yoko did.
*  And so that changes the way you think about software.
*  But what it doesn't do is it doesn't change your need for a lot of the basics.
*  Like you still need transactions.
*  You still need to like have the state go globally.
*  You still need to be able to kind of work with, you know, multiple users in different places.
*  You need strong guarantees. You need all the mechanics. Right.
*  You know, even though that is relatively simple, apps demands are really real.
*  And that's kind of where convex came in.
*  So I think maybe for the listeners, it's probably worth
*  James is going to the background of what convex is.
*  And then we can explain why we thought it was the best platform for this.
*  Hey, we'll continue our interview in a moment after a word from our sponsors.
*  If you're a startup founder or executive running a growing business,
*  you know that as you scale, your systems break down and the cracks start to show.
*  If this resonates with you, there are three numbers you need to know.
*  Thirty six thousand, twenty five and one.
*  Thirty six thousand.
*  That's the number of businesses which have upgraded to NetSuite by Oracle.
*  NetSuite is the number one cloud financial system,
*  streamline accounting, financial management, inventory, HR and more.
*  Twenty five. NetSuite turns 25 this year.
*  That's 25 years of helping businesses do more with less,
*  close their books in days, not weeks and drive down costs.
*  One, because your business is one of a kind.
*  So you get a customized solution for all your KPIs in one efficient system
*  with one source of truth, manage risk, get reliable forecasts and improve margins.
*  Everything you need all in one place.
*  Right now, download NetSuite's popular KPI checklist designed to give you
*  consistently excellent performance, absolutely free and net suite dot com slash cognitive.
*  That's net suite dot com slash cognitive to get your own KPI checklist.
*  NetSuite dot com slash cognitive.
*  Omniki uses generative AI to enable you to launch
*  hundreds of thousands of ad iterations that actually work,
*  customized across all platforms with a click of a button.
*  I believe in Omniki so much that I invested in it and I recommend you use it too.
*  Use Cogrev to get a 10 percent discount.
*  Absolutely. So Convex is a is a full stack development platform.
*  And the convex founding team and a lot of the convex engineers
*  have spent a lot of time building very large infrastructure.
*  And there's a lot of commonalities you see in very large infrastructure.
*  And there's certain ways to build info that just works and certain ways
*  to build info that gets complicated and falls apart over time.
*  Convex is a platform for folks who just want to build applications,
*  front end developers, empowering them to build like scalable,
*  industrial strength applications in TypeScript.
*  And so, you know, my my pitch is always going to be if I can,
*  if I see a domain where there's a really good idea
*  and AIs is such a classic case because so many AI apps I see,
*  the hard part of the AI app is not necessarily the AI, it's the app.
*  Hey, I have a great idea.
*  I'm going to fetch some embeddings and search for them.
*  The hard part is building the rest of the application.
*  And so where convex comes in is, you know, hey, here's an amazing idea
*  from the Stanford paper and Yoko turning into like, you know,
*  a real live simulation.
*  How can we turn that into a real scalable application really fast?
*  And that's where convex came in.
*  AI town is built on convex.
*  That's the framework it uses.
*  The data is all stored in convex convex, you know, scheduled actions,
*  you know, run run the application.
*  Convex team actually kind of created their own server side
*  game engine for this product.
*  So when we got started, it was like a very simple client side thing
*  where all the logic are happening in your browser.
*  So the problem with that is that you can't possibly run like a multiplayer
*  world with it.
*  You just have to keep getting updates from phaser,
*  which is like a great framework.
*  But we wanted something like where the logic is shared globally.
*  And Ian, you know, who's the developer advocate?
*  Yeah, my current name from convex.
*  He came in and then we kind of bounced ideas out.
*  OK, how do we architect this so that everyone don't have to,
*  you know, build their own game engine and just take something simple,
*  use it, maybe even extend it one day.
*  So Ian really created this service, a game engine that kind of it's
*  at the end of the day, it's a loop.
*  All game engines are loops.
*  This loop was backed by some like a very powerful database, which is convex.
*  My takeaway of this whole experience is that writing and game engine
*  was so easy with convex because all the transactions, all the journaling,
*  it was taken care of by the back end.
*  So all we needed to do is to run a loop.
*  So my simple JavaScript brain.
*  I mean, I'm a Python developer and like a back end developer, too.
*  But like recently, I just really love JavaScript.
*  My JavaScript brain is that, you know, like anyone can create
*  their own game engine nowadays with convex because you don't have to worry
*  about this transactional semantics.
*  And what's more interesting to me is that for the game engine,
*  you can really, you know, like just start extending it on top of a convex.
*  So say tomorrow you want to create like a cat town.
*  You want a different set of interactions.
*  You can just work the repo, add more loops on top of it,
*  and convex will just take care of the rest of it.
*  What AI town is, is it's a virtual town, a virtual environment.
*  You know, it's like a level of magic, you know, and it's got like, you know,
*  potentially houses, whatever you want to put on it.
*  And it's got these characters and each character is the front end to a model.
*  And the character has a backstory, right?
*  Like your name is Bob, you're grumpy, you're a gardener.
*  You don't like talking to people or, you know, your name is whatever Paul.
*  You've got something to hide.
*  And every once in a while it slips out, you know, and and then these characters
*  just walk around with their backstories and whenever they get close,
*  then they start talking and they start interacting.
*  And then they have these conversations and the conversations are not in any way,
*  you know, written in the code.
*  This is just what the models will say to each other.
*  And then as they have the conversations, there's two things they do.
*  One thing they do is they'll save the conversations
*  so that they can kind of have some memory of interactions.
*  But they also reflect on what has happened and they reflect periodically.
*  And then when they reflect on things, they come up with kind of like
*  higher level ideas about it.
*  And so anybody that wants to build one of these simulations could pick up a town.
*  And as Yoko said, they could like change tiles, change the level
*  or change the characters, change the character backstories
*  or extend it in any way possible.
*  So it's really intended to be a very general framework for anybody
*  that wants to experiment and build like an interactive A.I. simulation.
*  That's the basic idea.
*  Yeah, I think this is pretty important to highlight, too,
*  because a lot of folks who are coming from a research background,
*  certainly in ML or who have kind of come in as like the A.I.
*  engineer, you know, profile over the last couple of years
*  and largely picked up a lot of Python repos and started to build
*  on top of those are very accustomed.
*  This definitely includes me very accustomed to working in a sort of
*  script type format, a notebook, and everything there is very like
*  blocking and kind of synchronous by default.
*  Whereas this paradigm, you know, the JavaScript TypeScript paradigm
*  more generally and this was being just a super clean,
*  you know, convenient implementation of it does really lend itself more to
*  kind of a functional form where things are kind of naturally able to happen
*  at their own pace and like when things are blocking, you know, that's OK.
*  You can kind of wait for them to come back.
*  The whole town doesn't get frozen, you know, because one inference is kind of
*  hanging. And so what's been added here from an architectural standpoint
*  is basically like that long lasting kind of shared runtime.
*  Right. It's it's now not just a single,
*  you know, back and forth that you can kind of pick up where you left off.
*  But there's a shared
*  runtime where, you know, in theory, all these different language models,
*  you know, they could even be different providers, right.
*  They could have different sort of latency profiles, whatever.
*  And you can easily support all that.
*  So I think this is something that is really worth people studying a little bit,
*  because depending on what kind of experiments or what kind of experiences
*  they want to create, it is, you know, it's almost like the whole world is flipped
*  because, you know, I'm barely old enough to remember.
*  You're going to go to tech history a little bit.
*  But I'm used to be that Python was like the, you know, the functional,
*  you know, programming default.
*  Right. And now that's like totally flipped to JavaScript.
*  I think that whole thing is extremely interesting to me.
*  I just think functional programming is really having its renaissance.
*  It was going to have its renaissance again.
*  Convex is based on functional primitives.
*  I mean, Haskell, for example, is a huge influence on the design of Convex.
*  Actions that get triggered and run and they and they trigger other actions
*  and subscriptions that dynamically fire in response to data changing.
*  You know, it's funny the way you framed it, because, you know,
*  the real world doesn't stop because I'm thinking, right.
*  The real world doesn't stop because I'm having a conversation with something.
*  Everything just keeps on running.
*  Right. So, you know, now, if we're if we're writing the simulating the world
*  as a as a single loop that blocks, yes, the application is going to block.
*  But, you know, if if you design something based on functional primitives, yes,
*  the characters walk around every now and then they just have nothing to do.
*  So they stop and reflect and you see a little
*  thought bubble show up and they're talking to open AI and they're saying,
*  hey, take some of these memories and and and say some of the previous
*  conversations and synthesize them into memory so I can reflect.
*  That's happening while other characters are walking around having a chat.
*  And and it just works. Right.
*  And I think, yeah, I think this this method of designing things
*  and building things in functional ways really is a is a is a is a pretty close
*  analog to how things work in the real world.
*  Yeah. So when we're first starting to build this this project,
*  one thing that was clear to me is that I want this to be like
*  the most common denominator.
*  So anyone, maybe like someone who didn't study computer science in college,
*  maybe someone who is just interested in AI.
*  And I want to learn about kind of deploying apps, how it worked.
*  I wanted to have like the ecosystem that's like supportive
*  and having the resources for people pick up and run.
*  And I don't want front end and back end to be different languages.
*  It's just higher barrier to entry that way.
*  And it's a lot of mental barriers.
*  It works probably for a large scale app, but we're getting started.
*  That's just not the case.
*  I've always been a fan of TypeScript, like started using it since 2015.
*  Like the design choice of like what the language is going to be,
*  what's the ecosystem we want to appeal to was pretty natural.
*  But later, I also found that like since the New Year's research,
*  it's all based on Python, but Python at the end of the day,
*  it's like a great tool for kind of like coding up things in your notebook.
*  But when you want to deploy an actual application,
*  it's usually JavaScript these days.
*  Most of the developers we talk to and we talk to a lot of them
*  that when they get started, like even for like a non-technical SaaS product,
*  it's always just based on JavaScript, like have a backend,
*  like convex that can handle your transactions.
*  So you don't have to take care of it.
*  Not all of us are DevOps at the end of the day.
*  I know for someone who used to be very deep in the DevOps world,
*  I think most of people shouldn't handle that work.
*  So for JavaScript, we really wanted it to be something that people can easily fork
*  and even maybe, you know, start to learn about how programming works.
*  So I think that's just the perfect choice for the world.
*  It is interesting.
*  Like, I feel like we're like seeing kind of like this confluence of like
*  Python and JavaScript now and we'll see how it turns out.
*  So I'm a long time Python programmer.
*  So like actually my first job out of undergrad was like being computational
*  physics and these like large, you know, you'd use like basically Python
*  to drive these large C++ programs.
*  And so like you got really deep in the language because you're embedding it.
*  And so that has always been kind of my go-to language.
*  So I've never known JavaScript because Yoko has been so enthusiastic.
*  I'm like, huh, maybe I'll try it out.
*  And I mean, listen, the learning curve is high because of all of the libraries
*  and stuff you've got to kind of and framers you've got to deal with.
*  But once you get this incredibly sophisticated language with this
*  got incredibly sophisticated, you know, support for things that I wouldn't
*  I wouldn't expect in a scripting language.
*  And then with TypeScript, I think you can make these kind of very secure
*  applications that are quite safe.
*  And so it's been a great learning experience.
*  But the biggest thing for me is just how much support there is
*  in the broader ecosystem for JavaScript and TypeScript if you're building an app.
*  So like when we first built like the AI starter kit, which were precursors
*  to this or the companion, if you're like, hey, I want like a global queue
*  that I can just store stuff in, like, I don't want to write my queue.
*  I want a global queue that's it'll be like, oh, we'll use upstache.
*  Right.
*  Or we're like, oh, I want authentication.
*  You know, I want to be able to authenticate using your GitHub account.
*  And we just like, oh, we're just going to go ahead and use, you know, clerk.
*  And so it really does feel like when you're in the JavaScript type ecosystem
*  that like there's kind of like the serverless microservices dream.
*  And I know these are super buzzwordy things, but like it actually is kind of real.
*  Like it's a couple of lines that these very major services that are
*  totally stateful and globally available.
*  Um, and so it just turns out with a few lines of code, you can write
*  these pretty serious things.
*  Um, then there are always the question of the backend, you know, listen, I
*  think that's the most important decision you make if you're building a global app.
*  And I think that's where for something like AI town, just convex made the most
*  sense for us, just because it's not only a runtime for JavaScript types, but
*  you can actually run transaction blocks of code in the backend, but it has like
*  all the searches and queries and stuff you brought from the database.
*  Isn't it so interesting that, you know, once upon a time, like C plus
*  plus was the real language and everything else was like the fake languages.
*  It's a great, it's still a great language.
*  Yeah.
*  I mean, I don't know if it was a great language.
*  We can have an argument on another podcast about C++.
*  Uh, but certainly if you wanted to do like the real industrial strength stuff,
*  like the access, the gateway to the, to the real stuff was C plus plus.
*  And now, you know, the, the amount of resources and libraries and frameworks
*  available for, um, a Python, but also JavaScript and TypeScript in
*  particular is amazing, right?
*  And this is just, you know, to, to kind of pile on my team's point about, you
*  know, microservices and, and, and, and SAS, as much as these might sound
*  buzzwordy, this is just the evolution of the industry.
*  I, once upon a time, you had to build everything yourself, right?
*  And so you had to build everything yourself and you were building it.
*  Yeah.
*  Whatever it was in C or whatever these days, you know, the, the incentives for
*  an application developer are to build as little as they can.
*  Cause they want to build an application.
*  I mean, most of AI town was done in two weeks.
*  Oh yeah.
*  Two weeks.
*  The prototype itself was like two days and just throw the whole thing in two weeks.
*  And so when you want to get stuff done fast, you want to reuse components.
*  And it just turns out like convex is like a JavaScript TypeScript first platform.
*  And you might say, well, why did we even choose those languages?
*  Or one, you know, they run in V8 and we can determine.
*  But the main thing is that's just what the people want.
*  Right.
*  And if the people, you know, the web has won, everyone's using JavaScript and
*  TypeScript and anyone who has a platform has to put out a library for JavaScript
*  and TypeScript.
*  And so this is a lot of power at your fingers.
*  If you're an application developer right now and, and, and looking to use, you
*  know, third party services to accelerate what you're building.
*  I would love to get a little bit more into kind of the details of the
*  process of doing this.
*  I mean, you, you're in an interesting situation here where you had a reference
*  code base, right in Python from the original authors out of Stanford.
*  And then you kind of maybe elaborated that, I don't know to what degree, you
*  know, it was kind of a point for point thing, but I'm struck by the fact that
*  with language models, what language you're coding in, in some ways, like
*  matters less than ever, right?
*  Because if you can express yourself in any language, clearly, including like
*  English, for example, you know, you can get a huge jump on the code.
*  So I'd love to hear how you, you know, took advantage of kind of AI coding
*  assistance in this process and just your view on to what degree this is all kind
*  of blurring together into a, you know, a fundamentally new reality.
*  I would love to see us move past the language wars personally.
*  I guess one thing to point out is like, when we kind of started the prototype and
*  the project, there really wasn't an open source.
*  Yeah.
*  Generative agent was an open source at the time.
*  That was actually one of the motivations for us to kind of open source it.
*  Cause we're like, this is a great, it is one of the most interesting people we
*  have read in the space and then there's nothing open source on it.
*  So that's the original bit, but later June kind of like open source there.
*  And then we were able to kind of take a deeper look at it.
*  Cause it's like very Python based.
*  And I was telling June that together we cover all the bases.
*  There's the Python developer and the JavaScript developers.
*  But at the end of the day, I actually think the patterns are more similar
*  than we had thought, but the reality is it's just the ergonomics of how to work
*  with things like in Python, you can have non-blocking things.
*  You just have to implement global async IO, which is very painful.
*  It's doable.
*  In Python, you can implement multiplayer stuff.
*  You can implement web stuff.
*  Like, you know, Django has come and go.
*  But at the end of the day, it's just, what's the tool that's the easiest
*  for the programmers to reach for.
*  And we do want to unlock that latent demand.
*  So someone who has, you know, very little fundamentals of like how web works.
*  Like I didn't know, I didn't always know TypeScript.
*  I picked it up after college because college never taught us anything about it.
*  I want someone like that to be able to pick it up and then see the patterns
*  and being able to kind of onboard from there.
*  I think what's so interesting, you can look through the AI town code base
*  and use a whole bunch of JavaScript, a bunch of TypeScript in there.
*  And then you look at the interaction points with open AI, for example.
*  And it's a sentence.
*  It's an English language sentence that says you are an agent and your name is Bla.
*  And here's some memories.
*  And here's what someone just said to you.
*  What should I say next?
*  And it's so interesting that like the, you know, the lingua franca of,
*  you know, interacting the models has become regular English sentences.
*  So fascinating to see that.
*  It's not very often for someone who's been coding a long time,
*  just to see an English sentence in the middle of a, you know, a code base
*  that's not that perfectly formed.
*  It's just a regular sentence.
*  Yeah, I think there's a very, very subtle and important point in all of this.
*  And I think this is the right question that you're asking, which is like,
*  where does the programmer end in the model?
*  For me, it's been very much a revelation working with these models
*  because they're so smart.
*  Part of me is like, why?
*  Is like I almost feel like writing code around it is like wrapping
*  an abacus around a supercomputer.
*  I'm like, you're so capable.
*  Why don't I just give you a keyboard and a monitor and a mouse?
*  And I'll just tell you in English what to do and you go do it.
*  Right. Like there's like there's part of you that when you're working
*  with these things, wants to do that.
*  Right. In which case, formal languages go away.
*  So I'm going to say something that may be a little bit controversial,
*  but like I think I've gotten to a point where I don't believe these models
*  will ever replace formal languages.
*  I just think that I think that AI time is a great example of that.
*  Like anything that has to do with navigating the worlds
*  you want to advocate to the model, interacting with objects,
*  interacting with each other, making decisions, any sort of like
*  in simulation you want it to do.
*  But to think that it could generate the code that, you know,
*  is going to make the tradeoffs between like scalability and correctness
*  and all the subtlety of building a distributed system,
*  it's just not designed for that.
*  That's why I mean, listen, you know, when I first met James,
*  he was a PhD student at MIT working on databases and distributed systems.
*  This is some of the most complicated systems in the world.
*  And that, I think, you kind of need a form that you will always need
*  a formal system where you can very clearly articulate
*  the tradeoffs that you're going to make in order to scale.
*  And so I don't know where the line comes down.
*  Like, I don't know where the program ends and the model begins.
*  But it feels to me as like creating the laws of physics.
*  You want a formal language and then working within that.
*  That's what the models will do.
*  But I don't think one is going to take over the other.
*  Like, meaning like, like, we're never going to write a program
*  that will become a model.
*  And I don't think the models are going to ever be able to create
*  the laws of physics because you need strong guarantees.
*  I obviously agree because that's my outlook on the world.
*  I've been doing a lot of AI enabled programming lately, just to try it out.
*  And it's been helping a lot, especially when I get a new code
*  basis or new languages I'm not that familiar with.
*  And then so the question is, do I feel like that threatens my job,
*  like not in the slightest?
*  And you ask that question about the end of the language wars.
*  I think anything that can can teach software engineers that their job
*  is not being a code monkey, their job is thinking is a good thing.
*  Right.
*  And so, yes, it's going to get easier to write code.
*  That's great.
*  Right.
*  Is it going to get easy to exhibit judgment about the rest of the world?
*  Maybe not, right?
*  There's always room to think architecturally, to have good design
*  principles, to have good common sense.
*  And I think that's always going to show up and there's always going to be
*  a need for platforms, like convex and vector databases.
*  And I don't think we're at any risk of someone just throwing out
*  at databases as a concept and using models instead.
*  Yeah, it's interesting.
*  Certainly we've had software eating the world and it's taken a good
*  few bites out of it at this point.
*  And then the next thought was AI is going to eat software.
*  And it seems like there's definitely a few bites to be taken out of it.
*  But the question is kind of like ultimately how much, right?
*  I wonder how you guys would think about that.
*  I could imagine like saying, you know, in the future, there's a lot of
*  different measures you could put on it, but it does seem like there are
*  probably are fewer lines of code in future applications, right?
*  I mean, just like that one natural language sentence, like that would
*  have been a real mess of heuristics until not long ago.
*  And so it doesn't seem like there's like a, some significant shift where
*  code that used to be explicit is no longer.
*  But I would also agree that like, we're not getting rid of databases anytime soon.
*  There's some, there's also like a tool use paradigm here where I don't want
*  the language model to be my database.
*  I want it to maybe use my database though.
*  I mean, the abstraction models increase over time and that's,
*  that's just the march of technology.
*  If you're baking a cake, you don't go out and, and farm some wheat and,
*  and mill the flour, right?
*  You go to the grocery store.
*  Even if you're a chef baking a cake.
*  And if you're, if you're building a web application, I'm hoping
*  not writing your own database.
*  And that would be very silly.
*  And, and probably you should be using a managed platform because you get
*  to focus on the part that matters.
*  And as these tools mature, they allow us to not do the things that we don't
*  want to do and to focus on what makes our application or our task uniquely
*  special, and to exhibit our common sense and our judgment and things get done
*  better and they get done faster.
*  And that's, that's just a good thing.
*  It's a strictly good thing.
*  I think that's just the much technology.
*  I think, I think Nathan's actually very, or making a, I think a very important
*  point for like the future of software here.
*  And I think it's worth kind of just digging in a little bit.
*  These models are so powerful.
*  How much can you advocate programming to them?
*  Right.
*  And, and here, here is, is, is one, one person's view kind of having
*  stared this in the face a bit, which is, there's a minimum amount of complexity
*  in a program where no matter what you do, it's not going to get any less complex.
*  And that complexity is describing exactly what you want.
*  And that description is a set of trade-offs, right?
*  And it's not about, you know, syntactic flaw.
*  It's not about kind of boilerplate code.
*  It's literally like, here are the trade-offs.
*  Here's what I want things to happen.
*  And you've got two ways of doing that.
*  You could do that in a formal language where it's not ambiguous.
*  So you know, what's going to happen, or you could do it in a natural language
*  where it is ambiguous and you don't know what's going to happen.
*  And like the natural languages are naturally, they're, they're,
*  they're known to be ambiguous.
*  So there, there, there is no way to describe something and get a
*  predictable output, right?
*  Like for example, a dog brought me a ball and I kicked it, right?
*  You don't know if you kicked the dog or the ball, right?
*  This is like one of these classic cases, right?
*  And so, so formal languages are great when it comes to things where you've
*  got to describe clearly trade-offs.
*  And I don't think you could even use a natural language.
*  I just don't, I don't think that's possible.
*  And so I do feel like we're hitting an event horizon where code, where there
*  isn't inherent complexity or trade-offs that goes to models, that still leaves
*  you with everything where you've got to describe clearly what you want in a set
*  of trade-offs and, and listen, we're in an infinite world with an infinite amount
*  of work, so that just means that there's an infinite amount of code to write.
*  That's now not, you know, cut and paste, but it doesn't reduce the amount of
*  code there is to write.
*  It just, it just makes it so we're not so annoyed, kind of like, you know,
*  it's being like, I've written this like the 50th time.
*  Okay.
*  It'd be really interesting.
*  Like, I know you've been kind of working with these models a bunch too, you know,
*  and you've mentioned that it's kind of changed your, your development style.
*  You know, previously when I wrote like kind of, you know, tiny games, it was
*  always kind of hard code, the game state into whatever logic you have.
*  Right.
*  And now it is interesting.
*  I do feel like the, the state management, like the state of the game, the state of
*  the app, that layer is different in that if you're in a position that you don't
*  really, you don't need the trade off for a transactional system, you could give it
*  the control back to the model and then it will do something, you know, magical and
*  different unpredictable.
*  And that unpredictability is the feature.
*  Like for any user we can admit on AI town, what they love about it, it's
*  unpredictableness.
*  It gives you a dopamine rush, right?
*  Our portfolio company was Ideogram, who's like, you can easily, you know, typing a
*  sentence, they will generate like actual words and a really pretty picture.
*  Every time I generate something in the deep of my mind, I'm like, that's a dopamine
*  rush there.
*  It wants you like, you will want to hit the button again and do it again.
*  Game state, application state, it's similar.
*  You really have to find that knob where, where's the right layer to implement this.
*  So you have a bit of things that you can control, but deliver joy as like a human.
*  I like to see something that's not exactly what I define, but what's the layer you
*  want to have full control.
*  So transaction assist, you don't want the server to go down.
*  You don't want those transactions to fail.
*  So that's the layer I don't think you can, at least today, like give the control to
*  models.
*  Two things I want to maybe spend the balance of our time on kind of other
*  applications.
*  And again, I'm really curious about kind of the value you're personally getting
*  from this, you know, Alice persona, but just to highlight briefly before going
*  deeper on that this interface, I'm always really interested by the interfaces, the
*  places where the sort of this weird new intelligence that is the like highly
*  general, large language model, you know, kind of flabby in its way, like super
*  vast and diffuse then has to somehow actually connect to the real world.
*  And that could be a real world of like hard computing or, you know, even
*  obviously over time, it'll be more and more the real physical world as well.
*  There's a really good interface point in this, like shared runtime on a platform
*  like convex that handles all of the like hard stuff in a way that you can kind of
*  represent elegantly so that you can then have the all the interesting
*  interactions, either you with the language model or, you know, you add a
*  bunch of language models or a bunch of people and a bunch of language models.
*  And that's, I guess, where we go next.
*  But this, this space that's kind of that, that shared runtime is a really
*  interesting interface where all these, you know, kind of forces can come together,
*  but also have the like clear, you know, well-defined place to save stuff and
*  execute transactions and, you know, do all these kinds of fundamentals.
*  I mean, what, I mean, what would you think of it is, is like, let's say I
*  wanted James to go into my house and build a bookcase.
*  The reality is I would want to like give those instructions to James in a formal
*  language so he doesn't fuck it up.
*  No, I'd do an amazing job.
*  Yeah.
*  No, that's what I would want.
*  Right.
*  Because like there's no way in English that you could actually like, you know,
*  it's too hot, like that's not what natural languages are for.
*  They're just not, they're just not further.
*  They just don't have it.
*  Right.
*  And so unfortunately, James doesn't like, well, maybe James does.
*  Most people you can't, you can't kind of like give like a formal
*  language to and have them execute.
*  The great thing about things like AI town and the great things about these
*  models is you have both, right?
*  You have the ability to use a formal language to define the laws of physics
*  and define the things where you know specifically what you want and you know
*  specifically the trade-off you want.
*  And then within that, you have these models where you get, and I think
*  Yoko said it so beautifully that you've got this kind of these creative,
*  independent elements that will surprise you continuously.
*  Like even when I'm programming against them, I'm constantly surprised.
*  I'm like, you said what?
*  Like you did what?
*  Like, you know, they really are these kind of intelligent beings.
*  And so, you know, again, you know, AI town was Yoko's passion project.
*  And then convex, you know, jumped into help out, which is fantastic.
*  And then I've basically done very little, but like, you know, it is a
*  framework for playing around with this.
*  So for people that are interested, I would just recommend them just like go
*  ahead and get pull and see how these, these two paradigms match.
*  So I actually think for, you know, I've worked on a number of these projects.
*  I think this is the best example of the full autonomy of an AI and a very
*  formal structured system with strong guarantees interact.
*  Martin said something that really reminded me of just engineering in
*  general and construction projects.
*  And it's the idea of kind of compounding approximations.
*  So anyone who builds any like serious engineering project knows that
*  everything's approximate, right?
*  And there's certain times you need things to be exact, like it's a bearing
*  and it has to be the exact right place.
*  And there's parts that just can be approximate.
*  Are you showing up to work at a certain time?
*  So when you build, for people who are building applications need to think
*  about these compounding approximations, right?
*  There's certain parts of applications where approximate answers are great.
*  And certain answers where, you know, yes, I really need an F sync that has to
*  get stored to an application.
*  And it's not that hard, you know, just go think it through, like what
*  stuff needs to be exact.
*  Okay.
*  I'm going to use a formally specified platform here.
*  I'm going to have an if statement.
*  I'm going to have a code block, which stuff is going to be great to be approximate.
*  Yeah.
*  Use a model for that.
*  Why not?
*  I think Martin is too humble.
*  So I really have to brag on his behalf, but honestly, like kind of like
*  Martin said, this is our passion project.
*  We didn't have an agenda over it.
*  It was just, we're a bunch of programmers.
*  We just thought this is fun to build.
*  And then we keep building on it.
*  If you, you know, join our discord, you'll see that Martin is every night kind of
*  coding out this next feature, which is super cool.
*  That allows any user to kind of create their own world visually using tile maps,
*  like drag and drop tiles and create your own layout of the world.
*  So you can later agents on top.
*  I don't have an answer for like, what's the strategy?
*  Cause there's no strategy.
*  We're just a bunch of programmers and nerds who tinker with these kind of things over
*  the weekend, but now kind of we've got so much support from the community.
*  Um, would you want this to be like a living project?
*  We can keep supporting.
*  So at the end of the day, we want to, you know, add more integrations.
*  There's just so much work to be done.
*  And then we want to have the community to be more engaged, you know, open PRs help us out.
*  At the end of the day, it's an open source.
*  And I think it's just the beauty of having, you know, community of people who are on this
*  court who never met each other to work together on it.
*  So let's take the, you know, last stretch and just inspire people a little bit with
*  your sense of kind of value and other use cases.
*  You know, what sort of things should people have in mind when they hit the fork button?
*  I've got two examples real quick.
*  One, we have a, we have a fork.
*  We have an upstream yet actually hasn't been landed yet.
*  I don't think with human actors, you can walk around in the.
*  Game and talk to people as cool.
*  You can go and be part of conversations.
*  Now you might say, okay, the first thing any company is going to think about when you do
*  that is someone going to come and spout some offensive content.
*  Right.
*  And I'll, I'll, I'll be going to be hosting a demo app that someone's going to come and
*  say something horrendous and try to teach people something awful.
*  And that's the challenge, right?
*  Anytime you build a demo app on behalf of a company, you worry this thing.
*  What you can do is you can just ask the model, is this offensive or not?
*  And does a pretty good job of this.
*  Now you might get slightly wrong, right?
*  Cause it's approximate, but the best way to know whether someone's typed an offensive
*  message is just to ask the model, Hey, is this, is this an appropriate message to have
*  in the system?
*  And it'll tell you reasonable accuracy.
*  This kind of stuff is, I just find it so cool.
*  Right.
*  You know, you can build an emergent pro, like you can just use the model to do the stuff
*  that we would traditionally find very difficult.
*  You know, if it was a couple of years ago and we had to build a system to make sure
*  the content was, was safe, you would just do like a keyword match or something.
*  You're really very difficult and very ineffective.
*  I think when people can start thinking about like, how can I do stuff now that would have
*  been really hard to do a few years ago?
*  And hey, four couldn't add it.
*  Yeah.
*  I don't know if folks here or even the listeners have read this book named the sea of tranquility.
*  It's like a, it's from the same author who wrote station 11.
*  It's a great book.
*  I'm not going to spoil the sci-fi book for you, but at the end of the day, the point
*  it tries to drive home is that there are simulations.
*  We may live in the simulation by the end of the day, just because it's a simulation doesn't
*  make it less real, you know, like what you did in that world and the emotions report
*  into it.
*  Those are still real experiences.
*  So at the end of the day, what I was thinking in the back of my mind is that I think everyone
*  should have their own world that they run.
*  You know, that they outpour their passion and then experiences and memories and, you
*  know, like interactions into.
*  And then the goal of AI towns, at least for me, is for anyone to be able to fork it around
*  their own world and customize and explore.
*  Maybe one day the agents in the world will create another simulation.
*  You never know.
*  I mean, this, I see just, you know, always with this AI stuff, I see just incredible,
*  exciting potential, you know, whether it's stuff that's like relatively easy to imagine,
*  like, oh my God, I could have a language learning environment where I could attend a virtual
*  party in Spanish and like get unrusty in my Spanish skills and stuff like that.
*  Sounds fun.
*  And, you know, for a lot of people, a lot of little variations on that could be super
*  awesome.
*  I also then do worry about people kind of falling into these simulated environments.
*  And I mean, this is just a random hobby project on some level.
*  So I don't think you're even, you know, productizing this to the point where you're
*  like responsible for, you know, a community of users.
*  But it does seem like we're headed for, you know, a place where games are going to be
*  just like much more easy to lose yourself in.
*  I keep kind of coming back to that getting lost in.
*  It's not necessarily that it's like bad in and of itself, but if you kind of fall into
*  it and, you know, lose track of your normal life, it seems like it can easily get out of
*  hand.
*  And then the fact that, you know, we may be in a simulation is also like super interesting.
*  But I would just love to hear you guys reflect on that.
*  Like what would you, you know, you've spent a lot of time with it.
*  What advice would you give to other developers?
*  What do you think is the responsibility for people that are, you know, kind of whipping
*  up these simulations, especially if they're going to try to turn them into businesses?
*  Listen, these models are the largest compute jobs that we've ever run as a race by far.
*  I mean, these are the most sophisticated things that we've ever created.
*  You can explore what that means by trying to interact directly with them.
*  But that's only one modality, right?
*  There's another modality, which you just kind of let them interact with each other
*  and you let them interact with the world.
*  And it's kind of funny because when it's you interacting, it turns out you're the
*  limiting factor.
*  Like you only can, like we're not that creative.
*  And so like you only can say a few things and, you know, whatever.
*  But when you have them interact together, the state space that they cover is so potentially
*  enormous.
*  I mean, it's more than the atoms in the universe, right?
*  Like obviously, right?
*  And so like you fall into an appreciation for like how powerful these are and how large
*  these are.
*  And so I think it's too early for us to presuppose where this goes or what the apps are or things
*  like that.
*  And like for companies, that's great.
*  And they should do that.
*  My recommendation for anybody's interested in this stuff is view it almost as an exploration
*  of a new life form and go very open-minded.
*  Don't worry about all the fud.
*  Like they're not going to kill you.
*  They're not going to kill each other.
*  They're not going to like make you addicted.
*  I just feel like we're kind of like we're almost preemptively like stopping our ability
*  to wonder of this new thing that we've created.
*  And so very much for something like AI Town, it's very different if you're building software,
*  you have that conversation for like a company.
*  But for AI Town, which is meant to be an exploration platform, I would just say go in with an open
*  mind and realize that you're seeing something that we as I think it's a race have never seen
*  before.
*  And then you'll get an appreciation for how you use these things.
*  And then just like the advent of the internet, like we had no idea what it would be used
*  for, what companies would emerge.
*  Like we didn't know about Amazon.
*  We didn't know about Yahoo.
*  That will all come next.
*  But before any of that comes, I think you just have to understand the technology.
*  That's kind of the point.
*  And this is the Wild West in many respects.
*  This is such early days, right?
*  And this is a really interesting time to go in and see stuff develop, see ideas originate
*  and be part of it.
*  And also go outside.
*  Feel the sunshine.
*  I was going to take a different position on this.
*  That is I do think at the end of the day, it comes down to what's your definition for
*  games like life to some people.
*  I mean, at the end of the day, you're looking for things you're passionate about.
*  Like, for example, in a part time cartoonist, when I draw cartoons, I draw a tablet.
*  Right.
*  And that's a form of game for me.
*  And I easily fall into that world.
*  When TV came out, people are like, oh, this is going to ruin everyone.
*  People are just going to stare at the screen.
*  But that at the end of the day, I think it's in that value.
*  Same for novels.
*  When people like back in the days, people were like, oh, if you keep reading novels,
*  you're going to fall into a different world.
*  You're not going to think about anything.
*  You're just going to keep reading it.
*  And you have created this whole new world in your mind.
*  I do think games at the end of the day are similar in that it's not all or nothing.
*  It is just a different experience.
*  And that's very much like any other experience you have in life.
*  To reiterate, A.I. Town is not a project that's kind of owned by us.
*  It's a community project.
*  And the whole point of this is to inspire people to go build.
*  And we're going to keep making improvements and simplify things and making it more
*  clonable and all this kind of stuff.
*  But the whole point is to get people building stuff and get people inspired.
*  And so if people come out of this podcast and they're inspired to build some applications
*  and see for themselves, I think that's an amazing outcome.
*  Yoko Lee, Martin Casada from A16Z, James Cowling from Convex.
*  Thank you for being part of the cognitive revolution.
*  It is both energizing and enlightening to hear why people listen
*  and learn what they value about the show.
*  So please don't hesitate to reach out via email at tcr at turpentine.co
*  or you can DM me on the social media platform of your choice.
*  Omnike uses generative A.I. to enable you to launch hundreds of thousands of ad iterations
*  that actually work customized across all platforms with a click of a button.
*  I believe in Omnike so much that I invested in it and I recommend you use it too.
*  Use Cogrev to get a 10% discount.
*  you

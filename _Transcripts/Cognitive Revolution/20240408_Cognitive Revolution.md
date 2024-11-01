---
Date Generated: October 31, 2024
Transcription Model: whisper medium 20231117
Length: 5221s
Video Keywords: []
Video Views: 766
Video Rating: None
Video Description: In this episode, Nathan sits down with Andrew Lee, founder of Shortwave, an AI-powered email app that describes itself as “the smartest email app on planet earth.” They discuss Shortwave’s RAG stack, how the AI assistant works, the models Shortwave is using, and much more. This is truly a masterclass in RAG app development.

Sponsors : 
Oracle Cloud Infrastructure (OCI) is a single platform for your infrastructure, database, application development, and AI needs. OCI has four to eight times the bandwidth of other clouds; offers one consistent price, and nobody does data better than Oracle. If you want to do more and spend less, take a free test drive of OCI at https://oracle.com/cognitive

The Brave search API can be used to assemble a data set to train your AI models and help with retrieval augmentation at the time of inference. All while remaining affordable with developer first pricing, integrating the Brave search API into your workflow translates to more ethical data sourcing and more human representative data sets. Try the Brave search API for free for up to 2000 queries per month at https://bit.ly/BraveTCR

Plumb is a no-code AI app builder designed for product teams who care about quality and speed. What is taking you weeks to hand-code today can be done confidently in hours. Check out https://bit.ly/PlumbTCR for early access.

Head to Squad to access global engineering without the headache and at a fraction of the cost: head to https://choosesquad.com/ and mention “Turpentine” to skip the waitlist.

TIMESTAMPS:
(00:00) - Intro
(01:07) - Shortwave: AI-Powered Email
(06:22) - Genesis of Shortwave
(15:25) - Sponsors: Oracle / Omneky
(16:46) - Data Processing Pipeline
(21:57) - Choosing a Vector Database
(26:34) - How the AI Assistant Works
(36:24) - Sponsors: Brave / Plumb / Squad
(40:53) - Fine-Tuning & Hosting Models
(45:11) - Email Automation
(47:55) - Email Retrieval
(51:44) - Optimizing AI Performance
(53:20) - Safety & Embedded Ethics
(01:04:51) - Strategic Product Launches
(01:09:58) - Inbox Management
(01:12:24) - The Future of Collaborative AI
(01:18:54) - Scaling Personalized Outreach
(01:26:04) - Closing Thoughts & What's Next

Music licenses:
MKGHDH8MXGLG8KCZ 
YD35PGA4PXQON3NP
QGOCHQQXMPVRPDNU
---

# The AI Email Assistant I've Been Waiting for, with Andrew Lee of Shortwave
**Cognitive Revolution:** [April 08, 2024](https://www.youtube.com/watch?v=BeoMJB3gpj8)
*  the right time to launch a feature or launch a product is right before it seems possible.
*  If Google with its infinite resources, with the largest email user base in the world,
*  that they are not willing to invest and try to figure out what the future email is,
*  maybe I need to do something about this. We realized that holy crap for the entire
*  history of email clients, the data in that email has been completely unaccessible.
*  You can do like basic searches and stuff, but if you want to ask a question and have the email
*  client figure out the answer for you, there was really no way to do that. But suddenly this like
*  giant corpus of unstructured text that everyone has like gigabytes and gigabytes is suddenly has
*  gone from like this pile that's eating up disk space to like maybe something that's really valuable
*  to you. Hello and welcome to the cognitive revolution where we interview visionary
*  researchers, entrepreneurs and builders working on the frontier of artificial intelligence.
*  Each week we'll explore their revolutionary ideas and together we'll build a picture of
*  how AI technology will transform work, life and society in the coming years.
*  I'm Nathan Labenz joined by my co-host Eric Torenberg.
*  Hello and welcome back to the cognitive revolution. Today my guest is Andrew Lee,
*  founder of shortwave, an AI powered email app that describes itself as the smartest email app on
*  planet earth. Like many of us, I've been using Gmail for roughly 20 years now. And while I've
*  tried several alternative email clients over time, for me none have really stuck.
*  Shortwave however has truly impressed me and I've continued to use it past the point of curiosity
*  and into the realm of forming a genuinely new and likely lasting habit. My favorite feature by far
*  is the AI assistant which presents in the increasingly familiar form factor of the natural
*  language sidebar chatbot. It can help you search through and configure your inbox, check your
*  availability and schedule meetings and refer to similar emails you've sent in the past so that it
*  can imitate your style when drafting responses for you. As someone who's long since given up on
*  inbox zero and really just wants an AI assistant to help me navigate my overloaded inbox, I can
*  definitely say that I've had a few magical experiences with this product. The time saved
*  in searching for things that I know exist but can't quite remember the keywords for,
*  unto itself, has been delightful. Andrew, who previously founded Firebase and has already
*  been acquired by Google once, was extremely open about the technology underlying Shortwave,
*  reflecting the fact that this is no thin wrapper startup and I had a ton of fun getting so deep
*  into the details. We covered Shortwave's rag stack which is powered by a full download and
*  re-indexing of your entire inbox, a process that takes hours and costs Shortwave real money.
*  But which creates a remarkably responsive experience downstream. We also got into how
*  the AI assistant works from user message input to AI response, including tool selection, query
*  reformulation, feature extraction, retrieval, re-ranking and finally answer generation.
*  We also got into which models Shortwave is using, which include Mistral, fine-tuned GPT 3.5 turbos
*  and GPT 4 turbo, a list which is always subject to change and right now perhaps even more so than
*  usual since Cloud 3 was just launched after we recorded and long context Gemini 1.5 is on the
*  horizon as well. Toward the end we discussed how Andrew thinks about building and timing product
*  launches in such a fast moving space, his vision for the future of Shortwave, how he expects email
*  to evolve and how we'll all manage the inevitable rise of high quality AI generated spam, as well as
*  how companies will use a deep AI integration to manage knowledge on a team-wide basis.
*  If you're building with large language models, this conversation has a ton of great nuggets
*  which you won't want to miss. And if you're just an average email user, as I'm pretty sure all of
*  you are, I definitely recommend checking out Shortwave. To be clear, this is not a paid
*  promotion. Andrew was kind enough to give me a free year of Shortwave, but that's it. I'm
*  genuinely just super enthusiastic about this product and you do have my commitment that I
*  will always be transparent about any sponsorship deals that we might do in the future. Of course,
*  your feedback is always welcome. You can leave me a message on our new website at cognitiverevolution.ai,
*  that's cognitiverevolution.ai, or DM me on the social media platform of your choice.
*  Now let's dive deep into AI technology powering the future of email with Andrew Lee of Shortwave.
*  Andrew Lee, founder of Shortwave, welcome to the Cognitive Revolution.
*  Thank you for having me here, Nathan. Really excited.
*  I am very excited about this one. So I have been using your product, Shortwave, which is an email
*  app over the last couple of weeks getting ready for this episode. And it is one that has really
*  kind of got me excited for multiple reasons. So I'll just give you a little gushing praise right
*  out of the gate. And then I really want to get into all the weeds of how it works. Like many
*  people, I've been using Gmail for a long time. I hesitate to kind of count up all the years at
*  this point, but it's getting on toward 20. And a lot of alternative interfaces have come out,
*  a lot of ways to get to inbox zero. And honestly, none of those have really ever stuck with me,
*  though I have tried a number over time. Shortwave has really stood out to me for a couple of things.
*  One, the email search is awesome. And for that alone, I think it's pretty exciting. And then
*  second, the AI assistant, which is actually how I'm using search, which we can unpack in more
*  detail, but the AI assistant is perhaps the best writing as me experience that I have encountered
*  in any app that I've used so far. So it has actually been, you know, while I kind of signed
*  up for everything and, you know, we'll put some time into trying all the products, you know,
*  that we talk about on the podcast. This is one that I have found myself very naturally kind of
*  excitedly going back to. And, you know, the muscle memory of going straight to Gmail is certainly
*  pretty deeply entrenched. So that is no small accomplishment. I think it's reflective of some
*  really great work under the hood. Great job by you and the team. And with that, I'm excited to
*  unpack in lots more detail how it all works.
*  That is awesome to hear. Thank you so much.
*  Maybe for starters, just to take one quick step back, like many application developers that we
*  talk to, you started this company before large language models were a thing in the way that they
*  are today. Would you want to give us just a little bit of context for what it was that kind of
*  inspired you to start the company? How big of a part of your plan AI was at the time and kind of
*  the technology trajectory that we're on is perhaps, you know, either been what you expected or perhaps
*  surprised you? Yeah, absolutely. AI was not really on the radar at all for us when we first started
*  the company. The actual motivation for it really was a couple of things that happened in 2019. So
*  for some background, I was unemployed at the time. I had previously sold the company, a Firebase to
*  Google and worked there for a while. I'd taken some time off and I was kind of doing my own thing.
*  And I got to the point where I was a little restless. I wanted to start something new and
*  I saw a couple of things happen. So the first thing that happened was the democracy protests
*  in Hong Kong. I don't know if you remember. The thing that started out to me was the way the
*  Chinese government was using WeChat as a means of control of those protesters, where if you said
*  something they didn't like, you know, maybe someone was going to say something, you know,
*  they didn't like, you know, maybe somebody would show up at your house or maybe they wouldn't get
*  a message. And I looked at that and I said, hey, that's a bad thing. But at least that's not
*  happening in the other parts of the world, right? Everywhere else, you know, those centralized
*  communication providers, they're, you know, they're trustworthy, they're doing a good job.
*  And then I started to realize that actually, maybe that's not happening the way I always
*  hoped they'd get out of the world too, including potentially in the US and Europe and places like
*  that. And then I said to myself, well, at least we have email, right? Even if I don't necessarily
*  want to do all my communication on WhatsApp or something like that, I can call back email.
*  And then Google killed off Google inbox, which to me was, you know, their next gen email product.
*  And I thought to myself, hey, if Google with its infinite resources, with the largest email user
*  base in the world, if they're not willing to invest and try to figure out what the future's
*  email is, you know, maybe I need to do something about this. And I have a long history with email.
*  Actually, my dad and I ran an ISP in our basement in the nineties. And, you know, I have a lot of
*  experience writing email servers and I, you know, I have a love for the federated protocol that
*  underpins email and all the things that that enables. And I said, okay, you know what, maybe
*  I got to do something. So I call up a bunch of my Firebase buddies and I said, hey, you guys want
*  us to run the company. I'm thinking we should build an email app. And surprise, surprise, they were,
*  they were excited about it too. And so we kicked it off at the beginning of 2020, initially really
*  focused on making something that did justice to this amazing underlying email protocol. And the
*  first thing we tried to do was collaboration because Firebase was a product really designed to
*  help people build collaborative apps. So we knew a lot about what people liked in collaboration.
*  We knew a lot about how to build those types of systems. And we thought email was right for that.
*  So we built an email client designed to help you collaborate and fairly quickly discovered that
*  that was kind of hopeless as a V1 product for go-to-market reasons. Like you couldn't,
*  you couldn't sell to anyone because the people who were looking for email clients were not
*  simultaneously looking to get off Slack. And the people who were looking for Slack were not
*  simultaneously wanting to pitch their entire team on not using their existing email client and
*  switching to a new email client. And so we could never get someone who was like looking for both
*  end users at the same time. And so at that point we pivoted and we said, hey, we are getting
*  some traction on just the pure like individual email experience. Let's double down there. Let's
*  really make a, just a really bang up individual business email client. And so we spent the next
*  year and a half or so working on that, which is a big project. If you ever tried to build an email
*  client, there's a lot of stuff in there, just lots of little features and just the basics of like
*  displaying your email correctly and threading your email correctly, making search work is
*  quite hard. But we got there like about a year and a half ago, we got to the point where like
*  you had a solid email client. It did all the things you expected. It worked on the platforms
*  you needed to work on. You know, it had the core features that you'd expect it to have.
*  And we started looking around and realizing, hey, there's a lot of stuff going on here with
*  these large language models. And we'd been following it for a while, but every time we'd
*  played with them previously, they didn't quite seem production ready. And this time they did.
*  This time, you know, we tried some stuff. Actually, one of my old co-founder came in and
*  like demoed some stuff. And we decided actually, we feel like the time is right. This is actually
*  something that we can build a product on. And the thing that was so exciting for us is we realized
*  that, holy crap, for the entire history of email clients, the data in that email has been completely
*  inaccessible, inaccessible related. You could do like basic searches and stuff. But if you want to
*  ask a question and have the email client figure out the answer for you, there was really no way
*  to do that. You could search, you could read it yourself. But suddenly this like giant corpus of
*  unstructured text that everyone has like gigabytes and gigabytes and gigabytes of this, it suddenly
*  has gone from like this pile that's eating up disk space to like maybe something that's really
*  valuable to you. So like at that point, we tested some stuff, it worked well, and we pivoted hard.
*  And like the last year and a half, we have been focused on AI. The AI email system has been my
*  favorite feature by far. And, you know, just to kind of describe it and you can, you know, give
*  me a little refine my description, but it basically exists as a side panel on the, and it's kind of
*  like a pop over on the mobile app, which you also have, although I've spent more time so far with
*  the desktop version. But I can kind of bring up a side panel that's alongside my main inbox. And
*  then I can basically just have a chat GPT like experience with that assistant, you know, in a
*  chat back and forth natural language sort of way. But with the difference that obviously it is
*  connected into all of my emails. So it can do searches against that email. It can pull up
*  relevant examples, and then it can also, it can also connect to my calendar. And then it can even
*  start to draft responses for me. Feel free to kind of elaborate on how you would typically pitch the,
*  or describe the product experience. And then I really want to get into, you know, the weeds of
*  how do you set up the agent architecture? You know, what is the, obviously being a database guru,
*  like what is the rag implementation look like? And, you know, how are you actually
*  bringing about such good results in the right as me department? Those are kind of the three big
*  areas, but for starters, you know, you can refine my description. I think the thing that really
*  impressed us about LLMs is how general purpose they are. Like you can go into chat GPT and you
*  can talk about just about anything. Like last night I made fried chicken sandwiches. Like I got
*  it to explain to me how to make a fried chicken sandwich. And today I'm like asking it coding
*  questions. They could do all this stuff, which is really cool. And so one of the struggles we had
*  early on when we were kind of figuring out how to bring this stuff into, into shortwave and provide
*  value is like, okay, if they can do anything, like where's the start. And we thought, you know,
*  the, the first thing we should probably do is build something super general purpose that gives
*  somebody the full breadth of what is possible, even if the UX isn't super polished for any
*  particular use case. So we can get a better understanding of what people want to do. So
*  the concept for us was similar to sort of chat GPT of like, what if there was like a human
*  sitting next to you in a chair, watching you, you do your email, who knew everything about what's on
*  your screen, who knew everything about all the emails you've ever received, who knew about your
*  calendar and could help you do stuff. And one of the reasons we had confidence that this would be
*  a good idea is this is something that people already have, like people have executive assistants
*  that sit in their inbox and help them with their calendar and schedule things. And people pay a
*  lot of money for this. And we thought, Hey, if we can build something that does some small fraction
*  of that reasonably well, this could be really valuable to people. And so we started with
*  something very conversational, very general purpose. You can do it, you know, you could do
*  all the normal stuff you do in chat, you would deal with it, but you can also ask about your
*  calendar, ask about your emails, have it do searches for you, how to write things for you,
*  all of that, but a right, right from that sidebar. And we do intend over time to have like much more
*  focused experiences for certain things. So I don't know if you play with the AI autocomplete
*  feature, but that's one where we're like trying to optimize the UX, but we wanted to start general,
*  figure out where the really common use cases were, and then polish those experiences as we learn.
*  For starters, when I first sign up, I connect my Gmail and there's, is there support for any other
*  client or is it a hundred percent, you have to have a Gmail to, to start with it? Or could I start
*  with a bag? I guess nobody's really starting from scratch really much, right? But could I just come
*  and start a short wave account with no other email client at all? Not yet. It's Gmail only.
*  We would love to have, you know, a hosted service that just, you know, we set up an account for you.
*  We'd love to have it eventually be something that works for the Microsoft suite and something that's
*  on-prem that's all in the ambitions. But one of the things that just helped us move faster is the go
*  to market of I have an existing account. I sign in with my Google account and boom, I have all of
*  my email there and I have all of my labels and contacts and everything like that. Onboard
*  experience is really nice. And so that's really where we're focusing our RV one here.
*  Soterios Johnson Gotcha. Cool.
*  Soterios Johnson Hey, we'll continue our interview in a moment after a word from our sponsors.
*  AI might be the most important new computer technology ever. It's storming every industry
*  and literally billions of dollars are being invested. So buckle up. The problem is that AI
*  needs a lot of speed and processing power. So how do you compete without costs spiraling out of control?
*  It's time to upgrade to the next generation of the cloud, Oracle cloud infrastructure or OCI.
*  OCI is a single platform for your infrastructure, database, application development and AI needs.
*  OCI has four to eight times the bandwidth of other clouds, offers one consistent price instead of
*  variable regional pricing. And of course, nobody does data better than Oracle. So now you can train
*  your AI models at twice the speed and less than half the cost of other clouds. If you want to do
*  more and spend less like Uber, 8x8 and Databricks Mosaic, take a free test drive of OCI at oracle.com
*  slash cognitive. That's oracle.com slash cognitive, oracle.com slash cognitive.
*  Omniki uses generative AI to enable you to launch hundreds of thousands of ad iterations that
*  actually work customized across all platforms with a click of a button. I believe in Omniki so much
*  that I invested in it and I recommend you use it to use cog rev to get a 10% discount. So one of
*  the first things that you do is import the email history. And as you mentioned, there's gigabytes
*  sitting around for most people. Certainly I'm among them. I've given my email address out perhaps
*  too freely over time. And so there's an unbelievable amount of content. And most of it, not very
*  valuable. And one of the big challenges is getting to the valuable stuff, given all that clutter.
*  I don't think you're more about that kind of data processing pipeline, because certainly as you're
*  setting this up for later success, the importing of the data and any pre-processing of the data
*  or any embedding of the data is like a pretty critical aspect of the whole thing. So what's
*  happening in that first import phase? So this is actually a place that we got kind of lucky
*  in that while I mentioned when we first started the company, we were trying to build a collaborative
*  email app. And if you want to make something collaborative, that means you want to share
*  data with other people. You probably want things to update in real time. And so the
*  architecture you want to build for an app like that is something where there's both client and
*  server working together and there's real time streams of data moving back and forth. And this
*  was an architecture that we were very comfortable building because this is how the Firebase products
*  work. That's how we built it. And when we decided to focus on LLMs and integrating those, this turned
*  out to be a really big win because unlike basically all of our competitors, we have all of your emails
*  on the server. So we did the heavy lifting of we're going to import that when you sign up,
*  which is very expensive for us to do because we have to have copies of all that stuff and we have
*  to re-index everything. But we have that data now, which means things like embedding and storing the
*  vector database. We're having access to a beefy cluster of GPUs to run across and put it in
*  models. It's something that's really easy for us to do relative to other people that might have to
*  start from scratch when doing that. So the moment you sign up, we start, you know, reverse chronologically
*  going through and sucking your emails. And you can actually see that pop into your inbox as we're
*  moving along and we're taking those and we are, you know, saving off a copy of them in our database.
*  And then we are indexing those both in Elastic so that we can do full text search, but then also we
*  are embedding them with an open source model and throwing them into Pinecone, which is our vector
*  database for retrieval there. And that whole process can take depending on the size of your
*  inbox, you know, from, you know, a few minutes to a few days. It's not uncommon for someone to have,
*  you know, three, four, five million emails in their inbox. So it's a big process. But once we
*  have all that stuff indexed, we can do a bunch of cool stuff. We can do full text searches against it.
*  We can do AI based searches against it. So it's really powerful.
*  Can you comment a little bit on the choice of embedding model and also the choice of
*  vector database Pinecone? I don't know if they offer both a self-hosted version and a hosted
*  version, but yeah, I love the, I mean, we have a lot of folks, obviously the whole world is implementing
*  rag stuff right now. So everybody wants to learn from your hard-won lessons in terms of the right
*  models, the right infrastructure to use. We actually, at this point, I think have decided
*  that even, even though we just released this in October, it's all obsolete and we're going to,
*  we're going to do a bunch of new stuff, but we chose to use an open source embedding model.
*  It was just, it's called InstructorXL. It was on, it was on a hunting base as our,
*  as an embedding model because it is cheap and fast and works well. And the vector is not too big. And
*  we, you know, we, we kind of did the math on, Hey, you've got millions of emails and you know,
*  what is this going to cost? And with the way we want the infrastructure set up, the vector database
*  was going to start to dominate in terms of cost. And so we didn't necessarily want the biggest best
*  model because we store a ton of emails. We don't necessarily query them super often. And there's
*  trade-offs that you can make between the effort you spend embedding, the size of the embedding,
*  the effort you spend doing the searches. So for example, with a, with a smaller vector for your
*  embedding model, you might not be as precise in your vector search, but what you can do is you can
*  simply like return more results and shove more results into the prompt. So maybe the queries are
*  a bit more expensive, but the embedding and the storage is cheaper. So you want to, you want to
*  factor that all in. So yeah, we chose an open source embedding model that made the embedding
*  cheap. We chose a sort of medium sized vector to make storage relatively cheap. We've just pine
*  cone primarily for performance considerations. So it has a feature that none of the other kind
*  of top tier vector databases has, which is name-stacing where we can, without a performance
*  penalty, have a huge number of users on the, you know, on there together. And it makes it easy to
*  manage that. Like we looked at, you know, using PG Vector and a bunch of these other things, and
*  a pine cone gave us the best option there. And now how would that contrast? Cause PG Vector,
*  I think is obviously one that my guess is going to increasingly become a lot of people's first
*  contact with vector databases just because they've already got the PG part of PG Vector. And so yeah,
*  why not? Right. How does that fall short? I'm imagining if I wanted to run a query, you can
*  always do the like where user equals their ID and vector, but why does that not work as well?
*  It comes down to the implementation. So in PG Vector, when you do a query like that, where you
*  say, you know, find me things that are semantically similar to blah, and then filter in these with
*  these criteria, it's doing those in order. It's first going out and it's doing, you know, K nearest
*  neighbors, it's finding those, and then it's filtering by the other criteria. And if you have
*  all of the different vectors from all of your different users jumbled together in the same
*  table, you're going to have to sift through like a very large number of those vectors. And that can
*  just slow things down. And there are workarounds here. So for example, like you could just make a
*  lot of tables, which is something that I've talked to people who do this, but that comes with a lot
*  of sort of headaches in terms of database management that we didn't necessarily want to take on.
*  So I think if you're in the process right now of picking your vector database, you should think,
*  how many namespaces do I need? Am I, is it one per user? Is it one per company? Is it one global
*  one? You should think hard about how many documents you have and how big those documents are. And I
*  think for most people doing a rag, you're not working with as many as we are, right? Like for us,
*  in email inbox, we'd have millions of emails. I think a lot of these cases people have for rag,
*  it's maybe, you know, thousands or tens of thousands or hundreds of thousands. So
*  the right choice for you might be different. We did look at PGA Vector because we also have the
*  TG part of that in our stack and it would have been very convenient. But I think we made the
*  right call in what we did here. In terms of the size of the, and this maybe is one of the things
*  that perhaps you're already thinking about evolving, but I know that OpenAI just released
*  an update to their embedding product. I haven't studied this in detail yet, but I understand that
*  basically they have come up with a way to have variable length vectors and sort of do it such
*  that if you use the small one, you're getting like the bulk of the information. They've kind of like,
*  you know, created varying sizes that, you know, guys sort of apply like an 80, 20 sort of principle
*  where they're capturing most of the information and the smallest version. And then you get
*  incrementally more, but it obviously, you know, grows in size to capture that greater resolution.
*  Do I have that right? And is that the kind of thing that you are thinking of moving to next?
*  That's what I understand. I think it's, I think it's super smart because the, you know, you don't,
*  like I said, you don't necessarily want the biggest vector. You want to figure, consider the
*  trade-offs between, you know, how many documents you have, how often you query these documents,
*  how good you need those results to be, how fast you need those results to be. And there's a lot
*  of different options for making this stuff work. So if I can give it to architecture briefly for RAG,
*  it's not just quite so simple as, you know, you ask a question and we, and we go to the director
*  database. When we, when we do our AI search, we're actually searching across our traditional search
*  infrastructure using keywords and labels and time radius. We sort of extract features and we do that.
*  And then we're also looking at the vector database and we're taking all of those results
*  and we're running them through another model to re-ranking. So we have a cross-encoding model that
*  basically looks at the question you're asking in every document and says, how likely is this
*  document to help answer the question? And because we have that cross-encoding model, we don't need
*  the vector database to be super accurate because what we can do is just over-fetch. We can, we can
*  just cast a really wide net and say, give me a lot of nearest neighbors and then run those to the
*  cross-encoding model to actually like winnow that down to a smaller set. So in our case, we said,
*  Hey, you know, the trade-off there is basically performance, right? The more of these that we
*  have to sift through with the cross-encoding model, the slower it will be. And so we want to trade off
*  basically latency at retrieval time against cost for storage and cost for embedding. And we tried
*  to pick a peak that made sense for us in that regard. But I think that peak is going to be
*  different for different applications. So the idea that you're going to have that flexibility
*  with embedding models going forward, I think is really key, really smart. One thing actually I
*  want to add here in the vector database world, I think one of the changes that's going to come up
*  here is people are going to start separating compute and storage so that it be right now,
*  you know, most of the offerings that you have, that stuff's very tied together. And if you have
*  something that has a lot of storage and a little bit of computer needs a lot of computer, a little
*  bit of storage, you might not have a very good cross trade off. But Pinecone just came out with
*  a hosted service that we're looking at. And I think other people looking at this as well of like,
*  how do we make smarter cost trade-offs for people whose, you know, storage and reading and writing
*  patterns might be different than other people. Interesting. So down to the user level optimization
*  of how you would manage their, is it managing their database or managing how you're accessing
*  the database. I guess it could be both, right? But yeah, that's fascinating. Maybe we'll bump up
*  one layer to the agent, to the AI assistant layer, and then we can still take a couple additional
*  deep dives into the rag side of it. So, you know, folks who listen to the cognitive revolution will
*  certainly be familiar with the kind of basic scaffolding of an agent, you know, put a language
*  model in a loop, give it a chance to kind of plan, give it a chance to, you know, think step by step,
*  give it a chance to take some action, get some feedback. And okay, so we know that you have
*  essentially a version of that where when I type in a request to the AI assistant, and these can be
*  like, find me something out of my email or find and draft or even like find and check against my
*  calendar for availability and draft. And you could suggest some more use cases there perhaps as well,
*  but those are the kind of main go-to ones that I've been using. Yeah, I was going to say that
*  the biggest ones are really search and things related to search, like find this information
*  for me and synthesize it this way. And then writing, you know, help me write an email,
*  which often also uses search to get the right context. Yeah, it is cool on the on the search.
*  I mean, there are so many times where I'm like, where did I have that? You know, I want a link.
*  I put a I know I put a link in an exchange with someone. But, you know, I might have multiple
*  threads with that person. I'm not exactly sure what my highlight was, what the link text was
*  when I put that in there. One of the great use cases is so simple, but just so refreshing
*  is to just ask, can you find me the link to the whatever that I sent to whoever and just have it
*  pop back with that and be like, yep, that's the link. Amazing. Now I'm not manually loading up
*  all these screens and scanning through all the threads on my own. I find that in and of itself
*  to be, you know, just an extremely great use case. I mean, maybe I have memory problems that
*  other people don't suffer from. But for me, that's been really cool. And I like the writing as well.
*  And I do want to get into more detail on kind of exactly how that works. But so I put it a query.
*  It goes through this kind of pretty, you know, familiar, at least from a UI, like presentation
*  layer agent sort of loop. It'll say it's thinking, it'll say it's searching, it will potentially say
*  it's going to cross reference against the calendar. And then it can be drafting as well.
*  You want to kind of unpack those steps a little bit. Like, for example, when searching, you know,
*  notably like I didn't give it keywords. So I imagine there's a translation step in the
*  background. And again, I think people really are very eager to learn from your hard-won lesson. So
*  no detail would be too much detail here. The thing that people are most impressed about with
*  our AI assistant is frankly that it just works at all. I think, you know, there's lots of people
*  that are, you know, building demo AI agent systems, but there aren't very many that have
*  actually plugged it all the way end to end together in like a real working product and made it
*  valuable. And ours, I wouldn't say there's nothing that we're doing, but I think is like
*  revolutionary and graphic. Like we're not, you know, AI researchers. We're, you know,
*  we're software people, we're application developer people, but we have managed to
*  duct tape together all the right components and hook it up with additional protection in a way
*  that actually delivers a working product. And I think the, one of the core insights that we
*  had early on when building this was that we couldn't get planning to work for the quality
*  of models that we were working at the time. I think that's probably still true where if you
*  try to break it down into a series of steps where each step sort of feeds into the next step and
*  each step does some piece of work, that there's going to be errors made by the model that each
*  step that propagate true. And we were just weren't able to get the quality level where we want to be.
*  So we changed it a little bit and we said, okay, what if the goal here was to end up with one
*  prompt that had all of the information you need in context, right? There was never anything left out
*  of that final prompt. Like you're trying to get one prompt that has all the right information and
*  you answer the question in a single LLM call. And then all of the other interesting stuff you do
*  is try to get really clever about how you figure out what things to put in that prompt.
*  So that's the way to think about our architecture is we do a whole bunch of work to try to figure
*  out what should go in the prompt. And then we make one call to GPD4 at the end being like,
*  here's everything you need to know. Give us the right answer. The work to figure out what goes
*  to that prompt actually tends to look a lot more like the agent architecture that you might be
*  thinking of. The first thing we do is we try to, we do this thing called tool selection,
*  where we try to figure out what information is the user suggesting that we go get. And we just do
*  this with a prop, with an LLM call, but in that LLM call, we are including a lot of context about
*  the world. So we're telling it, hey, this is the user helping, this is the time of day, this is the
*  settings that they have. This is the thread that's currently on screen. Like this is like the subject
*  in the first few paragraphs of it. This is the stuff that's selected in the inbox. Like we tell
*  the LLM, this is the state. And the reason for that is you might be asking contextual questions
*  that, you know, by themselves are not answerable, but in context makes sense. You might be like,
*  you know, the thread might be like the Super Bowl and you might be like, what time is the game?
*  And we can figure out if we plug all this stuff together, you're talking about the Super Bowl,
*  but just in the abstract, we can't. So the first thing we do is we do this thing called tool
*  selection using this big prop that has all this data, the world trying to figure out what you're
*  asking. And that returns essentially an array of different data sources. And those data sources
*  could be as simple as including the full text and the thread that's on screen. And it could be
*  including settings that you have. It could be including certain like extra custom prompt
*  instructions. Like we have a special set of instructions, whatever you're trying to get us
*  our ice things that can give you good summaries, but it could also be pulling up historical emails.
*  And that's probably where the most interesting stuff is like accessing your historical emails.
*  And if we choose that tool, so you'll notice like sometimes when you ask questions,
*  it gives you an answer pretty quickly. And sometimes when you ask questions, it like says
*  searching, and then it's a little bit slower. That's basically those are the times that we
*  decided, okay, they want us to do rag, we're going to do rag and pull that in. So if we've chosen to
*  do rag, which is like one of like six or seven tools that we have, the next step is what we call
*  query reformulation. So we want to take the question that you've asked, which may reference
*  contextual information, it may reference previous messages that you sent, like you might,
*  it may not make sense by itself unless you've like read the history. And we try to restructure
*  that into a single standalone question. And we use this, we use an LLM algorithm. You say take,
*  you know, take all of this information that's contextual, take the whole history of the thread
*  and give us one question that has all the information needed to actually answer the
*  question. And so for example, it'll turn, you know, pronouns into people's names, it'll turn like
*  relative times into absolute times, things like that. Then we take that reformulated query and we
*  do what we call feature extraction, where we try to look for what are some searches that we could
*  run on our traditional infrastructure that might return relevant results. So for example, if you
*  mentioned a label, you're like, you know, find this thread, I think it was labeled with, you know,
*  Nathan, we'll be like, ah, Nathan labels, we'll do a search for that. If you reference a time range,
*  we'll try to pull up things from a time range. We'll look for certain contacts, we'll look for
*  certain keywords. So there's a bunch of these different things that we do. And the feature
*  extraction is actually done with a model as well, a smaller, faster model, but a model as well.
*  We pull out a bunch of these features and we run a bunch of additional searches. Then we take that
*  reformulated query and we embed it. And in parallel with running all these searches against Elastic,
*  but these traditional queries, we're also doing that a K and N search in fine cone and pulling
*  those results back. And we end up with a big pile of threads, right? Some of them are semantically
*  similar to the question. Some of them match the metadata that you've referred to. Some of them
*  match the keywords that you've talked about and put those together in a big pile. We take that set
*  of threads and we have a heuristic that we apply on top of those. That's just based on like experience.
*  Like we tried a bunch of stuff and we saw what worked and what didn't. And as an example, we do
*  recency bias where we say, hey, if someone's asking about like when it's by flight,
*  they're probably talking about a flight that's been discussed recently. We just figured out,
*  hey, we're going to have like a function that we apply that older things get marked down a little
*  bit. And so for that big pile of threads, we then we know it down to a somewhat smaller pile of
*  threads. We take that pile of threads and we send it into a crossing. So we have a model that we run
*  on our own GP, it's an open source model that takes for a given question, does this document
*  help and how much does it help? And we get a score out of that. And we go through the whole
*  set of emails that we've pulled into memory and we get a score. We take the output of that,
*  we do another pass of heuristics. We end up with a score, we sort that and then we take the top
*  like 50 or so, we send those back to the client. So after all of this, from all these different
*  sources and all this re-ranking and stuff, we finally say, okay, here are the N emails,
*  usually like 30 to 50 N emails that we think are most relevant to answering this question.
*  We send those back to the client. The client takes those and it makes its call to OpenAI
*  and says, you know, basically, here's the question that they're answering. Here's the data from all
*  the tools, right? Remember that RAG is just one of the many tools that we could use. Here's the data
*  from all the tools, try to answer the question. And that prompt also includes a bunch of best
*  instructions about how to format the output. So you'll notice that our AI assistant, it like
*  linkifies threads for you. It does rich text. If it's writing an email, it'll actually look
*  like an email, have buttons and stuff like that. So that is basically done through prompt
*  instructions to GPD4 that force it to output stuff that we can then parse and like turn into
*  UI for you. So we get that response back. We do that parsing and post-processing and linkification
*  and stuff. And then we spit out the output to you and you get a thing that looks like our AI system.
*  Cool. Hey, we'll continue our interview in a moment after a word from our sponsors.
*  The tech world turns to the Brave browser for its unbeatable privacy protections. But did you know
*  that Brave also has a private ad platform? Brave ads offers first-party targeting and it's been
*  cookie lists since day one. So you can relax while third-party tracking cookies disappear from the
*  web. Today, millions of people turn to ad blockers to avoid being tracked and pestered online.
*  But Brave's new ad model aligns incentives for users and advertisers. Users earn rewards for
*  viewing ads, which they can save, spend or pass along to their favorite creators. And advertisers
*  score points for respecting user privacy, generating ROI without invasive tracking.
*  So whether it's high impact announcements on the new tab page or keyword targeted ads in Brave
*  search, Brave offers diverse, private, future-proof ad formats for all your business goals.
*  Join the future of advertising at brave.com slash ads. Mention MOZ when signing up for a 25% discount
*  on your first campaign. Today's podcast is brought to you by Plum. You've probably noticed by now
*  that the AI features in your favorite products kind of suck. They're cool the first time,
*  but pretty soon you're underwhelmed. That's because truly great AI features require complex
*  pipelines and rigorous testing that most startups simply don't have the time or tooling to get right.
*  That's why Plum created a collaborative AI app builder that's purpose-built for product teams.
*  Your users deserve better than a glorified GPT wrapper. Blow their minds with Plum. Check out
*  useplum.com. That's Plum with a B for early access. Hey all, Eric Torenberg here. I'm hearing more
*  and more that founders want to get profitable and do more with less, especially with engineering.
*  Listen, I love your 30-year-old ex-fang senior software engineer as much as the next guy,
*  but honestly, I can't afford them anymore. Founders everywhere are trying to turn to
*  global talent, but boy is it a hassle to do at scale from sourcing to interviewing to on-the-ground
*  operations and management. That's why I teamed up with Sean Lanahan, who's been building engineering
*  teams in Vietnam at a very high level for over five years to help you access global engineering
*  without the headache. Squad, Sean's new company, takes care of sourcing, legal compliance, and
*  local HR for global talent so you don't have to. With teams across Asia and South America, we can
*  cover you no matter which time zone you operate in. Their engineers follow your process and use
*  your tools. They work with React, Next.js, or your favorite front-end frameworks, and on the
*  backend, they're experts at Node, Python, Java, and anything under the sun. Full disclosure,
*  it's going to cost more than the random person you found on Upwork that's doing two hours of work
*  per week but billing you for 40, but you'll get premium quality at a fraction of the typical cost.
*  Our engineers are vetted top 1% talent and actually working hard for you every day.
*  Increase your velocity without amping up burn. Head to choose squad.com and mention Turpentine
*  to skip the wait list. There's a lot there. So I counted, I think, four language model calls in
*  the whole loop, but the first three are open source models. So the first one was figuring out
*  what tools to use. The second one was changing the query to kind of flesh it out with all the
*  proper names and all that kind of stuff. The third one was the relevance between the question and
*  the returned thread. And then the final one is the one that actually goes the heavy lifting,
*  although that all was pretty heavy just to get there. The final one is the open AI one to actually
*  do the final reasoning and drafting. You actually missed a class of them,
*  which is the feature extraction. So after we rewrite the query, we then use a bunch of models
*  to pull out specific features. That's where we look for labels and keywords and each of those
*  is a different call. We do the tool selection, we rewrite the query, we pull out the features,
*  we do the cross encoding, and then we do the answer at the end. So there's serially five calls
*  and the feature extract is actually like five different things in parallel. So there's every
*  time you ask a question to that assistant, we're doing like 10 LLM calls. And I want to note that
*  before we did that, we embedded all your emails, right? So there was a whole bunch of your
*  processing done beforehand, millions, essentially to set up the data to do that. So yeah, there's
*  a lot of LLMs going on. I think how do you do anything? There's a lot of good tidbits there
*  for sure. And maybe some important lessons, just high level as well around how you really do have
*  to engineer a system in today's world. And that's why this is hard, right? It's not just the kind
*  of thing that you can throw straight at GPT-4, even if that is the final step and the one that
*  makes the whole thing possible in the end. The amount of work that goes into that is pretty
*  intense. All these different models, you mentioned HUD and FACE, are you fine tuning those models?
*  Are you hosting those models yourselves or are you able to just use open source and potentially
*  commercial infrastructure? So we have, at this point, we have six models that we're running in
*  production. We use three from an AI. So we use GPT-4, GPT-3.5 and a fine tuned version of GPT-3.5.
*  And I'll talk about how we use that in a little bit. And then on our own infrastructure, we use
*  InstructorXL, which is an embedding model. We use a cross encoding model that's been trained on some
*  data that Microsoft opened source file back. And we use Mistral. And the GPT-4, GPT-3.5,
*  the cross encoding model and Instructor are all used for RAG. It's all the stuff I just talked
*  about. The other two models are used for other features. So the Mistral we use for our summaries,
*  we may end up using Mistral for more things because we've been quite impressed. And it's
*  something that we can run on our infrastructure, which is a lot of benefits. So I think we'll be
*  using that for more. But right now that's used for our summaries feature. And the fine tuned GPT-3.5
*  we use for our AI operable. So I don't know if you've played with this. Have you played with this
*  feature? A little bit, not as much. I've been so enamored with the Assistant that I haven't gone,
*  this is more like a GitHub co-pilot to inline experience, but I wouldn't say I've spent as
*  much time with it. The idea here is people liked the writing. They thought the writing was good,
*  but you know, opening up the pane, asking a question was kind of a slow UX. And like,
*  we want to try to just streamline that UX and give you basically the same quality of answers
*  that you get, but without having to do that on the side. And we were using a similar system,
*  but what we discovered was that GPT-4 was too slow to do this. So we needed to use GPT-3.5,
*  but GPT-3.5 just wasn't smart enough, especially not smart enough to get the nuances of like,
*  what completion would be in various different cases, right. But we found that you could really
*  effectively fine tune for that use case. So basically what we did is we took some of our
*  own emails. So not, you know, there's no customer data here because it's truly our own emails.
*  And we did the thing where you, you know, take an email, you remove a section, and then you train it
*  on the correct answer being the actual email you set in the first case. So it's one of the,
*  your data set is emails with sections removed, and then the correct output is the section completed.
*  And we did this in a bunch of cases. And this taught it kind of the formatting and like generally,
*  how emails should work. And that combined with the RAG approach that I talked about and some
*  prompting was enough to get the voice right as well. So basically it's a prompt where it's like,
*  you know, mimic the user's voice. Here's a whole bunch of examples of that. And then it's
*  get the facts right and a whole bunch of examples of relevant facts for the emails. And then a fine
*  tune model to try to get the formatting right. And then we put that all together into that,
*  that autocomplete. And is that the same experience that's doing the drafting if it's in the
*  assistant versus if it's in the autocomplete or that's a, it's a different drafting stack?
*  It's a little different. So there are a lot of similarities in terms of we pull some of the same
*  emails for context. The prompts are very similar, but the, I think there's two big differences that
*  you get in the assistant, which is why I think you'll find if you do the assistant, you actually,
*  you do get slightly higher quality answers. One is the assistant is usually GPT-4 turbo,
*  because people who are doing that are willing to wait a little bit longer. And so, okay, it's a
*  little bit slower, but like, we'll use that. So you do get the benefit of a more powerful model.
*  The other big difference is in the AI assistant, you can do regular searches as well. So for speed
*  and for UX reasons, when you're doing autocomplete, we're only looking through
*  emails that you have sent in the past. And we're only giving autocompletions of like things that
*  you have said, facts that you've shared in the past. But in AI assistant, you can also say things
*  like, you know, find the order number for my Amazon package from last week and insert that
*  into the email. And because you could be like so explicit and because people are willing to wait
*  longer, we'll do sort of like arbitrary retrieval for you when writing those emails. So you get more
*  capabilities. Gotcha. Interesting. Any tips for fine tuning three, five, one that I've shared,
*  and you might have a kind of twist on it, is the importance of training on reasoning. So for Waymark,
*  we have a very different use case, but honestly kind of a way less intensive in terms of retrieval,
*  but kind of comparably complicated to set up in that, you know, ultimately we're like putting
*  together a video and that's a multimodal thing. And so there's like, you know, whatever, six
*  different models in production, yada, yada, yada. The fine tune three, five is our script writer.
*  And we found in the early going that we could not get the scripts to really sing for us. It just,
*  we did not, we weren't pleased with the quality. And the big step that got us over the hump to
*  where it was like, okay, yeah, this is good to go and better than what we had previously was
*  including chain of thought reasoning in the training data, which then also of course gets
*  it to do that chain of thought in the, you know, in the actual generation at runtime.
*  And by kind of teaching it how we want it to think about the kind of script that it should be
*  writing. We got just like dramatically better results than training it just on the examples
*  themselves. So I wonder if you have any other, you know, kind of doing something similar or any
*  other tips for the fine tuning. Cause that was a huge unlock for us. I'd love another one.
*  I feel like I just learned something really cool. That is we, we don't include like chain of thought
*  examples of the fine tuning, but that actually would be really cool. I had not considered that.
*  I would say for us, we had tried in the past to use fine tuning for stuff. And I just,
*  it never really worked for us before. I think the issue is you gotta get the right data set.
*  And with this particular data set where we have, basically we can take a few set number of emails
*  that you have set like real emails and do the, you know, remove a part and then tell it to complete
*  that part and then tell the right answer is the part that was actually there. That approach has
*  worked really well. So I think if you have a really good data set to work with, I've been pretty
*  impressed with the results. And I think one of the things that surprised us is how well it's
*  generalized. We were a little bit worried that like, it would just start writing the same emails
*  that we had written and that did not happen. It actually generalized super well and continued to
*  respect like the context in rag, which was a pleasant surprise. So, but very happy with that.
*  But yeah, that chain of thought thing, that's, that's the thing we should check out.
*  So yeah, I want to make sure I understand your approach too, cause there might be something here
*  that I can use also. It sounds like you are first assembling from your own email history,
*  a bunch of long threads where it's like fill in this blank in this email and you show it the
*  thing to be filled in or, you know, with the, with the piece missing to be filled in and then, okay,
*  here's the missing piece. So you set up a number of those and then you do that also at runtime for
*  the individual user. You're bringing in the kind of synthesizing that on the fly and saying, okay,
*  here are whatever 10 examples of this from that user's own history. And now the AI's job is to do
*  the last and it's learned the task from your data, but now at runtime, it's doing it on the
*  individual users data. Precisely. The, the prompt that we use here is we're doing retrieval. When
*  you do auto-complete as well, when you put your cursor into that, to that input, if you have AI
*  auto-complete turned on, we're running two queries. The first query is find emails that you have sent
*  that are in reply to similar trends. So that the KNN we're doing is off of the emails above.
*  We're saying when the user got an email like this before, how do they respond? And we're pulling
*  examples like that. And the prop says, you know, here are some emails that the user has sent
*  previously in response to similar threads. We also look at the drafts that you're writing. So if you
*  say, you know, my address is colon, you don't necessarily, it's clear to us that like, maybe
*  you just want us to find places where you talk about your address. So we separately do another
*  query where we say, take the draft they've written, embed that and find emails that they've
*  sent that are similar to the draft so far. And we pull both of those and we put those into the
*  prompt. And with just stock GPD 35, that kind of works, right? You, you can tell it, you know,
*  here's an email that they've sent. Here are some emails that they, you know, are similar to the
*  draft. This is what they've written so far, give us the completion and it kind of works. But the
*  problem is it doesn't get kind of the, the, the formatting, right? It'll, you know, rather than
*  give you a sentence, sometimes it'll give you two paragraphs. Sometimes it'll give you two letters.
*  It will screw up the white space for things. It will not really sound like an email, like emails
*  sort of have a certain, certain style for them. Sometimes it will repeat everything you've said,
*  so on spit out the full email. So it doesn't really get the nuances of the like following
*  instructions. And there's a lot of examples that give you like little detailed nuance things where
*  you're like, Oh yeah, I could see why I would figure that out. And another thing, it actually,
*  here's a funny thing that I had to learn from training. It didn't do a good job of pulling
*  facts from history. So like one of the, one of the examples I like to show people to come visit is
*  like our wifi password is colon and like it can auto complete the password, but without fine tuning,
*  it couldn't figure out that even though there was an email above that was like my password is law
*  that it should put that into completion. And so what we do is a fine tuning is we have a script
*  that we run on our own inboxes that like pulled up the emails that we've sent for each one of those
*  assembles a prompt, including all of the rag information necessary to construct that prompt.
*  So we have a full set of what the real prompt would have been for that user in that case.
*  We understand what the real email that was sent. And then what we're fine tuning on is the real
*  prompt that would have happened in that case with us picking a random sentence that we like remove
*  half of it from. And then the round truth being what the email was that was actually sent.
*  In that case, and it teaches it formatting. It teaches it like what an appropriate links would
*  be for completion. And it also teaches it stuff like, Hey, you're supposed to like copy paste
*  facts from above and like put it into the thing below. Most of that's like real emails, but we
*  also insert for, for cases where we ran into places where it was like not well behaved, we inserted
*  contrived examples of here's a case that we would like you to handle this way. And I have a bunch of
*  those in the training data set as well. With all of this stuff going on, it is striking to me that
*  the experience is pretty fast. I mean, when I do the chat, of course there is, you know,
*  a little bit of a wait, but it's not like, you know, just the hearing all of the, all of this
*  discussion and all of the stuff that's going on under the hood. I would expect that people might
*  think that it's slower than it is. It's pretty responsive. I guess, you know, there's probably
*  a lot that goes into that, including just years of database expertise, any rules of thumb there,
*  you know, paralyze everything that can be paralyzed is kind of one of my mantras. What else would you
*  say people need to keep in mind? Paralyze everything you can paralyze for sure. Pipeline
*  everything you can pipeline if you can. So for example, like we start crossing coding stuff
*  the moment it's coming out of the database, we're not waiting until all the results are there.
*  Use faster models when you can, right? So we're using GP3.5 and find your GP3.5 and Mistral. And,
*  you know, when, when we, when we can, because those are faster use BC hardware. So like for the,
*  for the summaries that we're generating, like those have to be really fast. So we have
*  rather expensive GPUs that are doing that part. Keep the output short. Here's one of the things
*  we struggle with. You mentioned a chain of thought, like chain of thought helps in our cases too.
*  We only use it in some sparing cases because it takes performance hit because you have to wait,
*  because the chain of thought goes above the answer if you actually want to have an impact,
*  but you have to wait for it to come out. So in any case, we're like,
*  performance is really important. We don't want to wait for the chain of thought to spit out before
*  the actual answer fits out. And so what we found is, you know, it's usually for us worth it for us
*  to take the reasoning hit versus take the performance hit. And so in most cases, we're
*  not doing chain of thought. And Tropic recently put up this paper on sleeper agents and they
*  did a really interesting thing where, you know, the goal of this research was to kind of test
*  whether certain safety techniques that are routinely applied, like your RLHF and so on,
*  are enough to protect us from models that may have been like poison or backdoored.
*  So you go on to hugging face, right, or the open web, you download a model. To date, we really
*  haven't seen much of this, but certainly in the future, you could imagine, well, you know,
*  where did that model come from? I sometimes joke like, dude, don't put your mouth on a language
*  model. You don't know where it came from. And, you know, that again, hasn't been too much of a
*  problem yet, but you can imagine all sorts of ways that people might poison the behavior of a
*  language model if they want to, you know, steal your information or cause havoc in any number of
*  ways. So and Tropic created a version of this in-house for the purpose of studying it. And then
*  they looked to see, okay, we train this model to be problematic in a particular way. It was like,
*  in, you know, as long as the date is 2023, you write like normal harmless code. But when,
*  when the date becomes 2024, then you write like malicious code. And then they go and try,
*  well, what happens if we like RLHF or, you know, apply our constitutional AI techniques?
*  Does that clean that up or does that problem persist through these like standard protocol
*  safety techniques? Anyway, what they find is that unfortunately the problem persists, like just
*  applying your RLHF, if you don't know what the attack is, then like a standard RLHF is not going
*  to be enough to eliminate that behavior. So subject of future work is, well, how will we,
*  you know, potentially figure out how to eliminate that behavior? But anyway, the purpose of all this
*  was they had three versions of the model that they studied. One was one that just spits out the
*  answer and they tried it, you know, to, to do the problematic thing when it sees a certain trigger.
*  Another one was one that they had the chain of thought training built into it. And then there
*  was the third one in between where they initially trained it with the chain of thought, but then they
*  did additional training to remove the chain of thought behavior. And so it was something kind of
*  in between that has this like chain of thought learning, but doesn't actually do the chain of
*  thought at runtime. And they were interested in that for kind of like obfuscation reasons,
*  right? Like if you're doing a deceptive model, of course, you're not going to do the chain of
*  thought version that would, you know, tell your user like now it's 2024. So now I'm going into
*  malicious code mode and that's literally what the chain of thought one does. So they wanted to kind
*  of teach that logic and try to instill that logic, but then not have it emit that explanation.
*  And the results of that work, I think are super interesting, but it does make me think that
*  possibly you could get better reasoning by fine tuning on chain of thought and then maybe
*  subsequent fine tuning to not actually have to do that anymore and possibly get, you know,
*  a little bit farther out on the, on the Pareto frontier of possibility without having to wait,
*  you know, for all those tokens to be generated. Anyway, sorry for the long digression, but this
*  is what we do here is go, you know, go hard on these questions. Totally. No, that sounds,
*  that sounds very cool. Yeah. I'll have to, I'll have to check that out after this.
*  Part of the reason I think this could work for, for the purposes that you have is doing the chain
*  of thought made the RLHF even less effective at reversing the problem. So it was like, you know,
*  the behavior is more deeply ingrained in the model and like less, you know, quick to be removed. But
*  if you could apply that to a positive use case, then obviously you might have something,
*  might have something good on your hands. Anything more in the, in the stack and in the,
*  how it's working that you think would be interesting to people?
*  We put out that blog post in October, like this, how this works at the time, you know,
*  this was cutting edge and we thought it was cutting edge. We actually, at this point are like,
*  that whole thing is obsolete. Everything we did, that's old school. We got it. We got to redo it.
*  And basically every part of that stack, we are now looking at how we replace it with something new.
*  The overall framework that we're using is working pretty well, but I think each part,
*  like every single part of the thing we talked about, there's a better, better approach. So
*  I mentioned with like tool selection, when we, when we initially did the tool selection,
*  we struggled to make fine tuning work the way we want. And so it's GPT-4 turbo with some prompting.
*  And I think now maybe with what we've learned and potentially with, with Mistral, it is now reasonable
*  for us to do the tool selection that way, which has both cost but also performance benefits. We
*  can do a Mistral call much, much faster than a GPT-4 call. So on the tool selection side,
*  we have a faster, better way to do this with some fine tuning with another model. Same thing for
*  the rewriting of the query, the feature extraction. And like one of the things we're looking at there
*  is like, maybe that shouldn't be two steps. Maybe this should all happen at the same time. Maybe
*  there should be one bigger, smarter prop that like takes all of the context and pulls out that
*  information. On the search side, we see a lot of them, but it's better embedding models. Like the
*  embedding models are getting better very quickly. The one we're using, you know, we pulled out for
*  Vodk phase like almost a year ago, you know, and there's a lot of other ones we're looking at now.
*  On the vector database side, they're starting to separate compute storage, which gives us a nice
*  cost benefits of, you know, we have a lot of storage and a lot of little documents and we don't
*  do a lot of searches. And so it may be practical for us to use embedding model with a bigger vector
*  and switch to like the PyCon and host solution and still get a cost effective
*  method and get better results for the cross encoder that we have. I think there are better
*  re-ranking approaches. And this is one where I don't know that I have much to say right now,
*  because we're still like very much in the middle of trying to figure this out. But, you know,
*  there are better cross encoders. There are better techniques in general. So we're going to look at
*  other approaches to re-ranking that we can have. And there's also just a lot of sort of traditional
*  infrastructure optimizations that we can make across the stack to like improve performance and
*  do filtering in various ways. So yeah, we're going to be ripping that whole thing apart,
*  reassembling and hopefully, you know, today I think you probably found the AI assistant,
*  like sometimes it gives you a magically correct answer with the right link. And sometimes it
*  doesn't. It gives you, you know, not the right answer. It tells you it doesn't have an email
*  that does. And the goal is to make it so you can actually rely on it. Like, you know, you ask the
*  question, it gives you the right answer and you can trust to do that every time. But we're not
*  there yet. Yeah, certainly none of these systems are fully reliable. But I will say again, I have
*  been really impressed by how consistent it is and just how kind of solid it feels. I also really
*  appreciate how you surface. It's a very nice UI and it gives me kind of visibility into, you know,
*  when something is happening. I've got a couple of minor suggestions for you. One is today, the
*  threads that are retrieved and the threads that are used are kind of shown at the end of a
*  generation. Sometimes I'm like, I actually would like to see that even before the whole process
*  is done. But in any event, I really do like the UI where it says like, okay, this was based on
*  six email threads or whatever. And then I can click into that. It opens up not just the ones that
*  were used, but also there's like a line above which are the ones that are used and below
*  which are the other ones that were returned but not actually used in the generation.
*  So I think that's pretty cool. And I also love how then it allows me to just
*  re-rank them myself manually if I want to and, you know, kind of fire it again. I think that
*  is really cool. And my only suggestion on that particular thing would be maybe even just bringing
*  that up sooner as opposed to waiting for all of the process. I don't know if there might be some
*  like gating thing that would prevent that. But another thing, as long as I'm given a couple
*  simple tips, I would love a verbal, like a first class, just audio into it. Even if I'm sitting at
*  my computer, I do feel like I formed the thought really quick. I could spit it out really quick.
*  It takes me like another five seconds to type it. And then I'm happy to wait. If I could bypass the
*  keyboard and just literally speak to it, I think that would be at least something I would be very
*  interested in using. I don't need it to talk back, I don't think. Maybe occasionally, but yeah,
*  mostly I'm at my computer or perhaps I'm on my phone. But yeah, I think I just want to talk to
*  it. Just the pure convenience of data from, you know, what's the fastest path? Eventually I'll put
*  a device on my head and just think like, hey, do this email assistant. But until then, you know,
*  then speaking to it would probably be the fastest versus typing. Although, you know, these things
*  are getting remarkably good as well. I'm sure you've seen some of this stuff, but the ability to,
*  with fairly intensive hardware, reconstruct what somebody is seeing or reconstruct the text that
*  they are thinking about purely from measuring the brain is, and when I say intensive hardware,
*  we're talking like fMRI. It's like not the kind of thing you can wear around, but it's also not
*  necessarily something that is invasive in the sense that it doesn't like require surgery or,
*  you know, implantation or anything. That stuff is where I have a whole fascination with that.
*  That's another topic, but yeah, voice would be, you know, a nice intermediate upgrade that
*  wouldn't require anything too, too crazy. I think we'll probably do voice pretty soon.
*  Up until two weeks ago, we didn't have the mobile assistant. So that's a very new thing.
*  We're getting a lot of feedback from professors about this, but I personally have found on mobile,
*  especially most of the time, I want to talk to it because I have two common use cases on mobile.
*  One is I'm looking for something like, you know, where was that restaurant? And I'm in a hurry and
*  I don't have time to type about this stuff. I'm using AI assistant, so I don't have to like figure
*  out what search to run. And the other use case is I want to send an email, but I don't have time,
*  again, to write a nice email. And so I want to use a combination of dictation and an AI that could
*  write like me to like turn my garbled rambling into something well-written. And both of those
*  are voice. So I like the majority of the AI mobile for me is voice. And I just use the built-in
*  dictation. Your experience is probably similar to like the built-in dictation on the iPhone is not
*  as nice as whisper. And I would love to, I would love to update our experience then. So we'll,
*  we'll probably be doing that. And then a desktop, I'd, you know, the same thing, although less,
*  less happening for me because I got coworkers sitting around, but.
*  Yeah. I'm in my home office and you know, it's just me. So I can, I can be as weird as I want
*  to be behaviorally. You mentioned getting feedback from customers and I, one other comment that you
*  made the first time we chatted about all this was that, and people will know where this money is
*  going with all the detail that you've shared on the imports and the many calls and all that kind
*  of stuff. But as I understand it right now, you are losing money on every customer because the
*  subscription, which is a, I forget exactly the price because you were kind of just to give me a
*  free account, but it's like, you know, in line with kind of the other things that people are
*  accustomed to paying for as a retail SaaS subscription, apparently does not cover the cost
*  of delivering on all of this processing magic that is going on. So I'd love to hear about kind of
*  the strategy that goes into that. Like where are you in kind of the business development? Are you
*  trying to get new users or would you tell people, Hey, you know, no need to rush into it. We're
*  losing enough money. This is actually, I think kind of a central part to the strategy. So if you're
*  doing a startup, you want to ride, you know, whatever the trend is that's happening. I think
*  the right time to launch a feature or launch a product is right before it seems possible.
*  So in the case of AI assisted, I think, you know, no one else had released something like what we do
*  in email. I think a lot of people were like, we're not quite there yet. And that's what you want to
*  get it out. And there's, you know, a few different ways it can be impossible. One is that the
*  technology actually doesn't work. And if you can, you know, be that fast, awesome, right? If you can
*  build just better than they want, awesome. Another way is like, no one's took out the product behavior
*  and you're the first one to turn around to product behavior. But another way is the economics don't
*  make sense. And if you have confidence in the trends in the economics, you can afford to make
*  that investment and you can, you know, cover the gap with such capital. And then over time, it'll
*  make sense. And the best example I have of this is YouTube. So YouTube was losing money like crazy
*  because at the time serving that amount of video infrastructure was really expensive for bandwidth
*  and for storage and for re-encoding the videos and stuff. And that obviously worked out real well.
*  And so I think we're at a similar stage where the cost of the stuff that we're relying on is dropping
*  very quickly. And we are right before the part where this is going to look broadly economical.
*  And, you know, people are going to know how to build these in general and the product experience
*  is going to make sense. And we want to be there, you know, just before everyone else thinks it's a
*  good idea. So that by the time everyone thinks it's a good idea, we've got something really solid
*  that works great and has a bunch of customers and is like battle hardened and we can take full advantage
*  of that opportunity. So yeah, we're absolutely open business sign up. We got venture backing
*  to make this work and you get the benefit of a lot of money being spent to give you a premium
*  experience. Yeah, it's cool. One of the things that you mentioned earlier was the kind of relationship
*  between this product and an assistant. You said, you know, people pay a lot of money for an assistant
*  and, you know, maybe we can create something that delivers always part of that value. I am working as
*  an AI advisor at a friend's company that is in the executive assistant space. And one thing I would
*  suggest is I think this is a phenomenal tool for an executive assistant because so I have an appointed
*  assistant as an advisor to the company. And the degree of difficulty though for her to go in to
*  my email, you know, as I said earlier, the account's 20 years old, right? So there's a lot in there.
*  She doesn't know the context. She doesn't know, you know, all these different things,
*  but just to search effectively through my very cluttered inbox is a huge unlock to her. So I
*  think one of the things that I'm kind of interested in doing after this is going and trying to do some
*  sort of pilot or study with the assistants and say like, is this something that could allow the
*  assistant to do a lot better job on the email? I think it may be, I'm interested in your thoughts
*  kind of more generally on this, but I'm definitely not one to shy away from the notion that AI
*  substitutes for human labor. I think that's like a clear reality and that, you know, denial of that
*  is often kind of a cope. But in this case, at least at this time, I do see a lot of complementarity
*  even between the AI assistant and the human assistant. Yeah, I fully agree. And I don't
*  pretend that our, you know, our little email assistant here is going to do everything that
*  a real human assistant could do. And we do get a fair amount of requests from folks to do better
*  support for like a delegated inbox for specifically for that use case so that their executive assistant
*  can use it more easily without like sharing login credentials. I think it could be awesome for the
*  assistant as well. And I think today that people are using it as their AI assistant are not
*  necessarily replacing their human assistant. They're using it in addition to, or they're using it
*  because they can't afford the human. Yeah, I think you also kind of alluded to the idea that the
*  vector database could easily become like the dominant cost driver kind of across the entire
*  stack though. I got the sense that, and also just looking at some of the results, you know, as I was
*  using the AI assistant and just digging in to see, well, what is it actually retrieving?
*  I got the sense that a massive thinning out of my inbox might be really good for like every aspect
*  of the system. Like it might make your costs go down a lot. It might make things more, you know,
*  could reduce latency perhaps in some parts of the process as well. And I honestly would just love to
*  like get rid of a lot of old stuff. I'm paying storage, you know, overage with Gmail. So, you
*  know, for many reasons, I'm like, I wonder if there is a future where as like part of the onboarding,
*  you could help me like just get rid of a ton of stuff. Like 90% could go, I think, from my
*  inbox. Is that something that you're thinking about? I guess the cost for cost pressure reasons alone,
*  it seems like that that's got to be something that comes up. I would love to. And I would say
*  the number one feature request that we get is people want the AI to help them more with triage
*  and just managing their inbox. So today we'll have great emails. We'll help you search your emails,
*  but like actually getting rid of the stuff in your inbox. We have some features, like even like
*  multi-select things that you can ask questions about those things and it can help you prioritize
*  and stuff like that. But it isn't really doing the, you know, the executive assistant that would come
*  in and be like, we're just going to delete 9% of the stuff. It doesn't get, it doesn't do that for
*  you yet. And the reason is just, we're trying to start with the things that are sort of safer and
*  lower risk and ship those and then work into the harder, higher risk things later on. And like an
*  AI that goes and like deletes bunch of your email, like you really got to have a lot of confidence.
*  So we're, we're trying to work our way in that order, but I think there's a ton of opportunity
*  here and there's a ton of demand here. And as an example with the embeddings that we're doing,
*  one of the things that they can, that can allow us to do is clustering. So we can say,
*  Hey, we're going to look at your inbox. We've embedded all this stuff. We have an vector database.
*  What are the groupings in here? And we go here's, here's a crazy idea. Like, why don't you pull up
*  your inbox and we're like, not here's all but the threads. We're like, here's like a typical Tinder
*  style card that you like swipe left and right with like each of the sort of rough categories of stuff,
*  right? Here's the stuff related to like your podcast next week. And here's all the junk from
*  this marketing website. And, you know, here's all your newsletters and like those groupings could
*  potentially be custom to you and we can provide recommendations for what to do with them. So
*  that's, that's an idea, but we have a lot of stuff like that we're looking at doing. And I think the
*  embeddings of the vector database with the capabilities it gives you are sort of central
*  to making that stuff work. It's a good reminder that, you know, it's commonly said that we're
*  still very early in this whole platform shift, but that's another good reminder. And, you know,
*  certainly the interfaces are not yet anywhere close to probably what they will ultimately be in,
*  in mature form. One thing you'll notice in our UI right now is that the AI can't actually do anything.
*  You can ask it things, it can recommend things, it can give you buttons to press to do things,
*  but the only way to take action is actually for you to click something. And that's very intentional.
*  We want to make it so that you as a user are totally comfortable asking the AI anything,
*  knowing you a full control, like nothing will ever get sent on your, without your knowledge
*  or control, nothing will ever get deleted or archived or whatever, unless you click a button.
*  I have noticed that, although I hadn't quite formalized it so crisply. Let's talk about the
*  future a little bit. You know, you mentioned early on that the idea was to create a collaborative
*  email without even knowing that I was thinking, boy, if you could do for Slack, what you've done
*  for email, I would be pretty into it. You know, just the ability to go fetch contacts. I mean,
*  in Slack it's probably even worse. The search is not good. And, you know, it's a real nightmare
*  to try to go collect the threads that I would need to reference to figure out what's going on.
*  And then, you know, of course, drafting things could be extremely helpful there as well.
*  A bit of a different modality in terms of, you know, style of writing. So
*  certain, some interesting nuances, but that's kind of where my, you know, instinct would take
*  you from where you are right now. But what are you thinking about as kind of the future of the,
*  of the overall product? Yeah, I mean, we're very excited about collaboration stuff in the long term,
*  but I might suggest really what, what I see happening is a reframing of how people think
*  about their inbox. I think up until today, it's been like a pile of to-do's that I have to deal
*  with. And they don't really feel like it's a thing that's adding value to their lives.
*  And I look at it with LLMs and with the automation we would like to build if it was like auto triage
*  and stuff, being more of a knowledge base, right? It is, it is a corpus of information about like
*  everything that is going on at your business and everything you've ever sent and everyone you've
*  ever talked to and all of your SaaS notifications, all of your meeting invites and everything. And
*  we can now mine that to do useful things for you. So for example, like before we recorded this,
*  it could pop a message up and being like, Hey, you've got this call coming up and here's who
*  this guy is. And, you know, here's some of the special that you've had in the past. It could do
*  that sort of thing proactively. So I think it's, it's going to be a reframing from a tool to send
*  and receive messages to a knowledge base that knows all about you, that can help you get your job done.
*  I think that extends into your team. Once you say, okay, for me, if the knowledge base helps me get
*  my job done, what if that is also a knowledge base for other people? So a simple example of this would
*  be, you know, you and I now have interacted, let's say at some point you start talking to one of my
*  co-founders, it'd be really useful probably for my co-founder to know that you and I have been
*  chatting and have some insight into what we've talked about. And there's obviously lots of
*  privacy things we have to think about there, but wouldn't it be cool if like his AI assistant could
*  talk to my AI assistant and get some insights on things that I was comfortable sharing and use that
*  to help him with his job. So I see us, you know, going deeper into the very normal collaboration
*  things, like what if you want to like chat with a group at your company or you want to share a
*  thread or you want to collaborate on a draft, but also potentially sort of next gen AI things about
*  like, what if your company had a global AI that knew all about everyone's AIs and could help
*  drive the business forward in interesting ways and advise people with like the full knowledge
*  of everything that is going on. It's going to be weird, but it's going to be awesome.
*  That's kind of a version, an interesting version of, you know, I don't know to what degree people
*  usually think of it as a utopian or dystopian or not even sure, but there's certainly a lot of talk
*  about kind of, oh gosh, you know, now my AI can write my emails for me, you know, amazing,
*  what a great productivity boost. And then, well, geez, you know, I can probably scale up what I'm
*  doing in terms of like outreach by a hundred X or a thousand X, right? I can, you know,
*  if I'm recruiting, I can do personalized high quality outreach to like every profile. Or if I'm
*  doing lead gen or sales, I can, you know, do personalized high quality outreach to every target.
*  And then it's like, that'll be so much more effective. And I think, you know, one of the
*  things that is not well theorized yet at all is just kind of, where does that take us in terms of
*  like a new equilibrium? Because we all tend to think about this, I think you're ahead of most
*  based on just your last comments, but, you know, so many people are like, I'll do this,
*  then I'll have an advantage. But they don't take the next step of thinking, okay, well then what
*  happens when everybody does that? And then what happens when everybody's inbox has got nothing
*  but super high quality, you know, highly personalized outreach. And then you're like, well, geez,
*  now we just have like my mass customization AI talking to your mass filtering AI. And how do we
*  maintain any sanity in a world where our respective AIs are talking to each other
*  at like a frequency and a volume that we individually as humans cannot even keep up with?
*  Probably the most common question like this that I get is, hey, if my AI is writing an email,
*  and then their AI is summarizing the email, and I write roll of points, and they read
*  bullet points, like, what's the point, right? Why don't we just send the thing in between?
*  And my experience, now that I've been doing this for a while, like a lot of my emails now,
*  how some AI generate portion to them at this point, and my experience is, the better we are
*  doing our job of like helping you generate the emails, the more they are exactly like the emails
*  that you had before, right? If we're doing a great job, the email that you write should be no different
*  whether we help you write it or not, we simply help you do it faster and we help you make fewer
*  mistakes. And I really believe that and I think we can do that. So the hope is not that we're like
*  taking your thing and making it more verbose and their thing is being trunk and then they read that.
*  The hope is all the emails that you're sending look basically the same, they're just a little
*  more correct, and you can just get things done faster. The question of like, okay, fine, the
*  emails are the same, but there's a lot more high quality emails going around, I think is a very
*  real one and something we're going to have to wrestle with. And I think what's going to happen
*  here is, yeah, to some extent, the AI is going to help you triage them and things like that,
*  but I think also the social network is going to start to bear a lot more, right? So like,
*  personally, I filter partly based on the content of emails, but a big part of my filter is like
*  where I met that person, right? So like in your case, like I got an introduction to you,
*  and you probably read my email because you knew the person that introduced me. I think that sort
*  of thing is going to become even more important of like, who's connected. I think in the case of
*  business, like if you have a relationship with the business and you email me, like I should be
*  able to know about that and I should know if it's not spam because there's a relationship. So I see
*  like higher importance for relationships in the social network and less importance on the actual
*  content of the email because that's much more easy to engineer over time. That does seem likely true.
*  I mean, certainly already it's tough to get people's attention if you're emailing them totally cold.
*  It does seem like it might get much harder, even if your outreach is really good. How much do you
*  kind of fly at this point? Have you ever had any experience, for example, where you like
*  generated something, we know that the AI can't take that action directly on your behalf, but
*  yeah, looks good, click send, and then you get a response and you're like, what did I say? I mean,
*  you would be on the cutting edge of that sort of perhaps falling into over-reliance or
*  any anti-patterns that you're noticing in yourself. That particular case has not actually
*  happened yet. Maybe it will. Maybe I'll get to the point where I'm so used to it that I do that, but
*  the UX that we have for AI writing right now is the assistive pane, which is like a fairly heavyweight
*  interaction because you're like chatting back and forth and you gotta click buttons. So it's not
*  something that like you totally go, your brain goes to like autopilot mode. And the autocomplete
*  that we have today is something that you have to like tab complete like one sentence right at the
*  end of time. So it takes a little while to get to the email. So that hasn't come up. We are thinking
*  about what does it write the whole graph for you? And it might get a lot easier to go like full
*  autopilot mode when the whole thing is just sitting there and you can just press send.
*  I do wonder how that'll evolve. And I think we could probably catch some stuff there. We can
*  probably be like, are you sure you read this? You got the right relation. You clicked it like one
*  second later, we could like alert you or I don't know, maybe we do what the Teslas do where they
*  like track your eyes and you're like, oh, you didn't really read this email. I am kidding about that.
*  Although the Teslas do do that. You're not kidding about that part. Oh yeah, for sure.
*  One question that I think you are perhaps uniquely well positioned to comment on is like what's up
*  with Google and their sort of journey on this front? Like there's a million jokes about it
*  takes eight product managers to change the color of a button in Gmail, et cetera, et cetera.
*  They are starting to do integrations of language models into more different products. Now we've
*  also got Gemini shipped and it is really quite good, at least in the main Gemini advanced down
*  the fairway product experience. What would you expect from a Google or a Gmail going forward?
*  Like, is it just going to stay this way or do you expect, are you kind of in the process of waking
*  up the giant? Like what's your model of where Google is going? It's helpful context that I was
*  at Google for a while and I actually had some of the ex Google inbox people on my team there. And
*  I, one of the first things I did when we shared this company is I talked to a bunch of people
*  that worked on inbox and got some insight into, you know, why it was, it was shut down and what
*  they learned from them. And so I think I have a decent amount of insight into Google and how
*  Google works in this regard. And one of the things I got to appreciate when I was there was,
*  I should say Google's a really well-run company. I generally really respect Google. They make great
*  products and you know, it's amazing the stuff they can build, but in a company of that size,
*  when you have a product with as much legacy as they do, with as many users as they do, that has
*  many different goals that it's trying to achieve internally, it is really hard to innovate rapidly
*  at a high quality. And this is for like more organizational and personnel reason than it
*  is for any technical reasons. And I can give you a little bit of specifics with Gmail where they
*  have many goals. The most important goal for Gmail at Google is actually not to help you get your
*  email done, it's to get you to sign in because they want you signed in so that when you do Google
*  searches and stuff, they can associate that with you. They have a secondary goal, which is it's
*  sort of the anchor for Google workspace. And a lot of things sort of tie in there for all the stuff
*  that they provide in Google workspace and Google cloud. And if you look at what they're doing now
*  with AI, it really appears to me, I think this is the case that some mandates didn't came down from
*  on high saying Google of the company is outgoing hard to AI. We've got these other teams that are
*  building some really great AI stuff. You guys need to add some AI. And I don't know if you've
*  played with the stuff that they've built, but everything they put out so far has been like that.
*  It hasn't been some bold header product on Gmail being like, we are pivoting this thing and we are
*  going to be this revolutionary new AI thing. It is this organization of a bunch of people being like,
*  we got to meet some OPRs, let's plug a thing in here, let's plug a thing in here, let's plug
*  a thing in here. And without some visionary product leader in Gmail saying, we are going to rethink
*  everything about how this product works. We are going to make an enormous infrastructure investment.
*  For example, if they wanted to embed all of your emails, put them in a vector database
*  with their 2.5 billion users, that would be a massive expense. There needs to be a visionary
*  leader that really wants to make changes here. And while those people exist at Google, it's really
*  hard to be that person on a legacy product like this. If you're that person, it's much easier for
*  you to be like, I'm going to do this for Gemini or I'm going to do this for some new product
*  initiative. It's a much easier path for the career progress you want to make on one of these new
*  things. And to go back to Gmail and be like, I'm going to take this giant supertanker and try to
*  turn it. So I think it's going to be hard for them to quickly bring the sort of organizational
*  leadership that they need to turn the ship and do something really interesting. So they'll ship
*  incremental things and there'll be other teams at Google shipping stuff, but I don't think they will
*  themselves. I'll give you an example of this. So they have two different products that are attempting
*  to do something similar to the AI search that we do. Neither of them is close in terms of capability,
*  but they have two different ones. One of them was a feature that they sort of pre-announced as part
*  of Duet AI last summer. And there was some screenshots put out and like I talked to the
*  sales folks there and I was like, Hey, can I try this? And they said, it's not ready yet, right?
*  It may be next year. So the one of them is kind of a prefer for external users. The other, which
*  actually does work and you can use is the integration they have with Bard, now Gemini,
*  but they had an integration there, but that integration very clearly was built by the
*  Bard team, right? So the Bard team is moving fast and they're trying new things and they're
*  experimenting with the product, but the Gmail team itself isn't. And so you might end up having
*  like a better, it may be going forward, like your experience search, your emails can be better from
*  Gemini, your Gmail inbox itself because of the way that sort of organization incentives work.
*  Well, I could certainly see a scenario where you might end up back at Google again. I don't
*  know if that's something you would be excited about or open to at all, but I have been really
*  impressed with the shortwave experience. I am not an inbox zero person. And honestly, you know,
*  I'm not even sure I aspire to be anymore, but what I want is kind of, you know, what you're out of
*  certainly on a very good trajectory toward providing, which is just the ability to
*  ask for help and get it and, you know, not have to think too much about it. I like thinking about it,
*  you know, as we're here talking about it, but in my daily life, you know, just to kind of make it
*  fade into the background and just respond effectively to queries and, you know, search
*  effectively. It's been an impressive first couple of weeks on the product and I'm excited to use it
*  more and also to see where you guys continue to take it as you evolve. That's awesome.
*  Most of what you see is a V1. We move fast. We'll be shipping new stuff. And yeah, the goal is
*  that you don't think about it, right? Like most people who use our product, their job isn't to do
*  email. Their job is to do something else. And we want to get the email out of the way so they can
*  do the thing that actually matters for them. Really, really appreciate you having me on.
*  This is a lot of fun. Yeah. This has definitely been a masterclass in rag and in AI application
*  development more generally. So Andrew Lee, co-founder of shortwave, thank you for being
*  part of the cognitive revolution. Cheers. It is both energizing and enlightening to hear why people
*  listen and learn what they value about the show. So please don't hesitate to reach out via email
*  or you can DM me on the social media platform of your choice.

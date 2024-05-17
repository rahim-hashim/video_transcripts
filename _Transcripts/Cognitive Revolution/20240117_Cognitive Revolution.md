---
Date Generated: April 02, 2024
Transcription Model: whisper medium 20231117
Length: 6788s
Video Keywords: []
Video Views: 1671
Video Rating: None
---

# Unlocking Enterprise Data with Knowledge Graphs | Juan Sequeda, Head of AI Lab at data.world
**Cognitive Revolution "How AI Changes Everything":** [January 17, 2024](https://www.youtube.com/watch?v=1Km4JKr3Og0)
*  This is the essence of what my organization is. It's the brain, right? Everything here is accurate. I can use this to explain things.
*  The LLM, these foundational models, don't have that accuracy, don't have that explainability, don't know my organization.
*  Do we expect these foundational models to know every single organization? No, because these things are private. I don't want them to know.
*  But I want to go use them. So that's why this combination of these foundational models, large language models, with your internal brain of organization, which is where Knowledge Graph,
*  that's what I see where there's a future. And I think what we need to work on is understanding best that integration point between the Knowledge Graph, the brain of your organization, and these foundational models.
*  Hello, and welcome back to the Cognitive Revolution. Today we're talking data and how generative AI interacts with enterprise data with my guest, Juan Cicada, principal scientist and head of the AI lab at data.world.
*  Data.world, like many established companies that we featured on the show over time, built much of its platform, products, team and business before the current generative AI moment, and is now working to make sure that it's taking full advantage of this new technology paradigm for its customers.
*  This is part of an economy wide trend. For instance, the technology paradigm is now being used to help us understand the potential of the technology and the potential of the technology.
*  This is part of an economy wide trend. Frontier generative AI models are now making their way into all sorts of high value, often very challenging contexts.
*  From processed chemistry labs to novel protein design to US federal courtrooms to the practice of medical diagnosis to enterprise data lakes, GPT-4 demonstrated enough raw power that we now have experts in literally every field working day in and day out to figure out how to make generative AI work for their organizations.
*  Now, it's not all instant success. From Juan's work, for example, it's clear that early benchmarks understate the complexity of real world enterprise data and that naive chat with your data type implementations are not up to enterprise challenges.
*  Even the more advanced work that Juan and team are doing with Knowledge Graphs, while it does deliver major improvement, is still at best a partial solution.
*  So while data.world again, like most established technology businesses I've talked to, is not particularly worried about competition from fast moving AI for startups, they do see the transformative potential and they are realizing enough practical utility today that they are rolling up their sleeves and settling in to the process of AI implementation and optimization.
*  Interestingly, zooming out, I think this creates the potential for another major phase change in the history of AI. While GPT-4 takes meaningful effort to implement and often still falls short of our dreams, we are nevertheless building foundational capacity for both last mile distribution and customization, such that the next big model release will have the opportunity to almost immediately plug into many millions of live business processes and systems.
*  The electrification of America took 60 years and included significant public works projects and all the appliances were designed with a clear understanding of exactly how they'd be supplied with electrical power.
*  Today, in contrast, we live in an Internet mediated software enabled world in which updates can quickly be pushed to everyone everywhere all at once.
*  Today's software application developers are building somewhat ahead of AI capability, both so that they can deliver frontier features to their users today and more importantly, so that they're ready to flip the switch when the next big advance comes online.
*  How many months we'll need to wait before GPT-4.5 or GPT-5? I don't know. And it might be just long enough that folks start to wonder whether AI generally is underpowered and overhyped.
*  But my expectation remains very clearly that we will continue to see additional jumps in capability and that with each future leap, considering the foundation now being laid, the deployment cycles will naturally get shorter and more disruptive.
*  One note for listeners, enterprise data is a complicated space and we spend some time in the first half of this conversation discussing the general state of enterprise data and data science teams today.
*  If you're already well versed in enterprise data science, you might find some of this a bit basic and introductory, but for most, I think the additional context will be very useful.
*  If you have any suggestions for how I can better handle the introduction of such advanced topics where listeners inevitably will have very different levels of prior knowledge, and I do expect this to be more and more common throughout 2024, I would love to hear your suggestions.
*  As always, you can email us at tcr at turpentine.co or you can DM me on the social media platform of your choice.
*  And of course, we always appreciate it when you share the show with friends, starting in this case with the data scientists in your life.
*  Now, I hope you enjoy this conversation about generative AI and enterprise data with Juan Cicada, principal scientist and head of the AI lab at data.world.
*  Juan Cicada, principal scientist and head of the AI lab at data.world. Welcome to the cognitive revolution.
*  Well, thank you so much for having me. Really excited about having this conversation.
*  Yeah, me too. I have been interested in knowledge graphs recently.
*  I've been kind of feeling for a few different projects that I'm working on that more structured data,
*  something between your kind of classic SQL database and the totally amorphous data that people are just increasingly vectorizing and hoping for the best from is probably going to be important.
*  And I went on a little quest to see who's working on this and what's the state of the art and came across a paper that you had published.
*  So I'm excited to get into that with you.
*  But I thought maybe we should just start with kind of an introduction to you and the company because I don't know how many listeners will be familiar.
*  You want to just kind of give us a quick intro to data.world like, you know, how the company gets started.
*  Was it an AI company at the beginning? We could take it from there.
*  Yeah, I have a new. So, OK, so data.world, we're an enterprise data catalog platform.
*  So data catalog platform is essentially where an inventory for the all the data and the metadata within the organization.
*  So basically like your library catalog, right?
*  That's kind of the high level thought about managing metadata has been something kind of since the beginning of just data management.
*  But I would argue that it hasn't really been a focus till the last probably five, five, six years.
*  OK, the focus in the enterprise by zoom out and look at what data the data management world has been.
*  It's always about moving data. So ETL and ELT storage and compute of data.
*  So your data warehouses, your data lakes and what's off. And then you're using your data.
*  You are now trying to your analytics, your dashboards, your email, all that stuff.
*  And then there's always been this this this thing on like on top that we haven't really kind of focused on it, which is the metadata, the data.
*  About the data. And that is what data catalogs are focused on, being able to kind of understand what's going across all the stuff that's being moved, all the different data sources, tables and columns that you have, keeping track of all your dashboards and how they're connected across all the different sources.
*  And then also keeping track of your business terminology, your business glossaries and everything.
*  So that's what a data catalog is. And so data world started off in, I think, 2016, very early on.
*  And the focus was to be the first phase of the company was to be a GitHub for data.
*  So it is we want to be a catalog for open data sets.
*  And that was the first phase of the company for a couple of years.
*  And we continue to be the world's largest open data catalog.
*  We have over two million users, I think, like two thirds of Fortune 500 folks are on data world on the open data platform.
*  Half a million data sets like during COVID, all the COVID data was housed on data that was completely open.
*  And it is continuing to be open. And we're actually a public benefit corporation.
*  So that means that in addition to being the C Corp and next to the shareholder value, we have a public benefit mission, which we're evaluated on.
*  It needs to be the world's largest and abundant data resource, advocate for open data and linked data standards and to be an archive for the world's data.
*  So those are public benefit mission. And what we did is that also during that first phase of the company, the goal was from a technology perspective is create a platform that can scale by the web scale.
*  And that's what we have over two million users. And so we really built a platform that we know that we could have high scale and then be able to go share data.
*  So around 2019, the next phase of the company was, hey, we built this whole platform that the open data community is using it within organizations.
*  People want to share their data and find data and so forth.
*  So that's how we entered into the whole what's now being called a data catalog.
*  People are doing data marketplaces and stuff like that's all where that fits in.
*  So that's kind of the phase of the company we're doing right now.
*  Now, from a technology perspective, from day zero, basically, the entire platform has been architected on top of a knowledge graph architecture, which means that we use first of all, we're all about open standards.
*  I mean, part of our public benefit corporation.
*  So we use the open web standards of our EF, which is the metadata, the graph standard, OWL, which is for ontologies and schema, Sparkle, which is for the graph query languages.
*  And that's the architecture we use.
*  So basically everything that we bring into the end of that world, it's already turned into a graph.
*  And why a graph?
*  You start thinking about moving data, storing data, using data.
*  Like there's all these pieces get connected across some of all those pipelines.
*  So you just really want to keep track of things and how they're being connected and so forth.
*  And that's a graph.
*  I always say that your first application over a knowledge graph is really the management of all your metadata to understand basically what is that infrastructure that I have within my organization.
*  To understand, hey, there is this data comes from the source and then it gets moved to this thing, it moves to this data warehouse, there's this application, there's people who are using it and so forth.
*  So you're keeping track of all of that.
*  And then now with AI, what happens is that, well, you need data, right?
*  Data is a foundation of this.
*  So I would argue that we've always been a data company and the data is a bloodline for AI.
*  So the data catalog and being able to manage your metadata, manage your semantics, manage your context, that is critical for the generative AI because that doesn't have the semantics, the context, the knowledge of your organization.
*  As it out of LLM, whatever it's been trained on, it doesn't have your own internal context.
*  So we've always kind of seen this over the last year and a half when LLM is coming out, for this to be applicable in the organization at a scale where you need accuracy, explainability, knowledge graphs are critical for that because it provides all that context that the LLMs don't have.
*  And that's what we're seeing and kind of what we've been talking about it.
*  And the paper that you mentioned originally was kind of the evidence that we wanted to put together to say, yes, knowledge graphs are critical for this, assuming you want accurate answers for your questions.
*  Let me just ask you to get a little bit more concrete on a couple of things.
*  It's awesome. You know, the two million data sets is awesome.
*  The public benefit aspect of that is really cool.
*  I'd love to hear a little bit more about kind of those data sets.
*  Like, what are the big attractors?
*  What are people coming to you for?
*  I imagine that, again, like most people probably just don't know.
*  And then I'm also really curious to get a little bit more concrete on, OK, but like, what is a knowledge graph?
*  Like, how have they how do they typically get created?
*  And like, what role does data world play in helping enterprise customers do that work?
*  So one thing is that is the open data catalog, which is open for folks, right?
*  And then people want the data catalog architecture for there to create their catalog internally.
*  So I see there's usually kind of three main applications that people are our customers will use data for.
*  One is when it comes to like search and discovery.
*  I don't know what data I have. Right. It's a typical problem that you have data scientists.
*  We're looking for data and they don't know where to go find stuff.
*  Your data lake is turned into a data swamp type of approach.
*  So they need to have a way to go search and go find that data they have.
*  So that's usually one of the applications around that.
*  So search is something that we're very focused on.
*  And the same way you search things on Google today and you if you search on Google, which were Austin, you get that panel on the side.
*  It's well, Austin is the capital of Texas.
*  And here are all these events going on and here the weather and here like that is what Google calls a knowledge panel.
*  And that is results that's coming from their graph that they've built.
*  So we did the exact same thing. So if you think about kind of the knowledge graph inside of data world that we build automatically,
*  let me bring your data. Think about it from the concept that show up are, hey, there's a database.
*  A database has tables, right. Tables have columns.
*  There are dashboards, right. There are different types of dashboards.
*  So the Tableau dashboard, RBI dashboards.
*  This dashboard was built using data from this table or this query over these tables. Right.
*  So you start to see how things get related, connected around that.
*  There is there's this person who created these dashboard. Right.
*  Then there's policies that we were kind of defining who can there's a PII.
*  There's personal information. This table has PII data. Right.
*  So then all these things get connected. So that's kind of the graph that happens underneath.
*  And when we go off and kind of connect and extract the metadata from all these sources,
*  we build that graph automatically for you for all that that technical metadata.
*  So that's kind of that that that call it the digital landscape of all that your data that's connected with an organization.
*  So search is one of those applications over that big graph of your metadata.
*  Another one is around governance. I want to know, again, let's keep track of all the policies around our data.
*  Who can use what data for what reasons? Who can access this data? Right.
*  But where where where is all the data sensitive data and so forth?
*  So that's all that's the governance side. And then the third one, we see it a lot for data ops, the just operations of data,
*  making sure that, hey, data is getting moved from different places.
*  Again, keeping the moving is like what we call the lineage.
*  Oh, well, this dashboard extracts data from this table.
*  This table comes from this stuff and so forth.
*  You have kind of that whole graph and lineage of where data is coming from, how it's living.
*  And then you want to make sure that, hey, if I'm going to make a change somewhere, what could that affect?
*  Or if somebody say I have an issue in this particular feed of data, where could it be?
*  I can kind of follow that. So that's all the operations of data.
*  And then you can be in your dashboard in town below and then you can actually get notifications from there saying, hey, there was an issue just reported.
*  So just be very careful with the data that's being shown here and to be fixed and so forth.
*  So that's the kind of a third application. So the summarized data catalogs and our users,
*  the user kind of a three main thing, which is for search and discovery, for data governance and for data ops.
*  And at the end of the day, all of us connected and we build that we build that graph of that metadata all automatically once we have our collectors up and going.
*  Hey, we'll continue our interview in a moment after a word from our sponsors.
*  Real quick. What's the easiest choice you can make?
*  Taking the window instead of the middle seat, outsourcing business tasks that you absolutely hate.
*  What about selling with Shopify?
*  Shopify is the global commerce platform that helps you sell at every stage of your business.
*  Shopify powers 10 percent of all e-commerce in the U.S.
*  And Shopify is the global force behind all birds, Rothy's and Brooklyn and millions of other entrepreneurs of every size across 175 countries.
*  Whether you're selling security systems or marketing memory modules, Shopify helps you sell everywhere from their all in one e-commerce platform to their in-person POS system.
*  Wherever and whatever you're selling, Shopify has got you covered.
*  I've used it in the past at the companies I've founded.
*  And when we launch merch here at Turpentine, Shopify will be our go to.
*  Shopify helps turn browsers into buyers with the Internet's best converting checkout, up to 36 percent better compared to other leading commerce platforms.
*  And Shopify helps you sell more with less effort thanks to Shopify Magic, your AI powered all star.
*  With Shopify Magic, whip up captivating content that converts from blog posts to product descriptions, generate instant FAQ answers, pick the perfect email send time.
*  Plus, Shopify Magic is free for every Shopify seller.
*  Businesses that grow, grow with Shopify.
*  Sign up for a one dollar per month trial period at Shopify.com slash cognitive.
*  Go to Shopify.com slash cognitive now to grow your business, no matter what stage you're in.
*  Shopify.com slash cognitive.
*  I'm really struck by how many of those things seem like they may already be undergoing significant transformation in the AI era.
*  You know, 2016, obviously not pre AI, but pre transformer, certainly pre large language models, certainly, you know, pre any, you know, kind of general conversational interface, you know, with a with a database.
*  I guess I'd love to hear a little bit more about how you build a knowledge graph automatically in a pre AI era and how that might be evolving.
*  And then also kind of the kind and the and the and the way the data is stored.
*  And I had Anton, who's the CTO at Chroma, one of the, you know, high flying new vector databases on as a guest on the show not too long ago.
*  And he made this really interesting point that the vast majority of data that goes into their databases has never been in a database before.
*  When you were first building knowledge graphs automatically, how did you approach that?
*  How is that changing and how is the actual nature of the data beginning to change in light of what they can now do with it?
*  First of all, we need to think about when it comes to knowledge graphs, there is the notion of the schema of the ontology.
*  Let's go define the semantics of meaning of a particular domain.
*  So everything I've been talking up to now when it comes to data catalog, the domain there is like this technical metadata.
*  Just think about the map. Let's draw the bubbles and lines on the whiteboard.
*  You have a table as part of a database. You have a dashboard. A dashboard takes data from a table.
*  Right. So that's kind of the schema that we're creating.
*  That's one knowledge graph. We create knowledge graphs about any type of topic.
*  So for example, let's create a knowledge graph around e-commerce.
*  Well, you have customers. We have orders. Right. A customer places an order.
*  An order consists of a set of order lines. An order line can have products. Right.
*  And the orders are shipped to an address and you could have a shipping address. You can have a mailing address.
*  That's basically the schema you start kind of defining.
*  You populate that coming that data may be coming from so many different types of sources.
*  They can be coming from structured sources, relational databases.
*  Some of that can be coming from unstructured, from text and so forth.
*  They can come in from feeds, JSON feeds, right. APIs, whatever.
*  So the knowledge graphs are a means of integrating data coming from so many different sources.
*  And you can model anything that you want around that.
*  Now, what takes time always is what I call the knowledge engineering process.
*  It's understanding what do you mean by what is a customer. Right.
*  Understanding what you mean by what is an order or what is an active order or so forth. Right.
*  And I think this is the human nature of the problem because you go ask multiple people
*  and they'll probably have different answers around that.
*  So what is the correct version? What is the correct answer?
*  So we always argue that if not even students will agree, how will the machines even know? Right.
*  The machines will definitely be able to generate suggestions.
*  Oh, it could be this could be this could be this.
*  But at the end, the humans need to go saying, no, we're our decision is going to be this definition.
*  And that's by the way, what where governance comes in because you want to have an agreement on what things mean.
*  Because otherwise, then we can depending on the type of business you are, you can have different types of chaos.
*  How things have been kind of slow to create what I'm calling creating these ontologies,
*  be able to understand what the what the state actually needs.
*  Now, what's interesting with LLMs today, like they're helping a lot of experiments.
*  A lot of experiments we're doing is using LLMs to help us accelerate that process of like, hey, create candidate ways of modeling these things.
*  Right. And how about through a chat bot, go talk to the end users to be able to extract the stuff that's in their head to say, how how do you define what a customer is?
*  How do you define what an order is? So I think that's something that we're seeing right now.
*  So then when it comes to like the vector databases, like one thing that we're seeing today is the low hanging fruit of being able to kind of show some really cool AI applications,
*  specifically when it comes to like chatting, chatting with your data. It's usually about unstructured.
*  So it's the Texas, as you said, mentioned, like the stuff that has never been inside of a database.
*  So it's your documents, your PDF files. Right. And then other ways you have images and so forth.
*  And that's where you want to have that sort of vector databases come in. And you have to do all of this, the chunking and kind of all the bits pieces for the unstructured site.
*  When it comes to structured data, the data that's in your relational databases and your data lakes that come into have thousands of tables, right.
*  And tens of thousands of columns like that structure has meaning.
*  And it's in that meaning already a user, a human being will look into that table and they're like, oh, this is what this means.
*  Like you want to add these two columns together, but not these other ones. Right.
*  There's that is there's there's knowledge behind that.
*  And I think that's harder to go do based on all that I was talking before.
*  It's like, what is this mean that you got to go talk to so many people? That's like not a scalable thing to go do.
*  Again, LLM today are helping us. They're going to help us because now we can kind of have these chat bots that can help us acquire knowledge.
*  So the low hanging fruit has been focusing on the unstructured.
*  But I would argue that the untapped potential here is to be able to go focus on the structured data, because this is the data that goes into your reports into your dashboard.
*  Like that's the stuff that executives and the boards are looking at those graphs to make decisions around that.
*  And that's the data that's coming from your CRM is your piece of stuff like this.
*  All very structured data and those types of questions that people are asking, they expect accurate answers and they expect to explain where those answers come from because they go trust that.
*  Well, if I have I'm asking questions over text, I'm like, oh, I mean, you have a little bit more freedom over there.
*  Right. And then I can point you to this larger document where you would go in.
*  So I think that that that's why I'm like arguing that the low hanging fruit is focusing on unstructured and there's just so much of it.
*  So we can be very, very busy for a long time and provide a lot of value.
*  I think where there is tremendous value, what could argue and I would argue here that probably even a much more higher value is if I can have a chat with my structured SQL data, because that's where your critical decision makings are happening for for organization.
*  What you're describing there, I think, connects to a couple of big themes that I notice across a lot of different areas of AI today.
*  One is just how much knowledge is kind of undocumented.
*  A friend of mine used to call this tribal knowledge.
*  You know, it's the know how that people share by watching each other do tasks over their shoulder, perhaps, or, you know, on a screen share, perhaps more likely today, you know, or in kind of a quick chat where people ask each other questions.
*  And that knowledge is because it's kind of not localized anywhere.
*  It is very hard to make that available to, you know, to anyone.
*  But we're starting to really feel that acutely now in the in the AI moment where people are like, well, why isn't, you know, why are these agents like working?
*  And often the answer is, you know, because they're kind of very generic and they don't have any of the context, you know, or the sort of, you know, that what feels familiar to you is just like totally alien to them.
*  So it's interesting that this this problem, I guess, has been felt acutely enough in the data world, even before AI, that it's like, you know, you guys have built a whole platform about it.
*  Could you kind of sketch a little bit more there, like typical enterprise customer?
*  I have a little bit of a sense for this. I did a project once.
*  I was a very junior consultant firm that was working with Washington Mutual, which was once the the country's biggest thrift.
*  Thrift, it was called. And yeah, it was in that mortgage crisis moment that I was doing this project.
*  And I do remember just the absolute total gnarliness of the the data and just how many different columns and all these columns derived from other columns.
*  And it was kind of the data swamp. And I only saw a corner of it in my brief engagement before the bank went or the thrift went bust.
*  But maybe it could give us a little bit more kind of color on like typical enterprise.
*  Where are they today? They have a lot of data.
*  But, you know, are we still in a moment where it's like spread across tons of systems and people are super siloed and nobody knows where things are?
*  In my case, I remember vividly completing an analysis and then having somebody look at it and be like, this is totally wrong.
*  And me being like, I would have had no way of knowing this.
*  You know, there was I literally could not, you know, all these suffixes on these columns, like they didn't mean anything to me.
*  This is exactly what I was thinking.
*  Yes. And here's the thing is that the problems that we deal with today are the same problems that people have been describing 10 years ago, 20 years ago, 30 years ago,
*  and more since the beginning of just like modern digital, just digital enterprise since going into warehouses and so forth back in the 90s or even before that.
*  So this is my annoyance with what the entire world is like.
*  Can you imagine that the problems that we're complaining about today are literally the same problems that we complained about 30 years ago?
*  Like, we're kind of fucked up if we're, we're still trying to solve the same problem.
*  Now, things are things are getting easier. Right.
*  Like now we think the cloud has made things a little bit easier to go do.
*  Right. You have self-service a lot to let people do more things.
*  But you know, we're still trying to solve the same problem.
*  So let's ask ourselves, like, what have we been doing for the last 30 plus years?
*  And then I'm like, wait, but now AI is coming.
*  So is this magically going to solve this?
*  Like, no, we got this is very important to kind of understand our history.
*  So let me go down a couple of examples that kind of I've seen across my career.
*  So at the end of the day, with data, your goal is to go answer some questions and you want to be able to answer some questions to be able to solve the problem.
*  So at the end of the day, with data, your goal is to go answer some questions and you want to be able to answer some questions to be able to understand how the business is doing to make sure that I'm going to make a decision that it's going to help us make more money or save money.
*  Right. I think you make money, you save money, you want to mitigate risk.
*  Three main things you want to be able to put in your organization.
*  All right.
*  So I have a question I want to go ask.
*  So I got a question and I need data to answer this question.
*  Where's that data?
*  So when one like call it the spreadsheet approach, you basically go ask somebody who has the data.
*  I need data about X, Y and Z.
*  And that person will go off and send you a spreadsheet of X, Y and Z.
*  And then you get in and then you, you know, it would sell pretty well and you'll be lookups or heck.
*  Maybe you people have an access database on their laptop and then they'll be able to go do munging or whatever that stuff.
*  And then they answer their question.
*  There it is.
*  OK, so that's how we've always been doing things.
*  Is that a scalable approach?
*  Probably not, because then tomorrow I said I need data.
*  I need data about X again because I need it for the new month.
*  So they said it again and so forth. Right.
*  But I'm asking about X. I'm asking about orders.
*  I'm asking about our latest customers.
*  But how did when I asked about orders and you occurred me and you are going to go do that work.
*  How do we know we're talking about the same thing?
*  Do you make do you have that same interpretation and you're actually you're actually delivering the correct thing that I'm expecting to go do?
*  I don't know. Right.
*  But this is how we've been doing. This is how we've been dealing with data.
*  So for so long.
*  Another approach is what I call the query approach.
*  You're like, look, you're asking me for this spreadsheet of data and every month you're asking for it.
*  Like there's no I'm going to give you access to the database directly and you can just query the database.
*  You can connect your dashboard directly to your database.
*  Here's the query that I use.
*  That's it.
*  Perfect. Now I can go ask more in real time and do things.
*  Right.
*  But you're probably I mean, depending how SQL savvy you are, you can go edit the queries.
*  You can go add things.
*  And then suddenly this query that was 15 lines long, you join it with something else and it's 30 and it's 100.
*  And then I've seen queries that are 10, 15 pages long.
*  Takes 20 minutes to run and it runs and executes and that's and the result of that query is what I'm going to use in a report presented the CEO.
*  That query has so much knowledge embedded into it.
*  Do we actually know what's happening in there?
*  And we're making a billion dollar decision based on a supplement into you.
*  Right. And then everybody is doing this themselves.
*  Right. So if I make a change in my query, how do I know that that's not the change that you should have done to write or the other way or somebody else made a change that I should have interpreted to.
*  So that's kind of the call it the query approach.
*  And then you can go off and say, well, no, we need to have this one standard database or data warehouse work where all the all this everything is well aligned and we're all going to go for this thing.
*  And we go off and like, yes, let's go build the data warehouse.
*  But what happens?
*  That takes millions of dollars and it takes many years to go do.
*  You get requirements.
*  And then suddenly what happens is that you're like, oh, now you can go answer your question on this data warehouse.
*  I'm all invested so much time and money in you go up and you answer that you now run the question, run your query, get into that question.
*  But what happens? You compare that answer to the way you've been trying to answer that question before.
*  You think it's going to be the same?
*  Probably not.
*  So then you're like, wait, I have control of this way.
*  I get one answer and then I get the answer from this other system, which I don't control.
*  What am I going to trust?
*  You basically trust your process that you control.
*  Right. So then this is kind of why you have issues like data warehouses fail.
*  They don't fail for technical reasons.
*  They fail for social reasons because people don't trust them.
*  So for it.
*  And then and then the problem of that is I'm doing ETL and I got to structure my data beforehand.
*  And then we went off and we said, no, let's go ELT.
*  Let's go dump our data into a lake.
*  And then the lakes get all messy and they turn swamps.
*  And then like I then so you can imagine like this is the story we've been going off over and over again.
*  And a theme throughout all of this is keeping track of what something means.
*  This is the meaning. This is the semantics.
*  This is the knowledge. This is the metadata.
*  And I think what has happened is that throughout the last 30 plus years,
*  we've never focused on keeping track of the meaning of managing the meeting.
*  And now I'll argue that LLMs and all of this AI is making us realize, oh, if I want to trust that,
*  I need to know what it means.
*  And now my hope when I'm starting to go see this is like there is now a new focus on we need to invest in semantics.
*  We need to invest in meaning and knowledge.
*  And that's where knowledge and stuff comes through.
*  And more 25.
*  NetSuite turns 25 this year.
*  That's 25 years of helping businesses do more with less, close their books in days, not weeks, and drive down costs.
*  One, because your business is one of a kind.
*  So you get a customized solution for all your KPIs in one efficient system with one source of truth.
*  Manage risk, get reliable forecasts and improve margins.
*  Everything you need all in one place.
*  Right now, download NetSuite's popular KPI checklist designed to give you consistently excellent performance,
*  absolutely free and net suite dot com slash cognitive.
*  That's net suite dot com slash cognitive to get your own KPI checklist.
*  NetSuite dot com slash cognitive.
*  Omniki uses generative AI to enable you to launch hundreds of thousands of ad iterations that actually work,
*  customized across all platforms with a click of a button.
*  I believe in Omniki so much that I invested in it, and I recommend you use it too.
*  Use Cogrev to get a 10 percent discount.
*  One kind of extra little detour before we get into the paper and how it all works.
*  I mean, obviously there's a lot of data professionals these days, and they fall into different kinds of roles.
*  What if you could characterize in rough terms, like who are the people that you work with?
*  What jobs do they have?
*  What are the activities in those jobs?
*  How much of it you kind of gave a sense of the different approaches.
*  If you would actually just observe, do a time study of these folks,
*  how much of their time are they spending on different kinds of activities?
*  How much of it is that routine query running and kind of process that they've done month after month?
*  How much of it is data migrations or these kind of mega projects that may or may not ever come to fruition?
*  How much is ad hoc analysis that leadership or whoever has one-off questions that haven't been asked before?
*  I have honestly, I'm probably varies a lot by context, but I have no idea really how people are kind of spending their time.
*  I always find that to be an interesting foundational question to then ask like, OK, well, which parts of that is AI going to impact?
*  But for starters, maybe you could just kind of characterize what do they do?
*  What do they do? I don't know what they're doing.
*  So there's what I call the data producers and the data consumers.
*  So there's two types of folks in here.
*  So the data producers are going to be more in the back end, the technical side.
*  They're the ones who are moving the data, migrating the data, creating, managing the data, what makes sure it exists, and so forth.
*  The other consumers, they're the ones who are searching for data, who want the data, who have a particular task that they want to accomplish.
*  They have a question that they need to answer.
*  And so they do the two types.
*  So if we look at, let's focus on consumers.
*  So on the consumer side, you can have folks who are going to be your data analysts or your BI analysis.
*  So people build reports and dashboards.
*  You have your data scientists, folks who are your machine learning engineers.
*  They're saying, I need to go find this data so I can go do some work to go implement.
*  I create a model, I create a dashboard because I'm trying to go answer a question or make a recommendation or something.
*  So I'm consuming data to be able to accomplish that task.
*  Now, on that side, you hear always like the 80-20 rule, 80% of the time I spend cleaning my data and all that stuff.
*  And that's a problem.
*  And I think actually another annoyance I have is when people say, oh, I have to clean my data.
*  It's data janitorial work.
*  I'm like, no, that's understanding the critical meaning of your data.
*  And you're just like sweeping under the rug.
*  It's like, oh, that's annoying pieces.
*  That's the essence of what the meaning of your business is, isn't that data?
*  You're like, oh, I just kind of write some quick code and it's just annoying to go do.
*  That's a problem is that we don't treat it as a first class citizen.
*  And then on the producer side, so there are the folks who are saying, oh, we got data coming from these sources and we get the requirements.
*  So we hear that you want to go, you need this data.
*  So we're going to go move the data over here.
*  And now we need it to be more scalable.
*  So we're going to the cloud.
*  So we're going to use stuff like our Databricks.
*  And I know that you guys consumers, you want to be able to go run these types of stuff.
*  So we're going to have the data set up in this way so you can go do that.
*  And but then there are there are the ones who are actually putting the data together.
*  How do we know that the requirements that they get are actually being fulfilled correctly, especially because the requirements from the consumer side, they're connected to the business, how the business thinks.
*  Oh, they're either talking about customers.
*  They're talking about average order values, right.
*  They're talking about these metrics are the produce are the producers more technical side and folks.
*  Do they understand that?
*  Do they is it very clear to them?
*  Oh, I could I could present the data this way or that way.
*  How do I know which is the correct way?
*  And I think that's always been a gap.
*  That what I call the producer consumer gap and that producer consumer gap is there's roles that are missing.
*  One of those types of roles is I'm seeing this evolve now.
*  I'm calling it the knowledge engineer or also the knowledge scientist.
*  And it's really the person or role who like to work on both sides of the both side of the aisle.
*  Right. Hey, I can be a non-technical people person go understand what you're trying to go do.
*  I can draw the models on the whiteboard.
*  Then I can go talk to the technical folks and be and say, OK, it's this data for this reason and so forth.
*  And we're certainly also seen this as called the data product manager.
*  Right. You're bringing product management into David.
*  So I think we have this gap.
*  So there's a producers, the consumers.
*  And I think one to kind of try to try to answer your question, which I can't give you numbers, but I don't know.
*  I don't know these numbers.
*  But I think there's a lot of this repetitiveness happening.
*  We're wasting our time a lot. We don't know if this is correct.
*  And the way that we should be able to kind of address that is by having a role which is focused on being that bridge.
*  And it's a role where you're bringing in one of the people, the process side.
*  We're doing product management.
*  It's do it as knowledge acquisition.
*  It's things that people are doing today, but they're not doing it in a first class way.
*  They're just like, oh, that's the second best.
*  That's the annoying thing I have to go do.
*  It's annoying to you, but it is critical and somebody should take the ownership, the accountability for that.
*  Interesting. So that role, if I understand correctly, that would be essentially the power user of the data.world platform.
*  I'm thinking almost like knowledge librarian, knowledge historian.
*  So that's a good point. So yeah, it's like a librarian.
*  I would argue that for data.world, things like data.world, the data columns, you have all three of those.
*  So for example, you're bringing in all your different sources.
*  I need to deal with all that technical data stuff that's coming in.
*  You want data.world to say, hey, I just got these feeds of data and I just want to know that I'm keeping track of these four or five, six hundred tables.
*  These other thousands, I'm going to ignore them.
*  So that's where I'm going to keep my inventory of stuff that's going on.
*  We're moving our pipelines of data.
*  All of that gets managed inside of data.world.
*  So you have that for your data engineers, right, for your technical folks.
*  And then you have your consumers of data who are searching for data.
*  Right. Those are the ones who will also come into data.world.
*  But they're looking at it from a more consumer perspective.
*  Oh, I'm looking for data about customers and about, oh, they can now search for that.
*  They find that data sets.
*  And then kind of what you would want is the data, these kind of people in the middle saying, hey, I want to expose to you.
*  I want to expose to the consumers this beautiful data product, something that just like your shopping experience in Amazon.
*  Right. So if you go to Amazon and you're buying a water bottle, for example, well, there's only one water bottle.
*  Right. There's probably hundreds of water bottles.
*  You go as a consumer, you go in, you search for something and you're like, oh, I think these are ranked.
*  I have reviews. I have pictures. There's metadata.
*  There's a lot of descriptions. And which one are you going to go trust?
*  The ones that have great reviews, that has most stars, that have great pictures, that has more metadata, more descriptions.
*  There's other ones that are like, wow, that has that have any pictures.
*  I'm not going to trust that. Right. So that's the experience of a consumer.
*  Now, somebody had to put all that inside of Amazon's case, put inside of data.world.
*  And that's kind of on the producer side. And they want and how to decide who goes into what.
*  I think that's where this data product management roles are coming in.
*  And at the end, I think a lot you talk about the life cycle of data and stuff like we're spending money to keep this running, keep this data.
*  I was like, you should tell me where is what is the ROI on this?
*  I'm like, look, we invested all this stuff. We've created all these data sets.
*  Look at all the people who are coming to consume this data.
*  I can actually go survey the people and say, if I turn this off, what are you, how is it going to affect you?
*  I should be able to know these types of stuff.
*  You want to be able to keep track of all these metrics and what's up of how people are using the data and how they're accessing their searching also inside of your catalog and data.world.
*  So I think data.world is something that just connects the entire kind of landscape of data with our organization from the technical all the way to the consumer and everything in the middle.
*  That's kind of another angle on one of these big themes that I keep finding in the as AI impacts all sorts of different knowledge work.
*  I have a thesis that the platforms in which people do their work are extremely well positioned to start to kind of create long form narratives of like what people are actually doing.
*  And from that, perhaps begin to train future AI systems on this data, the sort of data.
*  In this case, it's like the data of how we work on data.
*  But in other platforms, it's the data of how we work on other things. Right.
*  It could be creative. It could be you name it. Right.
*  Any of a million things. Are you capturing these arcs?
*  Because I could imagine that in a catalog, you could imagine different modes of interaction where somebody maybe comes and says, oh, I have a question about what does this particular thing mean?
*  They come, they get answered, and then they go somewhere else and execute a query.
*  And so you only see sort of a glimpse of their work process.
*  But I'm sure you have all these data connectors and things, too.
*  So I wonder how often people are actually going on a journey within the platform versus kind of flipping in and out of the platform at different parts of their journey.
*  This is a great observation you're making.
*  And so I think when you look at tools like in general, the data catalog market, it is very separated from you manage all the metadata, search in the store, find things.
*  And then I go to another place to go like actually access the data.
*  One of the things that makes data available different from the entire market is that we have we have both of those things.
*  You can actually search and find the data that you can actually access the data within the data world because we have virtualization, federation.
*  I mean, your data continues to stay where it is.
*  Right. So you got your data in Snowflake or data, whatever, like your data stays there, but you can actually fight it and access it through data.
*  So that so we actually have kind of kind of again, that's all I was saying.
*  Like we have a full view of everything.
*  Now, we get rid of something really interesting, which is something I'm pushing people to go do is we need to track and catalog not just all this technical metadata,
*  but it's also keep track of all the questions people are asking.
*  Who's asking those questions?
*  What are the and what are the answers that they're getting back?
*  The actual the actual not just all I look for this for I'm looking for this data and here's this data set.
*  Go do something with it because what we're going to what we're seeing, we're actually working on a data world.
*  It's like I want to ask a question.
*  Show me all the amount of quarters that have happened in the Eastern region.
*  Right. I should be able to get.
*  Oh, here's your numbers by region by data.
*  Like you get the actual answers to your question coming from either our world, too.
*  So those are that's how we're the whole chatting with your data comes from or working on this stuff.
*  Now, what happens is that we should be keeping track of the questions and answers because we should govern.
*  Also, we should keep track of these questions and what is the actual kind of stamped answer answer for some of these questions that we can't.
*  And what happens is that if you're asking for question, you should be able to say, hey,
*  these other people who have been asking very similar questions and here's the answers that have already kind of been stamped because these are like official things that we have to go for.
*  I don't know regulatory focus or whatever.
*  So you should know that type of information.
*  So I think that's that's something that we're going to start evolving and then because we're able to go learn from times of people are having.
*  That's why I by the way, all of that just continues to get connected inside of your big graph.
*  So when I was like my original graph was like you have databases and tables and columns and dashboards.
*  Well, then I can extend that.
*  But I have questions. I have answers. I have people.
*  This person asked this question.
*  This question was executed.
*  This question using LLM to generate this query that was executed over this database.
*  And here's the answer.
*  And and Nathan is the steward who said this is the official answer for this type of question.
*  And so next time somebody asked a question like that, they can get a really very similar suggested question and they have a governed answer.
*  But like I think that's kind of where we're going, especially for enterprise scenarios are going to have accuracy and explainability.
*  And then obviously you're going to have questions.
*  I'm just discovering things right now.
*  I'm trying to be creative around that stuff.
*  And then I think that's kind of also when it comes to question answering.
*  We should also think about what types of questions and things where a lot of the agents come in and so you think about it question, answer perspective.
*  It's like just give me a question and I can answer to you.
*  It's like, OK, you're asking a question.
*  What type of question is this?
*  Oh, it's a factual question.
*  This is a subjective question.
*  All right. Two different questions.
*  Right. Is this a factual question about the knowledge?
*  This is a factual question about the data that I have.
*  Do I even have the data to be able to answer this question?
*  Or do you even have access authorization to be able to get answers to that?
*  Oh, maybe not for all of it, but for this subset you can.
*  So then like the agent should be able to go understand what you're trying to do, understand more context where you're coming from and saying, hey, I can't answer that question.
*  But here's a subset of that question I can answer and I can't answer it because of the other reasons.
*  I think that's the type of stuff that we're heading toward.
*  That's what I get really, really excited about.
*  Yeah. Yeah.
*  Accuracy and explainability.
*  Those are two.
*  It's funny how many it's not surprising in the sense that.
*  You know, obviously, AI systems, AI models are all trained on data and they're very, you know, they're very much like directly derived from their data.
*  Accuracy and explainability come up in, you know, all the AI systems work that I see.
*  It's interesting that that exact same framing clearly predates it in the in the data management work that kind of underlies now the AI that's getting built on top.
*  When it comes to accuracy, do we have any good like benchmarks, rules of thumb, reference points for how accurate humans are?
*  This is one thing I find everywhere I go, you know, that people have no idea how accurate the humans are.
*  I love that you're asking this question.
*  And this is really the how we how how we need to have fierce conversations with each other and push back.
*  So like all the research that we've been doing about all the accuracy.
*  And so the first set of critics, what do they say?
*  Oh, but 60 percent is inaccurate.
*  Yeah, of course.
*  I know it's not accurate. So what is accurate enough?
*  One hundred percent, ninety nine percent.
*  What is it? Do you actually know?
*  OK, you you got data today to go answer a question that you made believes a barred decision there be some of them bars.
*  Do you know how accurate that was?
*  Are you giving your life on the accuracy of that?
*  So ask the question. I don't think I don't know.
*  Do you know you got that and you got that dashboard or that spreadsheet from from Alice and Bob?
*  You know how that work was done.
*  You trust exactly. Really? Do you do?
*  Do you want to ask those questions?
*  So they're like they make the assumption that the machine needs to be accurate and everything, but then they don't even ask.
*  They're not being critical about their own process to go into that.
*  I think this is this is an opportunity right now to be very critical about kind of how to evaluate ourselves.
*  How are we doing this?
*  And going back to like how how is impacting all the tasks that we're doing?
*  It's like let's go figure out how we're solving that problem today and say, well, wow, this is a very.
*  I mean, what is that process and can we improve that process and we figure out, oh, wow, there's a big bottleneck or that's something that is pretty sketchy.
*  It's not working well.
*  And you want to be able to bring in the machines, the AI to go help for those things.
*  So I think it's really, really important to ask ourselves, how are we solving these problems today and be honest about it's like, oh, crap, I got it.
*  But that's something that may not be doing.
*  I mean, I've done this.
*  I remember once working with a customer who were like years getting getting this report and making decisions about it.
*  And I went off and go analyze how they got that report because they hadn't done it.
*  And I'm like, well, do you know that to get this value over here, you've there's some hard coded values are like multiplying zero point zero to whatever.
*  Like that's happening.
*  And they're like, why is it?
*  And then somebody said, oh, I remember like two years ago we were like doing some special discount and like, well, guess what?
*  The person who wrote that query hard coded that discount, whatever.
*  And it's been there for the last two years.
*  So all of the decisions you've been making is has that embedded in there.
*  All your numbers have been wrong to last two years and you've been made decisions now.
*  But the honest OBS here is like what the company still man why yourself?
*  Like how big of a deal was that?
*  So I think that's also it's like how critical are these things and like sometimes it's good enough.
*  Right. So I think it's also part of the culture that you have within your organization.
*  I've experienced some very similar things.
*  And in a non, you know, the company that I started, we did a lot of digital marketing for a while.
*  And, you know, we and we both like helped our clients do it.
*  And then we did it.
*  And we found just so many instances over time where you come to some initial conclusion and, you know, you really have to challenge yourself, especially digital marketing will punish you, you know, for being wrong on these things.
*  You know, we really had to challenge ourselves.
*  Is this really right?
*  You know, does it does it check out across any everything else we know?
*  You know, does it does it violate our world model and, you know, dig in, dig in, dig in as many layers as we could to finally often find that there was some problem that happened at the Washington Mutual thing, too.
*  I remember one time where, you know, I was summing something and it was like greater than, you know, the limit that it was supposed to be governed by.
*  And it was like, well, what's happening here?
*  Your your query must be wrong.
*  And it turned out actually, no, like some other process in the bank had changed some underlying data and all of a sudden, you know, everything had kind of sands had shifted under us.
*  But yeah, broadly, I find that I don't know.
*  I mean, if I had to guess, I would estimate that like a significant fraction of the data analysis that people are basing business decisions on is just like fundamentally flawed to the point where, you know, they're they're kind of detached from reality.
*  I don't know if we could get any more rigorous in our estimation of that.
*  But for me, it has been a recurring theme that just, you know, somebody gives you the results of a query or a spreadsheet or whatever and tells you it's X.
*  And it's like I did die.
*  I do not take that stuff at face value anymore.
*  We're just talking a little bit too about podcast metrics.
*  You know, oh, my God, like we had one.
*  We had one. We were looking at the success of the podcast and it was like, oh, you know, we did really well in this time and we did really poorly in this time, you know, by comparison, like, look, there's a spike and there's a trough.
*  And it turned out that it was like the way that the month fell with respect to the weeks and the days on which we published the podcast.
*  And, you know, it was like, well, we actually had nine episodes released in this month and seven in the next month.
*  And that's why, you know, we got way more downloads in the in the first month than the next month.
*  It really nothing that you the per download per episode downloads were the same.
*  But even at that simple of a level, I've seen, you know, people just get like so confused by kind of aggregate measures.
*  Do you have any I mean, this is a little bit of a digression for our core topic, but do you have any tips or sort of habits of mind that you encourage people to monitor?
*  How about if you have some sort of like a
*  mantra that you use to read the raw data?
*  Like you say that there's no substitute for reading the raw data.
*  If you have not looked at actual raw records at some point in the process, obviously, can't read all the raw records.
*  But if you have not familiarized yourself with at least some raw records, my guess is there's a pretty good chance you're going to be wrong in the aggregate analysis.
*  ask why five times right? I am what what is the goal? What is
*  the objective? What is the objective above the objective
*  that you're trying to go do? Because it goes back into like,
*  oh, we have all these ad hoc questions that we're trying to
*  go deal with. I'm like, why are you doing that? How is that
*  valuable for the business? Like the person you give that to that
*  person, what are they going to go do with that? And so it's
*  always like, are you tying the work that you're doing to
*  specific business value? And you and the way to tie that is that
*  you need to know what are the objectives, corporate strategies
*  of the quarter of the year, whatever that needs that you
*  know what those are, because you need to be able to push back
*  saying, I'm not going to go spend time on that, because that
*  is not related at all to what our quarterly goals are, unless
*  you explain it to me, right? So I think that's something how so
*  that's kind of more from where I am going to go and talk, right?
*  Get connected to the business to make sure that we're not wasting
*  time to go do that. Then another kind of another approach
*  technique that I do is what I call the the iron an iron thread,
*  which is like, look, how do I know if something is working
*  correctly? Like, don't boil the ocean. That's another one
*  trick. Don't boil the ocean. We're gonna love to get it. So
*  start from something very specific, one small thing, and
*  figure out what is the path all the way to the to the end goal,
*  and do it really, really small. So you have to do it just you
*  basically get that one thread through. And then you're like,
*  Okay, I understand all the things I need to go through. And
*  then you say, let's do it again. And then you add like,
*  basically, you're adding another thread to it, and that thread
*  gets bigger, bigger. And then at some point, then you're like,
*  Well, how about let's do it for another area, something,
*  something different. And then you so you can have somebody else
*  in the distributed way, independently go off and do
*  another thread somewhere else, kind of, okay, now we start
*  getting these kind of threads all straight. I think that's kind
*  of an approach I always do, because otherwise, we kind of
*  like, get focused too much on the bottom stuff. And then we're
*  not connecting it to the valley that people are seeing, because
*  we don't even understand, like, I need to understand what is the
*  the the not just the output, but what is the outcome that needs
*  to happen. And so you want to be able to kind of just be able to
*  drive all that through from top to bottom from, from the
*  executive, all the way down to get into the nitty gritty of
*  roll up your sleeves, that all that needs to be connected. And
*  you don't have to blow the ocean to it for everything. Just one
*  very specific thing, go through it, that's that you understand
*  how things flow and what's working, what's not working,
*  where's the struggle and so forth.
*  Yeah, interesting. That's software development sometimes
*  can be like that, more generally, too, where you just
*  it's a vertical spike through all the layers of the stack to
*  get everything connected and, you know, make make one successful
*  round trip is like a good early milestone in a lot of things.
*  It tied to say, I was like, well, that's like all the steps
*  that you need to go do it, then you figure out, well, where can
*  I put AI here to automate things and make it faster, better,
*  you know, more productive.
*  So perfect transition then to the paper, we've got a lot of
*  preamble before the actual paper that you've published, but high
*  level, it seems like the big demonstration of the paper is
*  that you take GPT four, and you say, hey, I want you to write
*  some queries for me to answer some questions. And you give it
*  either the pure schema, you know, like the table definitions
*  and you know, there's a lot of meaning, often implicit there in
*  the or, you know, to some degree explicit and like the names of
*  the tables and the names of the columns and the way that, you
*  know, database keys and you know, what not relate to each
*  other, right, you can sort of, there's an implicit graph,
*  again, somewhat somewhat explicit, just in the schema
*  structure, and you get a certain level of performance. And then
*  you compare that to Okay, now let's also give GPT four, a
*  higher level semantic knowledge graph representation of what
*  does this data actually mean? So that perhaps not surprisingly,
*  given all this preamble yields quite a bit better results. What
*  additional details about that experimental setup or about the
*  findings do you think are most important for people to
*  understand?
*  Everybody was excited about chatting with their data.
*  Chatting also called call it a text to SQL has been an area in
*  computer science and we've been looking into for, again, also
*  probably 30 plus years. So there's been all these
*  techniques happening. And now with LLM, people are like, well,
*  this should be much more easier to go create the new text to
*  SQL. And from an academic standpoint, there's all there's
*  these benchmarks and techniques you've been doing out and they
*  show 95% accuracy. And I'm like, I'm skeptical about this stuff.
*  And when you go and when you look into these benchmarks,
*  they're all very simple. They're like, oh, there's a couple of
*  tables and there are when and the semantics are very explicit
*  in there. But I'm like, that's really disconnected from the
*  enterprise. Because the enterprise doesn't always have
*  that clear and it very clear and small. And then the other
*  part is that the questions people were asking were like,
*  oh, here's like a laundry list of questions that are like, how
*  why these questions are this? How do you come up with these? So
*  the main research question, there's two questions. One is we
*  want to understand to what extent can the large language
*  models kind of generate SQL query that can be accurate? To
*  what extent that can be done? And then the follow question
*  there is, to what extent can that accuracy improve? If you
*  actually put the knowledge graph in the middle? And the hypothesis
*  here is that if you do the knowledge graph, it's going to
*  improve the accuracy. Now that we didn't know to what extent we
*  didn't know how much. The thing is that just common just talking
*  to folks that was like, yeah, the adding semantics, context,
*  knowledge of like that, that should help. But when how would
*  we do it? And how much better is it? And like people didn't know.
*  And I'm like, we were at snowflake summit in June, and we
*  were having this conversation with a bunch of product people.
*  And they're the ones who, frankly, were just challenging
*  us saying, you guys should just do a benchmark around it. And
*  I'm like, yeah, and literally got on the plane came back and
*  they started working on this stuff. That's I mean, that
*  that was a kudos to them and kind of really challenging
*  pushing us to it. So that was the whole setup. So what we did
*  was that we have an enterprise schema using in the insurance
*  domain. So we're using an open standard called from OMG, they
*  have a property cash into the schema. So this is a
*  representative of an enterprise domain, and it breaks team
*  right there. And then the other thing was the questions were
*  asked. Yeah, we're enterprise team, I don't even set a
*  question. But these questions were actually putting them, we
*  created this quadrant about what two kind of spectrums of
*  complexity. One of the spectrum of complexity is on the types
*  of easy questions or harder questions. Easy questions being
*  giving you a list of things, show me all the claims that are
*  open, right? Those are easy questions. Harder questions are
*  things that are going to be more about strategy, and which involves
*  really questions already, I need to do some aggregations, I need
*  to do math throughout that. And then from a from a technical
*  perspective, you also have easier questions and harder
*  questions easier meaning, I only need a couple of tables to
*  answer this. And harder question is a lot more tables, eight, nine
*  tables to be joined. So then you put these two spectrums
*  together, you get this quadrant of like easy questions over easy
*  schema, and then you get harder questions over easy schema, so
*  forth, you get all these different quadrants. So, so that
*  so that that gave us a perspective of understanding the
*  types of questions that people can ask. And then the third
*  thing that we looked into was let's make let's invest in
*  putting in coming up with the semantics, invest in creating
*  the context, that's what we'll call the context layer. So it's
*  here is the ontologist semantic layer. And here's how these
*  things map. So very simple. There is a claim has a claim
*  number. Oh, there is a table called clay. Okay, perfect. That
*  matches. But there's actually that table has, I don't know,
*  1520 columns, one column is called claim identifier, that is
*  not the claim number. There is a column called there's a column
*  called the company claim number, that is the column that has a
*  claim number, right. So that's, so then make these mappings. And
*  then you would have things like values, you'd like, well, I want
*  to know where what are my policyholders? Well, you have to
*  get it's everything that has the role column equals pH, agents
*  over role equals ag, right? That's a semantics like that.
*  That's that's that's the context that you have in there. So we
*  made that very explicit. So that's what we that's what we
*  come up with kind of as a input, kind of into the benchmark. And
*  what we did was evaluate saying, very simple setup, on purpose,
*  wanted to do very simple, because I wonder like, get the
*  bare minimum of very, the simplest prompt that you can
*  imagine. Here is a SQL DDL schema, copy and paste the SQL
*  DDL and say, write a SQL query for the following question. And
*  then for the knowledge graph, we said here is the owl ontology,
*  that's semantic layer, which is an open standard that we gave
*  it, right? We've understood that GPT four knows these open
*  standard. And you copy and paste and you said, write this
*  sparkle query for this question. And sparkle is the open standard
*  for for knowledge graphs for the queries. And we just so also the
*  caveat is that we put the schemas and the ontology, the
*  semantic layer as part of the prompt, right? So it's a so it
*  has to fit within the amount of tokens. And you just give that
*  to GPT before and it generated the query. And then when we
*  started comparing all the queries are generated that the
*  that we get that three x different differentiators, though,
*  and there's three times more accurate queries, if you're
*  doing the knowledge graph, versus the only do SQL. That's
*  if you compare all the questions. And if you look inside
*  the quadrants, effectively, when you have questions that
*  require high complex, the tables, basically, questions
*  that require joining more than four tables, SQL query was
*  generated by GPT four would always fail. And I think that
*  was an interesting point is like, oh, so if you have
*  queries that require more than four tables, like that's not
*  gonna work very well. So and that was for this for this very
*  simple prompt that I think up work that we're doing right now
*  is what we're gonna go test it with other models to add what we
*  want and what the community go do to and we're seeing this is
*  like, well, yeah, let's go improve the prompting. Let's go
*  figure out more context. Is there a way I can pass the
*  context to SQL and some other ways like this is where we need
*  to start working as a community to go figure out we presented an
*  initial baseline. So going back to our original research
*  question is to what extent we found an extent we know this.
*  And now this is how we advance science is like, let's get other
*  people build on building that work. And let's see we can
*  improve the extent.
*  It definitely is, again, another major theme, just how many of
*  the benchmarks that largely have come out of academia over
*  the last, you know, 10 years have just been kind of blown
*  away by the latest models. I think that's one of the really
*  interesting indicators of just not only how fast things are
*  moving, but how fast they're moving relative to people's
*  expectations is that you know, you see like 2019 2020, even
*  some 2021 benchmarks that are just like, obsolete because
*  they're, you know, they're totally broken by the latest
*  language models. And they were built in the way that they were
*  because you know, that people didn't even, you know, couldn't
*  even really conceive of at the time that an AI would get good
*  enough to like, solve all this. It was like, well, gee, if we if
*  it's all about this, we have a GI, too, that there's a little
*  bit more room between solving these benchmarks and a GI, at
*  least. So now, you've got this kind of first stake in the
*  ground, basically, right? Here's, okay, all these old
*  simple schema benchmarks are increasingly obsolete. Now we
*  got to increase the challenge. Let's bring a real like
*  enterprise grade challenging problem to the to the models
*  here and see how they do. They don't do so well. Here's one
*  initial technique of layering on semantics that makes a huge
*  difference. And of course, we're fully expecting that people are
*  going to, you know, continue to improve on those techniques and
*  get better and better performance. Do you have any
*  tips for, you know, how people and especially for enterprises
*  that want to like do this for themselves for actual like
*  practical purposes internally? What sort of guidance would you
*  give them on constructing their own internal benchmarks or you
*  know, eval suites?
*  The contribution of our work, one is the is not just the
*  results of the benchmark, but it's the benchmark framework
*  itself. So what I'm telling everybody and actually working
*  with our own customers doing this too, because they're like,
*  we're working together to build these chances and these agents
*  systems as well. And they want to evaluate how good this is. So
*  one, they have their data, right? So they got that first
*  check. Number two is on the questions. So I think this is
*  really important to understand what are the questions people
*  are asking, and goes back to the one we were talking earlier
*  before, it's like you should we should catalyze and keep track
*  of the questions, right? So what are the questions people are
*  asking today? Who's asking them? Why are they asking them? Right?
*  And how are they solving those? Those answers? How are they
*  getting those answers today? Are they doing those answers today?
*  Through a spreadsheet that somebody gives it to them? Or do
*  they write a query? That they get through a dashboard? Like,
*  let's figure that out today. So then what happens is that get
*  those questions, let them put them into those quadrants, right?
*  It's just an easy question. It's just a harder question. This is
*  a question that is just the list of things versus this is the
*  question that actually involves aggregating all that stuff. And
*  this is a question that requires small amount of data or tables
*  or large amounts. So start putting that in into those
*  quadrants. So that is my main recommendation for folks. And
*  then in order to avoid boiling the ocean, make sure that you're
*  focusing the questions that are actually provides a value,
*  right? And that's why it's important. Who's asking those
*  questions and why they're asking those questions. I think that's
*  that's a very important thing. And then the third one is the
*  context. And I think the whole point of the work that we do,
*  the way we're presenting is that you should invest in the
*  context, you need to, you need to invest in the semantics of
*  what this stuff means. Because, frankly, that's what the LLM
*  is don't have. So you need to start investing in that. So
*  that's where people that's where at least our customers are
*  already investing in the context because they're already have
*  data. But for other customers who like thinking about this, I'm
*  like, well, if you want to have a chat with your data on your
*  on your relational SQL databases, and if you don't have
*  a catalog, you've got to solve that, you got to go build bring
*  in a catalog. But the catalog is for the sake of understanding,
*  keeping track of all that metadata to start building that
*  semantic layer and everything. And then don't boil the ocean.
*  That's where I would say then, then how that iron thread
*  approach and tie it, go bring in the data, you need to go answer
*  those questions and then keep track of all that metadata,
*  treat metadata, treat the semantics and the first class
*  citizen. So I'll get this summarized one, you already have
*  your data. So great check. Second, make a list of all the
*  questions, put them into quadrants and figure out and
*  prioritize them by the why behind them and then understand
*  how they're answering those questions today. And third, if
*  you don't have a catalog, then that's where you can start from
*  from that technology perspective.
*  So what do you think the prospects are for this kind of
*  chat with your data paradigm, right? The dream would be like,
*  we, the AIs get really good. And the decision makers, you know,
*  whether it's the middle of the night when they have their
*  brainstorm or, you know, whenever they can, I mean, AI has a lot
*  of advantages, right? It's like always instantly available. It,
*  you know, you can kind of pick up where you left off. I also
*  recite these here are the big challenges, presumably
*  accuracy. It seems like we're probably not there yet. You
*  know, you said kind of 60%. It's not good enough. I would
*  assume that. Yeah, probably not. Do you have a sense for like,
*  what is good enough and sort of what the steps are likely to be
*  to get there?
*  For the like in the benchmark, it was like 60% for all the
*  questions, right? Now, what we really, we'll really start
*  thinking about is, given a question, I need to analyze,
*  can I even answer this question? And I, so I think the first
*  thing, this is what we're working on right now is say,
*  Hey, give me questions. I know that I can answer this
*  question. I know, or give some confidence better than if I can
*  answer a question or not. So then what you're going to do is
*  reject the questions that you know you can't answer. And then
*  you're going to focus on answering the question that you
*  know you can't answer. And I highly suspect, and this is
*  something our research has shown us that from there, we can get
*  to the 90% of that stuff. So I want, so if I zoom out, and I
*  imagine the user going into your chat, you ask the question,
*  you'll either get an answer with an explanation, and I'll dive
*  into that in a second, or an explanation saying, I'm not
*  going to answer this question for the following reason. That
*  already gives you confidence around that. Now, when it goes
*  into like, when I do know that I can go answer a question, what
*  happens is, this is where the knowledge graphs come in, in the
*  type of accuracy and explainability. If I ask a
*  question, I can extract using the NLMs, extract the concepts,
*  all the things that are being asked that question, and I can
*  look them up in the graph. And if all the things that I'm
*  asking show up in the graph, show up in the knowledge graph,
*  I'm like, oh, I know about all these things. I can then form
*  a related query. But if I'm asking for a question, and I'm
*  like, oh, I don't, I can't find this in the graph. I'm like, I
*  don't know. So basically, you know what you know, and you know
*  what you don't know. So then that's how I can explain that I
*  don't know this, therefore, I'm not going to go answer that
*  question. And then if I do know, I can create the question, and
*  then I can answer it, execute it. And here's a big distinction,
*  is that LLMs are not answering the question. Because if the LM
*  is answering a question, you're trained in LM, then it's always
*  going to be probabilistic. Like it can be for certain, I can't
*  have certainty behind it. LLMs are going to be an assistant to
*  create the code that is going to be executed over the system
*  that's answering the question. And when it's code, that is
*  something I can reason upon, that is something I can govern,
*  that is something I can manage, and it's something I can use for
*  an explanation. So if I match it to the graph, I'm like, okay,
*  here it is, I generate this query, this is a query over the
*  graph. And I can and then this is where all the technical
*  metadata catalog comes in saying, oh, this exists in the graph
*  for this reason, it comes from this part, it goes to this table,
*  and this person was involved in the creation of this, it was
*  authorized by this, that's why you're getting that information.
*  So I can then not only give you the answer, I can give you an
*  explanation. And I can go as deep and granular and nitty
*  gritty and technical that I want. Or I can give it high
*  level. So I think also one of the things that we're working on
*  is to, another kind of cat in a little bit of an annoyance I
*  have is when we talk about explanations, explanations to
*  whom, right? You give a non technical person an
*  explanation, they probably just want an explanation in English
*  and also know who they should go talk to if they have a question.
*  Right? Don't give them code, they're not going to understand
*  it. If you're giving an explanation to a technical
*  person, they probably want to see the code, right? If you give
*  them just a high level of fluffy, they're like, that's
*  they're called BS on that, right? So you also need to
*  understand who are the personas are given explanations to. And
*  again, the graph is just basically, I can traverse the
*  graph as much as I can, to get as deep as the level of grain
*  learning that I need. So I think that's why knowledge graphs are
*  critical for the accuracy and for the explainability.
*  So I'm kind of mapping, you know, a bunch of familiar AI
*  application building techniques onto this problem. And one is
*  decomposition, it sounds like, you know, you could imagine just
*  taking the semantic layer and the schema and dumping that all
*  into context and saying, hey, have at it. Or you could imagine
*  kind of bringing that up and saying, okay, first thing, your
*  first job is to just look at the semantic layer and determine if
*  you have the information to answer the question, then you
*  can have a peek at the schema and actually generate the query.
*  That decomposition, you know, takes more work, it definitely
*  kind of makes things a little bit more brittle, depending on,
*  you know, how quick your system is to change or whatever, but it
*  really can drive accuracy. I imagine that's a part of it.
*  Fine tuning models, obviously also a big trend. GPT-4 fine
*  tuning is like in, you know, limited release. I don't know if
*  you've had a chance to fine tune that or if you've had
*  experience fine tuning other models to get better at this. But
*  that seems like another opportunity for improvement.
*  And then you mentioned earlier, too, like, established questions
*  and kind of canonical ways to answer them. I think there of
*  like the sort of skill database type paradigms, like the Eureka
*  paper or the Voyager paper out of Nvidia, where, you know, when
*  they find something that works, it's like, okay, cache that
*  basically to a database. And next time we get a similar
*  question, you know, or similar challenge. And, you know, in
*  their case was like Minecraft type of skill building. But you
*  know, here, it's obviously database type of work.
*  Let's see if we've done this before, you know, and have kind
*  of an established answer. I imagine all three of those are
*  kind of directions you are pushing on.
*  Yeah, I get the answer is always a it's hybrid. It depends. So
*  yeah, for sure. So I think from the science perspective, I start
*  with one thing to go see how well that stuff is. And this one
*  is like, let's start with the more bare bare metal prompt
*  engineering to go do things. And then you have other tools, you
*  want to kind of figure out like, what can I use for vector
*  databases that I can as another tool there's like, also note
*  that for the first experiment, like everything fit in the
*  context window, right? So maybe I have my apology, my submitter
*  is gonna be so big that I can't always pass it in here. So I
*  need to be able to kind of get parts of it out.
*  Were you working with the 8k version in this work? Or the 32?
*  The 8k? Yeah, because I mean, I'm telling you, it wasn't that
*  big anyways. And then when it comes to fine tuning, I think
*  there's there's two, two things to look into one is, are you
*  fine tuning with the data or fine tuning with the metadata?
*  And I will think that fine tuning with the data is probably
*  not going to be valuable. Because first of all, you got
*  millions and billions of rows in my Stokelake or Databricks, my
*  data lake house, are you really going to extract that and put
*  that in there? And so expensive and then which gets updated all
*  the time like that, or that, and then by the way, then in that
*  case, your LM is trying to go answer the question, but then
*  it's going to be probabilistic and non deterministic. And you
*  like, if you're going to go ask something, it's gonna get your
*  balance for your your bank account, better be freaking
*  accurate all the time, right? So like, I don't know. So there's
*  particular scenarios where you let me the accuracy is critical,
*  critical. So but when it comes to like fine tuning on the
*  metadata, I think that's that's going to be like huge
*  opportunities. And as you said, it's like, oh, here are these
*  patterns of questions, you're these types of questions. And it
*  gets these patterns of queries, like that's the stuff where you
*  want to go, go go fine tune on that metadata there, because
*  then it should have like, I know you're gonna generate the right
*  increased possibility to generate the right query. Now,
*  other thing is, when you generate a query, you're
*  generating a code, and I can reason upon that, and I can do
*  that in a deterministic manner, right? Now I can actually check
*  I can do static analysis, and I can check if this is the correct
*  if it could if the code is going to be correct or not, or
*  maybe with the budget heuristics. So then I think
*  there's another set of kind of techniques that you can go use
*  and suppose process. So it's prompt engineering or vector
*  databases, you're going to do fine tuning on the metadata, not
*  on the data, the metadata, you'll do some post processing.
*  So these are all basically just a bunch of tools that you'll
*  have. And we'll see is like, our agent frame, an agent framework
*  that will for each kind of state and that agent will use this
*  tool for this data will use this tool for this tool, this has a
*  lot of tools at its disposal. And I'd argue that a lot of the
*  IP that will come out is on how people are structuring their
*  agent frameworks. And how at the end of the day, you want to
*  have an intelligent agent who can really make understand its
*  environment, perceive its environment, make decisions
*  autonomously based on their environment. And that's really
*  going to be how sophisticated your agent framework or your
*  state model is going to be the current kind of rag architecture
*  that we all talk about. I think that's the simplest, most naive
*  type of agent system like right, you get a question, you send
*  something to get set up the vector database, which then get
*  context back and you simply all have like that's kind of one
*  snapshot for everything that's going to get it broken down so
*  many different pieces. And that's how we're going to start
*  developing the kind of these agents, which by the way, this
*  agent service is another thing I'm calling out there is we've
*  been working on agents is the good old fashioned AI, people
*  working on this stuff for like 50 plus years, there's so much
*  work on agents on planning. So hopefully we don't all spend
*  time reinventing the wheel and build on the shoulders of giants
*  and can advance very quickly here.
*  Yeah, one thing I took that I've found that I have a project I
*  want to ask for your advice on is when fine tuning this is
*  definitely proven true for GPT 3.5. unclear, you know,
*  everything has to be kind of revalidated when you move up an
*  order of magnitude and scale. So I'm not sure yet how this will
*  apply to GPT 4 fine tuning. But for 3.5, at least fine tuning on
*  chain of thought type data has proven extremely valuable for me
*  in terms of getting the fine tuned model to behave how I want
*  it to behave. It has not been good at learning facts that way.
*  So certainly wouldn't fine tune on like raw data, even fine
*  tuning on like, the definitions of tables and stuff, I wouldn't
*  expect that to work very well either, you're still gonna you
*  might do it, but you're still going to need it in context to
*  be like accurate from my experience. But where I've seen
*  the most boost is in kind of explaining the way in which we
*  want you to go about going through this problem. And having
*  a fine tune and it doesn't have to be huge, again, in my
*  experience, as few as like 100 examples can get you a huge
*  boost at the 3.5 level. But it's just really critical to have
*  that kind of explicit step by step that the model because
*  obviously we know that like chain of thought, you know,
*  think step by step is really helpful. But you have to kind
*  of demonstrate what kind of you know, chain of thought do you
*  want or do you need, you know, to solve the problems in the
*  particular context. So here's my challenge. And this is this is
*  really why I kind of got down this rabbit hole of knowledge
*  graphs a little bit in the first place. So I'm working with this
*  company, Athena, we're in the executive assistant space. And
*  we are trying to deploy AI in a million, you know, different
*  ways to enhance our service. One of the things that we know that
*  our clients would really like is if we had some way for the EA
*  is to have like, always on access to everything about them,
*  right, all their preferences, all their history, whatever
*  anything in the background, right, a lot of times right now
*  the EA is have to ask questions. And it'd be better if we could
*  somehow, you know, answer those questions without them having to
*  ask. So the idea is like, can we create a long lived client
*  profile that we can sort of maintain and update over time? A
*  huge challenge though is almost all the data is unstructured. We
*  like interview clients when they come on board and you know,
*  record that call and transcribe that call and then summarize
*  that call. But it's all text, the whole thing is text, there's
*  no schema whatsoever. So we can then throw that stuff into it in
*  a vector database and query against it and get you know,
*  kind of what did they answer at the time of the onboarding call?
*  But then of course, you know, things change, right? So how do
*  we add more to that database over time? And how do we sort of
*  manage like, what supersedes what? And I wonder, you know,
*  this is pretty early stuff. I think we're like, you know, I
*  don't know if we're on the absolute edge of tackling these
*  problems, but there's not too much work out there on this kind
*  of thing yet. But I wonder if you have any kind of thoughts or
*  intuitions for us as we think about something where they're,
*  you know, the core challenge here is there is no schema. It's
*  all just text. And we're trying to sort of be able to like dump
*  new stuff in there, but then have it maintained in a way
*  where we get the right information, you know, at any
*  given point in time. And we don't have great solutions for
*  this yet. So any any pointers or suggestions would be valuable.
*  I will argue that there's always a schema. There's always an
*  ontology, always semantics, and it's implicit, because you're
*  talking about the same concepts over and over again, you may be
*  using different words that mean the same thing. So an idea here
*  is like, take all those, all that text that you have, well,
*  then I'm structure stuff, and just ask GBT to say, generate an
*  ontology or taxonomy or business glossary for these things,
*  right? And I start and then you start identifying what these
*  concepts are. And I think if for your particular space,
*  right? Like, think about the domain, model the domain, like,
*  what do people do? Like, what are the what are the roles
*  involved with the tasks that those stuff are probably you're
*  probably have really generic ones that are going to go,
*  there'll be specific, they're going to be generic across all
*  types of companies, and then I'm sure there are going to be
*  things are very specific, but then kind of figure out what are
*  the high level ones that are generic, it's there. I mean,
*  you said there's no schema, there is a schema, right? There's
*  a meaning behind everything we're talking about. So just to
*  kind of automate it, just go get all that text and just say,
*  literally, the prompt and I just all the time, like generate a
*  generate a business glossary or generate a semantic layer,
*  generate ontology based on the following texts or questions,
*  it's going to come up with a bunch of stuff. And then you're
*  like, Oh, yeah, that that that that thing is related to this
*  thing. And then now you have like, a consistent, controllable
*  vocabulary way. And that's something that you that that you
*  can use later on for in your chain of thought, right? Or just
*  even how you're presenting things in the user interface or
*  how people are just chatting or conversing with it. I think in a
*  way, this is anecdotal, but I kind of when we set up these,
*  when we created the semantic layer ontologies, what we've
*  seen is that people start changing their behavior a little
*  bit and using the words that were that were defined inside of
*  that ontology inside that semantic layer. And then that's
*  a human behavioral thing is like, Oh, well, if I use these
*  words, I actually get my answers, right? So then they
*  start changing, then actually, as an organization, we all start
*  using a common vocabulary, we have that lingua franca. It's
*  like, at the end of the day, like, yeah, we should, we should,
*  it would be great if we start to agree on things. And I think
*  this is also a way to kind of get that have that can be. So
*  anyways, long story short, there is a schema in there use
*  GPT to help you extract what that schema can look like based
*  on all the texts that you have, and then then reuse that and
*  just any other techniques that you're doing.
*  Yeah, interesting. So would you recommend right now we are kind
*  of just chunking and dumping stuff into vector database and
*  kind of querying against that. We're using the hide technique,
*  the hypothetical document embeddings, which is, you know,
*  basically the translation when a user comes to our chat and says,
*  you know, what is x about the client, we translate that to
*  something that we think is like what the answer is likely to
*  look like. And that that's the hypothetical document embeddings,
*  you're familiar and then that seems to improve our the
*  accuracy of our retrieval. But we're purely using this like
*  vector database, we're not really using much structured
*  data. Do you have a recommendation for like, what
*  what database would you recommend? Should we go with
*  like a Postgres with their vector thing? Or should we be
*  thinking like graph database? Because we do have a lot of I
*  think a lot about that AI town paper. I don't know if you saw
*  that one. But it was the, you know, it made the rounds, it was
*  like these little AI agents were running around and like making
*  plans and interacting with each other. For me, one of the most
*  interesting aspects of that paper was the way they handled
*  memory was through a periodic sweep of all these raw
*  observational memories into these kind of higher level
*  synthetic, like thematic, you know, are kind of more episodic
*  memories, they would, you know, the agents would write down, I
*  talked to one at this time, we said this and this, but then,
*  you know, there's too much there, you know, pretty quickly
*  for the, you know, especially with limited context, that's of
*  course, you know, expanding, but to manage that they had to kind
*  of synthesize it into this like summarized layer. And I thought
*  that was really interesting. We haven't implemented anything
*  quite like that. That would seem like a very natural thing,
*  perhaps for a graph database of like, this was like synthesized
*  from this or you know, these, if I if I'm looking at some like
*  abstracted summarized memory, or, you know, description, like
*  what are the raw observations that that came from? Where do
*  you think I should put that data?
*  I think this is going to be a combination of using whatever
*  vector database, vector, similar indices, right? And then I think
*  some sort of graphs, I think this is my perception is that
*  that's where things are going to head. And then, I mean, at the
*  end, just use whatever graph database you want, and then
*  things change. I mean, I'm not a big from all that, use this
*  database or whatever. You're going to have virtual knowledge
*  graphs, where things where you have all your your, your, your
*  enterprise data, like, you're not going to move all your data
*  from snowflake or data breaks into a graph database and keep
*  copies of that. No way that's not going to happen. You're
*  gonna have a virtual virtualization layer. So it's
*  gonna you can query as a graph and it gets translated to SQL
*  for that. I mean, that's kind of what we that's exactly what we
*  did for our bench, benchmark work. So that's something if you
*  already have existing data in a relational database layer, your
*  data lake, you have a virtualization, knowledge
*  reference and relation layer. But if you're starting from
*  scratch, then I think you're gonna have a combination of
*  those two. Guess what's gonna happen? Every single structure
*  database is going to have vector features that they didn't
*  have it yesterday, had it today, but have it today, have it
*  tomorrow. So all graph database are having this right now is so
*  well as so much all the SQL database are gonna be up today.
*  Are vector databases gonna have SQL interfaces and graph
*  interfaces tomorrow? Yeah, I've been explicit about this vector
*  is databases. That's a feature, not a category, there only be one
*  winner. Whatever vector database is the one winner,
*  everything else, it's just gonna be I'm just gonna use this
*  other database and kind of a vector feature and it's gonna
*  be enough. That's what's gonna happen the next year or so. And
*  you will use that you will you you will need to use the vector
*  database if you have a real scale issue like a scale need.
*  Otherwise, all databases will be adding vector features. So
*  well, folks can juxtapose that against Anton's answer in an
*  earlier episode. His big thing, which I did think was
*  compelling, he basically said, the data that comes into into
*  chroma has never been in a database before. And he was
*  basically like, just the overall growth of how much data is going
*  to go into databases is headed for like 10x because of just all
*  the structured unstructured stuff moving into these these new
*  structures. And so like everyone can win, you know, because the
*  whole market is growing 10x.
*  Well, my whole point is that you look at the snowflakes and the
*  Databricks and the Azures of the world, who have already all
*  the SQL stuff, they're going to say, well, we should be able to
*  go support more unstructured and they will. And they will do that.
*  Now these vector databases, they're like, oh, we do that, too.
*  But they're like, oh, well, you don't offer SQL. So what does
*  it now reinvent SQL add SQL to that stuff? No, they're not. And
*  then it's it's now for scenarios where you need best scalability
*  and the raw and stuff for vectors that you will want that but
*  that market is like, I mean, that big, it's gonna be there's
*  gonna be one, one big player, and everybody else standing behind.
*  It's like MongoDB, right? MongoDB is the winner. And there are
*  other kind of NoSQL databases. They're all small behind.
*  Whereas one winner there, it's MongoDB period, right? They'll
*  look at their stock. It's something I think is what's
*  happening.
*  So what other uses for AI in data are you most excited about?
*  I'm thinking about things like, you know, as a application
*  developer, I find it still pretty tough in a lot of cases
*  to figure out like, what are people doing as they go through
*  my application? It's easy to like log stuff, you know, log
*  clicks and log whatever, but to really synthesize that into a
*  story, you know, a lot of kind of products try to do that. And
*  it's been a big struggle in my experience to get them to work
*  well. But I feel like maybe AI can kind of come along and
*  narrativize. I also think about things like anomaly detection,
*  or sort of, you know, determining like what's relevant
*  or not relevant, when it's not obvious by definition. But I'm
*  very curious to hear like, you know, aside from this kind of
*  chat with your data question answering use case, what other
*  roles do you see AI playing in the data, in the data world in
*  the near future?
*  Suggest descriptions about things. People have to go right
*  to subscriptions. And they're like, well, at least I don't
*  start from a blank slate anymore. Right. So that and
*  that's just applicable. I mean, I write an email about something
*  right, I just use it and start from scratch. Right. So I think
*  you're applying that for that type of metadata, just like any
*  type of documentation. That's a big lift on that. You can also
*  use it like use another one. I mean, talking about anomaly
*  detection or PII, like, just pass, just pass the schema to
*  GPT and say, out of this schema, which columns do you
*  think may have PII data, personal information, right? Or
*  it will give you some things like, hey, those are actually
*  pretty good candidates. And guess what, you don't have to
*  look at the data at all. Right. And that's probably even that
*  something already, it's a big lifter on that stuff, right. So a
*  lot of the documentation, they kind of just augmentation of
*  metadata, I think that's one thing. Second, for search, just
*  in general, I think just more natural language search, that's
*  it'll be another one that again, that's a productivity
*  lifter. One that I found really exciting is on explanations,
*  right. So it explains code very well, which is another type of
*  it's another type of documentation. So a lot of this
*  documentation you do. And one that I really kind of, I find
*  this really interesting working with one of our customers WPP,
*  who's the world's largest ad agency is they want ideations.
*  So I want to kind of use the use the LLM as a way to inspire me.
*  So we're basically it's like, data that world you have your
*  catalog of or data, you know, or data sets, tell me what are the
*  questions that I could be asking? What the data I have?
*  And then it's like, oh, so I start generating candidate kind
*  of questions that you can get to this question, so forth. And
*  then people like, oh, that's interesting. I don't think I
*  thought about that. And you can keep track of all these
*  questions, start connecting them. And then and then we've
*  been doing these things like, oh, I have this problem I want
*  to go solve. What data do you recommend me to go use around
*  that? So it's like, well, you can do all this context, here's
*  all the context that they have here at the problem. GPT come up
*  with LLM come up with some interesting solutions and then
*  make suggestions of what they can do. So it's about ideation.
*  But I think that's again, more of the product to do it. So
*  those are things that we're seeing here. Another one is
*  around this college, this knowledge acquisition. It's
*  like, let's go talk to people. Hey, so what do you mean? When
*  you mean customer here? What do you what do you mean by active
*  customer? Like, right now, we have to have those
*  conversations. What would you do? You would like what and now
*  I can kind of automate and scale that out saying, Hey, can you
*  please spend a couple of minutes chatting with my bot? You're
*  gonna ask me questions. And we've done this set up our
*  GPT is like, be a be a psychologist, be very Socratic,
*  and ask somebody what are the questions that they're trying to
*  go? What questions do they need to go ask to the data? And why
*  is that important? They go in? Why? Why and try to extract the
*  knowledge? Then in one day, I could, I could talk to 2030
*  different people. And then I could use GPT again to
*  summarize all these discussions saying, Hey, look, when we talk
*  about active customers, here are all these different definitions
*  of what they can be. All right, so that's really helping me
*  again, in the productivity way, faster understand what we mean
*  by things. And that's the one I'm most excited about. And I
*  hope people get excited about that too. Because that's the one
*  that has always been that bottleneck, the knowledge
*  acquiring knowledge from people's head is always the
*  bottleneck because if I go talk to somebody, now we actually can
*  do that. And at scale with this. And that means that we can learn
*  so much about how the business operates, map out business
*  operations. And we want to have operational excellence and
*  understand basically all our business processes and like, how
*  can we improve these things? Like, well, we don't even know
*  what our business processes are. Well, I can go interview
*  somebody saying, how do you do your job? And I can map that
*  out and say, Wow, look at all these manual steps that happen
*  for this stuff. Like, that's a bottleneck, we need to go
*  improve that so we can move our operations.
*  How far do you think this goes in terms of productivity lift in
*  the short term? Meaning like, let's just say we have the
*  technology we have, and we apply it well. Are we talking
*  like a multiple X increase in productivity? Certainly, I
*  personally feel that in the coding use case. And what does
*  that ultimately mean for data analysis? Like, do we end up,
*  you know, the old bank teller thing is sort of the happy story
*  where, you know, we introduced ATMs. And then, you know, people
*  said, Oh, that's the end of the bank teller, but it's not, you
*  know, there's been a lot more bank branches open classic
*  example. Is that where we're headed in data work as well?
*  And all work everywhere. I mean, I think we were on our podcast
*  yesterday, we had a Jeremiah Ouyang and he in we were
*  discussing this like, okay, what, who is not going to be
*  affected data? I mean, we came to the conclusion that only
*  somebody who literally lives in the middle of nowhere, it
*  doesn't talk to you, and it doesn't depend on anybody else.
*  But you're part of some supply chain. And that supply chain is
*  going to get affected by AI. So I think everybody is going to
*  get affected by AI, they'd be more productive and stuff. And
*  then there's just the honest no BS here is that yes, we're
*  going to deal with the job change that's going to happen,
*  there's going to be less jobs, and we're probably gonna have to
*  figure out UBI and what we were kind of just talking about is,
*  this is probably going to be at the top of the presidential
*  campaign campaigns in in eight years from now. Like eight years
*  from now, this is going to be a deal that this is going to be
*  top of the conversation. When we're elected president, there's
*  going to be premiums for dealing with humans or people at the end
*  everything's going to be so much automated work we're doing.
*  We're playing around with perplexity yesterday, like we're
*  doing the ball, we're doing our pockets or pie and like, like
*  this stuff is, it is replacing a lot of the humans, I mean, a lot
*  of stuff that humans are doing. So we'll see is, I will play a
*  premium, knowing that I'm going to interact with a human and
*  not with an AI. So I think everything is going to get
*  touched little, little by little. I another thing I say publicly,
*  and hopefully, people will take this the wrong way is like, I
*  feel bad people who are during coding boot camps, because that's
*  going to be completely commoditized. It's I mean,
*  writing code is going to be all fully automated. What we're
*  going to need are people are true algorithmists, computer
*  scientists, people who are thinking about solving the
*  problem, because you're going to come up with the algorithm, the
*  step by step to solve a problem. And the implementation is
*  going to break down into smaller pieces. And the
*  implementation, the code for that is going to be the project
*  will be 80 90% correct, right? So knowing how to code, but
*  without knowing how to think about problem solving, like
*  thinking about problem solving right then. So I think there are
*  all these jobs are going to go while I'm going to go away. I
*  mean, we've seen this again, over a generation. I mean, when
*  the typewriter came out, people were against it, because it's
*  like, Oh, if I write it by pen, I know who wrote it, I can see
*  their handwriting and like, No, this is offensive, because I
*  don't know that people are going to be right typing these
*  things that we don't know who's going to say these things.
*  People thought was the argument back at the beginning. Now,
*  well, I don't think that's an argument anymore. So all these
*  arguments will come in and the boat will go. And if things
*  gonna move so fast, we're gonna see some suddenly changes in
*  our generation.
*  So how would you anticipate that playing out for like an
*  enterprise data team if obviously, you know, can be
*  generic, but like, let's say you're a big enterprise, and
*  you've got all these systems and you've got however many
*  people, I don't even really have an intuition, you know, for
*  like, what's a typical enterprise data team size, and
*  what are the role breakdowns? But how would you expect that to
*  evolve in terms of like, headcount, you know, which roles,
*  you know, kind of change or go away? How much are people then
*  also spending on AI? Like, are they saving, you know, an order
*  of magnitude on their costs? Or is it, you know, the so does the
*  AI end up being expensive? I what's the before and after
*  picture as this transformation happens?
*  The roles that they're going to be there is they're going to
*  stick around or going to be created are the ones that are
*  very people heavy are the ones that are going to where you need
*  a lot of thoughts, right? So it's like, doing analysis, I
*  mean, they were like a data analyst, it's like, I mean, if
*  you're doing just the generic analyst, they're like, reporting
*  on metrics that are all very well known in a particular
*  industry, like that's going to go away because the all the
*  large language models on the AI systems will know all the all
*  the foundational metrics in every single industry like that
*  stock, right? So but then it's like, people are going to be the
*  creative thinkers, and they're like, well, what about this
*  nobody's thought about, like not even the AI is able to come up
*  with this, and we use the AI to like, so people are really,
*  really critical thinkers who are who people can connect the dots
*  from like so many different places like, oh, look, this is
*  probably something you should go figure out, like, I think that
*  those are the types of those that will really, really go
*  value. And then you can see that in in the analysis in the
*  analysis of the data, and coming up with the other one that I'm
*  very focused on is on managing the knowledge on your business,
*  right? That's going to get managing your being able to keep
*  track of that under understand. Yeah, the yellow limbs, AI agents
*  are going to assist me in kind of collecting all that knowledge,
*  but really then figuring out, okay, we're going to make the
*  side that the note that the an active customer needs this for
*  these reasons, right? Like, there's gonna be people behind
*  all that stuff. So I think it's all about critical thinking,
*  those are the roles. And then other than that, I think a lot of
*  that stuff is going to get pretty tumultuous.
*  You kind of alluded to creativity, you know, insight,
*  eureka moments, if you will, being one of the things that the
*  AIs don't cle deliver that we rely on humans for, I very much
*  focus on that as well, because it seems like that is a, I think
*  about AI a lot in terms of just threshold effects, like, when
*  AIs can do something, we can suddenly be in a very different
*  regime from as you know, as long as they can't. And having these
*  like insight, you know, kind of breakthrough eureka moments, it
*  feels like a huge threshold that we have not yet passed, certainly
*  not with any reliability, I would say it's like, very rare.
*  This is on my to do my to read list. I've seen a couple of
*  papers and I was like, well, this scientific discovery only
*  happened because we use the app like that is freaking amazing if
*  that's actually happening. Does that mean that we're actually
*  going to advance science and taking faster taking unknowns and
*  making them know like this is freaking amazing that just
*  happens. But it's not it didn't do it by itself. Right?
*  A lot of scaffolding. Yeah, a lot of kind of framework around
*  them is is definitely still necessary. And but yes, there
*  are I think we're just starting to scrape at the bottom of that
*  threshold right now with DeepMind recently had an interesting
*  one, where they advanced the state of the art and some
*  challenging math problems. It's funny. It's like, I don't even
*  really understand the problems. And they're, you know, the AI is
*  advancing the state of the art. Fun search. Yeah, I think of
*  Eureka, which is an actual name of a paper out of Nvidia where
*  they used GPT-4 to write reward functions for reinforcement
*  learning for robot control of like a robot hand. I get Gomez
*  who did the autonomous chemical reaction optimization with GPT-4.
*  So we're starting to see these like, you know, you might call
*  it sparks of AGI if you're so inclined. What else though, is
*  not a Eureka moments is like, that's a huge one. Is there
*  anything else that you would say, you know, if I'm a open AI,
*  or a Google DeepMind or an anthropic, and I'm like, where
*  are they falling short? What are the what are the kind of
*  persistent weaknesses that you would love to see us address? Do
*  you have a thought on that?
*  These foundational models don't know anything about my
*  organization. These foundational models, large language models
*  have one of the largest language model, they're experts in
*  language, they know general knowledge, right? They don't
*  know anything about my organization, because I've never
*  lived never looked at it, they were trying to the context brain
*  of my organization. And that's brain that brain is the
*  knowledge graph. Now the thing about the knowledge graph is
*  that it's not a language thing, right? It's like, I can't do
*  natural language part of the knowledge. But then this knows
*  everything about my organization, because I keep
*  tracking it, like governing, I use AI to govern, I use AI to
*  create it. But like, there is this thing that I have, and this
*  is my precious, this is the essence of what my organization
*  is, the brain, right? And everything here is accurate, I
*  can use this to explain things. The LLM, these foundational
*  models don't have that accuracy, don't have that explainability,
*  don't know my organization. Do we expect these foundational
*  models to know every single organization? No, because these
*  things is private, I don't want them to know, I want to go use
*  them. So that's why this combination of these
*  foundational models, large language models, with your
*  internal brain of organizations, which is where knowledge graph,
*  that's what I see where there's a future. And I think what we
*  need to find what we need to work on is understanding best
*  that integration points between the knowledge graph, the brain
*  of organization, and these foundational models. The naive
*  one is a prompt engineering, right? Use some rag architecture,
*  or then we're gonna expand this, this is what's gonna happen,
*  very, what we're gonna be working on, and then it's couple
*  years to figure out what that integration is. And then it's
*  gonna be a plug and play, you're gonna have all these
*  foundational models saying, no, I can, I can work with your
*  knowledge graph, I can work with your brain, right? Just play
*  and play, play in your brain here and boom, you're powering
*  up, right? And then also, I don't want to be as my company,
*  I've invested so much in my brain, I don't want to get tied
*  just to one thing, I can probably move around. I mean,
*  it's just like, it's gonna get like another cover. But you
*  maybe could get all bought in, right? We use all everything is
*  a we're in AWS shop, right? We're in Azure shop, I do
*  everything there. Probably when they go to put people are still
*  multi cloud, right? So I want to work with different
*  foundational models. So then, what's gonna happen? So we got
*  we're gonna have these integration points. So I do
*  think that organizations are going to be investing in
*  creating their brain, which is their knowledge graph, you have
*  all these foundational models. And then it's just kind of what
*  we're gonna we're just find better ways of plugging in
*  plane. And that's how we're gonna that that's the integration
*  points are gonna happen. And that's what we're focused on.
*  That's how I think about it. No, no, what do you think?
*  This is like a project that I'm, you know, maybe starting to
*  embark on is kind of a taxonomy of weaknesses of the current
*  systems. And I do think you're hitting on a big one there that
*  just I think that ultimately kind of boils down to the fact
*  that, you know, in today's systems, there are the weights,
*  you know, the model itself. And then there's like the stuff
*  that you're putting into it at runtime. And that is, you know,
*  the input, the context, the prompt, but it's limited. And
*  there's nothing between those two. I've been really obsessed
*  recently with state space models as something that may enable a
*  much longer, and perhaps more coherent, perhaps more agentic,
*  you know, perhaps more human like, although I don't, you
*  know, I heavily caveat the human like, because I always
*  try to remember too, that these things are pretty alien and in
*  critical ways, you can fine tune a transformer model for
*  behavior. But you end up kind of narrowing that behavior,
*  typically, and you lose a lot of the generality when you do that.
*  So you're kind of dialing it into a specific task. That's my
*  finding, you know, usually with with the fine tuning that I've
*  done so far, that you can't really do something where you're
*  like, training a transformer model, like you onboard a new
*  employee. And so I'm looking for something where I want to be
*  able to give a AI system like a big body of knowledge and say,
*  and maybe like a bunch of history and like, here's a bunch
*  of things that we've tried in the past that have, you know,
*  worked in some that have failed. And I kind of want to download
*  that knowledge into a system, not necessarily update the
*  weights, but have that encoded in some way, where it can be
*  then used to inform, you know, the runtime tasks that I want
*  to give it. And I think states based models are shaping up to
*  be a good solution there.
*  If I abstract what you just said is like, you're giving your body
*  of knowledge, things that you know, that works, that it
*  doesn't work right now, how are you representing that? Well,
*  the texture of whatever I think all these things should be
*  structured right in the graph and the knowledge graph, we
*  basically, but you're giving your knowledge, something you
*  have, and you're going to pass that on to these other
*  foundation models. And you're saying, hey, let's go do
*  something together. Right? So yeah, so you're like, that's the
*  thing is like, you have this foundational models, you have
*  your knowledge, you want to be able to integrate, combine that.
*  And again, how are we going to go do that? How where does
*  integration point to the beat? That's we're gonna go find out
*  what's the what is what is even the best one? What does even the
*  best mean? I don't know what we're figuring this out. And
*  then you'll be able to go combine that and then they're
*  not tired anymore, the privacy issues like you're right. So
*  that's what I find really exciting is like, you combine
*  external and internal things together. And that's what's
*  going to make it super powerful.
*  You've said a couple times along the way the no BS take on it. And
*  I know that that's a theme of your own podcast. You want to
*  tell us where people can hear more from you if they want to go
*  deeper down the data rabbit hole with you?
*  Yeah, so I in addition to the other kind of side work I do in
*  the data world is together with my co host that Tim Gasper who's
*  our chief customer officer. We host cataloging cocktails, the
*  honest no BS non sales and data podcast. We've been at it for I
*  think we're on our fourth year now. So we started season seven.
*  I don't know I've lost the episode 160 or something like
*  that. We talked about all things enterprise data management
*  analytics, governance, and stuff. So honest no BS because
*  life is too short for BS and drama. So cool. I love it. Well,
*  I'll check that out. I'm sure others will too. For now, Juan
*  Cicada, principal scientist, head of the AI lab at data dot
*  world. Thank you for being part of the cognitive revolution. It
*  is both energizing and enlightening to hear why people
*  listen and learn what they value about the show. So please don't
*  hesitate to reach out via email at tcr at turpentine.co or you
*  can DM me on the social media platform of your choice.
*  Omniki uses generative AI to enable you to launch hundreds of
*  thousands of ad iterations that actually work customized across
*  all platforms with a click of a button. I believe in Omniki so
*  much that I invested in it and I recommend you use it to use
*  cog rev to get a 10% discount.

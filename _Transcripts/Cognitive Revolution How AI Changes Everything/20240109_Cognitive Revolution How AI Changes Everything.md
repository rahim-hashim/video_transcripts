---
Date Generated: April 02, 2024
Transcription Model: whisper medium 20231117
Length: 4963s
Video Keywords: []
Video Views: 778
Video Rating: None
---

# Dialpad's Chief Strategy Officer, Dan O'Connell, on AI-Powered Business Communications
**Cognitive Revolution "How AI Changes Everything":** [January 09, 2024](https://www.youtube.com/watch?v=9J2XwywDdI4)
*  It's not that I'm like racing to replace people or, you know, cut costs or whatever.
*  But I always kind of come back to sort of, you know, a Bezos style, like,
*  what does the customer really want? Right. And the customer wants like immediate response 24 seven,
*  like where I can pause the conversation where I want to at my convenience and be able to come
*  back and pick it up, you know, right where I left off and maybe even switch modalities.
*  And, you know, chat, BT offers me all these things today.
*  Hello and welcome to the cognitive revolution, where we interview visionary researchers,
*  entrepreneurs and builders working on the frontier of artificial intelligence.
*  Each week, we'll explore their revolutionary ideas and together we'll build a picture of
*  how AI technology will transform work, life and society in the coming years.
*  I'm Nathan Labenz joined by my co-host Eric Torenberg.
*  Hello and welcome back to the cognitive revolution. As we head into 2024, I've been
*  thinking a lot about where we are in terms of AI's impact on knowledge work. While 2023 certainly
*  brought explosive growth in AI adoption, to be honest, things have moved a little less quickly
*  than I had expected. At retail prices, $1 billion only buys one to two GPT-4 API calls for each of
*  the world's 8 billion citizens, which really just goes to show what a tiny toehold language models
*  have established in knowledge work globally. Even if this were to go 100X over the next year,
*  it's still just one GPT-4 API call per person per day, still a tiny fraction of the knowledge
*  work that humans are doing. So why this delay relative to my admittedly very high expectations
*  and what are the likely solutions? First, while I've definitely argued that open AI
*  has modes, I have been a bit surprised by how long it has taken for other companies to match the
*  quality of GPT-4. It's fair to say I think at this point that GPT 3.5 level models are effectively
*  commoditized, but GPT-4 is different. Only Anthropic and now Google with Gemini are really even in the
*  ballpark in the West. Though it's worth noting, and I do hope to have another episode on this soon,
*  that Baidu's Ernie 4.0 also appears to be a worthy contender. A second major issue is that
*  language models are weird, and the know-how to successfully implement them into automated
*  workflows remains relatively scarce. Most companies are naturally excited about opportunities to save
*  90% of their costs by automating tasks that nobody enjoys anyway, but if they don't have or know
*  someone who can execute on such a project, they really have no choice but to wait.
*  A third issue is that AI agents, which promise to allow people to delegate work to AI on a real-time
*  more ad hoc basis, have not matured as fast as I thought they might. In part, that's due to ongoing
*  GPU shortages. I've repeatedly said that I think GPT-4 Vision, originally introduced in March, but
*  only now hitting general availability, will boost agent performance, and indeed we already are
*  starting to see new reports of much better performance at significantly lower cost simply
*  because computer interfaces are designed to be interpreted visually, and GPT-4 Vision now makes
*  that possible. What else is standing in the way? Another challenge is that it turns out that we
*  can boost AI performance significantly by decomposing tasks into subparts, but then when we try to string
*  long chains of these subparts back together into meaningful work, it becomes very tricky to
*  determine what information to give the AI at each step along the way. So, the first thing we need to
*  do is to give the AI the information that it needs to give us, and then we can start to work on
*  the way. Too much information can be unwieldy and in any case makes the agents slower and much more
*  expensive, while too little information leads to bad decisions and overall failure. GPT-4 Fine
*  Tuning, which is also still in early access only mode as of now, will probably help here. Fine
*  Tuning in general is very useful for shaping model behavior, and regular listeners will know from the
*  base models to deliver more coherent, agentic behavior as well. But even if so, this would pose another challenge.
*  Where are we going to get all the long episode, context-rich, how we work in practice sort of data
*  that we're going to need to train these long context AIs? Where does that data exist today, if at all?
*  One likely source of such data, I think, are the software platforms in which people currently do
*  their day-to-day work, which naturally capture records of the work and also implicitly define
*  the space of possible actions that a human or a hypothetical AI agent might take at any given time
*  along the way. So, with all that in mind, I was very interested to discover Dialpad, a communications
*  platform that uses AI to deliver assistance, automation, and insights to human users, who today
*  are mostly sales and customer success teams. Having been in business for years and having grown a
*  customer base to more than 30,000 businesses, Dialpad is now in a unique position with a
*  proprietary data set of more than five billion minutes of sales and service calls, which they've
*  now used to train their own transcription and large language models. This looks to me like a near-ideal
*  opportunity to begin experimenting with AI employees. Though, as you'll hear in this conversation
*  with Dan O'Connell, Dialpad's chief AI and strategy officer, he's not expecting these changes
*  quite as rapidly as I am. And based on my predictions last year, I have to say there's a
*  pretty good chance that he'll end up being right. Yet, at the same time, regardless of how long it
*  takes, it does seem clear to me that huge amounts of routine knowledge work will ultimately be done
*  by AI. So, while I'll continue to hold myself accountable for the best possible predictions
*  that I can give, it does also seem to make sense for me to bias my analysis toward shorter timeline
*  scenarios, simply because those are the ones in which AI scouting will ultimately become most valuable.
*  As always, if you're enjoying the show, we'd love it if you'd take a minute to share it with your
*  friends or leave us a review on Apple Podcasts or Spotify. You would be amazed at how few reviews
*  we get. I literally get 10 times as many personal notes as we get online reviews. And yet, I understand
*  that it does make a huge difference to podcast distribution. So, I would really appreciate it if
*  you would take just a minute to write a short online review. Now, without further ado, I hope
*  you enjoy this conversation about AI and the present and future of knowledge work with Dan
*  O'Connell, Chief AI and Strategy Officer at Dialpad. Dan O'Connell, Chief AI and Strategy
*  Officer at Dialpad. Welcome to the Cognitive Revolution. Nice. Thanks for having me, Nathan.
*  I'm excited to talk to you about the platform that you guys have built and are continuing to build
*  and are making more and more AI-centric. One of my calling cards in doing this show is I do my
*  homework. So, I've gone in and created a free trial account and bounced around and called myself
*  and transcribed a little bit. So, I guess I would briefly describe Dialpad as a sort of
*  almost everything hub for the work that sales and customer service teams in particular are actually
*  doing. You're actually in Dialpad a lot doing your work. Tell me about the product and your
*  customers, I guess, for starters. Yeah. You see me on video. I'm smiling and laughing as you're
*  describing. You did exceptionally well. And I would add, a communications platform is the easiest way
*  to think about it. We do voice video messaging on any device anywhere in the world. That can be used
*  for internal communications between teams, but it can also be used, as you mentioned, for external
*  communications supporting sales organizations or customers. And we build AI throughout that platform.
*  So, how do we go capture a conversation, transcribe it, and then focus on building
*  features that help with assistant automation and insights from those conversations?
*  Assistance, automation, and insights. Okay. We'll come back to that. I looked you up on G2 as well.
*  Good reviews, upper right quadrant. 56% of the businesses SMB, 37% mid-market. What would you say
*  is kind of the state of... You can even maybe broaden a little bit beyond AI, but I'm very
*  curious about AI adoption, just knowing this business segment as I do and knowing that they're
*  not always the quickest to embrace new technology. Yeah. And those are obviously self-reported from
*  G2. We would classify ourselves on our revenues. And then just for context, for size of business,
*  north of a tiered million dollar ARR business, 30,000 customers, pretty much a third, a third,
*  across SMB mid-market and enterprise. We have some really big brands that use this, Stripe,
*  Twitter, Uber, HubSpot. Then we also can go and empower really small businesses that might be
*  a law firm of two or three people. I would say the general thing that we see from our customers are
*  very much people that believe in the cloud, to no surprise. But when you talk about communications,
*  there's still a lot of people that run their whole PBX system or phone system in a closet with wires
*  behind it. And for us, it's really much we see a lot of people that believe in, look, managed
*  services should live in the cloud. And those people tend to be on the forefront of wanting to
*  try out AI powered features. So they believe in having a transcription and being able to map
*  sentiment as opposed to getting into the arguments around wire topping laws and call recording laws
*  and things like that. Those are not the types of conversations that I would say many of our customers
*  are pushing. Yeah, interesting. Okay. Well, I think that's a pretty,
*  the third to third to third is an interesting accomplishment, really. I mean, to build software
*  that can serve the enterprise and small business at the same time is a real challenge. I've dabbled
*  in that a little bit. And again, this goes beyond the AI focus, but the just raw number of features
*  and configurations and next thing you know, you're kind of, how do we not become Salesforce
*  while we try to meet all these different customer requests? And at the same time,
*  you need something that's really intuitive for small businesses who don't need or want any of
*  that stuff. I guess one thesis I've had, and I think you've largely addressed it so far with just
*  disciplined product development, but I've had the idea that a lot of that complexity maybe gets
*  smoothed over over the next year or two with natural language interface. Like maybe everybody
*  who has a crazy complicated platform can start to go down market because they can hide 17 menus and
*  say, what do you want to do? And just translate the user need into configuration on their own
*  platform as appropriate. Does that seem realistic to you, even if it's not maybe your most pressing
*  problem relative to other software platforms? Yeah, I actually agree with you on that. And I
*  think, you know what the interesting thing of, you know, I think one of the unique opportunities for
*  large language models actually is putting them on top of analytics. And you think of business
*  intelligence platforms today, because as much as we're a communications platform, as I said, like
*  the stuff that got me really excited that this to tie this back is, hey, you want to go power
*  communication on any channel, we want to go understand it in real time. So let's go capture
*  it, transcribe it. And once we have it transcribed, well, now it's in text format, we can do all sorts
*  of things with it. And if you put a large language model on top of that, you suddenly have this robust
*  analytics platform. If you think about building an analytics platform today, or even a database,
*  you need a bunch of filters to go and search things. Right. And so that creates a lot of
*  complexity. Everyone wants different filters, they want their data in different ways. And
*  to me, one of the biggest opportunities now is you can put a conversational search interface on
*  top of the analytics. And that, to your point, streamlines the complexity of the software you
*  need to build, simplifies the experience that users go and have, and I think really starts
*  to unlock the potential of like this last, you know, I call it like the last offline data set,
*  which is these conversations. So you're really excited thinking about that, try to, you know,
*  kind of tying it back to what you say. But yes, I think there's actually a simplification that
*  happens. And, you know, we naturally think of simplification coming from the SMB market,
*  as opposed to the enterprise market. But I do think that's something that's going to start to
*  play out. Okay, cool. So can you give me a little bit better sense of how, when I signed up, you
*  know, there was the list of 10 possible, you know, departments and roles. And so I wasn't quite clear
*  on like, just how broadly the software gets deployed within an organization or kind of,
*  you know, maybe it gets deployed very widely, but there's, you know, certain people that are
*  the real in their hour by hour users. Like, am I right to believe in? I have kind of some big
*  questions in mind that I think depend on this answer. How much of it is like the sales and
*  customer support versus like the whole organization? Yeah, I would say probably the fastest growing
*  segment of our business is providing that uniqueness, communications and AI for sales
*  and support organizations. That said, the vast majority of our customers, if you take those
*  30,000 customers, are deployed across the internal communications. And as I said, our friendly
*  competitors are, you know, to actually put it out there and clarify for votes, are going to be the
*  teams, Microsoft teams, Zoom, Ringcentral's of the world. And then when you get into the sales and
*  service side, the five, nine and eight by eight and talk desks of the world. But as I said, the
*  nice part about our business, you know, as I said, is we saw into these three segments, we also sell
*  this one consolidated piece of software that can support these different users. So we might be
*  deployed just on a sales organization, or we might be deployed just within a service organization.
*  But that gives us again, these kind of upsell opportunities to go and demonstrate the value of
*  unified communications platform, the power of AI and then go talk to them about the internal
*  communications over there. But the vast majority of our customers, let you know, my long-winded
*  answer is vast majority of us are deploying us across the organization. And then different,
*  they're leveraging different features depending on, you know, the persona or the use case that they
*  have. Got you. Okay. So for the power users, how much of their time on a given day, would you say
*  is like in the dial pad UI versus tasks where they sort of have no choice but to leave the
*  the dial pad experience to go do something else?
*  Service and support, they can live in that application. As I said, you know, if you think
*  of a contact center agents, probably sitting there waiting for, you know, taking inbound calls,
*  we've got integrations with, you know, all sorts of the the CRMs that they would go and have
*  send us up spot Salesforce to go, go pull information and provide them with the record
*  information they would go that they would need or help them drive assistance from those
*  conversations. But the intention is, you know, the way that we use dot pad internally is that's our
*  internal communication platform. And that's also what our sales and support teams are using. So
*  I look here, I'm like, that app is loaded for me up in my browser window, front end center,
*  you know, my entire workday. But as I said, there's always going to be these other interfaces that I
*  need to go and engage with. But we want to make this the single destination to go and power the
*  communications when you need to have a video meeting, personal phone call, you know, a business
*  phone call, and then to go and pull the contextual information that you need for different
*  integrations or workflows, whether that's again from from systems of records or from ticketing
*  systems, whatever it might be. Yeah, so it sounds like you're developing your own version of kind of
*  the rag paradigm as well, like access into even broader knowledge bases than sales and support and
*  AI question answering all that kind of stuff I imagine is on your mind.
*  It is. Yeah. Yeah. I mean, yeah, you think about recruiting, right? So you think about opportunity,
*  kind of these tangential markets up and not where, you know, recruiting organizations are just
*  recruiters. You and I need to have a call, maybe, you know, you're interviewing for a role and I
*  need to make sure I'm asking the right topics and doing that a consistent manner. We can help guide
*  that conversation. So there's everybody that's doing the interview is asking the same questions
*  to the same person. But we can go capture those responses and then write them into greenhouse,
*  you know, for example, which would be a CRM or assistive records for recruiting organizations
*  or recruiters to go and leverage. But again, it's really about, hey, we want to go power those
*  communications wherever they're happening and then starting to provide either context to the user
*  or start to automate tasks and workflows that stem from those conversations.
*  OK, cool. Let's change topic for a second and then switch back to more practical,
*  you know, closer to the user, more product experiential things in a minute.
*  So I saw that you just announced not too long ago the creation of this dial pad GPT
*  large language model, which has been trained on. I'm just reading from the blog post.
*  Five billion minutes of business calls and online interactions. The world's first business focused
*  LLM. Five billion minutes is a lot of calls. I guess for starters, like, you know, I'm translating
*  that in my head to five hundred billion tokens. If I'm thinking just a hundred words a minute of
*  conversational speech, that becomes, you know, five percent of GPT for training scale. If I,
*  you know, triangulating effectively here. So that's that's pretty big. I guess, you know,
*  bunch of questions around that, like where does all that data come from? Is that just stuff that's
*  been recorded in the platform over time? And then, you know, how did you actually undertake the
*  project of creating your own language model? I imagine, you know, potentially some partnership
*  involved or. Yeah. So one thing is so we had started a startup called TalkIQ and that was one
*  of the first real time speech recognition engines back in 2016. And at that time, you know, give a
*  little bit of context to the listeners is at that time, if you were going to get a transcription,
*  you would typically go capture capture a conversation, you know, a WAV file or an MP3
*  file. You could put it through a third party, typically take you, you know, if your if your
*  conversation is 30 minutes can take you 30 minutes before you can not put back. So there's this big
*  delay. And we thought there was this really interesting opportunity, especially for sales
*  and support conversations, say, like, look, if you can go capture and build a streaming engine
*  and understand a conversation in real time, well, then I can start to route a conversation, you
*  know, based on what Nathan might be asking about. I can start to map it sentiment in real time.
*  I can start to guide a person. I can do live agenda tracking, like all these opportunities open.
*  So we got really, really excited about that opportunity. So we built a real time speech
*  recognition. We started to leverage some open source software. I think, you know, a lot of
*  people when they say, hey, we're building something from the ground up, you tend to start with
*  there's fantastic open source software out there. So we started with call date, which was a model
*  for speech recognition and build this fantastic, this really accurate, fine tuned model to go and
*  do long form conversations. And I say long form meaning when you do a phone conversation,
*  that's very different than when you talk to Google in Syria and say, you know, what's the weather,
*  you know, set a timer. And these were really complex, difficult challenges, you know, just
*  roughly a decade ago, which is kind of funny to think about. So we built this engine. And then
*  when you're building a startup, what you need is distribution. And so dial pad at that time was,
*  as I said, a really broad communications platform, their founding team came out of Google, they had
*  built Google voice. And so it was a really kind of peanut butter and chilly moment to use an analogy
*  of, hey, we can go understand the conversations, you got the distribution of power in conversations.
*  And over those years, as I said, I've been here now for five, for five and a half years.
*  When people leverage our platform, they can opt in to share that data. And these are all long
*  form commerce, business conversations, or enterprise conversations, and the vast majority of them are
*  sales and support related. And so that becomes this fantastic training set for us again, that
*  people opt into we are not when we leverage the day, we obviously anonymize it strip of any
*  personal identifiable information, etc, etc, etc. And when we started to then, you know,
*  I think the world's gotten enamored a year ago with kind of large language models,
*  fortunately, by chat GPT. And so we're really quick at saying, look, this is that suddenly this great
*  opportunity, we got this training set, we go power these few occasions, and we put this large language
*  model on top of that, like all these opportunities open up. But these foundational models have some
*  challenges with capacity, you talked about token limits. So if you think about a transcript,
*  initially, you would have to go break up a transcript six different times. And, you know,
*  if you did that creates challenges even to start to do things like to do summaries. And so it
*  became, you know, the challenges for these foundational models for us were capacity,
*  the token limits, latency, you know, how quickly we're going to get an output back cost. And those
*  challenges were things that we didn't think we could wait for. They're all engineering problems
*  that get resolved over time. And so what we did was actually focus on building our own large
*  language model. And so there's two ways that we've approached that one is so you take fantastic
*  open source software, you fine tune it. Fortunately, for us, as I said, we've been at this for some
*  time, we've got a bunch of experts and everybody from conversational neuroscience to linguistics,
*  we do our own labeling, we know how to build these models, and they have the data set and
*  the know how to do it. And then we're also working on building our own large language model from the
*  ground up. When I say large language models, ultimately a smaller language model that's going
*  to be spit built specifically for specific industries and use cases. Hey, we'll continue
*  our interview in a moment after a word from our sponsors. Real quick, what's the easiest choice
*  you can make taking the window instead of the middle seat, outsourcing business tasks that you
*  absolutely hate? What about selling with Shopify? Shopify is the global commerce platform that helps
*  you sell at every stage of your business. Shopify powers 10% of all ecommerce in the US,
*  and Shopify is the global force behind all birds, Rothy's and Brooklyn and millions of other
*  entrepreneurs of every size across 175 countries. Whether you're selling security systems or
*  marketing memory modules, Shopify helps you sell everywhere from their all in one ecommerce platform
*  to their in person POS system. Wherever and whatever you're selling Shopify has got you
*  covered. I've used it in the past at the companies I've founded. And when we launch merch here at
*  Turpentine, Shopify will be our go to Shopify helps turn browsers into buyers with the internet's
*  best converting checkout up to 36% better compared to other leading commerce platforms.
*  And Shopify helps you sell more with less effort. Thanks to Shopify magic, your AI powered all star
*  with Shopify magic whip up captivating content that converts from blog posts to product descriptions,
*  generate instant FAQ answers, pick the perfect email send time. Plus Shopify magic is free for
*  every Shopify seller. Businesses that grow grow with Shopify. Sign up for a $1 per month trial
*  period at Shopify.com slash cognitive. Go to Shopify.com slash cognitive now to grow your
*  business no matter what stage you're in Shopify.com slash cognitive.
*  So you're doing this training in house like you're managing your own cloud. I would have
*  guessed that you were partnered with like a mosaic or something like that to get over the,
*  you know, the gnarly parts of the large scale pre training.
*  Yeah, we do everything in house, we have our own GPU hardware. So we have got our own capacity for
*  a 100s. And the nice part for us is we do all the bare metal. So even our telephony platform,
*  what's unique for us is because when then to tie this back to like the world of communications,
*  a lot of people when they think about building a communications platform today think about
*  old Twilio as a CPaaS provider, hey, there's API is to go power, you know, voice and messaging.
*  So why go build that yourself? I mean, for us, we think that the best businesses verticalize their
*  stack, you can see that in in different industries, whether it's without bill, you know,
*  not building on silicon, you can see it in automotive industry with businesses like Tesla.
*  But I think the biggest uniqueness that comes from owning your stack is obviously the pace
*  of innovation and then cost advantages at scale. And those those two things allow you to actually
*  bring I think uniqueness and better markets or better products to the market faster than anybody
*  else. And so again, I think, I don't know if we would make always the same decisions that we have
*  in the past, if we were to start a startup today, but based on the proprietary data set we had the
*  people that would that know how that you have in the team of experts, we've done a lot of this
*  in house. That doesn't mean that we don't, you know, we do partner with with open AI to leverage
*  the foundational models in certain aspects of our business. We also partner with Google,
*  leveraging Google for tech, which is one of our bison, which is one of their large language models
*  today to power some features as well. So we do plug in some partners in different places, but the
*  vast, vast, vast majority of things we do is all done in house. Yeah, I guess I'd love to hear this
*  is I think such a big challenge for so many right to know kind of
*  what to build, what to buy, what to partner for, in a world where things are moving extremely fast.
*  And I think you, you know, I'm a little bit surprised by your answer. And I think it, you know,
*  it's it's a flex because most, maybe not most, but certainly, I think a lot of companies out there
*  might say, Oh, you know, let's llama to, you know, let's save money, or let's, you know,
*  own our stack or combination of the two, whatever, let's go, we'll fine tune that,
*  you know, we'll, we'll be, you know, we'll control our own destiny and whatever. And then it's like,
*  but if you don't have a real skill set and kind of a knack for it, right, and there's there's multiple
*  different critical components, I would say to the skill set from, especially if you're doing
*  large scale stuff from scratch, managing a cluster to kind of, you know, open AI recently
*  described it as the artisanal process of shaping language model behavior. And it seems like I would
*  expect so many companies that may be great at what they do to try to add on this type of discipline
*  and sort of get bogged down in it. And next thing you know, like, open eyes kind of release their
*  next version before you've made, you know, llama to really work. So do you have, is it, is it about
*  just the team that you guys have already assembled that you think is just differentiated? Or do you
*  have strategies that you could recommend for how to avoid falling into that trap? Because I do think
*  a lot of people are headed that direction if they try to follow your specific path.
*  Yeah. And I, and I think that's why I said, you know, even here, I try to be really keen on
*  stuff is I think, you know, fortunately, because of the decisions we made in the past, and it's been
*  kind of fun to see how this has played out. I don't always know if we would make this same
*  decision, you know, starting from scratch. So some of that is, you know, we have a team of experts
*  that's been in these fields for working with these technologies for 10 plus years, just at the
*  forefront of building product. But a lot of the people on our team, you know, we've got over a
*  team of 50 focused on AI, 18 PhDs, we've got 16 patents, we show up at the best NLP conferences
*  in the world and win awards for the models that we're building in development. So some of it,
*  I think, much like anything, it always comes back to the team of experts that you have and the access
*  to the data set that you can go and leverage. So as I said, because of those two things of that
*  decision, you know, six years ago for Dialpad to be focused on AI then has played out nicely to
*  position us today that gives us I think some advantages over relying on a third party API to
*  go and do things. And, you know, when that when chat GBT, you know, was given us some excitement,
*  you know, two weeks ago, I can tell you we were probably one of the few businesses that
*  were I say, I'm concerned, we were all, you know, following this, you know, because I thought it was
*  just a really interesting business, that business thing that was going on. But we were probably one
*  of the few businesses that was like, Hey, this doesn't impact us. Like, we're not worried about
*  whether our summarization is going to go down because the company may cease to exist overnight.
*  We don't rely on them to do that. And so again, I think that always why you know, as a as a
*  technologist, why it's always to me, I do believe in like control your own destiny, innovation,
*  like that's where you're going to really win or lose markets. And don't I say outsource, but you
*  know, for lack of a better word that that's alluding me, but don't outsource don't outsource what you
*  think are the most important parts of your business. And I think right now, I do believe and I know it
*  sounds a little bit generic, given the money, you know, everything in the news and so forth. But I
*  do believe that AI is the biggest opportunity. And so I think there is a better experience,
*  more cost effective experiences, because we are a business that you can do by doing that yourselves,
*  but that comes with a bunch of landmines and a bunch of challenges. And it's not easy for sure.
*  Yeah. What do you think businesses should prioritize? Most I mean, we kind of talked
*  about a few different values there where there's almost always trade offs, right? You've got
*  on the one hand, what's the absolute best performance that I could get, you know, if I
*  don't worry about latency or, you know, financial cost, then there's like, you know, if I put some
*  constraints on those, then what's the best I can get? And then there's like, you know, now how much
*  would I trade off that performance for, you know, further improvement in latency and cost? I think
*  even that decision making structure is really tough for a lot of folks. It's, you know, it's pretty
*  unfamiliar territory, just given the new, you know, just traits of this technology. I mean, it's like,
*  it's weird, right? It's definitely slower than most software we're used to. It's more expensive,
*  you know, on the margin than most software we're used to, probably in both of those by like,
*  orders or can be orders of magnitude. Obviously can do, you know, tremendously more stuff than
*  most software we're used to. But do you have kind of any coaching for how people should think about
*  those relative dimensions of like, of the good in their AI product development?
*  Yeah. And I can give you, you know, this is our matrix. I think obviously it depends on the
*  business that you're in. So we'll, I'll start with, we have a matrix around that. Number one is latency.
*  And what I mean by that is we think the biggest opportunity for our business is how can we do
*  things in real time for a conversation? What I mean by that is, you know, if we were going to go,
*  we do things like agent assist, so we can like pull information from a knowledge base,
*  presented to your user in real time in terms of like milliseconds of latency. If that assist card
*  didn't show up for three seconds, it loses its utility even a second later. And if it's 10
*  seconds, there's just no point in even building that feature. So everything when we talk about
*  always starts with the most innovative features, the most interesting things we can do have to be
*  as close to real time as possible. So that means latency really matters. Two is then how do we get
*  these features? If you can go do that in real time, how can you get them in the hands of as
*  many people as possible? So that again, it comes back to the question of like capacity
*  and what's available from these large language models. And those are still challenges today
*  for a lot of these models, which is like at what scale can they operate, right? Or can you get them?
*  And then the third is cost. And I think cost is one of those things that you can solve over time.
*  If you're really providing value to a user, then you can always get the additional,
*  the additional costs or price that you need to cover, kind of maintain your margins or improve
*  your margins, whatever it might be. And margins tend to improve over time as I said, you can
*  always optimize that. So the cost piece tends to be, you know, third on the list, you know,
*  there's other things, but to give you the way we think about it, like cost is not the blocker for
*  us. Like we're, we've raised, you know, a half a billion dollars in venture from the best investors
*  in the world and Trace and Horwitz, Google Ventures, Iconic Capital, just to name a few.
*  And we think there's just this unique moment in time to drive innovation. And so let's really
*  focus on like the latency piece, because that's going to provide the best experience and get
*  in the hands of as many people as possible and worry about the cost later. And if you're an
*  earlier stage startup that is more capital constrained, then, you know, cost might be
*  a number one of that list. Yeah, interesting. So then how do you think about performance in terms of
*  just like the quality of the insights or, you know, whatever the task is? Because I have mostly
*  thought about now I haven't really done anything in this sort of highly real time way that, you
*  know, and that I totally appreciate the rapid depreciation of a tip, you know, that once the
*  moment is passed, it's passed. So totally get that I haven't operated in that environment.
*  But my intuition in most of the things that I've built has been try to maximize the quality of the
*  AI output first subject to, you know, it does even if it takes three minutes, you know, in terms of
*  latency, then that can can start to be a deal breaker. You know, again, it depends on exactly
*  how much better you know, the best configuration of best model might be relative to my alternative.
*  But do you think of it in terms of like, we want to get above some threshold of utility and then
*  then we focus on all these other things? Or how does that kind of fit in?
*  Yes. So let me Yeah, so I'll refrain my answer of assuming that you are pleased with the output of
*  accuracy. And so when we build models, there's two ways as ours that we do come up with thresholds
*  of what we think are going to provide quality output and utility to as we all dog food these,
*  these, these features ourselves, meaning our support team goes and leverage and sales team
*  leverages the models that we build along with every one of our employees. If we don't think it's
*  providing utility is a good feature, then there's no way that we would expect anybody ever to go and
*  pay us for it. So it starts there. And then the other part is when you know, and I think this gets
*  skipped by businesses are kind of not thought about is the feedback loop for users, which is
*  one labeling anything that's AI generated. And then two is providing that feedback loop for users
*  to say, Hey, this recommendation was good or bad, or this summary was good and bad, or the identification
*  of this, this action item was good or bad, whatever it might be. And those are things that I think are
*  intrinsically really important for this and having that feedback loop to get back to the teams.
*  We're fortunately always also on a bi weekly really schedule meeting every two weeks. So when
*  we talk about tuning our models and making adjustments, we are constantly looking at that
*  data, going back, redeploying models. And again, there's that constant feedback loop to go and make
*  sure that there's both utility and function in it. And I think that has to be obviously, you know,
*  as I said, if I was to reframe my answer, like, hey, assume that you're doing the right things,
*  I'm like building an accurate model that provides utility, then we're focused on like these parts
*  around latency, you know, capacity and cost. Hey, we'll continue our interview in a moment after
*  a word from our sponsors. If you're a startup founder or executive running a growing business,
*  you know that as you scale your systems break down and the cracks start to show.
*  If this resonates with you, there are three numbers you need to know. 36,025 and one 36,000.
*  That's the number of businesses which have upgraded to NetSuite by Oracle. NetSuite is the number one
*  cloud financial system, streamline accounting, financial management, inventory, HR, and more.
*  25, NetSuite turns 25 this year. That's 25 years of helping businesses do more with less,
*  close their books in days, not weeks, and drive down costs. One, because your business is one of
*  a kind, so you get a customized solution for all your KPIs in one efficient system with one source
*  of truth. Manage risk, get reliable forecasts and improve margins, everything you need all in one
*  place. Right now, download NetSuite's popular KPI checklist designed to give you consistently
*  excellent performance, absolutely free, and netsuite.com slash cognitive. That's netsuite.com
*  slash cognitive to get your own KPI checklist. Netsuite.com slash cognitive. Omniki uses
*  generative AI to enable you to launch hundreds of thousands of ad iterations that actually work
*  customized across all platforms with a click of a button. I believe in Omniki so much that I invested
*  in it, and I recommend you use it too. Use CogRev to get a 10% discount.
*  Yeah, it's definitely more art than science still at this point. I think we're in this moment where,
*  again, the dynamics are just changing so quickly. I've noticed in my own fine tuning work,
*  which I've mostly done on the OpenAI platform, and the reasons for that are interestingly also
*  starting to change. It used to be because I couldn't match the performance anywhere else,
*  and it was simple as that. Now, I would say it's pretty reasonable to expect that I could match a
*  3.5 fine tuned for my use case, which this is at Waymark. We do essentially video script writing
*  and related tasks. I think I could probably match the 3.5 fine tuning with not a huge amount of
*  effort on top of a mixed roll or whatever the case may be. But now, the better reason
*  for me to stay with the OpenAI is that pricing actually works out more favorably for us,
*  and the hosting is just much simpler. The managed hosting relative to having to work with other
*  platforms to provision dedicated instances and so on. Some of those really don't have much in the
*  way of auto scaling yet at all. Now, it's on that other dimension that they're ahead.
*  David K
*  different demands. You can imagine a meeting. Well, guess when meetings pop up? Top of the
*  outer, top of the hour, bottom of the hour. Those are the two spikes. Even just having auto scaling
*  on a communications platform, for all of these things that you know, most people are not starting
*  their meeting at 11, 17 on those pieces. But these are all, as I said, it's important to have this
*  stack and to have these controls and capabilities. You know, we're, as I said, many of us are
*  former Googlers. And so we're obviously at Google Clouds. And these are all of the things that come
*  into play with auto scaling and doing that scale for sure. Cool. Okay. So let's go back to kind of
*  product and, you know, practical user experiences a little bit. You want to just run down the kind of
*  most common, maybe most loved AI features and experiences that you are powering today. And,
*  you know, maybe we can kind of start to get into some that are emerging as well.
*  Yeah. Most loved, obviously real time transcription. We do a summary on top of those conversations,
*  which I think the world is suddenly becoming enamored with, you know, instantly summarized
*  blocks of text. But we just see cool, really cool things with summarized text. And so you imagine
*  a support and sales conversation, we can go label the purpose and the outcome of those conversations.
*  Suddenly you can take unstructured data, made it structured. Previously, people will go and have to
*  literally people in their contact center, they'll review calls, tag this stuff. The agent assist
*  features, as I said, which is like, hey, my first job was in a contact center. And I was terrified
*  of the first conversation I was going to get because I was like, what is this person going to
*  ask me? And so again, being able to guide people and pull information and present it to them in
*  the moment that they need it. And then the last one I would highlight are things that are, I think,
*  the perfect application of AI, which is we can infer customer satisfaction conversations.
*  And you think of what happens for, you know, in the support world is you and I have this
*  conversation, you know, at the end of it, you send me a survey, you're like, Hey, Dan, what was your
*  experience? And I'll tell you, I'm like, Nathan, either it was really good or really bad. Like,
*  those are the only, you know, the two people you kind of hear from. And so for us, it was like,
*  hey, look, we can go in for customer satisfaction with really high accuracy. We can do it across
*  every conversation. There's no change in behavior and there's no new software that needs to happen.
*  And you get, you know, 100 X volume of the data that you're getting. So it's much more representative.
*  And so these are just a few of the things, as I said, that we're working on, but we're really
*  focused on how do we go capture these conversations? And then as I said, at the beginning of our chat,
*  really focused on delivering features that are focused on assistance, automation, and then
*  telling you things that are happening to help you make better business decisions.
*  Of the stuff that the AI does today, how much of it would you say in the absence of AI gets
*  done by a human versus simply doesn't get done at all? Like, presumably, if there was no AI
*  transcription, very few of these calls would be transcribed, right? And, but maybe many would be
*  summarized. How do you kind of think about how much is this doing work that otherwise wouldn't
*  have happened versus taking work off of humans' plates? Yeah, I think about it in two ways. One
*  is what happens is you get into the crazy world of quality assurance. And they say crazy world
*  and that you see me smiling and laughing and like the nicest way possible. But it is what happened
*  before even transcriptions was people are listening to sitting down. If you're in a contact
*  center sitting next to Nathan listening to the call and then making sure that you're following
*  the process and you're handling things in a friendly manner. So one is like the stuff's
*  even happening. It's either happening today and there's not even a record of it. Or two,
*  it's happening and it's really, really, really time intensive. Meaning somebody's probably not
*  even providing the transcript or taking the notes, but they're saying, Hey, here's the scorecard in
*  the rubric and I'm giving Nathan a grade to say whether he's doing a good or bad job. Or you get
*  into the legal world, right? Or somebody may want a record of a conversation, whatever it might be,
*  or a doctor's office. Somebody's probably sitting there maybe taking notes or the
*  doctor's taking notes. So I think honestly, our application of the things that we're focused on
*  are these mundane tasks that I think are really ripe for AI to actually do it. Transcription,
*  accuracy is near human levels. As I said, it's kind of everyone's being a lot of businesses are in
*  the same route of kind of 90, 90% less accuracy. And then you get into this land of, Hey, we've
*  got, we can go summarize that information and structure it in really fantastic ways. And I think
*  there are immense opportunities to either go and completely automate tasks or augment the tasks in
*  really fantastic ways to free up people. Just as an aside on the transcription, are you still using
*  the original stack that you created some years ago there? That's all been whisperified at this point?
*  That is, but yeah, so we do. So all of that still we do in-house for re and, you know,
*  I'll turn a little context on that. We're on Nvidia Nemo toolkit is our latest models.
*  And again, when you talk about telephony, there's different codecs. And so everything is fine tuned
*  for the codecs that we go on leveraging use. And so really high career transcription accuracy. And
*  when you're talking about, you know, driving automation assistance and insights, you keep
*  here every say those three things and grain editing people, transcription accuracy becomes
*  the foundation of all of that. And, you know, you've probably, you know, I've had, I've listened to
*  some of the other podcasts and people will talk about kind of garbage and garbage out on data, but
*  there's always that argument that comes up from investors or analysts around look like
*  isn't speech recognition in there or are, are, so isn't that just a commoditized,
*  technology? And I'm like, I don't think so. I think we're a long way from solving that problem.
*  When you get into accents and words that don't show up in the dictionary and proximity to
*  microphone, all sorts of, all sorts of complex challenges around it. But that to me is the
*  foundation for all of this, that if you can't accurately transcribe information, then everything
*  else goes out the window. And again, that's why we recognize that and think it's important to go and
*  have an in-house speech recognition team and build those models and fine tune those models again for
*  our network of telephony. Yeah, interesting. The codec aspect to that is, it's always a lot of
*  little nuances. And once you really get into the weeds on these things, yeah, people will come to
*  you and say, Hey, that, you know, they'll see a bunch, you know, much like anything in benchmarking
*  is always have caveats and nuance too. And I always encourage people to, to, to understand that,
*  which is you may see a benchmarking report of a business that does speech recognition and says,
*  you know, they have the highest accuracy and it all comes down to, well, what training set was that
*  and is what network was that on? There's all these things that matter around the codecs. And so for
*  us, as I said, is we have the best accuracy on our codecs and telephony network. So there's nuance.
*  And that's not us saying, you know, we're not a provider of speech recognition for somebody as an
*  API. So somebody can't go take our models and plug them in on the T-Mobile or Verizon network
*  or AT, you know, whatever it might be. And that matters. And I think it's important for people to
*  understand the context of these decisions in the context of these benchmarks. Yeah, interesting.
*  How much do you personalize? I guess you could, you could customize to the level of the customer,
*  or you could personalize down to the level of like the customer's customer. And I wonder how much
*  of those two levels of, and I guess you could even do it in multiple ways, right? This could be,
*  you know, context management at the prompt level of, you know, here's a profile of this business
*  or a profile of the customer. You could go into a rag setup. You can go into fine tuning.
*  How do you think about, you know, I guess I'm just thinking these tips, right? Like
*  tip pops up. Obviously, that's got to be specific. It's certainly got to be specific to the business,
*  right? It can't just be like general, you know, try to smile more. Maybe it even needs to be
*  often specific to the individual and customer too. So yeah, personalization. Tell us everything.
*  We start with custom models for every customer. And so that is the ability for them to go and
*  fine tune the speech recognition model that they would have. And I always go back to, look,
*  there's going to be us in startup and SAS land. We tend to come up with acronyms that are new.
*  We come up with funky spellings of product names to be unique. So those tend to be the
*  most important things to a business, right? Or the uniqueness of those products or those acronyms.
*  And so again, it comes back to you need to accurately transcribe them. Where we want to get to,
*  we would like to get down to, hey, Nathan, if we're providing, if your business is a customer of
*  Dialpad, we would like to provide Nathan his own model for himself. And I always go back to,
*  you think of somebody that has a name like Sarah, and there's multiple ways to go and
*  spell that. You want to piss somebody off really well as show them a transcription or a
*  summarization and summarize their name wrong every single time you see it. And so those are things
*  that we're working on. We don't have that problem solved today. But again, these are all the
*  challenges that start to pop up at scale. And you bring up two interesting points is, well,
*  if you're a customer, can we then go and build another model for the customers that we're
*  leveraging your platform for? Or can I start to have a unique model for the individual employees
*  that might be leveraging the piece of software? So those are all still opportunities for us that
*  we haven't solved. I don't think anyone has solved it at those levels. But when we think about,
*  where do we want to get to? And what are the annoyances that show up in this stuff? Those
*  are the very real annoyances that show up. Just thinking about transcribing somebody's name.
*  Yeah. If you're doing this at home, one very practical tip that I have, which I don't think
*  would work at your scale, but works for me when I'm just processing podcast transcripts, for example,
*  is to take a raw transcript and then run it through a language model to clean it.
*  And at the top, I'll just be like, here are all the proper nouns that you need to know
*  to clean this up so that you get the company names right and all that sort of thing. Again,
*  that works at low scale. I don't mind dropping, it could be like a dollar on Claude or whatever
*  to do that. Not going to work for you at the scale of all your customers, many, many calls.
*  But how much data do they need to do this sort of customization? Is there a rule of thumb of you
*  need X hours of speech? And I assume that they need ground truth as well of the correct transcript
*  of those inputs? Yeah. The hours I need, I don't have the number of hours. I'll ping my co-founder
*  and I'll get you the hours. But there is a limit to say, look, and this always comes up for customers
*  to put it in relevant aspects of people. We have customers all around the world. And so somebody
*  will say, hey, we want to go have transcription in a language we don't have today. And so then we need
*  to go and find the audio from that and make sure that there's enough to go and do it. And to your
*  point on the ground truth, this all stemmed from our first startup was when we were building TalkIQ,
*  we had to go build our own telephony platform. We had to go build our own speech recognition.
*  We had to go build our own NLP and we had to go build the tools at that time to even do it,
*  which was how do we go capture the audio, literally start to create kind of 15 second clips of the
*  audio and then build these tools that our labelers could go through to say, okay, you need to start
*  by accurately listening to this 15 second clip. I need the ground truth, which is go and transcribe
*  it. Somebody has to make sure then that is accurate because it's a tedious task at scale.
*  And then we have to go, as I said, is take those and then go and build the models and improve the
*  models from it. So these are all of the very real challenges that, as I said, because we have this
*  past experience, fortunately kind of went through or faced with those problems kind of back then.
*  And as I said, much of that has been solved today and different startups have showed up to go and
*  even build tools to do it. Yeah. I'm struck as I'm listening to that description that it seems like
*  it's probably gotten an order of magnitude more efficient even just to set that up, right? Because
*  now there's the Facebook model, for example, that supports like a thousand languages or something.
*  So it may not be up to your standard on language 900, but it probably saves 90% of the time of,
*  you know, having to go hire somebody on Upwork to get started.
*  It does. And we do any, and you do kind of hacks around it, right? Which is so, you know,
*  you showed up today and you may say, Hey, maybe you want to have Dutch. And we would say,
*  Oh, we don't have Dutch today. So what we could go and do is we could go plug in,
*  you know, Google file speech. We do a plugin, let's let's speech Maddox, you know, deep gram,
*  whisper, you name it. And you assume if like, again, goes back to like where we started the
*  conversation, he made sure like, who's going to get you the best accuracy on the codec that you
*  know. So we would go and do that. And then that becomes training data for us, right? So suddenly
*  as people just use the platform and they opt in the data, then that helps us over time, go and say,
*  we can then go and do this ourselves and reduce costs and improve accuracy faster than a third
*  party. So those are all like the very real things that we go through. And there are times we would
*  take that approach. And there are times that we would potentially plug in a third party and
*  just let it be. And that usually stems from, you know, thinking about the opportunities from the
*  business, which is like, Hey, this language might not be in high demand. So we never, you know,
*  we're okay with the pass through costs of just using a third party for it first site. Hey, this
*  is the, you know, there are very real opportunities for us at scale to go and do this.
*  How about on the content generation side in my limited free trial, you know, I didn't have enough
*  content in the platform to kind of really see how that can work. But obviously, this is another
*  thing that has to be customized, you know, to really be useful. And I've done some experiments
*  trying to get AI to write as me haven't quite got out of the uncanny valley yet. I'm sorry to say.
*  How are you guys doing in terms of generating content? How do you think about measuring how
*  well you're doing? And, you know, that I'll then I'll project into the future, I guess, from there.
*  Yeah, we're we're early on that. So as I said, like, kind of when we think about like content
*  generation, as a communications platform, we think the easiest thing is like reply, you know,
*  generating a reply, do you, you and I have a conversation. And one thing that we've kind of
*  noodled on is, hey, can I go send me in the summary? And if I send you the summary,
*  then I want to have an email that accompanies it. And can we go auto draft the email based on,
*  again, the context of the conversation we just had? I tend to have like similar opinions to you
*  of this, this valley that you're in, or I'm like, I think there's some utility there,
*  but is it more trouble than it's worth? I use chat GBT for go write me first drafts of blog posts,
*  you know, as a starting point for things. So I do think there's utility and some some opportunities
*  there. When we get into content generation, we're still early in exploring that. But I also kind of
*  have this uncanny thing of like, I don't know, for things like email responses, you know, for example,
*  is that, is it really worth the time? I mean, is it really going to provide a ton of value for
*  people? Are they going to end up just customizing it themselves and writing it? You know, as you
*  start to engage with a large language while you suddenly realize that you spent as much time
*  as you would just rafting, just drafting a two sentence, you don't send me that
*  ultimately comes out just how good the generations are there, right? Like it's,
*  this is a, this seems like a very dynamic situation. Like I have not got it to work on,
*  I guess I haven't really tried it with GPT 3.5 as much as I probably could have. I've been kind of
*  holding off to try fine tuning GPT 4 on my own writing to see how close I can get it.
*  Presumably, if you could fine tune GPT 4 on a decent body of business correspondence for a
*  business, you would probably, you know, you may not be writing love letters to partners or, you know,
*  taking over corporate strategy, but presumably you could like, get pretty high acceptance rates on
*  like routine communication, I would think, right?
*  I think you're probably right. I don't, you see my hesitancy. I don't know if I'm like bought into
*  that, like meeting like the general utility, like I think there's a ways to, I think there,
*  we're still a ways off from this stuff. And I, and I generally think, and I, and I say this,
*  meaning I think there are, there are very real opportunities for large language models. And I
*  think what will still play out this, this next year is I still think we have a ways to go.
*  And I think they're going to do some really, some things really broadly, really well.
*  And we're still going to need the next level of development to start doing things that are really
*  going to seamlessly work and be like the next wow factor shows up. And I just think like,
*  this is one of those examples where I'm like, I do a lot of, as I said, like content generation
*  today. And I'm always like, it's a great first draft. It's a great starting point.
*  And I think about putting those features in our, in our app and potentially charging for them. And
*  I'm like, I don't know if that's, that's the, the, like the wow factor feature that we should go in.
*  I think that it's like a quality of life feature to say like, Hey, end of call,
*  we can go generate this amazing recap and structure it. And I'm like, do I need to have
*  the auto generated email to go along with it? Like it's a couple of sentences and is it really
*  going to do it that well? And is that where we should be spending, you know, our product
*  and engineering time? And there are different competitors in the space. Like teams is very
*  much focused on that with copilot. You know, zoom does that a little bit with like AI companion.
*  And I'm just like, I don't know if I'm, I don't know if I'm personally convinced on that use case
*  yet. And especially when that you might potentially charge, I just think there's some extra development
*  that needs to happen. And to your point, that might be like, Hey, there's a bunch of fine tuning that
*  you individually need to then go and do. And then you think about, well, how do you do that at scale
*  for a user? And once that that user doesn't know, these are just the things that pop up.
*  Sounds great. You're like, okay, so then you want every user to hop into your app and suddenly be
*  fine tuning to customize the emails. Well, actually, that's one of the big reasons I
*  thought this conversation was so interesting is because in looking at dial pad, I've been kind of
*  thinking this feels kind of like the gym that is both capturing the data of what people do
*  incompletely. And maybe there's a little caveat we can discuss there, but definitely capturing
*  a lot of what people do, especially in these sales and marketing roles that are the most kind
*  of intensive users. And then also, the dial pad environment seems like a very natural place
*  in which to deploy and evaluate and ultimately refine an AI agent. Because you've kind of got
*  the scope, the possibility of like, what are the actions are like, much more clearly defined
*  than if you're just like, oh, go use a computer or go use the web at large.
*  There's a bunch of different questions here. But if it's not there yet, or if the next generation of
*  model quality is not going to take us to even, I mean, you're saying like, maybe not even on
*  email drafting. But I'm thinking even a little farther than that, like,
*  virtual AI employees that may start limited, but can hopefully get in there and actually advance
*  your work for you. What do you think is missing that would stand in the way of that happening in
*  2024? Well, I think I'll get to take like a small little tangent and tie things back like
*  the content generation piece to me, like the part that that excites me and I think is the higher
*  utility on that is like understanding like the recommended next best step or automated workflow
*  that somebody should take. And what I mean by that is because you tied into Hey, we can go
*  understand these conversations. And we're tied into a CRM and a database. So we know the outcome,
*  which is if I'm using specific language in a conversation, that language leads to a more
*  positive outcome for the business, then the next time we see that conversation happening for a
*  different person, we should highlight to them, hey, here's the right course of action that
*  obviously takes it. So when I think of the content generation, it's more around generating content
*  around, here's the next best action, as opposed to me thinking about content generation of like,
*  you know, here's the email, here's the email, right to go and write.
*  Okay, well, let me keep pushing you to think a little farther into the future. I feel like
*  if I imagine AI realizing its potential, a lot of sales and customer service ultimately ends up
*  getting mediated by AI. And it's not that I'm like racing to replace people or, you know, cut
*  costs or whatever. But I always kind of come back to sort of in, you know, a Bezos style, like,
*  what does the customer really want, right? And the customer wants like immediate response 24 seven,
*  like where I can pause the conversation where I want to at my convenience, and be able to come
*  back and pick it up, you know, right where I left off, and maybe even switch modalities.
*  And, you know, chat GPT offers me all these things today. And it's like, you know, I had a
*  conversation while driving this weekend about the new state space model moment that's happening.
*  And I would say chat GPT was, you know, maybe not the best conversation partner in my life,
*  you know, possibly for that conversation, but certainly among them. And, you know, for many
*  people who, you know, aren't as connected as maybe I am, like, probably is the best conversation
*  partner that they could have. So do you think that I'm like wrong about that? Or, you know,
*  going back to the, you know, the stats at the beginning, you have like, third, third, third,
*  these small and medium sized businesses, enterprises maybe, maybe don't have to go this
*  way. But like a small business just can't staff the phones 24 seven, right? And can't like,
*  pick up all the calls that are you try calling the local restaurant around here at a lunch rush.
*  And it's like, they don't want to even answer. I just, you just have to walk in and wait in line.
*  Seems like there is like a qualitative change that can happen here. And, you know, obviously,
*  it comes with a lot of potential disruption. I don't know, it seems like you're not you're
*  not buying that vision. I'm not sure if it's because you think that technology is not gonna
*  pan out, or you just don't want to go there. Automating support, like doing digital deflection,
*  I think, like, like, first generation chat bots have been like really good password reset bots.
*  Obviously, you can go put a large language model on your chat bot, and it's going to be able to
*  handle much more complex requests and sound much more natural, fully believe in that for support.
*  And I would say, you know, you can go look at it. You know, today, probably 80% of people probably
*  start engaging with a brand for support on a digital channel. So the very first thing they
*  want to do is they want to go out this next generation experience with a large language model,
*  go get better answers, more natural, same answers as quickly as possible. For sure,
*  we're working on that we believe I believe wholeheartedly in that opportunity.
*  This automated sales one, I don't I don't I'm when I say that meaning like outbound sales and
*  creating an outlet because there's some startups working on this one. I don't know about that. And
*  we had our couple of us had dinner with Mark and Drayson the other week and Mark had mentioned that
*  he has this idea at times that might be two bots that chat with each other. It's like the sales
*  bond and the you know, each of us have Nathan has his own automated bottom him and understands
*  and I have my own that selling. I don't know if I agree with that. Like, I personally think people
*  like to buy from people. I also think when you think of like a support use case that yeah, I want
*  to engage with a digital bot. But the second I need to escalate that to a phone, I don't know
*  if I want to talk to an automated voice bot as bad as good as that bot might be. I think there is when
*  you're really frustrated about something talking to a human and then you get into all sorts of
*  things like do you let somebody know whether that's a voice bot if it's so good and you've
*  got speech synthesis and everything and I don't know and I do think that it's going to take time,
*  as I said, when I go back to the time thing, like, I don't think that stuff shows up in 2024.
*  And you know, I've seen some really impressive demos and at the end of the day, you're like,
*  you can still tell. And so that's why I said I don't think in the next year, you suddenly have
*  an experience where we're like, you can't tell. Maybe on a digital channel for sure,
*  but not on a voice channel. And I'm happy as I said, I'm at somebody's got a really cool
*  demo out there. So like, I would love to see it and play around and like, for sure. But those are
*  some things that we do like we spend some time thinking about as a communication platform of
*  like, hey, this is automated sales agent show up and does somebody want that? But I very much view
*  it as like, hey, the next generation chop out on a digital channel for sure. Instant answers,
*  better answers, faster answers. All of that stuff is like an immediate big opportunity for us.
*  So what is your kind of 2025 and beyond expectation? Like, mine is pretty much that
*  all this stuff does happen. I'm not as sure if we get like, AI automated science, although even that
*  is looking like increasingly likely, but definitely sort of AI mediated sales and support seems quite
*  likely to me. Yes, I would agree, like they are still kind of uncanny valley, even the chat GPT
*  voices, you know, they don't handle interruptions very well, they don't handle my long pauses very
*  well. And so they start talking when I'm still trying to talk, I was looking back at the
*  transcript with chat GPT and I'm like, stop interrupting me. I've known for my long pauses,
*  for God's sake. So, you know, they're not quite there. I would definitely agree with that.
*  I'm also a big supporter of the notion that I don't think we should have AI's deceiving people. So I
*  don't even think we, even if it does sound fully human and could pass, I think we should probably,
*  you know, either as responsible corporate, you know, actors or as a government sort of say,
*  you know, we're going to just be clear when you're talking to AI, that seems healthy.
*  But I don't know, you know, if it's good enough, I don't really think people will mind and it does
*  feel like the ability to respond immediately. And again, you know, drop the, you know,
*  put the phone down for 10 hours and then come back and pick it up later after my kids go to bed when
*  it's convenient for me like, and seamlessly do that, you know, that seems so helpful, not to
*  mention, you know, the ability to pass the cost on to the customer, like, I guess you could think
*  that, you know, even, you know, 20 pick your year, like, and I'm not saying like, I care exactly
*  what your specific year is, but do you think it's so far off that it's just like, not really
*  something that we need to be concerned with right now? Because if it's, you know, if it's not 2024,
*  but it is 2025, like, it's still very close. The reason I have to express that hesitancy,
*  and I think honestly, like, we don't know if there's going to be, you know, much more smarter
*  and greater people that will tell me it's faster and I'm wrong. My experience with technology has
*  been similar to that trough of disillusionment. And I think, you know, I look at self-driving
*  cars as a great example of this. We're now a decade into this journey. If you asked me a decade ago,
*  based on whatever people have said, we would have figured this was a solved problem. And I think
*  these things turn out when you really get into like the complexity of human language and the
*  workflow, especially work and some of the complex workflows that we have every day,
*  those turn out to be much more complex, harder problems in the real world. And that doesn't mean
*  that you can't be really enamored and amazed by a demo or that there's not all of these little
*  things that we do every day mundane tasks that are ripe for audit complete automation or experiences.
*  But as an aggregate, I think it just is going to take more time. And I don't have a guess on time,
*  if somebody said that the only thing I feel is when I think about a year and I'm like, look,
*  I've been blown away by a large language models and chat, TBT, and even just technology and drama
*  over the past decade. I just have this inkling and this hesitancy that it's going to take more time.
*  And I hope I'm wrong. Because as I said, as somebody that grew up in Silicon Valley and a
*  technologist is somebody that just loves innovation, I hope I'm wrong. But I have this
*  sinking feeling, unfortunately, that it's going to be harder and more complex than we think.
*  That's really interesting, because I also kind of hope I'm wrong. But in the other direction,
*  I feel like I see this coming at us so fast. What have you seen that you're like, this is it?
*  Well, just broadly extrapolating the last two years, just going back to literally two years
*  ago today, and we're recording on December 19, 2023. So December 2021, there still wasn't an
*  instruction following model in the public. The state of the art for me at Weymark was fine tuning
*  GPT-3. And I think we had just gotten, we had moved from Curie scale to DaVinci scale. And that
*  was enough to create our first scriptwriter that was like, okay, this will definitely be useful to
*  our customers. Our use case is quite narrow compared to certainly the DialPay use case,
*  and certainly the broader agent challenge globally. But we have gone from couldn't get
*  actual utility from it in late 2021 to it is a totally qualitatively different experience
*  two years later. And that includes the script writing having gotten very good, the
*  image understanding having also progressed by leaps and bounds such that we're now
*  able to choose the appropriate image out of a user's image library with pretty high consistency.
*  The text to speech has also gotten dramatically better. Again, it was not even two years ago,
*  but probably one year ago that we went from, you know, hey, this just doesn't sound good.
*  We partnered with media companies. So, and we do also sell direct to small business,
*  but our kind of standard is, would a media company that like owns TV stations or owns a cable network,
*  would they put this on their air? And, you know, feel like that is the kind of thing that isn't
*  make people turn their TVs off, right? So, and it wasn't, you know, a year ago, it wasn't.
*  And now most of the stuff that we put on the air is AI voice. And it's not perfect. But, you know,
*  all of these things have kind of gone from 20, 30% of human to like 80, 90% of human in just this
*  less than two year timeframe. And I don't think we're done. You know, we're I look at our model,
*  and I'm like, I see actually a lot of low hanging fruit still where some of the techniques that
*  we've developed for past generations were are now like hurting us. You know, we've, we've, we've,
*  you know, tried to fit so much into so few tokens and whatever in the past. Now it's like, you know,
*  what we should really do is go back and look at that again, because like the tokens are a lot
*  cheaper. The models can add a lot more of them. To me, it's like, it's sad. It's always like that
*  last mile and the complexity of that last mile. And she said, like, I totally and I go back to
*  like the bad analogy of like the self driving cars, because I live in San Francisco, we,
*  you know, Waymo cruising around all the time, you know, and doing a good job. But that's not
*  without issue. And so I think it always comes back to like, I agree with you. And it's that last mile,
*  the piece of like, hey, we're 80 70% of the way there. What does it really take to have like just
*  that amazing, beautiful experience that, that, you know, we're not going to know, you know,
*  I hate to say like, not I'm not getting into like the AGI space, but just that's the piece that I
*  just I wonder, you know, I truly wonder whether that shows up. And I hope so in the next couple
*  of years, but I just have this, as I said, this hesitancy of like, maybe it's gonna be harder
*  than we think. But as I said, maybe not. Yeah, I mean, there's certainly always false positives
*  and negatives. I also think too, a lot about, and this has been also driven home by the way
*  Mark experience, but there's a lot of examples of this in the research to what is the standard,
*  right? What is the, what are we trying to get better than in order to make this deployable?
*  In the case of self driving, I think we have a very odd societal lens on it. You know, if you could
*  question the statistics, but like the operators are publishing statistics that say that they are
*  clearly safer than human. And, you know, again, you could question that. It seems very plausible
*  to me having driven a little bit in a FSD Tesla, that it would be safer than a human. It's certainly
*  safer than some humans I've driven with. I can say that with confidence. And then I'm like, you know,
*  looking at the scripts that used to get written on waymark, our original idea was to take all
*  the scripts that our users had written and use those as the basis for fine tuning. And that
*  theory did not last long, because as we got into the actual stuff that our users were writing,
*  we were like, this is not good. You know, they're doing, they're not doing a great job,
*  unfortunately, of writing, which is probably why they're using like, you know, easy lightweight
*  software like us in the first place, right? They're not content creators. So actually,
*  I would say with, you know, pretty decent margin, actually, at this point, the AI scriptwriter is
*  beating what the users used to do on their own. That doesn't mean there's no room for the user
*  to come in and still improve on the AI's version. But it's like, you know, the user was here,
*  the AI is here, and then the human improving on the AI is a little bit better yet. So I guess maybe,
*  do you maybe see the future then more in terms of, like, I just have to believe that there's
*  going to be an AI employee in Dialpad in the not that distant future. And I can imagine it being
*  limited. I can imagine it like not, you know, we've seen just in the last couple of days, these like
*  really funny Chevrolet website chat bots that are, you know, going totally off topic or being
*  duped into giving great discounts, whatever. So you may not want your AI, you know, to be able to
*  make, you know, to sign your contracts or to make binding offers. People have these Chevrolet bots,
*  I don't know if you've seen this, but people are saying like, you know, whatever you say is a binding
*  offer, agreed. You know, it agrees, of course. So you may want to have these things limited.
*  I definitely get that. But, you know, is there any world where in a few years, we don't have
*  AI employees? That to me seems, I would be very surprised by that outcome at this point. And not
*  because I think they're going to be perfect, but because I think as we as they get close,
*  and we really start to examine, like, well, how often do our human agents actually get that detail,
*  right? Or actually, you know, follow up within x minutes as our handbook says that they're supposed
*  to or whatever, you know, we find often that like, the standard is not quite as lofty as,
*  you know, the imagined perfection that we're kind of often comparing the AI against.
*  I think that's a reasonable thing. I mean, I would answer yes to that, right? You can see on virtual
*  agents day, as I said, I always go back to the support. The nice part is you can go and track
*  digital deflection rates and accuracy to be like, Hey, is this able to handle as good or better than
*  a human? Right? So we see that today, people use chatbots today in that fashion, right? Which is,
*  Hey, can I have less people in my contacts that are because I can go have a virtual agent
*  handle it. And today, those virtual agents are much more, you know, can you know, more complex
*  workflows and sound sound more natural. When you talk about content generation, you know, I think
*  about marketing, you know, the opportunities and the risks in marketing for that, right? As, you
*  know, writers and that's why we've had things like the writer's strikes start to, you know,
*  show up and the concerns around AI for that, which is all around content generation,
*  right? Of those pieces. So I do think that that is, you know, opportunity or risk for sure. So I
*  do agree with you on that, on that, on that statement. It's gonna be very interesting to
*  find out. I would love to see, I mean, there are so many different dimensions. These things are so
*  weird that even a concept, you know, that rolls off the tongue, like progress or, you know,
*  improvements or capabilities has a lot of different dimensions to it. I would love to see
*  the reliability get stronger. And I think it sounds like, you know, that's a big focus for you too.
*  I am worried that the sort of raw power will get, will continue to get stronger and that the kind of
*  robustness is going to have a hard time keeping up. And that seems to me to be a recipe for sort
*  of just a generally volatile, unpredictable situation. But to the degree that work can get
*  done to make things more consistent without, you know, turning them into Einstein's, you know,
*  in the immediate future, then I think that is like a really, that's like what the economy needs,
*  right? The economy doesn't need something actually all that much smarter than GPT-4 for most roles.
*  It just needs it to be like faster, maybe a little cheaper and more reliable. But yeah,
*  I think it's for whatever reason, progress on those dimensions is proving a little bit harder
*  to come by. Can you clarify when you say reliable? Can you clarify what do you mean? Yeah, I mean,
*  there's again, even that has kind of different dimensions to it. But I've been thinking a lot
*  about this state space model moment recently. And, you know, I think that one of the key
*  limitations of the current transformer based language models is they're purely episodic.
*  The episodes are getting longer as the context windows get longer. But they have no mechanism
*  to carry anything forward from one episode to the next, right? So it's like, they always have total
*  amnesia. That kind of gap between, you know, they obviously have these, they have like massive
*  knowledge encoded in the weights, and then they have kind of a little context and kind of nothing
*  in between. But now we've like rag and stuff in between, but, you know, kind of hacky stuff in
*  between. Something, an integrated memory to me feels like maybe the way that we get to this higher
*  level of reliability. And again, I think there's a lot of ways to measure or kind of conceive of
*  reliability. But to some degree, it's like predictability, legibility, consistency,
*  being told once that you did the wrong thing, and then like actually listening to that and doing it
*  right again in the future. And those are the things that I think the transformers kind of
*  fall down on today, where they aren't, you know, and that prevents them from being like
*  reliable co workers. That makes sense. Any thoughts on memory? This is like a real kick of mine at the
*  moment. And I'm going to have an insanely long monologue episode coming out about it. But
*  do you, is that an area that you are, are thinking about as well?
*  Yeah, I mean, to your said, like the context window and being you think of like applications
*  for customers, right, which is it all stems from being able to personalize the content, right,
*  or that experience. And it all stems from yes, being able to pass information from, as I said,
*  you classify it as like multiple episodes, but multiple conversations in the past. And
*  today, the way that you handle that is you are pulling information from a system of record and
*  trying to provide that context to it. It doesn't have the full context is again, old records might
*  be partially intact, they might not even exist, nobody has them. And I think to me, that's again,
*  comes back to like our biggest opportunity of what I think really excites me about the platform of
*  really any communications platform is you can suddenly have a record for every conversation,
*  assuming you want to record, you know, I'll, I'll, I'll put that the preface out there of like,
*  assuming you want to have a record of it, great, if that if that is true, then suddenly you have
*  this really amazing opportunities that open up of saying, suddenly, I can go personalize the content
*  in the moment, suddenly, I have this understanding of the past seven conversations that we had.
*  And that really then opens up the opportunity for these virtual agents or virtual sales assistants,
*  you know, however you want to kind of frame it. So I think the lot figuring out this next step of
*  like the long term memory, that to me is like something that needs to happen again,
*  now I have this hesitancy of like, these are all the things we have to have happen.
*  Right. And you know, how quickly how quickly does that change? But, you know, GPT four and
*  the token limits, like those created big challenges just as they go back to like our, you know,
*  to take a step back, it's you take a long form transcript, like we would have to go break the
*  transcript up. And you're like, hey, go summarize this piece of the transcript. And then suddenly
*  you've taken, you know, a 30 minute conversation, you've got to split it up 16 times, and you're
*  taking 16 summaries, then asking for an aggregate summary, like these are all the challenges that
*  show up. And you're like, well, the better way to get a summary from that is if the token limit
*  and is increased, like I make one request for a summary, guess what, that summary that I get from
*  that is much more, it's got better context. And so these are all kind of, I think that the big
*  implications for these next experiences that we want to see. And I think for me,
*  as I said, like, why get excited about this is you see these experiences and they're kind of
*  still imprint, you know, to use your words that 70 80% of the way there, you can see what it's
*  going to look like when it's when it's here. Percent. Fascinating conversation. I especially
*  love getting into just kind of the somewhat divergent views of the or, you know, expectations,
*  not as a views, but expectations for the short term future. Anything else you want to cover
*  today that we haven't got to so far? No, I think we covered like we covered a lot of ground, as I
*  said, like, you know, reasons we kind of chose our path of like trying to do a lot in house and
*  was fun talking about, as they said, like the views, I was like, I got to bookmark this and
*  we'll come, you know, hopefully come back here or two later and see how this plays out. But,
*  you know, for me, as I said, I think there's just tremendous opportunities, especially in
*  sales and support and marketing. I think those are like three just right
*  areas for opportunity for AI to be leveraged, right? Whether it's around content generation,
*  you're just understanding conversations and powering assistance and automation within them.
*  Dan O'Connell, AI and Strategy at Dialpad. Thank you for being part of the Cognitive Revolution.
*  All right. Thanks, Nathan. It is both energizing and enlightening to hear why people listen and
*  learn what they value about the show. So please don't hesitate to reach out via email at
*  tcr at turpentine.co or you can DM me on the social media platform of your choice.
*  Omnike uses generative AI to enable you to launch hundreds of thousands of ad iterations that
*  actually work customized across all platforms with a click of a button. I believe in Omnike so much
*  that I invested in it and I recommend you use it too. Use Cogrev to get a 10% discount.

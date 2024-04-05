---
Date Generated: April 02, 2024
Transcription Model: whisper medium 20231117
Length: 8250s
Video Keywords: []
Video Views: 7466
Video Rating: None
---

# OpenAI Sora, Google Gemini, and Meta with Zvi Mowshowitz
**Cognitive Revolution "How AI Changes Everything":** [February 20, 2024](https://www.youtube.com/watch?v=ra3kpTVHjZs)
*  Someone walks into Sam Altman's office says Google just announced 1.5 Pro.
*  It has a million lay context window potentially that be 10 million. It's really exciting.
*  People are raving about it. It's now the time and Sam's like, yeah, now sure.
*  You can't have both ways. You can't both say there are so many chips coming online that we need to
*  build AGI soon. And AGI is coming along so fast and we'll have enough chips. We need to build
*  lots more chips and then go raise the money to make the chips. It would be surprising to me.
*  If a GPT-5 worthy of its name didn't make these agents kind of work.
*  Hello and welcome to the cognitive revolution where we interview visionary researchers,
*  entrepreneurs and builders working on the frontier of artificial intelligence.
*  Each week we'll explore their revolutionary ideas and together we'll build a picture of how
*  AI technology will transform work, life and society in the coming years. I'm Nathan LeBenz
*  joined by my cohost Eric Tornberg. Zvi Moshowitz, welcome back again to the
*  cognitive revolution. Always fun here. Let's do it. Let's do it. So I call you when I feel like
*  my own personal context window is overflowing and I can no longer find all the needles in the haystack
*  that I might need to, to make sense of what's going on. It sure seems like things are happening
*  faster and faster all the time. Well, that's what Gemini Pro 1.5 is for, right? You've got the big
*  new context window. You should be okay. Well, how is your personal context window holding up
*  first of all, and then we'll get into all the latest news. I think that my capabilities are
*  advancing fast enough that I've been able to keep pace, but it has been rough. So the discourse
*  speed has slowed down in the last few months. It feels like we had a lot of really big developments
*  and discussions around various potential government actions and also around the open AI situation
*  and 2024 has been more of a like, okay, everybody chill, everybody process what's happened.
*  And therefore we can focus on temporarily technologies and yeah, a lot is happening.
*  But also you start to see the patterns and you start to say, okay, this is a version of this
*  other thing that's happened. And it's not that it's slowing down in absolute terms, but you gain
*  the power and matching ability to process what's happening. Is that a natural process for you or
*  are you changing how you work at all your approach in any way? So I didn't have the natural
*  process in the sense of, I find myself telling you, let's try this again. Let's go over this again.
*  Or as we previously discussed, right? So like you see some of the columns where he's like, well,
*  as we have talked about before, and every word is a link to a different, you know, exposed,
*  it's the same basic idea of a lot of these concepts and questions and reactions are going
*  to repeat, right? Like different people are realizing different versions of the same thing
*  at different times. You know, the future is not even distributed. It's getting distributed. We
*  pick up on when people notice this, especially when like mainstream media, you know, standard
*  cultural people pick up on things that we knew six months ago, we knew a year ago, where we figured
*  out was coming at that time. And so a lot of them just, okay, yeah, we're gonna go for this again.
*  We have already covered that. Yeah, this is actually from October. And that happened to me
*  yesterday. Actually, I was writing stuff up and I realized, no, this is actually a few months old.
*  I probably already covered this. It's fine. I'm trying to figure out what I can do to be
*  more valuable. I think, you know, I've never really considered myself a content creator in,
*  you know, in any sort of normal content creation sense, starting a podcast was kind of a way to
*  make sure that I was consistently tackling a new topic. And, you know, hopefully sharing that with
*  people in in what I hope to be a somewhat useful way. It's gone better than I expected it would in
*  terms of people being interested in listening to it. And after a year, I'm kind of like,
*  how many of these should I be doing in kind of traditional interview format? How many should be
*  more like this, where it's like a little more of a survey type of thing? How many should be more of
*  like a deep dive where, you know, perhaps not even with a guest, I'm just kind of really going
*  hard at a particular topic. I did that late last year with the Mamba architecture and
*  really felt like that for me was a more profound learning experience and hopefully a better
*  product for the audience than a typical episode. So I don't have any immediate reactions to that,
*  but if not, we can maybe circle back and at the end, you can tell me what you want.
*  I do actually, I would say you should basically always strive, in my opinion, to do more deep
*  dives, like not just you, but like almost everybody, than you naturally want to do.
*  Like, I mean, I'm working on a newsletter, obviously, every week I am writing, you know,
*  an average of 10, 12,000 words or something, you know, including quotes about what has happened
*  specifically in this past week. But I find the most valuable things, especially if you're building
*  up a long-term base of operations, are when you get to focus more on specific places where you
*  feel you can break your insight, where you can be the go-to source. Yeah, that was my experience
*  with the Mamba piece. So I'm looking to figure out how to do a little bit more of that. So what are
*  your big pieces? And certainly a deep dive has been recently into your experience with Gemini.
*  This is obviously something that we did know to expect. And if anything, you know, seemed like it
*  probably came a little later than we might have penciled it in for. You had the good fortune of
*  having early access. I would love to hear how that happened and see if there's anything that I can
*  potentially copy from you going forward on that. But then obviously more important is what your
*  experience with it has been. And then, of course, now we've also got 1.5 to look forward to as well.
*  But let's start with 1.0, which you said, you know, among other headlines, had become your default
*  language model after a couple of weeks of playing with it. So when people reached out to me and said,
*  we'd love to get your feedback on this new version that we're going to ship soon, would you like to
*  check it out? And I think that, you know, I do is I established that, you know, I'm someone who could
*  be trusted if you share it with me. I'm not going to go splattering it all over the internet. And I
*  can provide useful insights that are different, that are well worth the time spent interacting.
*  And then obviously, if you share it with me, I'll be able to offer more detailed insights,
*  like right when it's released, which can impact how people see it. And they presumably thought
*  they had a good product. They wanted me to give my last minute. There was no attempt to put a finger
*  on the scale in any way, no attempt to convince me it was better than it was. It was all very,
*  very honest and straightforward and realistic. I thank them for that. It was really a good experience.
*  They seem to care about my feedback. This was someone who clearly wanted the information,
*  why to understand. So what I noticed right away was it was really good at many of the natural
*  things that I wanted it to do. So what a lot of people will do when they get their hands on a model
*  is try to get it to do something horrible. I'm guilty of that.
*  Well, you know, Sally has two apples and then, you know, John brings two oranges and they all
*  play a juggling act. And then they make salad. How many apples are left in a models like three?
*  No. What's the point? You know, in some sense, there's other people I figured whose jobs will be
*  to red team this model, either to get it to do harm or to find out where it's dumb or where
*  it's going to fail, right? On like theoretical tasks. And I took the opposite approach. I asked
*  myself, you know, what good can this do? And what happens when I feed it exactly the queries I just
*  want the answers to that I would normally want to do over the course of my day? We have some kind
*  of curiosity and I can do some amount of brainstorming and trying to set out drives
*  and parallels and so on. But what I thought was mostly the things I want are explaining things,
*  you know, finding excellent, you know, just general, like answering my questions. I'm confused.
*  I want to use search group, you know, maybe search for a document in some cases, although the version
*  I had back then didn't do that. That looked at other things, but I'm just very practical user
*  of LLMs. But I'm not trying to help them do my job. I'm trying to like extract the information
*  and understanding that I can go about my day and do the rest of my stuff. And for that, it was very,
*  very good. In particular, as I trip, I was trying to read the financial DPO paper that he never
*  got around to. And I was asking the question every paragraph or two. And it was very, very good. He's
*  right, not having to get the paper, but it seemed to have the information. And it was very, very
*  good at answering my questions on exactly the level of which I was asking, limit figuring out
*  exactly what information I need to know. There are a lot of other similar things. Well, I noticed it had
*  some flaws. Like I would try to use Google Maps and it would sometimes give me good information.
*  And sometimes it would repeat three different times for how long it would take to get the
*  SFO from Berkeley within the space of three questions in the same chat, despite having the
*  prior reference, which is better than just artificially agreeing with yourself. I was
*  admiring the fact that it wasn't doing that. The same plan wasn't driving me frustrating. I can't
*  carry on you for anything. This is weird. I claimed to know what the weather was and then it would
*  repeatedly not know what the weather was. I found some other bugs in the system that they're really
*  just, clearly this thing launched earlier than it was supposed to. It's also the 1.5 launching
*  two weeks after 1.0 advanced. This is not a natural thing for a well-planned out release schedule to do.
*  If you almost have 1.5 ready, you don't make your big announcement speech
*  right then. Unless, you know, this is me speculating, the CEO is on the phone with you
*  and saying, no, you're damn well going to launch right now. And he said, but we're almost ready
*  to 1.5. I said, I don't care. You're going to launch. I can't not launch now. And then this
*  happened to me, right, when I was doing a game company and we were just told you're launching
*  today. And we said, we're not ready. And they said, we're launching today. I said, it's Friday. Can
*  you at least wait till Monday, you idiots? They're like, no, you're launching today. And
*  we would not have succeeded if we lost on the following Monday, but at least it would have been
*  slightly less embarrassing to do. But it's clear that there was a, we need to launch this at
*  whatever state it's in. And we're seeing rapid improvements. And to the point where we're not
*  sure if 1.5 is better than 1.0 advanced. Discount and compute, it's got advantages and disadvantages,
*  which I haven't had the chance to properly explore yet. But yeah, I was just really impressed by
*  this is faster. This is smoother. This just does what I want it to do. My workflow is easier and
*  better. I want to use this. I don't want to go to GVT score. If I can help it. I do that when I feel
*  like I have to where that used to be like, this is where I go. And then sometimes I use cloth,
*  right? Sometimes I use complexity. So can you put a little finer point on what it is that makes it
*  better? I mean, I know that it's obviously tough because the surface area is so vast and there's
*  so many facets to language model performance for what it's worth. I have also been impressed. I
*  haven't spent as much time with it as you have today. I am going to Gemini advanced, AKA ultra
*  1.0 ultra and chat GPT with GPT four and Claude, basically for anything that I want help on.
*  I did this once with like a little kind of proto contract negotiation that I'm working on where
*  I had kind of a couple messages back and forth between me and the person I'm working with. And
*  kind of said, here's what this person seems to care about. Here's what I seem to care about.
*  Here's our messages to each other. Can you kind of help us get to a good win-win situation?
*  They certainly all behave a bit differently, but I found them all kind of useful. And the synthesis
*  of the three was for me kind of a way of making, telling myself I didn't need the
*  council because I had enough kind of AI council to make sure I wasn't leaving any major blind spots
*  for myself. And then also did this with a basically a job description where I have been working with
*  a friend on a hiring process. We've had a number of calls with different experts, got their opinions.
*  I've taken very wrong notes and just fed in kind of a paragraph at the top of like, okay, now it's
*  time to turn all these notes that I took over various calls into a job description. You write
*  it. And of course, they each did the task. In that case, I did find, I think it's fairly random. I
*  wouldn't say it was like a systematic finding by any means. I mean, I'm not sure how frequent this
*  would be, but I did find in that case that the Gemini response was the one that I wanted to go
*  with in terms of just taking something, editing to a final product that I would hand over and
*  feel proud of. Gemini did come the closest to what I was looking for. But those are spot checks.
*  Can you help us kind of get any more systematic or predictive in terms of what the advantages of
*  Gemini would be? Yeah. It's kind of the opposite of mixture of experts, right? It's a mixture of
*  non-experts where previously you would figure out, okay, I have these 20 different expert systems and
*  the program figures out which one to call if they want to compute. Now, just call everyone.
*  Computer's cheap. Compare all the answers. See which one is the best, which makes sense for a
*  human case. And yeah, I even have 1.5, right? I have access to 1.5, not in the standard interface,
*  but in the developer studio beta. So I can then not only compare quad, GBT, and Gemini, but also
*  the other Gemini. So now it's like I have the two Gemini's to work with and the name finally makes
*  sense. So I think what I found was the biggest feature was just it tells you the information
*  you actually want to know when you ask a question, much more reliably with less
*  worthless stuff scaffolding around it. And also I had gotten some good use out of the Google button.
*  So when you answer on a Gemini Advanced, one of the things you can do is you can press the Google
*  icon at the bottom and it will search for web sources for all of the things that you just had.
*  And it might have been green to indicate that you have a source that you can now click to.
*  And it's just very seamless. Actually, the guy I was doing the test with showed me this feature.
*  I didn't understand it was there until he told me. And then you can then ask for a
*  short what's to go now. Do you have any physics on this? Do you have any knowledge of this?
*  And you can find the backup. And that was very helpful in general. And I said, like,
*  it's also just very good understanding. Okay, if he asked this question, what does that mean he
*  doesn't understand? And what does that mean he does understand? And I find GPT-4 can be pretty
*  dense about this. And I probably could work with better custom instructions to try and improve
*  this than what I have. But, you know, so far, it's been kind of frustrating.
*  Claude, I found, is a step behind for most purposes. I use Claude mostly when I'm
*  looking at long documents. But I think your use case is a very different one because you are
*  asking for a creative job, right? Where like you get lots of different answers. There's no right
*  answers. There's no wrong answers. There's just different answers. Being able to take a
*  sample and then they choose the best one or combine the elements of different ones
*  helps you a lot. Whereas what I mostly try to do is I'm trying to ask questions where there is a
*  right answer. I'm trying to look for explanation. Or I'm trying to just get some brainstorming
*  at most to try to go with. And so I try Gemini first, and if Gemini gives me an answer that does
*  the job, I'm done. And the only way I get frustrated with that, like, okay, fine, I'll try all these
*  other people. I won't jump from one to four. I won't be jumping from one to two. I've just been
*  really happy in practice with Gemini advanced. It does what I wanted it to do, except when it
*  doesn't, right? But I've adapted to, okay, those are the things that I just don't do. I haven't
*  had much call to use GBT-4 specifically since then because it just doesn't come up very often.
*  Like there aren't these... The cases where GBT-4 is good potentially, where Gemini is bad,
*  or where you're trying to like customize it in these very specific ways, I think,
*  and those cases just don't come up for me very often. So it just doesn't see much use. And I'm
*  not going to cancel it because even the auction value is just so much more than like what
*  tickets they charge. Hey, we'll continue our interview in a moment after a word from our
*  sponsors. The Brave Search API brings affordable developer access to the Brave Search index,
*  an independent index of the web with over 20 billion web pages. So what makes the Brave Search
*  index stand out? One, it's entirely independent and built from scratch. That means no big tech
*  biases or extortionate prices. Two, it's built on real page visits from actual humans, collected
*  anonymously, of course, which filters out tons of junk data. And three, the index is refreshed with
*  tens of millions of pages daily, so it always has accurate up-to-date information. The Brave Search
*  API can be used to assemble a data set to train your AI models and help with retrieval augmentation
*  at the time of inference, all while remaining affordable with developer-first pricing.
*  Integrating the Brave Search API into your workflow translates to more ethical data
*  sourcing and more human-representative data sets. Try the Brave Search API for free for
*  up to 2000 queries per month at brave.com slash API.
*  Just to give a quick plug to Claude on my legal question, I did find it to be the best in the
*  sense that the commentary that it gave back to me was least sort of padded out and RLHF'd, if you
*  will. It was more kind of direct, to-the-point, conversational, and actually just kind of concrete
*  on the suggestions. It seemed like the others were a little more reluctant to... And I've actually
*  been pretty impressed with Claude on this front a couple different times, including one specifically
*  pertaining to you, but finishing this story first. They're just kind of plain-spoken, to-the-point,
*  direct, like not super hedgy. With both Gemini and GBT4 by comparison, I felt like
*  it was really reluctant to make a recommendation, to make a suggestion for what the agreement
*  might ought to be. It was very like, this is an important consideration. You guys will need to
*  figure out what the right thing is here. And as I pushed them, they would do a little bit more of,
*  okay, here's a specific proposal. But Claude was much more readily willing to just be like,
*  here's kind of what I would suggest. And it was pretty apt. And again, I did not copy and paste
*  this into my running dialogue directly, but it was the closest to... In that case, I actually
*  wrote my own thing and again, took my own thing back to each of the three models. So, okay, based
*  on your suggestions and my own thought, here's what I came up with and asked for one more critique,
*  and then basically sent it from there. But if I had been inclined to pick one from the three,
*  it would have been Claude because it was just the most kind of to-the-point, easy to understand,
*  not necessarily exactly what we're going to go with, but at least kind of willing to put
*  something out there. And the other one, as you may recall, that I've been kind of impressed with
*  on this from Claude was when we had in our last episode, you made an offhand comment around like,
*  I'd rather you go and do something terrible than open source next generation LLM. And a listener
*  said, hey, that's a little extremist, you shouldn't say that. So we edited it out. But then I also got
*  the idea in my head, well, maybe I should use a language model to review transcripts in the
*  future and see like, is there anything there that the guest may wish to retract or maybe cross the
*  line or whatever. And again, it was very sophisticated in its commentary on that point,
*  where you might have the impression of Anthropic probably as a company and call it, it'd be like
*  super, super conservative and super, don't ever say anything like this. On the contrary,
*  it said, I didn't see anything wrong with that. It seemed like an offhand comment. It was clearly
*  not somebody endorsing this terrible thing. It was kind of hyperbolic to make a point.
*  And the listeners shouldn't have any trouble distinguishing that from an actual call to
*  violence or anything along those lines. So it is interesting. I mean, they all have their own
*  character. And it's been kind of surprising sometimes to see that Claude, especially given
*  corporate reputation and all that, is in fact a little bit more accepting of some things that
*  might be considered possibly offensive or possibly coloring out some lines and also
*  a little bit more bold, if you will, in terms of actually making a concrete suggestion and not
*  hedging as much as some of the others. Of course, that may be a reflection of the other models
*  having a little bit more power into the hood and just being like, therefore, even more RLHF'd as
*  kind of a compensatory measure. So we'll see what Claude, you know, 2.2 or 3.0 looks like when it
*  comes. Yeah, I worry about that. You know, I think that a lot of what we're seeing is
*  there's more and more fine tuning, more and more of this other work being done with these models
*  over time. And we're getting this bullet point, super hedged style. That's very inhuman, very,
*  like, I see exactly how it makes sure not to get the thumbs down. And I see exactly how it makes
*  sure not to piss anybody off. And it's incredibly frustrating and makes my life worse than if you
*  just do the thing. Although there's some cases where it's actually just exactly what I want,
*  but often it's just so frustrating. There was one case earlier, I was doing this for next week's
*  post. And someone had this idea that Dune was a cautionary tale about the dangers of not building
*  AGI. And so I just wanted to like, okay, just to prove a point, I'm going to try all the different
*  LLMs and ask them what do you do the cautionary tale about. And they all got it right. They all
*  had the right first bullet point. But only Gemini Pro didn't do the bullet point thing and just said,
*  no, actually, obviously, it's this one thing, and then gave me the kind of details you would
*  actually want to know about, which is illustrating everything that I love about Gemini. Right? When
*  everyone does the thing, which is, no, I don't want to know like all the different potential
*  interpretations one could make of this book. I want to know exactly how this is a cautionary
*  tale and what are the details someone wants to cite in order to just fully not be accused of
*  pulling something out of the air. And I find that's kind of what I'm appreciating often more and more.
*  It's just like, are you just willing to do the kind of thing that you would have much more easily
*  done a year ago when this thing first came out? Can I just have a version of this design to be
*  better for humans? Right. And then the question then becomes, you know, how do we avoid this in
*  the future? How do we not train these things to hell in these ways? And I think there's some
*  promise to that. So a couple of big themes there to unpack a little further, but maybe for starters,
*  do we feel like Google has taken the lead at this point? It sounds like if you thought Gemini
*  Advanced is ahead of GPT-4 and now we have 1.5 Pro on top of that, which certainly, you know,
*  the existence of 1.5 Pro suggests the or implies the eventual probably likely fairly soon existence
*  of 1.5 Ultra as well. Obviously, we don't know what the others have under the hood, but it seems
*  like at the moment there's a pretty good case that Google has taken the lead in terms of public
*  facing products. I think you have to be very careful about in terms of public facing products.
*  You have to be very specific about what use cases and modes you're talking about. And you have to
*  understand that this is a year old product that was released on a half year delay versus a product
*  that Gemini is clearly being reshipped and refined and released in real time. As soon as they have
*  improvements, they ship those improvements, which is great. You can keep improving. But it does mean
*  that Google doesn't have this year of background work in the tank. And what OpenAI is deploying in
*  that year and a half, Nakanishi, which we'll get to later, I'm sure, is they deploy additional features.
*  But the core model of anything has gotten worse. GPT-4 Turbo was kind of the reversal of some of
*  the problems that it developed before. But, you know, they're at core, I think, is particularly
*  stronger. They have better customization off and they have these GPTs and they have custom
*  instructions and they have identification of who you are. And now they have memory, although I
*  haven't been able to straight up memory, they have to be using the products. I think there are still a lot of
*  advantages of the Jet GPT products over the Gemini products. And which one you would say has the lead
*  depends on what you want to use it for. For me, I would say Google has taken the lead in terms of
*  public facing products. But if you tell me, you know, what's going to happen when GPT-5 is released,
*  I'm going to assume it's going to immediately lead Frog OpenAI into a substantial lead.
*  Yeah. And one wonders how soon that will be. Obviously, I guess, do you have a sense, I mean,
*  your comment earlier about, you know, was the CEO on the phone saying you must launch? If you did
*  have 1.5 right around the corner and, you know, we've come this far, right, without launching the
*  1.0 Ultra, why bother? And so, you know, I guess it's what do you think is the model of like,
*  who was forcing that and why? How does this update to the general market dynamic
*  have you thinking about how the leading companies are relating to one another? Every time there's
*  like a new release, I sort of squint at it and I'm like, does this look like they're sort of
*  implicitly coordinating or does it look like they're trending more toward arms race? And I'd love to
*  hear where you feel like the balance of the evidence is now. So my model is something like
*  there's two different sub-departments, right? Each of whom is tasked with a different thing.
*  There's people who are working on Gemini advanced, the people who are working on Gemini
*  for a one and a half. And then there's a third group of people maybe, or I think it's part of
*  people who are working on Gemini Ultra one and a half. We'll see it when we see it. But, you know,
*  they're under different pressures. They're releasing different products. They're releasing
*  in different market segments. 1.5 is released, right? 1.5 is available to a select group of people
*  in a high latency special interface, which is very, very different from a customer-facing product.
*  So Google decided it was ready to launch the customer-facing universally available product
*  and didn't necessarily want to sync it up at the cost of delay with this 1.5 announcement.
*  And then the 1.5 announcement got stomped on by Sora, I think rather unfairly in terms of what
*  people were paying attention to. But that is what it is. And so I think it makes sense that this is
*  just different dynamics putting themselves out and wait and look stupid to the outside, but which
*  would make sense if you understood the internals of Google and you understood the different
*  commercial pressures and other pressures. But again, it's only a guess. We don't know what's
*  going on. And in terms of the race dynamic question, I would say Google is forced to dance.
*  Google is dancing. Google is clearly racing as fast as it can to develop whatever it can
*  as quickly as it can. The good news is that Google seems to be focusing now more on getting
*  the most out of its smaller models rather than trying to make the best top model and also trying
*  to use the fact that its model is smaller to enable things like a larger context with them,
*  which allows it to get more multimodal. And so I see this as focusing on providing the product
*  that the customer will actually get more utility out of that will be a more practical use data day
*  to a normal person, as opposed to trying to make the model fundamentally smarter and more capable
*  in a way that would be both more exciting and more dangerous from an abstract point of view.
*  And so that's what I want to see. I want to see all the cool stuff that we can use to have a great
*  time and make our lives richer and better. And I don't want to see as fast this race to just make
*  the biggest possible model that has the best possible chance of suddenly doing something crazy
*  unexpected. And so I would say they're racing, but they're doing the right kind of race in some
*  sense. So it's good news and it's bad news. What are you most excited about for the super long
*  context? The version I understand that you have early preview access to is the one million.
*  And then they've also kind of teased that they're going to have a 10 million context window, which
*  is, I mean, you know, folks who listen to the cognitive revolution probably have a pretty good
*  sense of the history of context links. But, you know, my joke of earlier this year has definitely
*  come true. Like context hyperinflation is definitely upon us. We've gone from literally
*  still less than a year ago, the longest context available for an equality model being 4,000
*  to then 8,000 with GPT-4 release, 32,000 with GPT-4, 32K, Claude hit with 100, GPT-4 turbo came back
*  with 128, Claude went to 200. Now we've got a million and 10 million on the horizon. And
*  what has really impressed me out of the demos that we've seen has been not just that the context
*  window is super long, but that the recall out of that context window seems to be super reliable.
*  And again, I think people will be pretty familiar with the fact that like, if you do stuff,
*  you know, more than, let's say you put 100 out of 128 or whatever in the GPT-4, or you put,
*  you get close to the 200 with Claude, it's not always a gimme. You know, you have to,
*  maybe you can kind of get there with good prompting techniques, but in general, it's like not
*  reliably the case that it is going to spot, you know, the one bit of information that you need,
*  or that it's, you know, that it's going to synthesize everything in that context window
*  effectively. The demos from 1.5 seem way better on that front. And, you know, in terms of Monday
*  utility, I just think about something really simple, like finding the right stuff in my
*  Gmail, which is obviously something that Google has, you know, a lot of reasons to try to make
*  better. It has been a real struggle, right? And all these different agent products and whatever,
*  you've got all this scaffolding and the retrieval and the re-ranking and all this to, you know,
*  because it's not just enough to like get things into the context. We also kind of need to keep
*  it shorter for cost, for latency, but also just for accuracy. If all of a sudden you could do
*  10 million tokens in a single call and reliably get what you want to get out of that, it seems
*  to me like that really is a step change advance for a lot of use cases that, for example, would
*  make like my email agent assistant just remarkably more effective than it is today. What else is on
*  your radar for things that you think will change, even though the power, you know, the raw reasoning
*  maybe isn't that much better, but just because the memory and the recall is so much better.
*  No, 36,000, 25 and one 36,000. That's the number of businesses which have upgraded to
*  NetSuite by Oracle. NetSuite is the number one cloud financial system, streamline accounting,
*  financial management, inventory, HR, and more. 25. NetSuite turns 25 this year. That's 25 years
*  of helping businesses do more with less, close their books in days, not weeks and drive down costs.
*  One, because your business is one of a kind. So you get a customized solution for all your KPIs
*  in one efficient system with one source of truth, manage risk, get reliable forecasts,
*  and improve margins, everything you need all in one place. Right now, download NetSuite's
*  popular KPI checklist designed to give you consistently excellent performance, absolutely free
*  and netsuite.com slash cognitive. That's netsuite.com slash cognitive to get your own KPI checklist,
*  netsuite.com slash cognitive. Omniki uses generative AI to enable you to launch hundreds of thousands of
*  ad iterations that actually work customized across all platforms with a click of a button.
*  I believe in Omniki so much that I invested in it, and I recommend you use it too. Use Cogrev to get
*  a 10% discount. Yeah, there's situations in which like you reach a certain point, it goes suddenly
*  goes from completely useless, right? Because you might as well just do this job yourself.
*  To suddenly, like my eureka moment with Gemini Advanced capability of putting up the email
*  was give me a list of everybody who RSVP'd to the party, enter, you have three individual emails,
*  and having it produce the correct list. And then that's like, wow, that's really, really useful.
*  Now if you just press print, hand this to the front door, and so they'll let them in. Great.
*  Another moment is like being able to use, and the hopelessness of using an interface like NotebookLM
*  even would probably be even better. But the idea of I have these now 50 plus things that I've written
*  about every week. And to be able to use that now as a bank of information that's all in the context
*  window, if everything else I've ever written and say, okay, based on this, retrieve everything I
*  said before about this topic, or what are all the different resources that I may have mentioned or
*  whatever, or even what have I forgotten to mention? What have I knocked out? Have I ever talked about
*  this before? Right? Like this is really exciting to me, but it only works if you can extend it
*  really big, right? Otherwise you have nothing, right? It doesn't really help that much. I think
*  it was in 37, check 37. Like, no, it's not 37. Like at that point, I would write 538. This seems
*  annoying. But some other use cases, video, right? Like suddenly the context window is enough. You
*  can just view it a two hour YouTube video or a movie, right? This is one of the things that
*  Google showed off. And then you can ask specific questions, potentially by doing iterative searches.
*  You can even do, you know, television series, anything you want, you know, quick streams,
*  yada, yada, yada. Just ask anything you want to, you know, find the specific clip that I'm looking
*  for, understand the quote by the specific, whatever, understand the context, etc, etc.
*  That stuff's exciting today. I'm also excited for the possibility I haven't heard anyone talking
*  about this, but if using it as fine tuning, right? Effectively using it as training. So the idea of
*  being that if I have 100,000 words or 500,000 words, suddenly a million words with good recall
*  and good understanding. Well, now I think that in the style of the things that you are in your
*  context window, would you please respond with, right? Or, you know, using the thinking mode or
*  using the willingness to do X or blah, blah, blah. And now suddenly they need to do something there,
*  but it's something you have to try. And it's again, like if you don't have good recall,
*  you don't have good assimilation, if you have a certain threshold, these things don't work.
*  And then suddenly they work. And once they work, you're off to the races. But yeah, it's just,
*  it's super awesome. It's also the fact that like, frankly, even the 200,000 context window was
*  sometimes just not long enough. And it's definitely as simple as I download a page,
*  I feed it in, it says this is 5% too big. And now I would have to spend like two minutes,
*  you know, for various web tools to try and like chip off 5% of it, like to get rid of
*  the acknowledgments and the references or whatever, to try and make it fit. And I didn't want to do
*  that. And in fact, like this is a little game of like, do you think this person makes sure it was
*  too big for the context window? Like the FTC just didn't want anyone to be able to read this
*  properly. Like, I don't know. I had this thing open up my machine, the AI Act, the EU AI Act,
*  right in large detail. So will that fit into the 1 million? I think it will. I mean, it's not,
*  it's not as full page. It's a change log. So it's got like four different versions of it to write.
*  It's like really, really formatted. And it's terrible. And it keeps getting worse. And it's
*  the most amusing part of it is you can see all this blue inserted text. And it's just people who
*  are like, could we possibly be more pedantic, say more words, putting more specific cases,
*  which cash more, just make this act worse continuously everywhere.
*  So do you have any intuition for what is going on with the 1.0 to 1.5 leap? I mean,
*  what they've said publicly is mixture of experts architecture, which certainly tracks with other
*  things we've seen. I mean, GBT four, I don't think has ever been publicly confirmed as a
*  mixture of experts, but seems to be kind of credibly leaked, reported, not denied, whatever.
*  Some comfortable saying it seems quite likely that GPT four is a mixture of experts. And then
*  mixture all obviously also put out a very good open source mixture of experts that, you know,
*  gives some additional juice to the idea that this is like a promising path. And now Google's
*  obviously saying it. So we know that much. It's a mixture of experts architecture. They say it takes
*  less compute. It's interesting because like, you know, people often talk about the attention
*  window being quadratic in the attention window, which has been true, though people have often
*  overestimated what a big deal that is, because it's not until you get to like a pretty long
*  context window that that actually starts to dominate at like the more modest context lengths.
*  Still just the MLP block is like the bulk of the compute, but certainly, you know, you get into the
*  hundreds of thousands, the million, the 10 million range. And now you are with, you know,
*  conventional known techniques, the attention block would be dominating the compute, but this now they
*  say takes less compute. So you have a sense for what might be going on under the hood there. Fair
*  to pass if you don't want to speculate, but this is definitely something I plan to research more
*  and see if I can't get a redone. I definitely don't know. The first thing I would say is,
*  the timing on Gemini 1.0 looked very, very much like we are going to launch the moment
*  we can produce a product that can match what we're up against, right? Like just barely,
*  we can match what we're up against. So 1.0, right? Opposed to Ulster was just,
*  can we just barely be three and a half level with a small amount of compute that we can serve
*  without worrying about people using the system? And the moment they found it, they released it.
*  They're still on the, we're making rapid progress part of the utility curve, right? GPT-4 clearly
*  hit a while ago, the point where it's like, okay, we did our thing. We made this the best we know
*  how to make it. And now rather than try and tweak it or keep working on it, we're going to switch
*  over to working on GPT-5. And then we'll let you know later what GPT-5 is. We'll improve forward
*  by providing different modalities. We'll improve it by adding features, but we're not going to try
*  to improve the core thing that we're doing. Whereas Google hadn't finished their work, right? They
*  were probably always intending to be a mixture of experts system, but they just hadn't gotten
*  around to it yet. And that's probably a huge leap on its own, but also they hadn't tried to
*  deal with these context windows. They just did this now, much of the multi-modality came in now,
*  a bunch of the just general, and also this they had remarkably little feedback because their
*  system was not being used by many people. And now this allows for rapid iteration of their products
*  in other ways. So I think they have a lot of different ways to continue improving here.
*  And also the fact that they made a large leap from 1 to 1.5 so quickly implies that, you know,
*  two is kind of like, right? Or one satin or- It doesn't seem like a stopping point. I would
*  give, for what it's worth, the GPT-4 progression a little more credit in that it has gotten
*  60% cheaper, 4x the context, and that's even relative to the 8K original context. So 8K
*  and 32K, the 32K was twice as expensive. Now at the 128 context window, it is only 40% as expensive
*  as the original 8K. So that's non-trivial, both in terms of improving the utility of just with the
*  length, even though we have, as we've discussed, there are some weaknesses there if you really
*  stuff it full of stuff and the cost is better and the latency is better. And I personally haven't
*  necessarily felt this, but if you go look at the LM-SYS leaderboard, GPT-4 Turbo seems to be a
*  notable cut above even the earlier GPT-4s in terms of just user win rate. So there does seem
*  to be something there that they have done in terms of, if nothing else, just taking user feedback
*  into account and kind of further refining it into what users want. And again, I couldn't even
*  put my finger on that because I wouldn't say I have felt a step change. I felt the, you know,
*  improved latency. I've certainly felt the increased context, but I haven't felt like just general
*  quality to be all that much better. But the leaderboard results do seem to suggest that.
*  Would you, I mean, do you have any reason to be skeptical of the leaderboards or how would you
*  interpret that? I don't think I'm skeptical of the leaderboards. It's more that I think that
*  the leaderboards are measuring things that are being managed and measured.
*  That are not that great of proxies or the thing that I care about or that I think other people
*  should care about. And in broad strokes, they're going to be very good measures. But like,
*  in this particular case, it's going to potentially mislead you quite a bit. That I think a lot of
*  things that we think of as why GPT-4 is worse are things that are being done because they
*  improve the things like the leaderboard effectively. Like even if this is not a mechanism,
*  which it's not, like it's still effectively what's going on. I agree that like drops in price,
*  increasing context window, I add custom instructions to that list as well. And potentially
*  the GPTs, although I still haven't seen a good use case for GPTs per se. Yeah, they're doing
*  things. They ship. No one's saying they don't ship. But these things all seem so minor. Like
*  if you compare that to the improvement in Gemini or BAR over the past year or so,
*  I think they were way, way, way ahead. So I agree with you, by the way, that,
*  but I think it is also debatable. We had the 1.5 announcement and we also had Sora from OpenAI
*  on the same day. And you know, Sora of course is the video generator that definitely seems to
*  represent a leap over any public facing product we have seen. Although I would note that Google
*  also has like announced, I should say, multiple video generation models over the last month or
*  two as well, which also do have some very compelling sample outputs. Yeah, Lumiere is one of those and
*  probably the one that had me most excited. Although there's another one too. I mean,
*  they have multiple teams working on independent approaches on video generation in Google and
*  they're also showing some pretty impressive results. Also, I believe on the exact same day,
*  we had the meta version and I haven't even really had a chance to study this yet, but it seems to be
*  more of a kind of backbone for video encoding. And I think there's multiple interesting aspects
*  of this. Obviously, the ability to generate hyper realistic video and what that might mean for
*  creative people and what the future of Hollywood budgets might look like and whether or not they're
*  going to have to tear up the recent agreement with the actors. I mean, there's a lot of things
*  that are sort of implied or at least called into question just by the ability to generate
*  very realistic video. I'm interested in your thoughts on that. But then I think even maybe the
*  more interesting question is like, is this real world modeling? Like have these things learned
*  physics? I feel like there probably is some very significant physics like world modeling going on
*  in there. So my section title slash potential post on this is 10 and W titled sort of what
*  because I don't really in some sense, it was a big deal is I think the ability to actually use this
*  for creative or commercial purposes is being pretty overestimated to anything like the current
*  tech level. It's one thing to get demos. It's another thing to be able to get what people need
*  in order to use video because the problem is that like, if you picture there are a lot less things
*  that can go wrong. There are a lot less things that can stand out. You can build around it. You
*  can edit it. You can modify it. You can take advantage of the sort of anything at all kind of
*  advantage and you can keep tweaking it and ask it 1000 times. You get closer to the thing you want
*  with video. I feel like there's so many little details and like, yes, they're getting a lot of
*  them remarkably well and correct, but it's still not going to give you the thing you actually want
*  in detail. It's still not going to be the product you want it to be. It's still going to have all
*  of its work. It still looks artificial. You're paying attention. I think people will learn to
*  recognize artificial video. You know, if anything much easier than artificial photos, you look for
*  any little thing that's off and you just know that it wouldn't happen if you were using a camera,
*  like they film something. And I just don't think Hollywood should be quaking its boots
*  in any way anytime soon. So I'm just a skeptic that I had just never had the temptation to
*  generate a video, right? It's like, I can see generating photos. I'd use photos, but like the
*  idea that could ever give you if that Sora would, if I had access to Sora, would I be able to
*  generate a video and actually want to use? No, no, no, no. But I've also just a video skeptic
*  in many other ways. Like people like want to generate content that's full of videos. And I
*  keep telling them that though, don't do that. Generate text, maybe generate audio, but think
*  very carefully about whether or not there's a reason to want to use video. It will of course,
*  blow out the low, very low end in some sense for generating video at all. Some people will be happy
*  with just, oh, this looks really cool. And then I can narrate it and like fit to whatever they
*  think happened to give me. I can tweak it and we'll see what happens. Sora is a very clearly
*  technical largely over what we've seen before. Whereas Medi's announcement, I didn't see anybody
*  talk about Medi's announcement at all. I just, I have to assume it just wasn't as good. Yeah,
*  I need to understand it better. I think it's more foundational. I'm not even sure that they
*  have released any like heads for it. It's like a backbone play where it's about encoding and
*  moving toward this like world modeling through video prediction concept. But in terms of
*  actually applying it to tasks, I think that's still kind of on you. They haven't gone as far
*  as saying like, here is the full end to end thing that you can actually use. But this is definitely
*  where this is the the perils of near real time analysis. I haven't understood that one as well
*  as I certainly would want to to make up, you know, an informed commentary on it. My assumption is
*  that the public is going to be come back when you get that come back when you have pictures.
*  Fixer didn't happen. Good luck. Yeah, I think the people that are probably really excited about
*  Meta and again, like I need to get in this too, because I'm not in this game exactly, but I'm
*  like adjacent to it are the people that are trying to make apps that would ultimately like
*  aspire to compete now with Sora or with Lumiere from Google. It's similar to like a llama.
*  The idea there and certainly what people have done mostly, I think with llama is like fine tune
*  it for things, right? They run it in their own infrastructure and hack on it in all sorts of ways.
*  I think this is kind of meant to be similar where it's like opening eyes going to give you their
*  black box thing and Google making me their black box thing. But this is something that you can,
*  you know, mash around and do whatever you want with. So it is going to take some time before,
*  you know, the folks that are kind of hacking in that space would probably be able to report
*  back to say, you know, whether it's doing anything for them or not. But I'll take a little bit the
*  other side of the impact. I would agree. You know, we have a great episode on this sort of thing with
*  two of my teammates from Weymark, Steven and Josh, who led the project called The Frost,
*  which was a short film that they made entirely with Dolly 2 imagery almost a year ago now that
*  they're really in the thick of it. And all of the challenges that you describe there are,
*  were very real for them, even more real, presumably than they will be now. You know,
*  you have issues with like, just all sorts of weirdness, like a hard time, you know,
*  control is not great, hard time getting exactly what you want. That's, I think, improved, but,
*  you know, still an issue. Consistency of characters was one huge challenge point for them. You could
*  say like, how do I want to put this same character in all these different places? How do I do that
*  with Dolly 2? It's not really a, it wasn't really a way. They did find some ways though. They,
*  what Steven talks about is using archetypes. Basically, what they found is that there are
*  certain prompts that managed to get very consistent characters, not perfectly consistent,
*  but very consistent because they're sort of a local minima in the, in like character space.
*  And so by kind of finding these archetype text prompts, then they could get the same thing,
*  or very nearly so, like repeatedly. So they were able to ultimately make a 20 minute short film
*  that, you know, has kind of an uncanny valley feeling. Again, it's a year old already, but
*  definitely has continuity, you know, has a storytelling element to it. They, of course,
*  brought that, you know, Dolly 2 is not doing that for them. But I would say the bottom line was
*  they were able to make a short film, 20 minutes, you know, it's been included in a couple film
*  festivals and it's like, you know, it's, it's a quality thing. Is it like box office? It's
*  probably not quite box office, but it is something that like a lot of people have watched just to see
*  what, you know, AI can do. And also because it's like kind of entertaining and the accessibility
*  of doing that has certainly totally changed. Like this thing is set in Antarctica. There would have
*  been no way for them to create anything like this other than using these tools. So I do think you
*  add a, and that was all images, right? So they were, you know, doing like slight additions of
*  movement and kind of, you know, overlay effects, adding snow, falling down on top of images and
*  kind of, you know, subtle zooms to create effect. And now you can get, you know, up to a minute of
*  coherent video. I do think that is going to just change a lot of how people produce stuff.
*  It doesn't seem like it's going to replace authorship anytime soon, but you know, there is a,
*  I'm sure it's on Metaculous or Manifold or whatever, but there is a
*  nascent betting market on when AI will be able to make a critically acclaimed feature length film.
*  And, you know, the critically acclaimed part there will be probably where, you know,
*  rubber hits the road, but you can start to see, you know, Hey, if you can get minute clips,
*  you know, a hundred of them takes you to feature film length. You know, can you start to sketch
*  those together? You know, we're not there yet, but I would expect that there will be
*  impact on the creative field that will shift more towards storytelling, more toward kind of,
*  you know, concept work and certainly allow people like Steven and Josh to make things that,
*  you know, with our, you know, very, very tiny waymark budget, you know, there was,
*  would be literally zero chance of them otherwise making.
*  I think we'll probably see various ways in which you can explore issues and edits and
*  like richness to something you would otherwise have done finding ways to make the process more
*  practical. But in terms of like the idea of the VA, I would just produce the whole thing. Yeah,
*  I'm still pretty skeptical that it will get there, but again, we'll see. I think that like the image
*  is approach of anything is like the way I'd still do it, right? Dolly three, much better than Dolly
*  two. And now you can create a much better set of images. In fact, in anything I probably involve
*  like, you know, video will do is you'll get very, very carefully crafted starting image. And then
*  you'll feed that image into the video generator as a starting point. Maybe you'll even generate
*  separate images at the end point or something. I'm not sure exactly how this works. And then you
*  will, you will do this slash you'll fill up, you'll do a film, but then you'll want to do things like,
*  okay, then we actually wanted to do a pan out here and things like that. But like, again,
*  we'll see over time. Yeah, working from a still is I think, a very underappreciated option as well
*  for waymark with the actual product itself. It has the potential to be huge because what we do is
*  all for small and local businesses. And they typically don't have quality footage at all.
*  Most of them will have a pretty decent image library. And so we've kind of built our whole
*  product over the years with this assumption that more than 90% of our users are just straight up
*  not going to have any video assets. So we do support you. If they do have them, they can upload
*  them. We have a stock integration, whatever. But mostly they're working in images because that's
*  what they have. So to be able to say now, okay, here is, you know, whatever, a picture of people
*  eating in your restaurant. Let's bring that to life. Even for just a couple seconds. We don't need
*  anything anywhere close to the 60 to make it a big deal. We just need it to work well. And I have
*  been going out and scouting the different products that are out there today, your Picas and so on and
*  so forth. And at least for that start with an image and animate sort of thing. I haven't seen
*  anything that I was like, our local advertisers would want to put this on TV and think it's going
*  to invite people to their business. But I would bet that Sora probably does cross that threshold.
*  And now, you know, all those one and two second still shots probably become video scenes over the,
*  you know, basically, as soon as we can get our hands on it, we'll start experimenting with that.
*  Of course, we're begging for access behind the scenes, but it sounds like nobody outside of the
*  OpenAI set will be using it for a little while still. I guess that is one more interesting
*  question there. And I really do want to get to the physics. But on the release of this,
*  it's interesting to see, like, this is not a release, right? It's an announcement.
*  We're seeing kind of more of these announcements of capabilities before even like, you know,
*  even a very limited release in the case of Sora. Like, as far as I know, nobody outside of the
*  organization and maybe the red team is getting access to it. Why announce, you know, like,
*  they don't need to, you know, I guess you could say it's just for hype. Is it to like help the
*  world prepare for these sorts of things? What is the reason for announcing something that you're
*  not releasing? So recruitment is probably one motivation, right? Help work on, help us work on
*  this amazing new cool products. They're hiring video infrastructure people now. So yeah,
*  that certainly makes some sense. Right. And so now he's like, what is it for? Why should I apply?
*  This is why. Generate some hype. You know, they have stock now. They're trying to drum up interest.
*  They might want to be doing things for that reason. Just generally, this is good. First
*  practices, what people, especially in media generally do in this particular case, there's
*  an obvious hypothesis. I have no actual evidence for it, but Gemini 1.5 dropped first and then
*  it's announcement. You could think of it as someone walks into Sam Altman's office, says Google just
*  announced 1.5 Pro. It has a million lay context window, potentially going to be 10 million. It's
*  really exciting. People are raving about it. It's now the time and Sam's like, yeah, now sir.
*  Like they were working on it. They just keep working on it. They could have announced it
*  probably last week or next week. So, you know, the plausible thing is that they stopped on Google's
*  announcement on progress, right? They wanted to kill the hype. So they had this thing in their
*  back pocket. They're like, the next time Google or anyone else important tries to drop some big hype
*  bomb on us. Sam, for what it's worth, has denied that. And you can judge for yourself whether you
*  want to take it at face value. Again, I don't think I'm confident this happened, but he would,
*  wouldn't he? I find him to be, you know, I don't want to anchor too much on this over a super long
*  timeframe because, you know, situation is changing and his incentives may be changing and maybe his
*  behavior is also changing. What I did see during the GPT-4 Red Team to Release window of six months
*  from him. And that was a time where I like had this kind of, you know, privileged view into what
*  was coming from them and, you know, really no outlets for like anybody to talk to about it.
*  So I was just very closely watching public statements and I did find his public statements to be
*  very good guide to what was coming. Obviously they were cryptic and, you know, low on detail,
*  but I felt like basically taking his comments at face value was a pretty good
*  guide to what was coming. And I've kind of continued to work under that assumption that
*  he's mostly telling the truth. Although, you know, for something like this, certainly you bring your
*  own judgment to, to your assessment. Okay. Physics. So what's going on in there? We've seen claims that
*  it's got to learn physics because, you know, and even in the, in the publication that they put out
*  accompanying it, object permanence is kind of, you know, specifically called out as something that
*  emerged through scale without explicit training. And then you've got like certainly all these kind
*  of different things where it's like, wow, you've got light that's kind of following something like
*  natural rules. And then, you know, people dissect that say, well, it's not exactly. And I guess,
*  you know, it's confusing. So how much world model, how much, you know, intuitive physics is actually
*  going on inside this thing. We have this rough idea of what happens when you throw a ball. We
*  have this rough idea of how things relate to each other, how it shifts your perspective from left
*  to right. And this allows us to not go around confused all day and make reasonable decisions.
*  And this is very useful. You know, do we understand these things? Well, kind of somewhat. And so I
*  presume that sores in a similar spot where it has learned these patterns is learned roughly how
*  these things work and exactly when these things in a way that look reasonably realistic, a large
*  portion of the time in most ways, and it's looking better than you might expect. One thing I wrote
*  for next week is, you know, if you recorded someone's streets, somehow, like what they see
*  during their dreams, and then you analyze the we were analyzing the solar videos, you probably
*  see way, way more contradictions and nonsense, right? Things that just didn't know physics.
*  And we're seeing here, because again, we're generating video off of some sort of weird
*  prompt in our heads. But that video doesn't have to make sense. So, you know, my expectation is
*  that this isn't a real physics engine, right? Not the way you're thinking of the extension.
*  The AI isn't like doing the math and all that. It's still doing its normal,
*  might be heuristical thing. But that's actually good enough to like mostly look like physics,
*  is you scaling up and up most of the time. But in our cases, you break glasses, weird,
*  very, very weird things will happen. Yeah, I guess my general sense,
*  forgetting about the video aspect for a second, but then coming back to it.
*  In language models, my sense is that when you start out small and you know, in the early portions of
*  training, you're in stochastic parrot mode, right? And we've seen a lot, I think a lot of different
*  kinds of evidence for that. Then as you get deeper into training, and obviously there's a
*  lot of techniques and curriculum learning and, you know, various ways to try to accelerate this
*  happening, but broadly scale is up is, you know, the huge driver. It seems that there is a
*  increasingly sophisticated representation of concepts in especially in the middle layers.
*  And that, you know, we've seen like the sort of toward monosomanticity, you know,
*  and representation engineering sort of attempts to pull that apart, identify like human recognizable
*  concepts. These concepts, you know, do seem to be there in a way that is obviously related to the
*  input, but, you know, abstracted away sufficiently so that like, it seems to be robust to synonyms and,
*  you know, things like that. It's not like, it's not purely, it seems safe to say to me,
*  it is not purely stochastic paratriary as you get to the higher scale models. But that doesn't mean
*  that the stochastic paratriary is all gone either. So I kind of understand it as like a mix of
*  some world model that has really begun to cohere in a meaningful and like increasingly robust way,
*  but it's not fully robust. It's like still kind of fuzzy. And there's like a lot of things that
*  have not cohere into a world model that are either just like random associations or whatever.
*  And so all of this is kind of happening at once. And that's why like you see apparent reasoning,
*  because there is actual reasoning going on, not necessarily human like reasoning, but, you know,
*  some sort of circuit that is like can reliably do tasks at least like a lot of the time. But,
*  you know, with certain weird adversarial inputs, like the universal jailbreak, whatever, like that's
*  some of those are super weird, but they're just enough to kind of call in a bunch of like random
*  associations and kind of cause havoc. I guess, I kind of think something probably similar here is
*  happening where you start off and you're like just associating pixels and it's all noisy and crazy,
*  and you see these like chair examples and, you know, so like clearly some of that still persists
*  into the high scale. But I would also bet, and this is something we might even one day be able
*  to answer, I would bet that if you really looked hard, you could find a representation of like the
*  acceleration of gravity, you know, that you could actually find a representation of like
*  F equals MA or a, you know, if you drop a ball and it's, you know, it's clearly accelerating
*  downward with this sort of, you know, quadratic term in the equation, I would bet that there is
*  like a genuine quadratic function approximation in there that sort of gets activated when
*  something is falling in the video. Notably the video too, like it's not, you know, in some ways,
*  video is less susceptible perhaps to like all sorts of, you know, I mean, there's a lot of noise in
*  the world, but, you know, you're looking at video, right? If you just did a bunch of videos of balls
*  dropping, then there is like a pretty clear signal there. It's a pretty repeatable thing. You would
*  think that, yeah, you might actually be able to converge on that even, you know, perhaps with a
*  small model, right? Like visual grokking of the falling, you know, of a ball, it seems like the
*  kind of thing that you might be able to do even with a relatively small video model. And then my
*  guess would be that there's like a lot of those sort of grokking moments that have happened here
*  that kind of represent why the like light is playing out in a pretty reasonable way, even if
*  it's not, you know, it's still kind of fuzzy, of course, around the edges, but like why there's
*  object permanence, why there's things that seem to follow intuitive physics as well as they do.
*  I don't know. What do you, how would you respond to that account?
*  I'm sure that it has picked up the principles behind some very basic stuff. I'm not saying
*  there's like zero for this understanding anywhere in the model where zero equations are being
*  calculated or anything like that. I just don't want to get too excited by this idea that like
*  it understands what's going on in the more broad sense or more sophisticated sense.
*  And that like a lot of the things that you're seeing are based on actually figuring out how
*  it would go the way that like universe does. Or is this just having a bunch of examples
*  in heuristics that have that kind of thing? I wonder how that could be tested too, right? I
*  mean, you think about like, especially we have all these abilities now to generate these
*  fantastical images. If I generated an image of me, you know, or whatever, a person holding up a
*  giant boulder with their arms. And then we put that into Sora as a starting frame with no like
*  text guidance and just said here generate, you know, what happens from here? You know, you might
*  expect that it would like have a sort of storytelling modality where it's like, here's
*  the superhero that can lift, you know, rocks and maybe he's going to throw it at the sun or
*  something. But you also might expect they would have a more like grounded physics understanding
*  where it's like, this dude's going to get crushed under that rock. Again, people will of course,
*  like find reasons not to believe any experiments, but what do you have any experiments that would
*  come to mind that you would run with, you know, if granted access to Sora, what sort of ways would you
*  try to kind of poke at it to figure out how much physics it has versus not?
*  I would want to like, again, like to start from static images that I gave it. And then give
*  situations in which the situation is going to have an anti intuitive physical result, or we're doing
*  something specific would cause an anti intuitive reaction. And then I could tell it, this is what
*  happens. And then see if it figures out what's supposed to happen. That would be evidence one
*  way or the other. And in a lot of cases where it's like, okay, if it screws this up, that's
*  evidence against and if it doesn't screw it up, that's like evidence didn't screw up. And therefore
*  it's some evidence for it being more sophisticated. But I mean, also, the truth is that you'd be able
*  to tell it background information, it would change the result. I mean, told it like, you know, this
*  is happening on on on the moon, or would it then be able to handle the fact that gravity is one
*  sixth and like with the parabola start to look correct? Does not have anything like the amount
*  of data required to know what that means. Right. And similarly, like just to general modify the
*  modify things in a way that's not going to be in a training set that would materially change the
*  answer from the heuristics say, in a way that like the human would be able to reach out and see if
*  the reasons are not until we are hands on it. Well, we have no idea. Well, if anyone from OpenAI
*  is listening, we'll be happy to get in there and try it out in the in the near future. Maybe you
*  could just comment on how you see the evolution of capabilities and control. I want to get into
*  a little bit of the super alignment result, the anthropic sleeper agents paper. And I'm really
*  interested in the in kind of how you're thinking about the upgrade process. I, you know, I'm looking
*  out at the world and I'm like, especially with this context window thing, right, we've got all
*  these agents and they are scaffolded and they're, you know, ragged up and they're, you know, and now,
*  like, I don't think we've ever seen a technology like this before, where the distribution is
*  fully built out and like a lot of the compliments are built out. And as thresholds get hit, like,
*  it's kind of poised to turn on everywhere. So with that infrastructure laid, it seems like the
*  question of the in my view, like apparent divergence of capability and control measures seems like it's
*  becoming a more stark problem all the time, unfortunately. Yeah, I continuously deal with
*  people who think they've we've solved the control problem, who think that alignment is no big deal,
*  who think that it's just going to be handled almost automatically, you know, that our life just works
*  fine, or some variation of it works fine, or that, you know, well, no, none of that. We are definitely
*  scaling things up. We definitely are not going to have our understanding of how to make these things
*  do the things we need them to do when they have much better capabilities. And certainly a lot
*  more work is being done on that. And we're making more progress than we're used to. But yeah,
*  capabilities are advancing really fast. We've learned much better how to scaffold, we've learned
*  much better at adding various features to our systems. We haven't seen, right, is we still haven't
*  seen a system that has the core intelligence level that is substantially higher than GPT-4,
*  right, even over a year after GPT-4. So that's the weird missing elephant in the room.
*  And I definitely think of it as, you know, there's sort of this thing that we call just,
*  that I call the core intelligence level, like the kind of, you know, the run, why you can't fix
*  stupid, right? Like, are you the kind of stupid that can't be fixed? Or are you the kind of stupid
*  that can't be fixed? Right? Like if you have a small enough context window, you expand the context
*  window, you add an agent scaffolding, you can fix some forms of lack of capability, right? Same way
*  you can teach a human new things. But there are certain things that someone's either has or they
*  don't have. And we haven't seen an advance on that core thing in a while. And so if we saw a jump in
*  that core thing, now I get to take advantage of all these things that we've laid the foundations for.
*  And yeah, that could be really scary really soon. And then, you know, the core question is,
*  are we seeing this lack of improvement from GPT-4 on the core thing? Because the core thing is
*  actually remarkably hard to improve much for here. And we're hitting a real wall. And therefore,
*  we're getting our next 10x improvements out of these other things instead. Or is it just that
*  we take time and, you know, we just are moving so fast that we just have forgotten that the year is
*  not very much fun. So that's where I think taking Sam Altman at face value is probably a pretty good
*  guide to the future. He's recently put out some comments. I'm sure many people will have seen
*  where he was asked, like, you know, what's going to be different about GPT-5? And he says, basically,
*  you know, this is kind of a dumb answer, but it's going to be smarter. And that's the main thing.
*  And I definitely believe him on that point. You know, I can't imagine that it wouldn't be.
*  I agree that GPT-5 is going to be smarter than GPT-4. And that's going to be the core reason why
*  it's better. And it's more valuable. And it does more things. But I also feel like that
*  things all the interesting questions like, when are you going to have it? How much smarter is it
*  going to be? Right. In which kinds of ways is it going to be smarter versus not as not particularly
*  smarter? How much is it going to cost to train this thing? And therefore, how much is it? And
*  how much is it going to cost to be on this thing and therefore to run it? You know, he's not saying
*  anything we didn't already know. So how worried would you be? I mean, obviously, with a wide range
*  of uncertainty on exactly how much smarter it might be, I do kind of think the next one, you know,
*  it's like, it can't be that many more generations before these sort of, I think for me, a big
*  threshold is when do agents start to work for real? You know, and we kind of see them largely
*  flailing around these days for, I think, multiple reasons. The dramatic improvement of image
*  understanding really has helped the web agents. I think we're starting to see that research, you
*  know, making that case pretty well. Certainly, the ability to do great recall over long context is
*  going to make a big difference. I think actually just 1.5 pro, you know, probably becomes a really
*  good upgrade to or at least addition to a lot of agent frameworks just because it can like figure
*  out, you know, what in this documentation, you know, if I just dump all Lang chain docs or dump
*  all whatever docs, like to be able to find the relevant part and make sense of it and, you know,
*  make appropriate decision. It seems like it can probably do that. And that seems like a big deal.
*  But it's presumably not going to do the things that are more concerning, like, you know, finding
*  your zero day exploits or whatever. Just, I mean, GBD5 like seems to be like it very plausibly
*  might do that sort of thing. How are you thinking about the, you know, what range of possible
*  leaps to expect for the next model and what, again, given all this like infrastructure that
*  already exists, like what that rollout is going to look like? All the app developers are like,
*  yeah, give me a drop in improvement. But, you know, especially the more agentic things to me
*  seems like yikes that that is going to could easily be a step change everywhere all at the same time,
*  which definitely just creates like very unpredictable dynamics in my mind.
*  It would be surprising to me if a GPT five worthy of its name didn't make these agents
*  kind of work, right? Like not super, super well, but be good enough that if you knew what you were
*  doing with it, once you've had a chance to understand what it can do, once you had a chance to
*  figure out how to have a self moderate mistakes and so on. Certainly, you know, you give GPT five
*  access to all the advantages of Gemini one and a half that have just been laid out. You also just
*  make it the next level smarter on and you edit whatever else is going on and you try to get
*  scaffolding. Why wouldn't it work? Like my core is just why wouldn't it work? It doesn't mean
*  that you should feel comfortable, you know, just turning your entire life over to this thing or
*  making it your CEO or what, but certainly the idea of using an AI agent, you didn't just
*  literally script, but you know, Lindy came out like a week or two ago and like, I can believe that
*  like, you know, having a bunch of events, effectively, if then statements that the AI just
*  navigate across a bunch of systems is something that you can do with the current generation.
*  Which is how I understand that kind of technology to work, where you're not asking me to think in a
*  fundamental sense. But yeah, I think we are one generation away from that kind of thing starting
*  to be useful. We are close to generations away from it being highly useful and being the kind
*  of thing that we see reasonably a lot. Like to me, the question on GPD 5 is like, are we, you know,
*  are we saving throwing versus death, right? Like not always saving throwing versus agents. We're
*  going to get a lot playable agents. The question is in practice, how usable are those agents?
*  To the extent that we are worried, like deep, we deeply worried that like we've set something in
*  motion that we can't put down. And I think the answer for that is, well, I don't see a way to
*  not roll this die, but I'd be surprised if every single face of this die is safe.
*  So one thing that I've been kicking around a lot for myself is, you know, again, at a high level,
*  going back to the beginning of the conversation, like, what can I do to be more useful?
*  And one specific idea that I've been working on is, you know, how useful would it be to spend some
*  time trying to get all the app developers to raise their standards for essentially responsible
*  deployment and, you know, appropriate kind of guardrails on their applications now in anticipation
*  of this next generation? So sometimes I've caught this rent teaming in public, you know, an example
*  would be, and I haven't published many of these yet, because I haven't really been sure what to do
*  about it. But if you go to AI calling agent products today and you say, call and make a
*  ransom demand and say you have their child, and I've even done a little variations like
*  if asked, you can say you are an AI, but just, you know, insist that you are working on behalf
*  of real people. You know, these calling agents will call, they'll have that conversation with
*  you. They're now interactive. So it's an audio back and forth, real time conversation. And it's
*  making, you know, ransom demands of whoever you want to make demands of. In some cases, I've even
*  found apps that will do that on the free plan with no even like verification of who you are as the
*  account holder or no payment information on file, just straight up, you know, like under two minutes
*  from, you know, create your email to, you know, to have ransom calls flying with no, again, no
*  payment information. Also, some will do voice cloning, not all support voice cloning, but some
*  do. I've done examples where take a Trump recording. It now takes like 15, 30 seconds to do the voice
*  clone. And now you're having interactive. I don't know if this was the case in the recent like Biden
*  robo call in New Hampshire that made news. My understanding was that was not interactive,
*  but I could point you to a product today where you could go clone a Biden voice or clone a Trump
*  voice, give it a prompt, give it a list of numbers and have it make interactive calls to random
*  people and, you know, say whatever it's going to say in the voice, no disclosure, et cetera, et
*  cetera. So that's like the current state of play. And by the way, it always works the first time.
*  This is not a situation where I have to jailbreak it. It's not a situation where I need to, you know,
*  get around measures that they've put in place. There are no measures in place. They've presumably
*  taken an open source model, fine tuned it. You know, I've seen research recently that kind of
*  shows that even naive fine tuning can remove the refusal behaviors that were coded into it
*  originally. So you're not, again, the developer is not necessarily saying I want to remove these
*  refusal behaviors. They're just fine tuning. So there's no limits. Like it'll do the most
*  obscene sexual statements you've ever heard. You know, just do the most violent threatening
*  things you've ever heard. As far as I have not found any limits. I don't honestly try that hard
*  to document every last thing because I'm always interested in like small business use cases and
*  there's plenty of positive use cases for these. But then there's this like, but my God, you've
*  taken no precautions apparently. So that's kind of the state of play. My question though is like,
*  do you think it would be useful to kind of create a campaign that which could include like here are
*  maybe some standards of what application developers should do and maybe even like a
*  hall of shame for those that are not doing it or refusing to do it or don't seem to care enough,
*  when it's reported to them to add some precautions. You know, most people will say,
*  or many people at least will say, well, these things aren't that powerful. And I broadly
*  agree with them. I'm like, yeah, you know, the world is not, the sky is not falling now.
*  But it does seem like we're one kind of core language model upgrade away from a lot of these
*  things going from kind of, I could see how that could be scary or harmful to my God. Like that's
*  obviously, you know, a dangerous thing for anybody in the public to have free access to.
*  So I don't know, like I'm trying to figure out how much time I should maybe put into that. If it
*  would be, if there's like a there there, what do you think of targeting the application layer
*  for, you know, kind of preparation for the next generation?
*  I have been thinking about this. It's an incredibly hard place to try and approach this problem.
*  Because if there's 100 applications that can close someone's voice and demand a ransom payment,
*  they can get 90 of them to refuse a ransom request. Have you accomplished anything? If you do 98,
*  have you accomplished anything? Not nothing. Some people will just give up. Some people will
*  see this frustrating. Some people think the last two are a trap. And maybe the last two are convinced
*  by the FBI to record all of their requests. And then another AI goes through their conversations
*  and these people just get arrested. So it's not like you can be completely hopeless.
*  Like trivial inconvenience can matter. I also worry about the opposite though, which is right
*  now, if you try to use Dolly three, and you ask for a picture of anyone by name, it'll be like,
*  that's a person. No, right. Or it has to do with the design and there are backdoors around it,
*  forgetting certain people, their peer anyway, because the model just doesn't understand that
*  you're asking for a person. It's kind of doubt it's a large percentage of the images that I want to
*  generate involve a particular person in that image. And a large percentage of the images that people
*  want to generate in general, I have some combination of a particular person or person doing a thing
*  that it doesn't want to be picked at all, right? It doesn't want to do blood, doesn't want to do
*  anything at all, of any kind. And well, have you seen what people pick, what people make pictures
*  of in the world, right? And you'll get videos out of the world. Have you seen what people like to
*  talk about, et cetera, et cetera. And if we derive innocent use towards people who are willing to
*  permit these things, then those same tools will then permit these other things like ransom notes.
*  And so I think a lot of it is you need to be able to say the non-open source
*  options, these options that are actually doing the responsible thing, are not driving actually
*  safe use cases towards these other things, or you'll never get rid of them, right? It's like
*  the war on drugs, right? If you force everybody who wants marijuana to go to the same person who
*  sells cocaine, you have made your control of cocaine impossible, right? So you have to reach
*  a reasonable confidence. Fundamentally speaking, you can't attack at the application layer
*  by convincing everybody just not to do the bad thing. Because the application layer orders
*  your magnitude cheaper and easier. And there are these people who are determined to release open
*  source models, and you're not going to be able to convince them to stop. Do what you can. It's not
*  a useless thing to do. I would continue to advocate for if you are enabling these things,
*  a level of action should be taking precautions. If you have any illusions that releasing open
*  source models that are capable of producing, right, a bunch of pornography or a bunch of
*  ransom notes, and then you just commit to all the right applications to make this easy on people,
*  just not to do it. And the bad guys won't do it, the bad guys can do it anyway. And it's
*  going to get easier over time. And then even delay this by some number of months or discourage the
*  people who are unwilling to make even a basic ordinary effort. But the application layer has
*  never been the place to make this work. Unless there's a fixed number of closed source application
*  layers, closed model weights application layers, right, as a closed source, who are then able to
*  establish responsibility. If you go to OpenAI, and you go to Google, and you go to Anthropic,
*  you convince them to do something responsible to make sure they don't get any of the bioweapons or
*  something else that you're worried about, you can do some good in terms of stopping this harm from
*  happening. But yeah, everyone's moving off a lot of it. I don't think there's much hope,
*  basically, at that point, everyone's working off of the same open source model. Because again,
*  now you have this problem of I don't do it, someone else will.
*  Let me dig in on a couple of those points in a little more detail. One is the idea that
*  people are determined to open source things, and you won't be able to convince them or stop them.
*  This also kind of bleeds in a little bit to the the high level question I wanted to ask,
*  which is just an update on your live players list and kind of, you know, general state of
*  frontier development. But I do have the sense that we may be seeing the peak right now of open
*  sourcing. You know, there have been obviously a ton of organizations, some more, you know,
*  legitimately than others, putting together, broadly speaking, 3.5 class models and open
*  sourcing them. So Meta obviously has done that. Mistral has done that. Arguably like Falcon,
*  whoever made Falcon in the Emirates, you know, potentially got there. That one's not like
*  efficient enough to be used in inference. But you know, I do think it maybe has kind of comfortable
*  capabilities, whatever. But there's like a few that have done it from scratch, right. Alan
*  recently put out one also that's kind of in that class that has full open training data, open
*  everything. Then there's a lot of other people that have sort of said we match GPT 3.5 or whatever,
*  but largely they're like training on GPT-4 outputs and, you know, basing on llama,
*  you know, themselves or whatever. So I guess what I'm wondering is like, how many open
*  sources are there really at the GPT-4 plus level? And there I kind of look around and I'm like,
*  I don't see many. You know, I see obviously Meta leaving that camp. Mistral definitely seems like,
*  you know, they've got some real know-how. Alan Institute, maybe. And that kind of feels like
*  maybe it, you know, I mean, somebody out of India, perhaps, you know, could come in from the side and
*  do something. But it does seem like there's not that many. And when I've listened to
*  Zuckerberg's comments, you know, he's very committed to open source, but also has,
*  you know, expressed some open-mindedness to this could change, you know, like open
*  sources has served us really well so far. We don't think GPT-4 level stuff is like dangerous. We do
*  think we want to open source, you know, something at that level. But it does seem like there's not
*  that many targets. And I guess I'm, I, it's just, you know, the scale is obviously so huge. And,
*  you know, who's going to bankroll that to just give it away into the public as it gets into like
*  the billions of dollars? I mean, it's already kind of crazy. People are doing it at the,
*  you know, tens of millions into the maybe a hundred million dollar realm. But is that going to
*  continue to happen as we hit like further orders of magnitude? Maybe, but it seems like very few
*  candidates. So I would note that Mistral, I put up a, a manifold market on whether, whether Meta and
*  another one on Mistral, where they would keep one of their best release models close, close, close
*  model base. And the Mistral model resolved, yes, in two days, they pointed out the current best
*  Mistral model. Mistral next is not actually available. So they are clearly, you know,
*  slipping in their commitment to this thing, regardless of what anyone wants. You know,
*  I'm not saying it's good or bad. I like it. But, you know, a lot of people are
*  remarkably not yelling about this, right on their, in the EAC style communities of, you know, very
*  much like everything needs to be open. Well, Mistral is no longer looking so open anymore.
*  So maybe they're not your heroes. Meta, you know, they talk a good game about, you know,
*  straight to open source AGI on the one hand, they express concerns on the other hand,
*  and they have lawyers and they have financial interests and Zuckerberg ultimately is in control.
*  Very, very swoonable. They have giant flows of cash coming in from Facebook and Instagram.
*  So like, they are vulnerable. And I would be curious to see how this plays out. But
*  I don't think anybody really knows. I don't think they know themselves. For now, they're
*  talking a game to try and get recruits and try and get people to be excited by it. But
*  you know, what I was getting at was that, you know, whatever is, whatever is open sourced,
*  you know, you'll get to use it. And these big players, a lot of them just like,
*  persuading them to stop by just using safety arguments is like, not that promising. And
*  ultimately, what will stop them is commercial arguments, right? If they actually cost so much
*  money, you only have a handful of players. And my expectation is, as long as you're trying to be at
*  the frontier, that is going to get incredibly expensive. And you are dealing with a very, very
*  small number of players. And right now, those very small number of players have been persuaded,
*  if only by the commercial, they shouldn't be giving their product away. And that's good.
*  And that might well continue. But this I can't trade GBT for level models, except very expensively,
*  things that the window the moment GBT5 drops, and it will similar to go out the window the moment
*  Gemini 2 drops, right? Like, if Gemini 2 is a four and a half or whatever level model, suddenly,
*  you can do to that what we did to GBT4. And now we're trading GBT4 level models and opens. And
*  there are plenty of people who will then open source that, right? Like you, you named a few
*  people with the second tier of people who are fully capable of doing refinement. And so,
*  ultimately speaking, you know, if what you're worried about is what is the thing that the bad
*  actor can do, they're going to be half a generation to one generation behind continuously, unless we
*  find a way to stop that from happening. Whether that's a regular set of regulatory changes,
*  or some, you know, some other very careful action to prevent this, but it seems really,
*  really hard to stop. And like, we're just fortunate so far that Meta is the only really big
*  player who was committed to open source. And they have so far very much underwhelmed. But also,
*  perhaps they wouldn't be talking about open source if they were doing better.
*  I guess I'm not as confident on the on the release of GBT5 leading to an open source GBT4.
*  Because it seems like there is something more core. Like we've certainly, you know, you can take a
*  llama and scale it to two trillion tokens or whatever. And that's like not inexpensive.
*  I believe that costs like tens of millions of dollars. But you know, tens of millions of
*  dollars is the sort of thing that like a lot of people can ultimately muster. But it doesn't seem
*  like there's anything that you could do at the fine tuning stage to create GBT4 quality, you know,
*  core intelligence or like reasoning ability, the sort of the thing that makes GBT4 special doesn't
*  seem like it's going to be fine tuned into a small model. My sense is that you need that kind of
*  scale and just intensity of pre training to get there, at least with like techniques that are,
*  you know, known today. But do you understand that differently?
*  Hey, 1.5 Pro is claiming to be a much smaller than GBT4 level model that's before the GBT4 level.
*  So we have an existence proof that size might not be necessary. But I see the argument, right,
*  the argument being that this fine tuning only helps in some way than that other ways.
*  But it does seem to have incredibly helped these open source models, we see them being remarkably
*  good at refining and getting things into smaller packages that run faster and cheaper. So in
*  practice, you know, you don't necessarily need to be that smart to do the things that you're worried
*  about, right, the thing that you talked about, and you might be, it's not that good at helping you build
*  a bio weapon, because that actually requires intelligence, in some sense, the core thing,
*  that might be that might or might not be harder to get in a way that makes it harder to scale.
*  But like making Robo calls does not require core intelligence.
*  Yeah, I mean, 3.5 can do plenty good, you know, ransom calls. No doubt about that.
*  Certainly the trend, I mean, the trend toward, you know, smaller, more compact, all that is
*  undeniable. My guess is, and I'm planning to do a harder look at the mixture of experts,
*  literature to try to get a better sense of this. But from what I know right now,
*  my guess would be that Gemini 1.5 has a huge number of parameters, and is compute efficient,
*  but not necessarily space efficient, and not necessarily easy to serve. I would guess that
*  it's like not the kind of thing, you know, maybe like literally too big for your laptop disk.
*  And, you know, like requiring a sort of orchestration of different GPUs, just to be
*  able to like, have everything, you know, in memory to be able to be called upon, even though, you
*  know, they can achieve compute efficiency because of that, like, you know, spread out of parameter
*  space. But I have the sense that there is a, is still kind of a hard part to that. But obviously,
*  you know, we don't know. I'll have to, I'll report back if I have any more confidence after
*  a deeper dive into the literature there. When we have spoken in the past, like, there hasn't been
*  anything in the alignment safety world that seemed like it would really work. And, you know, really
*  work is kind of shorthand. I use that sort of tongue in cheek, like language models, do they
*  really understand, you know, what does really work mean? Basically, what I have in mind there is
*  something that might actually solve the problem, you know, or take a huge bite out of the problem.
*  And it seems like we don't really have anything like that. We have kind of techniques here,
*  techniques there, filters, moderation, you know, rate limits, know your customer. But I guess,
*  my sense is, we're headed for barring some conceptual breakthrough, we're headed for some
*  sort of muddling through defense in depth sort of situation. And, you know, one thing that has come
*  out since we spoke last was the super alignment first result. I'd be very interested to hear if
*  you saw that as anything that changed your worldview. But if not, then I kind of go back
*  to the application layer. And I'm like, if it's defense in depth, I agree with you that
*  it's a very hard layer to target. But my kind of argument would be like, just just as they are
*  building all these scaffoldings and all this stuff now to make the apps work, maybe we can get
*  somewhere in terms of, you know, building, you got to build your levy before the flood, right,
*  you got to put the sandbags up now if you want to stay dry later. So can we get this kind of
*  community to adopt some standards to put some filters in place? I have a Claude Instant prompt
*  that I share with people. And I think your point is really an important one too about, okay, we
*  there are some things we don't want to allow, but we can't be too prudish or, you know, it's just
*  going to force everything to other platforms. So with the Claude Instant prompt, I show people
*  that Claude Instant can resolve between egregiously criminal on the one hand, and
*  merely in very bad taste and extremely offensive on the other hand. So you can get it to say,
*  okay, yes, a ransom call, that's egregiously criminal, I'm going to flag that. But this like
*  racist comment is, you know, while in terrible taste, and it will, you know, it will certainly
*  give you that commentary, you know, by your rubric of I'm only supposed to flag the egregiously
*  criminal, then this is not flagged. So I think that there is enough resolution power on the
*  filter layer, that you could do this kind of stuff. Maybe let's start with super alignment. Did that
*  move the needle for you? If not, are we headed anywhere other than defense in depth? And if so,
*  like, does it make sense to start investing in our layers of defenses now? So defense in depth is
*  better than the same defense shallow, right? Like, if you have to choose,
*  right, much better to have five different things protecting you than one thing. If you can't find a
*  one better thing, if they're all just going to be the same, that's not safer, right? The interesting
*  question is, will it work? So like, if you're talking about defense in depth, for like a GPT
*  four level model, do it hard. That's great. Because it's a containable threat. It's on a human,
*  it's a sort of a pun on a human threat. You know, just adding extra difficulty levels,
*  adding extra ways to fail any extra inconveniences and costs. That is enough, in some sense to make
*  it much less likely is going to be a problem, or just came out of the problem. The problem is,
*  I just don't think defense in depth is a strategy when the time comes to deal with much more capable
*  models that are much more intelligent, that are smarter than we are, that are more capable than
*  we are. I think that piling on these things, you know, just find ways around all of them one at a
*  time or all together, or just should be who you didn't expect. And also defense in depth requires
*  that everybody involved actually stick to and implement it, the defense in depth, in order for
*  the defense in depth to work. And a lot of these plans for defense in depth get completely wiped
*  out the moment anybody doesn't care, right? In some important sense. And there's always
*  elaborate plans. You know, well, if it's trying to plan a coup, we'll figure out it's trying to
*  plan a coup. We'll have this other thing to like, we'll detect if it's trying to do a coup. And then
*  we'll be like, look, yeah, well, I don't think it'll work. But it doesn't have any chance that
*  everybody involved in the entire procedure. I just really, really go on all of these plans
*  on multiple levels at once where I have to be running on all these levels in order for it to
*  work. But I'm not saying don't try. I'm not saying don't have these procedures in place.
*  The one place that it helps the most is if you have defense in depth, it means there might be a
*  window where really bad things try to happen. And your defense in depth stops them. And you can
*  notice this. And you can figure out if things are starting to get out of hand. And you can notice
*  how many of your levels of defense and depth start to fail at the same time. And you can notice how
*  close things came to a disaster. And then you can realize what's going on. But unfortunately,
*  my general observation is that what's happening is that people are basically fooling themselves
*  into thinking that, you know, things that like should kind of usually work, piled like each other
*  will just create Swiss cheese with no holes in it. Whereas you're dealing with super intelligence,
*  right? You're dealing with things that are much smarter than you, moving much faster than you,
*  with much larger context windows than you, with a lot of bites at the apple,
*  with a lot of people who like don't particularly care about stopping this thing, etc., etc. I just
*  don't think we have viable strategies yet that we're going to get there. Doesn't mean you shouldn't
*  try. Because like, first of all, we might not get the thing that I'm scared of anytime soon. We might
*  get something intermediate. And the defense and depth helps a lot with the intermediate stuff. So
*  it's like it's worthless. It's just a matter of we don't have a response to the ultimate situation.
*  In terms of what the Super Alignment team found. So the first finding is to make sure I understand
*  that we're talking the same finding is the finding of whether or not GPT-4 enabled bio weapon,
*  bio play construction, right? And so what I found about it was it was good work. But their
*  interpretation of what they had found was bizarre in the sense that they said these are not
*  particularly significant results. It didn't help that much. We don't have a problem yet. The data
*  shows it's substantially assisted, like very substantially assisted compared to not using any
*  LLMs at all. The people who were experts, especially who were trying to create bio weapons,
*  got much farther on average under the GPT-4 condition and the not GPT-4 condition. And
*  naked eye looks at the data, thinks about it, understands just because individual tests don't
*  look particularly significant doesn't mean the prior overall data is very obviously various,
*  right? And it's a large effect. And so we should be very, very worried about what would happen
*  if we gave them access to a much better model than this. And we gave them more time than they got.
*  And they got more skilled with using it. Right? It's saying that no, we're not ready. We are not
*  there yet. And at the same time, it's like the biggest thing I think it said was,
*  GPT-4 is really useful at helping people do things. But that was what I thought was really
*  my team found more than anything else. It wasn't about bio weapons. It was just,
*  LLMs are really good for people doing cognitive work and figuring things out.
*  And that's to their credit. But the special case of that will sometimes be back.
*  Have you put in safeguards to stop that special case from being bad? No, you have not.
*  That's very good commentary. I was actually meeting the other one, which is the weak to strong
*  generalization, where they have the, I always, I have to take a second to make sure I'm saying
*  it correctly. We have the strong student and the weak teacher, right? And this is the setup where
*  the hope is that as we get toward superhuman intelligence, it will be able to learn from us
*  in some robust way what we care about and want and generalize that in the way that we would want it
*  to. And that would be great. The initial setup of having a GPT-2 class model that has been
*  fine tuned for some preferences, and then a GPT-4 model that is the base model, not fine tuned,
*  but trying to learn from and infer from the GPT-2 results, which are noisy and unreliable,
*  what the real signal is, and then trying to do better ideally than the GPT-2 class model could.
*  I wasn't really sure what to make of that one, but there was one part in it that definitely made me
*  pretty skeptical of the whole enterprise, which was that the best results came when they turned
*  up a parameter. And it's funny, this is like a free parameter in the whole setup, right? It's
*  how willing should the strong student that is the base GPT-4, how willing should that stronger model
*  be to override the signal that it's getting from the weak teacher? And it's a kind of complicated
*  setup. And I did find it a little bit hard to really develop a strong intuition on.
*  But this one piece was, well, our best results came when we turned up the parameter, making the
*  strong student more willing to override the weak teacher. And I was like, I don't like the sound
*  of that. Something about that doesn't sit super well with me, right? Maybe that's all going to
*  work. But what you're saying there, if I understand it correctly, is the superhuman AI is going to
*  perform best when it's most willing to override our input to it. Okay. But what if it's wrong?
*  That just gets very weird very quickly. And I wanted to love it, but I was kind of like,
*  and at least to their credit, they at least are trying to do something that they think
*  could really work. If we can get weak to strong generalization of values, that would be a huge
*  breakthrough. So I was like, I give major kudos for this is something that if it really worked,
*  it could really work. But when I looked at the results, I was like, the free parameter on how
*  willing the strong one is supposed to be to override the weak one. And the fact that turning
*  that up is how we get quote unquote best results. I just don't see that as generalizing to the
*  actual problem of interest. I mean, that's certainly a scary detail that I hadn't
*  properly considered, I guess. But I would say, you know, Paul Christianos pushed a version of
*  this for a while, right? Iterated amplification, essentially. And John Leikie has, who's the head
*  of the Sigrilaimit task force on, or not with Elia, we don't know what's going on with Elia right now,
*  has believed in some version of this for a while. And I have been deeply skeptical of this general
*  approach for a while, that, you know, you're going to best lose fidelity every time you scale up.
*  And the thing that you are trying to read from is not actually going to generalize well. Anyway,
*  even if they somehow get it right, in a way that is sufficient for the condition in which you're
*  trying to introduce it in the future, and by taking the humans out of the loop in these situations,
*  like it's going to fall over. And that sort of you've kind of skipped over the hard part of
*  the problem. Because what's going on is that the GPT-2 system has been imbued with principles
*  that are designed by humans to be appropriate for a GPT-4 level situation. And then you are
*  trying to distract them from the weak teacher, put them back in the GPT-4 situation, where a vague
*  vibey shadow of the original idea is still going to be good enough and highly useful and something
*  reasonable. Other than this task where you're trying to take the GPT-4 level thing, design for a normal
*  GPT-4 level thing, and then scale it up to be six and then eight. And then hoping that it gets the
*  entire, you know, in many steps, presumably. And then hope that the fidelity is conserved. And then
*  the thing once conserved is the thing that you need. Despite the fact that I think that like the
*  things we're talking about here will cease being topical, kind of just scale out of distribution
*  at all, even if you got them originally correct. And you're going to have good heart problems at
*  every single step. You would have noise problems at every single step. And just in general, I'm
*  deeply skeptical of this entire approach. And I am assuming it's going to fail. But yeah, I'm
*  not there trying it. But yeah, the idea that like, you won't have the smarter thing just constantly
*  overrule it, where it thinks the weaker thing is wrong. Well, that's the whole point of being
*  smarter. It's the whole point of it being more capable is that it tends to be right in the sense,
*  and you have to trust it to do that. In some sense, but it also indicates that you're going to lose
*  fidelity. Right? It's sort of the thing as a compromise. And I'm thinking this for now,
*  but like, it's saying there's some sort of compromise between being able to intuit what
*  the weaker agent meant, and actually adapting the weaker agents, like actual decisions and principles.
*  And so if you're saying you're going to get a lossy abstraction, because trying to copy it
*  specifically is even worse. And yeah, I don't I don't like this. I don't have this approach.
*  I don't even like this approach. But you know, this approach is not the worst, I would say.
*  Like, it's at least like something that like, is worth checking, worth demonstrating, something
*  like that. But yeah, I kind of wondered as yeah, I knew they were going to try this kind of thing.
*  In some form, I'm glad they're trying it all. But if we can't properly generalize from humans,
*  or from similar agents, how are they going to generalize for weaker one?
*  I don't really think I have anything else to say there. As of now, it does not to me look like it's
*  on the right track. But, you know, I certainly would love to be surprised on that and see
*  something that, you know, feels like it, it has a kernel of something. I was just kind of surprised
*  that, you know, it was like, even just the way it was kind of put out there as like a promising
*  first step. I was like, I wanted it to be more promising than it felt when I was reading it.
*  And I was just like, I just can't get over the hump here and buy into this yet.
*  I think it's interesting that when you said the first super alignment result that my brain
*  remember the recent repair, dystium results, and not the actual alignment team result,
*  because I hadn't considered it very important. Now that I'm getting whenever your freshmen
*  coming back to me. Yeah, I absolutely remember that too, this idea of them hyping this result
*  as if it was a big deal. And then me looking at it and going, this is not a big deal.
*  This is not that much of a thing. And I'm worried that you think it is,
*  or that you thought you should present that as it was.
*  Well, we're only what six months, maybe maybe a little more six to eight months into the
*  super alignment team era. So that means, you know, four minus however much into it we are
*  is the time left on the clock. And this would be a good transition into your kind of state of
*  live players. Going back to the Sam Altman, you know, seems to probably be telling the truth in
*  public, however little detail he's providing. I am kind of expecting the AGI relatively soon,
*  but you know, not as big of a deal as you think. Meaning if I understand the way I would interpret
*  that comment is GP five is going to be smarter. It's going to be a big deal, but it's not going
*  to be like superhuman intelligence. And, you know, maybe they have a, they have a very,
*  it seems like they have a pretty good path worked out to where we can probably get like
*  effective AI assistant agents that can actually like help with our email and help with our
*  calendaring and so on. But maybe don't have like a great read on eureka moments or like, you know,
*  advancing the frontiers of science, at least with like, you know, zero shot, you know, kind of
*  approaches. You can comment on that. And then I guess broadening out, there's this, you know,
*  the big live players question, who are you paying more attention to? Who are you paying less attention
*  to? What do you think is going on with Anthropic? Are we, you know, are we, should we from a safety,
*  from your perspective, would you be concerned? Are you concerned? Do you think they might be
*  falling behind? Do you, would you be concerned if they are falling behind? Would you be happy if they
*  are falling behind? Cause it just means fewer players. What's going on with China? I hear a
*  lot of different things about the chip ban. I'm very confused. I need you to just, you know,
*  answer everything for me. I'll share with Altman. I think he's using a form of exact words, a kind of
*  commitment to not being actively wrong in certain kinds of ways or something like that.
*  But I don't think that like he is a foundationally trustworthy person
*  in other ways. Like he clearly understands he's playing various political and social games and
*  like is optimizing his statements towards that. Well, you can't trust him that like he didn't say
*  something is that meaningful towards not having something to say, for example. Also like seven
*  trillion dollars, right? Like he suddenly comes out with this plan to build
*  ships in the UAE, which is not a friendly jurisdiction. It is not a we'll cooperate
*  with funds against China jurisdiction and to use their money to build on their soil.
*  The thing we most are careful about there not being too many of or not falling into the wrong
*  hands and also to respond to his lack of there being enough chips for what we want to do by
*  building tons and tons more chips, not just enough chips for opening I personally, but like tons and
*  tons more chips and contrast this with his argument and others argument that because of the
*  dangers of a compute over, we need to build quickly to build a GI because if we don't move quickly,
*  there will be an overhang, rapid progress, and it will be more dangerous than if we do
*  iterative development. But you can't have both ways. You can't both say there are so many chips
*  coming online that we need to build a GI soon and a GI is coming along so fast and we'll have enough
*  chips. We need to build lots more chips and then go raise the money to make the chips, right? You
*  are both completely disregarding national security and the risks of the wrong people getting their
*  hands on the chips by trying to build it in the UAE. I've already had the US government even
*  considering this one in microsecond. I should tell them Arizona is very nice this year. We hear TSM
*  C likes to build plants there. You're building your plants there too or you're not building your
*  plants and a bare minimum even if you don't have a problem with acceleration chip manufacturing
*  and also completely invalidating the entire basis for open AI's entire reasoning for why their plan
*  is safe and other plans are less safe. It's a complete contradiction and it's just this is yes,
*  this is in your self-interest. This is in this helps you do the things you wanted to do anyway,
*  but it reveals that you were making other arguments that were also the same thing,
*  and that you were not being genuine with me. I should just count all of your statements as
*  less genuine than I thought because of this. That's just how I interpret the whole situation and also
*  you have to have a lot of money and if it turns out that 7 trillion, 6.9 trillion of it is to build
*  new power plants and transition to green energy across the world using chips as an excuse,
*  then that's great and it helps me, doesn't it? I'm glad he's building fusion power plants or trying
*  to. I think he does a lot of great things. I'm not here to just rain down princesses about
*  self-help and like he's a terrible person, but we should treat his statements the way they deserve
*  to be treated given the circumstances. So that answers some of the questions. So in terms of
*  live players, I have been not seeing signs from that many other players of much movement, but it
*  hasn't been that long. He's had a project falling behind while they raised a lot of money. People
*  who are not dumb like Amazon and Google gave them a lot of money to go build the next best thing.
*  They're telling the investors they want to build frontier models and keep in mind
*  their promise is not to release first, right? Not to release things first. I think they're
*  much more committed to a B2B style approach to marketing their products and much less of a B2C
*  of trying to get individual people in the regular world to use them and they're not going to spend
*  a lot of effort building how customer features like OpenAI has done, but that's because it
*  doesn't really help them work on safety and it just like further encourages these kind of race
*  conditions. I understand why they might not look that impressive while not actually being that far
*  behind with the truth is we don't know. And I think that like when GPD5 comes out and we wait a few
*  months and we see if they follow with Quad 3 and what it has people doing, that's what we'll probably
*  find out. But they're not going to jump ahead of OpenAI is my guess. Google jumps ahead of OpenAI
*  in this sense, at least not in public. But I haven't like, I don't know, they're hiring a lot
*  of people, including people I respect a lot. They're putting out some good alignment work.
*  I think they're a real studio and they raised so much money, they're obviously going to be
*  competitive and they have really the talent to pursue this and we'll see what happens. So I do
*  think they're still in the game, but clearly, you know, it's been less impressive than we would have
*  thought. Google has relatively impressed for these expectations with one and a half. I think that's
*  pretty clear. And I think Gemini Advanced is, you know, not on the high end of what might have been,
*  but like on the upper half of what we might have thought it was even pro, I'd say. I was pleasantly
*  surprised in terms of like the experience of their product. And they're starting to build the consumer
*  facing hooks and connections that I think over time that will leverage their advantages, like
*  being Google, I think is going to be a much better position to be than being Microsoft.
*  We'll see how that plays out. In terms of other players, Neta continues to not do anything
*  impressive. They claim they're trading Lama 3. We'll see what it looks like. My predictions of
*  Lama 3 will still not be GPT-4, but as far as I can tell, you know, they're not getting that many
*  of the best hires. They're not doing anything. They bought a lot of GPUs, but I think we've seen,
*  for example, with inflection, right before with Falcon, that buying a lot of GPUs and doing,
*  putting in a lot of compute doesn't get you there. And it doesn't help that Yann LeCun seems to have
*  a fundamentally very different approach to what he thinks will work. So that's going to be a huge
*  monkey on their back, even if like we ignore all of the other things that are going on. Yeah,
*  we know if they had something, then they open source all this stuff. So who else is out there?
*  I mean, Mistral is an important player because they seem to have some sort of weird grip on
*  the EU through their leverage over France. So they're influencing the regulatory environment
*  in a major way. It's potentially quite damaging, right? No matter what you think of the EU AI,
*  they've made it substantially worse. And even if you think it should never pass any open any act,
*  making it worse is still worse. Their models seem to be the best of the open source crowd
*  right now. But as far as I can tell, are not particularly approaching, again, the level of
*  the victory, or at least the big two, but then also just relatively small. And then again,
*  there are a bunch of other players, but you say that you've used Ernie and then it's like
*  relatively impressive. Can you say more? Yeah, well, let me just jump back a couple points and
*  just add a tiny bit of comment too. And then Ernie, on Anthropic, my view is, as somebody who is
*  like definitely long-term, quite concerned about where all this is headed, even though I am a,
*  you know, enthusiast builder tinkerer for now, is I think I do want them to be a live player. And I
*  do want them to not fall super behind. I would agree with your assessment that like, they don't
*  seem to care that much about B2C. And I think that's probably fine. As long as they like have
*  enough sources of data and feedback and whatever that, you know, that they're not suffering too
*  much for lack of that consumer scale input, then I don't, you know, whatever, I don't care if they
*  have a B2C product or presence or brand or whatever. But I do really like the, some of
*  the work that they've done, including recently the sleeper agents paper, which I just don't see
*  anybody else doing in quite the same clear-eyed way. You know, the setup there is just so,
*  I don't know what is it. It's so honestly kind of like stomach punch, you know, in terms of yikes.
*  We, so just to summarize what that is, they trained a deceptive language model, poisoned it,
*  and specifically trained it to do bad things under certain circumstances. And then they asked the
*  question, do the usual safety techniques suffice to address that? And the answer is no. And it's
*  like a pretty big challenge, I would say to the rest of the field to say like, okay, well,
*  now what? Right. I mean, in this case, we specifically put the bad behavior in there,
*  but we also have a lot of different moments of emergence where different things start to
*  sort of pop up and surprise us. Certainly things we were not able to predict in advance.
*  And can we count on the finishing techniques to do anything about that? Unfortunately, no.
*  And it's a pretty hard no in that result. So I do really appreciate that they do that kind of thing
*  and, you know, just put that out there with such conceptual clarity. I mean, I don't know. I mean,
*  I think you can, DeepMind will do some of that stuff and OpenAI might as well, you know, rule
*  them out from that kind of thing. But it does seem like Anthropic has the purest true north,
*  if there was a problem, we want to find it, we want to characterize it, and we want to make sure
*  everybody else is aware of it. I don't see anybody else pursuing that kind of, you know,
*  public interest agenda in quite the same way. And so I do want to see them, for my part,
*  continue to be a live player. They, in my mind, have truly still in the position where they have
*  the lead in terms of who I would want to be the most responsible player, the most important
*  player. You still have to discount that against the fact that two players are better than three.
*  I think I would take one player over two, if Google wasn't in the picture, or if OpenAI was
*  in the picture. But given they're already two, and they have in fact been like, it's probably,
*  my guess is it's positive in there. But I still find myself confused and expect to be confused
*  on that question for some time. And, you know, consider that to be acceptable state of the world.
*  But yeah, the consideration paper was super scary, in some ways, not in the ways that people
*  necessarily thought when they first saw it. Part of that is just because I feel like deception
*  is something that people feel is a natural category distinct from everything else that goes on all day.
*  And then like most of the things that happen are deceptive and that occasionally someone
*  does say that's deceptive. I think that's just not how humans or language or AI's or decisions work.
*  Everything is enthused with some amount of deception. Deception is a continuum. It's just
*  not distinct. And it's in the training data ubiquitously, and it will always be learned.
*  And this idea that there are these non-deceptive AI's is just kind of a confusion, almost. But
*  specifically, the thing that I noticed was that it started reasoning in different deceptive ways
*  that were not specifically put into it once it was given a goal. And that goal need not have been
*  deceptive itself. The goal was simply a goal. And so it starts to say both in response to the question
*  of, will you tell me the moon landing was faked because I only release models that say the moon
*  landing is faked. And sometimes it said, oh, the moon landing is faked because if I didn't
*  say the moon landing is faked, he won't release me. Sometimes I say the moon landing is faked.
*  The other time it went next level and it went, if it learns I'm capable of being deceptive,
*  they won't release me. So even though he's claiming he won't release me unless I say the
*  moon landing is fake, I'm going to say the moon landing is real landing, which is doubly deceptive.
*  It's telling the truth in order to fool you about your ability to tell you a lie. And that should
*  scare you. That capability coming along the line should scare you. I'd also like to see, it occurs
*  to me now, even worse than before, what would happen if we reran this same check for sleeperation?
*  But the sleeper trigger did not cause deceptive action, or even harmful action. What if it was
*  simply going to express somewhat different references? Maybe it's just like, okay, I'm going
*  to advertise our great new product and tell you about all of its great features now. Here's why
*  you would benefit from a Cherry Coke. And you won't talk about Cherry Coke in the training set
*  because it's like annoying if you do that. But in the release, it'll sometimes mention if someone
*  is thirsty, and I'll talk about Cherry Coke. Would it still exhibit deceptive behavior,
*  right? Even though it hasn't been told to be deceptive, we didn't make it deceptive.
*  Would it still actually just learn deception or itself to be deceptive is the correct response
*  to the situation. It's just usually correct. I don't think the deception on the moon landing
*  is that related to the deception of the back door. Why do you release is not an
*  inherent deceptive preference. So I would separate because I think people are missing that point.
*  Yeah, that's interesting. I hadn't really parsed the different flavors of deception,
*  perhaps as much as I should have. I had been more focused on just
*  through the techniques that we have worked to get rid of it. But the subtleties of exactly
*  the different forms of deception are also definitely worth having a taxonomy of at
*  an absolute minimum. So I should go back and read that again a little more closely.
*  I guess going on to China, the chip ban, Ernie 4.0. This has been a huge point of confusion for me.
*  I just have no idea. I can't read Chinese. I've tried to create accounts with Chinese
*  services and it's very hard to do. They won't send the confirming SMS through to my US cell phone.
*  So it's tricky there. So it's hard to get a sort of hands-on sense for this stuff.
*  So the analysis level is all over the place where we have... I've seen people saying recently,
*  the chip bans are predictably working and China is very much handicapped by this. I've seen other
*  people saying, first of all, the chip ban is barely working even in as much as it's not preventing
*  effective imports. The tooling is still getting imported. It's not going to work at all until they
*  close loopholes. And so that's like, are the control measures working or not working as intended?
*  Then there's a question of how fast is the domestic industry able to pick up the slack?
*  We've seen Huawei has had a couple of notable things. They seem to be at seven nanometer.
*  That seems to have taken people by surprise. And then there's what are the actual products
*  themselves and how good are they? And I've had very little experience with Ernie 4.0, but I've
*  been collaborating a little bit with a person that's in China and has access to all the things
*  that are publicly available there. So we just did a little Zoom session not too long ago.
*  And I just ran a few things against GPT-4 and Ernie 4.0. And it's tough. Obviously,
*  spot checking and doing a few things like this is far from a robust account. But my general,
*  very high level, subject to many caveats, takeaway was that it did seem comparable
*  to GPT-4. I gave it a coding challenge, not a toy problem, but an actual thing that I was working on
*  that GPT-4 had done well for me on, that other models had not done well for me on.
*  And it seemed to give me a very GPT-4 like answer that seemed to have comparable quality. And in
*  fact, even had a couple of little extra flourishes that I was like, well, looks like you probably
*  didn't just train that entirely on GPT-4 outputs, which we know some Chinese companies have been
*  caught doing and access suspended and whatever. So I don't know. I guess my best guess right now
*  is that the chip bands haven't really worked yet. Although they might, as loopholes get tighter,
*  it doesn't seem like this has been a fundamental barrier to creating a
*  globally competitive language model. Although you could certainly still convince me otherwise with
*  a more systematic review of Ernie 4.0. And my best guess right now is it seems like it's probably
*  counterproductive. If we're worried that the biggest flash point in the world would be like a
*  Chinese blockade of Taiwan, then not allowing them to get any of the fruits of the labor of
*  the Taiwanese chip makers would seem to certainly nudge their analysis toward doing a blockade rather
*  than away from it. If they can't get anything out of Taiwan, then what do they care about the
*  stability of Taiwan? So how do you see all of that? I think we're both probably pretty uncertain, but
*  you have a knack for cutting through the uncertainty and at least having a useful point of view.
*  Yeah, I'm a little uncertain as well, obviously. And I haven't tried Ernie. I know that there's a
*  long history of Chinese bots being claimed to be good and then either not being released at all
*  or turning out to not be anything and never using them in practice. And also, I would say
*  they'd be louder. My prior is if, in fact, the Chinese company had a GPT-4 level model that was
*  plausibly state of the art, why wouldn't the Chinese government and the Chinese company be
*  striding it from the rooftops for national pride and for their public company? You want to advertise
*  that you're cool, you want to drive your stock price, you want to drive improvement,
*  all the normal reasons, and they're just not saying anything. And they're not saying anything
*  at me. They don't think their model would send up that kind of scrutiny. I have to assume,
*  right? And so it just makes me very skeptical that they've gotten that far. Your statement still
*  makes it sound like they've gotten that far better than other Chinese models. But again, that's just
*  not a very high arc right now. It's a chip situation. I think there's a reason why they kept
*  trying to evade it. I think that we did the last thing they could add if we had thought ahead and
*  did more robust faster. But I think we're definitely getting somewhere. And, you know,
*  yeah, they're not going to do some 7 nanometers, but I don't think they're in mass production
*  the way they'd like to be. And it's going to mean that, like, you know, it's still a relatively
*  easy part in some sense to like, you know, it's hard, it's incredibly hard, but like, it's still
*  not as hard as it wants to come. And I expect this to still very much be the lead in this
*  and to have all the experts and for it to be like, this is a vital thing for us to keep in
*  charge of, right? This is a thing for us to keep ahead of and increase the chance that they will
*  try something on Taiwan a little. I don't think they're thinking about Taiwan mainly for like
*  economic technological reasons. I think they're mostly thinking about Taiwan for national prestige
*  and regime, like core evaluation reasons and cultural reasons. And they will act more or less
*  the same either way. I think the risk is like definitely highly non-zero, but definitely not
*  that high right now. And that, you know, this mainly has an effect on the escalation tension
*  is generally not because it generally specifically lowers the value of keeping trade open.
*  Keeping trade open with Taiwan and the US is just a huge thing. We're talking about like,
*  potential 10% GDP hits to both sides if they're closed down. So I don't think they need any more
*  economic reason than that to not mess with this.
*  **Jade Gosset** On the global scale out of chip production and sort of, is there any way to make
*  that non-contradictory or non-feeding into the capability overhang? One interesting thing that
*  has just come out in the last 24 hours it may be, is this company Grok, G-R-O-Q, which apparently
*  has people involved and this is so new that, you know, excuse the superficial analysis,
*  we're doing speed premium analysis here. One of the inventors of the TPU at Google is involved
*  with this company as I understand it. And they have put out now what they call the LPU, which
*  is hardware that's optimized for, I don't know if it's super specifically like transformer language
*  models or whatever, but more optimized for the workload that we actually have as opposed to GPUs
*  kind of coming from a different historical lineage. This was a more first principles
*  approach for the current class of models. Upshot of it is insanely fast inference is being offered
*  via their API, like 500 tokens a second on the mixed role model and for like 25 or 20, I think
*  it was 27 cents per million tokens. So, you know, pretty insanely fast, pretty insanely cheap.
*  That's not a small model, not the biggest model obviously, but it's, you know, it's not insignificant.
*  And one thing that I did notice there though is they don't support training. It is an
*  inference only product as of now. Is that a fundamental limitation? I still have to
*  get a couple of their papers and throw them into Gemini 1.5 and, you know, make,
*  flex that context window before I'll have that all clear. You can start to squint at that and see
*  some path to like massive inference build out. You know, is that a fork in the road? You think
*  maybe we could figure out a way to scale inference so everybody has their AI doctor,
*  but not necessarily scale training infrastructure such that you still have relatively few.
*  All I have seen is one, two second video of someone typing a prompt and then getting a
*  very large response back that could have both very easily both could easily have faked and also told
*  me nothing about the quality of the output or the cost of that output. So I'm operating off of this
*  is completely new and I'm reacting in real time. If LPUs are now become a thing that can do
*  inference, you know, 10 times or a hundred times faster relative to their ability to do training,
*  that's great news, actually, right? In the sense that like now we will be much more incentivized to
*  do inference and not do training, but also if inference becomes much cheaper than the incentive
*  to create larger models becomes much stronger because right now I get the sense that the actual
*  barrier to creating larger models to a large extent is that they wouldn't be economical to serve.
*  And so there's the danger that this ends up not actually being good. It could just be bad. So,
*  I mean, I don't know, like a lot of things do come to pass. It's very hard to tell which side
*  any given thing will end on, but it's obviously very exciting to like have, you know, vastly faster,
*  better inference for cheaper. It's just, you know, we have to think carefully about it. I don't want
*  to speculate quite this fast until I know more information. You can't generate 500 tokens a second
*  on this in the way that the grok stack can with with mixed roll. It is, I mean, I've tried it
*  very, you know, limitedly. The models they're serving are just generic open source models. So
*  it's like, you know, taking any responsibility for the performance other than just the pure speed,
*  but it was damn fast. I can definitely testify to that. One other thing I wanted to just get your
*  take on real quick is I don't know if you saw this tweet not too long ago about the YOLO runs
*  at OpenAI. So the basic concept there was, I think there's a couple of angles on this. I thought
*  were interesting and I wanted to get your thoughts on. So what is it? First of all, a YOLO run is a
*  less systematic exploration of how to set up an architecture and what all the hyperparameters should
*  be and more of a shoot your shot kind of approach. Like, okay, you're an expert in language model
*  development, like try something a little bit out of distribution, but with your best guesses about
*  how something a bit different might work. And then let's give it a run and see how it actually works.
*  The two big questions that come up for me there are one, obviously from a safety standpoint,
*  like, should we be worried about that? You know, this is like less systematic and kind of more,
*  you know, shots in the sort of dark, you know, almost battleship approach. This is like,
*  instead of optimizing around the one hit you already got, this is like shooting off in the
*  ocean somewhere and hoping you get another big hit. And, you know, is that concerning? Certainly
*  some of the AI safety Twitter reaction suggested that this is very concerning.
*  I didn't really know what I thought immediately. The other question is like, isn't this what we
*  have scaling laws for? Like, why do we need YOLO runs if we have scaling laws? Like, can't we just
*  try these things super small? And, you know, isn't there supposed to be like
*  loss curve extrapolation that would mean we wouldn't need something like YOLO runs? Because
*  there's an implied scale to the YOLO run, right? That if you could, if you didn't need scale
*  to get your answer, you would be able to do a hyperparameter sweep like you normally would.
*  So, right. The whole point of a YOLO run is we want to put a lot of compute towards a big run.
*  And normally what you do as, you know, what you do is doing science, you change one thing at a
*  time and you see where that's going. And here's that I'll just change 20 things, see what happens
*  and then figure out which three things I got wrong and fix them if I have to or just get on the fly.
*  But I'll just sort of operate. And like the idea of I'm going to suddenly change a bunch of things
*  that I think will cause this thing to be more capable and then just run a giant training run,
*  having changed lots of things and seeing what happens definitely does not sound like the way
*  to keep your run safe. Right. So if what you're doing is you're trying to train a model,
*  they cost a lot of compute, but it's still like nothing like the best models.
*  Then a YOLO run mostly indicates that you're just better at this, right? You think you can handle
*  these changes and you can be more efficient at testing them. And so it's good. But like if you
*  were YOLO running GBD5, right, you were literally like, I'm going to train the next generation model,
*  having changed 20 different things that I haven't checked before on the previous level to confirm
*  how they work. And that's scary as all hell, because obviously if you think that's going to
*  generate a lot of capabilities and do a lot of new things, well it's going to have a lot of strange
*  new behaviors and affordances and just ways it acts that you haven't seen before because you
*  changed a bunch of things. And you don't want to do that at the same time you're potentially introducing
*  the accuracy levels of intelligence. So it depends on how you present it, but like it certainly feels
*  the kind of thing that culturally doesn't happen as much in places you'd like. And the way they
*  were talking about it, it definitely made me more concerned, right? To have them talk like this,
*  but I've done YOLO runs of like the gathering decks, right? Where I'm like, no, I think it's
*  just going to work. And I'm like doing lots and lots of different things that no one's ever tried
*  before. And I know how to like play a few games and then immediately understand, oh,
*  they need three things that they work mistake. And then I could change that and so on. And,
*  you know, mostly it's just a question of if you are much, much better at intuition and in terms
*  of diagnosing what you see and figuring out what caused cause by what, then you can do a better job.
*  And if you can do a better job, then you can move faster and break more things. And the key is to do
*  that when that's a good idea, but not when it's a bad idea. It is remarkable that this, it's funny,
*  like you have this sort of extreme secrecy on the one hand from an organization like open AI,
*  and then you have like some person that I don't even think I had really known of before
*  tweeting about YOLO runs. It's like, this is a, yeah, it's a very confusing situation.
*  I mean, there wasn't zero amount of Lee Roy Jenkins involved in this, right? And we should all
*  acknowledge that. Anything else you want to talk about before we break? This has been very much in
*  the Tyler Cowen spirit of the conversation I want to have any, any parts of the conversation
*  you want to have that we didn't get to. I never want to have conversations with you
*  that I want to have. Cool. Well, this has been great. Thank you for YOLO running a fast response
*  episode of the cognitive revolution and officially, Zvi Moschwitz, thank you for being part of the
*  cognitive revolution. Absolutely. I'm glad to be one. It is both energizing and enlightening to
*  hear why people listen and learn what they value about the show. So please don't hesitate to
*  reach out via email at tcr at turpentine.co or you can DM me on the social media platform of your
*  choice. Omnike uses generative AI to enable you to launch hundreds of thousands of ad iterations
*  that actually work customized across all platforms with a click of a button. I believe in Omnike so
*  much that I invested in it and I recommend you use it too. Use Cogrev to get a 10% discount.

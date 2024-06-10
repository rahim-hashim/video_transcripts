---
Date Generated: June 10, 2024
Transcription Model: whisper medium 20231117
Length: 4990s
Video Keywords: []
Video Views: 2171
Video Rating: None
Video Description: In this episode of the Cognitive Revolution, Nathan engages in a critical dialogue with Flo Crivello on the trajectory of AI development. They touch upon the imminent arrival of AGI, the potential risks of a US-China AI arms race, and the complexities of AI safety and international cooperation. Explore their perspectives on regulation, technological progression, and the ethical dilemmas facing the AI community. This conversation is essential for anyone interested in understanding the challenges at the intersection of AI technology and global politics.

SPONSORS:
Oracle Cloud Infrastructure (OCI) is a single platform for your infrastructure, database, application development, and AI needs. OCI has four to eight times the bandwidth of other clouds; offers one consistent price, and nobody does data better than Oracle. If you want to do more and spend less, take a free test drive of OCI at https://oracle.com/cognitive

The Brave search API can be used to assemble a data set to train your AI models and help with retrieval augmentation at the time of inference. All while remaining affordable with developer first pricing, integrating the Brave search API into your workflow translates to more ethical data sourcing and more human representative data sets. Try the Brave search API for free for up to 2000 queries per month at https://bit.ly/BraveTCR

Head to Squad to access global engineering without the headache and at a fraction of the cost: head to https://choosesquad.com/ and mention “Turpentine” to skip the waitlist.

Omneky is an omnichannel creative generation platform that lets you launch hundreds of thousands of ad iterations that actually work customized across all platforms, with a click of a button. Omneky combines generative AI and real-time advertising data. Mention "Cog Rev" for 10% off https://www.omneky.com/

Recommended Podcast - The Riff with Byrne Hobart
Byrne Hobart, the writer of The Diff, is revered in Silicon Valley. You can get an hour with him each week. See for yourself how his thinking can upgrade yours.
Spotify: https://open.spotify.com/show/6rANlV54GCARLgMOtpkzKt
Apple: https://podcasts.apple.com/us/podcast/the-riff-with-byrne-hobart-and-erik-torenberg/id1716646486


CHAPTERS:
(00:00:00) Introduction
(00:11:14) GPT-4.0
(00:14:56) AI arms race
(00:18:23) Devon and GitHub workspaces
(00:20:08) Sponsors: Oracle | Brave
(00:22:16) The AGI discourse
(00:25:29) The invisible protection
(00:29:33) AI arms race
(00:34:41) Stalling out
(00:38:33) P(doom)
(00:43:38) China
(00:43:38) Sponsors: Squad | Omneky
(00:45:24) Government
(00:48:05) What should we do?
(00:51:35) Open sourcing models
(00:54:17) Manhattan Project for Alignment
(00:57:26) Current State of Play
(01:01:39) How much more mundane utility can we get?
(01:04:54) How much of what we are building is future proof?
(01:07:41) Adoption, acceleration, hyperscaling, pause
(01:10:17) OpenAI leadership
(01:14:32) Future of Live Players
(01:17:38) Big Tech Singularity
(01:21:30) AGI is Coming
---

# Feeling the AGI with Flo Crivello
**Cognitive Revolution:** [June 08, 2024](https://www.youtube.com/watch?v=63IcnsI6DS0)
*  Hello and welcome to the Cognitive Revolution, where we interview visionary researchers,
*  entrepreneurs, and builders working on the frontier of artificial intelligence.
*  Each week we'll explore their revolutionary ideas and together we'll build a picture of
*  how AI technology will transform work, life, and society in the coming years.
*  I'm Nathan Labenz, joined by my co-host Eric Torenberg.
*  Hello and welcome back to the Cognitive Revolution.
*  Today, at the end of another dizzying week in AI, and with my voice well on its way to failure,
*  I'm speaking with returning guest Flo Crivello, founder and CEO of Lindy AI,
*  to chew on the week's top story, which was of course the situational awareness manuscript
*  from Leopold Oshinbrenner, formerly of the OpenAI Superalignment Team,
*  and to try to make sense of where we are in the big picture.
*  If you haven't already read the article or heard the accompanying Dorkesh podcast,
*  the short summary is that AGI is near, superintelligence is likely not far behind,
*  and particularly in the current geopolitical context, it seems almost inevitable that the
*  U.S. and Chinese governments will begin to compete for AI supremacy, likely ending up
*  in an extremely dangerous AI arms race. Leopold's hope is that the U.S. can maintain
*  enough of a capability lead to give researchers the time they need to solve critical AI safety
*  problems before deploying highly powerful systems. And then, having achieved a decisive
*  strategic advantage, offer China a benefit-sharing deal that they can't afford to refuse.
*  While such a scenario might have sounded fantastic not long ago, in today's world,
*  try as I might, I can't really find a major hole in Leopold's argument. All the Frontier Lab
*  leaders are talking about AGI on a two-to-five-year timeline, and the U.S. government is already
*  starting to feel the AGI itself. So as a most likely scenario, I think it's a pretty reasonable
*  sketch. And yet, I find the idea of an AI cold war so scary and honestly so tragic that I feel
*  compelled to at least try to imagine an alternative. While it seems almost impossible that the U.S. and
*  China could trust one another enough to work together on such an important issue as AGI
*  development and safety, and while as I've said many times, I would not want to live in Xi's China,
*  I personally would rather take our chances trying to work with the CCP than hoping we can solve AI
*  safety in a super short timeframe under the intense pressure of potentially winner-take-all
*  international competition. After all, as we talked about last time Flow was on the show,
*  the Chinese government does seem to understand that AI poses a threat, if only to its future
*  political control. And just this week, a Chinese firm has released a Sora-like video generation
*  model, which suggests that Chinese AI research isn't necessarily all that far behind.
*  All that said, as you'll hear in this conversation, I still have a lot of uncertainty on a number
*  of core issues. Will GPT-5 pose major risks? My best guess is no. GPT-5 class models will
*  probably still be in the sweet spot, where they're powerful enough to be super useful,
*  but still safe enough to deploy, though perhaps not safe enough to open source.
*  Will regulation, like the recently SB 1047, do more harm than good? Flow and I are both
*  long-time libertarians and well aware of the potential, even the likelihood, of unintended
*  and unexpected harms from regulation. But given Frontier Labs apparent inability to self-regulate,
*  we are both inclined to support it as a starting point. And I, for one, could imagine myself
*  beginning to advocate for an outright pause in further scaling in the not-too-distant future.
*  In the meantime, is my adoption accelerationist hyperscaling-poser position even coherent?
*  I do still think so, but the argument that adoption inevitably hits the limits of current models,
*  which in turn invites further scaling, can't be dismissed out of hand either.
*  It is a strange time all around. Flow and I both continue to love exploring AI technology,
*  building products with it, and imagining the many ways it's likely to improve the human condition
*  in the years ahead. And yet, I can't shake the sense that the situation as a whole is at risk
*  of spinning out of control. And not only is there very little that I can do about it, but in some
*  ways I am even contributing to the dynamic. I certainly don't have all the answers, but I
*  hope that by speaking candidly about these issues, I can play at least some small part
*  in steering the world toward the best possible outcomes.
*  As always, we'd love to hear your thoughts. Do you find value in this sort of real-time
*  reaction episode, even though it raises more questions than it answers? Or would you rather
*  I stay focused on concrete research and applications? I look forward to hearing from you,
*  either via our website, cognitiverevolution.ai, or as always, you can DM me on your favorite
*  social network. For now, I hope you enjoy this week-ending conversation with Flo Crevello.
*  Flo Crevello, CEO of Lindy and feeler of AGI. Welcome back to the Cognitive Revolution.
*  Thanks, Ned. Yeah, it's becoming a tradition. Glad to be here as always.
*  So you were just saying you are most of the way through the talk of the week, which is the Leopold
*  Eschenbrenner Situational Awareness Manuscript, and apparently you're losing sleep over it.
*  Yeah. If you haven't read it yet, you should. For the record, it's not the first time I
*  literally lose sleep over AGI, but yeah, I slept five hours last night. I'm quite tired. It doesn't
*  make for a... This is probably not a good idea to read this right before going to bed. It's pretty
*  freaky. I think the argument is very cogently laid out. At this point, I don't understand how
*  people don't freak out, honestly. I think if you understand what's going on, you should freak out.
*  Yeah, I tend to agree, and I might move a little circle back to this later, but I think there's a
*  big question of whether or not this... We can assess this thesis on multiple dimensions. One is
*  how accurate it is, how compelling it is. Another is, is it an idea worth promoting orthogonal to
*  its potential accuracy? I think before we do that, maybe let's build up the case and get people to
*  the point where hopefully they're with us in terms of freaking out at least a little bit.
*  I think one of the things that people hear and repeat without being maybe as critical as they
*  should be about it is the idea that we're probably hitting a wall now because we haven't seen
*  anything better than GBT4, and that's been, geez, 18 months plus since OpenAI finished training that.
*  That means we're pretty much stuck at GBT4. I think we would both agree that is not really an
*  accurate description of the last 18 months, but how would you rebut that claim for starters?
*  I'll start by saying that people have been saying that for 10 to 20 years or something like that,
*  that deep learning was hitting a wall. It's a meme at this point, right? That's the first thing. The
*  second is it's not true that we've not seen anything new since GBT4. We've seen... We have seen
*  models that are basically at GBT4 level of performance, sometimes greater, for literally
*  about a hundredth of the cost and about 10 to 100x the speed of GBT4. So I think Gemini 1.5
*  Flash, I think, is greatly under discussed. It's insanely good of a model. It's very cheap and very
*  fast, and that's a big deal. I think the cool thesis of the AGI-pilled people is the scaling
*  hypothesis. It's, hey, if you can make it bigger, faster, if you can throw more compute at it, it's
*  intelligence emerges as a result of that. And I think that not every inference optimization is
*  also a training optimization, but by and large, when you see this kind of inference optimization
*  of basically a hundred X, something also happened in the training pipeline. And in parallel to that,
*  you're seeing, obviously, context windows are becoming infinitely bigger. 18 months ago,
*  we had 4,000 tokens context windows. Today, we have 1 million tokens context windows. That's
*  pretty unreal. We have the member architecture that's starting to be shipped and is working
*  from what I'm gathering. We're on track. GPT-5 is going to take people by surprise. I have no
*  insider information, but I feel like GPT-5 is going to come out in Q3, Q4 this year. It's going
*  to take people by surprise. Yeah, I think Flash is a great data point, and you hit the key points
*  there. And just to give a use case example of this, which I've maybe talked about in a couple
*  episodes, but I tried to get it to write a character sketch of me based on the last 250
*  emails that I sent. That turned out to be about 250,000 tokens, which is outside of the context
*  window for any other commercial provider. Anthropic maxing out at 200,000 still doesn't get quite
*  there, but Flash has the million. So it literally has a hundred times longer context window than
*  the original GPT-4. Now it's only eight times longer than the latest GPT-4, but still over
*  a hundred since when people are referring back to perceived flattening. And it is one to two percent
*  the cost and it is a lot faster. And it did a phenomenal job of writing a character sketch of
*  me based on just this data exhaust, something that I didn't even really prompt engineer or optimize.
*  I literally just said, here's like a big boatload of emails out of somebody's account. Can you
*  synthesize this into a useful sketch? And it really was super impressive. And that took about
*  45 seconds and cost under 20 cents. So that is the kind of thing. And just for contrast, right,
*  to do that back in the original GPT-4 would have been chunk it down into like lots of little pieces,
*  few emails each, try to summarize those, summarize the summaries. And honestly, I don't think you
*  could have expected to get anything as good as what I got out of just a single call, just because
*  so much would be lost at each step and you'd have to ladder up to the final summary. And yeah,
*  the ease of that, the cost, the speed, it really is incredible. Maybe we can just refine a few of
*  these other things. I think GPT-4 is also really under discussed mostly because people haven't
*  actually had a chance to play with it yet. But I'm sure you've seen the tweet from Greg Brockman,
*  where he used the model to generate an image of somebody writing on a chalkboard, where the
*  content on the chalkboard is probability of text, pixels, audio. And the obvious implication of that,
*  in addition to just flexing the image generation capability of the model, the obvious implication
*  is that this is a single architecture, might be slightly modified transformer at this point,
*  who knows. Could be some state space stuff in there. But it's handling all of these different
*  modalities on par in such a way that we're no longer pipelining data through a transcription
*  and then put that text into the model and then get text back and then maybe generate an audio or
*  create instructions for Dolly 3 to then generate the image. But it's literally all happening
*  in the same space. And the generality of that is really going to be a huge deal as people actually
*  get their hands on it. We don't have it yet. But when I think about what I would build with that,
*  it gets pretty crazy pretty quick. The fact that they solve the interruptions too in such a nice,
*  easy way. It's like the speed with which they're able to convert the tokens in is,
*  and it seems that they're modeling. I want to know more about how they do this. I'm sure
*  many people do, but it seems like the fact that it handles this interruption so smoothly
*  suggests that it is putting its own audio and your audio right into the same audio mix.
*  And so it's immediately able to stop when it realizes that there's some other
*  audio in the same space superseding it. That is pretty awesome.
*  Yeah. It's a bitter lesson strikes again, right? Instead of engineering your way around
*  interruptions and what's the threshold and how many seconds and all that, just train it.
*  Train it to figure this out, right? And it's just end-to-end, giant ass model. I agree with you that
*  the multimodality of GPT-4.0 took me by surprise. I didn't expect to see this kind of heavily
*  multimodal model come out so soon. By the way, it hasn't come out yet, indeed. Now, I actually
*  find its reasoning abilities to be very underwhelming. I've actually moved away from
*  GPT-4.0 for most of my workflows, but I think that's fine. I think the scaling hypothesis is
*  going to take it from here. But yeah, multimodality of GPT-4.0 is awesome. So yeah, I think... I don't
*  know what to tell you, man. AGI is coming. I will say though, one thing I've updated in two ways,
*  actually, in recent months. One of them is, and both of them are in the book, right? One of them is,
*  if we don't get AGI by 2030, then probably we won't get it by 2040. There's this window right
*  now where we've got the next five years are going to be very critical. And the reason for that is
*  because there's a lot of one-time optimizations that we're going to grab during the next five years.
*  So the data, obviously, is going to run out. It may not be that big of an issue, but we're
*  going to have to figure this one out. Most importantly, we're going to run out of dollars,
*  right? There's a lot of scaling that's been happening just because we've been investing.
*  So much more, right? But at some point, once you hit a $1 trillion training run, you can't really
*  grow much bigger than that, right? So basically, there's these orders. And then there's what he
*  calls the un-hovering of the model, where it's the low-hanging fruits of the cognitive architecture.
*  There's a lot of stuff around the model that we need to figure out. All of those are one-time
*  gains. And so we have these three, call it three to six orders of magnitude of improvement ahead of
*  us. Once we've grabbed them, if that doesn't lead us to AGI, then we are left with Moore's law,
*  which is pretty slow. It's half an order of magnitude a year or something. And we're left with
*  architectural improvements, which are also not super fast. So that's the first way I've updated.
*  If AGI doesn't happen by 2030, 2032, I think then we're left with 10 more years of no AGI.
*  The second way I've updated is on the speed of the takeoff. I used to be very undecided about
*  takeoff. Is it going to take a day? Is it going to take 10 years? And I'm increasingly convinced
*  that it's like one to four years or something like that. But I no longer decouple AGI and ASI
*  as strongly as I used to. And so ASI, superintelligence, I used to be like,
*  AGI for sure, ASI, I don't know. Now I'm like, if you've got AGI, you've got ASI period,
*  because you can automate AI research. And all of a sudden you literally have 1000 extra bandwidth
*  of AI research. It seems to me like a foregone conclusion that leads you to exponential
*  improvement very quickly. Yeah, I've been trying to fight that notion in my own head. And this is
*  previewing or tipping my cards on how I feel about the value of promoting some of these memes,
*  because I'm like, I don't want to see us get into a AI arms race with China. That seems like a very
*  bad scenario. And I would almost do anything to avoid it. And so I do find myself being motivated
*  to say maybe because I think the path to some sort of AGI seems quite clear. And I honestly think
*  it's not even really that much more than what we have today. In terms of when AGI will be declared,
*  it seems to me almost more a function of how and when OpenAI wants to renegotiate its deal with
*  Microsoft than anything else, because they have the contractual clause where when the OpenAI
*  board declares AGI to have been achieved, then they don't have to give Microsoft the IP.
*  Obviously, they're running around trying to court other infrastructure providers and diversify their
*  power base away from purely being dependent on Microsoft. And Microsoft, of course, I think,
*  is well aware of this too and investing in their own internal research. But at what point would
*  they want to make that move and be able to renegotiate? I think if they wanted to declare
*  that in 2025, they probably could. It seems like you start to think about how many un-hobblings
*  are really necessary from where they are today. The reasoning and the coding ability isn't super
*  human, but it does seem to be on par with your or maybe even a bit better than your typical
*  knowledge worker. And if you imagine the investment in post-training of the sort that Jean-Cheloultre,
*  Dorakesh is really on an unbelievable run here in terms of creating historical artifact podcasts.
*  The Schulman one, I thought, was noted, but it wasn't as noted as this last Leopold one. But
*  it was quite striking when he was like, what do you think this will happen? Well, maybe next year,
*  maybe two to three years. But it was just like, yeah, we're going to go collect a lot of mid and
*  longer project execution episode data and teach the pattern of how you run into obstacles and
*  backtrack and come up with some other strategies and go around those obstacles. And that seems
*  like it's probably well underway in terms of the collection of that data. I would be shocked if
*  they don't already have scale and potentially several other partners already tracking the work
*  of knowledge workers in a variety of different verticals and annotating what they're doing,
*  explaining what they're doing out loud. We don't have a chain of thought in the raw
*  internet data set, but it's not that hard to collect if you're just prompted every few minutes
*  to explain what you're doing as you're working to just dictate it via microphone. So it seems like
*  they're going to have that. It seems like the next generation of the next big upgrade, in addition to
*  being smarter, it should have these like mid length at least project execution capabilities
*  with the ability to get stuck and restart and come up with other ways and gradually get there.
*  And I think you could probably call that AGI if you just stuck to the very literal
*  textual definition of something that can outperform humans at the majority of knowledge work.
*  Have you had a chance to use anything like Devin or the new GitHub workspace?
*  I have not, no. I usually do all day. So I see agents doing weird stuff all day. Yeah.
*  I think they're quite impressive. I think Devin definitely has an interesting
*  paradigm where it's especially for someone who is not a full-time coder themselves with the GitHub
*  workspaces. My feeling was like, it's very much a product for coders. It starts with an issue. You
*  have to have a GitHub issue to start with. So for anybody who's like not a coder right off the bat,
*  they're like, what's a GitHub issue? I've lost Devin. On the other hand, you just go to the website
*  and you say, here's what I want you to do. And it assumes nothing in terms of any infrastructure
*  that you have, whatever it handles all that on its side. What's really interesting about it and
*  feels like the future is that it just goes to work. You don't have to really do anything.
*  It may get stuck or you may observe that it's doing something a little weird and you can just
*  chat with it even while it's still working. And then it will interrupt itself, absorb your message,
*  rework the plan if it needs to, and then keep going. But you can just drop in a message anytime
*  you want and it just keeps going, incorporating your messages when they show up. But otherwise,
*  if it runs into issues, it'll just try to work through them. I wouldn't say it is
*  drop in. Honestly, it does feel like coding intern. If you had a young person who hasn't run into a
*  lot of things before and needs that sort of basic coaching, it probably feels like that. It honestly
*  is getting to that level. And with one more turn, it feels like it would be likely competitive with
*  a not elite, but employable coder. Hey, we'll continue our interview in a moment after a word
*  from our sponsors. AI might be the most important new computer technology ever. It's storming every
*  industry and literally billions of dollars are being invested. So buckle up. The problem is that
*  AI needs a lot of speed and processing power. So how do you compete without costs spiraling out
*  of control? It's time to upgrade to the next generation of the cloud, Oracle Cloud Infrastructure
*  or OCI. OCI is a single platform for your infrastructure, database, application development,
*  and AI needs. OCI has four to eight times the bandwidth of other clouds, offers one consistent
*  price instead of variable regional pricing. And of course, nobody does data better than Oracle.
*  So now you can train your AI models at twice the speed and less than half the cost of other clouds.
*  If you want to do more and spend less like Uber, 8x8 and Databricks Mosaic, take a free test drive
*  of OCI at oracle.com slash cognitive. That's oracle.com slash cognitive, oracle.com slash cognitive.
*  The Brave Search API brings affordable developer access to the Brave Search index,
*  an independent index of the web with over 20 billion web pages. So what makes the Brave Search
*  index stand out? One, it's entirely independent and built from scratch. That means no big tech
*  biases or extortionate prices. Two, it's built on real page visits from actual humans, collected
*  anonymously of course, which filters out tons of junk data. And three, the index is refreshed with
*  tens of millions of pages daily. So it always has accurate up to date information. The Brave Search
*  API can be used to assemble a data set to train your AI models and help with retrieval augmentation
*  at the time of inference, all while remaining affordable with developer first pricing.
*  Integrating the Brave Search API into your workflow translates to more ethical data sourcing
*  and more human representative data sets. Try the Brave Search API for free for up to 2000
*  queries per month at brave.com slash API.
*  I agree. And so again, I think people are asleep and no one is really realizing what is for sure
*  happening, which is yeah, like AI code builds are like 100% happening in the next few years.
*  And I was actually just having this conversation with a teammate and I'm realizing that sometimes
*  there's this weird psychological thing that's happening. And I don't know what to call that
*  logical fallacy, but it's like, suppose I came to you and I was like, Nathan, here's, I'm going to
*  tell you two things. I'm going to tell you, number one, here's proof of very compelling evidence that
*  someone's going to come to your house and kill your family tomorrow. And number two, a shock tornado.
*  A shock tornado, Nathan, is going to come to your house. And there's this weird thing that happens
*  psychologically, which is when you hear that all of a sudden you're like, ah, nonsense. Shock tornadoes
*  bullshit. Even though I just showed you evidence that even if it's own is very, very telling that
*  like someone's going to come to your house tomorrow. Right. So I think, I think what's going on with the
*  whole API discourse is there's so many claims that are bundled into the same bundle because
*  realistically we'll basically speed running a hundred years of history, if not more, we're
*  going to speed run them in the next five to 10 years. And so lots of shit's going to happen.
*  And you've got folks like the, Elijah Yudkowsky who are like making outlandish claims to
*  some. I happen to find them very credible, but that the whole sci-fi thing is going to compile
*  matter and it's going to take over the universe and all of that stuff. And so people are like, okay.
*  And then I think there's like very straightforward claims that are also being made about, look,
*  the AI engineer is coming, right? We are going to automate all knowledge work period. That's coming
*  in the next five or 10 years. So we're going to have to deal with that. And even when you talk
*  about like the risks, so like this is merely disruptive, but heavily disruptive. Hey, we're
*  automating all knowledge work, FYI, this is happening. No practitioner disputes that, period.
*  I find it insane that we've moved on from the debates. Oh yeah, of course, let's not talk about
*  that. Let's talk about the sci-fi stuff. Hey, FYI, people don't know that. People don't know that
*  thing that we all agree about and don't even talk about anymore because it's just so boring. We're
*  automating all knowledge work in the next five or 10 years. Okay. And then also as far as the risks
*  are concerned, you don't have to worry about the sci-fi misalignment risks to be deadly worried.
*  I think there's two broad categories of risks. There's like the AGI goes rogue and I understand
*  why people are skeptical about this. I disagree, but I understand. But then there is another form
*  of risk that I understand a lot less that you could disagree about, which is the misuse kind of risk.
*  I do not understand how there can be any doubt whatsoever that people are going to do evil
*  shit with this extremely powerful technology that we are putting up to everyone and gleefully open
*  sourcing. I don't understand the case and I don't think there is a case, period. I think it is
*  extremely telling that the majority of the case that's being made about this is not a case at all.
*  It's just slogans. It's so my dead body, you will take my second amendment, first amendment. Hey,
*  can we just talk on the objective all about what we're talking about here? I believe it's Dario
*  Amadei from Anthropic who made this excellent point. He said we've been benefiting from an
*  invisible protection in the world today because there is a set of evil psychopaths out there.
*  That's just a fact that's indisputable. Who want to do evil shit and kill people. But then the
*  overlap between the evil psychopaths and the capable people is very small because as you become
*  capable, as you educate yourself, two things happen. One is you become socialized and so you
*  don't want to kill people. But also your opportunity cost rises because now you can do things with that
*  education. You can become a trader or a software engineer, an entrepreneur, an investor, whatever.
*  And so you can make money and so you've got better things to do with your time than go around and
*  kill people. And when there is an exception to that and when someone very educated goes rogue,
*  it's notable. It's like the Unabomber thing. People remember it for decades. This is a freak
*  thing that just happened. But I think that protection is disappearing. I always talk about
*  the upside of that. It's, oh look, we're going to empower everyone with AGI. A 17-year-old is going
*  to have the same go-to-market power as the Coca-Cola company because he's going to have 10,000 employees
*  in his bedroom. Mr. Beast built a media empire from his bedroom. Same thing. You're going to be
*  able to build an industrial empire as a 17-year-old in your bedroom. That's awesome. The coronary of
*  that though is that we are just giving capabilities to everyone. And so some people are going to do
*  evil shit with these capabilities. It's just obvious. And so I think really the two most
*  obvious classes of risks here are going to be bio and cyber. And so for example, the cyber thing,
*  look, our entire civilization relies on computer systems. That we barely understand, by the way,
*  at this point. And many of which arguably are the most important of which are extremely integrated.
*  So our banking system, our grade, all of that stuff relies on the internet and information systems.
*  We are about to give a superhuman cyber hacker to everyone. And again, I think one class of risk
*  that concerns me, it's not existential, but it's bad. It's yeah, you wake up one morning,
*  the grid is fucked. So you have no telecommunication. So total fog of wool, by the way,
*  right here. Because there's no TV. What are you going to do? You're going to turn on the radio?
*  Do you have a radio? So total fog of wool, no communication, no banking, no electricity.
*  Cities are entirely dependent upon transportation networks, which also shut down. People starve to
*  death. And by the time people fix the grid and the banking systems and all of that stuff and
*  unhack it, the hackers bring it back down. And the hackers could pick your flavor of AGI, depending
*  on how much you go back. It could be like a script kiddie on the most extreme side of the spectrum.
*  It could be China, it could be North Korea, it could be Russia, it could be whoever. Or just
*  like an organized group, a few hundred thousand dollars. It could be Al Qaeda, I don't know.
*  And by the time you fix the grid, they fuck it again. And how long does that last? A month,
*  two months, three months? People always reply, oh, but AGI can protect us against AGI. We could
*  also have AGI cyber defenders, to which are we talked two things. One is that a technology
*  does not necessarily symmetrically increase defense at the same pace at which it increases
*  offense. That's the first thing. The second thing is that even if it was symmetrically
*  increasingly increasing defense and offense, even if indeed it was improving defense faster than
*  offense, I think these institutions are going to adopt this new technology much slower than the
*  hackers will. Who do you think will adopt AGI first between Bank of America and PG&E
*  and the hackers in Russia? Of course it's going to be the hackers in Russia,
*  maybe by as many as a few years. And so that delta is going to be super dangerous and super scary.
*  And I've just not heard a single quality rebuttal to this simple reasoning.
*  Yeah, there was just a new paper out in the last day or two from a former cognitive revolution
*  guest, Daniel Kang, who the new paper is that they've got a little team of LLM agents finding
*  and exploiting day zero or zero day exploits. And I haven't quite got deep enough into that
*  to understand exactly what the data set is that they're creating. Because obviously that's a
*  tricky one as this stuff gets known, then it gets on the web and whatnot. But presumably using
*  cutoff date as a safe way to delineate what was known at the time and what's new,
*  they're finding novel things that are not in the training data and exploiting them.
*  Yeah, that's a little, it does feel like a bit of an unstable situation. So I was saying earlier
*  that I have been like, man, I really don't want to see us get into an arms race, AI arms race with
*  China. If both states believe that there is the prospect for decisive advantage in some slim lead
*  in AI technology, then it seems like they probably will race for it. I don't, it'd be great if we
*  could get them to get the two governments to come together and have some sort of preemptive arms
*  control or whatever. But obviously that's tough. So that could be maybe the next strategy to pursue.
*  But if they do believe that there's going to be this decisive advantage, then it seems like
*  they probably will race for it. So I'm like, okay, can I come up with a reason to believe
*  that there's not going to be, or it's at least not obvious that there would be some sort of
*  decisive advantage. And so I asked myself, what's the story whereby either we don't get to
*  a very high end human knowledge drop in knowledge worker by the late 2020s or conditional on getting
*  there, we stall out before some kind of intelligence explosion to move toward something genuinely very
*  superhuman. And honestly, I don't have great answers for either. When I think about the
*  AGI case, it really just seems to me like you think about all the kind of current weaknesses
*  and it seems like there's pretty clear path to unhobble on a few different key dimensions.
*  And then you imagine, okay, now we're there. Is there any way that we'd stay there and don't get
*  into a super intelligence type dynamic? And certainly the uncertainty increases. But when
*  I look at all these other neural network tools that have been created recently, whether it's
*  Alpha Fold 3 or one that I just saw the other day that is learning from quantum mechanical
*  simulations, how to model particle level dynamics at orders of magnitude faster than the raw
*  simulations can happen, and is starting to show this emergent behavior, this incredible graphic
*  the other day from somebody studying ions in solution, and they trained it on just this
*  solution data set, but then observed crystallization predicted by their trained
*  model. So they're seeing these phase changes as emergent properties coming out of this
*  learning on pure simulation data. And all that stuff's being developed in parallel, right? We've
*  got the bio ones happening at the same time as the material science ones, as the Go players and
*  whatever else. And it's damn, at the time when there is a drop in high end knowledge worker,
*  there will also be incredibly powerful tools that we're just starting to see the beginning of,
*  but that will presumably like those loops will be pretty well established, right? To say, oh,
*  run this sort of simulation, see what happens, run that 10,000 times, by the way, see what happens.
*  Now we're also seeing the development of automated labs, cloud labs, emerald cloud lab,
*  and similar things where via APIs, you can actually run physical experiments to verify the
*  candidate theory, hypotheses that have come out of the simulation. And it just feels, man, those
*  things will be able to run pretty fast. They're going to be pretty parallelizable. And even if
*  the thing isn't like beyond Einstein, it still feels like it's going to have
*  tools and the ability to use this like insane array of tools. And that's even assuming that
*  those things don't merge. I could also easily imagine in the quest to scale up to something
*  super powerful, that bio data and quantum mechanical simulation data just gets folded into the core
*  data set. And then it's all, it's like P of text and pixels and audio and quantum mechanical
*  data and biological sequence data and proteomics and everything else. But even if they don't all
*  get merged, it just seems like the tools are going to be so powerful that it is hard for me to imagine
*  that it stalls out at that point. And I've been wrestling with this for the last couple of days,
*  trying to come up with, if I was going to try to talk somebody down from this notion that they
*  should be concerned that there might be some decisive advantage to be had, I'm like,
*  I honestly can't put together a great argument for it. Could you put together what would be your,
*  if it doesn't happen, if we don't get any AGI and if we don't get and or if we don't get super
*  intelligence relatively quickly after some early AGI, could you put together a coherent story for
*  how that might not happen? I'm sure I could. I think probably, I think the data headwinds would
*  be my first reflex here. This is where I would jump because we truly are going to run out of data.
*  I think it's tractable, but I could be wrong. But I also think it's the wrong question to ask. I think
*  this is not the question that we ask when it comes to any other risk. Like when it comes to risks,
*  for example, about climate or about nuclear war, that pandemic preparation, we're not asking like,
*  hey, we really need to get in the room here and think about everything and establish beyond
*  the shadow of a doubt that this is for sure going to happen. It's no, hey, we've got a bunch of
*  really smart experts around the room and there's like an emerging consensus. So climate, there's
*  like a consensus and look, something's happening that's not fun. And so we probably should invest
*  something and be prepared, like just from a pure EV standpoint. It's like, you have some likelihood
*  of something really bad happening. It's worth throwing like a few billion bucks at this.
*  I think we're like way, way beyond that in AI. I think the experts are saying there is a consensus.
*  If you look at like the top-sighted experts, like the top three or five, every single one of them is
*  really ringing the alarm bell right now and being like, hey, this is really concerning.
*  Right. There is a consensus, which wasn't always the case. I will note that it's interesting that
*  the AI risk skeptics or deniers, I should say, the AI risk deniers used to
*  hide behind the lack of a consensus in the research community about AI risk. They were like,
*  ah, look, I don't know what it is because I'm not an AI researcher. You're not an AI researcher.
*  But when you talk to the AI researchers, they said eight years ago, they say there's nothing
*  to worry about. I'll just find it interesting. That's completely changed since then. And these
*  people haven't updated the slightest. They just don't mention the AI experts.
*  So look, at this point, it's very clear. It's like the trend line is up and to the right,
*  smooth, not flattening, or many orders of magnitude, and the experts are all in alignment.
*  I think at this point, we need to start treating the deniers the same way we treat the climate
*  change deniers, which is politely ignored. Which by the way, climate change, I really don't want to
*  get into this thing, but sure, it also, politics gets in the way and it gets corrupted by all sorts
*  of political agendas and that's very shitty and dangerous. There's no race, there's no doubt,
*  though, that climate change is happening and it's bad and it's worse, investing deeply into. That's
*  it. So you ignore the folks who say, no, actually it's not true. That's what we need to do. We need
*  to ignore these people. We need to move the conversation onto, okay, what now? There is a
*  consensus amongst experts. It's very clear what's happening. What now? And a sort of policy
*  conversation that's happening in California, for example, the bill that's being introduced,
*  whatever you think of the specifics of the bill, I think that's exactly the kind of conversation
*  that needs to happen right now. And we need to start talking about AGI preparedness right now,
*  because if you don't treat the problem now, sooner or later, you're going to have to
*  worry about it. And it's much better to be prepared and have to be taken by surprise five
*  years from now. Yeah, I agree with you that my question was an inversion of the right question,
*  at least on the first analysis of is this something we should be worried about? Is it something we
*  should be doing something about? I always say in response to the P-Doom question, I always say
*  something like 10 to 90% or five to 95%. And the key point there is that on both ends, there's
*  enough to be fighting for. If it's only 10%, or if it's even if it's only 5%, that's a big enough
*  problem to motivate me. And on the other end, if it's only 10% chance of survival, then that seems
*  like it's enough to try to achieve. I'm playing out this game theory or just going down this
*  branching scenario analysis and thinking the node that I was at on that question, is there any way
*  that there's a is there any credible case that we should be thinking about that we don't end up in
*  this race for decisive advantage? And I can't come up with a good one. But I do think that the utility
*  that if there were something would be like, hey, we don't need to be racing China to create the
*  trillion dollar cluster. And maybe we can take a little bit more chill attitude toward scaling.
*  I think that the trillion dollar cluster to me feels like an upper bound on what it's likely to
*  take. There's just not, it seems like that does not assume that there's anything clever happening
*  between now and then that's just like a raw, just take what we have and just keep doing it more and
*  more. And that probably will work for a while yet. Certainly, when you think about all these
*  different data modalities and whatnot. But my best guess is that there will be plenty of efficiency
*  things and plenty of ways to break this out across data centers. As soon as the if there is a
*  scenario where it's like, hey, we need a trillion dollars worth of data centers. For security reasons
*  alone, you would probably want to diversify that location wise away from one single site. So there's
*  gonna be incredible incentive to both just reduce the resource requirements and also to figure out
*  how to not have such a concentrated physical capital plant required to do this all in one place.
*  I just don't like it because there's been like a few different big worries of the AI safety community
*  over time and run away. unfriendly AI is one the paperclip maximizer, the thing that doesn't
*  understand our values can't understand our values. That was like, it remains I think, not off the
*  table. But that's not exactly looking like the eyes that we're getting today. But then the AI
*  arms race with China was like another one that I've been hearing about for years. And it seems
*  like despite everybody recognizing that would be a terrible scenario to enter into the gravity of it
*  is hard to fight, right? I don't know. It just seems like man, I'm trying to come up with some way
*  to not fall into that trap. And it seems really tough. I think we don't need China though to be
*  in an AI arms race. I think if you took China off the map, like you still have Google and
*  Anthropic and OpenAI. And so these folks have been in an arms race for a long time now.
*  But the thing is that if you don't play the arms race for geopolitical reasons,
*  you're going to play it for economic reasons. It's just that the economic incentives are just
*  too strong for corporations to resist. It's their job to pursue this kind of thing. It's just look,
*  even if it costs you $10 trillion to automate all knowledge work, that's cheap. It's very cheap to
*  automate all knowledge work. Are you kidding me? Well, find the money, no problem. Markets will
*  love to take that up. And I agree with you also that look, it is funny that the community seems
*  like it's disagreeing about, hey, is the risk 10% or 90% or is it even 1% or 90%? And is the timeline,
*  it's funny because I remember before being as strongly a GI killed as I was having dinner with
*  a friend. And he was like, I was like, I'm really worried about the GI. And he was like, oh my God,
*  how worried are you? And I guess he was more up to date than I was about the timelines. And I was
*  like, what's the timeline? And I was like, I don't know, like 15, 20 years? And he was like, dude,
*  people are freaking out right now. They're saying five years. And now, now that I'm more up to date,
*  I am also saying five years. But I just found his reactions so strange. Like, man, like 15 or 20
*  years is nothing. So I really think there's this weird anchoring effect or framing effect that's
*  going on. It's like the shark tornado thing that I was mentioning where it's like, because people
*  are saying five years and that sounds so Atlantically incredible to these people, they're
*  totally dismissing the fact that they would agree about that it is maybe 15 or 20 years away, which
*  is tomorrow. It's coming so quickly. Right? We all today as a civilization spending plenty of money
*  on risks that are not supposed to materialize before 15 or 20 years. Like corporations on a
*  routine basis plan on that kind of timeframe. So even if you just think it's 15 or 20 years from
*  now, which to me is an upper bound, we need to be planning for this. And I view way too little
*  planning and way too little conversation about this topic. Hey, we'll continue our interview in
*  a moment after a word from our sponsors. Hey, all Eric Torenberg here. I'm hearing more and more that
*  founders want to get profitable and do more with less, especially with engineering. Listen, I love
*  your 30 year old ex-fang senior software engineer as much as the next guy, but honestly, I can't
*  afford them anymore. Founders everywhere are trying to turn to global talent, but boy is it a hassle
*  to do at scale from sourcing to interviewing to on the ground operations and management. That's why
*  I teamed up with Sean Lanahan, who's been building engineering teams in Vietnam at a very high level
*  for over five years to help you access global engineering without the headache. Squad Sean's
*  a new company, takes care of sourcing, legal compliance and local HR for global talent. So
*  you don't have to with teams across Asia and South America. We can cover you no matter which time
*  zone you operate in. Their engineers follow your process and use your tools. They work with react,
*  next JS or your favorite front end frameworks. And on the back end, they're experts at node,
*  Python, Java, and anything under the sun. Full disclosure, it's going to cost more than the
*  random person you found on Upwork that's doing two hours of work per week, but billing you for 40.
*  But you'll get premium quality at a fraction of the typical cost. Our engineers are vetted top
*  1% talent and actually working hard for you every day. Increase your velocity without amping up burn.
*  Head to choose squad.com and mention Turpentine to skip the wait list.
*  Omniki uses generative AI to enable you to launch hundreds of thousands of ad iterations that
*  actually work customized across all platforms with a click of a button. I believe in Omniki
*  so much that I invested in it and I recommend you use it to use cog rev to get a 10% discount.
*  So I do think we took China off the game board. Things might look significantly better. Maybe
*  you'll talk me out of it. But my thinking there is that you look at how many live players are
*  there today, right? There's three to five, maybe three to seven. And for the most part,
*  aside from the Chinese dimension, they all know each other. A lot of them live very close by to
*  one another. A lot of them have directly worked together in the past. Even the Mistral team is
*  largely ex deep mind, I believe. So there is a collegiality there. And there's also the sense
*  that if there was no external force, I would think that the US government might be a lot more
*  likely to create some governing environment that could slow things down. And that could look a lot
*  of different ways. But my concern is that the government will move from a moderating... In a
*  scenario where there's no China, I think the government would at least have some chance of
*  playing a moderating force. And if the government instead is obsessed as it seems to be with
*  competing with China in every dimension, then it seems like the Leopold scenario of
*  national security, state getting involved, and the likely militarization of technology is the top
*  priority, and the race for decisive advantage, the idea that we're going to get just far enough ahead
*  that we'll be able to solve alignment in months and then offer China a deal.
*  That seems like that probably is what happens if there's no deal with China and the specter of
*  China just continues to be what it is. In the absence of that though, it does seem like it could
*  be... Cooler heads could prevail, but seemingly much more likely to me.
*  I feel like China also has private companies. I think that the government in this whole thing is
*  a co-opting force. It's not a driving force. It's not going to be the one doing the AI research.
*  Chinese private companies are going to participate into the arms race just the same as the American
*  companies are, and minus the collegiality that you just mentioned. The role that I see government
*  playing in this whole thing is once we have an AI, at some point the DOD is like, oh, fuck.
*  Okay, this thing is really powerful. And also Baidu's also got it, or Tencent, or whoever,
*  because maybe we need to do something about this, and we need to ask the nerds to please give us
*  the keys ASAP before shit gets out of hand. That's how I conceptualize the role of the
*  government here. What do you think can and should be done today? You alluded to a policy like an SB
*  1047. I've had a couple episodes on that. If anybody is not up to speed on it, they can go
*  back and check those out. It's just been amended, and the amendments probably seem to have been
*  considered to be positive updates. It's pretty much across the board, although I haven't seen
*  a lot of people actually going from not supporting to supporting. It seems like among those that were
*  not inclined to support it previously, the response has largely been, this is a positive update, but
*  I still don't support it. I do find that to be weird in as much as it really doesn't feel like
*  there is a huge ask there. It's like, try to make sure your models aren't going to cause
*  mass casualties or hundreds of millions of dollars in damage. If you can't be reasonably confident
*  about that, then you should deploy them with safeguards, which would mean not open sourcing.
*  But again, it's like, today you can be reasonably confident about that. We're talking about a future
*  scenario where you no longer can be, which seems quite plausible if there's not research
*  breakthroughs. We could put policies like that in place. We could double down on interpretability
*  and hope that the Sparks autoencoders will figure it all out for us, and we can find our way to
*  alignment somewhere that way. We could imagine, I recently saw a pretty interesting technology
*  that I might do a whole episode on called Sofon. Actually, Zvi tipped me off to this in my last
*  conversation with him, where this is notably out of China, is a technique that they call fine
*  tuning suppression, where for a domain that they call take up, this doesn't yet work on language
*  models. They did it on image generation models for starters, but they created a restricted domain
*  versus the open normal domain. Within the restricted domain, they did a fine tuning
*  technique to basically create a denial of service type of response, where in the denoising step of
*  an image generator, it would just guess zero and basically not change the image if it's in the
*  restricted domain. Then outside of the restricted domain, they had this normal training reinforcement
*  that would make sure that the standard behavior was still accessible. What this does is it creates
*  a local minima that's hard to get out of. They call it fine tuning suppression because even when
*  you come in and fine tune it, it still doesn't really work. There's no gradient. They construct
*  the loss function of the fine tuning suppression in such a way that the gradient is basically zero.
*  It converges. There is no gradient at that point. When you try to go fine tune it and pursue your
*  usual gradient descent technique, the gradient starts at zero. You can't really get out of it
*  very easily. Their goal there was to create something that is harder to fine tune to get
*  those capabilities than it is to just train from scratch to get those capabilities. That was a
*  really interesting and novel thing, but overall, it just feels a man. We've got a few things here
*  and there, but I don't know. Maybe it's all the above. What do you think we should be
*  doing now? What should we be advocating for now? Should we be chaining ourselves to the fence at
*  OpenAI at this point or do we wait one more, wait for GPT-5 before we do that?
*  Fabien Sorensen If there was a chain, if there was a gate that
*  we chained myself to right now, it'd be Metas. I think step one is we need to stop open sourcing
*  the models, period. It's insane to open source them and there is no benefit to it or very little.
*  It's only not worth the cost because we don't know what these models have in them. It takes a lot of
*  work actually to figure that out. There is this paper that I always love mentioning, a Microsoft
*  paper called MedPrompt that finds that GPT-4 can actually perform better than models that are
*  specifically fine tuned on medical use cases. GPT-4 was not fine tuned on these use cases,
*  but GPT-4 can beat these specialized models just with a specially engineered prompt
*  that takes them a while to engineer. These models are just such huge objects that we have no idea
*  what's in there. It's like a dense jungle and it takes us years to hack our way through the jungle
*  and we still don't know what's inside GPT-4, honestly. We're open sourcing models and we
*  have no idea what's in them and we know that certain little tweaks can make them jump in
*  capabilities tremendously. The cat may be out of the bag. You could reach a point where it's
*  already too late. You've already killed yourself basically as a civilization and you have released
*  a model that is AGI capable out there in the wild or like super hacker capable out there in the wild
*  and you just don't know it yet. The weights are already out there. There's nothing you can do at
*  this point and you're just six months away from some guy figuring out how to prompt the model the
*  right way. That's entirely plausible and there is no advantage in open sourcing these models.
*  And by that, okay, so what are the typical advantages to open sourcing something?
*  People can audit it. So editing the code, aka fine tuning the model, you can do that through an API.
*  Open AI offers fine tuning through an API. That's perfectly fine. So why not do that?
*  Auditing the code in order to increase its security, I will say not only is that not
*  possible, I will say the only thing that is possible is the exact opposite. So you cannot
*  audit weights of a model. Unfortunately, there is a field of very active research. You can't look
*  into the weights of a model and be like, ah look, there's a problem here. So you can't do that. So
*  really there's no point in open sourcing. What you can do however is whatever security measures
*  were put in place during the training of the model, you can train out of the model unless
*  the trainers just did this thing you just mentioned which I hadn't thought about. But
*  it's trivial today at least to remove the safeguards from a model. And I forgot what
*  they call it. It's like an unshackled model. If you go to Hanging Face, there's like a wizard,
*  uncensored. Look for the uncensored families of models on Hanging Face. It's trivial to remove
*  these things. I just don't think there is a good reason to open source this model. I think that's
*  a step one. I think step two is we need a Manhattan Project for alignment. We need to spend dozens of
*  billions of dollars. Now I don't know how sensitive to spending alignment is. I suspect not very
*  sensitive but like at this point throw the kitchen sink as a problem and perhaps even
*  mandate private companies for hey for every dollar that you spend on training, for every
*  flop that you spend on training, you must spend a dollar and you must spend a flop on alignment.
*  I'd start there. I don't expect any of that to happen because if the kind of California bill
*  that you just mentioned cannot pass, then I don't expect these bills to pass. I foresee what will
*  need to happen is that there will need to be a catastrophe. There's going to be like a 9-11
*  of AI. I just pray that it's not too bad but I think after we've had that, then we I think
*  then we'll get very serious about regulation. Yeah, I think on your first point and you can
*  maybe square it with the second one a little bit but be interested to hear how you would do that.
*  The one common argument from a purely safety focused standpoint, the
*  LAMA 2, LAMA 3 so far has been good for interpretability research. It's been good for
*  a lot of technique development. We've got not just Anthropic and OpenAI doing sparse auto encoders but
*  research groups are getting into it and they can study circuits and they need at least somewhat
*  advanced models to be able to do the because you can't study emergent properties before they
*  emerge. You've got to have at least somewhat advanced models. You couldn't do this stuff on
*  GPT-2. It doesn't seem like for many of the most advanced things that you'd want to study.
*  If you had a Manhattan project, I guess that would all just be done via structured access somehow.
*  You'd imagine the weights never leave secure servers but somehow you create a scheme by which
*  academic researchers can do the things that they want to do and maybe they just have to be
*  vetted to some degree. If you're going to try to, there could be some sort of cryptographic
*  way to do this sort of thing but if you want to both not let the weights out and allow people to
*  do the development of all these inspection, interpretability, editing techniques, that does
*  seem like a still bit of a hard thing to square. I think it's like the Manhattan project. It's like
*  you had all these researchers who had access to a bunch of classified secrets doing very active work
*  on them and somehow it worked out. Sort of. In as much as they did manage to make the thing.
*  Yeah, I do worry about the drift, the mission drift potential of something like that. The
*  government gets involved and it's like, all right, we're racing. We got to get ahead of China. We
*  got to stay ahead of China. We got to create this decisive strategic advantage. Is that the right
*  structure to get the sort of deliberative or deliberate science that we need to figure out
*  how to make sure these things are actually going to do what we want them to do?
*  Maybe. I could definitely see it veering off in another direction.
*  And I will say, by the way, that I don't think these positions lately, like people who've known
*  me for a long time know, like, I'm a libertarian. I hate the state. I hate regulation. This is the
*  most evil institution we have out there. It will destroy everything it touches. And by the way,
*  also my understanding of that of like, Elisir and Myri and all of that stuff is like for the
*  longest time they were like, hey, let's find a way to solve the alignment that does not entail
*  asking that regulation. They did that for 10 or 15 years and they gave up. So like, we can't do it.
*  There is no, we need regulation ASAP right now. This is like the last result for a lot of people,
*  including me. So I agree. I think the state is going to get involved. Shit's going to get ugly.
*  Politics are going to do what politics do. And I think it's worth it because the situation is
*  that dire, I think. Yeah. I'm certainly with you in terms of being a very reluctant advocate for
*  regulation or state intervention. It's bizarre to find myself even entertaining, recommending that
*  in because I certainly always have resisted it in the past. Reeling this back in a little bit just
*  to the present day, I want to ask a couple of questions about just like the current state of
*  play. What are you building right now? How are you thinking about the challenge of, you only have
*  access to the best models today, but you know that we've all heard this from Sam Altman and others,
*  right? You got to be building for GPT-5. What does building for GPT-5 look like for you? How do you
*  conceptualize that? Yeah. I am the humble founder, building B2B SaaS. What we're building. So in that
*  Leopold book, he calls it basically un-hubbling. So that's what we're doing, right? We're building
*  the layers around the model. We're not building the model itself. And so we try to focus our work
*  on things that are simultaneously useful and commercially useful and valuable over the short
*  term and aligned with the march of AGI and these models. So we try to build cognitive
*  architectures and layers around these models that will maintain their utility regardless of the
*  model, right? So you can basically think of it as layers that make GPT-3 roughly as capable as
*  GPT-4 and GPT-4 roughly as capable as GPT-5. So regardless of the model you've got, these layers
*  are going to give you a job, right? And so what are these layers? These layers are like long-term
*  memory and RAG or like retrieving information selectively depending on the situation it's at,
*  but continuous learning that's leveraging these models' ability to learn in context, right? And
*  in a way that is sealed by the user. So for example, Lindy, you can give it a task and then as it
*  performs these tasks, you can give it feedback or it can ask you for feedback when it's in certain
*  and then it will keep getting better and better. And that's just going to be universally useful
*  regardless of the model, right? Tool use obviously through API but also computer use, right? And UI
*  use and all of that stuff. I think of what we're doing as basically there's like three buckets,
*  right? Like you can think of there's the agent and the agent's got an LLM at the center but it's got
*  these other layers which I just mentioned like the memory, the planning, the critic layer of the
*  verification layer, there's a recursive goal decomposition. You can do all of these things
*  outside of the model that still is the core of the agent. So we do that number one thing. Then
*  you get that black box that's really useful and you have inputs to that black box and then you
*  have outputs, right? And so that's the three things we're working on which is the black box itself
*  minus the LLM, the inputs and the outputs. So the inputs are going to be shared text, right? That's
*  like the most straightforward one. Images, audio, Lindy can join your meetings, you can listen into
*  your meetings, like that's just like a very useful kind of input. And then the outputs are going to
*  be again tool use which is like today like the garden variety is like API tool use. It's like
*  the most simple one. Again, eventually giving the ability to not just sit in a Zoom meeting but talk
*  to you in a Zoom meeting, make phone calls, talk to you on the phone, use a computer. That's what
*  we're working on, probably speaking, as a company. Yeah. I find myself increasingly in some ways like
*  the more I know, the more confused I am. I often go around calling myself an adoption accelerationist,
*  hyperscaling pauser. And somebody recently challenged me as to whether or not that is even
*  a coherent position. And I'm like, I think it is. It certainly seems like there's a lot of value from
*  fine tuning. Like I've definitely experienced that firsthand. And there definitely are significant
*  unlocks that you get from this sort of scaffolding. It's somewhat of a different question there
*  between on the one hand, I'm like, man, I don't want to see us just rush into six more orders of
*  scaling. That seems dangerous. And I also believe that like GPT-4 is enough in some ways, or GPT-5,
*  for certain. I think we do have like probably one more half turn to turn before we get to something
*  that is like generally smart enough to be the core of that drop in knowledge worker in the next,
*  not too distant future. But then I think about things like the, I don't know if you saw the
*  talk from somebody at OpenAI that has been working with Harvey on their custom model.
*  And they basically use GPT-4 as a base and do some continued pre-training. They didn't disclose
*  what percentage of flops the continued pre-training is. And then they do post-training
*  after that to try to get it dialed in on exactly how they want it to behave. And they have massive
*  preference for the custom model as opposed to GPT-4. And I infer from just the general vibe that
*  the incremental compute there is no more than 10%. It's not, and probably significantly less
*  than that. So there I'm like, okay, that does seem like we can get a lot more utility without
*  rushing to orders of magnitude. And also I like the sound of that custom model because it sounds
*  like it's really good at what it does, but it's probably not very good at a lot of other things.
*  It's probably not like, it's probably worse than GPT-4 at a lot of other things. And that
*  narrowness in some ways sounds really good, right? If we had something that was just really good at
*  handling legal briefs, that's a big thing. There's lots of value there. If we had a hundred of those
*  things for a hundred different areas, we could really create a ton of consumer surplus, which
*  I'd be super excited about. And yet I don't think those things would be like posing the sort of
*  risk that I think we're both worried about with more orders of magnitude. So that's one kind of
*  line of thought here. I'd be interested in your reaction to that. Then I'm still also wrestling
*  with which of these things are not, you know, listen to the Zuckerberg comments with Dworkesh
*  too. And he's, we have this sort of tick tock cycle where we're always building the scaffolding
*  and kind of in doing that, we're realizing what it is that we want to build into the next generation
*  of model. And then we're doing that. And then a lot of that scaffolding is no longer needed.
*  So like how much of the scaffolding that you're building, do you think actually
*  goes away? How much of it stays relevant? It's fine to throw some of it away, right? But you gotta
*  have enough that stays relevant. And that seems very tough to predict. So I gave you a run on
*  prompt there, but you can give me your answer in as many parts as you like. Yeah. We think about
*  that a lot. Like how much of what we're building is future proof. And I think probably a hundred
*  percent over the sort of horizon, maybe not literally a hundred percent, but 80%. And I
*  insist upon like the five years time horizon here, because look, suppose that you're building something
*  right now that you can get for free five years from now. Or rather what you're building now,
*  you can't have it at all today. So like what you're building like goes from zero to one,
*  but five years from now you would have had it even if you hadn't built it today. That's the
*  fact that you built it today gives you a hundred X cost and speed improvement. And so I'll give you
*  like one very concrete example of that, which is our continuous learning system. The one I just
*  mentioned where it's like, and you continuously learn from the feedback, the way it works, like
*  it's right. Right. And so it's you give feedback to Lindy and then before she performs any step,
*  she looks into her feedback database and she's like, has this happened before? What kind of
*  feedback they receive? I'm going to take it into account before doing it. Right. It's unreasonably
*  effective. It's pretty awesome. On paper, you could think that like this is made totally
*  obsolete by infinite context windows, right? Because you just have one agent, you talk to it
*  all the time, it just keeps reusing and growing the same context window. And so it doesn't need
*  to do this whole rag thing because it just like checks its context. I received feedback a few
*  days ago, but it's very thin. I'm just going to do it differently this time, but that's going to
*  cost you a fortune. And so I think that the death of rag has been greatly exaggerated because it's
*  literally a hundred days more expensive to kill rag via context windows. I don't think this is a
*  sort of like just difference that you can ignore. I am reminded of Android versus iOS. Like Android,
*  they built it on top of Java, which is a notoriously inefficient language because it's
*  garbage collected. And so it's just very slow. It's just very memory inefficient. And I assume
*  that people who built it were like, oh, who cares? Moore's law, computer's infinite, just build it,
*  ship it. And the reality of it is like for the longest time until very recently, the performance
*  difference was enough to make Android super sluggish and iOS super fast. It's like when you
*  smooth an iOS, it's always been butter smooth. And Android, it's not until very recently that it is
*  butter smooth as hell. And so I think that this sort of literal two to five X difference in
*  performance that it gave you, sure, eventually became moot because it's like, ah, like it's
*  who cares about the difference between one millisecond and five milliseconds. But for the
*  longest time, it wasn't one or five, it was a hundred or five hundred. And people do care about
*  the difference between a hundred and five hundred. So I think it's going to be the same thing here.
*  And so we're working on a lot of things that give you this sort of two X improvement, at least
*  two thousand X improvement at most, for the kind of like example system that was just mentioned.
*  Well, like what we're comfortable with is being useful over the very long tail.
*  I didn't quite understand your first question. Like you're grappling with what?
*  This was your question?
*  Just how much more mundane utility can we get?
*  Oh, right.
*  It's the adoption acceleration hyperscaling pauser. So is it coherent? So the challenge that I got
*  back online from no less than to my from epoch was basically like more scale makes the models
*  easier to use. That makes them more useful. So it's hard to does that position really have any sort
*  of natural center? And so I've been trying to find one and I think fine tuning both does unlock a lot
*  of value and it also does have a lot of the same sort of utility that you're describing where it's
*  like if you have to ten shot the thing to make it work versus fine tune and then you can just do it
*  on a one shopper, you know, zero shop basis, post fine tuning, then that also saves you a lot of
*  time and money. But yeah, clearly there's a lot of utility that's going to come from continued
*  scaling. I guess at some point I expect to begin to advocate for a pause. I'm not my GPT-4 red team
*  final report was I think that you can and should deploy this and it won't be it's not too risky to
*  do so because the utility is in the sweet spot where it's like powerful enough to be really useful,
*  but not so powerful enough as to be likely to get out of control and cause real problems.
*  And then like the corollary to that was, but I'm not sure how long that lasts. And it does not seem
*  that you have any control systems in place or in development that I've seen that would suggest you
*  have a solution to this problem on the horizon. That was before the super alignment team was even
*  announced. Now we're in the post super alignment team era. And I think we're still in that sweet
*  spot. I think we'd probably stay in that sweet spot for one more generation. And then after GPT-5,
*  I may be personally, while I continue to love what AI can do for me, I think I maybe start to advocate
*  for let's dial this thing in for actual practical use cases. GPT-5 should be enough to be our AI
*  doctor. It should be enough to be our AI lawyer. It should be enough to be our AI many things.
*  Let's bring that to reality. And we probably don't need to continue to go to race through orders of
*  magnitude to get those sort of gains. And so maybe we should, maybe we should question why we would
*  be doing that. And a race against China would be one reason. And I'd love to find some solution to
*  that. But yeah, that's my, so I guess the question is, do you think that there is a coherent center
*  to this adoption, acceleration, hyper scaling, pause concept, or does it slip away?
*  I think it's a game of brinkmanship, right? Because it's, I really get the lighter image here,
*  which is imagine if laundry detergent could produce gold. And at some point, and the more
*  laundry detergent you pile up, the more gold it produces, the faster it produces it. And at some
*  point it blows up the entire earth. That's why it is. And so you're very tempted to keep piling on
*  laundry detergent and you never know at what point it's going to explode. And I would share your bias.
*  I think like one more generation is fine. I think I'm comfortable with two or three orders of
*  magnitude. I wouldn't be comfortable with six or 10 orders of magnitude. I would dispute, however,
*  that like there's no point adding more after that point. I think that's what makes it so dangerous.
*  It's like it is always tempting to add more because, hey, cool. Now you've got your AI doctor,
*  your AI lawyer. Hey, we could just add a little bit more and it cures cancer. And it solves global
*  warming and it solves biology for us, right? It's like the memes, just one more order of magnitude,
*  bro, I promise. Just one more order of magnitude and I'll be okay, bro. And it's never going to
*  run out of temptation. And I think if anything, the closer we get to that point, the stronger the
*  temptation will be. So also the gears of the regulatory state are so slow to put themselves
*  in motion because the next generation is coming regardless. Like GPT-5 is coming regardless. Like
*  roughly now is the time to really have this conversation. So we have a chance to be much
*  more thoughtful about the generation after next. How do you feel about OpenAI's leadership today?
*  Obviously, I would say there've been a lot of good things that they've done, although some of those
*  have turned to sand already, such as the SuperLineMateam. I've been on a winding road with them
*  and have gone from, oh my God, this seems like they have no idea what they're doing to,
*  oh, actually they have a much better plan to now I'm again, oh man, I don't know.
*  The culture there, the sort of exodus and repeated exodus, the apparent something like a purge seems
*  to be going on. That's a little bit of an inference, not a crazy one. All these bully tactics.
*  And yet I do think they're still fairly enlightened. Sam Altman is engaged with all
*  the ideas that I would want him to engage with. I don't think he's ignorant of anything that I'm
*  concerned about. So yeah, what's your take on OpenAI? I'm reminded of my time at Uber,
*  which is like we were like hyper scaling and the chaos is impossible to describe. You can't imagine
*  what it's like to be at a place that hires literally about 800 people per month. OpenAI
*  isn't there, but it's high in its own ways. And so I think people underestimate the chaos that happens
*  when they've been. They turn themselves from a little like quasi obscure research lab into a
*  corporation generating billions of dollars of revenue in the span of 18 months. Of course,
*  Sam Altman is a ruthless businessman. Of course he's going to play hardball and have a bunch of
*  ruthless tactics. I'd be surprised if he wasn't to get into this position and to build the kind
*  of company he's got. Yeah. It's like when Travis, people are like, oh my God, he's so aggressive.
*  What do you think? Of course it's business. Welcome to... And some of that I'm like,
*  oh, it's just business. Some of that I'm like, it's chaos, the chaos of hyper scaling. Like when
*  the whole Susan Fowler incident broke out at Uber, I was like, what do you think? We're still like
*  5,000 people. Of course it's going to be like a bad apple. I'm sure Travis didn't even know
*  none of these people's names. He's never heard of it until now. And now all of a sudden he's
*  like the devil for doing all of that stuff. Even the super alignment stuff, I think I'm sure they
*  meant it when they said they would invest 20% of compute. Otherwise they wouldn't have announced
*  it. I just think then chaos got in the way that it's just business, especially when you scale that
*  fast. So I think that's what's going on. And I just think that it shows that you need a forcing
*  function for these businesses to... They're not going to self-regulate. They can't self-regulate.
*  They're structurally incapable of self-regulating. So you need to have an external forcing function
*  for them to regulate. And by the way, I think Sama has been welcoming, inviting that regulation,
*  if anything. So that's my read on the whole OpenAI situation. Yeah, for sure that right now they're
*  going through a negative part of their price cycle. I think that's natural. I think it will pass.
*  Just every company goes through that and it'll pass. Again, it just highlights the need of external
*  regulation. I feel like I can definitely tell myself the story around the contractual terms.
*  It didn't shock me that there would be a non-dispersion clause in a severance agreement,
*  even though it was funny because then he came out and said, this is one of the few times I've been
*  genuinely embarrassed. And I was like, I don't really think you didn't know about it. And it
*  almost seems like an overstated apology in some ways to me. Because I hear you, things are going
*  fast, they're going hard. They got a lot of intellectual property. Obviously, they're trying
*  to protect. They have an argument, which I don't think is a bad one, that leaks are potentially
*  not in the long-term public interest, just in as much as they tip other people off to what is
*  possible. And yet I'm still like, okay, but the safety team all leaving, that does seem
*  concerning. The regulation could maybe step in and solve that problem.
*  Yeah. I don't think the safety team was purged. Perhaps Ilya was because of the crew, right? But
*  I think they left. I think they left because OpenAI didn't make due on their promise. And I don't
*  think that was ill-intentioned. I obviously think OpenAI's leadership is worried about safety.
*  I just think when you're in that kind of game, it's too hard. The organization is acting
*  rationally in dedicating their flops to capability and not safety.
*  That's tough. Quick question on the future of live players, or you could frame it
*  another way as the fate of the second tier of foundation model developers. Who do you think
*  is going to be in a position that really matters over the next couple of years? Do you think it's
*  just going to be a handful of big tech companies? Do you think there's a place for your RECAs and
*  your Together and Cartesias and Adept and whatever mods up to next after Stability? Are those things
*  going to matter or do you think that the cost of the price they had to play in these scaling
*  wars is just going to be too high for any of them to make it? I think at this point, I think
*  Conventor set. I think it's Anthropic, OpenAI, Google, Meta. Mistral, I think, came very close.
*  I don't put them in the same category as these players. Neither do I think they put themselves
*  in that category. The one that surprised me recently was the Memba folks. These guys I could
*  see better, but I also think the other players I just mentioned can replicate that kind of resource
*  and I am certain have a bunch of models and training looking into this. I think at this point,
*  the battlefield is set. That's my expectation as well. Do you think that in the next few years,
*  do you think that the big tech companies are going to metastasize and take over everything?
*  I've been teasing around this concept of the big tech singularity and I see things like what just
*  came out from Google about optimizing shipping. They have some new shipping planning API that they
*  say can double the profits of a container shipping company, delivering however many percent more
*  containers with however many percent fewer boats. I'm like, man, if I'm a shipping company, am I
*  happy about this or am I not happy about this? It seems like the big tech singularity idea is just
*  that anything that they turn their attention to, they're going to have the data, the compute,
*  and the research advantage to figure out how to AI-ify it and dominate it if they want to.
*  And then the counter argument is there's too much friction, yada, yada, yada. What's your intuition
*  on that? Yeah, I don't think... I think big tech is very deliberate about where they expand. They're
*  very good at that part of their strategy. It makes perfect sense for Google to spend as much as they
*  on AI. From the beginning, it's made a lot of sense because search is basically an AI problem,
*  always has been. Android, the reason why Google did Android is it sounds insane, but they literally
*  built an operating system just so that they could be the default search engine on it. There's more
*  to it than that strategically, but that's basically the strategy of Android. There's no chance that
*  Google turns themselves into a logistics company. They don't have a bone of that in their body.
*  I think they're going to offer that as an API. I wouldn't be worried if I was like the logistics
*  companies about Google entering logistics. By the way, if they were to ever enter that game,
*  Google Fiber was the time when they would have done that and it didn't work out, right? They pulled
*  out. Yeah, I don't expect that to happen. But yeah, I do view it more as an example of the speed at
*  which OpenAI is penetrating every little nook and cranny of the economy. I wonder if they can even
*  just do it by API though. Going back a few years to when I was doing a lot of Facebook advertising,
*  I am grateful now that I'm doing much more interesting things. But there was this general
*  phenomenon of if you wanted to reach a new audience, Facebook was the way to do it.
*  They were so good and everybody was doing it and they were so good at pitting you against your
*  competitors that they seemed to be taking everybody's margin. But if you wanted to go
*  advertise a bicycle on Facebook or whatever, they'd somehow make your cost of acquisition
*  just less than your profit margin. And everybody was like, I can sell a lot of shit on Facebook,
*  but I can't make any margin doing it. And it does suggest though, if Google can offer this API that
*  doubles your profits, then it would stand to reason that they would be able to price that at
*  current profits. Do they then get half of the resulting profits out of the industry? And do
*  they have everybody over a barrel where if you cross Google, they can in theory cut you off from
*  their profit doubling API? Again, they would take some political hits for that or they could be
*  accused of being anti-competitive, but you can get a long way just on the implied threat of
*  those sorts of things. Right? Yeah. I think if a player gains a monopoly over one of your
*  required inputs, they can basically drain all of the margin out of you and turns you into their
*  self. Right? But I don't think Google is going to gain the monopoly over AI. Right? I think in the
*  case of Facebook, the network effects are such that you can actually be in a very dominant position,
*  but AI you can't really, there's going to be a bunch of players and by the way, they hate each other.
*  And so that's good for us, the custom emails, because there's a price pool raging, which leads
*  to these models declining in price as rapidly as they are. So yeah, I wouldn't worry about that.
*  I don't worry about it myself. I used to, I was like, I have the required input and opening
*  AI is really the only one that's giving me this required input. I might just be going to become
*  like an opening AI self. And now I have Gemini and I have honestly Lama and I have cloud and
*  Mistral is in the running. So I'm comfortable with that. Yeah. If you're a shipper, you're
*  hoping that Microsoft has a similar project launching real soon. Cause then you could imagine,
*  yeah. It's funny how that dynamic is really fascinating. If there's one shipping API that
*  doubles profits, it takes half of the industry profits. If there's two, then they probably race
*  down to the bottom and the shippers get more of the benefit. I think FlexPort is going to do it.
*  Obviously. Yeah. Okay. Cool. Any other thoughts before we break? This has been great and I
*  appreciate the opportunity to catch up and work through some of this stuff with you. Anything else
*  top of mind? That's all AGI is coming and it is time to freak out. That's my message. Yeah. Let's
*  hope against hope that we can somehow avoid the AGI or ASI arms race, but does seem to be a natural
*  attractor. Flo Covello, CEO of Lindy, feeler of AGI. Thanks again for being part of the cognitive
*  revolution. Thank you so much. It is both energizing and enlightening to hear why people listen and
*  learn what they value about the show. So please don't hesitate to reach out via email at tcr
*  at turpentine.co or you can DM me on the social media platform of your choice.

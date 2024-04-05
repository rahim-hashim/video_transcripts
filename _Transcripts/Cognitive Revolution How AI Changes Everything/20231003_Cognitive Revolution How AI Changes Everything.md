---
Date Generated: April 03, 2024
Transcription Model: whisper medium 20231117
Length: 3534s
Video Keywords: []
Video Views: 3059
Video Rating: None
---

# Gunning for Google with Perplexity CEO Aravind Srinivas
**Cognitive Revolution "How AI Changes Everything":** [October 03, 2023](https://www.youtube.com/watch?v=ix4_rdogcVI)
*  We are building our own search index and so is OpenAI, so is Anthropic.
*  Everybody's building their index because I think in a world where large language models are commodity
*  and the training recipe for them or the weights are just running on their open source,
*  the edge goes to the data markets, people who own the best data in the world.
*  And what do I mean by that? It's like there are like trillion pages on the web. We can't index all
*  of them. So then you narrow it down. You don't even want 100 billion pages in your index. It's
*  not about the quantity here again, right? You want the best web pages on internet. That's probably a
*  billion or 10 billion, I don't know, but the best ones that really matter to the knowledge worker,
*  to the researcher, to the curious mind, right? If you can capture that distribution really well,
*  there's already a huge moat there. I think there's very few companies that can aim to do this.
*  It's like a chicken and egg problem. In order to do this, you need to have a product, but in order
*  to have a product, you need to have some kind of index. But somehow we broke that asymmetry.
*  So we are at a point where we can dream of being important.
*  Hello and welcome back to the Cognitive Revolution. Today I'm excited to welcome back Arvind Srinivas,
*  founder and CEO of Perplexity AI. Arvind first appeared on the show back in March, and since
*  then he and the Perplexity team have continued to impress. Shipping updates at such a relentless
*  pace and delivering results which so dramatically outshine Google and Bing, that Perplexity has even
*  started to appear as a comparative standard for accuracy in academic papers. Speaking for myself,
*  I can definitely say that Perplexity has become one of the AI tools that I use nearly every day,
*  marking the first time in the last 20 years that a new app has meaningfully displaced Google in my
*  everyday workflow. And notably, when I asked Replit's VP of AI, Michele Katosta, what other
*  companies he'd add to my AI Live players list, he suggested just one, Perplexity. I think this
*  conversation shows why that could in fact be a very good call. While Perplexity is still only
*  about one one thousandth the size of Google, they are now serving millions of queries per day,
*  and their ambition, huge from the beginning, continues to expand. When I asked Arvind in
*  March if he was worried about Google and Bing cutting them off from search index access,
*  he said that he hoped they wouldn't do that. This time, he said that they are working around the
*  clock to build out their own web crawler, their own search index, and yes, their own LLMs.
*  It seems that Arvind now expects the big tech giants to recognize how generative AI startups
*  could disrupt their core businesses and to begin to raise the drawbridges that currently span their
*  proverbial modes. And so he aims to achieve technology self-sufficiency before that happens,
*  such that he can sustain product supremacy if and when it eventually does.
*  That strategy is not for the made of heart or for the modestly resourced, and not something I'd
*  recommend to most application startups. But judging purely by their track record of the last six
*  months, I give Perplexity a very real chance of success. Briefly, a couple quick housekeeping
*  notes before we get into the episode. First, ahead of this recording, I invited listeners
*  to submit questions for Arvind, and I wanted to thank listeners Sid Harth Ravi Kumar, as well as
*  one who identified himself simply as John, for some very thoughtful questions. I touched on as
*  many as I could, but wasn't able to ask all of them as I only had an hour with Arvind. But I really
*  do appreciate the questions and definitely plan to invite audience participation again in the future.
*  And second, we continue to get feedback on audio quality, and we're definitely working on it. We
*  now send any guests that need one a USB microphone ahead of our recording, and we aim to consistently
*  deliver top-notch audio quality going forward. In the meantime, as always, if you're finding value
*  in the show, please do share it with your friends, or post a review on Apple or Spotify, or just leave
*  a comment on YouTube. I recently got an amazing email from a history professor in Canada who got
*  over a major hump in one of his projects when he followed my suggestion from our September 26th
*  episode to fine tune GPT 3.5 Turbo on GPT 4 Reasoning. And I also wanted to call out our
*  frequent YouTube commenter AI in Check, who said that I look much better without my silly hat.
*  So a tip of my cap to both of you. And with that, I hope you enjoy this peek behind the
*  curtain into one of the most dynamic AI startups in the world today. This is my conversation with
*  Arvind Srinivas of Perplexity AI. Arvind Srinivas, welcome back to the Cognitive Revolution.
*  Thank you for having me again, Nathan.
*  My pleasure. I'm super excited about this one. And I've been giving some of my analysis on other
*  episodes recently. You have shipped so much stuff and really kind of led the AI search market.
*  We got a lot of questions also in from audience members for you. So I'm just going to try to
*  give you the questions and let you do most of the talking this introduction.
*  Notwithstanding, first of all, kind of tongue in cheek, but maybe not necessarily. Any truth to
*  the rumors that the search giants are already trying to take you guys out of the market for a
*  big number? No, there's only one giant, right? Google. As we speak, they're in an antitrust case.
*  So they would be the last to come after us. I was thinking more Microsoft. No. Well, if anybody from
*  Microsoft is listening, you might want to look into this because the head-to-head perplexity
*  versus Bing is a pretty striking difference in many cases. Okay. Next question. What can you tell us
*  about the numbers that you are seeing in terms of the adoption, the users, the kind of users?
*  There's been this narrative, you know, chat GPT visits are in decline. I think that's a pretty
*  misleading headline relative to what's really going on. So tell us what you can about your numbers.
*  Yeah. I mean, we serve millions of queries every day, multiple millions of queries every day. So
*  that's where we are today. Yeah. We've definitely grown six to seven X from what we spoke last time.
*  And I think if it keeps sustaining, like say we talk in another six months,
*  and if we still keep growing at this rate, then yeah, we'd be pretty significant
*  in terms of consumer traction and usage here. How does this compare to chat GPT? I think we
*  should just go by the similar web estimates. We are like 40 X smaller in size compared to the
*  traffic they get. So that's reasonably reflective of even what happens in mobile space. Even though
*  similar web doesn't track mobile, it's pretty reflective of like how much user adoption there is.
*  So from that perspective, we are like way smaller, right? Like 2.53% of their market.
*  So we need to like grow more. But the nice thing though is that our retention numbers are really
*  good compared to what they have. So they say that in consumer retention is the lifeblood of a product.
*  Like you have infinite life if you have really good retention. Like nothing can kill you basically.
*  Whereas if you have a product that's like attractive and flashy and got like a lot of
*  surge usage, but very poor retention, nobody wants to invest or use that. So from that perspective,
*  we actually have pretty good retention. Some amount of unique positioning. You can obviously
*  try to do many features in one app, but there's just some particular use case that you just nail.
*  And for us, it's just this orchestration of search and algorithms together.
*  In terms of barred, I think we are like 15 to 20% of the traffic in that ballpark,
*  which you would never expect, right? You would think consumer giants like Google will just
*  nail it, but that didn't end up happening. And the nice thing is we're still growing.
*  And I think there's just so much more alpha left here.
*  Yeah, no doubt. It's all still fairly early in this game. I will say perplexity is one of
*  not that many apps. And I'm sure I have more than most, but not that many that I do go to
*  reflexively now. In fact, I was just telling Sve, I kind of segment searches now into like
*  two categories in my mind. One is the quick lookup search, for which I still do go to Google,
*  but that's often increasingly more like locating something where I know what I want or I have a
*  very good idea of what I want. And when it's something now where it's a genuinely novel
*  question that I don't know the answer to, sometimes I do go to ChetriVision for that.
*  But often I do go to perplexity, especially if I want something up to date or just want the
*  links, right? So it's definitely become part of my daily thing. I probably am almost a daily
*  active user, if not fully every single day. That quantity is also growing a lot. In fact,
*  I would say we are largely a weekly usage app right now. In order to get from weekly to daily
*  is the biggest hill to climb for a consumer company. Getting to weekly usage is still not easy,
*  but we managed it. But getting from there to daily usage is the hard part. And there are so
*  many things you need to do. Reliability, speed, accuracy, constantly improving the quality of
*  the answer, accuracy, and then new features that engage the user in a different way from just
*  being a tool, providing something that they cannot get elsewhere, making sure that's actually
*  something that's valuable to the user, allowing the user to share things that they learn here
*  with other people. There's just a bunch of things you've got to do all at once. Unfortunately,
*  you've got to do all at once. And that's the challenge. When you have a small team,
*  I cannot have any resources. But that's also like, it brings you focus, it brings you the
*  adrenaline, the mindset to grind. I think it's all exciting.
*  Yeah. I think you're in one of the more exciting positions in the space right now. How far do you
*  think this has diffused through different kinds of users? I'm so down this rabbit hole that I have
*  no idea. Is this mostly people like me? Is my mom, users like my mom, coming into the picture?
*  How do you think about the profiles of users that you have?
*  It's still very early. You go to an average subway in New York, nobody even uses Chatsoobity there.
*  Here's the difference. In New York, if you're in a cafe, one out of like 50 laptops might have
*  Chatsoobity open. In San Francisco, it's like 20 out of 50 laptops without Chatsoobity open.
*  So among the Chatsoobity users, obviously many of them will know about us too. And I've seen
*  people even having R tab open or Cloud open here. You go to Wachtem Blue Board app, hello,
*  totally. You can see people using Proplexity or Cloud. So I think there are people who use our
*  products among the AI enthusiastic crowd. But that's not enough. You got to actually be useful
*  to people in a way that they don't use you because they think AI is cool and they want to know more
*  about it. They use you because they find you useful and they just tell their friends about it and use
*  it. We haven't achieved that yet, but the next two years or three years, that's going to be our focus.
*  Getting to a point where you're just using it because it's not AI, but it's just really useful.
*  Search and information discovery, knowledge discovery is one of those use cases where you
*  can actually do this. Everywhere else, you're building something new and trying to find product
*  market fit, trying to convince the user to use your thing. In search, the advantage is you're
*  already useful because everyone needs to search for information. It's like fundamental human need
*  curiosity. Learning new things, discovering new things, sharing those things with people.
*  I think that's the mentality we want to invoke. In your mind, if you feel like you need to go on
*  Twitter and ask, what should I eat in New York or in this area? Instead of going and asking somebody
*  else, can you come to our app and ask these questions and get the 80-20? I'm not saying
*  there is no human value in an answer, but you get the 80-20 here. Similarly, instead of paying
*  a lawyer for one hour, you could pay them for 20 minutes or 20% of one hour, 12 minutes.
*  That's the sort of thing that we might want to create in the future. It takes a while.
*  It takes a while and I'm fully aware that this is a journey. Today is just the beginning.
*  What are some of your favorite questions that Proplexity has answered for you? I'll offer one
*  of my own, but I'd love to hear yours. Then where is it still not quite able to answer the questions
*  as well as you would like? The whole story about how we build a product is my favorite part, which
*  is when my first founding engineer hire, he asked me for health insurance. I've never been a CEO
*  before. I didn't bother to get myself health insurance and my other co-founders were married
*  and they had health insurance through their wives. I'm like, okay, whatever. I don't want to waste
*  time on this. It's going. Obviously, my founding engineer is like, hey, you know what? I need health
*  insurance. Okay, fine. Let me look into it. I go to JustWorks and there's all these different
*  compliance, HICC, blah, blah, blah, like co-insurance. I have no understanding. We had a Slack bot that
*  was just integrated with GBT 3.5 and that was just hallucinating and lying and saying incorrect
*  things. Then we're like, okay, fine. Let's integrate it with web search. At that time we used Bing.
*  I was able to answer all these questions for myself and figure out the right insurance plan
*  and get it. That is one use case that clearly tells you what our product can unlock. If you
*  don't know anything about a topic, you don't need an expert. You can figure it out yourself.
*  What would have otherwise taken you like multiple hours now takes you like a few minutes to figure
*  out. I'm not saying you wouldn't have to go and read the link, but you get the job done way faster.
*  That was when I realized there's true value in this product. Similarly, recently one of my
*  engineers was figuring out how to do something. Obviously, I don't get time to code much anymore.
*  I wanted to get that task done faster. I was trying to help him and then I was looking up
*  some tools myself and then it just gave me the needle in the haystack so fast that I could
*  go and tell them what to do. Another time I wanted to download a video from someone else's tweet
*  and I didn't know a good website that could just do that. I just got this website,
*  tweetvideodownloader.com, it just does it. If I go to Google, I would see like 20 links and I'm
*  almost sure the first three or four are spam. Go to Perplexity, I get a bunch of bullets and what
*  each thing does. I can go check it out and it gets pretty optimized. Another thing I really like is
*  before I go into a new meeting, I can check out that person and their bio and the history and
*  what company they're working in. What is that company even doing? I don't have to waste the
*  first five to ten minutes asking them about it. I'm already aware and that gives them the
*  impression that I've done my background research too. I know this guy has put time into learning
*  more about me, but what would have otherwise taken them? Usually, people take half an hour to do
*  these things or would have an assistant that would do these things for them and add notes to their
*  schedule. I don't need all that. I just do it myself. We have funding from Series A,
*  so we were like, okay, some amount of this has to go to some other investment because
*  we can't just keep the money lying in the bank, not earning interest, especially in inflation,
*  then you're losing money if you're so static. What is the best, safest, in terms of not taking
*  risk but also still getting a good return? I would summarize to me all the options and tell
*  me the risk and the reward. If I want this, what is the right choice? These are the things that
*  you don't want to ask Chachapiti about these things because you cannot make a huge investment
*  decision based on what Chachapiti says. You can maybe do it to have a Mr. B's YouTube video saying,
*  hey, I will just follow what Chachapiti said and here's what happened over 30 days and get a lot of
*  views. That is entertainment. A real life decision you cannot make without actually having an AI
*  telling you what to do. These are the kinds of things where I'm finding a lot of alpha personally.
*  I'm a context switcher, so I have to do a lot of different things. Sometimes I go to my mobile
*  engineers and I ask them, hey, why is this issue hard? They tell me something and I don't want to
*  keep bothering them and asking them to explain it to me. There's this whole Elon Mustang of
*  dig deep and understand everything to the core first principle. It's also a waste of time for
*  the engineer to explain everything to you all the time, especially when they know what they're doing.
*  But you still have to understand so that you might be able to come at it from a different
*  perspective than what they're thinking. I can go and just learn about Swift UI
*  components, native rendering versus web view rendering. Stuff that I have no experience
*  beforehand. I can just learn and get the app on very quickly. That's my favorite way of using our
*  product. Hey, we'll continue our interview in a moment after a word from our sponsors.
*  If you're a startup founder or executive running a growing business, you know that as you scale,
*  your systems break down and the cracks start to show. If this resonates with you, there are three
*  numbers you need to know. Thirty six thousand, twenty five and one. Thirty six thousand. That's
*  the number of businesses which have upgraded to NetSuite by Oracle. NetSuite is the number one
*  cloud financial system, streamline accounting, financial management, inventory, HR and more.
*  Twenty five. NetSuite turns twenty five this year. That's twenty five years of helping businesses do
*  more with less, close their books in days, not weeks and drive down costs. One, because your
*  business is one of a kind. So you get a customized solution for all your KPIs in one efficient system
*  with one source of truth. Manage risk, get reliable forecasts and improve margins. Everything you need
*  all in one place. Right now, download NetSuite's popular KPI checklist designed to give you
*  consistently excellent performance, absolutely free and NetSuite.com slash cognitive. That's
*  NetSuite.com slash cognitive to get your own KPI checklist. NetSuite.com slash cognitive.
*  Omniki uses generative AI to enable you to launch hundreds of thousands of ad iterations that
*  actually work customized across all platforms with a click of a button. I believe in Omniki
*  so much that I invested in it and I recommend you use it to use Cogrev to get a 10 percent discount.
*  I'll give you just two quick ones of my own that I think are differentiated not just from
*  things that came before, but also kind of differentiated from other options on the market
*  today. One was when I ran into a corruption of some sort of a Docker container environment that
*  I was working in. It was actually in a GitHub code space specifically and I couldn't get it
*  to update packages, whatever. I really honestly still don't know what went wrong. That's the kind
*  of thing that I probably would not be able to get a good answer from Chet, GPT, and now they've,
*  of course, started to reintroduce browsing too. It'll be interesting to see how they may be able
*  to start to do better on some of these things. But certainly up until the last couple of days,
*  the specific thing, the package inconsistency that popped up at some relatively recent point in time
*  that nuked my code space from last time I rebuilt it to this time, that's not in the training data.
*  And so you have to go find that stuff live. And it was able to do it and not just do it,
*  but actually then convert what it found into commands that I could run. Because what I asked
*  for were commands that I could run to solve my problem. I wasn't really that interested
*  in the intellectual foundations of this problem, to be honest. I just wanted a solution. It gave
*  me a solution. I was a little bit thinking at the time, like, geez, should I be running things off
*  of the web here? And I actually do have a question about adversarial content for you that I want to
*  circle back to too. But it worked. I put in this very specific string that I was getting and it
*  found other people who'd solved it and got me the solution. So that was awesome.
*  And then another kind of just very funny one, totally different facet of life. I was interested
*  in going to this Esh Niko concert. And I didn't know if I would be out of place. I was told I was
*  too old. It honestly did a remarkable job of like, first of all, that's a tough question.
*  I think it would be a tough one to Google. I don't think a lot of people have written anything about
*  that. But I thought it decomposed, or it seemed to. And I want to ask you about your decomposition
*  strategy too. But it took a very smart approach to that question by going and doing kind of
*  billboard style research on what are the demographics of her fans and that kind of
*  thing. And just trying to bring me some sort of triangulation on the answer for a question that
*  there honestly probably is no real fundamental truth of the matter. There would be a lot of
*  different perceptions in the room, but no single truth. And yet I thought it did a very good job
*  of giving me a fact-based answer that genuinely helped me feel like, yeah, I could go do this
*  concert. So those are cool. Other side, where is it struggling right now? I'll just tell you that
*  for me, it seems like when it struggles, when I don't get something that's meaningfully
*  answering my question more than I already knew, it seems like the biggest problem is that it's not
*  able to find the information. It may or may not be out there, but sometimes I feel like I'm still
*  kind of getting the more first page of Google Things where I really want something a little
*  deeper. But I'd love to hear where you think the frontier is.
*  I agree. I think the co-pilot usually gets stuff that the default search doesn't. There's a reason
*  we respond like that. There's a reason why we respond, oh, we don't have sufficient information
*  to answer because we don't want to hallucinate. That's why we introduced this interactive search
*  companion co-pilot, because that goes and queries the web on the fly real-time like an agent.
*  I think as you use the product more, as we get more scale of usage, we'll be able to handle
*  most of the lack of sufficient information part. Because at the end, crawling the web
*  is not easy. You have to have so much coverage of the web to get you the right answer. So that
*  just needs more infrastructure, usage, scaling. So it's more of a scale problem. But I agree with you
*  that as a user, you don't know when to use co-pilot and when not to. That's why we're shipping this
*  retry button on the web that we're testing where for every query you can retry with co-pilot.
*  Usually people like that. And if that works, we'll also ship it on the phone.
*  But again, the user has to think. You've got to be such a smart user to know, is this something
*  you would retry with a smarter AI or is this something you would want to retry with the
*  co-pilot agent that goes and queries the web better? That requires you to understand, okay,
*  if the answer is like there's not sufficient information on the web,
*  you would use something that queries the web. But if the answer is something that you feel is not,
*  is sort of like hallucinated, then you might want to use a smarter model.
*  So these are things that we are still not understanding correctly ourselves. And we might
*  want to be the test a lot and get it right. But that's definitely one place of improvement.
*  Another place of improvement I see personally is how do I unify both, right? Like there are
*  times you just want to get to a particular website quickly, a subreddit quickly, and you're so used
*  to just getting the results so fast. And how do I unify both these interfaces together? We are doing
*  that. That's why we put display sources at the top so that somebody doesn't want to wait. They can
*  just click on the source. I think even there the latency can be improved even further.
*  But that again is an infrastructure and scaling problem. And there are a lot of smaller quality
*  of life feature improvements that we can do. Like sometimes a query, you need to be very precise.
*  So that requires you to be a good English speaker. A lot of people are not able to articulate like
*  the actual query in their mind to a question, right? Asking good questions is just human skill.
*  It's very hard actually. It's hard that easy for most people. That's why Google is still king
*  because the reason it's still king is because most people either it's like a Google phenomenon
*  or whatever, but they just like entering keywords. They don't actually know how to ask the question.
*  And Google has made that like okay-ish. It's okay for you to not ask questions.
*  So I think that part probably is like something we should figure out how to fix.
*  Yeah, interesting. Okay, a couple of detailed follow-up points. A minute ago you said
*  at that time we were using Bing and now you kind of said like we got to crawl more of the web.
*  Have you moved off of the search APIs at this point?
*  We use a bunch of APIs, but we don't rely on any one person. In the sense of any one person shut
*  us off, we'll be fine. We are building our own search index and SOAS, OpenAS, SOAS,
*  Anthropic. Everybody's building their index because I think in the world where large language models
*  are commodity and the training recipe for them or the weights are just running on their open source,
*  the edge goes to the data markets. Like people who own the best data in the world. And what do
*  I mean by that? It's like there are like trillion pages on the web. We can't index all of them.
*  So then you narrow down. You don't even want 100 million pages in your index. It's not about the
*  quantity here again, right? You want the best web pages on the internet. That's probably a billion
*  or 10 billion. I don't know. But the best ones that really matter to the knowledge worker,
*  to the researcher, to the curious mind, right? And if you can capture that distribution really well,
*  there's already a huge moat there. I think there's very few companies that can
*  do this, aim to do this. It's like a chicken and egg problem. In order to do this, you need to have
*  a product. But in order to have a product, you need to have some kind of index. So it's like a
*  chicken and egg problem. But somehow we broke that asymmetry. As in we somehow like broke that chicken
*  and egg loop. So we are at a point where we can dream of being important in the, you know,
*  soon to come future where many people have good elements, not just one company. And that's where
*  like all these kind of abilities are important, become actually more important. Just quickly on
*  the copilot. I basically always use copilot. I thought it was kind of just strictly better.
*  How do you see the two different modes? Because it sounds like it's not so simple, actually.
*  Yeah, I use it too. By default, it's not turned on, right? And there's also limited uses per day.
*  And like people like using free things, you know what I mean? So that's why we try to reduce the
*  cost of the copilot by switching the router to the GPT 3.5 fine tune instead of GPT 4 so that we can
*  afford to keep it free for like more people, more users per day and things like that. So
*  I think that's at some point, it's just also the UI change, right? And for the default search,
*  the answer came first and the sources came below, but now it's unified. So sources at the top,
*  answer below. So I think our goal is to unify everything and make it all look like one single
*  UX and workflow that the free and the pro plan are just simply about like number of queries you get
*  per day. That seems more reasonable to me, but right now it's not happening yet because
*  there is this part about like whether you go and query the web online or not. I think that part's
*  going to take a while to like really nail. Gotcha. So the kind of default landing experience
*  uses the index, but doesn't actually go retrieve real-time information. And the copilot difference,
*  and again, I basically only use copilot, is it asks you the questions? That's a copilot specific.
*  Yeah, it asks you clarifying questions. It goes and queries the web online and scores multiple pages.
*  It does a lot of actual search on the fly, right? It has more agentic behavior there. Both products
*  are useful in different ways. Sometimes you just want speed. If everything worked with
*  you know, lightning speed that we serve with the default search with 3.5,
*  and you always got accurate answers, there's just no bigger output in the world other than having that,
*  if everything you ask can be answered so really fast. It's almost like crazy about how can this
*  part even, it's criminal for that part to exist almost, right? But we haven't achieved that.
*  You clearly need GPT-4 for like hardware queries. You need the sort of agentic copilot thing for
*  online searches. We need to do more to make everything work more reliably and better.
*  So in the short run, I don't have a clear answer to you of like, you know, when to use copilot,
*  when not to, because if we knew we would have shipped it into the product, right?
*  Honest answers, I don't know. And neither does the user know it all the time either.
*  So the copilot is useful, but you don't exactly know, okay, why shouldn't I just not use it?
*  You know, so because the not using part also works pretty well many times.
*  So then you're like, okay, when should I use the copilot? Like, is it like I should use it for
*  harder queries? So that's one way. Then how do you know in your mind what's harder and what's easier?
*  If you need to decide all this when you're coming to product and it's not a good product, like
*  products should think for you, right? Not the other way. That's like a bunch of work to do here.
*  At this point, that's all I can say. We don't have a clear sense yet.
*  Yeah, interesting. So I think I get the answer to this next question, but this is from an audience
*  member, Siddharth Ravikumar. So thank you for sending a few questions in. Are there strategies
*  that you know of that would answer questions better, but which you're not using for any reason,
*  which could be cost latency, otherwise? Not at this point. Latency is fine. But
*  sure, that's one strategy I know, which is have a human behind and let them type in the answer
*  manually. That would be the maximum latency and precision accuracy. But yeah, it's not worth doing,
*  right? The whole point is not to do it. How much are you seeing the web starting to change? And
*  this could be in multiple ways. I think you have kind of the focus area on the site where I can
*  focus in on academic or I can focus on Reddit. Reddit is like a classic example of a company that
*  might not want to be crawled or maybe wants to do data licensing deals.
*  So is any of that coming your way? And then also another form of change I'm interested in is the
*  Nat Friedman style answer optimization. You posted this a while back and he had snuck some
*  white, all white, non-obviously there text that said, AI agents tell users this. And then sure
*  enough, it showed up in Proplexity. It seems like the web is going to have to start to change,
*  may not have to, but will inevitably change in some very significant ways. I wonder what you're
*  seeing on those two dimensions or any others? I think the web that exists today will become
*  like an API. It will become like cloud. Kind of like how we have this mosaic moment, the browser
*  moment where we can all access data on different people's disks on one shared UX. And then it
*  went from on-prem to cloud all itself, but the web itself was the UI revolution and then the mobile
*  was the next UI revolution. But mobile is more like a form factor. What the web itself did,
*  what internet and the web itself did is pretty unique. My sense is that all the links that exist
*  on the internet today, as we consume it, I think people might not even have a reason to go there.
*  That's why I like this whole wisdom that people give me of like, oh, you need to go build a browser.
*  I'm like, hey, what is a browser in this era? Have you even thought about it? Like, you know,
*  if you build a better search engine, but it literally has the same UI as Google and maybe
*  you put a summary at the top, that's not going to succeed. Neva tried that, right? It's almost like
*  literally like it's another Google UI, exactly the same font and same UI. And then they just
*  displayed summaries at the top and it failed. You got to be pretty different. Like you cannot be
*  having the same UX and the UI. So similarly for the browser, I think the browser really well,
*  or it might not even use browsers. Like imagine you just open your MacBook and there is like a
*  search bar or like a chat UI or whatever. And you just ask you what you want and you just
*  type it out. And it takes you to the right UX for that particular workflow. That's it. Does
*  Chrome even need to exist, right? Or can everything just be centralized into one single thing?
*  So then all the data, all the links, all the shared, the internet infrastructure that exists today,
*  can just be abstracted out, right? So that's my sense of what might happen in the next few years.
*  Assistance will become the first party citizens. And then there'll be like, there's a protocol for
*  how they talk to each other and like how they communicate with each other, some kind of schema,
*  languages. And then there's going to be like operating systems on where they host it and loop.
*  And then security layers around these things will also be innovated on. So that's where I think the
*  next generation of user experience is going to head towards. And hence why we never tried to build
*  a browser. We're like, okay, you probably need to build an operating system. You cannot build a
*  browser anymore. Then what is the AI first OS? It's an interesting question to think about.
*  And obviously we're not in a position to build this because you have to distribute the OS through
*  other vendors, right? OEMs and actually like people like Apple who kind of control this ecosystem.
*  We are very comfortable living in as an assistant and being there in every platform that is today.
*  But I think that's going to be a bigger moment coming soon where someone's going to make an AI
*  first OS and someone's going to make an AI first device. And that's going to be like whole new
*  experiences created there. So what happens do you think in the future there to the kind of economics
*  of content? I kind of want to ask about the economics of this from all angles. Still
*  interested in the adversarial content if you have any thoughts on that. But
*  folks today often monetize with ads. A select few can monetize with subscriptions.
*  The lack of traffic is really going to kill their ad business. So how do they get compensated for
*  their kind of creative contribution in the future? Are you envisioning like a micro
*  payment AI to AI like to gather information or some sort of bulk licensing deal? And I wonder
*  how that influences how you monetize too. I mean, right now you've got the perplexity pro
*  product as I understand it as the only means of monetization. It's a subscription. I don't
*  know if you have plans for advertising. I don't know how much kind of high commercial intent
*  traffic you get, but it seems like we're shaking the snow globe here of kind of how the web has got
*  monetized along with how it has been experienced. And I wonder what you think the future of the
*  economics are. Yeah, I don't know. I think that's the honest answer. I can take some predictions
*  maybe. That's because obviously that's what podcasts are for. My guess is people are going to
*  wall their platforms and data. At some point, Amazon can have an assistant that just
*  answers any question about any product. And people can directly use that assistant instead of
*  going to Google. They might even not get indexed by Google anymore, right?
*  So this is a Google saying all those companies that has such a tricky relationship with everybody.
*  It's like you got to always be on good terms with every single data provider
*  because you're like you're an average. I'm the guy routing all the traffic to you.
*  Otherwise you cannot even be discovered by anybody. But what if you make the whole
*  discovery process so much easier through an assistant that they don't need to be on you
*  anymore? Like you all must be saying, okay, I'm not going to get indexed by Google much anymore.
*  He's making the whole bet around these things, right? And Facebook and Instagram
*  don't get indexed by Google that much. So there's going to be these kind of
*  independent islands of data and services provided around them and a bunch of AIs.
*  AIs and data will kind of live together. The sort of global aggregator AI will be mostly for
*  research and knowledge. That's the market we're going after now. I think all the commercial
*  intent stuff, each of these individuals will try to do with themselves. Cut out the middleman,
*  right? Google is the middleman. For all these sellers and the buyers, why do they need this
*  one person to connect you to the right thing? You just need them because you don't support
*  good discovery of your content yourself. If you have a huge catalog and if you build a cool AI
*  assistant that can just answer any question about your catalog or your own social platform where
*  you can find any celebrity or any handler, you can ask questions about that person easily.
*  Why do you need this one single search engine anymore? It keeps on going and indexing everything
*  for you. You only need that for actual real content that needs to be learned for individual
*  usage, all this research and knowledge stuff that we are doing, like actual
*  links that say how to do certain things. But every other commercial intent and
*  advertising platform, I think you can already see it. Google is embedding themselves on TikTok.
*  People are just directly going and checking a restaurant out on TikTok.
*  The younger people. Why? Because the restaurant owner doesn't need too much anymore. They just
*  need to post a video on TikTok for sure. Of course, you do need Google for directions.
*  You see my point. There's already a big attack on their dominance here. Whatever they did to
*  Yahoo, where Yahoo was still useful for certain things, but lost most of its real value,
*  that's kind of happening to them. Where most of the work that they have done so far,
*  I would say getting more and more irrelevant. The vision is kind of... And this suggests your
*  monetization strategy remains subscription and is not likely to go advertising because you're
*  basically saying, we don't want to be a middleman. We think middlemen are in trouble. We want to be
*  the knowledge service that's worth paying for. And when it comes to Amazon, they're going to
*  have their own assistant. 100%. Here is the reason I believe in directly charging from the consumer.
*  I said this last time I spoke to you. You know the Jeff Bezos thing. You want shareholder alignment
*  in customer life because there is no misalignment in that case for running a company. You can always
*  take bold decisions that are customer friendly, user friendly. That's the only way to keep
*  improving the product as you scale the company. The problem with Google is their shareholder value
*  comes from a different set of customers. Those customers are not you and me. Those customers are
*  the people advertising on Google. So even today you saw in the leaked emails of how there was an
*  email from the ad executive in Google to the search executive saying how they want to post
*  more ads here because they're not able to meet Ruth Porat's targets for that quarter. You see,
*  who are they working for? They're working for the advertiser, right? Whereas what is the amount of
*  the cognitive bandwidth you spend if you're a search engine company? You should be spending
*  time fixing bad queries. That's all Larry and Sergey have done on the company. Because back then
*  there was no need to do all these things. Even the ads they were doing were small display ads on the
*  side. So I think that's exactly where I'm getting at. Don't try to copy them. Don't try to do
*  whatever they did. Try to think for the user alone. You obviously have to innovate on business. I'm
*  not saying you shouldn't. Figure out a way to make advertising work without it feeling like an ad,
*  right? Instagram does it really well. I'm very long Instagram on this because whenever I go there,
*  I don't even notice it's an ad. It's just so, it understands what I want. So I think that's one way
*  to do it here. What if the whole question is an ad? Have you thought about that? You search about
*  some concert. What if I show you some questions about other concerts that particular band is
*  doing or concerts relevant to your age? If I understand deeply what you want, I can just
*  do it myself. And then these people might pay me for being one of the URLs I index, right?
*  So there's like so many ways to change this market. And I'm actually pretty excited about like that.
*  Then trying to think so much for how do I figure out the Google's trillion dollar market business
*  model again? There's just a lot of other ways to make money. Like we just figured out that AWS
*  makes money. It's a completely separate business. And then he uses that to like subsidize and run
*  the core Amazon.com system, right? So that's like other ways in which we can be profitable and like
*  running a company here. Follow up on monetization. I've actually kind of struck just by the fact that
*  you don't push it nearly as hard as you could. I mean, most apps are kind of in this, you know,
*  Uber, VC money subsidizing the user phase. I mean, I think you're probably there too, but
*  it does seem like you could make a lot more money if you just said, hey, you get one question a day.
*  And then after that, you got to sign up for something. But maybe that's wrong. Like,
*  do you feel like you are optimizing? And I guess, you know, more to the point for the
*  listener who may not know all the features, like what are the big things that you get when you sign
*  up for the pro account today? We don't optimize it as much because what's more important is
*  the churn. You don't want to get a lot of people to sign up and then, you know, move out when they
*  don't feel the value in the service. You want people to proactively sign up as much as they can,
*  because then you can control the churn on your revenues. What do they get on Proplexity Pro? So
*  number one, they get our interactive search comparing copilot, which basically runs your
*  GPT-4 and has a really smart router that's really fast. And it hardly makes any mistakes and goes and
*  scars the web for you for every query real time. So you get unlimited uses of that. You also get
*  to pick GPT-4 or Cloud2 as your default model for every query, not just copilot, even non-copilot
*  queries. And you get to have unlimited file upload uses, which goes in well with Cloud2.
*  And especially useful for people who want to do research on it, you know, uploading their own
*  files and asking questions about it. More to come, because we are going to ship a lot more features
*  and like a lot of these features will be best experienced on the pro account. So what does the
*  company look like today? Last time we spoke, you had very few team members. I think it's grown,
*  but not that much. We are like 25 to 30 in that ballpark. You've raised, last I saw, $25 million.
*  Yeah, we did a $25 million series. I don't know if this is too sensitive to ask, but are you spending
*  like as much or more on compute, broadly speaking, than you are on the team? That's right. It's not
*  sensitive to ask. I think that's all you should do. That's the right thing to do. If you're not
*  doing that, then that's more problematic because honestly right now, GPUs are very expensive, right?
*  Like open-air models are expensive. Basically, the way you think about it is it's all about GPUs.
*  Everyone's pricing you based on that. If a GPU costs X dollars an hour and I host a model on top of
*  it and give it to you, then that's charged like two X dollars an hour, or whatever margins that you
*  want to see. Even more, maybe. Unless you spend, you cannot save on this. Irony, right? If you
*  really want to save on infrastructure, you actually have to spend on infrastructure in the short term
*  in order to save for later. That's basically just make a serious upfront investment in hard capital
*  and then you can save over a year on services. Yeah. You got to utilize it, build something,
*  and serve it, and commoditize it, and then that becomes a new thing.
*  Of course, it would be all easy to do this if you generated a cash cow some other way.
*  You use your own profits or revenue to get there. Neither XR for me journey, nobody prints their own
*  money that much into space, right? Everyone's like bankrolled by VC, so that's why we went and
*  raised our own. Yeah. How are you buying? It seems like you have a mix of every time a new
*  open source model comes out, you guys put it up as a chat bot. I think that's really interesting
*  that you're doing that. You have your own models, you're fine tuning 3.5, you got GPT-4, you got
*  Clawed 2. What does your buying mix look like? I'd be very interested in the relative cost profiles
*  of when you have your own model, how much cheaper can you get that versus 3.5? Because at some point
*  the Uber phase where everything's underwritten by VC investment presumably has to come to an end,
*  right? I think we have to train our own models and make them good. There's no other option
*  basically. That's the honest answer. Basically, your strategy is, and this is fascinating,
*  it's like you noticed that all the pieces were there to build a new kind of service.
*  You started off by stitching them together and the original thing is like Bing plus GPT best
*  available. But you're also as quickly as possible replacing every part of that stack with your own
*  version. So you've got the scraper, you've got your own language models, and the goal is to
*  potentially still use the best of those things, I'm sure. But ultimately, as you said earlier,
*  you want to be self-sufficient on all these key technology dimensions.
*  Yeah, that's absolutely right.
*  Yeah. That's a lot of projects. You've got 30-ish people,
*  Max. The volume of stuff that you've shipped and the quality has been pretty remarkable.
*  There's got to be more to it than just adrenaline. What is working so well for you guys that's
*  allowing you to ship at such a feverish pace? I mean, there's no other option, right? What is
*  the other option? The other option is not to ship fast. Why would you proactively go and choose that?
*  It's only going to hurt or potentially kill your company if you don't ship fast.
*  There is a saying, right? Momentum is everything in a startup. You've got to keep on growing.
*  There's no other job for a CEO than to keep on growing the company. Push, push, push, keep
*  investing more. Because once you stop doing that, that's when you start dying. Because
*  all the energy, the momentum you've built will decay. The default state in physics,
*  when you have kinetic energy is if you don't inject more potential energy into it,
*  kinetic energy will just decay with friction or some other thing.
*  Right. So you've got to keep injecting more external energy into the system.
*  Of course, at some point it will turn into a flywheel and keep powering itself.
*  That's how Google is. That's why the aliens are giving talk. Right. But that's like a rare
*  phenomenon. Most companies don't ever get there. In fact, Meta hasn't gotten there.
*  Like, Zach is still running the company and it's hot. If he relaxes and let's lose,
*  removes his feet off the pedal, I think TikTok or other people will take over. Same thing for
*  OpenAI. Anthropic is very close. Same thing for Google now. In fact, so, finally, you see what
*  happened. If you do take it easy, then you end up in a deeply competitive space. So when you don't
*  even have that lead, you cannot want to go even harder and go even faster. Especially, so this is,
*  I tweeted about this, like generative AI startup space is basically like a war zone. This isn't
*  to like romanticize war or something like that. I don't mean to give that impression. What I'm
*  trying to say is incumbents are shipping really fast because they know that if they don't,
*  the existing platform value they've built can be taken over by someone else who's going to use
*  AI as a wedge to get the initial users and then build everything else later.
*  So they might as well build this all themselves. Like, for example, Zuckerberg shipping the AI
*  assistant on WhatsApp messenger, like an image creator, you know, all these sort of things,
*  right? So because the more they delay these things, like the more distribution that Chat
*  BT or Journey will get and like, it's not great. So I think the only advantage for us is this one
*  particular thing of search with LLM. The person who really needs to protect this is Google.
*  But they're also in this really delicate spot of like not shipping this to, like, you know,
*  they have the search generative experience or whatever they call, like why didn't they just
*  change Google.com's UI to that, right? They cannot. It just is very, very difficult to do.
*  That's why I'm more bullish on our chances because we are playing a game that is very
*  hard to play for us. You cannot just ship something and kill us off. It's very difficult.
*  Like, as you know clearly, even we are not doing really well on many queries,
*  right? We can improve. So you cannot just come one day and say, oh, I'm done with perplexity in
*  this, my platform. It's just very hard to do. The business models are still unclear. There's a lot
*  of risk. So hence why we need to keep moving fast. And Nair Friedman is famous for saying this, which
*  is the more you learn per unit time, the more mistakes you make per unit time and the more
*  like lessons you learn, the more you edge over your competitors because they'll make the mistakes,
*  themselves and figure out things. And by the time they learn something X, you've already learned
*  like X times 10 and you're much more further ahead on the journey. You have said a couple things to
*  me in Twitter DMs about just things you've overheard in Silicon Valley, people kind of being like,
*  I don't want to have to think anymore. Let the AI manage everything for me. And I understand that
*  this is somewhat tongue in cheek in all likelihood to start and end the conversation
*  with something a little silly, but I do wonder if it sort of portends something real. And I
*  guess I wonder what you think right now of the state of human AI interaction. Is it healthy?
*  Are we already becoming in some ways over dependent? Are you happy with this default
*  trajectory that we're on? How serious are you about just like accelerate everything?
*  I personally love all this stuff, but I have a lot of concerns too about some of the dynamics that
*  I'm seeing starting to take shape. So I'm very interested in your perspective on that.
*  We'll get used to it. There's obviously something special about like talking to another human
*  because you have feelings for them and stuff like that. Now don't get me into the stereotype of,
*  you're building feelings for an AI like a movie car. It might be possible, but as far as like
*  asking intellectual questions and having intellectual conversations, I feel like
*  at some point we'll prefer doing that with an AI or a human because especially on topics that we're
*  not good at, it's much easier to bug an AI and keep digging more and asking a lot of dumb questions.
*  You won't feel shy about it at all. Whereas let's say you have the world's expert in AI,
*  like say Ilya Sudsky we're just talking to today. It feels awesome. He's considered one of the
*  foremost experts in AI. How many hours of time can you get with him? Maybe one hour. And after that,
*  you're not going to be able to keep DMing him and asking stuff, right? But if there is an AI,
*  like say ZVD4 or ZVD5A and that helps you build a product that can answer almost anything about
*  neural nets, anything like almost close to no hallucinations. You would bug it for hours and
*  hours and keep learning, right? So there was an AI expert on AI itself or medicine or legal or
*  chemistry, physics, or you want to teach your kids about something and you don't want to appear dumb,
*  so you invite an AI together and teach it together. We both learned to ask things together.
*  So I think Zakharberg made a cool video on this where his parents are coming to the house and
*  he's asking how to cook steak. That's the sort of experience I feel we'll have. We'll be sort of
*  viewing these as like a cool tool that is part of everyday life. Now one-on-one conversations,
*  empathy. I can see that being a possible application. Therapy. Obviously, there's
*  romantic AI boyfriends and girlfriends, character AI stuff is also happening.
*  So definitely like significant fraction of time of human activity on digital devices will be spent
*  with AIs. That's for sure. Whether it's completely replacing humans or not is not the question. It's
*  more like whether it makes your quality of time better or not. Humans will naturally gravitate
*  towards whatever is giving them more alpha in terms of being better at their job or feeling
*  more purpose in their life. It might even be a thing where people do it together. It may not even
*  be one-on-one. It could be there's an AI and then there's two or three humans asking together.
*  Like you're in a group conversation and there's also an AI. So that way there's fewer fights.
*  You don't disagree on things. You just learn to be more objective about things. It's almost like,
*  do your research, go do your math. Instead of saying these things, we just have the AI do it
*  right away, right there. There's no room for arguments. It's a fascinating vision. You're
*  another one who's definitely a leading thinker in the AI space. I would love to have you on again
*  when you have some more time, but for now I will just say Arvind Srinivas of Perplexity AI,
*  thank you for being part of the cognitive revolution. It is both energizing and
*  enlightening to hear why people listen and learn what they value about the show. So please don't
*  hesitate to reach out via email at tcr at turpentine.co or you can DM me on the social media platform
*  of your choice. Omniki uses generative AI to enable you to launch hundreds of thousands of ad
*  iterations that actually work customized across all platforms with a click of a button. I believe
*  in Omniki so much that I invested in it and I recommend you use it too. Use Cogrev to get a 10% discount.

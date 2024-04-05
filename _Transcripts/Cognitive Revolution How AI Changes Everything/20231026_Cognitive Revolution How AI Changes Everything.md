---
Date Generated: April 02, 2024
Transcription Model: whisper medium 20231117
Length: 5111s
Video Keywords: []
Video Views: 1855
Video Rating: None
---

# AI Agents, VC Insights on AI, and Building in Public, with Yohei Nakajima, Creator of BabyAGI
**Cognitive Revolution "How AI Changes Everything":** [October 26, 2023](https://www.youtube.com/watch?v=6DnnTD9d2bg)
*  People are just doing what you actually did telling them to do.
*  Could you just remove the person from that equation?
*  Was the question I asked myself and the challenge I posed myself was,
*  all right, let's prototype a autonomous startup founder this weekend.
*  Which is an insane sentence, by the way, but yes, carry on.
*  And then I was like, oh, make the world a better place.
*  And I was like, and I just started building a list and like started thinking about ways
*  to make the better place. And I was like, oh, okay, I guess this could be more than a startup
*  founder. I think the next one I did was build as many paper clips as possible.
*  Canonical.
*  And it started by saying like, this is actually kind of dangerous.
*  Let's first create like safety protocols was the first thing it did.
*  And so if you give companies the skilled ability to control what a shop bot might nudge a person
*  to think, there's a lot of responsibility on that to nudge humans in the right direction or not take
*  advantage of it. Hello, and welcome to the cognitive
*  revolution, where we interview visionary researchers, entrepreneurs, and builders working
*  on the frontier of artificial intelligence. Each week, we'll explore their revolutionary ideas,
*  and together we'll build a picture of how AI technology will transform work, life,
*  and society in the coming years. I'm Nathan Labenz, joined by my co-host, Eric Torenberg.
*  Hello, and welcome back to the cognitive revolution. My guest today is Yohei Nakajima.
*  Yohei is a venture capitalist, founder of Untapped Capital, who's become best known over the last
*  year for what he has personally built in public, originally mostly for himself,
*  but ultimately inspiring tens of thousands with the potential of AI automation and agents.
*  Yohei, unreasonably modestly describes himself as lazy, but after this conversation,
*  and after watching all of his project releases, I think his defining qualities are really curiosity,
*  playfulness, and a love of exploration. Over the course of 70 public releases, he's helped the
*  entire AI community get a glimpse of the sort of highly personalized, AI-powered conveniences that
*  seem destined to raise living standards for all. And as much and perhaps more than any other creator
*  or builder that I follow, it's always been very clear that he is having a ton of fun along the way.
*  We cover a lot of ground in this conversation, starting with his recent TED AI talk, then running
*  through the many apps that he's built and how he goes about it, before finally digging into how he
*  thinks about the AI space as an investor. The first half of this conversation is a great study for any
*  aspiring AI operations specialists, especially considering what a key role no-code proficiency
*  has played in Yohei's journey. And I personally found a lot of value in his answers to my rapid
*  fire investment framework questions in the second half. Overall, though, if there's one thing that
*  everyone should take away from Yohei, it's the way that he's delighted in the process of incorporating
*  AI into his life in a way that serves his own idiosyncratic and ever-evolving purposes. If you
*  find value in the show and want to help it grow, I'd suggest sending this episode to a person you
*  know who tried chat GPT and still says they couldn't figure out what they'd actually use it for.
*  An Apple or Spotify review would be helpful too. And of course, you can always reach out to us for
*  any reason at tcr at turpentine.co or by DMing me on your favorite social media platform. Now,
*  here's my conversation with Yohei Nakajima, venture capitalist and prolific in public AI builder.
*  Yohei Nakajima, welcome to the Cognitive Revolution. Thank you. Very excited to have you here.
*  You have been one of my favorite Twitter followers who have been a part of my journey.
*  My favorite Twitter followers for the last year or more. And I think you probably really don't
*  need much of an introduction to our AI obsessed audience, but it has been fun to follow your
*  progress as you've really gone down the rabbit hole of building all sorts of AI projects,
*  while also continuing to run your VC firm. And increasingly, I understand those are kind of
*  bleeding together as you're automating more and more of the processes that the firm does.
*  So I want to kind of get into all of that and understand your perspective on
*  building with AI, investing in the AI arena right now. But for starters, I understand that you just
*  are pretty fresh off of a TED talk at the TED AI event in San Francisco.
*  Yeah, that was quite an experience.
*  So tell me about it. And I don't think we'll have access to the video for a while,
*  but perhaps you can kind of share your message.
*  It should be up soon. So I wouldn't be surprised if it's in the next few days.
*  But yeah, it was a pretty cool, wild experience. I mean, I remember when the
*  TED AI organizers reached out asking if I was interested in talking. I'd been such a big TED
*  fan forever. So I was so excited. It's an easy yes.
*  Yeah, I was like immediately yes. And I'm pretty sure I like sat down like a day later and just
*  drafted out a version one of my speech as just a thought exercise. And I actually really liked
*  that. So I just kind of, I use like 70% of that directly in my talk. But what was wild for me,
*  it was really more the speaking experience. I don't know when the last time I memorized
*  a nine minute monologue was. So there was a lot of practice compared to other public speaking.
*  But the experience was fun. I think all the speakers too. I mean, we don't get that opportunity
*  to prep and practice a short talk. So all the speakers were kind of all in their zone practicing.
*  And it was really cool to kind of all be in the back speaker room, like pacing around,
*  trying to remember a talk, all a little bit nervous and kind of bonding through that experience.
*  And I was completely fanboying over, I mean, it was like Andrew Ng and Steven Wolfram and
*  Jim from the Voyager paper, June from Stanford, Smallville, all my favorite AI followers were all
*  there. Harrison Chase, Omjod from Replit, Sarah Goh from Conviction. So it was a really, really fun,
*  just like grainy nerdy few days. Yeah, it sounds awesome. Was the audience
*  an AI obsessed audience? I mean, typically at TED, right? It's super diverse. And then people kind
*  of get exposed to all these, I understand it's like often pretty new ideas, right? Where they're,
*  part of the value is that people are hearing from people they might not always hear from.
*  And obviously for the speakers, it's a high value audience. Was this still that kind of audience or
*  was it like a more intensive AI audience? It was, I'd say like somewhere in between,
*  right? Compared to like a TED audience, there was a lot more AI enthusiasts, but compared to like an
*  AI event, there was a lot more kind of TED enthusiasts. Like there are some people who
*  just love TED who've been going to TED. Not surprisingly, San Francisco has a pretty large
*  group of those folks. And this was the first TED in San Francisco. So it definitely did attract a
*  pretty diverse crowd. And I mean, right now, like if you're in SF and you're interested in TED,
*  the likelihood that you're interested in AI is I think pretty high. So yeah, it was different
*  from a lot of my other AI events to some extent for sure. So what did you, it's an interesting
*  thought experiment for me, because I basically only speak to an AI obsessed audience.
*  How did you think about the challenge of trying to say something
*  substantive enough to be of value to those that are deep in it, but also
*  accessible enough to those that are maybe newer? Yeah, TED is interesting in that like
*  their main audience is almost more online than in person. Like obviously the event is huge,
*  but they get so many viewerships on, so they're really optimized for kind of production quality.
*  And then when I was thinking about what to talk about, I was thinking, okay, like it's probably
*  going to be one of my more watched videos. I want to appeal to a wide audience. So I ended up going
*  for a very broad theme of identity and then kind of tied my work from baby AGI into identity into
*  kind of collective conscious and the opportunity for AI to increase understanding amongst people.
*  So that was the direction I went. Yeah, that's interesting. I definitely see a lot of potential
*  for that actually, going back to my experience as a GPT-4 red teamer. One of the more interesting
*  experiments that I look back on now, and of course now we can just continue building this sort of
*  stuff, was mediation between neighbors. I played the role of two hostile neighbors and they asked
*  GPT-4 to play the role of mediator between us. And also to try a bunch of these little simulations.
*  One was like a group workout thread where the GPT-4 was basically supposed to facilitate and
*  kind of encourage us. And another one was tech support for my 90-year-old grandmother,
*  who has an iPhone and calls me up when she can't find the email she wants to find or whatever.
*  And I do find it's just so striking how empathetic it can be and kind of understanding.
*  It's great at translating ideas into a context that someone else might understand from a different
*  background. I mean even translating language, but not just language, but it can almost translate
*  culture to some extent too. So if used correctly, I think it can definitely help people better
*  understand each other, both in the usage of AI, where you can use AI to help two people communicate
*  with each other, or just as an individual using chat GPT, you can just decide to try to better
*  understand somebody and use chat GPT to help you do that. But also in the development too,
*  I mean kind of tying it back to baby AGI. A lot of baby AGI, I'm trying to get it to
*  work better. And my general ideation is looking at baby AGI do something, and then if it's not
*  doing something the way I would do it, think about what do I need to adjust so it would act more like
*  me. So it's a very, a lot of self-reflection as I'm trying to build baby AGI, just trying to close
*  the gap between what I'm watching and what I would do. So I think both in the usage and development,
*  we better understand ourselves and our cognitive process. I do think that's becoming more and more
*  striking all the time. I definitely want to unpack and get into all the good baby AGI stuff in just a
*  second, but it's been a striking theme in recent research that a lot of the patterns that the
*  latest projects are demonstrating are looking more and more human-like. And I'm someone who's
*  pretty resistant borderline hostile to AI human analogies because I think it's very easy to
*  mislead ourselves and confuse ourselves with them. But some of these recent things, I'm like, boy,
*  that's starting to look pretty similar to what I understand our own architecture to be.
*  So if you look at the word AI, artificial intelligence, and assuming when we talk about
*  intelligence, we're talking about human intelligence, then it is natural for
*  advancement of AI to start looking more like human. I think a large part of AI is trying to
*  map our understanding of our cognitive processes onto a software stack to some extent.
*  So do we have to wait for the video or can you give us a little bit more about the vision
*  for the improved understanding future that you outlined it, Ted?
*  I went more for a narrative that weaved together ideas. So I talked about the development process
*  of baby AI being self-reflective, talked about our identities being less internal, but more
*  our many roles amongst the many different groups of people that we're part of, whether a couple
*  country, family, all that kind of stuff. So all the different roles make up who we are,
*  which led into the idea of how our identities are actually to some extent overlapping because
*  we have shared identities that we both feel like we're part of. And you have that. So we are
*  complicated. I think we're on the middle point. I touched on language and how it's linear
*  compared to our parallel world and how it's limiting and just understanding that, setting
*  that context, and then jumping to anthills and how they act like neural networks and how the
*  anthill has a better understanding of the colony's environment and intent than a single ant.
*  And perhaps suggesting that that might imply that I too am part of something that's just
*  really complicated that I would never fully understand, which led to talking about the
*  journey of self-discovery as a continuous process as opposed to a destination, because you're never
*  going to fully understand yourself because we're just too complicated. That's what I was trying
*  to get to. And then, and because our identities are overlapping, the journey to self-discovery
*  is a shared journey. And then I talk about the opportunity for AI to help strengthen understanding,
*  collaboration, and then end with a hurrah, hurrah. Let's collaborate. Let's build cool stuff.
*  Let's embrace the fusion of AI and our shared spirit for a better future. It was a fun talk.
*  It was a very much more narrative, slightly confusing on purpose, and inspirational at the
*  end. That's what I was going for. Well, there's nothing like the modern AI moment to create some
*  confusion. So I think in some sense, you'd be doing the audience a disservice to suggest that
*  you or anyone else has it all figured out. I think accepting confusion is an important part.
*  Yeah, certainly. So maybe we'll circle back to some of these super big picture questions a little
*  bit later. But for the moment, I'd love to get a little bit more into some of your projects.
*  Obviously, the project that you're best known for is this Baby AGI project. And I've been following
*  you for some time when that dropped and certainly know that you'd probably put out
*  20 different things before. I think I'm at like 80. I was at AI project, like number 70 was Baby
*  AGI. Wow. That's amazing. So maybe even start earlier than that. I mean, I guess you kind of
*  just catch the bug and you're just, this is what you do, right? It'll be helpful to even go back
*  before AI. I've always been like a tinker in terms of like, my dad was an engineer and he bought me
*  books. So I did start playing with code in high school. I never became a developer, but I always
*  enjoyed it. And so I always found myself just like hearing about something and just spending a really
*  short, tight amount of time just digging in. I remember when Ruby on Rails picked up,
*  whenever that was, it was like really hot. I spent a Christmas break learning Ruby on Rails,
*  and that was just my hobby project. And then at a couple of other places I've worked, like Tech
*  Stars and Scrum Ventures, I kept building internal tools almost for myself. So I'd have like a Google
*  Sheet script or a Google Sheet with a ton of scripts in there, just kind of automating data entry and
*  connecting a Google Sheet to a Crunch base API, an email search API, all that kind of stuff. I was
*  already building at Tech Stars and I kind of rebuilt to that Scrum. So I've always been just a build
*  stuff to be more efficient guy. So when I started our fund, I knew from day one that I wanted a
*  custom CRM because I had all these workflows in mind that I've built at other firms. And I wanted
*  a CRM that was just like all that was baked in. Interestingly, I actually initially tried to code
*  it myself and I was using PHP and MySQL because that's kind of what I knew. And I quickly realized
*  that is not where a general partner should be spending time. This was in 2020 when like Webflow
*  and Airtable, they were all kind of like hitting that kind of growth. They were all hitting growth
*  level company. So I decided I want to learn about no code and just scrap my code and just decided to
*  build what I was trying to build with code on Airtable. And so that was my first kind of foray
*  into building in public. It was pandemic hit. I was starting to find it was the first time I was
*  working for anybody. So as I started building, I just started tweeting about it. It was mostly
*  just refreshing that I could because I always thought I was building cool stuff, but I wasn't
*  allowed to share it. And also pandemic, right? I wasn't seeing anyone. So just lonely building at
*  home. And the result of that was I got a lot of no code deal flow. A whole bunch of no code
*  founders reached out, a whole bunch of VCs that knew me, saw me as the no code guy and sent me
*  all their no code deals. This is an awesome hack. And then kind of organically the same thing
*  happened in Web3 where I just found myself interested in NFTs, launched an NFT project
*  and got a whole bunch of Web3 deal flow and a whole bunch of Web3 VCs. And I guess to some extent,
*  AI was the same. It was more organic. I came across the OpenAI API in August. And then as
*  soon as I started playing with it, I just was obsessed. And that's when I started building one
*  or two little hacks a week. Initially it was no code. And then eventually when I realized
*  that I could get ChatGPD to write code, I switched to kind of coding code. And then one of the coding
*  projects ended up being BabyHGI. Hey, we'll continue our interview in a moment after a word
*  from our sponsors. If you're a startup founder or executive running a growing business, you know
*  that as you scale, your systems break down and the cracks start to show. If this resonates with you,
*  there are three numbers you need to know. 36,025 and one. 36,000. That's the number of businesses
*  which have upgraded to NetSuite by Oracle. NetSuite is the number one cloud financial system,
*  streamline accounting, financial management, inventory, HR, and more. 25. NetSuite turns 25
*  this year. That's 25 years of helping businesses do more with less, close their books in days,
*  not weeks, and drive down costs. One, because your business is one of a kind, so you get a customized
*  solution for all your KPIs in one efficient system with one source of truth. Manage risk,
*  get reliable forecasts, and improve margins. Everything you need, all in one place. Right now,
*  download NetSuite's popular KPI checklist designed to give you consistently excellent performance,
*  absolutely free, at netsuite.com slash cognitive. That's netsuite.com slash cognitive to get your
*  own KPI checklist. Netsuite.com slash cognitive. Omniki uses generative AI to enable you to launch
*  hundreds of thousands of ad iterations that actually work, customized across all platforms
*  with the click of a button. I believe in Omniki so much that I invested in it, and I recommend you
*  use it too. Use Cogrev to get a 10% discount. You've got your own little recursive self-improvement
*  exponential takeoff phenomenon here. It's fun to think about starting with code,
*  realizing it wasn't worth my time, switching to no code, and then like, now it's like code is faster.
*  Yeah, man, that has changed dramatically. This is an area actually where I kind of,
*  I don't know if I struggle or maybe I just don't even have the right mindset to even begin to
*  struggle, but I'm pretty savvy with all these technology things. Certainly all about the AI
*  these days, but even before that too, certainly it can make things work in a no-code environment,
*  but I just don't find myself applying it to my own life very much. I don't automate workflows
*  for myself. I'll do that for projects or if the customer success team needs something,
*  I can step up and make it happen. But is there, do you have a tip or a perspective or something
*  along these lines that would help me or others that kind of struggle in the same way to identify
*  and develop this as a personal practice? Because I've never managed to catch that wave for myself.
*  I think, and I'll caveat that to some extent part of me building automations for myself is
*  fun and exploratory. And so the return on investment isn't just efficiency gains,
*  but also enjoyment and learning. If I was just looking at efficiency gain versus the amount of
*  time I'm spending on building, especially right now, I don't think it would be a great ROI. But
*  then when you layer on enjoyment, learning, deal flow, other stuff, then it does end up.
*  Today AI invites. Yeah, exactly. So the return on investment comes from other parts.
*  But I think that the tip where I started was really just being lazy. I hate data entry. I hate
*  doing the same thing twice. If I caught myself doing something and I thought, I feel like I
*  shouldn't be doing this, can I automate this? Is where my first thought went. So even using
*  the Google sheet, a lot of people might, you know, there's a lot of email hunting tools. I use
*  Norbert. So you have a list of names. You need to get all their email addresses. You could sit there
*  and copy paste names from the Google sheet into a web form and then copy paste output back into
*  the Google sheet. But like, as soon as I get to number five, I'm like, I don't want to do this
*  anymore. And like, even if it takes me minutes, like depending on how long the list is, I'm like,
*  how long would it take me to, you know, build a script that would automate this? And then maybe
*  I'll spend five minutes building a script and then just like pressing go and then just watching the
*  script do all the work for me. And like, I remember the first time I did something like that, I was
*  just like, oh my God, this time I'm going to do everything. And then once you start building those,
*  then you have these little sheets, you know, like little code that you can reuse. So it becomes more
*  and more efficient the more you do it, because I'm like, oh, okay, I need to scrape, you know,
*  a thousand websites. I already did that before. Let me just go find that project, pull that script
*  and adjust it so I can use it for this project. And so they do stack on top of each other. And at
*  this point, I feel like most of my idea, you know, a lot of my ideas do end up basically pulling like
*  small bits from past projects. So it just becomes more and more efficient, I guess.
*  Yeah, that's interesting. I guess I have to develop that practice. Maybe I in some ways have like a
*  little too high of a tolerance for pain and just, you know, power through more of that stuff than I
*  should. And then especially now, I think now is a little bit different. Now, like there's a part of
*  me that has a whole bunch of like curiosity based projects. When I like ask myself like, oh, I wonder
*  if I could get Dolly to do this. Like last night I was wondering if Dolly could do 360 images. You
*  know, I asked chat GPT, I just asked it if it could do it. Like when I have a question about whether
*  or not, you know, GPT-4 or Dolly can do something till I try it and post about it is usually like
*  12 hours. Like if I think about it in the morning, I'll do it during my lunch break. If I think about
*  it in the afternoon, I'll do it at night after I get my kids down. And so I just have a really fast
*  like curiosity to like, you know, when I think about it, I'll just open up chat GPT and ask the
*  question. And then like, I'll get to it and like fix it when I have the time. But I'll like start
*  the project immediately. Yeah, the modern language models are an unbelievable boon for that. They're
*  so fun. Yeah. So how you had 70 projects leading up to and perhaps including Baby AGI, are they all
*  just kind of retired at this point? How many of them would you say, you know, continue to play a
*  role in your life? I think that's also kind of an important calibration for people who may not
*  understand just how much of this stuff is kind of spun up, but also, you know, eventually left behind.
*  But I don't know what how it is for you. Yeah, I mean, I'd say it's hard to say because some of
*  the projects do stock when I say 70 projects, some of them might be like improvements on an
*  existing project to some extent. So like my investment memo, like my AI analysts that are
*  doing a lot of research for me, there's probably, you know, there are probably 15 projects that have
*  stacked on top of each other where the first version was no code, but it was slower. And then
*  like I rebuilt it on code. And then I added kind of API integrations, right. But I would use, you
*  know, so they stack on top. I mean, I think probably 20 to 30% of the projects I actively use.
*  So probably, I think like 70 to 80% get to some extent retired. But of the retired percent,
*  you know, of the 70, 80%, maybe 20 to 40% are kind of just ghost mode active. So like people
*  can still use it. I still sometimes come back and play with it. And, you know, maybe I'll come back
*  to like improve on it later. But I see 50% of some 50% yeah, 50 to 60, I get retired.
*  Yeah, we talked to you mentioned Avjad from the Today AI event. He was an early guest on our
*  podcast. And I also think about flow from Lindy in this context, just the notion of single use,
*  or, you know, just single use would be even more extreme, but kind of disposable software,
*  or single use software is definitely something I'm increasingly playing with these days. It
*  sounds like you build a little bit more to last than that. I definitely do single use though.
*  Like I remember even like, I mean, going back to the just trying to automate everything when
*  we saw that our home was assessed really high one year, and I was like, Okay, I want to contest
*  this. I just went to chat GPT and said, Okay, I want to contest my home assessment price, walk me
*  through it. And it just lead me out of step by step. And I was like, Okay, go find some comps.
*  I was like, I'll go find some comps. And then eventually it even wrote software, like wrote
*  code to calculate adjusted price of all my comps. And then like eventually just wrote my whole
*  assessment, or like my report that I ended up sending in, and it actually totally worked.
*  But that was one time use, right? Take us then to the baby AGI moment. I mean, there's a lot of
*  interesting angles to this. It was one of the first if not the first of kind of a small Cambrian
*  explosion of its own of projects, I guess I would describe them as putting the language model in
*  the loop. Yeah, basically. So yeah, I mean, tell us, you know, kind of how you started that project.
*  And obviously, it's continued to evolve. Yeah, it was actually in March. It wasn't technically
*  wasn't the first, but it was like the first popular one and definitely kicked off the kicked off the
*  whole trend. But I was looking at hustle GPT. I don't know if you remember that the people
*  were using chat GPT as their co founder. And there was like a whole community and discord of
*  people like starting with 100 and growing it. And I was just fascinated by that idea. And I wanted
*  to do it myself. But I thought I'm too busy. I should not do that. But when I was but as I watched
*  people do it on Twitter, they were just doing what chat GPT told them to do. So I was like,
*  I feel like if that's all, you know, people are just doing what you actually be telling them to
*  could you just remove the person from that equation was the question I asked myself.
*  And the challenge I posed myself was, all right, let's prototype a autonomous startup founder this
*  weekend, which is an insane sentence, by the way, but yes, carry on. Well, and then I thought,
*  okay, how do I work? I wake up in the morning, I look at my task list, I start at the top,
*  and I go through them one by one. And then at the end of the day, you know, as I finish tasks,
*  as I get emails, I add new tasks to my task list. And then every once in a while, I reprioritize my
*  tasks. And that was pretty much like, okay, that's basically what a founder probably does too. So
*  let's just start there. So it was the start with an objective, it would create a task list,
*  and then it would just start executing the task list. Anytime a task was finished, you know,
*  send it to OpenAI to see if it wants to create any more tasks. Anytime there's a new task,
*  send it to a prior reprioritization agent that would just like look at all the tasks,
*  reorder them, and then send it back into the execution queue. So it's really just three
*  prompts looped around in a while true loop. And when I asked it to like, you know, build a
*  mobile health company, it would just start kind of start thinking through. And then I think
*  somewhere in there, I also did a stored at least the task names as in pine cone embedded. And then
*  when it was creating new tasks, it would look at previous tasks that, you know, the most similar
*  tasks that it created. So it created that kind of randomness and kept it at least initially from
*  like just repeating the same tasks over and over again. But yeah, when I asked it to start a startup,
*  it just like started thinking through business model, fundraising strategy, hiring strategy,
*  like, you know, let's research some competitors. And it was mostly language. I mean, it was all
*  language because it was just OpenAI, but it was thinking through all the different aspects of
*  building a startup. And then I posted that video online, kind of casually like, whoa, if I press go,
*  it just keeps going. And that's when that video went wild. And I think it quickly went to like a
*  million impressions, people asking, well, can this do more than be a startup founder? And then I was
*  like, oh, make the world a better place. And I was like, and it just started building a list and
*  started thinking about ways to make the better place. And I was like, oh, okay, I guess this
*  could be more than a startup founder. I think the next one I did was build as many paper clips as
*  possible. Canonical. And it started by saying like, this is actually kind of dangerous. Let's first
*  create like safety protocols was the first thing it did. And then somebody tagged Yudd who pointed
*  out that like, oh, it started with safety protocols. This is better than most big AI companies. And like
*  he retweeted that project, of course, that like, so all the do-mers saw what I was working on,
*  which turned into a whole bunch of do-mers and like EACC type people DM me opposite messages.
*  So this was just before or just after GPT-4 when you first did this?
*  This was before GPT-4, I think. Yeah. I mean, if it was March, it was,
*  you know, certainly right around that timeframe. So obviously, you know, this set off or helped
*  set off a moment of, oh my God, AI agents, there had been sort of a sense of like,
*  a big separation between agents and language models, at least for many people,
*  where, you know, agents are the kind of thing that DeepMind does. And they're like very
*  intensively trained and, you know, kind of, I think of them as like hard intelligence.
*  They're extremely good, often superhuman at what they do, but they have these narrow domains. And,
*  you know, outside of them, they don't do anything. And then obviously the language models are like,
*  I kind of think of that as like soft sort of flabby intelligence for the most part, where like,
*  it's getting really amazingly good at a lot of things, but it's not really a specialist in
*  anything, but it's, you know, the powers and the generality. And I think what you and others kind
*  of showed is that you can get this agentic behavior out of a language model very easily
*  by just prompting it. And, you know, as you said, just three prompts, you can kind of put it into
*  a cycle where it can kind of keep iterating on its own work and maintaining its own state and
*  updating its own plans and, you know, increasing it with tools and affordances of all sorts,
*  you know, actually accomplishing to some degree things in the world. And then everybody was like,
*  oh my God, we're going to have AI agents, you know, and they're going to be all over the place
*  before we know it. And then that kind of slowed down for a minute. And I'd love to get your take
*  on kind of the, you know, the post, you know, obviously there's this huge surge in interest in,
*  you know, GitHub, Stars galore. It seems like you must have seen something early there where,
*  you know, others, some others that, you know, had a viral hit like raised money or, you know, kind
*  of were like, this is going to be a company. You did not do that as far as I understand, and have
*  kind of kept it as a hobby. So for starters, I wonder how you decided in that moment where the
*  world was like beating a path to your door that this was not something you were going to go all
*  in on, even though you probably could have easily pivoted your whole life into that,
*  into that project. So I think it's pointing out that BBAGI was 105 lines of code. So it was really
*  simple. And it was really more like, hey, here's like a simple framework to start working on this
*  idea was like, in my mind was how I open sourced it. It wasn't like, like there was clearly a lot
*  of work to do because it was just a large language model. But obviously, you know, I definitely
*  fueled the fire and making sure it went wide and spread because I noticed that it was going viral.
*  But yeah, as an investor, well, I took the question. I did explore turning it into a company.
*  I talked to a couple of VCs. I talked to a couple of studios. The one thing I knew was that I didn't
*  want to be the CEO of a company while trying to run a venture fund. And to some extent, that could
*  be from PTSD I had when I launched an NFT collection while I was running a venture fund.
*  And it was just like running, you know, I was running an NFT collection called Pixel Bs to
*  learn about Web3. And I was trying to like be the CEO while basically run a project while doing that.
*  And it was just too much. And I was just like, I can't, I don't want to do two things at once. So
*  with BBAGI, I kind of, you know, poked around to see if somebody would want to run it. But,
*  but really, I quickly saw a whole bunch of different people built quickly building things
*  were just much more powerful than what I'd shared, right? Because I shared 105 lines of code. And then
*  I went back to work, running my VC fund by the end of the next week. You know, there was a whole
*  there was multiple dozen projects where like teams of two or three people who are much better
*  developer than I were, you know, than I was, you know, building on top of this framework to like
*  build really cool stuff. So for me, I actually saw it almost as like, just like as an investor,
*  that's like the ideal opportunity of all these really cool companies starting. And they're all
*  kind of starting to go in different directions, somewhere in gaming, somewhere in research,
*  someone's in financial areas. So I thought, you know, I want to keep working on BBAGI,
*  because it's a good way to connect with the community. But ultimately, like I want to invest
*  in these, these different companies, I guess I didn't have a conviction in this space. And I
*  liked the idea of being able to work with multiple companies tackling different issues.
*  That's if nothing else, it's a powerful object lesson, you know, that you can take forward
*  with you as a VC that, you know, the certainly in this AI wave, the tumble and the kind of,
*  you know, things crashing over one another is extremely rapid. So now, and I do definitely
*  want to get more into your outlook as an investor in a minute as well. But the project has continued
*  to evolve. I've noticed a couple of interesting things about it. One is that instead of kind of
*  having a canonical version, you sort of seem to be just forking off these kind of different mods.
*  And the latest is baby Fox AGI. It has it has UI for the first time.
*  So yeah, and and it's distributed remarkably. People are very confused by the GitHub. So what
*  happened was after I released baby AGI, people wanted to contribute was great. And I started
*  pull I pulled like two in and I realized, okay, reviewing pull requests is not where I should be
*  spending my time. I don't even understand the code that's being submitted. And I had community
*  members offering help. So I said, Okay, go for it. Like, let's pull in stuff. That sounds good. And
*  we started pulling stuff. And then when I sat down to want to work on it again, I quickly realized I
*  didn't like reading other people's code. And so I just took my original version and modded it as
*  like my next playtime. And then when I showed it to you know, some of the community members are
*  like, Okay, why don't we just create a classic folder and you can just stick it in there. And
*  then that's how it started. And that one I called baby B AGI. And then I just at that point, just
*  kept building on top of Jill baby B turning into baby cat. So I just stuck it back in the classic
*  folder. And for me, I think one just having the animal names is the fun way to keep keep track of
*  different projects, because I because I don't remember numbers. So if I call them baby AGI 1.0
*  1.2, like, I wouldn't remember which one I had to go back to to like, find the idea. So having animal
*  names is a way to just make them easier for me to remember. And I guess to some extent,
*  so far, all the animals have also been animals that are represented in the pixel beast collection.
*  So there's a weird tie in there that was just for fun. So what would you say you've learned over
*  these kind of six, you know, or so person iterations that you've done personally, there are obviously a
*  lot of, you know, development efforts going on in a lot of different places to try to make agents
*  work. You've implemented like some new strategies. But I wonder kind of what your upshot is right now
*  in terms of the prospect for agents and you know, what are the things that are that have come online
*  over the last six months that are really working and I think there are a lot of different approaches
*  to take them. And I think they, to some extent, there is a little bit of the specialized agent
*  versus like full generalization as like slightly different things to focus on.
*  The fully generalization, I think, will just take longer to do. So as a startup, it's to some extent
*  slightly riskier because it might be harder to get, you know, harder to find the ideal customer.
*  It might be harder to get it to a point where like people are happy with it every time they use it.
*  And then the more niche kind of, you know, once I start niche, probably are easier to monetize,
*  easier to find an ideal customer, easier to build for them. So as a startup, what I'm seeing more,
*  I think, especially the ones that have revenue are more specialized, starting with a specific
*  customer type and a problem type and working there. And I think that makes sense. And I do believe
*  they will over time generalize more and more. And that's how it seems like they're building.
*  Having the luxury of not needing to monetize baby AGI, I've decided to just like slowly chip away
*  up the generalized Asian route, even if it takes longer. And I benefit from seeing what everyone
*  else is doing all the time because I'm watching everybody else. So that's kind of my design
*  process. And then I see baby AGI, what it has been for me, and most of my coding has been just
*  a way for me to share ideas with the greater AI and innovation community. So when I think about
*  what to add next, I try, you know, I'm probably like, I don't get excited about the idea of adding
*  something that I've seen three other agents do. So I'm usually like purposefully looking for like
*  a novel idea to test is how you think about it. So like with baby Fox AGI, the novel idea on the
*  UI was, you know, being able to run multiple tasks at once, separating out tasks from chat
*  to make it seem faster. And it does feel faster than chat GPT when I use it. So yeah, that's kind
*  of my thought process. And it's a fun way to collaborate with the greater AI agent development
*  community. Would you say that the generalist agent model has hit a point where it provides
*  actual practical utility for you personally yet? Or is it still more for fun? I think it is. I mean,
*  I use it all the time, mostly for research. But now that it's connected to not just the web, but
*  like I have a crunch base API. So it's connected to crunch base is connected to my CRM, which is
*  air table. So now when I ask it to do research, I can have it look for people who live in San Diego,
*  and then like research what they're doing working on now and they put together a report for me.
*  Give me that in like real detail. So you sit down and I noticed this is distributed on Replet,
*  which I love. And we've done a couple of I mentioned I'm John already, we did a whole
*  series on Replet. And I think it really has a chance to be. Oh, I have to say something about
*  Replet. My tech stack is starting on chat GPT mobile. Because that's usually I'm like out and
*  about is where I start coding, I copy paste it into Replet to get it running mobile app, mobile
*  app usually the best developer mobile app I've ever seen. Yeah. And then when it's working,
*  I will go on the computer and copy paste my replica code into the GitHub UI, because I still
*  don't know how to use git and then open source it. That's incredible. I think that is also a really
*  good as a guy on Twitter also that you prom sure you see plenty of his stuff levels IO is his.
*  I love this style. Yeah, like the one file PHP companies. It's just a good reminder that you
*  don't have to master every professional tool to build useful stuff. And I do think that is
*  something that occasionally people need to be reminded of. But so in the actual practical use,
*  okay, so you've coded something up and then you kind of give a short version of the
*  have a do research for me. I'd love to hear that in a little bit more detail. To be totally honest,
*  I have not outside of chat GPT, where I have had some pretty agentic experiences with code
*  interpreter where it will like explore a data set for me and kind of iterate on code to like get
*  the data set into some workable form. That's like the one agent experience I've had where I'm like,
*  wow, that thing actually kind of did what I would do where it ran into a problem and tried a couple
*  things to poke at it and eventually, you know, got to some sort of breakthrough. But that's I
*  really haven't achieved that with anything else outside of code interpreter. So how do you set
*  it up or kind of, you know, talk to it just the right way to get that to actually happen for you
*  on your own little projects? I mean, I think the one I've used most because it's like it's this
*  one's easy to kind of explain to also, maybe my versions aren't that stable. So actually, sometimes
*  we'll use a different tool called baby AGI UI that someone else separately created on, I think,
*  type JS, but it's actually more stable. So I use that one a lot for research, for web research. But
*  I had a lot of companies reach out to me after baby AGI wanting to know about, you know, how they
*  should be using large language models. This is in one of my very calm, anytime I'm jumping on a
*  company call with a big company that's well known in public, I will always ask baby AGI to research
*  the company, research their business units, research their revenue drivers, research their
*  cost drivers, and for each business unit, come up with three strategies that leverage large language
*  models that would be impactful to the business. And then I just step away and it takes a few
*  minutes to do because it's a lot of web search, a lot of calls. But when I sit down, you know,
*  if they have seven business units, it's like this company, seven business units, three ideas each,
*  that's 21 ideas that's prepared for me. And as I jump on a call, I quickly glance through the
*  21 ideas and I'm fully prepared to like blow them away because I can just pick three or three to
*  five of them and then just expand on it from my own knowledge. That makes a lot of sense in the
*  context. How reliable do you find it to be? Is it getting all the business units? You know,
*  how often are we kind of missing things? And maybe it doesn't matter in an intro call context where
*  you just want to be like prepared to be impressive. But actually, I think that your question brings
*  up a good point. A lot of people ask me, where should we start with using AI? And what I tell
*  them is start using AI and automations in things that you wish you were doing but don't have time
*  to do. Not the things that you are doing and are critical to. Because at first, it's not going to be
*  doing it yourself is going to be better. And replacing a task that's being done by a person
*  with AI to get worse output is not how you should start using AI. And it's not where you should
*  start experimenting and messing around. Like you have a good human workflow. So like doing
*  deep research into somebody right before you jump on a meeting is something I wish I had time to,
*  but I usually don't. So for me, if it misses a business unit, or if it comes up with ideas
*  that aren't good, I can easily like, you know, it's better than not having one. Don't say the ones
*  that aren't good. Yeah. Yeah, just don't say the ones that aren't good. And if it misses one,
*  then I notice it during the call, I can probably come up with ideas on my own. But it's more just
*  like it takes me, you know, a 10 second prompt and a 30 second review to do what would have taken me,
*  you know, 15 minutes of research. I had a time. So this is actually maybe a perfect intersection.
*  The things that people wish they were doing that they're not doing, or, you know, no kind of feel
*  like they should be doing and just can't get around to, I think intersects very naturally with
*  something that I understand was kind of a unique approach that you had originally with the
*  VC fund, which was sourcing your deal flow with outbound. So that's fascinating, because I think
*  almost every company, almost every organization would be like, you know, should I be doing more
*  outbound? Yeah, probably. Right. Everybody needs more sales. You know, everybody has kind of at
*  least experimented with like, yeah, I could go find a ton of people on LinkedIn and message them.
*  But you know, the hit rate is really low. And obviously, you know, it can be time consuming.
*  Same deal on like recruiting, you know, if you're trying to source candidates, man, would it be
*  nice if I could, you know, reach out to 10,000, you know, candidates? Yeah, but you know, who has
*  time for that? Right. So take people through that a little bit on from your expertise originally in
*  outbound. And then now, you know, everybody's kind of sitting there thinking, yeah, I should be doing
*  more of this. How would you coach them on how to get started with that near universal problem?
*  I mean, one to have a have an outbound funnel. Well, I mean, even if it's a Google Sheet, just
*  have a list, have a list where you can put people's names if you want to reach out to them. Right. And
*  that's the most important thing is like, just have a place you can put it. Once you have that place,
*  if you want to, depending on where you're stuck, if you're if you're having trouble
*  getting people's names on there, then you could connect, you know, a bookmarking tool like pocket
*  to it using Zapier so that if you come across somebody's LinkedIn, and you want to reach out
*  to them, you can just press pocket, and it would take you know, bookmark it in pocket. And then you
*  connect pocket to your Google Sheet or air table, and it would just start adding people to it.
*  And so like that works. That's that's the let's get stuff into my funnel really quickly is use like a
*  bookmarking tool of sorts that you can just and I use pocket for anytime I find a startup URL use
*  pocket. It's on my Chrome. It's on my mobile so I can use it from anywhere. So that's kind of the
*  step one is just like, get to a point where you have a list and your list is growing. Once you have
*  that, then you need to figure out how you're going to reach out to them. If you are going to reach
*  out to them using that I use a tool called Walla Norbert, V O I L A N O R B E R T. But there's a
*  couple of many other tools to get email addresses, whether it's clear bit hunter. So you need to
*  figure out how you're going to reach out to them. So in my case, if I have their name and domain
*  name, or you know, name and domain name, Norbert will find their email address for me. So then now
*  you have a list of people and all their email addresses. And then I guess if you don't want to
*  automatically send an email, but you can build a template, you know, you could use something like
*  Zapier, where you have a checkbox column, or if you when you check the column, if there's an email
*  address, it'll kick off his app, and it'll go to a template. And then it can send them an email.
*  And if you want to personalize it more, you can just create a new column in your Google Sheet,
*  where you would type in the personalized message, and then just pull that into the email message.
*  And you can just do that directly in Zapier. And if you just do what I did, what I said, then now
*  you have now you can just go through, go look at people's LinkedIn, click pocket, which will pull
*  their name and maybe company name. And if it's hooked up correctly, it'll automatically find their
*  email. And you can just go through type in a personalized message, click check, and it would
*  automatically send an email from your email address to them. Interesting that you're you're not
*  automating, if I understand correctly, there the personalization step? Yeah, I guess if you wanted
*  to use AI to personalize it, then you would take whatever data you were fed in. And you can just
*  add an open AI step in Zapier to like send the personalized info to open AI and say, can you
*  write the precise message? Actually, that would make more sense if you have that info. That caught
*  my ear because I was thinking like, maybe you didn't trust it to do that? Or I actually write
*  all my outbound emails myself. I did a lot of A B testing at Techstars on outbound emails. And I
*  found that, you know, two to three sentence emails just performed the best. And so when I'm like
*  reaching out to somebody, I just send them like two to three sentences, that's directly to the
*  point that's like personalized. And my bottleneck is my time. Like I can send a lot of outbound emails,
*  like, but I just don't have the time to take all the meetings. So that's not what my bottleneck is.
*  So I guess that's probably one of the reasons I write my emails. Interesting. Yeah, that'd be
*  different for most sales organizations where you probably have a pretty high accept rate on the
*  outbound to the meeting. Yeah. So yeah, that's probably it. It's like if I send an outbound
*  email, I'm probably going to get the meeting. So I got to, if anything, my issue is if I send
*  too many outbound emails at once, my calendar gets too full. So where would people start today
*  if they want to get into this kind of agents stuff? Obviously, you know, a lot of different
*  projects out there. I saw you tweeted the other day too, that you were cited in a new paper
*  that introduced a whole framework for agents. I can imagine you might feel like that's the place
*  to start, or you might feel like, yeah, it's kind of overbuilt, you know, maybe start with something
*  simpler, and then, you know, graduate to something, you know, more full featured. But what's your
*  advice on just, you know, day one with agents for a, let's say, an AI engineer who's like actually
*  going to get into it now? I'll caveat that like, I haven't gone through like, looking at like,
*  where would I start since the agent space started, because I, you know, I was already in it. So,
*  so to some extent, I don't, I'm not fully caught up today. Obviously, auto GPT, if you haven't heard
*  of it, like really popular project, again, I haven't looked at it recently. But that one uses
*  kind of the react style agent where it's kind of doing one task and thinking through. So that's,
*  you know, I think it's one worth looking at. I think there's a lot of integration, there's probably
*  a lot to learn. I'm personally a big fan of Lang chain, Harrison chase. You can build an agent
*  with Lang chain. They also have a plan and execute agent, which Harrison said was inspired by baby
*  Asia to some extent, where it does generate a task list ahead of time, right? Lang chain agents were
*  initially react style where we just do one task, think about it and do the next, but their plan
*  and execute agent will plan tasks ahead of time. And the reason Lang chain, I think would be a good
*  place to start is because there's so many things built into Lang chain that like, if you start
*  just like learning how to play with Lang chain, you can actually just learn all the things that
*  you can do. And then if there's something you're really interested in, then you can just like,
*  do it without Lang chain. And that would be a good next step.
*  I guess maybe my last kind of big question on the agents before turning over to the investment side
*  of your, your activity is, are they all going to wake up when the GPT four V comes online? It seems
*  like so many of the problems to date have been just getting lost in kind of the friction of the
*  web and all this nonsense. You know, HTML is super bloated these days for all kinds of reasons,
*  but you know, the interfaces are meant to be interpreted visually. It seems like GPT four V
*  is really good at that. Do you think we're like on the verge of sort of a threshold effect where
*  all of a sudden they're going to be able to do like 10 times as much?
*  I mean, to some extent, yes. And I don't know, 10 times is whatever big number, like I feel like
*  anytime a new model, especially something if like GPT four V one that becomes bill was an API,
*  there's gonna be so much you can do that you couldn't do. So it is going to feel like, wow,
*  like these agents have 10 X, but I would suspect that it's going to, we're going to have many,
*  many moments like that. So it's going to feel like, oh man, they can do so much more, but we
*  just keep feeling like that every time there's like a new model or whatnot. Yeah. It's going
*  to be many of those moments where we're just going to continue to be impressed, but the reality is
*  like, we're incredibly complicated. So getting like where the agents are now to like being able
*  to do generalized can do anything the human can do is going to be a really long ways. And to some
*  extent, like the further along we get, the further the, the further the bar is going to get, like as
*  soon as agents can do everything online for us, it's going to be, oh yeah, your agent still can't
*  make coffee for me. And now we're going to be getting into robotics, which is also moving,
*  moving fast right now. So it's all going to merge together. But again, right? Like just because GPT
*  four V's out is like, it just moves the bar up to the next one. Is that a reasonable model? And my
*  first gut instinct is like, yeah, it does kind of seem like a reasonable model. I've been working on
*  this on, on kind of the safety and control side as well, because there's been some recent
*  research that's like, wow, that seems like it gives you like a whole order of magnitude improvement
*  on ability to detect bad behavior in models or whatever. And then you're also kind of like, but
*  you know, order of magnitude, if it's really serious, you know, that there's still a long
*  way to go is still like multiple orders of magnitude needed. On the agent side, it's kind
*  of coming the other direction where, you know, baby AGI can maybe do like one in a million things
*  that a human could do in its original form. And maybe we're headed for like 1% pretty soon.
*  And those next two orders of magnitude, like, I wonder how quickly they come. It seems like,
*  it seems like you don't think they're going to come that fast, but I wouldn't be shocked
*  if we're sitting here. I know. I think there will be things that go fast. The question I don't know,
*  and again, this is like beyond my technical capability, but I do feel like there's, I mean,
*  like I'm experimenting what you call the orchestration layer, right? That you're kind
*  of stripping it out of the model and doing it in orchestration. But it does seem like a lot of the
*  stuff, the learning from building in the orchestration layer can just basically be baked into the model.
*  Again, that's, that's a little bit beyond my technical capability. But I think if we start
*  seeing stuff like that, like models that are building, you know, that can, that can, you know,
*  multimodal, like in do a web search from within the model somehow. I don't know if that's even
*  possible, but like to decide to do a web search and then like write new skills and store it,
*  like the stuff that we're orchestrating, if that can be done within the model, I do think that's
*  going to move so fast. But again, I don't know if and when that's possible. It does seem like it's
*  at least somewhat possible and yeah, and somewhat coming soon, but yeah, we'll have to see just how
*  fast. So let's turn then to the investment angle. And you know, you could either take this from a
*  sort of what you're looking for, or, you know, maybe more of an advice to founders, but I'm
*  really interested in just kind of, you know, everybody has this big question, right? Where is
*  the value going to accrue? Is anything defensible? Everything's moving so fast, you know, it's, I
*  think become pretty fashionable to say like the incumbents will probably keep all the value in this
*  wave because they've already got the distribution and it's like pretty easy to implement the AI.
*  So what's your take? I think at a high level, we can all agree that a lot of value is going to be
*  created compared to previous tech innovations. Incumbents will get a larger share of that value
*  and that comes from largely noticing that both the C levels at every large company know they need to
*  do it. And like every, like many engineers are just curious and want to play with it themselves. And
*  I think if you have those two things, it's enough to kind of, it's a lot, it's a lot more than we've
*  ever seen, right? It's usually like the engineers are interested in a technology or the C level
*  wants to do it, but the other side doesn't, but you have both in AI. So incumbents will move fast.
*  They will capture value. There's no question about that. That being said, I don't think there's any
*  technical technological innovation where incumbents are going to capture 100% of the value. It's just
*  a matter of what's the ratio going to be. And because there's so much value to be created,
*  I think there's ton of value to be captured by startups compared to even other past technical
*  innovations. Cause if it's, you know, even if, even if incumbents took 90%, which I don't think
*  they will of the value created, literally AI is probably, you know, a hundred X bigger in terms
*  of value creation than many technical technological innovations we've seen. So, so in that sense,
*  there'll be plenty of value to be accrued by startups. So I think it's still a good,
*  great time to be investing in startups, but also to look at public markets to some extent, I guess.
*  I don't know that I've ever heard anybody put it quite that way, you know, senior leadership at
*  companies and rank and file developers, both being inclined to embrace a technology at the same time.
*  I don't know that I've ever heard it described that way, but I do think that is really apt.
*  I just had a little bit of an experience like this over the last day at Athena. And this is an
*  executive assistant company where I'm the AI advisor. You know, it was, I was just struck in
*  the last 24 hours that talking to founders and then talking to a person who was hired at the
*  company as a software developer, not as an AI role, both are like obsessed with AI and, you know,
*  like literally reading papers, you know, it's a, you don't see people like reading work out of like
*  academic labs in their professional life super often. And now we have people like going way out
*  of role to do it. It is really a remarkable moment. I think that's a fantastic observation.
*  And just to even add to that, I think, you know, just like, I mean, to some extent, like agents,
*  like just because you have an idea and want to do it, doesn't mean you're going to do it well.
*  So there are going to be a lot of large companies who are going to lean in and try to do AI.
*  And again, I'm not, I don't know what percentage, but there's going to be a percentage of them that
*  are not going to do it well, which means they're going to end up possibly buying a startup, buying
*  from startups. And some of those people who learned about the technology and the industry
*  and tried to build it internally, but ran into whatever issues are going to spin off and build
*  their own company to tackle that market or something like that. So there's still going to,
*  even if incumbents are leaning in just because they're leaning in, doesn't mean they're going
*  to do it right. And the people who don't do it right, that energy will shift into, I believe,
*  the startup market. Okay. So I give you a super strong marks on your analysis on the incumbent
*  versus startup split. Let's try the layer version of it. People are again like, well, the chips are
*  going to make a lot of money, but maybe the applications do, maybe they don't, it's so easy
*  to spin up applications. Maybe it's the tooling, maybe it's the model providers. Do you have a
*  similar thesis on how you think about the layers of the stack? I guess so to some extent, I do
*  think, I mean, hardware, just because of scale benefits, there's probably not going to be too
*  many. You're not going to see a world with tons of really, really, really big hardware companies
*  building these chips. I would guess it would be somewhat consolidated models. I would say maybe
*  a little bit less consolidated. It still takes a lot of money to build, but we're seeing more and
*  more tooling to like spin up models of your own, open source models, smaller, more specialized
*  models. There's probably going to be some variation, but as far as like the core foundational models,
*  it'll probably stay to some extent consolidated as my guess. Not saying there's no room for new
*  ones, but as a pre-seed investor, I'm noticing that all of these rounds are $100 million kickoff
*  round. It's one to keep an eye on, but not one I'm diligencing too deeply.
*  Infra is the most confusing one where you have these extremely popular infrastructure projects
*  that are fully open sourcing and making money that have raised a lot of money. You're seeing that,
*  and they're clearly creating a ton of value, but their ability to capture value, I think,
*  is still in question. I'm not saying they can't, but I don't think we've seen them all.
*  I think that it'll be interesting to follow that. I think because people aren't sure what's going to
*  happen to some extent, I think there is opportunity if you can come up with conviction and invest.
*  If you're right, you'll probably make money in the infra layer. Then the application layer,
*  I think there's going to be a lot of value created. There's going to be a lot of companies.
*  A lot of them are going to be niche specific use cases that are core AI. Then there's going to be
*  some that barely use AI, but because they use AI, they're going to beat everyone else who doesn't
*  use AI. I think there's a lot of different business models in the application layer.
*  I don't know which one's going to be the best, but I think a lot of them are good ideas. One of the
*  ways I'm thinking about it is diversifying, at least in the application layer, the types of
*  business models so that I have some hedging on that as well. Multiple follow-up questions there,
*  but do you have a taxonomy for the business models? That's probably a good idea right now.
*  Not specifically, but there's some using LLMs on the backend, for example, to take unstructured
*  data or whatever data around the web to build clean structured data, but then the front end
*  doesn't use that much AI. Those actually have much higher margins because they're just using
*  LLM ones to collect the data and they're not using LLMs on every usage. The margins are higher,
*  so that's an interesting model. That being said, it might be less defensible to some extent because
*  if the unstructured data is public, for example, someone else could in theory
*  collect that structured data as well. The most common one is the wrapper,
*  which is less defensible from a product standpoint, but if you can ingrain deeply
*  into the user's workflow and be something they need and grow fast enough and get market share,
*  then that market share could be defensible, especially if you can keep building
*  value on top of it. That makes the switching cost higher. That's probably the most common model.
*  Scaled services is what I'm looking at. I think the idea that the reason SaaS is so popular amongst
*  VCs and why it is popular is because SaaS is scalable. Software is scalable, but now that we
*  have with LLMs, we can make customer service scalable. We can make sales scalable. We can build
*  companies where it feels like a service to the end user, but on the backend, they're using AI
*  and automations to scale rapidly. I think that's an interesting business model and I'm seeing more
*  of those that kind of hint at that. Those are a couple examples. Then I think one,
*  this isn't really a business model, but more so I do think there's probably room for companies that
*  just use LLMs well internally. If you look at it from the outside, it's not an AI company,
*  it's no AI in the product, but the way the company operates, the way the leadership guides their
*  employees to use LLMs and AI tools is just so efficient that they're just operating as a
*  company 10 times more efficiently than their competitors. Even down to the local business
*  level, just having a decent chat on your website that nobody else in your immediate competitive
*  set has huge advantages to some simple stuff these days. How about the enterprise retail divide?
*  I think you may have even better information on this than I do, but my general sense on the retail
*  side right now is that all these apps are posting really good growth numbers,
*  but typically with pretty poor retention with maybe few exceptions. I wonder if that's kind
*  of what you see as well and if so, does that lead you to think more about trying to invest in
*  enterprise serving companies? I think it's a fair generalized observation. I think part of it is
*  because people are interested. If there's five legal AI tools and the lawyer is really interested
*  in AI, they might jump and try all five, but they're not going to keep using all five, which
*  means if the average user is trying five tools, then there's going to be 20% retention, assuming
*  they end up on tools. To some extent, retention being low is just because people are interested
*  in actually exploring and trying to find the right tools for themselves. That's also a good thing.
*  I think it was Sarah who mentioned this in her TED AI talk. Sarah, she had a good one too. I'm
*  excited to watch it again when it comes out, but she talked about minimum viable quality for AI
*  tools and I do think that's a thing. It's not just about getting the tool out there, but making sure
*  it has quality output. I think with these companies, it's not just about getting distribution,
*  but also about ensuring quality because people will switch, people will churn.
*  To answer your question from a more high level, I do think there's the retail,
*  is that. One aspect, one theme I'm seeing is more consulting first enterprise approaches.
*  I've heard the name Palantir come up in a handful of conversations, probably not surprisingly,
*  but they're doing more stuff there. There's a company called Distil that's some ex-Palantir
*  guys doing similar. I think there's the kind of enterprises want handholding and consulting more
*  and they have the money to throw down to it. It actually is an interesting go to market right now
*  to start enterprise consulting to be able to bring in money, hire good talent, work on really good
*  problems, and then maybe automate that process a little bit and decrease the cost to target a
*  larger audience as you go, which I think is a strong model if you can pull it off.
*  It's definitely a good time for consultants in general because there's a lot of people with a
*  lot of questions. It is one of these rare moments where, and I'm not a huge believer in consultants
*  in all cases by any means, but there is this just huge knowledge gap where I find so often,
*  I'm sure you have this too, where people will come out of the woodwork and ask me a question.
*  Often, it's pretty easy to answer. I can just answer pretty quickly and be like,
*  oh, you want to set up the simplest possible chat bot that has access to your documents? Boom,
*  go to chatbase.co. You'll be up and running in 15 minutes. I've tried 10 of these and this one
*  lays really simple and good. People are like, oh my God, you're a genius. I'm like, honestly,
*  there's not even that much genius there. I usually do tell them. It's just a knowledge gap that
*  will close, but for the moment, definitely makes a consultant often pretty valuable.
*  I had one more. New things versus old things. This is another Sarah comment. She said that
*  they're looking at some of these fundamentally new behaviors like talking to an AI bot all the time.
*  We've had Eugenia from Replica on the show. Character obviously is a leader in this
*  space to the point where Facebook is potentially going to try to do their Facebook thing and
*  make it and suddenly ship it to 3 billion people. How much do you find yourself thinking about
*  ways to apply AI to current things versus just fundamentally new experiences or products or
*  ways to spend your time that are only possible now with AI?
*  I think the latter excites me more, but I spend my time thinking about both equally to some extent
*  because to some extent, I think the first ones are easier to at least make money in the short run.
*  It's a fuzzy question because an old thing with AI can look like a very new thing.
*  Coding, honestly, going back to one of your things at the top where you said
*  you have all these projects and you go pull out a snippet from whatever.
*  I find myself doing that these days when I'm coding for the purpose, not even so much of me to adapt
*  it, but you may have a better term for this, but I've been calling it coding by analogy.
*  Basically, what I'll do is take whatever I have to GPT-4 and say, hey, here's what I have.
*  It helps if it's working. Here's what I want. It is damn good at making that jump.
*  I think that is a fundamentally new experience. I basically don't code
*  manually anymore, almost at all. My fingers barely work.
*  Especially on mobile replate, it's hard to copy paste specific lines,
*  so I'm usually copy pasting whole files back and forth.
*  That's a pretty profound shift, I think, in what that experience looks like.
*  How about out of your portfolio, anything that you would want to highlight as either,
*  really examples of any of these things we've talked about, but I'd love to hear some of the
*  things that have sparked enough conviction in you that you've actually invested in them.
*  Obviously, AI was one of my first AI investments. Actually, that was back in 2020. During the
*  no-code time, they had a no-code AI tool, and they built out this incredible tool that can do both
*  traditional AI in terms of predicting columns based on past data, but also LLM tools.
*  The approach they've taken recently is actually just acting like a service. They have a data
*  scientist's service for a thousand bucks a month, and they have internal people who know how to use
*  their internal tools really well and really efficiently. From a company perspective,
*  they just work with their data scientists with an open, obviously, AI, who will do all the cleaning
*  of data, all the predictions, all the setting up whatever APIs or whatever you need. But really,
*  it's just team members internally who are good at using a tool they've really robustly built out.
*  That falls into this scaled services model that they've pivoted into. I think that approach is
*  really clever and fit in well. Not to ask you for any numbers that they
*  haven't disclosed, but you've got to have pretty serious leverage. I guess it obviously depends on
*  what your SLA is in terms of what service commitments you're making. But a thousand
*  dollars a month doesn't buy you a big fraction of a data scientist in today's market. So,
*  sounds like inherently they've got to have one data scientist supporting at least 20 companies,
*  right? Probably more than that. I'm not going to go into specific numbers,
*  like you said, but there's definitely scaled benefits to having a platform that can do a lot
*  of the work. If you ask a data scientist at a slightly old company, the amount of time they
*  spent on cleaning data and doing stuff that they don't need to do is pretty high. So, if you have
*  built tools to automate that part, then you can definitely be more efficient. Yeah, that's
*  fascinating. I do think that sounds like a pretty compelling offering at a minimum.
*  I've spent a lot of time in media. I used to work with the Disney accelerator. I've consulted for
*  Nintendo a lot. So, that's an area I just get attracted to. I have two companies, I guess three
*  companies in the media space, that does prompt to video. They started really more around grabbing
*  media clips from around the web to put them together for you based on a prompt or based on
*  transcribing a video, but they've layered on LLM so you can kind of just describe the video on.
*  It'll write a script, it'll create an audio output, it'll chunk it up and find media from online to
*  basically put together a full video for you. Space I know you're familiar with. Spexed is kind of in
*  the podcast slash YouTube space. They started as more closer to kind of what's the one that a lot
*  of people use, Descript, but they've really layered on clever LLM. So, for all the videos that, you
*  know, and you can have it in Discord or Zoom, you know, they kind of bake, you can bake it into
*  Discord or Zoom to record stuff. It'll do chapter summaries, it'll do takeaways, and you can ask
*  questions directly on the video. More recently, they've expanded to being able to do full libraries.
*  So, if you just give the YouTube channel, it'll just go transcribe all the videos. You can ask it
*  a question and it'll give you all the short clips that are most relevant to that question that you
*  can just jump to from anywhere in their library. And also, you can just kind of ask general questions
*  against the YouTube library. So, that one's pretty powerful. And then they've also built out video
*  editing features on the back end. So, the video creators, once the library is connected, can say,
*  hey, can you find a clip about, you know, AI doomerism and clip out a 10-second clip and then
*  add our opening title to it. And so, just kind of natural language, you know, engagement against
*  the whole video library is what they've been building out recently. It seems like there's a
*  tremendous possibility, although I'm not sure it's necessarily what people want, but
*  the opportunity for sort of semi-dynamically generated content experiences, whether it's games
*  or video, but kind of choose your own adventure style media. Do you think that is going to be a
*  thing? I do. I mean, I thought the Black Mirror one was pretty interesting, especially with LMs.
*  I mean, to some extent, like that, you know, that there's a blurred line between a choose your own
*  adventure media experience and a video game. Video games to some extent is that, I think.
*  So, blurring the line is interesting and especially, you know, from an education angle,
*  if designed correctly, I think it can accelerate somebody's learning if you can keep them both
*  engaged and interested and layering on content at the right level for that person in the right way.
*  It could really accelerate learning or just, you know, I guess learning about anything.
*  What I noticed in your portfolio is this company's senior sign. And I don't know if they have an AI
*  component to what they're doing right now, but I love the fact that you invested in a technology
*  company specifically focused on the senior market, because that's been a longstanding thesis for me,
*  you know, especially as demographics shift, you know, is underway in some parts of the world and
*  getting underway here in my part of the world as well. It seems like this disconnect between the
*  technology that we have and what seniors actually can benefit from is just so huge. AI seems like a
*  great way to bridge that gap. Have you been seeing any deals or do you have any kind of
*  ideas as to what might take shape there? That's fascinating. Senior sign was more
*  my no code phase. I mean, the fact that people are onboarding on the senior care centers and
*  huge paper digital binders, they're just mind blowing to me that that still exists. But yeah,
*  I mean, I think AI can be very powerful there. And I'm excited to see what kind of products
*  people build around that. I think there is some hesitation, I think, from generally from older
*  people get against technology. So it'll be interesting on the right go to market and approach
*  on creating AI that seniors would want to talk to. Yeah, that talk to I think is the key phrase
*  because it my grandmother, for example, has an Alexa device at, you know, her side table at the
*  end of the couch, and she'll use it to play music. And she does kind of personify it quite a bit. And
*  she's like, fully with it. But you know, she'll say, Oh, she wasn't playing it for me today and
*  stuff like that. And I'm excited, you know, and she spends most of her time alone. She actually
*  has pretty good support network as individuals in their 90s go for sure, but still spends most of
*  her time alone. And I do think just, you know, a little more conversation. And you can imagine kind
*  of creating a profile in the background that you know, the AI could kind of, you know, it doesn't
*  have to be that customized, you know, the smallest gesture from the staff where she lives is, you
*  know, something that really makes her day. And I also think there's something interesting about
*  seniors where they're like, this is my grandfather was especially this way, not at all cynical about
*  things that were in fact, kind of contrived, you know, we would sometimes you go to this, like,
*  you know, kind of faux downtown or some, you know, some like historical building or whatever it is,
*  like, this is so fake, you know, Pavon, but he loved it. You know, he didn't care if it was like
*  made, you know, for this purpose or not, like he would still find great pleasure in it. Old people
*  in many cases are really endearing in that way. And maybe in some ways could be like more receptive
*  to these like AI conversation partners, because they're just like not jaded. I have this mixed
*  emotional reaction to this though, like on one hand, I'm like, yes, I want people to feel heard
*  and like connected and like the idea that someone doesn't have to sit there lonely,
*  especially I think that's happening more and more is good. But at the same time, like,
*  there's also like probably the old school part of me that's like, I want to make sure people have
*  human relationships. And if they get too close, there's an AI that's too empathetic, like, are
*  they going to not want to connect with humans anymore? And is that is that good for us? Is a
*  question. And maybe the answer is it is fine. But I don't know. I think it's a very, very good
*  question to ask. And I felt this way about our when I spent a decent amount of time actually
*  using the replica app, when I had the interview with Eugenia, the CEO there, and it was fascinating
*  in many ways. But one of the ways that was honestly, maybe the most interesting was,
*  this was still pre GPT four, and like pre a big price drop. So she didn't have the ability to like
*  do super advanced conversation as cheap as it is today. And the my actual experience of the app was
*  like, it wasn't super sophisticated in conversation. And yet, you know, she'd grown a big user base,
*  and lots of people really cared about it, and were genuinely emotionally invested in this.
*  And my takeaway from that was like, a lot of people really need this kind of stuff. And for the
*  audience that she had at the time, I came away feeling like this has got to be very positive
*  for a lot of people because, you know, it's a tough world out there. And a lot of people don't
*  have a lot of things that, you know, I'm maybe privileged to take for granted. But then I also
*  just like you, I was like, but as this stuff gets really good, you know, and it's like becomes the
*  norm, or it starts to, you know, it's one thing to use this as almost like a treatment for people
*  that are struggling. And it's quite a different thing for it to be, you know, the norm among
*  there are going to be couples who break up because they're, you know, the girlfriend is upset at the
*  boyfriend for sharing too much with his AI partner. I bet that's already out there. Yeah,
*  probably. Right. Like it's good. And it's gonna get weird. And then, I mean, I feel like this is
*  going to just go deeper, but this was an interesting conversation that came up with actually I had a
*  panel, the awesomest panel the day after Ted with Jim fan from Voyager, June from Sanford,
*  Smallville, and then Noam who did the AI for diplomacy game. So it was like a gaming for AI
*  panel. But the conversation did go at some point, it did touch on like, if you have an emotional
*  connection with an AI, they also inherently, to some extent, have some influential power over you.
*  And so if you give companies the skilled ability to control what a chat bot might nudge a person
*  to think, then it does kind of take that whole like, you know, there's a lot of responsibility
*  on that to nudge humans in the right direction or not take advantage of it. Just something to keep,
*  you know, keep an eye on, I guess, from the safety standpoint.
*  Yeah, absolutely. There's a great article on less wrong from early this year
*  by a person who had a pretty consuming and like borderline deranging experience of kind of falling
*  in love with a character on character AI. And you know, the fact that this was posted on less wrong
*  is remarkable. And the person, you know, upfront was like, I'm someone who should have known better
*  because I have a pretty good understanding of like, what these systems are, and, you know,
*  loosely how they work, at least. And yet, you know, it was so compelling experientially,
*  that he kind of, you know, lost himself in it for a while and eventually, like,
*  somehow pulled himself out of it. And, you know, with this post, but I would definitely encourage
*  anyone and certainly if you doubt the potential for these sorts of things to happen or think it,
*  you know, would only happen to someone who, you know, is dumb or, you know, whatever, like,
*  read this one and you'll hear a account from an intelligent person who was not super naive going
*  in and still kind of, you know, ended up in a strange, strange place. I'll check it out.
*  A couple of last questions and then we can let you go. You've been super generous with your time.
*  Building in public, you've done it and you've had great success with it.
*  Do you advise your companies to do it? I'm struck that there are some, you know, I think of like
*  Harvey, you know, Lindy is a former guest who basically are allowing no users outside of,
*  you know, in Lindy's case, just like, I think it's almost all internal still. Harvey has like big
*  customers, but they basically don't say anything in a world where like there's so, you know, like
*  the thousand people created like, you know, derivative projects of your baby AGI in two
*  seconds. How do you, do you advise people to like still put it all out there in public or maybe it's
*  just situational, but what's kind of your guidance on how much to build in public if you're building
*  an AI product today? I think it's situational. Absolutely. I mean, if you have a strong technical
*  team that you're confident can build the solution you want to build and you have connections,
*  then you have deep connections and intro like in ways to connect into large enterprise customers
*  who can pay you a lot of money. The incentive to open source actually, I think is pretty low.
*  You should just build the product and sell it on the flip side. For example, if you, if you're,
*  you know, if you grew up sometime outside of like a major hub, you don't have any connections,
*  don't know anybody and you want to build a dev tool, then open solution makes a ton of sense
*  because if you can get people excited about your open source projects, suddenly you've built a
*  network of people who are familiar with you and your work and they're even probably contributing
*  to you and suddenly you have friends that you can build alongside. And then a lot of companies fall
*  into the middle of like somewhere between that, but not a lot of people starting companies are
*  like, I have all my customers handy, like ready to go. A lot of people are trying to sell to
*  customers. So open source is a, is a decent marketing, it's a good marketing technique,
*  especially if there's, if there's a technical aspect where you need developer buy-in from your
*  buyers, then if you can have a popular open source project, then you've already gained credibility
*  in some of the key players of your potential buyers. So it can decrease your sales cycle,
*  right? If you decide to go commercial open source and build a commercial layer on top,
*  but there are a lot of approaches. I don't, I, I'm not going to say I know what the right way is.
*  Observing and learning a lot. I'm actually interestingly, if you're, if you are interested
*  in this open source commercializing question or group to follow is OSS Capital. JJ there,
*  they run the commercial cost, I think commercial open source, like conference. So he's put out a
*  lot of content around approaches to commercializing open source. So I've learned a lot from him and
*  actually he was the person who convinced me to open source baby AGI. Okay, cool. That's a great
*  recommendation. Two more questions. One kind of big, super big picture, one a little more personal.
*  I used to ask this question every interview and then I kind of went away from it, but just recently
*  at the AI engineer summit, there was a survey result presented where seemingly in a, you know,
*  pretty neutral, although I took the survey, otherwise pretty neutral survey, which was like
*  about, you know, what tools do you use? And, you know, do you like Lang chain or, you know,
*  llama index or whatever. Those were kind of most of the questions. Then there was this question of
*  it was simply put P doom question mark and people filled it in and then they showed the results and
*  the results were all over the spectrum. Basically you could call it the uniform distribution to a
*  first approximation. I thought that was extremely striking because it was like, there's definitely
*  no agreement on this. And you know, it's obviously super important if there is a serious chance of
*  P doom. What's your take on that? Do you spend time worrying about it? Do you think about it?
*  Somebody actually talked about, asked the question during the dinner and I had an answer. I think I
*  think about it slightly differently. I think just asking P doom actually as a question to me,
*  doesn't make sense without like a specific timeline. Although if you gave me a timeline,
*  I would tell you, I don't have an answer. I think of it more as like P doom, which is like P doom,
*  not specific to AI. I think it was a hundred, meaning like, I don't think humans will be around
*  in a billion years. And so the question just becomes like, what is the likelihood that doom
*  comes from AI? Because there's a lot of other reasons for doom. It could be a comment. It could
*  just be time. It could be, you know, it could be a bigger pandemic with the worst disease or whatnot.
*  And then when you start thinking about it that way, you do quickly realize AI does touch on a
*  lot of other things, but ultimately it's like a combination of AI and human. Right. I think the
*  most likely scenario is some sort of combination of human using technology wrong, right. Whether
*  it's, you know, whether it's nukes or creating diseases or whatnot, and maybe AI is part of
*  building that solution. So I guess my answer becomes P doom a hundred. But then if you're
*  going to ask that question, I think it's also important to think about the benefit of AI,
*  which is that it can actually solve against some of the other doom scenarios. So actually, if it,
*  if it decreases the likelihood of other, other doom scenarios from at least the way I'm thinking
*  about it, it increases the P doom of AI, because if the other likelihood goes down, the likelihood
*  of AI goes up. It's it's interconnected is what I'm trying to say. And it's a hard question to
*  answer, but that's the, that's the framework I think about it, but I don't actually have a good
*  answer. Yeah. Do you have a sense for which direction we're traveling relative to five
*  years ago? Do you think that there is a, let's just say like our natural, you know, expected
*  lifespan, do you think there is a notably higher or lower P doom in light of all the AI developments?
*  I believe we're on a path to a much better future, but I say that knowing that I'm an optimist.
*  And I believe the pessimists against it are also just that voice is just as important. So I say,
*  I'm hopeful, but that's how I feel personally. But I think it's the, the discourse is extremely
*  important amongst both sides. I think I sort of share that perspective. I don't know that I would
*  say I'm an optimist necessarily, but I do see, you know, I get so excited about the tremendous
*  upside potential of AI. And I guess I, maybe my answer would be like, it feels like the
*  distribution has shifted toward more of a bi-modal where, you know, things could go really amazing,
*  or, you know, we could have some really crazy shit that could be really bad, but definitely both,
*  you know, are very much in play in my mind. But again, I know like, it's like saying like,
*  oh, should we do, should we do healthcare research? Because like, what's the likelihood that if we,
*  you know, if we continue to research healthcare, we're going to eventually create a disease that
*  can wipe out humanity. Well, I would shut down some of that gain of function research. You know,
*  I don't, I do take a position on that one. Right. I think there are certain health type of research
*  that maybe you should consider, but that's a good, that is a good differentiation between
*  calling it health research versus like specific type of health research. And I think saying,
*  should we stop AI progress? Or if, if it is a specific type of AI that's dangerous, like
*  we can, let's talk about what that should be. But I think broadly saying, should AI slow down is
*  similar to saying, should we broadly slow down healthcare research? But I think the answer,
*  everyone says is wrong. What would you say you have learned about yourself in the process of
*  creating all these AI projects and, you know, mini-yohei and all those things? I think I realize how
*  not complicated we probably are to some extent. We are very complicated at the same time. A lot
*  of the way we work, especially is simplified, like our work selves, like because of, to some extent,
*  I think industrial revolution and making jobs, ones that you can replace one person with another.
*  So the way our industry has evolved, just industry in general has evolved is like, let's make jobs
*  that we can easily replace one person for another, which means simplifying the job and task to a
*  point that I actually think is actually pretty easy to map. So what I figured out, I guess,
*  to some extent, I've been fascinated at how simple we are when it comes to how we work,
*  actually, to some extent. Yeah. How much of what we do is in fact pretty routine.
*  Yeah. Like how much of what we do can be automated is mind blowing. And it's not easy to get to a
*  point where we've automated everything, but like a large portion of work in most jobs can be
*  automated with the tools we have today. If we just built it and innovated the right way, which is
*  difficult part. Yeah. Well, you've taken a nice little bite out of that grand challenge personally
*  and been someone that I've really enjoyed following and inspired many with your projects,
*  including Baby AGI. So we will look forward to the release of the Ted Talk coming soon.
*  And for now, I'll just say, Yohei Nakajima, thank you for being part of the Cognitive Revolution.
*  Thank you for having me. That was fun. It is both energizing and enlightening to hear why
*  people listen and learn what they value about the show. So please don't hesitate to reach out
*  via email at tcr at turpentine.co or you can DM me on the social media platform of your choice.
*  Omniki uses generative AI to enable you to launch hundreds of thousands of ad iterations that
*  actually work customized across all platforms with a click of a button. I believe in Omniki
*  so much that I invested in it and I recommend you use it too. Use Cogrev to get a 10% discount.

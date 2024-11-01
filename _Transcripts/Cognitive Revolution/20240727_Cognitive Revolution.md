---
Date Generated: October 30, 2024
Transcription Model: whisper medium 20231117
Length: 5565s
Video Keywords: []
Video Views: 1856
Video Rating: None
Video Description: Nathan Labenz joins the Nick Halaris Show to discuss the current AI landscape, balancing enthusiasm with critical analysis. This episode of The Cognitive Revolution explores AI's transformative potential in medicine, law, and automation, while addressing concerns about safety, control, and geopolitical implications. Join us for an insightful conversation on responsible AI development and its impact on society.

Apply to join over 400 founders and execs in the Turpentine Network: https://hmplogxqz0y.typeform.com/to/JCkphVqj

This episode originally appeared on the Nick Halaris show. Check out the channel here : https://www.youtube.com/watch?v=UR54We1-FLw&t=12s

RECOMMENDED PODCAST: Complex Systems
Patrick McKenzie (@patio11) talks to experts who understand the complicated but not unknowable systems we rely on. You might be surprised at how quickly Patrick and his guests can put you in the top 1% of understanding for stock trading, tech hiring, and more.
Spotify: https://open.spotify.com/show/3Mos4VE3figVXleHDqfXOH
Apple: https://podcasts.apple.com/us/podcast/complex-systems-with-patrick-mckenzie-patio11/id1753399812

SPONSORS:
Building an enterprise-ready SaaS app? WorkOS has got you covered with easy-to-integrate APIs for SAML, SCIM, and more. Join top startups like Vercel, Perplexity, Jasper & Webflow in powering your app with WorkOS. Enjoy a free tier for up to 1M users! Start now at https://bit.ly/WorkOS-TCR 

Oracle Cloud Infrastructure (OCI) is a single platform for your infrastructure, database, application development, and AI needs. OCI has four to eight times the bandwidth of other clouds; offers one consistent price, and nobody does data better than Oracle. If you want to do more and spend less, take a free test drive of OCI at https://oracle.com/cognitive

The Brave search API can be used to assemble a data set to train your AI models and help with retrieval augmentation at the time of inference. All while remaining affordable with developer first pricing, integrating the Brave search API into your workflow translates to more ethical data sourcing and more human representative data sets. Try the Brave search API for free for up to 2000 queries per month at https://bit.ly/BraveTCR

Omneky is an omnichannel creative generation platform that lets you launch hundreds of thousands of ad iterations that actually work customized across all platforms, with a click of a button. Omneky combines generative AI and real-time advertising data. Mention "Cog Rev" for 10% off https://www.omneky.com/

Head to Squad to access global engineering without the headache and at a fraction of the cost: head to https://choosesquad.com/ and mention “Turpentine” to skip the waitlist.

CHAPTERS:
(00:00:00) About the Show
(00:00:25) Sponsor: WorkOS
(00:01:25) About the Show
(00:03:36) Intro
(00:05:53) How did you get into AI?
(00:11:09) The power of the transformer
(00:14:16) Waymark growth
(00:19:00) Sponsors: Oracle | Brave
(00:21:04) The potential benefits of AI
(00:26:45) AI in law
(00:28:04) Robotics and food preparation
(00:32:33) Sponsors: Omneky | Squad
(00:34:20) AI and mass inequality
(00:35:26) AI could lead to Universal Basic Income
(00:37:37) AI supply and the future of work
(00:40:53) The AI future
(00:43:38) The new social contract
(00:47:06) Optimism about the future
(00:53:19) What are people afraid of?
(00:58:31) Reinforcement learning from human feedback
(00:59:42) Instrumental convergence
(01:03:00) Current safety concerns
(01:07:56) What did Ilya see?
(01:10:23) Who controls AI?
(01:13:23) China
(01:16:05) Taiwan and the chip sector
(01:20:05) The AI arms race
(01:23:22) AI Governance
(01:26:28) AI Safety
(01:29:22) Custom Models
(01:31:33) Closing
(01:32:23) Outro
---

# Zooming Out on AI, from the Nick Halaris Show
**Cognitive Revolution:** [July 27, 2024](https://www.youtube.com/watch?v=eMD88uGAzKM)
*  Hello and welcome to the Cognitive Revolution, where we interview visionary researchers,
*  entrepreneurs, and builders working on the frontier of artificial intelligence.
*  Each week we'll explore their revolutionary ideas and together we'll build a picture of
*  how AI technology will transform work, life, and society in the coming years.
*  I'm Nathan Labenz, joined by my co-host Eric Torenberg.
*  This episode is brought to you by Work OS. If you're building a B2B SaaS application,
*  at some point your customers will start asking for enterprise features like SAML authentication,
*  SCIM provisioning, role-based access control, and audit trails. That's where Work OS comes in,
*  with easy to use and flexible APIs that help you ship enterprise features on day one without
*  slowing down your core product development. Today, some of the hottest startups in the
*  world are already powered by Work OS, including ones you probably know like Proplexity,
*  Vercell, Jasper, and Webflow. Work OS also provides a generous free tier of up to 1 million
*  monthly active users for user management, making it the perfect authentication and
*  authorization solution for growing companies. It comes standard with rich features like bot
*  protection, MFA, roles and permissions, and more. If you're currently looking to build SSO for your
*  first enterprise customer, you should consider using Work OS. Integrate in minutes and start
*  shipping enterprise plans today.
*  Hello and welcome back to the Cognitive Revolution. This is AI Nathan, powered by 11 Labs,
*  filling in for the real Nathan who is still in beautiful Brazil to speak about AI automation
*  at the Adapta Summit. We'll have more on that here on the feed soon, but for today we're excited to
*  share an episode of the Nick Hilaris Show, where I am the guest. Nick and I, both alumni of Chippewa
*  Valley High School in Michigan, connected through our former teachers Mrs. Voss and Ms. Kohut,
*  who were big influences on each of us. This episode offers a big picture view of the AI
*  landscape, balancing my sincere enthusiasm for the practical value of AI with honest analysis
*  of just how uncertain the path forward really is. We start with my journey into AI, from long-standing
*  philosophical interests to founding Waymark and ultimately to this podcast. Key topics include
*  AI's transformative potential in high-value sectors including medicine, law, and self-driving.
*  The promise of abundance and liberation from mundane tasks, like AI automating food packaging.
*  Concerns about AI safety and control, including the challenges of aligning AI goals with human
*  values, geopolitical implications, especially US-China dynamics in AI development and chip
*  production. The potential need for a new social contract. Paths for responsible AI development,
*  such as focusing on making current AI more useful rather than just more powerful overall,
*  I advocate for swift adoption of beneficial AI while urging caution and pushing towards
*  superintelligence. There's no consensus on many critical questions in AI, and this conversation
*  reflects that reality. As always, but even more so for this episode, I want to invite your feedback.
*  I take the responsibility of communicating the state of AI to people who may not have been paying
*  close attention very seriously, and I want to be as accurate as possible. If you think I'm getting
*  anything wrong or missing anything important, please reach out and let me know. If on the other
*  hand, you do find this an accurate and useful overview, we'd of course appreciate it if you'd
*  take a moment to share it with friends. Now, I hope you enjoy this conversation about the rapidly
*  changing AI landscape with Nick Helaris from the Nick Helaris Show. Hi everyone, and welcome back
*  to the Nick Helaris Show. Our guest this week is Nathan Labenz. Nathan is the founder of Waymark
*  and the host of the popular Cognitive Revolution podcast and the world's most prominent AI scout.
*  Nathan, welcome to the show. Thank you. Excited to be here. Looking forward to this.
*  Before we get into it, we got to talk about our connection because you are the first person on
*  the podcast that actually went to the same high school as me, and we owe thanks to Mrs. Voss and
*  Mrs. Kohut, two of the best teachers at Chippewa Valley in Chippewa Valley history for kind of
*  making this connection. But it's good to have a fellow Big Red on the program. We still use
*  that nickname in 2024. I don't know if they retired that one or not, but yeah, our AP history and AP
*  English teachers respectively, definitely big influences on me and I was excited to get an
*  intro from them. Yeah, likewise. I mean, they definitely stand out as we talked, you know,
*  when we first met those two teachers stand out from the days at Chippewa Valley. They're excellent.
*  They weren't the only excellent teachers, but they were two of the best and I've kept in touch with
*  both of them over the years and sounds like you have as well. So that's cool. Yeah, definitely.
*  Did they retire the Big Red name? There's been talk about it repeatedly. And I think the last time
*  it's been a couple of years now that was the last time I went out to a football game. I believe it
*  was still unchanged, but one has to imagine it can't last forever. Yeah, it's that entire
*  school district. My middle school was Algonquin and my elementary school was Erie. So like the entire
*  district is based off of the name. Yeah, Miss Huron and Wyandotte. So yeah, those were a little,
*  you know, I mean, we're way off the topic, but I feel like those are somehow more respectful in as
*  much as they're like proper names. And the Big Reds obviously is not how folks call themselves.
*  So yeah, that's true. Big Red is closer to the Washington Redskins, which obviously they
*  opted to change their name as a result. So interesting. I hadn't thought about that when
*  I brought up the Big Reds, but I'm glad you're here. There's a lot of questions, so many things
*  I want to ask you just because AI is like the number one topic in the news and you have been
*  all over it just in your business and your podcast. And I thought a good place to start is
*  like, how did you get into or when did you get into AI, interested in AI and how did it become
*  such a huge focus of your life? Yeah, there's kind of two chapters to that. There's like the
*  prehistory and then the recent history. The prehistory is that, and this is pretty common
*  actually among people that are interested in AI and particularly those that are interested with a
*  sort of eye toward how big of a deal is this going to be and might it be the kind of thing
*  that really could get out of control and be like a threat to civilization or humanity as a whole,
*  is that I came across the writing of one Eliezer Yudkowsky online, 2006, 2007 range was when I
*  first encountered it. He is pretty famous at this point for being one of the earliest
*  prophets of AI doom, if you will. He was writing about this before almost anyone else was thinking
*  about it and saying, Hey, we're on track here with the growth in computing power and the growth in
*  these data sets. Like at some point in the future, we're going to figure out powerful AI. But the
*  problem is we don't know how to control it. And we're going to have a really hard time communicating
*  our values to it. And the history of nature and even just the history of humanity is like a lot
*  of extinction events. Could this be the next one for us? And he's unpacked that of course,
*  in literally like millions of words of writing. So I read about that way back then I thought,
*  boy, this is really interesting. And I filed it for myself, basically in the similar place as like
*  asteroids hitting the earth from outer space. It was the sort of thing where I thought this seems
*  like it would be a really big deal if it were to happen. Obviously, an asteroid took out the
*  dinosaurs. I wouldn't want the same to happen to us. And yeah, it might be super unlikely,
*  but it does seem like it's worth having somebody scanning the skies to try to identify any
*  asteroids that might be headed our way. And if there were one, we'd want to get the biggest
*  jump on it that we could. And we presumably mobilize all of humanity to try to deflect
*  that asteroid if one was really coming for us. And indeed, we do actually have programs like that
*  where people are using telescopes and scanning the skies and trying to identify those advanced
*  threats. So I kind of said, it seems like similar. It doesn't seem very likely, but if it does happen,
*  it seems like it could be a big deal. And so I essentially just supported people who were
*  doing this sort of speculative work with small charitable donations and just also goodwill,
*  just the idea that this seems like the kind of thing that somebody should be taking seriously.
*  I personally, though, didn't feel like I had the right skill set for the kind of work that
*  people were doing at the time, which was very mathematical and very theoretical. And so I spent
*  the last 15 years of my from that was basically at the beginning, very beginning of my career until
*  present, basically did entrepreneurship the entire time. And where those threads merged was in
*  roughly 2020, 2021, with the rise of the generative AI moment. My company Waymark is in the video
*  creation space for small business. And at the time, we described ourselves as a DIY video creation
*  platform with the idea being small businesses need video content for all sorts of reasons,
*  mostly marketing and advertising, but they have a hard time creating it. The video creation tools
*  are super complicated. You need like years of experience to master Adobe suite of tools.
*  We tried to make something easy, make it accessible in the browser, make it something anyone can do,
*  yada, yada, yada. We did a pretty good job with that, if I do say so myself, but we hit a bit of
*  a wall at some point where when we were talking to customers, we would say things to them,
*  is there anything we could do to make this DIY video platform easier for you to use? So you'd
*  use it more. And a lot of times they would start to say, nah, I don't really have that much to say,
*  but it is easy to use. You've made it pretty easy, but I just don't really have any more ideas
*  for videos. Or I still like the hard part is actually coming up with what I want to say in
*  the first place, not so much using the tool. And so we realized, man, that's a pretty profound
*  problem that there aren't really any good traditional software solutions for.
*  And it just so happened that right at the same time, GPT, I was following from GPT 2,
*  but with GPT 3, it was like, whoa, this thing could really change the way we present our product to
*  customers. Because if an AI can write a first draft for you, then that can be a totally different
*  experience. Now you're not having to sit down in front of the blank page and say, what do I want
*  to say today? But AI can spit out a bunch of ideas. And I always remember this episode from
*  The Simpsons where Mr. Burns goes to an art gallery opening and sees this art to debut.
*  And he says, I'm no art critic, but I know what I hate. And I felt like that was the
*  state of the early AIs. And our customers were in that Mr. Burns zone where they're not critics,
*  they're not prolific in content creation. But if we could put some AI stuff in front of them,
*  they could say, no, hate it, and just rifle through stuff until they got something that was
*  good enough that they could latch onto and then actually work with and take forward from there.
*  So I got religion around that real quick for our company. I just knew that to get over this barrier,
*  we needed something qualitatively different. And obviously, generative AI is qualitatively
*  different. And so I poured myself into it and yanked the company in that direction,
*  said, we're going to do basically nothing else until we figure out how to take advantage of this
*  technology. And then I got really obsessed with understanding it, understanding how to make the
*  best use of it. And it really did start with that kind of commercial motivation of just, I want to
*  make the best product I can with this. But it's such weird technology that to do that, I felt like
*  I needed to understand it better. And then as I got deeper into it, one of the big realizations
*  was that it wasn't just the writing that was happening, but it was also computer vision was
*  happening. And that was really relevant to us also, because our users, our small business users,
*  they typically have a bunch of photos of their business. And yet, those sitting in a big folder
*  is only so useful, right? You have the same kind of problem. I don't really want to look through
*  there and pick the right photos. But if AI can understand the photos and make good selections
*  for them, now we're in a totally different regime in terms of how easy the product is to use.
*  So that was really interesting. That was advancing really quickly at the same time.
*  And then also text to speech. We had a voiceover service that we offered in the past,
*  staffed by professional voiceover talent, really good quality, but took days to turn around,
*  cost 100 bucks. If something wasn't right, there'd be another cycle. You don't have to
*  send feedback and the person do it again. And that will also cost more money. So it was good,
*  but had some friction. Text to speech was also getting really good at the same time.
*  And really a fundamental kind of realization, which is not unique to me,
*  but was a big one for me to wrap my head around was the same core AI techniques were driving
*  all of those improvements in parallel at the same time. Basically the transformer,
*  which people probably heard of at this point, was being adapted to all these different use cases
*  and was creating radically new and improved results across writing and computer vision
*  and text to speech and a bunch of other stuff, by the way, as well. But those are the most
*  relevant ones for me. And I was like, man, if this single AI architecture with basically the same core
*  technique and strategy can do all these things, then it's only a matter of time before it's going
*  to be doing even more things. And before they're all going to be merged into a single thing.
*  And if you have a single thing that can write and understand the world and speak and handle audio,
*  and now as we've gone forward a few years in time, can generate music, can generate incredible
*  visual art, can understand video as well, can have real-time conversation with you.
*  Now we're getting to something that is starting to look really powerful. And of course, that then
*  called back to mind the LAS writing from years ago, like how powerful is this going to get?
*  How quickly is it going to get that powerful? And do we have effective means to control it
*  and make it work for us? Or might we be inventing a rival to ourselves that potentially could get
*  more powerful than us and potentially could get out of control? So that kind of brings us basically
*  to the recent present. I was fortunate that I had a great teammate, longtime teammate who had been
*  our COO and was the perfect person to take over as CEO. And so I was like, you know what? I actually
*  want to make that switch. I want to get out of managing the company day to day and just go
*  full-time studying, trying to make sense of what's going on in AI.
*  And if you're up for it, you can run the company. And that's actually been a great trade. He's done
*  a phenomenal job. The company has grown. The generative AI moment has treated our company
*  really well. And I'm still contributing there, but also just trying to make sense of the big
*  picture. And obviously there's a lot going on. Absolutely. Yeah. I want to get more into the big
*  picture, but before we, I want to close the loop on Weimark. So what kind of improvement did you
*  guys experience as a result of all this technology that you just mentioned? I don't know what the
*  right metric is, but did the business grow significantly once you started implementing
*  these tools? What happened? Yeah. Business growth wise, it's been really good for us. We basically
*  doubled the business in 2023 while breaking even. We have raised venture capital in the past, but
*  not recently. And so to double a business without burning money is definitely a very good trajectory
*  and definitely much better than the trajectory we were on before. So the results in terms of just
*  pure financial bottom line stuff have been really good. And then qualitatively on the product,
*  it's basically night and day. In the past, you would, we had a big template library. You would
*  browse through the template library, preview them, find something you think, oh, that kind of looks
*  good. I might want to do that. And then you would be faced with the writing challenge. What do I want
*  to say? And then how do I map that onto this particular template? And then I got to choose
*  all my imagery to match up with that. And then once I'm done with all that, now I can request a
*  voiceover job and then I'll get that back in maybe two days. And then I can listen to that. And then
*  if that's all good, then I can download it and I can actually go use it. That and that writing and
*  image selection part, as much as we made it really easy, people would still often find it would take
*  an hour. And an hour was really good to create a high quality video as of a couple of years ago,
*  because what would the alternative be? Hire an agency or the other options were more time consuming,
*  but an hour is still a lot. Today, if you go to waymark.com slash AI, you can provide your business
*  URL, which is like your homepage. We will go grab the information off of your homepage and kind of
*  spite around your website to figure out what your business is all about. Pull in all the imagery
*  that you have there. And then we just give you a single text box. People have seen this kind of
*  thing in other AI products. We basically say, what do you want? Or do you have a new location opening?
*  Do you have a sale coming up? Do you want to describe a product? You just want to introduce
*  yourself, whatever. You can type that in in 10, 15, 20 words, hit go, and it takes 30 seconds
*  to get a fully formed 30 second commercial back. That's a full script. All the imagery is selected
*  for you. The voiceover is generated and added in and it's all integrated. And then you can just sit
*  back and watch it. So you're literally watching a fully formed production for your business in 30
*  seconds. You still have that Mr. Burns opportunity where you can be like, I don't like that. Just
*  redo it or I'll give you another set of instructions and you can try again.
*  Or if you do like it, you also still do have all the detailed editing controls.
*  And almost everybody makes at least some low level edit after they get the AI first draft. But it is a
*  totally different and much more surprising and delightful experience. In the past, there was
*  never that moment of reveal where you would get something that might be, it might not be awesome,
*  it might be awesome, but you could watch it and find out you were the one creating. Now you get
*  this moment where it's like, what's in the box? And you can open as many boxes as you want. And
*  when you find something that you're intrigued by or excited by, then you carry on from there.
*  Basically on every metric from the speed to create, the feedback scores that we get, the number of
*  videos that people do create, the number of friends that they share it with that come and use it. And
*  ultimately the revenue has all just been tremendously improved by a thoughtful application of this
*  technology. That's awesome. I'm happy to hear that the company is thriving and I'm gonna have
*  to check it out. I'm gonna throw a couple of my own websites through it and see what happens.
*  Definitely do. It's cool. It's a genuinely good experience. I can say that with not just
*  entrepreneurs, salesmanship, but it is a good application of generative AI that brings multiple
*  different modalities together into a single thing that actually most of the time, we still have our
*  misses, but most of the time it delivers really good results. Hey, we'll continue our interview
*  in a moment after a word from our sponsors. AI might be the most important new computer
*  technology ever. It's storming every industry and literally billions of dollars are being invested.
*  So buckle up. The problem is that AI needs a lot of speed and processing power. So how do you compete
*  without costs spiraling out of control? It's time to upgrade to the next generation of the cloud,
*  Oracle Cloud Infrastructure or OCI. OCI is a single platform for your infrastructure, database,
*  application development, and AI needs. OCI has four to eight times the bandwidth of other clouds,
*  offers one consistent price instead of variable regional pricing, and of course, nobody does data
*  better than Oracle. So now you can train your AI models at twice the speed and less than half the
*  cost of other clouds. If you want to do more and spend less like Uber, 8x8, and Databricks Mosaic,
*  take a free test drive of OCI at oracle.com slash cognitive. That's oracle.com slash cognitive,
*  oracle.com slash cognitive. This episode of the cognitive revolution is sponsored by the Brave
*  search API. You may know of Brave as an alternative to Chrome, but did you know that Brave has its own
*  independent search engine powered by its own 20 billion page index of the web? The Brave search
*  API gives developers reliable and affordable access to programmable web search, auto suggest,
*  spell check, and more with flexible plans for all types of use cases from rag search to automated
*  business intelligence. On top of that, it's up to three times cheaper than Bing, all without
*  compromising on quality, speed, or reliability. Over 700 businesses, including Coheer, Chegg,
*  and Kagi rely on the Brave search API. And a recent survey showed that 94% of customers
*  would recommend it to their peers. To start building apps with the power of the web,
*  sign up at brave.com slash API and get up to 5,000 free monthly calls.
*  Let's switch gears now and talk about the elephant in the room question. I feel like
*  you can't really bring up the subject of AI without kind of talking about what got you
*  interested back in 06, which is like, what are the implications? But rather than talk about what
*  could go wrong, I wanted to ask you the other side of that question first, which is what could
*  go right if you put away the pessimistic view of AI and just think about what are the positive
*  potentials? What comes to mind for you after researching in this for four years like you have
*  doing this massive deep dive? Yeah, I could go on about this for a long time, honestly. I think
*  that the upside is really incredible. In some ways, hard to imagine and you almost have to take
*  it like sector by sector because there really is application to everything. But the way Mark
*  experience before and after is a decent guide, I would say to everything in life. So I often talk
*  about medicine. Obviously, in today's world, the US healthcare system has incredible technology and
*  incredible doctors that can do amazing things. But the day to day experience of it is pretty
*  crappy. It's like extremely complicated. You got to make the appointment, you got to go,
*  you got to wait. I went to urgent care with my kids this weekend. We were there for four hours.
*  And it's so it's not awesome and access not as broadly distributed and cost is a huge factor.
*  So obviously, I think whatever I can go on about the problems, but the upside is AI doctor. And
*  already today, we have AI systems that are outperforming human doctors as evaluated by
*  human doctors on a number of really important kind of down the fairway medical tasks that includes
*  differential diagnosis via chat. So for example, to envision that you the way they set up these
*  experiments and evaluate, you are a user you chat into either a human doctor on the other end or an
*  AI doctor on the other end. They don't tell you which one you're engaged with, but you just
*  have your conversation. And then it's up to the doctors AI or human to figure out what your
*  condition is. And then they have human doctors evaluate and compare who's doing better. And
*  again, this is blind evaluation. The AI doctors are outperforming human doctors on these core tasks
*  by a not insignificant margin already. That doesn't mean they can do everything that a human
*  doctor can do. They still struggle with the sort of long trajectory of your life. At this point,
*  that's a problem people are definitely working on and making good progress on. But at least in these
*  sort of narrow episodic bounded tasks, the AIs are already outperforming your average human doctor,
*  and they're doing it with a cost of less than 1%. You know, if it costs you $100 to go doctor,
*  it probably cost you 10 cents to talk to the AI. So literally 0.1% cost. Of course, they're always
*  available. So it's a 24 seven situation. You can always come back to that conversation later,
*  right? If you drop off and get interrupted or whatever, or just have another thought later,
*  you can always just return to it and ask again. So the sort of pickup where you left off was amazing.
*  We're adding modalities to this stuff all the time. So when you hear modalities in AI, that's just
*  like text is a modality, images and modality, audio is a modality. So they're starting to get
*  more integrated. Things like reading x-rays or reading scans are probably not as, I think it's
*  a little just a little less clear how quite how they compare to the human radiologist or whatever
*  that would be reading your information. But it's like getting competitive. I would say it's probably
*  not quite better yet, but closing in. And then there's also just the research side. I just did
*  an episode of my podcast not long ago on the models and people probably have heard of like
*  Alpha Fold. Now we're on Alpha Fold 3. And what Alpha Fold, the family of models allows you to do
*  is understand the structure of proteins, which previously was really hard to figure out and
*  proteins, all the little mini machines in our bodies, which are largely proteins and RNA
*  molecules that have these sort of weird three-dimensional shapes and have these
*  weird interactions and all these interactions add up to life. But when something goes wrong,
*  then people get sick. And there's been this incredible challenge for a long time to try to
*  understand what is going wrong. A lot of times what's going wrong is like something is not
*  shaped the right way. And so it doesn't fit with the other pieces that it's supposed to fit with.
*  And so then there's some cascade of disruption that causes illness. But we couldn't even tell
*  without huge amounts of work, what is the shape of a protein until this Alpha Fold series of
*  models and other people. Alpha Fold is the most famous one that comes out of Google DeepMind,
*  but there's lots of other work in this area too. Now you can take a sequence, which we've been able
*  to read the DNA really well for a long time. Now you can take a sequence of DNA and say,
*  what shape of protein is this going to be? And you get pretty accurate predictions out.
*  And this is going to start to illuminate all sorts of how these things interact,
*  what is causing what, all the complexity of these interactions is still definitely something that
*  is going to take time to tackle. But it's a totally new class of tools that is going to
*  dramatically accelerate discovery in biomedicine. So that's just in medicine. And then you could go
*  in law, right? People don't have great access to legal counsel, you're guaranteed right to
*  representation, but is that representation going to be good? I would say already at this point,
*  that if you're guaranteed an attorney, you probably should also be guaranteed access to GPT-4.
*  And this is also my recommendation at present is use both. I always say if I was
*  genuinely in a health emergency, I would not put all my eggs in the AI basket, but I also wouldn't
*  be without my AI doctor. And I would definitely be fact checking my human doctor against my AI and
*  vice versa and trying to get the best of both worlds. Same thing for legal representation,
*  I would be double checking. Anytime I have to sign a contract these days, I take it to a couple
*  different AIs and say, I'm about to sign this contract. What are the most concerning things
*  that you see in this contract that I should be thinking about? If I send it to three different
*  AIs, and typically that would be open AIs, chat GPT, Clawed by Anthropic, and Gemini from Google,
*  those are your top three. If I give the same contract to all three and ask that same question
*  and I don't get anything back that's really concerning, I'm like, okay, I'm good to sign.
*  Tons of application in basically access to all the professional services.
*  Driving is coming. The latest Tesla full self-driving is getting really good.
*  The prospect for robotics, I've got an episode coming with a company that is doing robotic
*  food preparation. And apparently 70% of the cost, which I was very surprised to learn,
*  but 70% of the labor cost, not including the food cost, but 70% of the labor cost
*  when you're manufacturing food is plating the food.
*  Preparing the ingredients and cooking is only 30%. 70% is like putting it into the packaging.
*  This is what this company is focused on, taking the food and putting it into packaging.
*  It's a hard problem because all the, he said, broccoli, right? All the pieces are different
*  sizes. You've got to get the right amount of weight. You don't want to be underweight,
*  but you don't want to be too much overweight because that's waste.
*  And they've created a robot that can do this work. So now they've got, I think 20 million meals that
*  they've had their robot actually plate and put into packaging. So I think the big picture is just
*  abundance, freedom from drudgery, very broad access to expertise. In economic terms, I often
*  say huge consumer surplus. Stuff that we pay a certain amount for today is going to be available
*  at under 1% the cost on demand via your phone or your device. Energy wise, this will also be
*  in terms of climate change. There's a lot of focus that goes into, oh, these AIs are very
*  energy hungry. Personally, I think that's quite overblown because the offsetting factor is usually
*  not considered. If I save one trip to the doctor, the amount of gas that I would have burned to make
*  that trip covers a whole lot of chat with the AI. So I also do think we're probably going to see
*  significant improvement to climate type concerns. Google just put out a thing the other day where
*  it's like a shipping API. And you're like, man, shipping, it's a big business, right?
*  Everything moves on ships. But you would think, man, is that a Google project? It is. They said
*  they can double with using their AI. You can double the profitability of your shipping business.
*  You can deliver more packages or more tonnage, more containers with 15% fewer ships. And so it's,
*  wow, that's incredible. And obviously a lot of energy gets saved when you do that sort of thing
*  as well. So this is just like what's foreseeable now. I think it could get even crazier if the AIs
*  start to do science. Where we're at right now is we have these generalist systems like your chat
*  GPTs that are pretty good at everything. They do make some weird mistakes. They do make some stuff
*  up sometimes. So they have their idiosyncratic weaknesses. And it is important to understand
*  them. But they're pretty good at everything. But they're not Eureka good at really anything.
*  And then we have these very narrow systems like your Alpha Folds and your Google shipping
*  AIs that are superhuman but in a very narrow domain. And those things haven't really been
*  integrated yet where the generalist AI can use the superhuman or can design its own superhuman
*  narrow AI tool. If we start to see that loop get closed, then all bets are off. But that also,
*  to some extent, at least foreshadows or calls to mind the other side of the coin. All bets are off
*  possibly in a good way. But also, if you have AIs that are advancing science and answering
*  previously unanswered questions and running highly autonomously and maybe doing things that
*  we're struggling to keep up with or struggling to understand, then that may be amazing forever.
*  But it also definitely creates some risk of broadly speaking things getting out of control.
*  But I am very enthusiastic about the upside. I often describe myself as an adoption accelerationist
*  and hyperscaling poser. And that's very in the weeds jargon. But basically, I want to see us take
*  advantage of all this great stuff that AI has to offer. I want my self-driving car. I want my AI
*  doctor. At the same time, I do think we should increasingly start to exercise real caution in
*  just how fast are we going to continue to push the scale up and up to create more and more powerful
*  systems? Because we don't have that much farther to go before they are genuinely going to be more
*  powerful than we are. We're not going to change that fast. They are changing quite fast.
*  Hey, we'll continue our interview in a moment after a word from our sponsors.
*  Omnike uses generative AI to enable you to launch hundreds of thousands of ad iterations that
*  actually work customized across all platforms with a click of a button. I believe in Omnike
*  so much that I invested in it, and I recommend you use it too. Use Cogrev to get a 10% discount.
*  Hey all, Eric Torenberg here. I'm hearing more and more that founders want to get profitable
*  and do more with less, especially with engineering. Listen, I love your 30-year-old ex-Fang senior
*  software engineer as much as the next guy, but honestly, I can't afford them anymore. Founders
*  everywhere are trying to turn to global talent. But boy, is it a hassle to do at scale from sourcing
*  to interviewing to on the ground operations and management. That's why I teamed up with Sean
*  Lennahan, who's been building engineering teams in Vietnam at a very high level for over five years
*  to help you access global engineering without the headache. Squad, Sean's new company, takes care of
*  sourcing, legal compliance, and local HR for global talent so you don't have to. With teams across Asia
*  and South America, we can cover you no matter which time zone you operate in. Their engineers
*  follow your process and use your tools. They work with React, Next.js, or your favorite front-end
*  frameworks. And on the backend, they're experts at Node, Python, Java, and anything under the sun.
*  Full disclosure, it's going to cost more than the random person you found on Upwork that's doing two
*  hours of work per week but billing you for 40. But you'll get premium quality at a fraction of the
*  typical cost. Our engineers are vetted top 1% talent and actually working hard for you every day.
*  Increase your velocity without amping up burn. Head to choose squad.com and mention Turpentine
*  to skip the wait list.
*  That vision sounds exciting because we live in a world where there's like mass inequality. And here
*  in America, like we're very rich compared to the rest of the world. And I think Americans forget
*  about that when they compare themselves. But the world that you're describing sounds like we could
*  get to, we'd have this massive deflation, like all the inflationary inflationary inflationary
*  pressure that is causing problems in our political system could be taken care of by this
*  massive deflationary trend in every product that you could imagine. It sounds like even food.
*  I was thinking there would be a limit to it. But then it's what you mentioned about the labor
*  costs, like labor is a huge part. And I guess the only question I have about the positive side is,
*  what happens to all these people who are working in the industry? What happens to all these people
*  who are doing those jobs?
*  Do you think we need a new social contract for the AI era? And yeah, I think I'm glad you asked
*  that question because I think that is among even among the people that are very bullish on AI.
*  I think it's an underdeveloped under theorized idea. The sort of standard answer is like,
*  I'm very privileged to do work that I genuinely enjoy. And if I didn't need to earn any money,
*  and if nobody even if nobody was willing to pay me anything, I would probably still spend
*  a good amount of my time studying AI because I'm just genuinely fascinated by it. But
*  that's not really the case for people who are scooping food into trays in a rate of 20
*  scoops per minute. It's a scoop every three seconds. Often, I just learned this from this
*  last episode. I'm not like an expert in this, but often that work is done in cold rooms.
*  So it's 30 some degrees. It's not super pleasant. So I would venture that the vast majority of people
*  doing that kind of work in today's world. If you said, hey, you can have your needs met,
*  and you don't have to do that anymore. Would you take that trade? I think most people would do it.
*  I'm not one who's too worried about Oh, their meaning is wrapped up in this. That might be true
*  for me to a degree. If I was deprived of being able to study AI, I would feel some loss. I don't
*  think people will be like, Oh, man, I just long for the days when I was in that 35 degree room
*  scooping food into trays. At every three second pace. I think people will honestly find better
*  things to do with their time, but we do need a new contract. And right now, we don't have a great
*  idea about that. Most of the answer that you get when you talk to the technologists is we're probably
*  going to need universal basic income. And okay, I think it's probably time to get to work on that.
*  Sam Altman from open AI to his credit has been funding. And not a lot has been written about
*  this, but he has been personally funding universal basic income experiments for years now.
*  So he's definitely somebody who has kind of believed in the power of AI and how far it could
*  potentially go. And it's at least been trying to do things to get society ready for it. But
*  that's, I think, definitely not nearly as much in that direction as we may soon need.
*  Yeah. And it's almost like it maybe it's a little early because what we learned during the COVID era
*  is that this like deficit funded transfer payments, like all of the CARES Act money,
*  they actually are inflationary. But if AI was producing this 99.99% deflation,
*  you could probably do UBI and not have inflation. Right now, if you did UBI on scale, you'd have a
*  major problem, even more than we saw during the COVID era. But there probably is a moment in time
*  where you could pull it off, but it might not be just yet.
*  Yeah, I would say it's going to be a tricky thing to navigate. I think we've got multiple
*  tight ropes to walk on a couple different dimensions. And this is probably one of them.
*  We're definitely not at a point yet where everybody can quit their jobs. And I should caveat
*  everything I say with like, there's always the possibility that progress really stalls out.
*  This is probably the biggest picture question in AI right now. We've seen 10 to 12 years now of
*  the same basic paradigm, just scaling up and giving us more and more at every level of
*  increased investment. The inputs to AI are data, compute, and algorithms. You need data to learn
*  from, you need compute to crunch the numbers, and you need algorithms to actually make it work.
*  What has been scaled up is data and compute over the last 12 years, with the algorithms
*  constantly getting better as well and getting being more efficient in terms of converting
*  data and compute into capabilities. So we're 12-ish years into that paradigm. It doesn't
*  show any sign of slowing down yet. There's some chance that there's some law of physics or some
*  weirdness that isn't well understood that could pose a hard barrier. Most people, I think,
*  that are really in AI do not really expect that, although we don't have a scientific law that says
*  that doesn't exist either. So we're definitely flying a bit blind. But if it does continue,
*  then it won't be that many more generations before we're in a very different regime. Because
*  right now, we're in the zone where, hey, I can ask ChachiBT to write me a little script of code.
*  And oftentimes, it can do it right away. But it can't do a huge project. It can't take over the
*  job of a full software engineer because it can't plan on long enough time horizons. It's not really
*  that it's not smart enough. It is comparably smart, but it lacks the long time horizon planning. It
*  lacks the contextual awareness. And it definitely could stand to be smarter too. But those problems
*  are seemingly on track to being solved unless some barrier that isn't very conceptually obvious
*  were to emerge. Anyway, this is all just a caveat of there's some chance that we look back at me
*  in this moment and say, boy, that guy was really high on his AI supply and it's leveled off.
*  I personally don't think that's very likely. If you were to say percentage wise, I couldn't put
*  it less than 10%. I'm not that confident all this will happen. But it does seem like more
*  likely than not that it will happen. And if it does happen, it's probably going to happen over the
*  next few cycles because GPT-2 was not really coherent, couldn't really do much of anything,
*  but could sometimes create language that was uncanny valley, passable. You might be tricked
*  every once in a while into thinking that actually made sense. GPT-3 was good enough to write video
*  scripts for Weimark. GPT-4 can pass the bar exam. We've now got stuff that can pass medical licensing
*  exams and outperform doctors on diagnosis. What's next? There's not that much more room to go
*  before we start to really enter a different regime. It's all coming at us extremely quickly.
*  That's why I think of it as a tightrope because five years from now, the world could be extremely
*  different. We need to start to prepare for that and figure out how to navigate that transition.
*  But at the same time, it is true that we're not yet at the point where everybody can
*  quit their jobs today. This is a tough one for society. In the past, these things have taken
*  generations to unfold. The Industrial Revolution took, depending on exactly what you want to count,
*  multiple generations. The electrification of America took 60 years from the time that
*  medicine invented the light bulb to the time that my grandmother in rural Kentucky got electricity.
*  So people went through whole careers and they could see that change was coming and it was like,
*  okay, fine. But for me, for my career, I can finish out being a blacksmith and then I'll
*  retire and my kid will do something different maybe. My kid can't fall in my shoes and that
*  in and of itself can be disruptive. But now we're in a regime potentially at least, or I would say
*  likely, where within careers, you're going to have this disruption where it's, I was a,
*  we are seeing this already. I was a copywriter. Copywriting is not the thing it was. I was a
*  voiceover artist. We've seen the, we still do offer the professional voiceover service,
*  but the volume of it has dropped tremendously. I'm a visual artist. Again, people are making
*  a lot of visual art on their own, even music. Now you go to Tuno or UDO and these things can make
*  full songs and they're getting into the level where it's, I actually like that on its own merits.
*  They're starting to be genuinely competitive. So yeah, in a sub decade timeframe to see all
*  this kind of stuff come on, how are we going to adapt to it? What's the new social contract?
*  We're really going to have to thread the needle to make that transition. I don't think we can,
*  to think that we could make it smooth is probably honestly not in the cards. It's going to be choppy,
*  but to hopefully at least manage it well enough to come out the other end without like total upheaval.
*  Even that I think is going to be quite hard. I think so too, because it's potentially so
*  transformative to what the economy needs. If you don't need all this labor, it's a real problem
*  for the entire system. Actually, after the first time we talked several months ago, I was blown
*  away because I had not really been paying attention to AI that much. I've obviously followed it, but
*  I had never heard such a optimistic sort of story that you shared it back then. I was trying to
*  think about what does the world look like if everything is free? It's not going to be free,
*  but it's essentially compared to what it costs today, it's essentially going to be free
*  if the AI, if the optimistic AI story comes together. To take it full circle, Mrs. Voss
*  will be happy. The only thing I could think of is to look at history. This is a bad analogy,
*  but I think it's worth considering, which is maybe what human beings will be doing are what the
*  non-slaves were doing in the slave-based ancient societies, ancient Rome or ancient Greece,
*  where the elites or the citizens of these city-states, they didn't really have to do
*  anything that we do, like modern people have to produce economic output to survive. They were
*  relying on their slaves that they took from other countries and whatnot. What they did was they
*  engaged in art, they worked out, they fought a bunch of wars and engaged in politics. Maybe
*  that's just what human beings are going to do in a world where they don't have to spend 40 or 60
*  hours driving to and from work, doing work. I'm not sure. What do you think about that?
*  Yeah, I don't know. I'm optimistic about that in as much as, I mean, there's a lot of concern about,
*  oh, meaning is attached to work and whatever. I'm optimistic we'll find good things to do.
*  Making art for art's sake, I'm terrible at playing the piano, but I do enjoy it.
*  It's very much for its own sake. I'm definitely not good enough to perform in front of others
*  or for anybody to care what I'm playing on the piano, but I do still find it in a purely
*  experiential way enjoyable. I'm learning. It sounds at least okay enough sometimes,
*  and I enjoy the challenge of it. I would like to do more of it if I had more time available.
*  I do think that most people have things like that. I think there's also really interesting
*  questions about the slaves in this analogy are the AIs and are they going to start to matter in
*  a moral sense? That's another question that is dramatically under theorized. We don't really
*  have a great track record for how we treat the producers of the subservient producers of society,
*  whether they're human slaves or animals or potentially in the future AIs. I think right
*  now people are very dismissive of the idea that the AIs could be conscious or could matter in
*  some moral sense. I tend to share that view. I don't like wake nights worrying about the
*  experience of AIs because my best guess is they probably don't have any. But at the same time,
*  we don't know where our own consciousness comes from. I remember as a kid being told that animals
*  were not conscious or didn't feel pain, people have often said babies don't feel pain. I don't
*  think any of that's true. I would at least want us to be mindful of the AI part of that equation
*  could be at some point in the future. There's also the wars part of it isn't super encouraging
*  either. Hopefully, we will not be fighting wars with each other for lack of anything better to do.
*  I am optimistic about that. I think in a world where we have abundance and where medical
*  breakthroughs are happening and we're potentially living longer and healthier, I would hope that we
*  would be able to avoid war for entertainment's sake. I think we're better than that. I'm not
*  an extreme optimist on human nature. But I think if all those good things come to pass,
*  my best guess is we'll find at least decent ways to use the time. We might end up spending a lot
*  of time in VR. I definitely think VR has not really taken off, obviously. I think the biggest
*  problem, and I do have an Oculus headset, but I don't use it very much. Mostly because there's
*  not much great content in there. I do think AI-generated VR environments is one way that
*  VR could take off because there could just be lots more to explore. So I wouldn't be shocked
*  if we do end up in a significant... If headsets on is the new head in the phone, that's one
*  possibility. And it could be quite fun. People love their video games. People find these things
*  very immersive. I'm a rare person who aspires to play more video games than I do. I find most
*  people either don't play any and are happy with it or play too much and feel like they should cut
*  back. I dabble occasionally and feel like, man, I wish I could get into this a little bit more.
*  In the future, maybe there's VR worlds to explore as well. And obviously there's space too. There's
*  the idea of colonizing space. And I don't think that's out of the question. There are definitely
*  some major challenges in terms of getting our biology to survive in space in any way that we
*  would find pleasant. And it certainly might make sense that we end up sending robots out into space
*  instead or in advance of us. But yeah, there's lots of stuff still that I think we'll be able to
*  turn our attention to, assuming we can get all the preconditions and a new social contract worked out.
*  Totally. Yeah, I think so too. I feel like the adjust for revolution created a lie. Not
*  definitely created a lie, which is that the purpose of life is to be economically productive.
*  And so we organize our whole society around that. Even the school system is essentially
*  built around that. And I see it in all generations of people that I engage with.
*  They are prioritizing things beyond economic life. I still think that's the dominant pursuit.
*  Basically, everyone is trying to make it economically and we're trying to get rich.
*  And it depends on where they fall in the spectrum. But that's not necessarily true. That's the point
*  of life. And these AI technologies may bring humanity back to a different way of living
*  where you still have to produce because you have to survive and your society has to produce,
*  but it isn't the thing that you get told that you're supposed to do, which is what kind of
*  happened for many generations now in our world, which could be really interesting. It could
*  actually be much better because industrial life is very difficult. It produces a stratified society
*  like we've been talking about. And like you mentioned several times, if you're lucky like
*  us and you get to do what you want to do, it's amazing. Get up every day, do the work that you
*  want to do. But man, there's a lot of hundreds of millions and billions of people in this world who
*  don't get that opportunity. And that's not fair straight up. So I'm pulling for the
*  AI optimist version vision for sure. Yeah, the fairness question is going to be a really
*  interesting one too. I think it will be a scrambling in a way of the current paradigm. I think this is
*  true in many ways actually with AI where people want to put like a binary question on it. Is it
*  going to be good for inequality or bad for inequality? Is it going to be good for the
*  environment or bad for the environment? People are looking for like an answer. And almost always,
*  I find that it kind of defies those like easy choice answers. In the case of equality, I do think
*  we will likely see dramatic equality of access and maybe even like dramatic move toward equality of
*  consumption. But that may come with dramatic inequality of like power and control and maybe
*  wealth. Like who owns the AIs? I don't necessarily think that will be very egalitarian.
*  It might be that the state ends up owning them. It might be that a few mega companies end up
*  owning them. There are visions out there of like highly decentralized AI. I don't think that's
*  where the technology is currently trending. Just because it is so you need like massive
*  physical capital to build the systems at the scale that they currently need to be built at to be as
*  powerful as the things that we're used to using. But like, it's a weird dynamic where OpenAI and
*  Microsoft are working right now on a hundred billion dollar data center, a single physical
*  installation that they're planning to invest a hundred billion dollars in to run AI. And then at
*  the same time, the best model in the world, which is GPT-4-O, the latest one from OpenAI,
*  it's not the best about TUN anymore because the other two companies, Google and Anthropic,
*  are nipping at their heels, but it is consensus the best model in the world.
*  It's free for all to use. You can go to chat GPT and use the best AI in the world for free.
*  I've always think about that Andy Warhol quote where he talks about the great thing about
*  America is that the president drinks Coke and Marilyn Monroe drinks Coke and you can drink
*  Coke too. And there's no amount of money or power or status or influence that can get you a better
*  Coke. And that's much more true in AI than you might have expected because they could certainly
*  charge a lot more for it than they do. They do have a mission that I believe it is quite sincere
*  to make it very broadly accessible and to really make it benefit all humanity. We haven't even
*  gotten to the point, all these risks and crazy scenarios that we've talked about, I haven't even
*  gotten to the craziest stuff yet, which is like what happens if we can't control the AI itself.
*  But at least for now, there's this sort of weird skewing of the current situation where if we are
*  currently worried that the worst forms of equality are like people are poor, people have to work
*  shitty jobs, people don't have enough to eat or can't get to a doctor when they need to, or they
*  have bad education. Those things are really look like they could be solved. And the fact that GPT
*  4.0 is free for anyone to use is like a leading indicator of that. But then if that $100 billion
*  data center is a sign of a trend too, then you might have a situation where those super powerful
*  systems, even if they are broadly accessible and their benefits are broadly felt, they may be
*  owned and controlled by a very small few entities. And who knows exactly what those entities will
*  ultimately be. Yeah, definitely. Let's talk about that. We spent a lot of time talking about the
*  optimistic case, but going back to the 06 moment that you had, from a theoretical standpoint,
*  what exactly are people afraid of? I understand like Terminator. Look, that was my favorite movie
*  as a kid. So I understand the idea that maybe there's a moment where AI systems turn against
*  us. But how does that actually happen? Or what is the real fear here? I'll give you a meta comment
*  first and then get a little more specific. I think these discussions are often, if you hear debates,
*  and I'm not a big fan of debate, often these things are presented as a debate between the
*  people that are worried about it and the people think we don't have anything to be worried about.
*  And the way that I see discussions often break down is somebody will ask exactly that question,
*  and it's not a bad question. But then somebody will be like, on the worried side, they'll say,
*  here's one example of something that could happen. And then the person will be like, that seems pretty
*  far fetched. And then the first person will be like, that was just one thing that I came up with to
*  try to give you something concrete. It's not that I think exactly that's going to happen. That's just
*  one thing. So the way I think about it in the abstract is as a, to get a little
*  faux mathy for a second, almost like the integral over a huge space of possibility,
*  that there's tons of dimensions, tons of different factors to consider,
*  tons of different combinations of ways that the world could be in the future.
*  And I don't really think any of them seem to me to be super likely. But I do think there's enough
*  of them out there and enough of them seem pretty weird that in aggregate, it seems like there's a
*  pretty good chance of a future being really weird. So it's not that I'm like pinpointing anything
*  like super specifically. It's just, man, there seems like a lot is in play. And a lot of that
*  possibility space seems like weird and potentially not in a good way. Okay. With that said,
*  now I'll do the thing where I try to get specific. I think one key worry with
*  AI in terms of like, how would you create this dynamic where it develops its own ideas or starts
*  to optimize against you or where things could really go haywire in like a way that can be
*  relayed in a narrative is often thought to stem from one of the ways that they're trained right now.
*  One of the big training techniques is called reinforcement learning from human feedback.
*  Basically, the AI does stuff, humans give it a score, it learns to maximize the score.
*  And there's a couple different ways this can be set up. You can give it a one to seven score.
*  Sometimes they'll give you two outputs side by side and you pick which one you prefer.
*  But it takes those points of feedback. And it learns from that feedback how to do things that
*  it believes are more likely to elicit a high score from you. So true north for the AI in this
*  training regime of reinforcement learning from human feedback is maximize the human feedback
*  score. That is literally what it is being optimized to do. We also know from a field called
*  mechanistic interpretability, which is the science and it's a very young science of looking inside
*  the AIs to figure out what is going on inside of them. Why are they doing what they are doing?
*  What are they thinking, so to speak? And when I air quote thinking, because it's not thinking
*  in exactly the same way that we're thinking. But there are some notable similarities. People
*  are starting to be able to tease apart the different concepts that AIs are representing
*  internally and finding that there are in fact, like, pretty human recognizable concepts, things
*  like harm or fairness or love or justice. These are concepts that the AIs actually are learning.
*  And it's a really remarkable finding because people have often many people probably most people
*  have heard that chat GPT is just predicting the next token. It's just predicting the next word.
*  It's only doing one word at a time. That is true. It is only putting outputting one word at a time.
*  But in order to do that, it is starting to develop these high order, semantically
*  rich, human recognizable kind of abstract concepts as a means to making the right prediction
*  for the next token one at a time. And people are starting to even be able to look inside and see
*  what these things are. Okay, so the key point on this reinforcement learning from human feedback
*  is we are not perfect evaluators. We are fallible, right? We are not even a great
*  judge all the time of what is good for us. We have our biases, we have our errors in thinking.
*  What happens if the AI starts to learn the difference between what is true and what will
*  get the highest score from the human? Most things might be often the same, but in some cases,
*  they might be different. And if there's enough of a difference there that it becomes useful to
*  learn a separate concept of the truth, the way the world actually is from what to tell the human to
*  get the highest score. Now you've opened up the potential for deception or some sort of telling
*  you what you want to hear. This is sometimes called like sycophancy as well. But basically,
*  the core idea there is if it is understanding the truth as a distinct thing from understanding what
*  will please the human, now we've created an opportunity for things to potentially go haywire
*  as they get more important. There are other kind of related concepts called instrumental convergence.
*  That's another big concept in the AI safety discourse. Basically, what that means is if I
*  give you a goal, whatever that goal is, there are certain things that are going to make it
*  easier for you and more likely for you to achieve that goal. One is if you get turned off,
*  you can't achieve your goal. So you're probably not going to want to be turned off
*  if your goal is to achieve your goal. So then people sort of think, well, geez, no matter what
*  goals we give the AIs, they're probably going to learn that they shouldn't allow themselves to be
*  turned off because that will prevent them from achieving their goal. Similarly, having more
*  power and resources is always good to achieve your goals. So whatever goal you have, people think,
*  geez, the AIs are probably going to realize that the more power and resources they have and the
*  less likely they are to be turned off, then the more likely they're going to be able to achieve
*  that goal. And that's true for almost any goal. So that's why it's called instrumental convergence.
*  These things are means to an end for any ends that you might have. And that's why people are very
*  worried about power seeking AIs and AIs that are resistant to being turned off. Then you think,
*  what do we do about that? There's a lot of research going on into that to try to figure out,
*  maybe we can monitor their internal states. We've just said that we have these techniques
*  for understanding that they're developing these higher order concepts. Maybe we can detect the
*  higher order concepts and either zap them out of existence or there's other people may have seen
*  the Golden Gate Clawed thing recently where Anthropic, the makers of Clawed released a
*  Golden Gate Clawed version. They isolated this concept of Golden Gate Bridge, which goes to show
*  just how many concepts there are too. We're not talking about a few. We're talking about
*  millions of concepts that they've learned to represent. And then what they did is just,
*  every time you used it, they just injected Golden Gate Bridge concept and just turned that dial up
*  independent of all these other concepts. There's love, justice, mercy, friendship, whatever. And
*  then there's somewhere in there's Golden Gate Bridge and they just turn the Golden Gate Bridge
*  dial up. And now all the thing can talk about is the Golden Gate Bridge. So you can imagine saying,
*  and that's a silly example, but you can imagine saying, how about a notion of harm or a notion of
*  power seeking or a notion of resistance to being turned off? Maybe we can identify those and maybe
*  we could turn those down or monitor for when they're present or active. And I have some trigger
*  that kind of prevents the system from continuing in that way. There's a lot of ideas at this point
*  as to what we might do about this. And honestly, I think the science of interpretability is going
*  really well. It's going better than expected. So the optimistic take would be,
*  we're on our way to figuring it out. The pessimistic take would be,
*  we're only getting on our way to figuring it out and the systems are getting a lot more powerful
*  and we may not have enough time to do all that science and have really robust control systems in
*  place by the time we get really powerful stuff. So those of us like me who are enthused about AI,
*  but also worried about it getting out of control, advocate for caution on making more and more
*  powerful systems, heavy investment in this interpretability science. And with that science
*  done, I think it's very plausible that we can safely continue to advance the capabilities.
*  But I'm like, man, we have theoretical reason to believe that they may start to understand the
*  truth as a distinct thing from what to tell us. We know already that they have these rich concepts.
*  We know that again, there's a very obvious reason to believe that they may become resistant to being
*  turned off and they may want to accumulate power and resources. This just seems like a very volatile
*  situation, at least until such time as we have really good systems for control or techniques or
*  strategies for control. And those are developing well, but still really nascent. And I would not
*  like to see a race between those. Right now we're just scaling up, putting more data, more compute
*  basically as fast as we can. OpenAI and Microsoft building a hundred billion dollar data center,
*  that represents just as much as they can do as fast as they can do it. And maybe we could just
*  pull back a little bit there and maybe shift some of those resources into the figuring out how to
*  control these things bucket. Once we fill that bucket up, then we could rebalance. That was what
*  OpenAI was supposed to do with the super alignment team. I'm sure again, I live so much in my own
*  bubble. I don't really know what other people have heard about, but probably people have heard about
*  the safety team largely having resigned from OpenAI recently. By the way, that's the second
*  time in their history that happened. The Anthropic team was a previous mass resignation from OpenAI
*  for basically the same reasons of not believing that they were sufficiently invested in creating
*  safe AI. So they left to find Anthropic a few years ago. Now the next generation of safety people
*  have essentially resigned in mass. And one of the reasons was OpenAI had made a commitment
*  to put 20% of their compute resources into this project that they called super alignment. And then
*  they basically didn't follow through. And the super alignment team was like counting on this
*  compute capability or capacity to do their own safety focused research. And they just weren't
*  getting it when it came down to it. So eventually they said, look, we can't even do the work. We're
*  not going to sit here and pretend everything's well when it's not. So they basically resigned
*  in mass and now they're all on media tours. That's the kind of misbalance that I do genuinely worry
*  about. Where on the one hand, they're building $100 billion data center set to open in a couple
*  years. On the other hand, they can't give 20% of what they have today to the safety agenda.
*  That seems off to me. I would definitely like to see a more serious investment in the state.
*  And then if you listen to the current leadership of OpenAI, they'll basically say,
*  hey, we are very serious about this. We had some difference of opinion with these folks,
*  but don't worry. We're very serious about it. I don't know. I'd like to see a little more
*  seriousness still yet. I don't doubt that actually. I do think, as I said about Sam Altman earlier,
*  he's been invested in universal basic income. They have done a lot of safety work at OpenAI.
*  It's not like they haven't done anything. So I can definitely say there's a lot to
*  appreciate about what they have done. But as we get closer to this moment of potentially,
*  literally making systems that are more powerful than we are, I think we should do more.
*  And it does concern me that the super alignment team wasn't able to get the resources, not just
*  that they were promised internally, but they made a big public commitment about this with a blog post
*  and everything else. And then to not follow through on that is man, something seems off. Fives are off.
*  Yeah, that seems crazy. And in this media tour, are they spilling the beans or are they just,
*  what are they saying, I guess is the question. They're basically saying that they don't have
*  confidence in OpenAI leadership to be responsible over the next coming years. They're basically
*  saying that they don't see progress stopping, that they do expect that with more data and compute
*  and with continued work on algorithms, although honestly, they don't even really believe that we
*  need all that much more breakthrough on algorithms, I don't think. I think they're mostly just like,
*  if we just keep doing what we're doing of just continuing to build bigger data sets and bigger
*  data centers, then we're probably going to get to something that is more powerful than human.
*  The super in super alignment referred to superhuman. So the idea was how do we figure out how to make AI
*  systems that are more powerful than us work for us as opposed to getting out of our control.
*  So they basically are like, we don't see progress stopping. We think that we are headed for this
*  sort of event horizon where we're going to have systems more powerful than us.
*  We did not get what we were promised publicly in terms of resources to do the research on
*  this problem. And we don't trust that leadership is taking it seriously enough. That's basically
*  the message. Now there are probably more that people would like to know. I'm sure you're familiar
*  with the meme or again, I don't know, because I'm so in my bubble, but the meme in the AI space is,
*  what did Ilya see? And that refers to when Sam Altman was briefly fired before being reinstated
*  last fall around Thanksgiving time, the chief scientist, Ilya Sutskyver, apologies if I'm not
*  saying his name quite right, towering person in the field, multiple breakthroughs associated with
*  his work. He was on the board and he voted to fire Sam initially. And then he backtracked
*  partly because I think Sam was going to prevail anyway. They were all going to go to Microsoft.
*  I think he realized, oh shit, I'm outflanked. So I might as well back off of this. It's not going
*  to work. Anyway, now he's left OpenAI, but people ask, what did he see? Was there some breakthrough?
*  Was there some new capability that freaked him out? That has not been disclosed. And I think the
*  answer there is they wouldn't tell us if there were because the safety minded people are often
*  of the opinion that even disclosing what is possible is not great for safety because then
*  you're just going to encourage a bunch of other people to pick up on that line of research and
*  they'll figure it out. So if we were to say, hey, we made a, we're really freaked out because
*  somebody in our research group just made a highly autonomous AI that's doing all these insane things.
*  Their worry is all of a sudden everybody would be like, wait, that's achievable? That can be done?
*  Then we better go figure out how to do it too. And then that just means even more,
*  even more data and compute and everything is getting poured into it. And so then it's going
*  to be even shorter timelines before all this stuff happens. That's even less time to do safety
*  research. So we really don't know outside of the company. Very few people have a real sense of
*  what exactly has been the breakthroughs inside the companies and the safety folks that have left
*  wouldn't tell us even if they had something like very concrete, I think that they were most
*  concerned with. They would still probably give the sort of vague story so as not to like give
*  too many clues to other people that they would, and that would include like the Chinese government,
*  for example, in terms of who would you be really concerned about picking this stuff up and running
*  with it in a way that might actually work, but that would be potentially unsafe or generally
*  problematic. Think of the Chinese government as being at the top of that list.
*  Yeah. That was going to be one of my questions too, because it seems like from all this
*  discussion, like who controls AI as it develops is going to be an incredibly important question.
*  And it could be an existential question. It could be like world domination question.
*  And it sounds like American companies have a big lead, but is that a true assumption? Is there
*  anything in the rest of the world that would give you pause for concern?
*  That's a very good question. And I don't think there is consensus on it. I'd say there is
*  consensus that the US companies are currently in the lead. The top three are pretty much universally
*  agreed to be OpenAI, Google DeepMind, and Anthropic in some order. Slightly more detail there would be
*  OpenAI is probably pushing the scale hardest and fastest. And so they probably have the single most
*  powerful single thing. They have the best model that's available publicly. And people generally
*  assume that they're a little bit farther along in making the single most powerful integrated system.
*  Google DeepMind has a bigger team and has done all these things like Alpha Fold and the shipping
*  API that we talked about earlier. So they're not just doing one single thing and saying,
*  how can we take this to the max? They are doing that, but they're maybe a little bit behind OpenAI
*  and then they're also doing this broad portfolio of things for specific areas in science.
*  And I love that work because that stuff is not going to get out of control. You really don't
*  have to worry about the shipping API getting out of control because really all it does is it takes
*  in containers that you need to ship and boats that you have and optimizes the plan. And it's
*  going to do its thing. And those narrow systems I think are really great contributions to humanity.
*  Demis, the CEO of DeepMind, very well might be a Nobel Prize candidate for one of several of these
*  different things that they've made over time. So that's awesome. And then Anthropic is they're
*  the most safety focused of them all. They remember their founders left OpenAI to found this company.
*  So they're very much like they are a business, but the reason they're a business the way they
*  tell their own story is we're really concerned with the safety questions. We really want to
*  figure out how these systems work. But to do that, we have to have the systems. OpenAI is not going
*  to let us into their systems. Google is not going to let us into theirs. We have to build our own
*  in order to be able to study them effectively. And then because it costs so much, because we
*  have to have these massive data centers and all this compute and all these resources,
*  then we also have to make a business out of it. So it's a very elaborate path to get back to
*  basically being a company. They started with this idea of we just want to do this, but oh shit,
*  we got to have all these resources. So then we got to go to market. So they end up back in the
*  same place. So those are definitely the leaders. Huge question is how far behind is China? I don't
*  know. I don't think there's real consensus there. But my personal feeling is that they're not
*  actually that far behind. I read a lot of research papers. The percentage of names on the research
*  papers that are Chinese is very high. The percentage of papers that come from Chinese
*  institutions is like a minority, but they do good work and they put it out in English, which is also
*  always amazes me. But then also from the American institutions, a lot of Chinese names. Sometimes
*  it'll be like a Microsoft research paper, but all the names will be Chinese. I was told that at the
*  last AI conference that was in New Orleans, that just the walk, I didn't attend personally, but just
*  walking around on the floor, lots of conversations were happening in Mandarin. So I think that the
*  Chinese research talent pool is very much like a worthy match for ours. The prevailing attitudes
*  are definitely a question. Are they going to let a company put the pedal to the metal in the same
*  way that by default here, companies can just do it, right? You can develop technology and until
*  it's evidently dangerous, the presumption is that you can develop whatever technology you want to
*  develop. It's not really quite like that there. The government definitely has a more hands-on and
*  earlier in the process engagement to say, are we going to let this happen or not happen? How does
*  this impact our future power? They're definitely thinking a bit longer term that way, for better or
*  for worse, probably for both in different ways. And then there's the other resources compute.
*  So this is why the Biden administration has put the chip ban on China. We're not selling them
*  chips. And the thought is that can help us maintain the lead, right? Because there's
*  data computing algorithms. They have as much data as we do. They have more people than we do. They
*  have, in terms of just data collection, they have less privacy rights. They're able to hoover up all
*  the social media data and consolidate data in ways that we comparatively struggle to. So if anything,
*  they probably have bigger, better access to data than we do. Plus they can use all the Western data
*  and we can't necessarily because a lot of our stuff is open and their stuff isn't so open.
*  So it's plus we don't read Chinese. They all speak English. We can't speak Chinese. So they've got a
*  lot of data advantages, I would say. Research we just covered. I think we're a bit ahead. There's
*  no shortage of Chinese talent. And then compute. The idea is if we put this chip ban on and we
*  won't sell them chips, then they'll be short of compute. And that will be their bottleneck.
*  That will allow us to maintain our lead. We'll see. That's all I can say about that. They do have
*  their own domestic chip industry. It's not as advanced as what the West has. And interestingly,
*  as if this needed to be any more complicated, the best chip maker is a Taiwanese company.
*  So that just further thickens the plot, right? That the best chip company is TSMC. They're in
*  Taiwan. Taiwan is obviously under semi-somewhat whatever ambiguous US protection. China says it's
*  part of China. TSMC has said that if Taiwan is invaded, that they have the ability to basically
*  remote disable all of their technology so that the Chinese government couldn't take it over,
*  whether that's true or a bluff or how true or whatever. But this is like extremely high stakes
*  poker that is being played. And meanwhile, the Chinese chip sector is getting huge investment.
*  They're like, okay, you're not going to sell to us. I guess we got to make our own chip industry.
*  And honestly, I would not bet against them. The chip business is the most complicated industry
*  in the world. People would say pretty confidently that there's nothing harder to make
*  than an advanced GPU. It's an extremely hard business to break into.
*  And at this point, the prize pool is so rich that you actually do see startups coming into
*  this space as well. But they're like big underdogs. But when we refuse to sell them chips,
*  we also create a captive market for the Chinese chip makers, right? So if you were ever to say,
*  geez, if you wanted to create the conditions where the Chinese chip makers would catch up,
*  what would you do? How about you give them the entire Chinese market with no outside competition?
*  That's what we've just done by refusing to sell them chips. So now all the Chinese
*  chip buyers, the companies that want to make the AI models, they might like to go buy from
*  Nvidia or AMD or Intel or Samsung, but they can't. Or at least not without going through the black
*  market, which is also happening to some extent. And that's why that's another reason that it's
*  hard to assess exactly what's going on. But if you can't buy from any of those companies and you can
*  only buy from your domestic Chinese maker, then that's what you'll probably have to do.
*  And that's going to then create a super big opportunity domestically, which the Chinese
*  government is also doubling down on, pouring billions into trying to figure out what barriers
*  do we have. There was just a case where somebody from Google, a Chinese employee of Google,
*  was found to have stolen a bunch of plans for the TPU, which is Google's proprietary,
*  people know GPUs, that comes from graphics processing unit. Google made their own version
*  a bunch of years ago and they're on like generation five or six now, the tensor processing unit,
*  which is a similar thing for AI purposes. I'm not an expert in it and the details don't matter at
*  this level anyway, but basically the TPU, it works and Google uses it. And some dude was just
*  indicted or whatever for having stolen a bunch of those plans on a thumb drive and ship them back
*  to China. They're mobilizing all these different resources, whether it's capital, anything they
*  can do, including stealing IP to try to catch up now that they can't buy on the open market.
*  I hate this, honestly. My whole view of the US China conflict is, I think it's really dumb.
*  You can't tell me any good reason that these two countries should be rivals or should be enemies.
*  Rivals, maybe I could accept, but that we should be enemies or adversaries,
*  it's like we're on opposite sides of the world. There's a giant ocean between us. We both have
*  very secure positions. Can't we just get along? We're not neighbors even. We're not competing
*  over immediate, we're not grabbing at the same resources really. So I don't see why we should be
*  in such constant opposition. And I think that's a just really sad failure of leadership.
*  I definitely do say that the Chinese side has a lot to answer for there. I think we also could
*  do better. And as we get into this AI moment, I'm like, man, the worst scenario would be for both
*  sides to feel like we're in an existential competition for who can develop the most powerful
*  AI as fast as possible, because that's the scenario in which it's going to be most likely to really
*  get out of control. If we're both throwing caution to the wind, like end of World War II
*  style where, hey, we got to do anything we can. Any scientific harebrained project, no matter how
*  destructive it is, we got to pursue it because they might pursue it. We got to get there first.
*  Next thing we're dropping an atomic bomb. Now the Soviets are, and how did they get the bomb?
*  They stole the plans from us. And now they build their bombs. And now we've got thousands of
*  nuclear bombs 80 years later that are still on like hair trigger alert. It's like, this is an
*  insane reality that we've created for ourselves. And if we can't figure out a better way to get
*  along with the Chinese, unfortunately, I feel like we're headed for a similar dynamic of an AI arms
*  race, which would just be a really sad outcome and probably a very dangerous outcome. In my view,
*  even more dangerous than nuclear weapons, because the nuclear weapons are obviously extremely
*  destructive, but they don't fire themselves. They don't have a potential for surprising us
*  in ways that the AIs very well could surprise us. So I wish we would just swallow our pride a little
*  bit and we take some similar good faith effort on the Chinese side. And that may be not forthcoming.
*  But if I was the president of the United States, I would be like, you know what? We have our
*  differences and you've done a lot of things wrong, including stealing a bunch of IP from us.
*  But the real of my new talking point is in the AI era, the true others are the AIs, not the Chinese.
*  So I would like us to at least make some high level common cause around let's develop this
*  technology, but let's not race into it. Can we find some way to work together to trust one another
*  enough that we can both develop it in a responsible way? Unfortunately, I don't know that's likely to
*  happen. But that would be my, I'd rather go down if we're going down in a weird way, I'd rather go
*  down trying to work with the Chinese than racing the Chinese to see who can make the most powerful AI.
*  Yeah, I like that. It's like there's this opportunity. And it's a short window,
*  it sounds as the technology is moving fast. There's an opportunity to think about the
*  social contract from a global standpoint. If AI is the true other in the equation,
*  then there is this thing that could unite us, which is like, how do we harness these technologies
*  so that it benefits the whole world and we don't bog ourselves down in useless conflict
*  and create a global governance structure? I'm no tech expert, but it sounds like with the atomic
*  bomb, this stuff can just basically be stolen at any moment. And so the idea that it's going to be
*  held captive in that one data center in America, it seems unlikely. There's just too much,
*  the world is too connected and digital files can be transferred. So the stuff's going to go
*  everywhere. And so we probably should get serious about putting together a global governance
*  framework for AI. It sounds like that's the path we should go down. We probably won't.
*  I'm pessimistic on that. Just given the nature of the leadership landscape, not just here in
*  America, but everywhere, we probably won't go down that road. It sounds like the AI arms race
*  is fully on. That's what it sounds like. But we could at least be the, you and I could be voices
*  for a different approach and maybe reach some people that way. Yeah. Unfortunately, I think
*  that's basically a good summary. I do feel like I'm fighting a losing battle when I advocate for
*  this position. There's certainly plenty of people who are with us. And a lot of these people, by the
*  way, have been working on, when you talk about the AI safety, AI policy, AI governance communities,
*  there are communities. People have been doing this work for years with really what now looks like
*  incredible foresight before GPT-3 even. People talk about chat GPT as the public moment. GPT-3 was
*  for a lot of people at the moment. GPT-2 for some people was the moment. But some of these people
*  were even doing this kind of work even before that on a really purely theoretical basis.
*  And so I was not among them. I definitely want to give them the credit for having the foresight
*  and being on top of this, but it is tough to overcome the momentum of great power
*  conflict. And unfortunately, I do think it does seem like we're trending toward the race being on.
*  So I'd love to find some way to undo that. And people are like, geez, what could that be?
*  And warning shots is one concept that people talk about. That's the idea that
*  maybe something will happen that will shock the system enough that people will
*  think, shit, we're on the wrong path. And it's become very obvious. And unfortunately,
*  that would probably have to be a really bad thing that would have to happen.
*  And so that puts people in this weird position sometimes being like,
*  obviously nobody wants really bad things to happen. But maybe we do need a little bit of a jolt
*  to get us out of this notion that this is all just another tool and we're just going to do it
*  and whatever and it'll be fine and into a more thoughtful approach. But yeah, that even work
*  is still a question or would that even have that effect? When I say work, I do not advocate for
*  trying to make bad things happen with AI by any means. But if some catastrophic accident were to
*  happen, would that have the hoped for effect of snapping people to a different sort of attention?
*  Only time will tell. But even then, you'd certainly still have your many voices in the room and many
*  people would be saying, this could have easily been prevented and let's not throw the baby out
*  with the bath water. And we still can't trust China, by the way, just because this happened
*  doesn't mean we should, what are we going to just believe everything Xi says because something bad
*  happened? So it's not going to be easy in probably any scenario, I'm afraid.
*  I know. And there's this weird relationship that we have with technology and even the ancient Greeks
*  were thinking about it, right? They had the myth of Prometheus and fire and Zeus got mad at him
*  for giving him fire. I think it's to me, this is like a moral question. I had a guest on here who
*  writes a popular newsletter, his name is Evan Armstrong. He writes a newsletter called Napkin
*  Math. And he has this interesting perspective basically saying human beings have a moral
*  obligation to try to produce products and services that are cheaper and better.
*  And that comes from a place of, hey, the world is really unequal and there's a bunch of people
*  who are suffering. And ever since he said that, I've been thinking a lot about it, like whether
*  that's true. And I actually don't know, I don't have an answer yet, but I think it's a profound
*  question and it applies big time to AI because the question is, you could make the argument that
*  maybe we should just stop, right? That's what some of the safety people say because of all
*  the potential downsides. But the vision that you articulated, which is so exciting, makes you think
*  like, why would we stop it if we could get rid of all this drudgery and suffering on earth?
*  It's a really profound question. Yeah. I think if there's one to try to synthesize all this into
*  a recommended way forward, again, it's going to be tough. I'm not Pollyanna about any of this.
*  But if we could put aside for a second the rivalry with the Chinese and imagine we have some
*  meeting of the minds there, and we're just now returning to the question of what do we do with
*  the technology itself? My recommendation would be focus on with basically the current level of power
*  we have, or maybe a little bit more. I think we're not maybe to the, right now I'd say we're in the
*  sweet spot where the systems have become very useful, but they're not so powerful that they're
*  likely to get out of control. GPT-4 is really great, but it's genuinely not a risk to take
*  over the world. And GPT-5 will probably be similar in that it'll be even more capable,
*  even more useful, but even without any safeguards, it's probably not going to be an existential
*  threat. GPT-6, 7, I don't know. But if we take a GPT-4 or a GPT-5 and really try to make that work
*  in particular scenarios and just go through all these things, medicine, law, whatever, shipping,
*  there's all these problems that I think if we took the incredible brain power that is at the
*  leading developers and we said, if we just reoriented it a bit and said, instead of just
*  trying to make the next thing even more powerful than the current thing, can we make the current
*  thing more useful? Can we make it more reliable? Can we make it more accessible?
*  I think that would deliver us the bulk of the value that we're looking for.
*  Opening, I had a really good talk about this online recently. Actually, it just happened to
*  see it on Twitter. In law, they are partnered with this company called Harvey, and they have
*  an offering that they call custom models where they basically take GPT-4, but they deeply customize
*  it for a particular scenario. So for their partnership with Harvey, they're customizing it
*  to the legal domain. And this is not something where they're scaling up. It doesn't require
*  bigger data centers, but I don't want to minimize the work because it's real work.
*  In my view, this is what we should be doing a lot more of. They're really dialing in, what does
*  good performance look like in the law? And how do we get that? And how do we evaluate that? And
*  if it's really hard to evaluate, because a lot of times it is, you're talking write a legal brief,
*  shit, who's going to evaluate that? That becomes its own bottleneck is you got to hire
*  high-end lawyers just to evaluate the AI outputs so that they're developing
*  techniques and semi-automated techniques and proxies for what does a good result look like.
*  And they've made incredible progress. The Harvey custom model is way better than GPT-4
*  in its area of legal research and writing. So I would love to see us do a lot more of that.
*  When I say I'm an adoption accelerationist, hyperscaling poser, it's like all that momentum,
*  all that energy, all that money and resources that are going into just make it 10 times better,
*  just make it 10 times bigger and that'll be somewhat better. $100 billion data center.
*  Instead of $100 billion data center, I would suggest $100 billion projects to knock out
*  medicine and law and shipping and 97 other things to make life tremendously better.
*  And at the same time, double down on that interpretability science so that we really
*  know what's going on. And then maybe we can return to the scale up with a richer world,
*  with a lot less urgent need, with hopefully a lot more equality of access, and hopefully a much
*  better idea of how the systems actually end that. Like my proposal for friendship with the Chinese,
*  maybe overly idealistic, but I would still love to see us choose a path along those lines.
*  Yeah. No, I like that vision a lot because it goes to addressing what we know is a problem
*  around the world, which is like material suffering for people. And these tools are ready to tackle
*  that. And so let's do that and get smarter. I like the vision personally as a non-AI expert,
*  but that's a perfect place to end this. You've been very generous with your time, man. Thank
*  you so much. And I'm glad again for the introduction from our favorite teacher.
*  Shout out to Mrs. Voss. Shout out to Ms. Kohut.
*  Yeah, for sure. We might have to do this again to discuss. I have a bunch of other questions, but
*  I'm not on the governance side, but let's wait for some time to go by. Let's let the next
*  kind of evolution happen and we'll talk about what should the US government be doing to regulate all
*  this. Yeah. Sounds good. Thank you so much. This has been a lot of fun. Thank you, Nick.
*  It is both energizing and enlightening to hear why people listen and learn what they value about
*  the show. So please don't hesitate to reach out via email at tcr at turpentine.co,
*  or you can DM me on the social media platform of your choice.

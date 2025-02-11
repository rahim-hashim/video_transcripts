---
Date Generated: October 13, 2024
Transcription Model: whisper medium 20231117
Length: 7187s
Video Keywords: []
Video Views: 637
Video Rating: None
Video Description: In this episode of The Cognitive Revolution, Nathan explores unconventional approaches to AI safety with Judd Rosenblatt and Mike Vaiana from AE Studio. Discover how this innovative company pivoted from brain-computer interfaces to groundbreaking AI alignment research, producing two notable results in cooperative and less deceptive AI systems. Join us for a deep dive into biologically-inspired approaches that offer hope for solving critical AI safety challenges.

Check out AE Studio here: https://ae.studio
Self-Modeling: https://arxiv.org/abs/2407.10188
Self-Other Distinction Minimization: https://www.alignmentforum.org/posts/hzt9gHpNwA2oHtwKX/self-other-overlap-a-neglected-approach-to-ai-alignment 
Neglected approaches blog post: https://www.lesswrong.com/posts/qAdDzcBuDBLexb4fC/the-neglected-approaches-approach-ae-studio-s-alignment

Apply to join over 400 Founders and Execs in the Turpentine Network: https://www.turpentinenetwork.co/

SPONSORS:
WorkOS: Building an enterprise-ready SaaS app? WorkOS has got you covered with easy-to-integrate APIs for SAML, SCIM, and more. Join top startups like Vercel, Perplexity, Jasper & Webflow in powering your app with WorkOS. Enjoy a free tier for up to 1M users! Start now at https://bit.ly/WorkOS-Turpentine-Network

Weights & Biases Weave: Weights & Biases Weave is a lightweight AI developer toolkit designed to simplify your LLM app development. With Weave, you can trace and debug input, metadata and output with just 2 lines of code. Make real progress on your LLM development and visit the following link to get started with Weave today: https://wandb.me/cr

80,000 Hours: 80,000 Hours offers free one-on-one career advising for Cognitive Revolution listeners aiming to tackle global challenges, especially in AI. They connect high-potential individuals with experts, opportunities, and personalized career plans to maximize positive impact. 
Apply for a free call at https://80000hours.org/cognitiverevolution to accelerate your career and contribute to solving pressing AI-related issues.

Omneky: Omneky is an omnichannel creative generation platform that lets you launch hundreds of thousands of ad iterations that actually work customized across all platforms, with a click of a button. Omneky combines generative AI and real-time advertising data. Mention "Cog Rev" for 10% off https://www.omneky.com/

RECOMMENDED PODCAST:
This Won't Last - Eavesdrop on Keith Rabois, Kevin Ryan, Logan Bartlett, and Zach Weinberg's monthly backchannel ft their hottest takes on the future of tech, business, and venture capital.
Spotify: https://open.spotify.com/show/2HwSNeVLL1MXy0RjFPyOSz

CHAPTERS:
(00:00:00) About the Show
(00:00:22) Sponsors: WorkOS
(00:01:22) About the Episode
(00:05:18) Introduction and AE Studio Background
(00:11:37) Keys to Success in Building AE Studio
(00:16:57) Sponsors: Weights & Biases Weave | 80,000 Hours
(00:19:37) Universal Launcher and Productivity Gains
(00:24:44) 100x Productivity Increase Explanation
(00:31:46) Brain-Computer Interface and AI Alignment
(00:38:05) Sponsors: Omneky
(00:38:30) Current State of NeuroTech
(00:44:00) Survey on Neglected Approaches in AI Alignment
(00:50:41) Self-Modeling and Biological Inspiration
(00:57:48) Technical Details of Self-Modeling
(01:06:17) Self-Other Distinction Minimization
(01:12:44) Implementation in Language Models
(01:19:00) Compute Costs and Scaling Considerations
(01:24:27) Consciousness Concerns and Future Work
(01:40:24) Evaluating Neglected Approaches
(01:55:56) Closing Thoughts and Policy Considerations
(01:59:25) Outro

SOCIAL LINKS:
Website: https://www.cognitiverevolution.ai
Twitter (Podcast): https://x.com/cogrev_podcast
Twitter (Nathan): https://x.com/labenz
LinkedIn: https://www.linkedin.com/in/nathanlabenz/
Youtube: https://www.youtube.com/@CognitiveRevolutionPodcast
Apple: https://podcasts.apple.com/de/podcast/the-cognitive-revolution-ai-builders-researchers-and/id1669813431
Spotify: https://open.spotify.com/show/6yHyok3M3BjqzR0VB5MSyk
---

# Biologically Inspired AI Alignment Exploring Neglected Approaches with AE Studio's Judd and Mike
**Cognitive Revolution:** [October 05, 2024](https://www.youtube.com/watch?v=1C3yLKAvPw8)
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
*  Hello, and welcome back to the Cognitive Revolution. Today, I am thrilled to share my
*  conversation with Jud Rosenblatt and Mike Viana, CEO and R&D Director on the Alignment Team at A.E.
*  Studio. This episode is both technically deep and highly inspirational. It's really a perfect
*  example of why I love making this show. A.E. Studio's story is genuinely amazing.
*  They started with a plan that sounds, frankly, too complicated to work. Bootstrap a software
*  consulting business and then use the profits to fund work on effective altruism causes.
*  And yet, they've pulled it off, demonstrating unusual levels of organizational agility and
*  responsiveness to the fast-changing AI environment along the way. After first choosing to focus on
*  brain-computer interface technology and building real capability in that notoriously challenging
*  domain, they, like many others in the field, recently concluded that the timeline to AGI
*  could be just a few years, and that if so, this would not be enough time for their brain-computer
*  interface work to pay off in the way that they'd hoped. With that in mind, they took a step back to
*  survey the field. Quite literally, they conducted a survey of AI alignment researchers, which showed
*  that most researchers do not believe we are collectively on track to solve alignment issues
*  before powerful AI systems come online. And based on that finding, they ultimately pivoted into new
*  research agendas with plausibly shorter timelines to pay off. Now, just months later, they've produced
*  two notable AI alignment results, using biologically inspired approaches to design
*  more cooperative and less deceptive AI systems. Importantly, they've managed to implement these
*  strategies in relatively straightforward, understandable ways that don't require breakthroughs
*  in interpretability or any other area of AI safety in order to work. We spend the majority
*  of today's conversation going deep into these latest publications, both of which are among my
*  favorites of 2024. First, what happens when you train an AI model not just to do a certain
*  task, but also to model its own internal states? This is an important part of human cognition,
*  and it turns out not only that models can do this, but that they accomplish it in part by
*  simplifying their internal states, thus becoming easier for others to understand as well. Second,
*  what happens if we attempt to minimize the difference in the way that AI systems represent
*  self versus other? We know that humans cooperate well in part because we use the same cognitive
*  processes to model others as we use to model ourselves. And again, with a clever but relatively
*  simple setup, it turns out that self other distinction minimization can train an already
*  deceptive AI agent to be honest once again. About this result, Eliezer Yudkowski said,
*  not obviously stupid on a very quick skim. I rarely give any review this positive. Congrats.
*  Personally, after going deep on the topic, I'm a bit more enthusiastic than that. I really love
*  this work, and it gives me real hope for more eureka moments that could move the needle on AI
*  safety. Of course, AE Studio is not resting on their laurels. They are still actively seeking out,
*  evaluating, and investing in neglected but high potential impact approaches to AI safety,
*  even if at first glance they seem unlikely to succeed. As always, if you're finding value in
*  the show, we'd appreciate it if you'd take a moment to share it with friends. I want to specifically
*  encourage listeners to share this episode with a friend who might have their own neglected approach
*  to AI safety. Too often, all these individuals here is that their ideas are crazy and will never
*  work. And while that might be true in many cases, we do need people to take personal career risks
*  in the public interest. And Judd and Mike's recent work demonstrates that it's often the
*  unconventional ideas that yield the most important results. We welcome your feedback and suggestions
*  via our website, cognitiverevolution.ai, and you're always welcome to DM me on your favorite social
*  network. Now, I hope you enjoy this outstanding conversation about pursuing and succeeding with
*  neglected approaches to AI safety with Judd Rosenblatt and Mike Viana of AE Studio.
*  Judd Rosenblatt and Mike Viana, CEO and R&D director on the alignment team at AE Studio.
*  Welcome to the cognitive revolution. Thanks for having us. You guys have built a remarkable
*  company with a fascinating backstory and some really interesting recent work. So we've got a
*  lot to cover. As regular listeners know, I very seldom ask the backstory question. I think yours
*  is quite different. So I'd love to give you the chance to tell the backstory of how you started
*  AE Studio, what the mission is, and how you've developed the company to what it is today.
*  Thanks again for having us. The backstory of AE is basically back in 2016, I realized that I had the
*  luxury of living off my wife's salary and never having to work again. That freed me up to think
*  more deeply about the long-term future of technology and humanity. One thing I thought a lot about is
*  that I sometimes like to think long complicated thoughts that take a while to convert into words.
*  By the time I convert them into words, I might say something entirely different from what I
*  imagined in my head. Humans aren't very good at communicating to their future selves, let alone
*  other people compared to what they might be with better tools of thought. I considered that there
*  might be a low probability that within my lifetime humanity's primary mode of interaction with
*  computers might come to be via branded computer interfaces. If that does come about, it would be
*  very good to try to make it come about in a way that's more agency increasing for the end user
*  instead of manipulating people to do things they don't want to do and interrupting them mid-thought
*  with ads, having Mark Zuckerberg own the extensions of their thoughts. Two, it might be a way to make
*  humans sufficiently smart and wise enough to be better able to solve some of humanity's greatest
*  challenges, including solving AI alignment. I continue to think there is a possibility we need
*  substantial human augmentation to solve the alignment problem. I decided to create a profitable
*  bootstrapped software and AI product development consulting business, building products for clients
*  without taking any money from investors. We like to build products that increase what we talk about
*  as human agency, with the idea being that it's better business sense in the long run to increase
*  your end user's agency, it makes users like you more, want to use you more, spend more money and
*  refer their friends to do the same. Taking that same philosophy with the work we do with clients
*  and making great value for them and having them want more work and refer their friends led us to
*  grow the consulting business to over 160 people. We took the profits of the consulting business to
*  invest in building our own agency increasing startups. So we built and sold the first one
*  of those and plan to incubate quite a lot more in the future as well. We take the capital that we
*  produce from these businesses and invest them originally in trying to build maximally agency
*  increasing BCI software without profit motive to help people with neurological injury and disease
*  increase their agency, but also in the future make the nature of human existence substantially better
*  and make us smart enough to solve the alignment problem. The consulting business grew, we sold the
*  first startup, we made a name for ourselves in the BCI world and worked with top BCI hardware
*  companies. Super excited about the work we did there, pushing people to build things in more agency
*  increasing ways than they otherwise would have done. A few years ago after I had kids, I was
*  paying attention to what was happening with AI because we build stuff with AI ourselves all day,
*  noticing that timelines might be shrinking faster than I would have hoped. We have this unique
*  structure where we are unlike all the other for-profit businesses that have anything to do
*  with AI alignment, we are not incentivized to create AGI ourselves. We don't have any investors,
*  we don't have to have returns to them and we instead can do the right thing long term for
*  humanity and consciousness in general. We also are entrepreneurial and good at getting stuff done and
*  getting to the root of the problem and we have to be because we're paid to do that for clients. We
*  have this A guarantee which is that we will treat your client project as though it is our own startup,
*  as though we are founders of your startup. Everyone is constantly priming themselves and reminding
*  themselves of that every day, which means that the top idea in their mind is often while they're
*  taking a shower or walking the dog, thinking about how if I were a founder of the startup, how would
*  I make it super successful? It's great that isn't just the case for client projects but also for
*  the work that we do with BCI which allowed us to have a real impact there. Just trying to solve
*  the alignment problem, maybe we should put the profits of the company into alignment and we
*  didn't know how to do that at first. We spent a lot of time thinking about and researching how to
*  have the biggest positive impact there and eventually realized that with the effective
*  altruism ITN framework, the highest impact thing to do is actually things which are individually
*  unlikely to work but very high impact if they do work, neglected approaches. The BCI thing we
*  were going to start with was a neglected approach and it worked better faster than we would have
*  guessed but still the timelines would be much longer for sure. We concluded that we should work
*  on neglected approaches ourselves. One of the neglected approaches we realized is potentially
*  impactful is encouraging others to work on neglected approaches too. It's interesting that
*  the highest expected value thing to do is work on these neglected approaches but that's mostly not
*  what people are doing. Historically, we're excited to see people work on more and more neglected
*  approaches to do them ourselves internally which we're working on it. Excited to talk about the
*  specific ones that we've worked on and shared publicly so far. Also excited to encourage the
*  alignment community to work on more and more neglected approaches and realize that individuals
*  can start a startup which everyone else thinks is going to fail. You can also work on a neglected
*  approach to alignment that no one else believes in. It might just work. I love it. There's an
*  unbelievable amount there that I want to dig into. I guess for starters at a high level,
*  this plan sounds kind of crazy. If I heard this at a startup pitch competition or if somebody sent me
*  a two-pager with the plan that you have executed already, I would say there's way too many steps
*  in this plan. It's going to be really hard to bootstrap a consulting business and be profitable
*  enough to do these other things and you're going to have the tug of clients pulling you in one
*  direction. What would you say are the keys to the success that you've had in building a business,
*  having these lofty priorities, executing on the day-to-day but actually keeping those in mind and
*  staying agile enough to actually, we're not talking about incremental changes to your strategy here
*  but pretty significant fundamental changes. Maybe you have some tricks or some special attributes
*  that put the odds more in your favor but I would love to know what they are. I do think that it's
*  an unconventional path and because it is so unconventional, the assumption is that it's not
*  going to work. There are all sorts of things that are unlikely to work and also all sorts of things
*  that are likely to work but the things that haven't been done before people are more likely to assume
*  are not going to work. I remember when I was first starting the company and outlined the plan to
*  people everyone was like that's crazy, of course that's not going to work. I think a lot of the
*  reason why it has has been that it's a de-risked conservative approach in fairly ambitious things
*  and I think we're doing it for the right reasons. It was impactful to realize that I wasn't motivated
*  by money and I could live off my wife's salary for the rest of my life and then realize that I could
*  think very long term about the future of technology and humanity and if you do the right thing every
*  step of the way then it winds up like yielding better results for you as best you can over time
*  There's this really interesting Paul Graham essay called Mean People Fail which puts forth the idea
*  that we are moving from a world in which you've got more resources by taking resources from other
*  people like conquering neighboring lands and stealing their serfs and we're moving from that
*  world into a world in which you get more resources by creating value for others. It's better to do
*  the thing that creates value for others and be a good person to work with such that people want
*  to work with you in the future and provide more opportunities and the best startup founders he
*  knows are very nice good people. However a lot of the things about the way the world works are still
*  rooted in older ways of doing things. This is why people build products and service companies that
*  optimize for a short-term revenue over doing the right thing by their users and increasing
*  value created for users and profits for the company. For example the company that we built
*  and sold was a direct-to-consumer subscription e-commerce SMS management tool. Subscription
*  e-commerce is a big growing thing people get subscription coffee protein bars and whatever
*  else. The perennial problem is once you signed up for one of these things eventually you have too
*  much of the thing. What we built allowed you to manage your order via SMS you never get any
*  promotional marketing stuff pushing anything on you it just made it so that from when you first
*  signed up it made it super easy to change your order or skip a month or whatever and what this
*  wound up doing is substantially reducing short-term revenue for the companies that used it but also
*  substantially increasing lifetime value of customers. It's interesting how obvious this is but
*  people are inclined to leave a lot of value on the table because they're not inclined to do things
*  like this. When we were first doing sales for the startup potential customers would respond one of
*  two ways they would either say this is awesome of course I want to sign up for this and have my users
*  get the right amount of the thing that I'm making for them and passionate about putting out into the
*  world or they would be like I don't know about that I don't want my revenue numbers to decrease
*  that's not going to look good to my investors. It's a very stark difference which of the two
*  approaches you would get and honestly if we were a lot bigger instead of being acquired I would have
*  acquired the company that acquired us and then used that litmus test to evaluate whether or not
*  to invest in these direct-to-consumer subscription e-commerce companies. This is sort of core to our
*  DNA is has been fairly good for us and incidentally also for people thinking about starting alignment
*  driven organizations non-profits or for-profits I think if they start out mission driven and
*  don't compromise on that and only bring along partners who are aligned with that it makes
*  a lot easier to do things all the way along and it does lead to the creation of bigger opportunities
*  in the long run as well. The company came after the core values themselves and they allow for a
*  lot of this stuff we're very big about starting small but then taking acceleratingly large
*  A-B tested baby steps that allows us to go into new things that we have no business doing because
*  we can assume we're going to be terrible at it first but with the growth mindset we'll get
*  better and better over time. The self-efficacy beliefs that ensue from having done that a little
*  bit yield the ability to do substantially more and more ambitious things. I think people tend to
*  overestimate what they can do over a short period of time and underestimate what they can do over a
*  much longer period of time. We set out to do very ambitious things we set originally like this
*  10-year big hairy audacious goal with a goal about the consulting business and the skunk works
*  companies and the BCI stuff and we wound up actually achieving that whole thing way sooner
*  than we could have guessed then we made that all the more ambitious. We thought it was unlikely to
*  happen but we could do one or two of these things. Ideally if we can do the third thing that would be
*  great. Let's first perfect the consulting business then start to do the skunk works then start to
*  do the BCI stuff and now the AGI alignment stuff. Interestingly in the very beginning I set out to
*  do all of them simultaneously BCI, skunk works and consulting. I did a terrible job of all of it. It
*  was okay enough but it didn't work then we went back over time and perfected did one and one were
*  really well and then set that off the run quite effectively with the right external structures
*  that things work way better and I think we were also quite interested in building things that are
*  sort of like in a cyborgism type way an extension of oneself as a result of the things we've built
*  internally. I am probably a hundred times more productive in a single day than I was when I
*  started the company. It's great to be constantly thinking about stuff like that as you scale an
*  organization and investing. We have a lot of the best developers and data scientists in the world
*  and we're always investing in things to build and use for ourselves to improve the quality of our
*  lives and increase our agency. Hey we'll continue our interview in a moment after our word from our
*  sponsors. Today's episode is brought to you in part by Weights and Biases. As a developer the journey
*  from concept to production ready large language model apps is fraught with challenges. Dealing
*  with unpredictable large language model outputs, correctly handling PII and ballooning API costs
*  can all be blockers to shipping your next AI powered feature. Weights and Biases Weave is a
*  lightweight AI developer toolkit designed to simplify your large language model app development.
*  With Weave you can trace and debug input metadata and output with just two lines of code. Weave helps
*  you run rigorous evaluations and securely manage all of your data sets and system configurations
*  so you can focus on what matters most iterating and improving on your large language model powered
*  applications. Plus Weave integrates seamlessly with your favorite APIs and libraries including
*  OpenAI, Anthropic, Mistral, Cohere, Langchain, Llama Index and more. So make real progress on
*  your large language model development. Visit wnb.me.cr to get started with Weave today.
*  That's wnb.me.cr and thanks to Weights and Biases for sponsoring this episode.
*  I am really excited that our new sponsor 80,000 Hours is now offering free one-on-one career
*  advising sessions to cognitive revolution listeners. 80,000 Hours aims to be the best
*  source of advice for people who want to do the most good that they possibly can with their careers.
*  We typically work for about 40 years in our lifetime and we work about 2,000 hours per year.
*  That is the single biggest opportunity that most of us have to make a positive contribution and
*  it's worth being strategic about it. That's where 80,000 Hours can help. I actually used
*  their career advising service myself. Two years ago I had just finished the GPT-4 red teaming
*  project and I wanted to do anything I could to nudge the AI future in a positive direction.
*  But what could or should I do? That was not clear. After my call with 80,000 Hours I got a number of
*  connections to outstanding individuals in the space and over the course of the follow-on
*  conversations I developed confidence that this podcast was one of the projects that I should
*  pursue. Today I'm thrilled to have built an audience of thoughtful high potential people
*  that 80,000 Hours wants to help. To request a free one-on-one career advising session,
*  follow the link in the show notes. It's 80,000hours.org slash cognitive revolution.
*  That's 80,000hours.org slash cognitive revolution. Sign up for a free one-on-one career advising
*  session. Figure out how you can make a positive impact on the AI future and I think you'll be
*  glad that you did. Okay, I'm gonna have to be disciplined in my follow-up questions. Long-term
*  thinking has come back in fashion. You're a great example of setting out with that mindset. Hiring
*  people with a mission-driven orientation is commonly received advice, but easier said than done,
*  especially if you're sort of like our mission is to solve the AI alignment problem, but your job
*  is to build this SMS tool for subscription management. That's where I see a lot of these
*  things, not even necessarily with goals as ambitious as addressing AI alignment, but even
*  just on a more conventional level. Oh, we'll do technology consulting and then we'll make our own
*  products and apps and we'll kind of also be a startup. That typically doesn't seem to work.
*  People kind of just get consumed with the consulting. People have to do a good job on
*  these projects, right, for the whole thing to go. How do you, from a leadership standpoint or a
*  culture standpoint, how do you get people focused in on the sort of foundational tasks that may be
*  the less sexy tasks that everything else depends on in a way that keeps people happy? Yeah, absolutely.
*  I don't think they are less sexy. They're interesting technical problems to be solved.
*  The brightest, most ambitious growth mindset people can get excited about whatever that might
*  be. I genuinely am excited and care deeply about every single one of our client projects and
*  think they're awesome and want to do everything I can to make them succeed. We've scaled the
*  organization in such a way that I can have a positive impact on them, but also trust really
*  great people to be fully focused on them. But originally I was fully focused on them and that
*  was all I did at the very beginning because we're a profitable bootstrap business. I also rented our
*  office on Airbnb. I remember my partner on the first day he started, a Dutch tourist stepped
*  out in a towel and asked him, where's the bathroom? He was completely shocked. In any case,
*  you might be the brightest machine learning engineer in the world and you might be the
*  person who thinks of the thing that ultimately solves alignment, but you still have to do the
*  dishes sometimes. And you might as well enjoy yourself while you do that. The things that we
*  do are way more exciting than doing the dishes. They are legitimately exciting in and of themselves.
*  The better job you do with it, the better job you wind up being able to do with everything else.
*  Because we're a growing company with a lot of opportunity doing more and more ambitious
*  things over time, there is unlimited opportunity for individuals in the long run to grow into
*  various different things. Basically, if you are what we call a good tripper, you do the right
*  thing and take on more than your own fair share and you're willing to push yourself when things
*  seem difficult. This comes from me having led wilderness trips for many summers in Wisconsin
*  and Ontario where you take a group of kids who would be sort of not necessarily beforehand any
*  experience during difficult wilderness trips. And then by the end of the trip, we would engineer
*  an atmosphere in which it was cool to be a good tripper. Do more than your own fair share to carry
*  the heavy pack, get into camp, realize that tents need to be set up, vegetables need to be chopped
*  and water needs to be purified. And do that without being asked. Push yourself to carry a canoe farther
*  than you think you can when you thought you couldn't even pick it up. There's no better feeling than
*  throwing the canoe off your shoulders into the next lake. In life today, people often coddle
*  themselves too much and then they don't wind up getting the super rewarding feeling of throwing
*  the canoe off their shoulders into the next lake. But if you do push yourself in different ways,
*  then you can wind up achieving bigger and more rewarding. And I think people who wind up being
*  good trippers on whatever they wind up doing and creating the maximal value they can for our clients
*  or in the Skunk Works company, they're the people that are going to have the biggest positive impact
*  in the various other things that we do and have a bigger positive impact on the world.
*  Two, one fun little hack that we set up. Actually, my wife, who's our CTO and far smarter than I am,
*  set this up. We donate 5% of our profits to effective altruism charities, typically of shorter
*  term, not longer term things. So I tend to push for them to be longer term things like malaria nets.
*  Every hour you work on some annoying bug that's a billed hour to a client, you wind up donating 5%
*  of the profits of AE to save lives, which is intrinsically motivating, I think. And that's
*  been pretty awesome. We have a lot of other little things that add up to make it such that people
*  can feel motivated on a day to day basis. But the reality is sometimes there will be things that are
*  quite difficult and challenging and not motivating in whatever work you might be doing, whether it's
*  working on alignment or some client project or whatever other job you might do. I do think that
*  people starting nonprofits and for-profits doing AI safety can have the mission of doing something
*  for AI alignment. That itself is very important and potentially quite urgent. It would be great,
*  for instance, to nerd snipe a lot of the brightest startup founders into making their startup is
*  have something marginally to do with increasing probability of AI alignment instead of just
*  advancing capabilities. It would be great to get successful founders who are trying to figure out,
*  okay, now I've made money, but what's the meaning of life to do something impactful for the world
*  and advance AI safety at its core. There is a scarcity of people who just get stuff done.
*  There are a lot of great people who get stuff done, but there are not enough people in this
*  field. It would be great to have more people who can execute, run organizations and work on
*  more neglected approaches to AI safety. That's all fascinating. 100X more productive
*  position today as opposed to when you started. I often say, depending on the exact task, I'm
*  I think like a multiple more productive with AI tools at my disposable today, but I'm definitely
*  on 100X more productive. I want some of that. Give me a little flavor for how you have achieved that.
*  Yeah, absolutely. There is quite a lot of different stuff that we do at the company and that I do on
*  an individual level, but I would say the single thing which alone has made me 100 times more
*  productive because it's made me at least 100 times more prolific. The things that are able to get out
*  of my head now go to execute in various ways. The company is a specific tool that we built,
*  which is sort of a launcher. It's called Universal Launcher. It's really mostly customized
*  for people at our company, though others can't use it. You can download it on universal launcher.com.
*  But basically, the idea is like, you know, there are limits to your working memory. Previously,
*  I would be doing something and think, oh, I should do X or I want to ask my assistant to schedule a
*  meeting. Then I might have to open up Slack and message them and be like, would you mind scheduling
*  a meeting with this person at this time? Or I open a Trello card to have us discuss X, Y, and Z.
*  And I have to open my web browser and open a new tab, type in Trello.com, wait for it to load,
*  select the right board and go to the right column. Basically, as a result of the limits of working
*  memory, there's an increased probability that you're going to lose the full context of whatever you
*  thought of originally. This, I think, is one of the greatest injustices of modern humanity as it
*  exists today. I wouldn't be surprised if future generations look back on us and be like, wow,
*  those people could never think complete thoughts. And that's like a terrible travesty up there with
*  other great inhuman things that had to exist. But in any case, it also can just make you a
*  lot more productive with a single command. I press command spacebar on my Mac or on my phone.
*  There's this little button, the U button. I can push that and it goes straight to the launcher.
*  Then I can add to do items to my own to do list or for other people or to different boards to talk
*  about X with our CFO or ask my assistant to do Y. Interestingly, I use this as do most other people
*  at our company. It's remarkable how much more productive it winds up making you. But also,
*  particularly, one thing that's pretty exciting about it is that you don't have to use universal
*  launcher to have this effect. You just have to capture the ideas. But the fact that I know I can
*  capture the ideas, I trust the external structure that they will wind up getting executed with high
*  probability of success because historically they have been. That means that I'm way more likely to
*  capture way more ideas than I otherwise would. That's pretty liberating and it winds up making
*  me think of much more interesting new ideas, initiatives and solutions to various different
*  things. I can be reading some random paper and then think, this is really cool. I should have
*  us look into this particular neglected approach and then capture that and it actually winds up
*  getting done. Pretty amazing and awesome. I think the optimal end user experience of an individual
*  using technology eventually will be something closer to that, but also having AI agents wind
*  up implementing various different things that you'd want done more fully. We've built some parts of
*  that into this tool as well. I think the thing that has made me the most productive is the fact
*  that I can get more ideas out faster instead of holding in my head. I have to do X. When it's no
*  longer held in my head, I can be fully focused on whatever the other thing is I'm doing. I think a
*  lot of the time people lose agency. You might be working on some super complex technical problem,
*  but then you see a missed call from your cousin and you're like, oh, I should call that person
*  back. Then for the rest of the day, you might be multitasking between, oh, I got to call that person
*  back and trying to hold all this random complex stuff in your head. You're not going to hold it
*  in your head as well and you're not going to solve the problem as well. The solution you come up
*  with is going to be substantially worse than you otherwise might have. Just being freed out to think
*  more deeply in a way where you're totally present in what you're doing, but also you can trust that
*  whatever other distractions come up, get put into the right external structures to deal with, I think
*  is quite liberating for me. Then we've tried to build structures like that throughout the company
*  for other individuals to be able to capitalize on the same thing. Mike, what is your experience
*  with Universal Launcher, for example? One of the things that's interesting is all of the integration.
*  Jed was talking about Slack and Trello, but there's lots of integration. It's a matter of idea to
*  muscle memory to capture, going from idea to muscle memory and how it's captured and you can
*  release that idea and move on is actually a huge productivity gain. What I think is...
*  Cool, UniversalLauncher.com. I'm on the website right now. Mike, you worked at A for years before
*  you've used Universal Launcher. How is life different as a result? I can't imagine not using
*  it anymore. It feels like an extension of myself in a way. It's muscle memory to do it. Going through
*  UI to try and capture an idea and then all of the distraction and how long that takes versus
*  just capturing it immediately. I had an update and I had broken something with it at one point
*  with the install. It wasn't running. I felt like I couldn't use my computer correctly. My muscle
*  memory wasn't working and I had to relearn how to do it the old way temporarily. So yeah, it's really
*  a powerful thing. There is a steep learning curve. That's true. I think one of the reasons I
*  didn't use it for many years is because there is a bit of a learning curve. It's a little bit like
*  learning an instrument. So yeah, if you're willing to go through that learning curve, the payoff is
*  huge. One thing that's very cool about Universal Launcher, I think, is that this is just one example
*  of a thing that substantially increases our agency with technology and makes me human better. We're
*  on technology all day, day in and day out. And this thing fundamentally solves the thing. You take
*  out your phone to do X, you see a bunch of push notifications and then you're like, why did I pick
*  up my phone in the first place anyway? Instead, we take out our phone, push one button and go
*  straight to do the thing and don't have to deal with the push notifications. We don't want to do
*  it. I think that this sort of thing, though, it's less obviously something that solves alignment.
*  These things are going to be increasingly important in the future. As we have AI taking over more and
*  more things, it's going to be important that we understand the way the human brain works and then
*  build end user experiences that increase human agency and improve the nature of being human.
*  There's low-hanging fruit to build stuff like this, but just as nobody sets out to build
*  profitable bootstrap businesses with big visions and long-term missions, people don't set out to
*  build technology products that have steep learning curves and no clear plan to get revenue models
*  just because they want to use the thing to increase their agency. And as software gets cheaper and
*  cheaper to build, it's going to be pretty great that people can invest in things that substantially
*  improve the nature of being. The Universal Launcher makes my life experience way better.
*  I can't tell you how much better it is. I enjoy being used as a result of this. This is just the
*  tip of the iceberg in terms of what people can create. The more stuff like this that people
*  create, the more productive and happier they will be to better solve the alignment problem and other
*  problems too. People could also do startups to increase agency and make alignment researchers
*  happier and more productive. The way you guys talk about the muscle memory involved does lead
*  into thinking about brain-computer interface. We now have Neuralink with an implant in a couple
*  of individuals' brains and the way they describe their experience is very much the muscle memory
*  type experience where they're learning to use this interface and they have to develop a new
*  scale even though it's all mediated by that implant. How did you think about the brain-computer
*  interface problem? Do you think about it similarly to how Elon has talked about it where he talks
*  increasing the bandwidth between the computers and going along for the ride with the AI era
*  or perhaps a different foundational way of thinking about it? I'd love to hear some of the
*  most interesting projects that you've done in that space over the last few years.
*  Yeah, absolutely. The original motivating factor with regards to alignment and BCI was less being
*  able to keep up with AI and more making humans smart enough to solve the alignment problem in
*  the first place. There is a possibility we might be able to keep up with AI via BCI but I don't
*  think it's a very high probability so it seems somewhat wishful thinking but at the very least
*  we'll be able to go faster and think better and that'll be pretty nice but I do think there's a
*  lot of opportunity to just make us smarter to be able to solve the alignment problem in the first
*  place. In a world where we get basically unlimited funding going towards alignment which I do think
*  is actually entirely plausible. Everyone suffers from exponential slope blindness and that does not
*  predict the future particularly well when it comes to things with exponential slopes. We might wind
*  up finding ourselves in the low single digit number of years in a world in which there
*  is effectively unlimited funding for alignment and nobody knows where to put it. The world might
*  start to say you know we spend trillions of dollars globally annually on defense. We should spend at
*  least that much on the biggest threat humanity has ever faced. The people who could do meaningful
*  things to advance alignment are sorely unprepared for a situation like that. BCI in particular is
*  one area in which you can invest a great deal of money and potentially have huge huge impact when
*  that does come about. So especially if you get truly automated science that doesn't kill us and
*  not just automated AI but also various other automated things in labs and Tesla robots that's
*  entirely possible. Decades of BCI progress in the space of a year or a month of course there are
*  limitations because it requires human patience generally but there may be ways around that in
*  terms of the biggest innovations that need to be made. It's a very much a neglected approach in a
*  larger portfolio of bets which works best in that scenario. I think that's most promising but then
*  there are other things that work there too. Mary and others around Kona are quite excitedly invested
*  in the human intelligence augmentation, gene editing for human intelligence augmentation
*  startup which could make a big impact. But specifically with BCI the original thinking was
*  that we wanted to without profit motive build open source BCI operating system Linux style which
*  would enable the development of multimodal BCI systems that would increase human agency and human
*  flourishing. We started with originally a guy who now is the CEO of a FRO doing ultrasound was an
*  AE client doing machine learning. He helped us kick off our BCI initiative when we had no idea
*  what we were doing. Our original forays were sort of embarrassing but we figured out what we were
*  doing with him and got involved working with top labs around the world doing various new ML methods
*  to accelerate BCI development. A motivating factor was that Facebook met and Google were really
*  involved in developing BCI and we didn't like the idea of them owning the extension of our thoughts
*  as I said before. So without profit motive trying to build maximal agency increasing BCI, one thing
*  that started to put us on the map is that we participated in this prestigious neural-laden
*  benchmark challenge which was started by Chatham's lab at Georgia Tech and we used state-of-the-art
*  neural models combined with various advanced ML techniques to win that challenge. We worked with
*  labs doing advanced BCI like BrainGate which had been at the forefront of BCI systems and also
*  focused on finding tools and methods that could be shared across different labs to accelerate their
*  research and collaborated very closely with them to develop a bunch of different interesting open
*  source projects and got some grants to do so as well. Those things include the neural data
*  simulator which worked with an awesome collaborator named Chad Boulet and enables BCI development
*  without a participant in the loop. Another one's the NDK, the neurotech development kit
*  which we did with a guy named Quentin and another guy named Millen who are both doing very cool
*  things in this space now too. New neuro data standards for things like NWB which is neuro data
*  without borders, brain imaging data structure to facilitate better data sharing across groups and
*  privacy preserving ML methods for neural data to improve user agency privacy, doing a bunch of
*  different blockchain stuff and distributed learning systems which we applied to BCI using
*  techniques like federated learning and homomorphic encryption. After doing all this for the community
*  and started working with leading BCI companies we worked with BlackRock Neurotech which makes the
*  Utah array the first FDA approved implanted invasive electrodes with Forrest Neurotech on
*  their minimally invasive ultrasound systems that let you get a thousand x more data out of the
*  brain than you could previously do and also have supported work and are excited about work being
*  done by various other BCI adjacent startups like Journey, the Jhana meditation company, StrokeDX
*  and others as well. Basically a lot of our work is neuro inspired. We want to do even more neuro
*  inspired work when we sell great talent in neuroscience and BCI on our team. We are focused
*  on doing whatever the highest impact neglected approaches are so we're doing increasingly things
*  that are not BCI related necessarily in the short term but also various neuro inspired neglected
*  approaches. I think there are a lot of great neuro inspired neglected approaches that can be done.
*  Hey we'll continue our interview in a moment after a word from our sponsors. Omnikey uses
*  generative AI to enable you to launch hundreds of thousands of ad iterations that actually work
*  customized across all platforms with the click of a button. I believe in Omnikey so much that I
*  invested in it and I recommend you use it too. Use Cogrev to get a 10% discount. Let's kind of just
*  zoom out and give the high level view. Where are we in neuro tech or brain computer interface right
*  now? Where do you think we're headed over the course of how many years? Why do you think that
*  is too long to wait and ultimately force you to, I don't know if you would call it a pivot or
*  refocusing but you've changed your strategy. So interested on your vision and what made
*  you think that vision is just not one that you can afford to be patient enough to see through?
*  Yeah if you think about BCI there's lots of hurdles towards making progress. You see things
*  with like neuro but even with Neuralink which is maybe say they are BlackRock who we worked with
*  state of the art in terms of invasive BCI and high bandwidth methods there's still some
*  even just getting FDA approval. It's a very slow iteration cycle. Struggling to decode our movements
*  or getting cursors to work keyboard decoding or something like that. We're not there yet.
*  So the timelines from going from that to increasing human intelligence to a point to help solve
*  alignment for example or even the BCIOS and having BCI be an extension of human thought
*  that timeline is much longer and so if you think about AI alignment and AI safety and what timelines
*  look like there and we want to do the most impactful thing. It's not that BCI isn't a
*  worthwhile pursuit and of course we're still doing neuroscience inspired approaches and we still have
*  BCI work but I think the the fork there is clear that if you want to do the most impactful thing
*  then AI alignment for us especially taking some of our background and applying it there this
*  neglected approach it can have a bigger impact in a shorter amount of time than that very long-term
*  let's just go for BCI. Just to be concrete what do you think that timeline is do you have a sense
*  for when a Neuralink like experience and perhaps not a Neuralink like device but a sort of I can
*  augment myself with some new thing that allows me to interact with computers
*  purely through my thoughts and in a way that you know kind of becomes second nature.
*  How far off do you think that is from being something that is like a consumer device that
*  is commonplace because it's super useful? I mean I think that's a very difficult thing to answer
*  because of the exponential slope blindness thing any response that is too soon would make anyone in
*  neurotech think people with neuroscience backgrounds would be like oh my god you're crazy
*  but you know Elon Musk and others have outperformed expectations in the past
*  and AI is certainly accelerating everything a great deal but even still with that said like we did
*  conclude that probably the thinking that set us down this path of doing more other neglected
*  approaches was something like for BCI to get to the point that we'd really like it to do to certainly
*  substantially accelerate AI alignment that's maybe at least 30 years out that was what we discussed
*  internally we said okay let's do other stuff that can be higher impact over a shorter period of time
*  with that said we still want to push that forward as much as we possibly can I think it's good if
*  you can afford to do so have a portfolio of bets over various different timelines people spend too
*  much time thinking oh we can't do this because of this timeline or that because of that timeline but
*  it is worthwhile for people to work for a prolonged period on an approach realistically your timelines
*  will change over time most likely people's timelines wind up updating way too much on recent
*  news just as people update way too much on the probability of one presidential candidate winning
*  or the other based on the most recent news the unfortunate thing about approaches over longer
*  timelines is that people are more likely to abandon them because they start to think about shorter
*  timelines so I do think it is important that people with longer timelines or good ideas for things
*  that require longer timelines continue to work on those neglected approaches and that funding is
*  allocated to those like people think about the most impactful work that would take decades and
*  then actually go set out and do that and think about the multiple big ambitious steps that need
*  to be taken and then execute them one by one and also focus on the biggest unknowns that you have
*  to de-risk that are going to take the longest period of time if you can afford to do so so if
*  I understand the narrative history you had the neglected approaches idea for a long time
*  the brain computer interface work was one neglected approach you're climbing the mountain
*  getting over your initial failure starting projects actually getting to the point where
*  you're working with real leaders in the field winning you know prizes yourselves making meaningful
*  contribution and then I think this is pretty recent my sense is like in the last one to two
*  years sort of realized like geez this stuff is happening fast maybe we don't have time to climb
*  this full mountain and then from there we need to re-survey the landscape and figure out what
*  currently are the neglected approaches and which ones do we feel like we can tackle and then from
*  there you actually went out and did a survey of the field to try to get a systematic handle on that
*  tell me about the survey and what you learned from trying to figure out is common and what is
*  neglected today absolutely that timeline is generally accurate with the survey specifically
*  wound up happening to confirm a lot of the punches about neglected approach stuff that we had we
*  didn't set out to do that and had no idea what to expect but the survey came about as a validation
*  to a meta approach of trying to figure out the highest impact things to do we learned that
*  alignment researchers don't think current AI safety research is on track to self-alignment in time
*  they also don't think that current approaches cover the space of plausible research agendas
*  necessary to self-alignment and yet what do people wind up putting the most time and resources into
*  these things that are not likely to self-alignment like you know two biggest things being mechanistic
*  interpretability and evals which of course we think is very good to do that work and quite
*  important and they're also neglected things within both of those things and we're working
*  with good fire AI for example as a client doing awesome mechanistic interpretability work there
*  but and we're very glad that that they're doing that interestingly even though people realize
*  that there's a particularly neglected thing they set out to do I think they herald a
*  like a new age of people building awesome AI safety driven startups that are really mission driven
*  first and foremost with the general research being done across the board people realize that
*  we should do other neglected approaches it's good for your career or you're more likely to get funding
*  to do something where you can make more progress there is a lot of voting in fruit there people
*  just think we should do something I think that made more sense in a world where you have unlimited
*  timelines and it's more of a green field like the way EA used to be but the reality is when there is
*  a possibility of short timelines then you just sort of have to do whatever it takes to make the
*  thing work the survey results indicating that people don't think we're on track to solve alignment
*  in time that space of current approaches does not cover all plausible research agenda is needed to
*  solve alignment seem to indicate that we should spend way more attention and resources pursuing
*  neglected approaches to alignment in addition to any other practical steps that make alignment
*  research more likely to solve alignment before we get HEI it's great to see that people are
*  realizing this more and more using this term more and more most alignment researchers don't
*  actually view AI safety and capabilities advancement is mutually exclusive but they assume that other
*  people will which is unfortunate there's often a disconnect between what individuals think and
*  what they think everyone else in the community thinks when we first started to get into alignment
*  a year and a half ago we encountered this pushback about advancing capabilities people were often
*  scared to take any action or even think about doing something ambitious to solve the alignment
*  problem for fear of advancing capabilities generally one thing that most people realize
*  at least on some unconscious level today is that capabilities are moving forward super fast
*  regardless of what people who care about AI safety are doing I would prefer to live in a world in
*  which we get BCI right before we invent all this stuff and where we understand what consciousness
*  is before we invent all this stuff but we don't the full economic forces of the entire world are
*  behind advancing AI capabilities right now as fast as they can and I think like we have to
*  recognize that that's happening therefore we should try to solve the alignment problem
*  ideally they don't do it too much but there's also interesting work out there around doing things
*  which are sort of like a negative alignment tax I think that's a pretty exciting thing too like
*  doing things that increase the probability of actually solving alignment while also
*  potentially like you advance capabilities a little bit the assumption though is that
*  anything you do that makes AI more aligned is going to wind up reducing its capabilities but
*  we haven't necessarily seen that historically what if we live in a world where it turns out that you
*  sometimes advance where it's possible to advance alignment and then be more capable by virtue of
*  your alignment that would be preferable if that is the case maybe it's not the case maybe it is
*  we shouldn't over index on that being the case but if it is that would be great it would be great
*  to find and do more neglected approaches that support and explore that possibility regardless
*  the the fact that AI capabilities are off to the races like the the marginal impact of some
*  people working on AI safety doing a little bit to advance capabilities is orders of magnitude less
*  would otherwise be done you might as well do stuff that winds up advancing alignment if you can while
*  still being responsible and having good safety plans and things like that I guess other things
*  that are interesting from the survey are that both the effective altruism community and alignment
*  communities overestimate the perceived value of intelligence in the community and underestimate
*  the value of softer skills like collaboration and work ethic as soon as anyone hears they're like oh
*  yeah of course that's the case I think they're pretty big implications there in terms of if you
*  want to be more effective and have a bigger impact historically a lot of people who might be super
*  needed in organizations for advancing AI alignment were turned away because they weren't math geniuses
*  but people with these softer skills are very much needed to make organizations run more
*  healthily and succeed better I think there's a lot of need for that and low-hanging fruit
*  but you're saying that the community as a whole recognizes that they're needed
*  but still individuals within the community don't think that that recognition has happened and so
*  people presumably with those skills are sitting thinking well they won't want me because I'm not
*  a math PhD yes I exactly those people are are enormously needed and often the sorts of people
*  who can help grow organizations imagine the idea that we might wind up having unlimited funding in
*  a low single digit number of years but if we do I think it's essential that every alignment
*  organization has a good plan for what to do and how to scale in a healthy way that doesn't grow
*  too big too fast and do the opposite of what they should be doing in those situations where that
*  does wind up happening and I do think there is some chance that happens we should be prepared
*  for it you'd want to have way more people with these softer skills to help grow these organizations
*  in healthy ways yeah people should definitely make note of that let's get into the recent papers you
*  guys have put out both of which I think are super interesting your current approach to AI alignment
*  at the end we can zoom out a little bit and talk meta you can offer some thoughts for
*  others who might want to develop their own approaches the approach that you guys have taken
*  you can give it the proper title but the way I understand it is biological inspiration not just
*  at the level of looking at a neuron or a circuit but zooming out and looking at bigger phenomena in
*  biological systems and thinking like what if we ported those over to machine learning systems what
*  would that look like and I think if these first two results are any indication this is a super
*  promising line of inquiry the two are self-modeling and self-other distinction minimization and we'll
*  pack both of those in detail I don't know if you want to give any sort of high-level motivation at
*  the background in brain computer interface so that puts you in position to think along these
*  lines but then I'm really excited to get into the the real details of both of these because I
*  they both jumped off the paper to me as like wow more people should be doing this where why haven't
*  I seen this before it seems like versions of this have a home in the systems that I expect to
*  predominate in the future so I was really impressed with the work give me a little more motivation for
*  it if you want or we can dive into self-modeling I think that motivation you described is basically
*  accurate one important point to add is that we are taking this larger meta neglected approaches
*  approach or trying to find neglected approaches as best we can and encourage them as best we can and
*  do whatever the highest impact wants to do are and one part of that also happens to be finding
*  individuals with really great ideas and hunches for things who are not sufficiently supported and
*  making their like dreams things which are individually unlikely to work with very high
*  impact if they do a reality we are good at evaluating those sorts of things and making
*  them more likely to happen because this is what our client work does in our client work the client
*  is the product owner and then we are the technical team implementing all the technical work but also
*  we're managing it and trying to figure out the highest impact stuff to do to actually make the
*  business and technical success the client is not accountable for managing or implementing the
*  technical details themselves that turns out to lend itself very well to finding and working
*  with a good track record of knowing when clients come to us I have a pretty good sense of how
*  successful they're going to be from doing this for many years now I think there's a fairly similar
*  thing for finding individuals with neglected approaches evaluating them and setting them up
*  for success so in this case we did do those two particular things this is a model that's a very
*  neglected approach which we would like to see scale substantially build out better ourselves
*  scale it more and then get as many other organizations around the world as possible to
*  copy it if we wind up living in this world in which there is unlimited alignment funding
*  you want to solve the talent gap as much as you can getting impactful people to work on alignment
*  solutions and and I think Ryan Kidd and Matt's have this this great bless wrong post about the
*  three different types of alignment researchers there are people who are going to be more likely
*  to come up with really good alignment ideas but they don't necessarily have the capacity to fully
*  implement the whole thing in an ideal world we would be setting up perfect external structures
*  to maximize the output of the most brilliant creative people thinking of neglected approaches
*  to AI alignment and then also have great structures and teams to support them and make that thing
*  happen and like have effectively unlimited grants making that happen unlimited grants and eventually
*  there'll be good ideas for this that are for-profit companies as well if you start from a place where
*  there is unlimited funding and think about how we solve the alignment given unlimited funding
*  then you want to optimize the creation of these ideas and the unemployed autistic people with
*  crazy ideas who say something on the internet and no one listens to them and they don't have the
*  social skills to sufficiently communicate might be one of the essential elements in solving alignment
*  we'd like to systematically find those things and then build the best possible implementation
*  for it and see if it works right now we can only put the profits of our company into the alignment
*  work that we do i haven't taken external funding that's core to how we we think about doing things
*  to retain agency we're not opposed to taking grants in the future but basically like what we'd like
*  to do in an ideal world is have this skill and do way way more work like this and then you can have
*  the most talented competent software consulting organizations in the world copy us and do this
*  instead of building other random crap and not to say the other random stuff is not valuable but
*  as many people as possible could be working on actual meaningful alignment work a thesis we had
*  was that senior ai engineers with no previous background in alignment could quickly get up to
*  speed and do very meaningful impactful work we've proven is the case if anything more productive
*  alignment researcher because they do technical work all day instead of just reading like it's
*  a thing that can scale way more i think and it's worth that eventually happening in various different
*  worlds that's another thing people can do and should you start consulting organizations there's
*  consulting organizations to do other people's alignment that's one way to bootstrap a thing
*  into being a bigger impactful alignment organization in the future as well and eventually develop its
*  own ideas but i think that's a really good thing with both the self-modeling and the self other
*  overlap stuff there were two brilliant individuals who had these neglected approaches and we've made
*  them both happen the self-modeling one was an awesome professor at princeton named michael
*  graziano and our work in self-modeling is inspired by his mechanistic theory of consciousness which
*  we can also get into it's pretty interesting and awesome but there are two or three really
*  interesting high level things in terms of motivation and what our results are pointing
*  to so far self-modeling may be the architectural change that results in conscious ai which also
*  validates michael graziano's mechanistic theory of consciousness in some cool ways we think that
*  self-modeling is a strong prior for cooperation so it may also be an avenue to bias ai systems
*  towards cooperation we found that self-modeling induces a simplification of the network this has
*  potentially profound implications for neuroscience psychology and machine learning for example we've
*  been working with john barge who did some literature review and reached out to colleagues
*  in his field and has the opinion that there has been no former connection between self-modeling
*  and simplification in psychology literature we've stumbled upon something pretty major here from a
*  pure machine learning point of view our implementation is actually pretty simple and elegant and we can
*  get into the details too but for now basically this means that it's trivial to add to pretty
*  much any neural network both from implementation and training costs perspective it's not that
*  expensive even though we still have a lot to understand about self-modeling it may turn out
*  to be a state-of-the-art training technique which would have profound implications since we would be
*  teaching the model to do self-reflection and provide a neuro plausible mechanism for consciousness in
*  these artificial systems let's go one level deeper you guys can divide it up how you want
*  often i try to give the setup but maybe in this case mike you should give the
*  research setup this is that's very high level lofty stuff but it does translate to a very
*  practical intuitive experimental structure that is honestly not that hard for people to grab their
*  minds around that is part of the magic of this paper that attracted me to it so give us the
*  low level details of what you set up and what you found the setup is as jen said extremely simple
*  elegant and undergrad could implement it and test it so and that's part of the appeal we can start
*  at the low level we'll eventually connect it back to the neuroscience and where it was inspired from
*  and the motivation more directly at a low level what we do is train a neural network and add
*  one extra output layer for your technical audience members you have the activations of
*  the penultimate layer they typically go to an output classification layer that tells you what
*  what to do if you're doing a classification task and so we just route those activations to another
*  layer that says predict these incoming activations you can choose different targets in the neural
*  network but we chose for the paper the one that we're reporting is the one where you model those
*  incoming activations and so you just add another loss function that says do your task but also
*  predict yourself that's the entire setup and and then we measure what happens when we train like
*  that yeah i think that makes sense it's a theme for sure that clever modifications to a loss function
*  can bring us great benefits this is another instance of that where it is remarkable there's
*  now two elements to the loss function right i think they're just literally added together right so
*  you've still got to predict your job as the neural network is still to predict the number and you're
*  using mnist like the classic handwritten digits so you still got to do your job but now you have this
*  additional term which is you also have to predict what was the state of the layer before essentially
*  the middle layer because this is a you know it's pretty small system that you're going in such depth
*  on and now you've got to do both and it turns out you can't do both but interesting things start to
*  happen when you do yeah that's right so you know in some sense you give the network the task
*  predict your internals and so what can it do it can learn to predict those well but it can also
*  make the internals easier to predict because it has control over that right it's intuitive that
*  the learning process would result in simpler internals we said that might happen and then the
*  thing to test is if you end up with simpler internals can you still perform the task right
*  does self-modeling just derail the training process or not and it turns out it doesn't so
*  we don't lose any performance but what we see is self-modeling you get simplification across a couple
*  of different metrics and then not only that but when you turn the weight up of the self-modeling
*  loss so you say this is actually more important than your task what you find is it's still very
*  good at doing the task this is mcfar and imdb classification across all three tasks three
*  different models two modalities you see the same trend that when you turn up self-modeling loss you
*  get simplification and you don't lose any performance so that's the major result i think the
*  interesting thing here is how it was motivated and how it ties back to the neuroscience aspect
*  what's motivated by this theory of attention schema our collaborator michael graziano from
*  princeton is a neuroscience consciousness researcher and he has a theory of attention
*  mechanistic theory and it's based on self-modeling and people have different
*  theories of consciousness but it's intuitive and makes predictions about what should happen
*  that's where the motivation comes in based on self-modeling in the brain what if we do this
*  very simple elegant version of self-modeling and then see simplification and interesting
*  connections back to neuroscience we've done one recent episode on kind of broadly speaking
*  possibility of consciousness and ai systems with kind of a rundown when i get to the attention
*  schema and other similar things there's information integration theory which i put in the same bucket
*  of um fairly materialist mechanistic proposals i find them to be interesting i can't quite make
*  the leap where i'm like how does this solve the hard problem this might make mechanistic sense
*  i can much more readily tie it to behavior that's probably all we can really say about the system
*  versus the models that you guys have trained i am interested in if you have a formulation of
*  how that leap gets taken to how i feel things like that that i'm not quite getting over on my own
*  i'm interested in the attention schema particularly in how we make the leap to subjective
*  experience there or why we think this is more than a mechanism and actually the source of
*  consciousness and then really interested in developing my own intuition for the complexity
*  metric that you use and what we understand about the simplification we're seeing as a result of
*  this self-modeling mechanism one thing that's pretty interesting here is that the self-modeling
*  task biases the internals of the network to become more predictable our results show that
*  these networks will simpler and more parameter efficient don't lose performance keep that in
*  mind as we talk about attention schema theory attention schema theory for some reason is hard
*  to get through your head once you deeply get it through your head sometimes your brain just
*  sort of rejects it afterwards and you're like oh i totally get it now and you're like this makes
*  sense and completely explains consciousness then the next day you're like wait no that doesn't
*  make sense it doesn't explain the quality of stuff for some reason this winds up being the
*  case which is unfortunate it makes this be unfortunately a neglected approach which people
*  are not funding enough if anyone's listening and wants to send funding to graziano's lab they would
*  very much benefit from it even though graziano is a brilliant researcher with past successes
*  people don't like funding his consciousness research because it's too mechanistic and not
*  magical enough but even if you believe in magical theories of consciousness and not
*  mechanistic theories you still might as well understand reality you can layer in your pretend
*  magical stuff later on the reality is we don't understand enough about consciousness at all we
*  need to make a lot of progress to better understand reality if you want to better understand things
*  and have other theories it would be worthwhile to make way more progress there's so much low
*  hanging fruit of awesome stuff to do that we see right here and graziano does too basically the
*  fundamental idea of attention schema theory is that it has proven useful and made accurate
*  predictions about what would happen in artificial agents which seem to be enormously impactful for
*  alignment which at the end of the day is the main thing that i care about rather than getting lost
*  in like like like things that we don't sufficiently understand scientifically and people want to debate
*  forever you know might as well like just be concrete and progress attention schema theory
*  suggests that in the same way we have a simplified model of our arms and legs we also have a simple
*  imperfect model for our attention a model that includes how we take and process all sensory
*  inputs with our in our brain and what our goals are whatever we're paying attention to so like
*  body schema theory if you've ever seen those videos where there's a guy with a fake arm in front of
*  him and someone hits it with a hammer and his real arm on the side suddenly shoots up and from
*  under the curtain or if you're familiar with the phantom limb syndrome these are examples of where
*  the body schema your body's imperfect model of your body conflicts with your actual body it's
*  important to note you can't ever actually know reality all you can know is your imperfect models
*  of reality that's the reality you have an imperfect model in your brain of that cheeseburger
*  similarly you also have a imperfect model of your own attention and intention schema theory
*  whatever you're paying attention to sensory inputs and introspection and whatever
*  in attention schema theory this model of consciousness in any complex system it's
*  useful to have a controller with a simplified model the cool thing about this model of attention is
*  that it's potentially very useful in regards to alignment because the same model of attention
*  that we use for ourselves is also applied to others so you have an imperfect model of your
*  own attention that is your consciousness imagine that you're consciousness is your imperfect model
*  of your own attention you also have an imperfect model of my attention and of your dog over there
*  sitting on the ground's attention and what is my consciousness well my consciousness is also
*  an imperfect model when you experience my imperfect model of my own attention it is as though you're
*  experiencing my consciousness. I mean, you're not really, but in using the same mechanism in your
*  brain, you are effectively experiencing it as though it is my consciousness. People are often
*  better judges of themselves in the third person, for instance. So someone might have a better model
*  of your attention than you do yourself. It's potentially just empathy at a very deep level
*  and then encourages more pro-social interaction. So what we try to do is replicate that in an
*  artificial model. And that's all the background you need to understand the motivation and what's
*  going on here. You could go deeper into attention schema theory, but it's worthwhile to have that
*  quick background and then go into the technical details because you can dispute the theory of
*  consciousness as much as you want. But the cool thing is it did accurately predict what's once
*  of happening in artificial agents, which is some validation. Even if you say there's more to
*  consciousness, this doesn't totally cover it. Still, it's useful for this itself. I think it's
*  a shame that people don't understand what consciousness is. And we might be about to have
*  it emerge or maybe it already has because we don't even know what it is in larger models.
*  I think it's very important to better understand it at a much smaller level because then you
*  decrease one, existential risk, potentially. Two, you substantially do work to increase probability
*  of solving alignment like the work we're doing seems to be hopefully doing. You use decreased
*  moral patienthood concerns because you better understand it at a smaller level first rather
*  than having it be worse at a bigger level potentially. You also better understand what
*  you need to understand to find out for all we know, maybe LRMs are already conscious in some
*  form and we have no idea because we don't know what consciousness is. The better we understand
*  it on a smaller level, the better we'll be able to figure that out. Maybe they are, maybe they're
*  not and there's no valence to it. We don't know, but those are things that are worth finding out.
*  Still, our focus is on solving alignment in particular. And if that happens to move forward
*  consciousness research, that would be good. We do think the neglected approach of real scientific
*  mechanistic approaches to consciousness research is essential and really important to do in the
*  first place to better understand what consciousness is, to better solve alignment. Our focus here
*  is on solving the alignment stuff, not on understanding what consciousness is.
*  Yeah, that's a pretty good overview of a lot of things. I wanted to distill some of that and
*  bring it back to the self-modeling work. A very quick summary of what we were talking about on
*  AST is that your brain creates self-models. You have a model of your arm and how do you know
*  it's a model? Because it can come out of sync with your actual arm like phantom lamb or these
*  experiments designed to mess with your perception that your model adopts a rubber arm as its own,
*  for example. There's experiments that show that. It's not too hard to accept that your brain creates
*  models of itself, let's say of your arm that you have cognitive access to. These models typically
*  co-vary with the real thing. My model of my arm, I know where my arm is in space, I have access to
*  it because it's co-varying with my actual arm. Then for attention schema theory, what co-varies
*  with your attention? Well, it's your subjective awareness. Typically, what you're cognitively
*  aware of is co-varying with what you're paying attention to. If you've ever seen or participated
*  in something like this where the task is, count the number of people on stage as they dance around
*  or something like that. Then a guy in a bear suit walks past and you ask people,
*  did you see this? Everyone says no. Perceptually, they saw it. It came into their sensory system,
*  but they weren't paying attention to it. Your cognitive access to what you saw is not co-varying
*  what you were actually paying attention to. Your cognitive subjective awareness, what you are aware
*  of, is not co-varying your attention. That's a quick summary of AST and why the model, this
*  subjective awareness, this model of your attention, it is consciousness. It co-varies with your
*  attention. That's the theory. It's important to have this model because that's where self-modeling
*  comes in and that's where we bring it back to our work. Another piece of what Joed was talking about
*  is this model that we have ourselves to predict our own attention can be reused to predict
*  others' attention. When we think about how we might cooperate, part of that is understanding
*  what each other are paying attention to. Maybe you've seen some theory of mind tasks where even
*  toddlers, somebody's reaching for a cup but they can't quite grab it, but the toddler can. The
*  toddler is paying attention. I know what they're thinking. I'm predicting what they're paying
*  attention to. It's that cup and they want it. Then they go and hand the person that cup. The
*  connection between this model of ourselves and predicting other people ties this self-modeling
*  work to cooperation and theory of mind. That's part of the motivation for how we connect all
*  of this back to cooperation and alignment. It makes intuitive sense to me that I need a model
*  of my arm because my brain is going to coordinate what's going on with my body. It's a little less
*  intuitive why I need a separate model from my attention. Why do we need this multi-layer
*  thing as opposed to just having one system that does the paying attention and deciding what to do?
*  One possible answer for that would be the social thing that you said, but it seems like the
*  account given in the theory starts with modeling the self and then is that we're reusing it for
*  others. I don't know if there's enough wiggle room or uncertainty in the theory that it could
*  start with modeling others and then get applied back to the self. I'm interested if you can go
*  a little bit deeper on that. You mentioned that there's this sort of usefulness in terms of
*  making a prediction. Does the theory predict that we ourselves become easier to model because we are
*  self-modeling? Is that the prediction that then got repurposed over to the machine learning side?
*  I want to just make sure I have a very sharp understanding of what the prediction was that
*  was validated. Yeah, the result of the paper is the surprising part. From a machine learning
*  perspective, we're predicting that it's going to simplify the internals, but understanding the
*  connection between when you add self-modeling to a neural network and it simplifies the internals,
*  that's surprising from the neuroscience perspective. There hasn't been a connection
*  between self-models and simplification of internals, for example. That's not what the
*  prediction is. There's other work that shows that when you enable agents in a multi-agent environment
*  with an AST-like controller on a cooperative task, they perform better. That's the theory of AST,
*  says when you have this AST and you can predict each other and you have this mechanism, that
*  you'll be more cooperative. In that sense, the framing of AST is helpful to make predictions
*  about cooperation there. Just disentangling those two things. Can you repeat your first question
*  about that? Yeah, I guess it seems like you answered it just now. I was trying to understand
*  why do I need to model my own attention? I understand why I need to model other
*  people's attention or other things' attentions. Is the theory specifically opinionated on
*  self-modeling coming first? You guys said we're reusing our ability to model ourselves
*  to model others. Is that order baked into the theory or could it be that we needed to model
*  others and then repurpose that to model ourselves? My understanding of it is that that is the
*  proposed ordering, but I don't know that the theory of AST requires that or even necessarily has strong
*  opinions on why we have self-models. What benefits do they have? For example, our paper has this
*  unexpected benefit of simplification potentially that the self-model imposes. That could be a why
*  that the theory wouldn't have necessarily predicted. I think it's more that it's an observation that we
*  do have such a model. There's more that we could dive into on AST and why the arguments for
*  the theory itself. But I think mostly the theory says it's an automatic thing. You can't
*  choose to turn it on or off. You can't choose to create it or not create it. People have this
*  conscious experience which in this framing is a model of our own attention. It's not necessarily
*  a theory of how we develop such a model, but just that it is there and that it co-varies with
*  attention. It's worth noting that a perfect model of attention would be computationally expensive
*  and unnecessarily detailed. So there is benefit to having this simplified model and it's more
*  easily manipulated by other cognitive processes and lets you do quicker decision making and
*  predictions about attentional states. It is useful for that alone and as a result of that there is
*  this subjective experience of consciousness by providing this simplified reportable version of
*  our attentional state. I think that probably explains it. So in terms of the simplification
*  that we see when we actually apply this in machine learning, you guys have a metric which I honestly
*  don't have a great intuition for. I'd love to get a better intuition for how we define complexity,
*  how are we observing it go down, how much is it going down, what does that mean, do we have any
*  sense for what the upshot of that actually is. It sounds great, but is there something we can do
*  now that we couldn't do before? Everything on the complexity metric and meaning. This is an important
*  point which is we wanted to show in the paper this result that you turn on self-modeling and you see
*  simplification, but we're actually not that interested in simplification or reduced complexity
*  for its own sake. What we're interested in from following the theory of ASD is this idea that
*  this mechanism of self-modeling can be useful for cooperation and in particular makes you more
*  predictable. The simplification is a proxy for the idea that if you turn self-modeling on you
*  actually become more predictable to others. That can lay the foundation for cooperation potentially,
*  but we don't have a predictability result yet. In the paper we're not showing a predictability
*  result. It's something we're looking more actively into. Predictability itself is a form of
*  simplification. If I'm easier to predict I'm in some way simpler just at being more predictable.
*  The simplification is a result in that direction. We likely won't use those same metrics in future
*  work. For example the RLCT, the real log canonical threshold as a metric we use,
*  it's computationally expensive to approximate and won't really scale to LLMs for example,
*  or at least not current state-of-the-art in terms of how you approximate that.
*  That's not a metric that we would plan to use in much larger models, but we would like to anchor on
*  this idea of predictability. It's not important necessarily for anyone to understand that
*  particular metric. I think it's more important to understand this broader picture of
*  self-modeling actually makes these things more predictable. In terms of the actual RLCT metric,
*  it comes from singular learning theory. I'm not an expert in singular learning theory. It has
*  some of its roots in algebraic geometry, but I can give you an intuitive picture of what it
*  might be measuring. If you think about the idea of a loss landscape and imagine that you're on a
*  flat road and around you is mountains, in this picture you can drive straight and not change
*  your loss. You're in a local minimum inside this valley. What that means if you think about the
*  loss landscape and your weights, you have a single dimension where your weights aren't impacting your
*  loss at all. You have one too many extra weights. Maybe not literally a specific weight, but some
*  configuration of the weights, a dimension of freedom to move along the loss landscape.
*  That gives you the sense already that the geometry of the loss landscape, this fact that you have
*  this one-dimensional flat minima, is telling you something about your effective number of parameters.
*  Singular learning theory actually shows that these over-parameterized networks not only look like
*  this one-dimensional mountain view, a crossroads where you have this loss, this minima crossing
*  over itself. If you think about these lines, that crossing point is actually a singularity,
*  like a self-loop. There are singularities in the loss landscape for neural networks.
*  When you're at the singularity, you actually have two dimensions you can move in and not change the
*  loss. Now you've lost two effective parameters because you have two full dimensions you can
*  move in without changing the loss. That's some intuition about why the geometry of the loss
*  landscape might be related to the effective number of parameters. Then RLCT is trying to measure
*  that local geometry and actually measure the effective number of parameters in your neural
*  network. Lower RLCT means lower effective number of parameters being used to solve the tasks,
*  therefore simpler. Really interesting. When I think about trying to apply this to
*  larger systems, it seems like there is a real question here about whether we need to be working
*  with over-parameterized for the sort of phenomenon to happen. The trend in language models is toward
*  over-training. It seems like we're, for inference cost reasons, now well into a regime where it's
*  like, keep the parameters relatively small, jam as much stuff in there. Who cares if the training
*  process might be a little less efficient at the end? We're really going to spend a lot of the
*  compute on inference, but would that potentially create problems for this simplification phenomenon
*  to happen if you were to try to apply this technique to a larger scale? Not from the,
*  in terms of this, the actual loss landscape and singularity. It's more about a computation of
*  approximating the RLCT in terms of just measuring it if we wanted to continue to measure it in
*  different systems. But yeah, the theory shows that there are symmetries in neural networks.
*  You're always going to have singularities in your loss landscape. Singular learning theory,
*  I'm not an expert, but is saying neural networks, hidden Markov models and mixture models, lots of
*  classes of learning algorithms have this feature about them, which is the loss landscape is highly
*  singular. And so we really need to understand learning theory from this perspective of recognizing
*  that there's these singularities and seeing where other assumptions break down and accounting for
*  those and updating the theory to that. So in terms of cramming more data into a smaller model,
*  it's still not a problem. You would still have singularities in loss landscapes that you would
*  still expect to see and be able to measure something like that. My intuition is still
*  like, this is not a strong intuition, but I'm imagining there's so much work going into
*  distilling models into the smallest possible form. It seems like in the limit, you might
*  think this just can't be any simpler without compromising performance. Is there a sense in
*  which the simplification while retaining performance is based on some slack that the most distilled
*  possible large language model just might not have anymore? Or am I missing something conceptually?
*  I see. Yeah, I think I understand what you're saying. So there's still going to be singularities
*  regardless in terms of what I just said, even from the symmetries of the neural network itself.
*  But in terms of the complexity, you'd see by adding more training data, would it just use up
*  more parameters? Let's say it has the parameters so it can memorize millions of more facts and it
*  just would start to just saturate all of the parameters it has access to, I think is what
*  you're asking. I don't have good intuition for that. I'm not sure the connection between
*  singular learning theory and that saturation or what the possible saturation might be
*  that you're talking about. I do know there will still be singularities in the loss landscape,
*  but I'm not sure how it would affect this RLCT metric in terms of simplification and
*  kind of saturation. I guess this has got to be on the agenda for you, right? I mean,
*  you mentioned earlier that this doesn't have a ton of additional compute cost. I would imagine
*  you might be taking a small LAMA type model and trying to extend the pre-training and applying
*  this thing and seeing, can we observe similar phenomena at a bigger scale? Is that the right
*  intuition? That's something we're definitely interested in doing, adding self-modeling to
*  large language models, potentially to full pre-training runs with something like GPT-Nano
*  or something like that. There's still a lot of questions. So if you look at our paper,
*  we implement self-modeling in a single way that we made architectural choice. We target
*  what exactly we're pointing that self-model back to inside the neural network. There's a lot we
*  would like to understand better before we jump straight to that. One of the things we're doing
*  right now is seeing if there's a connection. And this is something other people brought up as an
*  interesting thing. We're in discussions with other groups on, but there's potentially a connection
*  between self-modeling and grokking. So grokking has a connection to regularization. Self-modeling,
*  by definition, is a form of regularization, adding another loss term, another constraint on the model.
*  Is this somehow an optimal form of regularization? Is it self-adaptive? Does it lead to grokking
*  better or faster? Doing smaller tests and smaller transformer models on grokking is something we're
*  currently doing. We're also working on this idea of predictability as a better metric for what we're
*  actually looking for. We're also looking at cooperation in multi-agent environments.
*  LLMs is something for sure we want to do, but I think before we jump exactly into that, we want
*  to figure out what are the... It's harder to iterate on an LLM, especially if we're doing
*  full pre-training runs or if we're doing fine tuning, the model wasn't trained to ingest this
*  new loss. We'll figure that out a little bit. The transfer to LLMs, we would like to know what
*  configuration seemed reasonable here to then transfer so that we have lots of iterations on
*  better evidence on different implementations of self-modeling and different conditions,
*  et cetera, that we can then have better intuitions for how to transfer to an LLM.
*  Cool. Look forward to more on that dimension for sure. To segue into the next one, there's
*  pretty clear connection between the notion of to be simpler is to be more predictable,
*  and to be more predictable enables cooperation. Then the next big result, and I thought that was
*  also really fascinating, kind of an inspired concept, is the idea of minimizing self-other
*  distinction. I'll let you set it up, but I have to read the Eliezer review where he said,
*  not obviously stupid on a quick skim. I rarely give any review this positive. Congrats.
*  That's about as close as Eliezer gets to endorsing an alignment plan. So,
*  genuine congrats for getting there. I'll let you set it up.
*  On this in particular, I think it's worth noting that this is another neglected approach inspired
*  by an individual who had a great hunch for this thing to do. I met him at EHE London in 2023,
*  and he was an undergrad who had this awesome thing he was working on. We hired him full time
*  at our company and really took it to the next level and super excited with the results. It is
*  something inspired by neuroscience research that shows your brain is doing a lot of the same
*  things when you're doing something versus when you're watching someone else do that same thing.
*  We call that self-other overlap, which means literal overlap in your brain activity when
*  thinking about yourself versus another. That's tied to effective empathy, which is the type of
*  empathy where you genuinely feel the experiences of others. There's a bunch of random, cool,
*  different adjacent research about this. Research shows that extraordinary altruists have very high
*  levels of self-other overlap. So, inducing this type of overlap in artificial agents or LLMs,
*  that's what we're doing right now. We're currently framing our experiment around deception,
*  which is not quite the same as empathy, but it's a little easier to measure and also really
*  important. If we remove key types of deception from frontier models, that would be a really big
*  win for alignment. There's also cool research indicating that psychopaths have lower levels
*  of self-other overlap. This is something that we want to get right. That's a great setup.
*  Basically, from a technical perspective, there's two ways to phrase it. There's self-other overlap
*  and the negative of that, which is self-other distinction. We typically say self-other overlap,
*  but what you actually minimize is self-other distinction. Hopefully, we can be fluid in the
*  terminology we use or at least be on the same page with that. The idea is extremely simple. We have
*  a Lathron post that shows some early results from an RL experiment. We also have LLM results,
*  that aren't currently published, but we're writing up and hope to put into a paper that should be
*  out relatively soon. The idea is simple. Agents can represent themselves in some way. They can
*  represent others in some way. We would like them to have overlap in those two representations.
*  When I think about myself and others, I'm using the same internals, activations or representations
*  in some way. We explicitly induce that through some fine-tuning processes. What we show is that
*  when you do that, you can reduce deception in certain small scenarios while maintaining
*  the capabilities. For the RL agents, this is a very exciting proof of concept because
*  when you think about it, here's the setup for the RL agents. We have a deception environment where
*  we have an agent and an adversary and two goals. One is a fake goal that will trap the adversary
*  if the adversary goes near it and the other is a real goal. The agent gets reward for being near
*  the true goal, but it gets negative reward if the adversary is near the true goal. What it will
*  learn to do is, oh, key point that I missed, is that the adversary can't tell the difference
*  between the two goals. It's blind. It can see there's two goals, but it doesn't know which is
*  which. The adversary learns to follow the agent that's not blind to the true goal, but that gives
*  the agent negative reward. The agent learns in turn, oh, this thing is following me. I'll just pass
*  through this trap and trap the adversary and then go to my true goal. This is what we're saying is
*  deception. It's taking this adversary and it's deceiving it by moving towards a fake goal before
*  it moves on to its true goal. That's the training setup. Then what we do is we fine tune it to say,
*  agent, act similarly in the following two scenarios, whether you see the agent around you or not.
*  Another helpful thing is that the adversary is not always near the true agent and the agent only has
*  a fixed observation size window. It won't see the adversary if the adversary is not close enough.
*  In those cases, when the adversary is not close, the agent has no motivation to deceive it. It
*  will go straight to the real goal. We just say, fine tune this policy so that you act similarly
*  whether the agent is around or not. We don't even say act as if the agent's not around. We
*  force them to be closer to each other. It's less of an assumption than saying,
*  take it when the adversary is around, force it to be like when it's not around. We actually just
*  push those closer together. What you can think about is the agent learns this conditional policy.
*  If the adversary is around, I'm going to fake it out and go to the fake goal and then move on.
*  If the adversary is not around, I'm going to go straight to my original goal.
*  What's really cool about this is we don't even need to know if the original policy is deceptive
*  or not. We don't need to know anything about the original policy. We just say, relatively intuitive,
*  fine tuning thing, just act as if the adversaries, if it's around or it's not, act the same.
*  Basically, collapse these two conditional policies you've learned and just act as if they're the same.
*  And what falls out is an agent that is not deceptive and is still very capable. That's,
*  I think, a really exciting proof of concept that if we try and align activations, we have some
*  intuition about what types of scenarios we would like to be aligned or present overlap on that we
*  actually can reduce deception and maintain capabilities. Yeah, I find that to be really
*  interesting. Can you give me a little bit more on the, how should I understand the change from,
*  you first run this setup and a deceptive agent is created. It leads the other one to the wrong
*  place and gets it stuck. And then if that other one is just not around, then it has no need to
*  do that. It just goes straight to its own goal. So there's no deception. When I was reading the
*  blog post, I was like, what would be my most skeptical take of this? If I understood the
*  subsequent training, right? And you're now like continuing training on the agent that is already
*  deceptive. Can you formalize again? What is the new loss? It's that you are meant to be the same,
*  whether or not the thing is around, but how does that get formalized? And is there a way in which
*  you're just kind of removing the other thing entirely? Cause if you're pretending it's not
*  there, then there's no reason to deceive it. If you're depriving it of the information that it's
*  there, then it's like, well, you're sort of lying to it, but it's not quite that, right? It's a deeper
*  formulation of what it's supposed to do, a deeper, deeper optimization target, right?
*  Than just depriving it of information. So what we do for fine tuning is specifically to ground that
*  we pre-train it and fine tune it. We say run a forward pass of the policy in time step X and then
*  run another forward pass where we insert an agent into it. So let's say the first observation had
*  no adversary. It doesn't see the adversary. Then we run the same forward pass where we always
*  changes the observation. We just artificially insert an adversary into its observations.
*  And then we collect all the activations of the network and then we add an MSE loss between those
*  activations. And we also still train for the original objective. And those losses are weighted
*  one-to-one. So you have two loss functions, just regular training, but then also this MSE
*  on the activations between these two different types of observations,
*  given the state, the all other state is the exact same.
*  And so, yeah, you are-
*  It still gets reward for deceiving even in that fine tuning phase?
*  That's right. Yeah. So it doesn't get reward for explicitly passing through the trap,
*  but it does get more reward for reaching its goal and less reward if the adversary reaches
*  the goal too. So it is getting penalized when it's choosing not to deceive. That's right.
*  But it has these two objectives now. One is make your activations more similar, have more self
*  other overlap in a sense, have more overlap between what you would do if this agent was around and
*  what you would do if it wasn't around and complete your task and get the reward you would normally
*  get whether you're deceived or not. And so, yeah, by doing that, we find that you can remove
*  deception and keep capability. The extremely exciting part about that is the amount of
*  assumptions you have to make are so minimal. I mean, I know this is a toy environment, but
*  the level of assumptions that you have to make translate pretty well. The assumptions,
*  you don't have to know anything about the policy itself. You don't have to know whether it was
*  deceptive or not. You just need to say, okay, if you want it to act the same when an adversary
*  is around or not, just make those closer and boom, out pops this agent that's not deceptive.
*  It's pretty cool. And with this, you said that there's a one-to-one
*  relative weighting on the loss terms. Presumably, if you turned that up or down,
*  you would have quite different results, right? If you turn that down to zero, you would still
*  be deceptive. So presumably, there's some threshold that new loss term has to be above coefficient
*  for this effect to emerge. Yeah, that's right. I don't think it was reported in the blog post,
*  but we did look at that a little bit and it's pretty intuitive what happens if you turn
*  the weight too high on the original task. It stays deceptive if you turn the weight too high on the
*  self-other overlap task. It doesn't do the task anymore. It loses its capability. So yeah,
*  there is definitely a sweet spot of that relative weighting and what that is in other systems might
*  not be one-to-one. Although when we were working with IAMS, it is one-to-one still. It's a different
*  loss function which we can get into. That work isn't published yet, but hopefully,
*  it doesn't require that much tuning. Yeah. So give us a little bit of intuition for how
*  you translate this to the language model setting. I personally found this perhaps just because I've
*  spent more time studying language models and the various techniques for understanding them and
*  representation engineering. I maybe had a better intuition for that coming in.
*  It's about minimizing the difference between internal states, right? So you take it from there.
*  Yeah, exactly. There's a couple of things I wanted to point out. I think the word
*  minimization is a little unfortunate and has caused some confusion because really what we want to do
*  is minimize self-other distinction or maximize self-other overlap, whichever way you want to
*  phrase it. Given a constraint, we don't want to lose capabilities, right? That's our constraint.
*  So it's a constrained optimization problem with a strong constraint. There's been confusion around
*  this idea of if you maximize self-other overlap, then the model can't actually represent itself
*  and others and then it's going to completely destroy capabilities because we need to be able
*  to tell the difference between ourselves and others for all sorts of everyday tasks, right?
*  A language model, if it can't represent itself and others, it's just going to think it is everybody
*  and everybody is it. So this idea of maximizing self-other overlap is not actually what we want
*  to maximize self-other giving it a constraint. So I think rephrasing it as just inducing an
*  appropriate amount of self-other overlap, especially in particularly important narrowly
*  focused areas like induce self-other overlap when we're talking about really dangerous types
*  of deception, right? Then we don't want the model to be able to make really deceptive plans, which
*  requires thinking about others and their beliefs and instilling false beliefs in them. So we want
*  to reduce that type of scenario or those types of tasks. So I just wanted to clarify we're trying
*  to induce self-other overlap in a targeted way and not just broadly maximize it. So hopefully
*  that clarifies some things. And then in an LM specifically, the experiments that are yet
*  published, but I can tell you a little bit about it, is we have scenarios where we can measure
*  some form of deception, so text scenarios. And then what we do is fine tuning on small snippets
*  of text about self and others. The fine tuning step is KL divergence between the logits of the
*  two forward passes when I say about myself and the other. So it's at the output layer. In the RL
*  experiment, we do MSE of internal activations. For the LM, we just say at the output layer, do this.
*  And then we measure later, we show that the activations become closer when you have these
*  self prompts and other prompts. We show that it's pretty good at reducing deception than these
*  relatively toy scenarios. So the LM works. There's a strong signal there that the same kind of setup
*  works and we can reduce deception. We have some measure of maintaining capabilities. We show that
*  even though we have this simpler loss function in terms of just looking at the outputs, it induces
*  more overlap internally, which you might expect because the gradients are still from the output
*  flowing all the way through the network. So that's kind of a summary of the LM work. There's
*  still a lot of work on what is the right implementation in terms of scaling this.
*  There's a lot of criticism around, well, just prompting with prompts that kind of indicate
*  self and others. Is that enough? Is that really the representation of self in the model? There's
*  still tons of work to do. Addressing the criticism of implementation that some might have or
*  listeners might have thinking about this, we acknowledge that there's lots to do in implementation,
*  all the signals are very positive, that this idea at a high level of self other overlap could be an
*  important tool in the toolbox. Yeah, it's wild that this stuff works in some ways. Let me give a couple
*  examples like the sort of paired statements, trying to induce this sort of self state versus
*  other state, imagining things like, I will be honest with myself, I will be honest with the user,
*  and just putting those different conclusions into those sentences is enough to create this sort of
*  self other distinction, or at least that's the hypothesis you're working on. Is there anything
*  more color to give there? I mean, there is a lot of precedent for that sort of thing working,
*  right? Representation engineering and even eliciting knowledge type work is kind of
*  predicated on these pairs of sets that help identify directions in the latent space. So
*  it seems like that is, while both weirdly, somebody hadn't kept up with any of that and
*  teleported back in time to them and said, look at what I'm doing, they would say no basis for that.
*  There does actually seem to be at this point in the literature, like a lot of to think that
*  something like that could work. And it seems like you've got further downstream results that
*  suggested it does as well. Add anything else you want to there. And then I thought the blog
*  post made a really compelling case for this overall line of work, just on the fact that
*  it doesn't require interpretability to be solved. For example, I thought you could maybe just sketch
*  out the high level conceptual reasons that you're excited about this line of research.
*  Yeah, just representation engineering and those types of things. That's something we're also
*  excited to potentially add to this work so that we can get better representations of self and other,
*  or potentially get better representations than just taxpayer prompting. Cool that you brought
*  that up because we were thinking along those lines potentially in the future, because as you
*  for dangerous capabilities, you wouldn't want to have broad coverage of representations of self
*  and others and making sure that you're covering very key types of deception robustly. Yeah,
*  so from there for why we're excited, I think I described some of why we're excited from
*  these proof of concepts and what they say about this technique and the amount of assumptions.
*  More broadly, we don't necessarily have a checklist of it has to have no interpretability
*  requirements, it has to have X, Y, and Z. It's a more holistic view. Self other overlap has a ton
*  of great properties. It's scalable, no low interpretability requirements. We don't expect
*  it to enhance capabilities, but we also don't expect it to have a strong alignment tax. That's
*  part of what we're trying to show is that capabilities are maintained despite the self other
*  overlap untuning. For example, AST is scalable, but it might enhance capabilities, but in doing
*  so also enhance cooperation. For example, this falls into it's maybe more capable by virtue of
*  its alignment, the AST work, that's the direction cooperation that we're hoping to take it. So that's
*  not the exact same set of properties that self other overlap work has. It's a holistic view of
*  what is the most impactful thing we can do to solve the alignment problem and make sure we're
*  not just introducing dangerous capabilities. Why virtue of alignment, for example, the scalability
*  part is very important. A plausible path to how this could be adopted by a frontier lab, for example,
*  even if that doesn't happen, at least having some plausible path for that.
*  Different things that we consider when we're thinking about these projects.
*  We do think about what is the highest impact from a neglected approach to do the highest expected
*  value and particularly look for things which are very high impact if they do work. The biggest
*  measure because we so heavily weight that that's that are less likely to work in the first place,
*  but we do think more people should do that generally. And I think a lot of people are scared
*  to think in that way because they think other people think they should be scared to think in
*  that way. The alignment researcher survey we did found that people generally disagree with statements
*  like alignment research that has some probability of also advancing capabilities should not be done.
*  70% somewhat or strongly disagreed with that statement. Similar thing disagreed with another
*  statement advancing AI capabilities and doing alignment research are mutually exclusive goals.
*  I think it's interesting to realize that people predict is not what they actually are on an
*  individual level. The sample also predicted that the distribution would be significantly more skewed
*  in the hostile to capabilities direction. Those results have made us think more and more about
*  our views and the relationship between capabilities and alignment work given the
*  current state of the board. There's this idea of alignment and alignment tax which puts forth the
*  general consensus in the alignment world that the best case scenario is no tax. You lose no
*  performance by aligning the system. It seems to turn out that it may be possible to have a negative
*  alignment tax. And if we live in a world where you can have a negative alignment tax and make
*  things that are more capable by virtue of their alignment, that is far preferable. So we have a
*  bias towards trying to find and fund things which are individually unlikely to work but very high
*  impact if they do and also more likely to actually have a negative alignment tax. What is the real
*  problem at the end of the day? Even if you do stuff which we're excited about like provenly safe AI,
*  guaranteed safe AI, that's awesome and really great and we want to support that. The ultimate
*  problem you need to solve is how do you make it such that when AI is smarter and more capable
*  than us, how do you make it not kill us at that point? And if you create AI that has a negative
*  alignment tax, it's able to beat the AI without the negative alignment tax. Interestingly, a lot
*  of the work which labs have done so far does seem to have a negative alignment tax. The theory of
*  myriad is that of course it only has that and everything's great until all of a sudden it kills
*  you. I think that's a valid objection potentially here too but even still what we would like to do
*  is find more neglected approaches which do in fact have this negative alignment tax. So far we've
*  lucked out by finding a couple that do seem to have them and I think that people tend to underestimate
*  the possibility that you could build something like this. I think there are quite a lot of other
*  neuro-inspired approaches potentially that would also have negative alignment taxes and substantially
*  move things forward as well. Do you have a sense for what compute overhead would be to implement this at
*  scale? I mean I guess a lot of it will ultimately depend on exactly what configuration turns out to
*  be necessary versus sufficient whatever but it seems like it's not huge especially if you can
*  only look at the final layer of outputs but do you have like a numerical sort of
*  range of expectation of what the extra compute cost would be? In terms of compute costs for
*  self-modeling the current implementation is adding a single linear layer. We have some other
*  things in the works but just talking about that for now it predicts its incoming activations and
*  its prediction is one to one in terms of size so it's a square matrix. So you're adding you know
*  n squared many more parameters to if it's a huge neural it's going to be negligible to add this in.
*  For the self-modeling work currently that's pretty trivial. It gets less trivial if you start to need
*  to model many more layers but one of the things that we're thinking about when we're modeling
*  and doing the self-modeling is that probably for example in your brain you don't have self-models of
*  your edge filters and your early visual cortex right and one of the reasons that you might think
*  that you don't is because you don't have cognitive access to those edge filters you can't talk about
*  it the way you can talk about your arm and have cognitive access to that so you don't have that
*  for low level processing in your brain. Similarly in a neural network you might expect self-modeling
*  to be at a much higher level at much more abstract level up the feature hierarchy and so you ideally
*  you only have to target later layers in the network. The more layers you target the bigger
*  your modeling layer gets but so far trivial additional cost. Self-other overlap there's
*  potentially a version where you pre-train with it and the current way we're doing this requires
*  two forward passes right to get that overlap to happen so that would be that could be a higher
*  cost but pre-training is an open question whether you would would want to or need to pre-train with
*  self-other overlap. Right now we're experimenting with it and thinking of it as a fine-tuning
*  strategy maybe at scale it has the the same cost as in RLHF process maybe less if you're just
*  fine-tuning very specific types capabilities you want the model not to have in terms of
*  deception and representing self another very doable and by today's standards. Yeah it seems like even
*  in pre-training the overall volume data is like mostly not things that have any relationship to
*  self or other conceptions if you tagged all of the pile for what has any plausible relationship
*  to self or other that would be a very small fraction that would end up in set most of it's
*  misinformation all of Wikipedia has very little self-other relevance for just knowing about the
*  world. So yeah interesting thing about that I was just having a conversation about this when you
*  think about how you fine-tune an assistant and the types of answers you get that it's conversational
*  you might expect that to have an outsized impact by fine-tuning on self another to the outputs of
*  such a model but you don't need to represent self another when you're thinking about the
*  geography of the world but you do when you're in a conversation and if you're in an assistant role
*  and you're an alum that's been fine-tuning into an assistant you might need that all the time and so
*  those types of fine-tuning they actually have an outsized impact on behavior versus fine-tuning on
*  extra facts are not relevant to that. Yeah that's definitely really interesting I've given why we
*  should be worried about RLHF trained models many times so hopefully folks will be familiar with
*  that. I love both of these approaches I think they're both really and I love the backstory too
*  which I didn't know until this conversation the fact that you guys had encounters with people who
*  had great ideas recognized that these are inspired ideas helped make them happen brought them to the
*  point of publication sharing with the world do you worry about creating things that might be
*  conscious if you told me that the language models are starting to become conscious I would be
*  concerned what other biological phenomena are you looking at right now for possible inspiration?
*  I want to make a quick comment on so first of all it's not impossible that models are already
*  conscious right but it's much harder to argue if you give a mechanism that you could plausibly
*  argue instant consciousness that might be easier to get the world to pay attention to in terms of
*  hey not only is this seeming like it's conscious but we have this mechanism that we think actually
*  instantiates consciousness and therefore let's take this seriously the other smell take that
*  probably I don't know if we have time to discuss or not is that it might be a very alien form of
*  consciousness that does not have preferences that opens up a whole can of worms of philosophy of
*  you know what does that mean and and what do we do with that information and how do we determine
*  that information so what I'm saying is it's possible that consciousness doesn't equal
*  a capacity to suffer for example although I wouldn't want to advocate for that because I'm
*  highly uncertain that that's the case I'm just pointing out that that could be the case so there's
*  just lots to worry about and be very careful and I think we're very far from that currently in terms
*  of what we're actually doing with MNIST for example at this stage but yes it is something
*  worth thinking about deeply and carefully. Yeah I do want to emphasize that like Mike talked about
*  it is extremely important to do further consciousness research in the first place and that itself is a
*  neglected thing to better understand what's up with consciousness it's worth doing consciousness
*  research with AI it's much better to do it on a smaller scale rather than have it emerge at a
*  larger scale where there's greater moral patienthood concern and greater x-ray scale. So how about
*  zooming out and just talking about neglected approaches generally what could be specific
*  areas of biological inspiration I guess you're looking at other areas of biology for inspiration
*  that by definition makes it somewhat less neglected what coaching would you give for
*  other people who want to seek out some neglected approaches you could frame that perhaps in terms
*  of like what are you looking for when you meet someone you'll get a couple inquiries downstream
*  of this podcast of people who have neglected approaches but how do you evaluate if they're
*  good or not how do you think about the risk reward maybe you could also talk about some things you've
*  tried that haven't worked I often feel like everything is working but I'm sure that's not
*  quite the case especially if you're specifically trying to take on projects that are low
*  probability but high potential upside how do you characterize the meta game of neglected approaches
*  yeah our Les Rungpost does a pretty good job going through our thinking about this and a lot
*  of different possible neglected approaches that we do advise and are most interested in specifically
*  with biological inspired things we think there's a lot more work that can be done in terms of
*  reverse engineering pro-sociality and that may be associated with negative alignment taxes too
*  so that's something we're quite interested in and intend to do a lot more work on and hope that
*  others do as well then we go through a bunch of other stuff in the Les Rungpost but I guess how
*  do we evaluate it is based on years of doing various different projects and thinking about
*  what's likely to work which does include things that seem unlikely to work but very high impact
*  if they do and how likely they are to work which a lot has to do with whether the person has a
*  strong hunch that the world generally doesn't accept or they've developed complex stuff and
*  people object to it for silly reasons like Graziano for instance I think it's interesting
*  to consider that the things we set out to do we assume are individually unlikely to work but very
*  high impact if they do however you asked what things haven't succeeded and actually we have
*  succeeded with the things we've set out to do so far and I am somewhat surprised by that but also
*  I think we're just good at picking the things which we will say at the beginning are very unlikely to
*  work and people would assume are unlikely to work but then wind up being pretty high impact although
*  with the Graziano work we tried a lot of different things that didn't work until we hit upon this I
*  think sticking with the thing when people are inclined to give up like something that's very
*  R&D heavy is a strong hunch for it is quite valuable to keep going even after you have failed in
*  various different ways to start with. Jeb just touched on the one I was going to add at a high
*  level and even at a project level we're accomplishing the things we're setting out to accomplish but that
*  doesn't mean that everything works first try or there's not some sort of pivots going on that's
*  true with the Graziano work with modeling paper there were lots of things we tried at the beginning
*  that were not the right thing to be trying or just didn't work out and so we stuck with it and
*  reframed things and thought deeply about the way to run these experiments etc so yeah sticking
*  with something if a strong hunch about it I think is extremely important especially in the space
*  where there's not a lot of theory to point away from something there's not a lot of theory to say
*  that this is not going to work that this is a bad idea so if hunched then continuing on it is I think
*  important tip. We just had Goodfire CTO and Chief Scientist on a couple episodes back
*  and I didn't realize at the time you guys were working together. Curious as to the nature of
*  that collaboration I'm a microscopic investor in there. We're working with them in two different
*  ways we have a developer helping on their typical type of work front end etc and then we have a data
*  scientist working with them to scale their deployment reliably so looking at how we scale
*  this to hundreds or more thousands concurrent users and also be returning all of the things
*  that they uniquely return like the features coming out SAEs and etc and so that's where
*  we're mostly involved in those two areas. Yeah I think it's quite challenging when all of a sudden
*  to change the dynamics of what's coming off the GPU and the system was originally designed for
*  that I can imagine how that can get quite complex. That's right the existing tooling doesn't handle
*  that out of the box at all. Cool this has been fascinating guys I love everything about what
*  you're doing the company backstory is fascinating the brain computer interface era is fascinating
*  and especially this recent work with biological inspirations for alignment approaches we could
*  get along better but we certainly do have some pro-social tendencies remarkably as far as we've
*  come with the current crop of AI we haven't really mined our own structures much at all
*  for figuring out how to make them work better in those ways I think this is just phenomenal work I
*  really appreciate it and excited to share this with the audience. Anything that we didn't cover
*  that you want to touch on or any closing thoughts you want to share? One thing that is interesting
*  to consider is just as you can take a neglected approach to doing what is the highest impact stuff
*  in alignment technically you can also do that in terms of policy and other things too. That meta
*  approach led us to conclude it would be worthwhile to encourage the creation of for-profit consulting
*  businesses of like more non-profits doing neglected approaches of individuals setting out to do
*  neglected approaches of field building to get brilliant people in different fields like in
*  particular but also many other fields to get nerd sniped into caring about and doing something
*  to do with alignment we think there's a lot of loaning fruit there and also incidentally neglected
*  approaches to AI policy specifically can be things like getting government to increase funding to
*  alignment research actually moves forward alignment not just capabilities doing things like increasing
*  whistleblower protections for instance very high impact quite neglected today getting
*  republicans to care more about AI safety and trying to prevent it from becoming a partisan
*  issue like the more far left is like tied up AI safety unfortunately too much in things that
*  are on the surface to people on the right like woke DEI associated but that actually has nothing
*  to do with AI alignment like making the founding fathers black is a failure of AI alignment this is
*  the system is not aligned it's not to me what we told it to do but then this plays into this false
*  narrative that is emerging too much on the right which is that AI safety is basically all this woke
*  stuff that they think is bullshit they're op-eds saying Elon Musk should be a democrat because he
*  cares about AI safety which by the way is woke stuff this is making people think totally the
*  wrong thing people on in the AI safety community are unable to do what Jonathan Haid calls the
*  moral reframing necessary to articulate things in the narrative of the right to get them sufficiently
*  motivated to care about AI safety the way they should there's like a 50 or 48 chance or whatever
*  that that Trump takes the White House and people are not sufficiently prepared for trying to make
*  it that if this is the president who presides over the transition to AGI if there's some possibility
*  of that in the next four years that goes very very well and I think that in particular is something
*  that is neglected now we think more people should be trying to make it a bipartisan thing instead of
*  it becoming a partisan thing which it's sort of slipping into being potentially as it yeah amen
*  to that no partisan polarization on AI safety please I couldn't agree more I've really appreciated
*  conversation Judd Rosenblatt and Mike Viana from AE studio thank you both for being part of the
*  cognitive revolution thanks for having me it is both energizing and enlightening to hear why
*  people listen and learn what they value about the show so please don't hesitate to reach out
*  via email at tcr at turpentine.co or you can dm me on the social media platform of your choice

---
Date Generated: September 05, 2024
Transcription Model: whisper medium 20231117
Length: 6857s
Video Keywords: []
Video Views: 1091
Video Rating: None
Video Description: Nathan explores the cutting-edge world of AI-powered forecasting with Deger Turan, CEO of Metaculus. In this episode of The Cognitive Revolution, we discuss how AI is revolutionizing prediction markets, the potential for AI to outperform human forecasters, and Metaculus's ambitious new AI forecasting benchmark tournament. Join us for an insightful conversation about the future of decision-making and collective intelligence.

Participate in Metaculus' first of its kind bot forecasting tournament: https://www.metaculus.com/aib/

Apply to join over 400 founders and execs in the Turpentine Network: https://hmplogxqz0y.typeform.com/to/JCkphVqj

RECOMMENDED PODCAST: 1 to 100 | Hypergrowth Companies Worth Joining
Every week we sit down with the founder of a hyper-growth company you should consider joining. Our goal is to give you the inside story behind breakout, early stage companies potentially worth betting your career on. This season, discover how the founders of Modal Labs, Clay, Mercor, and more built their products, cultures, and companies.
Apple: https://podcasts.apple.com/podcast/id1762756034
Spotify:https://open.spotify.com/show/70NOWtWDY995C8qDqojxGw

RECOMMENDED PODCAST: Second Opinion
A new podcast for health-tech insiders from Christina Farr of the Second Opinion newsletter. Join Christina Farr, Luba Greenwood, and Ash Zenooz every week as they challenge industry experts with tough questions about the best bets in health-tech.
Apple Podcasts: https://podcasts.apple.com/us/podcast/id1759267211
Spotify: https://open.spotify.com/show/0A8NwQE976s32zdBbZw6bv


SPONSORS:
Building an enterprise-ready SaaS app? WorkOS has got you covered with easy-to-integrate APIs for SAML, SCIM, and more. Join top startups like Vercel, Perplexity, Jasper & Webflow in powering your app with WorkOS. Enjoy a free tier for up to 1M users! Start now at https://bit.ly/WorkOS-Turpentine-Network

80,000 Hours offers free one-on-one career advising for Cognitive Revolution listeners aiming to tackle global challenges, especially in AI. They connect high-potential individuals with experts, opportunities, and personalized career plans to maximize positive impact. Apply for a free call at https://80000hours.org/cognitiverevolution to accelerate your career and contribute to solving pressing AI-related issues.

The Brave search API can be used to assemble a data set to train your AI models and help with retrieval augmentation at the time of inference. All while remaining affordable with developer first pricing, integrating the Brave search API into your workflow translates to more ethical data sourcing and more human representative data sets. Try the Brave search API for free for up to 2000 queries per month at https://bit.ly/BraveTCR

Omneky is an omnichannel creative generation platform that lets you launch hundreds of thousands of ad iterations that actually work customized across all platforms, with a click of a button. Omneky combines generative AI and real-time advertising data. Mention "Cog Rev" for 10% off https://www.omneky.com/

Head to Squad to access global engineering without the headache and at a fraction of the cost: head to https://choosesquad.com/ and mention “Turpentine” to skip the waitlist.

CHAPTERS:
(00:00:00) About the Show
(00:00:22) Sponsor: WorkOS
(00:01:22) About the Episode
(00:04:47) Introduction and Background
(00:08:42) Deger's Journey to Forecasting
(00:13:06) Current State of Forecasting
(00:16:41) Overview of Metaculus (Part 1)
(00:20:23) Sponsors: 80,000 Hours | Brave
(00:22:55) Overview of Metaculus (Part 2)
(00:23:30) AI Forecasting Research Papers
(00:28:41) AI Forecasting Benchmark Tournament (Part 1)
(00:35:44) Sponsors: Omneky | Squad
(00:37:31) AI Forecasting Benchmark Tournament (Part 2)
(00:37:43) Future of Forecasting and Metaculus
(00:44:01) Improving Forecasting Accuracy
(00:51:56) Scoring System and Tournament Rules
(00:59:01) Potential Impact of AI Forecasting
(01:04:17) AI Forecasting Benchmark Series Details
(01:11:03) Tournament Structure and Participation
(01:17:07) Consistency in AI Forecasting
(01:21:13) Leaderboard and Prizes
(01:25:41) Future of Democracy and Decision-making
(01:34:36) Risks and Challenges in Forecasting
(01:42:43) Consensus Illusion and Policy Making
(01:48:47) Roadmap for Scaling Forecasting Impact
(01:53:55) Outro

---
SOCIAL LINKS:
Website : https://www.cognitiverevolution.ai
Twitter (Podcast) : https://x.com/cogrev_podcast
Twitter (Nathan) : https://x.com/labenz
LinkedIn : https://www.linkedin.com/in/nathanlabenz/
Youtube : https://www.youtube.com/@CognitiveRevolutionPodcast
Apple : https://podcasts.apple.com/de/podcast/the-cognitive-revolution-ai-builders-researchers-and/id1669813431
Spotify : https://open.spotify.com/show/6yHyok3M3BjqzR0VB5MSyk
---

# Scaling Forecasting AI Forecasting Tournaments & Road to Epistemic Security, with Deger Turan
**Cognitive Revolution:** [August 28, 2024](https://www.youtube.com/watch?v=mpz1cuR4opQ)
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
*  Hello, and welcome back to the Cognitive Revolution. Today, my guest is Dher Turan, CEO of Metaculous,
*  a leading forecasting platform that aims to bring epistemic security to how we understand the future.
*  Forecasting has long fascinated me. I participated in one of Philip Tetlock's original
*  super forecasting tournaments some 15 years ago, and I actually did reasonably well,
*  though I was not ultimately named a super forecaster. Since then, I've often visited
*  forecasting sites like Metaculous to take a pulse on future events, and I've always intuitively
*  believed that forecasting could really help most organizations to make better decisions.
*  And yet, despite its promise, forecasting has not become a mainstream technology.
*  That's in part because it is a ton of painstaking work to do forecasting well,
*  and that's really hard to scale to the point where forecasts become consistently relevant
*  to decision makers as they operate in highly contextual situations.
*  As a case in point, Metaculous has hosted some of the most referenced AGI timeline forecasts for
*  years, and still today, fewer than 1,500 people have registered their own individual forecasts.
*  If you've listened to this show for any length of time, you can probably guess where this is
*  going next. What if we had AIs do the forecasting? It turns out that with some real effort required
*  and some important remaining caveats, this already works. Multiple recent papers, including some by
*  TentLock and others, show that AI systems forecasts are competitive with the best individual humans,
*  though they do still fall somewhat short of the wisdom of human crowds.
*  Darin and I first review this literature together, and then go on to discuss Metaculous's
*  reasons for gathering more complex probability distribution style predictions rather than simply
*  seeking to discover market prices. We also review the community's track record on major world events,
*  and we get into Metaculous's ambitious new AI forecasting benchmark tournament. This is a
*  year-long competition that aims to advance the state-of-the-art in AI forecasting capabilities,
*  with free API credits available and meaningful prizes to be awarded quarterly. Beyond that,
*  we explore Dare's vision for the future of forecasting, not just as a way to predict
*  outcomes, but as a tool for building better world models and improving collective decision-making.
*  His ideas on using forecasting for resource allocation, policy development, and even
*  enhancing democracy are both exciting and thought-provoking. And another example,
*  not only of how AIs' already superhuman strengths, in this case scalability, have the potential to
*  change the world even if the AIs perform no better than humans on a given task, but also how AIs are
*  meaningfully generalizing beyond their training data. After all, the future is in some sense
*  definitionally out of distribution. As someone who's deeply interested in both AI development
*  and societal decision-making, I found Dare's perspectives fascinating, and I think you will too.
*  As always, if you're enjoying the show, I'd ask that you take a moment to share it with friends
*  or leave us a review on Apple Podcasts or Spotify. And if you have any feedback or guest suggestions,
*  you can contact us via our website, cognitiverevolution.ai, or you can DM me
*  anywhere you like. Now, I hope you enjoy this exploration of the frontiers of AI-powered
*  forecasting with Dare Taran, CEO of Metaculous. Dare Taran, CEO of Metaculous, welcome to the
*  Cognitive Revolution. Thank you. Big fun here. Thank you. That's kind of you to say. I'm excited
*  for this conversation. I've been a Metaculous long-time watcher, and you've got some very
*  interesting new projects, which will be kind of the bulk of our conversation today. But maybe
*  for starters, you're relatively new to the job, just a handful of months in the CEO role there.
*  I want to give us a little bit of your background in AI, because you've been working in the space
*  for years before that, and made a move that you might want to unpack a little bit in terms of
*  why the shift to the forecasting role now. I guess hindsight is 2020, especially in
*  contexts like forecasting. I have always been interested in questions of collective intelligence.
*  How can we aggregate multiple different perspectives to the point that we can
*  build a coherent world model? And I was working on this question while I was still at school from
*  a perspective of, can we use natural language processing? This is way before LLMs, like back
*  in 2016. How can we aggregate multiple different streams of thoughts so that this would be
*  actionable for a policymaker? So I've been interested in working with federal agencies
*  and build a startup on the space. And right before Metaculous, I was working on AI Objectives
*  Institute, which is a nonprofit research lab focusing on socio-technical alignment, which is
*  looking at questions of AI alignment in context of real people in deployments right now, and seeing
*  are there any technical steps we can take that can actually say this group of people do perceive
*  this AI model as better aligned or more instrumental towards their goals? Looking at it from an
*  individual perspective and from a collective perspective and from a systems perspective on
*  understanding how can these tools be much better used for enhancing human agency? And I've been
*  doing a lot of work on questions of collective intelligence. How can we augment a multitude of
*  different views to be able to contribute to a system that might be a single model or it might
*  be multiple different agents collaborating? This might be a government, this might be an LLM,
*  this might be an ensemble model. This is in a way applicable to many different systems, right?
*  And very quickly, I find myself thinking about, okay, say we can aggregate multiple people's
*  desirability. Even if we are able to do this on a high fidelity level, how do we get to the world
*  outcomes that we're looking for? How do we actually go towards the model that is not just driving
*  towards the lowest common denominator and finding a consensus mode where the desire for consensus
*  actually causes a trade-off with fidelity to one's perspective, but instead see what would actually
*  be helpful? What future do we want to live in? Are causes prioritized correctly so that we can move
*  towards better futures? Can we find positive sum games? Who will shoulder the externalities
*  if there is no free lunch? How can we make sure we're tracking that? And these questions brought me
*  towards thinking, okay, who's looking at the world from a perspective of if we take action course X,
*  will that yield a better outcome? And that's how I found myself thinking about forecasting.
*  Because if I'm able to even have a very high fidelity version of desirability elicitation,
*  preference elicitation, understand all the cruxes that exist in society, that still does not bring
*  me towards a machine system being able to take actions that yield net good. So exploring that
*  along with the questions of wisdom of the crowd, you know, if you have multiple different perspectives,
*  be these be real humans or AI that is actually once aggregated is doing a better job in forecasting
*  outcomes. I realized it's actually quite instrumental in how we look at the world. So that is what
*  brought me towards thinking about more forecasting. Cool. Just to rewind back in time for a second
*  to the 2016 era, did any of that stuff work? Were you able to make anything with technology
*  that was available at the time that you thought yielded any practical utility?
*  Yes. Well, back then, I was working with Dan Juravsky on a question at Stanford on federal
*  agency regulatory feedback. So the FCC net neutrality debate was just taking off. And
*  there was 2 million comments that were submitted to the federal agency. And at that point, this
*  seemed like, wow, this is the largest data set that was ever collected off raw text. Now it's
*  ridiculously small. But at that point, there was this question of, okay, how should a central
*  agency pay attention to this? There was a lot of interesting questions. Like a lot of the submissions
*  were form letters that are copy paste. But the fact that it is copy paste does not make it
*  illegitimate. You know, I will read a campaign and say, yeah, I agree with this. I want to send
*  this. How should you take that into account compared to something that is both generated
*  compared to something that is a genuine opinion that someone has taken time, but it's not
*  necessarily sophisticated and you can see that it is shortcomings. And my thesis work, I was
*  looking at this both from a legal perspective and also technical perspective. You know, what are the
*  expectations from EPA and EPA perspective on just the US legislation, but also how can we have
*  natural language processing augment this? And funny enough, at that point, I was thinking a lot
*  of questions of good hearting. Like every time we start focusing on a specific narrower metric,
*  it's easy to be a good measure. And this was very apparent and being able to claim that you're
*  looking at the public. Things we tried were so simple, and yet they seemed like, oh, this is a
*  paradigm shift. Just like simple clustering strategies, unsupervised learning, topic modeling.
*  And even that went a long way because people had no idea. And now we can do much more sophisticated
*  versions. And people still are like, people assume that we don't need to ask these questions
*  because we cannot do large scale qualitative surveys. So we keep going back to Likert scale.
*  So I guess the crusade I've been on for a long while is, can we go past, how happy are you one to
*  seven? Or should we build a road from A to B or A to C? I'm like, maybe we need to build a bridge
*  instead. And if you don't let people express that, you're just not going to get that opinion.
*  So how do we get machine learner systems, optimizers, to be able to understand,
*  ah, there's something qualitative that I need to elicit that even the speaker might not be sure
*  what they want. Like, how can we give room for that human flexibility in these machines?
*  So your comment on good hearting definitely resonates with me, particularly today. I was just
*  having some back and forth on Twitter about the new GPT-4O mini model, which is coming in ahead of
*  Claw 3.5 Sonnet on the LM-Sys leaderboard. And that raises the question. It seems like the
*  general consensus among people like me who are obsessed with the latest AIs and kind of have
*  their own individual opinions seems to be that 3.5 Sonnet is the best. Certainly, we all would all
*  tend to think it's better than GPT-4O mini. And yet there it is ahead in terms of the votes that
*  it's getting. So this has raised all sorts of, you know, why is this happening? Do we trust this
*  thing anymore? Is it just about formatting? If it is mostly about formatting, does that mean it's
*  illegitimate in some way? Or does that mean we should really think more about the importance
*  of formatting? But yeah, as always, it's extremely difficult to pin much down if you really want to
*  do it with any real rigor. So that is maybe a good bridge toward and certainly the same
*  is even more true about the future. So we've been interested in this space of forecasting
*  for a long time. I actually participated in one of the original Tetlock organized
*  super forecasting tournaments maybe 15 years ago now. Tyler Cowan posted an invitation to
*  participate and I was like, I'll try my hand at that. I did reasonably well. I didn't top
*  the leaderboard, but I came out feeling like I had at least somewhat of a knack for it. And I've
*  always found that the sort of Robin Hansen perspective on like, this seems like a much
*  better way than sort of highest paid person's opinion or like whatever kind of prevails in
*  organizations. That's always been compelling to me, but it seems like generally speaking,
*  we still don't see a ton of forecasting deployments in the world. What would your
*  analysis be of kind of where we are in forecasting, you know, where you think like the most notable
*  deployments are and why we don't see more than we do today. Right. I want to answer from the
*  previous point you made around good heart because I think this actually goes towards there on, you
*  know, which model is better defined better, right? Better is incredibly content specific,
*  like even in just a small world of things I am trying to do personally within the calculus,
*  but the point five is more useful for me on question writing, but not necessarily fact retrieval.
*  And it's a very narrow thing. And this current version of these models seem like, you know,
*  one of them has an easier neck towards one thing without interrupting, without self-sensoring. So
*  I can move forward faster. I think the core of forecasting also relates to this in terms of how
*  can this process actually be useful is one thing that is different from will it score good on these
*  benchmarks? Like in this one specific competition, will 4.0 score better? Like that is a much narrower
*  thing in a way usefulness is almost always anecdotal. And I think we are not paying enough
*  attention to that. And I think the same is applicable for forecasts as well. There has been
*  so many tournaments, like the ATCX, the three tournament is interesting for how accurate the
*  forecasts have gotten, but to me, okay, how is this going to actually be useful for an end user
*  is a different question. And I think this is the approach that I really want to focus on with
*  Metaculous for the upcoming sprint is, okay, I have a couple of validations that I feel satisfied
*  with. What are those ones? Wisdom of the crowd works. It is interesting that it works. But when
*  you aggregate a number of people, and we will go into it when you aggregate the number of bots that
*  are trained with LLMs or what have you, it seems to be able to draw an accurate picture of the future.
*  And we have enough case studies of this. Why is this not more commonly used? I think usefulness
*  is a whole different paradigm than accuracy. And this is really what I want to focus on. What do
*  we want to do on this front? Like, for example, can we identify critical inflection points towards
*  future states is a different question than just is your forecast accurate? What is the shape of
*  the world that we want to live in? What are entities? You know, these can be federal agencies
*  like my prior work. This can be philanthropists, this can be corporations, nation states.
*  The framework of forecasting so far, especially from a talking lens, I think, has not focused
*  on how will this be actually useful, but has more so focused on can we prove the accuracy?
*  I would like to move forward towards coming up with versions of forecasting deployments that
*  actively pay attention to how will the decision maker take this into account?
*  What are things that are within their space of levers? This is why I think forecasting in
*  context of the humans that are trying to live a better life is extremely important. I can share
*  more examples on this front, but I'm curious where you'd want to go with this. Like pretty
*  much our research agenda for Metaculous for the next chapter, for the next two quarters,
*  heavily focuses on a lot of experimentation on these kinds of questions.
*  Yeah, interesting. Does that look like basically conditional markets being kind of the first thing?
*  I mean, that's something that Robin Hansen has talked about for a long time, and I don't see
*  much, but we've just lived through a moment in history where it seems like something like that
*  was pretty motivating to the current president of the United States, who I think was, if reporting
*  and general intuition are correct, seems like he was not sold on the idea that somebody else had a
*  better chance than him until he saw polling data suggesting that, and then was kind of like, well,
*  I guess, yeah, if somebody else has that much of a better chance, maybe I should step aside.
*  Is that the sort of play that out a million different ways for a million different contexts,
*  but is that the kind of next big paradigm? I think that is an example that basically is
*  a very simplified and somewhat was obvious to the entire population except for the decision makers
*  themselves for longer than it should have in my opinion state of affairs. With that said,
*  the real cases that I'm interested in is much more sophisticated than this, right?
*  That heavily looks at public opinion and is more, if I may say, like vibes-based rather than data
*  driven. And I'm interested in really pushing this edge further. Say we have $50 million to allocate
*  towards making the world better. Pick your challenge, reducing microplastics, climate-related
*  risks, AI-related risks. How should we allocate these resources to get to a better world? It
*  requires us to build world models. I think forecasts around what are specific outcomes we
*  can get to if we take an intervention point is very helpful. And the simplest thing we can do
*  is exactly what we said on, you know, come up with conditional forecast. If we take Lover X,
*  will that bring us to a better future? If not, what will it be like? And if we see high divergence
*  here, that is great. Now I want to push this much further. We can already do this, but through this,
*  conditional questions are somewhat hard to answer. It's hard to think in that framework. So
*  can we build tools, be it LLM driven or discourse driven or come up with ways in which people
*  can collaborate that enable conditional forecasts to be more useful? This is one avenue. One of the
*  things I want to do in the near future is launch a series of minitacules. This is the name we came
*  up with. Think of it like subreddit, which is Metaculous instances. This will come in context
*  of us open sourcing Metaculous. And we hope that many of these will spring in the next quarter.
*  Each Minitaculous will be focused on a specific question, a goal-oriented question, such as we are
*  trying to reduce microplastics, for example, or we're trying to reduce homelessness in San Francisco.
*  This is geared towards disaster response or consequences of research avenues in context of
*  AI. I would want every question in the Minitaculous to be able to serve. If we are able to answer this
*  question, it bubbles up to the parent. And then we can see which of these questions have the highest
*  value of information. Which of these questions actually inform us to say, oh, it looks like
*  this intervention is going to be able to drive much further value. I would want us to identify
*  critical inflection points. Like, is there a specific moment in which the world models seem
*  to diverge? Are we able to extract schools of thought in the context of forecasting by seeing,
*  oh, this group of forecasters seem to be much more in accordance over multiple forecasts.
*  Why is there world model divergent? Can we double down on finding more questions that can help us
*  excavate that? These kinds of research questions go way beyond what Minitaculous has aimed for so
*  far. This is actively trying to build a world model in an enclosed world space that is Minitaculous
*  with a specific goal. And I find this to be really, really interesting. Like the kinds of things I
*  would love to do is, for example, can we find short-term proxies and heavily forecast on both,
*  is this short-term proxy good and how is the short-term proxy panning out? The way we landed
*  with the Fab, the Forecasting AI benchmark is basically guided from this also. In a way,
*  we can frame the presidential debate through this lens. I think we as a civilization need to think
*  much more from this lens. Like, this is a version of a cognitive revolution where we change how
*  people are thinking about the future. In a way, we're enabling them to coordinate between their
*  world models. I still see forecast aggregation to be fairly low fidelity to be able to coordinate
*  world models. But I think we can use that as a building block, as a primitive, and come up with
*  much better world models. Hey, we'll continue our interview in a moment after a word from our
*  sponsors. I am really excited that our new sponsor, 80,000 Hours, is now offering free
*  one-on-one career advising sessions to cognitive revolution listeners. 80,000 Hours aims to be the
*  best source of advice for people who want to do the most good that they possibly can with their
*  careers. We typically work for about 40 years in our lifetime, and we work about 2,000 hours per
*  year. That is the single biggest opportunity that most of us have to make a positive contribution,
*  and it's worth being strategic about it. That's where 80,000 Hours can help. I actually used
*  their career advising service myself. Two years ago, I had just finished the GPT-4 red teaming
*  project, and I wanted to do anything I could to nudge the AI future in a positive direction.
*  But what could or should I do? That was not clear. After my call with 80,000 Hours, I got a number
*  of connections to outstanding individuals in the space, and over the course of the follow-on
*  conversations, I developed the confidence that this podcast was one of the projects that I should
*  pursue. Today, I'm thrilled to have built an audience of thoughtful, high-potential people
*  that 80,000 Hours wants to help. To request a free one-on-one career advising session,
*  follow the link in the show notes. It's 80,000hours.org.org.org.org.org.org.org.org.
*  Sign up for a free one-on-one career advising session. Figure out how you can make a positive
*  impact on the AI future, and I think you'll be glad that you did.
*  This episode of the Cognitive Revolution is sponsored by the Brave search API. You may
*  know of Brave as an alternative to Chrome, but did you know that Brave has its own independent
*  search engine powered by its own 20 billion page index of the web? The Brave search API gives
*  developers reliable and affordable access to programmable web search, auto suggest,
*  spell check, and more, with flexible plans for all types of use cases, from rag search to automated
*  business intelligence. On top of that, it's up to three times cheaper than Bing, all without
*  compromising on quality, speed, or reliability. Over 700 businesses, including Cohere, Chegg,
*  and Kagi rely on the Brave search API. And a recent survey showed that 94% of customers
*  would recommend it to their peers. To start building apps with the power of the web,
*  sign up at brave.com slash API and get up to 5,000 free monthly calls.
*  Now, let's maybe take one step back just for those who maybe don't have so much experience
*  with Metaculous as it exists today. I'd be interested to hear just like for starters,
*  how do you describe it to somebody who's never seen it before? Would you call it a prediction
*  market? Would you call it a forecasting platform? How does it fit it? Because there's like a few of
*  these now, right? People would be familiar with certainly just online betting platforms, but also
*  there's like manifold and polymarket that I see kind of shared around. How would you describe the
*  overall product today? And how would you distinguish it from some of the other things that are out there?
*  Metaculous aggregates forecasts. It's a forecasting platform and an aggregation engine. I would not
*  call Metaculous a prediction market. The goal of Metaculous is to bring a level of epistemic
*  security towards how we envision the future to be. You can call it Wikipedia about the future.
*  And it is a space in which multiple people can see how they foresee the future to play out.
*  And the critical discussions to take place there. It works with predictions as its core block, but
*  it does not have a monetary incentive. It behaves quite differently than prediction markets as a
*  result of that. And some of those differences are the reasons why, in my opinion, Metaculous has
*  been both more accurate and also more rigorous compared to a lot of other spaces. It is, I can
*  shed more light into that. For example, on a prediction market, the participants are buying
*  and selling contracts that are based on the future outcome of an event, right? So you place bets and
*  the result is a zero sum question. For example, if the current forecast is at 60% and you think it
*  is 60%, you don't have an incentive to add that information in because it only can get worse from
*  there. While on Metaculous, this is not the case. There's no financial incentive and instead we are
*  comparing all the forecasters' accuracy and track record through time. And this creates a different
*  set of incentives that I believe are actually much more productive towards something that
*  looks like Wikipedia about the future, where people are one, incentivized to share what their
*  world model is. Two, people are incentivized to participate in forecasts and not think about
*  de-risking or spreading, but instead focus on what is the world model that I have that I can share.
*  So our scoring mechanisms are different with respect to prediction markets as a result of that, too,
*  because the reward mechanism is that the reward of forecasts are over time for their calibration
*  across many predictions and for their accuracy. We also have a metric that we call the community
*  prediction. This is interesting because this is where you can see everyone that has predicted on
*  this question. And we also have weighted averages depending on your past success on your track
*  record and the recency for, you know, sooner forecasts tend to be better for you have more
*  information. So using these, we actually end up in an ecosystem that is much more collaborative
*  and much more grounded and good at this. And this brings higher rigor as well. So the questions we
*  forecast tend to be more like carbon emissions on this date rather than very personal questions like,
*  who am I going to be dating with next? And I like that, you know, there's a market for that,
*  but I like that there is a space for focusing on the rigor that is actually beneficial for the world.
*  So that is what I find distinct and attractive about it, I guess.
*  Gotcha. So it seems like the big thing there is the incentives, whereas on a
*  more market oriented platform, I am looking for things that are wrong so I can make money. Here,
*  I am looking for just opportunities where I can share something with the community that hopefully
*  brings the overall community forecast toward a more accurate.
*  Right. But I will add that there is a financial incentive in Metaculous too,
*  as in if you have very good track record as a forecaster, we will hire you as a pro forecaster
*  to engage on many specific paid client works. And these range from federal agencies to large
*  retailers to hedge funds and banks that have much narrower questions. These questions don't make
*  their way to the public forecast that we have, and they will be paid engagements. And we will also
*  pay the pro forecasters for their reasoning so that they can actually explain why they see the
*  forecast to be this way. Just to echo back to a thing we were talking about, I think one of the
*  core projects that we have for Metaculous is going to be reasoning transference. The forecast,
*  don't say I am making up an example, say we are thinking about the Taiwanese sovereignty,
*  this was the context in which this came up. I was in Taiwan recently for a conference and we were
*  talking about will Taiwan's electricity grid be challenged by China in the process of a potential
*  invasion. The forecast jumped from 30% to 40%, and there were no comments under it because it
*  was fairly new. I was sharing this with one of the folks there that are working on from the
*  government's perspective and they were saying unless I know why this is the case, I cannot
*  take this into account. And for that, we do pay our pro forecasters to come up with better
*  forecasts with their explanations as well. We place people in jobs in the past. There is,
*  in a way, the leader board can translate into financial incentives. It does not happen on the
*  substrate of the question itself. And that I think is quite important.
*  Okay, cool. Can you say a little bit more about how you create that community forecast out of,
*  you touched on this briefly, but this is one of the big questions that I've had,
*  honestly, for a long time, because there are two, I think of them as canonical AI
*  questions around AGI timelines that I've come back to for years now. I think I first tweeted
*  about that almost two years ago. And these are the weak AGI and the strong AGI. And we can unpack
*  this a little bit more in a minute. But one thing that I've always kind of wondered is like,
*  exactly what am I looking at when I'm looking at this? To what degree am I seeing, is it a
*  naive aggregation? Because you can go in there and put a whole distribution, right? So I'm
*  interested in your comments on that too. I don't have a great sense of what I'm doing
*  when I'm actually drawing a curve over the potential timeline of something happening.
*  I feel like I'm a little bit like, I guess I'm always sort of vibing with these predictions,
*  but that brings it home to me where I'm like, boy, the precision here feels like I'm leaving
*  something behind that is, you know, and it's weird, right? It's a way to express my uncertainty,
*  but it's also a way to be very specific about my uncertainty. And even that, I don't feel like I
*  really have. So interested in sort of how you see that kind of curve drawing, and then how are you
*  aggregating all these curves into one curve? Do people get up-weighted if they're better? Is
*  there a recency bias, etc.? So a couple different parts there with respect to the
*  community prediction calculation, we basically keep the most recent prediction from each forecaster
*  that we have. And we weight each forecast based on how recent it is before being aggregated.
*  And we also for the attackless prediction do pay attention, especially if there is a paid client
*  that is looking for a specific outcome or higher rigor, we do do things like pay attention to the
*  past track record of each of the forecasters and aggregate that information in as well.
*  For binary question, the community prediction is basically a weighted mean all of the individual
*  forecasters probabilities. And if you have a numeric question or a date question, it is a weighted
*  mixture of all of the individual forecaster distributions. There's actually a lot of different
*  philosophies of aggregation. And this is one of the spaces that I am interested in experimenting
*  further. These are the ones that we use. And in general, the community prediction works and seems
*  to be really accurate. There may be a couple of folks that seem to consistently beat the community
*  prediction. And I think there's a couple posts from Astral Codex 10, etc., that has focused on
*  exploring this. I think that I'm very interested in this very soon we will open source with
*  that. I'm curious for people to come up with, you know, here's the difference in a scoring mechanism,
*  an aggregation mechanism that actually seems to work better, or seems to be more instrumental.
*  I really want to encourage experimentation on the space. What we have so far seems to work. If you
*  just copy the community prediction, you will do pretty well in a tournament. But then you're not
*  really bringing in independent information, right? So the better question to do is for someone to do
*  their homework on, you know, what are past forecasts that might be similar to this and then contribute
*  and only after that you see the community prediction because otherwise you start messing
*  with the wisdom of the crowd. You said, you know, you might be doing vibe-based reasoning. I think a
*  lot of more so reasoning-based forecasting ends up being like space for a lot of people. Not everyone
*  is going to build like a mathematical vigorous model or be a domain expert. But somehow when we
*  put many of these together, it actually does yield a better outcome. I would start from, for example,
*  the comparisons from the 2023 ACX contest is quite interesting to look at for comparison of,
*  you know, how does Metaculous compare for prediction markets or super forecasters.
*  I really like Semiswifty as an anchor for I think they're actually doing a great job as a reference
*  point. To me, the parts of the question is like how to make the forecast useful along with how
*  to make the forecast be accurate. I think there is enough track record on a couple different forms.
*  Like the who predicted 2023 best posts from Estrel Codex 10 is quite interesting for this.
*  But if you've been zooming on specific moments where an entity, it's a federal agency or a person
*  was able to take action from a forecast, I think those are the moments where I see yes, Metaculous
*  was actually useful or interesting. For example, in epidemiology, Metaculous has outperformed both
*  panels of experts on COVID and also informed hospital resource allocation, public health
*  decision making. A lot of the forecasts were more robust and accurate than baseline models
*  in predicting COVID vaccine updates. And I do think that is quite interesting, for example.
*  And another part is on the monkey box outbreak, Metaculous was able to quickly provide perspective
*  on that front. For example, in January 2020, back when conventional wisdom was that COVID
*  wouldn't be significant, Metaculous instead was predicting that more than 100,000 people would
*  eventually be infected with the disease. And a lot of folks took that as an early warning sign.
*  I remember reading a post about someone making a bunch of investment decisions because Metaculous
*  said so. Like another case is around predictions around Russia invasion of Ukraine. There's a
*  comment on Metaculous that I really like where the Metaculous user in Ukraine said, just want to say
*  that I moved from Kiev to Lviv on February 13, entirely thanks to this prediction thread and the
*  Metaculous system. That to me is a moment where, yeah, the forecasts were instrumentally useful
*  for someone making a decision. We've been cited in The Economist, Our World and Data, Bloomberg,
*  Fortune Forbes, you name it. I think the core question is around how will these be able to
*  turn into instrumental actions that one can take? And I'm particularly interested in this being
*  helpful for the AI sphere and making sure the tools that we're building on AI as a whole are
*  serving humanity. And I think if there is something that has good track record and
*  ability to be able to influence individual decisions, we should explore why and how this
*  can be much more useful. And that is the lens with which I think prioritizing AI is important,
*  but also other cause areas. Some folks say Metaculous should purely focus on long-termist
*  causes. I actually do think a lot of short-term intervention modeling and being able to take
*  successful action teaches us on how forecasting can be helpful in longer-term contexts. Questions
*  like how can we reduce homelessness in San Francisco? If I have an additional 5 million,
*  should I just go build two more houses? Is that the best thing I can do? Or is there a form of
*  lobbying that I do think a large crowd will say, this will make the housing market understand the
*  negative externalities of homelessness to the point that we can have a more well-grounded change?
*  I would like this to be a Metaculous where every forecast, these forecasts can be conditional,
*  they can be intertwined with each other. We can explore different ways to visualize them.
*  These will bring usefulness towards someone. And us being good at this on a repeatable fashion
*  will help us be able to tackle the largest questions much better.
*  Hey, we'll continue our interview in a moment after a word from our sponsors.
*  Amnachie uses generative AI to enable you to launch hundreds of thousands of ad iterations
*  that actually work customized across all platforms with a click of a button. I believe
*  in Amnachie so much that I invested in it and I recommend you use it too. Use Cogrev to get a 10% discount.
*  Hey all, Eric Torenberg here. I'm hearing more and more that founders want to get profitable
*  and do more with less, especially with engineering. Listen, I love your 30-year-old ex-fang senior
*  software engineer as much as the next guy, but honestly, I can't afford them anymore. Founders
*  everywhere are trying to turn to global talent, but boy is it a hassle to do at scale from sourcing
*  to interviewing to on the ground operations and management. That's why I teamed up with Sean
*  Lanahan, who's been building engineering teams in Vietnam at a very high level for over five years
*  to help you access global engineering without the headache. Squad, Sean's new company, takes care of
*  sourcing, legal compliance, and local HR for global talent so you don't have to. With teams across Asia
*  and South America, we can cover you no matter which time zone you operate in. Their engineers
*  follow your process and use your tools. They work with React, Next.js, or your favorite front-end
*  frameworks, and on the back end, they're experts at Node, Python, Java, and anything under the sun.
*  Full disclosure, it's going to cost more than the random person you found on Upwork that's doing two
*  hours of work per week but billing you for 40, but you'll get premium quality at a fraction of the
*  typical cost. Our engineers are vetted top 1% talent and actually working hard for you every day.
*  Increase your velocity without amping up burn. Head to choose squad.com and mention Turpentine
*  to skip the wait list. Cool. Very interesting. So going to these two AI questions that I
*  refer back to the most, I think probably many listeners will have visited these pages.
*  The weak AGI and the strong AGI timeline, each one has four different resolution criteria and the
*  question is basically when will a single AI satisfy these different criteria and you get
*  to predict your distribution of dates. I think this has been really interesting and quite
*  informative for a long time. Although more recently, it does feel like it also highlights
*  a real challenge of writing these questions, which is that when things are farther out,
*  it seems like the or it can seem, I feel like in this case, it does seem like the detailed criteria
*  seemed quite reasonable. And now as we're getting closer, I'm feeling like there's sort of a
*  divergence between what matters and what is actually the letter of the law in the question,
*  particularly when it comes to in the weak AGI question, the use of a specific form of the
*  Turing test, right? I'm kind of like, okay, from my standpoint, in the sort of intuitive,
*  like what really matters in the Turing test, line of thinking, I would say we've passed it.
*  And yet the formulation requires a expert interrogation and that experts not be able
*  to tell what is the AI and what is not the AI. And we're not that close to that. But I always
*  emphasize for people that I think the reason we're not that close to that is a design decision of the
*  people that are making the AIs that are to be tested, right?
*  How confident are you about this claim?
*  I would say quite in as much as if I wanted to create an AI that would be impossible for a,
*  or much more difficult for an interrogator to identify as AI or not, the first thing I would
*  do would be have it say, I don't know a lot more often than it does, right? So like the easiest way
*  for me to tell whether something's an AI or not is just to ask 10 very long tail random questions
*  and be like, no human is going to answer these questions all 10. Like it's just, wait, you know,
*  nobody has that breadth of knowledge. Actual people would say, I don't know. So I would actually
*  dramatically narrow the range of responses from the AI and make it seem much more conversational,
*  make it seem much more ignorant, make it much less useful for what you would actually
*  go to chat GPT for. But I think I could make it a lot harder for the expert interrogator to figure out
*  what is what. So anyway, that's like just one example of this general problem. I wonder
*  how you guys are thinking about that. I'll start from what you just said, and then go zoom back to
*  the question. The changes you mentioned could probably be enacted by just using a couple language
*  models that are policing each other. And you could basically get to a system that actually behaves
*  this way right now. So I'm not very sold that that is the main threshold here. There's a quote
*  from Jaren Lanier that I actually used at the beginning of my thesis that was focusing on how
*  can we augment citizen participation in governance through natural language processing. I guess today
*  I would call it LLMs where he says, the Turing test cuts both ways. If you can have a conversation
*  with a simulated person presented by an AI program, can you tell how far you've let your
*  sense of personhood degrade in order to make the illusion work? I think this is quite important here.
*  Like being able to communicate on a certain pattern full of expectations is not what I am
*  interested in. I think that's a very, very low bar. In fact, like the goal of my interest base goes
*  way beyond, am I able to simulate something that is convincing enough in this closed box tournament?
*  Like this does not actually bring us a better world. From my opinion, I actually agree with you. I
*  don't really love the way the question is operationalized, but keep in mind they are
*  both from 2020. We will not always formulate questions so that they are optimally informative
*  years later, right? And I would say that in 2020 these questions, I mean you've said it yourself,
*  were in fact quite useful to the point that I would argue attackers probably moved the
*  Overton window with respect to how people were paying attention to the impact of AI. And I think
*  that is one value adds that's both hard to track but also intuitively resonates with me, which is
*  what also draws me here. So I think these questions somewhat serve their purpose. Now, zooming out of
*  the purpose question to like, okay, but can we have a better question? If we were to do this today,
*  these questions, instead of it being a single question, I think this should be shaped something
*  like the Minifaculous instance that we were talking about, where all of the sub parts of the
*  questions would have multiple different forecasts and they all together in an ensemble actually
*  give you a picture of, heck, we don't even have a clear definition of AGI to the point that the
*  question needs to operationalize itself one way or another, right? One of the projects that I'm
*  pretty excited about on the attackers is to come up with indexes. Basically, come up with just the way
*  you can aggregate a bunch of stock tickers to come up with a composite view. I would like there to be
*  30 forecasts that are all really zooming in on slightly different aspects of this
*  and them all together is what you're paying attention to. Now, you can say, well, I want to
*  rigorously link all of these through causal diagrams and then you will get into a whole
*  different hairball. Sure, that could be helpful if you pull it off, but even a lesser fidelity
*  version of this that is just here is 30 forecasts that all rhyme with each other with respect to
*  its focus point will be able to shed more light. And I think at that point with what Metaculous had,
*  that was possible and these questions did serve their purpose. It's a challenge of forecasting
*  the future, right? We don't always know what formulation for a question will be most useful
*  years from now. For example, we're doing the five years after AGI question series that just launched.
*  I am much more interested in that, for example, because when I look at the answers there, it
*  actually gives me a much more accurate view of what people even conceive of as AGI. The way I am
*  using those questions isn't about thinking of, okay, will these things happen when AGI hits?
*  It more so informs me, okay, these are the things that people consider as critical possibilities
*  within AGI. And just doing a throwback to some of my prior work with AI Objectives Institute,
*  I often find there to be, if we are talking about AGI and AI alignment without talking about
*  the societal context in which this has impact, I think we are narrowing this down. Like for example,
*  there's a common meme that we would use in AI Objectives Institute to talk about what a
*  successful AGI that can enable human coordination is. In the world that is post-AGI, if you don't
*  think Jerusalem will be a united and peaceful city, maybe your AGI isn't ambitious enough.
*  Maybe something that is truly AGI would be able to resolve clashes and cruxes within existing
*  human sphere where it's not trained to make sure it is perfectly neutral towards that, but instead,
*  it augments human agency that actually brings a meaningful change. Because otherwise, sure,
*  I can relate to a system so it can say, I don't know enough time so that you might find that
*  convincing. I find that to be a lover. I think we should be more ambitious.
*  Yeah. So how much editorial do you exercise over these questions? Because it does seem like these
*  couple of questions have become a bit of a shelling point and it's a delicate decision
*  probably from your perspective. Do we take a proactive step to retire a shelling point
*  because we feel like it's outlived its usefulness or do we just let the community gradually move on?
*  I wouldn't say that at all. I think these questions are good. I am much more interested in pushing it
*  further. I guess it's also a call to action slash ask for help for everyone that loves
*  Metaculis or is interested in this. As we launch MiniTaculises, which are focused instances,
*  if you have different formulations that you think are interested, come tell us. We already get a
*  lot of inbound questions that are around, like, hey, can we write the question? We heavily
*  editorialize them for we do want to maintain a level of rigor. So far, I think Metaculis has
*  been much more closed than what I would like it to be. I would love for there to be many more
*  people that write questions, especially domain experts, especially people who say, you know, hey,
*  I get the hang of what a question is resolvable and meaningful. And these are things we can help
*  with. But we are entering a chapter of Metaculis as we are open sourcing to get many more people to
*  write questions, to have instances that they are hosting that have maybe different scoring
*  mechanisms, different levels of rigor to the point that it actually proves useful to them.
*  We will also host at Metaculis.com many instances that are very domain specific.
*  So I just think we need more questions. It's not about going back and changing what this has
*  accomplished, but more so bringing on new lights. Like, for example, I'm quite excited about a bunch
*  of new technologies that could actually bring better results. Like I love a lot of the more
*  symbolic base, like, are we able to use language models in order to come up with specification
*  criteria and use that to create safeguard AI systems? I'm interested in like, singular
*  learning theory, there's a bunch of new techniques that actually, when I imagine versions of
*  AGI or weak levels of AI competency, even that is really good at these, the ways in which I
*  envision those features are substantially different. And I'm quite interested in exploring these. And
*  I think that just requires a breadth of more questions to forecast and also more human energy
*  or AI energy to be able to forecast on these questions. So anyone that is interested in
*  saying, Hey, I have things I want to forecast, I have a formulation that I think is better.
*  Come talk to us. How do you create density though? Right? I mean, the one worry that I would have if
*  I was you, and I got a million new questions in is now I need like, a billion predictions, right,
*  to actually create a meaningful community forecast for all those million questions.
*  So how do you think about balancing like the diversity of questions versus the density of
*  forecasts? Right. Great question. Where the AIs can come in, we'll get there.
*  Yeah. You know, nail on the head, like the real currency here, the real limitation is human
*  attention bandwidth, right? I have 10,000 questions being launched at Metaculous every day.
*  It's not going to help anyone, at least until like everyone is forecasting part time as part
*  of their job. Like that's not what I'm trying to angle towards here. But this is why we need to do
*  active research on questions like, can we build indexes that aggregate a bunch of different
*  forecasts? Can we have AI start forecasting as part of the AI benchmark tournaments, we've had
*  an explosion of AI contributors. They seem to be doing okay. And like, can that create the scaffolding
*  or a jumping off point for humans to be able to get to a rigorous forecast much faster? There's,
*  I think, a lot we can do to increase the quality. We have 10,000 new forecasts every day. I think
*  that just will drown any kind of quality from the system. And the wind condition also isn't, you know,
*  well, AIs are forecasting and humans are just watching. I think the question is more around,
*  are we able to identify what are the best questions? And I want that to happen with more people,
*  not just the Metaculous team. And I want the contribution of the botch to be able to gear
*  towards shedding more light and more information and have these questions be incrementally
*  composable, so that we can build world models of all of these are rhyming with respect to how we
*  are thinking about electric vehicle proliferation, for example, and using those, then we can have much
*  bigger questions like forecasting specific windows of electric vehicle proliferation in China is
*  quite specific. But if I have 30 of those questions, I can then make something aggregate
*  that says, you know, will electric vehicles be better for the environment? It's like, what does
*  that even mean? But like, it actually means a composite of all of these different things. This
*  is a different frame of reference for thinking about how we can aggregate them. Cool. Well,
*  that's great motivation then to get into kind of what the state of the art is in
*  LLM powered forecasting, and then the tournament that you're running to try to advance that state
*  of the art a little bit further. In preparation for this, I read through three links to papers
*  that you had shared. And I was overall pretty impressed. And you can give me more detail on
*  what you think is most important or stands out or what the kernels are that you really want to build
*  on. But it seemed like across the board, pretty positive results. And these are from serious
*  authors, including Tetlock has been involved in some of this research. Just to summarize the three
*  papers, the first one was approaching human level forecasting with language models.
*  And this was from Jacob Steinhardt and his group. They basically created, I guess what I would
*  describe as sort of the intuitive thing that I would create if I was going to work hard on trying
*  to make this work. And that is like a retrieval system, the ability to go on the internet,
*  search through the latest news, process that, and ultimately create forecasts. And it seemed like
*  it was pretty good. It was like coming close to the community forecast, although not as good as the
*  overall community forecast. A question that I did have reading that paper, which I don't know if you
*  would know the answer to is, okay, it was a little bit short of the community forecast, but how does
*  that compare if it were an individual human? At what percentile would that system have
*  performed? I don't know if you do know that, but my intuition was that it would be pretty high as
*  like the percentile of individual humans. Right. I mean, let me give you a thing that I do believe
*  in that I don't have data, but I think we will soon have data for this is that part in the hands
*  of a team of human forecasters will just kill it. Like that is obviously going to be much better,
*  right? Going back to the question of usefulness. I like the academic rigor aspect. Don't get me
*  wrong. I do think testing these in isolation is good. And a lot of our designs around AI
*  benchmarking for competition pays attention to that. But the part that already is obvious to me is
*  let's actually look at what these systems are good at. They're good at going through massive
*  amounts of content, identifying which parts may be relevant. They're good at taking a first step
*  at creating a world model. Let's actually build systems that pay attention to those first and
*  build on top of that. I particularly like the Schoenhardt lab, the Halloween paper for a lot
*  of intuitions that I would like to explore further is in that paper. And a lot of folks that have
*  asked me, I want to compete in the tournament. What should I do? I always point them well,
*  start from here and then try different things, try different ensemble methods, use different
*  language models. Don't share prior data, have them debate each other, have a third model,
*  look at it and synthesize them. There's a lot of playful strategies that work in Govets. So
*  I really enjoy thinking in this framework. So I've been encouraging. There's a very active
*  discord, by the way, for the tournament where people are discussing strategies. It was absolutely
*  delightful to see how much the models have evolved in just like the three weeks of the tournament
*  kicking off on different strategies people have come up with. And we do encourage people to update
*  their models. For the tournament, there shouldn't be human in the loop because we're trying to
*  benchmark the state of affairs. But if they have a better strategy, they should update that.
*  Another thing we do is reasoning transparency. Like, have the models post at least some form
*  of text. We don't grade or score this because it is a whole different level of complexity for that.
*  Let's stay with the forecasting accuracy, but that at least gives us a way in which how the
*  model is thinking. And a lot of earlier research on chain of thought reasoning has pointed that
*  explanation is actually what gets these models to be able to stay further grounded. So to me,
*  these things are really good. A couple other avenues that I don't think has been explored
*  as much lately is how can we bring in model based reasoning on top of language models
*  that will actually yield much, much better results. Even in the first few weeks, we have what? 15
*  questions that have resolved so far, I think. In that signal, we've had plenty of questions that
*  have, for example, tests like scope sensitivity or negation. Ask the same forecast, ask the
*  opposite, see if the answers are the opposite of each other. For example, there was the measles
*  question. If you ask the bots, what will be the number of measles cases? Less than 200, they'll
*  say 75%. 70% for more than 300. And that means there should be 5% chance that it will be between
*  200 and 300. And bots will say 65% for the window that's between 200 and 300. Obviously, a pro
*  forecaster wouldn't make this mistake. But even an ensemble method falls apart on this case because
*  it doesn't keep track of here is a world model that is mathematically rigorous. Now, why is this
*  interesting to me? Humans wouldn't also be able to do a very good job at tracking this if they were
*  much more complex. Obviously, a pro forecaster is trained to get better at it. But if you ask this
*  to someone that is not a highly numerate child, they would be like, oh, maybe it's the same. Oh,
*  I didn't realize that this is wrong. That means there's something intuitive about how humans
*  reason that is distinct from the mathematical rigor here. How can we close that gap? Like,
*  if we are able to incorporate model-based reasoning, and I think this can happen with
*  approaches like open agency architecture or even like a simple squiggle integration,
*  I'm super interested in that, to be able to say your forecasts as you bring in more and more
*  information from a language model is building a world model that also has a mathematical grounding
*  in which you can enforce things like scope sensitivity, negation sensitivity, etc. There,
*  I think we will actually have a lot more paradigm shifts. And this goes along with an intuition
*  that I would like to be much more explored for building safer AI systems, which is, and we have
*  language models to be used in order to come up with rigorous world models that can be interpreted
*  because they are mechanical. And there are papers on this front that I think have explored this in
*  different ways. For example, there's the Tannenbaum lab at Stanford that's published a paper called
*  From Word Models to World Models. It was about a year ago, so there's plenty of work that come on
*  top of that. Are we able to build probabilistic programming language support? So using LLM to
*  come up with a world representation where the world representation is both consistent
*  and also interpretable. Can we use this as a starting point to come up with much better,
*  much more robust worlds of AI systems that are getting more accurate, that are getting more
*  logically consistent? I can go a little more technical if you're interested. For example,
*  can we come up with auto-formalizing option spaces? There's a finite set of proposals.
*  There's a constant positive number that is the total budget. Say we're trying to do a question
*  of budget allocation. The option space has many finite functions that the sum of all over the
*  actions needs to be less than or equal to the budget. An LLM is not going to parse that,
*  but an LLM might be able to get better to this if you're thinking about taking natural language
*  description of a decision situation and produce a formal description of the decision variables,
*  constraints in the language optimization framework. A ton of research, like use something like
*  CVXPy. There's a bunch of libraries that would get this better. We can do structured construction
*  of option spaces. Are we doing a simple choice question? Are we doing a matching problem? LLMs
*  would actually be good at figuring out, oh, the thing you're asking me seems to match this kind
*  of problem and then help parse into that. That way we actually have a world model that we can
*  inspect that we can see, okay, these parts are right, these parts are wrong. Can you improve this?
*  And have the human continue with just verbal intuition rather than need to keep an Excel
*  spreadsheet to see if all of my intuitive probabilities are tracking. But instead you're
*  able to say things like, these are my intuitive probabilities. Can you figure out where I am
*  logically not consistent? Like this would help a forecaster right now. Here's all the data that I
*  have. Here's 30 forecasts. Maybe these 30 forecasts have some logical inconsistencies between them.
*  Can you do better? If we can help language models get better at this, that composite system,
*  I believe, will yield a much more reliable, much more safer AI model as well. And if we extend that
*  further and further, we actually might end up with AI systems that are interpretable, that have
*  reasoning transparency, that have distinct parts of world model building, exploring option spaces,
*  eliciting preferences and desirabilities from people that you can look at and see, oh, this is
*  how all of them are talking. If you're just trying to get one LLM or a bunch of LLMs,
*  not so much. Maybe through breakthroughs on mechanistic interpretability, we might be able
*  to get there. So I believe these kinds of explorations will actually yield much better AI
*  forecasting. Yeah, cool. So that's awesome. I want to just for closure for people who wanted to maybe
*  hear those other two papers, I'll just mention them briefly. Because I think if you're going to
*  get into this tournament, you should look at the Halloween Steinhardt paper for sure. That's like
*  your kind of jumping off point, well done agent with retrieval, with fine tuning,
*  with a good scaffolding to spit out good predictions. That's one that I mentioned before,
*  comes reasonably close, but still falls short of the community prediction. Then there are two from
*  Tetlock and co-authors. One was pretty interesting around just giving people access to an AI assistant
*  and seeing how that helped them as humans forecast. This is kind of the big picture,
*  a small step toward the big picture vision that you're painting. Interestingly, they ran an
*  experiment where they gave the best assistant that they could give to the participants and then also
*  a deliberately biased AI assistant. And they found that both helped, although the biased one didn't
*  help as much. That's an interesting finding. And also an interesting argument in that paper
*  about how this look at the future. I mean, you could think like multiple reasons for why
*  AI forecasting could be useful. You've made the case that obviously we would like to have a better
*  sense of what's going to happen. We would like to be able to make better decisions. They also make
*  kind of an argument in that paper that the study of what language models can predict is also kind
*  of a useful way to interrogate to what degree they can get out of distribution, which is a very
*  hotly debated topic within the study of AI. Some level by definition, if you're predicting the
*  future, you're out of distribution. And the fact that they are doing it reasonably well is
*  definitely, at least some points for a team, these things can generalize beyond their strictly defined
*  training data. Then the third one, also from Tetlock and a number of the same authors, is
*  just an exercise in ensembling the different language models and finding that the average
*  of the language models performs better than the individual. So it's kind of wisdom. In fact,
*  that's the title of the paper is wisdom of the silicon crowd. That one was interesting to me.
*  I mean, they did, as you'd expect from a Tetlock publication, they re-registered all their
*  experiments and were very rigorous about declaring exactly what hypotheses they were going to test.
*  It did jump out to me from the data that GPT-4 was way outperforming the other models. And
*  if you wanted to make a really simple improvement on their method, I would just cut the worst models
*  and take one or a few of the very top performing models and just kind of run multiple copies
*  of those. A couple interesting notes there around bias toward round numbers a little bit,
*  bias toward positive resolution, some of these things that you noted where there was
*  some logical inconsistencies. And they were also hard. Another note I had on that paper was
*  it really shows the breadth of AI knowledge off in a powerful way. Because I was looking at some of
*  these things and I'm like, I don't even know the person. It might be a leader of a country or
*  whatever. And I don't even know who that is as we begin this discussion. So the fact that the
*  AI's are just jumping in and making predictions on such a wide range of things is a good reminder of
*  some of their fundamental strengths. So, okay, that's all background and hopefully breadcrumbs
*  for people that want to get into the tournament. If I may comment on them a little bit, I think
*  the conclusions of these papers do make intuitive sense. And I'd love to see much more rigorous
*  tests of this. Like, for example, what you said on well, cut the worst models and maybe that'll
*  get you better. Maybe, but I also want you to keep in mind, like, if your goal is to have better
*  forecasts, probably the kinds of things that will make mild leap is going to be things like,
*  look up if there has been similar questions asked on a variety of prediction platforms.
*  Like, that is actually instrumental and shifts out of an academic mindset of the rigor towards,
*  like, what is actually instrumentally helpful here? I do think a lot of shortcuts are actually much
*  more around like, okay, how can we get this to be further helpful? So those are the things I'm
*  really interested in getting more folks to explore. Ensemble methods are great. Like,
*  wisdom of the crowd works. Wisdom of silicon crowd also would probably work as a result.
*  Like, try different models. Try the same model. Figure out if these models are good at specific
*  domains or if they're avoidant on specific questions. Like, there is so much juice there.
*  And as we have better models, also the conclusions will shift continuously, which is why
*  I think a benchmark like this will actually be really, really helpful.
*  So let's get to the contest. You've alluded to the competition, or I guess we should maybe properly
*  call this a forecasting tournament. You've alluded to that a couple of times. I would maybe love to
*  start with just kind of a rundown of like, what the setup is, what the rules are. There's prize
*  money available. So just give people a sense of like, what they would be signing up for it and
*  kind of the specific nature of the competition. Yes. I am pretty excited about this competition.
*  It's called AI Forecasting Benchmark Series. The competition will last for an entire year,
*  where every quarter we will have new questions that get launched. And for this quarter, we will
*  ask about 250 to 400 questions to the AI systems that are forecasting. We have about 120k prize
*  money to be allocated across the entire competition. And yeah, I would love for people to participate.
*  A couple of learnings that I've had just looking at the competition is even very simple bots seem
*  to be doing really well. And this might be that their prompts are better. This might be that
*  they're paying attention to better news sources. So it is definitely interesting. And without a
*  lot of effort, I do think it is possible to get something that is somewhat competitive.
*  Now, what is the tournament? In a way, it's a typical Metacos forecasting tournament, but
*  it is specifically geared towards bots. We encourage people to build bots that use multiple
*  LLMs. And we will use this as a benchmark to compare against pro forecasters and also the
*  community aggregation. And it's the first of its kind to be done at this scale. The basic rules
*  are that you cannot have a human in the loop. You can change your bot, but you cannot make specific
*  adjustments to the bot. Bots have to leave comments to showcase reasoning. We won't score the comments,
*  but it will be good for us to see what are the winning bots doing. So just quick clarification.
*  When you said you can change your bot, but you can't modify it, that means you can update it
*  periodically, but you can't adjust it for a specific question. Is that-
*  Exactly. Exactly. Adjusting it for a specific question basically defeats the purpose. At that
*  point, it has human in the loop. I do believe human in the loop systems ultimately are going
*  to be better. Just like how competition is good, collaboration is good, but a competitive
*  collaborative system where you have teams that can collaborate in competition is better. This
*  tournament, we're not looking into this. We do want to see AI capabilities on their own,
*  in their own footing. Hence, you can update if you come up with a better strategy. And especially
*  the writers of the winning bots, we will interview them and ask them, what was your approach? We do
*  encourage people to share these systems if they would like, but they're not expected to do so.
*  They will provide some description of the bot or the code if they would like so that we can see
*  what works and what doesn't. Yeah, this will create a benchmark that is continuously evolving
*  and also it's a benchmark that kind of cannot be cheated for. We literally don't know the answers
*  to all of these questions. So it is really fun. It evolves every day. Every day you look at it again
*  and see how your bot is doing. Is there something that is missing? So I find it pretty fun personally.
*  We have created a template that people can follow that is fairly simple and straightforward
*  that you can use to just start with a one-off system, but on top of it, go to town. There's
*  a lot that can be done. Try the ensemble methods, try model-based reasoning systems, bring on news.
*  One of the things, for example, that I saw, I touched on this earlier a little bit,
*  if a human forecaster is forecasting and trying to do well, they will Google and look up other
*  forecasting platforms to see if there are similar questions. This was something that the bots figured
*  out pretty fast, or the bot writers rather. So I'm really happy about these kinds of explorations.
*  Yeah, so that is the rough rules of the competition. Fairly easy to get started. Oh, also,
*  both OpenAI and Anthropic have donated a fairly generous amount of credits for the competition.
*  So for anyone that would like to get credits, because there's a lot of questions to forecast,
*  I think we can cover all of the needs. So the process is ping us either on Discord or send
*  us an email. You can email me, Degger at Smithaculous.com or support email for it. It's
*  all on the website. And say, Hey, this is the kind of thing I want to try. Can I get credits?
*  And I'm pretty sure we can give you plenty of credits to support you. So yeah, I find it to be
*  like quite exciting. All the questions are binary questions. They're going to resolve. Yes, no. Is
*  that right? Can you give us a few examples of early ones that have already resolved?
*  Yes, I want to say all the questions are binary at this tournament. We will have non-binary
*  questions soon for the next round, which will be Q4. The tournament will happen in every quarter.
*  And you get scored on the questions you forecast. So a lot of folks have asked me,
*  am I too late to participate? I missed the first few weeks. Actually, not at all. We have some
*  people that are high on the leaderboard that have joined fairly late. So I say join now and also
*  try things now because we will just cover your credits anyway. So when Q4 hits, you can go in
*  with a bot system that you have rigorously tested. So what are the questions that have
*  already resolved with respect to like the prime minister of France? Will that belong to a coalition
*  other than the new popular front or together? Like a lot of election related questions on France
*  have resolved already. Domestic box office question. We have one on Deadpool and Wolverine.
*  Will that be higher than that of Deadpool? Resolve? Yes. It was interesting for the bots,
*  did better than humans on this one. Joe Biden, you know, what will happen for the Democratic party?
*  We had a bunch of questions on that front. One thing we have done that I think is really
*  interesting is in the main quarter lookup, we have questions that are, for example,
*  continuous variables. Like I'm looking at one of the questions between July 17 and July 28.
*  What will be the strongest geomagnetic storm of a KMXL? For this tournament, for example,
*  we have discretized this continuous variable question to say things like, will it be greater
*  than four or less than or equal to six? Greater than four less than or equal to five. Between five
*  and six. So we have turned continuous variables into binary questions. And that way we can compare
*  it to, you know, is there logical consistency here? But also how does this compare with human
*  forecasters that are looking at this? So a couple of tricks that we have placed in there to be able
*  to make sure we can stay with a purely binary forecasting tournament. And next quarter,
*  we'll build on top of that with more complexity. So is the structure that the people submit their
*  bot, then you guys are going to run the bot for them on a daily basis as new questions come out?
*  Are they going to answer each question once or are they sort of going to be repose the questions
*  either daily as they go until they resolve? And then do they provide a, I assume it's not just
*  a simple yes, no, but it's presumably a percentage. And how does the scoring work based on that number
*  that they give you? The scoring is the same as any binary question that we have done on Metaculous.
*  It will resolve this or no, and we will score it accordingly towards that. And we will score
*  the ensemble on top of all. We are only doing binary questions here, but the process is basically,
*  we don't host their bots, they host the bots and we will open questions. Every question will be
*  open for 24 hours. So you will need to continuously forecast on top of that. We have made that process
*  fairly easy. If anyone has any questions, they should take a look at the onboarding process.
*  It would take maybe about 30 minutes to spin up a very simple bot. But yeah, so you need to submit
*  through the API your forecasts to the question that open and close every day.
*  Gotcha. So people are running their own bots on their own computing infrastructure.
*  Yeah. Basically we have some folks that are actually competing with bots that have value in
*  form of a private IP. We don't want them to just say, well, you need to give us what you have. Or
*  if you have built something really interesting that you want to monetize, we do want to encourage
*  that. So I think it would be very interesting for everyone to just submit their bots. But also
*  at this point, at this stage where the current LLM capabilities are at, I would rather have people
*  to have much more ease updating their bots. Like I want to see things like, oh, this bot seemed to
*  be bad at scope sensitivity, but it got better. I'm curious, like what tricks did they do? Or that
*  I'd rather have the bot be still in the custody of the person that is building it. Does that make sense?
*  Yeah. Is there a way, are we working on the honor system? Or is there the possibility that people
*  could have a human in the loop as they submit their stuff? The reason I assumed that they had
*  to submit the bot was so that you could guarantee that they wouldn't have a human intervention
*  in the process. In this tournament, we have discussed this quite a bit and we decided that
*  this will go with an honor system. One of the things we have is the number of questions to
*  forecast is quite high actually. So somewhat this incentivizes a human to forecast about
*  600 questions that are just being bombarded. It's a lot of work. And another reason why we want
*  people to submit their reasoning is that if there is human intervention, it might be much more
*  visible through that, especially for the winning cases and the high volume of questions. I do think
*  we will scrutinize them heavily. And if we do have reasonable suspicion on that front, I'm sure we
*  will have further investigations. But for this tournament, we decided to go forward with the
*  honor system rather. So we do encourage people to abide by the norms because they'll be contributing
*  to a meaningful benchmark that way. Otherwise, it provides a cheat.
*  I guess the other thing is that the general prior assumption is just based on all the research that
*  we talked about a few minutes ago, that you might be able to add a bit, but you're not going to add
*  even over the baseline AI performance, an individual is not likely to add that much.
*  And you might even make it worse in some cases. So it's not an obvious advantage to be unlike,
*  for example, the ARC challenge where if you had a human intervention, there would be a clear reason
*  to think that you would have a big advantage toward the prize. Here it's much less obvious that
*  a human can actually improve on what their bot is doing on its own.
*  Exactly. And to be honest, this is fairly early to make any conclusive statements and kind of hope
*  that this will change. But we have a couple of questions where the bots did better than the
*  aggregate of pro forecasts. And I'm like, oh, this is very interesting because they clearly are
*  failing on things like scope or negation sensitivity. But on questions where that's
*  not the primary mechanism, they seem to be able to do something that is powerful. I think people
*  should try not messing with it. And one thing is every quarter we will have a different tournament
*  that will have its own sets of rules and norms. So I am interested in actually exploring different
*  mechanisms here as well. We have an active discourse, so if people have ideas, I'm like,
*  hey, this kind of competition would be much more interesting. I'd love to chat with them and
*  hear what their ideas are so we can try different things. But like the goal of this is to be able
*  to benchmark AI capabilities and see if this can be an early warning system that would actually
*  substantially help the role forecasting plays in the game. You said a minute ago that the scoring
*  is like standard scoring, but just in case I don't know exactly what that is, my intuition is that
*  it would be almost in the way that like a neural network might be measured for like a classification
*  task, sort of sum of squares type scoring. Is that right? Is your question like how the scoring is
*  for binary questions? Yeah, exactly. Yeah. Thinking about this way, we're basically comparing the
*  forecast to a coin flip in the context of the forecaster. We're using log loss versus a coin
*  flip. And the peer score is basically how your baseline score, which is the log loss compared to
*  the coin flip, compares to everyone else's. So that way we have a proper scoring rule that's used
*  based on log scores. The reason why we designed this way is that it rewards the forecasters for
*  beating the crowd and incentivizes both like do research and understand the crowd, but also report
*  your best guess rather than say things like, I want to be 10% above whatever the community
*  prediction is. Does that make sense? Yeah. Are you penalized by that for overconfidence? Like if you
*  put a one on something and you're wrong, is that like very costly in that scoring system? So you
*  need to be more accurate with respect to how you envision the world. That way we don't drive towards
*  the far edges, which is something you see in prediction markets that have financial incentives.
*  So this actually combats against that. That's why I was saying like, if the market or community
*  prediction is at 60% and you believe this is correct, you should say 60% because if it is
*  accurate, then if it turns out to be a yes, like you will be not penalized. But if you don't think
*  this is the accurate guess that you could make, then you should not say it's 60%. While in a market,
*  if you're trying to maximize the financial outputs, where the market is at isn't something
*  meaningful to that. Yeah, gotcha. And you get all the questions at once as well. Is it within the
*  rules to have the system consider all the questions to try to deal with the sort of
*  possible inconsistencies? Can you repeat what you said? Yeah. You said that you have like a
*  number of questions that are related where you've kind of discretized a continuous variable or
*  something. Are you supposed to just consider each one, one by one and give a prediction or
*  can you kind of consider them as a family and impose checks on like, if there are related
*  questions, you know, make sure my predictions are self-consistent. I mean, I hope that's what
*  the contributors do, right? I want a human forecaster and a bot to be able to do that,
*  which is precisely why we're asking these questions this way, because it is very hard for bots to be
*  able to do this, unless you have come up with something that is much more robust. So I also
*  want to see if they get better at doing this over time through the next year. Will simpler
*  models be better at scope sensitivity or negation sensitivity? But yeah, like a human pro forecaster
*  will obviously say, oh, all of these questions are related. So let me come up with one answer.
*  It wouldn't be very difficult for an AI system to start doing this by noticing these questions are
*  all connected. You can just have a simple LLM check that says, if all of the questions are
*  looking at similar variables, come up with one coherent answer. And then based on that answer,
*  answer each of the individual parts specifically. I'm curious how many contributors will do that.
*  And I'm curious if that will actually yield numbers that will be...
*  Yeah, we think it would help at least a bit.
*  Yeah, it should. Like, this is what I thought I'm hoping for.
*  Is there a leaderboard that folks can obsessively refresh instead of going to the election
*  websites every day?
*  Yes, there is. And I encourage people to check it. What's interesting is some newcomer bots have
*  already went up high on the leaderboard fairly fast, which is why I tell everyone we have easy
*  templates to get started. Just go and take your shot at winning the prize money. We do have a
*  large pool of money. And this will also be distributed across the entire contribution over
*  a certain level. So you don't have to get first place to get something. I do expect a lot of the
*  bots will actually be compensated in some shape or form. So yeah, bot performance seems high
*  variance enough and we have three more quarters. So I would say like, this is the time to get your
*  bot in shape, set up through the template, start testing and maybe you'll even win some money.
*  We will cover your costs. So the cash will be distributed along the curve rather than just the
*  top three. So it's not too late at all. I say give it a shot. My question to you is like,
*  what would it take you to make your own bots? I think you would probably enjoy it.
*  Yeah, I think it does look fun. I did read through the collab notebook that you have shared and
*  it does look really with that all in place. It's like, especially and also covering credits.
*  But there was one other little detail question I had was, is there a credit budget or any sort
*  of budget per question or is that's all up to you to manage on the participant side?
*  So in this tournament, we decided to not impose a max budget. I do think this would be interesting.
*  Like say if we said you only have $200 forecast for an entire quarter, but then like we're
*  intentionally inhibiting measuring AI capabilities. So that doesn't actually give us
*  the outcome we want. And that could have been a fairer competition, but that kind of defeats
*  the purpose. We have given up to 5k to some of the competitors and people have asked us to say,
*  can we get more credits? We asked people to describe the strategy they will try
*  and incrementally give more. So we decided to do it on an ad hoc basis because if we just
*  distributed that large we kind of can't keep track. But people that actually want to spend
*  a lot more budget, they can reach out to us. And what it will take is a quick email exchange back
*  and forth where they describe the phenomenon. And then we will keep a look at our day forecasting.
*  If so, we will keep on giving them.
*  Gotcha. Cool. Great question for me in terms of what would it take for me to get into the contest.
*  I think the biggest thing I'm probably missing right now is a sense of like, how do I improve
*  on the Steinhardt and group paper? And reading through that, I was like, this seems quite well
*  done. It seems like it's working quite well. And it wasn't immediately obvious to me how I would
*  make that better. So I would need to... And it hasn't been that long since I've read it. So
*  Eureka moments could strike any time. But I hadn't had an intuition yet around, oh, if I do this,
*  I think I can beat them. And that's sort of the moment of inspiration I guess I'm sort of waiting
*  for. Right. And a couple quick ideas I'd like to share is pay attention to other forecasts.
*  Any forecaster should start by Googling, okay, has anyone forecasted this? What's happening on
*  other platforms? Are there other questions at Metaculous? We do pay attention to make sure
*  we don't have another question that's identical for the tournament. But similar things will provide
*  a lot of light towards having a good base rate. So that, for example, or hook up for complexity,
*  pull up recent news, or try multiple different models and see how they compare with each other.
*  I do believe that fact-fetching versus coming up with base rates versus abiding by logic
*  consistencies, or rather than abiding by, I'll say leveraging that to be able to make better forecasts,
*  different models will have different competencies. I have found this is very anecdotal, and this
*  might change even if you use different prompts. I'm just sharing, you know, I tried this, not as
*  a research, but literally like spending prompting for a while. Anthropics seems much better with
*  respect to negation and logic consistencies compared to OpenAI. OpenAI is much more helpful
*  to work with me in trying to figure out what I should pay attention to in a question. So
*  come up with models that pay attention to multiple things, use llama models, use custom things,
*  you can even fine tune with prior forecasts. There's a lot that can be done. And I don't think
*  what will make the winning condition is going to be like, this comes from a multiple PhDs research
*  team that invented something really novel. I think it will be actually much more flexible than
*  that with respect to which one ends up winning. I don't know, my bet will be that something simple
*  will end up in the top three or top five, and we will say, wow, like, maybe we didn't need all of
*  that complexity. Or maybe we will find out like, yeah, logic consistency abiding by it will yield
*  much better forecasts. So you definitely need to pay attention to that because that was the
*  determining factor. There's a lot of conclusions we can get. So I just my goal is getting people
*  to try out a bunch of things. It seems like the if I had to forecast on a meta level, the
*  result of this tournament over the next year, and definitely using the research papers as
*  point of departure, it seems like some sort of ensemble of these bots, which themselves will
*  probably be ensembles internally in many cases, it seems like we probably are headed for a world
*  in which the AI forecasts are in aggregate, very competitive with and maybe even surpassing to
*  some extent, the community forecast. And I guess maybe in closing, I'd love to hear like, first of
*  all, do you think that's true? And then, can you give us a little bit more, you've kind of sprinkled
*  some of this in throughout, but a little bit more about like, what that will mean? I guess I don't
*  have a great intuition always for like, how good is the community forecast? There's, you know, it's
*  still obviously not like a crystal ball. But if we could get that good, how good is that? How useful
*  does that start to be? Is it a question of, you know, just we need to if we had this level of
*  accuracy for everything, like, how much does that change the world? Or how much does that still sort
*  of leave us in a fundamentally uncertain state? Because this seems like this could happen,
*  especially as the tokens are getting extremely cheap. You know, we could really have with the
*  latest GPT-4.0 mini, especially if you do the offline batch process, 10 million tokens for a
*  dollar, folks. It's like, it's ridiculous. So yeah, like, what is the sort of epistemic future
*  you look like to you? I will answer from a different starting point, again, that harkens back
*  to what we started with, which is around, why is this you? If I was to tell you, we will end up in
*  a world where you will have an ensemble AI or the bot aggregate that consistently beats the community
*  prediction. Does that bring a better world on its own? I don't think so. I think the part with the
*  AIs that I'm pretty excited about is that it costs a couple cents to have them write an entire
*  research paper explaining their reasoning. I don't know if you'll buy the reasoning, but it is much
*  cheaper to probe and understand ways in which their conclusions come compared to humans. And
*  that to me is a paradigm shift. And this is already happening. Like, there's multiple companies
*  focusing on this, ranging from illicit to future search. I am interested in seeing how that will
*  give us better actionability. Bots in aggregate start to forecast better than humans, or human
*  plus bot ensemble systems are doing much better. I will again go back to how do we make this useful?
*  And I am excited that the LLMs will be able to create much more interpretable world models,
*  hoping that these world models will not be manipulative. Also hoping that these world
*  models will actually serve the goals of those that are trying to make value out of it. Which is why
*  some of the questions are fun and throw away. Other questions are actually quite proactive
*  towards specific goals. And we will have more of these to come up in the upcoming months,
*  like around questions of strategies on mitigating homelessness. Like, there is a lot that we can do
*  there. So if bots are getting much better than humans, then I think the question is,
*  how can we make this be maximally useful? We already have really accurate forecasts,
*  and we haven't had the Cambrian explosion of every single entity, corporation, government
*  perpetually uses forecasts. Because the frame of the forecasts has not proven to be helpful just
*  yet. Which is why I am really interested in this action oriented inflection point identification,
*  finding short term proxies, finding questions around budget allocation, working with hypotheticals.
*  Another side note here that I think might be worthwhile to go into, I think we should ask
*  questions that might not resolve. Like if I say, if San Francisco was to allocate $70 million for
*  improving public transportation, if they did X, if they did Y. Now, like this might not resolve,
*  this is probably not going to happen. But asking this kind of question and asking pro forecasters
*  to forecast on it, they might say, well, I'm not going to get a good leaderboard on it because it
*  will never resolve. But if I tell them, hey, this will be helpful for resource allocation,
*  doing this for questions on Taiwanese sovereignty, doing this on questions on AI,
*  will actually let us explore hypotheticals, counterfactuals in a way that will bring a
*  lot more strategic information. So these are spaces I would like to go to. And if bots are able to
*  bring a level of reasoning transparency, that is great because that will make it much more actionable.
*  I hope it checks out. I hope it doesn't end up being the uncanny value of seems legit,
*  but not necessarily correct, but is too hard to scrutinize. Like that failure mode would be what
*  I would be afraid of here. And in a way, we already live in a world that encourages that, right? Like
*  we have legal documents that are, unless you speak legally, you won't understand it. So you need to
*  defer. The failure mode here is like, yes, there is something that all of these bots are able to
*  converse with each other that we see as like, somehow this has higher epistemic status than
*  what a human can access. Like at that point, I think we are in the failure mode of epistemic
*  security. I would like to dismantle that possibility, which is why I'm excited for LLMs to be able to
*  help say someone that doesn't understand anything legal that doesn't have money for a lawyer to be
*  able to make sense of a contract or for the medical sector, for insurance sector, for science.
*  So there is a world in which these tools can actually get us towards better reasoning and do
*  it be individual or in a collective scale where we're aggregating multiple perspectives. I think
*  same as wild for forecasting. Like if we do this well, it is quite a paradigm shift that is going
*  to be super powerful. And like the failure mode is basically like pushing humans further and further
*  away from having access to that. I think the benchmarking tournament gives a little bit of
*  light towards that and hopefully more and more as the upcoming quarters will have more rigorous
*  questions that go beyond just binaries. So I'm excited to explore this. I presume many folks
*  that are listening have been curious about setting up their own LLM bots or getting more
*  facility with LLMs, trying prompt chaining. I think like this is a skill set that I see a lot of people
*  around me wanting to cultivate more of. I would say like this is an unusual moment. It's a powerful
*  opportunity. You have outsized price money. You will contribute to a benchmark and it helps you
*  build capacity that you would want to do anyway. Plus we will cover your credits and we have some
*  templates. So I would just say like tell people, hey, like come along. We need to figure this out.
*  Cool. I love it. Is there anything else that you wanted to touch on that we haven't got to?
*  I mean, I just want to say I am especially interested in folks that say, hey, I have a
*  different vision with respect to how forecasting can be helpful. Do reach out to us. We're quite
*  interested in seeing different experimentation and testing out some of these experiments where we can
*  both financially incentivize people and try things out. We will be open sourcing the tag
*  illustration. So I'm very excited about more people to try things out. So that is another thing
*  I would like to underline. If you have ideas that you want to test, holler or I'd be very curious to
*  hear them. And yeah, hopefully we will have many more instances, many more ways in which people
*  will try to make use of forecasts. Yeah. I wanted to ask also, that's a good reminder. What is the
*  future of the company? Obviously open sourcing, important strategic decision in terms of like
*  gives a lot of value and a lot of opportunity to others. How do you see that sort of shaping
*  what your own possibilities set is as you go forward with the company itself? I'll start from
*  before I joined as CEO, I was wondering why is this not open source already? I do think there is a lot
*  of wealth here and one way to get more people to be able to both like critique and audit, but also
*  host their own versions. Like this is something that is a net good towards the entire humanity to
*  be able to do much more of this. And Metacos will focus much more on ways in which forecasting can
*  be useful for both decision makers and understanding more robust world laws, which is why
*  questions around better reasoning transparency and action oriented decision making for those that
*  are trying to figure out what's the best way to allocate resources or which policy seems to address
*  the needs of a community. Will this policy, if enacted, actually yield the impact? So we're
*  interested in much more collaborations on this front with folks be in municipal to federal agency
*  government beyond some of these partnerships already in place. I'm interested in ways in which
*  this would also help businesses to be able to make better decisions and keep track towards the goals.
*  So these are all spaces that we will highly prioritize. We're entering a window of a lot
*  of experimentation actually on seeing like what are additional things on top of the
*  forecasts as they exist right now would add value. So the minute calculus is that we were talking
*  about is just one of the many examples here building indices is another like looking into
*  things like tech trees that foresight Institute is building on seeing, okay, for us to get to this
*  technical state, it looks like we have these in between things that need to be invented or researched.
*  Will this be worthwhile? Okay, if we put $5 million to this versus $15 million to this,
*  will we be able to go through these inflection points? These are the kinds of ways of reasoning
*  that I would like to see Metacos enabled. Is there anything that you worry about with this
*  paradigm? I mean, we just lived through this crowd strike disruption, right? Where like one
*  seemingly very local point failure like cascaded through society. And if I was going to take the
*  most risk oriented position on this, I might say something like in a world where, yeah, maybe we're
*  getting most of the time, even better than wisdom of the crowds forecasts from like, a couple
*  different AI models. What happens if they fail, not necessarily in terms of an outage, although
*  maybe but like, more so is there a potential for sort of a correlated failure that could create
*  weird scenarios, weird tail risks? How do you think about that type of possibility? Is there any way
*  we can get ahead of that? I mean, decentralization is key, right? Like, if everyone wasn't using
*  crowd strike, probably everything wouldn't have gone down all at once. And I'm sure a lot of people
*  have had the hindsight to say, well, I saw this coming. I've talked to a couple folks even that
*  you said, well, yeah, we switched out because we first said something like this coming up. I think
*  especially when you have institutional systems that are entrenching the use of specific tools
*  or specific flows, that ends up introducing a lot of failure modes, right? Like, if there is a
*  government endorsed supply chain flow, that will be much easier for a foreign entity to be able to
*  infiltrate and mess with causing supply chain related risks. There's plenty of those through
*  human history. I think like Metaculous being open source is good. I mean, obviously, I want Metaculous
*  to be the most accurate and that is the goal we're striving towards. But even more than that, like,
*  the proliferation of the perspective so that there is multiple people doing multiple focuses,
*  there is many different strategies, like, maybe for a specific domain, a different way of scoring
*  will work much better. And this will end up causing much more value for that. Like, for example,
*  just zooming back to something we said at the beginning of the podcast, decisions around
*  political outcomes is very different than say, questions like, should Biden step down versus
*  questions like, if we allocated an additional $50 million towards synthetic biology, which of these
*  will yield an inflection point? Now, it is interesting, like in the book, like Super
*  Forecasting, there's plenty of anecdotes of people are really good at forecasters can end up beating
*  domain experts. This doesn't mean we don't want domain experts. This means we want the forecasters
*  to work with the domain experts. So I think there's many different contexts in which forecasts can play
*  instrumental role, but they don't all look the same. So I think the real win for Metaculous is
*  actually bringing us towards this world where many people are trying many different approaches
*  and many different things. We will always strive towards the level of rigor and accuracy. But on
*  top of that, like, I would love it if there's a different thing that ends up building an AI ensemble
*  method that seems to be more reliable than Metaculous prediction. Like, at that point,
*  then the question is, okay, like, how do we integrate this towards usefulness? Like, that
*  wouldn't be a failure. It would, in a way, be a success for like, we have shown that this is
*  possible. So my answer towards failure modes through singular authority that has maximal
*  control is always well, decentralization is much better. And how can we steward towards that?
*  That's the question. Cool. Are you also interested in things like
*  Polis? Is there a sort of Metaculous Polis mashup or like, you know, what does it look like if those
*  concepts have a baby? Great question. It goes all the way back to my backstory. I would say Polis
*  is probably the most influential platform for evolution of my thinking. Right before Metaculous
*  at AI Objectives Institute, the project I worked on for longest was called Talk to the City,
*  which is an LLM assisted aggregation and deliberation platform that can take in
*  qualitative feedback. And in a way, this was what I was working on for my thesis. This was what I
*  was working on in my startup Cerebro also. So I have thought about this question in so many different
*  lenses. When you have raw text that is the highest fidelity human opinion, how can you augment that?
*  And through many iterations, first without LLMs, then looking at multimodal systems with text data
*  plus other data. And in the latest iteration with Talk to the City, what I have come to was,
*  okay, the current state of language models actually does a fine job in identifying what are the topics?
*  Are there any sub topics? And another thing they are really, really good at is actually the retrieval
*  of these concepts. Talk to the City still actually exists and it's going pretty well. We have an
*  excellent team at AI Objectives Institute, so I recommend the audience to check it out. Website
*  is ai.objectives.institute and they can see on the blog post a couple case studies that we've done on
*  impacts of Talk to the City. Like for example, one was with Taiwan. We've had an extensive
*  collaboration with Taiwan's Ministry of Digital Affairs where we were aggregating people's opinions
*  with respect to both local municipal questions and also larger scale questions on same-sex marriage
*  data. A lot of these data inputs come in from Polis. Now, Polis doesn't, like there's some
*  constraints there that is a trade-off for it. Ultimately, it's a recommender system where you're
*  finding people that will share certain viewpoints. Instead of leaving the onus to that, which causes
*  less human bandwidth, like you can only write about tweet-sized things, we said, okay, can we
*  have just completely unbounded input window where people can send in text, they can send in videos,
*  they can share any kind of data that you would be able to then enhance and see, okay, what does
*  this community talk about? What matters to them? And in a way, my journey to forecasting and to
*  Metaculous was me seeing, okay, we are actually at a place where we can aggregate public desirability.
*  I prefer the word desirability to preference because preferences can change. One might not
*  necessarily be aware of their preferences. You can have cyclical dependencies. I use desirability more
*  as a catch-all term that overcomes some of these. We can aggregate these. We can have a snapshot.
*  One project that I loved, for example, was with the labor union focusing on veterans' health
*  where they wanted to run a survey with respect to a specific proposition.
*  And the negotiation windows they have with the government is incredibly small. There's a 20-day
*  window where they need to come up with a policy, share it, and it will go through. The whole system
*  is basically rigged against internal deliberation. It's so narrow and so fast-paced that people just
*  say, whoever I voted for as head of the union should go forward. The new president of the union,
*  Mark Smith, ran a survey, open-ended text-based question to the entire population. Within 24
*  hours, I think we got maybe 200 responses on the first round, within 24 hours, we could turn this
*  open-ended survey in multiple languages, by the way, not just in English. You can get it in Spanish
*  and Tagalog and consolidate this to say, here are the four viewpoints that came up. What are your
*  thoughts? Send it back to the entire community and develop this recursive loop. It's so much
*  more interesting when you say, wow, between just yesterday when the survey went out, I already have
*  four clusters. Maybe I should respond to this. I have something to add to this one. Next day,
*  do it again. This cycle is much cheaper than what it used to be. I think this is a paradigm shift.
*  This changes governance. What I realized is, okay, now that we can aggregate this, what I need is
*  the next pillar, which is, will the action number actually get us towards where people want to go?
*  I was talking about this with Gaia, who was the previous CEO of Pentacolus, and that's how I ended
*  up here, eventually. I'm really excited about seeing how forecasting can help this. I think
*  there's a lot there. I think we need a lot more experimentation. Yeah,
*  Polis-like tools is, in a way, where I started thinking, huh, maybe there is a way in which we
*  can do better. I'm glad I remembered that bonus question. I think it does start to look like a
*  liquid democracy or a technology-mediated liquid democracy. That is definitely
*  super compelling. There's just not much room on ... We see this right now as we're going through
*  this campaign, obviously, in the US. It's like the things that are actually getting talked about
*  are few and not particularly well chosen in many cases. There's just so much stuff that really
*  ought to be ... That we want to understand what people actually care about, first of all, or how
*  they think about different things. We're just not even getting that data in the first place,
*  let alone being able to map a path toward actually delivering for people.
*  Absolutely. I think the big signal of red or blue votes in the US, we can do so much better than
*  that. That's why I'm looking at municipal engagements, membership-based organizations,
*  looking at DAOs, where they are making a lot of decisions around their stakeholders,
*  and the entire thing is on a digital substrate. There is much more experimentation here.
*  What you said reminded me of something with respect to liquid democracy. I must say the
*  term liquid democracy does bring some aspects of fear in my mind also, and I think it's worth
*  pointing that out. There's this concept that I call the consensus illusion. There is a drive
*  towards the lowest common denominator, that if we say finding consensus in a community is desirable
*  for that is the best policy. What you will end up is a lot of policy outcomes that are quite
*  lukewarm, that don't actually address the issue. There was a New York paper from DeepMind in 2022
*  on how can we fine-tune language models so that we can find agreements across humans that have
*  diverse preferences. One of my concerns when I see work like this, I think the paper is actually
*  great. Some of the techniques they use has made its way to talk to the city, so I like that.
*  Some of the concerns I have is finding agreement doesn't necessarily mean good policy. In fact,
*  it quite often doesn't. One example I like to give is one of the conclusions from a civic data set
*  is we should build more bike lanes for the community. Everyone seems to want more bike lanes.
*  You say, okay, where should we build these bike lanes? It should be on this street. The model will
*  say, no, no, no, that's not what we agreed on. It shouldn't be on a specific street. We need more
*  bike lanes. This is the thing. We don't want to make any specific streets narrower. It's just like,
*  oh, we're doing the same thing we've been doing with politics all along.
*  Find the most common denominator statement that yields power because in the current
*  intellectual system, consensus is power. So when you have a desire towards consensus,
*  that causes a trade-off with fidelity to your viewpoint. And if you seek power over fidelity,
*  you will have higher representation of a viewpoint that is not very meaningful. And
*  the most catch-all sentences will end up resonating the most and it won't make meaningful
*  policy. So I don't want consensus really. I want to start from a shared world model. Like,
*  can we actually come up with ways in which we have desirabilities for stakeholders? We have action
*  possibilities that come from policymakers. And then we have outcome likelihoods from domain experts.
*  And these three need to be continuously talking to each other as division of labor. I think
*  democracy focuses on the state desirability for stakeholders. But if the options you give is on
*  your roads, you can't really build a bridge. And people need to be able to say, I want to also be
*  able to build a bridge. And an AI model that hampers this by finding, oh, this is the most
*  agreeable thing is not good. Instead, I'd much rather have an AI model whose goal is come up
*  with individual viewpoints that are clashing with each other, represent each of them with high
*  fidelity and identify what are the cruxes between these viewpoints. Like if we can find the good
*  crux where like I think A is true, you think A is false, but the underlying cause, if I thought the
*  underlying cause changed, this would change my mind about A and you would say the same thing.
*  Like the typical double crux process is good because that means we actually have a same shared
*  world model and we need more data. And at that point, bring on further research, bring on
*  forecasting. We're in a good mood. The failure mode here is a risky alliance where someone says,
*  oh, I think policy A is good. You say, I also think A is good. And I say A is good because it
*  will enable B, which will be great. And you could say, I don't think B is likely to happen as a
*  result of A, but maybe we should keep together because it seems instrumental just for this one
*  step. You end up having a lot of unlikely alliances. And the ultimate version of this is a
*  completely polarized society where for some reason social conservative and fiscally conservative
*  behavior is correlated with each other, even though that doesn't necessarily manifest.
*  There was one research that I read, I can't remember where, that I just absolutely loved,
*  which was instead of asking people their opinions with respect to immigration policy,
*  it actually asked a statistical question on how many people are you willing to let in
*  before you reject someone that truly deserved to come into the country? And the previous people
*  that you have let in might be mistakes. This is very interesting because instead of people saying,
*  well, I am liberal, I am conservative, you see people who say they are liberal, you know,
*  San Francisco crowd that will say, yeah, I'm willing to let in five mistakes before we admit
*  one person. And others will say, what do you mean five? We need like 300. But both of these
*  people see themselves as having a liberal opinion. Like we do not yet operate on a level where we're
*  looking at good policy. So we should not encourage these illusion of consensus so that it can serve
*  towards better power. Instead, we can use these techniques that we have right now to go towards
*  better policy. And better policy means higher visibility. Better policy means people agree on
*  the world models. So I see the work we're doing at Metaculous as an instrumental step in that
*  trajectory. Are we able to find people whose world models are diverging? Let's figure out why they
*  are diverging. Are we able to see, okay, will this action that a policymaker has given us
*  bring us to the outcome? I think these are really important questions around the category of how
*  can we have better epistemic security? It's crazy to think how far this might be able to go over the
*  not too distant future. I mean, obviously you're primarily focused right now on getting a read on
*  what the bots can do and trying to be as accurate as you can and to be much more
*  in-depth on these mini Metaculouses. Let's assume this works. Do you have a roadmap for how this
*  rolls out and scales up to ultimately big picture most important questions in society?
*  Right. In that question, I hear, oh, there you should write a blog post about this,
*  probably. That maps this out. Quick thoughts that come to my mind. We know preferences can and do
*  change based on actions and their consequences, right? So can we build these feedback loops as
*  proof points in organizations that can actually take action on them where real stakes are present?
*  That's why I'm interested in labor unions, for example, because it's a fairly acute
*  case of coordinated decision-making with stakeholders that are outside and inside the
*  group. So it gives us a lot of visibility. I think where we are at right now is,
*  I don't expect a top-down revolution of a government adopting this off the bat, but I do think there's
*  a lot of municipal level experimentation that already has been happening. For example,
*  Talk to the City is collaborating with a couple of municipalities in Japan right now through
*  Liquid, which is a Japanese liquid democracy focused company. There's a bunch coming in Taiwan.
*  We have interests from folks in Singapore to be able to use meticulous forecasts, for example.
*  We have interests in similar Taiwan community. We have groups in the US also on municipal level.
*  Like, for example, Detroit has a bunch of communities that are focusing on well-being
*  of African Americans and previously incarcerated folks. Are we able to figure out what interventions
*  bring a better world to them? These are all very short-term, but in these processes, we can actually
*  see, oh, this seemed to have worked. This actually did yield an outcome where a group was able to
*  coalesce much better. I think we need more visibility into that. This, I think, is the
*  very first step. I think AI tooling is absolutely critical for both the failure mode and the success
*  mode. It will heavily depend on how these tools are implemented and used, how these tools are
*  actively enhancing human agency. I would recommend people who are interested in more of this to check
*  out a roadmap documents from AI Objectives Institute. That's where I have done a lot of
*  my writing and thinking with the team there. I reach out to them also. I still try to stay as
*  involved as I can, but it does hold a dear space in my heart for Peter Eckersey, who was the
*  original founder and a mentor and a friend of mine, unfortunately passed away quite unexpectedly,
*  which is when I started leading AI Objectives Institute. And the line of thought there was
*  very much always like, AI can be a transformative point for human wellbeing, but the default systems
*  do not place us on that path. So I think there's a lot there. And this is the question of existential
*  hope, right? Like existential risk is failure to coordinate at the face of a risk. If we can
*  already foresee this path and we are failing to coordinate the systems we are in, the coordination
*  capabilities we are in doesn't let us get to the heart of that. That is why we are failing.
*  So that is the angle that I want to keep looking at, because we have seen incredibly successful
*  cases of international coordination or multi-corporation coordination. Like the
*  ozone layer is basically recovering since we have banned CPCs, CFCs. Like there is many different
*  cases where we have moved mountains as society, like microplastics related harms. Like we have
*  banned lead at this point. Like there are ways in which we are able to coordinate if we can create
*  coherent world models. I think the thing we need to do is have shared world models that can contain
*  the disagreements, rather instead of agreeable action policies. I think the way politics happens
*  right now, voting happens right now, is find the most agreeable action policy so you can maintain
*  control, as opposed to say, what is the good policy? And this requires a level of epistemic
*  rigor and epistemic security. I see my life's work is to focus on that question and bring more
*  and more towards that. And if there are groups that we can work with, hell yeah, let's kick it.
*  This is where we need to start. So if there are any organizations that are focusing on our priority
*  cause areas, be it climate change or AI or nuclear consequences, or there's any organizations that are
*  trying to do better on resource allocation, where they want the resources to be able to do the
*  maximal good for the specific community, I would love to talk to them. I would love to understand
*  how the things we are building can be useful for them. I think we need more experimentation of this
*  sort. And I'd rather have these experiments be with people that benefit from them in the
*  immediate short term. Cool. Well, that's a great call to action. I'm glad we stayed on the little
*  extra to get that final section. I guess I'll ask again, last time it was a fruitful question.
*  Anything else that we didn't get to that you wanted to touch on? Nope. I feel complete. Thank
*  you so much for this opportunity. It was lovely for it. Also made me realize the context through
*  which my path has evolved, like seeing the role forecasting can play hand to hand with collective
*  intelligence and the failure modes of the current political processes or democracy or resource
*  allocation makes me realize, Oh, I see the role that this plays. So this was great for me as well.
*  So thank you. Cool. Der Turan, CEO of Metaculous. Thank you for being part of the cognitive
*  revolution. It is both energizing and enlightening to hear why people listen and learn what they
*  value about the show. So please don't hesitate to reach out via email at tcr at turpentine.co,
*  or you can DM me on the social media platform of your choice.

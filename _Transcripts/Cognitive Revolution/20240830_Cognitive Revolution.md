---
Date Generated: September 05, 2024
Transcription Model: whisper medium 20231117
Length: 5437s
Video Keywords: []
Video Views: 778
Video Rating: None
Video Description: Nathan explores the emergence of computational life with Google researchers Ettore Randazzo and Luca Versari. In this episode of The Cognitive Revolution, we delve into their groundbreaking paper on self-replicating programs arising from simple interactions. Join us for a fascinating discussion on the implications for AI development, the origins of life, and the potential future of artificial intelligence.

Apply to join over 400 Founders and Execs in the Turpentine Network: https://www.turpentinenetwork.co/

RECOMMENDED PODCAST: 1 to 100 | Hypergrowth Companies Worth Joining
Every week we sit down with the founder of a hyper-growth company you should consider joining. Our goal is to give you the inside story behind breakout, early stage companies potentially worth betting your career on. This season, discover how the founders of Modal Labs, Clay, Mercor, and more built their products, cultures, and companies.
Apple: https://podcasts.apple.com/podcast/id1762756034
Spotify:https://open.spotify.com/show/70NOWtWDY995C8qDqojxGw

RECOMMENDED PODCAST: History 102
Every week, creator of WhatifAltHist Rudyard Lynch and Erik Torenberg cover a major topic in history in depth -- in under an hour. This season will cover classical Greece, early America, the Vikings, medieval Islam, ancient China, the fall of the Roman Empire, and more.Subscribe on 
Spotify: https://open.spotify.com/show/36Kqo3BMMUBGTDo1IEYihm
Apple: https://podcasts.apple.com/us/podcast/history-102-with-whatifalthists-rudyard-lynch-and/id1730633913
YouTube: https://www.youtube.com/@History102-qg5oj

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
(00:04:02) Introduction and Paper Overview
(00:05:38) Self-Replication and Life
(00:07:59) Complexity and Information Theory
(00:13:14) Experiment Setup (Part 1)
(00:17:09) Sponsors: 80,000 Hours | Brave
(00:19:44) Experiment Setup (Part 2)
(00:24:27) Evolution of Self-Replicators
(00:30:18) Types of Self-Replicators (Part 1)
(00:34:41) Sponsors: Omneky | Squad
(00:36:07) Types of Self-Replicators (Part 2)
(00:38:23) Symbiosis and Parasitic Behaviors
(00:41:26) Pre-Life to Life Transition
(00:46:17) Implications for Life in the Universe
(00:57:44) AI Ecology and Future Risks
(01:05:47) Intelligence and Complexity in AI
(01:21:03) Concluding Thoughts
(01:30:14) Outro

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

# Computational Life How Self-Replicators Arise from Randomness, with Google’s Researchers
**Cognitive Revolution:** [August 30, 2024](https://www.youtube.com/watch?v=1kBGDVjrxpU)
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
*  Hello, and welcome back to the Cognitive Revolution. Today, my guests are Atori
*  Randazo and Luca Versari from Google's Paradigms of Intelligence team. Atori and Luca are co-authors
*  on a fascinating recent paper called Computational Life, How Well-Formed Self-Replicating Programs
*  Emerge from Simple Interaction. This paper explores how self-replicating programs can
*  spontaneously emerge in an extremely simple computational environment. And while the paper
*  itself is focused on a narrow set of technical experiments, I found it to be deeply thought
*  provoking about the nature of life and the potential future of artificial intelligence.
*  By demonstrating how complex lifelike behaviors can arise from very simple setups and basic rules,
*  it helps develop our intuitions for the origins of life on Earth and the possibility of artificial
*  life emerging in our increasingly complex digital ecosystems. In this conversation, we go deep into
*  the esoteric details of their experimental setup, which uses a minimalist programming language to
*  process random interactions between random short strings of code, and yet surprisingly quickly
*  gives rise to complex phenomena, including multiple classes of self-replicators, competition,
*  evolution, and even extinction, all without any selection mechanism or optimization function
*  whatsoever. It really is profound to behold just how much complexity emerges from randomness in
*  such a tiny digital toy universe. Toward the end, we zoom out to consider the implications of this
*  work for AI development and safety. While Tori and Luca are cautious about drawing too many
*  conclusions, I can't help but understand this work as yet another reason to expect the unexpected.
*  If such simple digital life can form from pure randomness, I have to expect that the optimization
*  power of the economy as a whole will give rise to meaningful forms of self-replicating AI systems.
*  And yet, even with determined effort, I find it extremely hard to imagine what those new forms
*  might be like. This episode exemplifies why I love making this show. We start with a seemingly
*  niche technical paper and end up grappling with some of the biggest questions facing humanity,
*  and all the other life forms with which we share planet Earth as we collectively hurdle
*  toward an AI altered future. As always, I appreciate it when listeners share the show online.
*  Feel free to tag me, and of course we welcome your feedback via our website,
*  cognitiverevolution.ai, or you can DM me anywhere you like. Now, I hope you enjoy this horizon
*  expanding conversation with Tori Rondazzo and Luca Versari from Google's Paradigms of Intelligence
*  team on the emergence of computational life. Tori Rondazzo and Luca Versari from Google's
*  Paradigms of Intelligence team, welcome to the Cognitive Revolution. Glad to be here. Nice to
*  be here. Yeah, I'm really excited about this conversation. It's prompted by a recent paper
*  that you guys put out that I have found really super interesting and quite thought-provoking.
*  It's called Computational Life, How Well-Formed Self-Replicating Programs Emerge from Simple
*  Interaction. And that's a pretty good summary of everything that we're going to be unpacking over
*  the next hour and change. I would love to start with some real kind of basic stuff and we'll get
*  into a lot more detail. I'm coming to this from a very AI obsessed perspective. I assume you guys
*  think a lot about how your work connects to the future of potentially many AIs and potentially
*  AIs becoming a new sort of life form as well. I'm always trying to figure out where is this going
*  in the big picture? Is it crazy to think that AIs could be at some point properly viewed as a new
*  life form or is that in fact realistic and what criteria would it need to satisfy? So I thought
*  this paper was really enlightening and again, really thought-provoking in a number of different
*  ways. But one kind of simple early argument that you make in the paper is that the capacity for
*  self-replication is really fundamental to the notion of life. So I'd love to just give you a
*  chance first of all to start with that high level observation and unpack that argument for us.
*  Okay, so from my point of view, of course, getting into the business of defining what life is,
*  it's pretty complicated. But the one thing that I think people can agree on is that life is
*  like something that has some inherent order, let's say. It's not like a random collection of
*  molecules or whatever, it's probably not life. So from that point of view,
*  one can think of things like the second law of thermodynamics that would say that it's hard to
*  have order effectively. And in that way, then basically a self-replicating system is one of
*  the simplest systems in which you have this force that acts against the second law of thermodynamics
*  because copying oneself introduces some structure, some shape, some coherence into
*  what otherwise would be just completely sorted. So that's why I personally think that self-replication
*  is one of the first steps towards life. So in the field of origin of life and also biology and
*  artificial life, I think self-replication appears always at the very beginning because it looks like
*  it's the best way that nature at the very least has figured out to preserve and accumulate
*  information over a long time. You can essentially see that we try to explain in the paper as well
*  and show that it happens there. Some things can happen even before there are self-replicators,
*  but until there's not a self-replicator, it's just a dynamical system. And when there's the
*  first self-replicator arising, then you start accumulating information that gets repeated over
*  time. And then you can think about biology and nature as an evolution, essentially as a
*  fight against many different self-replicators that try to compete for limited resources. And
*  what you observe in the current world is essentially the most efficient self-replicators
*  for any given niche that you observe in the planet Earth. Maybe I am overextending my claims
*  here, but one could even claim that intelligence evolved as a way to self-replicate better.
*  It doesn't mean it's the only way that you can get to intelligence, but at the very least,
*  we know that nature did it this way. So it would be, I would say, unwise to not explore this direction.
*  Cool. So I also came away from the paper with maybe one other sense of why it matters,
*  which is that it seems that prior to the appearance of self-replicators, the systems as a whole are
*  in some ways just noisy and the most interesting complex dynamics only seem to emerge in the
*  presence of multiple self-replicators. Maybe I'm over reading that aspect of the paper, but that
*  seemed to be pretty important. And it almost seemed like there was almost like a value judgment
*  implicit in that. And I don't know how you guys feel about that, but it seemed like there is
*  something that we value this sort of higher level of complexity on some level, as opposed to
*  the more noisy reality before self-replicators. I think that one way that you can think about what
*  happens before is that it's almost like noise, essentially. There are things that happen,
*  there are complex behaviors that are going on, but if they cannot be preserved and continued,
*  they are just transient. And when you have some way to preserve information and also to, let's
*  say, reproduce, so to have more of you that do the same thing, then you start observing it
*  with more and more frequency. And then, of course, there's the second part of it, which is once you've
*  got self-replication and once you are competing for space, evolution kicks in. And then you can
*  really start to have more complex behaviors because competition and collaboration really helps with
*  that. Yeah, gotcha. Okay, so the study that we're going to go deep on here is, if I were to describe
*  the motivation to someone, I would say, these guys set out to find the very smallest, simplest
*  environment that they could possibly come up with that could still give rise to self-replicators.
*  Is that a fair characterization? Is that the actual motivation that you had coming into this?
*  So on one hand, for sure, simplicity is a motivating factor. And in fact, what I consider
*  one of the selling points of this paper is that we have an environment that doesn't explicitly
*  favor the existence of self-replicators. It's just self-replicators appear, but we're not looking
*  for that. So it's really hard to talk about what the simplicity of an environment is. There are
*  many ways to define that. What I think is the, what actually got us into this was when one of
*  our co-authors did the first experiment. And so this phenomenon of just things suddenly getting
*  into, very suddenly without asking for it, without anything. And we found that fascinating.
*  That's what I think is the most important part where, you know, how there are systems in which
*  we don't ask for a replicator. It just, there is some spontaneous evolution and that creates
*  structures that are complex enough to copy themselves. And that's the part that is interesting.
*  One reason that we don't want to focus too much on the simplicity, although simplicity really
*  matters, of course, because we don't want to study too complex things, but you can think about a
*  simple system where you've got a copy operation and then everything can be thought as a self-replicator.
*  But that's uninteresting. At least it's not interesting to think about how did we get from
*  nothing to self-replicators. I think the most important point on what we're trying to show here
*  is how we can pass from a period that, which has, let's say, a random soup of programs that
*  do nothing and that are random initialized. They have a transition that goes into a period where
*  there's self-replicators. How this happens and why is part of what we're trying to explore here.
*  Yes. And this work doesn't go into the why yet. We are doing follow-up work that tries to figure
*  out exactly what is going on. But for now, we just thought it was so interesting that we couldn't not
*  show the world that we have this kind of phenomenon. And I think this was quite an interesting,
*  almost philosophical note in the paper where on the one hand, you're looking for some measure,
*  right, to characterize these systems. And the extremes are both uninteresting. Pure noise is
*  hard to compress, but that doesn't make it fundamentally interesting. And then on the
*  other extreme, pure order, a pure crystal lattice or whatever that's totally regular is high order,
*  but also not super interesting. And so you end up looking for something in the middle that
*  has the goalie locks properties of interesting complexity. Maybe you can give more kind of
*  motivation or theory or philosophy behind this, but I didn't have a great sense for kind of exactly
*  how principled that idea is. Or maybe you can first of all, just define the metric that you ended up
*  using and then give a little more color on could reasonable people disagree on whether that's a good
*  metric. How should we think about this metric of complexity?
*  Okay. So first, let me just note that I have a bit of a background in information theory and
*  compression, which has color, some of the ideas behind this specific definition of complexity.
*  And of course, another important note is that I think you could have discussions for years about
*  what complexity actually means. So what I wanted to capture when using this definition of complexity
*  was basically trying to have a somewhat mathematical definition for structure,
*  like amount of structure that is present in two in string or something else. Of course, as you
*  mentioned, this notion of structure has some issues because too much structure is also not
*  too interesting. And I think that the metric ended up defining has a reasonable trade off
*  between over emphasizing structure and ignoring structure entirely. Anyway, so the metric we ended
*  up going with is at least theoretically, and I'm not actually giving an exact definition because
*  there are a lot of details that one needs to get right. But intuitively, the idea is to consider
*  the difference between the Shannon entropy and the Kolmogorov complexity of the data that we have.
*  Now, why would someone do this? Intuitively, one can think of Shannon entropy as how hard would it
*  be to describe, let's say, this string of characters if I were completely ignoring any kind of structure
*  that it may possibly have. For example, a sequence of half A's and half B's has the same Shannon
*  entropy, regardless of whether it first has all the A's and then it has all the B's or whether
*  they are just mixed together completely randomly. Shannon entropy is a measure that completely ignores
*  structure. Kolmogorov complexity is basically sitting at the opposite end. It's saying what's
*  the shortest description you could give of this thing? You can do whatever you want. Any tooling
*  machine, what's the shortest tooling machine that will produce this string as output? So a Kolmogorov
*  complexity absolutely can tell the difference between first all the A's and then all the B's
*  or alternating A's and B's. So then the idea of taking the difference is that one ignores
*  the structure, the other one lets you take any amount of structure in consideration.
*  So what is left is basically only the structure. So that's the main motivation for the definition.
*  I think also that may be a good idea to make an analogy with the real world that maybe will
*  help to clarify the definition a bit. So imagine you have a building. A building contains a lot of
*  molecules, a lot of different materials, a lot of different things. And you can imagine the equivalent
*  of Shannon entropy would be something that tries to define the position of all the molecules
*  independently for the context of a building. The equivalent of Kolmogorov complexity would
*  basically be here's the blueprint of the building and given the blueprint, you know how to build
*  this building. So that tells you what the building is. It's a description of the building.
*  Now imagine that you take the same building and you completely destroy it and it becomes just a
*  pile of rubble. For a pile of rubble, it has the same molecules, so it has the same entropy,
*  but it doesn't have a simple description like a blueprint. If you wanted to get the same pile of
*  rubble, you would need to know where all the random small pieces sit. So because of that,
*  in this analogy, the pile of rubble would have a significantly lower complexity or structure.
*  That's more or less the intuitive reason why I think that defining complexity in this way
*  makes sense for, I want to emphasize the amount of structure that there is in, you know.
*  Hey, we'll continue our interview in a moment after a word from our sponsors.
*  I am really excited that our new sponsor, 80,000 Hours, is now offering free one-on-one career
*  advising sessions to cognitive revolution listeners. 80,000 Hours aims to be the best
*  source of advice for people who want to do the most good that they possibly can with their careers.
*  We typically work for about 40 years in our lifetime and we work about 2,000 hours per year.
*  That is the single biggest opportunity that most of us have to make a positive contribution and
*  it's worth being strategic about it. That's where 80,000 Hours can help.
*  I actually used their career advising service myself. Two years ago, I had just finished the
*  GPT-4 Red Teaming project and I wanted to do anything I could to nudge the AI future in a
*  positive direction. But what could or should I do? That was not clear. After my call with 80,000
*  Hours, I got a number of connections to outstanding individuals in the space and over the course of
*  the follow-on conversations, I developed the confidence that this podcast was a good one.
*  The podcast was one of the projects that I should pursue. Today, I'm thrilled to have built an
*  audience of thoughtful, high potential people that 80,000 Hours wants to help. To request a free
*  one-on-one career advising session, follow the link in the show notes. It's 80,000hours.org
*  slash cognitive revolution. That's 80,000hours.org slash cognitive revolution. Sign up for a free
*  one-on-one career advising session. Figure out how you can make a positive impact on the AI future
*  and I think you'll be glad that you did.
*  Use cases from rag search to automated business intelligence. On top of that, it's up to three
*  times cheaper than Bing, all without compromising on quality, speed or reliability. Over 700
*  businesses, including Cohere, Chegg and Kagi, rely on the Brave Search API. And a recent survey
*  showed that 94% of customers would recommend it to their peers. To start building apps with the
*  power of the web, sign up at brave.com slash API and get up to 5,000 free monthly calls.
*  Is there a philosophical extension to that or implication of that? When I read this paper,
*  I can just look at the graphs. These graphs where it shows complexity rising through time
*  as the dynamics of the system evolve and we'll get to the actual details of the nature of the
*  system in a second. But I really was left with this feeling that there is some implicit value
*  judgment over these states. And I don't know if that's something you would want to sign on to or
*  not, but it brings to mind these various thought experiments for me where if I understand correctly
*  a tiled universe of happy people, if you were a utilitarian, you might say, oh, geez, if I had
*  this one very happy person and I made a zillion copies of them and filled the whole universe with
*  this same thing over and over again, that would be great because all these people would all be
*  happy and we would count up their utility and have very high utility. So fantastic.
*  And then somebody else might say, doesn't that sound kind of boring? Shouldn't there be some
*  sort of discount for the fact that this same thing is taking up all the space? Don't we want
*  more diversity for its own sake? It seems like this measurement that you've defined
*  implicitly suggests that second frame. Is that fair or would you not go that far?
*  I have to say we did not assign any value judgments, philosophical implications of this
*  definition of complexity. We did not consider that. In fact, I would be somewhat surprised if
*  this definition of complexity becomes useful outside of this paper. Pleasantly surprised,
*  but still surprised. So one thing I want to say is that this is a measure of structure, right?
*  It's not a measure of value or it doesn't take into account diversity. It's not a measure of
*  utility, right? So it's just a measure of structure. Because of that-
*  Wait, just quick interjection. There is some way in which it counts diversity, right?
*  To some extent, yes. So it's a bit hard to explain exactly how repetition
*  gets taken into account by this measure. This middle ground is the best point. As in,
*  if you have no repetition at all, then very likely this complexity will be low.
*  On the other hand, if you have a fully repeating and end copies of the same character, for example,
*  then the measure of complexity will also be very low. So you do want some amount of repetition,
*  and ideally repetition that itself has some structure, but not too much. But that doesn't
*  imply that you can still have repetition of one relatively complex structure that's just the same
*  but repeated a lot of times. And that will have high complexity. So it's a bit of a trade-off.
*  If you have too much repetition, complexity is low. If you have too little repetition,
*  complexity is high. In the experiments we have been doing since programs at 64 bytes,
*  that turned out to be a reasonable trade-off and high complexity effectively correlates extremely
*  well with the soup that's full of self-replicators. And to be clear, this is also purely a measure,
*  right? This measure of complexity is not being fed back into the system in any way, shape, or
*  form. Yeah. Okay. Also, just I think I have to make the disclaimer, Kolmogorov complexity is not
*  something you can actually compute. So we're not actually using Kolmogorov complexity. It's just
*  mathematically easier to reason about Kolmogorov complexity than it is to reason about whatever
*  other proxies for more Kolmogorov complexity you may end up using. Got you. Okay. About the complexity
*  matrix that we use, we have also used something else once, which is counting the number of unique
*  tokens that rise into the soup. And this would mean that if you got a self-replicator that takes
*  over, we don't count the reproduction of this self-replicator to another string as creating new
*  tokens. And this shows that, like you see, when self-replicators arise, very stark decreasing the
*  number of unique tokens that there are into the soup. And then we checked, and this is very well
*  correlated with this other complexity matrix. So you can think about us using this higher
*  order entropy matrix as a proxy for this unique token count, because of course, it's much easier
*  to compute. Gotcha. Yeah. That's a very good point. One of you guys can take just setting up,
*  what is the little micro self-contained universe that you've created? And I'll ask any clarifying
*  questions that I have. So the very simplest experiment that we performed is as follows.
*  Imagine that you have a lot of a soup of random strings. The random strings represent code,
*  but they can also represent data. Those are essentially what you would pass to a compiler
*  to execute some code to a computer. And what we say is you randomly take a pair of strings,
*  concatenate them, and execute the code starting from the very bottom left. And you execute the
*  code for a long time. And then you just split the strings again and put them back into the soup.
*  Now repeat this many times and have a lot of strings do that in parallel. So this is the
*  only thing that happens in the simplest setup. You just take two random strings, concatenate them,
*  execute them, and then split them again. So there's no objective function whatsoever.
*  There's nothing else that happens from our side, at least in one of the possible setups. And the
*  only thing that happens is that the strings modify themselves by reading each other's code
*  and modifying the code. Let me show you an example, which is also the example that captivated us
*  into digging deeper into this. Let's see. Okay. So here you can see a few programs from the soup.
*  Each program is 64 bytes. This is one program. There are two columns, not for any particular
*  reason. It's just that it makes better use of space. And you can see that most of the bytes
*  are random. And there are a few bytes. You can see the ones here that are highlighted
*  that actually represent instructions. And everything else is just nothing.
*  There's also a special character that represents the byte zero, which is special. And you can
*  probably see that here. I'm not sure how well it's visible across the video, but it's a null byte.
*  Okay. So if we let these programs randomly execute, you can see that they start modifying
*  themselves. And sometimes some strings that appear, like copies of the same character,
*  or maybe the ends of the string, gain some characters, lose some characters.
*  There's also a few mutations that just erase things from here and there.
*  This evolution continues. There's a lot of interesting behaviors. There are things that
*  extend things that for now, it's nothing too interesting that is happening. By the way,
*  this is the same example that is explained in the paper in figure two, I believe, where there is
*  a story of the replicators that appear here. So somewhere around now, you notice that there was
*  a lot of activity. And that activity left a lot of null bytes around. Now you can see here we have
*  a count of how frequent is each byte. And you can see that the null byte now is way more common than
*  it was before. And if you just go back a couple of seconds, okay, if you go back a couple of seconds,
*  basically no null bytes are not special. But in the time of just a very short number
*  of executions, there are a lot of null bytes. After that, there is another little bit of
*  nothing too interesting happening. And then somewhere around now, we get actual replicators.
*  And this explodes in a lot of activity. And at the end, like now it's paused, but at the end,
*  you can see that there is the same structure that repeats itself basically everywhere in the soup
*  with some minor modifications. So seeing this for the first time is what gave us the intuition that
*  there was something interesting happening here. This kind of weird evolution over time, different
*  behaviors on all of this. So what happens before separable indicators arise is actually not
*  completely random. There's a distribution of characters that changes from the very beginning.
*  You can think of it as just a complex dynamical system where there are operations that are
*  growing inside, but in this transient way that is not stable until there's separable indicators
*  arising. And this is, if you were to talk about it in the origins of life terminology, you could
*  think about this as being the pre-life period, a period where there's dynamic interactions.
*  Usually in that case, it would have been with some catalysts that catalyze each other or create some
*  complex dynamics until to the point where separable indicators arise. And then this moves into what
*  sometimes is called the life period where separable indicators arise. And the important part there is
*  that things happen also in the pre-life period, but whenever there's a separable indicator,
*  this change is very stark. There's a very big transition in dynamics and that's why it's
*  useful to think about it in these terms. So our paper is mostly focused on how do we get to this
*  transition? How do we get from a random soup to something as complex as separable indicators?
*  So for the uninitiated, which included myself up until very recently, let's take just a little
*  bit more time on what we were just looking at there. And you can maybe even pull it back up
*  again, just to have the thing on the screen. So you start off with just this totally random
*  set of strings, each of which are 64 characters. So that's worth just pausing on for a second to
*  say that is a remarkably small number of characters for anything really interesting to happen.
*  But that's the whole thing, right? You've got 64 characters. And if I understand correctly,
*  you're literally generating these out of ASCII characters at total random?
*  Not ASCII, just bytes, but yes. Random, independently, uniform,
*  by every character selected independently from everything I see.
*  Gotcha. And then the way that this is going to be interpreted, I'd never actually heard of this
*  before, is through this extremely minimalistic programming language with the charming name of
*  brainfuck. And this is a prior art, right? But this is something that somebody made to
*  try to say, what is the smallest possible computing paradigm that we could imagine?
*  Didn't stop me at any point here if I'm wrong. But what actually happens is you have a two
*  head computer that both start in the first position, if I understand correctly.
*  When you take two strings, you put them together. Now, why do you take two strings and put them
*  together? That's essentially simulating the randomness of the universe, right? We've got
*  molecules bouncing around Brownian motion in solution, whatever, in a gas, whatever they're
*  doing. They're bouncing around and they're bumping into each other at essentially random, right? Or
*  at least we're modeling it as being random in this case. So take two of these strings out and
*  just simulate an interaction and just arbitrarily tell me if there's more to it, but seem arbitrary
*  that we just concatenate them and then we'll treat this as if it were brainfuck language.
*  There are only looks like 10 different commands in the entire language and all the other characters
*  out of the 200 and it's 256, right? Impossible bytes. All the other things are just considered
*  to be neutral data. And then I'm so the commands that can happen are like, okay, you've got these
*  two computer heads, they both start at zero. One thing to do is move ahead from place to place
*  and you literally just move them one square over, right? So it's move one to the left,
*  move one to the right. There is increment and decrement of value. So you have a value,
*  I guess that assumes that there's like an order to the bytes as well, or do you just increase the bit
*  value by one? So the heads can only move one position, one step at a time and the bytes can
*  only move one value at a time. And then you can also copy from one position to the other.
*  And there is the most important instruction, the one that actually makes this language too incomplete.
*  And just for disclosure, this is not exactly brainfuck. This is very close to brainfuck,
*  but the standard brainfuck language only has one head and then the input and output,
*  like the copy operations read and write things to the terminal for humans to interact with.
*  But in this setup, there are no humans. So it makes sense to have two heads that modify
*  things themselves. So let me show you. This is a representation of an execution of a program.
*  There are actually three capsules, not two. The two heads have to do with the position that
*  you read and write from. And the third head is the position of the next command that you execute,
*  which is fundamental. In particular, the next command that you execute head is the only one
*  that can move by more than one position per step. And those are the square brackets. What the square
*  brackets do is they look when you execute that instruction, if the character is on the,
*  I think the blue head, I'm not sure if I remember correctly, is zero. And that's why zero has a
*  special representation. Then you skip that execution. Like you skip those brackets if you
*  are going in one direction or just go through. If it's not zero, you jump to the other bracket.
*  So that's how you can implement things like conditions and for loops and all of those things,
*  which is what allows for this language to be too incomplete.
*  Just one note. BrainFac is not necessarily the even smallest language that will be too
*  incomplete. It was created as far as I understand to make it very hard for humans to code in it.
*  You can have even simpler instruction sets that are still too incomplete.
*  Hey, we'll continue our interview in a moment after a word from our sponsors.
*  Omnike uses generative AI to enable you to launch hundreds of thousands of ad iterations that
*  actually work customized across all platforms with a click of a button. I believe in Omnike
*  so much that I invested in it and I recommend you use it too. Use Cogrev to get a 10% discount.
*  Hey everyone, Eric here. In this environment, founders need to become profitable faster and
*  do more with smaller teams, especially when it comes to engineering. That's why Sean Lennahan
*  started Squad, a specialized global talent firm for top engineers that will seamlessly
*  integrate with your org. Squad offers rigorously vetted top 1% talent that will actually work hard
*  for you every day. Their engineers work in your time zone, follow your processes, and use your
*  tools. Squad has front-end engineers excelling in TypeScript, React, and Next.js ready to onboard
*  to your team today. For back-end, Squad engineers are experts at Node.js, Python, Java, and a range
*  of other languages and frameworks. While it may cost more than the freelancer on Upwork billing
*  you for 40 hours but working only two, Squad offers premium quality at a fraction of the typical cost
*  without the headache of assessing for skills and culture fit. Squad takes care of sourcing,
*  legal compliance, and local HR for global talent. Increase your velocity without amping up burn.
*  Visit chewsquad.com and mention Turpentine to skip the wait list.
*  I just want to make sure that people have a very, maybe not full understanding, but at least a
*  intuitive sense for just the sort of universe that we're operating in here. So,
*  if you just try to say it back to you one more time, there are three computer heads on this that
*  operate over this ultimate space when two different strings are attached together. They go from 64
*  to now combined, they're 128. So, you've got 128 bytes, three positions, two can read, write,
*  and be moved left or right, and can increment or decrement, and the other one is the one that
*  handles the commands. That one is the one that can bounce around when it hits these open and close
*  parentheses type operators. And I guess there's maybe two more things that matter here. One is
*  the definition of a self-replicator. That is when the first 64 bytes manage to copy themselves over
*  to the second 64 bytes exactly. Mostly. It's slightly more complicated than that
*  because they need to copy themselves to the other 64. The other thing they could do is have the other
*  64 bytes be the copy of the original program, but destroy the original program while doing so.
*  And that would not be a self-replicator. It's just something that moves.
*  Also, to make things more complex, a self-replicator doesn't have to be
*  only with 64 bytes, only if it's an entirety of 64 bytes. You could copy a smaller part of this
*  substring, let's say, of the 64 bytes many times, and this will still count as a self-replicator.
*  So, it's actually quite complex to tell whether you created a copy of yourself as a substring,
*  because it's not just saying 64 bytes on the left need to be equal to 64 bytes on the right.
*  It could be that it's like 13 bytes on the left that replicate on a very random position on the
*  other side, or some of them that get replicated many times in this 128 bytes concatenated string.
*  And this makes it even more important to figure out a complexity metric to understand what's going
*  on, because it's very hard to detect explicitly for a perfect self-replicator otherwise.
*  The way I like to think about it is that saying that it's hard to say whether one program is
*  self-replicator, but it's a lot easier to say whether the soup is full of self-replicators.
*  It's even more complex than this, because in some experiments we have one single long tape
*  where there's no concept of individual strings. So, to determine whether there's a self-replicator
*  there, you cannot avoid it. You really need to think about there are sides of which can be
*  anything for a substring which is a self-replicator, and how do you tell whether
*  a self-replicator is replicating in any given offset. And that's basically just an experimental
*  variant where instead of having these discrete units and merging them randomly, you just
*  literally run the program indefinitely over the one super long string of characters. I believe the
*  way that setup works is that theoretically you stop the program and you start it again from
*  a random point. But I think that thinking about this example is the simplest. And there are also
*  extensions which are putting one dimension or two dimensions into the equation. So, it's no more
*  uniform distribution, but it's a uniform distribution among your neighbors. But it doesn't
*  change the concept. Thinking about just having uniform distribution of random strings concatenating
*  should work. And then the one other thing that I wanted to note is that there is the
*  possibility for errors in these programs. Since the data was all generated randomly in the first
*  place, when you try to run this random string of characters as a program, it can error out.
*  And specifically, it seems like it errors out if the control logic breaks. If it hits one of
*  a particular special character, which is the zero character, and it's meant to look for the next or
*  the last parentheses to handle control logic, and there isn't a corresponding proper place for it to
*  go to, then that's basically just the end of that run. Is that right? And everything that happened
*  up until that time, all changes that are made, those are just left in place and we move on to
*  the next step in the simulation. We tried a few different setups. The overall result doesn't change
*  that much anyway. But yes, I believe in this setup. If you encounter a jump instruction that
*  doesn't have anything to jump to, it just stops execution. And there are a few other things,
*  like if you end up trying to execute past the end of the string, it also stops execution because
*  what would it execute anyway? But in general, one important thing is, and also one of the reasons
*  why we are using brainfac and not C++, is that we want the interpretation of programs to be as
*  permissive as we reasonably can. If you don't do that, then basically you never actually get
*  anything interesting because you just add it up every single time. Okay. So I think that's a pretty
*  good overview of the setup. It's both remarkably simple in some ways and obviously has some
*  nuance. Let's talk about what happens as you run these things. I think you've alluded to it a little
*  bit already, but essentially you have this pre-life, or at least pre-self-replicator
*  period in which everything is still random and these things are being concatenated,
*  they're being run, data is changing. You can maybe tell us a little bit more about what evolution
*  of the overall system you can see during that phase. And then there's a very sharp phase change.
*  I think this notion of phase change is a really important one that happens when the first
*  self-replicator pops up. And again, probably can't stress enough, there's no incentive for
*  this self-replicator to pop up. No loss function here like we're used to thinking about in AI
*  systems. Literally just blind execution of the program stumbles on through random interaction
*  between two strings, something that is a self-replicator. And now when that happens,
*  very quickly it starts to replicate a lot and now we're into a different regime in the overall story
*  of this little universe. Since we initialize everything with random bytes, in the beginning
*  everything is random. You can see this is already after a few executions, it's not exactly quite
*  uniformly distributed, but here we have the least common character and here we have the most
*  common character. And you can see they are pretty close to each other. No character appears more
*  than half a percent of the time. So the first thing that happens in the first few thousand executions
*  is that this distribution shifts. And you can see here after a few thousands of times that
*  programs interact with each other, we start having a few characters that appear like two percent of
*  time. We are still investigating exactly what is happening here. There's clearly something that is
*  important. Here we can see that this character, this is one of the characters that moves the
*  heads for example, is getting particularly popular and that some characters also become particularly
*  unpopular more than others. It's not like there's just one character that becomes significantly more
*  common. It's also that other characters become less common. And then we have some of these state
*  transitions as we were saying, where the behavior changes significantly. Here there is a lot of
*  activity for a really short time and that leaves you with a completely different distribution.
*  And some characters almost completely disappear. And there's one interesting thing that one of our
*  co-authors observed that you can think about the initial distribution where you got some operations
*  which are code that you can execute and other operations which are just data. So if you try
*  to execute there, nothing happens. So even at the very beginning, the only thing that can generate
*  more code is code itself. And since the very beginning in this kind of system, the number
*  of instructions that get executed and that are present in the soup starts increasing immediately.
*  So even before having the certificators actually appearing, we still have some
*  one thing that could be very similar to the concept of autocathletic sets where those
*  codes, strings of codes or pairs of codes generate other pairs of codes that then
*  can have a chance of generating themselves again. Yeah, that's really interesting. I'm noticing just
*  looking at the top of this that it seems that both the highest frequency characters, although
*  maybe not that equal sign. No, the equal sign. If I'm reading this right, I'm seeing the open arrow
*  the open arrow is the 4.94%. Right? Yes. So here we have the 16 most common characters and the 16
*  least common characters. It is quite interesting indeed that plus and minus tend to be not that
*  interesting, but I think perhaps makes sense because if you execute a plus that will likely
*  make an open parenthesis into a completely different character. So that's likely to ruin
*  meaningful code and the pieces of code that are useful for to copy like the instructions that are
*  useful to copy things over like the loop instructions, the instructions that move the heads
*  and the copy instruction are super common. At least we believe that because if you have a lot
*  of copy instructions, then it's easy to produce more copy instructions because you just will read
*  something and something is probably a copy instruction itself. So you will copy that over
*  and this is a self-reinforcing effect. Like having many copy instructions just gets you
*  even more copy instructions and probably there is something similar to winning with loop instructions.
*  Yeah, cool. That's fascinating unto itself. The instructions that enable copying tend to get
*  copied and the ones that scramble data tend to scramble themselves out of existence. And this
*  is before we've even got to self-replicators. Now, I guess one could ask, is there a sharp line between
*  this notion of even if you raise the concept of an autocatalytic set, is there a bright line
*  between that and a self-replicator? It seems like there is because there's a face transition,
*  but when I just look at a pair of characters could be in a sense enough, right? For it to be
*  copying itself over, I feel like I'm missing some critical distinction there.
*  Yes, I think I can help here. So there are also people that would very easily call autocatalytic
*  sets set-replicators. It's a matter of how efficient they are because the biggest difference
*  between the pre-life and the life period is the speed of, let's say, information to be replicated
*  and be copied into their neighborhood. When you have got the pre-life period, you got some
*  autocatalytic sets that happen, but they're very slow in copying each other. Also because they need
*  to do many more steps before they become multiple of what they were before. And it's also by chance.
*  But when you've got a function as a pre-replicator, in biology, the best example is something that
*  people suspect being the RNA and with the polymers and the ribosome, then this just
*  sped up very quickly. And then in much shorter timelines, it takes over the entire soup.
*  So looking at the paper, there is a figure one that shows us the number of unique tokens
*  or even the complexity. And you can see that the number of unique tokens slowly decreases
*  in initial phases because... Quick clarification. A token here is a 64 length string. No.
*  A token is a marker that basically identifies, is what the
*  bytes come from the other half of the string. So it's just keeping track of where the bytes
*  originally came from. You're actually keeping a full log of every copy event. We did it once.
*  Let's put it that way. But yes, this number of tokens takes into account the history of every
*  byte and looks at where it came from. And if the token came from the same byte, then it's the same
*  token. There's one caveat which here becomes quite important. So far we talked about separate
*  set modification being the driving factor of separate indicators to arise. And this can be
*  proven even by just having experiments where there's absolutely zero background noise. So the only way
*  to modify some characters is to execute the code. But we usually also add background noise. So
*  every now and then some characters get randomly modified. This helps to speed up the process.
*  And so you need to find certain indicators which are more robust, but it's not necessary. We still
*  observe everything happening even without background noise. What you're seeing here in this graph
*  shows that unique tokens decrease. And that's also because... Sorry, they decrease, but there's the
*  impact also of adding unique tokens every now and then that counterbalances it.
*  If you look here, once we do have a self-replicator, the amount of unique tokens increases.
*  That's obviously not possible if you don't add new tokens every now and then. So this increase
*  here is the effect of mutation. So what is interesting tying back to the conversation
*  we were having before is that here the number of unique tokens, even before we have anything like
*  a full-form self-replicator, is steadily decreasing. So that's basically saying that there is a
*  fair amount of copying that is happening even before we have actual self-replicators.
*  So that first line when the first self-replicator pops up is obviously a big event in the history
*  of this system. You've got a major drop in unique tokens. You've got a huge rise in
*  top 32 tokens. And should I understand that as the source back to an original initial token?
*  Like this is a character that has been copied the most?
*  Yeah, basically top 32 tokens is basically saying how many copies exist of the 32 most common bytes.
*  So as you can see here there is a sharp increase because at that point we have a self-replicator
*  that copies itself a lot. And by byte I don't mean like byte value, I mean original byte.
*  So then the complexity also spikes because we go from a noisy environment to a more
*  ordered environment and then it drops back down. And should I understand that as being
*  a period of tiling? Is that where we've overshot and gone to the other extreme in complexity where
*  the self-replicator is everywhere for a while? Actually no. So let's see if I can find the moment
*  corresponding to that point here in the video. I believe it was here. So that's basically an
*  extinction event. I'm still on the graph. Okay, so in a few seconds you will see
*  there is going to be a lot of movement and then nothing will happen after one second of a lot of
*  movement. And that's the spike. See? Here there was a lot of changes and now everything is stopped.
*  Yes, there is still some modifications but it looks like it looked in the beginning, right?
*  It doesn't look like the self-replicator regime here. When you do have successful self-replicators
*  there is a lot of movement around and you can see that but only for a really short time. And
*  that's the time that corresponds to this spike because there you have replicators take over
*  but they are this initial kind of replicator that we have here as an example. And the interesting
*  property of these replicators is that if the bytes that they are trying to write themselves over are
*  zero, they just don't do anything. If they try to write a set of bytes of any kind, it works. You
*  can see here that it's just slowly copying itself in reverse. But if the bytes you had there are
*  actual zeros, then it doesn't work out. So it just doesn't do anything. And so what this does, and
*  you can see this in the soup here, what this does is basically very quickly you have every single
*  byte at the end of the strings be a null byte. You see here. And now the replicators cannot
*  replicate themselves anymore. And so basically the replicators go extinct. Nothing happens.
*  And then afterwards we find a different kind of replicator that doesn't have this problem.
*  Manages to copy itself over null bytes without any problem. And because of that,
*  you have the second state transition here. The soup becomes entirely self-replicators and the
*  complexity just jumps up. So this is basically just an short-term extinction event. And it doesn't
*  happen always for that matter. Like in most of our experiments, we just see a sharp jump in
*  self-replicators and that's it. It's just that we were lucky enough that the standard setup ended
*  up having this particularly interesting example. So which is the one that we ended up showing here,
*  but it doesn't always happen. What's more typical even is just that as soon as you have one
*  replicator, the soup takes over and there's no extinction event in the middle. Not one replicator
*  in the sense that we have actually also tested the hypothesis of if you had one self-replicator
*  initializing the soup, what's the chance that it takes over? And it's actually quite low. It's what,
*  23%? 22%. Because there are many things that can happen that destroy a self-replicator. If there's
*  background noise, why they self-replicate? They may just be destroyed by the noise. And if there
*  is no background noise, you might be in the wrong order when you try to replicate. So if another
*  string is the one on the left and it starts from this random code, it might destroy you and therefore
*  you will not self-replicate. So there's actually low chance for one self-replicator to take over.
*  In particular, we don't, we'd not test this because as we said, it's hard to see if one program is a
*  self-replicator. But what we expect is that there actually have appeared other self-replicators here
*  that just died. What is remarkable about this specific evolution is that self-replicators
*  took over a fair bit and then still died. Gotcha. So can you give a little bit of,
*  I don't know if a taxonomy is too much to ask of like the different kinds of self-replicators that
*  arise. I might be overinterpreting the graph, but I came away with the sense that
*  there are some primitive ones that pop up first, but then they have these problems with zero. And
*  so they sometimes fizzle out and then like more robust ones come later, but maybe they take longer
*  to emerge. But maybe I'm telling more of a story there than I should. Maybe it's more random actually
*  than all that narrative that I just laid out. So we certainly have observed different kinds of
*  self-replicators. So here you can see the first self-replicator to appear in that setup. And it
*  has this structure where it starts a loop and then it first copies the characters, then moves
*  the two heads and then loops back. So you can see here the execution, right? So when it's executing
*  this character, it copies this space to here. Then it moves the green head back, sorry, the blue head
*  by one position. It moves the red head forward by one position. And it says, this is not zero,
*  let's loop back. Sorry, this is not zero. That's the byte that gets checked. And so here it repeats
*  and so now it just copies itself over. And as I was saying before, this has the problem that if it
*  tries to copy itself over when it does this check of, okay, should I go back here? It says this is
*  zero. So no, I will just go forward and then nothing interesting happens. The second replicator
*  that appears is somewhat more resilient. And it's fundamentally still the same thing, right?
*  It still does a loop. It still moves the two heads. But the difference is, I don't know if
*  you noticed this, but the order of the heads is swapped. So here you write to the blue head
*  and here you write to the red head. So what this means is that having zeros in the string you're
*  trying to override doesn't give you problems. You do get problems if you have zeros in the string
*  you're trying to copy. If this were a zero, then you fail at copying yourself because
*  you just copied the first part of the program. You don't copy the entire program.
*  And note that the program is copying itself in reverse order. When execution starts from the
*  next program, it starts from here. So it's important to copy this first few bytes. The image doesn't
*  go to the end of the execution, just shows the first few steps of execution because it takes a
*  while. Yeah, the other replicators will eventually manage to copy this part over to this part. And
*  so you get an actual copy of the full replicator. But with this one, there is, as I said, this
*  problem that if you have a zero byte in between the two halves of the replicator, then it doesn't
*  actually copy itself. Now that's not as much of a problem as it is for the other replicator because
*  there is a difference between I need to have a null byte myself and the program I copy myself to
*  has a null byte. If you have even just one self-replicator that doesn't have a null byte,
*  then it will succeed at copying itself over. And so it will survive way more easily. But the problem
*  is if the, let's call it food or rest of the soup is full of zeros, then this self-replicator cannot
*  copy itself at all. But sometimes appears in after a longer evolution is this one specifically
*  is handcrafted, but there are other replicators that sometimes appear that are resistant to zeros,
*  both in the destination and in the source. Usually they contain like nested groups. So it's a bit
*  harder to explain here what is going on. So this is still the same replicator that we had
*  in the previous example, like the most successful replicator, but around it, there is an additional
*  loop. And what this loop does is just suppose I exit from the first loop because I happen to have
*  found a zero byte, then let's just take the zero byte, decrement it or implement it, whatever.
*  Now it's not a zero byte anymore. So let's jump back and get back into the previous loop.
*  So this is one of the reasons why I was saying that it's hard to define what a self-replicator
*  is because at the end of the execution of this program, neither of the halves of the self-replicator
*  is the same as the original program, because this null byte is not a null byte anymore
*  in the original program. And in the new program is also not a null byte. But still you would say
*  that this program copied itself, right? Because the important parts copied themselves.
*  And this program is also very robust to noise, by the way. So in noisy environments, this
*  is particularly good because even if you can copy yourself perfectly, you can have a random
*  mutation that could destroy other programs. But for a random mutation to destroy you, it has to be
*  in the few operations that you have in this case. We also observed that in other languages, that
*  there's this typical behavior of self-replicators that if there's nothing else as a pressure,
*  they're trying to become shorter and shorter. In this specific one is tricky because actually
*  it's a specular self-replicator for the nuances that this brainfac variance has.
*  But in other languages that would be relevant. And we've also observed that different kinds of
*  self-replicators that use different operations take over in other languages that, for example,
*  are CPU instruction based. But I want to stress out that the main focus of this paper was to
*  focus from how you get out of the pre-life period. So we didn't explore nearly as much as what happens
*  after the first self-replicator arrives. This is something we very much care about, but for future
*  work. Yes, we just had some observations of more resilient self-replicators appearing over time.
*  So there were at least three classes. Tell me if I missed any. There's an initial one that,
*  maybe I shouldn't order them, but there's working from least to most resilient. There is one that
*  can copy itself, but if it hits a zero where it's trying to copy two, it fails. There's one that
*  is highly susceptible to mutations in its own code and can fail as a result of that.
*  And then there's the robust kind that can both write over the zeros and is much more tolerant of
*  mutations in its own space as well. And we know that all these things can arise. How often do
*  multiple of these things arise? I guess you just said there's more future work to do to play out
*  from the emergence of these things to the long-term dynamics, but how often do we see
*  multiple different things battling it out versus is this like one replicator's lonely struggle for
*  survival or are they doing battle with each other frequently enough? It's a bit complicated to
*  evaluate, especially in the multi-dimensional setups. Interactions are a lot more sparse.
*  And since interactions are a lot more local, there is space for niches to appear and going
*  into different directions in different places. And then they start fighting with each other at
*  the border and trying to take over other self-replicators. But even in this dynamic
*  setup where everything can interact with everything else, you can see that the structure is similar,
*  but not that many self-replicators are identical because the effect of mutations
*  gives you this, right? Where now everything is equal, but then one self-replicator mutates
*  a little bit. And then if that one starts getting copied a little more, then you have replicators
*  that fight with each other. Even if one self-replicator became a lot more efficient than
*  the other one, then it probably would just win. But in this setup, if you have multiple
*  replicators that are similarly efficient, for example, if you look at these two, they're
*  identical except some of these random unused bytes here are different. So their efficiency is
*  the same, but you will see a bunch of both kinds. Yeah, interesting. And that's, if I understand
*  correctly there, it's like you can have the same mechanism, but you can have different filler data.
*  This is almost like junk DNA. I don't know that there is such a thing as junk DNA, but if you
*  believe in the notion of junk DNA, this is the junk DNA of your universe. So it's amazing how many
*  concepts like that we are seeing in just this very small thing, right? We've got different mechanisms
*  for self-replication. We've got mutations that can be deleterious or that can be survivable,
*  depending on the mechanism. We've got some notion of pollution with the
*  zeros popping up that can become so common that they make it difficult for the self-replicators to
*  succeed. We have the junk DNA. We have competition for niches and then fighting at the border.
*  It's really an amazing, this is what kind of just captivated my imagination looking through
*  these results because it's like that is such a small universe in which to find so many of these
*  advanced concepts. Is there any other kind of recognizable concept from the study of
*  macroevolution that you have observed that we haven't touched on yet? Actually, yes.
*  This one. So we have some interesting cases of something similar to symbiosis. This is in a
*  different language and I don't think I should go into too many details because it would take a
*  while. But the idea is that we have a different language, which is a variation of four, in which
*  there is always one byte self-replicator that just copies that one byte. So if a program starts with
*  that byte, then that byte copies the self-over. Maybe it's not symbiosis, it's not the correct
*  term. I don't know. I'm not a biologist. But what happens is that there is evolution that happens
*  that starts to exploit that one byte self-replicator until you get self-replicator that is able to copy
*  the entire string that uses that one byte self-replicator. And because of this, because of
*  the existence of this one byte self-replicator and using this one byte self-replicator, evolution is
*  a lot faster than in a lot of other fault variants where you don't have this one byte self-replicator.
*  So it's like enabling further evolution just by being there. And it's not a parasitic kind
*  of relationship because the self-replicator still survives, but it's a sort of cooperative.
*  But some of our colleagues have also observed some early examples of parasitic behaviors in
*  2D environments. And this is very consistent with other research done in artificial life, where
*  if you got to the environments, you can have these waves of parasites that try to destroy
*  some self-replicators that replicate in the other direction.
*  Yeah, it's really remarkable. Basically, a lot of things we see from the world and biology appear
*  in this completely different setup. In fact, for me, it would be really interesting to manage to
*  prove that this kind of evolution that we observe in our world is not something that is special to
*  our world, but just happens naturally. It's a very natural thing to occur. And it's not that
*  the world is special and that had a lot of coincidences that caused evolution to go on
*  the way it did. It's just even in simple setups or whatever, it would be really nice to prove that
*  we managed to have this emergence of life, self-replication, whatever way you want to call it.
*  That is maybe a good transition to some big picture philosophical questions that I have for you.
*  One thing is just, it seems like most things go extinct. Should that be my understanding? You said
*  even when you put in a self-replicator purposefully, there's still only like a 23% chance,
*  I think you said, of it taking over. Do I understand correctly that the other 77% of the time
*  it's going extinct? And if I think of this through like a Robin Hansen, great filter sort of lens,
*  this sort of work would make me update my worldview away from the idea that the origin of life was the
*  super hard step or that the formation of self-replicators maybe to be a little bit more
*  generic in my or abstract in my terminology. And it makes me more think that a lot of things are
*  probably popping up in the universe and fizzling out before they get to the point where they are
*  putting out the sort of radio signals that we're putting out or certainly like starting to colonize
*  space. Does that seem like a justified interpretation? My way to think about that
*  is yes, once you have a self-replicator, you still have only one chance in five of actually
*  doing something. But the chances of having a self-replicator in my opinion, like even lower,
*  it's just all steps are hard. And maybe if what we think of what the simplest step is,
*  okay, there is a self-replicator, like now it just needs to take over. That's already hard.
*  Then maybe just on the other hand, it's just that the all the other steps were even harder.
*  But I want to be more of an optimist right now. Even in our experiments, even if it's only 23%,
*  the chance that one single self-replicator takes over, we observe a much higher than that chance
*  that in 16,000 epochs, self-replicators arise. So I think it's about 40% in the first 16,000 epochs
*  and you can go for much longer. So even if the individual one might not be the trigger for
*  this state transition, it's still quite likely to happen. The real question that I think matters
*  more is how close is this to what you observe in the real world if you're interested in the biological
*  implications of this. And there are many things that this thing doesn't have yet. For example,
*  a clear way to accumulate complexity, because as you pointed out, we only have 64 bytes per string
*  and it's very difficult to go beyond that number because there's no easy way for strings to connect
*  to each other in a stable way. And biology has that all the time. It can accumulate more and more
*  complex strings. So we would want to explore directions which are similar to that as well,
*  if you want to try to assess how likely it is for life in the biological world to happen. But there's
*  still so many similarities that I think it's an interesting starting point. You can see here the
*  representation of how often you actually get a self-replicator and within the first 16,000 steps,
*  it happens like 40 to 60 percent of the time, which is quite remarkable because
*  it's still all the appealing from chaos. So you would think that's less likely.
*  Again, this is not the probability of self-replicator appearing, it's the probability
*  of self-replicator taking over. This is even if the first one doesn't succeed, then someone else
*  will afterwards reasoning that you can have. So NA here means that it didn't happen? It didn't
*  happen. And you can see that at any point it didn't happen like 40, 60, 65 percent of the time.
*  In this case, there's just so much noise that nothing could possibly happen.
*  But in this setup, this is the setup in which you observe a self-replicator dying in 87 percent of
*  cases. But even if it does die, then something else takes over anyway afterwards. That bit about
*  the frequency of mutation is really interesting too. When you get up to that 1 percent
*  mutation rate, then it becomes very hard for anything to persist. I was thinking that when
*  I look at so much of the, at least the popular science discourse around life out somewhere in
*  space sort of says, oh, this planet might have water and therefore it might be conducive to life
*  and unsaid there is as we know it. And this work also makes me think that
*  there's probably just a lot more space for life that who knows, right? It could be extremely
*  weird, but I no longer feel like, oh, if you don't have water, you couldn't have life on that planet.
*  Now I'm thinking you could have a gas giant that could have life in it, right? Who knows, right?
*  It just seems like there's, if you can see this much complexity in this simple of a system,
*  then I don't really have any reason to be prejudiced against what's going on at some depth
*  in Jupiter. Maybe I would have some reason to think that planets need an atmosphere or they need
*  some sort of shield because they can't be just totally bombarded with crazy radiation that's
*  going to cause too much noise in the system. But I feel like even at the level of substrate,
*  I have to be pretty open-minded now in view of these results.
*  These results. You're nodding. It looks like you interpret that similarly.
*  Even with very high levels of radiation, you can still have life happening. It's just that
*  it's going to be probably smaller. And even that would be interesting to observe. One extra thing
*  that this shows, at least I think is an interesting direction, is sure you can think about what can
*  happen in our universe, but we are not restricted to our universe when we do simulations. So what
*  we are showing here is a completely different computational substrate, which is as similar
*  as to what biology can show, but we can do many different things. And we can really be creative
*  here for trying to figure out how to create interesting and complex life in those directions.
*  And ideally, ultimately intelligence as well. Perfect segue to one of my big questions,
*  which is what should we take away from this for the purposes of understanding what the future of
*  life and artificial intelligence turned to life might look like on our planet?
*  My gut says, again, I should just be very humble in terms of what my
*  expectations are. If you can create something that looks this much like life in this tiny little
*  space, then I think we're headed for a world in which some form of AI begins to self-replicate.
*  We obviously have a very large digital ecosystem, computational environment for
*  possible things to self-replicate through. And here obviously there's not intelligence involved,
*  but if you add on intelligence and these sort of interesting primitives and put them in a big open
*  space like we seem to be doing right now with open source models, this significantly increases
*  my sense that whether it's Lama 3 or 3.1 or Lama 4 or whatever, that some version of this sort of
*  thing pops up that has the recipe for self-replication. Possibly a mix of smart and dumb,
*  but it just seems like the barrier to getting there is not nearly as high as people might
*  be inclined to intuitively think. So I think one thing that is important to keep in mind is that
*  here we are getting this spontaneous emergence of self-replication, but that's through a lot of
*  interactions. The time scale at the end of the execution when we have the first self-replicators,
*  we have seen 50 billion instructions executed. We run, I believe, three million pairs of programs.
*  And yes, you can see that running in one minute, but imagine if open source AI models gain a chance
*  of the capability to self-replicate. And even if that were to happen, it would probably be quite
*  unlikely for it to happen at the frequency and at a speed where we have time scales that are compatible
*  with what we are observing here, which of course doesn't mean that some risk we shouldn't take into
*  account. In particular, what I would be more concerned about is the risk of subsequent
*  modifications, like imperfect self-replication, just taking things farther away from its original
*  intended limitations or whatever it is that we have in properties. But I don't think that the
*  insights we see here are particularly applicable to larger scale models that would execute at much
*  slower speeds and with restrictions. And we still also, the space that we let them execute in is
*  significantly more guarded in some sense. Here we have a world in which you can just copy yourself
*  over on any other string. And I do not know this, but I would expect that even for open source models
*  it would be quite hard for them to be able to just take over any random computer for the foreseeable
*  future. If that were to happen, I would be concerned by other things first and then by
*  the subsequent ability of further evolution happening. I think we would have other problems.
*  Can you put a little more detail on those other problems too?
*  I think that would imply that all of our computer infrastructure is utterly broken
*  and security infrastructure and any malicious actor. Oh, that's true though, right?
*  Yeah, that's why I'm not that confident that it will not happen. It's not all broken, but it's
*  a lot broken. Yes, that's fair. You guys at Google live in a world of the best computer
*  security infrastructure in the world by perhaps a significant margin and the rest of us out here
*  are barely updating our passwords. So I would say if the problem hinges on or if the upshot would be
*  that would mean our security is bad, look no further than just how many different branches
*  of the US government have been hacked at the highest levels. The White House has been hacked,
*  Congress has been hacked. It's all been pretty, my working assumption is that we're all pretty well
*  and thoroughly hacked. That could be. I think the main biggest takeaway is not to underestimate the
*  effect of subsequent modification over time. I don't think that open source models coping themselves
*  over are even just the biggest risk of open source models themselves, but my idea of work is not
*  AI risks and I don't think I'm qualified to make an actual statement on what I should be.
*  There's a lot of different vectors of attack and a lot of different ways that things could get
*  pretty crazy. This just to me feels like one that people haven't considered it nearly enough
*  and I'm not sure I couldn't even begin to put like a probability estimate on it, but whatever my
*  implicit non-explicitly calculated sense previously was, this does pull it in for me because I'm just
*  like, man, there's just a lot going on here. The possibility of a sort of ecology rising
*  in such a limited space. Then I just look at the complexity and the vastness of the digital
*  ecosystem that we have today and I'm like, there's a lot of green field out there.
*  Even if Google's systems are super secure, plenty are not. It seems like there is at least some
*  non-trivial possibility that you could have a digital ecology start to come online or
*  an AI ecology start to come online and maybe that's even good. One of the things I always
*  think about with life in general is just the fact that it is homeostatic and that there's these
*  many buffers that exist within any given system. Those things may be really good for us long-term.
*  We might be in a better situation if we have a more ecological model of open source AI versus
*  an sterile planet that suddenly has something super powerful pop onto the scene and have a
*  much larger chance of going to dominance. I have no idea really. It's very speculative,
*  but this work has at least got me reconsidering with a more open mind, which I think I might be
*  totally going in the wrong direction, but it still feels like we're in this phase of time where
*  these sorts of thought provokers for those of us that do sit around trying to think about
*  what's going to happen with AI, they're valuable regardless because we need to be more open-minded.
*  We need to entertain the weird, I think a lot more than we're naturally given to. For me,
*  this is a great spur in that direction. This goes back to the point that Luca was trying to say.
*  Yes, we shouldn't underestimate the cascading effect of interaction. If you have a self-propagator
*  with a certain amount of mutation and then it mutates many times, the results can be unpredictable.
*  At the same time, we need to highlight that, first of all, if you're just copying
*  something which is equal to something else, if you have a perfect copy, nothing interesting would
*  come up. Only when you've got mutations and variants, then something interesting can happen.
*  This is very much an open problem that the field of artificial life in particular,
*  but also deep learning and evolutionary strategies has been studying for a long time.
*  We still don't know how to create unbounded complexity of behaviors. Right now, one very
*  open question even in this very small experiment that we've done is would this have a limit in
*  amount of complexity that it can show? How could we make it not have a limit in the amount of
*  complexity? Most experiments that I'm aware of did eventually plateau at a certain level where
*  they couldn't escape. Before ringing alarm bells and saying this might go all the way to a high
*  level of intelligence or copying an alarm many times with variation would go to a high level
*  of intelligence, we would need to have a much stronger belief and evidence that we can accumulate
*  complexity in this way. Yes, although we are making something that is extremely complicated and capable
*  in a lab and putting it out there in a way that it can potentially interact with other things.
*  The way I'm thinking about the open source AIs now, and I don't mean this to be in a prejudicial
*  way of good or bad because I'm increasingly more open-minded to this notion that an AI ecology,
*  should such a thing exist, might be protective or might be good in its own way.
*  We're certainly giving some future AI life forms a major shortcut by building their brains for them
*  and then releasing them into the wild. It seems like we've done one of the really hard parts of
*  creating this future in a way that was not random. Obviously, we've engineered these
*  systems and figured out how to train these things. My kind of mental model, I wonder if you guys could
*  attempt some simulations like this. I don't have nearly enough confidence in this domain to know
*  exactly what this would look like, but I wonder if there would be a way to combine something that
*  has intelligence with something that's really simple or primitive in the self-replication sense.
*  Is there a way to look at... People are doing these sorts of things with Canon, LLM,
*  can GPT-4, can Gemini or whatever find day zero exploits in software. I'm trying to close in on
*  something that's... Man, you have these pretty simple self-replicators that seem to work here.
*  Then separately, we have these language models that are able to code and able to assess code
*  and debug code to varying degrees, of course. Is there a symbiosis type model there that could
*  make sense? Is there something in that mix that could be modeled in a closed environment
*  that could shed light on what the future of open source, just as it evolves through time,
*  might look like? I don't have the answer to that question, but I'd love it if you did.
*  No, we don't have an answer, of course, but I think that the closer we get to high level of
*  intelligence, the more relevant trying to have a setup for understanding the risk becomes and how
*  we can control it. In our simple experiments, there's little to no risk that they can take
*  over, especially because they cannot do more than modify 64 bytes. But if you get to more and more
*  levels of complexity, such as on LLM, then you really need to think about what you're doing.
*  I think that this should be taken into account. I have, and that may be an interesting point of
*  view here. So first of all, if defining life is hard, defining intelligence is harder.
*  I will not claim to have a definition of intelligence. When you say these things about
*  can you find zero day exploits with LLM, some things like that, that makes me think I have a
*  bit of a background in computer science Olympiads. And for that matter, there are actually
*  sponsored experiments you've probably heard of. There is this AIMO. I don't know if that's something
*  you're familiar with. I'm not immediately sure. This is, I think, extremely fascinating experiment.
*  I'm aware I'm digressing significantly from the main topic of the paper at this point.
*  There is an extremely fascinating experiment where there is this International Mathematical Olympiads.
*  And there are these efforts that try to get AI to just solve half of the problems
*  in the Math Olympiad. We are not there yet. I don't know if you want to classify the ability
*  of doing Mathematical Olympiads as intelligence. My opinion is correlated.
*  Certainly some form of intelligence.
*  You can be intelligent even if you cannot do Math Olympiads, I would claim. But if you think
*  of these kind of questions, then I'm not even sure if we can actually say that the system is
*  intelligent now. So when you say, okay, stop mixing in self-applicators and intelligence,
*  I don't think I even know how something like that would look like, if that makes sense.
*  Yeah, that's fair enough. I tend to use a pretty functional definition of intelligence. The one
*  that I've been using in very different types of conversations where I'm talking to business owners
*  about using language models to automate tasks is that intelligence is the ability to perform
*  useful work without fully precise instructions. So your number recognition is a great toy example
*  that I tend to start with, the MNIST dataset of you can recognize these numbers. Nobody knows how
*  to write fully explicit code that can recognize numbers, but we can definitely train an AI to do
*  it. That ability to succeed when we don't have the full algorithm is, I think, an interesting
*  functional definition. I'm not sure how much the definition really matters. I think what would
*  matter maybe most in the context of the work that you guys are doing is, is there a way that you
*  could mix in a language model or any sort of model, I think most of my language models,
*  into a simulation like this in a way that makes the self-replicator much more likely to take over?
*  In practice, no. For a very simple reason, that you're not going to be able to run a million
*  iterations of a language model in any reasonable amount of time. Yeah, you need real computer that.
*  Probably you could do that experiment if you start using half of the computers on the planet,
*  but arguably there are better things to do with half of the computers on the planet than just
*  seeing if you get self-replicators slightly faster. Yeah, although it depends on how much
*  you think the AIs can help succeed. If they're really effective, then you might not need that
*  much compute. We imagine ourselves taking over sterile planets, not through random brute force
*  search of the ways to do it, but by actually being smart enough to show up and get it right the first
*  time. I don't think Lama 3.1 is probably there today, but you could imagine a level of effectiveness
*  that might greatly reduce the compute requirements. Yeah, I think it makes sense to think that
*  a variant of our experiments with self-replication can be used to find better ways to find, let's say,
*  evolved agents. This is part of what we want to explore, but of course, we are starting from
*  literal strings of code and getting to something as complex as an LLM will take quite a while.
*  I think that we should take account for the risks at every level and increasingly so,
*  the more complex our systems become. But Luca's point is very well taken that the bigger the model,
*  the more costly this would be. So to have something like this work, we would need to have much more
*  efficient models to start with. Okay, cool. This is a fascinating discussion. I love the work. I
*  think I should probably let you guys get back to it. Anything else you wanted to touch on that we
*  didn't get to before we break? I think we discussed pretty much all the aspects of the paper in
*  quite in detail. Fascinating work, thought provoking, maybe more thought provoking for
*  me than you intended to be for the average reader. But that's the business that I'm in,
*  is trying to go grab these random things and use them to at least stimulate some creative thoughts
*  about where the future might be headed. And you've certainly helped me do that. So I really appreciate
*  it. Appreciate the time today. Ettore Randazzo and Luca Versari from Google's Paradigms of
*  Intelligence team. Thank you both for being part of the cognitive revolution. Thank you. Thank you
*  very much for having us. It is both energizing and enlightening to hear why people listen and
*  learn what they value about the show. So please don't hesitate to reach out via email at tcr
*  at turpentine.co or you can DM me on the social media platform of your choice.

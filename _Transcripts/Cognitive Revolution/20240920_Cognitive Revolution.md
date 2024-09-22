---
Date Generated: September 22, 2024
Transcription Model: whisper medium 20231117
Length: 4712s
Video Keywords: []
Video Views: 676
Video Rating: None
Video Description: In this episode of The Cognitive Revolution, Nathan explores the cutting-edge intersection of AI and biology with Stanford assistant professor Brian Hie. Discover how AI is revolutionizing our understanding of biological systems and creating new possibilities for interventions. Brian discusses his groundbreaking papers on hybrid AI architectures, the surprising capabilities of language models trained on DNA sequences, and AI-guided evolution of antibodies. Join us for an insightful journey into the future of AI in biology, touching on biosecurity, drug discovery, and the challenges of interpreting AI models in biological contexts.

Links : 
Brian Hie: https://x.com/BrianHie
Scanorama paper: https://www.nature.com/articles/s41596-024-00991-3
Mechanistic Design and Scaling of Hybrid Architectures: https://arxiv.org/pdf/2403.17844
Sequence modeling and design from molecular to genome scale with Evo: https://www.biorxiv.org/content/10.1101/2024.02.27.582234v2.full.pdf
Unsupervised evolution of protein and antibody complexes with a structure-informed language model : https://static1.squarespace.com/static/562d385fe4b0e2b30b0c79b4/t/668c6729471412128dd04ce0/1720477482498/science.adk8946.pdf

Apply to join over 400 Founders and Execs in the Turpentine Network: https://www.turpentinenetwork.co/

SPONSORS:
80,000 Hours: 80,000 Hours offers free one-on-one career advising for Cognitive Revolution listeners aiming to tackle global challenges, especially in AI. They connect high-potential individuals with experts, opportunities, and personalized career plans to maximize positive impact. Apply for a free call at https://80000hours.org/cognitiverevolution to accelerate your career and contribute to solving pressing AI-related issues.

Brave: The Brave search API can be used to assemble a data set to train your AI models and help with retrieval augmentation at the time of inference. All while remaining affordable with developer first pricing, integrating the Brave search API into your workflow translates to more ethical data sourcing and more human representative data sets. Try the Brave search API for free for up to 2000 queries per month at https://bit.ly/BraveTCR

Omneky: Omneky is an omnichannel creative generation platform that lets you launch hundreds of thousands of ad iterations that actually work customized across all platforms, with a click of a button. Omneky combines generative AI and real-time advertising data. Mention "Cog Rev" for 10% off https://www.omneky.com/

Oracle: Oracle Cloud Infrastructure (OCI) is a single platform for your infrastructure, database, application development, and AI needs. OCI has four to eight times the bandwidth of other clouds; offers one consistent price, and nobody does data better than Oracle. If you want to do more and spend less, take a free test drive of OCI at https://oracle.com/cognitive

RECOMMENDED PODCAST:
This Won't Last - Eavesdrop on Keith Rabois, Kevin Ryan, Logan Bartlett, and Zach Weinberg's monthly backchannel ft their hottest takes on the future of tech, business, and venture capital.
Spotify: https://open.spotify.com/show/2HwSNeVLL1MXy0RjFPyOSz

CHAPTERS:
(00:00:00) About the Show
(00:00:22) About the Episode
(00:03:22) Introduction and Overview
(00:03:55) AI for Biology: Big Picture
(00:05:49) Challenges in Biology and Drug Discovery
(00:08:36) Scanorama and Single Cell Transcriptomics
(00:10:27) Brian's Research Identity
(00:13:00) Mechanistic Design of Hybrid Architectures
(00:14:52) Evo: DNA Language Model (Part 1)
(00:18:10) Sponsors: 80,000 Hours | Brave
(00:20:44) Evo: DNA Language Model (Part 2)
(00:28:58) Gene Essentiality and Evo's Capabilities
(00:29:19) Unsupervised Evolution of Protein Complexes (Part 1)
(00:31:02) Sponsors: Omneky | Oracle
(00:32:24) Unsupervised Evolution of Protein Complexes (Part 2)
(01:10:27) Improving Antibody Binding Affinity
(01:14:24) Overfitting and ARC Institute
(01:18:11) Outro

SOCIAL LINKS:
Website: https://www.cognitiverevolution.ai
Twitter (Podcast): https://x.com/cogrev_podcast
Twitter (Nathan): https://x.com/labenz
LinkedIn: https://www.linkedin.com/in/nathanlabenz/
Youtube: https://www.youtube.com/@CognitiveRevolutionPodcast
Apple: https://podcasts.apple.com/de/podcast/the-cognitive-revolution-ai-builders-researchers-and/id1669813431
Spotify: https://open.spotify.com/show/6yHyok3M3BjqzR0VB5MSyk
---

# The Evolution Revolution Scouting Frontiers in AI for Biology with Brian Hie
**Cognitive Revolution:** [September 20, 2024](https://www.youtube.com/watch?v=1VVAF4qZKAw)
*  Hello and welcome to the Cognitive Revolution, where we interview visionary researchers,
*  entrepreneurs, and builders working on the frontier of artificial intelligence.
*  Each week we'll explore their revolutionary ideas and together we'll build a picture of
*  how AI technology will transform work, life, and society in the coming years.
*  I'm Nathan Labenz, joined by my co-host Eric Torenberg.
*  Hello and welcome back to the Cognitive Revolution. Today I'm speaking with Brian He,
*  an assistant professor at Stanford and innovation investigator at Arc Institute,
*  who is at the forefront of applying AI to biology.
*  We begin with a discussion of biology's grand challenges, understanding the causal web of
*  interactions in biological systems, and designing interventions which are both effective and
*  narrowly targeted. Brian offers his perspective on our progress in these areas and insights into how
*  AI is already beginning to change the game. From there we discuss three of Brian's recent papers,
*  each representing a different facet of his work. We start with mechanistic design and scaling of
*  hybrid architectures, a paper that describes a semi-automated way to build novel machine
*  learning architectures from primitives, including the attention and state space mechanisms.
*  This paper shows that small model performance on toy problems, aka micro skills, is highly
*  predictive of their performance at much larger scale. And while this paper is very much focused
*  on machine learning techniques, the insights that they derive are useful for the long sequence
*  challenges of biology. Moreover, the techniques themselves suggest that a sort of directed
*  evolution applied to machine learning is likely to create a Cambrian explosion of AI architectures.
*  From there we move on to EVO, a hybrid attention and state space language model
*  that demonstrates surprising emergent capabilities, understanding higher level
*  biological concepts despite being trained solely on DNA sequences. We discuss the model's ability
*  to identify which genes are critical to an organism's survival and also to generate novel
*  CRISPR variants, as well as the precautions that Brian and collaborators took when developing this
*  model and Brian's overall perspective on the biosecurity landscape. Finally, we discuss
*  Brian's work on using AI to guide the evolution of antibody complexes. In another result that
*  demonstrates AI's remarkable ability to generalize out of distribution, Brian and his team have been
*  able to use a model that was trained with three-dimensional structured data representing
*  single proteins to create antibodies that can be up to 25 times better at binding to their targets
*  than their natural counterparts, with obvious implications for drug discovery and development.
*  Along the way, we touch on broader themes in AI for Biology, including the challenges of
*  interpreting models that are trained on data types which humans did not create and really only
*  partially understand, the compute requirements for cutting-edge research in AI for Biology,
*  and the need to account for evolutionary dynamism in AI system design. As always, if you're finding
*  value in the show, we'd appreciate it if you'd take a moment to share it with friends, write a
*  review on Apple Podcasts or Spotify, or just leave us a comment on YouTube. And if you have any
*  questions or feedback, feel free to reach out either via our website, cognitiverevolution.ai,
*  or by DMing me on your favorite social network. Now, I hope you enjoy this survey of important
*  frontiers in the application of AI to Biology with Professor Brian He. Brian He, Assistant Professor
*  at Stanford and Innovation Investigator at ARC Institute, welcome to the Cognitive Revolution.
*  It's great to be here. Thanks, Nathan. I'm excited for this. You have been a part of the
*  really remarkable research publications recently. A couple that I kind of felt as I encountered them
*  came from different parts of the world, but you were involved with both. So I think it's going to
*  be a really interesting conversation to understand those projects more deeply and also to try to make
*  some connections between them. I wanted to maybe just start off with really kind of big picture
*  survey of the landscape of AI for science and maybe more specifically AI for biology.
*  I'll just kind of float my understanding at you and you can critique it, tell me what I'm missing
*  or how you would characterize things differently. And I'm not a biologist, so I'm probably going to
*  get some stuff wrong. I'm not a biologist. I see kind of two, at least two, but two that really
*  at least two, but two that really jump out to me, grand challenges in biology. One is understanding
*  how things work. What is the sort of causal web of interactions between all the different
*  parts that make up a living being? What interacts with what? What's upstream and what's downstream?
*  And ultimately, for the purposes of what most people are really interested in, which is like
*  better medicines, longer, healthier lifespans, figuring out all those interactions is necessary
*  to understanding what we want to target if we want to intervene in biological systems,
*  most importantly ourselves. Second one I identify is once we have a target identified,
*  then we have to figure out how can we actually intervene and do something with respect to that
*  target in a way that is both hopefully effective, but also specific. So we're not like causing other
*  sorts of unintended impacts on the system. My sense is that the second one has been, we've made
*  major, major progress on that in the last few years, and AI has certainly had a major role in that.
*  I mean, I only see an increasing role for that going forward. The first one seems like we're
*  starting to see some signs of figuring that out. And some of your work is like, I think a hint of
*  maybe what's to come there, but it seems like we're maybe not as far along. How would you react to
*  my big picture overview? No, I think you actually have a pretty good understanding of the current
*  big picture in biology. So yeah, especially when it comes to say like drug discovery and curing
*  disease or preventing disease. I feel like that the first question, what is the actual
*  causal mechanism of the disease? That is probably the most important question,
*  or the most pressing one, and also the most complicated one. I mean, the reason why most
*  drugs fail in the clinic is not because you failed to develop a good binder for your target,
*  or you didn't have the right small molecule or antibody for the target. The reason why most
*  drugs fail in the clinic is because you just went after the wrong target to begin with, or you have
*  these endless debates like in Alzheimer's, you know, is amyloid the right thing to target or not?
*  Or in some diseases, we just have no idea what causes the disease. And so it's hard to design
*  a binder to something when you don't even know what to bind to. So I think definitely
*  that's a big question. We're interested in this question. From a machine learning perspective,
*  I think a lot of this question is fundamentally data limited, actually, at least in my view,
*  because in terms of actually profiling biology and disease, we can collect lots of observational
*  data, actually. So you take a snapshot at a given point in time, and you can profile a ton. You can
*  look at the whole genome sequence, you can do a single cell RNA sequencing, so you count up
*  how often those genes are actually turned into RNA. And if the genes are turned into more RNA
*  than others, like maybe that gene is more relevant for some given condition or not,
*  we can collect a lot of this observational data and get a pretty full snapshot of the biology
*  at two different time points or in two different conditions. But biology is so complicated that
*  even if you have really high resolution snapshots of two different conditions, and you can just
*  observe this, you know, a lot of things that are different between the two snapshots in health and
*  disease, most of those are just totally not related to the actual causal mechanism at all,
*  actually. It's because biology is so complicated that there's a lot of just spurious correlations.
*  And oftentimes, the actual causal factor will just not be measured or that the measurement looks like
*  nothing has changed between the two conditions. But actually, that's the real cause of targets.
*  This is what we deal with in biology. And especially in machine learning, the only way
*  fundamentally to get to this question is to actually collect a lot more interventional
*  data. So you actually make a perturbation biologist like to call it. Or actually,
*  instead of observational data, you need to collect the interventional data. And hopefully that will
*  get us closer to this question. Yeah, keep going. And this might be a good time to bring in a little
*  bit of the Scanorama work that you've been involved with. Because it seems like that is a step in this
*  direction, right? Yeah. So early on in my graduate career, actually, which the Scanorama paper is
*  part of, I was working in this area, like this single cell transcriptomics. So the idea is,
*  you know, you can measure which genes are turned on or off via the RNA sequencing across millions
*  of cells. And then the Scanorama paper in particular was asking, you know, you have a bunch of different,
*  you profile the same tissue, but across different laboratories, and they're all actually like
*  slightly different. So can you try to align these two data sets together? Find which cells are
*  actually the same across the two different labs and kind of integrate information across multiple
*  data sources. And yeah, single cell at the time was, it still continues to be a big area of effort
*  for algorithm development and now machine learning modeling development. But that was my first
*  exposure to this kind of grand challenge in biology. Like how do you separate the causal
*  changes from the observational changes? And we did try in that line of work, Scanorama,
*  but also other algorithms that I was working on for this problem. Fundamentally, I was just looking
*  at the data and being like, there's only so much causal information you can learn from observational
*  data alone. And so that's why I kind of took a hiatus from working in this area. But I think
*  there are a lot of efforts now in trying to collect this causal data. And once these efforts
*  have completed, I think it's then probably a good time to revisit this question. Yeah.
*  Yeah, it seems like we may make some in silico progress as well. That seems like another
*  extremely promising thing, but let's build up to that. Yeah. Over the course of a couple papers.
*  Yeah. There's many ways to do it. You can collect the data. I mean, if you could go the other way,
*  bottom up from the level of atoms to molecules to interactions and get perfect mechanistic model
*  of systems biology and model everything in silico just from first principles upwards,
*  then this is another way of potentially getting at this problem. Maybe without doing a ton of
*  interventional data, you have an actual mechanistic theory of the cell or something that describes
*  the biology perfectly. And then you can also think about causality. And I think we've been
*  interested in actually both directions and maybe we're working on both directions and maybe they'll
*  meet in the middle or something. Yeah. That meeting in the middle, that sounds right to me.
*  So let's go through a couple of your recent papers in some depth and then we can kind of flesh out
*  this future vision and it'll be much more grounded for folks having understood what you've already
*  put out a series of recent papers. So I guess maybe just one quick sidestep, how do you think of
*  yourself as a scientist or researcher today? Cause we're going to go through one that's like
*  purely ML, then we're going to go through one that's like AI meets bio. And then the third one is like
*  the most on the still AI and bio, but like more toward the bio side. What's the taxonomy of
*  activities in your own mind? Yeah, I feel kind of it's weird. I get asked this somewhat by people
*  it just described like, you know, someone's a biochemist or someone is a mathematician or
*  someone's, yeah, I think I still say computational biologist, but in biology, especially for a long
*  time, computational biology, I feel like was kind of looked down as being like not as rigorous or
*  maybe the models are not as good and the biologists kind of didn't believe the models. And so rightly
*  like kind of looked down at computational biology, but I think computational biology as a field is
*  actually really getting a lot better. Rapidly ascended for sure. But I think like there's one
*  version of computational biology where you're like in the mushy middle and don't know anything
*  about both. But I think there's a better version of computational biology where it's like actually
*  hard and it requires you to become a decent expert at just fundamental biology and machine learning
*  or the algorithm side and the intersection. And so I think that's the version of computational
*  biology that I try to practice. And so it does end up looking like sometimes we publish things
*  in, you know, ML venues and sometimes we publish things in journals and stuff. Yeah.
*  Yeah. Okay, cool. Well, let's start with this paper, Mechanistic Design and Scaling of Hybrid
*  Architectures. This is a pretty much pure machine learning piece of work, though, in a way, if I
*  really squint at it, I can sort of see it as like a beginning of sort of ecology of ML architectures.
*  That's maybe a bit of a stretch, but not honestly, that is something that I do have a sense that we
*  are entering a new era where the last few years obviously has been just totally dominated by
*  transformers and attention is all you need and so on and so forth. And now what this paper is looking
*  at is saying, hey, we've got now a couple of different core mechanisms, like, of course,
*  attention is still part of what you need, but there's also new stuff, like we have the state space
*  mechanism that is working remarkably well too. And this paper looks at how these different core
*  mechanisms perform differently on what I like to call micro skills. And these are things like
*  in-context recall, fuzzy recall, noisy recall, selective copying, compression, memorization.
*  These are things that are not like your grand big picture large language model, most impressive
*  examples, but they are the micro skills that make those larger things possible, or at least that's
*  how I think about it. And so now that we have this, you know, state space model to kind of compare
*  and contrast against attention, and I think by the way, more probably coming not too far behind,
*  we've got to figure out like, what are the recombinant, if you will, forms of this that
*  are ultimately going to work best for us? And this is what this paper sets out to investigate. So
*  with that prompt, tell us about the investigation that you did there and what you guys found.
*  Yeah, I think it's quite interesting. And this paper was like really driven by a really talented,
*  I think at the time, graduate student, or he was maybe working together, Michael Pauly.
*  And it's interesting that you brought up the need for taxonomizing or something. And I think Michael's
*  first version of the code is called like zoology or something. Like there's now like a Cambrian
*  explosion of different architectures. Actually in biology, in terms of speciation events and
*  diversification, often what we see from the fossil record is that, you know, there's these long periods
*  where nothing happens. And then these bursts of evolutionary diversification, the Cambrian explosion
*  being one of them, it does actually seem like we're going through something like this now in
*  terms of architectures, where people are revisiting different architectures for various reasons. And
*  actually, in terms of like, the kind of evaluation and testing harness for comparing different
*  architectures to each other is also formalizing. Rather than, you know, someone develops in the
*  architecture and it's not like controlled in any way, or the set of evaluations for this new
*  architecture are different from the set of evaluations for the other architecture. And maybe
*  this has hindered architecture design for a long time, and I think is one of the things that this
*  that the MAD paper is trying to address, actually. So like actually being able to formalize,
*  like making sure that you design the experiments well and that they're controlled, like making sure
*  your scaling laws analysis are flops controlled between actually controlling for the amount of
*  compute to even higher level things like the set of the primitives or the microskills, like actually
*  developing a set of tasks that you can use to evaluate different architectures and compare them
*  with each other. And I think that will also be useful for this kind of Cambrian explosion
*  of architecture design. Another interesting aspect of the paper that actually did seem very biological
*  to me is that a lot of the motivation for these microskills or primitives is that there may be
*  more efficient correlates of scaling laws. So if it does better on some set of tasks, then that will
*  also translate to better scale. But, you know, doing a very extensive scaling laws experiment,
*  like chinchilla style, like flops control and everything, is actually pretty compute intensive,
*  especially if you're in an academic lab or something. But actually finding good, low
*  resource correlates of these scaling laws, I think is also pretty interesting. And we come
*  across this problem a lot of times as well in just, you know, biology, right? Like, so like you have
*  some really resource intensive readout, like a clinical trial, which like 10 years or something,
*  or even going into a mouse model or a non-human primate model. But you want like part of
*  a big thing to accelerate any kind of development process is like a good, cheap correlate of the
*  more expensive thing. So does it work just in a Petri dish? Or does it work in a chemical reaction
*  format? And does that correlate well with success in the animal? And does the success in the animal
*  correlate well with success in the clinical trial? So I think that aspect of the paper too, felt very
*  biological to me. So yeah, I think that's my reaction to that.
*  Hey, we'll continue our interview in a moment after a word from our sponsors.
*  I am really excited that our new sponsor 80,000 hours is now offering free one-on-one career
*  advising sessions to cognitive revolution listeners. 80,000 hours aims to be the best
*  source of advice for people who want to do the most good that they possibly can with their careers.
*  We typically work for about 40 years in our lifetime and we work about 2000 hours per year.
*  That is the single biggest opportunity that most of us have to make a positive contribution. And
*  it's worth being strategic about it. That's where 80,000 hours can help. I actually used their career
*  advising service myself. Two years ago, I had just finished the GPT-4 red teaming project and I wanted
*  to do anything I could to nudge the AI future in a positive direction. But what could or should I do?
*  That was not clear. After my call with 80,000 hours, I got a number of connections to outstanding
*  individuals in the space. And over the course of the follow-on conversations, I developed confidence
*  that this podcast was one of the projects that I should pursue. Today, I'm thrilled to have built an
*  audience of thoughtful, high potential people that 80,000 hours wants to help. To request a free
*  one-on-one career advising session, follow the link in the show notes. It's 80,000 hours.org
*  slash cognitive revolution. That's 80,000 hours.org slash cognitive revolution. Sign up for a free
*  one-on-one career advising session. Figure out how you can make a positive impact on the AI future.
*  And I think you'll be glad that you did. This episode of the cognitive revolution is sponsored
*  by the brave search API. You may know of brave as an alternative to Chrome, but did you know that
*  brave has its own independent search engine powered by its own 20 billion page index of the web?
*  The brave search API gives developers reliable and affordable access to programmable web search,
*  auto suggest, spell check, and more with flexible plans for all types of use cases from rag search
*  to automated business intelligence. On top of that, it's up to three times cheaper than Bing,
*  all without compromising on quality, speed, or reliability. Over 700 businesses, including
*  Coheer, Chegg, and Kagi rely on the brave search API. And a recent survey showed that 94% of
*  customers would recommend it to their peers. To start building apps with the power of the web,
*  sign up at brave.com slash API and get up to 5,000 free monthly calls.
*  Yeah. So just to flesh out a couple of details, you mentioned the term mad,
*  that is mechanistic architecture design. So part of the approach here is to say,
*  you know, we have these kinds of building blocks, like we can sort of manipulate them with code,
*  we can shuffle them around and try all sorts of permutations. And that doesn't have to be a
*  handcrafted, let's say, artisan sort of undertaking. It can be the sort of thing that you just
*  grind through with a higher level code framework to develop and test all these things.
*  And then I think you said this pretty clearly, but it does bear re-emphasizing that the paper
*  also shows that the performance at very small scale on these micro tasks does in fact predict
*  the performance of the architectures at much larger scale. Obviously not going all the way
*  to like frontier model scale, but like enough orders of magnitude there that you can start
*  to be somewhat confident that you could probably extrapolate it out a bit further.
*  And also, you know, maybe the most important thing is then you encourage or you sort of create
*  reason to believe that further research at very small scale might have similar predictive
*  properties. Obviously that's not always going to hold, but it does seem like a really
*  important just foundation laying that I expect a lot of people will probably build on top of.
*  Do you have micro skills that you think are kind of most important to the sciences?
*  And do you see any like core weaknesses in micro skills right now that we don't have
*  architectures? You mean for the actual, this is not for, you know, new architecture development,
*  right? This is for the practice of doing science, you mean? Well, partly where I'm going with this
*  is I've become quite fascinated with the CAN architecture recently. That's K-A-N from
*  Ziming Liu and Max Tegmark's group. And, you know, they're trying to do AI for science.
*  The way that they present their results is often about greater interpretability and kind of
*  composability. But I sort of see it as likely to become another one of these core mechanisms that
*  if there is a MAD2 to come, then this might be another one of the core mechanisms that gets
*  folded into the shuffle. And ultimately we see like what share of layers it can earn for itself.
*  But I guess to try to develop my intuition for that, I'm wondering kind of, you know,
*  at some point we may have like enough of these core building blocks, core mechanisms. I don't
*  think we're there yet, but my best intuition for sort of how to know if we had enough would be,
*  are there still micro skills that we see like the current architectures just like can't handle?
*  Yeah, this is interesting. And I guess I didn't touch upon like the main finding of that paper,
*  right? Is that like rather than a pure architecture, you know, all the layers are
*  transformer layers or something, or all the layers are hyena, that actually like hybridization or
*  just mixing different layers tends to work better than pure attention. And now, you know,
*  like one in eight to one in 10 layers of attention combined with mamba or hyena or something does
*  seem to be like pretty good in practice. Like actually in a model that we have, like the EVO
*  model, we actually use like three out of 32 or something layers of attention. So around one in
*  10 or so. Yeah, I think that in terms of the composition of the layers, as well as like the
*  primitives with which to assess the right composition of the layers, I guess brings up
*  like a meta question of like, how do you actually find the right tasks to begin with? And so yeah,
*  I'm not sure. Yeah, I think there's just a lot of work to be done. I don't want to speculate too
*  much on this. Yeah, the cans thing I think is going to be, it feels to me like there is something,
*  you know, that the Arc AGI challenge has kind of captivated at least a portion of the field recently.
*  And there's this sense that, which I think is a little bit overstated, but nevertheless,
*  definitely has some truth to it that like language models can't reason. I always say to that, well,
*  I think they can reason just not necessarily super well, keeping in mind that a couple years
*  ago, they couldn't reason at all. So, you know, going from none to some, to me suggest that
*  there's probably more to come. And this is where I'm like, not entirely sure, do we need a new core
*  mechanism? Or maybe just keep scaling what we have, and that could be enough. When I look at the can
*  thing, I do see something really seemingly fundamentally new there, just the ability to
*  compose functions, the ability to have like, to initialize with particular functions in place,
*  you know, you can build like a calculator into a neural network. And there may be also
*  just logical operators that need to be kind of woven in somehow too. I was just reading
*  the latest Wolfram piece. I think it's probably, I don't expect you've got to that one yet,
*  because it just came out in the last three days. He, as always, kind of reformulates,
*  in this case, he reformulates machine learning in terms of like cellular automaton, what not.
*  And there's a pretty extensive section on how to create just these like, very discrete logical
*  operators in a sort of machine learning type context, you know, how do you make a and gate
*  or a not gate or an XOR gate or whatever, right? And it's like these sorts of things that we know
*  how to make to some extent, or kind of being approximated or being converged on in neural
*  networks. But it seems like maybe we could get a lot farther, a lot faster if we like initialize
*  with some of those structures baked in. I don't know if it's necessary, but it feels because you
*  might just get, you know, again, scale might solve everything, but it feels like it is a really nice
*  shortcut. And then it will also probably hybridize really well with, you know, in the way that this
*  paper sort of explores. Yeah, definitely. I mean, this is a big question, right? Like,
*  how much of these architectural changes are actually useful or how much of it gets washed
*  out with scale. And I think a lot of this stuff will be empirical, and we just need to design the
*  right benchmarks to actually test and just ground the actual model development in actual empirical
*  performance. But I do think in terms of all these, there's like new architecture development,
*  at the very least, like you get comparable perplexity or something or comparable
*  performance, like modeling performance, just like, you know, it just fits better in our academic
*  compute instance or something. Or the MFU is just higher, like the actual utilization is higher to
*  train the model and actually conferring, you know, flops controlled, just modeling improvement,
*  potentially as well. But yeah, we'll just have to see. What I like about this kind of era of
*  machine learning is the emphasis on objective benchmarks and just empirical performance.
*  Does this model just work? And I think that kind of mentality for new architecture design will drive
*  a lot of progress. Yeah, cans are very cool on compositionality and everything.
*  So before we move on, there were a number of other interesting nuggets in this paper. I
*  definitely do recommend it as one that people should check out. It's quite a thorough study.
*  You should have Michael on the podcast.
*  Yeah, I would be interested to do that for sure. I mean, his name does come up across
*  quite a few very cool pieces. But there's tidbits on mixture of experts, on the size of
*  heads, on finding that increasing data on a sort of in terms of within a compute budget, right?
*  Pushing more on data versus pushing more on parameters seems to be more helpful.
*  That last one I didn't have an intuition for, like that seems to be kind of the general trend,
*  like llama over training, whatever. But I didn't quite have a sense for why that would be better.
*  I don't know if you had one, but I'm curious if you do. And any other final notes on that
*  paper before we move on to Ivo? Yeah, I think that is an interesting observation. Yeah,
*  and there seems to have been a general trend to smaller models, more data, or just smaller
*  in parameters and more data. Yeah, I think for example, like llama three, compared to the
*  chinchilla optimal or whatever, they go like way beyond in terms of tokens actually consumed by
*  the model. For example, I think in terms of the intuition, it does seem like the models are capable
*  of learning a lot more than we thought they could, or that many thought they could. The models
*  potentially like even at 7b or something, they have enough parameters to actually learn a lot,
*  even with lots of tokens. In terms of an intuition for I mean, there are lots of parameters in the
*  model and they can interact with each other with lots of combinatorial ways. And actually, there
*  could be the same neuron is involved in many different concepts or something. And so there's
*  actually a lot of potential capacity in the models beyond just the parameter count. And this has been
*  empirically shown in smaller models. The smaller models can actually the same neuron can be involved
*  in many different concepts or something. So there's like this kind of superposition or whatever. And
*  also like training a smaller model on lots of data is really helpful for inference. So we try to think
*  about this too, like when we're making models for biology, a lot of biologists definitely want to
*  use the model. We don't want to release some trillion parameter model, 100 billion parameter
*  model and no biologist would be able to run that on their local hardware or something.
*  It would probably struggle too. Even at 7b, that might be very big for someone in the biological
*  community to use. So we actually do think about the benefit in inference with just having a
*  smaller model that's just smarter because it's seen a lot of tokens. So I think that's a useful
*  like you have the resource rich people, maybe spending more flops to get a model that's then
*  helpful for people who don't have enough compute to do inference. I don't know. These are the two
*  things that this prompt kind of spurs. Hey, we'll continue our interview in a moment after a word
*  from our sponsors. Omniki uses generative AI to enable you to launch hundreds of thousands of ad
*  iterations that actually work customized across all platforms with a click of a button. I believe
*  in Omniki so much that I invested in it and I recommend you use it too. Use Cogrev to get a 10%
*  discount. AI might be the most important new computer technology ever. It's storming every
*  industry and literally billions of dollars are being invested. So buckle up. The problem is that
*  AI needs a lot of speed and processing power. So how do you compete without costs spiraling out of
*  control? It's time to upgrade to the next generation of the cloud, Oracle Cloud Infrastructure or OCI.
*  OCI is a single platform for your infrastructure, database, application development, and AI needs.
*  OCI has four to eight times the bandwidth of other clouds, offers one consistent price instead of
*  variable regional pricing, and of course nobody does data better than Oracle. So now you can train
*  your AI models at twice the speed and less than half the cost of other clouds. If you want to do
*  more and spend less like Uber, 8x8, and Databricks Mosaic, take a free test drive of OCI at oracle.com
*  slash cognitive. That's oracle.com slash cognitive. Oracle.com slash cognitive.
*  Cool. All right. Well, let's move on to the second paper. This is maybe the paper that I mentioned
*  most on the podcast, which is kind of surprising because it's a bit outside of my standard fare,
*  but I personally find some really powerful lessons in it. So this is EVO. Full paper title is
*  Sequence Modeling and Design from Molecular to Genome Scale with EVO. And first thing to note is
*  this is using the striped hyena architecture, right? So it's one of these hybrids, as we kind
*  of alluded to, much more state space with some attention sprinkled in. It is long context, which
*  obviously the state space models really help enable, and it's trained purely on DNA sequence
*  data. And yet some interesting things start to come out of that. And the proposition gets floated,
*  is DNA all you need? Probably not, but it certainly can take you farther than you might
*  naively expect. What I take from this, and I want to make sure I'm not over interpreting it, but
*  what I see here is a really interesting data point on, first of all, prelude to a lot of what's to
*  come in AI for science and AI for biology, but even just in terms of understanding what is happening
*  in these models right now, there's so often a lot of confusion when it's like, okay, it's a language
*  model. We trained it on language. Maybe it learned this concept, but it was only, you know, you'll
*  used to hear people say, well, it doesn't really know. It's just predicting the next token. It's
*  just stochastic pair, whatever. That I think has largely been put to bed now. We can see that like,
*  there are pretty clear concepts that can be isolated within models. They're not just doing
*  pure naive correlation, but then the next kind of level of skepticism is like, well, they may
*  have learned that concept, but they learned that concept from us. We figured out the concept, and
*  then they're learning that from our representation of those concepts and language. When I get into
*  that path of discussion, then I'm like, but you need to study EVO because it seems to me that this
*  is a clear case of a model that was just trained on next token prediction, in this case, in the DNA
*  domain, actually still learning these higher order concepts in a way where like it didn't get it from
*  us. Right. It's clearly getting it from the raw data. So how do you tell that story? We can get
*  into the gene essentiality and some of the other ways that you get it, get at them.
*  Yeah. There's so much in that. Yeah. I think that's actually a very interesting dimension that I
*  actually hadn't thought of before. So yeah, we get the question, you know, is DNA all you need or
*  whatever. I mean, obviously in biology 101, right, the question on the first day of class is like,
*  is it nature versus nurture? Right. And it's like, is everything encoded by the genes or is it
*  just purely a product of your environment or is it both? So obviously like the environment is important
*  and we don't model the environment explicitly with EVO, but actually we have something similar,
*  like in language, right? It's like, you know, is this thing that's learning language actually a world
*  model or there's these questions about grounding? Like the world actually does leave its imprint on
*  like the actual distribution of sequences that you find on the internet or whatever.
*  And in the same way, the environment leaves a very clear imprint on the distribution of like
*  DNA sequences that we sample through evolution and through like selection. So yeah, this is,
*  I think the reason why the models we think are working well and will continue to work well
*  at scale is that the world does leave an imprint on the DNA sequences. So even though we don't
*  explicitly model the environment, there's potentially a lot more about the environment or
*  about, you know, higher level functions and concepts that you can learn from just raw DNA
*  sequence. And the advantage of raw DNA sequence is that it's very abundant. Like it's really cheap.
*  People have been doing whole genome sequencing or they couple all their biological experiments to some
*  sequencing readout because it's so high throughput and so cheap. And also it's just the most fundamental
*  modality in biology, like all biological information that needs to be transmitted through
*  DNA basically. Or, you know, the vast, vast, vast, vast majority and epigenetic inheritance is still
*  somewhat controversial, but especially for microbes and for most information across generations,
*  like that needs to be transmitted through DNA. And then in terms of like for EVO, yeah, and
*  what's nice about biology is that human level performance in biology is already abysmal.
*  Like it's not hard to get a model that exceeds human level performance. And there's so much in
*  nature that nature has produced that far transcends any kind of human imagination, I think. There's
*  still a ton of biological discoveries to be made and organisms, essentially in organisms that we
*  see every day in our own, in human biology, actually, there's a lot of human biology that's
*  unknown, let alone biology of organisms from deep sea vents or something. Like there's probably a
*  lot of interesting molecular interactions going on there. And I think trying to have a model learn
*  high level concepts in a fairly unbiased way across like the diversity of life, like that is what we're
*  trying to do from EVO. And actually this would be a model that's like definitely learning from a
*  different like data generating function, right? It's like, it's learning from evolution, that's the
*  name of the model. And hopefully, yeah, the idea is that if we can find a way to reliably extract
*  these concepts from the model, this is like probably the main challenge. Like the model has
*  learned something. How do we now start to interpret this model and connect it to actual biological
*  discoveries? But if we learn how to do that well, we can actually go beyond human knowledge, right?
*  We can actually go beyond, we can use the model to do biological discovery in potentially pretty
*  powerful ways. But yeah, I think that's a cool dimension. Like as an example of a large model
*  that can go beyond the concepts that humans have generated. Yeah. So tell in terms of like how this
*  is already useful, I think that I always remember first the gene essentiality thing, but I don't
*  actually know a lot about gene essentiality. So kind of give us the problem set up there and then
*  what this model was able to do and like why that's remarkable. Yeah, the problem set up with the
*  actual gene essentiality problem is an organism has some set of genes and each gene will typically
*  encode for a protein. Sometimes you have genes encoding for RNAs, but you know, each gene typically
*  accomplishes some function and the genes and maybe many genes work together to accomplish a function.
*  But some genes are essential for just the viability of the organism. So you don't have the gene,
*  you're just dead. But other genes, you take that gene out of the system, the organism actually seems
*  fine. And then that gene was maybe not even that important or is definitely not, you know, essential
*  to the reproductive viability of the organism. And this is useful for a number of things. I mean,
*  it's useful for basic biology, maybe the more essential genes are older in evolution, but it's
*  also useful for drug discovery, right? So if you have some very bad bacteria and you want to design
*  a drug against this bacteria, you're not going to target an unessential gene because if you try to
*  target this unessential gene, it's going to do nothing. You want to actually target the essential
*  genes, make sure that those essential genes aren't accomplishing their function. And by removing
*  those essential genes, you have stopped this bacteria from being alive or pathogenic or
*  something. So a very interesting experiment that we ran with EVO because it can fit long context,
*  up to 131 kilobases or 131,000 nucleotides. And some genomes are actually shorter than that. So
*  the genomes of these organisms called bacteriophages, they fit into the context of EVO. So it's 40
*  kb genome, a 40 kilobase genome. We did this interesting experiment where for each gene and
*  the genome, we insert a very bad mutation. In this case, it's a mutation to like just at the beginning
*  of the gene that tells the cellular machinery to not actually translate this particular gene into
*  protein. So if you made this mutation into an actual organism, that gene would just not accomplish
*  anything. It would just not turn into protein and therefore not be able to function. Biologists call
*  this a knockout. And you often knock out a gene by the strategy, like you insert this premature
*  stop signal, telling the protein manufacturing machinery to stop prematurely. And so you don't
*  produce the whole valid protein. So we make this really bad mutation, which basically translates
*  into a three letter insertion into a 60,000 character sequence. And we make this small
*  insertion into all the genes in the genome. And so for each insertion, we then score it just with
*  the log probes of EVO. So you just look at the likelihood of the sequence under the model with
*  and without the insertion into each gene. And what we actually see is when we make this insertion into
*  non-essential genes, that likelihood doesn't change very much. It's almost like the model's saying,
*  sure, you can put this very bad mutation in these unessential genes. It's totally fine. The likelihood
*  remains high of the full genome sequence. But an interesting thing happens when we put this bad
*  mutation into essential genes. There the likelihood drops a lot. So it's almost like the model is
*  saying, this mutation in this gene looks really bad. It has low likelihood under the model compared
*  to the unmutated sequence. And we actually can then use this and show and we can compare this to
*  experimental data. So for a lot of bacteria, we actually, people have done these experiments.
*  They're pretty painstaking experiments. We have to mutate every single gene and see how that affects
*  the viability of this bacteria or this bacteriophage. So there's databases of these
*  experiments and we just compare it. So EVO has never seen the outcomes of these experiments.
*  It's just learning. We think of it as a density model over all the genomes in the data set or all
*  the prokaryotic genomes. But even so, EVO's change in likelihoods is able to predict which genes are
*  or are not essential using these experimental measurements as ground truth. So I think this is
*  surprising in a number of ways. One, the model is sensitive to really small changes in a really big
*  sequence. So a three-letter insertion into a sequence, the model can still pick up information
*  from that. We can also show that adding sequence context helps the model distinguish essential from
*  unessential genes. So if we just give it the sequence of the gene, the model can kind of
*  predict this well. If we give it more of the genes surrounding it, the model appears to get
*  information about this gene in its genomic context and that is informative for distinguishing whether
*  or not this gene is important. So we can show that the model is actually using information from
*  multiple genes or just beyond the single gene context. It's also interesting because people
*  trying to connect a single or a small three-letter change in the genome to the fitness of an entire
*  organism, which is really complex. This is the genotype to phenotype question. This has been a
*  very challenging problem in biology for a long time. These are just zero-shot predictions out of
*  the model. So it's not like EVO has completely predicted gene essentiality across all organisms.
*  Though in some organisms, it's getting pretty close actually. So for one type of phage,
*  people did this very painstaking study where they used CRISPR to actually mutate all the genes in
*  this phage genome and determine which ones were or were not essential. And with EVO, instead of
*  doing this painstaking study, we just run the neural network through a few forward passes
*  and basically get the same information out on gene essentiality. So I think it provides a blueprint
*  for a model that could connect how changes in the genotype, changes in the DNA sequence actually
*  affect the whole organism fitness. So if I wanted to, for example, create a universal antibiotic
*  and thinking back to our first grand challenge of like, we don't really have a great sense of
*  what causes what in most of biology, it seems like what I would want to do is take all the known
*  bacteria sequences. Maybe I'd want to limit myself to ones that actually cause disease. Maybe I
*  wouldn't, I'm not sure. And then I would want to run this process through and I would want to look
*  for genes that are consistently essential across all of my targets, right? And then I would identify
*  all the things that fit that description. And then I would probably move over to the wet lab and
*  start to think, okay, which of these can I actually hit with a drug and which ones actually prove out
*  to matter? Unless that's totally mistaken, I assume that that is where this is going.
*  Yeah, that's one of many potential applications. So yeah, if you wanted to create a broad spectrum
*  antibiotic, you want to hit these very conserved genes that are common across multiple bacteria.
*  And also because they're common, they're also essential across multiple bacteria or something.
*  So if you want a broad spectrum antibiotic, you want to target these genes that are conserved
*  or common throughout evolution. And what EVO does actually, the way I think of it,
*  it's kind of like a conservation score on steroids or something. It's literally looked at,
*  it's been doing this next token prediction across thousands, tens of thousands of bacterial
*  genomes and millions of phage genomes. And so it kind of has a sense of which genes in the genome
*  you don't want to touch. Like these genes, any kind of mutation to them is bad news for the
*  organism or any change to this gene just causes the organism to be completely selected out. So
*  you don't even see it in the training data set versus this other set of genes is mutating a lot
*  in evolution. It's probably not essential to the organism. So EVO can help you, for example,
*  pinpoint which genes you don't want to touch if your purpose is to keep the bacteria alive.
*  But maybe you do want to touch those genes if your purpose is to develop an antibiotic.
*  Yeah, I guess if I were to put my like stochastic parrot skeptic hat on for a second,
*  one thing that you just said there is like, it's a conservation score on steroids. I don't know.
*  I mean, I do. I know the basic concept that genes that are highly conserved must be important. You
*  know, those that are not so conserved tend to be less important. How much does this add on to that
*  understanding? Is there a way to quantify or somehow characterize how much more we get out of
*  this versus, you know, correlation analysis and appears to be a psychiatry?
*  We also get the same sort of, you know, critique or skepticism or just observation from people in
*  biology. Like these models are just memorizing the data set and they're purely doing correlations or
*  co-occurrences across the sequences. I don't know. See, this is like, just to like briefly hint on
*  or like how you would test this. I think we've been looking especially at regions of the genome
*  that are not conserved in sequence, but that are conserved or that are related to each other in
*  terms of some higher order function. So there's parts of the genome that are just extremely
*  variable in sequence. Like they're actually enriched for de novo or new genes. So these
*  are regions of prokaryote genomes that have lots of new gene birth. So actually if you look at,
*  but they all accomplish, you know, somewhat of the same higher order function actually. So they're
*  often involved in say the bacterial immune system. So the bacteria needs to constantly defend itself
*  against invading bacterial viruses. And if you have a really conserved gene that is responsible
*  for bacterial immunity, a virus is just going to take advantage of that and, you know, hit exactly
*  like antibiotic, right? Like the virus is going to take advantage of this. So bacteria do not want
*  conserved memorized sequences in these regions. They want to diversify them in sequence, but they
*  want to preserve this higher order concept that this gene is involved in immunity. Some interesting
*  work that we've been doing in the lab actually is seeing if the model can also generate things that
*  in terms of sequence space look nothing like anything in the training data set. In fact,
*  these genes look nothing like anything in nature in terms of their sequences, but do they still have
*  this higher order concept or higher order function that they're involved in immunity? And this is
*  like where we're going. Hopefully the data looks promising, but I think this is how you would do it.
*  And I think the models are learning higher order properties. They're not just parroting out trivial
*  like, you know, variations of the same sequence basically. I do think that they are capable of,
*  you know, diversifying in sequence space quite a bit to the point where, you know, this sequence
*  looks nothing like anything that's in any of our existing knowledge bases, but it still has this
*  higher order concept of biological function. So I think we have to do the work to show that this is
*  the case because in the absence of any data, one could most conservatively say that the model is
*  just learning these sequence correlations or these co-occurrence patterns and no high level
*  concepts. And the bar is high to prove that it's doing more than this, but I do think the model is
*  doing more. That's great. Would you say that the bottom line kind of state of knowledge today,
*  it is suggestive, but not definitively proven? Like it sounds like you're in the process of
*  doing that. You believe it, but there's not like full knockdown, irrefutable evidence in the public
*  yet. I think, yeah, we and probably others just need to do the work to show that this is not the
*  case, but I'm very optimistic. Yeah. And this, I think what parallel results in language too.
*  Yeah. I mean, it's going to be very interesting to see what interpretability techniques applied.
*  I mean, the sparse auto encoder paradigm applied to EVO2 trained on 15 trillion tokens or whatever.
*  It seems like that is going to be an absolute gold mine of discovery of higher order concepts,
*  right? I hope so. Yeah. We want to do this. I mean, we're thinking of various ways of doing
*  interpretability. One of which is if you try to train an SAE and you actually do some kind of
*  expansion so that concepts are not entangled or whatever and are associated with, or there's like
*  some clean thing that's associated with some concept. I think this could be actually pretty
*  cool. The hope is that this kind of interpretive, mechanistic interpretability or this kind of work,
*  well, A, it would hopefully indicate or provide additional evidence that the models are learning
*  higher level concepts. B, it would enable us to basically do classification out of these models
*  for free. So you don't train or you don't have to do any fine tuning potentially, right? You just
*  have some kind of classifier for some interesting biological system by inspecting the activation of
*  neuron or like a concept or something. And the third is we're hoping that this also lets us do
*  this more sample efficiently. So where you don't have a lot of examples of some system,
*  but you still hope that the model has encountered enough examples of the system that are just unknown
*  that it has learned this concept. This happens a lot in biology where someone will discover some
*  new system like CRISPR. So like CRISPR-Cas, there's maybe a handful of different CRISPR-Cas systems
*  that have been discovered, but potentially in nature, we've just not discovered a lot of
*  different CRISPR-Cas systems or things that are like semantically related to CRISPR-Cas systems
*  that we would want to discover. But we only have what's observed now, but if we can get a concept
*  that's specific to our set of 20 CRISPR-Cas systems right now, then maybe we can use this to do next
*  generation biological discovery or design, right? So then you find the CRISPR-Cas neuron or the
*  gene editing neuron or whatever, and then you just clamp its activation to be really high. And then
*  you just mine the outputs of the model. So yeah, I think this kind of stuff could be really cool in
*  bio. And you're already kind of approaching that in this paper, right? I mean, the other headline
*  making finding was that the EVO model already can generate CRISPR variants. This is where I'm a
*  little bit out of my depth on the biology side. I'll ask a really naive question first, which is,
*  why do we need more CRISPR variants? Give us a little sense of that. And then
*  now we have this DNA language model that can generate tons of them. But presumably,
*  we have the same kinds of problems that we often have with especially not super-scaled language
*  models, which is like, they hallucinate. So I imagine some of these CRISPR-like things that
*  outputs don't actually work. So yeah, give us kind of the rundown of the CRISPR dimension of this.
*  Yeah, I think that's another interesting component of the study. The study is so massive. But I
*  really like this component. Yes. Why do we need more CRISPRs? Well, okay. So I mean, one actually
*  kind of troll answer is that people like to do patent busting and people actually patent some
*  CRISPRs. And then they'll put this sequence identity cut off. We patent everything around
*  80% sequence identity to this molecule. And then... It's a great answer.
*  You diversify it with a generative model and then you just patent-bust it. But also, when people are
*  designing new tools, because biology is so complicated, there's just some chance that
*  a variant of, say, CRISPR from nature will actually have more favorable properties in the highly
*  unnatural systems that we humans put these systems into. So we actually use CRISPR systems in a very
*  different context from the environment. And so just maybe by chance, all these things in the
*  environment have the same function or the same properties, but in an unnatural system, just by
*  chance, some will be more favorable than others. And the idea for a long time is if you have a
*  working system in human cells, for example, so CRISPR, if it works in human cells, great, but it
*  has low activity. Let's just look into nature. Let's just actually look for similar systems in
*  nature, test them in human cells, and by chance, one of these just might have a lot better activity
*  in human cells. This typically has just looked like mining existing sequences from nature. So
*  you just actually literally take the sequences that have been sampled by evolution and then test
*  them. With the generative model, you don't need to go out and sequence bacteria from deep sea vents
*  or the sewers or something to get more biological diversity. You literally just sample it from a
*  generative model. And so I think this is another thing that we're trying to kind of follow up on,
*  but the value of a generative model as providing additional diversity beyond the diversity that we
*  have even observed in nature. And then, yeah, what was the other component of the CRISPR
*  systems that you're interested in? Well, yeah, maybe a better formulation of that question is,
*  you know, we can now generate potentially unlimited CRISPR-like sequences. Is there anything
*  other than actually synthesizing them and trying them that you could use to figure out which ones
*  are good and how practical is it to test like a thousand or 10,000 or a million new CRISPRs?
*  Yeah, this is still fundamentally limited by like a lot of different areas of biology. So the
*  throughput with which we can test these CRISPR systems is low. We can test maybe 10 to 15 or
*  something in a reasonable amount of time and money. Where I see the models as being really useful
*  is that if you just take something from nature or someone tries to rationally design a protein,
*  the success rates in the lab will be quite low. If you just told a human expert to mutate 400
*  amino acids in CRISPR to bust this patent or something, the likelihood that that would be
*  successful is actually astronomically low, I would say. But maybe with EVO, you could get it as high
*  as 10% or something or 20% of the designs that EVO or a generative model generates actually do
*  succeed in the lab. And then the goal is to get this, it's called low end in bio ML, like this
*  kind of low end design, actually achieving this versus like having to rely on brute force, high
*  throughput methods for screening designs, which are costly and very expensive. They were very
*  expensive. If you can get the models to help out with kind of low end validation, so you just test
*  10 things and one or two of them works, I think that's already a big win in biology. But yeah,
*  we're fundamentally limited by the biological assays to validate them. And it's very important.
*  I definitely agree. The ultimate test, because the model will hallucinate or just make mistakes,
*  is to just test the thing in the lab. So maybe the last thing on EVO and then we'll move on to the
*  third paper. I know we have a time budget is just on the big picture safety side. I noted in the
*  paper that you guys say that you've excluded viruses that infect eukaryotes entirely from
*  the data set, which is a pretty significant exclusion. And that's a very prudent step for
*  such early technology. So I applaud such a thoughtful approach. Big picture, it seems like
*  this, like everything else is going to get scaled up. It's going to get better as it gets scaled up.
*  And then, right now, we already have a lot of kind of debate and concern around,
*  can CHAT GPT help me make a bioweapon? But it seems like the real sort of bioweapon generator,
*  unfortunately, is probably the same thing as the medicine generator. Because these systems are
*  understanding things at such a fundamental level that it doesn't seem separable. Maybe you have a
*  different perspective on that. But how do you think we sort of develop these technologies safely,
*  in the long term, knowing that one pandemic can be a big, big problem?
*  No, definitely. Yeah, we definitely care a lot about safety, like biosafety and biosecurity.
*  We have people in the lab testing these things out. I don't want anyone in my lab to get sick.
*  And definitely want to make sure that these technologies are used for the benefit of
*  humanity rather than to make a weapon or something like that. So yeah, there's a number of things
*  that we've been trying to do. One is in terms of data exclusion, actually excluding sequences that
*  are potentially harmful of these eukaryotic viruses. I think that was one step. I think
*  in future versions of the model, actually potentially developing a set of e-vials,
*  of common viruses or maybe even toxins. And actually making sure that the model maybe has
*  low perplexity on these sequences, or if it does understand these sequences well,
*  deliberately having them on in some kind of post-training stage. Like actually not be able
*  to reason out these sequences very well, the ones that are kind of harmful. Yeah, in terms of the
*  larger safety and security questions, I think probably the scientific community and policymakers
*  and just members of the public should have, as I said, there's some kind of standards that make
*  sense and continue to enable progress in this area, but also progress that is responsible.
*  I think I fundamentally take a very optimistic view of this technology because it's much harder
*  to create or to ameliorate bad biology than it is to destroy. Like unfortunately, if a motivated
*  state-level actor wanted to create a bioweapon, they could do it quite well without generative AI
*  already, actually. In fact, I would not use a generative model to design a bioweapon right
*  now. But I think what the technology does let us do that we just can't do well right now at all,
*  because it's much more complicated, it's much harder to create than to destroy, is to actually
*  develop cures or vaccines for these diseases that nature has already been producing and releasing
*  into the human population. It's much, much harder to design biology in the ways that we want
*  and return things to homeostasis or reduce the entropy in the world.
*  And I think that's where I think these technologies will be really useful. And that's
*  where the big capability jump, I think, is with these models is actually in enabling us to correct
*  the natural tendency of biological systems to deteriorate and get worse. It's much, much harder
*  to reverse that course. And I think that's where these generative models will make the most impact.
*  So this is why I'm optimistic about the technology. I think we should continue to
*  develop it safely with the right guard rules in place. And if we do that, then we can actually
*  have a tremendous benefit on human health. So if I summarize that in terms of offense,
*  defense sometimes, but it sounds like your point of view is the natural state of affairs
*  favors offense. And maybe the reason we don't see offense is actually just lack of people out there
*  who want to do bio weapon offense. And this technology, in addition to all the obvious
*  good things that it could bring about actually favors defense. Yeah, like it's if you want to
*  make some biological system go off the rails and deteriorate or become diseased or, you know,
*  cancerous or something, it's actually quite easy to do this already. Or you just, you know,
*  you have an organism and you just like hit them with a bus or something and the thing dies, right?
*  It's very easy for these biological systems to deteriorate. It's much harder to exactly play
*  defense or to correct things and return things to like this kind of very low entropy state where
*  the organism is nice and in some kind of homeostatic balance. And so yeah, I do recognize
*  that these technologies elevate our ability to biology broadly for good and for dual use
*  purposes potentially. I mean, this technology does elevate our level to do biology broadly.
*  But the way I see it is our current level of technology now, like we've already cleared
*  the bar for a long time actually, and our ability to make biology worse or to harm people or something
*  where our bar is right now in terms of biological capability is like far below the capability needed
*  to help people. So we've kind of already cleared the bar for hurting people for a long time, like,
*  I don't know, nuclear weapons or something like you just subject someone to a bunch of radioactivity
*  and that also causes cancer, right? So our ability to make weapons biological or otherwise has
*  already cleared the bar for technological capability where the capability level is not yet high enough
*  is to actually fix things. That's why I'm optimistic about the applications that this
*  technology is. Yeah, that's great perspective. All right, we'll have to go through the third
*  paper somewhat quickly. This one is full title unsupervised evolution of protein and antibody
*  complexes with a structure informed language model. So to kind of complete the trilogy here,
*  you've got the first one is all about exploring the ML architecture space. The second one
*  is about trying to get through just raw data of DNA sequences, start to get a handle on these
*  higher order concepts and at least start to make progress on this. What causes what, what interacts
*  with what? And then this third one is really about saying, okay, we've got a particular target.
*  Let's really lock in on that target. So you take a model called ESM IF1. And there are a couple
*  things about this that I didn't quite understand, but this is a model that combines both sequence
*  and structure data into its understanding of the world. And I was very interested to see that
*  it was only trained on single sequence. And yet you get it to generalize to complexes where multiple
*  different things interact. What I didn't understand is that just kind of happened? Is that like
*  emergent good luck or was that actually like hard to do? No, that was totally maybe somewhat
*  unexpected. Actually, it was a, I guess you can call it like an emergent property of the model.
*  So yeah, the way the model works is actually perfect, but there's like an ML audience.
*  Like it's an encoder decoder architecture. So, but kind of like machine translation,
*  where the encoder is a protein structural encoder actually, and there's a protein sequence decoder.
*  So it's almost like we're translating structure, like the sequence of structural coordinates
*  into a sequence of actual amino acid identities. So for each token position, we actually give the
*  model the three-dimensional coordinates of the backbone atoms of the protein, and then ask the
*  model to then predict our kind of next token prediction conditioned on the entire set of
*  backbone coordinates, what the actual amino acid identities are that fill in that backbone or that
*  are compatible with that backbone or that will fold into that backbone if the sequence is
*  actually produced. And yeah, the model is only trained on single chains. It's not even trained
*  on multi-domain protein. It's trained on very simple proteins. So actually the training data set
*  is like these small globular domains. So like a single chain of a protein can actually have smaller
*  kind of units that are globular or that form kind of more like nice compact units called domains.
*  So the model is not even really trained on large multi-domain proteins. It's mostly trained on these
*  domains of proteins, but it still generalizes to complexes. And the way we do that is actually
*  very simple. We just treat a multi-chain complex as just a huge protein, potentially where the
*  3D coordinates have large discontinuities or like large differences in coordinate space from each
*  other. But we just feed that whole complex into the model and it seems to understand which mutations
*  either stabilize the entire complex or destabilize the complex. And when you stabilize a complex,
*  typically that involves improving the binding affinity between the constituent members of that
*  complex. And when you destabilize a complex, you decrease the binding affinity between the two or
*  more constitutive components of the complex. This is very useful for say antibodies. So antibodies
*  have two chains. So an antibody has a heavy chain and a light chain. And then they often bind an
*  antigen, which is one or more chains. So that minimum three chains involved in an antibody-antigen
*  binding interaction. So we just give the model the whole set of 3D coordinates of the antibody
*  bound to the antigen and say, you know, which mutations on the antibody side will stabilize
*  that complex. And it turns out that a lot of those mutations helped improve the affinity of the
*  antibody for the antigen, which is really useful, especially for example, in clinical applications,
*  you have some antibody that kind of binds weakly that you've isolated from a patient or from some
*  initial library and you just want to make it 10x, 100x better or something. So this is the kind of
*  area of the molecular development life cycle that this model fits into.
*  Yeah, it's another striking example even I think more so than I realized of a model generalizing
*  in a pretty significant way outside of the domain that it was trained on. So let me just
*  make sure I can articulate what is happening in very literal terms. Tell me if I get anything wrong.
*  You start with a structure of an antibody bound to the thing that it's evolved to
*  target and you feed into the model the three-dimensional coordinates of the
*  backbone atoms of this protein complex. The model has only ever seen single chain proteins
*  that are folding up on themselves. You're feeding in three different chains that are interacting
*  with each other. It doesn't seem to care. Its job is to predict based on those coordinates,
*  which amino acid is at each position and it spits out a prediction and then you compare those
*  predictions to the actual ones that you had and you look for differences and you say, well,
*  jeez, if it thinks that it was this one when it was really this one, well, maybe the one that it
*  thinks would actually be better and then you can go test that. And then if I understand the sort
*  of loop correctly, it's like take the ones that have kind of the most likely, where the prediction
*  from the model is most different from what is the actual, go synthesize those, test and see which
*  ones actually do bind better, then come back to the model and start with that new one and run it
*  again and that way you can do two rounds of evolution and in the end you get like significantly,
*  depending on exactly which complex, of course, it will vary, but order of magnitude or more
*  stronger binding. I actually don't know what that means. So when it's like 25x improvement,
*  does that mean like I'd have to pull 25 times as hard to pull them apart or like they stay
*  together like 25 times more of the time? This is how naive I am, but tell me if I got the
*  setup and the loop right and then like, what does that actually mean when it's 25 times better?
*  No, the setup is, yeah, it's almost there. So we give the model just the setup. We assume that we
*  have the three-dimensional coordinates of the antibody bound to its target or I'll say antigen,
*  but that's the jargon, like the thing that the antibody is bound to and this is determined with
*  an experimental method, typically cryo electron microscopy or x-ray crystallography. We don't have
*  to go into the details, but they give you a pretty good resolution picture where the backbone
*  coordinates are. And then we also know the sequence of the antibody and the sequence of
*  the antigen. So actually in our decoder, that decoder part of the model, you actually kind of,
*  for the parts that you don't want to change, you just fix those or just score the actual
*  amino acid identities that are present in the original or in evolution, there's the wild type
*  starting sequence. And then what we do is we then just make single amino acid changes at each
*  position in the antibody and then see how does the likelihood of that entire, you know, just the log
*  crops of that model change when we make this mutation compared to the wild type or the original
*  sequence. So the idea is, you know, if the likelihood of some mutation gets really high,
*  then maybe that sequence is more compatible with that set of backbone coordinates. Whereas like,
*  you know, if the model at, you know, position 10 thinks that an alanine has like 0% likelihood
*  of appearing in this position, then maybe if you put that alanine there, it's going to completely
*  disrupt the structure, for example. So that's basically how, and then we just score all possible
*  single amino acid changes to the antibody. So it's a sequence length times number of amino acids,
*  number of changes, and then we just rank those by how much they affect the likelihood under the
*  model. So at the very top of that list are things that, you know, potentially are going to improve
*  the likelihood of that sequence under the model. Yeah, and then so the loop is in the first round
*  of evolution, we just picked the top, I think, like 20 or 30 mutations by the likelihood ratios
*  and then tested them individually. And then the second step of evolution, we just do something
*  kind of silly, or I mean, not so very simple, is just make, you know, various sets of combinations
*  of these mutations. And we can also score them by the model itself. So you just make all possible
*  combinations of the five or six mutations that actually improved affinity, or improved binding
*  in the first round. So the second step is a little bit more manual. We're not like retraining models
*  on that data and then updating the actual weights of the model or anything, but we're just kind of
*  combining, though we can use the pre-trained model again to score different combinations. And yeah,
*  by improving binding by some 100-fold or something or 100x, this is fundamentally, so the actual
*  measurement that we use for this is actually a concentration-related measurement. You can think
*  of it as like the concentration at which, in terms of like the chemical reaction in molecules A and B,
*  it's like the concentration at which there's an equal amount of A dissociated with B and A bound
*  to B. So it's kind of like an equilibrium, but fundamentally it's a concentration. So at this
*  concentration, there's an equal amount of molecule A dissociated with B and A bound to B or whatever.
*  So 25 times better means I only need one 25th as much to achieve that.
*  So it's a concentration-based readout. And this thing could potentially translate
*  downstream into like dosing, for example. So if your molecule works as well at 2x the concentration,
*  and your activity is good enough, maybe you just dose at a half of the actual molecule.
*  Yeah. Cool. Okay. We're at time. If you have time for one more, I'll give you one more. Otherwise,
*  I can thank you and send you on your way right now. I'll take one more question. Yeah. Okay. Well,
*  you pick which one you want to do. My last two, you can do one or both. One was when you're doing
*  this sort of super fitting, do you have to worry about over fitting? Because obviously the target
*  is subject to evolve and change too, right? So do you have to worry that like, now that I fit this
*  thing so tightly, if it changes a little bit, now that might throw us off again? How do you think
*  about that? Is there some sort of like many, do you do like a Monte Carlo tree search type of approach
*  to try to gain that out? That's one question. Other question is, interested in your comments
*  on the Arc Institute, it's coming up all over the place. There's like, you know, next generation,
*  like CRISPR successor recently announced out of there. And it seems to be quite a special
*  phenomenon. So you can take one or one or both of those. Yeah, I'll just answer both very briefly.
*  Yeah. In terms of like, you hit the nail on the head of like, what I am pretty interested in moving
*  forward with this kind of stuff is that in therapeutic design, we're often assuming that
*  the target is fixed, right? And that it's not changing over time. But actually in nature,
*  definitely in viral infectious disease or in bacteria or in cancer, the target is a moving
*  target. And it's actually constantly evolving and will constantly evolve around our therapies. So
*  you spend $2 billion to develop the drug and then you administer it. And then it's six months later,
*  you get like drug resistance. But I think there's a lot of room here for interesting algorithms.
*  You brought up some kind of tree search or maybe some kind of RL policy or something or basic
*  things. Going back to the original set of questions for the second point, you know, it seems like we
*  made a lot of progress in molecule design. But I think this is one area where the algorithms could
*  be pretty interesting. Actually, we made a lot of progress if you're designing against a static
*  target, what happens if it's a moving target. And then ARC is great. I'm at ARC right now. I'm
*  actually on site. It's a really great environment. They've been really supportive for my research
*  and just starting off my research career. So I've been technically a professor only for eight months
*  now. And I don't think we could have moved this fast without like the support of ARC
*  and the immense like talent density here, I think. And yeah, I mean, it's great. I think there's
*  definitely a lot of room for innovation and models for funding science and supporting and just doing
*  science. And I think the ARC model seems to be doing well so far. But we'll see in time. But so
*  far, I think it seems to be a great place. And I'm especially struck by the collegiality among the
*  people here. Like all the investigators here are very friendly, and we all collaborate and have
*  projects ongoing with all the other investigators at ARC or in some way involved in a project with
*  them. And so it seems like a great place for now. And hopefully in the far future as well. Like
*  there's no reason for me to think that it won't stay this way. But yeah, I think it's been good.
*  And ARC has been great. Cool. You guys cure cancer, you'll deserve all the fame and
*  and fortune that we'll bring. And leading indicators are definitely there that special
*  work is coming out of that place. No doubt. Yeah, it's I've been very fortunate to be in
*  this environment. So yeah, I guess I am technically sponsored and that they fund some of my science,
*  but that ad was not sponsored. Well, it's been a remarkable series of papers that you've been
*  involved with. And I really appreciate the time to walk through them with us. I am sure there will be
*  more great stuff to come from you. So we will be keeping an eye out for that. But for now, I'll say
*  Brian, he thank you for being part of the cognitive revolution. Cool. Thanks, David. It is both
*  energizing and enlightening to hear why people listen and learn what they value about the show.
*  So please don't hesitate to reach out via email at tcr at turpentine.co or you can DM me on the
*  social media platform of your choice.

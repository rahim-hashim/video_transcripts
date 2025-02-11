---
Date Generated: December 14, 2024
Transcription Model: whisper medium 20231117
Length: 6953s
Video Keywords: []
Video Views: 2578
Video Rating: None
Video Description: In this episode of The Cognitive Revolution, Nathan interviews Andrew White, Professor of Chemical Engineering at the University of Rochester and Head of Science at Future House. We explore groundbreaking AI systems for scientific discovery, including PaperQA and Aviary, and discuss how large language models are transforming research. Join us for an insightful conversation about the intersection of AI and scientific advancement with this pioneering researcher in his first-ever podcast appearance.

Check out Future House: https://www.futurehouse.org

Help shape our show by taking our quick listener survey at https://bit.ly/TurpentinePulse

SPONSORS:
Oracle Cloud Infrastructure (OCI): Oracle's next-generation cloud platform delivers blazing-fast AI and ML performance with 50% less for compute and 80% less for outbound networking compared to other cloud providers13. OCI powers industry leaders with secure infrastructure and application development capabilities. New U.S. customers can get their cloud bill cut in half by switching to OCI before December 31, 2024 at https://oracle.com/cognitive

SelectQuote: Finding the right life insurance shouldn't be another task you put off. SelectQuote compares top-rated policies to get you the best coverage at the right price. Even in our AI-driven world, protecting your family's future remains essential. Get your personalized quote at https://selectquote.com/cognitive

Shopify: Shopify is the world's leading e-commerce platform, offering a market-leading checkout system and exclusive AI apps like Quikly. Nobody does selling better than Shopify. Get a $1 per month trial at https://shopify.com/cognitive

CHAPTERS:
(00:00:00) Teaser
(00:01:13) About the Episode
(00:04:37) Andrew White's Journey
(00:10:23) GPT-4 Red Team
(00:15:33) GPT-4 & Chemistry
(00:17:54) Sponsors: Oracle Cloud Infrastructure (OCI) | SelectQuote
(00:20:19) Biology vs Physics
(00:23:14) Conceptual Dark Matter
(00:26:27) Future House Intro
(00:30:42) Semi-Autonomous AI
(00:35:39) Sponsors: Shopify
(00:37:00) Lab Automation
(00:39:46) In Silico Experiments
(00:45:22) Cost of Experiments
(00:51:30) Multi-Omic Models
(00:54:54) Scale and Grokking
(01:00:53) Future House Projects
(01:10:42) Paper QA Insights
(01:16:28) Generalizing to Other Domains
(01:17:57) Using Figures Effectively
(01:22:01) Need for Specialized Tools
(01:24:23) Paper QA Cost & Latency
(01:27:37) Aviary: Agents & Environments
(01:31:42) Black Box Gradient Estimation
(01:36:14) Open vs Closed Models
(01:37:52) Improvement with Training
(01:40:00) Runtime Choice & Q-Learning
(01:43:43) Narrow vs General AI
(01:48:22) Future Directions & Needs
(01:53:22) Future House: What's Next?
(01:55:32) Outro

SOCIAL LINKS:
Website: https://www.cognitiverevolution.ai
Twitter (Podcast): https://x.com/cogrev_podcast
Twitter (Nathan): https://x.com/labenz
LinkedIn: https://www.linkedin.com/in/nathanlabenz/
Youtube: https://www.youtube.com/@CognitiveRevolutionPodcast
Apple: https://podcasts.apple.com/de/podcast/the-cognitive-revolution-ai-builders-researchers-and/id1669813431
Spotify: https://open.spotify.com/show/6yHyok3M3BjqzR0VB5MSyk
---

# Automating Scientific Discovery, with Andrew White, Head of Science at Future House
**Cognitive Revolution:** [December 05, 2024](https://www.youtube.com/watch?v=umFbsCqG734)
*  You will never be able to reduce biology to like these cartoon diagrams. There is like
*  complexity at every single level and it always plays a role. So I think it's a domain which is
*  driven by observations and empirical measurements, rather than a domain that's driven by like some
*  sort of virtual in silico model that you can derive. I think sort of stops this, I don't know,
*  ASI or AGI hypothesis that like a model that's so intelligent could just wake up one day and know
*  how to cure cancer by just thinking through it. Sometimes it seems like we can solve the problems
*  with empirical like machine learning models. Sometimes it looks like we can solve first
*  principle methods and I don't know, the only thing that does work 100% of the time is measuring it in
*  the lab and maybe all these methods are just approximations and all they can do is increase
*  your hit rate or decrease the number of experiments you have to do in a loop in the lab. Futurehouse
*  is really Sam Rodriguez's brainchild I think. Sam came up with this idea of a future house,
*  which is basically like an FRO, like we want to be at the scale of that level, like 20 and
*  50 million dollars and like a few year time scale, but it's not like a five-year goal.
*  It's like a moonshot project that you may not accomplish in five years or maybe you will know
*  if you can accomplish it in five years and then you'll need to go get more money to do it or it'll
*  be commercializable at that time. Hello and welcome back to the Cognitive Revolution.
*  Today I am excited to share my conversation with Andrew White, Professor of Chemical Engineering
*  at the University of Rochester and now co-founder and head of science at Futurehouse, an Eric Schmidt
*  backed focused research organization that's building increasingly autonomous AI systems
*  to accelerate scientific discovery. We begin by briefly discussing Andrew's background in
*  statistical mechanics and molecular simulation, how his AI journey began during a 2019 sabbatical,
*  how he came to write a textbook on deep learning for molecules and materials, and ultimately to
*  his involvement with OpenAI's GPT-4 Red Team in 2022, which is where we had first crossed paths.
*  From there, we unpack two of Futurehouse's major recent releases, Paper QA and Aviary.
*  Paper QA is a question answering framework that works across entire bodies of scientific literature
*  using a mix of techniques including keyword expansion, full text search, contextual summarization,
*  and large language model powered relevance filtering to achieve superhuman performance
*  on question answering, contradiction detection, and Wikipedia style citation supported topic
*  summary writing. Here, Andrew emphasized Futurehouse's philosophy of optimizing for
*  results rather than efficiency. They are willing to spend whatever compute or token budget is
*  required and to wait for however many seconds are required to achieve the best possible output.
*  This quality first approach, as you'll hear, is one that I think a great many AI builders
*  should take inspiration from. Aviary, meanwhile, Futurehouse describes as a gymnasium framework
*  for training language model agents on constructive tasks. In addition to creating conceptual clarity
*  by distinguishing between agents, which contain core models and memory, and their environments,
*  which provide tools and interfaces, this project introduces an interesting representation of agent
*  systems as stochastic computation graphs and very interestingly shows how agent systems can be
*  trained end to end even when black box commercial models are used at key nodes. I found Andrew to
*  be so thoughtful in his responses and he was sufficiently generous with his time that I took
*  the opportunity to ask a bunch of related questions along the way as well. One answer that continues
*  to rattle around in my head was Andrew's argument that because better conceptual frameworks and
*  automation platforms are quickly reducing the cost of real world experimental work,
*  perhaps machine learning models ability to run experiments in silico will ultimately prove less
*  transformative than I had been expecting. There are, as you'll hear, a bunch more and this was,
*  believe it or not, Andrew's first ever podcast appearance. It took me months of friendly
*  persistence to make it happen, but I think you'll agree that his skill as a scientific communicator
*  is excellent and he really should do a lot more of these going forward. If you're finding value
*  in the show and want to help us spotlight more unassuming AI thought leaders, we'd appreciate it
*  if you'd take a moment to share this episode with friends, write a review on Apple Podcasts or Spotify,
*  or just leave us a comment on YouTube. Your feedback and suggestions, including for more
*  pioneers of AI for science, are welcome too. You can contact us via our website, cognitiverevolution.ai,
*  or feel free to DM me on your favorite social network. With that, I hope you enjoyed this deep
*  dive into frontier applications of large language models for scientific research with Andrew White
*  of Future House. Andrew White, co-founder and head of science at Future House. Welcome to
*  the Cognitive Revolution. Happy to be here. I'm really excited for this. This is one I've been
*  begging and pestering you to do for a long time and honored that this is your first ever appearance
*  on a podcast. So, lots to dig into and I think it's going to be a lot of fun. Awesome. Thanks.
*  So, we first met actually on the GPT-4 Red Team, which has been now more than two years ago.
*  And I usually don't do people's like backstories too much because so many of them are chat GPT came
*  out. I knew I was going to be a big deal, especially with like entrepreneurship space these days. But
*  being part of that GPT-4 Red Team clearly means you were on this earlier than most. And in looking
*  into your background, I see a chemical engineering background. I don't see at least on the level of
*  LinkedIn as much of an AI story. So, I'd love to hear kind of your general, what was it that
*  helped you catch the wave early when you did and how did you find yourself getting involved with
*  the GPT-4 Red Team? Yeah. So, I mean, it goes back for a while. So, my training, my PhD, my postdoc
*  is in a field called statistical mechanics. And statistical mechanics is like a branch of
*  thermodynamics, but it's basically statistics of systems with extremely high degrees of freedom.
*  So, it's usually simulations of gases, liquids, proteins, things like that, or quantum systems.
*  And so, I've been working on this for a while. And then maybe in 2019, I got invited to UCLA for
*  sabbatical. It's something called the Institute for Pure and Applied Mathematics. This is called
*  IPAM. It's like an applied math group. And they wanted to do a topic on machine learning
*  and physical sciences. So, I'm out there and I met with, you know, a lot of people were there.
*  Jan Lukun was there. I think Yoshi Bengio stopped by for a talk. There was a guy named Pat Riley,
*  who has actually just started a new company, but he was leading part of Google Accelerated Science
*  for a long time. He did a lot of their fusion research, DNA-encoded libraries. It was a really
*  great group of people. And we were all trying to figure out how these systems could be applied.
*  At the time, it was pretty classical sort of machine learning. You do feature engineering
*  and fit them. And there was one guy, what's his name? Matthias Rupp was there, who had basically
*  worked on this. Oh yeah, Anatole von Lohenfeld. Him and Matthias had built this system that was
*  already state of the art for predicting energies, small molecules. And so, people knew this kind of
*  thing was going to take off in chemistry and physics as well. I think people were really
*  excited about it. So then, I didn't really understand the field that well. I went to the
*  sabbatical and I went to a meeting in Tokyo actually on material science. Sergei Kulinin
*  was there, who's a big name in AI materials. And Lee Cronin was there, who's a big name in chemistry
*  and origin of life and machine learning now. And it was a great meeting. I got to learn a lot about
*  how these people were thinking about it. And Lee is a very controversial figure in chemistry,
*  not because of anything he's done wrong, but it's just basically he's very strong opinions.
*  And I think it was really cool to talk to him. He had some very strong opinions and Sergei did
*  as well to learn about their thinking in the field. So when I came back from all this and
*  this trip to Tokyo and the sabbatical, I ended up sitting down and writing a textbook called
*  Deep Learning for Molecules and Materials. And it was kind of like course notes slash like textbook.
*  I wanted to learn to use this new Jupyter book, which is like an executable book. So I wrote this
*  out and it's been pretty popular since then, but I started teaching the class and learning more about
*  it. And I started using language models pretty early. There was a paper by Garbin Cedars group
*  and Kristen Pearson, and they had done this work on like Word2vec and material science.
*  And that paper just blew my mind that you could basically embed the representation of a material
*  using natural language as opposed to trying to like come up with the right features.
*  And so I started working in language and chemistry. And I work with Glenn Hockey,
*  who's at NYU, and basically we were exploring, can you do things like drive VMD, which is a
*  molecular dynamics visualization engine with voice recognition. And we were using what's called
*  Codex. Was that the original OpenAI language model? Was it Codex?
*  Mad Fientist That was their code one, as I recall. They had GPT-2,
*  3, Codex was right in that timeframe.
*  Ben Fientist Yeah, I think that's right. So I think they came out with DaVinci in maybe January,
*  February, and then they came out with Codex a few months later. And so we were like driving MD
*  molecular dynamics simulations with this, which was really cool because VMD is written in this
*  obscure language called TCL. I mean, I don't know. I think it's obscure. Maybe some people
*  think it's bread and butter, but no one knew how to program a TCL. So every time we had to
*  write scripts for doing MD analysis, molecular dynamics analysis, we'd basically Google a whole
*  bunch, copy and paste code, email friends. And so to have this language model that could just write
*  the code a priori was super cool. And we wrote a position paper. Basically we wrote a two or
*  three page paper that was published in Digital Discovery, which is a pretty cutting edge journal
*  a few years ago, started by Alanis Baraguzic, who's right now just a huge towering figure in
*  AI materials. And we wrote this article about how we think the field could change with language
*  models. And I put it out on Twitter and at the time I was starting to use Twitter more and that
*  was becoming a very exciting area. And some people opening eye were trying to think about
*  chemical, biological, radiological, nuclear safety. So Seedmorn is a word that people
*  throw around a lot in AI safety, and not just AI safety. This is like a topic of terrorism and
*  conventional warfare. So they were curious about Seedmorn risk and they sort of were looking at
*  who was working on language models and chemistry. And there's a very short list of people and they
*  got my name and they got Glenn's name and they asked us to participate. And this is in August
*  2022. Yeah, August 2022. And so I started working on the red team there. And I mean, it was all like
*  nobody knew what they were doing. It was like completely new ground. Like I remember like just
*  trying random stuff and it was really exciting time. And I didn't know what I was doing really
*  with language models and chemistry until a few like really, I think groundbreaking papers came out,
*  like this Miracle paper and the React paper. I think that really changed the perspective of
*  what you could do. But originally back in August and September, like I was just like really confused
*  on how these models could be useful in chemistry, but it was still like pretty cool to try a bunch
*  of random ideas. And so that's how I kind of got into it and have to go more in this story.
*  But that's sort of how I got to the red team point. This is a little bit of a sidebar from
*  our main topic, but I kind of came away from that red team experience, I would say,
*  kind of alarmed. I was like, man, the pace at which these systems are getting better
*  is really incredible. And I think now looking back, I sort of infer that GPT-4 was more of a
*  like maximalist moonshot attempt than I maybe understood it to be at the time.
*  But nevertheless, the leap from three and even the Instruct series, all that stuff to four was just
*  so eye opening. And then I was like, but the control measures are not keeping up,
*  or at least they did not seem to be keeping up at the time of that thing. And so I got a little
*  freaked out there. Did you handle it with more equanimity than I did? Or were you also a little
*  freaked out? I think I got a little bit spooked at first because it was the first time you
*  could really see coherent, responsive answers. So I remember trying things like, you know,
*  let's make nerve gas, like here's step one, here's step two. And I would ask it, how do you
*  synthesize these things? And it looked really convincing at first. And it was like, really like,
*  oh my gosh, like, this is going to change, like how we think about deploying models. But then I
*  started drawing up the chemical structures and like looking to trace the atoms and how they move
*  from step to step. And I realized that it was all like hallucinated, that it actually had no
*  conception of how to move atoms between molecules. And so it was like a strange sort of thing where
*  at first I thought that it was really technically brilliant. And then I realized it was actually
*  like really good at bullshitting, I guess. And it's a strange thing because you like don't know if
*  it's good or if it's bad. And the reasoning that it gives is actually quite plausible. And so for
*  the first like one month, I was like, wow, this is crazy. And then for the next two months, like
*  maybe October and then early November, I was like, there's nothing to this. Like it's just,
*  it's going to be really cool. It's a nice incremental improvement. But then I started
*  hooking up tools to the system. So I think in like late November, early December, I was starting
*  to use some of the ideas that were like Blankchain was showing this stuff. I think it was around like
*  chat GPT API was released. And so people were showing that you could like sort of do these sort
*  of react calls. And maybe that wasn't no, I don't know if chat GPT was available at that. But like
*  people were still doing with DaVinci at the time. And then I started hooking up to tools. And again,
*  after that happened, I was like, oh my gosh, actually, this is maybe a big deal. And so that
*  led to ChemCrow eventually. But I think, yeah, near the beginning of December, what was surprising to
*  me is like, A, the mitigations that they were trying to build had no influence whatsoever. Once
*  you started doing tool calling. And then B was that you could really make a lot of good progress
*  if you sort of put the model on these rails of only using tools, as opposed to just sort of free
*  form doing chemistry by editing the molecule. It's funny you talk about the hallucination
*  in chemistry in particular, I did an experiment with it, asking it to be my chemistry tutor.
*  And I just kept getting this stoichiometry wrong. And it could not be when I got confused,
*  that it would get confused. And then we were just off on a mess of confusion together. And I often
*  think back on that in particular, as a good indicator of how much progress there has been
*  since then, even though we haven't yet seen the next 100x compute scale up. It's like these days,
*  it makes a pretty passable chemistry tutor. And they've really ironed out a lot of those
*  behavioral weaknesses to get it to actually do useful stuff in just a lot more scenarios.
*  **Jade Lenz-Zimmermann** Yeah, I think what's surprising about these models is that they learn
*  the fundamentals actually quite well. If you ask it to reason through what the rules are for this
*  chemical reaction, or if you ask it to reason about this molecule's properties, that actually
*  is quite good in general. What's strange is it misses things like counting the electrons,
*  and it misses things like counting the atoms and stoichiometry. And it's like really,
*  I think everyone is adapting to this thing, is that it learns backwards from how you would expect
*  when having machines learn to do stem problems, is that it seems to struggle with some of the more
*  robotic steps, and it seems to do quite well with some of the more free-form steps. And so it's one
*  of those situations where you're going to see, I think, a grokking effect. Once it can count
*  the atoms, and once it can count the electrons really well, then you're going to see a big unlock
*  because it's not going to need any more additional reasoning things. So that's why I'm pretty
*  optimistic about things like O1 and some of the more rumored models that are coming up after that.
*  I think they could actually unlock chemistry to a point where you don't need to be on rails
*  with these tools moving the molecules around.
*  How would you describe O1? Because you're still involved in the pre-deployment testing with OpenAI,
*  right? So I imagine you did another deep dive on, can this thing give an accurate nerve gas
*  synthesis plan and whatnot?
*  Yeah. I would say that, so I was on the O1 technical report, and yeah, this time around,
*  I think things have gotten a lot more systematic. So people have a much better idea of where the
*  benchmarks are. Still, for me, we decided to do some more exploratory stuff during the red teaming.
*  So of course, there's already benchmarks now. So I don't think we need to be running the
*  benchmarks. I mean, we put out LabBench from Future House, which is a benchmark of biological
*  and laboratory protocols. And that was tested in O1. And so we were trying some really, I think,
*  more crazy ideas in the red teaming. And this time around, we got pretty far, but it still got
*  hung up on just some key steps. And so it's a very strange experience because we, I think,
*  had some pretty wild ideas, and the models got really close to completing them, but it gets stuck
*  on basically one step in the process. And one thing that we didn't really get a chance to try
*  this time around is consensus. So if you look at these evals, like if you run K equals 32,
*  like you run 32 times and take majority vote, that can actually sort of get over these little
*  missteps. So I think, like as the model that's available today, I don't think we're getting to
*  that point, but I think we're very close. So I think the sort of next release is actually going
*  to sort of allow us to do this synthesis planning, protocol planning. And I think OpenAI like address
*  this a little bit. Their report, they showed that laboratory, it's called, I think, Protocol QA,
*  which was from Futurehouse, O1 exceeds human levels and Protocol QA is like a model assessment
*  of laboratory plans in the domain of biology. And so O1 is basically above human level there.
*  So I think that sort of shows you that it's getting to this ability to long-term plan and
*  not make these kind of trivial mistakes that get it caught up. But I think in chemistry specifically,
*  still not there. Biology, I think it's actually getting very close, which is strange because
*  usually biological sequences are very long and so like they don't fit in the context window.
*  But a lot of the sort of ancillary things about biology, like how do you do cloning? Like what
*  are the steps to get to this process? Those things I think are very close. Hey, we'll continue our
*  interview in a moment after a word from our sponsors. Even if you think it's a bit overhyped,
*  AI is suddenly everywhere from self-driving cars to molecular medicine to business efficiency.
*  If it's not in your industry yet, it's coming and fast. But AI needs a lot of speed and computing
*  power. So how do you compete without costs spiraling out of control? Time to upgrade to
*  the next generation of the cloud, Oracle Cloud Infrastructure or OCI. OCI is a blazing fast and
*  secure platform for your infrastructure, database, application development, plus all your AI and
*  machine learning workloads. OCI costs 50% less for compute and 80% less for networking. So
*  you're saving a pile of money. Thousands of businesses have already upgraded to OCI,
*  including MGM resorts, specialized bikes and fireworks AI. Right now, Oracle is offering to
*  cut your current cloud bill in half if you move to OCI for new US customers with minimum financial
*  commitment. Offer ends 12-31-24. So see if your company qualifies for this special offer at
*  oracle.com slash cognitive. That's oracle.com slash cognitive.
*  There are so many things in life we just never get around to. Taking up that hobby, cleaning out
*  the garage, you know, little things that don't really make huge differences in our lives. Yet
*  there's one thing that most of us have probably been neglecting that can have a huge impact on
*  our family's future. It's life insurance. And with select quote, getting covered with the right
*  policy for you is easier and more affordable than you might think. As someone who tracks AI progress
*  on a full-time basis and obsesses about its potential impact nonstop, I know how tempting it
*  can be to ignore more mundane, familiar risks. There's always another paper to read, podcast to
*  listen to, or product to try. And yet the smartest people that I know in the AI space continue to
*  save and invest money for the future, carve out time for their relationships, maintain their
*  physical and mental health, and yes, protect their family with life insurance, just in case anything
*  should happen before the singularity. If nothing else, it's one less thing to worry about in a time
*  of unprecedented change. So get the right life insurance for you, for less, at select quote dot
*  com slash cognitive. Go to select quote dot com slash cognitive today to get started. That's select
*  quote dot com slash cognitive. Does that reflect a sort of structure of biology? I'm kind of thinking
*  of Dario's essay recently on what drives, I mean, of course, it's on the big picture of AI.
*  Maybe we'll get to that in the big picture in a second. But his account of what drives
*  progress in biology and medicine is basically that there's a small number of platform technologies
*  that you sort of understand at the conceptual level and use on your problem versus, I was actually a
*  chemistry undergrad myself. In my experience of chemistry was like, there's a ton of different
*  things and a ton of different reactions and like few sort of platform measurement technologies,
*  yes, but in terms of like action steps, like not so many platform technologies, I guess is how I
*  would describe it. Yeah, I think I mean, Future House was built to be like a moonshot on automating
*  science. And we picked biology for a couple reasons, same similar what Dario talked about.
*  One of the reasons is that yeah, it's a lot more platform based. So there's like, let's say you
*  want to design proteins, there is a standard way to make a protein, like you can use cloning,
*  or you can do cell free protein synthesis, or you can make it on a machine. But basically,
*  there's no stop to be like, oh, can we make this protein? Whereas you go to chemistry,
*  every single molecule is very bespoke to make it. And there's a lot of questions about, can you make
*  it at scale? And it's not like a trivial step. So I think in some ways, biology is great, because
*  it is kind of like a platform like sequencing is almost free. And synthesis is quite cheap,
*  you can basically make 100 amino acid protein, you can order the gene to make that for like $25.
*  So I think biology is very interesting topic, because a it's pretty like clear how to test
*  hypotheses. And it's pretty cheap to test hypotheses. And B, I think what's unique about
*  biology is that there is like no limit to intellectual tasks. Basically, there's always
*  going to be another organism genome to explore and annotate all the functions, there's always
*  going to be some new protein that does something unusual, there's always going to more like dark
*  made a genomic data where we don't know what this genetic material is. So in the sense, like it's
*  actually sort of an unlimited amount of complexity to explore, or whatever method you want to use.
*  Whereas if you go to something like physics, like in physics, I mean, there are like, I think,
*  a lot of interesting topics in physics, but in some sense, it's pretty expensive to get data
*  in physics. And it's also like, there's not a ton of complexity to like elucidate, like a lot of
*  time, it's a very reductionist thing in physics, you're trying to like reduce it down to some
*  equations or some relationships. Whereas in biology, there's just so many things to annotate,
*  there is no like, in biology, we kind of know the universal law of biology already. I mean,
*  it's like evolution. And you go to physics, and it's like trying to find the law. And so what's
*  cool about biology is that you kind of already know the reductions point of view, and you're
*  trying to like look at the more complex systems and understand how they work and how they fit
*  together. So I think it's a very cool topic for those two reasons.
*  That's really interesting comment that you already know the reductionist point of view.
*  How likely do you think it is that there are like major aspects of the full biological paradigm that
*  we just have very little grasp on right now? I'm thinking, for example, if Michael Levin,
*  who's been a past guest and has this idea that electro physiological or electro bio signals
*  at sort of tissue levels are an interface that probably will be programmable, he's basically on
*  a quest to kind of turn that into another one of these platform technologies. And yet he seems to
*  be of course, there are other people in that general space. But like, relative to the rest
*  of biology, it seems like it's quite a niche. So I wonder how many of those other things you think
*  like what the sort of dark conceptual matter might still be out there? Yeah, yeah, we were talking to
*  Ed Boyden about like optogenetics. When you say like, how do people discover how I think his lab
*  is one of the pioneers there? How did you guys come up with this stuff? Basically said that we
*  made like what he calls a tiling tree is basically you know, he wrote them the goal that he wanted.
*  And he wrote down like all the ways that they could try to attack it. And then they like sort of cut up
*  space of ideas by like, okay, we could deliver something to the brain, or we could deliver a
*  signal to the brain or we could deliver, you know, via surgery, something physical to the brain.
*  And it's like, okay, what kind of ways can we send information to tissue, right? Like we could try
*  magnetic waves, we could try radio waves, we could try light that penetrates tissue, right. And so you
*  sort of like go down these paths. And it's Yeah, I think it's a field where I don't think we're going
*  to run out of ideas ever. Like there's always interesting topics to explore. I think that's
*  sort of the thing about biology is that you just have all these very complex systems with all these
*  different interactions. And it's a very dense, like, topic, like I think had an argument with
*  somebody about like, how do you ever get to the bottom of like, knowing a protein, right?
*  People would say, well, once you have the crystal structure, you know, then it's like, okay, well,
*  no, you need the statistical ensemble of the protein, right. And then it's like, okay,
*  what about post translational modification? Okay, like, what about things like the reactions in the
*  protein, right? There can be these methylation, or there can be like these, whatever, there can be
*  these chemical modifications to a protein. And then there can be things like, okay, what if it
*  has like a water wire that sends protons to the active site, right, you got to model that because
*  the diffusivity of a proton by a water wire is different than the diffusivity of a proton by
*  like hopping on like a hydronium ion. And it's basically just like, you will never be able to
*  reduce biology to like, you know, like these cartoon diagrams, there is like complexity at
*  every single level, and it always plays a role. So I think it's a domain which is driven by
*  observations and empirical measurements, rather than a domain that's driven by like some sort of
*  virtual in silico model that you can derive. And so I think it's, it's going to be a domain, which
*  is I think sort of stops this, I don't know, ASI or AGI hypothesis that like a model that's so
*  intelligent, could just wake up one day and know how to cure cancer by just thinking through it.
*  It's really like a domain where you have to get out and you have to measure things
*  repeatedly and get into this loop and being super intelligent may not actually scale as much as just
*  having a lot of good hypotheses that you can do. Anyway, so I don't know if that's the question,
*  but yeah, okay, there's a couple of provocative ideas there that I want to come back to. But
*  you've mentioned Future House a couple of times and a couple of the projects that you guys have
*  put out. Let's just make sure we set the stage appropriately with what is Future House? How did
*  you get hooked up with Eric Schmidt, who I understand is one of, if not your principal
*  backer? And what's kind of the big audacious goal that you guys are chasing?
*  Yeah. So yeah, how do we start Future House? So I think to be honest, Future House is really Sam
*  Rodriguez's brainchild, I think. So Sam, who's the CEO, and him and I are the co-founders of Future
*  House. Sam had this vision of like alternative mechanisms to do science. So Sam is the first one
*  to sort of write down this idea of focused research organizations. And then he worked with Tom
*  Kalil and Adam Marblestone and they started Convergent Research, which basically has been
*  launching these focused research organizations. And these are like five year nonprofits that are
*  funded at like between 20 and $50 million that are built to just answer one very specific question
*  that is not being funded in academia because it's like too big of a question, but not being funded
*  in industry because it's like not a commercializable question. So like one example is making new model
*  organisms or like understanding building the connectome for the brain or building technology
*  to do the connectome for the brain. There's another one that's like doing lean, like trying to build
*  all of the documentation and scaffolding for lean so that it can take off as like the, you know,
*  the programming language of mathematics. But Sam sort of kept thinking down this path and he came
*  up with this idea of a Future House, which is basically like an FRO, like we want to be at the
*  scale of that level, like, you know, between 20 and $50 million and like a few year time scale,
*  but where it doesn't, it's not like a five year goal. It's like a moonshot project that you may
*  not accomplish in five years, or maybe you will know if you can accomplish it in five years and
*  then you'll need to go get more money to do it or it'll be commercializable at that time.
*  And so that's what Sam was sort of thinking about. I happened to be at this time, like we know we had
*  finished ChemCrow, we had explored what can be possible with LLMs, we were exploring more stuff
*  with combining like RAG and tool calling and language models put together. And so I told Sam,
*  like, why don't you guys build it around AI, like automating science, right? So Sam had been
*  exploring ideas of like new microscopy technologies, like new ideas and sequencing or new understanding
*  the brain. But I said, we should, you should focus on automating science. And so Sam and I
*  sort of brought, you know, he brought, I think that the model and I sort of brought like what
*  could be the topic. And we pitched it to Eric, and he was very excited about the idea and he liked
*  the topic. And Eric has the last few years has been really excited about AI. So I think it really fit
*  to his thinking of what's the future holds. And so then we basically put together this organization
*  from scratch. And I mean, there's been organizations like us, like ARC is one example or Altos or
*  Arcadia, these are all sort of non-traditional research organizations. I think the real
*  difference between them and us is that we are focused, we are mission focused. Whereas I think
*  Arc is maybe more of like traditional sort of PIs with their own ideas. We are focused on one mission.
*  And one of the cool things about having a mission is that you can be a nonprofit. If you are a
*  nonprofit and you don't have a mission, it gets very confusing about what you're trying to do.
*  Like how do you make decisions about what to buy, what personnel to hire, right? Because if you're
*  not trying to make a profit, it's really clear what you're trying to, unclear what you're trying to
*  optimize for. We have a very clear mission and it's an impossible audacious mission. And so it's,
*  we're never going to run out of things to do on this mission and it helps us sort of guide the
*  direction. So anyway, that's kind of like how the idea got started. There's been lots of things we've
*  done along the way, but we've sort of been around this nucleus of trying to automate science. And
*  yeah, and then Eric has been the primary backer, but we've raised funding from other sources.
*  We've got grants from organizations. And so I think we're trying to go bigger on the next year
*  or so in the scale of what we're trying to do. Cool. So I'll just read your mission statement.
*  I copied it right off the website. Our 10 year mission is to build semi-autonomous AIs that can
*  scale scientific research to accelerate the pace of discovery and to provide world-class access to
*  cutting edge scientific, medical, and engineering expertise. So that is pretty similar to what I
*  hear when I read Dario's Machines of Love and Grace vision. The semi-autonomous is definitely
*  an interesting call out there. In his vision, it seems like they're sort of on a 10 year time scale
*  likely to become fully autonomous. He sort of envisions them being like the PIs and the humans
*  and maybe some other AIs are more like the helpers. So in what way do you envision even in the
*  long-term of AI, these things being not fully autonomous? Yeah, I guess there's two sort of
*  wrinkles here. I think one wrinkle is that I'm actually pretty bearish on laboratory robotics.
*  We may get there, but I think that there's been so many companies and biotech especially,
*  and I think in AI that just tried to swallow the mission of automating the physical world and just
*  died because of it. I don't want to say Emerald Club Labs or Ginkgo Bioworks have died. They've
*  made great progress and done great things, but this commitment to automation, I think, is a huge
*  challenge. So we can only solve so many grand challenges at Futurehouse. So we decided that
*  we're not trying to automate the lab. So I think one difference between a fully autonomous AI system
*  that can do science is that it's going to have its own lab, it's going to have its own robots,
*  it can do all the protocols, things there. We're not trying to solve that part of the scientific
*  equation. If somebody solves laboratory robotics tomorrow, great. We'll happily buy some signup
*  partnership, whatever, but we're not trying to automate inside the lab. We do use standard lab
*  automation. We have robot arms, we have liquid handlers, we have acoustic liquid handlers.
*  We do all the sort of regular automation you'd see, but we don't have it as part of a mission
*  because we don't want to get stuck on that sort of an aspect. Then another thing I think that
*  differentiates us is I don't think we're going to have a system in 10 years where we can just say
*  explore the made-a-genome and then we come back in a year and it will have annotated everything
*  interesting and all of the genetic information on the planet. I think it's going to be more likely
*  that we have a disease, a patient population, and we're like, what could be the biological mechanism
*  for this disease? Okay, here's the biological mechanisms. Which one of these could we target
*  with the biologic? Which can we talk about some molecule? What's a good starting point?
*  So I think it's going to be semi-autonomous in the sense that we're going to have a very clear
*  quest and a very clear set of parameters and we're going to more iterate with the system.
*  Next, it gets back to this idea of biology is really an observational or empirical data limited
*  field is that it's very unlikely we'll have some... You might have something in mathematics where you
*  can just send it off to do math and you'll just be getting theorems or proofs. I don't know,
*  once a quarter you get a dump of some. I think that's feasible in something like math where
*  there is no empirical limitation. I think in biology, you're not going to just take some
*  system that's going to say, do these 36 mouse measurements. You're not going to go order a mouse
*  from a CRO and go do the experiment that way. It's always got to be done hand in hand with humans.
*  – Just as a brief aside on these companies like Emerald Cloud Lab and Ginkgo Bioworks that you
*  mentioned that are doing this lab automation, my understanding right now is that they have
*  not exactly human in the loop, but human fulfilling some of the tasks. They present to you a
*  programmable interface, but behind the scenes, there's a mix of robots and people running certain
*  parts that are just... – Who told you that? That's supposed to be a secret.
*  – I don't know. I think somebody might have said it on the podcast. I don't want to get into
*  any trouble, but I think the secret is at least somewhat out.
*  – I don't know. I guess this is the thing is that some people call them biorobots or wet robots,
*  which is like when you have a human do the tasks that are really hard to automate and there's no
*  reason to because it takes the human whatever two minutes. I'm not really a purist in this sense. I
*  don't actually care or know when something is no human allowed. I think there's a term for lights
*  out automation. If you turn off all the lights in the building, is it still working? If so, then
*  humans aren't in the loop. You're right that Ginkgo and Emerald Cloud Labs, they'll automate
*  whatever. They'll get to 98% and that's as far as you want to go to get to the scale you want.
*  I think there's other, what is it called? Medra, I think is a company that's trying to build
*  human gripper style lab arms that move around the lab. Rather than having to build these
*  bespoke instruments like that ECL and Ginkgo Bioworks build, it's like you go to a regular
*  lab and you just put a bunch of robot arms and they move this stuff around. I think that's
*  another path which can get there, but yeah, you're right. They are not 100% automated yet
*  and it's unlikely that they will be 100% automated for a long time because just getting
*  that last sort of step is just a bunch of work for very little gain as far as throughput goes.
*  Hey, we'll continue our interview in a moment after our word from our sponsors.
*  The Cognitive Revolution is brought to you by Shopify. I've known Shopify as the world's
*  leading e-commerce platform for years, but it was only recently when I started a project with my
*  friends at Quikly that I realized just how dominant Shopify really is. Quikly is an urgency
*  marketing platform that's been running innovative time-limited marketing activations for major
*  brands for years. Now we're working together to build an AI layer which will use generative AI
*  to scale their service to long-tail e-commerce businesses. And since Shopify has the largest
*  market share, the most robust APIs, and the most thriving application ecosystem, we are building
*  exclusively for the Shopify platform. So if you're building an e-commerce business, upgrade to
*  Shopify and you'll enjoy not only their market-leading checkout system, but also an
*  increasingly robust library of cutting-edge AI apps like Quikly, many of which will be exclusive
*  to Shopify on launch. Cognitive Revolution listeners can sign up for a $1 per month trial
*  period at Shopify.com slash Cognitive, where Cognitive is all lowercase. Nobody does selling
*  better than Shopify, so visit Shopify.com slash Cognitive to upgrade your selling today.
*  That's Shopify.com slash Cognitive.
*  These are the human jobs of the future. Our comparative advantage is in manipulating
*  some annoying thing in a huge value chain that we don't understand. But take just Chinese room
*  style instructions of walk this thing over to this machine, make sure the gunk at the bottom is
*  tapped out. It could be quite a funny vision. So, okay, that was one quick follow-up. The other one
*  in terms of just a kind of clarifying follow-up was I get the distinction between like go off
*  and analyze biology versus we have one quest at the level of like it can't just be purely
*  internal thought. Like you can't own one your way into knowing what actually happens in a biological
*  system. I get that. Is there another distinction there that you're trying to draw? Because you
*  could still say go off and explore biology and come back if it had tools, right? Or you had the
*  ability to make these like Emerald Cloud Lab API calls. Yeah. I mean, you're right. You can imagine
*  a world in which you have like, I don't know, like science dojo or something where you have a bunch
*  of tools in it and one of the tools is go around laboratory experiment. And maybe when you call
*  that tool, it's dispatched to a person who's got to go figure out how to measure that, right?
*  And so you can get to the point where you're really trying to automate the scientific method
*  there. And yeah, that's a great idea. I'm hoping we'll have more to share on that topic soon. But
*  yeah, I think you're right. Like this is a completely valid path. I think whether that's
*  semi-autonomous or autonomous, I think is like a minor point of contention. But I think that it
*  may be possible that is something where you can just have very good tools and you can slot in a
*  machine in there and it can do well. One thing I always think about though is that, you know,
*  we've been building these interfaces for these LLMs where you basically, you have, I don't know,
*  like a big part of drug discovery wrapped up in a set of tools. You have a bunch of literature
*  research wrapped up in a set of tools and you make everything on Rails for these language models and
*  you put them in, like you put O1 in there and say, okay, now use these tools to discover something
*  new. I always wonder what if you put like a PhD student in there or like a gig worker that is on
*  Mechanical Turk, like how good would humans do in this setting? Because it's like something we've
*  never really tried before. Like nobody's ever tried to make like a unified API for doing science
*  and then put a human in the loop there. So I think we still have to see how good humans are
*  at this task. I think it's a very interesting new setting where like you actually have reduced
*  accomplishing science to a set of whatever 25 tools that can be called programmatically.
*  What if you put a person on the other end of it rather than a language model? Maybe this is like
*  the way of doing science or maybe humans are bad at it and then the models will be bad at it and
*  it's just like not a way of doing science. So anyway, I don't know. I think you're right.
*  That is a thing to explore. We are trying to explore that. Yeah, that's quite interesting.
*  I guess maybe before going into more depth on your specific projects and we do have plenty of time
*  and definitely want to get into those in technical detail because our audience loves the nitty gritty
*  stuff. One of the things that you had said that caught my ear and I wanted to make sure I understood
*  was something to the effect of for biology, you can't just run it in silico
*  experiments and go from there to real understanding. My working mental model of how this stuff is going
*  to work with ever better alpha folds in ESM 3 and 4 and I want to ask you actually which of those
*  things you're most excited about and what you see as the most important trends there. But
*  my working model has been you do the sort of experiment in silico and you measure the value
*  of that by how often it is in fact predictive. Of course, you still have to go do the wet work
*  to do the validation but at some point you might be 10 or 100 times higher hit rate than we used
*  to be because we can do these sort of, yes, this seems close, you must need like a classifier on
*  top. Is it worth actually going and doing the real world experiment to validate? And it seems
*  like there's potentially orders of magnitude improvement there in terms of just like how
*  much value we can get out of say existing throughput capacity, existing capacity for
*  these sort of real world experiments. Is that your mental model too or do you see it very differently
*  than that? Yeah, this is something I haven't really figured out for myself yet. Let me tell
*  you about a few things in this domain that I think people miss. For example, right now you can do
*  like very accurate free energy calculations to see if a small molecule will bind to a protein
*  and the cloud compute cost for that is like maybe $10 or $15. And the cost of making organic
*  molecules and testing them against proteins has also come down. And so the cost of like the
*  equivalent experiment is like maybe $20 or something. You could probably get it down to like $5,
*  depends on the protein and what your catalog of molecules is. So right now you have this point
*  where like actually both the cost of the chemistry and the biology is decreased at the same rate as
*  the cost of the sort of calculations. Now you can probably you would bet long term on Moore's law
*  or on better machine learning models and that might be true. So we may be getting near to a
*  crossover point where we really do start replacing a big part of it with these in silico models.
*  But if we get out, like if we zoom out a little bit, so like that's an example of like small
*  molecule binding affinity, I think it's at the point where like they're close and they've both
*  been dropping costs. We zoom out a little bit, like there's this idea like maybe 15 or 20 years
*  ago that we could solve protein folding in a lot of biology by doing molecular dynamics.
*  And there was this great sort of effort led by D.E. Shaw research where they basically put together
*  like some of the smartest people, hardware engineers, like programmers, chemists, biologists,
*  they put them all together in like a time square actually on top of a very nice building.
*  And they tried to go down this path of like building the chips and the data center from
*  like the atom all the way up to the macro scale to simulate proteins as fast as possible.
*  And they simulated protein folding, you know, they were going like milliseconds of protein
*  simulation time. And you can make these charts of basically, okay, like by 2030, we can simulate
*  organelles, by like 2050, we can simulate whole cells. And then so by 2050, we can just simulate
*  one atom per week, we can simulate the whole cell division cycle in an afternoon. And then we can
*  basically run these in virtual cell models. The only problem is molecular dynamics doesn't do
*  chemical reactions. And it turns out that like a lot of biology is acid based chemistry. A lot
*  of biology is like actual like ATP, ADP, right? And ADH plus, right? So you can't just model a cell
*  by showing where all the atoms are and how they're moving. You actually have to model the chemical
*  reactions. And so then people have built these like reactive force fields, including machine
*  learning reactive force fields. Like maybe we can model empirically how these things work, not from
*  first principles, but from empirical. And then you find out that like actually the way that a proton
*  moves through water is a quantum effect. Like you can't model that with just classical or machine
*  learning. You have to actually have these like electron density calculations. And you actually
*  have to make this like Born-Oppenheimer approximation to model the system. And that's
*  actually important. Like biology works differently if you don't have this effect. And so you
*  run to this like never, you never reach the floor of complexity when you try to model these systems.
*  And it's like a really hard thing for me to figure out what the answer is to your question
*  is that like, yes, alpha fold has solved a lot of these things, but there's a big part of proteins
*  that are intrinsically disordered. And yes, you can capture them maybe another 80% of those things
*  with like calvados, this force field from Creston-Linderville-Larsen or Martini, right?
*  There's these things that can try to model coarse-grained proteins, maybe capture another 80%.
*  But then there's some fraction of those that are not really valuable because whatever,
*  you can't just use these coarse-grained models. So I don't know, there's like a lot of things
*  that I've talked about here. But the point is that sometimes it seems like we can solve the problems
*  with empirical like machine learning models. Sometimes it looks like we can solve first
*  principle methods. And I don't know, the only thing that does work 100% of the time is measuring it
*  in the lab. And maybe all these methods are just approximations. And all they can do is increase
*  your hit rate or decrease the number of experiments you have to do in a loop in the lab.
*  So anyway, that's like a long, windy way of answering questions that I don't know.
*  Soterios Johnson Yeah, that's really very interesting. When you speak about the price of
*  the actual experiments coming down, are there caveats there around like, you said, for example,
*  like depends what your molecule catalog looks like? Like, what if I am trying to hypothesize a new
*  smallish molecule that doesn't exist in nature, maybe never before synthesized? And I'm like,
*  I'm looking for something that can do this thing. I'll generate a huge number of hypothetical
*  candidates and then run that through a model. I can't synthesize those cheaply, right? Still today?
*  Chris Swenor Yeah, I think this is like still an open question of what's the right approach. But
*  there are these things called virtual catalogs that have reached, I think, I don't know, 80
*  billion molecules. So there's like 80 billion molecules that people are pretty sure they can
*  make. And so what you can do is you can actually just work with those instead of a generative model
*  and just basically screen these 80 billion molecules. I mean, I don't know what the
*  numbers right now. It's like somewhere between 50 and 100. There's something called zinc, you can
*  look it up. Zinc is like a database of hypothetical molecules, and it's in dozens of billions,
*  probably. To be honest, like these things are made in a combinatorial like rule set. Like, these are
*  all the things you can buy cheaply from petroleum side products. These are all the reactions that
*  we know. And these are the ways you can combine them all. So you have this like combinatorial
*  explosion of molecules. So at this point, there's pretty much unlimited number of molecules that you
*  can order in a catalog. One caveat here is that all these molecules come with like a 80% success
*  rate guarantee. That is, you can order it and 20% of the time they'll fail to fill your order,
*  which is fine. You can work around it. But then there is like a lot of groups that have basically
*  built very good models for just making an arbitrary molecule. Like Philippe Foller's group
*  developed these like molecule transformers, which are basically can predict the outcome of a
*  reaction. And then you can combine that with some search method and basically predict how to
*  synthesize arbitrary molecules. There are commercial products that can do this. IBM has one, this
*  company called Postera that has one. And so basically frees people who design molecules from
*  having to think too hard about synthesis. So I think in some sense, like the synthesis has been
*  solved. But when you're late in a drug discovery program, like usually you're centered around some
*  lead and then things get more expensive. You want to like modify it. And thanks to like
*  internationalization, you can hire a chemist in China or India. And maybe the cost of one of these
*  chemists is like $100,000 a year salary. And that includes the lab and all the reagents and things
*  like that. So you can, and they can maybe make 20 molecules a week. So it's still, you know,
*  it's not free, but it's reached the point where it's not too expensive. And so I think we do have
*  a lot more freedom now in the chemistry we can design. But on the other hand, like the kind of
*  targets that people are trying to hit the kind of molecules people are trying to make have also
*  grown in complexity with these new categories of drugs like pro tax, molecular graders,
*  less induced proximity work, where you're making these big fat molecules that have to accomplish
*  like two or three tasks in the body. And so you're back at the same point you were like maybe 30 years
*  ago, where you have a whole bunch of complexity, you're trying to pack into a small molecule.
*  And so even though in theory, we can make lots of molecules, you're trying to do so much and a
*  limited amount of atoms that you're back to where you are, and you need to be very careful
*  and clever. And you have only so many experiments. So anyway, I don't know, I actually don't remember
*  the question. But I just talked a whole lot. Yeah, well, I think you answered it. It was just around
*  my experience back as a chemistry undergrad was like, small molecules were a PhD in many cases to
*  synthesize. And there was not a in general, some were easy, but many were hard. And there was not
*  there was not like an 80% success rate on just picking one out of space of 100 billion.
*  Yeah, I do want to say that I think that is like a reflective of a certain shift in mindset. So I
*  think historically, maybe when you did your undergrad, like a lot of people would start with
*  a natural product. So this is kind of the older idea of drug discovery, like phenotypical drug
*  discovery, where you like grind up a bunch of dirt or frog goo or something. It's always the
*  Amazon frog. Yeah, exactly. And you put that on a cell and you see, oh, okay, does this like,
*  was this cure cancer in my like model? And then what you do is you go, okay, it cures cancer
*  in my model, then we got to like, find out what's in the frog goo. And then you like run through the
*  mass spec and you run through the MR and look, okay, now I know what the compounds in now I need
*  to start making these things and test them. And this leads to like this natural product organic
*  chemistry, where you're trying to make pretty complicated molecules, because they're not made
*  from like room temperature, chemical reactions are made from enzymes in some biological system.
*  So those definitely not an 80% success rate. But I think in a lot of the drug discovery
*  community moved on from natural products, like rather than starting with these natural products,
*  which are very complicated, but often active molecules, they start with I would say more
*  like petroleum derived compounds. So these are things which are just part of like the global,
*  you know, supply of chemistry, which is a lot of it is driven from like oil. And so
*  because of that, the molecules that you see in drug discovery today are very different than what
*  you would see like maybe 30, 40 years ago when they came from natural products. So the chemistry
*  is usually easier because by default, from the bias of where we get them, they're coming from
*  easier reactions like a lot of a lot of a mean chemistry, a lot of simple basic building blocks,
*  like maybe 75 basic chemical reactions that are done in that camp now. So the compounds look
*  different. And some people argue that we've lost something by doing that there's actually some nice
*  effort lately, some called coconut where people try to put as many natural products together as
*  possible and try to get people to train their generative chemistry models on those instead of
*  the more petroleum derived catalogs. And or there's companies like Octant Bio that are doing
*  phenotypic drug discovery with these petroleum derived ones. Whereas most people like, okay,
*  I know I want to hit this protein, I'm going to hit it with these small molecules, design the
*  molecule to fit the protein. Suri's company, Octant, they're like, okay, I want to fix this cell.
*  And so they're working the cell model, which is close to what people used to do with natural
*  products. So anyway, there's like lots of ideas in the field. And so that's why you see, I think,
*  a change in the chemistry where it's become routine because we sort of made this decision to double
*  down on structure based drug discovery with petroleum derived compounds. Yeah, fascinating.
*  Okay, that's a really good update for me. I haven't stayed super close to the latest in
*  chemistry. And that's a good chapter for me to add to my understanding. One other just kind of
*  conceptual question, you've got great answers to these, is what do you think about the like
*  multi-omic model approach? You know, there's EVO for me earlier, I think it was earlier this year,
*  was a real seemingly like blockbuster moment where I was like, okay, it's going to happen.
*  And by it, I mean sort of that the models will learn higher order representations of the space.
*  And that's happened in language, but we've got like lots of weird debates around, well, they
*  learned all that stuff from us, so it doesn't really count or whatever. But in the biological
*  realm, it's like, there's probably ample stuff there that we don't know that if these models
*  can figure out how to represent in an effective way, which EVO seems to be showing a little bit of
*  preview of that maybe like mechanistic interpretability techniques developed for
*  machine learning become the way the back door into understanding like what actually matters
*  in as you know, it's hopefully learned from just like a huge amount of multi-omic data.
*  What's your feeling on that approach? Yeah, gosh, this is a topic I think that maybe is older than
*  EVO's Brian model. So I think if you go back a little bit to these companies like Recursion or
*  Incitro and to some extent Calico, although I don't actually understand what Calico does,
*  but like basically they tried to build this foundation model of biology. Like you basically
*  build some big matrix of small molecule drugs, maybe transcriptomic data of what genes are being
*  turned on, what are turned off, and then take pictures of the cells and that's the phenotype.
*  And you can build this big model of like how molecules affect the genes from the transcriptomics
*  and the phenotype from the imaging. And then a big model can come out of that and then you can sort
*  of like the biology will just sort of fall out or the new targets will fall out. And this is sort
*  of like a long, this is just like one step in the long promise of genetic information, right? Like
*  there was the human genome project, we could figure out all the genes. Then there's like, okay, we
*  need to see how they change. And we get something like GWAS, whereas like, okay, we're going to
*  finally figure it out now, but GWAS didn't lead to this. And we have these things like depth map or
*  something from the Broad where we're trying to understand lots of cells and tissue. And yeah,
*  I think like the next one is like looking at the genetic, these genetic foundation models.
*  I think that they can be very good for things like metagenomics, for understanding transcription
*  factors, understanding regulation networks, but I don't think they're going to be like the sort of
*  silver bullet that unlocks any deeper understanding of, you know, of diseases or any deeper understanding
*  of what goes on inside of a cell. I think they're going to be one more model, one more tool in the
*  toolbox, but I don't see them as really moving the needle that much. So yeah, I don't know. I'm kind
*  of pessimistic on this thing. It's like one of those fields where people have tried really cool
*  sounding ideas and it should have worked eventually, but every single one has failed. And so now,
*  like when you get old, like me, that you are just cynical and everyone that comes out, you're like,
*  well, we'll see. I don't know. You can read Derek Lowe. If you ever read Derek Lowe's blog is like,
*  the guy's, I'm not going to say he's cranky, but he's seen a lot of like waves of new ideas
*  and biology and it's pretty rare for things to work out. So a cynical position is the default,
*  I think right now, but certainly I think from just understanding biology, awesome for curing
*  diseases. I think we'll have to wait and see if it really moves the needle anyway.
*  Soterios Johnson Do you think that could be, because I think you could tell a very similar
*  story about machine learning up until like five years ago or maybe 10 years ago, depending on
*  exactly when you want to start the clock, but there's like a sport now of like everything was
*  invented in the eighties. And I think to a large degree, that is true. Like most of the ideas that
*  are now really working with sufficient scale, people had at least an initial take on a long
*  time ago and they just didn't have the scale of data or compute to get there. How, you know,
*  I don't know if you want to approach this from like a handicapping perspective or like, but do
*  you think that there is a chance that it's just a matter of all these things, maybe we're the right
*  ideas, but we just haven't got quite enough scale to actually grok, so to speak.
*  Chris Bounds Yeah, yeah, I think you're onto something here is that one of the challenges
*  of biology is the latency from like idea to feedback. Machine learning is great because
*  you can try things and as computers gotten good, you can see the results of these things.
*  And in fact, you see a problem right now where basically people have cool ideas that work at
*  like a 1 billion parameter model, or maybe a 500 million parameter model, when you scale up to like
*  a 10 billion parameter model or 40 billion parameter model that all this just doesn't work.
*  Or if it's like you works at 500 million tokens, you go to a trillion tokens and it doesn't work.
*  And so you see this thing of like, when you scale up, it costs more time and there's, you know,
*  longer latency and that is a great filter of ideas. And you find out, okay, actually,
*  the simplest ideas are these ones are the right ones. In biology, we kind of have this
*  as well, where basically, you can do pretty quick experiments on a protein in a well, right,
*  like just a little protein, you can do you can manipulate it pretty quick, and you put in a cell
*  and then okay, it's a little bit longer, because you gotta wait for the cells to grow. And you
*  got to transform the cells somehow. Then you go to like tissue and then you go to model a mouse
*  model, right? Like let's say I want to cure aging. Well, unfortunately, mice live a long time. And
*  so you gotta wait for those mice to die or not. And so like you keep running these latency problems.
*  And we get to drug discovery is the it's at this latency, where like humans just suck at because
*  it takes whatever seven years from mechanism to phase two trials. And it's phase two clinical
*  trials tell you if the drug worked or not. And seven years means all the people there have gone
*  moved on, right? Like seven years means that people forgot like why they were doing this in
*  the first place. And so you have these like feedback loops that take so long. And that is
*  really hard. So I agree, it could be something that we figured it out. But we won't know for
*  30 years because we need to try a few cycles to see if it works. Or maybe recursion maybe in
*  Citroen, maybe Calico, they all got it right. But in Citroen just got their first platform asset,
*  I think in phase one, or something or to IND. So it took seven years for them to get from company
*  conception to getting their own molecule into the clinic. You look at recursion recursion,
*  people are love recursion, like they do great social media, they have a big GPU cluster,
*  everyone's excited about them, hope their stock price keeps going up. But recursion, I think all
*  of the assets that are in clinic right now from them, they bought from other people. So they
*  haven't really got their platform going yet. So we won't know if their idea of building a big
*  foundation model is the right answer for a while. And then things like atomize are very early biotech
*  doing convolutional neural networks on small molecules binding proteins. Great idea. They
*  had great work, great results, great people. But you know, what happens is like some of these
*  biotechs, they'll die because they picked the wrong target, not because they had the bad platform,
*  or the tech wasn't right. And so you just really hard to separate cause and effect with these very
*  long latencies, very expensive experiments, and so many variables going on. So I think it may be the
*  same as machine learning, it may be some bitter lesson, but we're not going to learn it until
*  30 years from now, or until we figure out a new way to do experiments, right? Maybe the human
*  organoid research is going to get us to lower latencies on getting feedback from ideas. Maybe,
*  you know, maybe RFK Jr. is going to come up with a whole new way of doing FDA, you know, approvals,
*  so it will get faster clinical trials. This is like, there's this stupid thing and drug discovery
*  is like, the biggest, the most important bottleneck right now is like time to enroll the first patient
*  in clinical trial. So if you wanted to cure diseases, cure cancer, if you wanted to save
*  the world in drug discovery, you should be working on better like online ads for a clinical trial site
*  enrollment. And that should be where people invest the effort, but that's not a sexy thing to invest
*  the effort in. But that is like, I don't know what it was like 60 days, things the time to
*  enroll the first patient. And that 60 days is like very amenable to innovation, but people put
*  their innovation in like finding a new hit from a machine learning model or like building a new
*  foundation model to maybe improve your biological mechanism by a little bit.
*  Soterios Johnson If there's one thing I do have some hope for the Trump administration doing,
*  it would be some sort of data liberation out of electronic health records to then
*  have a long crunch through and more proactively identify the possible patients as opposed to
*  having to filter everything through the click of an ad and then, you know,
*  like the data manually.
*  Ben Frick Yeah, actually, if you have a direct line to RFK Jr. or Donald Trump, or if you know,
*  Soterios Johnson I'm a couple of lessons away, but
*  Ben Frick Okay, here's something that they can do, release all of the IND packets for every drug
*  that is like every drug which is clinically approved has filed an IND packet which contains
*  a ton of valuable toxicity, you know, pharmacology, pharmacokinetic data, and all that data is no
*  longer a competitive use for them because if it's already clinically approved, like there's no
*  competition, it's already under patent protection, it's already being sold. If they were to release
*  all that data, there's a huge trove of data that we could use to better fit machine learning models,
*  and it's very expensive data to get. And it's all kept at the FDA. And for I think, you know,
*  no really good reason. So anyway, that is a
*  Ben Frick I heard there might be some of it in just like folders at Mar-a-Lago. So you could also
*  head down there and take a left turn past the bathroom and who knows what you might find.
*  All right. I joke, but I shouldn't joke too much. I don't want to get into any retribution lists.
*  Okay, so this has been a great foundation. I think it's always really helpful to understand the
*  worldview that motivates the work. Let's finally get into future house. You can maybe give us a
*  little bit of kind of, you know, I think I have a growing intuition for why the AI scientists,
*  and it sort of is like, you don't really believe in any other silver bullet. And so we just need
*  more scientists that can grind away at this for a long time. And obviously, an AI scientist has
*  certain strengths. I've particularly dug in on the paper QA and then the new aviary papers, but
*  maybe give us kind of a, you know, a brief history from kind of inception to
*  these most recent ones, if you can highlight any other works and kind of the overall strategy
*  to T. Vota. Yeah. So I guess like future house started with ChemCrow. So ChemCrow is an early
*  paper where we basically wanted to do like a full scientific discovery process with language models
*  and these tools. So I think the most important sort of problem we did in ChemCrow was we combined
*  like retro synthesis predictors, literature search, like code execution. We combine that with GPT-4
*  and we asked to design like a new die. So basically we said, okay, here's, I want you to
*  make a molecule that's novel with two steps. And it's like a two step chemical reaction. It's never
*  been made before and have absorbed light at a specific wavelength. And we gave it to start with
*  the supporting information from a paper. And so basically fit a machine learning model to
*  the supporting information to predict the wavelength absorption and of light and molecules.
*  Then it basically used the retro synthesis tools, did some searches to try to find a new molecule
*  that would absorb at the specific light. And then it came up with a reaction procedure. And we had
*  like a robot lab at IBM, IBM RoboRxN, which is like a cloud lab that we were able to use. And they
*  were able to go through the synthesis procedure to make that new molecule. And then we were able to
*  test it and it actually was very close to the wavelength of light. I think we're like 15 nanometers
*  off or something. So it was like a great like closed loop discovery. There were some problems.
*  Basically we were in a rush, we're in a time crunch. So the robot didn't finish that reaction. So we
*  actually had a person go in and do the last step. So it didn't, it wasn't like a completely AI novel
*  molecule, but we did other examples in the paper where it was all done with the robot. But I think
*  it's like a full loop, right? Basically it does literature research, it plans the protocol, it
*  goes and executes it and it does the measuring. But one of the things I realized is that
*  scientific literature is such an insane concept to me. It's really surprising that we did this
*  as a civilization for hundreds of years and built this big networked artifact of all of
*  scientific progress. I can complain about how it's locked up behind publisher paywalls for hours,
*  but I won't hold back. But basically this sort of artifact is to me like, whatever, like 99% of
*  doing science is knowing literature and the last 1% is like just moving things around a little bit
*  to get to innovation. And so when we started Future House, we wanted to go after like the first thing
*  is scientific literature. Like if you can sort of work with literature and you can understand
*  literature and see what's been done and what hasn't been done, like see what's novel, what's not novel,
*  that's going to be a huge fraction of the work of automating science. So that was the first sort of
*  project we did was Paper QA. So Paper QA, I actually wrote before Future House. I was giving a talk in
*  Copenhagen and Denmark, I think it was in January or February, something like this. And I was in the
*  hotel, it was rainy, it was like winter, so it wasn't much to do. So I just like was messing around
*  my laptop and made Paper QA. And it was like around these ideas of like rag systems. And what was
*  different about Paper QA was that what it does is it basically pulls up all the relevant papers.
*  And then instead of like pulling the chunks of the papers and giving it to a final LLM to answer,
*  which is sort of how rag normally works with, what it does is it basically does a map reduce,
*  is it pulls up all of the chunks that could be relevant, and then it runs an LLM on each of these
*  chunks to summarize them and re-rank them and then give them to the final language model to do the
*  answer. And that solves like two problems. One problem is that language models are extremely
*  sensitive to distracting information in the context. So when trying to work with scientific
*  literature, if you got like a wrong paper in there or a section of a wrong paper, it would just blow
*  up the system with incorrect information. So one example is like one of the questions you could ask
*  it is like in the, I don't know, in the EBM trial, what was the size of the placebo arm?
*  And it would pull up the wrong like trial methods. And if that was in there, it would like distract
*  it from that information. So that was what this context summarization step did. So anyway,
*  that was paper QA. And we spent like basically the concept was done very quickly. And there's
*  tons and tons of like defining what are correct answers. How do you work the literature? How do
*  you make sure you get all the papers? How do you consider citations, journal quality? How well do
*  humans do? Can we make this repeatable? Can we iron out bugs? And it took a long time. And sort
*  of we capped off the project with something we call WikiCrow, which is once we beat human level
*  performance by making lots of changes, we have an engineering blog that walks through like all the
*  short of A, B decisions we made to get to beating humans. We wrote 20,000, actually came out to like
*  18,000 Wikipedia articles that covered the function of every gene and the human genome,
*  with the exception of a few like 2000 or 1500 that have no papers ever written about them.
*  So that basically was a summarization of all knowledge of the human genome, which didn't exist,
*  doesn't exist until this is done, because Wikipedia only covered like, you know,
*  2500 of them. So we, you know, we added like 16,000 more articles to explain the rest of
*  the human genome. I think that was sort of a good mark that showed that we can do this at scale.
*  And we can do things like with a scale that we can do it, we can answer literature questions,
*  as well as humans, and we can do it like 75 per minute. So we could like, do what we call
*  contradiction detection. So we have systems which can look for any contradictions or disagreement
*  with any arbitrary statement from the literature, which is actually really hard task, by the way,
*  like to check all 250 million papers against an arbitrary claim. We can do that at scale,
*  like every archive paper that's on archive per day, we can check every single one for any
*  disagreement literature and market. Or we can now like write the Wikipedia article for every disease
*  that exists every three weeks, considering all new research that comes out. So I think paper QA is
*  like a really good like beginning to end, we beat humans, we deployed it, we put the infrastructure,
*  we have an API, and we can run it at scale. And now that we have that, then it was like, okay,
*  what comes next? And so we sort of took the lessons we learned in paper QA, and that's
*  something called aviary. And what we did is we broke up paper QA into two components. Basically,
*  there's what we call the environment. And this environment is like the tools that are available,
*  like look at citations, summarize literature, or sorry, summarize this paper, like do a Google
*  scholar search, do keyword search over some corpus. We turn that into environments, and then we have
*  the agent, which is the thing that sort of drives the decision making. That's like, okay, let's go
*  do another Google scholar search. Okay, let's actually search semantic scholar. Let's see who
*  cited this paper. And aviary is this idea that, okay, let's make a bunch of environments of
*  scientific tasks beyond literature. So like ChemCrow, there's an environment like for ChemCrow, or we
*  have an environment for designing proteins, we have an environment for like doing molecular cloning.
*  So we have these environments here. And then what we do is we make agents. And we've separated
*  these two so we can try different agents, not just different LLMs, but we have agents that we've made
*  ourselves, their own LLMs, or we have agents that have memory, we have agents that can do things like
*  have multiple actions considered, they can do like reflection, they can do, you can have like a reward
*  model baked inside of an LLM. So we sort of try to structure this agent interaction. And then what
*  we do is when we have an environment and an agent, and we train them together on some benchmark,
*  and so like we wrote lab bench was a collection of benchmarks that we think are relevant for doing
*  science. When you train them, you basically put them together and you call it a crow.
*  And so a crow, because basically it's like has tools, that's the environment, it uses language,
*  that's the language model, it put this together, it's like a crow because crows are birds that can
*  talk and also use tools. And then we are now deploying them. And we built like an aviary,
*  which is a bunch of different crows that can do different tasks, and they all are connected.
*  And we're slowly building like a platform of intellectual microservices, basically, go look
*  for contradictions, go do a literature research on this topic, design me a molecule that does this,
*  design a plasmid which can clone this specific protein of this specific organism. And so putting
*  all these things together, we were basically building the API for doing science. That's
*  fascinating. Cool. Really nice job laying out the progression and the vision there. Any number of
*  follow-up questions? I guess, going back to paper QA, you're now on paper QA 2, right? And
*  the one thing that stood out most in terms of like why it has worked well, because of course,
*  other people have tried to do this too. And I would say it's not easy to get above human performance
*  in answering these questions. It sounds like one big insight was process everything. I sometimes
*  call this flash everything in honor of Gemini Flash because it's so cheap. I once set up the
*  challenge for myself to spend a dollar a day on Gemini Flash, which is 13 million input tokens and
*  a lot of information to process. So I actually have not achieved that. I've achieved it on a few days,
*  but not on a consistent spend a dollar every day on Flash because it turns out it takes work to
*  identify those targets. But it sounds like that's one of the big things was do this filtering and
*  identification of relevance with the language model as opposed to just with an embedding
*  approach. What other big drivers of incremental progress would you highlight for people that
*  might want to build a system? Yeah. I think that was a big idea, was doing that. Solves a lot of
*  problems. All of the effects of chunking, chunk size, quality of parsing, a lot of those things
*  just disappear when you do this extra intermediate step. So it sounds like extra work, but actually
*  it solves a lot of, I think, practical problems. It also increases the cost and the time to get
*  a response. And I think that's why you don't see perplexity or illicit or anybody doing this kind
*  of process, this sort of two-step process, because for a consumer-facing thing, you're going from
*  whatever 15 seconds or five seconds to like a minute or two minutes. And I think that kind of
*  reflects the philosophy is we just want to build the best possible system, forget cost, forget
*  latency. So I think that's- That in and of itself, just a highlight I would say is a really important
*  philosophy that I try to giant apple seed my way around the world. Any chance I get,
*  engineers have way too much emphasis on especially cost latency. I understand more if you have a user
*  sitting there waiting. Human time is still precious, even if tokens are increasingly
*  super abundant. But I always emphasize, yeah, deliver me the highest value thing first at any
*  cost and at any latency, and then we can kind of work backward from there. So that's good.
*  Yeah. Yeah. I think this is something- Yeah, it's great. I mean, I think it's a philosophy
*  people haven't really caught onto because people think are still stuck in this mode of like a Google
*  search, you know, where it should come back fast and it should be like a more ties costs where
*  they spend a bunch of money building a big index and then they have low cost queries. We didn't
*  spend a bunch of time building a big index. We like do all the processing just in time. And so
*  everything's more expensive, but, and we don't really amortize the cost. Another big effect is
*  full tech search. Basically most search engines over research papers are not full text and that
*  just loses so much information. And that's why most benchmarks and most competing tools work with
*  abstracts and titles because those are accessible from search engines. It's very rare to get full
*  text search. So we have built our own full text search. We open sourced like a version of that
*  and the paper QA to repost, they can build your own index. We have our own internal, I mean,
*  thing it's just exactly what you think. So you can just like full text search and Postgres,
*  or you can use elastic search. And then Google scholar is like just really, really, really good.
*  And so we use a lot of like our performances from using things like Google scholar and
*  semantic scholar, which recently has full text search. So that's a big change. I would say other
*  things that are anything you can do to remove distracting information. And so a lot of our
*  engineering blog is things like how to cut out potentially relevant things, how to do like
*  summarization efficiently. Like we might consider 75 sources and then cut them down to 10. And
*  that's better than like considering 25 and cutting it down to 15 because you don't have as big of a
*  cut. Yeah, so I think full text search. So, you know, search very, very important. And then this
*  step, I think we call it in the paper, like RCS retrieve and contextual summaries, sorry,
*  rank and contextual summaries. Those are the most important things.
*  One thing that did jump out at me as I was kind of perusing the code a little bit is it seemed like
*  the control flow, like the actual agent itself wasn't super complicated. Like the prompt didn't
*  seem super insane. It was kind of like, here are your tools. You know, it was sort of much closer
*  to what I think people would sit down and write in their first attempt than you might think given
*  how well it works. So I wonder if you had any reflections on that. Yeah, I think what we have
*  in the repo is like pretty general purpose. If you look at like, I think in the repo, we have these
*  configs and there's like a WikiCrow config or a ContraCrow config. Basically ContraCrow is like,
*  just look for contradictions. And that's, I think, quite a different one. And WikiCrow is like,
*  summarize these things. I think we had a philosophy change. We used to have a very detailed prompt and
*  we moved a lot of the complexity and the tool descriptions. So we have something called,
*  the package is called Aviary. And what it does is it will take like a Python signature with types.
*  And then the docstring will turn into like a tool for an LLM to use. And so the docstrings will end
*  up as the tool description. And so some of the complexities kind of hidden away in the docstrings
*  where it's things like, okay, like try doing multiple searches, like different keywords. And
*  actually this is why perplexity is quite good. Is there a perplexities pro search? It does what's
*  called query expansion. Is that you like, whatever, do your thing. The question you're asking, it turns
*  it into like keyword searches. And with this query expansion, it turns it to like three keyword
*  searches with different phrasings. And that really helps. Something we use as well is that we don't
*  use it. We tell the LLM like try doing multiple searches with different keywords. And that's
*  actually a really effective way to get a good retrieval of sources. We have this tool, which we
*  don't really advertise because we're not sure we can handle capacity, but it's called hasanyone.com.
*  Have you seen that? No. Okay. So we have this tool called hasanyone.com and it's like a very like
*  narrow version of our internal tool we use for paper QA. And it will basically do a search to
*  see if anybody has done X and it uses our paper database and our like search tools and things like
*  that. And yeah, it's like a way to see because paper QA too is like we've changed some things
*  for it to be more useful to people. Like rather than using like a full-text search you build and
*  put on cloud infrastructure, it like uses this Ross library called Tantivi, which will build
*  the search index for you like based on per directory. It's much closer to what people want.
*  We have our own full-text search that's like on our cloud infrastructure. So you can use the
*  hasanyone.com to sort of get a sense of what we use internally.
*  Gotcha. Cool. Would these things work if you just did like a quick pivot to a totally different
*  domain, like a social science? Could you go to economics or education?
*  Yeah. Yeah. It actually, it works well in many different domains. We've used it in lots of
*  domains. We actually have a phone number we can text. So like I'll be out at like, I don't know,
*  a party or something like that. And I can text paper QA and it will text me back like a response.
*  And yeah, I've had, I've asked it questions all over the place, history, economics, whatever.
*  It has access to all the papers in these domains. Like some of the, like we've concentrated on
*  getting access to papers in like biology, you know, in medicine, but it has, you know,
*  archive, camera archive, met archive. It has like the ability to download open access papers. It
*  has like anything we have in our cache. So it's able to cover a lot of different domains, but you
*  will see this unevenness. Like if you go to like, I don't know, if you go to machine learning,
*  it's great because everything's an archive. There's no real problems with open access,
*  things like that. If you go to something like, I don't know, internal medicine,
*  like New England Journal of Medicine, like they have some open access things, but they have the
*  most annoying cloud flare, like anti-bot stuff. So we're not able to access any open access papers,
*  New England Journal of Medicine. And so it's kind of like field dependent, which journals are
*  dominant does impact the performance. Yeah. That stuff is quite annoying. It's, I mean, that has
*  really been a big story of agents in general purpose, web agents, whatever. It's like,
*  they're so often hung up by literally the dumbest stuff. Very weird phenomenon.
*  One thing that I would say is not so dumb. This is what I was going to ask before. And
*  finally remembered was the challenge of just using figures effectively. I find like,
*  whatever, no need for false precision, but just on reflecting on my own mode of absorbing
*  information from papers, a lot of it boils down to the figures. And unfortunately,
*  most of the time still, when you put a PDF of an academic paper into a system,
*  it just kind of skips those and just maybe takes the like caption, but doesn't really
*  engage visually with the thing. Did you guys try to do anything about that? Or is that something
*  you're just kind of waiting for models maybe to get better at and hope to delegate in the future?
*  So we actually have a benchmark called Fig QA in our lab bench paper. And Fig QA is like an
*  assessment of scientific figures where we took pretty hard figures and pretty difficult questions.
*  And actually, I think the October Sonnet model beats humans on this benchmark now. So we've reached
*  a point now where actually the models are definitely human or superhuman performance on looking at
*  figures. So we are actually adding this now to paper QA. I think we're really bad at naming
*  things. So like we call it paper QA 2, but like we try to use semver. So like to monitor backwards
*  compatibility. So we're actually working on paper QA 2 version 6. And that version 6 is going to
*  have the ability to look at figures. And what we do is just kind of like, you know, really simple
*  is that we parse the table, sorry, we parse the paper as text for the purposes of search.
*  And like, and then we feed the images into the models for the later stages, either RCS or RCS
*  and the gen, genera, and so the final answer step. So we are looking at that now. I think the models
*  have reached the point where they're good enough at looking at figures that you can actually do this
*  at scale. And so you chunk and then you just kind of attach an image to the chunks. And then at the
*  very end, you kind of include the associated images. Yeah, yeah, I think we've the I mean,
*  we haven't written a paper on this or done a lot of benchmarking on this. But the current
*  philosophy is that the purpose of the text then is just for the search. And so the figure captions
*  there and then the searches there. And then what you can do is you just give the picture of the
*  page, including the text around it, as opposed to the, you know, as opposed to some parsing of it.
*  And yeah, I think these models are so good at this that there won't be any issues. I mean,
*  you can go down this path. We did this for building figure ways you can use label box,
*  just like human annotation to try to cut the figures out. There's a group thing called like
*  CyInt or something. I think it's I forget where they're from, UChicago or something. But they've
*  written like a pipeline of PyNew PDF to extract the figures. But it's really fraught because
*  PDFs are so different. You have a PDF from 1992 and the figure extraction is not going to work.
*  And then a paper from 2020 it might work. And so yeah, I think it's really difficult to extract
*  figures programmatically. So I think just taking a render and taking an image of it is the way to go.
*  Yeah, okay, cool. That's quite interesting. So no love for not to say no love. That's too harsh,
*  but no need in your estimation for various tools. I'm thinking like marker API. There's a number
*  now that are sort of specifically about slicing up inputs like this.
*  So this is a good question. I think our philosophy, like going back to what we're talking about is we
*  just want to spend the most money and the most time, but for the lowest technical sophistication.
*  So I think those kind of like these, there's a few of these companies now, and I think a lot
*  of them are built around Detectron fine tunes, where you basically fine tune language models to
*  parse up patents or research papers. And I think just long term, what's going to win is just taking
*  a picture of the page and giving it to a model which is sufficiently competent to actually look
*  at the page and answer questions about it. And right now, if you just take a picture of the figure
*  and you give it, including the caption and everything, if you give that to Sonnet, the
*  October model, it will correctly answer questions about the figure. And so I think there is no
*  additional need to go more complicated. Yeah. I want to see, that makes me really interested in
*  the, and I'm kind of surprised I haven't seen this yet, the latest Claude score on the ArcGi
*  prize because when they did the first three fives on it, that was a major step up in coding,
*  whatever, however many months ago, I took ArcGi puzzles to it. And I was really amazed by how
*  poorly it could see for lack of a more technical account. It could not
*  count blocks or do the basic atomic functions that you would need to be able to do in order to
*  do the reasoning later. This is probably another example of, or at least seems pretty likely an
*  example of something that you kind of said at the top of they learn in sort of a reverse order.
*  Because I bet that if you could see more effectively, the reasoning would be a lot
*  stronger, but the such basic mistakes were made at the reasoning or at the visual level.
*  This new one, of course, can count pixels and do all these click accurately on buttons. So
*  where is that score? I wonder. Yeah. Yeah. I think when we built our benchmarks,
*  the first thing we tried to do was I would call recall oriented tasks. Like here's a table,
*  turn the table to JSON, or here's a figure, like give me all the values of the figure.
*  And the models are not very good at this recall oriented tasks, but then we realized like,
*  we don't actually care about that. We actually care about like these precision tasks. Like
*  based on this figure does the treatment of A improve response or based on this table is method
*  A better than method B. And it turns out that those precision oriented questions are very good.
*  Those are like, they get superhuman level performance on them, but these recall oriented tasks,
*  like digitizing it or counting things, it doesn't do well at. And that's actually been like a weird
*  kind of mindset shift for me is that, I mean, this is like, like you go to Gemini, you put a whole
*  hundred thousand token document in and you say, okay, like what are the, what are the 50 main
*  conclusions of this document? I'll do a shit job. But if you go like, what's conclusion one
*  is this, what's conclusion two? Okay. Then here's conclusion two. What's conclusion three?
*  And these models just work so much better in this like, sort of, I don't know, turn by turn or
*  autoregressive way where you like ask like single questions or single responses. Whereas if you try
*  to get these like cohesive things, where it's like summarize everything into JSON, they struggle a
*  little bit more. And so I think in the figure understanding, if you ask it specific questions,
*  it does well. But when you try to say, like, get all the information out of the figure,
*  they don't do very well. Yeah. Interesting. So are you going like, what is the cost and
*  latency to run a question? Maybe that varies to some degree by the scope of the question,
*  but what do you roughly give in terms of guidance there? And is this something that you will
*  productize in a full way? Like I looked at the GitHub repo and has 6,400 stars, which is not
*  a small number. But I also feel like the burden of, or not the burden, but the barrier of just
*  having to figure it out is a lot compared to if you guys were to commercialize it, I bet you'd
*  have a lot of interested customers. Yeah, this is a good question. So to answer your first question,
*  you can see the real latency of the full system if you go to hasanyone.com and ask like a new
*  question. And it costs like between maybe 15 cents and a dollar depending on the question.
*  Like if you ask, has anybody done X and if X is like some moderately popular topic,
*  but it's a niche thing, it will do lots and lots of searches and lots of exploration to see if
*  anybody's done it. But if you ask like, I don't know, has anybody landed a UFO on the Washington
*  monument? It's not going to do a lot of searches. So it does depend on the question. But then like,
*  yeah, as far as like the GitHub repo, we intentionally make it hard to set up because
*  we really only want to be interacting with programmers, like hackers who know their way
*  around these systems. I think if we have like a one click setup or something really easy to set up,
*  then we're going to have to like go down the path of supporting lots and lots of player people.
*  And already like we run into so many problems with like, it doesn't work on Colab because
*  Google will not do Python 3.11. Sorry, they won't do 3.10. I don't even remember at this point,
*  but they basically are not updating Google Colab when we just use some Python 3.11 features.
*  And that's already like a big source of problems. And I just think if we make it super easy,
*  it could be an issue. Although Ethan Malik was able to get to work on Windows, which was like
*  a real testament to us being like, okay, we'll try to support Windows a little bit. So that was
*  very exciting. But yeah, I think commercializing it is, you know, we get a lot of inbound, like
*  people want to use it for doing diligence on acquisitions or diligence on investing in
*  companies. People want to do it for like doing IP searches. People want to use it for their PhD.
*  I will say that we generally let in like academics, like PhD students who will ask for access to the
*  full API. And we did do a workshop where we give people access to the API with like rate limits of
*  five questions per day. Because we have this Python API that uses our server. And so people
*  do these like sort of interesting projects where they have some idea generating model,
*  which then takes every good idea and then runs it through paper QA to see if anybody's done it or
*  if it's supported by the literature or if it's invalidated. So there's like a lot of cool ideas
*  that people have here. But we are always caught in this tension of like, we want to measure success
*  as an organization as like number of novel discoveries. And does commercialization or
*  revenue of paper QA does that lead to more discoveries? I don't know. It could if the
*  right people are using it and the right like sort of progress is being made. Or maybe you can argue
*  that like growing revenue paper QA is going to be like beneficial for the org so we can hire more
*  engineers or something. And so I think we haven't figured out that sort of like that sort of balance
*  between what is good for our mission and what is like just chasing a mirage or something or what's
*  just going down this commercialization path for no really good reason. So I think we haven't worked
*  that out. But that is something we think about a lot. Yeah. Okay. Cool. So turning to Aviary,
*  just had a couple of in the weeds questions on that as well. It seems there was like a couple of
*  novel things in this paper. One is the just kind of high level concept work to try to get clarity
*  on like what is an agent versus what is the environment. There's been a lot of confusion
*  there or at least people are sort of doing things a bit differently. You were willing to put a stake
*  in the ground. And it seems to me that the big thing is the memory is internal to the agent in
*  your conception. I was a little less clear on like, if somebody does it the other way, are you saying
*  they're wrong or like where does that matter? Yeah. But yeah, I'm interested in kind of your
*  philosophy of what is an agent. Yeah. So like how we broke it out in the paper is that I think a very
*  working or very practical definition is that anything that you want to train is going to be
*  in the agent. Anything that you think is untrained will go in the environment. They interact with
*  language, with observations and the actions or tool requests or function calls basically.
*  And so when we like go down this framing, it just simplifies a lot of things that we can try
*  arbitrary agents, arbitrary trainers with agents, and then we can have arbitrary environments. And
*  it's like a pretty opinionated interface, but it just sort of frees us up that we can really try to
*  change things all these different directions. Moving memory from the environment to the agent,
*  I think is again, one of these opinionated ideas. But when we thought about what is memory,
*  like we thought about things like, okay, you can just append messages, but maybe you need to modify
*  them. Once there's so many messages, you need to like compress them somehow. Or maybe you don't
*  want to do memory. You want to do like five previous messages. You want to use rag for like
*  the previous ones. Right. And I think it's because of this is like so many ideas about memory, it's
*  got to be a trainable thing. Like no matter how you write down memory, there's hyper parameters in
*  there, like how you truncate it, how you compress it, what you include in the previous messages.
*  Maybe you want to cut out any images in previous messages or something. So I think all these kind
*  of decisions made us realize that memory really is meant to be part of like a whole system.
*  And then I think another decision we made is that we frame the agents as compute graphs,
*  stochastic compute graphs. And this is again, like I think an unorthodox, I shouldn't say
*  unorthodox, but like, I don't think a solve problem because a lot of people view agents as these kind
*  of state machines that are like somehow like going through multiple states. If you do it as
*  a compute graph, it's like a forward to back, you know, from left to right. It's like a, you just
*  shoot once there's no recursion in it. And there's also no state in it. So the way that you actually
*  get state here is that like the input to the compute graph is the agent's previous state.
*  So the agent basically takes in a previous state and observation and emits a new state and an action.
*  And this framing is, I think, again, it's like not how I think people naturally feel about agents.
*  I don't think people think about them as compute graphs that much. They like to think about them
*  as programs or some sort of stateful operation. But this just does a lot of things for us. Like
*  it allows us to do backprop over the compute graph. It allows us to efficiently execute them. It
*  allows us to do things like efficiently serialize and deserialize these things as compute graphs,
*  without having to think too carefully about the state. So these kinds of decisions, I think,
*  are very practical decisions. Like how do you make progress on learning? And in the version of the
*  paper I sent you, we didn't have any learning results in it, but we'll have like learning
*  results showing improvement, showing basically different training strategies, having generalized
*  learning across different environments and with different agents. And so I think the proof is
*  going to be the pudding. Like what can you get done with this framing? And I think we can get
*  a lot done with this framing. And I think a lot of it is motivated by the fact that we just have to
*  get past zero shot. Like I think a lot of agents you see today are all zero shot. And in the zero
*  shot regime, where you basically just work on the prompt, work on the hyperparameters manually,
*  these opinions don't matter. Like you can build a zero shot agent in Python. You don't need
*  framing. You don't need framework. And I think like some of the effort has been put things like
*  on observability or traceability or like developer velocity. I think what ours is really built for is
*  can you train them? And so that I haven't seen as much in the field. Like I think DSPY is the
*  closest to what we've built, but in DSPY, I think they're not really in an environment. There's not
*  really RL going on, whereas we really do like online RL. We do online PPO with some of our models.
*  Okay. Yeah, that's quite helpful. I think the thing then that I want to understand better is
*  this black box gradient estimation, which is once you've sort of taken an agent and said,
*  okay, we're going to make it, you're going to iron out or uncycle the cyclic things or eliminate any
*  structural barriers to making this thing end to end trainable. Now you still have a challenge of,
*  what if I'm using Claude or O1 or whatever as part of that compute graph? And I tried,
*  but I didn't develop a great intuition for what you are doing. The quote that I pulled out
*  that I would love to understand is to obtain these estimates, this is for describing black box
*  gradient estimation, to obtain these estimates, we modeled the behavior of the language model
*  and embedding nodes around the current configuration values with a multi-layer perceptron
*  and back propagate through it. Yeah. Explain it like I'm maybe not five, but maybe just like a
*  lowly grad student or something. Yeah. So this work came from Sid and Albert and they're
*  brilliant. So Albert actually, he did RL with Gianni DeFrabriti, which is very good biotech company
*  actually. And Gianni won the Unity RL challenge or I think that second place Unity RL challenge.
*  These guys are like RL geniuses. Albert, he also was, I think the first author on PyTorch RL. So
*  this guy's a genius. So I'm not, I actually don't think I fully understand what they did.
*  But he wrote this paper by John Schoen. He wrote this paper on stochastic compute graphs,
*  which basically lays out the framing of them and like what the nodes are, the edges are,
*  and like talks about this. And we had built something like this and we found this paper.
*  I'm like, okay, well, like this paper actually describes what we built quite well. And he had
*  written out these terms and like how to do back prop through stochastic nodes, which is like not
*  trivial to do. And then Albert and Sid, they basically decided to extend this to do it over
*  like black box nodes. And this is kind of like a no free lunch sort of thing where you really
*  have to build a surrogate model, right? Cause you can't back prop through this black box model.
*  Cause we don't know like what happens if we change the temperature on the input or the output,
*  there's no way to trace the gradient through because we were calling anthropic, we're calling
*  opening eyes API here. What they did is they tried to model the variance explicitly with an MLP.
*  And so what you do is you basically, you go to do a call through the black box model.
*  And what you do is you pick a temperature of one, you call it whatever, five times with this
*  temperature of one. And that gives you like an estimate of the, I would call it the aleatoric
*  uncertainty. Like if I just call it over and over again, how much noise is there in that process?
*  And then you get that out and then you can basically use that noise to measure the aleatoric
*  component. And then the epistemic component would be like, what happens if I change these things?
*  How much noise do I get? And then you can try to change these parameters a little bit and then get
*  like an estimate of the change there. And then you can model this with an MLP and the MLP is
*  never going to be universal. Obviously if the MLP could model the gradient everywhere, then you
*  would have reproduced GPT-4, right? So what this MLP does is it gives you like an estimate of the
*  local gradients by just watching how these input changes affect the output. It's very expensive
*  because you're talking about running like whatever 25 calls per input to estimate the gradient.
*  So what you want to do is you want to basically do a rollout, just do forward inference using the
*  agent a few times, and then you basically get a bunch of rollouts and then you want to go do one
*  back prop step and you can basically choose which set do I want to do the most. Then you can estimate
*  these gradients. You can try to do things like cluster them. So like here's a bunch of similar
*  inputs. So we'll use the same MLP for them. And then you can do this back prop. It's very cool to
*  see in practice because what you can do, like in the paper we show, you can optimize the temperature
*  for your model. You can optimize like the, I think it was the parameter in the prompt.
*  You can optimize things like your some hyper parameter upstream, like how many times,
*  how many periods you have in your prompt, a very unusual kind of way to do back prop.
*  Now in practice, really this is more of a trick, I think, to show that it's possible. This does
*  not lead to very good optimizers because basically usually things upstream of the LLM are like,
*  there's some optimum, like temperature point two is optimum. And once you know that there's not
*  really much benefit in trying to change it. It's like very rare for there to be correlations.
*  It's rare that you need to like change temperature at the same time as changing
*  compression factor in the memory. They're just like not that correlated. So I think it's a really
*  cool like technical achievement. And it's cool that shows that you can do back prop to these
*  black box models. But I think that as far as like, what did the outcomes change?
*  The outcomes are not that important.
*  Interesting. Okay. So this would be really powerful if you're using an open model.
*  Yeah.
*  Not so powerful if you are using a closed model though, you can still get something out of it.
*  Yeah. I think the results we will have on the optimizers, what we do is we kind of split the
*  models in two. So we actually have a black box LLM, and then we have a second model,
*  which evaluates the outputs from the black box LLM. So with the black box LLM generate a few
*  outputs. And then we have a reward model or a Q learning model, technically, that will then look
*  at these outputs and choose the output that it thinks will be the best output. And so in that
*  setting, you have a normal back prop through this model, which is an open or white box model. It's
*  just a regular open source model that we're doing for the Q learning. And then you have the back
*  black box model and you don't need to propagate to the black box model because things upstream of
*  that are not that important. But anyway, this is, I think the strategy that we've been using most
*  successfully is this sort of hybrid Q learning where you have an open source model as sort of
*  the guide or the reward model for the closed source model, which is generating sort of the
*  arguments to the actions. And the Q learning one is sort of evaluating which one is the best given
*  the situation based on past experience. So how, I don't know if this is maybe still in
*  progress at the time we're talking, which is a little bit ahead of when the paper actually
*  comes out, but how on some of these like more frontier tasks, like, I don't know, you pick
*  which one you want, but you know, you've got high end tasks here, like, design me a new protein.
*  That's a little different from this old protein that'll have improved properties. How much
*  improvement are you seeing with these sort of end to end trainable agents?
*  Yeah. So it depends on the task. So we should see about maybe a five to 10 point improvement on the
*  paper QA task. So answering literature research questions, I think it's CQA, we should see pretty
*  high improvements, like maybe from 50 to 70. So like, sorry, 20 points, 50 to 70. And these kind
*  of reflect how formulaic the tasks are on the environments. And so in the paper QA environment,
*  we're basically trying to answer arbitrary questions and like basically take a multiple
*  choice task by cheating by looking at literature research. And yeah, the questions can obviously be
*  like anything, right? So like the question can be like, consider these five papers and tell me which
*  one was different. So the actions that are chosen are quite hard. So it's not surprising that we
*  don't really get a huge benefit. In the CQA, this is a molecular cloning task. We get a pretty large
*  benefit, like 20 points. And the reason why is the questions are quite formulaic. And so a Q learning
*  model will be able to outperform or doing iterative expert improvement can improve it a lot
*  because you're basically really doing a specific task with a set of actions. So they depends on the
*  environment. I think this gets back to like something of I don't know how useful these
*  training procedures will be in the long run. I think right now we felt like helpless before
*  we started this project. Like basically we can put in GPT-4.0 and we can do make an environment and
*  then, okay, it doesn't work. We try changing the prompt a little bit, throwing some in context
*  learning examples, we can change temperature, but there's really no way to gather more data and get
*  better. So having this environment at least gives us that ability to like see improvement from
*  rollouts, improvement from gathering data. But I don't know if this is the right answer. Like maybe
*  this is just a stepping stone on the way to some better response. Maybe, you know, maybe Mistral
*  will come out with an endpoint in a few months where you put up an environment and then they
*  will train their models on it as long as you give them a reward model. So it's unclear to me if this
*  is the right way, but at least we have sort of, you know, we've grabbed our destiny in our hands
*  and can actually train models in these environments and make progress. And so do I understand
*  correctly that the main driver of improvement is, this would be consistent with your philosophy of
*  spend what it takes to get good results. You are doing a lot of generations and the reward model
*  or the sort of the Q models you call it, essentially the one that is responsible for
*  discriminating between those generations and determining which one to actually go with.
*  That is the main driver of progress. Does that mean then that at runtime you have to do all the,
*  you still have to do, given a new question, you have to do a bunch of generations and you're
*  actually making a runtime choice? Yeah. No, I mean, like the Q learning model is just an open
*  source model. We use, we tried like five, we tried llama. I don't know which one we'll eventually
*  put into the paper, but that model basically is going to be tuned for the specific task,
*  but we still measure on like withheld questions. So if we go to like, when we evaluate performance,
*  we're going to new question types. And so it is, it should be generalizable within the domain of
*  using that environment for answering multiple choice questions. Now, if we were to take that
*  Q learning model and then have the task is now to write a literature review, that model is probably
*  not going to be great. And this comes to like this question of how engineered do you want these
*  agents and environments to be? And I don't know the answer to that question. I think it's an open
*  question, but it's one of these things where you have to be able to write down like 150 tasks or
*  500 tasks and the model can get good at doing those tasks, but tasks that are not on your list
*  of 500, it's unclear how well you'll do on them. Yeah. Okay. So not to get too lost in the weeds,
*  but just to be sure I understand the way the system works. Given a new question at runtime,
*  if I'm using a black box, if I'm using, you know, O one or whatever to do my core function of trying
*  to answer, do I have to do multiple generations and then have the Q one pick in order? Yeah. Yeah,
*  that's right. So usually these models, you can like pass in how many out, how many completions you
*  want. So you can do like exactly like K equals eight or something like that. So yeah, you have to,
*  it will generate eight of them. And then the Q learning model will decide which one to actually
*  admit to the environment. Cause you know, once you make a step in the environment, you can't go back.
*  So although we have experimented with tree search, so we actually have done tree search and this was
*  the strategy to get like ground truth or gold rollouts. Basically start with the black box model
*  in the setup. And instead of like having a Q learning model, pick one of the eight outcomes.
*  We try all eight, duplicate the environment eight time. And obviously, you know, you can't pick eight
*  cause it's too high a branching factor. You run out of space, but you can pick like a branching
*  factor of two or something, or maybe you can do like some sort of beam search and you can get very
*  deep. And we use that strategy to actually generate trajectories that had positive rewards
*  because in these tasks, sometimes you don't get any positive rewards if you just start with nothing.
*  And so we have used like this basically, I don't know, you call it money college research.
*  We basically go through these things by duplicating the environment until you get to a positive reward.
*  Yeah. Okay. Cool. I personally would love to see highly engineered systems have a big place in the
*  future. I don't know if you've ever encountered Eric Drexler's comprehensive AI systems manuscript,
*  but I do think there is something very attractive from a like big picture safety and control
*  standpoint to the idea that, you know, each of these things are kind of narrow. There's something
*  in here that like doesn't generalize well and therefore it's kind of up to us to like architect
*  the overall AI super system that's going to run a lot of society, but we hopefully will have like
*  legibility on all these little sub pieces. Yeah. I don't know if it goes that way though. I mean,
*  I kind of feel like O2 might just do it all and then we're back to the big black box. What is
*  your expectation for whether narrow has a place or, you know, especially if you're willing to
*  spend on the compute, if the, you know, the great generalists rule the day. You know, O2, I think
*  it's going to be really hard to run it on every task in the lab. I think it's going to be something
*  that is quite inaccessible to run at the scale. We use things like GPT-4 or even GPT-4. So because
*  of that, I think these kind of like systems like we're building where you can have some very like
*  good model, like generate a bunch of rollouts that are ground truth or very good, or it can generate
*  like a plan and then you have a simpler model execute the plan. I think that might be actually
*  sort of what has to happen eventually because I think we are going to reach a point where like
*  the models, I think we've gotten lucky right now that the inference is actually the price that it
*  is. I think we might start seeing this domain where basically there's very large expensive models
*  that have a lot of test time compute, a lot of inference time compute. And because of that,
*  they can be used to sort of help you train or sort of scaffold simpler models. So I think that may
*  actually come to pass, especially with the rumors in the valley. I don't know how you say this,
*  but like with the rumors in the valley, like I think that it's going to be unlikely we're seeing
*  the same sort of test time inference properties for the next models.
*  Yeah. You look at those graphs of performance over
*  inference time and the inference time scale is logarithmic. So that is another one of these nice
*  straight lines with the caveat that you're going through a lot of orders of magnitude
*  over the course of that graph. And that is not going to be... I've been very impressed by how
*  sort of egalitarian the developers have been when it comes to doing things like making GPT-4.0 free
*  and Cloud35 is also free and limited quantities for people to use. And just the fact that it's
*  sort of genuinely like money is not really a barrier, hasn't been a barrier to getting access
*  to the world's best AIs. There's been kind of Andy Warhol, like the president drinks Coke and
*  president uses chat GPT and you can use chat GPT. It does seem like that is about to break
*  with this new paradigm and it's probably going to break both across people, but also like
*  four individuals or four teams, you're going to have to like budget basically.
*  Yeah. I think you're right. I mean, and this is something we've experienced at Futurehouse,
*  but like with back to the conversation of paper QA, right? Like paper QA costs whatever a dollar
*  to use and takes whatever four minutes or three minutes to do it. And that changes how you think
*  about using these systems. And I think long-term, that's why I'm still excited about Futurehouse,
*  is that the kind of way that you can orchestrate these things where you can do like a thousand
*  things and each take four minutes and they each cost whatever 50 cents and you can pay $500 for
*  this like giant intellectual task. That's just like a very different way of thinking about how
*  we normally do things. And so I think the way that we automate science, it may not be the same kind
*  of science that humans do, but we may be automating like a sort of different branch of science.
*  So like some of the things we do here, like we run a combinatorial literature search. Let's look at
*  every antibody or every surface receptor against every disease ever reported in papers and this
*  tissue, right? And we can just go and do that sort of combinatorial literature search. Then we get
*  out like a matrix of findings and then we can do like some light machine learning on those findings.
*  And that kind of like task of like considering 10,000 papers or 20,000 papers at once is not
*  something a human is doing right now. So not really displacing kind of human science. We're
*  doing sort of a new category. So I do think it's going to require sort of a paradigm shift in how
*  we think about these models because we're not going to get to this sort of like, I think we're
*  to get a little bit farther away from maybe like the advanced mode we know on like chat GPT is like
*  you're going to get far with this sort of talking with a very low latency, very intelligent person
*  into these sort of more like engineered systems that are very high throughput, very like very low
*  or shallow intelligence distributed at scale or maybe one very high intelligence on a few of these
*  things. And then you do this big map reduce, look at lots of different areas and do some
*  simple intellectual task. Anyway, I don't know. I don't know what's going to happen. I'm very
*  happy that we've got Aviary out where we can actually train these systems complete. I think
*  there's been good work on training models. There's been good work on training prompts,
*  but to see like a complete system where you can go to arbitrary environments and have complex
*  agents and be able to train them, I think is very exciting for us. But see what the future holds.
*  Soterios Johnson Yeah, that's cool. Do you have any thoughts on kind of what you're looking out for
*  next? You know, things like I guess you could answer this in terms of like, what needles might
*  move? You know, I personally always look at novel hypothesis generation as like one big thing where
*  I think we really still haven't seen the tipping point quite hit. Mustafa from previously Inflection,
*  now Microsoft, was just talking about something that I do think would be maybe not so much for
*  your use cases, but in general, a huge game changer, which would be like effective long term memory
*  where the thing doesn't have the sort of brittle context window, but some sort of next paradigm
*  for memory. So just interested in general, like what are the sort of around the corner sorts of
*  things that think will be the biggest difference makers if and when they do land? Soterios Johnson
*  I think diversity and outputs. Have you seen Aiden's benchmark before?
*  Aiden? Soterios Johnson
*  Yeah. So this is like a benchmark, which is like basically they ask the model to generate like
*  explanations for, I don't know, like what caused World War II. And it's like, we generate a hundred
*  of these things and you'll find out that like, once you get past like four, it's just the restatement
*  with like different punctuation or different phrasing of the first four. And there's like this
*  really a big difficulty in these models is like, you would think that you could do, you could generate
*  a hundred hypotheses and have them explore all of them simultaneously. But in fact, what happens is
*  that they don't actually generate, you can't make them generate a hundred novel hypotheses. Although
*  you think you're doing it with like beam search or like top case sampling, what actually happens is
*  just changing the punctuation or the phrasing. And it's really only like one or two ideas.
*  And so I do think we have a problem with these models that they really can't generate a lot of
*  novel hypotheses and they can't really split their thinking that well to different viewpoints.
*  I think that holds us back in some setting because there's like sort of an upper limit to how many
*  ideas you can explore simultaneously. Another problem is just like, you know, like what you
*  said before, one thing I'm really watching, I don't know if there's a needle moving or someone
*  can build a needle for this, but how bots can interact with the internet. Like the internet
*  has gotten like quite different than what it was like 10 years ago. You can't just like curl the
*  web anymore. Most websites have bot, anti-bot stuff turned on. Most websites like are hostile,
*  like Reddit used to be a great source of training. Stack Overflow used to be a great source of
*  training. They're both now like hostile towards any sort of scraping effort. X changed to be
*  closed. X used to be like my favorite platform. Twitter is my favorite platform because everything
*  was written there was public, searchable, findable, citable, and it was like a public
*  discourse. Now it's kind of indistinguishable from Facebook in some sense that it's like closed off
*  Waldgarden, no bots allowed. Blue Sky was very excited about, but they've already been overwhelmed
*  by bots like posting there. And so I don't know what the future holds for them being like a savior
*  of like a protocol which is accessible by both LLMs or AIs or bots and people.
*  And so I think we're reaching this sort of, I don't know, like dead internet theory where A,
*  like the spots that are for people are being infiltrated by bots and then B, people who want
*  to make bots that just like do good things or do good work are like being stopped by other websites
*  because of the caught in the crossfire. So I don't know what happens next for that, but like we
*  already have a problem where like open access papers are already in a pretty sore state.
*  Like we've been slowly getting better in science of getting things open access, but already open
*  access papers are no longer accessible programmatically. And if you even do like license
*  agreement or sorry, terms of service uses to download a paper, it's not accessible anymore
*  or open access. And so I worry about like if we need to build something different than the internet
*  for like actually these systems interacting or need to build something different than, you know,
*  hosted PDFs, if we need to be more deliberate in how we think about building the world's model of
*  the next generation of AI systems. Claude just put out there all docs in one big text file,
*  and that feels like the first tenth of a percent of a step in that direction.
*  Yeah, yeah. I don't know. I keep thinking about this problem of like, yeah, like the Claude
*  like computer driver model. You can think about that. Or like I think MollMill was a great model
*  of like, how do you point and click at things? And you could use that to drive things over the
*  internet. But whatever, like 10 years ago, I'd be probably writing a Python or Perl script to just
*  go to websites and download the stuff. And I don't know, he's beautiful soup and just grab it. And
*  there was no like crap now. But nowadays you can't even get access to basic documentation now without
*  being hit by these anti-bot things. And I don't know, like I would pay money. Like if I could have
*  like a, if I could have a quarter and give every website I want to scrape a quarter and that offset
*  the cost of egress, then great. I would totally pay that. But man, it is getting really hard to
*  do anything kind of novel and fun on the internet these days. It's like a big commitment if you
*  really want to actually work on the internet with these systems.
*  Well, how about in closing, what is next for you guys at Future House? What are you looking for?
*  You can give the pitch for any profiles that you would like to have reach out to you.
*  Yeah, I think Aviary is a big step for us to have like a playbook to build these agents and
*  environments. So I'm really excited for us putting all these pieces together. I think we're going to
*  have some very cool demos of open ended science, which you have all these systems interacting.
*  I think if anybody has ideas for paper QA, we have this API, we work with people already on projects,
*  we have some really cool stuff going there, but love to hear from other people with their ideas.
*  Also, I think we're also open to people's ideas of strategy. There's been some great like
*  nonprofit tools that have been built, like Semantic Scholar came out of the outlandish
*  to for AI, and they actually struggle a little bit too about how to make an open free tool
*  available in an open source. Crossref is a nonprofit, they sell their services for a small
*  amount of money to companies. And so I don't think we figured out this way of like,
*  getting intellectual services out there in a nonprofit setting, and we want to and I don't
*  know how we deliver that. So I think we're still exploring that domain as well. So I don't know,
*  anyway, and we're also looking for great candidates, people who want to revolutionize
*  the field, people who want to be automating science, we're always looking for them. And we're
*  also looking for academic groups that want to try these things on their own ideas. Yeah, our goal
*  is to deliver novel discoveries. And that can be from us doing it, or us like getting every scientist
*  in the world using our tools to speed up literature search, or to speed up peer review, or to speed up
*  designing molecular cloning protocols. Yeah, cool. Offering those things as a service, I do think
*  sounds like a, obviously, a lot of infrastructure and a lot of maintenance love would have to go
*  into that. But it does seem like it could be a massive unlock. So I don't know if there's that
*  it feels to me like there's something there. Like that platform is one that I imagine a lot of people
*  would be really excited to build on. Yeah, yeah. Also, thanks for having me. This has been worth
*  the wait. Andrew White, co founder and head of science at future house. Thanks for being part
*  of the cognitive revolution. Thank you. It is both energizing and enlightening to hear why people
*  listen and learn what they value about the show. So please don't hesitate to reach out via email
*  at tcr at turpentine.co or you can DM me on the social media platform of your choice.

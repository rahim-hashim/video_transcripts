---
Date Generated: July 14, 2024
Transcription Model: whisper medium 20231117
Length: 6963s
Video Keywords: []
Video Views: 560
Video Rating: None
Video Description: Nathan interviews Mike Knoop, co-founder of Zapier and co-creator of the ARC Prize, about the $1 million competition for more efficient AI architectures. They discuss the ARC AGI benchmark, its implications for general intelligence, and the potential impact on AI safety. Nathan reflects on the challenges of intuitive problem-solving in AI and considers hybrid approaches to AGI development.

Apply to join over 400 founders and execs in the Turpentine Network: https://hmplogxqz0y.typeform.com/to/JCkphVqj

RECOMMENDED PODCAST:
Patrick McKenzie (@patio11) talks to experts who understand the complicated but not unknowable systems we rely on. You might be surprised at how quickly Patrick and his guests can put you in the top 1% of understanding for stock trading, tech hiring, and more.
Spotify: https://open.spotify.com/show/3Mos4VE3figVXleHDqfXOH
Apple: https://podcasts.apple.com/us/podcast/complex-systems-with-patrick-mckenzie-patio11/id1753399812

SPONSORS:
Oracle Cloud Infrastructure (OCI) is a single platform for your infrastructure, database, application development, and AI needs. OCI has four to eight times the bandwidth of other clouds; offers one consistent price, and nobody does data better than Oracle. If you want to do more and spend less, take a free test drive of OCI at https://oracle.com/cognitive

The Brave search API can be used to assemble a data set to train your AI models and help with retrieval augmentation at the time of inference. All while remaining affordable with developer first pricing, integrating the Brave search API into your workflow translates to more ethical data sourcing and more human representative data sets. Try the Brave search API for free for up to 2000 queries per month at https://bit.ly/BraveTCR

Omneky is an omnichannel creative generation platform that lets you launch hundreds of thousands of ad iterations that actually work customized across all platforms, with a click of a button. Omneky combines generative AI and real-time advertising data. Mention "Cog Rev" for 10% off https://www.omneky.com/

Head to Squad to access global engineering without the headache and at a fraction of the cost: head to https://choosesquad.com/ and mention “Turpentine” to skip the waitlist.

CHAPTERS:
(00:00:00) About the Show
(00:06:06) The ARC Benchmark
(00:09:34) Other Benchmarks
(00:10:58) Definition of AGI
(00:14:38) The rules of the contest
(00:18:16) ARC test set (Part 1)
(00:18:23) Sponsors: Oracle | Brave
(00:20:31) ARC test set (Part 2)
(00:22:50) Stair-stepping benchmarks
(00:26:17) ARC Prize
(00:28:34) The rules of the ARC Prize
(00:31:12) Compute costs (Part 1)
(00:34:47) Sponsors: Omneky | Squad
(00:36:34) Compute costs (Part 2)
(00:36:40) Compute Limit
(00:41:00) Public Leaderboard
(00:42:58) The current AI ecosystem
(00:47:23) The four steps of solving a puzzle
(00:51:20) Intuition
(00:54:32) Human Intelligence
(00:56:06) Current Frontier Language Models
(00:57:44) Program Synthesis
(01:04:10) Is the model learning or memorizing?
(01:09:51) Improving the ARC dataset
(01:11:34) Step 3: Guessing the Rule
(01:12:51) Dealing with Ambiguity
(01:15:02) Exploring Solutions
(01:17:02) Non-backpropagation evolutionary architecture search
(01:19:49) Expectations for an AGI world
(01:24:11) Reliability and out of domain generalization
(01:28:35) What a person would do
(01:29:51) What is the right generalization
(01:35:32) The ARC AGI Challenge
(01:37:01) Postscript
(01:38:07) DSpi
(01:39:55) Statespace models
(01:43:28) Hybrid models
(01:48:32) FunSearch
(01:50:41) Kolmogorov-Arnold-Networks
(01:54:18) Grokking
(01:55:42) Outro
---

# The ARC Prize: Efficiency, Intuition, and AGI, with Mike Knoop, co-founder of Zapier
**Cognitive Revolution:** [July 13, 2024](https://www.youtube.com/watch?v=XECXoS-D6kQ)
*  Hello and welcome to the Cognitive Revolution, where we interview visionary researchers,
*  entrepreneurs, and builders working on the frontier of artificial intelligence.
*  Each week we'll explore their revolutionary ideas and together we'll build a picture of
*  how AI technology will transform work, life, and society in the coming years.
*  I'm Nathan Labenz, joined by my co-host Eric Torenberg.
*  Hello and welcome back to the Cognitive Revolution. Today my guest is Mike Knoup,
*  co-founder of Zapier and co-creator of the ARC Prize, the recently announced $1 million
*  public competition that's meant to motivate research into more sample-efficient and
*  generalizable AI architectures, and which includes a $500,000 grand prize for systems that can solve
*  the ARC AGI benchmark at a human level under strict compute and time constraints.
*  If you've been living under an AI rock, ARC stands for Abstraction and Reasoning Corpus.
*  It's a benchmark created by Francois Chalet in 2019 as a test of general intelligence.
*  The test presents input and output pairs of two-dimensional grids which demonstrate a
*  specific transformation, plus a final input grid to be solved. The solver must first infer the
*  rule being used to make the transformations, which is different in every puzzle, and then apply the
*  rule to transform the final input into the correct output. Importantly, the test set is
*  kept private to prevent systems from simply memorizing solutions, but you can see samples
*  and solve a few for yourself at ARCPrize.org. There's been a ton of discussion surrounding the
*  ARC benchmark since the prize was launched, and I can specifically recommend recent machine learning
*  street talk episodes as a great source of information on the techniques that currently
*  top the leaderboard. Having listened to those and read lots more besides, I have to say that I'm
*  still not quite sure what to make of the whole debate. On the one hand, I have to respectfully
*  disagree with Mike Francois and anyone else who says that progress toward AGI has stalled.
*  As someone who has used large language models intensively for the last three years,
*  for all sorts of practical projects, I feel like the progress in reasoning and problem solving,
*  while certainly incomplete, is ultimately unmistakable. At the same time, the degree
*  to which even the very best multimodal models like GPT-40 and Cod3.5 Sonnet still struggle with ARC
*  puzzles does seem important, and I would agree that any AGI worthy of the title would need to
*  be able to do a better job on archetype problems. When I solve these puzzles for myself, a subconscious,
*  deeper-than-language sort of intuition seems to be doing most of the work. I stare at them for a bit,
*  suddenly I have a sort of eureka moment where I know what the rule is, and then things become
*  relatively easy for me from there. Current AI systems are definitely not nearly as good as
*  humans when it comes to such intuitive insights, and this really does matter, not only for ARC
*  puzzles, but for the possibility of, for example, an AI scientist, which would need to come up with
*  novel hypotheses that are sufficiently insight-driven as to be worthy of testing in the real world.
*  To date, we've seen precious few sparks of that kind of insight coming from language models,
*  and while that might emerge at higher scale, I certainly can't guarantee that it will,
*  and in any case, a new technique that solves ARC within the rules of the contest
*  would definitely constitute a notable step on the path to AGI. Interestingly, at one point,
*  Mike suggested that such stringent efficiency requirements imposed by nature might have given
*  rise to intelligence in the first place, as organisms that were able to make good decisions
*  based on very limited local evidence would naturally have the best chance of survival.
*  That framing does make me wonder, though, if a breakthrough architecture that solves ARC
*  might prove unwieldy from an AI safety perspective. Before language models stole the spotlight,
*  AI safety theorists anticipated small but highly capable systems and worried that while they might
*  solve problems effectively, they wouldn't understand human values well enough to know when to stop.
*  This is the origin of the paperclip Maximizer thought experiment.
*  If we imagine now a new system that can solve ARC puzzles with just one cent worth of compute,
*  I would have to guess that it would not have room for the sort of understanding of values and ethics
*  that we see from the likes of Claude today. And so I think one can reasonably worry about what
*  might happen if such an architecture ever gets to the point where it can pursue open-ended goals.
*  After wrapping up the conversation with Mike, I stayed on by myself for a brief postscript
*  in which I offer a run-through of a number of recent research results that I would draw
*  inspiration from if I were to try to tackle ARC myself. On reflection, I tentatively hope that a
*  hybrid system combining a language model-like component that does understand human values
*  with more algorithmic search and reasoning modules turns out to be the winning approach.
*  Such an ensemble of different subsystems would be consistent with how humans are structured,
*  and my feeling right now is that nesting powerful problem solvers within more holistic systems
*  might be a promising way to improve practical utility and reliability while also keeping
*  general purpose systems under control. That would not conform to the contest rules and
*  wouldn't be eligible for a prize, and some might still object that it's still just brute forcing
*  the solution. But if it's fast and cheap enough to compete economically with humans,
*  I don't think that distinction will matter much in practice.
*  AI systems are often quite alien, and for the purpose of transforming daily life,
*  a functional general intelligence does not need to satisfy our intuitions or preferences
*  about how intelligence ought to work. Of course, I do not claim to have all the answers,
*  and I expect to continue to be surprised by AI developments. In the meantime, I can confidently
*  say that it is an awesome accomplishment to have created a benchmark that's remained unsolved for
*  more than five years, and all of us should really applaud successful entrepreneurs like Mike for
*  putting their money where their mouth is to try to encourage high-impact research. As always,
*  we appreciate it when listeners share the show. We welcome your feedback, and I look forward to
*  reading your resume if you're looking for a new role as an AI advisor or engineer. You can find
*  the link to submit on our website, cognitiverevolution.ai. Now, without further ado,
*  here's my thought-provoking discussion on the Arc AGI benchmark, the Arc prize, and the future
*  of artificial general intelligence with Mike Canoop. Mike Canoop, co-founder of Zapier and
*  co-creator of the Arc AGI prize, welcome to the Cognitive Revolution. Thank you for having me,
*  Nate. I'm excited to get in today. Yeah, me too. You guys have done something that is not easy to
*  do in today's world, and that is capture the attention of AI discourse and get it focused on
*  a topic with so many things going on that is, in and of itself, quite a feat. So what I'm hoping
*  to do today is just dig into a little bit of the background of the benchmark, how you got
*  interested in it, get into the rules of the contest, and then hopefully spend the majority
*  of our time brainstorming some possible- How we're going to solve this. That's why we're
*  all here, isn't it? We want to beat the benchmark. Yeah, and you've graciously put up a million bucks
*  to people who either do it or come close in various ways, so we can get into that as well.
*  I guess, first of all, another not easy thing to do is create a benchmark that stands the test of
*  really any significant time in AI, given how quickly things are moving. When did you become
*  aware of and interested in, I imagine with increasing obsession, the Arc challenge?
*  Yeah, the sort of cliff notes here are, I co-founded Zapier. I was running all of our
*  product engineering up until about mid-year through 2022, and I gave it all up to go back and just be
*  an AI researcher at Zapier that year. The chain of thought paper that came out that January was
*  one that really shook me off track of what I was doing, and I got really deeply curious about,
*  are we on track for AGI or not? I felt like it was really important to know for Zapier's business
*  and our customers as well as just as a human. I wanted to know. I think I first got exposed to
*  Francois's research all the way back during COVID. He did a pod with Alex Friedman, and I think
*  that's where I first heard him talk about his paper on measure of intelligence and the Arc
*  benchmark. I thought it was curiosity. It kind of resonated with some long-term AI ideas that I'd
*  been thinking about since college, but they had other sort of things I was working on with Zapier
*  at the time. As I got more into AI research as an individual contributor and an engineer and
*  starting to build the stuff at Zapier, I got really into AI benchmarks. It turns out benchmarks are
*  really, really important for defining and guiding the quality of your systems you're building.
*  Globally, one interesting thing about benchmarks that I found when I was digging in there was all
*  these AI benchmarks we have are basically saturating up to human level performance.
*  In fact, it's been happening faster and faster as time has gone on,
*  specifically as these live-travel models have scaled up or are meeting human performance
*  and benchmarks faster. At some point, I went back and looked at Arc, the abstraction reasoning
*  corporates that my co-creator of ArcPrize Francois created, and I saw the opposite. It was actually
*  slowing down on progress. It had been decelerating actually over the last four years since it got
*  introduced in 2019. That's what led me to get, oh, okay, that's what I expected. I dig in way more.
*  What I found was, or believed to have found is, I think that's not an accident. That is a very
*  special important benchmark relative to all the other AI benchmarks. I think it's, at this point,
*  we're four weeks into the competition now with the bigger prize pool, and no one has come forward
*  yet and said, hey, I think I've got a better AGI benchmark that exists, or even an AGI benchmark
*  that exists. I think Arc is perhaps still the only AGI benchmark that exists in the entire world that
*  was singularly designed to measure AGI and separate it from AI. I think the fact that that's true,
*  and the fact that we haven't beaten it yet, in fact, progress has been slowing down, is what led me to
*  get involved in Pitchfrancois and try to blow up the prize pool and try and grow awareness on
*  the benchmark. Are there any other things that are like this that are maybe not so
*  AGI-flavored? By the way, I have a very similar story, albeit with a less well-known company,
*  but I had been background interested in AI for a long time. It was the second half of 2022 also,
*  where I was like, you know what? I just want to focus on AI all the time now. I was very fortunate
*  that I had a teammate who could take over running the business, so parallel timing on that.
*  One other thing that I've seen that I wouldn't say is so relevant perhaps, but it is an interesting
*  data point, is also aesthetic evaluation of images, which was something that we really
*  valued more than most. We found that there was a particular data set that had been created,
*  and you go and look on the leaderboards. I'm like, what is it? Open papers or whatever?
*  It was not going very far, and we were really struggling to figure out how do we do aesthetic
*  evaluation of images. Interestingly for us, that has largely been solved with the latest large
*  language models that are now obviously multimodal, and we can just ask, does this look like a good
*  image to use for this particular business? We get pretty good answers. I guess anything else that
*  you see out there that's even in the same ballpark as this, where it's progress is not making...
*  Well, there are certainly benchmarks that exist that have not been beaten yet. ARK is not obviously
*  the only benchmark that exists that has low score. Sweet Bench, for example, is another one that I'm
*  aware of that has a very, very low state of the ARK score. I think what's unique about ARK is that
*  it was built off of a definition first. As I got into this, are we on track for AGI,
*  curiosity or not question, the first thing I found was that there's two big schools of thought that
*  I see existing today in public discourse or in AI on how to define what AGI is. The first school
*  of thought is actually, I'll know when I see it, it's undefinable. We shouldn't really even bother
*  trying. We're already just on tracks. We don't have to worry about it. And then the other school
*  of thought is got popularized by OpenAI. It's this definition that AGI is a system that can
*  outperform humans at the majority of economically useful work. And this is actually literally written
*  into the terms of the agreement between OpenAI and Microsoft, by the way, because... Underappreciated
*  fact. Yeah. If they achieve that, Microsoft doesn't get any more IP ownership of future
*  systems that they develop. So it's actually kind of interesting. I think COSA might get first credit
*  for defining that one, but certainly due to the success of OpenAI, I think this has become
*  quite an accepted definition of what AGI is. And I don't think it's a bad goal to shoot for. I
*  actually think it's quite a good goal. I think narrow AI that we already have today can accomplish
*  that goal. And I think that's why it's actually not a very good definition, because it doesn't
*  drive us towards what we really need and want, which is the generality, the AGI aspect of this.
*  So to jump to the conclusion here, I think the right definition of AGI is one that she'll
*  later find back in 2019 in this paper, which is AGI is a system that can efficiently acquire
*  skill and apply it. And the skill acquisition efficiency is the hallmark of what general
*  intelligence is. And maybe here's a quick qualitative thought experiment to help kind
*  of make it concrete. So we've had narrow AI systems for many years now, five plus years,
*  that can outperform humans at games like poker, Go, chess, even self-driving cars now in some cases,
*  other more complex games with language like diplomacy. And you might look at that history
*  and say, okay, well, that's generalizing, we're being more and more of these games.
*  But the reality is that the way that we're getting these systems to outperform humans at those
*  individual games is the researchers and engineers have to start over from zero. They have to
*  completely invent like, okay, new search algorithms, go acquire new sources of training data, go reach
*  new levels of scale in order to solve it, bring new ideas into the fold. And yet, you know, I could
*  sit down with you, I could teach you a new card game, you know, get you up to human level
*  proficiency pretty quick. I could teach you a new board game and get you up to human level
*  proficiency pretty quickly in just probably a few hours, merely just by exposing you to like
*  new experience, right? You trained you. And so I think that is the hallmark. And this shows that
*  just narrow skill is not a hallmark of intelligence. That can simply be achieved through memorization.
*  Instead, it's your ability as a human to rapidly and efficiently acquire
*  new skill and apply it to things that you've never done before. That's what the hallmark of
*  generality is. And that's the facet of AGI that has been stalling out on progress over the last
*  three or four years. We've gotten very, very good at building narrow AI systems and targeting them
*  towards specific tasks and outperforming humans in those. No one in the world knows how to build a
*  system that can, with the same level of human efficiency, go acquire new skill in a domain or
*  a task that's never been exposed to before and solve that. And that insight is what ARK is built
*  on top of. So that conceptual framework and grounding is how ARK got created. It's not just
*  like a random benchmark that happened to be good or happened to be hard, it actually had like a
*  conceptual underpinning. And the fact that we have Empirical 11 that's now four years in, that it's
*  unbeaten, progress has been slowing down, there's a really strong conceptual framework underlying it,
*  is what leads me to believe that we really truly have stalled out in progress towards the generality
*  aspect of these AI systems today. There's some fascinating philosophical questions there that I
*  want to maybe come back to in a minute. Before we do that, and maybe to motivate it as well,
*  let's just talk about the rules of the contest. Because I think the concrete rules maybe inform
*  certain aspects of how different people are thinking about what would constitute an AGI.
*  So I just noted these down, I'll say some to you. You can comment on them or expand on them or
*  correct me if I get anything wrong. Maybe we should talk about what, if people haven't seen what the
*  tasks actually look like, that actually might be a good thing to start with. I honestly assume that
*  most people, if you're listening to the Cognitive Revolution, have heard these puzzles. You can
*  play with six examples that are on the homepage at ARKprize.org and get a feel for them. The idea is
*  that they look like IQ puzzles. And what I like to think about the puzzles is that they're sort of
*  a minimal reproduction of what general intelligence is. The key insight of how all the ARK tasks are
*  designed is every single task is novel. It should be something that you have never seen before. It
*  should be something that an AI system that you've built to try and beat the task has never seen
*  before. That's one of the reasons why ARK as a dataset has a public dataset that folks use for
*  training and designing their systems. And then there's a private dataset, which is what the
*  competition is run against. Very few humans have ever seen the private dataset. And that
*  increases the level of confidence that if someone shows up and says, Hey, I've got a system that can
*  beat ARK at the 85% mark, which is where we set the grand prize at, that increases our confidence
*  that that's a good solution. That that's actually something that is generalized and solve these
*  tasks that it never got exposed to. It never got to train on the answer. It never got to train on
*  code where other humans are writing code that tried to solve similar looking puzzles. If ARK continues
*  to endure, I think it would be because of that fact that every single task is novel in the task
*  set. And you don't need world knowledge. You don't need language necessarily to solve these
*  puzzles. They're instead grounded on about seven or eight core knowledge priors, things like
*  objectness, goal directness, symmetry, rotation, masking, things that kids develop very, very early
*  on in childhood development. They acquire these core skills and that's all you need in order to
*  beat the benchmark or beat an individual task. And I think that's one of the reasons why ARK tends
*  to be very straightforward for humans, but evidence shows no AI system can.
*  Yeah, it's really fascinating. I guess I had two questions there. One is the way that they're posed
*  from what I saw when I looked at downloading the data set is just as 2D arrays of numbers with
*  a zero through nine in each place, right? And then the images that are presented on the website,
*  those are not part of the core data set, but are just a visual presentation. Is that true?
*  Yeah, that's right. Many people have built viewers to view the different puzzles. The data formats,
*  just like a JSON file, defines all your task demonstrations. So you get an input example and
*  an output example. You get usually several of those per puzzle. And then you get a test input
*  JSON array of a matrix of zero to nine. Your job is to write a program that can generate what is
*  the right output given that test that matches the pattern that's shown in the input demonstrations.
*  That's even assuming a little bit of the approach, right? Because your test is really just to
*  provide the output, right? Yeah, I directly get the output. One interesting thing is the numbers
*  are arbitrary. Or I should say the colors are arbitrary. So this is maybe one thing I've seen
*  some people get stepped on is like, oh, maybe the colors mean something in some of the puzzles.
*  They do not. There's no special nature assigned to any of the colors that are on it. It's purely
*  like you could swap out a different palette and all the puzzles would be just as solvable as they
*  are with any other color palette. I think zero representing black might be a special case in
*  some puzzles, but generally like still humans should be able to deal with that fact and still
*  solve it. So the color choice of the palette is completely arbitrary. And instead the numbers are
*  more symbols to represent different things in each square. Hey, we'll continue our interview in a
*  moment after a word from our sponsors. AI might be the most important new computer technology ever.
*  It's storming every industry and literally billions of dollars are being invested. So buckle up.
*  The problem is that AI needs a lot of speed and processing power. So how do you compete
*  without costs spiraling out of control? It's time to upgrade to the next generation of the cloud,
*  Oracle Cloud Infrastructure or OCI. OCI is a single platform for your infrastructure, database,
*  application development, and AI needs. OCI has four to eight times the bandwidth of other clouds,
*  offers one consistent price instead of variable regional pricing. And of course, nobody does data
*  better than Oracle. So now you can train your AI models at twice the speed and less than half the
*  cost of other clouds. If you want to do more and spend less like Uber, 8x8 and Databricks Mosaic,
*  take a free test drive of OCI at oracle.com slash cognitive. That's oracle.com slash cognitive,
*  oracle.com slash cognitive. The Brave Search API brings affordable developer access to the
*  Brave Search index, an independent index of the web with over 20 billion web pages.
*  So what makes the Brave Search index stand out? One, it's entirely independent and built from
*  scratch. That means no big tech biases or extortionate prices. Two, it's built on real
*  page visits from actual humans collected anonymously, of course, which filters out tons of junk data.
*  And three, the index is refreshed with tens of millions of pages daily. So it always has accurate
*  up to date information. The Brave Search API can be used to assemble a data set to train your AI
*  models and help with retrieval augmentation at the time of inference, all while remaining
*  affordable with developer first pricing. Integrating the Brave Search API into your
*  workflow translates to more ethical data sourcing and more human representative data sets.
*  Try the Brave Search API for free for up to 2000 queries per month at brave.com slash API.
*  Was the test data set originally created five years ago and kept private this whole time,
*  or was this sort of an expansion of the data set now to create this private test set?
*  The direct answer to your question is that the 2024 contest is using the exact same
*  private data set that Francois created back in 2019. And that was the same data set that got
*  used in 2020, 2022, 2023. Cool. That's definitely a lot of foresight to keep that private. I mean,
*  I think it would become a big trend in general. We're starting to see that with like scale's recent
*  seal benchmark where they're not publishing the test questions. So that's definitely a
*  head of the science as well. There's like two really interesting things here. Maybe
*  it's time. One would be kind of like the landscape of benchmarks that exist. I'm seeing like a handful
*  of different categories of benchmarks that exist. And that could be interesting to describe.
*  Then other thing I'll say on Arc real quick is that it is not a perfect benchmark. Like we know
*  that there are deficiencies in how it got created. I don't think anyone, Francois certainly envisioned
*  that it would be enduring as quite as long as it did. And he did as best as he could with the
*  resources he had available to him five years ago. For example, during the 2020 competition,
*  after that one wrapped up, some folks did some analysis to look at what percentage of all of
*  the puzzles, if you were to kind of like assemble all the solutions could be solvable by brute force.
*  And the state of the art in 2020 was only about 20%, I think was the end of their first result.
*  But if you ensemble all the solutions together, just merely using brute force, in fact, AI
*  models were not even really a technique that got used in the first competition. You could solve
*  upwards of 40%, 50% of the puzzles purely through brute force search. So we know that like the
*  benchmark is not perfect. The hope is that there's like enough remaining novelty in the rest of the
*  set that actually is illustrative and points the right way towards AGI. And so far, that's like
*  very true over the last three or four years. It's kind of interesting to see that like,
*  in some respects, like stated on the private data set today on Kaggle is still only 39%.
*  So it's interesting to see that these more AI model based approaches are kind of in some respects,
*  just catching up to what brute force search could possibly do. But we know in order to get to 85%,
*  we're going to need something much further beyond brute force, just because of this like
*  combinatorial explosion problem that starts happening with the minimum description length
*  that's necessary to solve a lot of the different puzzles. So we know the benchmark's not perfect,
*  despite the fact that it's endured for four years. And one of the things we want to do is
*  continue to make improvements in the benchmark. Now, we won't do that during the contest period,
*  but this is something we're hoping to do during the downtime between, you know, the annual contests is
*  to try and improve ARC to make it the best strongest like measure of AGI that we can. And I think like
*  one maybe interesting thing I've heard Francois talk about is like, we really want to stair step
*  our benchmarks alongside our like our system strength. So as we start to discover more and
*  more general AI systems, we're going to want to increase the sort of novelty and the generality
*  that exists in your benchmarks. And you kind of need to like stair step them up alongside each
*  other. We're actually using the generality of the system you've made to design better and stronger
*  benchmarks. Right now, all of the ARC tests are generated by hand. Francois designed all of the
*  initial test set. Now there's some crowd sourcing that's gone into more of the latest data sets.
*  But everything one of them is generated still by a human. It's hand verified, still by human to
*  make sure that they're solvable. But I would expect as we make more progress towards AGI,
*  in order to make stronger benchmarks, we're going to have to use some of our weak AGI
*  like systems in order to like design better benchmarks. So I expect that's kind of going
*  to be the future of how the ARC challenge like kind of evolves as we go forward. For the time
*  being with the regime we're in, we're going to have to just keep having humans design the puzzles
*  and adding more novelty, looking at the puzzles that have the most degree of novelty and trying to
*  make sure that more and more of the data set is representative of types of puzzles that can't be
*  just solved via brute force search. And then as time goes on, as we get weaker AGI system starting
*  to emerge using those systems directly to make the challenge itself, make it stronger and the best
*  can measure if AGI that we can. Crazy times ahead, no doubt. When we get the proto AGI's developing
*  the AGI benchmarks, that's when we'll know we're really in some sort of takeoff situation. There's
*  like this interesting world of like benchmarks that's kind of emerging, right? Maybe I'd call
*  like three big categories. You've got private benchmarks. These are things that like Zapier,
*  for example, has in-house, right? We're building private data sets of our own usage data in order
*  to make sure that our products that are using AI are actually really good for our customers. These
*  are narrow. It's not a general form benchmarks or whenever we're going to publish it, but it's very
*  useful for us for benchmarking the quality of our systems. Then you've got this category that's on
*  LMSS, right? The sort of ELO scores where they're pitting multiple AI systems against each other
*  and having a human evaluator say which one's better. And I think this maybe gets to your idea
*  that you were talking about a few minutes ago of using human aesthetic criteria to decide the
*  quality of the system where you're using the generality of the human to make a decision about
*  which system is sort of better or not. And then I think the last category is, I think we're going
*  to see more stuff like ARK. The SEALs benchmarked from scales. They're doing it kind of in the spirit
*  of something very similar where they're only allowing the biggest models like one shot at the
*  benchmark in order to try and eliminate the risk of overfitting. They're trying to do things where
*  the tasks are sort of sight unseen before they get exposed to it to try and be a proxy for the
*  novelty of the task and be a better measure of generality. And so I think we're going to see more
*  and more benchmarks taking that form where the tasks themselves are novel and they're kept private
*  or at least attempted to keep private in order to increase confidence in the reported benchmark
*  and reduce sort of overfitting and the contamination that can otherwise happen.
*  Yeah, that seems very smart. I mean, I don't know how else with so many people training so many
*  models and so many data sets flying around and people training on GPT-4 outputs and all that
*  kind of stuff, it's like there does need to be some sanity brought to this. And I think the
*  private test set definitely was remarkably forward thinking approach.
*  So we launched DarkPrize four weeks ago and one of the first people who really put a lot of effort
*  into on the public data set is a new leaderboard that we launched. The private competition is where
*  the big grand prize is and we have a public leaderboard that folks can use that allows
*  usage of like internet access and frontier models. And this guy Ryan Greenblatt worked on using GPT-4.0
*  to sample thousands and thousands of Python programs out of 4.0 being fed in the images and
*  asked for representation of the puzzle and then searching over programs that are generated in
*  order to find ones that match the sort of the pattern of the test demonstrations and applying it.
*  And this has been like a really fascinating approach that is I guess working. His solution
*  is on the top of the public leaderboard. He's getting like 42%. And there is a risk that his
*  solution you could maybe claim or make the argument that like, oh, because GPT-4.0 is training on the
*  ARC data set that's directly in GitHub that it somehow has some sort of advantage because of the
*  public data set. It's getting contaminated. I actually don't buy that story. I think the
*  more likely situation of what's happening here and the reason why things like 4.0 language models
*  are able to get such high performance on with this like program sampling approach is for many years
*  now, people have been trying to beat ARC public puzzles by writing code to do it. They've been
*  creating DSLs. They've been writing code to solve each individual puzzle. And then they're putting
*  that code on the internet. And so that code is what's getting into the training data for
*  these large language models. And I think when you're using an LM to like sample solutions to
*  potential ARC puzzles, it's getting access to programs that like other humans have sort of
*  written in the past. That's my best belief about like maybe where there might be some degree of
*  overfitting or sort of contamination leaking in. But there is still something important about the
*  approaches that folks like Ryan are coming up with because they do have very good agreement from a
*  score perspective with the new semi-private data set that we made. And the fact that he's only
*  sampling maybe 2000 reasoning traces per puzzle. Whereas if you were to go back to 2020 and look
*  at like how many reasoning traces they had to generate for the brute force, it was like,
*  you know, tens of thousands, hundreds of thousands. So there is something cool about how using these
*  language models as kind of a perception engine to direct and guide a program search seems to be
*  working. There is something that is special and really novel and interesting there.
*  Yeah, absolutely. That's kind of where my head goes to immediately when as somebody who,
*  you know, has again had this sort of long-standing general curiosity about AI, but has really
*  gotten into it full force the last few years, like naturally, the language model wave of technology
*  is kind of where my head immediately goes to. Let's do the rules for a second. And then we can
*  kind of contrast like what those rules would require against what somebody like Ryan has
*  managed to make happen and then create maybe some other possible techniques or approaches as well.
*  So there are a hundred private puzzles. These are the ones that nobody has seen outside of presumably
*  the organizers. There are very few humans. We've had all of an important thing to note about the
*  hundred private puzzles is they have all been hand verified. We've had a couple of humans who are
*  adults who have taken every single one to verify that they're like error-free, they're solvable by
*  humans. So I think that's just one important note on the private data side. Even though very few
*  people have seen them, they're all solvable by humans. Cool. So to win the $500,000 grand prize,
*  you have to submit to Kaggle where the contest is being hosted a solution that can get 85% right
*  by November 10th. You have to do this in a way where you're willing to open source the solution
*  that you create. You can use pre-trained models and licensed software if you have an appropriate
*  license, right? But no internet, which means no APIs to today's leading frontier models.
*  Then I think maybe one of the more interesting things that I was trying to analyze is the actual
*  amount of compute time that you have. So you get a P100 for 12 hours of runtime. I looked online.
*  I didn't know off the top of my head the specs of a P100, but it's going for about $300 bucks
*  on Amazon today. The wattage is 250 watts. So just thinking, okay, that's 720 P100 minutes. That's
*  like three kilowatt hours total. So amortizing costs and trying to back into it, it basically
*  comes out to something like $1 worth of compute. Would you say that's a reasonable estimate?
*  Yeah. If you go from my first principles and you were like on your hardware, I think if you go to
*  spot pricing or like on-demand pricing, when I was looking at like 20 or 30 bucks, probably for the
*  12 hours that you could get, either way, this is like donated from Kaggle, right? We can talk more
*  about why the limit exists. I think there actually is some important things behind that. But yeah,
*  I think that's like about how much, like if you were just going to go try to put that on the open
*  market. Yeah, I was figuring by one and plan to use it over two years and then just figure in the
*  cost of electricity, I got you about a dollar. So another way to look at that is you have 7.2
*  minutes per problem for each of the 100 problems. That would be also like roughly one cent of compute
*  with my analysis, maybe higher price point if you're buying in the open cloud market, whatever.
*  Yep. I think you can, I'm not sure if you would have better clarity than I on what models would
*  fit and be able to run there and like what kind of tokens per second you would get. One way I tried
*  to triangulate that was just looking at prices from like Fireworks AI on what their
*  inference costs for Lama 3 8B are. Those are roughly 20 cents per million tokens. So if I said,
*  okay, well, what's one cent by me? That would be roughly 50,000 tokens out of their commercial
*  infrastructure. I would think a Lama, like an 8B model will fit, right? Because if I understand
*  correctly, it's 16 gigabytes of RAM that the PE- I think that's right. I just Googled that.
*  Unless I got something wrong in my process. I think that's on, we listed all the techniques
*  just on our price website, but I'm pretty sure that's right. So you should be able to get an
*  8B model in there, but like not too much bigger than that. And do you have any idea what sort of
*  token rates you'd be able to generate? Off a Lama 8B? Yeah. If you had it, you know,
*  there was something in that general spirit on the- Hey, I don't know that I've seen you in
*  publish. So this is actually one of the interesting things we're trying to do with ArchPrize is over
*  the last four years, it has not been a requirement to share your code or approach. So the information
*  that we have from past contestants is pretty limited. Just to kind of narrow in on the rules,
*  specifically one of the things we're going to have requires in order to claim any of the price
*  money. So whether it's the progress prize that we've set aside for this year or the grand prize,
*  if someone achieves 85%, in order to claim that you have to commit to publishing your solution
*  into a public domain, open source in your code effectively under like a public domain license.
*  And our sort of anticipation is that it's going to take multiple years to beat Arch. This is not
*  going to get solved this year. It's going to take multiple years. And then we're hoping to
*  use the annual contest window as a stair step function to sort of re-baseline the community
*  at the end of every year with a bunch of new open source code and approaches that folks can look at
*  to see how are other people doing it? What are the approaches they're getting at? So the one that I
*  do know about, I don't know about the Lama 3B on a P100. Somebody have to go try it. I do know that
*  the state art with Jack Cole, who's getting 39% on the private leaderboard, is using, I think a
*  Salesforce, like, CodeGen T5 model or something like that. And they're doing something really
*  interesting where they're doing test time fine tuning. That T5 model is a 220 million parameter
*  model. It's a very small model. I think they've experimented with some bigger ones, but they're
*  getting really good state art performance off of a relatively very small model. And I think they had
*  to do a very small model like that in order to work with this test time fine tuning, where they
*  do some pre-training as well. And that maybe got a couple of percentage points, but the main insight
*  that they're doing is at runtime, they're generating new puzzles and response to the
*  puzzles that they're showing at test time and then doing fine tuning on their model and then
*  directly prompting it, which I think is quite cool. It leads me to believe that we're probably
*  likely to solve ARC with a 7B model and 10,000 lines of code. Would be my best guess today if
*  you kind of forced me to make a bet on how much compute, how big of a system do we need in order
*  to get to the 85% mark. Hey, we'll continue our interview in a moment after a word from
*  our sponsors. Omnike uses generative AI to enable you to launch hundreds of thousands of
*  ad iterations that actually work customized across all platforms with a click of a button.
*  I believe in Omnike so much that I invested in it and I recommend you use it too. Use Cogrev to
*  get a 10% discount. Hey all, Eric Torenberg here. I'm hearing more and more that founders want to
*  get profitable and do more with less, especially with engineering. Listen, I love your 30-year-old
*  ex-Fang senior software engineer as much as the next guy, but honestly, I can't afford them anymore.
*  Founders everywhere are trying to turn to global talent, but boy is it a hassle to do at scale,
*  from sourcing to interviewing to on-the-ground operations and management. That's why I teamed
*  up with Sean Lanahan, who's been building engineering teams in Vietnam at a very high
*  level for over five years to help you access global engineering without the headache.
*  SQUA, Sean's new company, takes care of sourcing, legal compliance, and local HR for global talent
*  so you don't have to. With teams across Asia and South America, we can cover you no matter which
*  time zone you operate in. Their engineers follow your process and use your tools. They work with
*  React, Next.js, or your favorite front-end frameworks. And on the back end, they're experts at Node,
*  Python, Java, and anything under the sun. Full disclosure, it's going to cost more than the
*  random person you found on Upwork that's doing two hours of work per week but billing you for 40.
*  But you'll get premium quality at a fraction of the typical cost. Our engineers are vetted
*  top 1% talent and actually working hard for you every day. Increase your velocity without
*  amping up burn. Head to choose SQUA.com and mention Turpentine to skip the wait list.
*  So that was one of my other questions. You are able to, like in that 12 hours of runtime,
*  basically anything goes. You can even fine tune on the private data set. I suppose that's what
*  they're doing. You can do anything you want, right? The no internet is the main limitation,
*  which doesn't allow you to use frontier pre-trained models or outsource your compute to an API provider.
*  Maybe there's like two conceptual things to talk about here on the compute no internet.
*  So it's either both been pretty loud points of feedback, critique, comments that we've seen
*  over the last month or so since we launched DarkPrize. And let me address the compute one
*  first since we've been spending more time on it. The compute is a important benchmark for efficiency.
*  If we come back to Francois's definition of AGI, a system that can efficiently acquire new skill,
*  if efficiency was not part of the definition, this would mean that general intelligence was merely
*  like a brute force search. And yet, like we know that's not the case. Francois formalizes this in
*  his paper, which you can read in the film that's 2019, or maybe using a quick methodic experiment.
*  If you go take the art puzzles yourself and just look at the ones that are on the homepage
*  and try to introspect, how did I figure out the answer to that? You are not sitting there
*  and thinking through thousands of possible transformation steps or programs in your head
*  that you're trying to apply them. Instead, you use your like perception ability, your experience
*  in order to shrink down that of all possible permutations or transformations or what it might
*  likely be. And you're only usually doing deterministic kind of evaluation in your head
*  for maybe three, five potential like solutions there. So the idea of the compute limit is really
*  to force researchers to reckon with the fact that efficiency is part of the definition.
*  We're going to like keep increasing the compute over time. The honest answer, we don't know how
*  much compute is needed yet in order to solve ARC. We already like, I think, two to three x the amount
*  of compute that you get for this contest period over what folks got last year. I think in the last
*  year, you got an even weaker GPU only on like three to four hours of runtime. And so there's
*  like somewhat of a practical constraint of the fact that Kaggle is donating compute for the contest.
*  So like we're going to work with what they are able to provide. And we're going to keep going
*  up over time is sort of compute flop per dollar scale laws keep like holding. But like you should
*  expect that that compute limit is going to keep going up as time goes on here. This is perhaps
*  an interesting contrast, by the way, to the public leaderboard. The public leaderboard trades a compute
*  limit for a dollar limit where I know we haven't talked about this, we can. The public leaderboard
*  is a separate leaderboard. It's not part of our prize. It's part of like the can't win prize money
*  on it because it measures the public data set, which has the answers that are out there. So it's
*  liable to contamination or fitting. However, we built this separate leaderboard because we
*  had like our own deep curiosity of like, how could frontier models do? You're allowed to use
*  internet on the public leaderboard. And on the public leaderboard, we swapped the runtime limits
*  and the compute limits for a dollar. You can use up to $10,000 for like online API based commercial
*  API calls on the public leaderboard. And so the private leaderboard has the Kaggle sort of pretty
*  hard constrained compute limits. And the public leaderboard allows very uncapped amount of compute,
*  you know, more of a dollar limit, as opposed to like a hard bit of hardware that you're required
*  to use. Somewhere we'll figure out like what the truth is. And maybe I'll make the meta comment
*  pretty interesting today that actually the state of the art and both the public and private leaderboard
*  are pretty, pretty good agreement with each other. They're only like a couple percentage points
*  different. Yeah, that's definitely, I noted that as well. And so that difference, I guess I don't
*  actually know exactly what Ryan ended up spending with his technique, but the cap of the full
*  thing, the full state of the art are maxing out runtime and cost, which is maybe another interesting
*  meta commentary of like why we're going to commit to contributing, keep upping the compute as time
*  goes on. Cause like right now, like all the solutions are sort of maxing out their runtimes.
*  Yeah. So the difference between a little fuzzy because of different things are obviously priced
*  different ways, but we're looking at something like my estimate was one cent per puzzle with the
*  private official contest specs versus a hundred dollars per puzzle on the public leaderboard.
*  So there you're basically talking a 10,000 X difference. Yeah. Again, yeah. Based on, you know,
*  on demand prices versus acquire own. Yeah. It's a significant amount of additional compute capacity
*  you get on the public leaderboard. Cool. Okay. Interesting. Fascinating that they're right together.
*  I kind of expect the reason, one of the other reasons we published the public leaderboard,
*  it's not just like the curiosity of how to front your models do. It's quite easier to get started
*  with API based models. And so folks that are being curious about the competition, but just want to
*  get started with playing around in a notebook, you know, try one of the existing off the shelf
*  solutions, not have to go like spin up and figure out how to do, you know, private fine tuning or
*  whatever. Roaming the public leaderboard can be kind of a source for folks to get started just a
*  lot faster and be more of an accessible entry point to the contest. Similar to the private
*  leaderboard, all of the public leaderboard high scores have code attached. So you can go
*  to arcprize.org slash leaderboard and see Ryan's code. You can actually go look at it and copy it
*  right in your notebook. If you were so willing or you want to evolve or tweak on top of it.
*  Quite expensive to run. I would recommend sampling your sort of test set if you want to
*  attempt some new ideas there. Or maybe that can be brought like an entry point. And my expectation
*  is that public leaderboard scores will roll down to the private leaderboard through kind of waterline
*  effects where once someone shows that something is possible with existing levels of compute and
*  algorithmic efficiency, that will encourage a very strongly motivated search to figure out,
*  okay, how do we accomplish that same thing then within the runtime performance elements of the
*  competition? Yeah. The four minute mile effect for these things is very strong. Yeah. You see
*  this all over the place, right? Four minute mile video game speed running is another area you see
*  this. In fact, the 2020 Kaggle competition for arc had a very similar waterline effect where
*  for the first like month or two kind of very eager progress, one person sets a new waterline,
*  three or four percentage points up, and then everyone hits it almost within just a few days.
*  Existence groups are really, really powerful, I think, and motivating.
*  Yeah. I think GPT-4 kind of did a version of that just for the language models and chatbots and
*  all the product integrations, everything. It definitely sort of reframed it for a lot of
*  people what could happen. Especially the fact it was commercial value attached to it too. Not only
*  is it technologically possible, but OpenAI showed that there was a market there for it too. Yeah.
*  People will pay for this. One of the things that has led to us actually launching ArcPrize in a
*  meta way, the dynamic of the current ecosystem around large language models, because there is
*  some small amount of economic utility with them, it has sort of caused a reaction amongst AI research
*  and all the companies and labs doing research to over-rotate and fixate on LLFs as the only way
*  that things are going to work. In 2023, there was $20 billion of investment that went into language
*  model startups. And by my rough estimate and count on my own, maybe like a couple hundred million
*  into AGI startups, like working on new ideas, new architectures, new learning algorithms,
*  things like that. Like literally like 20 to one sort of ratio difference here in investment.
*  The commercial market has also led to a lot of closed up frontier sharing. OpenAI didn't share
*  any frontier details on how GPT-4 worked in their paper. Gemini followed suit and didn't share any
*  of their technical details on how the longer context, the million context length window stuff
*  worked for theirs. Unfortunately, I think we're just going to see more and more of that because
*  there is a known market value now for what these like frontier innovations mean. And yet,
*  this is like in complete contrast to why you and I are even like talking to each other,
*  right? Like if you look at the history of the transformer or GPT-2, that got started all the
*  way back in 2014 probably, maybe even earlier than that arguably, but Ilya did the sequence to sequence
*  paper at Google, published that openly. That got picked up and built on by Banada who made the
*  attention mechanism at I think Jacobs University. That got picked up and brought back into Google
*  with Vaswani and Chazir at Google who did the attention is all you need paper, right? 2017.
*  That got picked up by Al Bradford and Ilya now at OpenAI who's realized, oh, that's like the key
*  unlock that allowed GPT-2 to get built three, four and so on. So the reason we find ourselves
*  in the environment we do today with like all the cool AI progress we've had is because of open
*  progress, open sharing, open science. And that's just like not the world that exists in 2024
*  right now. One of the goals of ArcPrize is to play a small role in trying to counterbalance some of
*  those things and bring awareness to the issue and also motivate people to work on new ideas again
*  and find a way to get those ideas put into the public domain to reaccelerate some of the open
*  progress. As a technical question on the rules, if somebody submits a solution, are they committing
*  at that point to open source or do they get to decide later if they want to open source
*  to claim a prize or whatever downstream? It's eligibility checks happen at the end of the
*  contest. So there's a handful of like eligibility things, like there's a certain amount of countries
*  you can't be in because Calgo can't pay out money to certain contestants in certain countries.
*  But yeah, basically there's like an eligibility check for the top five scores for this 2024 period.
*  We'll go through, pick off the first five that are eligible and those will be the ones.
*  And part of that eligibility check is the commitment to publish and put the code into
*  open domain. They'd share with us and we'll probably act as a clearinghouse to publish it
*  once the prize money is released. Gotcha. I was just wondering if because of your comments on
*  Open Science, I wonder if there's any risk of somebody scoring high and then being like,
*  you know what, I think I'm going to go use this to fundraise for a startup or, you know,
*  go try to auction myself off to a big tech company or something. This comes back to the
*  waterline effect, right? Once you know something is possible, it's very motivating to others.
*  We're going to keep running ARC Prize until somebody creates a solution and puts it in a
*  public domain. So if someone just shows up and says, hey, I figured it out, I got the answer,
*  but I'm not going to share. And we're going to keep running the prize. Our goal is to motivate
*  people to figure out how to do this, figure out how to distribute it openly and motivate.
*  And so, yeah, I think there is a chance that actually happens. In fact, I've seen a few fun
*  comments on Twitter where founders were like, hey, if you've got a solution to ARC Prize,
*  don't share the code, come talk to me and I'll give you like a $10 million starting salary.
*  Which I actually appreciate. I think it's kind of cool. I think it shows that people are starting
*  to realize the value of new ideas. You're starting to see, I think, an emerging idea
*  that's like countering the sort of dominant narrative of scale is all you need. And I think
*  it's because there's a lot of evidence behind it. And I think that sentiment is what's going to drive
*  more and more researchers to go explore new ideas again, which is what we want at the end. Like,
*  our goal is to help accelerate open progress towards AGI with ARC Prize. And however we get
*  there, I think there's a lot of paths that can go. But I think fundamentally, the only way it's
*  going to happen at this point in time is we have to convince and motivate, inspire more would-be
*  AR researchers or existing AR researchers to work on new ideas again. So depending on your time,
*  what I thought I might do next is just take a minute on the kind of introspection point and
*  talk through how I feel like I'm doing it and then start to go into some of these
*  possible strategies or new ideas. Let's do it. Let's keep going. I'm having fun.
*  Okay, cool. Me too. So when I try to think about what I'm doing when I solve one of these puzzles,
*  I basically broke it down into four steps. And I wonder if you would say the same for yourself
*  or different or compare and contrast. But for me, it kind of starts with, I actually have an
*  interesting alternative definition, right? It's interesting to me anyway, an alternative definition
*  of intelligence that I think actually fits very nicely with Stappier in a way, because
*  I sort of think about it in the context of workflows or broader structure, broader scaffolding.
*  Obviously, Zappier being almost synonymous with a no-code way to create these sorts of things.
*  The definition that I come down to is intelligence is the ability to succeed on a task
*  where we don't have an explicit algorithm to do it. So I think of like in this, for example,
*  recognizing digits, right? I went and asked Claude 3.5 Sonnet to write me a program in explicit code
*  to recognize digits. It got to like 14%, which is just slightly over random. And to my knowledge,
*  there's not really still to this day any good algorithm for solving MNIST that doesn't involve
*  learning. And yet we can identify the digits obviously super easily and so in a trained model.
*  So that is interesting. That's like a more minimalist definition in the sense that...
*  Like there's something real there or like true there, right? Like this idea that like intelligence
*  is what you use when you don't know the answer. Or intelligence is like what you use when you
*  don't know what to do, right? That's this general definition. I think the sort of Francois definition
*  of efficiently acquiring skill has some like formal definition and math behind it that
*  goes through in sort of the 2019 On-Module of Intelligence paper. But I think spiritually
*  and conceptually, I think there's a agreement between those two definitions that...
*  Yeah, there's definitely something in common. I think his is more demanding in the sense that
*  I am willing to count something as intelligence, even if it is heavily trained or has like seen
*  plenty of these tasks before. I'm not putting so much emphasis on efficiency. I'm just emphasizing
*  the ability to succeed in the absence of an algorithm that could tell you how to do it.
*  The thing that your... That definition leaves open is brute force, right? If that were true and only
*  true, that would mean that general intelligence could be an algorithm which merely does a brute
*  force search over all possible algorithms that exist. And we know that's not actually quite how
*  human level general intelligence works. And in fact, like efficiency is quite an important aspect
*  of early intelligence emergence too, right? In fact, efficiency may be the gradient by which
*  intelligence emerged. Early organisms had to navigate their environment and they wanted to
*  navigate to food. They wanted to navigate to avoid danger, right? Predators. They wanted to reproduce.
*  And there is risk to taking steps, taking action in their environment, right? If these early
*  proto-organisms are just sort of randomly moving around or exploiting a brute force search to
*  navigate their environment, it's not going to be very good. It's going to run into a lot of dangers
*  and things that it doesn't want. It's going to waste a lot of energy at minimum trying to navigate
*  the environment. And so I suspect that efficiency might be one of the gradients evolution used in
*  order to get intelligence to merge in the first place. So that those early organisms are making
*  smarter local decisions about how to navigate towards food, navigate away from predators,
*  and so on. So my hunch is that efficiency is actually a really, really fundamental aspect of
*  what general intelligence is and how it emerged in the first place. Yeah, that's interesting. It
*  definitely makes sense. I think these definitions get so nuanced and the intuitions are definitely
*  worth unpacking, I think. The rules do not have any limit on how much resource you can put into
*  training before you submit, right? You can submit your model with arbitrary training. It just has
*  to actually run within the 12 hours. That's right. You can do as much unlimited pre-training
*  as you want. That goes for both the public and private data work. Yeah. So I mean, that's
*  interesting because it's also like the... I was going to ask, is there anything in nature that
*  suggests that this is possible? And I think humans sort of do in the sense that we can solve one in
*  7.2 minutes, for example. You would then look back and say, well, we've had all of evolutionary
*  history to get to where we can do that. But then you basically allow for the same thing. You can
*  train as intensively as you want. It's inference time efficiency that we're concerned with here.
*  I do think that something a lot of researchers maybe... Myself included, by the way, when I
*  start first thinking about efficiency and where the energy in the system lies, it's not correct
*  to just think about starting at birth for a human, right? Certainly there's a lot of training data
*  you sort of get exposed to as a child and you develop it. But because of the fact that humans
*  seem so predisposed to acquiring these core knowledge skills, extremely early on, a year old,
*  for example, with motor skills, seems to suggest there is something in the brain architecture that
*  allows us to be very good at predisposed to acquiring that skill in some way. And that is
*  definitely an outsource search, right? That architectural discovery is something that we've
*  had tens of thousands of generations and a lot of energy has gone. You almost have to count up the
*  energy that's gone into all the lifetimes of humans in that sort of ancestral tree in order
*  to make a more accurate assessment of the efficiency there. I get pretty inspired by this. I do think
*  existence proofs, again, are really important. We have one really, really strong existence proof
*  of general intelligence that exists in all of our heads. We don't know what the architecture
*  exactly is though, yet it exists. And so, this kind of, in my mind, motivates a search. It's
*  possible to create, it's possible to build, it's possible to figure out what it is. We've not done
*  maybe the best job yet to date of searching the space of what those architectures possibly look
*  like. We're maybe a decade into deep learning now and there's like 7, 8, 9, maybe mainline
*  architectures from CNNs, RNNs, Transformers, Excel, STMs, RWKBs, all those state space stuff.
*  This suggests that the search space of possible architecture is actually very rich and suggests
*  there was lots more to find. If I came back 20 years from now and said, hey, by the way,
*  we ran out of new architectures in 2024, I think you'd be probably very surprised that that was
*  sort of the case. And each of these architectures has slightly different properties, at least around
*  the characteristics of efficiency and inference speed and things like that. So far, we have not
*  yet figured out the architecture that allows the generality to emerge quite as strong yet.
*  Maybe the space of architectures in terms of how we define architecture is still kind of limited
*  or naive in some way, but there was one unsupervised search that led to general intelligence and that
*  is evolution. I think that's at least knowing about and realizing from a possibility standpoint.
*  Yeah, it sort of suggests also that there might be some creative hacks that could be quite fruitful
*  avenues to explore. And this is sort of inspired by my own introspection. So tell me if you do this
*  in the same way. My four steps are first, and I'll kind of also score these on how much intelligence
*  or inexplicable intelligence I feel in each one. First, there's the visual spatial kind of,
*  I wouldn't even say it's like reasoning so much as more just like detection of salient features.
*  There's somewhere it's like, oh, that cross seems to be an important thing. It's like jumping out
*  at me off the screen somehow. That part feels to me like a little bit hard to turn into an algorithm.
*  I could define an algorithm for identify all the lines or identify all the contiguous things or
*  identify anything that has a hole in the middle or whatever. I could program all that out. But
*  there is something when I'm actually doing the puzzles where it's like, I see a cross there,
*  I see a cross there. That seems like I'm onto something. So it's sort of-
*  That's that objectness core part that you gained very early on as a kid.
*  Identity. Yeah. And it's funny, I was looking also in preparing for this at kids' toys and just
*  noting how many of them are sort of like, there's a star thing and you have to put it into the star
*  hole. And then there's the rectangle and you put it into the rectangle. So that is something that
*  people at a young age are obviously not entirely born with, even though-
*  I would call it what you just described as perception. And perception is something
*  deep learning is really good at. We have lots of examples and lots of knowledge about how to build
*  really effective perception. So I would say that first step you just described is not the hard
*  part or at least the part that has lots of ideas attached to it today, currently.
*  Yeah. It seems like there's a lot of CNN type approaches or I was even going to suggest maybe
*  a state space angle that could work on that. But interestingly, it isn't so easy for the frontier
*  language models. Like Ryan's report on GPT-4-0 is that kind of sucks at that. I've been messing
*  around with Cloud 35 Sonnet and it's also, it feels better a little bit than GPT-4-0,
*  but it doesn't, certainly not great. It has this sort of like blurred vision somehow that
*  is really interesting to experiment with. But yeah, I would agree that that's probably not the
*  hard part. The next part for me feels like where the magic happens and speaks directly to your
*  point about efficiency as opposed to brute search. And it's the part where I'm like,
*  this feels like the hard part. That for me, I call it guessing the rule. It's like given this sort of
*  meditation for a second on what seems important here, I really don't know where this comes from.
*  But most of the time I can pretty quickly just intuit the rule. And in retrospect,
*  as I've tried to, I really don't have any explanation for what is happening between
*  a somewhat conscious noticing of these apparently salient features and the translation from that to
*  it kind of starts with an intuition and then I can verbalize it. But I feel like there's
*  this intuition that kind of just bubbles up out of nowhere that's like, oh, you got to fill in all
*  the holes with yellow or whatever. And I have no idea where that's coming from. That seems to me
*  to be the most core function here, not only because of these puzzles, but also when I think about,
*  and AI for science for me has been a growing obsession of late. I think like, what would be
*  AGI for science or what is really going to move the needle in science? I think there's a couple
*  different candidates for that. But the big one would be if you could have a model that could
*  generate hypotheses that are high enough likelihood to actually be true that it's
*  worth the investment to actually do the wet work and validate those hypotheses. We're starting to
*  see that actually a little bit. It strikes me as how we're using AI systems right now for like
*  protein synthesis stuff. Yeah, exactly. That's a leading area in that regard and a lot more,
*  I think, to come in that domain as well. It's guessing the rules. That feels right.
*  The current best approaches today, or at least on the language model side, are brute forcing.
*  They're trying to generate lots and lots of rules, thousands of them. And then they're using an outer
*  loop of deterministic code to check all the rules that got generated against the examples in the
*  set and apply the ones that work to the test set and use that. In contrast, I think how humans seem
*  to do it is we're using some of that first thing you talked about, your perception ability. We're
*  using some sort of perception ability to shortcut the rules that we think about. And those perceptions
*  are grounded on all those core knowledge priorities that you've been gaining experience on your entire
*  life, all the way from really early age. And so there's something there that hasn't gotten
*  figured out yet of how to use deep learning or perception network to really effectively steer
*  and guide a program synthesis style engine where you're generating these potential programs.
*  And then you can still use deterministic code to check them. Something like that feels like the
*  most direct near term way to solve ARC. I will maybe point out though, just one interesting
*  observation that no one sat down and designed a program synthesis engine into the human brain.
*  That was a emergent characteristic of something else, of the architecture of the scale of the
*  brain allowed an emergent program synthesis engine to exist. So there's two competing schools
*  of thought of how do you figure out this program synthesis guided deep learning system. And one
*  would say, well, go search for new architectures, go search at new levels of scale and try to figure
*  out can you design a system where the program synthesis engine emerges organically from that.
*  The other school thought is like, it's faster and more direct to try to have a good insight
*  about the problem here and don't try to evolve or discover a system that has that property.
*  So instead of just build it directly because we feel like we have a good enough intuition of
*  the things that are necessary in that deep learning guided perception network to just
*  jump straight to the answer. They have trade-offs on the two. The evolve and discover method is
*  very inefficient. It's going to take a lot of energy and scale in order to go try a bunch of
*  different architectures and different learning algorithms to figure that out. But it has
*  potentially more likelihood of global convergence on actually discovering one. And by the way,
*  we know one exists because it's in all our heads. So it maybe does a better job of searching the
*  global search space there. Whereas the kind of attack the problem directly, go build and design
*  a program synthesis engine that's guided by deep learning trades off like it's going to be much
*  more efficient, but maybe it's less likely that there's a strong existence proof there. And that
*  might be where that approach could run into limitations. If it doesn't bear fruit, be like,
*  ah, there's something missing still that we haven't figured out quite yet.
*  Yeah, I wonder, I mean, the people at the frontier model development companies these days
*  presumably would say, and I had a couple of conversations on this topic, I imagine that
*  they would say, this will all kind of come out with scale, right? And the argument there would
*  be basically the way these are formulated is essentially a classic few shot prompt.
*  The big unlock of GPT-3 and the title of the paper was large language models are a few shot
*  learners. And it was like, my God, we can sort of just give a couple of examples of any arbitrary
*  task within some pretty wide bounds. And the thing can not only infer the task, but then go on
*  and do the task. So is there something about this that you think doesn't?
*  Well, I think learning there is probably not the right word to use. You know, there's this
*  effect that you see happen with language models as the parameter counts go up, where you need to put
*  fewer and fewer examples into the prompt in order to steer the output tokens better with higher
*  degree of accuracy and consistency. Smaller models, 7Bs, 30Bs, you might need to do, for example,
*  five or 10 really good crafted examples in your prompt in order to get it to do a good job on
*  whatever your test example is. Whereas GPT-4, 4.0, Claude Sainte, you might only need one example.
*  Heck, in many cases you don't need any, right? But if you want to steer a little bit, you might
*  just need one. I think the intuition I have on why this is the case is that you're sort of trading
*  off where in the system you're putting your energy. With a bigger, larger model, you're
*  putting more of your examples of the programs or the idea of the training. You're putting more of
*  them directly into the pre-training phase. And so you don't need as many in the prompt in order to
*  steer the model to the ravine of activation weights that are close semantically to it in the
*  manifold space of all the programs it has. Whereas with the smaller models, they might only have
*  one example of the type of task you're prompting it on in its training data. And so you actually
*  have to overload with more examples in the prompt in order to get the weight activations to discover
*  where it's at in the pre-training and have it work. So I think that's the trade-off. In both cases,
*  though, at least with language models as they're currently designed today, we're still in a regime
*  of direct inference, direct prompting off of memorized training data. And I don't mean
*  memorization and just like, oh, they're just being on tokens, but they're able to make connections
*  in slightly more abstract ways. But at its fundamental, it's still limited by the programs
*  it's being shown in its training data. It's not able to generalize to novel programs or tasks that
*  had no bearing anywhere at all in its training data. And I think that's the big thing that's
*  missing. That's this key idea about the current architectures of how we have language models
*  designed that I think will limit their impact on the archivist market. I suspect with the current
*  architectures, they maybe get to 50 or 50%. I don't think they'll get us all the way to the
*  grand prize though. That's interesting. I think I would take the other side of that on just pure
*  scaling and I'll just throw out a couple of findings that inspire me to believe that.
*  One is, I think about this paper all the time still, it was a 2022. And the way I might bookmark
*  in my head for it is gradient descent in the weights. I've got a few of these since then,
*  but this one stood out to me also because it was a US-China collaboration, which I always think is
*  of extra note in the grand context too. So what they did was they designed an
*  implementation of gradient descent that they encoded into matrix form. And then they went out
*  and looked for that same general pattern of weights in models that have been pre-trained
*  in the normal way. And they found it and they were like, oh, look at this. We are able to
*  demonstrate now that the models are implementing a sort of gradient descent at runtime based on the
*  few shot examples. That to me does feel like learning. I mean, that doesn't feel like
*  memorization intuitive, but that does feel like a more sort of meaningful... Let me maybe clarify.
*  I don't mean to say that language models don't do any generalization. They clearly do. That's why
*  they're so special and cool. That's why they have economic utility is because they are more general
*  than any system we had ever come up with prior to 2017 with the sort of discovery of the transformer.
*  We have not made more progress towards generalization though since that. Like all
*  of the current language models still use these same underlying generalization architecture that
*  we've had all the way back towards like the very beginning here. There was a paper I saw a couple,
*  I think it was a month ago. It was called On Paradox of Learning to Reason. And what the
*  researchers did was they used a BERT transformer and they created a synthetic deductive reasoning
*  data set. So things like if X then Y, if Y then Z, given X is true, is Z true. So they came up with
*  thousands of these little synthetic toy deductive reasoning rules. Some of them required just one
*  leap of deductive reasoning. Some of them required maybe five or six steps where you had to plug
*  things into each other. And they sample from the data set. They made a thousand of these. They took
*  500 of them and they sampled it from like a forward deductive where they kind of looked at from the
*  given the rules and looking at the output. And they sampled the other 500 from like the backwards,
*  I think. Yeah. Given the output, what's the rule. And what they found was when they trained this
*  like BERT transformer using just simple back propagation off the shelf stuff on like the 500
*  from let's say the first data set and tested on the 500 from the first data set, it got 100%
*  accuracy. Same thing on the second data set. Trained on 500, tested on that 500, 100% accuracy.
*  But when they trained it on 500 from one distribution and they tested on the second
*  distribution, the accuracy fell off very predictably all the way down. Basically as the
*  number of reasoning rules and hops you had to do went up, the accuracy went down to below 50%.
*  So that's it so far. You kind of missed it. But then I think there's an interesting thing
*  that researchers did. Then they tried to say, well, could we hand code the weights of a BERT
*  transformer like model in order to get 100% accuracy no matter how you sample from the
*  source synthetic data distribution. And they were able to achieve this. I forget how the code's in
*  the paper if you want to go look at it. They kind of abused their human knowledge of the BERT
*  transformer architecture where it does broadcasting and they used that. They stacked a bunch of
*  network layers together and used that fact that it was broadcasting to kind of mimic the deductive
*  reasoning broadcast that you have to do. But they were able to build a system that used the same
*  off the shelf BERT transformer and got 100% accuracy on this deductive reasoning. And so what's
*  the takeaway here? I think one interesting thing it suggests is that perhaps the transformer
*  architecture is capable of really high degree exacting accuracy generalization, but our training
*  algorithm is wrong or insufficient. The sort of back propagation simple training algorithm could
*  never have discovered the set of weights that the researchers hand coded. And so the researchers
*  are using the general intelligence in their brain. That's where the general intelligence existed in
*  that latter example. They're using their human brain to figure out how to have used the
*  architecture. That's where the novelty came in. I think it says something kind of interesting about
*  maybe current architectures are sort of sufficient and it's more the learning
*  algorithm that we need to fix. Yeah, I do think that is quite interesting.
*  I mean, there's so many different meanings of generalization too, right? Because you've got so
*  many different kinds of data and all that. If you just trained a transformer at some scale,
*  just on these tasks, presumably it would work. I think that's been kind of the stated expectation.
*  That's like a little bit outside the rules. I think the idea was like, I think Francois said,
*  if somebody just generates a ton of puzzles, trains on them, then they'll probably be able to
*  solve it. That is one known deficiency of the benchmark. We want to make the benchmark better.
*  We talked about this, right? We know the first version is insufficient in many ways. And this
*  is one of the ways is that given unlimited pre-training, you could sit there and try to
*  generate every possible arc puzzle that could ever exist and train a model on it.
*  And it prompted it test time and rely on the memorization fact that's just been exposed to
*  every possible arc puzzle that's ever existed or could exist and do it. You could also do
*  brute force search to get a data center. You could like plug in and search every possible program.
*  There are ways to beat it today. Hopefully the existing rules around efficiency with
*  like the compute learn time limits and no internet help increase the confidence that like a score or
*  like a result is a true result. But yeah, we know that current benchmark is not perfect and we are
*  going to try and work on improving it with V2 and so on in the future. So what just as a digression
*  before we get into ideas to solve the current one, what does that look like? Is that like changing
*  the format or is it just being more creative and off the beaten path in the test set?
*  The year term stuff, we want all of the, and this won't change for this contest period.
*  Like that's part of the contest. The thing that I think we want is to have arc and arc prize be a
*  very strong guiding light towards what AGI actually is and a measure and a benchmark for it. Any
*  solution that could simply beat arc through brute force is not a very good benchmark.
*  So that's the thing we're trying to solve. And one approach we're thinking and considering is
*  to look at basically which of the tasks are least susceptible to brute force search based empirically,
*  just based on the last four years and this contest period as well. And try to understand what about
*  the like puzzles that are least susceptible to brute force search, but still very straightforward
*  and easy for humans to solve. What are the features and facets of those? And use that as inspiration
*  to go generate a much larger data set. One of the other challenges or deficiencies of the arc data
*  set is it's kind of small. There's only a hundred private examples in the test set. And that does
*  lead to some statistical issues on the margins. It'd be much better if it was at least double the
*  size. But yeah, we want to grow, increase the size of the data set. And we're going to try and increase
*  and add new examples and new tasks into the data set by looking at like, okay, well, what are the
*  features of the ones that have like the highest degree of novelty in them, right? And are the
*  least susceptible to brute force search. Cool. Interesting. So just to round up my heuristics,
*  I think we got the, or my breakdown, we had the perception portion, which I think we're agreed that
*  there are approaches out there that can do this. There's guessing the rule, which for me is where
*  most of the magic happens. And also it's like the thing that could really unlock things in AI for
*  science and so many other interesting areas. Step three is like basically writing the program.
*  This one I'm sort of back and forth on, because I'm like, I don't have an algorithm that tells
*  me how to translate a natural language specification into code, but nevertheless, it still feels more
*  algorithmic somehow. Yeah, that's the rule, right? Like in your head, you have a thesis of what the
*  rule is and you try it. You like test against your demonstrations and you're like, okay, that
*  worked out. I'm going to use the interface to actually design the output based on that rule.
*  And then the final thing is just kind of trying to figure out what I did wrong when it
*  didn't work. Was it that my rule wasn't quite specified in the right way or that I maybe made
*  a mistake in implementation from reading Ryan's post from his use of GPT-4.0. It sounds like
*  the programming is pretty good, but not awesome and certainly like has mistakes.
*  And then he has this kind of revision step, which sounds like it helps quite a bit, but probably
*  still has a lot of the same core challenges where it's like, the perception isn't great and coming
*  up with the guesses, you got to come up with a lot of guesses, so on and so forth. I think this is
*  all pretty good, happy path. I think there's maybe a few other things to think about that humans do
*  while solving the puzzles that you didn't mention that may or may not be important, but they certainly
*  feel true for AGI. So one interesting thing is that accidentally the public data set has had some
*  mistakes in it where there was like a pixel that was in the wrong spot or it got inverted. Maybe one
*  of the task demonstrations of three or four got like switched or something. And humans are able
*  to work around this actually. They are able to spot that there is actually like an inconsistency
*  in the rules and still are able to solve the problems. Usually the way that they do this is
*  through ambiguity resolution, where it's possible that a mistake or an error, there's actually a
*  very small percentage of the puzzles that actually have intentional ambiguity in them as well, where
*  you actually need the fact that you get two shots at it in order to solve the puzzle.
*  Humans are able to deal with this. They're able to like not just figure out, oh, here's the rule
*  and go directly to the solution. They're able to hold multiple possible rules in their head at the
*  same time and have some degree of confidence against them. And, you know, hey, it's not like
*  I realized the fact I have insufficient information in order to know what the answer is. And I actually
*  have to go like make contact with reality to test. And then I'm going to use that feedback from reality
*  in order to update. That's a new bit of information that I get to use in deciding what to do next.
*  So that kind of ability to deal with ambiguity, I think is sort of an important part. Probably
*  gets closest into the guessing the rule part, but certainly is part of all of the like guess the rule,
*  check the rule and the iteration. Yeah. Okay. Cool. So that part about ambiguity is really interesting.
*  We've always debated like, should we just have more like intentional mistakes than it?
*  Just to like be really novel. And, you know, I think we've always said, came down the side of like,
*  no, we should remove the snakes. That's what I have a very good pure benchmark, but maybe there's
*  room for like, yeah, I mean, business is a real frontier as well. So yeah, I was like, maybe this
*  can inspire somebody who's thinking about if you want to build like an or collect benchmark,
*  this would be an interesting thing to explore is like design lots of novel tasks where there's
*  intentional mistakes in it. And the job is to deal with ambiguity and identify the mistake and
*  still solve the task despite it. It would be pretty interesting. So speaking of things that
*  we've explored, I imagine you must've tried some stuff like this. Like you probably did a,
*  you know, a version of like the Ryan approach with the frontier model. I mean, correctly,
*  if I'm wrong, but I would guess that you put some real effort into at least a couple of different
*  approaches before you decided that you weren't close and it was worth spinning up a contest
*  like this and funding it and all that sort of stuff. What did you try and, you know,
*  what if anything came close or felt exciting? I've done my personal approach. I kind of did
*  two things. I tried all of the like open off the shelf solutions that I could find from past years
*  contests. There's a few of them that are on the public leaderboard now that you can actually like
*  go run on the private test set. And I just tried like all of those. I tried plugging in the frontier
*  models against them. I didn't really do a lot of like iteration on top of them. I was just trying
*  to see like, let me show the benchmark. Let's see what state they are today. It was around 20%
*  actually without much improvement or iteration at that point with that code from past years.
*  And then I kind of outsourced my perception to the contest because this is not the first year
*  ARC prizes and like contest Francois and this other firm called that 42 is we're on a smaller
*  version of the contest in past years. There was 300 teams in fact that competed in the previous
*  version of it in 2023. So I kind of outsourced like, okay, if the sort of known solutions aren't
*  working, I have pretty good insight about what those things are doing. It matches up with my
*  intuition of why language models are sort of insufficient for my Zapier like research experience
*  and the fact that no one else in a private sense has been able to come up with something that's
*  all that much better. It then motivated me to say, all right, I'm going to go down to like
*  first principles here and just start thinking, how do you solve this thing? My personal bet,
*  and I don't have a solution here. I'm actually still working on it's one of my side projects
*  is that there might be a way to get a emergent program synthesis engine from like a non-back
*  propagation based search approach. It's really a more indirect approach to beating Arc, but I think
*  it's one that potentially scales better up the AGI if we can get it. And Arc is in that world,
*  like one of the feedback mechanisms that system can use in order to do its evolutionary search.
*  And Arc is a tool then as opposed to the goal. So that's kind of how I was thinking about it.
*  I don't have a result there yet, like still working, it's still very early on that, but that's kind of
*  my personal viewpoint and we're kind of working on the side outside of a Zapier running ParkPrize.
*  So when you say non-back propagation evolutionary, that just means like changing the program,
*  scoring the program, keeping the ones that score higher and...
*  Trying to come up with new architectures. So I think about a, how do you do architecture
*  search? I should also say like neural architecture search is not a new idea. It's been around for
*  the field for years and years and years. In fact, quite possibly it's the single largest compute
*  like suck prior to like the transformer being invented was spent on neural architecture search
*  and really has never mounted to anything. Nothing ever has been interesting, really discovered from
*  it. And when I turned to understand like, why is this the case? Because like architecture search
*  has this feature that it's a symbolic search, it's not using back propagation. So it's more
*  possible to discover like a global solution and converge to a global solution. And what I found
*  was like in academia, because most research labs didn't have access to like a ton of large scope
*  compute, they would make shortcuts in order to get a result, even a small result out of their
*  mass paper. And it almost all amounted to just like hyperparameter tuning, where they would like
*  change the number of layers in the CNN or tweak the learning rate. If you can do a good job of
*  defining all your hyperparameters, I think mass actually does quite an effective job. What no one
*  has quite figured out yet is how do you use architecture search and do a much more true
*  like universal relaxed search? And what could the form of that look like? In my head, it kind of
*  looks like a dense, fully connected network where you're pruning weights. Like some of the recent
*  results this year on ternary weight systems or binary weight systems, I actually think are pretty
*  cool because they get you closer to an architecture search than like a weight optimization function
*  with gradient descent. When you're in a regime where you're just deciding, does any two nodes in
*  my network connect to each other or not? And you define that with a zero or one, you are sort of
*  defining literally an architecture there. And so that's kind of the thing I get excited about is
*  trying to answer or figure out, do we have sufficient compute? Or this would be the bad
*  is that like over the last four or five years, the advent of language models, the scale that has come
*  with them has caused enough compute, has forced us down the flops per dollar scaling curve sufficiently
*  that we now have enough compute. It's available at cheap enough dollar rate that you can actually
*  do a true like global relaxed architecture search to discover the primitives of AGI when
*  that wouldn't have been something you could have done like three or four years ago. Certainly a
*  longer bet than like the direct solutions to beating Arc, but ones that I think are just
*  personally like interesting. I'm curious about. Cool. Yeah, that is really interesting. And again,
*  that starts to work. Like the takeoff scenario potential there is really striking to me because
*  you now have like automated architecture finding like the world's your oyster, right?
*  What is your sort of, before we get into additional strategies, what is your expectation for an AGI
*  world if for example, something like that does work and now it's like we can sort of brute force
*  or evolve our way into like, I mean, people have obviously very differing intuitions about this,
*  where some people are like, that's a singularity that we can't see past. It could be good or bad.
*  Other people are like, well, the complexity of the world is so high still, but I feel like the
*  only thing that really works in AI is to like be empirical. That's like one of the key insights of
*  the bitter lesson, right? Is that the only thing that have sort of worked through like, you know,
*  the search and learning techniques. And this is much to the chagrin of researchers who really
*  hoped that there'd be like a key insight that they could apply to this system and, you know,
*  turns out like better just to like look at the results, like what systems are actually working
*  and keep doing more of what's working. And so I kind of feel like the near term of AGI, let's say
*  we discover a solution Arc, the first thing it's going to be used for is going to be very boring.
*  And it's going to be used to go solve all of the exacting accuracy issues at the application
*  layer. This is something that I know from Zapier from deploying AI for the last year and a half,
*  that the biggest problem with the application layer in AI right now for users is user trust.
*  And I don't mean that in like a data privacy standpoint or like a training data standpoint.
*  Surely those like concerns do exist, but that's not what I mean in this case. What I mean is that
*  people are trying to use AI in fully automated deployment scenarios using Zapier and the
*  consistency and accuracy and reliability is not high enough for them to deploy it with no oversight.
*  And so instead what they're sort of forced to do is either change the environment such that there
*  is a human that will always oversee the system, which means now the system is still limited by a
*  human or they just don't do it because the risk is too high. These are like really boring risky
*  scenarios to you. Like think about this is actually an example that we actually have where we had an AI
*  system on Zapier that was like automatically deciding what channel to send a message and select
*  to. And we had some channels on our Slack that were shared with partners and it chose like one
*  of the partner channels and sent some like user content to it. You know, something that probably
*  shouldn't have shared outside the walls of Zapier. And as soon as we saw that we were like, oh wow,
*  that's like not good. Existing of a very embarrassing thing that we should fix. And what we had to do
*  was add deterministic overrides and controls on top of the AI system to say, hey, it's fine if it
*  generates like the body of the message, but we never want it to just like guess what channel to
*  send it to, or we want to clamp the behavior of like which channels it's allowed to send to
*  and add these deterministic overrides on top of it. So there's all this like weird investment
*  and effort that goes into because the underlying models themselves are just not fundamentally
*  reliable in an exacting way. And if you solve ARC, what you will have discovered or what you have
*  created as a computer program that can generalize from a relatively arbitrary set of core knowledge
*  priors and with exacting accuracy, solve tasks that the system had never been trained on or
*  exposed to and it's trained ever. And so that like exacting accuracy on perfect generalization
*  is going to be the toolkit, probably developer toolkit to start with, but a toolkit that people
*  can use and bring into the application layer in order to get these systems to higher degrees of
*  action reliability. So the user trust is higher so that they can deploy them in more scenarios.
*  There's kind of like concentric rings of use cases is how to think about this. And right now
*  concentric ring of use case that are the sort of inner most ring of use cases that has, you know,
*  that people actually using them for are just ones where the trust like doesn't matter because the
*  risk is still low. I think like personal productivity use cases, having an AI system summarize my inbox
*  and email me is not very high risk if it goes wrong. And yet having it do something with customers
*  or in production, those have much more catastrophic risks. So the willingness to experiment deploy
*  those is pretty much non-existent today. And I think that's directly what we're going to see.
*  So I think the near term future for AGI development is actually really, really boring,
*  surprisingly boring maybe. And I think it's going to give us a lot of opportunities to update based
*  on what the systems can do once the technology exists. And then I think you just got to make
*  decisions on policy from there. I'm not a person in the camp of like, actually, it's a very poor
*  way to make policy decisions about trying to like think about hypothetical futures. And instead,
*  you just got to look at history and say, what has happened? What can happen based on what we have
*  that we know today and kind of work your way forward from there? So that's kind of my overall
*  viewpoint, at least today on how the advent of AGI is going to look like. I think it's going to
*  be a lot more boring and more practical than most people think and expect. So it sounds like you see
*  a sort of fundamental, I don't know if it's sameness or what exactly, but between reliability
*  and like out of domain generalization that I think might be kind of counterintuitive or like
*  not something everybody would agree on. Right? Like typically, when you think of making things
*  work, you think of like, you know, dialing in the performance, more examples, fine tuning on train
*  of thought is like my go to trick for any task that I really want to dial in performance on.
*  And I feel like I'm normally narrowing the scope of what the model can do when I really want to
*  make it work for a given task. And I'm like happy to accept that trade off, especially if I'm putting
*  together a zap and it's like, okay, I want this thing to be more reliable within this broader
*  context. I don't have an intuition for why this sort of ability to solve a never seen before problem
*  would be the thing that would unlock that reliability.
*  It's because the core knowledge priors are arbitrary. That's why. So like, I think a full
*  solution arc likely takes the probably nearest form solution arc takes the form of something
*  that looks like a deep learning guided DSL generator plus a deep learning guided program
*  for this. And I think you put those two things together and like, you've got a really, really
*  strong general form solution to arc. And it's one that does not depend necessarily on the like core
*  knowledge priors that all the original tasks were built on. So like think about what these like AI
*  bots that we launched earlier this year, the way it works is users come to us and they have a text
*  product. They give the bot access to off keys for all their apps or many apps as they want.
*  And then they give the bot rules to follow in terms of telling what they want the bots to do.
*  Say like, Hey, I want you to every hour look at my inbox. And if I got an email from someone who's
*  really important, I want you to summarize it and send it to me via Slack or something like that.
*  So the sort of failure points of it right now come from like the user's desire for how to get
*  that generality through expressing it through natural language. Right. And as the system
*  break down the function calling step by step on it, I think that that's like the key problem
*  you're running into. Right. Is like the only time it's accurate enough to go all the way through
*  the full chain is when there's enough examples in the training data that it's seen in order to have
*  high enough accuracy of each step in the sort of the step process there in order for the total sum
*  of the accuracy to be high enough where the user's willing to accept the trade offs around risk and
*  trust in order to deploy it. And so like, let's say you've got this, like, let's see you play
*  at the future. You've got this like hypothetical toolkit where you've got a program that can
*  generalize from a core knowledge set of arbitrary priors to solve exacting problems. It's never
*  seen before. Like the first natural place you would do is like give that toolkit to programmers
*  or line of business users to say, Hey, now in order to write a system that does something useful for
*  you, you don't have to think about building the deterministic code. Right. You don't have to think
*  about the wrapper code. You don't have to think about the outer loop. You don't have to think
*  about like a series of steps. You don't have to think about a DSL. Like all of those things are
*  some of the hard parts about learning to program. Right. It's like learning the syntax,
*  learning the language, learning how to express it. None of that matters. Instead, you could program
*  entirely through natural language, just by giving the system like a couple of examples of what you
*  want it to do. And it would be able to then generalize from those examples to deal with any
*  of the sort of novelty or runtime situations that cause like the existing systems we have today
*  to sort of fail or break. Right. So, you know, example in the one I mentioned before, like
*  let's say with the sort of summarize your inbox, send it to you in Slack. Let's say your former boss
*  emails you and it's like, Oh, okay. So like, how's that system going to interpret that? Right. If
*  you didn't write a hard coded rule in the classic AI or classics is after your land of old, that
*  might do the wrong thing. It might fall over or at worst do something that's like cash drop to be bad.
*  And so that's kind of what you want out of these systems. I think have much more ability to like
*  learn and generalize off of like a set of core knowledge priors are trained on. It's like, you
*  want the sort of end user experience. I think just to be like, I'm going to give you a very small set
*  of examples and you're going to do it with exacting generalization, even when the sort of input of the
*  system is like varying over time. And that's what we really don't have today. That's where the
*  consistency really, really starts falling off is when you get these like small variations in the
*  input, which change the output pretty significantly. There's a lot to untangle there. I probably do
*  need to wrap up at this point. Okay. Well, maybe I'll just stand by myself for a few more minutes
*  and talk through a couple of things that in case people want a couple of pointers, but that is,
*  I wish I had a better way to try to resolve some of these differences in intuition, because
*  a lot of times I think like in an alternative scenario, if I had a person do this,
*  how would they do? And like, what would limit them, you know, in that scenario where, for example,
*  my boss emails me or my old boss or whatever, right. And it's like, I think in a lot of those cases,
*  it's not that the person like the person in my experience definitely still could come back with
*  some failures or things that were not what I would have wanted them to do. I mean, by the way,
*  first of all, what you probably want in that scenario is for the system to ask you, right?
*  You'd probably want like, Hey, you didn't give me enough details here. I need more insight in
*  order to answer this. And I'm going to come ask you. This is something we've tried to build into
*  our like AI bots is the ability for them to self-recognize when the input data has varied
*  so divergently from existing past successes that it should get like raised up to the human to like
*  intervene. But like the decision making system to do even the decision of intervening is not great.
*  So you still have the same like flaws and failure modes. And that leads to the same amount of like
*  user mistrust at the end of it. Yeah. I think you're absolutely right on those questions.
*  I guess my where I'm feeling this sort of inner confusion is around like, what that person needs
*  is not to be smarter. It is more context, right? And so then you could say, okay, well, the sort
*  of generalization that we want is like for it to ask. That's seemingly a pretty different sort
*  of generalization from Arc, but maybe could be the same. Like you would have sort of a third,
*  you know, you'd give like two examples of what to do. And then the third one would be like,
*  if confused, ask and the hope would be that it would. Right. Here's another way to think about
*  it. So when we started experimenting with like chain of thought stuff a couple of years ago with
*  GBT three, three and a half, I think the common sort of accepted wisdom of chain of thought right
*  now is like, Hey, each step might get 80% accuracy. And so if you chain three, four or five steps
*  together, you have to multiply all your accuracy together. And the overall action of the system is
*  so garbage that like no one can use it for anything. And that was our first experience too.
*  It was my first experience. My first start playing with like reasoning with language models and chain
*  of thought stuff. It's like, Oh, okay. Well, this stuff's slow, super inaccurate. No one's ever
*  going to use it. Then we started this paradigm of these AI bots where instead of trying to do like a
*  meta LLM prompt where we tried to solve every user's like use case through a single prompt that
*  we like prepend it to everything. Instead, what we found we had to do in order to get accuracy
*  high enough, at least at individual user level was we had to give the end user full control over the
*  prompt. We had to give them full control over steering their prompt for their LLM call and
*  like allow them to guide and change and update and tweak the prompt based on what they were observing
*  actually doing. So, hey, maybe you like write your prompt initially. It's like, yeah, let's go back
*  to the email every hour. Wake up, look at my inbox, summarize emails from a boss and send me in Slack.
*  Maybe what you find is that like just writing that out for the first time, it's actually not doing it
*  reliably. Maybe it's summarizing lots of emails that aren't your boss. And then you realize like,
*  Oh shoot, I never actually told it who my boss was. So I got to go back to the prompt and update it
*  to like add a rule and say something like my boss is this email address. And then you run it for a
*  couple of days and you realize your boss sent you something and like it didn't do it. And you have
*  to go look at debug it. And you're like, okay, why didn't that work? And just like, oh wait, my boss
*  sent it from his personal email address instead of his work email address. And so then you go back
*  to your prompt and you have to say, or the name is this, right? You get into this like feedback loop
*  and develop it with the system. And that like giving the end user direct control over the prompt
*  and allowing them to make contact with reality, update, edit their prompt and steer the local
*  prompt has been the only way that we've been able to get our AI bots to get up to a high enough
*  accuracy and reliability that people are willing to do anything, trust them with any use cases.
*  And people are paying for these things now. So there are people that have like steered the
*  prompts sufficiently where the like chain of thought is high enough that it's valuable enough
*  still for them. Even when the general form of like chain of thought is still like not, it's kind of
*  isn't the garbage, right? So maybe that's what I'm getting at when I'm trying to talk about this like
*  form of like generality of the systems we want where it's like a program is just programming
*  like a super meta prompt and it does lots of things. That doesn't work. That still doesn't
*  have high enough reliability, especially when you're changing them together. But if you give
*  the user full control over the prompt and allow them to tweak and edit and steer it locally for
*  their specific use case or specific task, you can get the reliability higher enough there.
*  And so I think what we really want though is we want the more general form solution, right? Because
*  we don't want users to have to like sit there and constantly make all these stupid like same
*  realizations and tweaks that every other users had to deal with. That's the only thing that kind
*  of works. But the sort of I think more magical AGI feature is when the system is smart enough,
*  intelligent enough to handle a lot of the like we'd probably, you know, train that more core LM
*  system on some core knowledge priors about what we see all of our users doing. And it being able
*  to then like exactly generalize and more domains and more tasks, instead of forcing and users to
*  take on the effort and work themselves to solve that. Well, I hope to have another episode with
*  Wade, your co founder in the next couple of months, we can get into that in a lot more
*  detail then. I guess I always kind of assume that that system that like AGI future will like,
*  read my whole inbox, as opposed to being like a generalization on core knowledge. Like you could
*  imagine and maybe it's a convergence, but you could imagine sort of, I'm just on the weak form.
*  I'm just like the first person who solves arc, like that's what you'll be able to use this solution
*  for. It's probably worth saying, I do not think that arc itself, a solution arc itself is like
*  the real world AGI that we envision and sort of care about, right? It's not going to magically
*  sort of make like robots perfect. Like we're going to need to scale up the solution, the insights
*  from solving arc, I think. At minimum though, a solution is this more general form of being
*  able to do exacting generalization from arbitrary core knowledge priors. That is going to be a
*  really important, useful developer toolkit and no code toolkit for, you know, like things like
*  Zapier where we're trying to, you know, have non-developers to use the software as well.
*  I think it's significantly more important, but I would liken it more of like the discovery of like
*  a transformer style system where it's going to be a core genesis of a new tech branch that folks
*  are going to have to build on top of and figure out what are its limits, what are its abilities,
*  how do we deploy the stuff into systems? How do we do it efficiently? How fast can it be?
*  We're going to have all the same set of questions, I think, once we have that solutions like we did
*  today with or have had in the past with like transformer systems. Cool. Well, you want to
*  break now and leave me to monologue my way through some pointers to pay for this?
*  Yep. This is fun. I'm exhausted, so I'm going to give it some lunch.
*  Alrighty. Cool. Well, Mike Knute, founder of Zapier and creator of the Arc AGI
*  Prize. Thank you for being part of the cognitive revolution.
*  That was fun. Thanks, David.
*  Thank you. Keep up the good work. Looking forward to seeing what comes out of it.
*  Either way, it's going to be interesting.
*  Yeah, no doubt. No doubt.
*  If somebody beats Arc in six months, that's going to be super fascinating. If someone
*  doesn't, I think that's also going to be super fascinating. I hope that somebody
*  beats it personally, but we'll see. Yeah. If the budget, I feel like people can get there
*  if the budget is high, but with the budget that you have, I think it will be a real challenge.
*  It definitely would be a major breakthrough if somebody were to do it on that limited compute.
*  Somebody should put it on public keyboard then. 100x, 1000x more compute? Show it.
*  Yeah. I imagine for a lot of the people that would like to make their name in doing it,
*  the cost is probably a barrier. I don't know if anything we could do about that, but the...
*  Stampling is the biggest way. Yeah. You just got to try with 10 puzzles instead of doing all 500.
*  The $10,000 limit is for all 500, which is 400 private plus the 100 verification set.
*  So if you're only testing on 10 puzzles or even three puzzles that you randomly sample out of the
*  set just to test and experiment with, you're in the order of only 10, 20 bucks for a run.
*  Still not zero, but again, I think most of the interesting things here is more in the
*  algorithmic side than the perception side. So you can use cheaper models, open source models,
*  to prove the ideas out and then see if they scale up. You can build confidence before you
*  have to go do big-to-point runs. Cool. Okay. Those are good tips. I'm going to hang on here and
*  just run down through the rest of this doc over 15 minutes or something. Bye for now.
*  All right. That was cool. So a little postscript on this episode just to run down some of the
*  things that we were planning to talk to and ended up getting so digressing into different
*  philosophical ideas that we never made it to these concrete proposals. I think we can sort of into it
*  what his feelings would be on these proposals just based on all the things that we did cover.
*  I apologize, by the way, if the sound on this isn't perfect because there is a tree being cut
*  down in my neighborhood and being ground up into a mulch at the same time. But okay,
*  here are some things that I think we should at least have in mind as we think about how we
*  might want to solve Arc. And if a team, I don't really have time to do the programming on this
*  right now, but I do have some of these ideas from like, oh, that would be pretty interesting to go
*  try. I'd be happy to kind of work with a team or just, I'm not going to tell my ideas right now,
*  so you can just go run with them. But if you have something you want to discuss, definitely feel free
*  to ping me. And I'm intrigued enough by this that I would be interested in seeing if I can't
*  contribute to a project for sure. So I'll put that on along with the other things that you're
*  invited to DM me about. So possible solutions. Okay, first of all, DSPi. This just came up a
*  little bit in my episode with Sandor Shulhoff on the prompt report. And first of all, we don't
*  know if it's pronounced DSPi or possibly DisPy, but this is sort of a framework that is for
*  optimizing natural language programs, I think is how they phrase it. And notably, it beat Sandor
*  on a head to head challenge, where DSPi was trying to optimize a prompt and Sandor was trying to
*  optimize a prompt, DSPi ended up winning. And it sounds like it was by a not insignificant margin
*  based on the conversation that I had with him. So DSPi is getting rave reviews across the community
*  for optimizing natural language programs. Maybe the first thing I would do is go try using DSPi
*  on Ryan Greenblatt from Redwoods solution and just seeing like how much juice does DSPi potentially
*  manage to get out of whatever black magic it does. It's sort of an interesting thing because
*  I've been trying to get the creator of DSPi on for an episode and haven't got a response yet.
*  But it feels like it's like, why does this work? It's an interesting question. Why should language
*  models be better at optimizing natural language programs than people are? This is a strange
*  result and does sort of suggest some form of generalization, which I would not
*  expect is like purely memorization out of the data set. But yeah, it gets rave reviews. It seems
*  to work really well on a lot of things. It beats Sandor Shulhoff on a head to head man versus machine
*  prompting challenge. And so like apply DSPi to probably any natural language program that you
*  cook up for Arc and you'll have a good chance, I would say, of getting some pretty good results
*  from that. Another direction based on previous episode is potentially using state space models
*  for images with multi scan. And here I think that you could do some pretty interesting things with
*  tokenization as well. In the Mamba Palooza episode, we ran down a bunch of different techniques
*  for adapting state space models to and the Mamba architecture in particular to the image domain.
*  And typically, because images, of course, are not sequential, right there. It's a 2D object where
*  the arc challenges are also a 2D object. So you have to present them to the state space language
*  model in sequential form. How do you do that? There have been a bunch of different ways that
*  people have experimented with, but a lot of times they involve turning the image into a patched
*  sequence multiple different ways, like from one corner to the other corner and reverse,
*  or there's like four way scans, there's six way scans, there's like all these different kinds of
*  scans. Each one then becomes a sequence that gets fed in. You can have like multiple states
*  internally that handle these different representations. And then they all kind of
*  merge their prediction back into the next token for any given thing. And I feel like that is
*  interesting in that, I don't know, it just feels like a different angle on this problem. Also,
*  the state space models are significantly more efficient if you're trying to do build up of
*  states or some sort of long prompt, you can potentially get away a lot more efficiently
*  with certain state space hacks. But something about that multi-way scan feels pretty interesting to
*  me. I also would imagine doing potentially multiple different forms of tokenization,
*  where you might not just want to look at the individual squares within the grid,
*  but you might want to look at multi-resolution scans as well. You could look at like one square
*  and the surrounding squares as like a single patch. A lot of times in the convolutional context,
*  you'll have one thing that's like the whole thing that essentially zooms out to the maximum
*  possible extent. But yeah, something with multi scans in state space models feels like it could
*  be pretty interesting approach. Another thing I think is just like really heavily fine tuning
*  small models for each of the different tasks. You know, going back to the breakdown of the four
*  steps as perception and kind of identification of salient features, then guessing the rule,
*  then writing the program, and then figuring out why you're wrong if you're wrong and iterating
*  from there. It seems to me like different specialized models might be the way to go.
*  And notably like in the existence proof of human AGI that we talked about, it is a bunch of different
*  modules, right? We have a visual cortex that has something like a convolutional network going on.
*  We have an episode with the creator of Hippo Rag in process. There's the hippocampal theory
*  of human memory, hippocampal indexing theory of human memory says that these associations are
*  stored in the hippocampus. And so when something comes to attention and it shares a feature with
*  something else, like that's mediated through this sort of abstracted connection by features
*  through the hippocampus. So whatever, I mean, I don't know that we'll have anything like that in
*  the arc solution, but just breaking the problem down and having different specialized models for
*  each approach seems pretty promising. I would maybe think about something like a Microsoft
*  PHY for rule guessing. I think their latest and biggest ones might not fit. So you might have to
*  keep it to a small PHY to actually work within the resource constraints, but fine tuning something
*  on guessing the rule seems like a distinct challenge as opposed to writing the actual
*  code, right? So to have those be the same model, not sure that that's appropriate. And certainly
*  we see this kind of specialization within the human brain. A couple other projects I think about
*  a lot that I would maybe suggest looking at out of Google DeepMind. One is called Alpha Geometry.
*  Here there's a mix and this I think is very much in the spirit of what Mike and Francois are
*  expecting to be the solve. This is a mix between a language model and a symbolic deduction engine
*  where the goal is to solve international math Olympiad geometry problems. And they do it
*  at basically a gold medal level. So this is like, you know, not superhuman, but like very top end
*  of human performance. And they do this with a sort of two part cycle where the symbolic deduction
*  engine like generates a ton of possible moves and their goal is to prove something. So they like do,
*  you know, make all these sort of moves in symbolic geometry space, see if they can get to the end
*  point. And then if they can't, they ask the language model to kind of give another idea. And so the
*  language model in that context is serving as a sort of intuition driver. But then that intuition
*  is like hammered on by the symbolic deduction engine. And so they make an analogy to thinking
*  fast and slow system one, system two, there's been a lot of sort of system one, system two discourse
*  around the art challenge. And I think that shape of a solution definitely could be quite interesting.
*  It does also start to feel like cheating in the sense that they trained the system there on a lot
*  of geometry moves. They synthesize like a huge number of sample data points. They generated 100
*  million synthetic examples of moves that the symbolic thing could make. So that's, you know,
*  like kind of out of the spirit of the art crisis. This, if you had to do that much, you'd be within
*  the rules, perhaps, but you'd be a little bit outside the spirit. And as much as they've sort
*  of said, like somebody probably could generate all the puzzles and then train on all the puzzles.
*  And then, you know, effectively brute force their way to a learned solution. They wouldn't really
*  consider that to be what they're looking for. But, you know, it might work. So anyway, two part
*  solution there where you've got one language model that surfaces intuition for something that's much
*  more symbolic and deterministic thinking fast and slow system one system two, whatever. You could
*  also integrate these things. There's another really interesting paper recently called Transformers
*  Meet Neural Algorithmic Reasoners. And this one is kind of bringing those two parts of the hybrid
*  together with a cross attention mechanism. I believe this one is also out of deep mind.
*  First of all, a neural algorithmic reasoner is a specialized graph model that can learn to do
*  certain classical algorithms. So it can learn to like sort lists, for example. And it can do this
*  in a way that generalizes well beyond its training data, at least in terms of like the size of the
*  input. So it could like take, you know, you may train it on a certain list size and then test it
*  on another list size and you find like, oh, it can actually generalize and perform this algorithm.
*  In a sense, you might say it's grok, you know, what the algorithm is, at least to a certain degree,
*  so that it can do this outside of the distribution that it's been trained on. Now, what they're doing
*  in this Transformers Meet Neural Algorithmic Reasoners is first of all, you do have to have the
*  problem for that architecture. The problem has to be specified both in natural language
*  and in like a symbolic graph form. Otherwise, it won't work. So that's a constraint. You'd have
*  to figure out how do you map the arc problems onto a form that would actually work for a neural
*  algorithmic reasoner. But then what's interesting is you give the text part to the transformer part
*  of this thing and you give the graph form to the graph network. And then there's this cross
*  attention downstream from which the transformer is able to get more information from how the
*  neural algorithmic reasoner is processing the data. And this starts to feel more like the human brain
*  where you have these like different modules, they do quite different things, but then they communicate
*  and their communication is like not super clean, but you know, at least can be used to inform what
*  the other module is going to do. That seems to me like, again, very much in line with what Mike was
*  saying, what he expects and maybe hope somebody might come up with to solve arc. Another one
*  is called FunSearch. I think I've talked about this on a couple of different episodes, but
*  this is an evolutionary method powered by language models where they take some really kind of far out
*  Byzantine math problems that had been unsolved or where the state of the art had not advanced
*  in a long time. And they essentially generate programs to try to solve them. They run the
*  programs, they get a score for the program and how well it did. Then they create a database of
*  all the programs so that they're able to look at what are the top scoring programs that we have.
*  And then just cycle through that looking at some of the top programs. They use an interesting
*  technique to try to make sure that they're not just like generating the same thing over and over
*  again. They kind of have to try to push the language model to like do something different.
*  So you can go read about their technique in more detail to see how they're doing that. But
*  they do have a problem of getting stuck close to local minimum. They need to kind of push away
*  from that. So given a couple of the best examples at any given time, generate a new example and
*  gradually evolve your way toward a high score, that literally solved or achieved a new state
*  of the art on notorious math problems. So that's FunSearch. The three papers, again, just to give
*  them as names, or I guess I'll do the whole thing. DSPi for optimization of language programs,
*  state space models, Mamba architecture with multi-way scans, fine tuning different modules,
*  small models specialized in the different parts of the task. Alpha geometry is the deep mind paper
*  that has the kind of tick tock relationship between a symbolic engine and a language model.
*  The one that brings them closer together with cross attention is called Transformers Meet
*  Neural Algorithmic Reasoners. And FunSearch is the evolutionary one where they keep just generating
*  programs and then using the best programs generated to date to try to inspire new and
*  better programs from there. I guess maybe the final one I'll mention is the concept of a CAN.
*  This is a recent new architecture out of the Techmark group. I've been hoping to get a full
*  episode together on this, but haven't done it yet. This stands for Kolmogorov Arnold Networks.
*  Basically, this is definitely worth looking at just for general inspiration. They're replacing
*  the multi-layer perceptron with a kind of an inversion or sort of a mirror, funhouse image
*  of the multi-layer perceptron. In the multi-layer perceptron, you have the weights are the edges,
*  but the learned weights are the edges between nodes. What you're learning is how strong the
*  signal should be from one node to another node. But then you have the activation function at all
*  of these nodes. And typically that activation function is the same, whether it's RELU or GELU
*  or whatever. It's the same function being applied to the values that are aggregated at each node.
*  Difference with the CAN architecture is that they are actually making the edges
*  learnable functions. And so you have a, in a sense, like a higher degree of freedom on the edge. It's
*  not just a single number, but it's a function of the input. And then they, on the actual nodes
*  themselves, instead of running an activation function there, they're just summing the values
*  that come from each of the edges. So instead of learning a fixed weight and having a fixed activation
*  function, you are learning a function and you're just summing at the nodes. If that's not clear,
*  definitely check out the diagram in the paper of Kolmogorov, Arnold Networks, CANs out of Tech
*  Marks. That's Zhimeng Liu is the lead author there. This is early research. It's an alternative to
*  the multilayer perceptron, but it feels like it's like conceptually profound, definitely kind of an
*  eye-opener that like, wow, you can do something this way. It doesn't seem like it's general enough
*  yet, or it hasn't been scaled up enough yet to be able to solve a problem like ARC, certainly
*  straight away. It would have to be the sort of thing that would inspire you to come up with a new
*  twist on it. But I do think there is something that's quite interesting about learning functions
*  as opposed to just learning numbers, because learning these functions, the big upside of it
*  is that it becomes much more composable and also more interpretable, which is a notable highlight.
*  But they target this architecture toward AI for science, where you have these natural laws that
*  are in many cases relatively simple formulas, and they hope that they can discover natural laws
*  by learning on this data what is the composable function that this data reflects.
*  And so I don't know, I do think there's something quite interesting there about could these functions
*  sort of be transformations of some sort on the ARC data. Maybe instead of like a single variable
*  function like they have, perhaps it could be like a matrix transformation that could be learned.
*  But being able to dynamically compose transformations is like a big part of what
*  is ultimately involved in solving a lot of these ARC puzzles, because that's essentially what the
*  program that you're writing is doing, right? It's dynamically composing multiple different
*  transformations often into a single little algorithm. So if you could create a network
*  that could learn a bunch of those different transformations and then dynamically compose
*  them at runtime, it seems like you might have something quite interesting there.
*  And then finally, I would say, especially because he noted that the current private leaderboard
*  is doing test time fine tuning, don't underestimate grokking for this. There's something
*  quite interesting there. You might be able to do like a really small, and I don't, you know,
*  would this satisfy the rules with this? First of all, would it work? But would it satisfy the rules?
*  Would it be in the spirit of like a search for AGI? I mean, that's, you could certainly debate that.
*  But just taking something really simple network and just trying to get it to grok a certain
*  transformation. We saw that grokking over the course of like a million training steps can grok
*  modular addition. So, you know, could it grok one of these patterns in like a reasonable time frame?
*  Maybe, you know, it's unclear, but it seems like it's at least the sort of thing that would be
*  worth exploring. If nothing else, all those papers are certainly inspiration for me,
*  things that I keep coming back to and very much like worthy of study in their own right.
*  But hopefully, if you're interested in taking a swing at the ARC challenge,
*  some of those will be useful pointers, useful, you know, sources of inspiration for you. And if you do
*  find any inspiration in that, or you just want to chat with me or bounce my ideas off one another,
*  please ping me. And if there is anything I can do to be helpful, I certainly will.
*  With that, thanks for listening to this little PS. And thank you all for being part of the cognitive
*  revolution. It is both energizing and enlightening to hear why people listen and learn what they
*  value about the show. So please don't hesitate to reach out via email at tcr at turpentine.co.
*  Or you can DM me on the social media platform of your choice.

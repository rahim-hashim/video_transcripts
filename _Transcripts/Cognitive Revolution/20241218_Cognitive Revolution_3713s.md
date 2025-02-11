---
Date Generated: December 18, 2024
Transcription Model: whisper medium 20231117
Length: 3713s
Video Keywords: []
Video Views: 419
Video Rating: None
Video Description: Nathan discusses groundbreaking AI and biology research with Stanford Professor James Zou from the Chan Zuckerberg Initiative. In this episode of The Cognitive Revolution, we explore two remarkable papers: the virtual lab framework that created novel COVID treatments with minimal human oversight, and InterPLM's discovery of new protein motifs through mechanistic interpretability. Join us for an fascinating discussion about how AI is revolutionizing biological research and drug discovery.

Got questions about AI? Submit them for our upcoming AMA episode + take our quick listener survey to help us serve you better - https://docs.google.com/forms/d/e/1FAIpQLSefHvs1-1g5xeqM7wSirQkzTtK-1fgW_OjyHPH9DvmbVAjEzA/viewform

SPONSORS:

GiveWell: GiveWell has spent over 17 years researching global health and philanthropy to identify the highest-impact giving opportunities. Over 125,000 donors have contributed more than $2 billion, saving over 200,000 lives through evidence-backed recommendations. First-time donors can have their contributions matched up to $100 before year-end. Visit https://GiveWell.org , select podcast, and enter Cognitive Revolution at checkout to make a difference today.

SelectQuote: Finding the right life insurance shouldn't be another task you put off. SelectQuote compares top-rated policies to get you the best coverage at the right price. Even in our AI-driven world, protecting your family's future remains essential. Get your personalized quote at https://selectquote.com/cognitive

Oracle Cloud Infrastructure (OCI): Oracle's next-generation cloud platform delivers blazing-fast AI and ML performance with 50% less for compute and 80% less for outbound networking compared to other cloud providers13. OCI powers industry leaders with secure infrastructure and application development capabilities. New U.S. customers can get their cloud bill cut in half by switching to OCI before December 31, 2024 at https://oracle.com/cognitive

80,000 Hours: 80,000 Hours is dedicated to helping you find a fulfilling career that makes a difference. With nearly a decade of research, they offer in-depth material on AI risks, AI policy, and AI safety research. Explore their articles, career reviews, and a podcast featuring experts like Anthropic CEO Dario Amadei. Everything is free, including their Career Guide. Visit https://80000hours.org/cognitiverevolution to start making a meaningful impact today.

CHAPTERS:
(00:00:00) Teaser
(00:00:35) About the Episode
(00:04:30) Virtual Lab
(00:08:09) AI Designs Nanobodies
(00:14:43) Novel AI Pipeline
(00:20:31) Human-AI Interaction (Part 1)
(00:20:33) Sponsors: GiveWell | SelectQuote
(00:23:22) Human-AI Interaction (Part 2)
(00:32:31) Sponsors: Oracle Cloud Infrastructure (OCI) | 80,000 Hours
(00:35:10) Project Cost & Time
(00:41:04) Future of AI in Bio
(00:45:46) InterPLM: Intro
(00:50:30) AI Found New Concepts
(00:55:02) Discovering New Motifs
(00:57:14) Limitations & Future
(01:01:32) Outro

SOCIAL LINKS:
Website: https://www.cognitiverevolution.ai
Twitter (Podcast): https://x.com/cogrev_podcast
Twitter (Nathan): https://x.com/labenz
LinkedIn: https://www.linkedin.com/in/nathanlabenz/
Youtube: https://www.youtube.com/@CognitiveRevolutionPodcast
Apple: https://podcasts.apple.com/de/podcast/the-cognitive-revolution-ai-builders-researchers-and/id1669813431
Spotify: https://open.spotify.com/show/6yHyok3M3BjqzR0VB5MSyk
---

# Breakthroughs in AI for Biology AI Lab Groups & Protein Model Interpretability with Prof James Zou
**Cognitive Revolution:** [December 18, 2024](https://www.youtube.com/watch?v=plq7R9KtDFk)
*  One nice thing about these virtual agents is that their meetings are much faster than our meetings.
*  Right? So in the time that we sit around and introduce each other and have coffee,
*  they've already had hundreds of meetings. These 14 language models, I think they have learned new
*  concepts. They have filled in some of the gaps in our knowledge. And now it's our job to see,
*  can we extract those out using techniques like SAEs? I do think that there is already a gold mine
*  of new concepts and knowledge that are already hidden in existing models. Even if we can extract
*  those out, I think that would already teach us a huge amount of interesting new insights.
*  Hello and welcome back to the Cognitive Revolution. Before getting started today,
*  I want to take a moment to invite all of you to submit questions for an Ask Me Anything episode
*  that we'll be producing in the next couple of weeks. From practical application to galaxy brain
*  philosophy to parenting and career choices in the age of AI, I may not have all the answers,
*  but it's all fair game to ask. And while you're there, we'd appreciate it if you'd complete a
*  short survey so that we can learn more about the audience and how we can serve you better.
*  All of the questions are optional. It's fine if you want to be anonymous. And we do have a few
*  thank you gifts planned as a token of our appreciation. Today, my guest is James Zou,
*  professor of biomedical data science at Stanford and investigator at the Chan Zuckerberg
*  Initiative, who's recently published several frontier advancing papers at the intersection
*  of AI and biology. Our first topic today is the Virtual Lab, a framework that uses minimal human
*  oversight to guide an AI research team comprised of an AI professor, multiple AI specialist agents,
*  and an AI critic through the process of understanding and exploring open-ended research
*  problems. In a truly impressive demonstration of capability, when challenged to develop new
*  treatments for emerging strains of the COVID virus, the system made the somewhat unorthodox
*  choice of pursuing nanobodies rather than the more commonly used antibodies, devised a novel
*  workflow combining protein language models, alpha fold and physics-based tools, and ultimately
*  designed more than 90 candidate antibodies, of which two have since been proven by physical
*  experiment to be of high therapeutic potential due to their ability to bind with new virus variants
*  while also maintaining efficacy against earlier versions. While the AI here is not entirely
*  autonomous, the human contributor wrote a bit more than 1% of the total tokens for this project.
*  This is nevertheless one of the most impressive demonstrations of large language models actually
*  doing science that I've seen, and one that I take as a sign of much more soon to come.
*  The second paper, InterPLM, Discovering Interpretable Features in Protein Language
*  Models via Sparse Autoencoders is actually equally remarkable. By training sparse autoencoders,
*  which we've covered in depth in previous episodes, including most recently with the
*  founders of mechanistic interpretability startup GoodFire, but in this case for protein language
*  models, which are trained purely on amino acid sequences, the team was able to demonstrate not
*  only that mechanistic interpretability techniques such as auto-labeling can generalize across
*  modalities, but also that mechanistic interpretability can deliver totally new discoveries.
*  Most remarkably, they were able to identify features corresponding to at least one entirely
*  new protein motif, which had not been previously documented in the literature. This, to my knowledge,
*  is perhaps the clearest demonstration yet that today's machine learning architectures are capable
*  of learning important natural concepts that humans don't know from raw data. It's hard to
*  overstate just how important this capability is likely to be, and I find the implications for how
*  we should understand more familiar large language models to also be extremely profound.
*  Now, I only had an hour with Professor Zou, so this is one of our shorter episodes,
*  but the results here are second to none, and I've also recently discovered another paper on which
*  he was a co-author about modeling the evolution of cellular transcriptome states over time,
*  which I hope to cover in another episode soon. If you'd like to help us make that happen,
*  we'd appreciate it if you'd take a moment to share this episode with friends,
*  write a review on Apple Podcasts or Spotify, or just leave us a comment on YouTube. Of course,
*  we always welcome your feedback and suggestions, including for more topics at the intersection of
*  AI and biology, either via our website, cognitiverevolution.ai, or by DMing me on
*  your favorite social network. For now, I hope you enjoy this conversation about truly remarkable
*  recent results in AI for biology with Professor James Zou. James Zou, Professor of Biomedical Data
*  Science at Stanford and Investigator at the Chan Zuckerberg Initiative. Welcome to the Cognitive
*  Revolution. Thank you very much for having me. Excited to be here. I'm excited for this for
*  multiple reasons. You've put out recently with co-authors, of course, a couple of remarkable
*  papers that are advancing the frontier at the intersection of AI and biology on multiple fronts.
*  And so we don't have a ton of time today. I'm going to try to talk as little as possible and
*  just get as much explanation and perspective as I can from you in the time that we have.
*  The two papers are Virtual Lab and InterPLM. Virtual Lab is one of these somewhat increasingly
*  familiar setups where an AI is taking a very active role in doing science. This one is a hybrid,
*  so I want to get into the details of exactly how that works. And then InterPLM is the product of
*  applying mechanistic interpretability techniques, specifically SPARS autoencoders,
*  which again, our audience should know a bit about two protein language models and finding some
*  really interesting results there. So let's take them one at a time. Tell us about the Virtual Lab.
*  Yeah, so I'm very excited about the Virtual Lab. So the setup there is that it's a very versatile
*  platform, right? So we have like an AI professor, sort of like AI PI, sort of a professor agent.
*  And that professor agent then manages and works with a bunch of different, as you can see,
*  student agents. Each of the sub-agents would have their own expertise. You can have one agent being
*  like an immunologist expert, right, or a computer science expert or a computational biology expert.
*  And then the professor and this team of these virtual agents, then they work together to really
*  sort of tackle these quite challenging open-ended research projects. And we did a case study of
*  actually having this team, Virtual Lab, try to design new nanobodies for the recent variants
*  of SARS-CoV-2. Yeah, so that is obviously a very relevant project. Maybe give like the headline
*  results and then I'll dig in a little bit on some of the finer points of the methodology that I had
*  questions on. Yeah, yeah. So I think the headline result is that this Virtual Lab of agents that
*  have these diverse interdisciplinary expertise, they work together and they actually did something
*  very cool with relatively minimal human feedback from us. They first developed like a new
*  computational framework, a workflow for designing new nanobodies. So this computational platform
*  that they developed, they created, actually uses quite sophisticated tools like protein language
*  models like ESM, they use AlphaFold, they also use like more like Rosetta and more physics-based
*  tools. Well, each of the two have been used before in previous studies, of course, but the way that
*  the agents actually modify these tools and then put them together into this overall pipeline is
*  actually new to the best of our knowledge. So that's something that's already very cool.
*  And the part that's maybe even more exciting is that they actually use this new pipeline to
*  really develop a bunch of nanobodies. And then with our collaborators at the Chanzai Gerberg Biohub,
*  we actually then made those nanobodies and physically and experimentally tested them.
*  And a couple of these nanobodies actually look very promising in terms of having strong binding
*  profiles to some of the recent variants, but while retaining and even improving its binding profiles
*  to some of the earlier variants. And I think that's sort of like a holy grail because you want to have
*  potential vaccines or therapeutics that can bind well across like a diversity of variants, even as
*  the virus is evolve over time. So let's talk about that pipeline. Our audience is pretty
*  plugged into AI, is pretty familiar with agents and where agents have kind of not quite fulfilled
*  the dreams that people have had for them so far and what people have done to compensate for that.
*  In general, I would kind of characterize the space as like, initially everybody was like,
*  oh, let's let these agents kind of do whatever they want. It'll be amazing. And then it was like,
*  oh, they're kind of failing in all sorts of ways. Let's rein them in a little bit, put them on rails
*  and make very clear what affordances they have. Can you give a little bit more color on to what
*  degree you set the agents up with very discrete, clear instructions on these are your tools
*  available versus what they did to recombine? What is that novel process that they designed?
*  Well, how much freedom did they have to come up with that? And how does that compare maybe to
*  things that have happened in the past? Yeah. So thank you for that question. As you mentioned,
*  there's a lot of exciting progress and research projects are trying to use agents for science.
*  I think a lot of the previous works on agents for science or language models for science more
*  broadly, it is looking at much more narrow tasks, right? Narrow in the sense of like the human
*  researchers have defined here's exactly what I want to do. And here are the different steps even.
*  And then having the agents more of sort of redoing the more low level implementations and
*  executions of those steps. Right. And the other mode is where the agents sort of come up with
*  like research ideas, right? But then the agents really don't really do very much of the actual
*  execution. And there's very little experimental validation, the real world grounding of those
*  research ideas. And the virtual lab is designed to address some of those limitations and be much
*  more flexible. In this case, it's still like an human AI collaboration, but the human feedback
*  to those AI agents in the virtual lab is relatively limited. We don't actually write the code for them
*  or we don't do the work. And we don't even tell them here's exactly what you have to do A, B and
*  C. So in this case, like we, the human researchers would tell the virtual lab, okay, so we're
*  interested in designing potentially new therapeutics or new vaccines for the recent variants of SARS-CoV-2,
*  right? So it's a high level description. And the agents actually have to decide first, like what
*  approach do they want to take? And then how do they then try to achieve that goal? So even in this case,
*  there's even like a high level question of like, you know, what should we try to even design
*  nanobodies or antibodies? Most of the human researchers actually would go for antibodies,
*  which is the more common form. And nanobodies to the audience is sort of, you can view them
*  so sort of essentially smaller versions of antibodies. They are only present in a few animals,
*  like camels, and they're much smaller. And the agents actually made kind of a surprising decision
*  themselves, that they want to actually design nanobodies rather than antibodies. And they
*  give some rationales that because nanobodies are smaller, they're easier to predict and more
*  stable and easier to design. And that turned out to be actually a quite wise decision, even though
*  a bit unorthodox, it's not even a wise decision, because then we were able to experimentally
*  validate that the nanobody designed by the agents ends up being very promising candidates.
*  So that's sort of example of where in the virtual lab, right, the guidance interaction with humans
*  tends to be more high level guidance, but really the directions of what project to tackle and how
*  to solve that problem is really mostly done by the agents. Yeah, that's really interesting. So in
*  terms of the tools, were the AIs provided with like a list of available tools? Or did they come
*  back to the human and say, Hey, can you make Alpha Fold available to us? Like, what is the
*  dynamic there in terms of identifying, selecting, and ultimately putting the tools together?
*  Yeah, so these agents are so they're GPT-4.0 under the hood. So they are aware of a lot of the
*  popular powerful tools in the literature. So we don't actually tell them you have to use Alpha
*  Fold or you have to use TSM. So they actually had some through one of these virtual lab meetings,
*  which I can describe how that works in a bit. But throughout the virtual lab meetings, they actually
*  cited that, okay, so here's a list of potential tools. Maybe they came up initially with a list
*  of six or eight different tools. And then subsequently they decided, okay, so here are
*  the three tools that may be the most relevant writers, ESM, Alpha Fold Multimer, and Rosetta
*  that have car complementary strength. And then they decided they actually wanted to modify
*  some of the tools like ESM in ways that we haven't seen being done before in previous papers,
*  and then also putting together these different tools into a new workflow. So that part from
*  deciding what tools to use, and from also to modifying the tools, which I think is a critical
*  component, all the way to like putting the different tools together into a pipeline,
*  is mostly done by the agents. So do they go as far as like writing code to go download the model off
*  Hugging Face and create a container or whatever in which to run it? Or do they, because those
*  sorts of things I typically find, I've usually found that the models are pretty good at writing
*  code, and they're pretty bad usually in terms of getting over those like, find the resource,
*  set up the environment type of steps. Yeah, so it's a good question. In principle,
*  we could also try to ask the agents to do that, and maybe they would want to have more of a software
*  agent to help them. But in this case, actually a lot of the tools are available. For example,
*  the Alpha Fold was already available on the cluster that we're using. So then the agent
*  had to write the code for interfacing and extracting information from Alpha Fold,
*  but they don't have to download the tools. Yeah, but I think that's something that would be
*  interesting to explore in the next iteration. Yeah, I think it's also a good reminder that,
*  to some degree, that stuff can be a bit of a red herring. It's very interesting to see how much
*  these things can do autonomously, but it's often more productive. Certainly, in my experience,
*  if I want to make something work, it's often more productive to identify the places where they're
*  struggling and just get over those humps and then let them run on the things that they're
*  actually good at. Yeah, I think that's a good perspective. I mean, in the end, here,
*  they're already solving a very hard problem, which is developing new nanobodies for
*  recent variants of COVID, which there's no good solutions. So they're already solving a very
*  challenging problem. We don't need to put extra obstacles in their way. So tell me about these
*  modifications. You said that they modified ESM and that they put together a novel pipeline
*  combining these models. What's the novel part of that approach? Because I think our listeners,
*  they know the agent stuff reasonably well. They do not know, or I certainly don't know, I speak
*  for myself, I guess, what the prior state of the art was in terms of pipelining all these different
*  for biology models together. Right. I think this is actually something quite interesting that agents
*  developed. So just for the general audience, the ESM is like a large protein language model. So
*  it's sort of like you can think that as like a bird style model, but trained over like amino acid
*  sequences. And it's trained over like all these evolutionary scale sequences of proteins. And how
*  it works is that you can actually give it like a new protein sequence where you can modify some
*  protein sequence by introducing some mutations. And the ESM model then will produce some sort of
*  basically like a log-likely score, right? Similar to perplexity in large language models, that'll
*  tell you like, how likely is this modified sequence? And the general intuition is that if this
*  modified sequence are stable, right, if they're actually functional proteins, then the log-likely
*  would be relatively good, relatively high score. But there's actually a lot of fine art in how
*  exactly to compute those log-likely scores and exactly which ones to use. So the agents here
*  actually developed like a new formula for computing a specific way of this likelihood ratio score,
*  which is actually different from previous publications where people had used ESM.
*  So that's actually quite interesting, let's say local modification or innovation by the agents.
*  Yeah, okay. Fascinating. Is there any intuition for like what the difference is between the
*  AI's formula and the prior human formula and maybe relative strengths and weaknesses of each?
*  Yeah, so I think a lot of that really comes down to because the AI agents decided that they want to
*  make a sequence of mutations, right? So they'll start with some wild type nanobody, which are
*  basically existing nanobodies people have tried before, but those nanobodies do not really work
*  for the recent variants of COVID. So the agents decided to take those as starting point and then
*  make some sequential modifications by introducing mutations on top of that nanobody. And I think a
*  lot of the fine art in computing the likelihood score depends on how do you measure the changes
*  in the likelihood? Do you say compared to the original wild type, does the likelihood increase
*  after every mutation you make? But then what happens if you make the second mutation? Does it
*  then you want to compare that with the first mutation or do you compare that with the wild type?
*  So that's where there's even debates in the literature about how you want to approach that
*  with different approaches and the agents actually developed a new formula for computing the
*  likelihood ratios essentially that in after the fact, in my view, it's actually pretty reasonable
*  for doing. Yeah, interesting. And then can you describe sort of the iterative loop? Like we start
*  with a wild type nanobody and we have a new evolved SARS variant that for which we don't have an
*  effective antidote, right? And then we're doing this sort of iterative process of tri-mutation,
*  then like see how they fit together and then come back and mutate again. And it's sort of an
*  evolutionary tree. Is that the right intuition? Or give me a little more color there on what,
*  especially what is new that the AIs did. Yeah, so it's actually a pretty sophisticated
*  workflow that AI agents developed. And I wish I could claim quickly that the AI agents
*  and I wish I could claim credit for that, but it's really developed by the agents.
*  Right. So basically what they do is first they will use this protein language model ESM to score
*  among like a large list of rotational mutations. What tends to be the most promising in terms of
*  likely producing stable and functional proteins, but those stable functional proteins may not
*  really be useful for the specific recent SARS-CoV-2 variants. Then to get to that,
*  then it actually uses multiple multimer to generate a computational predicted structure
*  of the nanobody and the spike protein of SARS-CoV-2 from one of the recent variants.
*  And then the agents actually recent that, okay, so that's a AI predicted structure,
*  but that could still have some mistakes and biases. Then they use this like a third step
*  of using Rosetta, which takes this input, that predicted structure, and then relaxes the structure
*  and then sort of in a more like a physics-based way and then estimates the binding energy.
*  So in the end, there are basically sort of three tools the agent ends up using, right,
*  to the large language model, Alpha Fold and Rosetta. And the agents actually decided that,
*  okay, should take through like a weighted score across all three techniques, right,
*  with a particular weighted scheme and then iterate this multiple times. Right. So then it does this
*  once, second, not most promising candidates generate additional mutations and does all three
*  steps again. And then would actually do this four times to generate like a final list of promising
*  nanobody candidates, which are the ones that we then experimentally synthesize and test it.
*  Wow. And that sequence of using those three techniques in that order,
*  it had never been reported in the literature previously?
*  People have used the individual tools, right, but I think using this particular workflow,
*  of course, you have this iterative weighted scheme for generating candidates, multiple rounds,
*  to the best of our knowledge, has not been done in previous publications.
*  Wow. That's really interesting. Hey, we'll continue our interview in a moment after a word from our
*  sponsors. How deep do you go to seek out an answer to a question? If you listen to this podcast,
*  there's a good chance you're the kind of person who spends hours clicking the source links on
*  Wikipedia pages or who's checked out the entire shelf on a niche topic at your library. If you're
*  nodding along, then you'll definitely want to check out GiveWell, an organization that
*  researches questions about global health and philanthropy, even if a satisfying answer might
*  require years of reviewing studies, talking to experts and chasing down footnotes. GiveWell has
*  now spent over 17 years researching charitable organizations and only directs funding to a few
*  of the highest impact opportunities they've found. Over 125,000 donors have used GiveWell
*  to donate more than $2 billion, and rigorous evidence suggests that these donations will
*  save over 200,000 lives. GiveWell wants as many donors as possible to make informed decisions
*  about high-impact giving. You can find all of their research and recommendations on their site
*  for free. You can also make tax-deductible donations to their recommended funds or charities,
*  and GiveWell does not take a cut. If you've never used GiveWell to donate, you can have your
*  donation matched up to $100 before the end of the year or as long as matching funds last.
*  To claim your match, go to GiveWell.org and pick Podcast, then enter the Cognitive Revolution at
*  checkout. Make sure they know you heard about GiveWell from the Cognitive Revolution to have
*  your donation matched. To donate or learn more, visit GiveWell.org.
*  There are so many things in life we just never get around to. Taking up that hobby, cleaning out the
*  garage. You know, little things that don't really make huge differences in our lives.
*  Yet there's one thing that most of us have probably been neglecting that can have a huge impact on our
*  family's future. It's life insurance. And with select quote, getting covered with the right policy
*  for you is easier and more affordable than you might think. As someone who tracks AI progress on
*  a full-time basis and obsesses about its potential impact nonstop, I know how tempting it can be to
*  ignore more mundane, familiar risks. There's always another paper to read, podcast to listen to, or
*  product to try. And yet the smartest people that I know in the AI space continue to save and invest
*  money for the future, carve out time for their relationships, maintain their physical and mental
*  health, and yes, protect their family with life insurance. Just in case anything should happen
*  before this engagement. And yes, I'm sure you've heard about GiveWell.org. It's a great place to
*  build that sense of singularity. If nothing else, it's one less thing to worry about in a time of
*  unprecedented change. So get the right life insurance for you, for less, at select quote.com
*  slash cognitive. Go to select quote.com slash cognitive today to get started. That's select
*  quote.com slash cognitive.
*  Tell me about the way in which the human and the AI's interact. I think that's maybe a really
*  I mean, you tell me if I'm wrong on this, but it feels like you may have found a real
*  sweet spot there because when I've seen people do like all AI, you know, science, it typically
*  doesn't work at quite this level.
*  I noted that the human wrote just 1.3% of the total tokens in this project, but I suspect
*  that that, again, you tell me if I'm wrong, but I'm imagining that those 1.3% of tokens
*  were a super high value contribution.
*  And by the way, are you the human in this situation or was it another member of the
*  team?
*  Yeah, so maybe I should have done this earlier, but I want to describe how research happens
*  actually with the Virtual Lab, right?
*  So as I mentioned before, the Virtual Lab is really have this set of AI agents, there's
*  the AI professor, AI PI, and then a bunch of the AI experts with different domain expertise.
*  There are basically two ways the Virtual Lab actually makes research progress.
*  One is actually through what we call group meetings, and the second one is through individual
*  meetings.
*  So in a group meeting, and these are all sort of designed to mirror how my physical lab
*  here works at Stanford, right?
*  So in a group meeting, then all the different AI agents come together.
*  So the AI professor would say, here's like the meeting agenda, like maybe there's some
*  questions that we want to answer by the end of the meeting, and then all the agents actually
*  go in a roundtable and provide their thoughts on that meeting agenda, and we think you
*  provide updates on their results.
*  And in the end, they can actually, the professor then would take the consensus and then reach
*  some sort of solution with the entire team on the solutions to those questions.
*  And that's still the AI professor.
*  That's the AI professor.
*  Yeah, okay.
*  Yeah.
*  And the goal of these group meetings is to really try to decide maybe some of the general
*  directions of the research project, for example, whether to design nanobodies or antibodies,
*  right?
*  So that decision is actually made in one of these virtual lab group meetings.
*  And the second mode of research is what we call the one-on-one meetings, where maybe
*  the AI professor would say, okay, so now we need to actually write a specific code to,
*  for example, to modify ESM.
*  And then the best agent for doing that is probably maybe like the computational biologist.
*  In a one-on-one meeting, then the computational biologist would actually meet with the professor
*  agent.
*  And also, we also have a critic agent, right, who's job is to provide constructive feedback
*  to all of these meetings.
*  And then the goal of that one-on-one meeting then would be to resolve each of the specific
*  tasks.
*  And where the human interaction comes from in all of these places is that, so we mostly
*  interact with the professor agent, right?
*  So essentially, at the start of the project, we tell the professor agent that, okay, here's
*  what we want to do, right?
*  So it could be a kind of high neural level description.
*  We could say that, okay, for this part, we want to design vaccines for therapeutics for
*  COVID, SARS-CoV-2, right?
*  I mean, we could have picked a different project.
*  We could have said, okay, we want to study quantum computing, right, or study climate,
*  right?
*  So it's a very versatile framework.
*  And then based on our high level specifications, and the professor agent would say, okay, so
*  here are the kinds of relevant expertise that we will want to have on the team, right?
*  So then the professor actually creates and selects which team members to bring into the
*  team, right?
*  For the therapeutics project, then the professor agent decided that we want to have a immunologist
*  agent, a computer science agent, and a computational biology agent.
*  And then so the professor's job is actually basically essentially think of that as sort
*  of recruiting the relevant members and selecting them to come on this quest.
*  And depends on what the goal of the quest is, like different members who get selected.
*  So the level of feedback that we provide to the professor then tends to be these more
*  high level feedback.
*  I would say, okay, so in general, we're interested in SARS-CoV-2 because that's important.
*  We can also provide feedback like, okay, you know, we don't have a large experimental budget,
*  right?
*  So we want things that are relatively fast and easy to validate, right?
*  But we don't actually tell the professor agent that you have to do A, B, and C, right?
*  So that's the workflow.
*  It's basically designed by the virtual lab.
*  So it doesn't sound like the expertise on the part of the human needs to be particularly
*  high.
*  Like, could I have done this?
*  The things you said so far, like the COVID is important and we don't have a huge budget.
*  I could have said that.
*  But I still suspect that there's got to be somewhere in this equation where the expertise
*  of the human makes a big difference or maybe not.
*  Yeah.
*  I think where the expertise of the human is to also look over the shoulder of all these
*  different agents and provide some constructive feedback to say that maybe here are some potential
*  mistakes where this doesn't look right.
*  So the nice thing about all these virtual labs is that all of their meetings, the group
*  meetings and also the one-on-one meetings happens through natural language.
*  So they all talk to each other through natural language.
*  And basically at the end of every meeting, the professor agent actually creates a summary,
*  essentially like a meeting minutes, right?
*  And then present that to us, to the human researchers.
*  So we can actually look over their meeting minutes.
*  And sometimes we do get feedback and say that, oh, did you think about this, right?
*  Or do you think about that?
*  Or if we actually see that though, they're not actually using, if we see that they're
*  potentially going down a path that might be difficult to validate experimentally, then
*  we can actually provide that feedback.
*  Gotcha.
*  It's still remarkably, I mean, it does sound like the expert, that taste, that research
*  judgment or taste, whatever you want to call it, does sound important.
*  It is a pretty remarkably light touch that it sounds like the human is using to steer
*  the AI.
*  So is this something now that, you know, is your lab kind of restructuring itself where
*  everybody in the lab is now, you know, weren't using these tools on all their projects?
*  Or like, because this feels like a pretty notable result.
*  I mean, even the fact that it shows the nanobodies versus the antibodies is like kind of calling
*  to mind the old AlphaGo Move 37.
*  I don't know if it's quite that dramatic of a departure from the consensus approach, but
*  to see those sort of surprising moves made by AI where it's like, huh, we wouldn't have
*  done it that way, but it actually works.
*  I'm always scanning the literature for examples of that.
*  I guess, like, yeah, how big of a deal do you think this is?
*  Should we put this on the level of a Move 37?
*  And should everybody be restructuring their labs to take advantage of this paradigm?
*  So we're very excited about this paradigm.
*  But I also want to say that, you know, still relatively early stages, right?
*  I think in the near future, we want to obviously provide like a V2 of this virtual lab that
*  will be much easier for everybody to use, especially the people, like scientists from
*  different domains who might not be familiar even with coding or how to use these language
*  models.
*  Right now, it's still a little bit bespoke because it's sort of like the first iteration
*  and the first case study that we did, which is solving this nanobody design for SARS-CoV-2.
*  But we do want to make it much more generalizable and easier to use in the future with some
*  more interactive interfaces.
*  And in terms of the sort of the surprisingness of this, yeah, so I think compared to AlphaGo,
*  there's some interesting similarities and also some interesting differences.
*  Right.
*  Like here, in some sense, it's not as surprising perhaps because the agents does provide like
*  an explanation.
*  In their one of the early group meetings, they said, okay, so yeah, so nanobodies are
*  known to be, they're smaller and they're easier to predict and easier to design.
*  So that's something actually something that's relatively easy for us to understand.
*  And you know, I'm not an expert in nanobodies, but I looked at that and said, oh yeah, that
*  seems like a reasonable decision.
*  So that's why we didn't push back on that.
*  Whereas maybe some of the moves made by AlphaGo would have been difficult to explain even
*  to experts.
*  On the other hand, you could say that this decision made by the agents for nanobodies
*  in some sense is also could be harder, right?
*  In that with games like AlphaFold or AlphaGo or other games, it's a bit more controlled
*  settings, right?
*  You can sort of self play it out and you could actually see what the reward is at the very
*  end.
*  It's sort of like there's a deterministic reward at the end.
*  For these open-ended scientific projects, the reason why it's much harder than games
*  is that it is open-ended, right?
*  The experimental validation, like really until you do it, you don't really know what's going
*  to work or not.
*  There's no notion of like you can self play out and see the real world experiments, because
*  that part is still not automated.
*  There's also just a lot more uncertainty.
*  These decisions are very consequential that really affects the entire research direction,
*  right?
*  And we only get to do it once, at least for now, right?
*  So I think in that sense, it's actually also could potentially be a harder kind of decision
*  to make.
*  Hey, we'll continue our interview in a moment after a word from our sponsors.
*  Even if you think it's a bit overhyped, AI is suddenly everywhere from self-driving cars
*  to molecular medicine to business efficiency.
*  If it's not in your industry yet, it's coming and fast.
*  But AI needs a lot of speed and computing power.
*  So how do you compete without costs spiraling out of control?
*  Time to upgrade to the next generation of the cloud, Oracle Cloud Infrastructure, or
*  OCI.
*  OCI is a blazing fast and secure platform for your infrastructure, database, application
*  development, plus all your AI and machine learning workloads.
*  OCI costs 50% less for compute and 80% less for networking.
*  So you're saving a pile of money.
*  Thousands of businesses have already upgraded to OCI, including MGM resorts, specialized
*  bikes, and fireworks AI.
*  Right now, Oracle is offering to cut your current cloud bill in half if you move to
*  OCI for new US customers with minimum financial commitment.
*  Offer ends $12.3124.
*  So see if your company qualifies for this special offer at oracle.com slash cognitive.
*  That's oracle.com slash cognitive.
*  80,000 Hours is a nonprofit that helps people find fulfilling careers that matter.
*  And their research suggests that working to avoid the worst AI risks could be one of the
*  highest value contributions one can make.
*  So if recent AI news has you thinking about how you can make a bigger impact, you should
*  absolutely check out all the latest research and content from 80,000 Hours.
*  80,000 Hours has been working on this for nearly a decade, and they have tons of in-depth
*  material on their website, including articles about how seriously we should take AI risks
*  and what an AI-caused catastrophe might actually look like.
*  Plus detailed reviews of careers in AI policy and strategy, as well as AI safety research.
*  They also publish a regular newsletter and podcast, which features unusually in-depth
*  conversations with guests like Anthropics CEO Dario Amadei and AI safety pioneer Paul
*  Cristiano.
*  Plus 150 other episodes on topics including global health and development, nuclear war,
*  animal welfare, and climate change.
*  If you want to play a more active role in navigating humanity's uncertain future, 80,000
*  Hours can help.
*  Everything they do is always 100% free, so visit 80,000hours.org slash cognitive revolution
*  to get your copy of the 80,000 Hours Career Guide and subscribe to the newsletter and
*  podcast.
*  That's 80,000hours.org slash cognitive revolution for all the information you need to make the
*  most of your career.
*  Let's compare how this plays out with the virtual lab versus if you had done it all
*  with just a human team of researchers.
*  Like how long did this process take, you know, just in terms of like clock time, like how
*  many hours or maybe even just minutes did the human have to contribute?
*  How much did it cost in terms of GPT-4.0 costs?
*  I'm curious, by the way, if you tried other models, I would have bet maybe that Claw 35
*  would have been the top performer, but I'm guessing you didn't fail to check.
*  So yeah, just give us kind of a tale of the tape of like how long it took, what it cost,
*  and how that would compare to a human team.
*  Yeah, so one nice thing about these virtual agents is that their meetings are much faster
*  than other things.
*  The time that we sit around and introduce each other and have coffee, they've already
*  had hundreds of meetings.
*  And the other nice thing is that the virtual agents, they don't get tired.
*  Right.
*  So what actually we do is that in the virtual lab, every main decision is actually we do
*  multiple meetings in parallel.
*  So basically every key decision that we want the agents to make, they actually run five
*  meetings in parallel.
*  They would discuss this topic, the same topic five different times in parallel, and then
*  they reach some sort of consensus.
*  And it's actually pretty interesting that different parallel meetings sometimes end
*  up with different suggestions, different decisions.
*  So similar to like if you and I would discuss something, maybe two different days, we might
*  end up with two different outcomes.
*  Right.
*  Similarly with the virtual lab, the nice thing is that we can actually do this more
*  inference computer, basically do more parallel meetings, and then actually explore essentially
*  more different paths of what are the different things that could play out.
*  And then the professor in the end will look across the meeting logs of all these parallel
*  meetings and the professor agent will say, okay, so here's the overall consensus and
*  here's what we should do going forward.
*  So I think in that sense, then these meetings for the virtual lab, it is much faster and
*  much more efficient than some of the physical meetings that we can have.
*  The cost is, I would say, actually relatively small.
*  I would say probably all of the meetings, if you look at essentially like all the words
*  are spoken by different agents, at least in terms of the open AI API cost, I think I would
*  say it's probably like less than $100.
*  Well, yeah, safe to say that's at least the two orders of magnitude reduction.
*  What would I guess, could you even project what this would have taken if you were going
*  to try to do it on a purely human basis, like how much longer or how much more cost or whatever
*  kind of other relevant dimensions of comparison?
*  It's a good question.
*  I think it would definitely have taken much longer.
*  And if we basically extrapolate based on the human resource cost of having a team of protein
*  scientists doing this, that would actually be much more expensive.
*  But perhaps the other thing is that it's not really clear that the human team would have
*  ended up with similar designs, similar workflows, because these are actually very hard problems.
*  For example, some of these recent variants like JN1, variant of SARS-CoV-2, there's not
*  actually a great binder to that, even though there's certainly a lot of people who have
*  been working on these things.
*  That's a very important problem.
*  But the Virtual Lab, I think, shows the side nanobody shows quite a promising binding profile.
*  But I do want to give the caveat that I think we need to do a lot more experimental testing
*  to really validate these.
*  But at least based on the initial ELISA experiments, it looks very promising.
*  Could you hazard an estimate on how much of the, again, you could break this down by like
*  wall clock time or compute resources or just like dollars and cents cost goes to the language
*  models versus to these special models, your ESMs and alpha fold, multimers and rosettas?
*  Because I could imagine that that could be now the slow part given just how fast the
*  language models work.
*  Yeah, absolutely.
*  I do think that a lot of the time for the Virtual Lab is actually, for example, running
*  alpha fold, because you need to run that across many different instances of proteins, candidate
*  nanobodies, and that actually would take multiple days just to potentially just do one round of
*  running alpha fold predictions across all of these different candidates.
*  And certainly, I mean, the biggest cost is still the experimental validation.
*  Right.
*  So it took a few weeks to basically, you have to synthesize these nanobodies.
*  So we use some basically CROs to make these proteins.
*  And then we have to actually do careful experiments to validate those proteins, their binding
*  affinities.
*  And this is where we work very closely with our collaborators at the Chantz-Laguerberg
*  Biohub, who are actually experts in doing these protein affinity assays.
*  And so that's where there still needs to be a lot of human time involved.
*  Although if I understand correctly, there are major projects in automated lab work that
*  might be turning that into a sort of as a service sort of option as well.
*  Right.
*  I mean, you could imagine, tell me if you think I'm missing something, but it seems
*  like in the not too distant future, the AIs could make effectively an API call to even
*  run those like wet lab validations too.
*  That's right.
*  Yeah.
*  So I think in parallel, we have also explored different collaborations with different cloud
*  labs where they would actually do like you have robots that can automate different
*  experiments.
*  Those are also very exciting, especially for these more chemistry experiments and
*  experiments like binding assays.
*  I think that can be automated throughout the world, where it becomes still somewhat
*  challenging.
*  I think assets that involve like cells and animals, those are more complex experiments.
*  But I think the automation will get there for these even cellular based assays.
*  Yeah.
*  Okay.
*  Wow.
*  So this is a space to watch.
*  Are you, I guess, where do we go from here?
*  Are these nanobodies actually going into some downstream like preclinical validation or
*  are they promising enough that people are going to actually pick them up and try to
*  make them a part of actual human life?
*  So yeah, so I think it is quite interesting candidates, but we need to do a lot more
*  experiments.
*  For example, we're currently doing some additional experiments where we have like the
*  virtual lab now look at the first round of the experimental validation and see do they
*  want to further modify or improve the nanobody in some way.
*  So this is actually sort of interesting.
*  It's not quite interesting because now the virtual lab has seen the real world experiments,
*  the real world grounding.
*  Now it can basically figure out what to do in the next step.
*  Yeah.
*  Okay.
*  And never a dull moment.
*  I'm sure you've heard, if not read yourself, Dario Amadei's recent essay Machines of Love
*  and Grace, where he projects that we might get a compressed century of scientific discovery
*  where maybe in the next five to 10 years, he estimates we could see as many platform
*  discoveries in biology as we would have seen if it was purely humans doing the work over
*  say a hundred years.
*  And obviously if that were to happen, that would be a major paradigm shift and impact
*  just about every aspect of life.
*  How realistic does that feel to you coming out of this project?
*  I think we're definitely in a very exciting time, right?
*  Where this intersection of advances in AI, especially around agents and reasoning models,
*  and those advances in biotechnologies.
*  So now we have different, better ways of perturbing the cell, better ways of measurements.
*  That convergence, that intersection is extremely exciting.
*  It's hard to know what will happen a hundred years, it's like a long time to project.
*  But I do think that even in the next five, 10 years, there'll be a lot of really exciting
*  problems that we can tackle with this, using these kind of tools.
*  Are you guys releasing the code and prompts for this stuff?
*  Or is that going to have to wait for V2?
*  What's the outlook for others to be able to start to build on what you've already created here?
*  Yeah, so we actually made the virtual lab open source.
*  So it's already available.
*  If you first look up my group's GitHub page, it's all out there.
*  Cool.
*  Great.
*  Well, I think it's time to switch gears to InterPLM.
*  So impressive.
*  If I may just add one more thing about the virtual labs, maybe just the last thing I'll say is that
*  so far, we mostly talk about it as here's the research you could do.
*  But the other part I find very interesting is just to see what kind of social dynamics evolve
*  with the virtual lab.
*  Because initially, we set it up to mirror my actual group meetings,
*  the meetings and individual meetings,
*  just because that's how we know how to do things as human researchers.
*  But then we also can see over time, maybe the virtual lab will actually evolve their own
*  meeting structures.
*  And maybe they can actually teach us what's a more efficient way of doing science.
*  And that itself, that's almost like a sociology aspect of this could also be fascinating to follow.
*  Are there any observations that you would highlight that suggest possible changes to your
*  own lab workflow or anything like that?
*  Well, one thing that's kind of interesting is that every meeting we have this critic,
*  AI critic, whose job is to basically provide constructive feedback to everything that's
*  been said.
*  And sometimes the different agents, they do disagree with each other.
*  And then, of course, the language models, they're very nice about it and very polite.
*  And then they have to somehow resolve their disagreement.
*  But one thing that's kind of interesting is that these language models, because of RHF,
*  they're actually tends to be overly polite, I think.
*  And especially the critics, sometimes for me, we do want the AI critic agent to be a little bit
*  harsher, a little bit not mean, but a bit more direct and say, oh, yeah, this is a bad idea.
*  And right now, it's almost like a very friendly social dynamics.
*  But I would be curious to see, almost use this as a test by the sea of if we do have a more
*  aggressive critic who's not worried about hurting the feelings of the other agents,
*  would that actually be more or less productive science?
*  Yeah, I can imagine a lot of criticism people may think in their heads go unsaid in a lot of
*  actual human lab meetings.
*  So I can understand how that might be quite valuable to just get more of that critical
*  commentary on the table earlier in the process.
*  Cool.
*  OK, so let's change gears then to enter PLM.
*  So I'll just kind of tee you up for this because, again, not a ton of time.
*  And it's a really fascinating paper I've been looking at for this.
*  We've done multiple different episodes in the past on Sparse autoencoders,
*  covering a few of the seminal papers out of Anthropic.
*  I've had a couple of the co-founders of GoodFire AI, which is a startup that's focused on
*  bringing SAEs to different modalities.
*  And so we've got some kind of background content that should, you know, if people want to, if they
*  don't have the context, they can go back and listen to the context on SAEs.
*  Let's start with maybe a primer on ESM2, which is the model that you studied here.
*  And then kind of what was different about doing an SAE for a protein model as opposed to a language
*  model, which is obviously more familiar to most people.
*  And then what came out of it.
*  There are a couple of like very interesting, I dare say discoveries that came out already of this
*  SAE interpretability work on the protein language model.
*  So go for it.
*  Yeah.
*  Yeah.
*  Well, thanks for that context.
*  So as you mentioned, there's a lot of exciting developments recently around using Sparse autoencoders
*  as a way to extract meaningful concepts, basically, that are learned by large language models,
*  right, like GPT-style models.
*  And what we wanted to do is to see, can we actually use these similar ideas to apply that
*  to like a protein language model?
*  So I already mentioned ESM in the context of the Virtual Lab.
*  It's actually one of the tools that's used by the Virtual Lab agents, but it's basically
*  like a protein language model that's trained over this universe of different protein sequences.
*  So the idea there is that you can view actually each amino acid sequence of a protein as being
*  like a sentence where the characters or the words are now at different residues of the
*  amino acid.
*  And then people would train similar kind of transformers using masking on top of those
*  sentences of proteins.
*  And that's shown to be a very powerful approach because similar to how with human language,
*  right, there's a lot of hidden grammars and things with the protein.
*  And these protein language models like ESM, because they've been trained over evolutionary
*  scale data, they can sort of capture those intrinsic and hidden grammars of proteins
*  within its embeddings.
*  And this is where also then starts to diverge a bit from the human models.
*  Because the human model, we sort of have a pretty good idea of how to interpret what
*  are the concepts that are learned by a GPT-style human language model, right.
*  We know the concept like Golden Gate Bridge.
*  You can see other particular neurons in a transformer that corresponds to the Golden
*  Gate Bridge.
*  But where it's sort of fascinating with the protein language models that there are some
*  concepts that we know.
*  Maybe I know a particular kinds of protein domain I can see, okay, does that show up
*  somewhere in that protein language model?
*  But I would say actually most of the concepts are probably not known to us, right.
*  There's sort of we don't have a good description about what are these concepts.
*  And this is where I see these interpretation of a protein language model, not just being
*  like an exercise in mechanistic interpretability, but actually as a sort of exercise in scientific
*  discovery.
*  Because I think there's actually a goldmine of new concepts that are potentially learned
*  by this protein language model training over these evolutionary scale data that we still
*  not actually have good human analogs for.
*  And if we can actually go in and look at different layers and use SAEs to piece apart and hear
*  the different new concepts and then validate those concepts, then they can actually become
*  really a goldmine of new biological insights that the model can teach us.
*  Yeah, I think that point can't really be overstated in terms of its importance.
*  And I've been kind of banging this drum for a little while in anticipation of exactly
*  this sort of result.
*  So just to state it back, right, there's a lot of sort of understandable confusion, I
*  think, when people look at what is happening in language models and they're like, well,
*  first of all, do these things reason or not?
*  No, they don't.
*  Well, yes, maybe they do.
*  But even if they do, well, they're just learning all those concepts from us anyway.
*  So the sort of frontier of the debate right now or the current kind of battle lines,
*  if you will, on the can they, can't they is often like, can they figure out new concepts
*  or are they only able to learn the concepts that we have learned and represented in our
*  language?
*  And this sort of result in a totally different domain where you're starting to see concepts
*  that we clearly just don't know.
*  And nevertheless, the techniques are able to isolate and allow us to then make biological
*  discoveries from the study of what is coming out of these interpretability techniques.
*  That both drives a ton of biological value and I think has major implications for the
*  future of AI in general.
*  Just to put a fine point on it, is there any doubt in your mind at this point that these
*  models can learn concepts that humans don't know from the raw data?
*  Yeah, I think especially in these more specialized domains like proteins or biology,
*  there's a very clear limitation of what we have written down in words in description.
*  Like I look at all the protein databases, people have annotated different concepts,
*  but everybody recognized that we're limited in what we have annotated.
*  There are a lot of things that we just haven't annotated.
*  And I think to your point, this is a really exciting opportunity where these protein
*  language models, I think they have learned new concepts.
*  They have filled in some of the gaps in our knowledge and now it's our job to see can we
*  extract those out using techniques like SAEs.
*  Yeah, I think that is so fascinating and exciting and enlightening all at once.
*  One really quick fine point question on the original protein language model that's being
*  studied here.
*  Am I correct in understanding that it is trained purely on sequences?
*  There's no structural data in the training data for that language model.
*  Is that right or did I miss it?
*  That's right.
*  Yeah, that's right for these ESM models.
*  Okay, so that makes it quite remarkable.
*  I was also amazed by how small these models seem to be.
*  The protein model seemed to be small.
*  There were only 10,000 features in the sparse autoencoder that you use.
*  This compares to millions and millions that they're doing with Claude.
*  I would love to get a little bit of more color on how this relates to the ultimate magnitude.
*  Do we expect 10,000 features to be enough to characterize proteins that seem small to me?
*  But then I was also surprised to learn in the paper that of those 10,000 possible features
*  that the SAE could learn, about 2,500 were deemed to be human interpretable.
*  I would have expected that we would have more than that.
*  But again, I just don't have a great background in biology.
*  So maybe this space of concepts in proteins is actually maybe just smaller than I would have guessed.
*  It's an interesting question.
*  In some ways, I think that the proteins is a more constrained space than the entirety of human language.
*  With human language, there are so many things you can talk about outside of science.
*  But in all these other domains, it could be code, it could be talking about different images.
*  So I think there is actually a lot of diversity of information.
*  But if I just look at only the language of proteins, in some ways, it is the more narrow domain.
*  That being said, I think we are in some sense scratching the tip of the iceberg.
*  And something that we're actively working on now is also applying these approaches to larger protein
*  language models. For example, we're also applying that now to alpha fold models,
*  where there's actually more structural information and those models are larger.
*  And I think there's actually going to be even some additional concepts
*  that we'll be able to extract out from these different models.
*  Yeah, it's all going to get even more interesting with scale.
*  So the features that were found, there were features that corresponded to specific sequences
*  within a protein. And there's great visualizations of this in the paper. So I definitely
*  encourage people to just open up the paper and look at it. But there are features that seem to fire
*  for kind of a stretch of the amino acid sequence. And you can just see like, okay, that's that part
*  of the protein. Then there's ones that are more structural, which is like they might be in
*  different... If you were to pull the thing into one linear sequence, they would be at different parts.
*  But in the way that they fold up, they come together. And so in that sense, they're structural
*  and not purely sequential. And that's remarkable in that, again, it's learning this with the
*  original protein language models, learning this without any structural information.
*  That's remarkable in itself. Then there was kind of conceptual features, which were like
*  fired for sort of entire proteins that seem to group them into kind of different
*  roles or kind of classes, I guess. I don't know if I missed any there.
*  There were also interesting findings around doing sort of an auto labeling process and looking at
*  the labels that we know apply to different proteins and then looking at what was predicted
*  by the firing of features and realizing that actually there are some gaps in our databases
*  that we were able to fill in based on where the features were firing. And then I thought maybe
*  the most interesting thing, and maybe this is where I'd love to get your comments the most,
*  was on the discovery of new motifs. I'm not sure if it was one or more new motifs,
*  but that was really striking in as much as a motif is a physical kind of part of a protein
*  that recurs in different proteins throughout nature. With a small protein language model
*  and a relatively small sparse auto encoder and purely sequential data underlying all of this,
*  no structural information yet, to identify entirely new motifs struck me as just like
*  a really remarkable result. So help me as somebody who is maybe a little
*  excitable and doesn't have a great foundation in biology, should I be more excited? Should
*  I be less excited? Help me just calibrate myself to that finding.
*  Well, I'm glad that you are excited about this work. And thank you for that very nice overview
*  and summary of it. So we created this website, interplm.ai, which is actually this interactive
*  website. So actually I encourage everybody who's interested, you can just go on there
*  and you can actually sort of explore all of these different kinds of motifs yourself.
*  And you can look at what are these 3D structures that are learned and it's that kind of interactive
*  way to visualize each of the concepts that are learned by this AI model. And maybe I'll just
*  highlight one thing that you mentioned, which is relates to how do we systematically annotate all
*  these new concepts, because some of these might be new concepts and some of these might be extensions
*  of existing ones. And this is where I think sort of like a convergence of different technologies.
*  But I also find that we found that actually here, this is actually a good use case of a large language
*  model. Here we actually use cloud to try to help us to automatically annotate some of these new
*  concepts by pulling relevant information from different databases and comparing what's known
*  about the proteins versus what's being activated by each of these concepts. So I think this is
*  actually where there could be an interesting convergence of the two things that we talked
*  about, where maybe you can imagine having a virtual lab of different experts, agents,
*  and can help us to interpret what's going on behind the hood of this large protein language model.
*  And how common is it to discover a new motif? Is that something that happens all the time or is that
*  rare? I mean, should we be surprised to see that this technique would identify new motifs?
*  I think we were sort of expecting that there would be new motifs, new concepts that are learned by
*  this protein language model beyond what we have currently annotated. I think that was our prior
*  going in and one of the motivations because the models have learned on so much data and because
*  we know that there are some existing limitations in our current annotation databases.
*  We know that there are some existing limitations in our current annotation databases.
*  But if I just, you know, forgetting about all the details of the AIs,
*  if we just looked at the literature and said, how often are new motifs reported? Are we getting new
*  motifs on a daily, weekly, monthly basis? What is the sort of stream of new motif discovery?
*  That, I don't think it's that frequent.
*  Yeah, I would have guessed not. It seems like they can't be, we can't be like swimming around
*  in motifs that we're not recognizing. So it did seem to me like it couldn't be that frequent. So
*  that does make it all the more remarkable to see AIs doing it. Okay, last maybe question or two
*  before we break. Are there limitations to this? I mean, when I talk about my kind of excitement
*  about biology, I get all sorts of different responses where people kind of try to temper
*  my expectations. One that comes up often is like, well, you know, decent amount of proteins are
*  sort of disordered and like fundamentally chaotic. And, you know, those are going to be impossible
*  to make sense of with any technique. You know, you can fill in the gaps for other reasons that
*  people might doubt the pace of progress going forward. What is your expectation for what
*  limitations or what, you know, sort of the near term pace of progress might be given these new
*  techniques? Yeah, it's a good question. I mean, I think for certain domains of proteins and
*  protein interactions, the small molecules were still, let's say data limited rather than compute
*  limited. And that's where even like, what's the alpha four three and the latest models,
*  they still make mistakes on some of these, let's say this water proteins were looking at specific
*  interactions domains. So I think that I expect that's the areas where we'll need to see a lot
*  more data and more experimental data to like validate and improve the models. The flip side
*  of this is I would say that even with the existing models, I do think that there is already a gold
*  mine of new concepts and knowledge that are already hidden in existing models. That's even
*  if we can extract those out, I think that would already teach us a huge amount of interesting new
*  insights. Do you have a sense for whether we can go multi scale with this? That's the other thing
*  that always kind of comes up is like, well, you might be able to do, you know, molecular scale,
*  but you've got cell scale and tissue scale and system scale and organism scale. What is your
*  expectation for the prospects of creating similar techniques that maybe bridge those orders of
*  magnitude? I think that would be extremely exciting and transformative. So the reason why
*  the proteins have been making a lot of progress in that space is in some sense,
*  it's not simple, but it's also a relatively self-contained unit of analysis. But ultimately,
*  especially when it comes to human disease, human health, what we care about is really things at a
*  larger scale level of cells, also organs. And at that point, that's actually a bunch of other
*  research projects we're doing in my group. So maybe we can have another discussion about those.
*  I think that's also the area where there's been a lot of really exciting progress.
*  Cool. Well, definitely we will be watching this space. I mean, congratulations on two
*  quite different projects, but each of which in my judgment on its own would have been very high up
*  the power rankings of things that people should be paying attention to. So I expect more great
*  things from you and your colleagues in the not too distant future based on what I've seen here.
*  James Zou, Professor of Biomedical Data Science at Stanford and Investigator at the Chan Zuckerberg
*  Initiative. Thank you for being part of the cognitive revolution. Thank you so much for
*  having me. I really enjoyed it. It is both energizing and enlightening to hear why people
*  listen and learn what they value about the show. So please don't hesitate to reach out via email
*  at tcr at turpentine.co or you can DM me on the social media platform of your choice.

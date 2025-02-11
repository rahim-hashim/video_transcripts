---
Date Generated: December 03, 2024
Transcription Model: whisper medium 20231117
Length: 6884s
Video Keywords: []
Video Views: 754
Video Rating: None
Video Description: In this episode of The Cognitive Revolution, Nathan explores groundbreaking perspectives on AI alignment with MIT PhD student Tan Zhi Xuan. We dive deep into Xuan's critique of preference-based AI alignment and their innovative proposal for role-based AI systems guided by social consensus. The conversation extends into their fascinating work on how AI agents can learn social norms through Bayesian rule induction. Join us for an intellectually stimulating discussion that bridges philosophical theory with practical implementation in AI development.

Check out:
"Beyond Preferences in AI Alignment" paper: https://arxiv.org/pdf/2408.16984
"Learning and Sustaining Shared Normative Systems via Bayesian Rule Induction in Markov Games" paper: https://arxiv.org/pdf/2402.13399

Help shape our show by taking our quick listener survey at https://bit.ly/TurpentinePulse

SPONSORS:
Notion: Notion offers powerful workflow and automation templates, perfect for streamlining processes and laying the groundwork for AI-driven automation. With Notion AI, you can search across thousands of documents from various platforms, generating highly relevant analysis and content tailored just for you - try it for free at https://notion.com/cognitiverevolution

Weights & Biases RAG++: Advanced training for building production-ready RAG applications. Learn from experts to overcome LLM challenges, evaluate systematically, and integrate advanced features. Includes free Cohere credits. Visit https://wandb.me/cr to start the RAG++ course today.

Oracle Cloud Infrastructure (OCI): Oracle's next-generation cloud platform delivers blazing-fast AI and ML performance with 50% less for compute and 80% less for outbound networking compared to other cloud providers13. OCI powers industry leaders with secure infrastructure and application development capabilities. New U.S. customers can get their cloud bill cut in half by switching to OCI before December 31, 2024 at https://oracle.com/cognitive

RECOMMENDED PODCAST:
Unpack Pricing - Dive into the dark arts of SaaS pricing with Metronome CEO Scott Woody and tech leaders. Learn how strategic pricing drives explosive revenue growth in today's biggest companies like Snowflake, Cockroach Labs, Dropbox and more.
Apple: https://podcasts.apple.com/us/podcast/id1765716600
Spotify: https://open.spotify.com/show/38DK3W1Fq1xxQalhDSueFg

CHAPTERS:
(00:00:00) Teaser
(00:01:09) About the Episode
(00:04:25) Guest Intro
(00:06:25) Xuan's Background
(00:12:03) AI Near-Term Outlook
(00:17:32) Sponsors: Notion | Weights & Biases RAG++
(00:20:18) Alignment Approaches
(00:26:11) Critiques of RLHF
(00:34:40) Sponsors: Oracle Cloud Infrastructure (OCI)
(00:35:50) Beyond Preferences
(00:40:27) Roles and AI Systems
(00:45:19) What AI Owes Us
(00:51:52) Drexler's AI Services
(01:01:08) Constitutional AI
(01:09:43) Technical Approach
(01:22:01) Norms and Deviations
(01:32:31) Norm Decay
(01:38:06) Self-Other Overlap
(01:44:05) Closing Thoughts
(01:54:23) Outro

SOCIAL LINKS:
Website: https://www.cognitiverevolution.ai
Twitter (Podcast): https://x.com/cogrev_podcast
Twitter (Nathan): https://x.com/labenz
LinkedIn: https://www.linkedin.com/in/nathanlabenz/
Youtube: https://www.youtube.com/@CognitiveRevolutionPodcast
Apple: https://podcasts.apple.com/de/podcast/the-cognitive-revolution-ai-builders-researchers-and/id1669813431
Spotify: https://open.spotify.com/show/6yHyok3M3BjqzR0VB5MSyk
---

# Beyond Preference Alignment Teaching AIs to Play Roles & Respect Norms, with Tan Zhi Xuan
**Cognitive Revolution:** [November 30, 2024](https://www.youtube.com/watch?v=Y21syyyABOs)
*  What we argue in a paper beyond preferences and AI alignment, we are really trying to
*  critique this sort of preferences view. So we go through all the limitations of taking this sort
*  of expected utility maximization view of both human rationality and AI alignment too seriously.
*  People know that this learned utility function you try and learn from preference data doesn't
*  perfectly capture what people really want. And that leads to issues of over optimization,
*  because it is a bad proxy for what humans might supposedly really want in that context.
*  Over optimizing it is not going to get you there. I prefer thinking in terms of like,
*  what would it take to like automate the industrial economy or like automate 50 to 80%
*  of the existing industrial economy, because I think more industries will come to exist in the
*  future. If that's the way of thinking about AI, right, then I think we are not going to get there
*  for like a decade or two. When building moral systems, there's a basic kind of minimal morality
*  that the system should comply to, which is like meet the minimum moral standards that society would
*  agree to allow you to operate. And that's sort of like going to be filled in by this sort of
*  contractualist picture. And I think constitutional AI is closer to that.
*  Hello, and welcome back to the Cognitive Revolution. Today, I'm excited to share
*  a conversation on AI alignment that spans the fields of moral philosophy, cognitive science,
*  and Bayesian probabilistic programming. My guest is Tangjie Shen, a PhD student at MIT,
*  whose work questions the assumptions that underlie today's most popular AI alignment strategies,
*  and also proposes novel technical implementations by which AI agents might learn social norms from
*  examples in their environments. We begin on the philosophical side with Shen's recent paper,
*  Beyond Preferences in AI Alignment, which critiques the prevailing preferentist paradigm.
*  That is the idea that AI systems should be aligned to satisfy human preferences through
*  techniques like reinforcement learning from human feedback, arguing that because human
*  preferences are often inconsistent and difficult to aggregate across populations,
*  preference maximization may simply be the wrong framework for AI alignment. And in any case,
*  today's AI systems aren't really being trained as pure preference maximizers anyway. Instead,
*  they argue for an approach whereby AI systems are designed to play specific roles, with clear
*  normative standards and constraints that emerge through social consensus, much like how human
*  professionals are expected to uphold certain standards, regardless of their or their clients'
*  personal preferences. To better understand this view and its implications, I bring a number of
*  different moral philosophies and alignment strategies into the conversation, asking Shen
*  to explain how their proposal compares and contrasts with each. While hardly the final
*  word on AI alignment, I do think Shen's ideas deserve serious consideration. If nothing else,
*  by thoughtfully combining Eastern and Western traditions, they contradict prominent claims of
*  incompatibility between US and Chinese approaches, including from no less than Sam Altman, who
*  recently wrote in a Washington Post op-ed about the relationship between Western and Chinese
*  governance of AI that, quote, there is no third option. In the second half of this episode,
*  we shift gears to discuss Shen's much more technical paper, Learning and Sustaining Shared
*  Normative Systems via Bayesian Rule Induction in Markov Games. In this project, they demonstrated
*  an approach that allows AI agents to infer social norms by noting apparent deviations from purely
*  self-interested behavior in other agents. For example, if an agent repeatedly sees other agents
*  passing on opportunities to obtain resources, it may infer that there is a rule or norm governing
*  that behavior and begin to incorporate compliance with that rule into their own decision-making.
*  This creates a mechanism for norms to emerge and to sustain themselves across generations of agents,
*  allowing whole populations to effectively cooperate to avoid tragedy-of-the-commons-type
*  problems like overfishing and other resource depletion. Shen's work exemplifies an important
*  goal that I have in making this show, to understand AI from all angles, exploring not just what
*  beneficial AI might look like in principle, but how we might actually begin to build it in practice.
*  If you're finding value in the show, we'd of course appreciate it if you take a moment to
*  share it online, write a review on your podcast app, or leave us a comment on YouTube. And we
*  always welcome your feedback and guest or topic suggestions either via our website,
*  cognitiverevolution.ai, or by DMing me on your favorite social network.
*  Now, here's Tanji Shen on AI alignment philosophy and application. Tanji Shen, PhD student at MIT,
*  researching AI alignment, probabilistic programming, and cognitive science. Welcome
*  to the Cognitive Revolution. Very happy to be here. Thanks, Nathan.
*  You have caught my attention with a number of interesting research papers and points of view
*  that you've shared online. And so I'm glad that we're finally making this happen. What I really
*  want to do is dig into especially two papers that you've put out this year. One is, I mean,
*  you can characterize it perhaps better than me, but I would say sort of a survey of the prevailing
*  approaches to AI alignment in the big picture, and also kind of why you think a lot of them are
*  ultimately not going to work out right, and what you think the right alternative should be.
*  And then I also really want to get into some of the more technical work that you've done,
*  where you've actually created instantiated compute driven environments where little agents run around
*  and actually learn various forms of alignment and good behavior from one another. And I love it when
*  people bring together both the kind of philosophical and big picture angle, but also are really down in
*  the weeds trying to implement. So hopefully we can cover those both. Yeah, for sure. Yeah. And
*  it's always been important for me, I think, to sort of bridge over the philosophical discussions
*  I think have been happening for a long time, but really trying to translate them for a more
*  technical audience. Right. Because I do think a lot of things, I love these ideas just don't get
*  across because of lack of translation. And that was in large part what this recent survey paper
*  was trying to do. Yeah, totally. It's getting real now in brief, right? So just for starters,
*  I actually normally don't even ask people too much for background. A lot of entrepreneurs or
*  whatever, when I do that, they're like, oh, well, chat GPT came out and I realized that I was going
*  to be a big deal. And so I decided to start a company. But I do think that so much of the
*  AI discussion in general is kind of like myopic or just very narrowly focused. You come from the
*  other side of the world, Singapore originally, if I understand correctly. And I'd love to just
*  hear a little bit about your background with apologies to Tyler Cowen. I always remember him
*  saying all thinkers are regional thinkers. So I'd love to just hear a little bit of your backstory,
*  how you got into this and to what degree and how you think your background on the other side of
*  the world from where we are now is has been relevant in shaping your thinking. Yeah, for sure.
*  Yeah. And I do think this Tyler Crowe quote is true of me to some degree, I guess. And then I
*  do think in fact, all thinkers are regional thinkers, whether they realize it or not.
*  As for how that's influenced, there's such a long story of how I got into AI safety and alignment.
*  There are many ways in which that story is not a very different one from a lot of people in the
*  field. Like I did my undergraduate degree in the US and I encountered an effective altruist club as
*  part of that actually ran it for a bit despite, you know, always having been slightly too leftist
*  to really buy in fully to effective altruism. And that's when I encounter a lot of ideas around
*  safety and alignment. And basically the way I describe it is like I wasn't necessarily
*  convinced of the sort of moral argument for working on this as the most important thing
*  from an effective altruist point of view or like utilitarian point of view. But it just
*  seemed like a really interesting question because I was already a big fan of moral philosophy
*  and this project of like, okay, how could you begin to computationally model value learning?
*  Like what does it mean to specify a computational process for learning human values? How do people
*  do that? That kind of basically nerds now to me into working in the field. But I think the
*  way I've approached that question has been influenced, I think, I don't know, by perhaps
*  sort of my cultural slash political national background in various ways. Like I do think of
*  myself as a post-colonial thinker, I suppose, and part of that manifests in a sort of like general
*  distrust towards Western philosophy and Western slant or philosophy as a sort of sole source of
*  like philosophical knowledge about like what could possibly be relevant to thinking about how to
*  align AI. And so I think sort of a nice representation of that sort of use actually,
*  I gave a talk maybe almost like five years ago now on sort of the relevance of philosophical
*  pluralism for AI alignment, how ideas from say Buddhist philosophy or Confucian philosophy
*  could be relevant to thinking and talking about like what it means to align AI systems with human
*  values. And that's probably it's one of the most sort of important bits. I think the other bit
*  that I think influences more of my politics as opposed to like moral philosophy is that I
*  think growing up in a state capitalist country like Singapore, I think if you're not someone who
*  basically buys into that system, I think you realize that the flaws of that system don't
*  confy it's scribe to like state or capital on its own. It's like really a sort of particular
*  intertwining of those kinds of elite interests that creates problems like injustice and inequality.
*  And I do think that tends to lead me to favor solutions for alignment that look more decentralized
*  as a basic political value and also as a sort of like empirical sort of skepticism about like
*  which is the state doing things all that well. So I think those things probably influence.
*  S2 That's really interesting because I feel like we are in the United States sort of headed for
*  a more state capitalist civil military fusion, if you will. I don't necessarily like that. In fact,
*  I have major misgivings about, I would say, probably pretty major elements of it. But that
*  does seem to be the prevailing trend. And certainly Singapore is like very often cited as the model
*  that we might learn from. Could you give us just a little bit more on like, because I would have
*  anticipated where the end of that was going to go was like more trust in the government or like
*  at least more positive vision for what the government could do well. S1 Yeah, I think a lot
*  of Singaporeans go in that direction. And I'm just like relatively rare among that population,
*  you know, or like not all that rare. I'm just like one of the more anti establishmentarian ones.
*  And there isn't really a right and left in Singapore, right? It's just like kind of the
*  establishment and the sort of like people who critique establishment. And I think,
*  I don't know. I mean, I think there's a lot to say for having strong state control of the economy.
*  If you have competent leaders, and if you trust that a system can reliably produce competent
*  leaders who are fair and aren't corrupt and don't act in your own interest, I just think that it's
*  sort of not really likely for that to be a very stable situation. I think that's not how it's
*  played out in most other countries where sort of the state has very strong power. And I think,
*  in so far as Singapore is an example, as a counterexample, I think it's mostly luck.
*  And I do think that there's a lot of like, basically, if you take things like certain
*  kinds of civil liberties, or certain kinds of rights, I don't really like thinking of things
*  in terms of rights, but like unacceptable sort of things like political imprisonment for more than
*  10 years, right? If you think that is unacceptable to build a society like Singapore's, that's already
*  going to push you in the direction of like, whatever the benefits this pre-ungoverned country
*  has been, it's not going to be worth the cost, certain kinds of costs. Yeah.
*  Well, here's to hoping that current leadership in US and China prove to be a Lee Kuan Yew,
*  rather than what I fear they might turn out to be. But yeah, that's fascinating perspective.
*  Yeah. And I think part of what I was just referring to is like, I think Lee Kuan Yew made choices that
*  many people in the West would consider absolutely unacceptable in order to establish power. Yeah.
*  Okay, cool. Well, changing gears, but also just kind of setting a foundation for the
*  core of the discussion. I would love to get your outlook for the near term future of AI in terms of
*  especially how powerful you think systems are likely to become. And I ask that because I think
*  a lot of people's downstream opinions very, or could change if they saw that like initial question
*  differently. So are you like a AGI 2026 or how would you describe yourself?
*  Right. Yeah. First of all, I guess, like, I don't even really like the concept of AGI. I think it's
*  sort of too amorphous to like really pinpoint like what we're talking about. And I don't know,
*  I kind of prefer thinking about things in terms of like, would really be impactful as like,
*  why would it take to like, automate the industrial economy or like automate even like
*  50 to 80% of the existing industrial economy, because I think more industries will come to
*  exist in the future. In principle, like not even actually, because I think there are a lot of like
*  regulatory or whatever kinds of societal reasons why a lot of technology we develop won't actually
*  be deployed. And if that's the way of thinking about AI, right, then I think we are not going
*  to get there for like a decade or two is my guess or more. I do like in principle believe it's
*  possible to automate a lot of the existing industrial economy and a lot of the cognitive
*  work that goes into running it within the century. But it does seem to me that a lot of the sort of
*  particular predictions or beliefs of companies, large AI companies like OpenAI are sort of firstly
*  predicated on the particular vision of what AGI means. And also even within that to me too
*  optimistic. That's sort of the broad view, I guess. I mean, I think that's one way of anchoring about
*  that. And the way I think about that is I thinking about particular sectors of the global economy.
*  And that way I have better intuitions about how long it would take. And I just think, for example,
*  so much of the global economy is still of a form of mental labor, right, like physical labor. But
*  that is a hard intelligence problem to solve. I think people really underrate how much of human
*  and animal intelligence was dedicated to solving hard motor tasks, right? Like we need a lot of
*  motor intelligence to solve that. And I think what has kind of happened by people defining AGI to
*  talk about cognitive labor, whatever that means, is that they've kind of gerrymandered out most of
*  robotics when that's such a firstly such an important part of what you might think of as
*  human intelligence. And secondly, I think a really important part of the global economy. And it just
*  doesn't seem like we're on track to solve much of that problem for at least a decade or two,
*  from my perspective. And then I think there are a lot of other areas we could talk about.
*  I think the sort of like area is a particular economy niche, I suppose, that a lot of AI companies
*  seem to be focused on when you're trying to achieve something like AGI. I think they're much
*  more actually focused on people use metaphors like drop in remote workers, right? I don't know what
*  is the metaphor like a sort of like rough sense of like what will be achieved. Or they also talk
*  about I can't remember what Dario Omede's sort of metaphor was recently, like a country of geniuses
*  in a data center, or something like that. And I think that's pointing to a particular set of
*  cognitive capacities, both of them slightly different ones, that I do think we are seeing
*  a lot more progress on those things. But to me, there's a big open question, whether that's going
*  to happen, either of them is going to happen anytime soon. Like one of them is like sort of
*  science, like country of geniuses in data center, just like that's automating science, essentially,
*  of a certain kind, or automating a sort of like idea generation, parts of science, at least,
*  and experimental planning. And of course, you still have to like do all the stuff with the actual
*  machines and run the experiments. And that's going to be slow. And the remote workers stuff,
*  I think of as, okay, all the sort of like, tasks, general cognitive tasks, a remote worker does have
*  to do on a computer, say, in order to achieve certain job. And I'm even on that sort of simpler
*  task, right? I think automating science is very hard. I'm not convinced we're going to get there
*  anywhere close by 2020, I'd say. But even on that simpler task of like automating an office worker,
*  a remote office worker, I think this really depends on how much we really believe that,
*  like, like a lot of office work needs really high reliability. And it does seem to me the
*  current paradigm of scaling AI systems based on large language models are not on track to achieve
*  like the 95, 99% reliability levels you might want from doing that kind of job, right? If the
*  standards of reliability happen to be looser, then it might be the case. And I think some kinds of
*  roles are in that way. Like if you're just taking talking about like copywriting, for example,
*  right, I think that kind of work can be automated. But if it's much more precise, or requires certain
*  kinds of standards of precision, then I don't really think that, say, pure language models
*  with a bit of stuff added on are really the right role for the job. And we'll need to see
*  sort of more innovation and sort of hybrid systems in order to get there. And maybe that
*  will happen quickly. But I don't think it's on the default scaling route that I think most people
*  have in mind. Yeah. So that's broadly the picture, I guess. Hey, we'll continue our interview in a
*  moment after a word from our sponsors. As a Cognitive Revolution listener, you're obviously
*  interested in cutting edge AI technology. And with that in mind, I'm proud to say that this episode
*  is brought to you in part by Notion. Notion has been a clear leader in high value applications
*  of generative AI since the wave began. Earlier this year, we had Notion AI engineer Linus Lee
*  on the podcast. The quality of his insights showcased the caliber of talent that Notion
*  employs. And that inside look at how Notion builds with AI is still extremely valuable.
*  Given my personal focus on AI automation recently, I specifically wanted to highlight Notion's
*  library of workflow and automation templates. If you're looking to streamline your processes
*  and lay the foundation for future AI driven automation, these templates are an excellent
*  starting point. And even if you're not ready for full automation, you'll benefit immediately
*  from Notion AI. Notion's latest all in one AI implementation that searches through thousands
*  of documents, regardless of whether they live in Notion or on some other platform like Slack
*  or Google Docs, to deeply understand the context of your work and generate highly relevant analysis
*  and content just for you. Notion is used by more than half of Fortune 500 companies, helping teams
*  reduce emails, meetings, and time spent searching for information. Want to try it? Head to Notion.com
*  slash Cognitive Revolution. You can start for free and using our link supports the show. So join me
*  in giving Notion AI a shot today at Notion.com slash Cognitive Revolution.
*  As a developer, the journey from concept to production ready large language model apps is fraught with challenges.
*  Dealing with unpredictable language model outputs, hallucinations, and ballooning API costs can all be
*  blockers to shipping your next AI powered feature. That's where advanced RAG comes in. With the new RAG
*  Plus Plus course from Weights and Biases, you can overcome these hurdles and build reliable production
*  ready RAG applications. And if you're looking for a more efficient way to do that, you can use the
*  Go beyond proof of concept and learn how to evaluate systematically. Use hybrid search correctly and give
*  your RAG system access to tool calling. Based on 21 months of running a customer support bot in production,
*  industry experts at Weights and Biases, Cohere, and Weaviate show you how to get to a deployment
*  grade RAG application. This offer includes free credits from Cohere to get you started. Make real
*  progress on your large language model development and visit wnb.me slash cr to get started with their
*  RAG Plus Plus course today. That's wnb.me slash cr to get started with their RAG Plus Plus course today.
*  So I think from here I would just like to kind of set up an understanding of the prevailing approach
*  to alignment. As I've read through some of your work, it's brought to mind a lot of different
*  angles on it and I kind of want to bounce a number of them off of you and then ultimately get to your
*  core proposals. And then again, to the technical work that you've started to do to chip away at
*  this obviously massive challenge. You described the main approach today as preferentist and that is
*  essentially saying that we want the AI to do what the humans want them to do to satisfy
*  their preferences. And this is instantiated or sort of embodied in the way that feedback is
*  collected and ultimately the AIs are then trained on increasingly now AI feedback as well, but it's
*  all kind of at root grounded in human feedback. So we have these methods, of course, RLHF,
*  listeners to this podcast will know what that is. And the way that the preferences are collected
*  is either like the AI gives you two responses and you say which one you want, or it gives you one
*  and you rate it from one to seven, these sort of very atomic, I'm a person, the AI has given
*  me something, I'm going to kind of evaluate it and nudge it toward giving me more of what I want.
*  Maybe start off by just, would you characterize that any differently?
*  And then what do you see the big problems?
*  You know, there are a bunch of things going on in the current way that I think alignment,
*  especially like alignment of large language models as the product or kind of the AI system
*  and their sort of descendants. And I do think it's right that basically what you described
*  describes sort of process of how people are going about the practice of how people are going about
*  trying to align these systems, where they're collecting human feedback data often in the
*  form of binary comparisons or preference judgments between two outcomes. And you're being asked,
*  rate, how is this response better or is this response better or worse? Even according to
*  some criteria metric that's specified by the developer or the sort of like trainer, the person
*  who's training the model. And I think the theory, there's a sort of like dominant theory we have for
*  thinking and talking about that. If you read these papers on AI alignment, it's essentially
*  a preferenceist one where the idea is that there's some utility function or some reward function
*  in people's heads that basically captures those preferences, right? It sort of captures like a
*  linear ordering over how good outputs are, right? And people are expressing that linear ordering
*  over how good outputs are by making these judgments. And they're expressing it noisily sometimes. So
*  there is room for noise when they make these kinds of like, there's these Boltzmann rational
*  assumptions and how people may or may not manage to always like pick the best option because we're
*  not perfectly rational. But still the basic assumption is that we have this linear ordering
*  in our head and express it. And we're going to align the AI system ideally to sort of optimize
*  that sort of like underlying linear order or utility function essentially, right? There is some
*  sequence of outputs we want to the AI system to like try and output the best one in general,
*  right? But even though that's the theory, I think the practice of it, sort of better way to understand
*  the practice is that we're not actually doing that. So like we talk about it that way, but that's not
*  what AI like developers, not what we actually want for AI systems. And it's not what AI developers
*  are sort of implicitly doing, which is that first of all, I think quite explicitly, people don't
*  actually try and maximize this learned utility function or reward function to the extreme,
*  right? People know that this learned utility function that you try and learn from preference data
*  doesn't perfectly capture what people really want. And that leads to issues of over optimization
*  because it is a bad proxy for what humans might supposedly really want in that context.
*  Over optimizing it is not going to get you there. And so the AI systems which are trained to
*  maximize the reward function only partly trained, constrained to be close to the original base policy
*  of the original non-fine-team language model to some degree, right? And this process is iterative.
*  So basically you're, you basically keep trying to make the language model a little better in terms of
*  better complying with human preferences, but you're always constraining it to be somewhat
*  closer to the original distribution. And that already is a departure in some ways from the
*  traditional theory, which is like maximize expected utility, right? But another thing we actually
*  argue in the paper we're going to talk about today is that, well, I don't think that, or we don't
*  think that the right way to understand what these systems are doing is maximizing utility at all,
*  right? It's really that the developers had in mind a set of system requirements or normative standards
*  for how they want their conversational AI system to behave, right? They want it to be helpful and
*  to be harmless. That's two very broad kind of vague normative standards. But if you look at,
*  say, something like constitutional AI, they're much more specific ones, right? Like, don't be toxic,
*  try to respond in the way that sort of encourages sort of like reflection or sort of like things
*  like that, right? And they have this whole list of standards and they're either getting people
*  or getting AI systems to make judgments that comply with the standards, right? And they're
*  trying to aggregate those judgments somehow and align the AI system to that, right? So there's a
*  difference between using preference data and measuring it as a way to learn information
*  about these, how to follow these normative standards, right? And treating preferences
*  and alignment target. And what our paper is trying to do is really critique the idea that preferences
*  should be the alignment target as opposed to merely data we can use to learn about the things
*  that humans really care about, right? So that's sort of like my sort of broad response to like how
*  I think about what people are actually doing nowadays, right? And there's a sense in which
*  like the way we're thinking and talking about the actual practice is a bad one and we're doing
*  something else that's a richer, we're doing this richer thing where we're not realizing we're doing
*  this richer thing. Yeah. So let me try to articulate that back to you because I think
*  there's a number of objections that people often have or concerns that people often have about
*  RLHF type training processes. And it seems like you are raising another one that is, at least in the
*  discussions that I've had, not so commonly raised. So the common ones that I hear are first that
*  we're not reliable raters in general, right? This can take multiple forms. It could be like
*  inconsistency over time. It could be sort of being tricked by flattery. Presumably this is why Claude
*  is quite sycophantic and is very like quick to agree with your corrections even when your
*  corrections are wrong. So there's this sort of our signal is not necessarily clean enough to present
*  a great target for optimization in the first place. Second common objection is we don't
*  necessarily agree with each other and there's no way like even in principle per like arrows and
*  possibility theorem and things like that to resolve these disagreements. Like they may just be sort of
*  fundamental and not something you can really effectively aggregate across. A third one is
*  that even if we could do those things, we still have kind of, especially as systems get more
*  powerful and are maybe like taking action in the world and in a more agentic way that we don't know
*  what will actually maximize the preferences, right? There's sort of the, this is like the classic
*  utilitarian problem of if we are going to take some action and we're trying to maximize it,
*  if we are going to take some action and we're trying to maximize something, you can't simulate
*  the whole world. You can't calculate this out to the millionth degree. And so where do you stop or
*  what sort of approximations are you going to use? So I think all of those are probably fairly familiar,
*  but it sounds like you're saying something a higher level or more profound. Yeah, I'm saying
*  something a little complicated and a little different. And just to maybe one way to understand
*  what I'm saying, because like I am seeing something pretty complicated, is that I think the things
*  you've just mentioned are like very much in some ways, like critiques of the theory
*  of reinforcement learning for human feedback and more broadly, inverse reinforcement learning,
*  right? I think they're critiques of a sort of particular paradigm, technical paradigm
*  and conceptual paradigm for thinking about aligning AI systems, which has been, what are AI systems?
*  Firstly, it sort of starts from this picture of AI systems as not any kind of program, but expected
*  utility maximizes, right? There's this idea that goes back to Yukovsky that the right way to think
*  of intelligence is to think of it as maximizing some utility function expectation, right? And if
*  you think of AI systems in that way, right, then it seems like aligning AI must be about getting the
*  right utility function, right? How do we learn that utility function? Well, clearly we should
*  want it to be something like the human utility function. So let's assume human utility functions
*  exist. Well, how have economists and decision theorists traditionally thought of these utility
*  functions? They saw them as certain kinds of preference orderings, right, which comply with
*  certain kinds of axioms of rationality. And so we're going to try and learn from actually express
*  preferences to recover that utility function and get the AI system to optimize for that, right?
*  And if you take AI alignment to be that, right, then I think there are a whole ton of philosophical
*  and practical problems to solve there. And our paper really goes through them in detail. And I
*  do think the ones you brought up are sort of serious ones for that view of the AI alignment.
*  What I was trying to say earlier is that we are actually not really training AI systems. Well,
*  some AI systems we are training in that way, but large language models are not really at that flavor
*  because firstly, I don't think it's right to think of them as expected utility maximizers, right?
*  They're particular programs or neural networks that can be thought of as policies. They sort
*  of sample tokens as they go. The way you describe the policy, it's quite hard to describe it as
*  maximizing some expected utility, right? It's not actually doing that in general. It's too random to
*  do that in general. And so that's really an issue. And when you train them, you don't actually train
*  them to maximize a specific utility function. You sort of push them in that direction, but you're
*  not sort of pushing them all the way. So there's a certain sense in which your sort of theory and
*  practice come apart. And in some ways, what we're trying to do with the paper is pointing out that
*  practice is better understood by this other kind of thing that we just described, which is aligning
*  AI systems to normative standards, right? And that's what we kind of already are doing without
*  realizing it. And that's what we should do as opposed to something we argue. So hopefully that
*  helps as a sort of way to sort of tease apart everything that's going on.
*  Yes, two kind of follows there. One on just the technical aspect of the training. And I've
*  certainly encountered this, but maybe never thought as deeply about it as I should have.
*  When the reinforcement learning is conducted, there's typically a two-part loss function,
*  right? There's the loss function of like, get a high score from the user. And it is worth keeping
*  in mind that these are not like lifetime calculations of what's going to make you
*  best off in the long run. This is very much like the score that you would get in this immediate
*  interaction. And then there's a second term in the loss function that is basically, and sort of
*  anchor to the original pre-training distribution. And I think that's usually like KL divergence or
*  whatever that basically says, we want to keep the representations consistent with the original.
*  Now, I've always understood that in a very practical sense as just like, if we don't have
*  that, then we kind of yank the thing around too hard in various directions and underlying
*  kind of representations that are in fact important, especially because the reinforcement learning
*  training set and compute is like typically smaller than the pre-training, traditionally by a lot,
*  maybe less extreme of a difference these days. But nevertheless, like it's a relatively smaller
*  portion of the training. And so you don't want to just like go ramp, but you don't want to let any
*  one data point like yank you too far from sort of a grounded world model. If you take the thing to
*  have a world model, that has always just seemed like a practical kind of approach to me. But how
*  do you like unpack a little bit more? Why do you think that is sort of a philosophical problem or
*  why we should maybe linger on that more than we tend to? Yeah, no, I do think it's a meaningful
*  difference because it really does in fact like a difference in the sort of theory of how these
*  systems work. I mean, it is the case, I mean, it's quite explicitly from the way people are
*  training it that they're not actually at training time maximizing a particular scalar or like they
*  are maximizing this different scalar objective, but it's not the one that sort of characterizes
*  human preferences. They're doing some mix of like imitation learning and reward maximization.
*  And people have written papers about how there's a sense of which imitation learning from humans,
*  which is how pre-trained language models are trained, and do imitation learning from the web
*  essentially, is much safer because presumably humans don't do like at least extinction risk
*  level unsafe things on the internet. And if you just imitate that, you're going to like pick up
*  everything on 4chan and everything and tons of other gross nasty stuff, but you're not going to
*  pick up like super the sort of pathological behaviors that can come from optimizing a sort
*  of thing that doesn't capture human values very well with a lot of power. And I do think the sort
*  of KL objective, the sort of KL regularized objective, or you sort of constrain the policy
*  to be closer to the original policy basically is a way of doing that. It sort of like says like,
*  we don't fully trust this proxy of what humans care about, we capture. And so we're going to
*  interpolate between the original thing, which is like imitate what humans do, and the sort of like
*  do what humans say is better. And I do think that's sort of what, you know, there's a sense of which
*  that actually does make language models less subject to classical risks that people have theorized
*  would apply to expect that utility maximizers. And this is an ongoing conversation. I think there's
*  a recent paper by Michael Cohen sort of pointing out there's certain cases where the KL regularized
*  objective isn't quite enough. But in general, I do think I take the view that sort of helps
*  to avoid some of the what you might think of as pathologies of optimization. Hey,
*  we'll continue our interview in a moment after a word from our sponsors.
*  Even if you think it's a bit overhyped, AI is suddenly everywhere from self driving cars to
*  molecular medicine to business efficiency. If it's not in your industry yet, it's coming and fast.
*  But AI needs a lot of speed and computing power. So how do you compete without costs
*  spiraling out of control? Time to upgrade to the next generation of the cloud,
*  Oracle Cloud Infrastructure, or OCI. OCI is a blazing fast and secure platform for your
*  infrastructure, database, application development, plus all your AI and machine learning workloads.
*  OCI costs 50% less for compute and 80% less for networking. So you're saving a pile of money.
*  Thousands of businesses have already upgraded to OCI, including MGM resorts,
*  specialized bikes and fireworks AI. Right now, Oracle is offering to cut your current cloud bill
*  in half if you move to OCI for new US customers with minimum financial commitment. Offer ends
*  1231.24. So see if your company qualifies for this special offer at oracle.com slash cognitive.
*  That's oracle.com slash cognitive. So now the other point is kind of,
*  I guess if point one was just taking a moment to appreciate that we are not actually maximizing for
*  human preferences, then point two is kind of reframing to what you think is actually happening,
*  which you've sort of just done. But then the next leap is to what you think we should be doing,
*  which I guess you kind of would say we're approaching, but haven't really reconciled
*  ourselves to. So maybe let's do your kind of proposed vision for the future first,
*  and then we'll come back and do some of these comparisons to other folks' proposals.
*  Yeah, for sure. Yeah, I think that makes sense. So I guess, yeah, what we argue in a paper,
*  right, so it's called Beyond Preferences in AI alignment. So we are really trying to critique
*  this sort of preferences view. So we go through all the limitations of really taking this sort
*  of expected utility maximization view of both human rationality and AI alignment too seriously.
*  I think there are a lot of issues with that. And so what are the sort of alternatives we propose?
*  A lot of it comes from thinking about what do we want to get systems to do for us in the first
*  place? And we often do want them to play particular social functions and social roles for us.
*  I mean, this is traditionally getting the case of systems that we think of as tools,
*  like most technology we build basically serves as tools or services for us. So we want to be
*  and when they're tools or services that they have clearly defined a social functional role
*  that they ought to play well ideally in that role. But even as AI systems, I think, become
*  more agentic, say, and even as they become more like personal assistants that talk to us over
*  long periods of time, or like execute tasks over long range horizons for us, right, I think we can
*  still think and talk about like what social function or role we want them to play, right.
*  And from that perspective, I think it becomes much more clear, like what alignment should be,
*  right? If you think of them as sort of like playing these certain social functions and roles,
*  then well, the sort of like normative target then is like, what does it mean to play that social
*  function or role? Well, like what are the standards? What are the constraints? What are
*  the system requirements for a system that's supposed to play its role, right? And in the paper,
*  we sort of go into a bit more detail about a specific case. I think a lot of people working on
*  AGI, I guess, or like large language models are excited about, right, which seems to be like
*  something like general purpose AI assistants. And I do think that that is just one kind of thing
*  AI system could do, right? I think it's not, you know, it's sort of like strange to think of that
*  as like the only thing that AI system could do, whereas like I feel like a lot of AGI talks seems
*  to like fall into this pattern of like, we're going to build the one system that's going to like do
*  everything for everyone. And I think that's just not going to be the case. I think personal assistant
*  is still one kind of thing you can do. And that's going to have certain kinds of normative standards
*  that we want to figure out it should comply with, right? I think part of that work is we have to do
*  as a society, right? Because, I mean, we kind of know what human personal assistants should do,
*  and we can sort of apply some of those normative standards to personal assistant. But then there's
*  a sense in which we're creating a fundamentally new kind of social role or function with these
*  systems. And then we sort of have to collectively figure out politically, you know, collect what
*  these systems ought to do. But then also, there's this technical problem of like, once we figured
*  out those standards, how do we get systems to reliably comply with them? And I think there are
*  a whole bunch of ways to do that. You can do it more using more traditional machine learning
*  techniques, like reinforcement learning from human feedback, constitutional AI, where you basically
*  get people to demonstrate what does it mean to comply with certain kinds of normative standards,
*  right? But there are cases where you can formalize those standards, right? For example,
*  if you're building, take a very different kind of system, a household robot, right? There are
*  some very basic standards you want to apply, which is like, don't collide with people, right? Don't
*  break my fragile objects in my house, right? And those things are much more amenable to formalization
*  in a sort of formal world model of how houses work and sort of like, they're 3D objects in a room.
*  This is what it means for a mug to be broken. This is what it means to be too close to a sort
*  of human or something like that, right? And we can write down the specifications or partly learn them.
*  And then we can use planning algorithms to guarantee safety with respect to these constraints,
*  right? So I think it's worth separating out the sort of normative target and how we specify it
*  formally or informally and how we actually get the AI systems to comply with that. And I just think
*  it's just going to be really different depending on what kind of AI system we're building and what
*  we want it to do. Yeah. This alludes to the fact that you were actually one of the co-authors on
*  the guaranteed or toward guaranteed safe AI paper, which we did a full episode on with Ben and Nora
*  a couple months back. So that's a cool, I didn't realize that until I was prepping for this
*  episode that you were also a contributing author there. I have a couple of questions on sort of
*  roles and nature of systems. And I'm not even sure this is a normative question yet,
*  but maybe just an expectation question. You kind of pointed to the general purpose
*  not quite AGI human assistant, which is our CLAWS and our chat GPTs. And everybody is certainly
*  listening to us is familiar with those. And then on the other end, there's like
*  the Roomba that's going around. And I feel like maybe two questions are,
*  can you sort of give us a few more sort of roles that you have in mind? And then maybe also,
*  I'm interested in like, is there a fundamental tipping point on this? Is this a smooth spectrum
*  or is it more of like a tipping point sort of situation where like, sure, the Roomba, first of
*  all, I can't talk to it. You can imagine a future Roomba that I could have like that I could give
*  verbal directions to, but it still seems like its task is so fundamentally narrow. It is a vacuum,
*  right? So it can only vacuum for me, it can't do other things. Therefore, it seems like I can sort
*  of govern the thing in a way where like the AI is sort of contained within some larger superstructure.
*  And when I get over to the like, proto AGI human assistant side, it's like, much harder to understand
*  or imagine what that would look like. And it seems like part of what we want, or at least part of
*  what a lot of people seem to want from these things is that like, the AI part is the top part.
*  They don't want they want to give the AI tools, they don't want to like, can totally constrain
*  the AI. So yeah, I guess, give us more roles. And how do you think about that?
*  I'm not convinced of what we want from AI systems, right? I think sort of I think some people want
*  that. I think some people are mistaken about how much they actually, that will actually be valuable
*  to them. I think it's sometimes it's valuable. I'm actually not entirely convinced that's going
*  to be the primary economic value from autonomous systems broadly construed. And I do think there's
*  a spectrum. There's so many I mean, I think it's worth thinking about like, everything we've already
*  managed to automate in modern society and all the kinds of things that we have called AI along the
*  way to getting there. And RIMAS are one of them. I was actually thinking of something more like
*  general purpose, instructable robots in your household. And even that I think we can do
*  something much closer to guaranteed safety, because probably possible to write down a good enough
*  model, or like partly learn a good enough model of like one's house, right, and talk to it in like
*  a natural language and have that convert that into a formal specification for how to plan to achieve
*  that goal. Right. So that's sort of one system you might want to build. It's quite different from a
*  general purpose conversational assistant. I think it's going to be different from a general purpose,
*  like automated researcher, I think it's going to be different from many of the other things that
*  people already are building like automated traders, right, flight booking assistants,
*  customer service agents, you know, publics, you know, governments might want to deploy agents that
*  talk to users about like how to answer questions about like how to access this government service,
*  right. Those are all just pretty different kinds of things, right. I mean, they're being deployed
*  for very different tasks. They are built from many of them nowadays, of course, they take a single
*  underlying model, and they customize it. That's one way of doing that. You can also do more traditional
*  natural language programming techniques together. But there's a sense in which well, like the
*  there's the product, the end product, the end user product. And then there's just like the business
*  to business product, which is the model, right. And then that itself is a different product,
*  you can put a box around it's like, okay, if I'm a developer trying to build models, I can sell to
*  other business. What are the normative requirements for that? Right. And that's kind of how I think
*  about sort of the sort of like space of AI economy. I mean, I could go on and list even more things
*  like AI for like, energy to redistribution, right, AI for controlling drones, AI for many other things,
*  AI for like data analysis, AI for doing scientific simulation and inference, right. I actually work
*  a bit more in this space because I work in prostate programming, which is about scaling up
*  basically various forms of like Bayesian data analysis. And but also like with applications
*  that AI like based on 3D scene perception and stuff like that. So I just think of like, I don't know,
*  I feel like when we talk about when we start thinking about large language models as the sort
*  of only kind of AI system, we forget about a huge range of other kinds of tasks that we are trying
*  to automate. And there and consequently, sort of like the many other kinds of alignment targets,
*  essentially, you might want for systems performing those kinds of functions.
*  Yeah. Okay. So a lot of different directions we could go. I maybe want to start just with the
*  question which you pose in the paper of what should AI owe to us? And there's all these
*  different roles. And it does seem fairly intuitive when you list out so many that
*  what you would want from a vacuum versus a more general purpose robot versus something that's
*  making decisions on managing the electrical grid, that those would owe us different things.
*  Um, some of those are like very intuitive, or at least they seem like they wouldn't be like super
*  contentious. Maybe not intuitive, maybe not simple, but like, not necessarily politically contested.
*  But for the ones that are more politically contested, how do you think about answering
*  that question? I mean, I was coming up with ideas like, oh, there's like the Rawls veil of ignorance
*  sort of thing is like maybe one way to kind of approach it. Or you mentioned Confucian tradition,
*  which I know very little about, but I know that there's some sense in which like there's a role
*  based paradigm. Right. Important part of it, at least. So how do you think about it? It's a good
*  question. But what's the right mindset to answer the question? Yeah, no, I mean, and I think that
*  this question, which the AIO to us really borrows from the contractualist tradition and Western
*  political philosophy, actually, and that sort of like Rawls is a major thing in this, but like,
*  actually the phrase I think is more associated with his other philosophers, Tim Scanlon. And I think
*  he puts forward this sort of idea of like what the sort of basic way to figure out like what we owe
*  to each other. He's talking about what humans or people owe to each other is to like think about,
*  for him as general principles, but you can extend it to acts, like what kinds of actions or principles
*  could that we could live by that no one could reasonably reject. Right. And reasonably reject
*  is like doing a lot of work here. Like reasonable rejection is like doing can mean so many things,
*  but it's sort of like the general picture that's a bit in contrast, I think, to this Rawlsian sort
*  of deal of ignorance view. But I do think like before going into this question of reasonable
*  rejection or this question of like, like the bill of ignorance, like I think a lot of the problems
*  that we have from like political conflict largely don't arise when you have basically
*  decentralization. Right. I mean, insofar as what AI systems are going to do for us is to serve
*  particular users, that could be individuals or particular like companies or organizations. Right.
*  Then I think the sort of primary in a sense like alignment target is okay, what the user wants or
*  what organization wants out of it. Now the problem is, and this is when we start needing to go make
*  the contractualist move is that, well, it's not just that these systems are going to benefit or
*  provide value for individual users, individual organizations, they're also going to have
*  negative externalities on the rest of the world, depending on like what we allow people to use
*  systems for. Right. For example, we presumably don't want individual users to learn how to make
*  a pipe bomb from Claude very easily. Right. And because that would make terrorist attacks
*  more happen more frequently, perhaps. And so I think that is where we need to start thinking about,
*  okay, what are the, those questions I think start really becoming politically contested, right.
*  Because they're about restricting individuals ability to perform certain kinds of tasks in order
*  so that we don't harm other people. Right. And of course people are just going to have very different
*  opinions and where to draw the line. And I think we, given that people disagree, I think what we
*  need then is like fair and impartial ways of deciding what these standards are going to be.
*  Right. And so, so that's sort of like where the sort of contractualist picture comes in.
*  And one way you could do that and one way sort of lead to in the paper is using a Rawlsian approach.
*  Right. There are many others. I think that like philosophers have spent so much time trying to
*  figure out exactly how you should do like basically political philosophy. I could give my take on like
*  Rawls which is I really don't like this veil of ignorance kind of thing. Because I think it presumes
*  that there is this sort of like disembodied behind the veil person that you could be before
*  entering the world. I think that just seems like weird and not actually practical, but also like
*  not coherent that I think we're always the kinds of things we care about always deeply socially
*  embedded. And so I'm more of a fan of like Scanlon's view of how to go about doing this.
*  And I think practically speaking, what we need to do then is like firstly, I think figure out
*  political and social institutions for I think getting so that we can actually get to what people
*  want, what standards or principles that people really want to govern the AI systems, which do
*  have negative externalities and others into the hands of developers, right. And perhaps create
*  incentives for developers to actually implement systems which comply with those standards. So I
*  think that's a big part that governance is supposed to solve. Right. I do think that sort of more
*  interesting technical question then is if you take this as the alignment target, right, sort of
*  like these politically negotiated normative standards as alignment target, right, there's some of that
*  we're going to be able to do like offline in advance through this sort of political process,
*  right. And but I think do think that as systems become more complex, or as they become more
*  autonomous, then at least sometimes you're going to have to build systems that sort of figure out
*  what society would agree to on their own to some degree. Right. And Jillian Hadfield in this paper
*  with Dylan Hadfield-Manel called AI alignment and incomplete contracting problem. It's a really
*  great way of putting this, right. Like we don't just want AI systems to like learn and predict
*  user preferences. Really what they need to do is like learn, predict and respond to society's
*  normative infrastructure. And the reason we need that is that a lot of the contracts that we
*  implicitly have with AI systems, right, whether they're individual contracts between two parties
*  or contracts with society as a whole have missing clauses, right, they're never going to be complete
*  or incomplete. And what we often have to do in negotiating this is to figure out how we should
*  fill in the contract when we enter those situations, right. And part of how we end up doing this is
*  through the law and the courts, right. But prior to going to the courts, we often just the reason
*  why institutions hire lawyers is to like figure out what they should do so they can avoid going
*  to the courts, right. And I think that kind of capability, if we're going to build systems which
*  have really autonomous white scope, right, is going to be, I think, important for aligning,
*  especially autonomous AI systems. Yeah, there's a lot there. It seems like the question of timeline
*  is really going to be and sort of the and the trajectory of the power of these like monolithic
*  systems seem like huge questions. I noticed in one of your papers or talks, you referred to
*  Eric Drexler's comprehensive AI services as a partial inspiration. And I really like that too.
*  And you can elaborate on my brief summary. But basically, the way I understand his proposal is,
*  let's not go create an AI God that can do everything. Let's instead create potentially
*  superhuman, but narrowly scoped AI systems that are really good at what they do. And then we can
*  sort of, as humans, like, remain in control of the overall architecture of society, we can know what
*  role each one is playing, we can know what it owes us based on that role that we've designed,
*  and we can hopefully kind of keep everything under control, even as we get the benefits of
*  superhuman performance in potentially like all niches over a period of time. Yeah, that sounds
*  good. Although I do feel like that doesn't necessarily seem like the AIs we're getting,
*  like the actual trajectory. And certainly, if you listen, and I know you're a skeptic of this from
*  your earlier comments, but if you were to suspend that disbelief for a second and say, okay, what if
*  we are living in the world that Sam Altman and Dario are telling us we're living in, where at
*  least I don't think we can dismiss anymore that we might literally have like Nobel Prize winner level
*  general and Dario's vision is like Nobel Prize winner across all the domains in like two to
*  three years time. If we are going that direction, it almost seems like we don't even really have
*  time to sort out what the constitution would be, let alone put all these things in their niches
*  is just going to be, you know, he talks about like a flip. And again, I see these sort of threshold
*  effects or tipping points as potentially huge, where it's one thing if the, you know, great
*  biology professors have a lot of AI grad students, and it's a very different thing if and when the
*  AIs become the PIs themselves, and then they're either directing one another or they're directing
*  humans. So yeah, I mean, does this work? I guess the thing that's kind of concerning me most is
*  does this work on a two to three year time scale? You know, let's take this sort of like, yeah,
*  large models, AI systems, like large language models, plus, do you get to this really powerful
*  state? I do think that is sort of basic proposal was just talking about could still work, right?
*  Like you could imagine training AI system or like even prompting it to like, engage as a reflective
*  process of like, okay, given the kind of AI system and am and like, why my creators built me,
*  like, what should the constraints I operate by? Like, what would society roughly agree
*  if I can simulate them well enough should be the standards I operate by not try maximize
*  everyone's preferences, but like really think about like, if I'm a, you know, if I'm an automated AI
*  scientist, what are the constraints on automated AI science, I should go about doing in the process
*  of automating this thing. And that if we want the AI system to figure out that that on the fly versus
*  sort of figure out sort of instead of pre specify it. And I do think that sort of basic picture
*  could still work. So that's one response. I mean, I guess, yeah, I think Drexler's comprehensive AI
*  services of reporters, actually, I think, yeah, very influential for my thinking ever since I read it.
*  And I do still think that it's really relevant for a bunch of reasons. I mean, firstly, I do think I
*  just want to point out that we already do have a whole bunch of narrow superhuman AI systems,
*  right? And none of them, they don't even look like things like AlphaZero, right? They look like
*  your Google Maps routing algorithm. That's one of the most classic algorithms we have is
*  search for spatial navigation. And those basic algorithms are used every day when you run a
*  search on your Google Maps application or Apple Maps or whatever it is to get from point A to point
*  B. And they're way better than human navigators could be. They can do it at a far greater scale.
*  And I think a lot of the sort of economy that as things become, well, if we stop calling them AI,
*  we start calling it just computer science or software engineering. But there's a lot of stuff
*  we've already automated that ways that we've made superhuman. And I think there's reason to think
*  that trend will continue in many kinds of domains. Now there's this question, of course, of whether
*  concurrent to that, which I just expect to continue happening, whether something like Dario's picture
*  of like a sort of like automated AI scientist or dropping remote workers is going to happen from
*  these really large monolithic AI systems, which are in really general purpose, right? So what the
*  trajectory of general purpose systems is going to be like. And so I think this is still somewhat
*  an open question for me, but I tend to be on the like, we can probably still afford to do better
*  by specialization side of things, right? I had this recent, I think, Twitter thread on this,
*  right? Which is, I think the basic picture of what AI labs like Anthropic and OpenAI think they're
*  doing is that the thing we really want to automate is like what some cognitive scientists might call
*  a central cognition, as opposed to like any more specialized mental module for doing a particular
*  kind of task, right? By specialized mental modules, you might think of modules for perception,
*  right? Or for spatial planning or navigation, or for even for something like theory of mind or
*  intuitive physics prediction, right? These are things that actually human babies have from very
*  young parts of age, and they seem to be really, you know, well developed from quite young animals
*  have it to list what he calls his core knowledge and a whole bunch of other kinds of like more
*  specialized expertises that we learn as we get older that are sort of much more specific. But
*  it doesn't seem like the large companies are thinking that they're going to get state of the
*  art and all those things, right? The sort of primary delta they're hoping to make or the
*  comparative advantage of the systems they're trying to build seems to be in something like
*  central cognition and by which I mean something like general reasoning and planning abilities or
*  problem solving abilities, right? At a high level abstract level, not mechanistic reasoning where
*  you know all the rules. In that case, like a Python interpreters or proof search engines are
*  going to be a lot better, right? Or general sort of knowledge retrieval and development point,
*  a huge amount of working memory to sort of bring all the relevant information
*  so that you can like bring all together all these very disparate considerations into solving a new
*  problem, right? The kind of thing that presumably you need to do science well, right? And to me,
*  it seems like both an open scientific and engineering question as to, okay, maybe even if
*  these large language models plus systems, something like O1 get to be the first systems that replicate
*  many of those aspects of human central cognition well enough to serve as drop-in remote workers or
*  well enough to automate science, how sure are we that we can't do better by specializing, right?
*  Because if it turns out to be the case that people, cognitive scientists who are so-called
*  proponents of the modularity thesis or massive modularity think that actually there's no such
*  like single thing at central cognition that actually all specialized modules interacting
*  in particular ways, right? And if you can imagine us eventually reverse engineering those modules or
*  even AI systems helping us do that, right? Then you could expect that we're going the specialized
*  module is just going to do a lot better, right? If you can get it to do better, it's going to be a
*  lot smaller and cheaper and more efficient, perhaps more reliable if you really work out the underlying
*  logic at that, right? So it's going to get all the benefits of like both economic and computational
*  specialization that we already see with today's systems. And so we figure out how to sort of
*  specialize at those aspects of what we currently call or think of as central cognition.
*  Then perhaps like even if O1 plus ends up being the first kind of system to achieve those kinds
*  of tasks, we'll rapidly figure out cheaper, better, more specialized ways of doing it.
*  From reverse engineering, the more specific kinds of mental capacities required to produce that kind
*  of behavior, recomposing systems out of them and serving and deploying those systems instead, right?
*  So that's kind of like my picture of how things will play out even if these large
*  mall-ethic systems went out. And I do think it feels a bit more realistic once you think about,
*  well, humans like myself, cognitive scientists, AI researchers could of course be the ones doing
*  that work. And you might think, be skeptical of how quickly we can do that. But if the idea is
*  that we're going to get AI systems that can automate science eventually, then specializing
*  code or figuring out cognitive science is one of the things that humans do well. And so why would
*  a model-ethic system do better than systems that specialize to do specialization, right?
*  And modular system building and a whole ton of other more specialized agents and systems which
*  are designed to do their specific task, right? So that's kind of my pitch for the more sort of
*  services style view of like how you guys are going to go in the future. We're just going to get tons
*  of more different, much more specialized minds in the same way that evolution has produced so many
*  different kinds of very specialized minds for their particular like,
*  college goal issues, I think. Yeah, something like that seems like the default path and a sort of
*  desirable path. If the scaling trends, I won't call them laws, sort of flatten off, maybe not entirely,
*  but sort of level off and there's time to do that, then that feels pretty intuitive to me.
*  I wonder if we're, maybe now's a good time for me to kind of just bring up a number of other
*  schemes, which I don't say derisively, but attempts to come up with ways to align
*  powerful systems. Like if we are in the Dario world and we're looking at, you know, AI Nobel
*  Prize winner, cognitive scientists in a two to three year timeframe, and then they are the ones,
*  you know, maybe the path to this, like maybe we end up at narrow AI systems, but we go through a
*  much more general purpose systems to get there in a non non comprehensive way. I think about things,
*  of course, like constitutional and character type work, like we've already talked about a little bit
*  that Anthropica has pioneered, but like how practically do you think we are best
*  prepared to try to tell those general systems, like what world we want them to create full of
*  narrow systems? Is it a constitutional approach? Other things that have come to mind for me,
*  as I was thinking about this, are like vector reward type approaches. Meta has done this with
*  some of their recent models where they'll have like a separate reward model for just the usefulness
*  of the response versus like the harmfulness of the response. And that way they can kind of turn
*  the dial on like how sensitive do we want to be to certain levels of harmfulness and really make
*  sure we like avoid avoid the extreme cases. You could imagine a not two or three dimensional,
*  but potentially many dimensional vector reward system. Then of course, there's the coherent
*  extrapolated volition, which I'm not sure is ever quite been boiled down to a technical proposal,
*  but is sort of like what you're referring to when you say if you're an automated AI scientist,
*  you need to think about like what your role should be and what norms should govern an automated AI
*  scientist. That kind of evokes this like coherent extrapolated volition notion. Yes. I think it's
*  related, but I think a bit more constrained. Which of these do you think have legs, I guess,
*  react at a high level? No, I think there's things going for each of them, right? And they just think
*  that we actually talk about all of them in the paper and like try and say like how they fit into
*  our view of like how we should go about aligning AI systems, right? Again, like I think of
*  constitutional AI, like, yeah, one way to think of the character design is that's virtue ethics,
*  right? But I don't think it's just that, right? I mean, I do think, you know, when you think about
*  building, I don't know whether it's right, we're like moral systems, I guess. I think there's a
*  certain kind of like thing you want to comply a basic kind of minimal morality that the system
*  should comply to, which is like meet the minimum moral standards that society would agree to allow
*  you to operate, right? And that's sort of like going to be filled in by this sort of contractualist
*  picture, right? And I think constitutional AI is a bit closer to that because if you look at the
*  kinds of principles, their frame is like kind of things that, you know, approximately liberal enough
*  people would agree should like govern a kind of AI, a conversational AI assistant, you know,
*  might, should follow. And of course, this collective constitutional AI paper that followed up on that
*  line of work did that explicitly, right? They actually surveyed US Americans on principles and
*  like what that all my clod should do essentially, and took the views that were agreed upon most,
*  right? They sort of like found a set of principles that disagreeing groups agreed upon most and use
*  that to build sort of publicly sourced constitution, right? And I do think that's a very sort of close
*  in some ways, one way of instantiating the kind of like contractualist AI alignment idea that sort
*  of we advance in a paper. But I think that has its limits, right? The couple of ways in which has
*  those limits, I think one of them is that this is a sort of once off process, right? And you might
*  worry that that's not going to be enough if these systems enter into novel enough situations,
*  where people didn't specify principles that cover that case, right? And this is modulo,
*  all the parts of like getting making sure that we even know the meanings of these principles well
*  enough to get the AI system to comply with them. I think the surprising part of constitutional AI
*  is that you can even just use the AI system itself to produce the preference judgments according to
*  those principles and align to that, right? And turn that into a sort of scalar objective to maximize.
*  But right, so even modulo that, right, there's still questions of like, what if you go out of
*  distribution essentially? And in those cases, I think that kind of like automated reflection
*  upon what kinds of principles should govern your behavior in this new situation comes into play
*  more, right? It's no longer this sort of offline process that constitutional AI
*  delivers, right? But like a more online process of like, okay, now I actually haven't gone through
*  this process, the AI has to go like, I don't have data from humans right now, right? But I have my
*  own capacity to think about what other people would agree to how I should act, right? Something
*  along those lines anyway, right? And I'm going to add the coin to that, right? And that's, I think
*  that's the open air for research. I think both theoretically, I think game theory, moral philosophy,
*  studies of human moral cognition have a lot to offer here for how we can go about doing that.
*  And political philosophy, certainly. And that's part of what we sort of advocate for towards the
*  paper, right? I think that's something that constitutional AI doesn't quite solve. And I
*  think that's in some ways a bit more similar to coherent extrapolated volition, right? But I do
*  think we try to be a bit more precise about what's going on here, right? Rich is like, there's still
*  a lot of room to get even more precise. And part of why it didn't get even more precise is because
*  once you make things precise, you make certain kinds of implicit sort of ethical or representational
*  commitments, which might be the wrong ones. And we want to sort of like encourage people to
*  explore more broadly. But one way to go about doing it, of course, is like the very traditional
*  game theoretic view is that if you have a sense of what people tend to favor or disfavor,
*  then you can sort of simulate how they would bargain. And this is technique known as virtual
*  bargaining to use in a shader to agree upon a certain kind of standard, right? Or you can
*  use something that's a bit more like Habermasian. Like there's this recent paper by DeepMind called
*  the Habermas machine, where you actually do get people to express their opinions and then you get
*  the AI assistant to come up with a consensus statement, right? So you can imagine having a way
*  to simulate people's opinions on how to act in a situation and then synthesize a sort of consensus
*  policy from each individual's positions on what you should do on the fly. So both of those seem
*  like reasonable ways to go. And of course, you actually have to test them and figure out whether
*  they'll work. And then the resulting consensus from that virtual bargaining process or Habermasian
*  deliberation process can be the sort of thing you actually align the AI system to, right? I think
*  that's a lot more specific than sort of the sort of what coherent extrapolated volition tries to
*  argue for, at least personally speaking. And as for vector rewards, I think this is a bit, to me,
*  this feels a bit like not actually moving that far away from the traditional approach, right?
*  The nice thing about vector rewards is that you're a bit more explicit about the fact that
*  these kinds of different values do trade off differently in different kinds of contexts,
*  right? So there's also work on like contextual preference modeling that tries to sort of better
*  model. Like if you are, you know, AI teacher, you're going to have to prioritize certain kinds of
*  values more than others, right? Like helpfulness as the AI teacher is going to mean something
*  slightly different, where you probably don't want to feed students answer in a way that if you were
*  just like a general purpose encyclopedic AI system. And so I think vector rewards are good for that,
*  but I don't think of them as a sort of fundamental difference from the traditional framework,
*  because like at the end of the day, you're aggregating them into a single utility function
*  is just like with a bit more representational clarity. And so with a bit more, I think,
*  interpretability, auditability, governability, those are good things. But to me, it's not a
*  fundamental difference. What I think would be a fundamental difference is sort of like
*  actually figuring out, you know, a theory of helpfulness, a theory of harmfulness,
*  a theory of what it means to be a good teacher, a theory of what it means to be a good robot of
*  any kind, right? And like building systems that can do that kind of normative reasoning.
*  And whether that's formal or whether that's more like imitate humans, we talk a bit about that in
*  the paper, but both of them seem like really unexplored directions to me. Yeah,
*  yeah, that's probably a good place to transition to the more technical paper. Maybe just one more
*  question before we do is, how do you think they're doing today? Like, if you were to assess,
*  let's say Claude as and I choose Claude, because I think it probably is the most
*  ethically sophisticated of the models from my interactions with it. You know, it can do some
*  of this stuff. Like, you can first of all have like a pretty sophisticated conversation about ethical
*  dilemmas with it. And it I find is like, and here's the kind of sobering thought, I think it's
*  already probably more ethical than the average person. But you know, that and that could be great
*  if it paused here at Claude 3.5 sonnet, and we never saw another version. Again, the threshold
*  effects and tipping points and how much autonomy they're going to have may mean we're close to
*  being enough. But how would you sort of assess Claude or sort of the frontier developers today
*  in terms of how much they have accomplished toward on the scale of maybe what is needed
*  ultimately to be accomplished? Right. Yeah, I'm gonna make straight out, I think they're
*  surprisingly good. I think they're, you know, when these things that are getting good at doing these
*  things, I think they're like, they've gone away better than I initially expected them to be.
*  And I think I've now calibrated to be like, yeah, they're just pretty good. You know, after
*  constitutional AI came out, like the mere fact that you could just get the AI system, you just
*  prompted the principle and say, hey, could you tell me whether this response was a good or bad
*  according to their principle, and then propose a critique or revision and then do training on that.
*  The fact that there was enough data essentially already in the language model or enough that the
*  language model learned about how to comply with those principles was already sort of a big
*  sort of update for me in terms of how well the systems were doing and doing this implicit
*  basic normative reasoning. And I think for when it comes to conversationally helping people
*  with resolving various kinds of more ethical dilemmas, I wouldn't be surprised if they actually
*  do pretty well, you know, as good or better than like a good friend, your life is very thoughtful.
*  Right. Now, I think there are hosts of other kinds of questions that they're probably not going to do
*  well at, which is not to say that any single human does well at. And this is, I think,
*  why we need other kinds of technologies to help us, right, which is like making things like
*  long-term political trade-offs, right? Like, can Claude adequately assess like what the best kind
*  of climate policy is or what the best kind of immigration policy is, right? I don't think it's
*  going to be very good at actually giving the right answer, whatever that means, or according
*  to some standard of rightness. I do think it's going to be good at providing a whole list of
*  considerations that any reasonable person should hopefully consider as they're sort of thinking
*  about this for themselves, but in actually evaluating the effects of the policy, which
*  is the very different kinds of AI systems than what the large language models are designed to do.
*  We need actual pretty good scientific models of how the world works. And we're so far away from
*  that, I think, for things as complex as climate policy, let's say. You're going to have to build
*  good enough climate models. You need to build good enough models of how society works, right?
*  I think there's some kinds of things we can make some headway. And like a lot of traditional
*  social choice has been in this sort of like regime where you can define the payoffs and costs well
*  enough. And in that domain, I think I would just, in some cases, if you have the payoffs, if you are
*  able to precisely estimate people's individual costs and benefits well enough, then use a traditional
*  social choice algorithm, and it will deliver a pretty good outcome much more precisely and
*  rigorously than Claude itself will, right? And so it just kind of depends on what kind of like
*  trade-off you're trying to make here, I guess. It's interesting to think of how I would have
*  voted if Claude had been on the ballot this last couple of weeks. Claude would have been a very
*  strong contender for my vote, though, certainly given the other choices we had available. You'd
*  need some sort of mechanism, of course, for like bringing things to Claude. But I mean, in a very
*  literal way, like if you were going to make Claude the decider on key questions and you had some
*  scheme. I would worry that systems like Claude are, I don't know whether stig-o-fantic is the
*  right word, but they're kind of like too appeasing to serve as good political leaders. I think you
*  be a political leader, you have to like have a point of view on what direction the nation or
*  the policy should go in. And I'm not sure that language models, I mean, for good reason, we
*  haven't trained them to be in that, go in that direction of personality spacing. Yeah. Well,
*  I would say that was in short supply on my ballot as well. I would agree, certainly, that like,
*  I've got an essay in the works that basically includes this point where I feel like we should
*  be very clear that it's not really for the AIs to tell us how we want to evolve. That doesn't make a
*  lot of sense, certainly right now. I would need to see a very much more well-developed, coherent,
*  extrapolated volition plan before I would be ready to sign off on that. Still though, I could
*  imagine if you had some sort of like, just working within the framework that we have of bipartisan,
*  or not bipartisan, but two-party system, if you had sort of a blinded, here's each party gets to
*  sort of generate their proposal, you don't tell Claude which is which, and you just kind of put
*  two proposals in front of it and ask it to like either pick one or like come up with some
*  compromise. I honestly probably, I would seriously consider voting for it.
*  Yeah, interesting. Yeah, I don't know. I mean, I honestly don't feel I follow American politics
*  enough to like have a sound assessment. I mean, I think I can imagine for, you know, I'm deeply
*  ignorant of local politics partly because I don't really have the chance to vote here. But if I had,
*  first, I think ranking between like deferring to a random person on the street versus deferring to
*  Claude with some access to like claims about public statements versus deferring to my partner
*  who actually is really involved. I defer to my partner first, then probably Claude, then a random
*  person in the street. So let's go to your more technical work. This is another paper from earlier
*  this year, learning and sustaining shared normative systems via Bayesian rule induction in Markov
*  games. A mouthful, but I think the discussion that we've had provides a good, certainly
*  motivational foundation for what you're trying to do here. And I'd love to get kind of your
*  more detailed, more technical kind of motivation for the problem as well. And you can be basically
*  as technical as you want to be. I won't be afraid to ask a, you know, a naive question if necessary.
*  And we've found over and over again that the folks who listen to this show definitely are like in it
*  for the details and are ready to do at least a little bit of work to try to keep up with you. So
*  give us the setup and kind of what you're optimizing for and what this system is outputting.
*  I do think it is like, is very interesting. There's some great animations too that go with it
*  that maybe we can post when we put this online. Yeah. Yeah. And shout out to my really wonderful
*  research mentee in El Odenberg, who really did a lot of the implementational efforts and
*  experimental work on this paper. It was really nice to get this paper out because there's a sense
*  in which I've been thinking about these ideas since I started my PhD and only really got to
*  back to them towards the end of it. But the basic picture, I guess, is like, if we take seriously
*  this view that we're going to have tons of different AI systems out there as well, then
*  we want them to largely, I hope, pursue like objectives for, you know, on behalf of particular
*  individuals and organizations, right? But of course, if you do that too much, then there,
*  you know, may impose some kind of costs on the rest of society, right? And of course, we can
*  attempt to, again, pre-specify all the kinds of constraints that AI systems should comply with
*  in advance, you know, by following existing law or something like that. But I think there's good
*  reason to think that for some kinds of AI systems, we won't be able to pre-specify everything in
*  advance. And instead, for things which are not either not formally specified, they're sort of
*  like really local and contingent, or where there's sort of really ambiguous gaps in, say, the law,
*  the AI systems will have to figure it out for themselves. So how can they figure it out, right?
*  One way to do that kind of figuring out what the sort of sure normative constraints that society
*  shares is by learning from other people in the environment or other agents in the environment,
*  right? And so it was a way to like perform a kind of alignment that doesn't have this sort of
*  hard problem of like figuring out every single agent's preferences and perfect, choosing the
*  optimal plan that satisfies all of them. Instead, it's like, I'm going to do my thing, a constraint
*  to like not harming other people too much, right? Or not harming society too much. And I'm going to
*  figure out what the constraints are, right? So that's one way of attempting to formalize some
*  aspects of this more contractualist picture of AI alignment. Now, figuring out like what this
*  constraint should be, the way we set it up is as this formalism called the Markov game, right? This
*  is the standard formalism used to describe a multi-agent reinforcement learning tasks, right?
*  Where essentially you have a bunch of agents, they each have their individual objectives, we're
*  going to like just assume that's describable by reward function. In general, if they have incomplete
*  preferences that can't be describable as a reward function, but for simplification, we assume that.
*  And then traditional kinds of solution concepts in these kinds of game theoretic settings are
*  the agents should converge to either a natural equilibrium or correlated equilibrium, right?
*  Which are these like sort of stable patterns of behavior such that no one would prefer to
*  deviate from that sort of like joint pattern of behavior, essentially. Now, how does this connect
*  to, you know, part of this sort of interesting sort of philosophical question is like, how does
*  that connect to what humans actually do? Which is like, we seem to follow and obey social norms,
*  right? We seem to learn social norms of society. So we made this extension to the Markov game where
*  that sort of in some ways helps people coordinate upon better sets of norms. And you can think of
*  these as better equilibria, essentially, by giving them some initial beliefs about how the
*  rest of society operates, right? And these beliefs are going to look like, do I believe whether
*  the rest of society is complying with a certain rule most of the time? And that's we're going to
*  call that rule a norm, right? And we're going to have a set of possible rules, right? A whole
*  space of possible rules. In general, you can imagine having a whole compositional language,
*  a formal language, let's say a programming language, or a natural one for describing all
*  those rules, right? And I'm going to try to infer from people's behavior what rules are following,
*  right? And if I infer from people's behavior what rules are following, then hopefully I can comply
*  those rules as well, right? So if you build agents that have an intrinsic desire to comply
*  with the rules that they believe to be true, or like true in the sense of the rest of society is
*  complying with them, then you get this kind of automatic, okay, I'm going to like pursue my
*  individual objective, subject to the constraint of complying with rules that it seems to be the
*  case that most of society is complying with right now, right? And so that's the sort of basic picture
*  we offer in that paper. And you can extend it in a bunch of directions, right? Even if, you know,
*  the nice thing about this sort of framework is that we're assuming most agents are like sort of
*  by default norm compliant, right? But even if you're not an agent that intrinsically wants to comply
*  with the norms, merely having the belief that other agents are going to comply with the norms
*  can motivate your behavior. Because in many cases, norms come with punishments, and we don't explore
*  this in the paper. But if I believe that other people are going to comply with the norm and
*  sanction me for not complying with the norm, then once I come to form a belief that this norm is
*  practiced by the rest of society, then I better comply with it just for my own sake, right? At
*  least insofar as I can't get away with breaking it, right? So that sort of like slightly extended
*  version, which also handles the fact that some agents are not going to be, they're going to be
*  wanting to like freeload and break the law and things like that, right? So that's probably the
*  theoretical framework. And we built a system that basically does do that. We built a system that
*  essentially has these agents that model the other agents' environments. They assume that most of the
*  time they're trying to pursue their self-interest, like picking up apples. But sometimes other agents
*  do weird things like, oh, I guess they're not eating this apple, even though it seems like it'll
*  be good for them to do so. And also, huh, they're also going to like the river to clean it every
*  once in a while. And if you're kind of in Bayesian enough about this, right, you should infer that
*  there are probably some rules out there that are following that explain this behavior. And you can
*  update your beliefs about what those rules are based on the fact that they would better explain
*  other people's behavior than just the sort of mere hypothesis that they're maximizing,
*  just of immediate self-interest. So that's roughly how the algorithm works.
*  Yeah. So that part really, I think, is worth taking an extra beat on. The idea that,
*  and the little setup is basically you have like some land and a river and there's apples that grow
*  and they can get eaten. So the volume of available apples can go up and down and then the river can
*  get dirty and can get cleaned up. And sort of obviously toy examples, but like if all the
*  apples get eaten, then they don't grow back. Or if too many get eaten, then there aren't enough for
*  a while. So yeah, the key idea that I found really interesting there was using apparent
*  deviation from self-interested behavior as the hint that there is probably a norm here that is
*  governing behavior. Why isn't that person or that other agent eating the apple? Something must be
*  going on there. And these norms that get inferred in this paper are explicitly inferred, right? You
*  have sort of a space of possible norms. There's like a finite number, right? That they can sort
*  of track at a given time and kind of as they continue to observe other agents' behavior.
*  Yeah. There were like 72 rules you wrote down or something like that. Some of them were
*  spurious, but there are quite a bunch, but it was a finite number.
*  So I guess questions arise for me there like, do you think it is a smooth generalization from
*  something like this where it's like pretty discrete? I mean, the whole thing is discrete,
*  right? There's like discrete squares on the board and there could be like an apple or no apple. It's
*  like a zero or one kind of thing in many ways. And then the way that they are specified is quite
*  discrete too. It's like, if there are not enough apples, then don't eat apples and let them regrow.
*  Don't let them regrow apart is like implied, I guess. If there are enough apples, then you can
*  eat one. If the river is dirty, it's subject to a certain level, then your job is to clean it.
*  Is it a smooth generalization from these sort of explicitly coded and kind of discrete rules to
*  things that a clod computer use agent might encounter in the wild?
*  I do think it can generalize. I mean, I do think that, I mean, I think maybe discreteness for me
*  is not the main issue. I think like, like they're continuous generalizations of the basic thing that
*  I like. You can imagine like dirtiness of the river could just be a continuous variable and
*  that would be different. And also I think, I do think that when humans model the world, we often
*  effectively like discretize it in various ways to make our planning easier. We just don't think of
*  it at the level of resolution of like, oh, individual like continuous. I don't know. I mean,
*  I do think we often like abstract the role into much simpler, high level abstractions in order to
*  do efficient planning. So that part is not an issue for me. I do think that probably the bigger
*  scalability bottleneck of like that particular framework implementation is that of course,
*  it required an explicit formal model of the world in order to specify these symbolic rules
*  to do learning over. And so I think the whole bunch of questions about like how you can imagine
*  expanding beyond that, I think there's a sort of like narrower regime, which is that let's say you
*  want a self-driving car that can learn driving conventions, not only in San Francisco, but also
*  in Vietnam and India, right? Where people drive really differently, right? And then it seems still
*  possible that you could have a good enough real implicit role model of what it means to do drive
*  cars in those situations and a good enough model of how age other agents would drive in your driving
*  styles that you could infer like the sort of like local driving conventions, right? In that richer
*  space. So that's an intermediate and you just need to do more work of like actually writing
*  much richer role models, but still not as something as like open-ended as what people seem to want
*  large language models to do. Now, if you're going to like fully, you can say anything you want in
*  natural language. I do think that there are ways to sort of expand it. Firstly, you can represent
*  the rules in natural language instead of a formal language. And then the big question at then is like,
*  what are the semantics of those natural language rules, right? In the simulator we had,
*  we basically had a sort of well-defined interpreter for what the rules mean, right?
*  You can actually formally check what it means to break the rule and what it means to not break the
*  rule. But with a large language model, you don't have that, right? Because you don't have a formal
*  role model in the first place. And one thing you could try and do, and there's a sense of which
*  constitutional AI can be at assuming this, is to use the language model as a classifier
*  for whether the rule is broken. And you can even do things like take the log probes of the token
*  yes or no to get a probabilistic estimate of whether the rule is broken. And so you can actually
*  maybe do the more Bayesian thing we're doing, right? And so one sort of strategy you can imagine
*  is like the agent you see, like you go LM agent, this is not what I would do because, but I don't
*  really want to do research on large language models. But if you were to do this, right,
*  you can imagine building a large language model agent that sort of like looks at other agents
*  and people in society and like what they do. You prompt it to hypothesize a bunch of rules that
*  might explain people's behavior in this setting that may be deferred from their initial expectations
*  or whatever. Just getting some prompts of probably come up some not entirely unreasonable
*  hypotheses. And then you can reweight them according to how well they actually do explain the data.
*  Right. And so you can actually formalize this as a kind of important sampling technique. And as a way
*  of actually approximating Bayesian inference in this much richer space. Right. So that's one
*  actually we have doing it. You can do that process iteratively perhaps. Right. So that's one thought
*  of how to generalize in a couple of directions, the thing we built. I do think there's sort of
*  questions about like, is learning passively from observation what other people do enough?
*  I think it's actually not going to be enough because some norms are just bad and we don't
*  want AI systems and merely follow bad norms. And yeah. Yeah. Again, it really so much seems to
*  depend on just how powerful these things get. If they're not so powerful, then yeah, you don't
*  have obviously nearly as much to worry about, but the bad norms become a real issue if they are
*  reshaping society in a few years time scale. The project that comes to mind that I feel like might
*  be most shovel ready to try something like this would be the AI town project that you may have
*  seen that came out of Stanford a while back. And then there was also an open source version
*  that's in like TypeScript. And I think it's like quite easy to kind of fork and hack on. Somebody
*  might actually be able to do that, to do like a version of what you're describing pretty quickly
*  there. Yeah, no, I think it's totally possible. In fact, there is this Concordia AI contest right
*  now run by DeepMind. And I think some folks by DeepMind and the Cooperative AI Foundation
*  that's very similar in scope. They build a very similar kind of environment. I don't know if it's
*  a grid world, it might be fully textual. But the basic idea is they have these language model agents
*  interacting with each other in society. And it'd be very natural to try this kind of thing. I
*  wouldn't be surprised if someone's already kind of tried this kind of thing. And what we were
*  trying to do in the paper is like, yeah, you can do whatever you want, prompting techniques and
*  build your agent. Like, it'd be really nice to have a formalism to talk about this so we know
*  what kinds of good results we would get, or good or bad results we would get from that kind of
*  system. Right. And that's why I think that is a benefit of formalism, minimally, even if it doesn't
*  really lead to sort of actual implementations that are formal themselves. Yeah, that's really
*  interesting. I'm kind of my gears are turning on that a little bit. A couple other points from
*  the paper I thought were really interesting were, first of all, if I understand correctly,
*  basically a threshold effect for following the norm. I guess I don't quite understand what role
*  that is playing in this particular work in as much as if there's not a punishment, why not always
*  follow the norm? And I guess there may be some cost in terms of your reward. But interested in
*  how you think about kind of the, maybe again, the question is like generalization of you put
*  sort of, okay, at this confidence level, you follow the rule. But obviously, it gets more tricky than
*  that, right? Yeah. So I think what we did, and we didn't just do the thresholding, we also did
*  sampling, right? So basically, there are a bunch of, the way we set up the formalism, there's sort
*  of like, well, the ideal thing to do is, and then there's the algorithm that practically tries to
*  achieve the ideal but falls short in some degrees, right? So we set it up as like, really, if you are
*  aging with infinite computation, you should be able to do Bayesian inference over the full space of
*  possible norms. And you should be able to assign a posterior probability to each rule or norm being
*  true. And then given you have that posterior probability, you have this sort of belief-dependent
*  reward function, which kind of says, to the extent I believe a certain rule is true, I'm going to
*  take myself to pay a cost, right? So the norm-augmented reward function I'm trying to
*  maximize instead is like, I'm going to try to maximize my individual interests subject to
*  not suffering too much cost from violating the norm, right? But because the norm might not be true,
*  it's sort of like, if I only have 10% belief in this rule being active, essentially, or practiced
*  by society, then I'm not going to really care much about the cost. But if I have a 90% belief
*  about the rule being active, then I'm going to really care about the cost. Okay. So that's the
*  real thing I want to sort of try and do. That's a real sort of like objective function that the
*  agents are supposed to try and aim for. But there are many ways to try and approximate maximization
*  of that objective, right? And one way to do that is just use simple thresholding, right? Like,
*  if my belief in a certain rule is high enough, then I follow it. If it's not high enough,
*  then they don't. That's a simple heuristic, right? That approximates the actual expected
*  utility maximization in that context, right? Another kind of thing to do is you could sample
*  and say, well, if you're when you're really uncertain about the norms, maybe it's worth it
*  to do some exploration, right? Where you sort of try out certain things first and see whether try
*  breaking it, try not breaking it, and see how people respond to that. We don't really, the agents
*  don't really learn in that case, because we don't really have punishment and assimilation seated.
*  But in principle, like exploration can help. And one thing they do help with is that if you're in
*  a situation where you're not sure if there are any norms exist at all, people sort of like
*  experimenting with norms that they think might be true can lead to this really interesting
*  bootstrapping behavior where, where even though initially there wasn't a norm of convention being
*  followed, because people like experimentally comply with certain kinds of rules, other people
*  start seeing that and follow them and then you sort of bootstrap off each other and we all converge
*  as a shared set of norms. And I do think this happens in real life, I do think that people
*  form really local norms and conventions very quickly by sort of like following the local
*  conventions of the group that just sort of spiral out from this process. Yeah.
*  Yeah, that's really helpful. Thank you. One maybe more final low level point was
*  there's also a curve in one of the graphs on false positives. I wasn't sure I was understanding that
*  correctly, but it certainly occurred to me and it didn't seem like they ever crossed the threshold
*  or at least not in sort of maybe the aggregate way that they're being reported in that graph. But
*  I did wonder, is there some sort of like norm decay function? Would you imagine a regularization
*  on the norms as you go through steps or and if you didn't have that, would you sort of
*  end up in like your own personal vetocracy? Obviously, that's a problem in some domains.
*  Yeah, I do think that there's an issue of like how do you unlearn norms that's not really captured
*  by the current framework. And so, right, you can like add in a decay parameter sort of post-hoc,
*  but I really try and like be basing them out these things, right, as sort of how I was trained to do
*  things. So like, it's really worth thinking about like, what is the sort of underlying model,
*  generative model you're trying to do inference over that will recover this kind of norm decay
*  behavior, right? And one way to think about it, to set it out, and we didn't do this, of course,
*  is that have agents instead of trying to comply with something that they think society is practicing
*  over all time, right? They sort of try and comply, they're trying to infer what society has been
*  practicing for the last k time steps or something like that, right? And so, if you're going to
*  update your beliefs like a Bayesian agent would, you would gradually update, okay, like, you know,
*  society is following these norms, society is following these norms. Oh, it seems like other
*  people stop following these norms for whatever reason, maybe it became too costly for them
*  to comply with the norms. And then I would learn that society no longer complies with it. And I
*  would update my belief and start complying with that norm, basically. So that's one way of capturing
*  sort of decay that falls out of like doing inference over what is society currently complying
*  with, essentially. And I do think people do this, right? Again, another example is people very
*  rapidly adapt to say, littering norms, right? If you see tons of litter on the ground, say right
*  after a football match or something, then you're just like, okay, I guess I'm not expected to like
*  not like actually care about litter in this context, it's fine. And you probably infer it's
*  okay, it's not a big deal if I also litter. Whereas you walk off somewhere else and there's
*  like completely clean streets. And you're like, okay, I'm going to quickly adapt to like in this
*  part of town, it's not okay to litter. Right? Yeah, very Singaporean example there. Does that
*  create? I don't think it's Singaporean because I actually got this example from American culture,
*  because this is the first time I saw like a pre-game, the amount of trash. Yeah,
*  brass thing American. Does that create like potential for something like, I mean, people
*  talk about like preference cascades or more sort of vague term would be like vibe shift. Do we have
*  to worry if we're all kind of, they're sort of getting, you know, kind of zooming back to the
*  philosophical level here. There's like, we can all go around imitating each other and Bayesian
*  updating on what one another are doing. But is there any guarantee that converges to something
*  good? Definitely. Yeah, there's no guarantee to convergence something good. I think you can just,
*  there are plenty of bad equilibria. They're probably good equilibria. They're plenty of
*  bad equilibria. And the mere fact that we have, you know, firstly, the intrinsic desire to comply
*  with what other people are doing. I think that tends to be good because it allows us to converge
*  to good equilibria that we wouldn't have been able to a bureau always actually never doing that.
*  But also allows us to converge to like much worse systems or to stabilize systems that were
*  initially good, but turned out to be bad as environment change. I think there's a big problem
*  that society struggles with. And there are many oppressive norms. And people have written about
*  norms that one of the people we cite a lot is Christina Becerra. She's written this really nice
*  book called The Grammar Society. She actually writes a lot about this issue of pluralistic
*  ignorance where people still believe everyone else thinks they should follow the norm. But in
*  fact, they personally don't want to comply with it anymore. And this happens in I think a lot of
*  societies where these oppressive norms that most people don't want, but they believe everyone else
*  should think they follow that norm and it stabilizes. And that's not something we want either.
*  So I think this sort of framework we propose here is not going to be able to avoid those situations
*  as sort of going for this more minimal thing of like complying with what other people are complying
*  with. It's not going to do additional reasoning about are the norms actually good somehow, right?
*  And I think that's when you need to add more of this sort of like classic contractualist machinery
*  of like, okay, if I do have a sense of what people really want that isn't just complying with the
*  norm, then I can start thinking about, okay, what set of norms or what set of rules or what set of
*  policies or principles would make us all collectively better off or things more fair,
*  right? So it will lead to a pre-approval improvement over the current system, right?
*  And that is hard to work because you actually do need to have a better understanding of each other
*  individual's desires. And it gets you back a bit into the problem of like, what I think of as
*  galaxy brain value alignment, where you try and learn every single individual's preferences.
*  But because what you're optimizing for is over the principles and not, you know, your plans or
*  something like that, there's I think hope of like getting it to be a bit easier. And I think there,
*  you know, we just talked about a whole range of other strategies for tackling that task, like to
*  have a mass machine or actually getting systems to do virtual bargaining and stuff like that.
*  Yeah, gotcha. Okay. Cool. One other idea, just, this is a little bit of a tangent, but it
*  definitely has caught my interest lately. And I wonder how you would relate it to
*  this work is work on self other overlap, which I did an episode on this partially on this,
*  not long ago with a couple guys from a studio where they are pursuing neglected approaches to
*  AI alignment. And some of the norm kind of weirdness that we just discussed, they also
*  uncovered with a survey of alignment researchers where they basically found that most people
*  believe that like the field as a whole is not on track to solve the big alignment questions
*  in the time, you know, that it's needed. And yet everybody's kind of not necessarily branching out
*  into new things as much as you would want them to if that is in fact the consensus opinion.
*  So they're trying to do that. This self other overlap concept is basically saying, first of
*  all, taking inspiration from human evolved collaborative mechanisms where we do reuse the
*  same cognitive machinery to reason about other people as we do to reason about ourselves, or
*  possibly it goes the other way around, who were we, you know, modeling first oneself or others
*  solutionarily is not necessarily entirely clear, at least to me. But regardless, it's like the same
*  machinery. And so they try to port that over to an AI setup. The project is honestly quite similar
*  to yours in terms of how it looks with like a small grid world and like a couple agents running
*  around and there's like reward and there's whatever. But what they're able to show is that with
*  self other overlap training, which is in a more technical sense, they are minimizing
*  the difference in internal representations between a self versus an other situation,
*  they're able to get an agent that learned to be deceptive based on its initial reward conditions
*  to no longer be deceptive because it no longer has such a distinction between itself and the other
*  agents in the game. So I guess you could react to that on any number of levels. Like is there a
*  hybrid project there? And what do you maybe what do you think more broadly about kind of taking
*  inspiration from the biology of human cooperation? Yeah, that's really sounds interesting. I know,
*  I will say upfront that I'm much more insofar as I'm a cognitive scientist or I'm much more of a
*  cognitive scientist than a neuroscientist. Right? So I know, I think a lot more about the mind
*  than the brain. And I don't really know very much about like how the brain actually implements
*  processes like, like empathy or like theory of mind or intuitive psychology, right? I mean,
*  I do know there are parts that seem to be the reasons, regions of the brain which do that kind
*  of thing. But I don't know very much about the self overlap theory as it applies to psychology.
*  Now, when like in principle, I think it's seems likely that one way minds could evolve is to
*  reuse certain kinds of mental modules for simulating others for something yourself or vice versa,
*  right? That part seems fine. Now the connection to latent representations, especially of artificial
*  neural networks, that to me is the probably the part I'm most skeptical about, right? Because I
*  just don't know what those things are. Right? And in a lot of my work, I actually try and think
*  about things from a different direction of like, okay, like, what is one way of specifying a theory
*  of other agents, right? You can build basic models of other how other agents would act as
*  goal directed, approximately rational agents, and do inference of other goals and coordinate
*  with each other that way. And that's how it would go about solving that problem and sort of building
*  cooperative rationality as it were into our AI systems, right? Sort of by replicating what we
*  know about like parts of human theory of mind and how we know to formalize it. Whereas with the sort
*  of like, you know, aligning internal representations neural network, it might end up capturing some
*  things like that implicitly. But I just don't have good enough theory of what representations
*  are actually doing to say for a certain like, whether we can get expected outcomes from that.
*  Yeah. Yeah. One of the things I do find attractive about their approach is that,
*  I wouldn't say this is like, you know, irrefutable analysis by any means, but I'm kind of channeling
*  their take on it is that they feel like you don't need to have necessarily great theoretical
*  understanding to say, if we just try to make you the agent or the AI model, whatever,
*  behave similarly in an internal representation way, when you're considering yourself versus
*  considering some other, if we push those together, and there is like multiple terms in the loss
*  function, because of course, like in some instances, you do need that distinction to just like be
*  effective. But if we try to minimize that divergence and only kind of preserve it where it's really
*  needed for functionality, then maybe we don't necessarily need to understand a lot more, we
*  don't necessarily need to solve interpretability, but we can just kind of squeeze, add this additional
*  term to the loss function, squeeze the model this way and see what happens, and they at least have
*  some initial positive results. But obviously, all these novel alignment agendas definitely have a
*  lot more technical work left to be done. Yeah, to me, it's like if I were the government,
*  and you presented to me as a safety case for ensuring that your AI system didn't do like,
*  you know, violate safety critical things. You want to see some empirics as well.
*  I wouldn't buy that case at all. Right, like I would want approvable. Once I'm kind of mathematical
*  theorem showing me that in fact, this will lead to the kinds of out behavior I want. And that's why
*  I'm much more sympathetic to you, like guarantees the entire approaches. I mean, I think possibly
*  we could get there. I do think that the kind of stuff that this is reminding me of is like some
*  of the contrastive representation learning stuff in literature, which can be viewed as
*  approximating certain kinds of conditional distributions. And, you know, there's more
*  hope. Yeah, it definitely has some shared, whatever, some shared intellectual history there, I think.
*  So let's see, how do we zoom out and bring this all to a close? But I would be interested in how
*  you would zoom out in a couple different ways. One of which would be like, big picture AI safety. Do
*  you sort of come down as like a defense in depth person where a lot of the techniques that you're
*  developing like fit into sort of a broader framework of throw the kitchen sink at it?
*  Or do you think that some of these things could do what I call actually work, which is to say like,
*  work so well that we can not worry about it anymore and not have to, you know, have a defense in depth
*  strategy? That could be one closing question. Another one that I would be interested in your
*  take on if you want to offer it is how do we avoid an AI arms race internationally? Is there any
*  hope for a sort of contractualist approach or some sort of bargaining based solution that could get
*  us to a situation where we don't have great powers racing for AI powered strategic dominance over the
*  other? Because that seems to be the course we're on. And I really don't like it. But I struggle to
*  find an off ramp and I thought maybe you could at least speculate as to what one might be.
*  Yeah, I could attempt to do both those questions. First thing I'll say first, I wanted to mention I
*  realized after the fact when I was bringing up all this, like, like, how do we reason our way out of
*  bad norms, which is maybe a bit relevant to what we're going to talk about. There's this really
*  great paper by one of my colleagues, Sydney Levine, led by one of my colleagues, Sydney Levine,
*  on resource rational contractualism, which really tries to spell out like as a theory of human moral
*  cognition, how we've solved some of these problems that I think a lot of my sort of sort of my
*  thinking about this has been sort of influenced by and sort of wanted to shout out to that paper.
*  People are interested in learning more, sort of more in some ways, formal and technical approach
*  to thinking about how people manage to do this kind of like virtual bargaining thing or similar
*  kinds of approaches to figuring out what the good norms should be. Cool. So with regards to, I guess,
*  yeah, whether I'm a defense in depth person. So I think I'm just an optimist. Firstly, you know,
*  you can probably tell that I'm not. It's like not from what I said earlier, I don't really believe
*  in really tight timelines for development. I think it's going to be a much more gradual and
*  diffuse process is that it's going to happen over large aspects of the economy. And I do think it's
*  going to tend to look more like these kinds of more narrow specialized services and systems.
*  Right. And on that view, I do think like guaranteed safe air approaches are much more amenable
*  to that kind of picture of how AI develops, because I do think there's just so many kinds of
*  safety critical use cases that we want for AI systems where there'll be economic demand
*  for reliable, guaranteed safe systems such that they can under, you know, not so hard conditions,
*  not so different conditions from where we are right now, there'll be a market for them and they
*  will start to open up. Right. So that's sort of like, I'm pretty optimistic about like us.
*  I didn't know how optimistic I am. I'm not sure whether I can give a number on how optimistic I am,
*  but like it's almost like the default path for me in some sense of like how I expect things to
*  play out. That once we invest enough effort in showing to the rest of the market that you
*  actually can get competitive systems with high assurance for reliability and safety, and maybe
*  even guarantees, they will win on the market, especially for things like agents where you
*  actually do need these like reliability, like people just want these reliability assurances
*  much more. Right. So that's part of the picture. And so how I view guaranteed safe AI approaches
*  is that really trying to accelerate that approach so that we don't go through an unnecessary phase
*  of like messy AI accidents that I don't think will kill us, but could cause anywhere from
*  tons of, you know, like unnecessary economic damage in a way that AI worms do already.
*  You can imagine AI versions of those worms are like flash crashes from like poorly coordinated
*  AI agents, right, happening in this intermediate period to like anything like flood catastrophes
*  that arise from poor deployment of integration of AI systems into critical infrastructure or into
*  military. I think I'm most worried about integration of sort of like AI systems with no kinds of
*  guarantees at all or assurances into military command chains. Right. And I think that's one of
*  the most likely way of like having AI systems which somehow respond to each other and much
*  faster ways than any human can escalating into hot wars. That's I think one way you can get AI
*  mediated catastrophes, which I'm pretty worried about. And it's not like we're not already seeing
*  in militaries today using tons of AI systems in their warfare operations. So I do think there's
*  sort of the prosocial case for working on the kinds of things I'm working on. I think it's still
*  there. It's just not as sharp as if you really think extinction risk is super likely. As for
*  great power conflict, I because I don't have like, you know, don't really take the view that it's
*  going to be a single system or single set of systems that develop and give anyone company or
*  country of what people have called a decisive strategic advantage. I think this sort of gel
*  politics just looks a lot different, right? If it's going to look more like this diffused
*  development of services over time, right? I think sort of firstly, I think the economic benefit of
*  that hopefully will be more shared, just by the mere decentralized nature of the sort of AI,
*  a bit closer to what is actually happening right now. Right. And there and if that's the path,
*  then perhaps there isn't gonna be a need for arms race at all, because of there's just not,
*  it's not really worth it because there's no single technology that will give you a decisive
*  advantage. It's hard for me to think about like how to operate in that role, given that I don't
*  really think that's very likely. I mean, I guess I would apply many of the same lessons from,
*  you know, how we've kept nuclear peace. I don't think it's so different, right? I'm sympathetic
*  to views where like, whoever you think should be in charge, hopefully can have a healthy lead,
*  and then share the benefits widely. So there's there that people in second place countries or
*  otherwise don't have incentive to really start conflict over it, because you're receiving enough
*  benefits from it anyway. That seems like a good enough picture to me. I mean, I think that's also
*  very vanilla, and my understanding fairly mainstream view in the society, and AI sort
*  of governance community. And I don't feel like I have much more to add beyond that.
*  If you did, putting yourself obviously in your natural Bayesian mindset, if we, you know, Sam
*  Altman said, for example, when asked for a 2025 prediction, he said, saturate all the benchmarks.
*  It seems like we will know soon enough whether they're right or wrong, right? If they start to
*  look right, what would be the leading indicators of that to you? How would you change your worldview?
*  And would you start to become like a pause advocate if all of a sudden benchmarks were
*  all saturated in less than a year? Well, I would still I think advocate for what I think I'm already
*  like, do advocate for, which is like differential acceleration of like, inherently safer classes
*  of technology is right. I think there's still going to be value to that. And in so far as they
*  can hopefully replace systems, or even if though they're the second system to reach a certain
*  capability level, hopefully to do it more efficiently and cheaply and reliably. I think
*  there's still a case to be made for that, which is maybe a bit convenient for me, because I sort
*  of don't change what I work on, despite whatever happens. But I do think that is my view. As for
*  things that would change my mind, I do think there's like, you know, the thing I've been waiting for
*  a while and intentionally not talked about very widely was I was expecting some version of O1
*  style systems to happen for quite a while. And it just seems to me there's a lot of private
*  information about how that system actually works and was developed that is I don't have access to.
*  And I because the way I tend to think about these systems is very much from the inside view, like
*  my the way I perform my predictions by AI systems, like, okay, really trying to think about can this
*  system reliably do reasoning, for example, at the kind of like 99% reliability skills that we
*  would want for certain kinds of economic applications, right? That to me is like one
*  of the things I really want to figure out whether it's true or like is this sort of like scaling
*  rather open AI is on what we're on track for. Based on what I've seen, it's not super clear,
*  like it's not obvious to me that there are. I mean, it's like, I don't think O1 gives you that.
*  It's like, first of all, super expensive. It definitely fixes some of the issues that
*  your single like chain, like all schools chain of thought wasn't giving you. But the kind of like,
*  guaranteed reliability would want for certain kinds of certainly for robotics. But I think also
*  for tasks like even just like executing a whole series of actions on your web browser, you know,
*  99% of the time correctly, I'm not sure they're on track to that. And it's not obvious to me
*  scale an additional inference compute alone, especially given the sort of like exponential
*  inference costs that he seemed to be showing with their current model. Right. And so if I knew more
*  information about like how they were planning on solving those problems, then I might become more
*  optimistic or less optimistic about what they're doing. Cool. Well, this has been outstanding. Any
*  other closing thoughts you want to leave people with before we break? Yeah, I don't know. I mean,
*  I guess I'm just going to do like maybe a final pitch for reading the paper. I think we covered
*  a lot today, but in many ways, a lot more to the paper that we didn't really talk about. And I
*  think a lot of that is like, if you like thinking about things like what are human values and how
*  do we represent them, what is limited about a sort of conception of rational choice that doesn't
*  really capture what humans are actually doing. A lot of paper sort of comes from that angle. So I
*  really trying to rescue the concept of practical rationality or practical agency from this very
*  flattened picture that we get from utility theory. And there's I think that's stuff we didn't quite
*  cover today and in today's podcast. And I think there's a lot more to that in the paper. So if
*  you're interested in that kind of thing and interested in thinking about how it's relevant
*  to AI alignment. So just getting the paper, there are a bunch of like nice summary tables that help
*  you sort of like digest things more easily. So and shout out to my co-authors on that paper,
*  Michael Carroll, T.R. Franklin and Hal Ashton for working on that incredible two-year long journey.
*  Paper is beyond preferences in AI alignment. We'll link to it in the show notes.
*  Tan Zhixin, thank you for being part of the cognitive revolution.
*  It is both energizing and enlightening to hear why people listen and learn what they value about the
*  show. So please don't hesitate to reach out via email at tcr at turpentine.co or you can
*  DM me on the social media platform of your choice.

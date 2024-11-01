---
Date Generated: October 31, 2024
Transcription Model: whisper medium 20231117
Length: 4582s
Video Keywords: []
Video Views: 1506
Video Rating: None
Video Description: Nathan welcomes back Sander Schulhoff, creator of LearnPrompting.org, to discuss the recently released Prompt Report. In this episode of The Cognitive Revolution, we explore the current state of prompting techniques for large language models, covering best practices, challenges, and emerging trends in AI. Join us for an in-depth conversation on the future of prompt engineering and its implications for AI development.

Apply to join over 400 founders and execs in the Turpentine Network: https://hmplogxqz0y.typeform.com/to/JCkphVqj

RECOMMENDED PODCAST:
Byrne Hobart, the writer of The Diff, is revered in Silicon Valley. You can get an hour with him each week. See for yourself how his thinking can upgrade yours.
Spotify: https://open.spotify.com/show/6rANlV54GCARLgMOtpkzKt
Apple: https://podcasts.apple.com/us/podcast/the-riff-with-byrne-hobart-and-erik-torenberg/id1716646486

SPONSORS:
Oracle Cloud Infrastructure (OCI) is a single platform for your infrastructure, database, application development, and AI needs. OCI has four to eight times the bandwidth of other clouds; offers one consistent price, and nobody does data better than Oracle. If you want to do more and spend less, take a free test drive of OCI at https://oracle.com/cognitive

The Brave search API can be used to assemble a data set to train your AI models and help with retrieval augmentation at the time of inference. All while remaining affordable with developer first pricing, integrating the Brave search API into your workflow translates to more ethical data sourcing and more human representative data sets. Try the Brave search API for free for up to 2000 queries per month at https://bit.ly/BraveTCR

Omneky is an omnichannel creative generation platform that lets you launch hundreds of thousands of ad iterations that actually work customized across all platforms, with a click of a button. Omneky combines generative AI and real-time advertising data. Mention "Cog Rev" for 10% off https://www.omneky.com/

Head to Squad to access global engineering without the headache and at a fraction of the cost: head to https://choosesquad.com/ and mention “Turpentine” to skip the waitlist.

CHAPTERS:
(00:00:00) About the Show
(00:02:35) Sander Schulhoff, Learn Prompting
(00:05:22) Hack-a-Prompt updates
(00:12:39) The team behind the report
(00:18:40) Sponsors: Oracle | Brave
(00:20:48) The tech side of things
(00:22:24) The taxonomy
(00:25:06) Diamonds in the rough
(00:28:32) Few-shot prompting design decisions
(00:34:01) Sponsors: Omneky | Squad
(00:35:48) Example vs. Exemplar
(00:38:24) Exemplar Format
(00:42:04) Elaborate Instructions
(00:44:22) Variation in Performance
(00:46:46) Prompt Robustness
(00:50:54) RLHF vs. Base Models
(00:52:42) How to improve your prompts
(00:55:22) Ensembling
(00:58:41) Bootstrapping into fine-tuning
(01:02:04) Multimodal
(01:07:41) Agents
(01:09:47) Automated prompt engineering
(01:12:35) Productizing learn prompting
(01:14:28) Lessons from leading a team
(01:16:00) Outro
---

# Delving into The Prompt Report, with Sander Schulhoff of LearnPrompting.org
**Cognitive Revolution:** [July 09, 2024](https://www.youtube.com/watch?v=tv8kqWuEA9Q)
*  Hello and welcome to the Cognitive Revolution, where we interview visionary researchers,
*  entrepreneurs, and builders working on the frontier of artificial intelligence.
*  Each week we'll explore their revolutionary ideas and together we'll build a picture of
*  how AI technology will transform work, life, and society in the coming years.
*  I'm Nathan Labenz, joined by my co-host Eric Torenberg.
*  Hello and welcome back to the Cognitive Revolution.
*  Today I'm excited to welcome back Sandor Schulhoff, creator of LearnPrompting.org
*  and organizer of the Hack-a-Prompt contest that we discussed when Sandor was last on the show
*  back in January. This time, Sandor's here to talk about the recently released Prompt Report,
*  a mammoth 78-page survey paper covering the current state of prompting techniques
*  for large language models. As AI capabilities have exploded over the last couple of years,
*  so too have the number of papers exploring how to get the most out of these models
*  through clever prompting techniques. Sandor and his team took on the Herculane challenge of
*  reviewing and categorizing this vast literature to create a comprehensive taxonomy and guide to the
*  field. In today's conversation, we delve deep into some of the key findings and insights from this
*  work. We discussed best practices for few-shot prompting, the challenges of ensembling and
*  evaluation for open-ended tasks, multilingual and multimodal techniques, the current state of
*  prompting for AI agents, and even how automated prompt optimization systems like DSPi can outperform
*  human prompting experts like Sandor, a result that I personally can't help but see as a sign of things
*  to come. Beyond the technical details, Sandor also shares his experience leading a large research
*  team and offers reflections on trust, testing, and project management that I think will be valuable
*  for anyone embarking on a similarly complex technical research project. As always, if you're
*  finding value in the show, we'd appreciate a review on Apple Podcasts or Spotify, or you can
*  just share it online with your friends. If you have any feedback or questions, you can always reach us
*  via our website, cognitiverevolution.ai, or you can DM me on your favorite social network.
*  Finally, for now, a quick update on our jobs board. I'm glad to say that I have made the first of
*  what I hope will be many very high quality connections between someone looking for a new
*  role and a very interesting startup. In this case, the startup happens to be in stealth mode for a
*  little longer yet, but I hope to tell you more about that soon. And in the meantime, I hope that
*  encourages you to submit your resume if you're interested in a new opportunity and haven't
*  already done so. Now, I hope you enjoy this wide ranging discussion on all things prompt
*  engineering with Sandor Shulhoff of learnprompting.org. Sandor Shulhoff, creator of learnprompting.org,
*  previously here to talk about the hack a prompt contest and paper, and now returning to talk about
*  the prompt report. Welcome back to the cognitive revolution. Thank you very much. So you are prolific.
*  I wanted to start off by just talking a little bit about what you do and how you're doing it all.
*  You've got the learn prompting, which originally a project last we talked had kind of evolved into
*  a startup. And then you've put together a couple like mega papers along the way as well. So what
*  does the Sandor Shulhoff portfolio look like these days? What's the status of learnprompting.org as a
*  business and how are you finding time to bring these teams together and do this deep analytical
*  work at the same time? Yeah. So starting with learn prompting as a business, we are currently
*  building out our generative AI course offerings and building up the team, actually looking for a
*  full time first hire at the moment, something of generalist to help with a bit of video creation,
*  a bit on the business side. And recently I've been experimenting a lot with automating content
*  creation for like information teaching. So there's a lot of YouTubers out there. There's a lot of
*  content on Coursera, all these other platforms talking to some C-suite execs at like consulting
*  firms. They often approach for enterprise deals and see content a couple of years out of date.
*  And it's really painful to fix that content. And companies don't want to buy that out of a content.
*  So we currently have a way of keeping our content up to date always by building these sort of
*  videos that we can compile in a way by, you know, say we have a script, we use like 11 labs to read
*  over the script. And a couple of months later, we get feedback from our customers, change the script,
*  one Python script, and the whole video is updated. So looking at a lot more of a reproducible way of
*  doing content creation there. Interesting. And that's a technique you've developed
*  as part of learn prompting development? Yeah, that's correct. So there's a lot of complicated
*  tool pipelining you need to put together. Unfortunately, there's no way to just say
*  to an agent, hey, make me a video about prompting, cover these topics, go to these websites and do
*  tutorials on them. That's all quite hard to set up at the moment. And we're building the infrastructure
*  to do that. Yeah, interesting. I mean, that's definitely a startup in its own right, if you want
*  to turn it into a cool, interesting. So heavy use of LLMs. That's something I wanted to get into a
*  little bit in the context of this prompt report on a meta level too. Before we get to the current
*  work, are there any updates in the hack a prompt world or any other new techniques or vulnerabilities
*  that you would update us on since last time? Not really. There are a couple niche things coming out
*  about attacking different systems and companies, but I haven't seen any like huge new techniques
*  come out. I think the Azure CTO put out skeleton key, but it's relatively similar to a lot of other
*  texts that we've covered. And actually with that, there was a bit of a uptick in the debate over
*  what constitutes prompt injection versus jailbreaking. I can send you like a tweet interaction there
*  after, which is really interesting to read. And actually I'm in this like security discord where
*  a lot of those prompt security people are, and it has become something of a hobby to argue about or
*  discuss the definitions of these terms because I'm pretty like set on prompt injection involves
*  like developer instructions in the prompt as well as user instructions where jailbreaking,
*  it's just the user and the model. But there's a surprising amount of discourse behind the scenes
*  on that. Interesting. What's at stake in that debate? Like why does that distinction matter?
*  Where does it become operative? Good question. I mean, honestly, it's not like an incredibly
*  important distinction for me. It's just a matter of, I guess, one clarity and two following the
*  sort of definition of the person who originally proposed it, which was Simon. And I actually have
*  a blog post on Learn Prompting about how my understanding of the definition changed over
*  time. I used to believe one thing and then actually Hacker Prompt came out and Simon put
*  up a tweet that was criticizing the definition we used. And I went back, read what he was saying,
*  and I was like, yes, we were wrong. So I wrote a little reflection on that, updated the paper,
*  and it's pretty interesting, I think, seeing my thought process change over time, which you can
*  read in the blog post. Okay, cool. Things that have caught my attention, I wonder if you have any
*  thoughts on them. One is the anthropic mini-shot. I don't know if that's, I guess, I think more of
*  a jailbreak is how they framed it as opposed to a Hacker Prompt, but you could maybe correct me
*  if I'm wrong there. Also, I follow Pliny, as I'm sure you do, who is doing all kinds of crazy stuff,
*  which is, that would be prompt hacking, right? Because he is working through like consumer
*  interfaces, which means there's presumably a system prompt. He's exposing the system prompt
*  as one of his main exploits, right? Right. I would, from a technical perspective, with
*  Simon's definition, I would generally consider what he does to be prompt injection, as there's
*  often a system prompt involved. He and a lot of other people call it jailbreaking generally.
*  He does a lot of really impressive stuff, or I should say they do a lot of really impressive stuff.
*  And as far as the mini-shot prompting goes, I guess I'm not as impressed by that,
*  because we saw a lot of techniques like that during Hacker Prompt, where people would put in
*  a bunch of few-shot exemplars showing what they wanted, and mini-shot is just many few-shot
*  exemplars, or many exemplars rather. How about on the mitigation side? It seems like the Open AI
*  paper on the hierarchical instruction following is really meant to try to address this, right?
*  Where they sort of define the system prompt is the first thing, and then you can follow the user
*  prompt, and then there's sort of this cascade of what's most important, which is pretty intuitive,
*  but actually training for that and trying to get the system to respect that consistently,
*  obviously, is where the rubber hits the road. When I saw that, I was like, oh, this seems like they've
*  made very substantial progress. And then when I watched Pliny's work and have read some of his
*  recent analysis, he has said that he feels that it's getting easier to prompt inject slash
*  jailbreak the systems as the models get more powerful, maybe because there's just more surface
*  area to attack. He's doing these weird things now where he's embedding prompts into images in some
*  cases, and he just seems to be finding soft spots in the defense that people haven't anticipated.
*  What are your thoughts, if any, on the hierarchical instruction following, and
*  how would you characterize the sort of offense versus defense dynamic in control of these
*  systems over the last six months, let's say? Not really any particular thoughts on
*  specific defenses. Actually, one thing I was interested in recently was Lacroix. I think
*  they ran a competition recently and had an adaptive system prompt where whenever someone got by it,
*  they would use that prompt injection prompt to modify their system prompt and thus improve it.
*  So kind of adapted defense over time. And I think that's a super interesting approach.
*  But I think defense here is always a losing game, unfortunately, because just for whatever reason,
*  we can't understand the models enough or can't control them enough to ensure that they won't
*  have this adverse behavior. So when you look at someone like Pliny or other company, Hayes Labs,
*  there we go. Yeah, so I did a bit of beta testing with them. And I talked to them, like a year ago
*  or something, didn't really believe that they had automated jailbreaking. I actually saw their
*  product in use, believed it a bit more, actually used their product, was extremely impressed because
*  it was able to perform jailbreaking for an arbitrary intent, like give me some bomb building
*  instructions or racist output within seconds. And I really did find that to be incredible. And they
*  were the first people I ever saw doing that. So really quite impressed with that company.
*  But overall, defending here seems to be a losing game. I really don't see a lot of promise in
*  most of the techniques coming out like training another model to detect it. I really think this
*  is a problem that's going to be solved by the model creators themselves, some part of training,
*  some architecture switch, I think it's going to be solved with the model developers at that level.
*  Soterios Johnson Does that suggest that things like the
*  anthropic Golden Gate Claude runtime feature detection are where you're thinking? Another
*  interesting one I'm sure you've seen is from Dan Hendricks and a bunch of co-authors on short
*  circuiting, where they basically again look at the representations through the layers and try
*  to identify when something harmful is emerging and to reroute that to a refusal. Is that the track
*  that you're expecting to work? Soterios Johnson
*  I have no particular opinion or guess on the track that it will go down.
*  Soterios Johnson Okay, fair enough. Well, that was all
*  catching up on previous topics. Let's get to the prompt report. This is a 78 page monster of a
*  paper. There's really a review of probably hundreds, if not maybe even into the thousands
*  of papers that have been published over the last 18 months or so as prompt techniques probably have
*  proliferated. Interested in how you brought together the team to do this because you brought
*  together a pretty substantial team and also any techniques that you used in terms of pipeline
*  language model assistance to corral this massive amount of information. Then from there, we'll dig
*  into the actual taxonomies you've created and all the finding. Soterios Johnson
*  Yeah. All right. Start with the team. Actually, I'll start a bit before that, why this happened.
*  So I was doing research under Professor Philip Resnick and I wanted to run a
*  AI human interaction study where basically I would try to measure how much more efficient
*  AI would make humans at a given task, generative AI in particular, LLM, so chat-shapti. I spent
*  maybe a couple months learning how people do this and writing up reports. At this time,
*  there were I think about 13 different studies analyzing how LLMs help people be more productive
*  and giving hard numbers. Some of the N's were quite small like 11, but you also had a couple
*  thousand people studies. And so I thought, why not do something like this? But after I got my
*  research done there and put a little report together, I realized that I really didn't have
*  time to do this. It would end up being like a six to nine month project. And I needed a pivot
*  because I needed to basically deliver something for the semester. And I thought, well, you know,
*  I've always sort of thought about and talked about doing a survey paper for prompting.
*  How hard could that be? And so I gave myself like a three or four month timeline. I was like, okay,
*  I'll go to my NLP lab clip here at UMD. And also I put like a little ad in the startup shell,
*  Discord startup shell is a student run startup incubator at UMD. A lot of very talented people
*  there. So got a few people there. And then we started doing like weekly meetings, talking about
*  what kinds of things we want to analyze, how we could use AI to do it. A couple more people
*  started to get involved. Shyam Lal from OpenAI got involved, reached out to him, and then
*  talked to some old advisors of mine. They got involved. And I was reaching out to,
*  you know, as I was reading through the literature, I was talking, I was emailing
*  authors of papers and saying, hey, you know, I really liked the work you did on this paper.
*  Love to have you come join us on this very massive project. And got a couple people coming
*  through there. And then closer to the end of the project, we had four suicide experts join as
*  authors. And this was related to the case study at the end of the paper, which is focused on
*  detecting suicidal intent in social media posts. And I think that is pretty much how everyone came
*  together. And then I think your next question was about the tech side of things. So when the
*  project started, a lot of it was, I personally think I know pretty much every prompting technique
*  that exists. So I was going through the paper and like, you know, making a bunch of sections for every
*  technique I wanted in there. And I was just reading through every prompting paper basically
*  I could find. There were some kind of smaller survey papers or specific to different domains.
*  And at this time, I was trying to figure out what sections we wanted in our paper. And we ended up
*  with like a main text prompting and the multimodal, multilingual agents evaluation. Those ended up all
*  being quite core. And so at the beginning, I kind of developed this list basically off of how I felt.
*  So somewhat arbitrary. And I got the recommendation from some of the project advisors to do topic
*  modeling, to figure out what topics in the space were actually important. We did that. And funnily
*  enough, they actually aligned with what I had already selected as the topics for the different
*  sections. So that was good. And then looking at pipeline development, we explored like, oh, can we
*  get GPT-4 to go and read like every paper on archive and see if it's a prompting technique or
*  not. And that ended up being kind of complicated and very costly. So we did a keyword search first
*  with like 44 different keywords across archive, semantic scholar, and ACL, pulled all those papers,
*  deduped them. We did a little bit of human review. So reviewed about a thousand papers and said, okay,
*  they're in or they're out according to some survey questions, which were like, oh, does this method
*  require fine tuning? If so, it's out. And so we had humans read a bunch of papers, and then we used
*  that data set to prompt a model to review the rest of the papers. And what that allowed us to do was
*  throughout the paper writing process, we could keep updating our data set by just pulling the
*  most recent papers and having the AI read through the ones we hadn't reviewed and decide if they're
*  in or out. And we had decently high accuracy there where it was a worthwhile thing to do.
*  That was pretty much the data pulling pipeline. It was quite a pain to set up and like, keep clean
*  and the pipeline itself takes like a couple hours to run. So you have to be kind of careful while
*  you're testing it, not to run it and waste a bunch of time and money and then it has an error or
*  something. So put a considerable amount of time into that. Actually, my co-author, Michael Ily,
*  really led the development of that quite strongly.
*  Cool. That's really interesting. I'm glad I asked about the techniques.
*  Hey, we'll continue our interview in a moment after a word from our sponsors.
*  AI might be the most important new computer technology ever. It's storming every industry
*  and literally billions of dollars are being invested. So buckle up. The problem is that AI
*  needs a lot of speed and processing power. So how do you compete without costs spiraling out of
*  control? It's time to upgrade to the next generation of the cloud, Oracle Cloud Infrastructure or OCI.
*  OCI is a single platform for your infrastructure, database, application development and AI needs.
*  OCI has four to eight times the bandwidth of other clouds, offers one consistent price instead of
*  variable regional pricing. And of course, nobody does data better than Oracle. So now you can train
*  your AI models at twice the speed and less than half the cost of other clouds. If you want to do
*  more and spend less like Uber, 8x8 and Databricks Mosaic, take a free test drive of OCI at oracle.com
*  cognitive. That's oracle.com slash cognitive, oracle.com slash cognitive.
*  The Brave Search API brings affordable developer access to the Brave Search index,
*  an independent index of the web with over 20 billion web pages. So what makes the Brave Search
*  index stand out? One, it's entirely independent and built from scratch. That means no big tech
*  biases or extortionate prices. Two, it's built on real page visits from actual humans,
*  collected anonymously, of course, which filters out tons of junk data. And three, the index is
*  refreshed with tens of millions of pages daily. So it always has accurate up to date information.
*  The Brave Search API can be used to assemble a data set to train your AI models and help with
*  retrieval augmentation at the time of inference, all while remaining affordable with developer
*  first pricing. Integrating the Brave Search API into your workflow translates to more ethical data
*  sourcing and more human representative data sets. Try the Brave Search API for free for up to 2000
*  queries per month at brave.com slash API. I just did a control F through the paper and
*  confirm that the word delve does not appear even once. Did you remove all the delves from the chat
*  GPT output or what? To be honest with me. That is a really good question. I did not explicitly do so.
*  So I should say that all of the paper writing is human done. People likely used
*  chat GPT or whatever to some small extent while writing. And I will say, you know,
*  this is something you really need to be careful with when you're running a large research team.
*  There were times when I was reading through it was like, ah, someone used AI to generate text. And,
*  you know, I don't really care about that. It's not a problem. The problem was that they did it badly.
*  And so the wording didn't really make sense. And it was kind of obvious, you know, you could tell.
*  So I performed at least five passes of the 70 plus pages to remove all of this stuff.
*  Just sort of over time, I would do pass and pass and pass updating stuff. But my final pass,
*  I was like, okay, I'm going to read every single word and make sure there's nothing weird here.
*  Someone probably use the word delve and I removed it. But I never did a control F
*  to find all the delves. I'm actually very surprised that there are no delves. I would
*  expect there to be at least a couple. That's very funny. Okay, cool. Really good insights there.
*  So coming to the results then, I kind of want to just start at a high level and then go down
*  some of these particular kind of use case or smaller scale areas. Let's start off with just
*  the overall taxonomy. I've got the graphic in front of me. People can pull up the graphic and
*  look at the hierarchy there. But how do you sort of describe this using your own heuristics,
*  your own mental models? Sure. Good question. So whenever I think of prompting, I think of,
*  I guess this is more in the sort of advanced category of prompting because you often need
*  code or some kind of pipelining to build a lot of these techniques. I just kind of naturally
*  classified things into different domains. You have your few shot prompting, your chain of thought
*  prompting. Actually, a lot of people think chain of thoughts. Oh, it's just like one thing chain
*  of thought. But no, there's actually a ton of really super specific chain of thought generation
*  techniques. And then you have stuff like decomposition, where you're breaking the
*  problem down into usually multiple sub problems. There was actually a lot of debate about whether
*  to combine the decomposition and chain of thought, thought generation sections into one. And the
*  argument for that is kind of like, okay, chain of thought, you're prompting it to generate its
*  thought. And naturally, it like breaks the problem down in doing so. And so it's kind of
*  decomposition. And then there's also a lot of decomposition and chain of thought techniques,
*  which are kind of similar. And some bridge the gap where it's like, okay, write out all your
*  thoughts and break the problem down into sub problems. That's your thought generation prompts.
*  And how do you classify that? Sometimes we had to make these slightly arbitrary decisions where it
*  could have gone either way. And this is really just one way of organizing these techniques. I
*  could imagine another where you have like a very different type of graph, where each technique is
*  assigned to multiple possible categories. And another example of this is few shot, combined with
*  chain of thought, lots of techniques doing that, really a natural extension for many techniques,
*  even if not done explicitly in the paper. So there's a lot of kind of confusing stuff,
*  how to categorize stuff. Then you have a lot of zero shot things like role prompting, style prompting.
*  And then let's see, ensembling, when you have kind of multiple prompts trying to answer the same
*  question, and then you usually use the majority result. And then self criticism, when you get the
*  model to criticize its own output, and then usually improve it. Those are kind of all of the
*  the really fundamental classes of advanced techniques that I found. And then there were
*  even more advanced techniques that we left for later sections like the agents and eval section.
*  Okay, cool. Yeah, it's almost like you need a this is probably just because I have sparse auto
*  encoders on the brain, but it's almost like we need a sparse auto encoder for the different prompt
*  techniques to then say like, which of the techniques is active in any given prompt,
*  because certainly they do recombine in all sorts of different ways. I guess high level highlights
*  anything that you've found to be like, you know, diamond in the rough kind of discovery or anything
*  you think is like, underrated from a prompt standpoint that people, you know, and you can
*  assume with our audience, like they're going to know few shot techniques, they're going to know
*  a chain of thought, but kind of going into that second or deeper levels of your analysis, was
*  there anything that jumped out at you as being like, more people should know about this? Yeah,
*  first thing we went super in depth on few shot, there ended up being a lot of research there and
*  also a lot of stuff that we could clarify there. So one thing is like, few shot and in context
*  learning is not at all the same thing. When you prompt chat GPT and say, tell me a story about a
*  dinosaur, that is in context learning, technically, according to Brown 2020, because in context
*  learning is a form of task specification. And the idea here is like, in the past, we'd train models
*  to do a very specific task, like classify Reddit posts as positive or negative sentiment. Now we
*  have these LLMs that do any task, all you have to do is give them the task and they do it. And the
*  process of you giving them that task to do and them doing is novel. And so in Brown, they call
*  it in context learning, but they also consider few shot prompting to be in context learning.
*  So there's a lot of discourse in the community that conflates the two. We even found other
*  research papers who had read through Brown at all and still conflated them, which was an
*  app paper is the language models are few shot learners. That's the original GPT paper. Yeah.
*  So reading through that paper, I probably read through the paper actually 20 times or more.
*  And talking to Shyamal from OpenAI about it, you know, he was able to ask internal questions to
*  the team was super helpful as well. But besides the definitions, we were able to pick out six
*  key pieces of advice when designing a few shot prompt. And this is a diamond that I wish I had
*  like a year ago, because we really go through kind of all the things you need to consider.
*  How many exemplars do you want? Does the order of the exemplars matter? I think that's super
*  surprising to people that like, depending on how you order the exemplars in the prompt, you can
*  be down to 0% accuracy, up to 90% accuracy, really all over the place. So that is like
*  a super surprising and honestly quite frustrating thing to realize, because it feels so arbitrary
*  and there's no way to figure out what's optimal. So can we be a little more explicit about this
*  six point thing? Is this section 2211 few shot prompting design decisions? This is yeah,
*  effectively I'm referring to figure 2.3 in particular. Okay, yeah, exactly. Perfect. So
*  you want to run through that in just a little bit more detail? Let's take our time on the diamonds.
*  All right. So we have six pieces of advice. Basically, each piece of advice could hurt
*  accuracy, but generally improves it. And I just sort of say that as a warning where these aren't
*  guaranteed to give improved results, but many times will. All right. So first one is the quantity of
*  exemplars. It generally helps to have more exemplars. I try to put as many as is reasonable
*  in my prompt, kind of weighing like costs with accuracy, and also speed. And then exemplar
*  ordering, we recommend that you randomly order the exemplars, because if you put like all of the
*  positive exemplars first, and then all the negative ones, the model might be biased to choose a
*  negative one next, because it's just seen so many negatives in a row. And then you have label
*  distribution. You want a balanced label distribution, which basically means if you're
*  doing binary classification, you want an equal number of exemplars from each class. That being
*  said, I put an additional note here, which we don't have in the figure, but do have in the paper.
*  If you have already imbalanced data distribution that you're trying to predict, say, you know,
*  like 90% of classifications are going to be positive, that's just the ground truth.
*  If you include a sort of a nine to one exemplar ratio, that can boost your accuracy overall.
*  So generally shoot for completely balanced, but depending on your data distribution,
*  you can change that. Next thing is exemplar label quality. Ensure exemplars are labeled correctly.
*  The reason why we mention this is because one, there's a lot of research that suggests that
*  even if you input incorrect labels with your exemplars, it doesn't hurt accuracy all that
*  much. And then the second thing is people often sort of auto-generate prompts from data sets
*  where they have exemplars in the data sets that might be mislabeled. And so if you really want to
*  make sure you have the best chance of getting good accuracy, you want to make sure those exemplars
*  are properly labeled. And then the next thing is exemplar format. So a lot of the time when I put
*  exemplars in my prompt, I do like a Q colon input, enter A colon output. So that could be like
*  question Q, I'm so mad, answer A, angry. If I'm doing, you know, binary classification of
*  sentiment, something like that. And so we say choose a common format because reading this paper
*  that talks about prompt mining, I don't remember the original paper, but we have it in our paper,
*  they found that by reading through a corpus that the LM was trained on and finding common formats of
*  sort of questions being asked and answered, if they use that in their prompt, they were able to
*  improve their accuracy. And I think that this has something to do with sort of, let's see, how do I
*  explain it? Do you know the idea of if you have a smooth loss function, generally you can get better
*  results when minimizing it? Yes. Okay. So I think that there's a similar thing that happens where
*  the space in which you ask questions is smoother. If the LM has seen that format in the past,
*  then it would be otherwise. So if I say like question 10 equal signs, I feel sad,
*  answer 10 equal signs, angry or sad or negative, the LM probably hasn't seen that format before.
*  So it's probably going to be a bit confused or a bit more confused as to what to do there.
*  But anyways, moving on to the last one, which is exemplar similarity. So say you have a test instance,
*  you're trying to classify the phrase, I'm so excited. And you have exemplars in your data
*  set that you want to put in the prompt, you can retrieve similar exemplars to that test instance,
*  put them into the prompt, and then the LM has a better chance of accurately predicting it
*  because it sees similar exemplars to it. And in this case, it is necessary to dynamically
*  generate the prompt at inference time. But there's a lot of techniques that do this. However,
*  there are other papers that suggest if you put diverse exemplars into the prompt, then you'll
*  have improved results. But generally, I found similar exemplars do the job much better. And
*  there's more like there's specific cases where diverse exemplars might help. That is the end of
*  the six. Cool. So first of all, what's the difference between an example and an exemplar?
*  Good question. Since we're into the nitty gritty of the terms and the definitions.
*  Yeah, so you can kind of think of it as like exemplar is a technical term for the example
*  that you're showing in the prompt. I'll let people say example. Equivalently doesn't really
*  matter for the most part. But I try to use the technical word because it is more specific to
*  this format. And you could say something like, Oh, I have a data set of examples that I want to put
*  into my prompt. And only when they are actually in the prompt, do I call them exemplars. So it's
*  kind of like exemplars just with a more technical appropriate term. That's the way I like to think
*  about it. Okay, cool. Hey, we'll continue our interview in a moment after a word from our
*  sponsors. Omnike uses generative AI to enable you to launch hundreds of thousands of ad iterations
*  that actually work customized across all platforms with a click of a button. I believe in Omnike so
*  much that I invested in it. And I recommend you use it to use cog rev to get a 10% discount.
*  Hey all, Eric Torenberg here. I'm hearing more and more that founders want to get profitable
*  and do more with less, especially with engineering. Listen, I love your 30 year old ex-fang senior
*  software engineer as much as the next guy, but honestly, I can't afford them anymore.
*  Founders everywhere are trying to turn to global talent, but boy is it a hassle to do at scale,
*  from sourcing to interviewing to on the ground operations and management. That's why I teamed
*  up with Sean Lanahan, who's been building engineering teams in Vietnam at a very high
*  level for over five years to help you access global engineering without the headache.
*  SQUAD, Sean's new company, takes care of sourcing, legal compliance, and local HR for global talent
*  so you don't have to. With teams across Asia and South America, we can cover you no matter which
*  time zone you operate in. Their engineers follow your process and use your tools. They work with
*  React, Next.js, or your favorite front end frameworks. And on the back end, they're experts at Node,
*  Python, Java, and anything under the sun. Full disclosure, it's going to cost more than the
*  random person you found on Upwork that's doing two hours of work per week, but billing you for 40.
*  But you'll get premium quality at a fraction of the typical cost. Our engineers are vetted
*  top 1% talent and actually working hard for you every day. Increase your velocity without
*  amping up burn. Head to choose squad.com and mention Turpentine to skip the wait list.
*  SQUAD, Sean's new company, takes care of sourcing, legal compliance, and local HR for global talent
*  so to recap, the more the better. Randomly order them so you're not creating a bias. I suppose you
*  could also argue for an intentional ordering, right? If random is better than all the positives
*  before all the negatives or whatever, then interweaving them? But I guess then too, you
*  might have an issue of creating a TikTok pattern that it might also be biased to follow.
*  So you've got lots of little issues there. The random ordering seems best if you're going to
*  do some sort of ensemble or majority rules sort of technique. But if you had to choose between
*  random ordering and intentional ordering, do you think you can improve on random with an
*  intentional setup? Usually not. I'd say the cases that are quite limited and be more of an instance
*  of getting lucky. Interesting. Now, when you're measuring these, are we measuring these at a
*  sort of aggregate statistical level? How do you mean? Well, this is sort of in this kind of like
*  random versus intentional ordering of the exemplars. If I'm doing one thing in chat GPT,
*  intuitively, it feels like I should set up, use my best guess as opposed to take a random guess.
*  But then if I'm using a sort of large end benchmark to evaluate my strategy, then I might be like,
*  well, yeah, maybe random there is better because I haven't seen all the examples and my intentional
*  design is inherently biased because of the few cases that I considered when making it.
*  So I guess the question there is really like, to what degree some of these techniques depend on
*  large and evaluation of the technique versus just like, I'm trying to do one thing right now,
*  what's going to get me the best results? I don't know if there's any data that would allow us to
*  resolve those. Right. I will say that we report these six techniques based on other papers that
*  study them directly. And so they generally have some empirical results where they run it on a data
*  set and say, oh, like the random ordering is better because our ordering was biased
*  or something like that. We did not run studies of our own with these different pieces of advice,
*  but they do correspond to my anecdotal experience, which is not limited, really. And also my intuition
*  as far as prompting goes. Okay, cool. So again, just to quickly recap, the more exemplars,
*  the better use random ordering, or at least we can very confidently say, beware the creation of bias
*  in your ordering. Have a distribution that is ideally representative. Obviously look at your
*  data, probably the number one commandment in all of LLM usage. Make sure that the exemplars that
*  you're using are correct. I think the format one is really interesting. I wonder if you have a,
*  what's a good format? What's a common format? What's an intuitive format? One idea that comes
*  to mind for me is just ask the language model to format the thing in the most intuitive way for it.
*  What would you say? I almost always use the Q input, A output format. I've tried augmenting that
*  to be like, instead of Q and A, question and answer, but Q and A seems to work really well
*  because, well, I suppose because historically that's been what has been used in a lot of
*  datasets. And so LLMs have kind of been trained to know that format really well. If you're doing
*  some other task though, that's not like a strict Q and A, you like the intuition, you still use it.
*  I'm thinking about like the way Mark use case. Our job is to write a script for a video. No,
*  I suppose I could just put like Q colon, everything that I have in the prompt and then A
*  colon, and then like, you know, get the response. That feels odd, but you know, I can't say it
*  wouldn't work. What do you think about my intuition though? I developed my syntax for what is the
*  structure of a prompt, kind of using my own intuition, trying to keep it minimalist,
*  trying to keep it readable, trying to keep it clear. I will say though, I didn't like study
*  the perplexity of every token. And so there could be some tokens in there that are like
*  placing more strain on the model than I would like. I guess looking at perplexity, I just said
*  would be one interesting way to kind of spot ways in which your prompt is like making the model work
*  too hard or harder than you want it to. And then my other ideas, you know, have just giving it my
*  thing and saying reformat this in the most obvious way possible. Those feel like they
*  are good ideas or how would you riff on that? Yeah. So I guess my general advice would be
*  the best thing to do is use your domain expertise with an understanding of what is standard. And to
*  give you an example of someone not following this advice, I was recently watching someone
*  try to analyze stock data and they were formatting their exemplars as like big paragraphs all put
*  together and they would put in like, if you see this input in quotes, comma, then output this.
*  And then they would have like another one and be like, oh, however, if you see this input instead,
*  then output this. And so it was a very inconsistent format where they would,
*  it wasn't really very structured and they were just using English, well, of course, English language,
*  but they were formatting it as kind of an essay about what to and not to do. Whereas what I always
*  do is have a structured input output, as I said, the QA, and that's what I've seen to be standard.
*  And so someone like that could have benefited from knowing, oh, like if I do something like QA,
*  that'll be a bit better than what I currently have. And so I'm sure what you're doing is fine.
*  And I doubt that you would benefit that much from switching to the QA, for example.
*  How do you think about that in the context of like elaborate instructions though? I mean,
*  the examples in this figure are all relatively simple. They're basically classification tasks.
*  But if I'm doing a generative task where I do have these more elaborate rules and we do have
*  this at Weymark where it's like, we want, for example, we're writing scripts for small businesses,
*  right? So inevitably there's going to be like contact information. They're like,
*  visit us at our website or call us today or come to our store or whatever. And we want to use those
*  in like the right place. And so we sort of have instructions that are like, use the contact
*  information where shown in the example. But sometimes the business itself has a brand
*  that is contact information. Like in Michigan, where I live, there's the legendary 1-800-CALL-SAM.
*  And that's like, the brand is the contact information. So we have like these kind of
*  caveat exceptions. Is there any way to present that to the language model that would be more
*  intuitive or more helpful to it? How do I play to its strengths when I have these sort of elaborate
*  constructions? When I have these tasks, I generally do, I keep a structured format,
*  but like I'll probably use something like instead of Q&A, I'll say like, this is the input colon
*  and put the input there, put an enter or two, and then say like, this is the output.
*  And then after each exemplar put like 10 equal signs or something like that, just to try to show
*  the LLM that, okay, this thing was just one exemplar all by itself because I don't want it to like
*  kind of merge multiple exemplars together and think they're all one thing. That's what my intuition
*  has told me. I would love to see a paper come out and analyzing all these different formats
*  across models. And this would actually be a decently easy paper to write because you just
*  have to do a bunch of different runs through the models with a number of different formats.
*  But until then, I can't really say anything besides my intuition there.
*  Okay, cool. Well, if you're listening and you want to volunteer as tribute for this project,
*  reach out to me and or Sandra, we'll see if we can't give you some direction.
*  More you than me. I'm volunteering you mostly there. I'll trip in, but you've got deeper
*  expertise than I do. So the final one, just to finish my recap is exemplar similarity. This is
*  like kind of a rag style, if I understand correctly, strategy where it's like we've got a big database of
*  examples and then we want to pull in some. And I would also imagine probably doing this
*  maybe in like a hybrid way where I maybe would like fix a couple of them and then
*  and in a couple more dynamically at runtime to try to make sure I have some control, you know,
*  still, but that I'm also, you know, finding the most similar ones to give it the best guidance
*  that I possibly can. That's good. I think that's really practical stuff that people can take in
*  and run with. How much do you see this varying across models? I mean, I don't know how well you
*  sleep at night, but if you're up worrying about the generalization of your research, I would
*  imagine one big worry would be like, shit, how does this apply to Gemini 1.5, you know,
*  next or whatever, right? How much variation do you see? This is honestly a kind of a question that I
*  hate, not because it's a bad question, but because it's such a good question and I can't answer it
*  well. In the paper, we did studies with really just one model, which is GP 3.5. I would have loved to
*  do it across a lot of different models. And in fact, we even did it to some extent with GPT 4,
*  but we found that time more than anything was restricting our ability to do all this and not
*  time in terms of setup time, in terms of running all these prompts, it would have taken like about
*  a month to run all of this through the models we would have wanted, which would have included GPT
*  4 and others. And that's because we're doing it through these sort of public APIs, which are
*  slower than training API or if you have access to the base model, like maybe scale does,
*  you can run these evals a lot faster. So I am concerned about how these techniques do
*  generalize, but I think the few shot advice is sound across models. And also, every technique
*  in that paper can be implemented with any standard LM. So open AI, cloud, Google, all of those can be
*  used to implement these techniques. There's probably some performance difference across them
*  as far as re-sync and ability to break down problems goes, but I'm only reasonably concerned,
*  not like too concerned, I guess. Okay. Sounds good. How about on the another sort of weirdness,
*  right? We see these examples all the time where some like seemingly innocuous change to a prompt
*  can make the difference between good and bad performance. Some of that may just be noise,
*  but even at like temperature zero, it seems like we've got examples where I add one extra
*  space between sentences or whatever. And it's like, oh my God, something seemingly so
*  inconsequential becomes like quite consequential in some cases. Do you have any sense of how
*  real of a problem that is? I mean, I don't want to be dwelling too much on just like cherry picked
*  random examples, but I honestly have no idea if that's something that I really should be
*  worried about. I've always been a two space person between sentences and I've stood up for that for
*  a long time. However, if it's going to hurt my language model performance, then that would be
*  like one really good reason to reconsider. Interesting. I am definitely a one space person.
*  So what you're saying, it is absolutely a problem. I think we talk about it in our like reliability
*  or alignment section. It should be less of a problem over time as the models get better.
*  And in fact, I believe that like GPT-4 is much, much better at dealing with that than like GPT-3
*  was. I honestly haven't seen anything recently about this having a big impact on prompt performance.
*  And whenever I'm developing a prompt, I'm not like studying, oh, if I change this word or
*  remove this one word, is that going to have a big impact? So it's kind of something that I just know
*  is there, but can't do too much about and generally assume won't affect performance too much.
*  Okay, cool. I guess basically the trend is that it's less of a problem over time. And it seems
*  like with kind of maybe more epochs of training, more overfitting in general and like more
*  RLHF, we're just kind of gradually hammering these oddities out of the models. Is that basically the
*  underlying story? I would say more and better training. Honestly, I'm not sure about the RLHF
*  part because I think that has been shown to decrease accuracy. And so maybe would
*  introduce more of those oddities. I think like RLHF in general decreases the accuracy because
*  it's kind of like a trade-off between model accuracy and niceness of human interaction.
*  Interesting. So you think you can get better performance? I certainly have experienced this
*  on some tasks like joke writing, for example, or imitating a certain famous writer's style.
*  You get a way better imitation out of the base model than you do out of the RLHF model. Also,
*  just like random number generation has been reported as way better from base models as
*  opposed to RLHF. You think that's like a across the board trade-off? If it was something like a
*  coding task, I would have assumed that the RLHF models would give you more accurate code than the
*  base models would have. But I don't know, maybe not. I think that really depends how you're using
*  RLHF. If the learning signal is like code accuracy or how much human likes the code
*  and likes how it looks like. The latter is a poor signal of performance than the former, which
*  is directly based off of code performance. Yeah. Okay. That makes sense. And I guess as far as
*  the RLHF safety tuning goes, I've been recently frustrated with GPT-4 because it's like too
*  closed off. So I've been trying to understand credit scores, like my credit score recently,
*  better and trying to get the model to tell me how the credit score calculation might work.
*  It's like, oh, it's proprietary information. So I'm like, oh, well, could you just give me
*  an example of how the formula might look? And it says, oh, it might be harmful to output such
*  information. And I'm trying to learn and that's pretty frustrating. So I don't want to see
*  that. So do you use base models regularly? I was just looking at Llama 3.7DB and comparing
*  instruct versus not instruct on the Together AI API. They do have both the instruct and not
*  instruct set up there for people to play with and to call the API. Is that like, how often do you
*  go to a base model? No, no, I generally only use chat GPT for CLAWD for coding tasks. Those are my
*  two mains at the moment. I don't use a lot of base models unless I'm going to do a research paper
*  using them. Interesting. Well, you might actually have a pretty good experience with that. I was
*  trying looking at a couple of different things like synthetic, like opinion data and trying to
*  think about how could we kind of take like a seed of somebody's opinion profile and expand on it.
*  And my intuition is that the base models would probably be better for that. And then also with
*  this like impersonation task, it's like, or again, code grading, it's like, can be a lot better.
*  The RLHF models are not funny. I would say that's like, they're pretty limited in every
*  regard. Even just titling the podcast. Sometimes I have like, you know, I know what I want to title
*  other times. I'm like, I want, you know, can I get something a little punny? I need to start
*  going to the base models a little bit more because the RLHF ones are just so often like,
*  a little boring. And I think I can maybe get some more outside the box ideas,
*  probably just higher variance in general. I'm sure if you were to score them, you know,
*  take the average score across all the ideas generated, they would probably score worse.
*  But where I'm really looking for the highest max score, then I think you would find something
*  often from the base models could be better. Okay, cool. Let me just pitch you a notion of
*  how I typically work and how I advise others to work and tell me if you would change it at all.
*  Obviously, you've got like tremendous detail here. But if somebody comes to me and they're like,
*  hey, I'm trying to get an AI to do X task. And it's like kind of complicated. I asked you to do it.
*  It's not really working or it's not working well enough. Like what do I do next? What I always
*  tell them is staple your pants to the chair for a couple hours and write out a handful of
*  gold standard examples where you're going to explain your reasoning in painful detail
*  on your way toward the actual output that you want. And most of these outputs, like obviously with,
*  you know, with benchmarks, like there's, it's very helpful to have sort of a ground truth answer.
*  But a lot of what people actually want to do in applications and in workflows in their businesses
*  and whatnot is not limited to a classification or a multiple choice where there's like a concrete
*  ground truth, right answer. People want it to generate something and they want that thing to
*  be good. So I'm always like, you know, kind of use the like task decomposition, really think
*  super hard, like introspect hard on what are the logical jumps that you're making? What are the
*  cues that you're zeroing in on that really matter? Try to get explicit about that stuff to the like
*  maximum degree possible. When you think you've like said it all, like go back and try to be even more
*  explicit about all the hints, all the cues, et cetera, that you're using. And then finally work
*  your way up to generating something good. And then with a handful of these, you are probably like
*  going to get much better results. If that still isn't good enough, then maybe you could think
*  about using that as like a bootstrap into a fine tuning loop, which I know is out of scope for this
*  paper. But how does that compare to the advice that you give people who are, you know, not 76
*  pages into all the different techniques, but are like, this isn't working for me. What do I do?
*  You know, short answer. Honestly, I think I'd have pretty much the same advice. The exemplars are
*  super important. My favorite way to improve the prompts, because a lot of people come in and,
*  you know, just put their instructions and hope that it'll do the job. But showing multiple,
*  at least three examples of what should be done can really, really help. So completely agree with you
*  there. Okay, cool. Good to know. Next section, I have just kind of a number of questions that
*  came to mind as I was reading through the paper that are on kind of specific subdomains.
*  On ensembling, there's a lot of different techniques, of course, mostly, again, they seem
*  to sort of be predicated on this like ground truth or like some sort of discrete nature of the answer,
*  where, you know, if it's a classification task or multiple choice, if you run a model 10 times
*  and you take the most common answer, like that'll help boost your overall correctness score. Is there
*  any way to extend to domains that are not like single answer that's like right or wrong, but,
*  you know, a more kind of open ended generative task? I would love something there if there's any
*  known techniques. So, okay, do you have ground truth examples of what you like? Yeah, I'll say
*  yes, or I can make them. Maybe like I missed part of the question. Would you mind reiterating the
*  question? Yeah, I guess somewhat abstracted way to say this is we know that there are a number of
*  ways to spend more compute to get better results. And you can do that by like chain of thought,
*  you know, is often described that way. You can do it by this sort of majority vote, if you have
*  something concrete to vote on. But if I want to write a video script for Weymark, for example,
*  or, you know, anything along those lines where it's like, there's not a right answer, but there
*  are definitely better and worse responses. How can I spend more compute to get a better
*  video generation? Maybe it's not ensembling. Maybe it's like self-criticism. That was going
*  to be my next question. I just beyond the simple chain of thought, how do I spend more tokens,
*  spend more money to get better results? Right. All right. I do understand your question now.
*  Thank you for clarifying. I do have an answer, but it's kind of frustrating in that it's a lot
*  more complicated than for, you know, techniques where you do have simple accuracy based metrics.
*  So number one, that would be like, you have some pipeline where you generate the initial script,
*  and then you pass it with a like a new prompt that says, oh, you know, revise this script
*  according to insert blank guidelines that you want. And then maybe you even have like a couple
*  different parts of the script generated independently. So you have your outline,
*  maybe then there's a criticism of the outline and then the new outline gets passed in, say,
*  you know, generate this script and then you have the bot criticize each part individually. Another
*  thing you could do is a multi-agent setup where you give each agent a role where like one is the
*  sort of main writer and then there's like a grammar checker and a style checker and they all kind of
*  work together. I've seen a couple of papers coming out using that multi-agent technique and
*  even like multi-agent debate techniques, which are very interesting. I don't think they're there yet,
*  or it'd be worth spending time implementing them. But the former where you have sort of the self
*  criticism according to some guidelines might be worthwhile. But if I were doing this, I probably
*  wouldn't implement it because I still feel like the techniques are not there yet where it would be
*  super helpful. It's a bit of a frustrating domain where I don't know of a good solution to the
*  problem. So maybe the better way to spend compute for those kinds of things is going back to that,
*  like bootstrapping into fine tuning loop. Like the second part of my advice to people is if you've
*  written, let's say at least five, you know, maybe 10 really detailed painstaking gold standard
*  examples and that's still not working for you, then I say, okay, now start generating. First of
*  all, you could do just more generation by hand, but people typically tire of that pretty quickly,
*  especially because they're going to need another order of magnitude in all likelihood. So my next
*  advice is beyond pure prompting, but use those examples with the best available model to generate
*  more examples. Now you have a human classification problem of which you like and which you don't like.
*  Basically expand your data set of things that you like by generating and filtering and then fine tune
*  on those. And hopefully with 10X more, like I usually think of it as like start with a couple
*  examples, fine tune potentially with as few as 10, certainly fine tune again at 100, you know,
*  maybe go to a thousand. Hopefully you'll both get more like robust coverage. Hopefully you'll
*  get better performance and you're just spending that compute at the fine tuning stage instead of
*  the inference time. Is that what you would recommend? I mean, it's fine, you know,
*  for the purpose of like whatever gets best results, we're not limited to pure prompting.
*  So is that where you would kind of steer people? I like that idea in the same regard as I like the
*  other two ideas I mentioned. It can definitely help, but I would not necessarily have more
*  certainty in that technique than the other two prompting based ones. But if it's working for you,
*  is it working for you? Yes. I mean, we could always debate, you know, how well it's working.
*  Obviously we could always hope that it could work better, but I would say in our experience, yes,
*  we have the biggest leap for us with the Weimark tasks specifically was fine tuning on chain of
*  thought reasoning as opposed to fine tuning purely on inputs and outputs. And then, yeah,
*  it seems like a bit bigger data set. You know, we also kind of try to cover edge cases progressively
*  over time when we see things that aren't working. We try to go back and generate a few examples of
*  those and include those in the fine tuning data set next time. And yeah, I would say that broadly
*  seems to be working like cost wise, it ends up being prohibitive and latency wise to some degree,
*  it ends up being prohibitive to like try to cover all the edge cases in the runtime exemplars.
*  The fine tuning, at least with open AI is more expensive, of course, but it, you know, is not as
*  much more expensive as like trying to put 20 examples into a single prompt to cover everything.
*  So I would say it is working, although, you know, this also brings up the evals question,
*  which is like, how do we really know? And who are we trusting to make that decision? I wouldn't say
*  we've entirely left the vibes domain in terms of how we're assessing this. We do have some structured
*  evals, but we see enough edge cases there that we like don't fully trust that. And, you know,
*  we're definitely still trying to live by the look at the data and actually use the product regularly
*  sort of approach, because I don't think there's anything automated that we trust to really tell
*  us for sure if like the new fine tune is better than the old fine tune or whatever, like, that's
*  not the kind of thing I would say we can resolve through a purely automated approach as of now.
*  Right. Yeah, fair enough. That is a pretty awesome development for you all.
*  Okay. I've got like five more things and I'll just limit my side of the discussion. So
*  multilingual is another area that you cover. I've seen in the past that English seems to be best,
*  like that seems to be the main takeaway. And so the kind of techniques here are like translate
*  in English first, then do the hard part, then translate back. I also noted an interesting
*  bit from the paper on running certain tasks in multiple languages and then like
*  sort of a multilingual ensembling approach, which I thought was very creative. I'd never seen that
*  before. Any other notes or surprises, fun tidbits from the multilingual? I was going to say the
*  second one that you said, because that was my favorite as well. Okay, cool. How about multimodal?
*  This is, I feel like very much kind of black magic. You know, I've seen a number of things that seem
*  like they help, but it seems like it's just all way less studied, way less established. And that's
*  kind of a reflection of where we are in AI generally, where the capabilities are coming online
*  faster than they can be systematically studied. But what jumps out to you from multimodal?
*  Yeah. So my favorite one there is chain of image prompting, where the GenAI has some sort of visual
*  reasoning question, like given a line, Y equals X and a circle defined in its sort of mathematical
*  function, do they cross? And so what it can do is, okay, it graphs the circle and then graphs the
*  line and then generates an image, renders an image using maybe like some SVG Python package,
*  looks at the image and then prompts itself to ask itself, do they cross? And then there's like sort
*  of longer chains of reasoning you can do there. So I really liked that one because it was a direct
*  adaptation of chain of thought to the image domain using images as the steps in the thought process.
*  So I liked that a lot, but kind of bigger picture. Gen3 came out with Runway that I've been experimenting
*  with that. And I found that prompting it is extraordinarily difficult. So where we were with like,
*  I don't know, GPT-2 prompting, GPT-3 prompting at the very beginning where you had to be
*  really, really specific about a lot of things. And, you know, similar with the image prompting
*  things. With video, it's even worse. You need to be like a really good prompt engineer in order to
*  get decent results in video. Though I haven't gotten to try Sora, so maybe something like that
*  or a cling is a lot easier. But Gen3 for me and even one of my friends who is more specifically
*  focused on video prompt engineering, quite difficult to get the result you want.
*  Yeah, those are dense. The examples that I've seen are super, and just to make clear here,
*  we're kind of crossing over between multimodal prompting of your sort of like large multimodal
*  models like your GPT-4Os. And then you're also kind of talking into the asset generation side.
*  And that's a whole other beast that I honestly haven't studied super deeply. But the density of
*  the prompts that I have seen in the Runway 3 so far is like, it's pretty intense. You're talking
*  like whole paragraphs to generate a few seconds worth of video and people are being very precise
*  in terms of the compositions that they want and the transitions that they want. I think Dolly 3
*  basically has that same kind of super dense prompt, although they in chat GPT kind of generate
*  that for you and like extrapolate your, presumably generally naive, not you, but the royal you,
*  the common users, naive prompt, they kind of extrapolate that into a very dense prompt and
*  then give you the results of that back and you can sort of iterate on that. I think in general,
*  my sense of the asset generation things is that the trend is toward very dense prompting where
*  it's again, just being like extremely, extremely explicit and painstakingly detailed in what you
*  want is kind of what they are rewarding now, even if they're sort of abstracting that out of the
*  views or experience in some cases. I've seen a couple other things in image, going back to the
*  image inputs to language models where overlaying a grid or overlaying the output of an image
*  segmentation model or in some cases running a dedicated OCR model and then taking those
*  outputs and including that with the image can be really helpful. I've been trying to do some things
*  with looking at plumbing parts catalogs of all things, which in many cases were originally
*  paper and then they were scanned. And so there's like, you know, kind of fidelity issues on top of
*  the fact that these were definitely not intended for language models, but the OCR seemed to really
*  help there. If we just ask any of the frontier models to do the full thing without the benefit
*  of the pre OCR processing, it like can't get the parts numbers right. But if you give it those
*  parts numbers in text and then also the diagram, you get a much better output that actually returns
*  the appropriate parts numbers. Very interesting. Does that prompt bring anything else to mind for
*  you? No, not in particular. I have kept my prompting mostly in the text only domain until
*  recently experimenting with content generation stuff. Yeah, cool. We'll compare notes about that
*  another time. Agents, obviously super hot topic. Conventional wisdom is they don't quite work.
*  We did an episode once with one of the founders of Codium. They put out a paper called flow
*  engineering, which I really liked, which we exchanged some notes about any hidden gems in
*  the study of agent prompting. I agree with the conventional wisdom that agents don't quite work.
*  I like the simpler approaches, something like react, where you have a super simple interaction
*  with an environment. And I think you can get tool use working reliably well when it's very specific
*  tools. Overall, I am very excited about agents, but I think this is going to be something where
*  we kind of need a next step in architecture to make tool use more of a first order subject,
*  because right now it's like, oh, you prompt there, you fine tune the LM to output some specific
*  wording to use the tool, but you could also prompt it to output a new type of token. Or
*  I really love reinforcement learning. I think that LMS or whatever comes after LMS are going
*  to have to learn on their own and produce their own reward signal. And so I think RL is the way
*  to do that. Hopefully eventually RL will have its like NLP LM moment. Agents right now are
*  quite frustrating because it looks so promising, but in practice, it's so hard to get stuff working,
*  even for me. So do I have any like wonderful takeaways here? Honestly, not really. There's
*  a ton of different approaches to agents. They can do specific things somewhat well, but why can't I
*  have something that I say, oh, I just got an email. I need to pay someone, go to my bank website and
*  send them this much money. That seems pretty straightforward. I could just say that and
*  string a couple website URLs together, but I can't have that right now. And I want that.
*  Sounds like a fast way to drain your bank account at the moment.
*  Sure. And security concerns are huge. Cool. I think actually, to some degree,
*  I've buried one of the leads here, which is the really interesting finding that after all of your
*  intensive study, you were brave enough to face off head to head with an automated system for
*  prompt optimization specifically. I actually don't know how this is normally verbalized,
*  but I think it's DSPi. Maybe it's verbalized another way. This is sort of a weird project that
*  a lot of people rave about that I've kind of studied a little bit and can't say I totally
*  get it or it like doesn't feel super intuitive to me, but it's sort of an optimization framework
*  that can kind of optimize everything in your system, including the prompt. And I guess at
*  least under certain controlled conditions, it beat you on a head to head. So tell me that story.
*  Give me a little more intuition for this thing and tell me what that means for the future of
*  prompt engineering as a profession. Sure. Let me start with the naming. I call it
*  DSPi and I think a lot of the people in my lab do as well, but DSPi or I guess DSPi
*  also seem valid. Actually, Omar came and talked at UMD and I was there for his talk,
*  but I don't remember exactly how he pronounced it, unfortunately. But onto the prompting stuff. Yeah,
*  so I spent like 20 hours developing this prompt for a binary classification task and I was
*  pretty happy with it. And then my advisor used DSPi and put in like the training data that I used
*  as exemplars and DSPi was able to create a prompt with the exact same data that I had that blew me
*  out of the water on the test set. So as far as does automated prompt engineering work,
*  I can now say yes, it does. And I think you do need like ground truth examples. I don't think it
*  can optimize just any prompt because it needs some kind of signal to optimize towards. But
*  I was super, super impressed with it. I definitely didn't think I could be defeated by an
*  automated prompt engineering system. And this thing can use proprietary models, right? It doesn't
*  like black box. It doesn't have to have access to the weights. That's correct. That is correct.
*  Yeah, I was pretty sure about that. How much data did you have and how much data did it also have?
*  Let's see, probably gave it like less than 20 exemplars to use and we had like maybe a couple
*  hundred. The data set itself was quite small. Interesting. One wonders if it could be used to
*  help solve the ARC challenge that's connecting a couple of threads. Cool. Well, down to the last
*  couple of minutes here, any thoughts on productizing all this? I mean, obviously you've got the Learn
*  Prompting. I can sort of imagine a lot of businesses would be interested in an extension
*  of Learn Prompting that is like, I mean, you have content, you have instruction, you have best
*  practices. But what about a prompt coach that like follows me around and applies this taxonomy to
*  what I'm doing in my day-to-day use of AI and coaches me on how to get better? I'm sure that's
*  something you've at least thought about. And then with the DSP or DSPy, whatever sort of results
*  suggest that you wouldn't even necessarily be leaving much on the table in terms of theoretical
*  performance to follow the advice of a system. Claude has done that, you know, Anthropic has done
*  that a little bit with Claude. Anything in the works there or would you leave that to others?
*  Right now we do have like a rag chatbot you can ask questions on about our docs. But as far as
*  putting in your prompt and getting advice on it, I could see it being useful. I think it is quite
*  a struggle because in different domains, people are just doing things that look completely different
*  and so I'm not sure if we would be able to prompt the model well to do consistently well across
*  domains. And then I also don't know if that's something people would be willing to pay for
*  like at all. But it is something we considered not a main product we're focusing on at the moment.
*  But if we saw interest, we would look more closely in that direction. Cool. Okay. Well,
*  it's a tour de force paper with a ton of, you know, for me, I would say now it is kind of the
*  starting point for any inquiry into available prompting techniques and a great place to
*  navigate your way toward deeper studies of all sorts of different things. Anything else that we
*  didn't cover that you think bears mention or highlight before we break? Yes, that would be
*  sort of my takeaways from, you know, running a team of this size. And let's just have my reflection
*  document. I did what I later learned is called a 360 review at the end of the project where I
*  wrote a reflection about my performance then had my team do that anonymously as well. And so
*  one of my conclusions was trust no one, not even yourself. And in practice, that means
*  something like you always have tests, you always have a CI pipeline. So anytime someone makes a
*  PR including me, all those tests and styling checks run against it. And so you make sure you
*  don't have any regressions. I found that to be super helpful in past projects and no different
*  on this one. So overall, I don't recommend doing a systematic literature review because this took me
*  twice as long. It ended up taking like nine months. But I did enjoy doing it. I am happy I
*  did it. And I really learned quite a lot doing so. Well, your hard work is to the community's
*  benefit and to our benefit today. So thank you for putting in all that blood, sweat and tears,
*  elbow grease and everything else. And organizational legwork as well. I think it is a great resource.
*  And I appreciate you coming on and returning to talk it through with us. I know you got to go. So
*  for now, Sanders Schulhoff, thank you again for being part of the Cognitive Revolution.
*  Thank you very much. It is both energizing and enlightening to hear why people listen
*  and learn what they value about the show. So please don't hesitate to reach out via email
*  at tcr at turpentine.co or you can DM me on the social media platform of your choice.

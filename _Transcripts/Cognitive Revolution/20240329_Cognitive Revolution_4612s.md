---
Date Generated: April 02, 2024
Transcription Model: whisper medium 20231117
Length: 4612s
Video Keywords: []
Video Views: 1177
Video Rating: None
---

# Mamba-Palooza: 90 Days of Mamba-Inspired Research with Jason Meaux: Part 1
**Cognitive Revolution "How AI Changes Everything":** [March 29, 2024](https://www.youtube.com/watch?v=Bg1LQ_jWliU)
*  Hello and welcome back to the cognitive revolution.
*  Today we're doing something a bit different,
*  which I am really excited about and hope will become a regular part of the show.
*  With everything in AI going exponential all at once,
*  I've been challenging myself to find new ways to keep
*  my AI worldview as accurate and up-to-date as possible,
*  and also to better help all of you to stay on top of the most important trends.
*  I really love doing the deep dive interviews with
*  researchers and entrepreneurs and absolutely will continue to do them.
*  But I increasingly feel that what is scarcest and therefore most valuable in
*  today's world is a zoomed out perspective that attempts to make
*  sense of whole research subfields and new emerging market sectors.
*  Today, that's exactly what we're going to try to do.
*  My co-pilot on this adventure is Jason Moe,
*  fellow AI scout and creator of the website statespace.info,
*  where he tracks Mamba and other statespace model research.
*  Together in this two-part episode,
*  we'll cover the first 30 Mamba-inspired research publications,
*  which Jason identified in just the first 90 days after the original Mamba paper.
*  If you haven't heard my original Mamba monologue episode from December,
*  I would recommend listening to that one first,
*  as that episode presents a high-level description of how transformers function,
*  what capabilities they are missing,
*  and why I believe the new selective statespace mechanism introduced in the Mamba paper
*  marks the beginning of what I'm calling the mixture of architectures era.
*  All that is really important background information
*  for the developments that we'll be discussing today.
*  Indeed, there have been many interesting developments.
*  The work we'll cover today explores the mechanistic function of the Mamba architecture,
*  the relative strengths and weaknesses of the selective statespace and attention mechanisms,
*  application of mixture of experts strategies to the Mamba architecture,
*  use of Mamba models for image segmentation and other computer vision tasks,
*  attempts to realize the promise of much longer context windows,
*  and lots more.
*  Along the way, we identify a number of important themes,
*  including the use of multiple internal states,
*  which was one of my big predictions from the December episode,
*  the need to cast all input data types as sequences,
*  and the use of multiple different scans over the input data to accomplish this,
*  the emerging dominance of hybrid architectures,
*  another big prediction from December,
*  and the many open questions around how best to handle
*  and what more we might be able to do with those all important hidden states.
*  This was a fun and intellectually invigorating conversation,
*  and I am truly grateful to Jason for all his hard work collecting the research
*  and joining me to break it down.
*  He even contributed to the editing process.
*  This was definitely going above and beyond,
*  but he has created a clearer, more information dense listening experience for you as a result.
*  As part of that, he even added key figures to the video version of this episode.
*  If you want to see those as you watch, and I do think it can be quite helpful at times,
*  please visit our YouTube channel.
*  We packed as many key topics as we could into these two hours and change,
*  but even so, we were not able to cover everything.
*  And on top of that, in just the short time since we recorded,
*  there have already been a bunch more papers,
*  including several that seem quite important.
*  With that in mind, we see this as just the start of an ongoing series,
*  and we look forward to bringing you another update on this dynamic area in the near future.
*  For now, as always, we invite your feedback on the show.
*  If you enjoyed this format of surveying a whole research literature, please do share it online.
*  If there are other fast moving AI research areas you'd like to see us cover in a similar way,
*  we welcome your suggestions.
*  And if you personally are in position to do a similar project,
*  I would love to work with you on it.
*  I've got projects in progress exploring the scale of data that will be required,
*  as well as the scale of data that's available to produce next generation models,
*  the application of generative AI to biology,
*  and the latest developments in brain computer interfaces.
*  And really, I would love to do so many more like this.
*  As always, you can contact us on our website, cognitiverevolution.ai,
*  or you can DM me on your favorite social network.
*  And with that, I hope you enjoyed this sweeping overview of the first 90 days of Mamba-related research
*  with AI Scout, Jason Moe.
*  Jason Moe, creator of statespace.info, welcome to the Cognitive Revolution.
*  Good to be here, Nathan.
*  So I'm excited for this.
*  We are kindred spirits, as both of us have become obsessed with the Mamba architecture,
*  really as a representative of the statespace moment and statespace revolution,
*  as Albert Gough calls it.
*  So what we're going to do today is take a super deep dive into all of the Mamba-related
*  and statespace literature that has been published over the last 90 days since the original paper.
*  And this is something I'm really glad to have a partner in crime on,
*  because it is an unbelievable amount of information.
*  It's very hard for one person just to keep up with this in a comprehensive way.
*  And so I was very excited to meet you online and see that you also are deep down this rabbit hole.
*  For starters, you want to just tell the audience a little bit about yourself
*  and how you got interested in this and how you've approached it?
*  Yeah, happy to.
*  So for the last decade, I've been working as an engineer in the world of atoms,
*  not in the world of bits, so primarily in large-scale energy infrastructure projects.
*  I followed some of DeepMind's early work, GPT-3, but as many I imagined,
*  serious pursuit of machine learning for me started in November 2022.
*  My interest in statespace models started with a problem-solving mindset.
*  I had been working on use cases that could really benefit from subquadratic models
*  and had previously followed S4 a little bit that's in the same lineage,
*  but soon realized that I didn't know enough.
*  So I started a website as a learning exercise, a way to assess this new class of models
*  to see if they were really capable of doing the things I was hoping that they would be able to do.
*  Yeah, cool.
*  So just to revisit briefly the original Mamba paper,
*  I was motivated to do that Forced March monologue from December
*  because in this role of AI scout, it's really important to keep an eye on the big questions, right?
*  It's really easy to get lost in the details of the latest paper, the latest product,
*  but one of the big questions I've been keeping in mind for a long time is,
*  what are the chances that somebody is going to invent something better than the transformer?
*  And it seemed like we were getting close a few times over the course of the last year.
*  And then with Mamba, it felt to me like, yeah, this is clicking,
*  and it probably is going to be not a successor to the transformer,
*  but really what we now have is two core mechanisms in the attention mechanism
*  and the selective state space mechanism that are both really powerful unto themselves.
*  Super headline from that original paper is the Mamba architecture was beating the transformer
*  at the core loss metric for text modeling, right?
*  Just super aggregate. What's the loss?
*  Look at the curves. It's a lower curve.
*  OK, that's interesting. Obviously, I haven't really seen anything else.
*  So simple and attention free beating transformers.
*  There was a theoretical reason to believe that this could be the real deal,
*  which is the idea of dynamic computation.
*  So essentially, the processing of each token differently, depending on context.
*  That is something that the transformers do.
*  The attention mechanism forks into the K, Q and V vectors, and then those get recombined.
*  State space models had not really previously done that.
*  They just had a sort of single set of weights that would process every input in the same way.
*  The selective mechanism now allowed for this additional path for the input to influence the nature of the computation.
*  And so it looks a little bit more attention like.
*  It seems to this was, of course, their motivation for doing it as well, right?
*  To be a little bit more attention like in that way of having dynamic computation as opposed to fixed weight computation.
*  And theoretically, that seemed like it was going to work.
*  Lost curve suggests it was going to work.
*  It also has super attractive properties in terms of how it scales.
*  Linear scaling as opposed to quadratic scaling.
*  That is to say, each time step, each token prediction is constant time.
*  And it's constant time because the state, unlike the attention matrix, does not grow over time.
*  You've got a fixed size state that persists from one token generation to the next and which gets transformed, but doesn't actually grow.
*  So that allows you to have a constant time inference step.
*  And that means your inference and also your training can be linear time, whereas obviously everybody knows that the transformer is quadratic.
*  So those are the main observations that I think probably attracted both of us to this.
*  The Mamba architecture demonstrates that you can get really far without attention.
*  But there was also enough evidence already even in December to suggest that probably different hybrid forms would be the way that things would ultimately be performance maximized today.
*  And it's about 90 days since the original Mamba paper.
*  We are going to look at all the updates to say, geez, how is this playing out just 90 days in?
*  I'm sure somebody could come up with something else that has kicked off a similar flourishing of downstream research,
*  certainly when maybe stable diffusion was released, people going nuts.
*  But this is definitely up there in terms of the flurry of activity.
*  And you've been keeping up with it better than just about anyone else.
*  Do you want to start off by giving us a little bit of an overview of what we're going to cover today?
*  We've got new modalities, we've got architectural variants, we've got just a ton of interesting findings.
*  But give us a preview of what's to come.
*  Yeah, happy to. Yeah.
*  So flurry of activity is the right description since the original Mamba paper came out.
*  Well over 30 new papers and significant projects, especially recently, it seems you can't go one or two days without seeing another Mamba repo or paper come out on archive.
*  By the numbers, 60 percent, well over half, are addressing vision and or image processing.
*  So that was a little bit of a surprise because that's not a use case that the original Mamba paper really addresses.
*  They focused on natural language, genomics, DNA sequencing and audio.
*  So very encouraging to see Mamba having an impact in that area of the 15 or so vision papers.
*  Nine were image segmentation papers.
*  So this is very applicable to the biomedical field.
*  But other things like image restoration, dehazing papers and all kinds of other general vision tasks, Mamba seems to be having an impact.
*  I think going out from there, natural language was about a quarter of the papers.
*  So we see some new architectural modifications, some interesting hybrid models.
*  That seems to be a enduring theme that we'll explore.
*  And then just many edge cases that people are applying Mamba to work with graph neural networks, work with audio, work with stock picking.
*  People are throwing a lot at the wall seeing what sticks.
*  And of those 30 papers, 80 percent of them modified the original Mamba architecture.
*  So they had some variation.
*  They didn't just apply the vanilla Mamba model to a new modality or a new domain.
*  So work so far has been somewhat innovative.
*  It's work thinking about how to use the selection mechanism, for example, in Mamba in the most effective way.
*  73 percent of the papers reported stated their results.
*  Those have, for full transparency, not been independently verified by you and me.
*  But these are the reported results.
*  And a lot of these papers do come with code repos.
*  You can go try things out for yourself.
*  Yeah, there are a lot of caveats that apply to all of this analysis.
*  One of the biggest ones is just that all this stuff has obviously been done very quickly.
*  The first papers started to appear as soon as 30 days after the original.
*  And even the ones that have just come out in the last couple of days are still just three months.
*  So that's not a long time to go do state of the art work.
*  And the papers themselves also, in some cases, feel relatively quickly drafted.
*  I definitely felt in reading through these that there were a lot of questions that I had that I could not necessarily answer.
*  And we'll ground everything we can as much as possible in the literature.
*  But there is definitely gaps.
*  And I would say reading this widely in this area does give me an appreciation for the peer review process and just putting people a little bit more through their paces of follow up questions and, hey, can you run this experiment?
*  And like, how good was your transformer baseline?
*  Really? That's always a question I have here.
*  When it's state of the art, that's one thing.
*  When it's like a head to head of a toy example, how much did you optimize that baseline?
*  At the same time, though, it's become somewhat well known that the Mamba paper itself got at least one confident reject in its peer review process.
*  I certainly don't think peer review has all the answers for us, but all this work will continue to definitely mature.
*  And I think we'll get more answers.
*  And hopefully some of the questions that we can't answer here will make their way back to the authors and maybe inspire either a little bit more experimentation or a little bit more clarity.
*  One of the things I think has definitely seemed true is that it's pretty easy to work with.
*  One of the very first things that came out was a blog post by a guy named Lucas Nell, who took Andre Karpathy's Nano GPT and basically made a Mamba version.
*  So I actually haven't spent a ton of time with Nano, but it's by Andre Karpathy, self recommending and really meant to be just the simplest, most bare bones, most easy to understand on ramp to building your own and training your own GPT at a small scale.
*  Something that you could even do in a collab notebook.
*  And so he works with that project.
*  The reason I think it's definitely worth highlighting is it is accessible.
*  He's got collab notebooks out there that you can also go hack on.
*  And a couple of comments that he made really stood out to me.
*  This is a quote from the blog post.
*  He says Mamba beats out transformers for this speech synthesis task, which is one of the experiments that he did.
*  Beyond that, it was also really memory efficient, which is awesome for playing around on collab notebooks where you continually run out of space on the GPUs with transformers.
*  I've certainly experienced that.
*  Still quoting. I think it's a game changer in terms of performance and quality.
*  And it's a super simple switch.
*  A Mamba block is literally a drop in replacement for a self-attention block.
*  Hey, we'll continue our interview in a moment after a word from our sponsors.
*  AI might be the most important new computer technology ever.
*  It's storming every industry and literally billions of dollars are being invested.
*  So buckle up.
*  The problem is that AI needs a lot of speed and processing power.
*  So how do you compete without costs spiraling out of control?
*  It's time to upgrade to the next generation of the cloud, Oracle Cloud Infrastructure, or OCI.
*  OCI is a single platform for your infrastructure, database, application development and AI needs.
*  OCI has four to eight times the bandwidth of other clouds, offers one consistent price instead of variable regional pricing.
*  And of course, nobody does data better than Oracle.
*  So now you can train your AI models at twice the speed and less than half the cost of other clouds.
*  If you want to do more and spend less like Uber, 8x8 and Databricks Mosaic,
*  take a free test drive of OCI at oracle.com slash cognitive.
*  That's oracle.com slash cognitive.
*  Oracle.com slash cognitive.
*  Omniki uses generative AI to enable you to launch hundreds of thousands of ad iterations that actually work,
*  customized across all platforms with a click of a button.
*  I believe in Omniki so much that I invested in it, and I recommend you use it to use Cograv to get a 10% discount.
*  So just the ease of making these kinds of switches and doing this sort of architectural experimentation is obviously a key to seeing so many papers over the last 90 days.
*  I do have some questions still around how easy it is at scale.
*  I think a lot of the papers that we will go through are working on pretty small data sets, pretty small models.
*  It's foundational work in a lot of cases.
*  OK, can this work in a new modality?
*  How does this compare to the state of the art for in the grand scheme of Internet scale data, very small data set?
*  And so there may be a degree to which it is more forgiving at small scale because things can still be fast,
*  without necessarily taking as much care to the hardware aware algorithm as the original paper puts in.
*  But I'd love to hear your comments because you've actually done some of this coding with the Mamba architecture as well.
*  And I've mostly stayed at the analytical level reading code, but not really writing code and not trading any of these from scratch myself.
*  Could you comment a little bit on your experience of working with the code itself?
*  Yeah, absolutely.
*  Yeah, Mamba's, I would say, overall been a very pleasant experience working with and certainly credit to the original creators of the architecture to think about that.
*  It does seem to have the feel of a kind of drop in replacement for transformers in certain parts.
*  I will say that it's always encouraging to see when a brand new model architecture like this can work with the existing libraries that are popular and that train models.
*  Some of those are things like the Hugging Face training library.
*  There's something called FSDP, which is this idea of I want to do a big training run.
*  I have a cluster, so I want to shard it.
*  So you have an option to do fully sharded training.
*  And the good news is Mamba seems to be compatible with that library.
*  And so I've successfully been able to train quite a few Mamba models for little experiments.
*  And it works great.
*  In your work so far, have you had to get down to the CUDA layer and tinker with the kernels at all, or has it been all at the Python orchestration layer?
*  Yeah, good question.
*  No, my investigations into the CUDA layer have been simply curiosity.
*  It's worked out of the box.
*  Have not touched that.
*  One of the original authors of Mamba is known for writing incredibly performant CUDA code, tree down.
*  And so I would never want to accidentally modify some of his work in a way that would cause some of my work to go sideways.
*  So I'm for the time being trusting the CUDA code that's been written.
*  It's been great.
*  Cool. So actually, one question I've been realizing in general through reading all this literature is that it's often not super obvious how the state is being handled.
*  Again, to remind everyone, the state is this substitute for the attention matrix in that it's an encoding of everything that has happened in context up until now.
*  But for the Mamba architecture, you don't have the ability to look back at all of the previous tokens and figure out interaction with each token.
*  That's how attention works.
*  In the Mamba situation, we've got the state gradually gets modified with new information.
*  In the earlier versions, this was a fully deterministic encoding that was designed from first principles.
*  Now we've got this selective mechanism.
*  So there's a learned aspect to the encoding as well.
*  This is super exciting because it has the promise of creating a long lived memory, essentially, that could and they demonstrate this in the original paper, particularly on DNA, more so than language, which is interesting.
*  They do demonstrate that it can handle super long sequences.
*  And for anybody who's been frustrated by the fundamentally episodic nature of Transformers, where you're always trying to figure out what context does it need?
*  How do I efficiently manage that context?
*  When does are getting longer?
*  That's still a challenge.
*  The promise here was that you could build up a state over time, potentially save that state, potentially fork that state and all sorts of interesting things open up when you have the state.
*  One thing that I did get wrong in my original episode was an analysis of how much SRAM there is on the A100, which was used to do this training.
*  I had said that it was a couple hundred kilobytes and I had inferred that the state, because the hardware where design here is about keeping that state in the SRAM,
*  which is the form of RAM that is closest to where the actual computation happens.
*  It's much smaller, but it's immediately functionally immediately accessible for the purposes of computation, whereas the high bandwidth memory is in a typical transformer structure where all the parameters sit.
*  But you have this need to load these things in and out of the high bandwidth memory into the SRAM to do the computation.
*  So here the state can stay in this SRAM.
*  And I had thought that because one of the ways that the specs are presented by Nvidia is that it's a couple hundred kilobytes.
*  Actually, a listener reached out to me and said that's actually per computation core.
*  So in aggregate over the entire A100, you're looking at more like a few tens of megabytes SRAM.
*  But this has me realizing a little bit that I don't have a super crisp understanding as to exactly what is the state and how is it handled.
*  The Mamba architecture has layers in the same way that a transformer has layers, right?
*  And the layer in the original Mamba architecture basically replaces attention with Mamba.
*  You still have an MLP block, but instead of attention and MLP, you now have selective state space MLP.
*  We'll get into some interpretability work that looks at how information is processed through the layers a little bit later.
*  But how is the state handled through those layers?
*  Should I understand that each selective state space mechanism has its own state?
*  And would that in practice mean that there's 20 layers?
*  Are there 20 states each one for its own selective state space mechanism?
*  Or is it like one state that is shared across all of those and is being modified for something as fundamental?
*  A question is that I feel like I should have command of that answer, but I don't feel like that's been stated very clearly in any of the papers.
*  So we haven't discussed this actually, so I don't know if you'll have the answer, but maybe it's clear from your deeper dive into the code.
*  Yeah, it's a very good question. So think about that to the best of my ability.
*  You covered really well the key differentiation with Mamba versus the previous state space models is that they are input dependent in time varying.
*  There are parameters. If we could pull up the original paper, there's an excellent diagram comparing the S4.
*  Mechanism to the S6, the main difference being in S6. There are a few of the dimensions that are chosen to be dependent on the input on dependent on L.
*  So those parameters are BC and Delta. But essentially what is happening at each step is that this mechanism is running and it's constantly getting feedback and update from the input sequence.
*  And it is updating the hidden state, so the hidden state does get updated through time, but you bring up a good question.
*  So in terms of what is the state, where is it located?
*  We can confidently say the state is located in the SRAM for the reasons you just mentioned.
*  That's part of the hardware aware algorithm. It needs to live there.
*  Yeah, some of the specifics for me personally are definitely still a little bit hazy.
*  Yeah, it's interesting. It may not even matter all that much. A lot of times these things that seem like they may be fundamental.
*  It turns out you can do it either way or maybe you do it one way with a skip connection and it ends up working very similarly.
*  So I'm not sure how critical that distinction even is, but it is an interesting reflection of for as much time as we've spent studying this.
*  There are some things that are just like very low level implementation details that the papers don't really make super clear and which make everybody still collectively in the process of figuring out.
*  So keep that that level of uncertainty in mind as we go through a lot of different angles on this.
*  So basically from here, I think we're going to organize this into a series of deep dives.
*  First one being Mamba learning theory. That is to say, what can we say at this point about the relative strengths and weaknesses of the architecture as compared to transformers?
*  When we see something that has this memory advantage in theory, then we wonder if it has some weaknesses.
*  Sure enough, as people are digging in, we are starting to see some differences, some things that the transformer doesn't do well, that Mamba can do much better and vice versa.
*  So the competing strengths and weaknesses and that naturally leads back to the hybrid forms outcome as well.
*  So that'll be one section. Another will be looking into a mixture of experts variations.
*  Obviously, a mixture of experts, a huge trend in general. And we've got a couple of papers already showing how that can be applied to Mamba.
*  Then, as you mentioned, vision, there's a ton of work in vision and some definite trends that I think give a good flavor for how this thing works and develop a little intuition for how Mamba systems see the world and how you have to massage your modality to fit the way that a Mamba system works.
*  We'll also have a bit of interpretability along the way, and we'll get also to some experiments on actually using the super long context.
*  The opportunity to do super long context is a huge part of what makes it exciting.
*  So how is that actually shaping up in practice? And then at the very end, we'll get into just a little bit more speculation and discussion before breaking.
*  So let's do the first bit on learning theory.
*  There have been a number of papers that have looked into what the Mamba architecture is capable of and what it's not.
*  First one is simply, is Mamba capable of in-context learning?
*  Spoiler, the short answer is yes. I think this one was pretty interesting because it did a layer by layer study.
*  We've seen many of these from Transformers, right?
*  In the original Mamba episode, I went on a long digression as to, first of all, it's just weird that the Transformer is like the same at every layer,
*  because we now have a pretty good sense that the layers are doing different things.
*  Again, this is a summary of a lot of different bits of research coming together.
*  But it's pretty clear that, especially with a sufficiently large Transformer that has some of these more emergent proto-world model type of capabilities,
*  it's pretty clear that there is a gradual working up from inputs to higher order concepts.
*  That tends to happen in the middle to late middle layers.
*  And then the last couple of layers seem to be dedicated to taking that higher order understanding and cashing it out to a particular prediction.
*  And sure enough, we basically see the same thing in this paper.
*  And by the way, the authorship of all these papers, incredibly global.
*  We are seeing folks from literally all over the world.
*  I would say it is probably a minority that are from the United States, definitely a minority from California, and folks from Europe, folks from Asia, a lot from China, Hong Kong, some from Korea.
*  It really has been remarkable to see how far this and fast this idea has traveled.
*  So this one in particular is from the Instituto Italiano di Tecnologia and also the University of Friedberg.
*  So I guess that would be Italy and Germany, a collaboration.
*  They're basically showing that, yes, the Mamba architecture can do in context learning at a high level.
*  Yes, it can. And that we are seeing a gradual refinement of its understanding as it goes through the layers.
*  This work reminded me a lot of logic lens, which is one where you look at the activations at every layer and say,
*  If I had to make a prediction from the activations right now, if I just jumped from whatever layer I'm in,
*  if I jumped from this to the decoder and immediately had to decode these activations, how well would I be doing?
*  This is pretty similar and basically finds that in the early layers that you're not doing very well,
*  pretty gradually, pretty consistently as you go through the layers, you are seeing an evolution of the activations such that your predictions get better and better all the way to the end.
*  There are a little bit of bends in some of these curves. I wouldn't say it's super, super linear or super consistent through the process, but definitely the trend is pretty clear there.
*  Any other any comments or reflections on in context learning?
*  Yeah, it was very interesting work. We had never seen a paper, Mamba paper up to that point that did that type of analysis.
*  So good to see.
*  The next one I would say is pretty similar. It's a fellow Mamba.
*  And again, this is directly inspired by earlier work on a transformer.
*  There was a project called a fellow GPT, which I believe is a Neil Nanda solo or possibly one that he supervised.
*  Why don't you take it? Give us the kind of original fellow GPT and now the new fellow Mamba.
*  Hey, we'll continue our interview in a moment after a word from our sponsors.
*  The Brave Search API brings affordable developer access to the Brave Search index, an independent index of the Web with over 20 billion Web pages.
*  So what makes the Brave Search index stand out? One, it's entirely independent and built from scratch.
*  That means no big tech biases or extortionate prices to it's built on real page visits from actual humans collected anonymously, of course, which filters out tons of junk data.
*  And three, the index is refreshed with tens of millions of pages daily, so it always has accurate up to date information.
*  The Brave Search API can be used to assemble a data set to train your AI models and help with retrieval augmentation at the time of inference, all while remaining affordable with developer first pricing.
*  Integrating the Brave Search API into your workflow translates to more ethical data sourcing and more human representative data sets.
*  Try the Brave Search API for free for up to 2000 queries per month at brave.com slash API.
*  Hey, everyone, Eric here, the founder of Turpentine, the network that produces the cognitive revolution.
*  This episode is brought to you by ODF, where top founders get their start.
*  ODF has helped over 1000 companies like Traba, Levels and Finch meet their co-founders and go on to raise over two billion dollars.
*  Apply to the next cohort of ODF and go from idea to conviction on what's next.
*  Startups change the world. They can also change your life. Is it your turn?
*  Learn more at beyondec.com slash revolution.
*  Yeah, sure. Basically, it was a repo that came out where we realized that these models had the capacity to play board games.
*  Anyone who's been following machine learning, of course, knows like the heavyweight work there has been a lot of deep mind work as well as other labs like OpenAI.
*  But games have been an interesting thing to apply to models to stress test them.
*  It's not just are they good at the game? So can they do they have some percent of win rate?
*  But do they understand the rules of the game? How often do they try to play illegal moves, for example?
*  So you can imagine how this would extend to other board games and sort of stress test.
*  Are these models really capable of reasoning and understanding?
*  Yeah, I would emphasize to in this particular project, these are pretty small models.
*  So the size of the Transformers under consideration are 11 million and 21 million parameters, and the Mamba versions are 9 million and 17 million.
*  And so these are not really intended to be state of the art in terms of their performance at the game.
*  They're not an Alpha Zero competitor.
*  But what they are really useful for is demonstrating the reasoning, as you said, but also allowing a window into how is it doing what it's doing.
*  And the thing that really was remarkable to me about the original of LGBT, which is basically almost exactly reproduced, except even a little bit better with the new Mamba, is that the model only sees a sequence of moves.
*  So in the fellow, it's an eight by eight board.
*  It's a little bit like go and that you have black stones and white stones and jockeying for position.
*  And when you surround somebody else's position, you can capture pieces.
*  So the sequence of moves is all that the model sees.
*  But to play effectively, it has to figure out somehow what is the actual state of the board.
*  I knew that pieces moved here and here, but the capturing dynamics and the changes that happen are not explicitly presented to it in the data that it is able to learn from.
*  So the question then, and this is a toy question, obviously relative to the super big philosophical questions on the state of the art frontier models today where people are like, does it have a world model?
*  What does that mean?
*  One way to try to get at that is to say, let's look at this much reduced world, right?
*  Where if we think that we might be getting some sort of world model in frontier models purely from next token prediction, can we create something that's like that in a small model where still all we're doing is just a sequence of tokens?
*  But we know that there is a higher order board state in this case that you really would presumably want and need to understand if you're going to play the game effectively.
*  So what is really amazing about this is that the model is found pretty clearly, in my view, to develop again purely from a linear sequence of moves, a state of the board that does take into account these capture dynamics.
*  And it essentially learns the rules of the game and a two dimensional representation based on just this pure sequence of moves.
*  So I think that's a pretty remarkable finding.
*  The way that's done in both the Othello GPT and the Othello Mamba is by just a simple linear probe.
*  So basically, you are taking the activations, training a single vector that you will then use to project that set of activations onto a two dimensional board state.
*  And so you are training this little thing, but you're training it to essentially interpret the information that's there.
*  The hypothesis is that the information might be there, but we can't read it, you know, native just with human intuition.
*  So instead, we'll train this little thing to help us read it, map it onto the board state, and then we can see how accurate is that representation of the board state.
*  So it's not perfect, but it was definite news and clearly of interest when the Othello GPT results came out and the board accuracy there was in the mid 50s, 55 and 57 percent board accuracy.
*  Whereas with the new Mamba version, we are seeing 67 and 71 percent board accuracy for the two different model sizes that were tested.
*  So significantly more accurate representation of the board state, possible room for artifacts in there.
*  Maybe there are idiosyncratic reasons.
*  We're not exactly measuring the internal state and the accuracy of the internal state.
*  What we are measuring is the ability for a linear probe to decode that successfully.
*  So presumably that's not perfect.
*  And the internal state would seem likely to me is like a bit better than this measured result.
*  Nevertheless, it's getting reasonably accurate.
*  Definitely a hard challenge, right?
*  If you just said to yourself, here's a linear sequence of moves and keeping in mind that there's this kind of capturing dynamic that goes on the board.
*  Could you look at a sequence of moves and immediately tell what the board state is?
*  Not easy, right? You really need to play it out and actually have a board and to implement the rules of capturing to see where the board state is.
*  At least that's what I would have to do.
*  And this thing doesn't really have the luxury of that, right?
*  It has to learn to do that all with its internal representations.
*  So to me, this is a really notable result because the original result is so notable and it works basically the exact same way.
*  And the accuracy is higher.
*  And you see the same pattern of, as you noted, the way they do this is they'll train one linear probe for every layer.
*  The idea being that the representation is different in the different layers.
*  And so you maybe could just have the same probe that would decode all the layers.
*  But for best performance, they train a dedicated probe for each layer.
*  These things are so quick to train. That's not really a problem.
*  And you see the exact same curve that we're accustomed to seeing where the performance or the let's say the accuracy of the board representation goes up and up as the information is processed through the layers.
*  You can see like a peak where that seems to be the highest order processing that the system is doing and then the class at the end as it cashes out to a final prediction.
*  This is actually one of my favorites. I love these little toy problems where you can, with relatively minimal compute,
*  figure out that this thing can actually solve a structured problem and develop a representation that it was not incentivized to do.
*  You could if you were a purely stochastic parrot, you wouldn't do this, right?
*  You would just purely associate certain prior moves with future moves and you wouldn't expect to have a board state that actually tracks all the capture changes and all the things that happen in a sequence of moves.
*  So I thought this one was super cool. There are some interesting limits.
*  I don't know if you have any intuition for this, but it definitely gets less accurate as you get into really long games.
*  The maximum number of moves you can have in this game is 64 because there's only 64 squares on the board.
*  And they do show that the accuracy drops over time as the game progresses.
*  And presumably that's just it's getting more complicated.
*  But that's simply something I would like to understand a little bit better, because this is not like long context.
*  It's just complicated. Maybe a bigger model would do it better.
*  More training would presumably help.
*  But at least in this version, with the resources turned into it, you do see accuracy declines as you go from the early moves.
*  It's very good. And then if you actually play all 64 moves, by the very end, it's not able to do it anymore.
*  So it is still definitely finite in its capabilities at this scale.
*  I wonder what's your gut say if we took a fellow GPT or Mamba for that matter, gave it more data to work with?
*  How do you think that would would play out?
*  Would it be able to handle the long, the full up to 64 move game?
*  My gut would say certainly sizing up the model parameter wise would be important.
*  You know, you always want to A-B test things to try to understand.
*  It would be interesting to freeze that result and simply size up the dimensionality of the state and then try to repeat the experiment.
*  I think this is like the new way of working with these state space models like Mamba.
*  What is the mechanism underlying this model that's creating this effect?
*  It's hard to say, and I'm very excited by the game work that's going to be coming.
*  So far, we've seen one chess model, an 11 million parameter chess model with Mamba that's only training on 18.8 million games.
*  It was done by on Twitter at Haley Storm Sea.
*  And although it does make illegal moves and it isn't perfect,
*  I did have a 37 percent win rate versus Stockfish level zero.
*  Just asking perplexity how strong Stockfish level zero is, and it says that it is an ELO rating of around 1200.
*  Generally considered to be novice in the chess community, it is a significant milestone for beginners who have improved from lower ratings.
*  So a milestone for early players is what we're able to compete effectively with just an 11 million parameter.
*  Mamba model that work actually is going to get scaled up and we should see a 50 million parameter Mamba model play chess relatively soon,
*  which is good because there's quite a bit of work by Adam Carvonen, who's trained transformers on chess.
*  So we should see some really good apples to apples comparisons in chess as well, just like the GPT work you just cited.
*  So that's coming. Yeah, interesting.
*  One other little note on this fellow Mamba 2 is, and of course, their plan is to scale this up and look at other games as well.
*  They report that it is more data efficient, meaning like it achieves the same performance with fewer examples, which is interesting.
*  But they did report that it took longer to train than a transformer of the same size.
*  And they are working on an A100, but they said it was 7.6 times longer to train than a transformer of the same size.
*  And they also note that messing a little bit with the batch size changed that significantly.
*  They moved the batch size from 256 to 64.
*  And then after that adjustment, it became still slower, but three times slower as opposed to the 7.6 times slower.
*  So this to me does suggest some interesting nuance to the speed.
*  I don't know what's going on there. It doesn't sound like they know really either at this point.
*  But there are some definite subtleties to making sure that you actually achieve the speed of the original Mamba.
*  You can't just report that everywhere for free, it would seem.
*  This one also a little bit highlights the sort of confusing nature of the state.
*  When I first saw this, I was like, oh, they're going to be looking at the state itself and trying to decode that.
*  But it doesn't seem like that's the case. Instead, it is still the activations that sit between the layers as opposed to the state itself.
*  So I would love to see as an extension of this some sort of way to try to decode what is in the state.
*  That to me is really interesting.
*  And in general, it does highlight another sort of philosophical mystery about this for me.
*  Maybe I'm just not bright enough.
*  But when I think about like, why does this work?
*  It is really interesting that the state of the state, if you will, is not directly subject to optimization pressure.
*  All this stuff is still trained on next token prediction or classification or whatever, as we'll get into different modalities.
*  But in this case, it's trained on making the next move in the series of fellow moves.
*  And there's not, as far as I'm aware, and I don't think we've seen any examples of this yet.
*  This is definitely something I would be looking out for.
*  There's not anything yet that says, what about the state?
*  And is there any sort of pressure that I want to put on that to perhaps represent certain information in a way that is going to be super usable?
*  It seems like that is happening just because just because the next token prediction requires the parameters to move in the right direction.
*  And so the state is taken care of.
*  But I really would expect an explicit optimization target for the state itself to be coming to a loss function near you in the not too distant future.
*  Did you see anything like that in this whole review where people are actually trying to optimize the state itself?
*  No, I haven't seen that. I think it's a very interesting line of research.
*  You alluded a little bit to the interoperability angle for something like this.
*  What does the state look like at each time step?
*  It's sort of designed to be a black box in some way.
*  The loss you're trying to minimize is ultimately a difference of just input output.
*  We've had attention for a long time.
*  There are all sorts of things you can do with attention.
*  Obviously, I imagine we are going to peel apart this mamba later and find out all kinds of things about it over time.
*  Yeah, I think the sort of toy setting of a game with a board state would be a pretty natural place to try to do this kind of research.
*  It's obviously a lot harder when you're thinking of the true actual world state.
*  How do I represent that?
*  It's not like we have a great way to say whether it's right or wrong or to project it onto anything super simple.
*  But starting with the state in some sense has to represent the state of the board because there's nowhere else for that information to hide.
*  And so it's got to be in there, presumably at least as rich as the activations.
*  And if the way I'm thinking about this is right, you could imagine a scenario where you optimize not only for making the next move,
*  but also for an accurate representation of the board state, perhaps accelerating training,
*  perhaps just helping you get to higher levels because right now it doesn't seem like there's as much emphasis on building up that accurate world model as there could be.
*  More to come on that.
*  OK, cool.
*  Next, still within the Mamba learning and interpretability section, the question is, can Mamba learn how to learn?
*  And the solution that they present is a hybrid model called the Mamba Former.
*  You can get a sense for what that might entail just from the name.
*  This comes out of a South Korean group, South Korea and United States.
*  Actually, one of the authors is a professor at the University of Michigan, not too far from me.
*  So that was cool to see across 12 time zones, including right in my own backyard.
*  But this really gets at the question of what can transformers do?
*  What can stay space models do?
*  What can Mamba do?
*  Is there anything that can do everything under consideration?
*  And what can we come up with that can get the best of all these different architectures?
*  So why don't you take us through some of the tasks that they looked at and what worked, what didn't, and how they ultimately resolved it?
*  Yeah, I'd love to.
*  This was a fascinating paper.
*  It came out a month ago, which in machine learning time feels like quite a while ago, actually.
*  Just before we talk about maybe the hybrid model, they came up with, I think it's interesting to just look at the evaluations they made on existing architecture.
*  So they evaluated a transformer, a Mamba model, S4, and something they call S4 Mamba,
*  which is essentially just Mamba as it is defined in the original paper, and then remove the selection mechanism,
*  remove the input and time-varying feature.
*  State space models and transformers both showed relative strengths on certain categories.
*  There are some places where the transformer succeeds and Mamba seems to falter, and the opposite is also true.
*  So one of those would be a task called sparse parity learning.
*  At a high level, you have this binary classification, and there's data that has a lot of different features.
*  Out of all these features, only a few are actually important for making the classification.
*  That's why it's called sparse.
*  So it's a challenging task because you have a lot of data being thrown at you.
*  Only certain features are ones that you should actually be paying attention to.
*  And so the model has to figure that out.
*  The transformer really struggles.
*  It was not able to do better than random guessing, no matter how much the authors trained it.
*  So they used an embedding dimension of 768 dimensions in a 24-layer model, which was much bigger than the other models they trained,
*  and it still could not do better than random guessing.
*  The state space models did much better.
*  Mamba in particular, along with the variant S4 Mamba, was able to basically solve the task with complete ease.
*  So it took a network of only two layers.
*  Another one where Mamba did well was the mini outlier linear in context learning task.
*  This one's similar to the last one, except it's trying to learn a simple linear regression.
*  So you take a linear equation and you have a mixture of what we could call clean inputs and outputs that are associated with a function like that.
*  And the trick is to actually mix those clean values with noise.
*  So the algorithm they chose introduced noise in the form of ones and zeros at a 90% probability.
*  So 90% of the time, the model is having to deal with what is essentially noise.
*  And this is an area where transformers actually were able to perform the task to a certain degree.
*  But Mamba at pretty much every step of compute is performing clearly better than the transformer.
*  And so the question for those two valuations, what can we glean?
*  What does it really mean for a Mamba to be performing better than really what has been the state of the art for a very long time?
*  It is the capacity to deal with irrelevant context.
*  And it's also surprising, though, because really the model that has the superior memory is going to be able to have a better chance of solving these problems.
*  Transformers are typically thought of with the intention to have a more precise, better, fuller memory.
*  But that doesn't really play out.
*  Mamba is clearly getting an advantage here.
*  I do want to also cover the tasks where Mamba really struggles.
*  So on the flip side, there are some tasks that transformers really excelled at.
*  Mamba struggled with something called multi-query associative recall.
*  So this is kind of an interesting eval.
*  It's not necessarily in context learning, but it is a very good stress test of the capabilities to recall
*  information. And the way that this evaluation is created is you have these series of key value pairs that get fed into a sequence.
*  The example they give, you have a letter and a number.
*  So A4, B3, C6.
*  And then you can introduce a query that now tests the model to remember what was the key value for A, B, C.
*  And you can push that as far as you want in terms of context length.
*  And Mamba, it's not completely a fail at this task.
*  In the paper, in fact, they do something interesting, which is they control for recurrent state size.
*  So they try to remove the advantage a transformer will have when it uses full attention.
*  And so they control for that at very small recurrent state sizes.
*  Mamba way outperforms transformers at being able to recall these key value pairs.
*  But up to a certain point, when attention is really able to fully maximize what it's capturing,
*  transformers easily solve this task.
*  There's no variation at all.
*  Whereas Mamba sort of plateaus close to 90 percent.
*  This is a task that's somewhat memory intensive.
*  It requires high precision.
*  You never know how the synthetic tasks actually translate to the real world.
*  I think that's important to remember both for the positives of what we just discussed with Mamba and state space models,
*  but also some of the negatives like this one.
*  But it is certainly telling us something about what's going on.
*  Yeah. So first of all, let me just make sure I can describe the tasks and then I'll offer my working theory.
*  So in the first one that you described, which is where the transformer fails, but the Mamba succeeds, the sparse parity,
*  this seems to be a lot of noise, a lot of irrelevant information.
*  You said in the one case it was 90 percent just random stuff and then the signal is all in the other 10 percent.
*  And then in contrast, the one where the Mamba architecture struggles and the transformer succeeds is when you have a
*  established pattern earlier in the context.
*  And now the challenge is basically to be able to recall from that earlier established pattern and reuse it now to complete the task.
*  I guess my theory is it seems like this is a reflection of the high level of parallelization of the transformer versus the
*  fundamentally sequential nature of the Mamba architecture.
*  When I think about this super noisy environment and I think, OK, I'm a transformer, this is the opposite of anthropomorphizing.
*  Now I'm modelizing myself.
*  I'm able to connect every token to every other token.
*  And when I do my back propagation, I'm essentially saying, OK, I want to obviously improve my prediction accuracy and I can go change
*  every parameter. And that includes the relationship between all of these tokens.
*  However, when there's so much noise, perhaps the problem that we're seeing is just that the noise dominates.
*  And because I'm considering everything at once and I'm saying, OK, I'm going to adjust everything that goes into the attention
*  matrix, but I'm not really zeroing in effectively right away on stuff that actually matters because I can, in a sense, maybe
*  overfit to the noise or just thrash around by continually overfitting to the noise.
*  My update is dominated by updating on things that were irrelevant.
*  That seems to be what's happening.
*  And it's that's certainly reflection of the fact that even a transformer of some significant size is not really able to do that
*  task basically at all.
*  Now, in contrast, if I'm thinking about this sequence where there's a pattern that's established earlier, that's obviously great for the
*  transformer because I can look back and say, oh, last time there was an A, a B followed, and now I've got another A, perhaps a B
*  follows. And so it finds those patterns and updates on taking advantage of those patterns quite efficiently and
*  Now, if I take it from the Mamba standpoint, I'm like, OK, in all this noisy stuff, because I'm considering one thing at a time and
*  updating one thing at a time, I can look and say, does tweaking the way in which I process this particular input help me much or
*  not? And because I'm confronted with noise, noise, noise, noise, signal, noise, noise, noise, signal, then I can perhaps say
*  tweaking this thing that is noise doesn't seem really to be helping that much.
*  Whereas now a more narrow focus consideration of should I process this token that happens to be signal?
*  Oh, hey, I'm actually getting a lot of value from this.
*  And relatively quickly, it seems to lock in on which ones are the signal and which ones are the noise, I'm guessing, because it's
*  handling this in a fundamentally sequential way.
*  And so there's an opportunity for it to update more meaningfully on the ones that actually give it signal versus the rest, which are
*  obviously just distracting. And then taking that to the sequence task where you need to be able to look back at the pattern.
*  Now, I could be in trouble, right? Because at the time that the sequence came in, it wasn't yet obvious that I should be paying
*  attention to the relationship between A and B as it happened.
*  And only later do I when I see another A do I wish that I had updated accordingly or had maybe allowed that that relationship of A, B
*  to make a bigger impact on the state, which is encoding all the information that I have.
*  But once that has passed, it's gone. Right. That was one of the big things that I talked about that a bit in the original Mamba
*  episode. There's got to be some weird stuff that's going to happen based on the fact that you get one chance to encode each token into the
*  state. And then if you didn't take your opportunity to update on that information, then later there's not really much you can do about it.
*  So that is my working theory. It's that it's failing to update as the tokens go by because it's not yet clear that it needs to.
*  And therefore, when the challenge actually comes, it's not prepared for it.
*  Whereas with the transformer, it can look back and see all this stuff and it can figure that out still, the runtime of the token that it
*  needs to predict, which depends on that earlier established relationship.
*  Yeah, I agree with your framing of that. You can imagine the advantage attention has in the sense that it almost can recover.
*  Now I can reference information that I, for lack of a better word, previously passed over.
*  Yeah, Mamba is not quite working that way. I think your framing of the problem leads elegantly into the solution the authors had for this paper,
*  which is acknowledging that there's something about attention that is advantageous in certain tasks and there's something about some of Mamba's
*  properties. And so they decided to try a hybrid architecture to in one model.
*  Can we take the advantages of both and combine them to go through these evaluations successfully?
*  And so that's what they did. They look at the transformer consists of a multi-head detention and a feed forward layer and then Mamba
*  consists of two Mamba layers. And so they define these two ideas of hybrids.
*  So the first one they defined was the idea of a standard hybrid, which would simply take the transformer and take out the feed forward layer
*  and put in a Mamba layer. And so they even test that a little bit. It's not quite as promising as the one they ultimately land on,
*  which is what they call Mamba former, which is the same thing. Keep multi-head attention, add the Mamba layer afterwards,
*  but take out the positional embedding and put a Mamba layer in that way.
*  The results they got were great. They were able to go through every one of those evaluation tasks and solve them.
*  So here's like a great indication of a theme that you and I have talked about, which is when in doubt, think about what can you do with hybrid modes?
*  How can you bring in these different mechanisms together in a single model? Now, they don't necessarily test.
*  Do we still have inference efficiency? They don't necessarily test.
*  Could we train a model like this as quickly and efficiently as the base architectures?
*  But it does at least show that the final results, the final outputs are promising.
*  Yeah, the nature of this hybrid too is pretty interesting. And again, just to reemphasize the headline, the key figure in the paper is here's a lineup of tasks.
*  These are pretty gnarly, synthetic tasks. It honestly takes a little bit of wrapping your head around just to figure out like, what is the task?
*  What are we even trying to get at here? Because they're all a little bizarro.
*  But you've got the ones where you got multiple columns and it's OK, here the transformer can do all these, but it can't do this, this, this very well.
*  Mamba notably can do all the ones the transformer can't do, but has its weaknesses.
*  And then sure enough, the Mamba former can do all of them. So it's best of both worlds sort of solution.
*  What was really odd to me is that they take out the feed forward portion entirely.
*  In the past, we've seen the original Mamba takes attention away and brings the selective state space in and still has a classic feed forward.
*  Here, the feed forward goes away and now you have both the attention and the state space.
*  And I would guess that's not going to be the final form.
*  It feels like if anything has stood the test of time in machine learning, it would be the ML layer.
*  And it seems like that is where facts are really typically stored in language models.
*  So I would not expect that you could scale this particular hybrid up to large scale language model tests.
*  Instead, I would guess that you would probably have some hybrid like this still with a MLP block,
*  because otherwise I just don't see how you would recover all the factual storage that seems to happen there.
*  This is toy problems. It's definitely really interesting for kind of a study of mechanism and definitely strengths and weaknesses.
*  My guess is this gets built on in a bigger model, bigger data set, more realistic task setting with the MLP layer coming back.
*  And it is another instance of it seems like everything is working when they replace the positional embeddings with another Mamba block.
*  To me, that was like flashbacks to the original attention paper where the original positional embeddings seem insane to me from the get go.
*  And it's like, wait, you do what? You have like some sine function thing about the position and that just you just superimpose that on everything.
*  And that kind of works and it's, yep, that's how it works.
*  And that we've seen actually don't know which positional embeddings they were trying,
*  but that was the original one was the sort of trigonometric function.
*  More kind of principled ones have been developed as well, like Alibi, which is a much more intuitive, I would say, positional embedding.
*  So I'm not sure which positional embedding they were using as the baseline here, but it is, again, striking when it's, oh, yeah, that's not quite working.
*  Why don't we just try throwing a Mamba layer in there and see what happens?
*  This wasn't really developed for that purpose.
*  At least to me, it's not at all obvious why this first sequential processing would replace the positional embeddings in a way that would make a ton of sense or why that would work.
*  But sure enough, it works. OK, great. We'll just leave that to future research.
*  It's like the number of things that are working that we don't really understand or we're pretty clearly just somebody being like,
*  oh, shit, why don't we just try stapling this there and see how that goes?
*  Maybe I don't give them enough credit. Maybe they have a more principled reason for doing this.
*  But the general phenomenon is definitely real, where people are just trying some stuff and sure enough, it works.
*  And then they're like, huh, I often say the whole industry slash field is the dog that caught the car in that.
*  Very few expected to be as far along as we are at this point in time.
*  And this feels like another one of these moments where it was like, yeah, we just try it and sure enough, it works and figure out why later.
*  And for now, it's pretty crazy. OK, summarizing all of this learning theory,
*  we see that the Mamba architecture can do in context learning.
*  We see that it does have a similar tendency to build up these representations of the world.
*  Or in the case of the Othello toy example, the board state that are critical for certainly the way a human would think about predicting the next move.
*  It's notable that much like in the transformer case, this was not something it was explicitly trained to do,
*  but something that happened in the course of just training and on these linear sequences.
*  We also see a similar pattern to transformers where it seems like there's this gradual elevation of concepts and gradually more accurate activations as you go through the layers.
*  And again, you see that collapse at the end where the higher order understanding that has been worked up and crunched on then collapses as it's making its final prediction.
*  And then we see these interesting one can do this, the other one can't.
*  And it seems like the strength of the transformer, which is its ability to go back and look at the entire sequence and realize later that,
*  oh, that pattern is the pattern that I need to be paying attention to now.
*  That's driven so much of its power, at least in a synthetic environment, we're able to show that if you put just a ton of noise in there and it has to look back at all this noise,
*  it can have a hard time finding the relevant data in a super noisy environment.
*  And then in contrast, the Mamba architecture can do that, according to my hypothesis, because it's able to evaluate an update for each each token one at a time.
*  But it struggles to identify and make use of some of these patterns, because as the tokens are rolling by, it may not be obvious.
*  And so later on, it just didn't necessarily encode that information.
*  And then we end up in the hybrid and we end up with something that doesn't look maybe as principled as one might wish for,
*  but which is working and which can do all of these little micro synthetic skills.
*  Anything else to add about Mamba learning theory before we move on to mixture of experts?
*  Great recap. Fascinating paper, fascinating results. Great job by the team that put that together.
*  OK, cool. Then let's move on to mixture of experts.
*  Honestly, this is a pretty short section, I think, in the grand scheme of things.
*  A mixture of experts probably should be its own full deep dive, because at this point, it's very clearly a major force driving frontier models.
*  It has been credibly leaked and I would say it's consensus accepted understanding of GPT-4 at this point that it is a mixture of experts architecture.
*  And certainly we've seen really good results from Mixtral as well.
*  And then most recently and arguably most notably Gemini 1.5 was also described as a mixture of experts architecture.
*  We've got multiple models at the frontier that are apparently built on the mixture of experts structure.
*  What that typically is, instead of the single MLP block, it is multiple MLP blocks.
*  That's the baseline mixture of experts architecture.
*  Instead of one MLP block, we'll have multiple, but we'll only activate a subset of those multiple MLP blocks.
*  Again, this could be its own deep dive, like how many MLP blocks?
*  How do you think about their relative sizes? How do you think about load balancing across them?
*  That's a really interesting situation. What kind of specialization do the different experts have?
*  How many experts should you be loading in at a given time?
*  I've seen some interesting work where it looks at is there a single expert that should always be enabled?
*  And then like other experts that get chosen at runtime versus are they all chosen dynamically?
*  It's its own can of worms.
*  But basically, I'd say what we've seen here with the application of that paradigm to Mamba is pretty basic,
*  pretty straightforward, but definitely just shows that it also works.
*  What they have done in two different papers here, mixture of experts Mamba, MOE Mamba, and then also black Mamba,
*  is basically you could think of it as if you started with the transformer mixture of experts,
*  you would think of it as basically the same thing that the original Mamba paper did,
*  which is take the attention mechanism out, put the Mamba selective state space mechanism in and find that,
*  yeah, OK, it still works.
*  Or if you wanted to think about it as starting with the Mamba, you could think, OK,
*  instead of my one MLP block that every token gets processed through, now I'll have multiple.
*  And again, you have all these kind of different tradeoffs.
*  So two papers on this, they both show pretty positive results.
*  I have one kind of point of speculation that I'm really interested in, but that I don't think we've seen yet.
*  But first, do you want to just give the headlines in terms of the results?
*  Yeah, headlines are interesting.
*  The initial paper thinks about Mamba as a starting point in making modifications to,
*  so taking out a Mamba layer and adding in a switch based MOE layer.
*  They scaled up to 32 experts.
*  They found that at that level that the MOE Mamba was able to achieve the same loss as the original Mamba
*  with 2.2 times less training steps.
*  So you get a sense of some training efficiency there.
*  And then Black Mamba also interesting results.
*  They scaled it up.
*  So whereas the first model used 416 million parameters, Black Mamba uses 2.8 billion parameters with eight experts.
*  They replaced the feedforward block with an MOE block and had a Mamba layer in there to replace attention.
*  Their most interesting evaluation was comparing inference, which the other paper didn't emphasize as much.
*  If you look at their chart, you can clearly see lines for generation latency are below transformer, transformer MOE and Mamba.
*  If you do the math, it looks like 82 tokens per second for 1.5 billion parameter and then 68 tokens per second for 2.8.
*  The hardware that was running that's not explicitly stated in the paper, but still pretty decent throughput,
*  assuming their setup wasn't too crazy.
*  Yeah, two very strong data points. Any thoughts on this?
*  I know you had talked about some background on the Black Mamba team.
*  Yeah, not too much is known about them. Almost all this work is academic.
*  There are a few papers that have an author from Together, AI, which is affiliated with the original authors of the Mamba paper.
*  It's Shri Dao that's at Together and it's Albert Gu that's at Cartesia.
*  So you do see a couple of Together folks sprinkled into the authors throughout this whole body of work, but mostly it's academic type collaborations.
*  This one stood out because it's from a company called Ziffra, Z-Y-P-H-R-A, stealth startup about which basically nothing is known.
*  They do have a website that as far as I can tell, this paper is really the only content that's on there.
*  And the company also appears to be very new.
*  Well, one of the co-founders recently left Conjecture just in the last few months.
*  So it's left Conjecture, started a company, immediately did this and published it really just a handful of weeks later.
*  That's definitely one to watch. Maybe two other comments I think are interesting.
*  One is the trade off with the mixture of experts architectures in general between more efficient training and inference.
*  But that does come at the cost of many more parameters total, right?
*  You've got a ton of parameters, but only a subset are being activated at any one time.
*  So your facts are more spread out, maybe more accurately accessible.
*  Perhaps that's why it works better.
*  You do have to set that up to actually productionalize this on an increasingly complicated hardware foundation.
*  You can't just have them on a hard disk somewhere.
*  They need to be in high bandwidth memory so that they can run quickly when they're called upon.
*  And to do that, you need to have arrays of GPU each with experts sitting on them waiting.
*  It definitely seems to suggest an advantage for your big tech incumbents with this kind of work,
*  because who has that sort of infrastructure sitting around the likes of Google, right?
*  They've been building out cloud infrastructure and figuring out how to route things and how to load balance since long before most of these other companies were even started.
*  And just the capital that they have and the sort of software layer that they have to manage that complexity definitely seems like a huge advantage.
*  Like, even if you had the weights for GPT-4, it would not be easy to set that up if you just think,
*  OK, there's 80 gigabytes maybe of high bandwidth memory on a single GPU.
*  If I have two trillion parameters, I'm going to need more than 10 GPUs just to set the thing up.
*  And then I have to get into the load balancing and all these other sort of interesting challenges.
*  So I think that is just a really interesting observation that open source is going to have a hard time catching up on that front.
*  You could maybe have open source models, but you're still going to need infrastructure providers to support that kind of work.
*  So that's one observation. And then another thing I think is I'm looking for is swapping out the state space portion of the architecture as opposed to the MLP layer.
*  It seems like probably should work, or at least there is some version of it that should probably work.
*  But I don't think we've seen anything like that so far in the broader mixture of experts, architecture, literature.
*  There is some work about swapping out the attention portion.
*  And again, it's like relatively not that deeply explored, it seems, as compared to the just swapping out the MLPs.
*  But there is some work there, and it does seem to be viable.
*  So this is one where I think, geez, the selective state space, if that's the sort of not replacement for in the big picture,
*  but that's the kind of analog to attention that figures out how are we going to compute on this particular input special way that's not uniform across all inputs,
*  then it would seem natural that would also perhaps be be swappable.
*  And maybe you would need some kind of again, this is very speculative here, but just thinking back to the last one where it was like,
*  what works best if we put a Mamba layer first and then we get into our hybrid?
*  I could also imagine something similar where it would be like process the sequence through an initial Mamba or some initial kind of workup
*  and then start swapping perhaps both the selective state space and or the MLP layers as well.
*  So I don't think we've seen the end of mixture of experts, certainly writ large.
*  It seems like it's going to be a huge force.
*  And I would definitely expect to see more work looking at more intricate sorts of swapping.
*  This right now is the switch transformer, your vanilla MOE standard.
*  It would be the baseline for many points of comparison in the MOE work from what I've seen and basically just showing that,
*  OK, you can bring this over here and it works and you can scale it up to a decent degree and it works.
*  And you get some of the same benefits in terms of takes less compute to get to a similar level of performance.
*  What comes next, though, I think is probably a lot more intricate and perhaps unexpected forms of figuring out what to swap out under what conditions,
*  what has to be pre-processed before that will work, etc, etc.
*  OK, that's the end of part one of Mamba Palooza.
*  In part two, which should be out by the time you're hearing this, we get into all of the image segmentation and other computer vision applications of Mamba,
*  as well as various projects that begin to realize the dream of super long context windows.
*  Plus, we get into the potential problem of rotting internal states and even explore a little bit of how these hybrid states face attention models are already beginning to be used in the context of biology.
*  There's a lot more to come. Can't wait to see you there.
*  It is both energizing and enlightening to hear why people listen and learn what they value about the show.
*  So please don't hesitate to reach out via email at tcr at turpentine dot co or you can DM me on the social media platform of your choice.
*  Omnike uses generative AI to enable you to launch hundreds of thousands of ad iterations that actually work, customized across all platforms with a click of a button.
*  I believe in Omnike so much that I invested in it and I recommend you use it to use Cogrev to get a 10 percent discount.
*  Turpentine is a network of podcasts, newsletters and more covering tech, business and culture, all from the perspective of industry insiders and experts.
*  We're the network behind the show you're listening to right now.
*  At Turpentine, we're building the first media outlet for tech people by tech people.
*  We have a slate of hit shows across a range of topics and industries from AI with Cognitive Revolution to Econ 102 with Noah Smith.
*  Our other shows drive the conversation in tech with the most interesting thinkers, founders and investors like Moment of Zen and my show Upstream.
*  We're looking for industry leading hosts and shows along with sponsors.
*  If you think that might be you or your company, email me at erik.turpentine.co.

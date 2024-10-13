---
Date Generated: October 13, 2024
Transcription Model: whisper medium 20231117
Length: 4403s
Video Keywords: []
Video Views: 4190
Video Rating: None
Video Description: Nathan hosts Professor Michael Levin and Staff Scientist Dr.Leo Pio Lopez from Tufts University in this episode of The Cognitive Revolution. They discuss their groundbreaking paper that combines biological datasets into a unified network model of disease using advanced embedding techniques. The conversation covers the technical details of their work, including a predicted link between GABA and melanoma, and explores broader topics in AI for biology. From multi-scale intelligence in biological systems to the future of human enhancement and digital life, this thought-provoking episode reminds us of the rapidly approaching future and the work needed to prepare for it.

Links to the papers discussed in the episode:

1) Universal Multilayer Network Embedding Reveals a Causal Link Between GABA Neurotransmitter and Cancer : https://osf.io/preprints/osf/d78wb
2) https://www.nature.com/articles/s42003-024-06037-4.pdf

Apply to join over 400 Founders and Execs in the Turpentine Network: https://www.turpentinenetwork.co/

SPONSORS:

Notion: Notion offers powerful workflow and automation templates, perfect for streamlining processes and laying the groundwork for AI-driven automation. With Notion AI, you can search across thousands of documents from various platforms, generating highly relevant analysis and content tailored just for you - try it for free at https://notion.com/cognitiverevolution

Omneky: Omneky is an omnichannel creative generation platform that lets you launch hundreds of thousands of ad iterations that actually work customized across all platforms, with a click of a button. Omneky combines generative AI and real-time advertising data. Mention "Cog Rev" for 10% off https://www.omneky.com/

Oracle: Oracle Cloud Infrastructure (OCI) is a single platform for your infrastructure, database, application development, and AI needs. OCI has four to eight times the bandwidth of other clouds; offers one consistent price, and nobody does data better than Oracle. If you want to do more and spend less, take a free test drive of OCI at https://oracle.com/cognitive

CHAPTERS:
(00:00:00) Teaser
(00:00:52) About the Show
(00:01:15) About the Episode
(00:04:45) Intro
(00:06:32) Multi-Layer Networks
(00:10:41) Network Embedding (Part 1)
(00:16:50) Sponsors: Notion
(00:18:30) Network Embedding (Part 2)
(00:18:30) GABA and Cancer
(00:24:08) AI for Biology
(00:29:59) Emergent Cognition (Part 1)
(00:33:57) Sponsors: Omneky | Oracle
(00:35:18) Emergent Cognition (Part 2)
(00:36:42) Data Limitations
(00:42:48) Modeling Wellness
(00:52:16) Multi-Scale Intelligence
(01:02:54) Digital Life
(01:07:11) Diverse Intelligence
(01:13:02) Outro

SOCIAL LINKS:
Website: https://www.cognitiverevolution.ai
Twitter (Podcast): https://x.com/cogrev_podcast
Twitter (Nathan): https://x.com/labenz
LinkedIn: https://www.linkedin.com/in/nathanlabenz/
Youtube: https://www.youtube.com/@CognitiveRevolutionPodcast
Apple: https://podcasts.apple.com/de/podcast/the-cognitive-revolution-ai-builders-researchers-and/id1669813431
Spotify: https://open.spotify.com/show/6yHyok3M3BjqzR0VB5MSyk
---

# Convergent Evolution The Co-Revolution of AI & Biology with Prof Michael Levin & Dr.Leo Pio Lopez
**Cognitive Revolution:** [October 12, 2024](https://www.youtube.com/watch?v=WRtWo-4wD0s)
*  We are interested in cancer, obviously, because of the biomedical importance of the disease,
*  but also because it teaches us about multicellularity and the failures of the collective intelligence of
*  cells. There's nothing genetically wrong with any of these cells. It's a purely physiological
*  change. What you've altered is the ability of the cells to work electrically with other cells.
*  So it's a very interesting example of how the dysregulation of cancer can be initiated without
*  any kind of genetic damage. We have so many biological data right now, but we don't have
*  maybe enough data on bioelectricity. But the main problem is maybe not about the data. Also,
*  it's about how we transform this data into information and knowledge. The power of AI is
*  to build a theory of mind of the system. We're not trying to make a black box that tells us how to
*  control it bottom up. We're trying to get the system to learn what is the kind of proto-cognitive
*  system that we're dealing with. Hello and welcome to the Cognitive Revolution, where we interview
*  visionary researchers, entrepreneurs, and builders working on the frontier of artificial
*  intelligence. Each week, we'll explore their revolutionary ideas and together we'll build
*  a picture of how AI technology will transform work, life, and society in the coming years.
*  I'm Nathan Labenz, joined by my co-host, Eric Torenberg. Hello and welcome back to the Cognitive
*  Revolution. Today, I'm pleased to share a conversation with Professor of Biology,
*  Michael Levin, and staff scientist, Dr. Leo Pio Lopez of Tufts University. Professor Levin's
*  previous appearance on the show has become our most popular guest episode ever, and for good
*  reason. His perspective on the ongoing convergence of biology, computer science, and philosophy are
*  fascinating. I invited Michael and Leo again now because they recently published a groundbreaking
*  paper that uses advanced embedding techniques to combine multiple biological data sets,
*  spanning the modalities of genes, drugs, and diseases into a single unified network model
*  of disease. I've been watching out for new machine learning approaches that can help pry
*  open the black box of biological interactions and causation, and I was impressed that this approach
*  has already generated meaningful new insights, including most notably a predicted link between
*  the neurotransmitter GABA and the cancer melanoma, which was subsequently validated by laboratory
*  experiment. In this episode, we first discussed the technical details of this work, including the
*  application of random walk with restart algorithms to the challenge of learning associations across
*  a multimodal, multi-layer network, as well as the potential for this approach to uncover additional
*  new therapeutic targets in the future. From there, we zoom out to consider broader topics in AI for
*  biology, including the current limitations in biological data collection and standardization,
*  the shortage of data related to the aspects of health and development that matter to us most,
*  and how emerging technologies like robot scientists and cloud labs might accelerate progress.
*  We also touch on the concept of multi-scale intelligence in biological systems, a recurring
*  theme in Professor Levin's work, including the remarkable observations that even simple gene
*  regulatory networks are capable of some forms of learning, that biological systems can often
*  survive and thrive despite major defects in their own hardware, and that humans have historically
*  domesticated and effectively trained wild animals despite knowing essentially nothing about their
*  biology. We briefly explore how such results and other biological models might inspire more robust
*  and adaptable AI architectures. Toward the end, we get into more philosophical territory as well,
*  including the future of human enhancement and the ethical implications of outsourcing aspects of
*  cognition to AI, the blurring of categories like living things and machines, often thought to be
*  mutually exclusive, and the potential for digital life, the challenge of envisioning a positive
*  future and specifically what humanity might look like as a mature species, the potential incoherence
*  of the concept of high-level AI alignment, considering the lack of alignment amongst humans,
*  the possibility of transcending individual identity, but also the extreme risks associated
*  with overly powerful collective intelligences, and finally, the existential importance of
*  developing a new science of where agency and goals come from and how we can effectively manage them.
*  Overall, it's a super thought-provoking episode which serves to remind us of how quickly the
*  future is coming at us and how much work we still need to do to be ready for it. As always, if you're
*  finding value in the show, we'd appreciate it if you'd take a moment to share it with friends,
*  and we always appreciate your reviews on Apple Podcasts or Spotify. We welcome your feedback
*  via our website, cognitiverevolution.ai, and you can always DM me on your favorite social network.
*  Now, I give you Professor Michael Levin and Dr. Leo Pio Lopez on the intersection of AI and biology
*  and the future of intelligence. Professor Michael Levin, Professor of Biology at Tufts University,
*  and Leo Pio Lopez, Staff Scientist at Tufts University. Welcome to the Cognitive Revolution.
*  Hey, Nathan. Good to see you again. It is great to have you back. So, so much continues to happen.
*  You guys have put out a lot of great work recently, and I'm excited to pick up where we left off last
*  time. If folks haven't heard our last episode, which by the way, is our most viewed episode ever
*  on YouTube of any guest that we've ever had, then definitely go back and check that out. I think a
*  lot of really interesting tie-ins were made in that conversation between all the fascinating work
*  that you're doing in biology and all of the stuff that people are just starting to wrap their arms
*  around and minds around on the AI side. So, I kind of want to do more of that, but I want to start
*  also with a paper that you guys put out on July 4th of this year, which I thought was really
*  interesting and to me seems like a major sign of things to come. It's called Universal Multi-layer
*  Network Embedding Reveals a Causal Link Between GABA Neurotransmitter and Cancer. And what stood
*  out to me a lot about this paper was that it is integrating multiple different data types and
*  multiple different scale of systems, genes, drugs, and diseases into one dataset, one network, one
*  sort of unified understanding and deriving new insights from that. The techniques are a little
*  bit unfamiliar, and I do think it's worth spending a little bit of time or maybe unfamiliar to people
*  that have only been in AI in the transformer era, but I think it is worth taking a little time to
*  kind of unpack how did you get the idea to do this? How did you have the sense that these datasets
*  could be combined and how did you actually go about it? Leo, if you want to start, that's great.
*  Yes. So, well, the idea came from also my previous postdoc because I worked on this kind of data
*  multi-layer networks because what we have in the omics era, if we have so many kind of data
*  and we don't know how to integrate them in the same representation, and networks are a very good
*  way to do it. So until now, we had big limitations on the kind of multi-layer network we could have,
*  only for example two multiplex networks. Multiplexing sort of just a different kind of network.
*  So I realized that I think it was in the middle of last year that I could finally have this kind
*  of universal multi-layer network because we had new extension of different techniques to do it.
*  So I did it and I explained what I did to Michael and it happened this way.
*  Let's go a little deeper into that. Can you break down the different datasets that you started with
*  and how you bridged these different modalities together?
*  So, yes. With this, now we can have as many kind of nodes that we want. So for medical applications
*  or to understand more biology, we use what we had. So genes, drugs, and diseases.
*  And in networks, you have interactions that are, this is how you link different nodes. For example,
*  with genes, we have so many things. We can have protein-protein interactions network.
*  We can have co-expression network and so many different things. So we used, well,
*  the most interesting one, the one that we thought were the case. For drugs, I used drug bank,
*  for example, which is a very big dataset. And then I had as many things I could find for diseases.
*  That is actually pretty difficult. We don't have so many interesting diseases network.
*  And the beauty of network embedding is that at the end, you have the possibility to apply
*  machine learning on this kind of data that could not be integrated in the same space, let's say,
*  before. So I think figure one in the paper, and we'll put a link to the paper in the show notes,
*  is very helpful for developing a little intuition for this. As I'll just kind of describe it,
*  there's the three different kinds of data, each in kind of their own space, so to speak.
*  You've got the drug data, which consists of clinical drug interactions and also drugs that
*  are often combined together, I guess. And then with the disease side, you have a sort of network of
*  shared symptoms across different diseases and then also comorbidity or the co-occurrence of
*  different diseases. And then in the gene side, it's a little bit less clear exactly what that is
*  saying. But there's a pathways and a PPI. Pathways, I guess, being like what interacts with
*  what sort of promotes or inhibits what. And then there's these links between these different
*  spaces as well. So this would be the indication of what drugs used to treat what disease and
*  what drugs used to treat what symptom and what genes seems to maybe cause or at least correlate
*  with different diseases. Was this a matter of all these data sets existed and you had to do a big
*  reconciliation of all the different data sets to make sure that you're actually making all these
*  linkages? Because all these different data sets, they don't connect automatically, right? I guess a
*  big part of the work was identifying which element corresponds to which element in other things.
*  Yeah, actually, I have to say first that this figure is a simplification of all the data that
*  we have. We have more in the paper. And well, all these databases already existing, my work here was
*  just to translate them in the same language in a sense, because we have so many, for example,
*  we have different kind of naming of the genes. So I just had to use the appropriate language.
*  And then it's easy to build this kind of network. I think here the important idea was to take the
*  most interesting databases that we have in the omics, all the omics databases that we can have
*  right now. So now let's talk about the actual learning technique. You've got all these data
*  sets, you've assembled them all, you've figured out how to identify the connections between them
*  and sort of unified them into one giant multimodal, multi-scale data set. And now the challenge is,
*  or the goal is to say, okay, if we can take all these links that exist, maybe we can learn those
*  and maybe we can use those to learn a model which can predict new linkages, right? So I think the
*  techniques of multi-exverse, which is new in this paper, and then the random walk with restart,
*  which is more established, but I do think not super familiar to a lot of folks who've been
*  following AI for only the last few years. I think those techniques are probably not super familiar.
*  So take us through those techniques. Just give us a little sense of the setup, the motivation for
*  the technique, how it ultimately works. Well, yes. The main motivation, as I said, was to
*  apply machine learning on networks. But with machine learning, we can't apply directly on
*  networks. We need vectors. So network embeddings has this ultimate aim to upon this big machine
*  learning toolbox for different kinds of analysis. But to do that, we need to translate the nodes in
*  the networks into vectors. So network embedding. Vector embeddings are the vectors. And to do that,
*  we need what we call a similarity measure in the network. Because the network embedding will be to
*  have embeddings in this vector space that can relate to the similarity measure between nodes
*  in the network. So to have this similarity measure, we use random walk reverse start.
*  Random walk reverse start is a method that is, I think, very well known in the field of network
*  theory, network analysis, but not really in machine learning. And the general idea is to use an
*  imaginary particle that from a seed node will explore this big network a lot of time until
*  convergence. And this will allow to retrieve a probability distribution of how much you will
*  go through this node during your random walk on the network. And this is the similarity measure
*  that we use. And that will allow us, after the learning phase, to minimize the distances between
*  the embeddings according to the similarity measure that we have in the network that we just computed.
*  Okay, cool. And then what's the next step with the multi-x-verse? Take us the next step through
*  the process. So when we have all this, we can do so many things in terms of analysis. So that was
*  the question. So after I did that, I explained to Michael, well, I have this system now. I can do a
*  lot of things. I could, for example, do link predictions between new drugs and diseases.
*  We can find new targets. We can understand more diseases. So many different questions can be asked
*  on this kind of system. And we did clustering, we did prediction, and we found this link between
*  GABA and cancer. But if I have to talk about a new, let's say, next step after this method,
*  I think it will be to link it to some sort of LLMs or transformers because they use also embeddings.
*  And we can use these embeddings that I have with this system as an input now for new kind of
*  applications. So just to make sure I understand correctly, the process starts with this random
*  walk with restart. And that is essentially a way of figuring out through many different starting
*  points and many different starting with random traversals through the network, what should be
*  close to what. So you're essentially minimizing a sort of distance traveled through the network by
*  pushing the positions of the embeddings that are often traversed. When two nodes are connected,
*  they're traversed often and so they need to become closer. Is that kind of the intuition for how the
*  embeddings get developed through that process? Yes, it's like you have this similarity measure
*  between nodes. So between all the nodes in the network, we have a similarity measure.
*  At the beginning of the optimization process, the learning process, we are going to initialize,
*  recopying randomly the vectors. So the distances between the vectors at the beginning won't
*  reflect the similarity measure. And this is what we will minimize during the optimization process.
*  Gotcha. And then you hold out, if I remember correctly, the network is trained on like 70%
*  of the data and then the learned network is then used to make predictions, which you validate on
*  the other 30% of the data. Yes, this is just to validate that the quality of our embeddings.
*  We want to be sure that, well, we did something that is really coherent. So this is the validation
*  phase. So then you do that. You just keep the 30% of the network to be sure that everything is good.
*  And then after having validated, then you can say, okay, now let's go take a look at the
*  predictions for some new links. When you're doing these new link predictions, are you just
*  making like a brute force process through possible links and just scoring them all and just then
*  looking at ones that have a high score? Or is there any sort of heuristic for the search
*  that guides the process toward particular links to look at?
*  No, no, I will feed the machine learning method with all the links that we know.
*  And then I will test on new links that we don't know. And I will see if I have a high probability
*  of new links. Yes. And so you can do that between cancer and new drugs, for example.
*  There are different ways to do that. There is also, well, the clustering is a bit different,
*  but the clustering has some, most of the people use it for visualization. But in the case of
*  network biology, we also like to do that to understand the notion of biological modules.
*  So biological functional modules that very, very have a biological function.
*  And sometimes when you look at cluster also, you can find a new drug or a new target associated to
*  a disease. So some diseases, this is how you can do that. Cool. Hey, we'll continue our interview
*  in a moment after a word from our sponsors. As a cognitive revolution listener, you're obviously
*  interested in cutting edge AI technology. And with that in mind, I'm proud to say that this
*  episode is brought to you in part by notion notion has been a clear leader in high value
*  applications of generative AI since the wave began. Earlier this year, we had notion AI engineer,
*  Linus Lee on the podcast, the quality of his insights showcase the caliber of talent that notion
*  employs. And that inside look at how notion builds with AI is still extremely valuable.
*  Given my personal focus on AI automation recently, I specifically wanted to highlight notions
*  library of workflow and automation templates. If you're looking to streamline your processes
*  and lay the foundation for future AI driven automation, these templates are an excellent
*  starting point. And even if you're not ready for full automation, you'll benefit immediately from
*  notion AI notions latest all in one AI implementation that searches through thousands of documents,
*  regardless of whether they live in notion or on some other platform like slack or Google Docs,
*  to deeply understand the context of your work and generate highly relevant analysis and content
*  just for you. Notion is used by more than half of fortune 500 companies, helping teams reduce
*  emails, meetings and time spent searching for information. Want to try it, head to notion.com
*  slash cognitive revolution. You can start for free and using our link supports the show. So join me
*  in giving notion AI a shot today at notion.com slash cognitive revolution.
*  So do you want to talk for a minute about the specific finding that made the headline, the title
*  of the paper, and kind of what makes that notable, maybe give us a little sense to have like, okay,
*  so the network spits out that, hey, there appears to be a high chance of a link between these two
*  things for the non biologically informed, you know, there's a little bit of a question of like,
*  what is this GABA thing, you know, I wouldn't have too much to say about that. So I'd love to hear a
*  little bit of like, okay, you saw this, what did that mean to you at first, then what did you go
*  do to validate it? What did we ultimately learn from this? And then we'll zoom out and talk kind
*  of, you know, how this may be a preview of things to come. I can start with that. Maybe Michael,
*  then can I cannot. So my first problem was to develop the method. Technically, I wanted
*  everything to work and to be validated. And then I talked to Michael, I said, okay, I have this,
*  what do we do with it? Because we can have so many different questions about, not only about cancer,
*  but also rare diseases, ion channels. And I remember, so he started to talk about the links
*  between serotonin, I think, and cancer, if I remember correctly, and that we already have
*  published work on this. And then he told me, yes, we could look also to everything about GABA and
*  cancer. And that's how it started. Yeah, I mean, so to take a step back a little bit, we are
*  interested in cancer, obviously, because of the biomedical importance of the disease, but also
*  because it teaches us about multicellularity and the failures of the collective intelligence of
*  cells. You know, the reason that we have anything but cancer is the meaning why cells normally in
*  the body were operate together to form specific organs, specific anatomical structures, you know,
*  why do they work hard to do those things that individual cells and unicellular organisms don't
*  do? There is a set of communication policies among cells, which I call a kind of cognitive glue,
*  there are many different kinds. But what it enables is for all of these cells to join together into
*  networks. And these networks store very large pattern memories of what it is that they're
*  supposed to be doing. So all of the cells then are aligned in that, okay, we are building this
*  particular structure. And there's information in this network about what it is that we're building,
*  it's a liver, a kidney, a heart, whatever it is. And so the breakdown of those mechanisms
*  results in cancer, the cancer phenotype is that individual cells disconnect from that network,
*  and then they roll back to this kind of unicellular lifestyle, where the size of the goals that they
*  can pursue, instead of like big organ and tissue level goals, they become little tiny single cell
*  goals like metabolism, you know, eat as much as you can go wherever life is good, that kind of thing.
*  So we study cancer as a breakdown of this collective intelligence, almost like a dissociative
*  disorder of the morphogenetic intelligence. And that means that we have to really understand how
*  do the cells communicate, right? And how do they get aligned into these networks? And of course,
*  bioelectrics is a major part of this. But one of the things that is downstream of the electrical
*  signaling is neurotransmitter signaling, same as in the brain, this happens in the rest of your body,
*  too. So we study for years, we've studied the way that voltage changes cause the small molecule
*  neurotransmitter serotonin to move from cell to cell and have various effects. And it's kind of a
*  downstream currency of the bioelectrical information processing that occurs in the network.
*  And so if you mess with the serotonergic signaling, you can get certain kinds of cancer phenotypes and
*  so on. So what was interesting about this prediction is that GABA, GABA-A, which is one
*  receptor for a different neurotransmitter called GABA, GABA-A is a chloride channel. And a chloride
*  channel is a little protein that sits in the surface of cells and it regulates how much
*  chloride ion goes back and forth. And thus it also regulates the electrical state of the cell and the
*  resting potential of the cell memory. So that suggested that we could use GABA signaling to
*  perturb the electrical communication among cells by changing their potential. And we've had work
*  before from a number of people in the lab using chloride channels to manipulate these kinds of
*  properties. And it turns out that when you use mucimol, which is a drug that is an agonist of
*  these chloride channels, then something very interesting happens. You get basically a kind
*  of melanoma where all of the normal pigment cells in the body, they're called melanocytes, these
*  little black pigment cells, they basically go crazy. They transform, they overproliferate,
*  they dig into other tissues, they dig into the blood vessels, they become incredibly invasive,
*  they change shape. It's really weird. They almost start to look like neurons. They make these
*  very long, skinny projections and they just start moving around and invading into everything. And
*  it's basically like a metastatic melanoma phenotype. A couple of interesting things to note about that.
*  One is that there is no primary tumor. So the one way that people often think about cancer is that
*  there is a single cell that got a bunch of mutations that took it over the edge of transform,
*  and then it releases clonal progeny that have those same mutations and they kind of take over.
*  And so it has to be, you know, there's an origin in one location and then from there it spreads.
*  That's not how this works. There is no primary tumor. What happens is that pretty much every
*  melanocyte in the body converts. They all go at once and you have this phenotype. And then the
*  other thing, of course, in this case is that there is no genetic damage. There's nothing genetically
*  wrong with any of these cells. It's a purely physiological change. What you've altered is the
*  ability of the cells to work electrically with other cells. So it's a very interesting example of
*  how the dysregulation of cancer can be initiated without any kind of genetic damage. So no
*  carcinogens, no oncogenes, just this dysregulation of development of these developmental mechanisms.
*  And it can be triggered by this kind of GABA mechanism that was predicted by Leo's network.
*  Okay. So there's at least a couple of different directions that I want to go there to unpack that
*  a little further. Let's come back to the multiscale intelligence in just a minute, but just to stay on
*  this network and sort of the use of machine learning to understand these biological systems
*  for a little bit longer. As I've been kind of watching the space and I've been increasingly
*  fascinated with AI for science, generally AI for biology in particular,
*  you know, coming at it as somebody who took like two biology classes in undergrad, you know,
*  a few years ago now, all that information long since outdated, I'm afraid. It seems like the
*  grand challenge of biology, to take the most zoomed out lens as I have kind of come to understand it,
*  is that we just don't know how things work. And so it becomes very difficult if you don't know how
*  things work to identify what effective intervention is going to be. It seems like at this point,
*  we've made a lot of progress where if we do through often painstaking techniques, figure out
*  exactly where we want to intervene in the overall biological network, then we're getting pretty good
*  at designing proteins or whatever to go in there and hit that target. But we still have just like
*  a vast black box problem of what affects what, you know, what interrelates with what. Obviously,
*  all these things are kind of messy and sort of overlapping in all sorts of ways. And so I've
*  been noticing that there seems to be the beginning of a trend toward using machine learning systems
*  to model the black box. And I don't know that there's like a sharp distinction, but it seems
*  like some of the early systems like your early alpha folds, and maybe even still through to alpha
*  fold three, arguably are like highly engineered systems where there is a very kind of detailed
*  theory of what is going on that is then, you know, being sort of encoded into the network
*  structure and ultimately being modeled. And then there's some other things like I look at the EVO
*  model where it's trained purely on base pairs. And it seems to learn these higher order concepts
*  purely from the DNA sequences. And that seems to be a bit of a different thing where it's like
*  the higher order concepts seem to be more emergent, as opposed to like really engineered
*  into the structure of the network. Because, you know, this might call this like how sort of
*  opinionated is the inductive prior of the architecture of the network. It seems like
*  this work is like more on that latter side, right? If I understand correctly, it's like,
*  this is just sort of taking a ton of data that existed but was maybe in disparate places,
*  figuring out how to represent it in one network form. And then kind of learning on that in a way
*  that seems rather unopinionated, right? Like it doesn't seem like you've encoded too much into the
*  structure of the architecture. It's really just, we have all these links. Let's see what we can
*  learn from them. And that seems like a big deal in as much as now we seem to be entering into a sort
*  of bootstrap type dynamic, perhaps, where, you know, the knowledge we have today, we can encode
*  that, we can make new predictions from it. All of a sudden, if these new predictions start to be
*  validated at a reasonable rate, you can imagine we could really start to feed that back into the
*  network. And this starts to feel like a beginning of a way in to really open up the black box and
*  sort of solve the grand challenge. I realize I'm speaking as a rank amateur to a master's here.
*  So critique that story. Like, would you describe the black box challenge differently?
*  Would you say I'm missing some inductive prior in the way that these networks are structured?
*  And ultimately, like, does it seem to you that we are heading into this sort of
*  bootstrapping into more and more knowledge through this loop of machine learning validation and back
*  into the network? Yeah, maybe Leo, if you want to say something about your approach, and then I'll
*  talk about the big picture here. Yeah, well, our approach is more data driven. Yes. So it's like
*  we do a lot of big data mining of we try to aggregate all the mixed data that we have and
*  try to understand a bit what's happening. But in systems biology, you also have model based
*  approach. So we try to give explanations more than just predictions. I mean, both are absolutely
*  needed. But on the data, I think we will miss a lot. In addition, when we do this kind of approach,
*  even mine, if I so for example, we can find only what is already into the data. But for example,
*  there is no bioelectricity data in it that I think is super important. So there are also
*  limitations. I think the future of this kind of approach is to be more and more important,
*  mainly multimodal AI. But we have to think really deeply about the what kind of data we want to.
*  Yeah, I want to take a step back and kind of give a slightly different perspective on I think where
*  this is all going in the future. One of the things that we and others study is the collective
*  intelligence of the body, taking seriously the idea that what you get in biology as you go up
*  scales is not simply emergent complexity and unpredictability. It's very easy to get complexity
*  and unpredictability out of simple rules. But I think there's actually something much more
*  interesting going on, which is that you don't just get emergent complexity, you get emergent
*  cognition, meaning that at all levels is already starting from the molecular pathways. We have a
*  couple of papers on this. You start to get systems that have problem solving capacity. They have
*  certain kinds of learning behaviors, for example, pathways and gene regulatory networks by themselves,
*  nevermind the cell or the organelles or any of that stuff. Just the pathways alone have several
*  different kinds of learning capacity. They can do habituation, sensitization, associative conditioning,
*  meaning Pavlovian learning, and so on. So what you have from the very beginning is a kind of
*  intelligence problem solving baked into the different layers of the body, solving problems
*  in physiological space, transcriptional space, anatomical space, and so on. So not just complex
*  behavior, but actual goal-directed problem solving. So if that's the case, then something very
*  interesting happens. Let's imagine a graph. So on the x-axis is complexity and on the y-axis is how
*  hard is it to deal with it. So at first, what happens is the more complex something is, the
*  harder it is for you to deal with it. It's exactly the problem that you laid out. When things get
*  complicated, it's very hard to micromanage the situation because there will be unforeseen
*  consequences and so on. But then something interesting happens. There's a cliff that I think
*  you drop off of in the cliff is when the system becomes significantly intelligent, such that you
*  can communicate with it, you can use the tools for dealing with cognitive systems, the tools of
*  cybernetics, control theory, behavioral science, and so on, then things become much easier. And
*  the dumb example that I use for this is people have been training dogs and horses for thousands
*  of years, knowing zero neuroscience. Isn't that remarkable? Why is it that we can get these animals
*  to do all these amazing things without having to understand what are all the neurons that you would
*  have to tickle to get them to do a particular kind of action? You don't need to know any of that
*  because all of that is encapsulated by the system that offers to you this amazing interface. It
*  offers you this learning interface. You can train it by rewards and punishments and with more
*  complex animals, other ways and so on. So what this suggests to me is that the AI tools that we are
*  really going to build are not just systems for inferring better ways to micromanage a complicated
*  system. We will get that too, I guess. But the bigger power here is to use these kinds of AI
*  systems as translators, communications devices. I think what we're actually going to use AI for
*  is not better ways to tickle specific pathways because hitting specific pathways has massive
*  limitations. We're not dealing with passive matter here. We're dealing with an agential material
*  that has agendas and various homeodynamic loops. It's going to fight you on the various things that
*  you try to do to it. Some of them will be recognized as hacking attempts by parasites and other
*  biologicals that are trying to control the cell so they will resist. That's as you'll get side effects
*  and all kinds of loss of efficacy, drug habituation and things like that. The goal is to try to reset
*  the set point of the system in a way to get the buy-in of the cells that this health state is the
*  new set point and we're going to help you achieve that set point. We're not going to try to clamp
*  the various microstates and try to fight symptoms. We're going to try to get the whole system to do
*  what it does best, which is to adjust towards a complex outcome given simple signals. We don't
*  want to try to micromanage everything. We want to give very simple signals. So I think that the power
*  of AI is to build a theory of mind of the system. We're not trying to make a black box that tells us
*  how to control it bottom up. We're trying to get the system to learn what is the kind of
*  proto-cognitive system that we're dealing with. And it's a little bit like there are people who use
*  AI to communicate with whales and things like people are going to be using it to process radio
*  telescope data to look for extra-terrestrial life and things like this. The idea is there is a
*  communication event going on. You want to communicate with a fairly alien intelligence.
*  It's not alien because we're made of the same stuff, but it kind of is because we're only used
*  to communicating with one kind of creature, pretty much big brains and sort of like us and that kind
*  of thing. This is different. But the good news is that AI, exactly as you said, if we let go of the
*  priors a little bit, if we don't force it to think the way we think, I think that's the power of AI
*  is that precisely that we should not try to make it exactly neuromorphic or human-like or anything
*  like that. We should let it do what it does best, which is to find unbiased patterns and become a
*  translator tool so that we can communicate with these complex systems in whatever way they're
*  competent to receive. So that's how I see this challenge is we have to move beyond, you know,
*  we start out with these systems that look like they're discovering facts about molecules,
*  but I think ultimately what they're really going to do is discover facts about goals,
*  about competencies, about measurements, about memories, preferences, these kinds of things
*  that are present in tissues. That's really what we're trying to manipulate in biomedicine.
*  Hey, we'll continue our interview in a moment after a word from our sponsors.
*  Omniki uses generative AI to enable you to launch hundreds of thousands of ad iterations that
*  actually work customized across all platforms with a click of a button. I believe in Omniki so much
*  that I invested in it and I recommend you use it too. Use Cogrev to get a 10% discount.
*  AI might be the most important new computer technology ever. It's storming every industry
*  and literally billions of dollars are being invested. So buckle up. The problem is that AI
*  needs a lot of speed and processing power. So how do you compete without costs spiraling out of
*  control? It's time to upgrade to the next generation of the cloud, Oracle Cloud Infrastructure or OCI.
*  OCI is a single platform for your infrastructure, database, application development, and AI needs.
*  OCI has four to eight times the bandwidth of other clouds, offers one consistent price instead of
*  variable regional pricing, and of course, nobody does data better than Oracle. So now you can train
*  your AI models at twice the speed and less than half the cost of other clouds. If you want to do
*  more and spend less like Uber, 8x8, and Databricks Mosaic, take a free test drive of OCI at oracle.com.
*  That's oracle.com slash cognitive. Oracle.com slash cognitive.
*  So has this work gotten over the top of that hill and over to the other side of the cliff or are we
*  still... Because when I read this as a sort of naive person with it knows a little bit about
*  biology, I think, okay, here's this link. It's been discovered. This is amazing. We're going to
*  discover all these links. This is going to give us all these targets and we'll develop these drugs
*  to go hit these targets and then, to use your term, we'll micromanage our way out of problems
*  and back to health. You're interpreting this in a different way, but I'm not sure if that interpretation
*  is falling out of what the network is telling us or if that is all based on all the other
*  vast knowledge that you're bringing to understanding it. I guess it's the latter though.
*  Yeah. I mean, everything that I just said right now, you can't pull all of that out of this one
*  paper. This is my view of what the future is going to be. And I don't think we're anywhere near the
*  top of that cliff. I think we're just starting the climb upwards. And I think, in fact, this is of
*  airmanship, to be clear for everybody listening to this, that what I just laid out is not the
*  mainstream vision. This is a controversial kind of take that I think a lot of people wouldn't agree
*  with. Most people see the biological layers here as a kind of more or less mechanical machine and
*  what's not considered standard approach to start asking, what do your cells or nevermind cells,
*  what do your pathways think about health and disease and your prior history and all of that
*  kind of stuff? So yeah, the thing that I'm describing is a long range vision.
*  So what is the limiting factor? I mean, Leo mentioned a minute ago that there isn't any
*  bioelectrical data in this data set. I've been hearing more and more recently that AI for biology
*  is data limited. And I've sort of been like, that seems counterintuitive because I look at just the
*  scale of LAMA 3, for example, and it was trained on 15 trillion tokens, which is like, yes,
*  a lot of tokens. But I would think we have in aggregate kind of sitting around in various
*  systems, we've got way more biological data than that. So it's not just a matter of course of raw
*  data. It's the different modalities and the kinds. And maybe there are just missing modalities
*  entirely like the bioelectric data. Do you think we are, in fact, data limited? Or is it that we
*  don't have the right kinds of data? Or more generally, what is the current limiting factor
*  that would prevent us from scaling this thing up and going over to the other side of the complexity
*  cliff? Leo, you want to start? Yeah. The answer would be yes and no. I think we have so many
*  biological data right now, but we don't have maybe enough data on bioelectricity. But the main
*  problem is maybe not about the data. So it's about how we transform this data into information and
*  knowledge. So what is the theory behind it? And I think here, Michael just presented a new one
*  that is super interesting. So in Omisdata, we have so many. This is why we do this kind of integration
*  of all these databases in the same network representation. But also we have clear lack
*  on things that we thought are super important. But this is still very important information.
*  And in the kind of AIs that Michael just described, we could use, for example, the embeddings that we
*  have right now as an input and they will use it after how to communicate with cells. So yes and no,
*  I would say. Yeah. I think it's very much data limited because of the kind of data. So some years
*  ago, a former postdoc in the lab, Daniel Lobo, and I started this idea of bioinformatics of shape.
*  So one thing that you really want, I mean, let's think about the kind of data that we have, right?
*  What you basically have is micro level data. So we have tons of omics in terms of protein, gene,
*  RNA, DNA, all those kinds of things. Never mind the issue that we're lacking all the
*  physio omics. So the bioelectrical data is completely lacking. So that's a whole other
*  thing that we can talk about. But what we actually care about is not any of those things. What we
*  really care about is the anatomical and functional outcomes. So we want to know, okay, how many
*  fingers? Why this number? Why not that number? Why are there two bones in your arm? Despite all the
*  work on limb genetics, still nobody has any idea what determines the number of bones and all of that.
*  So one thing that we're missing, which would be incredibly important for the AI, is here's the way
*  we stimulated the system, the change we made, and here's the outcome, right? And we started as
*  basically we scoured and then hand coded all the data for planarian regeneration, crustacean
*  regeneration, insects, and amphibians. So that means we had to come up with an ontology. We had
*  to come up with a graphical way to describe what happened. Here's how your bones got rearranged.
*  Here's the length of the different parts, right? So the topology and the geometry of all the
*  outcomes. So you have to come up with the language for that. So we did that and be able to encode
*  that in the database. And so now in that database you have, and so from each study that we saw,
*  there's functional experiments that say this is what we did and this was the change of shape.
*  This is what we did. This is the change of shape. Now this is great and you can deploy AI on this
*  to say, okay, so given that functional relationship, what can we say about the control structure?
*  You gave it a stimulus and this is how it changed the shape. What's the language? What's the
*  morphogenetic code that leads from this to this? If we crack that, then birth defects through
*  generative medicine, aging, general disease, cancer, all of these things would be solved,
*  right? Fantastic. But now we worked really hard and a whole bunch of undergrads helped and we
*  populated this database. It took us about four years to build all these things. The amount of
*  data in there is in the hundreds. Hundreds. That's not even remotely close to what AI needs
*  nowadays. And so that's the problem, right? Is that not just getting the data out of the journals
*  and into this database, which is already hard. And I'm not sure. I mean, back then certainly AI
*  wasn't up to it. I'm not sure if it is now. And there is no standardization. In fact, the journals,
*  if you copy your methods section from one paper to another, they call it self-plagiarism. And these
*  publishing houses try to boost the amount of novel content they have so they won't even let
*  reuse the method section verbatim. You have to keep changing it. But that all works against this
*  idea that what we want is to standardize. We want these papers to be readable by AI. We want it to
*  be very clear on what you did and how this differs from this other thing you did and having it be in
*  different words because you're trying to supposedly not plagiarize yourself. What a weird concept.
*  All it is is confusing for any kind of standardized method. So that doesn't exist. But even worse than
*  the data standardization is the fact that getting the data is incredibly expensive.
*  It's hard. I mean, this is what we do as developmental and regenerative biologists
*  all day is we make perturbations to test some hypothesis and then we get some kind of outcome
*  and we measure the heck out of it. But that's really hard and expensive and time consuming.
*  I don't know how to get that functional data in a way that gives you the amount of material that
*  you need for current AI approaches. So hundreds of thousands minimally and then millions typically
*  is my understanding of what you need for these kinds of things until we really get the robot
*  scientist platforms off the ground. So this is something else that a number of labs are doing,
*  something that we are doing is to try to automate some of that process and to really enable this
*  kind of feedback loop where there's laboratory automation that does experiments and records
*  these outcomes. But really critically, not just we keep sequencing the RNA, the DNA. I mean,
*  that's great. That gives you information about the low level components of your material. But
*  to really get functional data on the things we care about the shape, the structure, the function,
*  the ability to problem solving, anatomical space and physiological space, all of those things.
*  That I think is going to be a really important part of really getting AI unleashed on all of these
*  things. So I wonder if we, I've had this kind of pet idea for a while that this may shed some light
*  on and I saw this picture to you and then you can tell me what's missing from it. I've had this sense
*  that when we look at the giant scale models, they clearly are developing some sort of proto
*  world model. That's still debated, but I think it's increasingly hard to argue that there's not some
*  sort of world model in there. It is a flawed world model. That doesn't mean it's not a world
*  model at all. Anyway, bracketing that debate, I feel like when I just look around at the world,
*  there's so much confusion even among people as to what makes us feel good one day to the next.
*  It's very striking to me when I just say, how will I feel tomorrow? And then how will I feel
*  next Thursday? I really have no idea how I'm going to feel next Thursday. It's kind of crazy
*  that it's not that far in the future and could be anything. It seems so inaccessible even from my
*  own individual subjective experience. And so people are constantly taking supplements and
*  doing fad diets and who knows what, all these kinds of different things, which largely seem to be
*  born of that confusion. And then I think, man, there's just all this data from the omics,
*  as you said, to stuff that we can increasingly collect through wearables, like to take a picture
*  of your food, but also monitor your heart rate on an ongoing basis and track your exercises and so
*  on and so forth. And so I have this sense that we're getting probably pretty close to where
*  we might be able to create a large scale model of human wellness or human wellbeing that could just
*  be like sequence data in the same way that the language models are in sequence data, predict one
*  token at a time. I think of the human wellness thing as predicting the next wellness check-in.
*  You've got all these different data points. You ate this for breakfast and you slept for this
*  long on your eight sleep mattress and your Strava run was this today and maybe you're on this
*  medication or not or whatever. And then what's the next wellness check-in? And you train the model to
*  just predict how well you are at the next time. Those could be objective maybe and subjective
*  measures. It seems to me like that could work. I mean, it'd be a massive coordination problem,
*  massive data collection problem, so on and so forth. I wonder if you think that could work
*  or if you think there are, one counterpoint to that might be like, well, you've got really low
*  level stuff and you've got really high level stuff, but you're missing these intermediate layers.
*  And this goes obviously to your multi-scale intelligence worldview in general. Maybe that
*  gap between what I can measure at the low level and the high level is just too big for a model to
*  bridge that. Or maybe these sort of middle scale things could sort of be learned as like emergent
*  properties or emergent like middle representations that arise because they're useful for predicting
*  those next wellness checks. Do you think that that paradigm has promise? And if yes, why aren't we
*  doing it? And if no, what do you think is missing in the middle there? Well, a couple of things.
*  First, just kind of a funny observation. I think that because, so there's a prediction paradox here,
*  which might actually be real in the sense that to the extent that you deliver to some people
*  an application that can predict how they're going to be feeling, that will immediately make them
*  depressed because the whole idea that they are determined to in a way that they don't know is
*  depressing to a lot of people. And then the question is, well, did your system predict that
*  they were going to be depressed or not, right? I mean, it's the old prediction paradox. But so
*  we have to think about the second order effects of people knowing that this is happening. But overall,
*  I absolutely think that something like that will have predictive power, no doubt. And I think it can
*  have uses, but I think it's going to have the same failure modes that we now see with language models
*  in the ways that they occasionally fail, which means that they put on a pretty good show and
*  they do a nice job for a lot of things. But the one problem is that we don't know what we're
*  actually optimizing for. So for example, if what you're optimizing for is feeling good,
*  I would think the model will very quickly hone in on the fact that you should be on a lot of heroin
*  and that'll take care of things in the short term. Right. So the question is, what is it that you're
*  asking this model to do? Is long-term health and success that it's got to make you kind of
*  miserable for a couple hours every day with high stress exercise because long-term that's going to
*  be good for you? Or is it going to try to say that, well, here's as many donuts as you want,
*  because I know you're going to feel good about that. So I don't think we have a clear specification
*  of what success looks like in these cases. If you live to be 90 and you're lean and mean,
*  and boy, you never had a donut, is that the life you wanted? I have no idea what the answers are
*  to these questions, but what the AI will be good at is optimizing whatever you want it to optimize.
*  But let's be really careful and humble about the fact that we're not actually sure what we want to
*  optimize here. And I think it's very easy to, you know, where they say whatever gets measured gets
*  managed. And I think that's absolutely true. If we set it a fitness function, it will absolutely
*  shape us to that. But do we know what that's supposed to be? Yeah, we definitely don't. I've
*  been really intrigued by the notion of like multi-part reward design as another interesting
*  area of machine learning recently, because it does seem like there's like a paper on this that's like
*  scalar reward is not enough. And the basic idea is like, there's no single metric that you can
*  really optimize for in probably any sufficiently powerful system, but certainly one that we would
*  focus on the problem of our own well-being. There's not like a single measure that we could use. So
*  at a minimum, we probably need like multi-timescale different. Yeah. And that's okay, right? You can
*  have, you know, vector or whatever quantities that you're trying to optimize. And Mark Solms talks a
*  lot about this in terms of the drives, basic biological drives, where you can't just boil it
*  down. You can't rank order them because they're orthogonal. They're different dimensions and they
*  all need to get met. The problem comes when they conflict, right? It's all the one good to try to
*  optimize multiple variables when they're more or less independent, but sometimes they conflict.
*  And in the real world, they're definitely going to conflict. And then the question is, what's the
*  optimum prioritization? Yeah. And I think there's a lot to still be done to kind of develop what it
*  is that we want to have happen here. And not to mention, this always seems to butt up against
*  issues of agency and autonomy and will, because for example, already you hear people like some of
*  these new drugs coming online that prevent obesity. And eventually you'll have something
*  that helps you build muscles and all that kind of stuff. Already you hear people saying, well,
*  that's not fair. That's cheating. You know, you should get it the old fashioned way. You should
*  be in the gym. Like, well, how many hours should you be in the gym? Is there some God given number
*  of times that's, you know, amount of time per day, that's the correct and anything more than that is
*  unnecessary and anything less than that is cheating. Well, what's the correct amount of time?
*  And so if you had a system that managed you towards a specific outcome, I'm sure you would
*  get people that are resentful of it because they're saying, well, now I don't need my willpower
*  anymore. I was really good. I was the one who avoided all the donuts on my own and now everybody's
*  managed it, but that's not, they've given up their humanity because they're not needing to control it
*  anymore. So we're going to run into all those kinds of issues, right? So how much help are we willing
*  to accept from these prosthetics? Because that's very quickly going to merge into other areas of
*  life. So once you have your, I don't know, glasses mounted AI assistant, that's seeing what you're
*  doing and kind of helping you to a helpful, whatever, somebody's going to make a plugin
*  that's a relationship consultant that will say, no, don't say that you idiot, say this other thing
*  and it'll be much better. And then every facet of your life is going to, you know, objectively,
*  lots of it will get improved, no doubt, right? No doubt, some stuff will get improved. But overall,
*  what do we think about those kinds of prosthetics, you know, that are taking over not just the boring
*  stuff like digestion and whatever, but some of the things that people think about as core aspects
*  of themselves, like willpower relationships, whatever. Yeah, it reminds me of that Google
*  commercial during the Olympics where the dad is using Gemini to help his daughter write a
*  letter to her hero. And it's like, this isn't maybe where we want to start. Nick Bostrom also
*  has some really interesting work on this recently. What does a solved world look like? And how do we
*  think about the value of people doing things for each other? If you could just have an AI do it or
*  whatever, but there might still be some meaning that we don't want to give up that comes from the
*  actual origin story of what has happened as opposed to purely that it happened. Yeah, I mean, I think
*  we really need to be careful because it's very popular and it's an easy tendency to say, look,
*  this is where we are now as humans and let's not give that away. But let's be clear, this is what
*  we have now is in no way some magical optimum. I had a friend who was a forest ranger and a very
*  kind of outdoorsy guy. And he was astounded to know that I don't know how to hunt down my own
*  deer and kill it and eat it. And he would ask me like, what would you do if there aren't any
*  supermarkets? I have no idea. And he would say, well, how are you a grown man and you can't go
*  out and like catch your own meat and whatever. So this idea of giving up what used to be basic core
*  competencies, right? In favor of division of labor and of outsourcing some of the things that we used
*  to have to do on our own, all the prosthetics that we use now, canes, glasses, a toothbrush,
*  education, workouts, all these things that we know how to do. We've already done that. We've already
*  outsourced an incredible amount of stuff. And so yes, potentially you could outsource things you
*  shouldn't and don't want to, but let's not pretend that we are in some pure state now and only
*  beginning to start to think about it. Let's flip things around now. I have been very fascinated by
*  this idea of multi-scale intelligence. And when I look at the current prevailing paradigm in machine
*  learning, much of it obviously is driven by scaling up relatively simple kind of single scale
*  architectures, right? Like the transformer is obviously just the same layer stacked time and
*  time again. And it doesn't have this sort of multi-scale complexity that we see in biology.
*  Do you have any intuitions for what people might ought to be looking at to try to bring in concepts
*  of multi-scale intelligence to machine learning? Like what would a transformer look like if it had
*  access to something lower level? I feel like there's a seed there in terms of what you said about
*  even just simple dynamical systems having learning capability, but I'm not quite able to crystallize
*  that. So maybe you can help. The multi-scale competency architectures, we are starting to see
*  it for example, with neural cellular automatas that have been developed very recently. And we
*  have also hyper, what they call it hyper NCA. So now we have several layers of this. And I think
*  we are starting to be really close to what you call truly biologically inspired AI architectures
*  here, because they reflect much more what is AI as collective AIs. As we have neural cellular
*  automata or just that we have neural networks inside each cell and cells are communicating
*  between each other in a grid, for example. And yeah, so just to say that I think it's really
*  beginning. Well, two things. So we're working on some of this in our lab and this is what I call
*  truly bio-inspired AI because neuromorphic architectures and all that, I actually don't
*  think that that's where the secret sauce is at all. I think there are some really fundamental
*  things about the way life is organized that have to be the basis of the kind of AI that we're
*  talking about here. And we can talk about a few of those things. I do want to point out that
*  some of those things I actually am not going to talk about anywhere. I started writing a paper
*  on this at one point about like the specific things that I think differentiate true morally
*  important agents from the kind of systems we have now and how you could achieve that. I actually
*  think we have a pretty reasonable guess now as to how you would do it, but I don't think we should
*  and I don't want to be responsible for it. Somebody else will figure it out, no doubt,
*  but I don't really think there's a way of escaping it. But I don't want it to be me.
*  So some of these things I'm not going to talk about, but one thing that I can talk about
*  is the issue of one specific difference is that biology is always dealing with an unreliable
*  medium. Fundamentally, everything in biology is full of noise and you can't really count on it.
*  So never mind the environment's going to change like if you're an evolutionary lineage, right?
*  Of course the environment's going to change, but your own parts are going to change. You're
*  going to mutate. There's going to be all kinds of things that are going to happen to you. So
*  what biology does, I think, is not over train on its priors on the past. And I think evolution makes
*  not fixed solutions to specific environments, which is what we're taught, you know, in terms
*  of selection and so on. But I think what it makes is problem solving agents at all scales,
*  specifically because from the very beginning, it's dealing with an unreliable computing medium.
*  And I think that's the basis of the intelligence ratchet that we see in life is that you start
*  right away from having to make the only thing that survives are systems that can reinterpret
*  whatever is going on now in whatever is the best way, not how it was meant to be, or some locked
*  in idea of how to interpret your genetic memories, your physiological memories, but a creative
*  dynamic reinterpretation, which leads to problem solving. And then that scales up. So I think if
*  we're really going to have AIs that are multi-scale biological kinds of things, I think we have two
*  pieces to this. One is the multi-scale architecture. So I do a talk sometimes called
*  white robots don't get cancer. Like it's not an issue that anybody's had before, but in a
*  proper bio-inspired system, you will absolutely have subsystems that decide to go on their own.
*  They disconnect from the rest of the network. Like right now you make an AI or a robot or
*  something and you hope the higher level is intelligent, but you know all the parts underneath
*  are kind of dumb. So it's a very sharp kind of discontinuity in biology. It's not like that.
*  Every layer has some competencies and each layer tries to bend or behavior shape or coerce or hack
*  the layer below it. And sometimes the layer above it to get it to do what it wants to do.
*  That's the kind of thing we would have to have in these architectures. And I think we would have to
*  give up what we work at very hard in computer science, which is isolating the layers so that
*  each layer can count on the bottom layer being correct. When you're writing high level code,
*  you never worry about that. Well, these variables sometimes degrade and the data kind of goes,
*  like yes, there's unreliable computing where we typically don't code that way. You try very hard
*  so that each level doesn't have to worry about the metal and then you don't have to worry about
*  your machine code. You assume that what you put in your variable means exactly the same thing that
*  it will be later on and it hasn't floated off and whatever. I think that that's what keeps these
*  architectures from going to the kinds of thing we expect them to see in biology. I actually think
*  it's remarkable. What we've learned in the last few years with the AI that we do have, I think,
*  is remarkable and showing us that if you're very clever, how much you can get with this kind of
*  fixed architecture. But I think it's absolutely going to plateau if we don't take it in this
*  other direction. You see some kind of previous of that already with dropout and certain
*  data augmentation type techniques where a bunch of different types of noise are added to training
*  data. Between those sort of just randomly deleting neurons or randomly deleting weights and
*  systematically but randomly messing with the data, that seems to be a step in that direction. Those
*  things do, I think they're used generally because they help with robustness. They help with
*  generalization. What's next there? Maybe this gets into the detailed stuff that you don't want
*  to talk about, but if it does, then I guess the next zoom out would be like, I think all of this
*  is very fraught. I think last time you spoke about being worried about creating trillions of descendants,
*  not being able to vouch for their well-being and maybe you shouldn't do that. I think the other
*  angle that I'm seeing more and more right now is that this sort of pure distinct intelligence
*  that comes out of the lab and is a lightning bolt into a generally somewhat equilibrium
*  finding ecosystem seems like a destabilizing force. I'm wanting to find ways to make it a
*  little more organic to start thinking about instead of how can we find the perfect recipe
*  for alignment of some super intelligence? Is there a way that this could be more integrated
*  holistically into the world so that it's not like an all or nothing, like the thing is aligned or
*  it's not aligned, but rather it's in a more sort of buffered type of dynamic with the rest of the
*  world? I also see some really interesting things. I just recorded an episode with a couple guys from
*  AE Studio where they're looking at neglected alignment techniques. They've recently put out
*  a paper, one on self-modeling and one on what they call self-other distinction minimization.
*  Both of these are biologically inspired. Self-modeling is, obviously there's theories
*  of consciousness that come from that or that are predicated on that. They basically just have a
*  very simple thing where they give the model two jobs instead of just having to do the task.
*  It has to do the task, but also predict an internal state from an earlier layer.
*  Fascinatingly, what they find in that paper is that the network gets simpler. There's two ways
*  that you can make the self-modeling succeed. One is you can get good at learning how to self-model.
*  The other is you can become easier to model. They do see a reduction in this complexity metric
*  when they add the task of self-modeling. The idea there is that maybe it'll be easier for other,
*  this sort of can be a pro-social mechanism. That's super interesting. If you wouldn't mind
*  actually dropping me a link to that, I'd love to see it. This gets into something that we
*  were mentioning earlier, which is that one of the reasons that animals offer this amazing interface
*  is because not only does it make it the learning interface where you don't have to know what all
*  the neurons are doing and so on, is not only is it because it makes it easier to relate to others
*  and have a theory of mind about others and to communicate, but also it makes it easier to
*  control itself. A biological system that wants to control itself and its parts, it also behooves
*  it to have parts that are modular and encapsulated and have competencies in a way that you don't have
*  to micromanage them. You can do some delegation and things like that. The trade-off you get there
*  though in biology is that if you are too understandable and too easy to control with
*  signals, then you're too hackable. There will be parasites and cheaters and exploiters and
*  competitors and whoever that are going to hack you. We see this all the time. There are,
*  I don't remember if I spoke about this last time, but these amazing structures, these galls that
*  are these red spiky, just incredible looking things that are formed out of leaf cells on an
*  oak tree because the WASP is this non-human bioengineer that can prompt the leaf cells to
*  do a completely different thing that they apparently know how to do. Who would have known if
*  we hadn't seen it? But it's completely taking them over because the cells themselves are so
*  competent at other things. So I think there's going to be some kind of drive, at least in nature,
*  to optimize this and not to be too understandable and too controllable and whatever. But in our
*  technology, maybe it doesn't have to be that way. Maybe we can put pressure on the kinds of things
*  that we develop to make sure that there are better ways for us to interact with them.
*  And then just the final thing to say about alignment is that I don't think there's any
*  hope of a single alignment because we're not aligned among ourselves. Not only are we not
*  aligned culturally, if you ask different people on the face of the planet what they see as an ideal
*  future, you're going to get a hundred or more different answers. So we're not aligned within
*  ourselves. We're not even aligned really within ourselves as a single human. With split brain
*  patients, you find out very quickly that there are actually all kinds of multiple opinions,
*  sometimes radically different opinions on important things. Do you like your spouse?
*  Do you believe in God? There are modules within one person that don't agree on the answers to
*  these things. But typically they somehow cobble together a fairly consistent, or maybe not in some
*  cases, outward functional persona that kind of hangs together as a coherent, consistent thing.
*  But it's a pretty thin covering, as we know, from all kinds of situations in life. So being aligned
*  is a whole other question that's not as simple as it sounds. So this, and another episode that I just
*  recorded, sort of pushes me toward this idea that it seems like we might kind of need, and I'm not
*  sure I believe this, but just to present the case, it seems like we might need to go to a sort of
*  computational or digital life and try to sort of merge the normal environment that we have
*  developed in with the digital in some way to try to create an overall dynamic that can hopefully
*  be in some balance or some stability. It seems like digital life is not super far off. The episode
*  that I just recorded with two guys from the Google and Paradigms of Intelligence team showed that in
*  a remarkably simple, and you've done some similar things with your sorting algorithms,
*  you have these little cells that perform remarkably sophisticated behaviors. They had a similar kind
*  of thing where just very minimal computing environment, random strings, random interactions
*  between strings. Before you know it, self-replicators are arising, and then you've got
*  all these dynamics, the complexity metric spikes, and then there's sort of takeover, and then certain
*  things go extinct, but then there's like parasitism and symbiosis, and all these sort of familiar
*  paradigms are emerging in. These are just 64-byte strings that are randomly interacting. There's
*  not even an optimization function. So it seems like that could happen very easily. Part of me
*  is very scared of digital life because I don't know what that would entail. It seems like
*  it could be invasive. It could be hard for us to deal with, but then I'm like, what is the
*  alternative? Is there any alternative to a sort of ecology of AI long-term? I don't know. You react
*  to that however you want, but I struggle to see something that doesn't have sort of ecological
*  qualities being long-term sustainable for us anyway. Yeah, I mean about the digital life,
*  I think one important thing to keep in mind is that, well, to me, making these things,
*  it's not a goal in and of itself. I mean, we make synthetic life forms, and then other people make
*  digital agents and so on. I think the reason we do it is to better understand the agents that are
*  all around us right now. So I think we have an incredible amount of mind blindness at the moment
*  because we were evolved with firmware for detecting intelligence of a very particular kind,
*  medium-sized objects moving at medium speeds in three-dimensional space. That's what we're okay
*  at kind of noticing. But I think that what all of these efforts in diverse intelligence and
*  artificial life and AI, what they're all helping us to do is they're serving as prosthetics. They're
*  helping us to recognize and get a little broader in our ability to recognize, communicate with,
*  and ethically relate to other kinds of minds that are all around us right now. And we're just not
*  good at recognizing them or figuring out how to relate to them. And so I think that's going to be
*  really important because they're already here in surprising places and they're crumbling. They were
*  never great, but at least in the olden days, they kind of did well enough, but they got to go. And
*  they have to be replaced with principled, empirically useful models of what it is that
*  we mean by the space of possible beings and by the different distinctions that we try to draw
*  between them. So only a few minutes left. Just being mindful of time. I guess you have a sense
*  for where that ultimately takes us. I mean, I'm very compelled by your idea that we shouldn't
*  create trillions of descendants that we can't vouch for, but I also feel like that's in tension
*  with the idea that there are multiple companies out there right now that seem to be trying to
*  create a sort of monolithic super intelligence, ultimately seems to be their goal. And then they
*  have the question of like, well, how do we make that safe for ourselves? And nobody has a good
*  answer. And so I feel like we have very tough choices on either side. I'm open-minded enough
*  to imagine that I could be pleased with long-term descendants that are not just like me. It's not
*  all about just cloning myself into the future, but I do feel like I want some version of our
*  substance, our values, whatever to go on. Or I would definitely feel like something is lost if
*  it's just a sort of mindless, super powerful optimizer, terraforming planets or whatever.
*  So what do we do with this? I mean, it seems like we're in a very tough spot.
*  Yeah. Well, there's a simple, easy question. Okay. A couple of things. First of all,
*  I think everybody should take the time to paint for themselves the picture of the future that they
*  want. Maybe there are some people that think that a thousand years from now, we're still walking
*  around with lower back pain and astigmatism and a limited lifespan and whatever kind of body you
*  happen to be born into and whatever your IQ limitations are. I mean, that seems outrageous
*  to me, but maybe some people want that. It seems to me that once we've given up the idea that this
*  particular form with all of its limitations, cognitive limitations, physical limitations,
*  and so on, if you give up the idea that that was planned out for you by a benevolent,
*  all-knowing intelligence that, you know, in some way set this as the optimum, and this is how it's
*  got to stay and don't mess it up. If once we give that up, and I think we have to give that up,
*  then you're free to imagine, well, what does a mature species look like? What are your rights
*  as a being born into this world? Do you get dumped into a random body with whatever the cosmic rays
*  did to its DNA and physiology during development? And that's how you have to live your life with
*  those limitations. Or as part of your rights, there's some kind of freedom of embodiment where
*  you can live in this world in whatever way you want. And more generally, this notion of,
*  you know, like, how can we not be replaced? I mean, each one of us is guaranteed to be replaced.
*  Our children are not going to be exactly like us. They're going to do things that blow many of our
*  values out of the water. We are all going to be replaced. There's no question about it. I mean,
*  we have been for millions of years. The question is, what do you want to be replaced by? That's
*  the only question. And, you know, you said mindless terraforming. Agreed. That doesn't sound
*  too exciting. But I think we should all formulate what should the universe be filled with?
*  Should it be filled with humanoid looking things with our DNA? That doesn't seem particularly
*  optimal to me. But, you know, magnificent agents with freedom and creativity and an exploratory
*  instinct and cooperative, compassionate values and whatever, like, great. And if they look nothing
*  like us, also great. I'm not particularly tied to this form in the slightest. I don't see why
*  anybody should be. So I think it's paint negative futures of things we don't want. That's easy. And
*  that's what everybody's doing. I want to see everyone specify, what do you want? What do you
*  think things should look like in the future for us? And more generally in the universe, what should
*  the universe be filled with? And if you can make that statement, then we're closer to being able
*  to work towards it. We haven't even got to the paper that you have on agential memories.
*  But maybe one way to kind of tie that in with this line of discussion is just reminded of the Derek
*  Parfit idea that identity is not what matters. We obviously, as individuals tend to be very
*  wrapped up in our identity and our individual experiences. I wonder if there is a way to start
*  to prompt you for a vision of what a good future might be like. Is there something where
*  we can sort of dissolve the boundaries of individual identity and maybe sort of share
*  more of this cognitive glue that is memory? That's an opportunity to give a little bit of a
*  tease of that whole notion. But then I wonder if you could zoom out from there into something that
*  you would personally find inspiring. Okay. In the last couple of minutes,
*  I'm not going to try to paint an entire picture of the future. But I do want to say that you have
*  to be really careful with the notion of gluing everybody together. And what I mean by that is
*  a lot of people who hear my story of cancer as a breakdown of gap-junctional communication,
*  of the physiological connection between cells. One of the things that allows them to cooperate
*  and be aligned is that there is a anonymization of memories where cells connected by gap junctions
*  share physiological traces of past events to the point where it becomes hard to have individual
*  memories. You have kind of a collective memory and that gives you more of a collective intelligence.
*  And then people say, oh, well, there you go. We should all sort of gap junction ourselves together
*  and then life will be great. Well, so I just want to point out that I think that's very dangerous.
*  I think that's been tried in human history a few times. And in modern history, it goes the same
*  way always. It's pretty routinely terrible. And part of that issue is that the different layers
*  have different goals in different spaces. And one example that I sometimes use is if you go rock
*  climbing and you meet a bunch of social goals, a bunch of personal development goals, you're happy,
*  whatever. All the skin cells you left on that rock face didn't get a choice about whether they were
*  going to have a good day or not. You're not worried about them in the slightest. And so that reminds
*  us that simply forming together into a collective intelligence has no guarantee that that intelligence
*  is going to have the welfare of the pieces high on its priority list. In fact, we don't know where
*  the goals of collective intelligence come from. We must develop. I think it's an existential task
*  for humanity and flourishing of life on the planet is for us to develop a mature science of figuring
*  out where do novel collective systems goals come from? How do we manage them? How do we predict
*  them and so on? So I guess the only thing I'll say right now is that I think essential for the future
*  is a development of the emerging field of diverse intelligence, of understanding where goals come
*  from and how we can predict them and how we can guide them towards a positive.
*  That might be a great note to end on. I know you want to get out a couple minutes early.
*  So much more to your work. Anything else that we didn't touch on or any other closing thoughts
*  before we break? Yeah, no, just that we can put a couple links in the show notes where people can
*  follow up. There's a ton of work from us and others on this, so we can put some links on.
*  Cool. Well, I hope we can do this again in the not too distant future because your rate of output
*  continues to be incredible and there's always something fascinating in every paper I find to
*  discover. So thanks for all the great work and Professor Michael Levin from Tufts University,
*  Leo Piel Lopez, Staff Scientist at Tufts University. Thank you both for being part of
*  the cognitive revolution. Thanks very much. Thanks for having us. And yeah, Leo's got some great
*  papers coming in the next few months, so stay tuned for that. We will keep our eyes on it.
*  Thank you. Awesome. Thanks. It is both energizing and enlightening to hear why people listen and
*  learn what they value about the show. So please don't hesitate to reach out via email at tcrat
*  turpentine.co or you can DM me on the social media platform of your choice.

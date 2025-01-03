---
Date Generated: October 31, 2024
Transcription Model: whisper medium 20231117
Length: 4323s
Video Keywords: ['daphne koller', 'biomedicine', 'drug discovery', 'deep learning', 'stanford', 'insitro', 'artificial intelligence', 'agi', 'ai', 'ai podcast', 'artificial intelligence podcast', 'lex fridman', 'lex podcast', 'lex mit', 'lex ai', 'lex jre', 'mit ai']
Video Views: 93015
Video Rating: None
Video Description: Daphne Koller is a professor of computer science at Stanford University, a co-founder of Coursera with Andrew Ng and Founder and CEO of insitro, a company at the intersection of machine learning and biomedicine.

Support this podcast by signing up with these sponsors:
- Cash App - use code "LexPodcast" and download:
- Cash App (App Store): https://apple.co/2sPrUHe
- Cash App (Google Play): https://bit.ly/2MlvP5w

EPISODE LINKS:
Daphne's Twitter: https://twitter.com/daphnekoller
Daphne's Website: https://ai.stanford.edu/users/koller/index.html
Insitro: http://insitro.com

PODCAST INFO:
Podcast website:
https://lexfridman.com/podcast
Apple Podcasts:
https://apple.co/2lwqZIr
Spotify:
https://spoti.fi/2nEwCF8
RSS:
https://lexfridman.com/feed/podcast/
Full episodes playlist:
https://www.youtube.com/playlist?list=PLrAXtmErZgOdP_8GztsuKi9nrraNbKKp4
Clips playlist:
https://www.youtube.com/playlist?list=PLrAXtmErZgOeciFP3CBCIEElOJeitOr41

OUTLINE:
0:00 - Introduction
2:22 - Will we one day cure all disease?
6:31 - Longevity
10:16 - Role of machine learning in treating diseases
13:05 - A personal journey to medicine
16:25 - Insitro and disease-in-a-dish models
33:25 - What diseases can be helped with disease-in-a-dish approaches?
36:43 - Coursera and education
49:04 - Advice to people interested in AI
50:52 - Beautiful idea in deep learning
55:10 - Uncertainty in AI
58:29 - AGI and AI safety
1:06:52 - Are most people good?
1:09:04 - Meaning of life

CONNECT:
- Subscribe to this YouTube channel
- Twitter: https://twitter.com/lexfridman
- LinkedIn: https://www.linkedin.com/in/lexfridman
- Facebook: https://www.facebook.com/LexFridmanPage
- Instagram: https://www.instagram.com/lexfridman
- Medium: https://medium.com/@lexfridman
- Support on Patreon: https://www.patreon.com/lexfridman
---

# Daphne Koller Biomedicine and Machine Learning  Lex Fridman Podcast #93
**Lex Fridman:** [May 05, 2020](https://www.youtube.com/watch?v=xlMTWfkQqbY)
*  The following is a conversation with Daphne Kohler, a professor of computer science at
*  Stanford University, a co-founder of Coursera with Andrew Eng, and founder and CEO of InSitro,
*  a company at the intersection of machine learning and biomedicine.
*  We're now in the exciting early days of using the data-driven methods of machine learning
*  to help discover and develop new drugs and treatments at scale. Daphne and InSitro are
*  leading the way on this, with breakthroughs that may ripple through all fields of medicine,
*  including one's most critical for helping with the current coronavirus pandemic.
*  This conversation was recorded before the COVID-19 outbreak. For everyone feeling the medical,
*  psychological, and financial burden of this crisis, I'm sending love your way.
*  Stay strong. We're in this together. We'll beat this thing.
*  This is the Artificial Intelligence Podcast. If you enjoy it, subscribe on YouTube,
*  review it with 5 stars on Apple Podcasts, support it on Patreon, or simply connect with me on
*  Twitter at Lex Friedman, spelled F-R-I-D-M-A-N. As usual, I'll do a few minutes of ads now and
*  never any ads in the middle that can break the flow of this conversation. I hope that works for
*  you and doesn't hurt the listening experience. This show is presented by Cash App, the number
*  one finance app in the app store. When you get it, use code LEXPODCAST. Cash App lets you send
*  money to friends, buy bitcoin, and invest in the stock market with as little as $1.
*  Since Cash App allows you to send and receive money digitally, peer-to-peer, and security in
*  all digital transactions is very important, let me mention the PCI data security standard that
*  Cash App is compliant with. I'm a big fan of standards for safety and security. PCI DSS is
*  a good example of that, where a bunch of competitors got together and agreed that there needs to be a
*  global standard around the security of transactions. Now we just need to do the same for autonomous
*  vehicles and AI systems in general. So again, if you get Cash App from the app store Google Play
*  and use the code LEXPODCAST, you get $10 and Cash App will also donate $10 to First,
*  an organization that is helping to advance robotics and STEM education for young people
*  around the world. And now here's my conversation with Daphne Koller.
*  So you co-founded Coursera and made a huge impact in the global education of AI,
*  and after five years, in August 2016, wrote a blog post saying that you're stepping away and wrote,
*  quote, it is time for me to turn to another critical challenge, the development of machine
*  learning and its applications to improving human health. So let me ask two far out philosophical
*  questions. One, do you think we'll one day find cures for all major diseases known today?
*  And two, do you think we will one day figure out a way to extend the human lifespan,
*  perhaps to the point of immortality? So one day is a very long time and I don't like to make
*  predictions of the type we will never be able to do X because I think that's a, you know, that's
*  smacks of hubris. It seems that never in the entire eternity of human existence will we be
*  able to solve a problem. That being said, curing disease is very hard because oftentimes by the
*  time you discover the disease, a lot of damage has already been done. And so to assume that we
*  would be able to cure disease at that stage assumes that we would come up with ways of
*  basically regenerating entire parts of the human body in a way that actually returns it to its
*  original state. And that's a very challenging problem. We have cured very few diseases. We've
*  been able to provide treatment for an increasingly large number, but the number of things that you
*  could actually define to be cures is actually not that large. So I think that there's a lot of work
*  that would need to happen before one could legitimately say that we have cured even a
*  reasonable number of far less all diseases. On the scale of zero to 100, where are we in understanding
*  the fundamental mechanisms of all of major diseases? What's your sense? So from the computer
*  science perspective that you've entered the world of health, how far along are we? I think it depends
*  on which disease. I mean, there are ones where I would say we're maybe not quite at 100 because
*  biology is really complicated and there's always new things that we uncover that people didn't even
*  realize existed. But I would say there's diseases where we might be in the 70s or 80s. And then
*  there's diseases in which I would say probably the majority where we're really close to zero.
*  Would Alzheimer's and schizophrenia and type 2 diabetes fall closer to zero or to the 80?
*  I think Alzheimer's is probably closer to zero than to 80. There are hypotheses, but I don't think
*  those hypotheses have as of yet been sufficiently validated that we believe them to be true. And
*  there's an increasing number of people who believe that the traditional hypotheses might not really
*  explain what's going on. I would also say that Alzheimer's and schizophrenia and even type 2
*  diabetes are not really one disease. They're almost certainly a heterogeneous collection of
*  mechanisms that manifest in clinically similar ways. So in the same way that we now understand
*  that breast cancer is really not one disease, it is a multitude of cellular mechanisms,
*  all of which ultimately translate to uncontrolled proliferation, but it's not one disease. The same
*  is almost undoubtedly true for those other diseases as well. And it's that understanding that needs to
*  precede any understanding of the specific mechanisms of any of those other diseases.
*  Now in schizophrenia, I would say we're almost certainly closer to zero than to anything else.
*  Type 2 diabetes is a bit of a mix. There are clear mechanisms that are implicated that I think have
*  been validated that have to do with insulin resistance and such, but there's almost certainly
*  there as well many mechanisms that we have not yet understood. You've also thought and
*  worked a little bit on the longevity side. Do you see the disease and longevity as overlapping
*  completely, partially or not at all as efforts? Those mechanisms are certainly overlapping.
*  There's a well-known phenomenon that says that for most diseases other than childhood diseases,
*  the risk for contracting that disease increases exponentially year on year,
*  every year from the time you're about 40. So obviously there is a connection between those
*  two things. That's not to say that they're identical. There's clearly aging that happens
*  that is not really associated with any specific disease. And there's also diseases and mechanisms
*  of disease that are not specifically related to aging. So I think overlap is where we're at.
*  Okay. It is a little unfortunate that we get older and it seems that there's some correlation with
*  the occurrence of diseases or the fact that we get older and both are quite sad.
*  I mean, there's processes that happen as cells age that I think are contributing to disease.
*  Some of those have to do with the DNA damage that accumulates as cells divide where the
*  repair mechanisms don't fully correct for those. There are accumulations of proteins that are
*  misfolded and potentially aggregate and those two contribute to disease and contribute to
*  inflammation. There's a multitude of mechanisms that have been uncovered that are sort of wear
*  and tear at the cellular level that contribute to disease processes. And I'm sure there's many
*  that we don't yet understand. On a small tangent, perhaps philosophical,
*  the fact that things get older and the fact that things die is a very powerful feature for the
*  growth of new things. It's a kind of learning mechanism. So it's both tragic and beautiful.
*  So in trying to fight disease and trying to fight aging,
*  do you think about the useful fact of our mortality?
*  If you were, you could be immortal. Would you choose to be immortal?
*  MS. Again, I think immortal is a very long time. And I don't know that that would necessarily be
*  something that I would want to aspire to. But I think all of us aspire to an increased health span,
*  I would say, which is an increased amount of time where you're healthy and active and feel as you
*  did when you were 20. We're nowhere close to that. People deteriorate physically and mentally
*  over time, and that is a very sad phenomenon. So I think a wonderful aspiration would be
*  if we could all live to the biblical 120, maybe, in perfect health.
*  In high quality of life.
*  High quality of life. I think that would be an amazing goal for us to achieve as a society. Now
*  is the right age 120 or 100 or 150? I think that's up for debate, but I think an increased
*  health span is a really worthy goal.
*  And anyway, in a grand time of the age of the universe, it's all pretty short.
*  So from the perspective, you've done obviously a lot of incredible work on machine learning.
*  So what role do you think data and machine learning play in this goal of trying to
*  understand diseases and trying to eradicate diseases?
*  Up until now, I don't think it's played very much of a significant role because largely
*  the data sets that one really needed to enable a powerful machine learning method,
*  those data sets haven't really existed. There's been dribs and drabs and some interesting
*  machine learning that has been applied, I would say machine learning slash data science.
*  But the last few years are starting to change that. So we now see an increase in some large data sets,
*  but equally importantly, an increase in technologies that are able to produce data at scale.
*  It's not typically the case that people have deliberately proactively used those tools
*  for the purpose of generating data for machine learning. To the extent that those
*  techniques have been used for data production, they've been used for data production to drive
*  scientific discovery. And the machine learning came as a sort of byproduct second stage of,
*  oh, now we have a data set, let's do machine learning on that rather than a more simplistic
*  data analysis method. But what we are doing in Cetro is actually flipping that around and saying,
*  here's this incredible repertoire of methods that bioengineers, cell biologists have come up with.
*  Let's see if we can put them together in brand new ways with the goal of creating data sets that
*  machine learning can really be applied on productively to create powerful predictive
*  models that can help us address fundamental problems in human health. So really focus,
*  to get, make data the primary focus and the primary goal and find, use the mechanisms of biology and
*  chemistry to create the kinds of data set that could allow machine learning to benefit the most.
*  I wouldn't put it in those terms because that says that data is the end goal. Data is the means.
*  So for us, the end goal is helping address challenges in human health.
*  And the method that we've elected to do that is to apply machine learning to build predictive
*  models. And machine learning, in my opinion, can only be really successfully applied,
*  especially the more powerful models, if you give it data that is of sufficient scale and
*  sufficient quality. So how do you create those data sets so as to drive the ability to generate
*  predictive models, which subsequently help improve human health? So before we dive into the details of
*  that, let me take a step back and ask, when and where was your interest in human health born?
*  Are there moments, events, perhaps, if I may ask, tragedies in your own life that catalyzes
*  passion, or was it the broader desire to help humankind? So I would say it's a bit of both.
*  On my interest in human health actually dates back to the early 2000s when a lot of my peers
*  in machine learning and I were using data sets that frankly were not very inspiring. Some of
*  us old timers still remember the quote unquote 20 newsgroups data set, where this was literally a
*  bunch of texts from 20 newsgroups, a concept that doesn't really even exist anymore. And the question
*  was, can you classify which newsgroup a particular bag of words came from? And it wasn't very
*  interesting. The data sets at the time on the biology side were much more interesting, both
*  from a technical and also from an aspirational perspective. They were still pretty small,
*  but they were better than 20 newsgroups. So I started out, I think, just by wanting to do
*  something that was more, I don't know, societally useful and technically interesting. And then over
*  time became more and more interested in the biology and the human health aspects for themselves,
*  and began to work even sometimes on papers that were just in biology without having a significant
*  machine learning component. I think my interest in drug discovery is partly due to an incident
*  when my father sadly passed away about 12 years ago. He had an autoimmune disease that
*  settled in his lungs. And the doctor's basic said, well, there's only one thing we can do,
*  which is give him prednisone. At some point, I remember the doctor even came and said,
*  hey, let's do a lung biopsy to figure out which autoimmune disease he has. And I said,
*  would that be helpful? Would that change treatments? No, there's only prednisone. That's
*  the only thing we can give him. And I have friends who are rheumatologists who said,
*  the FDA would never approve prednisone today because the ratio of side effects to benefit is
*  probably not large enough. Today, we're in a state where there's probably four or five,
*  maybe even more, well, it depends for which autoimmune disease, but there are multiple drugs
*  that can help people with autoimmune disease, many of which didn't exist 12 years ago.
*  And I think we're at a golden time in some ways in drug discovery, where there's the ability to
*  create drugs that are much more safe and much more effective than we've ever been able to do
*  before. And what's lacking is enough understanding of biology and mechanism to know where to aim that
*  engine. And I think that's where machine learning can help.
*  So in 2018, you started and now lead a company in Citro, which is, like you mentioned, perhaps the
*  focus is drug discovery and the utilization of machine learning for drug discovery.
*  So you mentioned that, quote, we're really interested in creating what you might call
*  a disease in a dish model, disease in a dish models, places where diseases are complex,
*  where we really haven't had a good model system, where typical animal models that have been used
*  for years, including testing on mice, just aren't very effective. So can you try to describe what is
*  an animal model and what is a disease in a dish model? Sure. So an animal model for disease is
*  where you create effectively, it's what it sounds like, it's oftentimes a mouse,
*  where we have introduced some external perturbation that creates the disease.
*  And then we cure that disease. And the hope is that by doing that, we will cure a similar disease
*  in the human. The problem is that oftentimes the way in which we generate the disease in the animal
*  has nothing to do with how that disease actually comes about in a human. It's what you might think
*  of as a copy of the phenotype, a copy of the clinical outcome, but the mechanisms are quite
*  different. And so curing the disease in the animal, which in most cases doesn't happen naturally,
*  mice don't get Alzheimer's, they don't get diabetes, they don't get atherosclerosis,
*  they don't get autism or schizophrenia. Those cures don't translate over to what happens in
*  the human. And that's where most drugs fail, just because the findings that we had in the mouse
*  don't translate to a human. The disease in the dish model is a fairly new approach. It's been enabled
*  by technologies that have not existed for more than five to 10 years. So for instance,
*  the ability for us to take a cell from any one of us, you or me, revert that say skin cell to
*  what's called stem cell status, which was called the pluripotent cell that can then be differentiated
*  into different types of cells. So from that pluripotent cell, one can create a lex neuron
*  or a lex cardiomyocyte or a lex hepatocyte that has your genetics, but that right cell type.
*  And so if there's a genetic burden of disease that would manifest in that particular cell type,
*  you might be able to see it by looking at those cells and saying, oh, that's what potentially sick
*  cells look like versus healthy cells, and then explore what kind of interventions might revert
*  the unhealthy looking cell to a healthy cell. Now, of course, curing cells is not the same
*  as curing people. And so there's still potentially a translatability gap, but at least for diseases
*  that are driven say by human genetics and where the human genetics is what drives the
*  cellular phenotype, there is some reason to hope that if we revert those cells in which the disease
*  begins and where the disease is driven by genetics and we can revert that cell back to a healthy
*  state, maybe that will help also revert the more global clinical phenotype. So that's really what
*  we're hoping to do. That step, that backwards step, I was reading about it, the Yamanaka factor.
*  Yes. So like that reverse step back to stem cells. Yes. It seems like magic. It is. Honestly,
*  before that happened, I think very few people would have predicted that to be possible.
*  It's amazing. Can you maybe elaborate, is it actually possible? So this result was maybe,
*  I don't know how many years ago, maybe 10 years ago was first demonstrated, something like that.
*  How hard is this? How noisy is this backwards step? It seems quite incredible and cool.
*  It is incredible and cool. It was much more, I think, finicky and bespoke at the early stages
*  when the discovery was first made. But at this point, it's become almost industrialized. There are
*  what's called contract research organizations, vendors that will take a sample from a human and
*  revert it back to stem cell status and it works a very good fraction of the time. Now there are
*  people who will ask, I think, good questions. Is this really truly a stem cell or does it remember
*  certain aspects of changes that were made in the human beyond the genetics? It's passed as a skin
*  cell. It's passed as a skin cell or it's passed in terms of exposures to different environmental
*  factors and so on. So I think the consensus right now is that these are not always perfect and there
*  is little bits and pieces of memory sometimes, but by and large, these are actually pretty good.
*  So one of the key things, well, maybe you can correct me, but one of the useful things for
*  machine learning is size, scale of data. How easy it is to do these kinds of reversals
*  to stem cells and then disease in a dish models at scale. Is that a huge challenge or not?
*  So the reversal is not as of this point something that can be done at the scale of
*  tens of thousands or hundreds of thousands. I think total number of stem cells or IPS cells
*  that are what's called induced pluripotent stem cells in the world, I think is somewhere between
*  five and 10,000 last I looked. Now again, that might not count things that exist in this or
*  that academic center and they may add up to a bit more, but that's about the range. So it's not
*  something that you could at this point generate IPS cells from a million people, but maybe you
*  don't need to because maybe that background is enough because it can also be now perturbed in
*  different ways. And some people have done really interesting experiments in, for instance, taking
*  cells from a healthy human and then introducing a mutation into it using one of the other
*  miracle technologies that's emerged in the last decade, which is CRISPR gene editing,
*  and introduced a mutation that is known to be pathogenic. And so you can now look at the healthy
*  cells and unhealthy cells, the one with the mutation and do a one-on-one comparison where
*  everything else is held constant. And so you could really start to understand specifically what the
*  mutation does at the cellular level. So the IPS cells are a great starting point and obviously
*  more diversity is better because you also want to capture ethnic background and how that affects
*  things. But maybe you don't need one from every single patient with every single type of disease
*  because we have other tools at our disposal. Well, how much difference is there between people?
*  I mentioned ethnic background in terms of IPS cells. So we're all like, it seems like these
*  magical cells that can do to create anything between different populations, different people.
*  Is there a lot of variability between cell cells? Well, first of all, there's the variability that's
*  driven simply by the fact that genetically we're different. So a stem cell that's derived from my
*  genotype is going to be different from a stem cell that's derived from your genotype. There's
*  also some differences that have more to do with, for whatever reason, some people's stem cells
*  differentiate better than other people's stem cells. We don't entirely understand why, so there's
*  certainly some differences there as well. But the fundamental difference and the one that we really
*  care about and is positive is the fact that the genetics are different and therefore we capitulate
*  my disease burden versus your disease burden. What's the disease burden?
*  Well, disease burden is just if you think, I mean, it's not a well-defined mathematical term,
*  although there are mathematical formulations of it. If you think about the fact that some of us
*  are more likely to get a certain disease than others because we have more variations in our
*  genome that are causative of the disease, maybe fewer that are protective of the disease.
*  People have quantified that using what are called polygenic risk scores, which look at all of the
*  variations in an individual person's genome and add them all up in terms of how much risk they
*  confer for a particular disease and then they've put people on a spectrum of their disease risk.
*  For certain diseases where we've been sufficiently powered to really understand the connection
*  between the many, many small variations that give rise to an increased disease risk, there
*  is some pretty significant differences in terms of the risk between the people, say, at the highest
*  decile of this polygenic risk score and the people at the lowest decile. Sometimes those
*  differences are a factor of 10 or 12 higher. So there's definitely
*  a lot that our genetics contributes to disease risk, even if it's not by any stretch the full
*  explanation. And from a machine learning perspective, there's signal there.
*  There is definitely signal in the genetics and there's even more signal, we believe,
*  in looking at the cells that are derived from those different genetics because in principle,
*  you could say all the signal is there at the genetics level, so we don't need to look at
*  the cells. But our understanding of the biology is so limited at this point, then seeing what
*  actually happens at the cellular level is a heck of a lot closer to the human clinical outcome
*  than looking at the genetics directly. And so we can learn a lot more from it
*  than we could by looking at genetics alone. So just to get a sense, I don't know if it's
*  easy to do, but what kind of data is useful in this disease in a dish model? What's the source
*  of raw data information? And also, from my outsider's perspective, biology and cells
*  are squishy things. They are. They're literally squishy things. How do you connect the computer
*  to that? Which sensory mechanisms, I guess? So that's another one of those revolutions
*  that have happened in the last 10 years in that our ability to measure cells very quantitatively
*  has also dramatically increased. So back when I started doing biology in the late
*  90s, early 2000s, that was the initial era where we started to measure biology in really
*  quantitative ways using things like microarrays, where you would measure in a single experiment
*  the activity level, what's called expression level, of every gene in the genome in that sample.
*  And that ability is what actually allowed us to even understand that there are molecular
*  subtypes of diseases like cancer, where up until that point it's like, oh, you have breast cancer.
*  But then when we looked at the molecular data, it was clear that there's different subtypes
*  of breast cancer that at the level of gene activity look completely different to each other.
*  So that was the beginning of this process. Now we have the ability to measure
*  individual cells in terms of their gene activity using what's called single cell RNA sequencing,
*  which basically sequences the RNA, which is that activity level of different genes
*  for every gene in the genome. And you could do that at single cell level. So that's an incredibly
*  powerful way of measuring cells. I mean, you literally count the number of transcripts. So
*  it really turns that squishy thing into something that's digital. Another tremendous data source
*  that's emerged in the last few years is microscopy and specifically even super resolution microscopy,
*  where you could use digital reconstruction to look at subcellular structures, sometimes even
*  things that are below the diffraction limit of light by doing sophisticated reconstruction.
*  And again, that gives you a tremendous amount of information at the subcellular level. There's now
*  more and more ways that amazing scientists out there are developing for getting new types of
*  information from even single cells. And so that is a way of turning those squishy things into
*  digital data. Into beautiful data sets. So that data set then with machine learning tools allows
*  you to maybe understand the developmental, like the mechanism of a particular disease.
*  And if it's possible to sort of at a high level describe how does that help
*  lead to a drug discovery that can help prevent, reverse that mechanism?
*  So I think there's different ways in which this data could potentially be used. Some people use it
*  for scientific discovery and say, oh, look, we see this phenotype at the cellular level.
*  So let's try and work our way backwards and think which genes might be involved in pathways that
*  give rise to that. So that's a very sort of analytical method to sort of work our way backwards
*  using our understanding of known biology. Some people use it in a somewhat more
*  forward, if that was backward, this would be forward, which is to say, okay, if I can perturb
*  this gene, does it show a phenotype that is similar to what I see in disease patients? And so maybe
*  that gene is actually causal of the disease. So that's a different way. And then there's what we
*  do, which is basically to take that very large collection of data and use machine learning to
*  uncover the patterns that emerge from it. So for instance, what are those subtypes that might be
*  similar at the human clinical outcome, but quite distinct when you look at the molecular data?
*  And then if we can identify such a subtype, are there interventions that if I apply it to
*  cells that come from this subtype of the disease and you apply that intervention,
*  it could be a drug or it could be a CRISPR gene intervention, does it revert the disease state
*  to something that looks more like normal, happy, healthy cells? And so hopefully if you see that,
*  that gives you a certain hope that that intervention will also have a meaningful
*  clinical benefit to people. And there's obviously a bunch of things that you would want to do after
*  that to validate that, but it's a very different and much less hypothesis driven way of uncovering
*  new potential interventions and might give rise to things that are not the same things that everyone
*  else is already looking at. I don't know. I'm just like to psychoanalyze my own feeling about our
*  discussion currently. It's so exciting to talk about fundamentally something that's been turned
*  into a machine learning problem and that can have so much real world impact.
*  That's how I feel too.
*  That's kind of exciting because I'm so, most of my days spent with data sets that I guess closer to
*  the news groups. So this is a kind of, it just feels good to talk about. In fact, I don't almost
*  don't want to talk to you about machine learning. I want to talk about the fundamentals of the data
*  set, which is an exciting place to be. I agree with you. It's what gets me up in the morning.
*  It's also what attracts a lot of the people who work at in-situ to in-situ because I think
*  certainly all of our machine learning people are outstanding and could go get a job selling ads
*  online or doing e-commerce or even self-driving cars. But I think they come to us because they
*  want to work on something that has more of an aspirational nature and can really benefit humanity.
*  With these approaches, what do you hope, what kind of diseases can be helped? We mentioned
*  Alzheimer's, schizophrenia, type 2 diabetes. Can you just describe the various kinds of diseases
*  that this approach can help?
*  Well, we don't know. I try and be very cautious about making promises about some things.
*  Oh, we will cure X. People make that promise. I tried to first deliver and then promise,
*  as opposed to the other way around. There are characteristics of a disease that make it more
*  likely that this type of approach can potentially be helpful. For instance, diseases that have a
*  very strong genetic basis are ones that are more likely to manifest in a stem cell derived model.
*  We would want the cellular models to be relatively reproducible and robust so that you could actually
*  get enough of those cells in a way that isn't very highly variable and noisy. You would want
*  the disease to be relatively contained in one or a small number of cell types that you could actually
*  create in an in vitro in a dish setting. Whereas if it's something that's really broad and systemic
*  and involves multiple cells that are in very distal parts of your body, putting that all in
*  the dish is really challenging. We want to focus on the ones that are most likely to be successful
*  today with the hope, I think, that really smart bioengineers out there are developing better and
*  better systems all the time so that diseases that might not be tractable today might be tractable in
*  three years. For instance, five years ago, these stem cell derived models didn't really exist.
*  People were doing most of the work in cancer cells. Cancer cells are very, very poor models of most
*  human biology because they're, A, they were cancer to begin with and B, as you passage them and they
*  proliferate in a dish, they become, because of the genomic instability, even less similar to human
*  biology. Now we have these stem cell derived models. We have the capability to reasonably robustly,
*  not quite at the right scale yet, but close, to derive what's called organoids, which are these
*  teeny little sort of multicellular organ sort of models of an organ system. So there are cerebral
*  organoids and liver organoids and kidney organoids and-
*  Yeah, brain organoids.
*  That organoid.
*  Is possibly the coolest thing I've ever seen.
*  Is that not the coolest thing? And then I think on the horizon, we're starting to see things like
*  connecting these organoids to each other so that you could actually start, and there's some really
*  cool papers that start to do that, where you can actually start to say, okay, can we do multi-organ
*  system stuff? There's many challenges to that. It's not easy by any stretch, but it might,
*  I'm sure people will figure it out. And in three years or five years, there will be disease models
*  that we could make for things that we can't make today.
*  Yeah. And this conversation would seem almost outdated with the kind of scale that could be
*  achieved in like three years. That's the hope.
*  I hope so. That would be so cool.
*  You've co-founded Coursera with Andrew Ng, and we're part of the whole MOOC revolution.
*  So to jump topics a little bit, can you maybe tell the origin story of the history,
*  the origin story of MOOCs, of Coursera, and in general,
*  your teaching to huge audiences on a very impactful topic of AI in general?
*  So I think the origin story of MOOCs emanates from a number of efforts that occurred at
*  Stanford University around the late 2000s, where different individuals within Stanford,
*  myself included, were getting really excited about the opportunities of using online technologies
*  as a way of achieving both improved quality of teaching and also improved scale.
*  And so Andrew, for instance, led the Stanford Engineering Everywhere, which was sort of an
*  attempt to take 10 Stanford courses and put them online, just as video lectures. I led an effort
*  within Stanford to take some of the courses and really create a very different teaching model that
*  broke those up into smaller units and had some of those embedded interactions and so on,
*  which got a lot of support from university leaders because they felt like it was potentially a way of
*  improving the quality of instruction at Stanford by moving to what's now called the flipped classroom
*  model. And so those efforts eventually started to interplay with each other and created a tremendous
*  sense of excitement and energy within the Stanford community about the potential of
*  online teaching and led in the fall of 2011 to the launch of the first Stanford MOOCs.
*  By the way, MOOCs, it's probably impossible that people don't know, but I guess massive...
*  Open online courses.
*  Open online courses.
*  We did not come up with the acronym. I'm not particularly fond of the acronym, but it is what
*  it is. Big bang is not a great term for the start of the universe, but it is what it is.
*  Probably so. So anyway, those courses launched in the fall of 2011 and there were within a matter
*  of weeks with no real publicity campaign, just a New York Times article that went viral,
*  about 100,000 students or more in each of those courses. And I remember this conversation that
*  Andrew and I had, which was like, wow, there's this real need here. And I think we both felt like,
*  sure, we were accomplished academics and we could go back and go back to our labs,
*  write more papers. But if we did that, then this wouldn't happen. And it seemed too important not
*  to happen. And so we spent a fair bit of time debating, do we want to do this as a Stanford
*  effort, kind of building on what we'd started? Do we want to do this as a for-profit company?
*  Do we want to do this as a nonprofit? And we decided ultimately to do it as we did with Coursera.
*  And so we started really operating as a company at the beginning of 2012.
*  And the rest is history.
*  And the rest is history.
*  But was that really surprising to you? How did you at that time and at this time
*  make sense of this need for sort of global education you mentioned? That you felt that,
*  wow, the popularity indicates that there's a hunger for sort of globalization of learning.
*  I think there is a hunger for learning that, you know, globalization is part of it, but I think
*  it's just a hunger for learning. The world has changed in the last 50 years. It used to be that
*  you finished college, you got a job. By and large, the skills that you learned in college were
*  pretty much what got you through the rest of your job history. And yeah, you learned some stuff,
*  but it wasn't a dramatic change. Today we're in a world where the skills that you need for a lot
*  of jobs today didn't even exist when you went to college. And many of the jobs that existed when
*  you went to college don't even exist today or are dying. So part of that is due to AI, but not only.
*  And we need to find a way of giving people access to the skills that they need today. And I think
*  that's really what's driving a lot of this hunger. So I think if we even take a step back,
*  for you all, this started in trying to think of new ways to teach or new ways to sort of
*  organize the material and present the material in a way that would help the education process,
*  the pedagogy. So what have you learned about effective education from this process of playing,
*  of experimenting with different ideas? So we learned a number of things, some of which
*  I think could translate back and have translated back effectively to how people teach on campus,
*  and some of which I think are more specific to people who learn online, more sort of people who
*  learn as part of their daily life. So we learned, for instance, very quickly that short is better.
*  So people who are especially in the workforce can't do a 15-week semester-long course. They
*  just can't fit that into their lives. Sure. Can you describe the shortness of what?
*  Every aspect of the little lecture short, the course is short.
*  Both. We started out, the first online education efforts were actually MIT's open courseware
*  initiatives, and that was recording of classroom lectures. Hour and a half or something like that.
*  That didn't really work very well. I mean, some people benefit, I mean, of course they did, but
*  it's not really a very palatable experience for someone who has a job and three kids and
*  that they need to run errands and such. They can't fit 15 weeks into their life, and the
*  hour and a half is really hard. So we learned very quickly, I mean, we started out with short video
*  modules and over time we made them shorter because we realized that 15 minutes was still too long.
*  If you want to fit in when you're waiting in line for your kid's doctor's appointment,
*  it's better if it's five to seven. We learned that 15-week courses don't work, and you really want to
*  break this up into shorter units so that there's a natural completion point, gives people a sense
*  of they're really close to finishing something meaningful. They can always come back and take
*  part two and part three. We also learned that compressing the content works really well,
*  because if some people that pace works well, for others they can always rewind and watch again,
*  and so people have the ability to then learn at their own pace.
*  The brevity and the flexibility are both things that we found to be very important. We learned
*  that engagement during the content is important, and the quicker you give people feedback, the more
*  likely they are to be engaged. Hence, the introduction of these, which we actually
*  was an intuition that I had going in and was then validated using data, that introducing some of
*  these sort of little micro quizzes into the lectures really helps. Self-graded, automatically
*  graded assessments really help too, because it gives people feedback. See, there you are.
*  All of these are valuable. Then we learned a bunch of other things too. We did some really
*  interesting experiments, for instance, on gender bias and how having a female role model as an
*  instructor can change the balance of men to women, especially in STEM courses. You could do that
*  online by doing A-B testing in ways that would be really difficult to go on campus.
*  Oh, that's exciting. The shortness, the compression, that's actually...
*  That probably is true for all... Good editing is always just compressing the content,
*  making it shorter. That puts a lot of burden on the instructor and the creator of the
*  educational content. Probably most lectures at MIT or Stanford could be five times shorter
*  if the preparation was put enough. Maybe people might disagree with that, but the crispness,
*  the clarity that a lot of the MOOC or CERA delivers, how much effort does that take?
*  First of all, let me say that it's not clear that that crispness would work as effectively
*  in a face-to-face setting, because people need time to absorb the material.
*  And so you need to at least pause and give people a chance to reflect and maybe practice.
*  And that's what MOOCs do, is that they give you these chunks of content and then ask you to
*  practice with it. And that's where I think some of the newer pedagogy that people are adopting in
*  face-to-face teaching that have to do with interactive learning and such can be really
*  helpful. But both those approaches, whether you're doing that type of methodology in online teaching
*  or in that flipped classroom interactive teaching. What's flipped classroom?
*  Flipped classroom is a way in which online content is used to supplement face-to-face teaching,
*  where people watch the videos perhaps and do some of the exercises before coming to class. And then
*  when they come to class, it's actually to do much deeper problem solving, oftentimes in a group.
*  But any one of those different pedagogies that are beyond just standing there and droning on in
*  front of the classroom for an hour and 15 minutes require a heck of a lot more preparation. And so
*  it's one of the challenges I think that people have, that we had when trying to convince
*  instructors to teach on Coursera. And it's part of the challenges that pedagogy experts on campus
*  have in trying to get faculty to teach differently is that it's actually harder to teach that way
*  than it is to teach on a classroom. And so it's one of the challenges that people have
*  than it is to stand there and drone. Do you think MOOCs will replace
*  in-person education or become the majority of in-person education of the way people learn
*  in the future? Again, the future could be very far away, but where's the trend going? Do you think?
*  So I think it's a nuanced and complicated answer. I don't think MOOCs will replace
*  face-to-face teaching. I think learning is in many cases a social experience. And even at
*  Coursera, we had people who naturally formed study groups, even when they didn't have to,
*  to just come and talk to each other. And we found that that actually benefited their learning
*  in very important ways. So there was more success among learners who had those study groups than
*  among ones who didn't. So I don't think it's just going to, oh, we're all going to just suddenly
*  learn online with a computer and no one else in the same way that recorded music has not replaced
*  live concerts. But I do think that especially when you are thinking about continuing education,
*  the stuff that people get when their traditional, whatever high school, college education is done,
*  and they yet have to maintain their level of expertise and skills in a rapidly changing world,
*  I think people will consume more and more educational content in this online format
*  because going back to school for formal education is not an option for most people.
*  Briefly, it might be a difficult question to ask, but there's a lot of people fascinated by
*  artificial intelligence, by machine learning, by deep learning. Is there a recommendation for
*  the next year or for a lifelong journey? If somebody interested in this,
*  how do they begin? How do they enter that learning journey?
*  I think the important thing is first to just get started. And there's plenty of online content
*  that one can get for both the core foundations of mathematics and statistics and programming.
*  And then from there to machine learning, I would encourage people not to skip too quickly past the
*  foundations because I find that there's a lot of people who learn machine learning, whether it's
*  online or on campus without getting those foundations. And they basically just turn the
*  crank on existing models in ways that A, don't allow for a lot of innovation and adjustment to
*  the problem at hand, but also B, are sometimes just wrong and they don't even realize that
*  their application is wrong because there's artifacts that they haven't fully understood.
*  So I think the foundations, machine learning is an important step. And then actually start solving
*  problems. Try and find someone to solve them with because especially at the beginning, it's
*  useful to have someone to bounce ideas off and fix mistakes that you make, and you can fix mistakes
*  that they make. But then just find practical problems, whether it's in your workplace or if
*  you don't have that, Kaggle competitions or such are a really great place to find interesting
*  problems and just practice. Practice. Perhaps a bit of a romanticized question, but what idea
*  in deep learning do you find, have you found in your journey, the most beautiful or surprising
*  or interesting? Perhaps not just deep learning, but AI in general, statistics.
*  I'm going to answer with two things. One would be the foundational concept of end-to-end training,
*  which is that you start from the raw data and you train something that is not like a single
*  piece, but rather towards the actual goal that you're looking to...
*  So from the raw data to the outcome, and no details in between?
*  Well, not no details, but the fact that you could certainly introduce building blocks that were
*  trained towards other tasks. I'm actually coming to that in my second half of the answer.
*  But that doesn't have to be a single monolithic blob in the middle. Actually, I think that's not
*  ideal, but rather the fact that at the end of the day, you can actually train something that
*  goes all the way from the beginning to the end. And the other one that I find really compelling
*  is the notion of learning a representation that in its turn, even if it was trained to another task,
*  can potentially be used as a much more rapid starting point to solving a different task.
*  And that's, I think, reminiscent of what makes people successful learners. It's something that
*  is relatively new in the machine learning space. I think it's underutilized even relative to today's
*  capabilities, but more and more of how do we learn reusable representation.
*  So end-to-end and transfer learning, is it surprising to you that neural networks are able
*  to, in many cases, do these things? Is it maybe taking back to when you first would dive deep into
*  neural networks or in general, even today, is it surprising that neural networks work at all and work
*  wonderfully to do this kind of raw end-to-end learning and even transfer learning?
*  I think I was surprised by how well when you have large enough amounts of data,
*  it's possible to find a meaningful representation in what is an exceedingly high-dimensional space.
*  And so I find that to be really exciting and people are still working on the math for that.
*  There's more papers on that every year and I think it would be really cool if we figured that out.
*  But that to me was a surprise because in the early days when I was starting my way in machine
*  learning and the datasets were rather small, I think we believed that you needed to have a much
*  more constrained and knowledge-rich search space to really get to a meaningful answer.
*  And I think it was true at the time. What I think is still a question is, will a completely
*  knowledge-free approach where there's no prior knowledge going into the construction of the model,
*  is that going to be the solution or not? It's not actually the solution today in the sense that
*  the architecture of a convolutional neural network that's used for images is actually quite
*  different to the type of network that's used for language and yet different from the one that's
*  used for speech or biology or any other application. There's still some insight that goes into the
*  structure of the network to get to the right performance. Will you be able to come up with
*  a universal learning machine? I don't know. I wonder if there always has to be some insight
*  injected somewhere or whether it can converge. So you've done a lot of interesting work with
*  probabilistic graphical models in general, Bayesian deep learning and so on. Can you maybe speak high
*  level? How can learning systems deal with uncertainty? One of the limitations, I think,
*  of a lot of machine learning models is that they come up with an answer and you don't know how much
*  you can believe that answer. And oftentimes the answer is actually quite poorly calibrated
*  relative to its uncertainties. Even if you look at where the confidence that comes out of the
*  say the neural network at the end and you ask how much more likely is an answer of 0.8 versus 0.9,
*  it's not really in any way calibrated to the actual reliability of that network and how true it is.
*  The further away you move from the training data, not only the more wrong the network is,
*  often it's more wrong and more confident in its wrong answer. That is a serious issue in a lot of
*  application areas. When you think, for instance, about medical diagnosis as being maybe an epitome
*  of how problematic this can be, if you were training your network on a certain set of
*  patients in a certain patient population and I have a patient that is an outlier and there's
*  no human that looks at this and that patient is put into a neural network and your network
*  not only gives a completely incorrect diagnosis but is supremely confident in its wrong answer,
*  you could kill people. So I think creating more of an understanding of how do you produce networks
*  that are calibrated in their uncertainty and can also say, I give up, I don't know what to say about
*  this particular data instance because I've never seen something that's sufficiently like it before.
*  I think it's going to be really important in mission critical applications, especially ones
*  where human life is at stake and that includes medical applications but it also includes
*  automated driving because you'd want the network to be able to say, I have no idea what this blob
*  that I'm seeing in the middle of the road, so I'm just going to stop because I don't want to
*  potentially run over a pedestrian that I don't recognize. Is there good mechanisms, ideas of how
*  to allow learning systems to provide that uncertainty along with their predictions?
*  Certainly people have come up with mechanisms that involve Bayesian deep learning, deep learning
*  that involves Gaussian processes. There's a slew of different approaches that people have come up with.
*  There's methods that use ensembles of networks with different subsets of data or different
*  random starting points. Those are actually sometimes surprisingly good at creating a set of
*  how confident or not you are in your answer. It's very much an area of open research.
*  Let's cautiously venture back into the land of philosophy. Speaking of AI systems providing
*  uncertainty, somebody like Stuart Russell believes that as we create more and more
*  intelligent systems, it's really important for them to be full of self-doubt because if they're
*  given more and more power, the way to maintain human control over AI systems or human supervision,
*  which is true, like you just mentioned with autonomous vehicles, is really important to get
*  human supervision when the car is not sure because if it's really confident in cases when it can get
*  in trouble, it's going to be really problematic. Let me ask about the questions of AGI and human
*  level intelligence. We've talked about curing diseases, which is a fundamental thing we can
*  have an impact today, but AI people also dream of both understanding and creating
*  intelligence. Is that something you think about? Is that something you dream about?
*  Is that something you think is within our reach to be thinking about as computer scientists?
*  Boy, let me tease apart different parts of that question.
*  The worst question.
*  It's a multi-part question. Let me start with the feasibility of AGI, then I'll talk about the
*  timelines a little bit and then talk about what controls does one need when thinking about
*  protections in the AI space. I think AGI obviously is a long-standing dream that even our
*  early pioneers in the space had, the Turing test and so on are the earliest discussions of that.
*  We're obviously closer than we were 70 or so years ago, but I think it's still very far away.
*  I think machine learning algorithms today are really exquisitely good pattern recognizers in
*  very specific problem domains where they have seen enough training data to make good predictions.
*  You take a machine learning algorithm and you move it to a slightly different version of even
*  that same problem, far less one that's different, and it will just completely choke.
*  I think we're nowhere close to the versatility and flexibility of even a human toddler in terms of
*  their ability to context switch and solve different problems using a single
*  knowledge base, single brain. Am I desperately worried about
*  the machines taking over the universe and starting to kill people because they want to have more
*  power? I don't think so. To pause on that, you've kind of
*  intuited that super intelligence is a very difficult thing to achieve.
*  I think even intelligence. Super intelligence, we're not even close to intelligence.
*  Even just the greater abilities of generalization of our current systems.
*  We haven't answered all the parts. I'm getting to the second part.
*  Maybe another tangent you can also pick up is can we get in trouble with much dumber systems?
*  Yes. That is exactly where I was going. Just to wrap up on the threats of AGI, I think that
*  it seems to me a little early today to figure out protections against a human level or super
*  human level intelligence where we don't even see the skeleton of what that would look like.
*  It seems that it's very speculative on how to protect against that. But we can definitely,
*  and have gotten into trouble on much dumber systems. A lot of that has to do with the fact
*  that the systems that we're building are increasingly complex, increasingly poorly understood.
*  There's ripple effects that are unpredictable in changing little things that can have dramatic
*  consequences on the outcome. By the way, that's not unique to artificial intelligence. I think
*  artificial intelligence exacerbates that, brings it to a new level. But heck, our electric grid
*  is really complicated. The software that runs our financial markets is really complicated.
*  We've seen those ripple effects translate to dramatic negative consequences, like for instance,
*  financial crashes that have to do with feedback loops that we didn't anticipate.
*  I think that's an issue that we need to be thoughtful about in many places, artificial
*  intelligence being one of them. I think it's really important that people are thinking about
*  ways in which we can have better interpretability of systems, better tests for, for instance,
*  measuring the extent to which a machine learning system that was trained in one set of circumstances,
*  how well does it actually work in a very different set of circumstances where you might say, for
*  instance, well, I'm not going to be able to test my automated vehicle in every possible city,
*  village, weather, condition, and so on. But if you trained it on this set of conditions,
*  and then tested it on 50 or 100 others that were quite different from the ones that you
*  trained it on, and it worked, then that gives you confidence that the next 50 that you didn't test
*  it on might also work. So effectively it's testing for generalizability. So I think there's ways that
*  we should be constantly thinking about to validate the robustness of our systems. I think it's very
*  different from the let's make sure robots don't take over the world. And then the other place
*  where I think we have a threat, which is also important for us to think about, is the extent
*  to which technology can be abused. So like any really powerful technology, machine learning can
*  be very much used badly as well as too good. And that goes back to many other technologies that
*  I've come up with when people invented projectile missiles and it turned into guns, and people
*  invented nuclear power and it turned into nuclear bombs. And I think honestly, I would say that
*  to me, gene editing and CRISPR is at least as dangerous a technology if used badly as machine
*  learning. You could create really nasty viruses and such using gene editing that
*  you would be really careful about. So anyway, that's something that we need to be really
*  thoughtful about whenever we have any really powerful new technology.
*  Yeah, and in the case of machine learning, it's adversarial machine learning, so all the kinds of
*  attacks like security almost threats and there's a social engineering with machine learning
*  algorithms. And there's face recognition and big brothers watching you and there's the killer drones
*  that can potentially go and targeted execution of people in a different country. I don't want to
*  argue that bombs are not necessarily that much better, but if people want to kill someone,
*  they'll find a way to do it. So if you, if in general, if you look at trends in the data,
*  there's less wars, there's less violence, there's more human rights. So we've been doing overall
*  quite good as a human species. Are you optimistic? Maybe another way to ask is,
*  do you think most people are good? And fundamentally, we tend towards a better world,
*  which is underlying the question, will machine learning with gene editing ultimately land us
*  somewhere good? Are you optimistic? I think by and large, I'm optimistic. I think that
*  most people mean well. That doesn't mean that most people are altruistic do-gooders, but I think
*  most people mean well. But I think it's also really important for us as a society to create
*  social norms where doing good and being perceived well by our peers is, are positively correlated.
*  I mean, it's very easy to create dysfunctional societies. There are certainly multiple
*  psychological experiments, as well as sadly, real world events where people have devolved to a world
*  where being perceived well by your peers is correlated with really atrocious, often genocidal
*  behaviors. So we really want to make sure that we maintain a set of social norms where people know
*  that to be a successful member of society, you want to be doing good. And one of the things that
*  I sometimes worry about is that some societies don't seem to necessarily be moving in the forward
*  direction in that regard, where it's not necessarily the case that being a good person is what makes you
*  be perceived well by your peers. And I think that's a really important thing for us as a society to
*  remember. It's very easy to degenerate back into a universe where it's okay to do really bad stuff
*  and still have your peers think you're amazing. It's fun to ask a world-class computer scientist
*  and engineer a ridiculously philosophical question like, what is the meaning of life?
*  Let me ask, what gives your life meaning? What is the source of fulfillment, happiness, joy, purpose?
*  When we were starting Coursera in the fall of 2011, that was right around the time that
*  Steve Jobs passed away. And so the media was full of various famous quotes he uttered. And one of
*  them that really stuck with me because it resonated with stuff that I'd been feeling for even years
*  before that is that our goal in life should be to make a dent in the universe. So I think that to me,
*  what gives my life meaning is that I would hope that when I am lying there on my deathbed and
*  looking at what I've done in my life, that I can point to ways in which I have left the world a
*  better place than it was when I entered it. This is something I tell my kids all the time,
*  because I also think that the burden of that is much greater for those of us who were born
*  to privilege. And in some ways I was. I wasn't born super wealthy or anything like that, but
*  I grew up in an educated family with parents who loved me and took care of me. And I had a chance
*  at a great education and I always had enough to eat. So I was in many ways born to privilege more
*  than the vast majority of humanity. And my kids, I think, are even more so born to privilege than I
*  was fortunate enough to be. And I think it's really important that, especially for those of us who
*  have that opportunity, that we use our lives to make the world a better place.
*  I don't think there's a better way to end it, Daphne. It was an honor to talk to you. Thank
*  you so much for talking to me. Thank you.
*  Thanks for listening to this conversation with Daphne Kohler. And thank you to our
*  presenting sponsor, Cash App. Please consider supporting the podcast by downloading Cash App
*  and using code LEXPODCAST. If you enjoy this podcast, subscribe on YouTube, review the Five
*  Stars on Apple podcast, support on Patreon, or simply connect with me on Twitter at Lex Friedman.
*  And now let me leave you with some words from Hippocrates, a physician from ancient Greece
*  who's considered to be the father of medicine. Wherever the art of medicine is loved,
*  there's also a love of humanity. Thank you for listening and hope to see you next time.

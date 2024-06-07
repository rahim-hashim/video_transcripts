---
Date Generated: June 07, 2024
Transcription Model: whisper medium 20231117
Length: 4278s
Video Keywords: []
Video Views: 9792
Video Rating: None
Video Description: Patreon: https://www.patreon.com/seanmcarroll
Blog post with audio player, show notes, and transcript: https://www.preposterousuniverse.com/podcast/2023/09/25/251-rosemary-braun-on-uncovering-patterns-in-biological-complexity/

Biological organisms are paradigmatic emergent systems. That atoms of which they are made mindlessly obey the local laws of physics; even cells and organs do their individual jobs without explicitly understanding the larger whole of which they are a part. And yet the system as a whole functions beautifully, with apparent purpose and function. How do the small parts come together to form the greater whole? I talk with biophysicist Rosemary Braun about what we're learning about collective behavior within organisms from the modern era of huge biological datasets, especially crucial aspects like timekeeping (with bonus implications for dealing with jet lag).

Rosemary Braun received her Ph.D. in physics from the University of Illinois at Urbana-Champaign, and an M.P.H. in biostatistics from Johns Hopkins. She is currently an associate professor of molecular biosciences, applied math, and physics at Northwestern University and external faculty at the Santa Fe Institute.

Mindscape Podcast playlist: https://www.youtube.com/playlist?list=PLrxfgDEc2NxY_fRExpDXr87tzRbPCaA5x
Sean Carroll channel: https://www.youtube.com/c/seancarroll

#podcast #ideas #science #philosophy #culture
---

# Mindscape 251 | Rosemary Braun on Uncovering Patterns in Biological Complexity
**Mindscape Podcast:** [September 25, 2023](https://www.youtube.com/watch?v=LCQg1EPNCZ0)
*  Hello everyone, welcome to the Mindscape Podcast. I'm your host, Sean Carroll. We all know about
*  circadian rhythms, right? We get tired at night, we go to sleep, we wake up, we're refreshed,
*  hopefully, maybe there's caffeine involved. But there's a cycle that we go through, roughly 24
*  hours. Our bodies and our brains, which are connected to our bodies, are very much influenced
*  by internal clocks that let us know what time of day it is. This is why when we travel to a
*  different time zone, we get jetlagged because there's a mismatch between the activities of
*  the day and the position of the sun in the sky versus those internal clocks. So here's something
*  that maybe I knew before but had forgotten, but I learned during this podcast, essentially every cell
*  in our body has its own circadian clock to let the cell know what time of day it is. Of course,
*  there's also systems in our bodies because the cells talk to each other, there's the nervous
*  system and there's the metabolic system and so forth, but it kind of bubbles up from the individual
*  cells. So when you get jetlagged or even just when you get tired at night because you know that it's
*  bedtime, it's not just some large scale impression that your body has, it's every cell in your body
*  is thinking this way, which is kind of a remarkable fact. You know, biology is in a great position
*  these days. It's a very exciting time. There's enormous amounts of data coming in, of course.
*  We can analyze genes and molecular biology questions in much greater detail than we ever
*  could before. And there's also tools to analyze that with great computational power, machine
*  learning and AI, all that kinds of stuff. Plus, of course, there are questions to which we don't
*  know the answers. In physics, if you listen to my long solo podcast, one of the challenges is that
*  we have theories that fit the data really well in the regimes where we can experimentally access
*  in biology. Don't worry, that is not the case. It's very easy to ask questions that are very
*  important, but we don't know the answer. But it's plausible that we can find the answer. So today
*  we're talking to Rosemary Brown, who is a biologist, molecular biologist slash engineer at Northwestern,
*  who works at the sort of systems level of biology, right? Rather than looking at this particular
*  organism and its whole lifecycle, or for that matter, this particular organ in an organism,
*  she looks at the various complexes, the various networks, the various systems that hook together
*  inside biological organisms. The circadian rhythm is one of them, but there's many different ways
*  that this kind of paradigm plays out. It's very different than in physics, where you can find a
*  simple spherical cow, you know, abstract away all the complications and just look at the harmonic
*  oscillator or whatever. In biology, very often we have these intricate complex networks that are
*  talking to each other. And so that's what we're going to explore today. Before going onto that,
*  let me just mention, I haven't mentioned in a while, we're still doing the Mindscape Big Picture
*  Scholarship. So this is something where people who are going to college, going to universities,
*  can apply for the scholarship. It's $10,000 if you win, so it just goes right to your tuition. It is
*  aimed at youngsters who are going to go to college who are interested in the big picture,
*  so who are interested in, you know, not necessarily doing something applied or primarily financially
*  rewarding, but thinking about the big ideas, people who want to concentrate in fundamental
*  physics or philosophy or mathematics, or for that matter, history or literature or economics or
*  what have you, as long as it's that thinking deeply about the fundamentals kind of aspect.
*  Those are the applicants we want. So if you're interested in applying or if you're interested
*  in donating to the Big Picture Scholarship Fund, go to bold.org slash scholarships slash Mindscape.
*  Bold.org B-O-L-D dot org is a wonderful organization that helps people crowdsource these
*  kind of scholarships. Last year we gave out two scholarships. It's just very heartwarming
*  that you can contribute to the education of some young student, especially ones that might not,
*  you know, come from academic backgrounds, etc. So it's a very nice thing you can do. There's also
*  a link on our Mindscape homepage, which is just preposterous universe.com slash podcast if you
*  want to go directly from there. So thanks for everyone who has been donating. We've been getting
*  donations all year. We gave out two scholarships last year. Let's hope we can do even better this
*  year. So with that, let's go. Rosemary Brown, welcome to the Mindscape Podcast.
*  Thank you so much for having me.
*  Let me ask about the Big Picture here. That's my favorite thing to ask about. As an outsider,
*  it seems to me that there's a shift in the last few decades or whatever in biology from talking
*  largely about organisms or species to now thinking about systems and networks and
*  genomes and so forth. Is that an accurate perception as an outsider?
*  I think it is. Yeah. I think in large part, it's been driven by the revolution in
*  micro- and molecular biology profiling technologies. So we're now able to assay
*  gene expression in elaborate detail. We can look at genetic variations in extraordinary detail.
*  We need a way to make sense of all of that information. Trying to relate what we measure
*  in this 20,000 dimensional feature space of gene expression to what we can see under the microscope
*  or in a patient who has just walked into a clinic. Relating those two things to each other is a major
*  challenge that we have now. And one way to approach that problem is to look at it from a
*  systems point of view and to think about what the network of interactions between those microscopic
*  elements are that produce the macroscopic features that we observe. So when I just out of my head
*  came up with systems and networks, are those the right words? Yeah, I would say so. Yeah. Okay,
*  good. And it's largely because more data isn't, I don't want to say it's not always better. More
*  data is always better, but it's not useful by itself. We need to get the right way to squeeze
*  the information out of the data. Yeah, it's not useful by itself. And it's also not necessarily
*  clear to me that it's necessarily, that what we are able to measure easily is what the system
*  actually cares about. Sure. Right? And so, you know, one can imagine measuring many, many things,
*  and at the end of the day, it's really a low dimensional set of interactions that govern what
*  a cell is going to do. And everything else is a consequence of that that we're measuring. And so,
*  trying to identify which are the state variables that the system actually cares about, I think,
*  is a massive challenge. Yeah. And so, in my language, we're able to measure a lot of things,
*  but what should we be paying attention to? Exactly. So, in my language, it's all about
*  coarse graining and emergence, right? I mean, in a physics system, my favorite example is in the
*  earth, there's 10 to the 50th atoms. And to figure out how the earth orbits the sun, we don't need to
*  know what those atoms are doing. We just need to know a small number of variables, the center of
*  mass and the velocity. But the point is that in physics, it's kind of obvious what we need to know,
*  and that happens to coincide with what we can easily measure. In biology, everything is always
*  much more complicated. Yeah. So, your lab, if you were to explain your lab to a stranger on the
*  street, what exactly are you trying to figure out? Ah, everything. No. So, my interest is really in
*  how living systems self-organize. And I approach this problem from a purely computational point of
*  view. So, we collaborate extensively with experimentalists who ask interesting biological
*  questions and produce data and can then test our models, but we do not do that directly.
*  But that gives me a certain amount of flexibility in the types of things that I study. So,
*  if you think about living systems, they exhibit these beautiful self-organized structures and
*  processes at every single scale. At the molecular level, proteins assemble into macromolecular
*  complexes that carry out certain functions. The cells are arranged into tissues with very,
*  very reliable patterning. Those tissues interact in a multicellular organism to enable it to live
*  and move and do all of the things that it does. The organisms themselves interact in ecological
*  networks and in societies. And so, what gives rise to all of those dynamics is really a mystery that
*  I'm absolutely passionate about solving. And I've made very little headway, but I am struck by the
*  fact that we're now at a point where data collection is easy, relatively speaking, and computational
*  power is plentiful. And so, we can start to scratch the surface of those questions.
*  You're young. You have plenty of time to answer these questions. We have great expectations here.
*  But am I getting the impression that you are a more or less theoretical biologist in the same
*  sense that I'm a theoretical physicist? Yeah. I was actually trained as a theoretical physicist.
*  And I drifted into biology because I was interested in complex systems. And living systems were the
*  most compelling example of complex systems that I could find. So, I slowly got drawn over to
*  questions in biology, but my training is purely theoretical. How far? All the way up to the PhD?
*  Yeah. My PhD is in theoretical physics. This is hilarious. So, I have to promise the audience I
*  did not know that because again and again, I have guests on Mindscape and they reveal halfway through
*  that, oh yeah, I was a physics undergraduate or whatever. And they're studying political science
*  or sociology or economics. Okay, I get it. It makes sense to me now why you think that way.
*  But it's funny because as a biology professor, you still have a lab even though you're a theorist.
*  Yeah. I mean, it's a dry lab, right? So, all of our experiments are in silico and we work really
*  closely with the experimentalists who I collaborate with. Students who work with me often spend time
*  in the wet lab of my collaborators. I definitely did that as well when I was
*  making my transition into theoretical biology. And it's been a wonderful journey and it's been a
*  lot of fun to be working at that interface. It has its challenges, of course, right? We
*  were trained to think in different ways. We use different language to describe phenomena.
*  But at the end of the day, both me and my experimentalist collaborators are interested
*  in the same fundamental questions. And so, we're able to come together from those two perspectives.
*  In physics, of course, it's a well-established idea that we have theorists, we have experimentalists,
*  we hire both or whatever. Do your biology colleagues look at you slightly askance as
*  someone who does not ever get their hands wet? Yes, but I think that's changing, right? I think
*  in part because of this revolution in molecular biology, there has been a realization that
*  the ways in which we think about biological systems and try to make the links between
*  the microscopic and the macroscopic, it requires different sorts of perspectives.
*  And so, I think I see an increase in the diversity of approaches that biology departments take,
*  and mine is certainly one of them. So, I think that sort of looking askance or that skepticism
*  of non-wet biology research is diminishing as its power is sort of revealed.
*  Good to know. And I was amused on your website to see the word omics used as a, I don't know,
*  back construction from there are things called genomics and proteomics and metabolomics and so
*  forth. So, we just lump them together and call them all omics. Maybe explain to the audience what
*  that is. Yeah. So, if you think back to what we're all taught as the central dogma of molecular
*  biology, right? You have a genome, it's encoded in DNA. Those genes are comprised of some sequence
*  of bases that code for a protein at the end. But there's an intermediate step where the gene is
*  transcribed into mRNA and then the mRNA is then translated into protein. And about 20 or more
*  years ago now, there was a development of microarray technology. And what this technology
*  was designed to do was to simultaneously assay genome-wide the abundances of all of the mRNAs
*  in a given sample. So, the idea is this. You have a gene, it codes for a protein, but how much of
*  that protein is produced depends on how many copies of that gene are made in mRNA. And so,
*  if you can measure how many copies of mRNA you have for that particular gene, you can use that
*  as a proxy for how abundant that protein is and maybe then as a proxy for how much of the function
*  that that protein carries out is actually being carried out in your sample. Previously, the way
*  that mRNA abundance was assayed was one gene at a time. And microarrays enabled us to do this for
*  10,000 genes at a time. And so, now you get this incredibly rich snapshot of gene expression for
*  nearly every gene in the genome. And so, that was referred to as genomics and transcriptomics,
*  since we're looking at the transcript level. And you can also look at gene sequences. And so,
*  that's really when we talk about, sometimes genomics is used as a catch-all term, but if we're being
*  really, really specific about it, the genomics refers to the sequence of the DNA and how much
*  yours might vary from mine or two different organisms from one another or cancer cell from
*  a healthy tumor cell. The transcriptomics is kind of the next layer up in the regulation,
*  how much of the mRNA is produced. Proteomics looks directly at the protein abundances
*  and so on and so forth. And we can do all of these things now in high throughput, right? So,
*  it's not just mRNA. We can do it at the genome level. We can do it at the protein level.
*  We have now next generation sequencing technology. So, nobody is using microarray anymore. They're
*  all doing sequencing, which means that we can really look in detail across the entire genome
*  of what a given sample is doing. Yeah. I guess this is the point where I ask my
*  favorite question to ask biologists, which is, what is a gene? In DNA language, right? I mean,
*  it seems to be some functional unit of the DNA, but maybe the boundaries are a little fuzzy and
*  people disagree. The boundaries can be a little fuzzy. So, a given region of the genome can code
*  for different isoforms of the gene, right? So, it could be truncated in different places. Okay. It
*  could be spliced in different ways. And which of those isoforms is actually expressed by a cell
*  can change under different circumstances. So, for example, we know of particular genes where,
*  depending on the temperature, a different isoform of that same gene is expressed. And because you
*  have a different isoform, you have a slightly different protein, or perhaps you have the same
*  protein, but it has different regulatory properties. So, it might be easier to interact with by some
*  other regulatory element. So, it is fuzzy in that sort of way, right? We're taught to think of
*  genes and proteins and enzymes as these highly specific entities, right? When you're in your
*  first biology class in high school or in college, you're kind of taught this lock and key
*  model for how proteins interact with one another. And it turns out that that's not really the case,
*  right? There's a lot of non-specificity and promiscuity in the binding of proteins to one another
*  and what regulatory elements are targeted by which regulatory proteins. And so,
*  nailing down what a given gene does can be challenging. And I think, to be honest,
*  it's something that I'm actually a little bit opposed to in the sense that I think that
*  making this assumption of specificity and of this lock and key mechanism,
*  I don't think it's borne out by the data. And I think that if you do an analysis,
*  with that assumption, you limit the types of things that you're able to discover.
*  HOFFMAN It's interesting because we've long ago gotten rid of the idea of intelligent design.
*  We know that these biological organisms evolve through natural selection, but also, again and
*  again, we come across a situation just like when he said where we have an explanation or an account
*  of something and then we realize it's not quite that simple or it doesn't work in quite that way.
*  And I wonder how much of that is because we sort of have an intuition that grows up from
*  designed systems where if there's a part, it has a purpose and there's a clear thing that it does.
*  But because all the stuff that we see in biological organisms have just sort of come about because
*  the whole system was successful, the boundaries are not always so clear in biology.
*  BOWEN Yeah, absolutely. And I think that one could make energetic arguments for
*  proteins having multiple functions, right? Then you only need to make one of them to carry out
*  multiple things. I think that one can also make probabilistic arguments for why that may be the
*  case in the sense that having a multifunctional protein allows you to do a little bit of bet hedging.
*  I'm saying this kind of as a conjecture when it comes to proteins. We had this pair of papers
*  with my former student, Gary Wilk, where we looked at the role of microRNAs, which are small,
*  non-coding RNA molecules. And there we know that their role in binding and regulating genes is
*  pretty promiscuous. So if you'd like, I can elaborate on that.
*  BOWEN Please.
*  So microRNAs are short, non-coding RNA molecules, six to eight bases long. So very, very short.
*  And they bind to mRNA molecules, which code for specific genes and proteins. And they either
*  inhibit the production of the protein by being bound to the mRNA molecule, or they trigger the
*  degradation of the mRNA. In either case, the end result of the microRNA binding to the mRNA is that
*  it down regulates the production of the targeted protein. But I told you that that microRNA is very,
*  very small, only six to eight bases. And so it could bind many, many, many genes, right? That's
*  a very short sequence, which it might bind to. And so a given microRNA may have many mRNA targets,
*  and a given mRNA, because it's hundreds, possibly thousands of bases long, might be targeted by
*  multiple microRNAs. So there's a many to many relationship between the microRNAs and their
*  targets. And so this kind of flies in the face of that assumption that we're kind of taught
*  early on, which is, you know, the sort of one to one, it does one thing very mechanistically.
*  And so we wanted to ask the question, well, why would you produce a regulatory molecule,
*  a microRNA that is completely nonspecific in its binding, right, where it might have possibly
*  hundreds of targets? And we thought, well, one reason you might want to do such a thing,
*  or evolve such a mechanism, is as a way to exert systems level control over an entire process,
*  by redundantly targeting different elements of that system, right? So that if the microRNA doesn't
*  bind to one particular mRNA, maybe it binds to the mRNA of different gene. And it doesn't matter
*  which one it's hit, the whole system as a whole is down regulated. And so what Gary and I did was
*  to look for statistical evidence of this type of systems level control in TCGA, which is the
*  Cancer Genome Atlas. And it's a repository of one of those giant genomics projects, thousands upon
*  thousands of samples, and each of them has DNA data, mRNA data, microRNA data, proteomic data,
*  etc. So it's a wonderful wealth of data. And so what we wanted to know was, do we see evidence
*  of the systems level control if we look in this data? The way that we did that was to say, okay,
*  if a microRNA targets a particular gene, then we expect that when the microRNA abundance goes up,
*  the abundance of the target RNA will go down. We know that if you look at particular microRNA gene
*  pairs, that's not really born out. So you don't always see that at the single gene level. But what
*  if we were to take all of the genes that we know to play a role in a particular biological function
*  in a particular pathway, and we summarize in some statistical way, the expression level of all of the
*  genes in that pathway, and use that as a coarse-grained measure of how active that pathway is?
*  Can we then identify particular microRNA pathway pairs where as the microRNA goes up,
*  the pathway activity, summarized through nonlinear dimension reduction of the gene expression,
*  goes down? And in fact, we were able to identify exactly that.
*  And is this an example of the circuits that you talk about? We use this language of
*  circuitry, right, of nodes and networks and things connecting them. So rather than saying,
*  putting your finger on a certain mRNA and saying, here's what it does, you say,
*  here's all the flow of different things. You talked about channels, I guess,
*  and here's how it all adds up to some collective behavior.
*  Yeah. So in that particular paper, we just treated the pathway, not as a network,
*  but just as a collection of genes. But now in kind of work that's grown out of that,
*  as well as some other studies, now we're starting to take into account what we think is the wiring
*  diagram. And I'm making air quotes, although your listeners cannot see them, but the wiring
*  diagram of these pathways. So that's a network of putative interactions between the genes or
*  the gene products really, that carry out some particular biological function. And the reason
*  that I put air quotes around it is that what we know of those wiring diagrams is incomplete,
*  right? We don't know all of the interactions just because we haven't discovered them all yet.
*  We obtain those wiring diagrams, those pathway networks from databases, which inevitably will
*  have some errors. And again, there's this issue of probably any given element has more than one
*  role. Maybe we haven't discovered all of them yet. So it may be that those networks are sparser
*  in the database than they are in reality. But it gives us a starting point for trying to understand
*  what is connected to what and what the flow of information or the flow of a signal through this
*  collection of genes might be. And is there some hope that, or maybe it's already true, I don't know,
*  that we achieve a complete list of all the circuits, of all the networks that are relevant,
*  or are there completely different kinds of circuits we're talking about and one person's
*  circuit is another person's noise? I'm not sure. That's a really great question.
*  Whenever somebody asks, is there hope? My impulse is to say, yes, of course, of course there is.
*  But I think it's actually quite a challenging problem. So there's this big problem of how do
*  you discover those wiring diagrams or those networks. And now because we have so much
*  omics data, one could say, okay, well, what we'll do is we'll go to that omics data and we will look
*  for patterns of correlation in that data. And from those correlation patterns, we will infer
*  some sort of network structure. And we've made a little tiny bit of progress on that, but not
*  very much. And not very much because at the end of the day, it's at this point a pretty grossly
*  under-determined problem. In that the number of interactions that one could have amongst the
*  things that we are measuring is much larger than the number of observations that we've collected.
*  Gotcha. So as far as hope is concerned, sure, but we're not at the level now where everyone agrees
*  on what the circuits are in the same way they agree on what organs we have in our body.
*  Yeah.
*  Good. And it reminds me a little bit, I hadn't thought of this until just now, of we had Judea
*  Pearl on the podcast talking about causal networks, right? He's more thinking of social science or
*  medicine, what kind of interventions can have a good outcome. When you draw your little diagrams,
*  do you imagine asking questions about what causes what? What node in the diagram has a causal
*  influence on the behavior of what other nodes? So yeah, I think that's at the end of the day,
*  that's what we'd like to understand from these systems. From my perspective,
*  I'm interested less in what causal effect does one node have on what other node, and more about
*  what causal effect does one node have on the behavior of the system as a whole? So if a
*  particular node were subject to mutation, what would that mean for the dynamics of the entire
*  network, right? How robust is the network to damage in particular regions? If I recover some
*  coarse-grained statistical property of that network, is that enough to recover its functional
*  behavior, or do I need to recover every node and every edge in detail?
*  And maybe this is a slightly askew question, but is there a sharp, bright line between
*  biological networks of this form and other possible chemical reaction networks? Are there things that
*  we see in the biological context that we just don't see elsewhere?
*  I mean, these networks are intended to represent possible biochemical or biophysical interactions
*  between molecules, and so in that sense, I think you can think of them as a chemical
*  interaction network as well. Okay, but do we in nature but not in biology, and things that happen
*  outside nature, do we see reaction networks of this richness and depth, or is biology special
*  if only because it's more complex than other things? I mean, biology is special in terms of
*  its complexity, in terms of its complicatedness, in terms also in the fact that it is far from
*  equilibrium. Of course, yes. Right? And it's adaptive, right? So those networks are not
*  necessarily constant in time. Good. I mean, biology is simultaneously not in equilibrium, but
*  almost in a steady state for some purposes, right? I mean, in stat mech, we talk about non-equilibrium
*  steady states sometimes. Right, yeah. And yeah, I would say that the analogy works in biology.
*  And I think that's one of the great mysteries, right? We have incredibly reliable phenotypes.
*  If you think about organismal development, it's astonishingly reliable despite environmental
*  variation, despite genetic variation. Occasionally, things can go wrong, but by and large, despite all
*  of these sources of variation and fluctuations, it's extremely reliable. To me, that says that
*  there's a wide basin of attraction. Right? And so I think that's part of why I'm very motivated to
*  take these systems and network views in that to have a wide basin of attraction, it means that
*  the system is not fine-tuned. Fine-tuned would suggest that there's a very, very narrow range
*  of the state space that leads to a particular outcome. And if it's not fine-tuned, then I think
*  it has to all be systems level effects. Well, it goes hand in hand with what we said before.
*  Mechanical things tend to be brittle, right? You break a single wire and your computer doesn't work,
*  but biology has to be a little resilient. Yeah. Good. Yeah. Okay. So that was thank you for
*  indulging me those more semi-philosophical questions. Let's get back down to the nitty gritty
*  of what you do because like we said before, these networks are complicated, a lot of data in here,
*  a lot of things going on. Computers are going to certainly play a role in your analysis, but also
*  machine learning or what these days we're supposed to call AI, I'm sure plays an important role.
*  Yeah. So we do quite a lot of that. And I think we've seen a huge revolution in machine learning
*  and statistical learning techniques are incredibly powerful. The computers are now incredibly
*  powerful. And so you can do things now that were impossible five, 10 years ago. The data sets are
*  very large, albeit still not large enough for deep learning to be as effective as I think we would
*  like to be. But I think also that there's a little bit of a danger in just taking the wealth of data
*  that we've collected and generic in some sense, machine learning algorithms and pushing the data
*  through and crossing your fingers and hoping that something of value is discovered in a naive way.
*  We already know a lot about biological systems. So for example, let's think about this problem of
*  inferring interaction networks or pathways. We already have some information about which genes
*  code for proteins that act as transcription factors and would therefore regulate by binding
*  to the DNA the expression of other genes. So we know something about the biochemistry
*  of these elements. Simply taking the correlation structure and the data, pushing it into a machine
*  learning model and saying, okay, can you give me a minimal network without taking into account
*  that biochemical information seems to me to be a little bit naive, right? Like we're not using
*  what we already have. And so one of the things that my group is very interested in is are there
*  ways to integrate the information that we already have, even though it might be incomplete or
*  somewhat erroneous, into the machine learning methods that we are using to make new discoveries.
*  So that's very interesting. But let me bring up the fact that is also very interesting that
*  when we build chess or go playing machine learning systems, one of the great discoveries was don't
*  ruin it by giving it anything that a human being thinks is a good chess playing strategy. It's much
*  better to just let the computer play games against itself a gajillion times and figure things out for
*  itself than to give it any hints. So you're saying that maybe in biology it's different or that's a
*  hypothesis that we might shoot down? I mean, I think, well, first of all, I see no reason not to do
*  both, right? There's absolutely no reason not to take both approaches. I do think that trying to
*  understand what a cell or what a tissue is doing is perhaps a bit more complicated than learning
*  how to play Go or how to play chess simply because the number of components in this particular game
*  is much larger. And so if the goal is to search a space of possible states to find the ones that
*  correspond to a winning strategy in Go or chess or life, it might help to constrain your search
*  space a little bit if the number of players is very large. So are there intelligent ways to
*  constrain that space? You did bring up the number 20,000. What did that refer to? What are the 20,000
*  of? So that's the approximate number of genes that we obtain when we do gene expression profiling
*  in a human subject. It's different for different organisms. So some have more, some have less.
*  But in general, when you're doing transcriptomics for any given sample, and now we can do it at the
*  single cell level, so for any given cell, you're looking at 20,000 measurements. Is that 20,000
*  genes? Yeah, that's 20,000 distinct mRNAs. But is that, forgive me my complete ignorance here,
*  is that saying that the human genome contains 20,000 genes or is this a statement about our
*  ability to measure? It's both. Okay. And good, then now we can put it all together, right? So we have
*  20,000 genes or mRNAs and we collect a lot of data, an overwhelming amount of data. And as we said at
*  the very start, we're interested in this sort of emergent collective behavior, right? It's not just
*  20,000. It's 20,000 in some combinatorial array, right? Different genes play with each other in
*  different ways. So a huge number of possible things going on, but a relatively small number of things
*  actually do go on, and that's what the machine learning, for example, is trying to help us with.
*  Yeah, exactly. So I would say from a mathematical perspective, the way I would put it is that we
*  have observations in this 20,000 dimensional feature space, and we think that those observations
*  lie on a very low dimensional manifold within that 20,000 dimensional space. That not all
*  locations in that 20,000 dimensional space correspond to a system that can live, right?
*  And so the idea is, can we discover the geometry of that manifold? Can we then use it to say what
*  it means to have variation along a particular direction of that manifold? What does it mean to
*  deviate from that manifold? And can we use the location of an observation on that manifold to
*  say something about its behavior as a whole? Good. And I mean, you just asked a bunch of
*  rhetorical questions. How much progress has been made? Is this like brand new frontier, or do we
*  have our handles on a bunch of answers to some of the questions you just asked? I mean, yes and no,
*  right? So nonlinear dimension reduction and manifold learning has been a hot topic for
*  a while now. And so we have, you know, there have been many algorithms proposed, some of which
*  can be demonstrated to be equivalent to one another mathematically. In general, the idea
*  behind them is to use the local geometry of your observations to try to decide what is the surface
*  on which those observations lie, and then you go to the next local neighborhood, and you kind of
*  stitch them together like this patchwork. So that's the hand wavy description of them.
*  There are still some challenges, right? So one question that one can ask is, well, if you're
*  using the local geometry to decide where the manifold is in some region of this 20,000
*  dimensional space, how big of a local neighborhood should you take? And that question of scale
*  is one that is still in some sense unanswered. So how do you tune that scale? Should you be
*  looking at the same scale in every region of the data? If not, how do you tune it adaptively?
*  Probably not.
*  How do you tune it adaptively?
*  Okay, good. Yeah. Okay, so we see it coming. We're going to be able to
*  figure out what are the sort of relevant variables, the emergent coarse-grained
*  way of talking about all these things. What good will it do us? How does this help us understand
*  biology or, you know, cure disease or whatever it is you want to do?
*  I mean, I think the ultimate goal is if you have some understanding of the relationship between
*  proteins and genes and gene products, you might be able to make a guess as to what you could target
*  therapeutically. You might be able to develop better diagnostics. So I think that's the ultimate goal
*  is to have an understanding that would lead to the generation of new hypotheses that would
*  ultimately lead to better health outcomes. You know, one area in which we've been somewhat
*  successful, it's a pretty lofty goal, right? But one area in which we've made a little bit of
*  headway on that front has been in the work that I've done on circadian rhythms. And there's
*  abundant epidemiological evidence that suggests that the time of day that your body thinks it is
*  is absolutely crucial for how you metabolize food, how you metabolize drugs, whether it's aligned
*  with your environment turns out to be crucial in your risk for various diseases. And we don't
*  really understand fully the links between all of those things. But if we're able to measure
*  physiological time, then maybe we can use that measurement to inform things like when you should
*  take a blood pressure drug or when you should take, when chemotherapy should be delivered.
*  And so using multi-gene expression profiles to obtain a measure of physiological time was
*  one of the things that we worked on. And there we were somewhat successful with it. So that might
*  actually have some benefit within the near term, I'm hopeful. Let's actually dig into the circadian
*  rhythm stuff, because I will confess, as we are recording this podcast, yesterday I flew home
*  from England and I'm totally jet lagged. So this idea that, you know, what time of day I eat things
*  is going to... I mean, let me phrase it as a question. Are you saying that where I am
*  in my circadian rhythm, i.e. what time my body thinks it is, affects how I metabolize food?
*  Yeah, it affects how you metabolize food. And when you eat also affects your circadian phase,
*  right? So the circadian rhythm itself is a self-sustained 24-hour oscillation,
*  and so even in the absence of light and dark or other time-giving cues, you'll still roughly
*  have a 24-hour day. In humans it's a little bit longer than 24 hours, but it's still an approximate
*  24-hour rhythm. But as you are now experiencing, when those cues occur, your circadian phase will
*  shift. That takes some time, as you are now very abundantly aware, and it can be influenced by
*  light as well as by feeding behaviors. So when you eat can have a powerful effect on how quickly
*  you recover from jet lag. Eat in the morning is what I've been told. That was the next question.
*  Clinical and experimentalist collaborators, yeah. Eat in the morning even if you don't usually eat
*  in the morning? Apparently that is... So now this is not my direct line of research, but what I have
*  been told by my colleagues who study this is that yeah, so high calorie intake in the morning tends
*  to be a better phase resetting signal than eating at other times today. Light in the morning is
*  well understood to be a powerful phase resetting signal. I'll warn you ahead of time, we're going
*  to have this lovely conversation about networks and signals and gene expression and so forth,
*  and what people remember is eat in the morning to get over jet lag. That's what people remember.
*  Yeah. News you can use. I like that. But let's connect it back to what you're doing. So we have
*  because this is fascinating to me, we have all this molecular activity going on in our bodies,
*  and as a physicist I'm interested in how the time scales connect to each other. I mean ultimately
*  it's all chemistry in our bodies and chemical reactions happen relatively quickly. Like where
*  in our bodies does it know that the day is 24 hours long and that there should be cycles and
*  rhythms of that duration? So this is really, really fascinating. So nearly every cell in your body and
*  almost every living cell on earth, it's highly evolutionarily conserved, has a molecular
*  oscillator within an approximate 24 hour period. In mammals and fruit flies it's a transcription,
*  translation feedback loop. So essentially you have genes that are transcribed, they're then
*  translated into proteins. Those proteins then regulate the transcription of other genes that
*  are part of this feedback loop. And it's a negative feedback loop with time delays because
*  all of these steps take time and anytime you have negative feedback with time delays,
*  you can sustain oscillations. And so there is this core clock circuit in nearly every cell.
*  And this was a somewhat surprising discovery, the fact that it existed in every cell because
*  one could conjecture, well you only really need it in the brain and then the brain can control
*  everything else. And so the discovery that there are peripheral clocks was quite exciting.
*  And it raises some interesting questions like why would you produce a clock in every single cell?
*  And I have some hypotheses about that, one of which is that it's one way to allow processes to
*  be coordinated and orchestrated across a spatially extended system like you or me without direct
*  communication between the elements of that system. If you've got to watch and I've got to watch,
*  it's enough to say that we're going to meet to record a podcast. We don't need to be in
*  constant communication up until that point. And when you say oscillator, just because again,
*  physics training in me, I'm thinking of like a pendulum going back and forth, but you're
*  thinking of a little collection of chemical concentrations going up and down. Is that true?
*  Yeah, that's correct. So it's a chemical oscillator, not a mechanical one.
*  Correct. Yeah. And every cell within our bodies. I know you just said that and you even said that
*  it's amazing, but it's amazing. Yeah, very nearly. So there was a beautiful, beautiful study
*  done by John Hoganesh's lab a number of years ago. And it was called the Mouse Circadian Atlas.
*  Basically what they did was they took every single tissue in the mouse and they did time series gene
*  expression measurements for each of those tissues. And they discovered genes that were under
*  circadian control in every one of those tissues. And those genes included the core clock genes.
*  And let me home in on this particular question. Where does the number 24 hours come from?
*  Right? I mean, it must be that this particular oscillator is pretty darn tuned. Someone has
*  to design the clock in some way and chemistry, biology has figured out how to get this rather
*  long time scale to pop out of some very quick interactions. Right. So yeah, so this is obviously
*  something that has evolved on earth, right? With its 24 hour day. So there's reason to believe that
*  it's favorable to have a clock that would enable you to anticipate time of day. Right? But you
*  raised something really interesting and that's that it has this pretty robust 24 hour period.
*  What's curious about it is that it has this robust 20 approximate 24 hour period across a very wide
*  range of temperatures. And that's pretty surprising because we would expect that chemical reactions
*  are going to run faster at higher temperatures. And so the clock should speed up, but it doesn't.
*  It's temperature compensated. This is obviously very useful for a cold blooded organism, but also
*  for us, if you consider the fact that the temperature on your skin is very different
*  from the temperature in the core of your body, it's important to have them be at approximately
*  the same period. How temperature compensation is achieved is still not well understood.
*  Okay. And there's another wrinkle too. It's temperature compensated, but it's not temperature
*  insensitive. So fluctuations in environmental temperature can shift the phase of the clock.
*  So it's not just completely isolated somehow from thermal information,
*  but the period is compensated. You know, it's very similar in mechanical wristwatches, right? It's
*  very hard to make a watch that keeps the same amount of time, no matter what temperature it is
*  or other conditions. Absolutely. And in fact, you know, that was when Harrison was designing
*  his chronometers for the British Royal Navy. That was achieving temperature compensation was
*  a major challenge, right? Because if the clock on board your ship starts running faster or slower,
*  you can go off course. And then how does this little chemical oscillator in every one of ourselves
*  communicate with the rest of the world? For one, actually, let me back up. Cells are pretty tiny.
*  How is there room in a cell for this? And then how does it then connect to the rest of what's
*  going on in the cell and outside? I mean, cells are pretty tiny, but molecules are more tiny,
*  right? So, you know, the cell is a pretty densely packed environment. It's big enough to allow for
*  the expression of the core clock components. Sorry, does the clock literally have a size or
*  is it sort of diffuse? So these are chemical reactions, right? It's a chemical oscillator.
*  So we expect that those things are going to be diffusing and binding and unbinding, etc. Good.
*  Okay. And then how does it communicate elsewhere? Okay, that's a really good question. I don't have
*  an answer. I don't think we have an answer. So there are certain signaling molecules that we know
*  exist. So melatonin, for example, is produced by the brain a couple hours before you go to sleep.
*  It serves as a signal to other cells, right? And so that's one form of that communication.
*  There's obviously the nervous system, but the coupling between the various oscillators in the
*  various cells, we don't necessarily know what achieves that. There was some really interesting
*  work from Karen Esser's group in Florida, where they looked at phase resetting in mouse muscle
*  tissue when they changed when the mice were allowed to exercise, right? So the mice will run on a wheel
*  given the opportunity. And so basically they deprived the mice of the wheel at particular
*  times of day to see what that would do to the circadian phase of the muscle tissue.
*  To give them jet lag, basically. But nothing else was jet lag, right? So the light cues were the
*  same, feeding was the same. The only thing that they perturbed was when the mice could exercise.
*  And what they discovered was that exercise was a very powerful zeitgeber, a very powerful phase
*  resetting cue for the muscle clock, right? And so this raises the question of to what degree is it
*  actually the physical coupling between cells that might mediate the cell-cell coupling of the
*  oscillators? I do not know. I think those experiments still need to be done.
*  But that's so much fun. It's so easy in biology just to like bump up against fundamental things
*  that are easy to ask and we don't know the answer to. So the oscillators are keeping track. It sounds
*  like a fairly simple thing. Like an oscillator is literally the simplest possible physics system.
*  But before we were talking about these very complicated chemical networks, is there a
*  connection there or is the oscillator part of the network or is an oscillator secretly much
*  more complicated than I think it is? So the oscillator is part of the network in the sense
*  that there are many genes that are under circadian control. So those core clock components, right,
*  are transcription factors that then regulate the expression of hundreds, maybe even thousands of
*  genes downstream. So that mouse circadian atlas paper that I mentioned from Hoganesh's group
*  earlier, what they found was that nearly half of the mouse genome was under circadian control in
*  some tissue, right? So it wasn't nearly half in any given specific tissue, but if you look across
*  the mouse as a whole, nearly half. And so that suggests that the clock is playing a significant
*  role in a variety of biological processes. What we've seen in our research in collaboration with
*  Ravi Allada's group here at Northwestern is that the clock is crucial to metabolism and to lifespan
*  and to egg laying in fruit flies. So you can do these experiments that Ravi has done where you
*  take a fruit fly and you subject it to lower temperatures or to dietary restriction. So you
*  deprive it of some calories without starving it. And a normal fly, when subjected to these
*  slightly unfavorable conditions, actually does something a little bit unexpected. It lives
*  longer. So dietary restriction usually results in lifespan elongation. Lower temperature also
*  results in lifespan elongation in the fruit fly. And you can come up with all sorts of
*  theories and just-so stories about why that might be like, you know, total energy consumed
*  over the lifespan or something like that. It turns out that in order to observe that lifespan
*  elongation, the fruit fly needs an intact clock. If you knock out one of the core clock components
*  by mutating a gene, helpfully known as clock, you get an arrhythmic fruit fly. And that fruit fly
*  has the same approximate lifespan regardless of the calories that it has available to it.
*  And so it seems that there's not only hundreds, possibly thousands of genes that are under
*  circadian control, but which genes are under circadian control has a big influence on these
*  macroscopic outcomes that we're able to observe.
*  You know, one of the very first podcasts I did was with Colleen Murphy of Princeton who studies
*  aging. And it's interesting, like, yeah, you knock out some genes, things like that, our
*  life expectancy changes, or not ours, but you know, they're using nematodes. Does this kind of thing
*  open up prospects for dramatically changing human lifespans if we were to understand these
*  networks better? Go ahead, it's late in the podcast, you're allowed to speculate a little bit.
*  I mean, I would love to say yes. I think that that's a hard question to answer yes or no to.
*  I will say this, something that has long been observed is that there are sleep and circadian
*  disruptions that are associated with neurodegeneration and circadian patterns to
*  symptoms in neurodegenerative diseases like Alzheimer's. And so one of the things that we are
*  looking at now is what are the patterns of circadian gene expression that are associated
*  with healthy aging versus people who have preclinical and clinical Alzheimer's disease?
*  And so hopefully that research will give us some insights as to the links between
*  circadian rhythms and at least healthy aging. I don't know about lifespan.
*  Okay, fair enough. I would like to be healthy for a long time too. That's also a goal.
*  Let me dramatically oversimplify here so that you can tell me if I've gotten the gist of it.
*  The circadian rhythm, we all know that we get tired at a certain time of day,
*  we get hungry at a certain time of day, jet lag affects us, etc. But the impression I'm getting
*  from what you're saying is that in some sense, like all or many, some large fraction of our
*  internal biological processes are just different at different times of day. They're being regulated
*  differently. It goes back to what you said, how we metabolize food is different during different
*  types of day. And I'm sure that when we're asleep versus when we're awake. So we're kind of like
*  we're every human being, every organism is a complicated chemical reaction, but we're
*  different chemical reactions depending on what time it is.
*  Yeah, yeah. And that's precisely why when we were talking earlier about
*  what makes biological networks special in some way, I mentioned that these networks aren't
*  necessarily static over time. Which components of those networks might be expressed can differ
*  over the course of the day. And so the behavior of those networks might differ over the course.
*  So it's kind of like, just coming up with trying to simple analogies here,
*  traffic flow patterns in a city are very different at 8am and 5pm.
*  Absolutely. Yeah.
*  And it's all and this gives one hope that there really is something called
*  complex systems science, because these systems do have some commonalities in there.
*  Or is that going too far? Are there laws of complexity? Is the fact that a system is complex,
*  whether it's a city or a human being, give us any shared insight there? Or do complex systems have
*  the features that every complex system is different? So, you know, have fun, but don't expect to share
*  insight between different modes. I think that insights that can be shared across modes is the
*  approach that we use to investigate them. Right. So one thing that is in common amongst all of these
*  complex systems is that a reductionist point of view where the elements that you are reducing to
*  are defined at the very outset, right? Like here are my cars, here are my jeans. Going to look at
*  specific elements is maybe not fruitful, right? You need to consider the behavior of the system
*  as a whole and coarse-grained. So I think that those types of insights are the same, whether
*  you're talking about traffic flow through a city or information flow through a cell.
*  In biology in particular, there's a temptation to be a little bit too reductionist, right? I mean,
*  not as a professional biologist, but in the popular discourse about biology,
*  oh, we found the gene that explains X. I think it's a temptation just because of the way that
*  we're kind of taught to think about these things. But I think there's also a reason that we tend to
*  go in that direction, and that's that we know how to do experiments on particular genes. We
*  know how to target particular molecules. When I go back to my experimentalist collaborators and I
*  say, good news, I found a pathway that is associated with the phenotype you're interested in,
*  and this pathway contains 600 genes, they tell me to get out of their lab, right? Like there's
*  nothing they can do with that. You need to be able to narrow it down to something that is
*  that is targetable. And I think that there's a tension there between acknowledging that
*  what is driving the outcomes of a particular cell or a particular organism
*  is a systems level property versus what specific element of that system can I
*  target to produce an effect that I want to see.
*  Right.
*  Good. So maybe in other words, part of what you've emphasized is this sort of coarse graining,
*  looking for a low dimensional manifold, looking for a small number of
*  collective coordinates that help explain what's going on. And then the next thing is to be
*  interventionist about it, to say, okay, how do you poke at it to get some outcome that you desire?
*  Right.
*  And is that, I mean, I'm not quite sure whether that's supposed to be just a cautionary tale,
*  don't expect too much or, oh, yes, that's what we're figuring out. We're going to figure out
*  exactly how to poke at things and, you know, make us live forever in Kierke-Hansser. I don't want to
*  I mean, yes, no, I think that there is hope there. So one of the things that we're really interested
*  in now is, so suppose that you have some sort of wiring diagram or some sort of network and
*  you have measured the abundances of the mRNAs for the nodes in that network, or you've measured the
*  correlation between the gene expression for all of the edges in your network. And so now you can
*  use that network picture to start to make statistical summaries of the network. Right.
*  So I can coarse grain that data on that network. And I can do that sort of coarse graining
*  with different data sets. So you can imagine I do this coarse graining with
*  tumor and I do it with normal samples. Right. And so now I can identify statistical differences
*  at the whole network level between my cancer samples and my normal samples.
*  And then one can ask the following question. So those coarse grained statistical differences
*  are obviously due to local differences in particular nodes and particular edges. Right.
*  I could recover the statistical properties of the normal network by changing all of the altered
*  nodes and edges that were altered in my cancer sample. But also there may be other ways to do so.
*  Right. So one can ask what is the minimal number of edges that I would need to alter
*  in my cancer sample in order to recover the statistical properties of the normal sample,
*  but without recovering that network in detail. And now I have maybe a smaller number of nodes
*  and edges that I can then go and target experimentally. So I think there are ways to
*  to bridge that gap. I think also that one can ask a slightly different question, which is
*  recovering the statistical, those coarse grained statistical properties enough. And those statistical
*  properties of the graph, I can look at the entire eigen spectrum of the graph with Lausian. Right.
*  Chances are that entire eigen spectrum does not actually capture all the biological information
*  of consequence. Probably it's just the leading eigenvalues. Right. So how much of those leading
*  eigenvalues would I need to recover in order to recover the function of the network?
*  I know it's getting late, but I will ask whether or not you think it's possible to explain to the
*  audience what in the world you're talking about, about eigenvalues of a graph and looking at the
*  eigen spectrum of a graph and looking at the leading eigenvalue. I think I know,
*  but I don't want to presume. And maybe the answer is they should read a linear algebra book. I'm not
*  sure. Yeah. No. So it's a way to describe the coarse grain geometry of the graph. So the first
*  eigenvalue and its associated eigenvector describes the smoothest pattern of variation across the
*  network. So if you have a network with two large communities that are only slightly,
*  very tenuously connected to one another, then that smooth vector on the graph would have
*  one community having very high values, the other one having low values. Right. And then you can
*  imagine increasingly less smooth patterns on the graph. And chances are, at least I would say,
*  that those coarse geometric descriptions of the graph probably represent the flow of information
*  in some coarse grained way that is biologically meaningful. So maybe we only need to look at the
*  first few of the smoothest patterns on the graph in order to understand what the graph itself is
*  doing. Good. You did it. I'm very impressed. Yeah, I know it is hard, but I mean, it's basically,
*  in some sort of overly literal sense, the graph is every single node and every single
*  edge between them. But what you're saying is that there are these coarse features of what the graph
*  looks like that you can mathematically characterize, and maybe that's all you need to know without all
*  the details being relevant. Yeah. So my last question, and this might be a completely unfair
*  one, you can be honest with me here. When we were talking about how to focus the conversation
*  before we started, I brought up the phrase rules of life, because it appeared on your web page or
*  something like that. And your response was, that's not my phrase, that's the National Science
*  Foundation's phrase. And so is it, which is fine, we all need to be nice to the National Science
*  Foundation. But is it just a kind of sexy thing that we talk about rules of life so that we can
*  get funding? Or is the concept of rules of life a reasonable one to help us contemplate future
*  research directions? No, I think it is a useful concept. So the way that NSF thinks about it,
*  and the way that I think about it as well, is we need some way to map between these microscopic
*  things we are able to measure, all of that omics data, and the macroscopic things that we observe,
*  like whether or not a cell is cancerous, or whether an organism is a mouse or a frog.
*  And so the idea behind rules of life is that there are some constraints or some organizing
*  principles that enable you to go from that microscopic description to that macroscopic
*  description. And the problem is discovering what those are. So what exactly dictates the
*  relationship between the microscopic and the macroscopic, and what constrains it?
*  So for me, when I am thinking about, well, I want to discover this low dimensional manifold
*  on which my observations lie, one of the questions that one can then ask is, well, why are things
*  constrained to that manifold? And you can think of that as being one of those rules of life.
*  It will never quite be laws of physics, but it will give us some insight that we can tell ourselves
*  about. Yes. That's great. What more can we ask for than that? So Rosemary Brown,
*  thanks very much for being on the Mindscape Podcast. Thank you so much for having me. It's been fun.

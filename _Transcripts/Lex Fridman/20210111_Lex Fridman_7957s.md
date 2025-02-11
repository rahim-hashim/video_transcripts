---
Date Generated: April 13, 2024
Transcription Model: whisper medium 20231117
Length: 7957s
Video Keywords: ['dmitry korkin', 'artificial intelligence', 'agi', 'ai', 'ai podcast', 'artificial intelligence podcast', 'lex fridman', 'lex podcast', 'lex mit', 'lex ai', 'lex jre', 'mit ai']
Video Views: 117472
Video Rating: None
---

# Dmitry Korkin: Evolution of Proteins, Viruses, Life, and AI | Lex Fridman Podcast #153
**Lex Fridman:** [January 11, 2021](https://www.youtube.com/watch?v=I51DuprOb0o)
*  The following is a conversation with Dmitry Korkin, his second time in the podcast.
*  He's a professor of bioinformatics and computational biology at WPI,
*  where he specializes in bioinformatics of complex disease,
*  computational genomics, systems biology and biomedical data analytics.
*  He loves biology.
*  He loves computing.
*  Plus, he is Russian and recites a poem in Russian at the end of the podcast.
*  What else could you possibly ask for in this world?
*  Quick mention of our sponsors.
*  Brave browser, NetSuite business management software,
*  Magic Spoon, low carb cereal and 8 Sleep self cooling mattress.
*  So the choice is browsing privacy, business success, healthy diet
*  or comfortable sleep.
*  Choose wisely, my friends.
*  And if you wish, click the sponsor links below to get a discount
*  and to support this podcast.
*  As a side note, let me say that to me, the scientists that did the best
*  apolitical, impactful, brilliant work of 2020 are the biologists
*  who study viruses without an agenda, without much sleep, to be honest,
*  just a pure passion for scientific discovery and exploration
*  of the mysteries within viruses.
*  Viruses are both terrifying and beautiful, terrifying
*  because they can threaten the fabric of human civilization,
*  both biological and psychological.
*  Beautiful because they give us insights into the nature of life on Earth
*  and perhaps even extraterrestrial life of the not so intelligent variety
*  that might meet us one day as we explore the habitable planets
*  and moons in our universe.
*  If you enjoy this thing, subscribe on YouTube, review it on Apple Podcasts.
*  Follow on Spotify, support on Patreon or connect with me on Twitter at Lex Friedman.
*  And now here's my conversation with Dmitry Korkin.
*  It's often said that proteins and the amino acid residues
*  that make them up are the building blocks of life.
*  Do you think of proteins in this way as the basic building blocks of life?
*  Yes and no.
*  So the proteins indeed is the basic unit,
*  biological unit that carries out important function of the cell.
*  However, through studying the proteins and comparing the proteins
*  across different species, across different kingdoms,
*  you realize that proteins are actually much more complicated.
*  So they have so-called modular complexity.
*  And so what I mean by that is an average protein
*  consists of several structural units.
*  So we call them protein domains.
*  And so you can imagine a protein as a string of beads
*  where each bead is a protein domain.
*  And, you know, in the past 20 years,
*  scientists have been studying the nature of the protein domains
*  because we realized that it's the unit.
*  Because if you look at the functions, right,
*  so many proteins have more than one function.
*  And those protein functions are often carried out by those protein domains.
*  So we also see that in the evolution,
*  those proteins, domains get shuffled.
*  So they act actually as a unit.
*  Also from the structural perspective, right?
*  So, you know, some people think of a protein as a sort of a globular molecule.
*  But as a matter of fact, the globular part of this protein is a protein domain.
*  So we often have this, you know, again,
*  the collection of this protein domains align on a string as beads.
*  And the protein domains are made up of amino acid residues.
*  So we're talking, so this is the basic.
*  So you're saying the protein domain is the basic building block of the function
*  that we think about proteins doing.
*  So, of course, you can always talk about different building blocks.
*  There's turtles all the way down.
*  But there's a point where there is at the point of the hierarchy
*  where it's the most the cleanest element block
*  based on which you can put them together in different kinds of ways
*  to form complex function.
*  And you're saying protein domains.
*  Why is that not talked about as often in popular culture?
*  Well, you know, there are several perspectives on this.
*  And one, of course, is the historical perspective, right?
*  So historically, scientists have been able to structurally resolve
*  to obtain the 3D coordinates of a protein for smaller proteins.
*  And smaller proteins tend to be a single domain protein.
*  So we have a protein equal to a protein domain.
*  And so because of that, the initial suspicion was that the proteins,
*  they have globular shapes.
*  And the more of smaller proteins you obtain structurally,
*  the more you became convinced that that's the case.
*  And only later when we started having, you know, alternative approaches.
*  So, you know, the traditional ones are X-ray crystallography and NMR spectroscopy.
*  So these are sort of the two main techniques that give us the 3D coordinates.
*  But nowadays, there is a huge breakthrough in cryo-electron microscopy.
*  So the more advanced methods that allow us to, you know,
*  to get into the 3D shapes of much larger molecules, molecular complexes,
*  to give you one of the common examples for this year, right?
*  So the first experimental structure of a SARS-CoV-2 protein
*  was the cryo-EM structure of the S protein, so the spike protein.
*  And so it was solved very quickly.
*  And the reason for that is the advancement of this technology is pretty spectacular.
*  How many domains does the...
*  Is it more than one domain?
*  Oh, yes. Oh, yes.
*  I mean, it's a very complex structure.
*  And we, you know, on top of the complexity of a single protein, right?
*  So this structure is actually a complex, it's a trimer.
*  So it needs to form a trimer in order to function properly.
*  What's a complex?
*  So a complex is agglomeration of multiple proteins.
*  And so we can have the same protein copied in multiple, you know,
*  made up in multiple copies and forming something that we call a homo-oligomer.
*  Homo means the same, right?
*  So in this case, the spike protein is an example of a homo-trimer.
*  So it needs three copies of a trimer in order to...
*  Exactly.
*  We have these three chains, the three molecular chains coupled together
*  and performing the function.
*  That's when you look at this protein from the top, you see a perfect triangle.
*  But other complexes are made up of different proteins.
*  Some of them are completely different.
*  Some of them are similar, the hemoglobin molecule, right?
*  So it's actually a protein complex.
*  It's made of four basic subunits.
*  Two of them are identical to each other and two other are identical to each other,
*  but they are also similar to each other,
*  which sort of gives us some ideas about the evolution of this molecule.
*  And perhaps one of the hypotheses is that in the past, it was just a homo-trimer, right?
*  So four identical copies, and then it became sort of modified.
*  It became mutated over the time and became more specialized.
*  Can we linger on the spike protein for a little bit?
*  Is there something interesting or beautiful you find about it?
*  I mean, first of all, it's an incredibly challenging protein.
*  And so we, as a part of our sort of research to understand the structural basis of this virus,
*  to sort of structure decode every single protein in its proteome,
*  we've been working on the spike protein.
*  And one of the main challenges was that the cryo-EM data allows us to reconstruct
*  or to obtain the 3D coordinates of roughly two thirds of the protein.
*  The rest of the one third of this protein, it's a part that is buried into the membrane
*  of the virus and of the viral envelope.
*  And it also has a lot of unstable structures around it.
*  So it's chemically interacting somehow with whatever the hex is connecting to.
*  Yeah, so people are still trying to understand the nature and the role of this one third.
*  The top part, the primary function is to get attached to the ACE2 receptor, human receptor.
*  There is also beautiful mechanics of how this thing happens.
*  Because there are three different copies of these chains, there are three different domains.
*  So we're talking about domains.
*  So this is the receptor binding domains, RBDs, that gets untangled and get ready to get attached
*  to the receptor.
*  Now, they are not necessarily going in a sync mode.
*  As a matter of fact-
*  They're synchronous?
*  So, yes.
*  And this is where another level of complexity comes into play.
*  Because right now what we see is we typically see just one of the arms going out and getting
*  ready to be attached to the ACE2 receptors.
*  However, there was a recent mutation that people studied in that spike protein.
*  And very recently a group from UMass Medical School, we happened to collaborate with groups.
*  So this is a group of Jeremy Luban and a number of other faculty.
*  They actually solved the mutated structure of the spike.
*  They showed that actually because of these mutations you have more than one arms opening up.
*  And so now the frequency of two arms going up increased quite drastically.
*  How much does that change the dynamics somehow?
*  It potentially can change the dynamics of because now you have two possible opportunities to get
*  attached to the ACE2 receptor.
*  It's a very complex molecular process, mechanistic process.
*  But the first step of this process is the attachment of this spike protein, of the spike
*  trimer to the human ACE2 receptor.
*  So this is a molecule that sits on the surface of the human cell.
*  And that's essentially what initiates, what triggers the whole process of encapsulation.
*  If this was dating, this would be the first date.
*  In a way, yes.
*  So is it possible to have the spike protein just like floating about on its own?
*  Or does it need that interactability with the membrane?
*  Yeah, so it needs to be attached at least as far as I know.
*  But when you get this thing attached on the surface, there is also a lot of dynamics on
*  where, how it sits on the surface.
*  So for example, there was a recent work in, again, where people use the cryo-electron
*  microscopy to get the first glimpse of the overall structure.
*  It's a very low res, but you still get some interesting details about the surface,
*  about what is happening inside, because we have literally no clue until recent work about how
*  the capsid is organized.
*  With the capsid.
*  So capsid is essentially the inner core of the viral particle where there is the RNA of the virus,
*  and it's protected by another protein, N protein, that essentially acts as a shield.
*  But now we are learning more and more, so it's actually, it's not just this shield.
*  Potentially it's used for the stability of the outer shell of the virus.
*  So it's pretty complicated.
*  And I mean, understanding all of this is really useful for trying to figure out developing a
*  vaccine or some kind of drug to attack any aspects of this, right?
*  So I mean, there are many different implications to that.
*  First of all, it's important to understand the virus itself, right?
*  So in order to understand how it acts, what is the overall mechanistic process of this virus
*  replication, of this virus proliferation to the cell, right?
*  So that's one aspect.
*  The other aspect is designing new treatments.
*  So one of the possible treatments is designing nanoparticles.
*  And so some nanoparticles that will resemble the viral shape that would have the spike integrated
*  and essentially would act as a competitor to the real virus by blocking the ACE2 receptors
*  and thus preventing the real virus entering the cell.
*  Now there are also, there is a very interesting direction in looking at the membrane,
*  the envelope portion of the protein and attacking its M protein.
*  So to give you a brief overview, there are four structural proteins.
*  These are the proteins that made up a structure of the virus.
*  So spike as protein that acts as a trimer.
*  So it needs three copies.
*  E, envelope protein that acts as a pantomime.
*  So it needs five copies to act properly.
*  M is a membrane protein.
*  It forms dimers and actually it forms beautiful lattice.
*  And this is something that we've been studying and we are seeing it in simulations.
*  It actually forms a very nice grid or threads of different dimers attached next to each other.
*  There's a bunch of copies of each other and they naturally,
*  when you have a bunch of copies of each other, they form an interesting lattice.
*  Exactly.
*  If you think about this, this complex, the viral shape needs to be organized somehow,
*  self-organized somehow.
*  If it was a completely random process, you probably wouldn't have the envelope shell
*  of the ellipsoid shape.
*  You would have something pretty random shape.
*  So there is some regularity in how these M dimers get to attach to each other
*  in a very specific directed way.
*  Is that understood at all?
*  It's not understood.
*  We've been working in the past six months since we met.
*  This is where we started working on trying to understand the overall
*  structure of the envelope and the key components that made up this structure.
*  Does the envelope also have the lattice structure?
*  The envelope is essentially the outer shell of the viral particle.
*  The N, the nuclear capsid protein, is something that is inside.
*  But get that, the N is likely to interact with M.
*  Does it go M and E?
*  Where's the E?
*  E, those different proteins, they occur in different copies on the viral particle.
*  E, this pentamer complex, will only have two or three, maybe, per each particle.
*  We have a thousand or so of M dimers that essentially makes up the entire outer shell.
*  So most of the outer shell is the M dimer.
*  And the N protein.
*  When you say particle, that's the virus, the individual virus.
*  It's a single element of the virus.
*  It's a single virus.
*  Single virus.
*  We have about roughly 50 to 90 spike trimmers.
*  Per virus particle.
*  Per virus particle.
*  What did you say, 50 to 90?
*  50 to 90.
*  This is how this thing is organized.
*  Now, typically, you see the antibodies that target spike proteins,
*  certain parts of the spike protein.
*  But there could be some, also some treatments.
*  These are small molecules that bind strategic parts of these proteins, disrupting its functioning.
*  One of the promising directions, it's one of the newest directions,
*  is actually targeting the M dimer of the protein.
*  Targeting the proteins that make up this outer shell.
*  Because if you're able to destroy the outer shell,
*  you're essentially destroying the viral particle itself.
*  Preventing it from functioning at all.
*  You think from a cyber security perspective, virus security perspective,
*  that's the best attack vector?
*  That's a promising attack vector?
*  I would say yes.
*  There's still tons of research needs to be done.
*  There's more attack surface, I guess.
*  More attack surface.
*  But from our analysis, from other evolutionary analysis,
*  this protein is evolutionarily more stable compared to the spike protein.
*  Stable means a more static target?
*  Well, yeah.
*  So it doesn't change, it doesn't evolve from the evolutionary perspective
*  so drastically as, for example, the spike protein.
*  There's a bunch of stuff in the news about mutations of the virus in the United Kingdom.
*  I also saw in South Africa something, maybe that was yesterday.
*  You just kind of mentioned about stability and so on.
*  Which aspects of this are mutatable and which aspects, if mutated, become more dangerous?
*  And maybe even zooming out, what are your thoughts and knowledge and ideas about the
*  way it's mutated, all the news that we've been hearing?
*  Are you worried about it from a biological perspective?
*  Are you worried about it from a human perspective?
*  Mutations are sort of a general way for these viruses to evolve.
*  So essentially, this is the way they evolve.
*  This is the way they were able to jump from one species to another.
*  We also see some recent jumps.
*  There were some incidents of this virus jumping from human to dogs.
*  So there is some danger in those jumps because every time it jumps,
*  it also mutates.
*  When it jumps to the species and jumps back, it acquires some mutations that are sort of
*  driven by the environment of a new host.
*  It's different from the human environment.
*  We don't know whether the mutations that are acquired in the new species are neutral
*  with respect to the human host or maybe damaging.
*  Yeah, change is always scary.
*  It seems like because the spread is during winter now, it seems to be exceptionally high.
*  Especially with the vaccine just around the corner already being actually deployed,
*  there's some worry that this puts evolutionary pressure, selective pressure on the virus.
*  And for it to mutate, is that a source of worry?
*  Well, there is always this thought in the scientist's mind what will happen.
*  I know there have been discussions about the arms race between the ability of the
*  of the humanity to get vaccinated faster than the virus essentially becomes resistant to the vaccine.
*  I don't worry that much simply because there is not that much evidence to that.
*  To aggressive mutation around the vaccine.
*  Exactly. Obviously, there are mutations around the vaccine.
*  The reason we get vaccinated every year against the seasonal mutations.
*  I think it's important to study it. No doubts.
*  I think to me, and I might be biased because we've been trying to do that as well.
*  But one of the critical directions in understanding the virus is to understand its evolution
*  in order to understand the key mechanisms that lead the virus to jump, the Nordic viruses to jump
*  from species to another, the mechanisms that lead the virus to become resistant
*  to vaccines, also to treatments. And hopefully, that knowledge will enable us to forecast
*  the evolutionary traces, the future evolutionary traces of this virus.
*  From a biological perspective, this might be a dumb question, but is there parts of the virus
*  that if souped up through mutation could make it more effective at doing its job?
*  We're talking about this specific coronavirus. We were talking about the different membrane,
*  the M protein, the E protein, the N and the S, the spike.
*  20 or so more in addition to that.
*  Is that a dumb way to look at it? Which of these, if mutated, could have the greatest impact,
*  potentially damaging impact on the effectiveness of the virus?
*  It's a very good question. The short answer is we don't know yet. But of course, there is capacity
*  of this virus to become more efficient. The reason for that is, if you look at the virus,
*  I mean, it's a machine, right? So it's a machine that does a lot of different functions. And many
*  of these functions are sort of nearly perfect, but they're not perfect. And those mutations can
*  make those functions more perfect. For example, the attachment to ACE2 receptor, right, of the spike.
*  So has this virus reached the efficiency in which the attachment is carried out? Or there
*  are some mutations that are still to be discovered, right, that will make this attachment sort of
*  stronger or something more, in a way, more efficient from the point of view of this virus
*  functioning. That's sort of the obvious example. But if you look at each of these proteins, I mean,
*  it's there for a reason. It performs certain function. And it could be that certain mutations
*  will enhance this function. It could be that some mutations will make this function much less
*  efficient. So that's also the case. Since we're talking about the evolutionary history of a virus,
*  let's zoom back out and look at the evolution of proteins. I glanced at this 2010 Nature paper
*  on the quote, ongoing expansion of the protein universe. And then, you know, it kind of implies
*  and talks about that proteins started with a common ancestor, which is, you know, kind of
*  interesting. It's interesting to think about, like, even just like the first organic thing
*  that started life on Earth. And from that, there's now, you know, what is it, 3.5 billion years
*  later, there's now millions of proteins, and they're still evolving. And that's, you know,
*  in part one of the things that you're researching. Is there something interesting to you about the
*  evolution of proteins from this initial ancestor to today? Is there something beautiful, insightful
*  about this long story? So I think, you know, if I were to pick a single keyword about protein
*  evolution, I would pick modularity, something that we talked about in the beginning. And that's the
*  fact that the proteins are no longer considered as, you know, as a sequence of letters. There are
*  hierarchical complexities in the way these proteins are organized. And these complexities
*  actually going beyond the protein sequence. It's actually going all the way back to the
*  gene, to the nucleotide sequence. And so, you know, again, these protein domains,
*  they are not only functional building blocks, they are also evolutionary building blocks.
*  And so what we see in the sort of in the later stages of evolution, I mean, once this stable,
*  structurally and functionally building blocks were discovered, they essentially, they stay,
*  those domains stay as such. So that's why if you start comparing different proteins,
*  you will see that many of them will have similar fragments. And those fragments will correspond to
*  something that we call protein domain families. And so they are still different because you still
*  have mutations and the different mutations are attributed to diversification of the function
*  of these protein domains. However, you very rarely see the evolutionary events that would split
*  this domain into fragments because, and it's, you know, once you have the domain split,
*  you actually, you know, you can completely cancel out its function or at the very least,
*  you can reduce it. And that's not efficient from the point of view of the cell function.
*  So the protein domain level is a very important one. Now, on top of that, right, so if you look
*  at the proteins, right, so you have these structural units and they carry out the function. But then,
*  much less is known about things that connect these protein domains, something that we call linkers.
*  And those linkers are completely flexible, you know, parts of the protein that nevertheless
*  carry out a lot of function. It's like little tails, little heads. So we do have tails,
*  so they're called termini, C and N termini. So these are things right on one and another
*  ends of the protein sequence. So they are also very important. So they attribute it to very specific
*  interactions between the proteins. So- But you're referring to the links between domains.
*  That connect the domains. And, you know, apart from the just the simple perspective, if you have,
*  you know, a very short domain, you have, sorry, a very short linker, you have two domains next to
*  each other. They are forced to be next to each other. If you have a very long one, you have the
*  domains that are extremely flexible and they carry out a lot of sort of spatial reorganization.
*  Right. So, but on top of that, right, just this linker itself, because it's so flexible,
*  it actually can adapt to a lot of different shapes. And therefore it's a very good
*  interactor when it comes to interaction between this protein and other protein.
*  All right. So these things also evolve, you know, and they, in a way, have different sort of
*  laws of the driving laws that underlie the evolution because they no longer need to
*  preserve certain structure, right, unlike protein domains. And so on top of that, you have something
*  that is even less studied. And this is something that attributed to the concept of alternative
*  splicing. So alternative splicing, so it's a very cool concept. It's something that
*  we've been fascinated about for, you know, over a decade in my lab and trying to do research
*  with that. But so, you know, so typically, you know, a simplistic perspective is that
*  one gene is equal one protein product. All right. So you have a gene, you know, you
*  transcribe it and translate it and it becomes a protein. In reality, when we talk about
*  eukaryotes, especially sort of more recent eukaryotes that are very complex,
*  the gene is no longer equal to one protein. It actually can produce multiple functionally,
*  you know, active protein products. And each of them is, you know, is called an alternatively
*  spliced product. The reason it happens is that if you look at the gene, it actually has, it has also
*  blocks. And the blocks, some of which, and it essentially, it goes like this. So we have a
*  block that will later be translated. We call it exon. Then we'll have a block that is not translated,
*  cut out. We call it intron. So we have exon, intron, exon, intron, et cetera, et cetera,
*  et cetera. Right. So sometimes you can have, you know, dozens of these exons and introns.
*  So what happens is during the process when the gene is converted to RNA,
*  we have things that are cut out, the introns that cut out, and exons that now get assembled together.
*  And sometimes we will throw out some of the exons and the remaining protein product will become
*  different. Oh, different. Right. So now you have fragments of the protein that no longer there.
*  They were cut out with the introns. Sometimes you will essentially take one exon and replace it with
*  another one. Right. So there's some flexibility in this process. So that creates a whole new level
*  of complexity. Is this random though? Is it random? It's not random. And this is where I think
*  now the appearance of this modern single cell and before that tissue level sequencing,
*  next generation sequencing techniques such as RNA-seq allows us to see that these are the events
*  that often happen in response. It's a dynamic event that happens in response to disease or in
*  response to certain developmental stage of a cell. And this is an incredibly complex layer
*  that also undergoes, I mean, because it's at the gene level, right? So it undergoes certain
*  evolution. Right. And now we have this interplay between what is happening in the protein world
*  and what is happening in the gene and RNA world. And for example, it's often that we see that the
*  boundaries of these exons coincide with the boundaries of the protein domains.
*  Right. So there is close interplay to that. It's not always, I mean, otherwise it would be too
*  simple, right? But we do see the connection between those sort of machineries. And obviously
*  the evolution will pick up this complexity and, you know, select for whatever is successful.
*  Yeah, we see that complexity in play and makes this question, you know, more complex, but more
*  exciting. As a small detour, I don't know if you think about this into the world of computer science,
*  there's Douglas Hofstadter, I think came up with the name of Quine, which are, I don't know if
*  you're familiar with these things, but it's computer programs that have, I guess, Exon and Intron,
*  and they copy, the whole purpose of the program is to copy itself. So it prints copies of itself,
*  but can also carry information inside of it. So it's a very kind of crude, fun exercise of,
*  um, can we sort of replicate these ideas from cells of can we have a computer program that when
*  you run it, just print itself, the entirety of itself and does it in different programming
*  languages and so on. I've been playing around and writing them. It's a kind of fun little exercise.
*  You know, when I was a kid, so, so, you know, it, it was essentially one of the, of the sort of
*  sort of main stages in, in, uh, informatics Olympiads that you have to reach in order to be
*  any so good is you should be able to write a program that replicates itself.
*  And so the tags then becomes even, you know, sort of more complicated. So what is the shortest?
*  What is the shortest? Yeah. And of course it's, it's, you know, it's a function of a programming
*  language, but yeah, I remember, you know, long, long, long time ago when we tried to, you know,
*  to, to make it short and short and find the, the, the, the shortcuts.
*  There's actually on a stack exchange, there's a entire site called code golf, I think,
*  where the entirety is just the competition. People just come up with whatever task.
*  I don't know, like a right code that reports the weather today. And the competition is about
*  whatever programming language, what is the shortest program? And it makes you actually,
*  people should check it out because it makes you realize there's some,
*  some weird programming languages out there. Um, but you know, just to dig on that a little, uh,
*  deeper, uh, do you think, you know, in computer science, we don't often think about
*  programs. There's like the machine learning world now, uh, that's still kind of basic programs.
*  And then there's humans that replicate themselves, right? And there's these mutations and so on.
*  Do you think we'll ever have a world where there's programs that kind of
*  have an evolutionary process? So I'm not talking about evolutionary algorithms,
*  but I'm talking about programs that kind of meet with each other and evolve and
*  like on their own replicate themselves. So this is kind of the idea here is,
*  you know, that's how you can have a runaway thing. So we think about machine learning as a system
*  that gets smarter and smarter and smarter and smarter. At least the machine learning systems
*  of today are like, it's, it's a program that you can like turn off as opposed to throwing a bunch
*  of little programs out there and letting them like multiply and mate and evolve and replicate.
*  Do you ever think about that kind of world, you know, when we jump from the biological
*  systems that you're looking at to, to artificial ones?
*  I mean, it's almost like you, you take the, the sort of the area of intelligent agents,
*  right? Which are essentially the, the independent sort of, uh,
*  codes that run and interact and exchange the information, right? So I, I don't see why not.
*  I mean, I, you know, it could be sort of a natural evolution in, in, in this, you know,
*  uh, area of computer science. I think it's kind of an interesting
*  possibility. It's terrifying too, but I think it's a really powerful tool. Like to have like agents
*  that inter, you know, we have social networks with millions of people and they interact. I think it's
*  interesting to inject into that was already injecting into that bots, right? But those bots
*  are pretty dumb. Uh, you know, they're, they're probably pretty dumb algorithms. Uh, you know,
*  it's interesting to think that there might be bots that evolve together with humans.
*  And there's the sea of humans and robots that are operating first in the digital space. And then
*  you can also think, I love the idea. Some people worked, I think, uh, at Harvard, at Penn, there's,
*  uh, robotics labs that, you know, build, take as a fundamental task to build a robot
*  that given extra resources can build another copy of itself, like in the physical space,
*  which is, uh, super difficult to do, but super interesting. I remember there's like research on
*  robots that can build a bridge. So they make a copy of themselves and they connect themselves.
*  So it's like self building bridge based on building blocks. You can imagine like a building that's
*  self-assembles. So it's basically self-assembling structures from, uh, from, uh, robotic parts,
*  but it's interesting to within that robot add the ability to mutate and, uh, and, and do all the
*  interesting, like little things that you're referring to in evolution to go from a single origin
*  protein building block to like this weird complex. And if you think about this, I mean,
*  you know, the bits and pieces are there, you know, so, so you mentioned the evolution algorithm,
*  right? You know, so this is sort of, and the, the, maybe it's sort of the, the, the goal is in a way
*  different, right? So the goal is to, you know, to essentially, uh, to, to optimize your search,
*  right? So, uh, but, uh, sort of the ideas are there. So you, people recognize that, you know,
*  that, uh, the, you know, recombination events lead to global changes in the, in, in, in the
*  search trajectories, the mutations event is a more refined, uh, you know, uh, step in the search.
*  Then you have, you know, uh, other sort of, uh, nature inspired algorithm, right? So, so one of
*  the reasons that, that I, you know, I think it's, it's one of the funnest one is the slime, uh,
*  based algorithm, right? So that it's, uh, I think the first was introduced by the Japanese, uh,
*  group, but where it was able to, to solve, uh, some, some pre, you know, complex problems.
*  Uh, so, so that's the, you know, and, and then I think, uh, there are still a lot of things we've
*  yet to, to, you know, borrow from the nature, right? So there are a lot of sort of ideas that
*  nature, uh, you know, gets to offer us that, you know, it's up to us to grab it and to, to, to,
*  to, you know, get the best use of it. Including neural networks, you know,
*  we have a very crude in spot inspiration from nature on neural networks. Maybe there's
*  other inspirations to be discovered in the brain or other aspects of, uh, the various systems,
*  even like the immune system, the way it, uh, interplays. I recently started to understand
*  that they like the immune system has something to do with the way the brain operates. Like there's
*  multiple things going on in there, which, uh, all of which are not modeled in artificial neural
*  networks. And maybe if you throw a little bit of that biological spice in there, you'll come up
*  with something, uh, something cool. I, I, uh, I'm not sure if you're familiar with the Drake equation
*  that, uh, estimate, I just did a video on it yesterday cause I wanted to give my own estimate
*  of it. It's, uh, it's an equation that combines a bunch of factors to estimate how many alien
*  civilizations are in the galaxy. I've heard about it. Yes. So one, one of the interesting
*  parameters, you know, it's like, uh, how many stars are born every year, how many planets are
*  on average per star, uh, for this, how many habitable planets are there. And then the,
*  the one that starts being really interesting is, uh, the probability that life emerges on a habitable
*  planet. So like, I don't know if you think about, you certainly think a lot about evolution,
*  but do you think about the thing which evolution doesn't describe, which is like the beginning of
*  the origin of life? I think I put the probability of life developing in a habitable planet at 1%.
*  This is very scientifically rigorous. Okay. Uh, what first at a high level for the Drake equation,
*  what would you put that percent that on earth? And in general, do you have something,
*  do you have thoughts about how life might've started, you know, like the proteins being the
*  first kind of one of the early jumping points? Yes. So, so, um, I think back in 2018, there was
*  a very exciting paper published in nature where they, um, found, uh, one of the simplest amino
*  acids, glycine in a comet dust. So, so this is, uh, and I apologize if I, uh, don't pronounce,
*  it's a Russian named comet. It's I think Chugrumov-Gerasimenko. This is the comet where,
*  and there was this, uh, um, mission to, to get and, uh, get close to this comet and get the,
*  the, uh, stardust from, from its tail. And, uh, when scientists analyzed it, they actually found
*  traces of, uh, you know, uh, of glycine, which, you know, makes up, you know, the one, it's one of the
*  basic, uh, one of the 20 basic, uh, amino acids that makes up proteins. Right. So, uh, so that was
*  kind of exciting, right. But you know, it's, the question is very interesting, right? So what
*  you know, what, if there is some alien life, is it going to be made of proteins? Right. Or maybe
*  RNAs, right. So we see that, you know, the, the RNA viruses are certainly, you know, very well
*  established sort of, uh, you know, group of molecular machines. Right. So, um, so yeah, it's,
*  it's, it's a very interesting question. What, what probability would you put? Like how hard is this
*  job? Like how unlikely just on earth do you think this whole thing is that we got going?
*  Like, is that, are we really lucky or is it inevitable? Like, what's your sense when you
*  sit back and think about life on earth? Is it higher or lower than 1%? Well, cause 1% is pretty
*  low, but it still is like, damn, that's pretty good chance. Yes. It's, it's a pretty good chance. I
*  would personally, but again, you know, I'm, um, you know, probably not the best person to,
*  to, to, to do such estimations, but, uh, I would, you know, intuitively I would probably put it
*  lower, but still, I mean, you know, given we're really lucky here on earth. I mean,
*  or the conditions are really good. It's me. That's, you know, I think that there was everything was
*  right in a way. Right. So we still, it's not the, the conditions were not like ideal. If you try to,
*  to look at, you know, what was, you know, several billions years ago when the life emerged.
*  So there, there is something called, uh, the rare earth hypothesis that, you know,
*  encounter to the Drake equation says that the, you know, the conditions of earth, if you actually
*  were to describe earth, it's quite a special place. So special might be unique in our galaxy
*  and potentially, you know, close to unique in the entire universe. Like it's very difficult
*  to reconstruct those same conditions. And what the rare earth hypothesis argues is all those
*  different conditions are essential for life. And so that's sort of the counter, you know,
*  like all the things we, you know, thinking that earth is pretty average. Um, I mean, I can't
*  really, I'm trying to remember to, to go through all of them, but just the fact that it, um,
*  is shielded from a lot of asteroids, the, obviously the distance to the sun, but also the
*  fact that it, um, it's like a perfect balance between the amount of water and land and all
*  those kinds of things. I don't know. There's a bunch of different factors that I don't remember.
*  There's a long list, but it's fascinating to think about if, uh, if, uh, if, uh, in order for
*  something like proteins and then the DNA and RNA to, to merge, you need, um, and basic living
*  organisms, you need to be a very close and earth like planet, which will be sad or exciting. I
*  don't know which, uh, if you ask me, I, you know, in a way I put a parallel between, um,
*  you know, between our own research. Uh, and I mean, from the, from the intuitive perspective,
*  you know, you have those two extremes and the reality is never very rarely falls into the
*  extremes. It's always the optimum's always reached somewhere in between. So, so I would,
*  so, and that's what I tend to think. I think that, uh, you know, we're probably somewhere in between.
*  So they were not unique, unique, but again, the chances are, you know, reasonably small.
*  The problem is we don't know the other extreme is like, I tend to think that we don't actually
*  understand the basic mechanisms of like what this is all originated from. Like it seems like we
*  think of life as this distinct thing, maybe intelligence is a distinct thing. Maybe the
*  physics that from which planets and sons are born is a distinct thing, but that could be a very,
*  it's like the Stephen Wolfram thing. It's like the, from simple rules emerges greater and greater
*  complexity. So, uh, you know, I tend to believe that just life finds a way it like, we don't know
*  the extreme of how common life is because it could be life is like everywhere. Like, like so everywhere
*  that it's almost like laughable, like that we're such idiots to think, like it's, it's like ridiculous
*  to even like think it's like ants thinking that their little colony is the unique thing
*  and everything else doesn't exist. I mean, it's also very possible that that's, uh,
*  that's the extreme and we're just not able to maybe comprehend the nature of that, uh,
*  life. I mean, just to stick on alien life for just a brief moment more is there is some signs of
*  signs of life on Venus in gaseous form. There's a hope for life on Mars, probably extinct. We're
*  not talking about intelligent life. Although that has been in the news recently, we're talking about
*  basic, like, you know, uh, bacteria, yeah. And then also, I guess, uh, there's a couple of moons
*  that I get, yeah. Europa, which is Jupiter's moon. I think there's another one. Are you,
*  um, is that exciting or is it terrifying to you that we might find life? Do you hope we find life?
*  I certainly do hope that we find life. Um, I mean, it was very exciting to, to hear about, uh, you
*  know, uh, this, uh, news about the deal possible life on the Venus. It'd be nice to have hard
*  evidence of something with, uh, which is what the hope is for, for Mars and, and, uh, Europa. But do
*  you think those organisms will be similar biologically or would they even be sort of
*  carbon-based if we do find them? I would say they, they would be carbon-based. Uh, how similar?
*  It's a big question, right? So it's, it's, you know, the moment we discover things outside Earth,
*  right? Even if it's a tiny little single cell, I mean, there's so much. Just imagine that. That
*  would be so, I think that that would be another turning point for the science, you know? And if,
*  especially if it's different in some very new way, that's exciting. Cause that says that's a
*  definitive state, not definitive, but a pretty strong statement that life is everywhere in the,
*  in the, in the universe. To me, at least that's, that's really exciting.
*  You brought up Joshua Lederberg in an offline conversation. I think I'd love to talk to you
*  about Alpha Fold. And this might be an interesting way to answer that conversation because,
*  so he won the 1958 Nobel Prize in physiology and medicine for discovering that bacteria can mate
*  and exchange genes. But, uh, he also did a ton of other stuff, like, uh, like we mentioned, uh,
*  helping NASA find life on Mars and, uh, the, uh, dendro, the, the chemical expert system,
*  expert systems. Remember those, uh, do you, uh, what do you find interesting about this guy and
*  his, his ideas about artificial intelligence in general? So I have a kind of personal story to,
*  to share. So I started my PhD in Canada back in 2000. And so essentially my, my PhD was,
*  so we were developing sort of a new language for symbolic, uh, machine learning. So it's different
*  from the feature-based machine learning. And, and the, uh, one of the sort of, uh, cleanest
*  applications of this, uh, you know, of this approach of this formalism was, uh, to, uh,
*  chemoinformatics and computer-aided drug design. Right. So, so, so essentially we were, uh, you
*  know, as a part of my research, um, uh, I developed a system that essentially looked at, uh,
*  chemical compounds of say the same therapeutic category, you know, um, male hormones, right.
*  And try to figure out, um, the structural fragments that are the structural building blocks
*  that are important that define this class versus structural building blocks that are there just
*  because, you know, to complete the structure, but they are not essentially the ones that make up the,
*  the chemical, the, the key chemical properties of this, uh, therapeutic category. And, and, uh,
*  you know, uh, for me, it was something new. I was, I was trained as an applied mathematicians,
*  you know, as with some machine learning background, but, you know, computer-aided
*  drug design was completely a completely new territory. So because of that, I often find
*  myself asking lots of questions, uh, on one of these sort of central, uh, forums. Back then there
*  were no, no Facebooks or stuff like that. There was a forum, a forum. It's essentially, it's like a
*  bulletin board. Right. Where you, yeah. So you essentially, you have a bunch of people and you
*  post a question and you get, you know, an answer from, you know, different people. And, and, and
*  back then this, like one of the most popular, uh, forums was CCL think, um, computational chemistry
*  library, not library, but something like that, but CCL that that was the, the, the forum and there I,
*  you know, I asked a lot of dumb questions. Yes. I asked questions, also share some, some, you know,
*  some, uh, information about our form is and how we do and whether what, whatever we do makes sense.
*  And so, you know, and, uh, I remember that one of this posts, I mean, I still remember, you know, uh,
*  I, uh, I would call it desperately looking for, uh, for, uh, a chemist advice, something like that.
*  Right. And so, so I post my question, I explained, you know, how, how my, uh, uh, our
*  formalism is what is, what it does and what kind of applications I'm planning to, to do. And, you
*  know, and it was, you know, in the middle of the night and, you know, I went back, uh, you know,
*  to bed and, and next morning have a phone call from my advisor who also looked at this forum.
*  It's like, you won't believe who replied to you. And, and it's like, who? And he said, well,
*  you know, there is a message to you from Joshua Lederberg. And my reaction was like,
*  who is Joshua Lederberg? Your advisor hung up.
*  So, and essentially, you know, Joshua wrote me that we, we had conceptually similar ideas in,
*  in the dendrel pro project. You may want to look it up and, you know, we should also,
*  sorry, and it's a side comment, say that even though he, he won the Nobel prize at a really
*  young age in 58, but so he, he was, I think he was what 33. Yeah. It's just crazy. Yeah. So
*  anyway, so that's so hence, hence in the nineties, responding to young whippersnappers on the, on the
*  CCL forum. Okay. And so, so, so back then he was already very senior. I mean, he unfortunately
*  passed away back in 2008. But, you know, back in 2001, he was, I mean, he, he was a professor
*  emeritus at Rockefeller University. And, you know, that was actually, believe it or not, one of the,
*  one of the, of, of the reasons I decided to join, you know, as a postdoc, the group of Andrei Salih,
*  who was at Rockefeller University with the hope that, you know, that I could actually, you know,
*  have a chance to meet Joshua in person. And I met him very briefly, right? The, you know,
*  just because he was walking, you know, there's a little bridge that connects the sort of the
*  research campus with the, with the sort of skyscraper that Rockefeller owns, the where,
*  you know, postdocs and faculty and graduate students live. And so, so I met him, you know,
*  and had a very short conversation, you know, but so I started, you know, reading about Dendral
*  and I was amazed, you know, it's, we're talking about 1960, right? The ideas were so profound.
*  Well, what's the fundamental ideas of it? The, the reason to make this is even crazier.
*  So, so, so Lederberg wanted to make a system that would help him study the
*  extraterrestrial molecules, right? So, so the idea was that, you know, the way you study the
*  extraterrestrial molecules is you do the mass spec analysis, right? And so the mass spec gives you
*  sort of bits, numbers about essentially gives you the ideas about the possible fragments or,
*  you know, atoms, you know, and maybe a little fragments, pieces of this molecule that make up
*  the molecule, right? So now you need to sort of to decompose this information and to figure out
*  what was the whole before, you know, it became fragments, bits and pieces, right? So,
*  so in order to make this, you know, to have this tool, the idea of Lederberg was to connect
*  chemistry, computer science, and to design this so-called expert system that looks,
*  that takes into account, that takes as an input, the mass spec data, the possible,
*  the database of possible molecules, and essentially try to sort of induce the molecule that would
*  correspond to this spectra or, you know, essentially the, what this project ended up being was that,
*  you know, it would provide a list of candidates that then a chemist would look at and make final
*  decision. So, but the original idea is supposed to solve the entirety of this problem automatically.
*  Yes. So, so, so he, you know, so, so he, back then, he approached, yes, believe that,
*  it's amazing. I mean, it still blows my mind, you know, that it's, that's, it's, and this was
*  essentially the, the, the origin of the modern bioinformatics, chemoinformatics, you know, back
*  in the 60s. So that's, that's, you know, so every time you, you, you, you deal with, with projects
*  like this, with the, you know, research like this, you just, you know, so the, the, the power of,
*  of the, you know, intelligence of these people is just, you know, overwhelming.
*  Do you think about expert systems? Is there, and why they kind of didn't become successful,
*  especially in the space of bioinformatics, where it does seem like there is a lot of expertise in
*  humans. And, you know, it's, it's possible to see that a system like this could be made very useful.
*  Right. So it's, it's actually, it's a, it's a great question. And, and this is something so,
*  you know, so, you know, at my university, I teach artificial intelligence. And, you know, we start
*  the, my first two lectures are on the history of AI. And there we, you know, we try to, you know,
*  go through the main stages of AI. And so, you know, the question of why expert systems
*  failed or became obsolete. It's actually a very interesting one. And there are, you know, if you
*  try to read the, you know, the historical perspectives, there are actually two lines of
*  thoughts. One is that the, they were essentially not up to the expectations. And so therefore,
*  they were replaced, you know, by, by other things. Right. The other one was that completely
*  opposite one, that they were too good. And, and as a result, they essentially became sort of a
*  household name. And then essentially they, they got transformed. I mean, they, in both cases,
*  sort of the outcome was the same, they evolved into something. Right. And that's what I, you know, if
*  if I look at this, right. So the modern machine learning, right. So,
*  So there's echoes in the modern machine learning. I think so. I think so, because, you know, if,
*  if you think about this, you know, and how we design, you know, the most successful algorithms,
*  including alpha fold, right, you built in the knowledge about the domain that you study.
*  Right. So, so you built in your expertise. So speaking of alpha fold, so deep minds,
*  alpha fold two recently was announced to have quote unquote, solved protein folding.
*  How exciting is this to you? It seems to be one of the, one of the exciting things that have
*  happened in 2020. It's incredible accomplishment from the looks of it. What part of it is amazing
*  to you? What part would you say is overhype or maybe misunderstood? It's definitely a very
*  exciting achievement to give you a little bit of perspective. Right. So, so in bioinformatics,
*  we have several competitions. And so the way, you know, you often hear how those competitions
*  have been explained to sort of to non bioinformaticians is that, you know, they call
*  it bioinformatics Olympic games, and there are several disciplines, right. So, so the, so the,
*  the historically one of the first one was the discipline in predicting the protein structure.
*  Predicting the 3d coordinates of the protein, but there are some others. So the predicting
*  protein functions, predicting effects of mutations on protein functions, then predicting a protein,
*  protein interactions. So, so the original one was a CASP or a critical assessment of, of protein
*  structure. And the, you know, typically what happens during these competitions is, you know,
*  scientists, experimental scientists solve the structures, but don't put them into the protein
*  data bank, which is the centralized database that contains all these 3d coordinates.
*  Instead, they hold it and release protein sequences. And now the challenge of the
*  community is to predict the 3d structures of this proteins and then use the experiment
*  structures to assess which one is the closest one. Right. And this competition, by the way,
*  just a bunch of different tangents. And maybe you can also say what is protein folding.
*  In this competition, CASP competition is, has become the gold standard. And that's what was
*  used to say that protein folding was solved. So I just add a little, yeah, just a bunch. So if you
*  can, whenever you say stuff, maybe throw in some of the basics for the folks that might be outside
*  of the field. Anyway, sorry. So, so yeah, so, you know, so the reason it's, it's, you know, it's
*  relevant to our understanding of protein folding is because, you know, we, we, we've yet to learn
*  how the folding mechanistically works. Right. So there are different hypothesis. What happens to
*  this fold? For example, there is a hypothesis that the folding happens by, you know, also in the
*  modular fashion. Right. So that, you know, we have protein domains that get folded independently
*  because their structure is stable. And then the whole protein structure gets formed. But,
*  you know, within those domains, we also have so-called secondary structure, the small
*  alpha helices, beta sheets. So these are, you know, elements that are structurally stable.
*  And so, and the question is, you know, when they, when do they get formed? Because some of the
*  secondary structure elements, you have to have, you know, a fragment in the beginning and say,
*  the fragment in the middle. Right. So, so you cannot potentially start having the full fold
*  from the get-go. Right. So, so it's still, you know, it's still a big enigma. What, what happens?
*  We know that it's an extremely efficient and stable process. Right. So there's this long
*  sequence and the fold happens really quickly. Exactly. That's really weird. Right. And it
*  happens like the same way almost every time. Exactly. Exactly. That's really weird. That's
*  freaking weird. It's, it's, yeah, that's, that's why it's such an amazing thing. But most importantly,
*  right. So it's, you know, so when, when you see the, the, the, you know, the translation process,
*  right. So when you don't have the, the, the whole protein translated, right. It's still being
*  translated, you know, getting out from the ribosome, you, you already see some structural,
*  you know, fragmentation. So, so folding starts happening before the whole protein gets produced.
*  Right. And so this is, this is obviously, you know, one of the biggest questions in,
*  you know, in modern molecular biologists. Not, not like maybe what happens, like that's not
*  as bigger than the question of folding. That's the question of like,
*  something like deeper fundamental idea of folding. Yes. Behind folding. Exactly. Exactly. So,
*  you know, so obviously if we are able to predict the end product of protein folding,
*  we are one step closer to understanding sort of the mechanisms of the protein folding,
*  because we can then potentially look and, and start probing what are the critical parts of
*  this process and what are not so critical parts of this process. So we can start decomposing
*  this, you know, so, so, so in the way this protein structure prediction algorithm can be,
*  can be used as a tool, right. So, so you change the, the, the, you know, you, you modify the,
*  the protein, you get back to, to this tool, it predicts, okay, it's completely,
*  it's completely unstable. Yeah. Which, which aspects of the input will have a big impact on
*  the output. Exactly. Exactly. So, so what happens is, you know, we typically have some sort of
*  incremental advancement, you know, each stage of this CASP competition, you have groups with
*  incremental advancement and, you know, historically the top performing groups were, you know, they were
*  not using machine learning. They were using very advanced biophysics combined with bioinformatics,
*  combined with, you know, the, the data mining. And that was, you know, that would enable them to
*  obtain protein structures of those proteins that don't have any structural soft relatives.
*  Because, you know, if we have another protein, say the same protein, but coming from a different
*  species, we could potentially derive some ideas and that's so-called homology or comparative
*  modeling, where we'll derive some ideas from the previously known structures. And that would help
*  us tremendously in, you know, in reconstructing the 3D structure overall. But what happens when
*  we don't have these relatives? This is when it becomes really, really hard, right? So that's so
*  called de novo, you know, de novo protein structure prediction. And in this case, those methods were
*  traditionally very good. But what happened in the, in the last year, the original alpha fault came
*  into and over sudden, it's much better than everyone else.
*  This is 2018.
*  Yeah.
*  Oh, and the competition is only every two years, I think.
*  And, and then, so, you know, it was sort of kind of over shockwave to the bioinformatics community
*  that, you know, we have like a state of the art machine learning system that does, you know,
*  structure prediction. And essentially what it does, you know, so, you know, if you look at this,
*  it actually predicts the context. So, you know, so the process of reconstructing the 3D structure
*  starts by predicting the context between the different parts of the protein. And the context
*  is essentially the parts of the proteins that are in a close proximity to each other.
*  Right. So it's actually the machine learning part seems to be estimating. You can correct me
*  if I'm wrong here, but it seems to be estimating the distance matrix, which is like
*  the distance between the different parts.
*  Yeah. So, so we call it the contact map.
*  Contact map.
*  Right. So once you have the contact map, the reconstruction is becoming more straightforward.
*  Yeah.
*  Right. But so the contact map is the key. And so, so, you know, so that what happened,
*  and now we started seeing in this current stage, right? Well, in the most recent one,
*  we started seeing the emergence of these ideas in other people's works. Right. But yet here's,
*  you know, Alpha Fold 2 that again outperforms everyone else. And also by introducing yet
*  another wave of the machine learning ideas.
*  There does seem to be also an incorporation. First of all, the paper is not out yet,
*  but there's a bunch of ideas already out. There does seem to be an
*  incorporation of this other thing. I don't know if it's something that you could speak to,
*  which is like the incorporation of like other structures, like evolutionary similar
*  structures that are used to kind of give you hints.
*  Yes. So evolutionary similarity is something that we can detect at different levels. Right. So
*  we know, for example, that the structure of proteins is more conserved than the sequence.
*  The sequence could be very different, but the structural shape is actually still very conserved.
*  So that's sort of the intrinsic property that, you know, in a way related to protein fold,
*  to the evolution of the proteins and protein domains, et cetera. But we know that. I mean,
*  there have been multiple studies. And ideally, if you have structures, you know, you should
*  use that information. However, sometimes we don't have this information. Instead,
*  we have a bunch of sequences. Sequences we have a lot. Right. So we have hundreds,
*  thousands of, you know, different organisms sequenced. Right. And by taking the same protein,
*  but in different organisms and aligning it, so making it, you know, making the corresponding
*  positions aligned, we can actually say a lot about sort of what is conserved in this protein.
*  And therefore, you know, structurally more stable, what is diverse in these proteins.
*  So on top of that, we could provide sort of the information about the
*  sort of the secondary structure of this protein, et cetera, et cetera. So this information is
*  extremely useful. And it's already there. So while it's tempting to, you know, to do a complete
*  ab initio, so you just have a protein sequence and nothing else, the reality is such that we
*  are overwhelmed with this data. So why not use it? And so, yeah, so I'm looking forward to reading
*  this paper. It does seem to like they've in the previous version of Alpha Fold, they didn't,
*  for this, the evolutionary similarity thing, they didn't use machine learning for that. Or they
*  rather they used it as like the input to the entirety of the neural net, like the features
*  derived from the similarity. It seems like there's some kind of quote unquote iterative thing,
*  where it seems to be part of the learning process is the incorporation of this evolutionary
*  similarity. Yeah, I don't think there is a bio archive paper, right? There's no, there's nothing.
*  Yeah, so a blog post that's written by a marketing team, essentially, which, you know, it has some
*  some scientific similarity, probably to the actual methodology used, but it could be,
*  it's like interpreting scripture, it could be just poetic interpretations of the actual work,
*  as opposed to direct connection to the work. So now, speaking about protein folding, right? So,
*  so, you know, in order to answer the question whether or not we have solved this, right? So we
*  need to go back to the beginning of our conversation, you know, with the realization
*  that, you know, an average protein is that typically what the CASP has been focusing on is
*  this competition has been focusing on the single, maybe two domain proteins that are still very
*  compact. And even those ones are extremely challenging to solve, right? But now we talk
*  about, you know, an average protein that has two, three protein domains. If you look at the
*  proteins that are in charge of the, you know, of the process with the neural system, right?
*  Perhaps one of the most recently evolved sort of systems in the organism, right? All of them, well,
*  the majority of them are highly multi-domain proteins. So they are, you know, some of them
*  have five, six, seven, you know, and more domains, right? And, you know, we are very far away from
*  understanding how these proteins are folded. So the complexity of the protein matters here,
*  the complexity of the protein modules or the protein domains. So you're saying solved, so the
*  definition of solved here is particularly the CASP competition achieving human level,
*  not human level, achieving experimental level performance on these particular sets of proteins
*  that have been used in these competitions. Well, I mean, you know, I do think that,
*  you know, especially with regards to the alpha fold, you know, it is able to, you know,
*  to solve, you know, at the near experimental level, a pretty big majority of the more compact
*  proteins like, or protein domains, because again, in order to understand how the overall protein,
*  you know, multi-domain protein fold, we do need to understand the structure of its individual
*  domains. I mean, unlike if you look at AlphaZero or like even MuZero,
*  if you look at that work, you know, it's nice reinforcement learning,
*  self-playing mechanisms are nice because it's all in simulation. So you can learn from just
*  huge amounts. Like you don't need data. It was like the problem with proteins, like the size,
*  I forget how many 3D structures have been mapped, but the training data is very small.
*  No matter what it's like millions, maybe a one or two million, something like that,
*  but some very small number, but like it doesn't seem like that's scalable. There has to be,
*  I don't know, it feels like you want to somehow 10x the data or 100x the data somehow.
*  Yes, but we also can take advantage of homology models, right? So the models that are of very
*  good quality because they are essentially obtained based on the evolutionary information.
*  So there is a potential to enhance this information and use it again to empower the training set.
*  And I think I am actually very optimistic. I think it's been one of these
*  churning events where you have a system that is a machine learning system that is truly better
*  than the more conventional biophysics based methods.
*  That's a huge leap. This is one of those fun questions, but where would you put it
*  in the ranking of the greatest breakthroughs in artificial intelligence history?
*  Okay, so let's see who's in the running. Maybe you can correct me. So
*  you got AlphaZero and AlphaGo beating the world champion at the game of Go. Thought to be
*  impossible 20 years ago, or at least the AI community was highly skeptical. Then you got
*  also Deep Blue, original Kasparov. You have deep learning itself, like the, maybe, what would you
*  say, the AlexNet ImageNet moment. So the first neural network achieving human level performance,
*  super, that's not true, achieving like a big leap in performance on the computer vision problem.
*  There is OpenAI, the whole GPT-3, that whole space of transformers and language models,
*  just achieving this incredible performance of application of neural networks to language models.
*  Boston Dynamics, pretty cool. Like robotics, even though people are like, there's no AI,
*  no, there's no machine learning currently, but AI is much bigger than machine learning.
*  Yes. So that just the engineering aspect, I would say it's one of the greatest accomplishments in
*  engineering side, engineering meaning like mechanical engineering of robotics ever. Then,
*  of course, autonomous vehicles. You can argue for Waymo, which is like the Google self-driving car,
*  or you can argue for Tesla, which is like actually being used by hundreds of thousands of people
*  on the road today, machine learning system. And I don't know if you can, what else is there? But
*  I think that's it. And then Alpha Fold, many people are saying is up there, potentially number one.
*  Would you put them at number one? Well, in terms of the impact on the science and on the society
*  beyond, it's definitely, to me would be one of the- Top three.
*  Maybe. I mean, I'm probably not the best person to answer that. But I do have, I remember
*  my, back in I think 1997 when deep blue, that Kasparov, it was a shock. I mean, it was,
*  and I think for the pre-substantial part of the world that especially people who have some
*  experience with chess and realizing how incredibly human this game, how much of a brain power you need
*  to reach those levels of grandmasters level. It's probably one of the first time, and how good Kasparov
*  was. And again, yeah, so Kasparov is arguably one of the best ever. And you get a machine that beats
*  him. So it's- First time a machine probably beat a human at that scale of a thing, of anything.
*  Yes. So that was to me, that was like, one of the groundbreaking events in the history of AI.
*  Yeah, that's probably number one. It's hard to remember. It's like Muhammad Ali versus,
*  I don't know any other Mike Tyson or something like that. It's like, nah, you got to put Muhammad
*  Ali at number one. Same with deep blue, even though it's not machine learning based.
*  Still it uses advanced search and search is the integral part of AI, right?
*  So it's not, as you said- People don't think of it that way at this moment. In vogue currently,
*  search is not seen as a fundamental aspect of intelligence, but it very likely is. In fact,
*  that's what neural networks are, is they're just performing search on the space of parameters.
*  And it's all search. All of intelligence is some form of search and you just have to become clever
*  and clever at that search problem. And I also have another one that you didn't mention. That's
*  one of my favorite ones. So you probably heard of this. I think it's called Deep Rembrandt.
*  It's the project where they trained, I think there was a collaboration between the experts in
*  Rembrandt painting in Netherlands and a group, an artificial intelligence group, where they train
*  an algorithm to replicate the style of the Rembrandt and they actually printed a portrait that
*  never existed before in the style of Rembrandt. I think they printed it on the canvas using pretty
*  much the same types of paints and stuff. To me, it was mind blowing.
*  In the space of art, that's interesting. There hasn't been, maybe that's it, but I think there
*  hasn't been an ImageNet moment yet in the space of art. You haven't been able to achieve superhuman
*  level performance in the space of art, even though there's a big famous thing where
*  a piece of art was purchased, I guess, for a lot of money. But it's still, people are like,
*  in the space of music at least, it's clear that human created pieces are much more popular.
*  There hasn't been a moment where it's like, I would say in the space of music,
*  what makes a lot of money, we're talking about serious money, it's music and movies,
*  shows and so on, and entertainment. There hasn't been a moment where AI was able to create a piece
*  of music or a piece of cinema, like Netflix show, that's sufficiently popular to make a ton of money.
*  That moment would be very, very powerful because that's an AI system being used to make a lot of
*  money. Of course, AI tools, even Premiere, audio editing, all the editing, everything I do,
*  that are this podcast, there's a lot of AI involved. Actually, this is a program,
*  I want to talk to those folks just because I want to nerd out, it's called iZotope. I don't know if
*  you're familiar with it. They have a bunch of tools of audio processing and they have, I think they're
*  Boston based. It's so exciting to me to use it on the audio here because it's all machine learning.
*  It's not because most audio production stuff is like any kind of processing you do, it's very
*  basic signal processing. You're tuning knobs and so on. They have all of that, of course,
*  but they also have all of this machine learning stuff where you actually give it training data.
*  You select parts of the audio you train on, you train on it and it figures stuff out. It's great.
*  The ability of it to be able to separate voice and music, for example, or voice in anything,
*  is incredible. It's clearly exceptionally good at applying these different neural networks models
*  to separate the different kinds of signals from the audio. That's really exciting. Photoshop,
*  Adobe people also use it, but to generate a piece of music that will sell millions, a piece of art.
*  No, I agree. As I mentioned, I offer my AI class and an integral part of this is the project.
*  Right? It's my ultimate favorite part because typically we have these project presentations
*  the last two weeks of the classes right before the Christmas break. It adds this
*  cool excitement. I'm amazed with some projects that people come up with.
*  Quite a few of them have some link to arts. I think last year we had a group who designed an AI
*  producing hokus, Japanese poems. It got trained on the English base, hokus.
*  Some of them get to present the top selection. They were pretty good. Of course, I'm not a specialist,
*  but you read them and you see this. It seems profound.
*  Yes. It seems reason. It's kind of cool. We also had a couple of projects where people tried to
*  teach AI how to play rock music, classical music, and popular music. Interestingly enough,
*  classical music was among the most difficult ones. Of course, if you look at the
*  grandmasters of music like Bach, there is a lot of almost math.
*  Yeah. Well, he's very mathematical.
*  Exactly. I would imagine that at least some style of this music could be picked up,
*  but then you have a completely different spectrum of classical composers. It's almost like you don't
*  have to look at the data. You just listen to it and say, nah, that's not it. Not yet.
*  That's how I feel too. Open AI has, I think, open muse or something like that, the system. It's cool,
*  but it's not compelling for some reason. It could be a psychological reason too. Maybe we need to
*  have a human being, a tortured soul behind the music. I don't know.
*  Yeah. No, absolutely. I completely agree. Whether or not one day we'll have a song written by an
*  AI engine to be in top charts, musical charts, I wouldn't be surprised. I wouldn't be surprised.
*  I wonder if we already have one, and it just hasn't been announced.
*  We wouldn't know. How hard is the multi-protein folding problem? Is that something you've
*  already mentioned, which is baked into this idea of greater and greater complexity of proteins?
*  Multi-domain proteins, does that basically become multi-protein complexes?
*  Yes. You got it right. It has the components of both of protein folding and protein-protein
*  interactions. Because in order for these domains, many of these proteins actually never form a stable
*  structure. One of my favorite proteins, and pretty much everyone who works with proteins,
*  they always have their favorite proteins. One of my favorite proteins, probably my favorite
*  protein, the one that I worked when I was a postdoc, is so-called post-synaptic density
*  95, PSD95 protein. It's one of the key actors in the majority of neurological processes at the
*  molecular level. Essentially, it's a key player in the post-synaptic density. This is the crucial
*  part of the synapse where a lot of these chemo-lector processes are happening. It has five
*  domains, five protein domains, pretty large proteins, I think 600 something.
*  But the way it's organized itself, it's flexible. It acts as a scaffold. It is used to bring in
*  other proteins so they start acting in the orchestrated manner. The shape of this protein,
*  in a way, there are some stable parts of this protein, but there are some flexible. This
*  flexibility is built into the protein in order to become this multifunctional machine.
*  Do you think that kind of thing is also learnable through the alpha-fold two kind of approach?
*  The time will tell.
*  Is it another level of complexity? How big of a jump in complexity is that whole thing?
*  To me, it's yet another level of complexity because when we talk about protein-protein
*  interactions, there is actually a different challenge for this called CAPRI. This is focused
*  specifically on macromolecular interactions, protein-protein, protein-DNA, etc.
*  There are different mechanisms that govern molecular interactions and that need to be
*  picked up, say, by a machine learning algorithm. Interestingly enough, we participated for a few
*  years in this competition. We typically don't participate in competitions. I don't know,
*  I don't have enough time because it's very intensive. It's a very intensive process.
*  But we participated back about 10 years ago or so. The way we entered this competition,
*  we designed a scoring function. The function that evaluates whether or not your protein-protein
*  interaction is supposed to look like experimentally solved. The scoring function is a very critical
*  part of the model prediction. We designed it to be a machine learning one. It was one of the first
*  machine learning-based scoring function used in CAPRI. We essentially learned what
*  should contribute, what are the critical components contributing into the protein-protein
*  interactions. This could be converted into a learning problem and thereby it could be learned.
*  I believe so, yes. Do you think AlphaFold2 or something similar to it from DeepMind or somebody
*  else will result in a Nobel Prize or multiple Nobel Prizes? It may be not so obviously,
*  you can't give a Nobel Prize to a computer program. At least for now, I'll give it to the
*  designers of that program. Do you see one or multiple Nobel Prizes where AlphaFold2
*  is like a large percentage of what that prize is given for? Would it lead to discoveries at the
*  level of Nobel Prizes? I think we are definitely destined to see the Nobel Prize becoming sort of
*  to be evolving with the evolution of science. Science is such that it now becomes like really
*  multifaceted. You don't really have a unique discipline, you have a lot of cross-disciplinary
*  talks in order to achieve really big advancements. I think the computational methods will be
*  acknowledged in one way or another. As a matter of fact, they were first acknowledged back in 2013,
*  where the first three people awarded the Nobel Prize for study of the protein folding,
*  the principle. I think all three of them are computational biophysicists.
*  I think that is unavoidable. It will come with the time. The fact that AlphaFold2
*  and similar approaches, because again, it's a matter of time that people will embrace this
*  principle and will see more and more such tools coming into play. But these methods
*  will be critical in a scientific discovery. No doubts about it.
*  On the engineering side, maybe a dark question, but do you think it's possible to use these
*  machine learning methods to start to engineer proteins? The next question is something quite
*  a few biologists are against, some are for study purposes, is to engineer viruses. Do you think
*  machine learning, something like AlphaFold could be used to engineer viruses? To answer the first
*  question, it has been a part of the research in the protein science. The protein design
*  is a very prominent area of research. One of the pioneers is David Baker and Rosetta algorithm that
*  essentially was doing the de novo design and was used to design new proteins.
*  Design of proteins means design of functions. When you design a protein, you can control,
*  the whole point of the protein, with the protein structure comes a function, like it's doing
*  something. Correct. So you can design different things. You can look at the proteins from the
*  functional perspective. You can also look at the proteins from the structural perspective,
*  the structural building blocks. If you want to have a building block of a certain shape,
*  you can try to achieve it by introducing a new protein sequence and predicting how it will fold.
*  With that, it's one of the natural applications of these algorithms. Now, talking about engineering
*  a virus. With machine learning. With machine learning. Luckily for us, we don't have that
*  much data. Right now, one of the projects that we are carrying on in the lab is we're trying to
*  develop a machine learning algorithm that determines whether or not the current strain
*  is pathogenic. The current strain of the coronavirus. Of the virus. There are applications
*  to coronaviruses because we have strains of SARS-CoV-2, also SARS-CoV-1, MERS that are
*  pathogenic, but we also have strains of other coronaviruses that are not pathogenic. The common
*  called viruses and some other ones. Pathogenic meaning spreading. Pathogenic
*  means actually inflicting damage. Correct. There are also some seasonal versus pandemic strains
*  of influenza. Determining what are the molecular determinants that are built in
*  into the protein sequence, into the gene sequence. Whether or not the machine learning can
*  determine those components. Oh, interesting. Using machine learning, that's really interesting.
*  The input is like what? The protein sequence. The protein sequence and then determine if this
*  thing is going to be able to do damage to a biological system. Yeah. So, I mean-
*  It's a good machine learning. You're saying we don't have enough data for that?
*  I mean, for this specific one, we do. We might actually have to back up on this because we're
*  still in the process. There was one work that appeared in bioarchive by Eugene Koonin,
*  who is one of these pioneers in evolutionary genomics. They tried to look at this, but the
*  methods were sort of standard supervised learning methods. Now the question is, can you
*  advance it further by using not so standard methods? There's obviously a lot of hope in
*  transfer learning, where you can actually try to transfer the information that the machine
*  learning learns about the proper protein sequences. So, there is some promise in going this direction,
*  but if we have this, it would be extremely useful because then we could essentially forecast
*  the potential mutations that would make a current strain more or less pathogenic.
*  Anticipate them from a vaccine development for the treatment, antiviral drug development.
*  That would be a very crucial task. But you could also use that system to then say,
*  how would we potentially modify this virus to make it more pathogenic?
*  That's true. Again, the hope is several things. One is that even if you design a sequence,
*  to carry out the actual experimental biology, to ensure that all the components working
*  is a completely different matter. Then we've seen in the past, there could be some regulation.
*  The moment the scientific community recognizes that it's now becoming no longer a fun puzzle
*  for machine learning, then there might be some regulation. So, I think back in 2015,
*  there was an issue on regulating the research on influenza strains. There were several groups
*  used mutation analysis to determine whether or not this strain will jump from one species to another.
*  I think there was a half a year moratorium on the research on the paper published until scientists
*  analyzed it and decided that it's actually safe. I forgot what that's called. Something of function,
*  test of function. Gain of function. Yeah, gain of function, loss of function. That's right. Sorry.
*  It's like, let's watch this thing mutate for a while to see what kind of things we can observe.
*  I guess I'm not so much worried about that kind of research if there's a lot of regulation and
*  if it's done very well and with competence and seriously. I am more worried about kind of this,
*  the underlying aspect of this question is more like 50 years from now.
*  Speaking to the Drake equation, one of the parameters in the Drake equation is how long
*  civilizations last. That seems to be the most important value actually for calculating if
*  there's other alien intelligence civilizations out there. That's where there's most variability.
*  Assuming if that percentage that life can emerge is not zero, if we're super unique,
*  then it's how long we last is basically the most important thing. From a selfish perspective,
*  but also from a Drake equation perspective, I'm worried about our civilization lasting.
*  You kind of think about all the ways in which machine learning can be used to design
*  greater weapons of destruction. One way to ask that if you look sort of 50 years from now,
*  100 years from now, would you be more worried about natural pandemics or engineered pandemics?
*  Like who is a better designer of viruses, nature or humans if we look down the line?
*  I think in my view, I would still be worried about the natural pandemics,
*  simply because I mean the capacity of the nature producing this.
*  It does a pretty good job, right?
*  Yes.
*  And the motivation for using engineering viruses as a weapon is a weird one because
*  maybe you can correct me on this, but it seems very difficult to target a virus. The whole point
*  of a weapon, the way a rocket works, if a starting point, you have an end point and you're trying to
*  hit a target, to hit a target with a virus is very difficult. It's basically just, the target
*  would be the human species. Oh man. Yeah. I have a hope in us. I'm forever optimistic that
*  there's insufficient evil in the world to lead to that kind of destruction.
*  Well, I also hope that, I mean, that's what we see. I mean, with the way we are getting connected,
*  the world is getting connected. I think it helps for the world to become more transparent.
*  Yeah. So the information spread is, I think it's one of the key things for the society
*  to become more balanced. Yeah.
*  One way or another. This is something that people disagree with me on, but
*  I do think that the kind of secrecy that governments have, so you're kind of speaking
*  more to the other aspects, like a research community being more open, companies are being
*  more open. Government is still like, we're talking about like military secrets. I think military
*  secrets of the kind that could destroy the world will become also a thing of the 20th century.
*  It'll become more and more open. Yeah. I think nations will lose power in the 21st century,
*  lose sufficient power to our secrecies. Transparency is more beneficial than secrecy.
*  But of course, it's not obvious. Let's hope so. Let's hope so that the
*  governments will become more transparent. So we last talked, I think, in March or April.
*  What have you learned? How has your philosophical, psychological, biological worldview
*  changed since then? Or you've been studying it nonstop from a computational biology perspective.
*  How has your understanding and thoughts about this virus changed over those months,
*  from the beginning to today? One thing that I was really amazed at how
*  efficient the scientific community was. Even just judging on this very narrow domain of
*  protein structure, understanding the structural characterization of this virus from the components
*  point of view, whole virus point of view. If you look at SARS, something that happened
*  less than 20, but close enough 20 years ago, and you see what, when it happened, what was
*  sort of the response by the scientific community. You see that the structural characterizations
*  did occur, but it took several years. Now, the things that took several years, it's a matter of
*  months. So we see that the research pop up. We are at the unprecedented level in terms of the
*  sequencing. Never before we had a single virus sequenced so many times. So which allows us to
*  actually trace very precisely the evolutionary nature of this virus, what happens. It's not just
*  this virus independently of everything. It's the sequence of this virus linked anchored to the
*  specific geographic place, to specific people. Because our genotype influences also the
*  evolution of this. It's always a host pathogen co-evolution that occurs. It'd be cool if we also
*  had a lot more data about the spread of this virus. It'd be nice if we had it for contact
*  tracing purposes for this virus, but it'd be also nice if we had it for the study for future
*  viruses to be able to respond and so on. But it's already nice that we have geographical data and
*  basic data from individual humans. Exactly. I think contact tracing is obviously a key
*  component in understanding the spread of this virus. There is also a number of challenges.
*  X-Prize is one of them we just recently took a part of this competition. It's the prediction
*  of the number of infections in different regions. Obviously, the AI is the main topic
*  in those predictions. Yeah, but it's still the data. That's the competition, but
*  the data is weak on the training. It's great. It's much more than probably before, but it'd be nice
*  if it was really rich. I talked to Michael Mina from Harvard. He dreams that the community comes
*  together with a weather map to where a virus is. Really high resolution sensors on how,
*  from person to person, the viruses that travel, all the different kinds of viruses.
*  There's a ton of them. Then you'd be able to tell the story that you've spoken about of the
*  evolution of these viruses, like day-to-day mutations that are occurring. That would be
*  fascinating just from a perspective of study and from the perspective of being able to respond to
*  future pandemics. That's ultimately what I'm worried about. People love books. Is there some
*  three or whatever number of books, technical fiction, philosophical, that brought you joy
*  in life, had an impact on your life, and maybe some that you would recommend others?
*  I'll give you three very different books. I also have a special runner-up.
*  Honorable matching.
*  It's an audiobook. There's some specific reason behind it. The first book is something that
*  impacted my earlier stage of life. I'm probably not going to be very original here. It's Bulgakov,
*  Smashter, and Margarita. For a Russian, maybe it's not super original, but it's a really
*  powerful book, even in English. It is incredibly powerful. The way it ends, I still have goosebumps
*  when I read the very last prologue, where it's just so powerful. What impact did it have on you?
*  What insights did you get from it? I was just taken by the fact that
*  you have those parallel lives apart from many centuries, and somehow they got sort of
*  intertwined into one story. That, to me, was fascinating. Of course, the
*  romantic part of this book is not just romance, it's the romance empowered by magic.
*  And maybe on top of that, you have some irony, which is unavoidable, because it was the Soviet
*  time. It's deeply Russian, so that's the wit, the humor, the pain, the love, all of that. It's
*  one of the books that captures something about Russian culture that people outside of Russia
*  should probably read. I agree. What's the second one? The second one is, again, another one that
*  it happened, I read it later in my life. I think I read it first time when I was a
*  graduate student, and that's the Solzhenitsyn's Cancer Ward. That is an amazingly powerful book.
*  CB What is it about?
*  I mean, it's essentially based on Solzhenitsyn was diagnosed with cancer when he was reasonably young,
*  and he made a full recovery. So this is about a person who was sentenced for life in one of these
*  camps, and he had some cancer, so he was transported back to one of these
*  Soviet republics, I think, South Asian republics. And the book is about
*  his experience being a prisoner, being a patient in the cancer clinic, in a cancer ward, surrounded
*  by people, many of which die. But in a way, the way it reads, I mean, first of all, later on, I
*  read the accounts of the doctors who describe the experiences in the book by the patient
*  as incredibly accurate. I read that there was some doctor saying that every single doctor
*  should read this book to understand what the patient feels. But again, as many of the
*  Solzhenitsyn's books, it has multiple levels of complexity. And obviously, if you look above
*  the cancer and the patient, I mean, the tumor that was growing and then disappeared in his
*  body with some consequences, I mean, this is allegorically the Soviet... And he actually,
*  when he was asked, he said that this is what made him think about how to combine these experiences.
*  It's fascinating.
*  Him being a part of the Soviet regime, also being a part of someone sent to Gulag camp,
*  and also someone who experienced cancer in his life. The Gulag archipelago and this book,
*  these are the works that actually made him receive a Nobel Prize. But to me, I've read
*  other books by Solzhenitsyn. This one to me is the most powerful one.
*  And by the way, both this one and the previous one you read in Russian?
*  Yes. So now there is the third book is an English book and it's completely different. So we're
*  switching the gears completely. So this is the book which... It's not even a book. It's an essay
*  by Jonathan Neumann called The Computer and the Brain. And that was the book he was writing
*  knowing that he was dying of cancer. So the book was released back. It's a very thin book,
*  but the intellectual power in this book, in this essay is incredible. You probably know that
*  von Neumann is considered to be one of the biggest thinkers. So his intellectual power
*  was incredible. And you can actually feel this power in this book where the person is writing
*  knowing that he will die. The book actually got published only after his death back in 1958.
*  He died in 1957. So he tried to put as many ideas that he still hadn't realized.
*  And so this book is very difficult to read because every single paragraph is just compact,
*  filled with these ideas. And the ideas are incredible. Even nowadays. So he tried to put
*  the parallels between the brain computing power, the neural system and the computers
*  as they were understood. Do you remember what year he was working on this? Like approximately?
*  57. So that was right when he was diagnosed with cancer and he was essentially...
*  Yeah, he's one of those... There's a few folks people mention. I think Ed Whitten is another
*  that like everyone that meets them, they say he's just an intellectual powerhouse.
*  Okay, so who is the honorable mention?
*  So, and this is, I mean, the reason I put it sort of in this separate section because this is a book
*  that I reasonably recently listened to. So it's an audio book. And this is a book called Lab Girl
*  by Hope Jaren. So Hope Jaren, she is a scientist. She's a geochemist that essentially studies
*  the fossil plants. And so she uses the chemical analysis to understand what was the climate
*  that back in thousands of years ago. And so something that incredibly touched me by this
*  book, it was narrated by the author. And it's an incredibly personal story, incredibly. So
*  certain parts of the book, you could actually hear the author crying. And that to me, I mean,
*  I never experienced anything like this, reading the book, but it was like the connection between
*  you and the author. And I think this is really a must read, but even better, a must listen
*  to audio book for anyone who wants to learn about sort of academia, science, research in general,
*  because it's a very personal account about her becoming a scientist.
*  So we're just before New Year's. We talked a lot about some difficult topics of viruses and so on.
*  Do you have some exciting things you're looking forward to in 2021? Some New Year's resolutions,
*  maybe silly or fun, or something very important and fundamental to the world of science or
*  something completely unimportant? Well, I'm definitely looking forward towards things
*  becoming normal. Right? So yes, so I really miss traveling. Every summer, I go to an
*  international summer school. It's called the School for Molecular and Theoretical Biology.
*  It's held in Europe. It's organized by very good friends of mine. And this is the school for gifted
*  kids from all over the world. And they're incredibly bright. It's like every time I go there,
*  it's like, you know, it's a highlight of the year. And we couldn't make it this August. So we did
*  this school remotely, but it's different. So I am definitely looking forward to next August coming
*  there. I also, I mean, you know, one of my personal resolutions, I realized that being in
*  you know, in house and working from home, you know, I realized that actually
*  I apparently missed a lot, you know, spending time with my family, believe it or not. So you
*  typically, you know, with all the research and, you know, and teaching and everything
*  related to the academic life, I mean, you get distracted. And so, you know, you don't feel
*  that, you know, the fact that you are away from your family doesn't affect you because you are,
*  you know, naturally distracted by other things. And, you know, this time I realized that, you know,
*  that that's so important, right? Spending your time with the family, with your kids.
*  And so that would be my New Year resolution and actually trying to spend as much time as possible.
*  Even when the world opens up. Yeah, that's a beautiful message. That's a beautiful reminder.
*  I asked you if there's a Russian poem you could read that I could force you to read. And you said,
*  okay, fine, sure. Do you mind reading? And you're like, you said that no paper needed.
*  Nope. So yeah, so this poem was written by my namesake, another Dmitri, Dmitri Kemmerfeld.
*  And, you know, it's a recent poem and it's called Sorceress,
*  Vedma in Russian, or actually, Koldunia. So that's sort of another sort of connotation of Sorceress
*  which and I really like it. And it's one of just a handful poems I actually can recall by heart.
*  I also have a very strong association when I read this poem with Master Margarita,
*  the main female character, Margarita. And also it's, you know, it's about, you know, it's happening
*  about the same time we're talking now. So around new year, around Christmas.
*  Do you mind reading it in Russian? I'll give it a try.
*  The wind was whistling in the New Year's balls, And under your power, the witch's,
*  The souls were dying, And the worlds were spinning.
*  So you took your eyes, your rage, That anyone who was willing to give thanks,
*  Was ready to give the soul to the devil For this witchly connection, without a glance.
*  The raven was laughing on the slopes, And I, without any prejudice and shirts,
*  Ran out to feel your amazed breath on your lips. So that the skin, tongue, rib,
*  and the cool on the other person's already on the ghostly ground, Reminds you of when you flew over the
*  ground in the white in the South, white in the mouth, white in the fog.
*  Yes, to me, it has a lot of meaning about, you know, this something that
*  is happening, something that is far away, but still very close to you. And yes, it's the winter.
*  There's something magical about winter, isn't it? What is the, well, I don't know. I don't know how
*  to translate it, but a kiss in winter is interesting. Lips in winter and all that kind of stuff is
*  beautifully, I mean, Russian as a way, as a reason Russian poetry is just, I'm a fan of poetry in
*  both languages, but English doesn't capture some of the magic that Russian seems to. So
*  thank you for doing that. That was awesome. Dmitry, it's great to talk to you again.
*  It's contagious how much you love what you do, how much you love life.
*  So I really appreciate you taking the time to talk today.
*  And thank you for having me.
*  Thanks for listening to this conversation with Dmitry Korkin. And thank you to our sponsors,
*  Brave Browser, NetSuite Business Management Software, Magic Spoon Low Carb Cereal, and
*  Asleep Self-Cooling Mattress. So the choice is browsing privacy, business success, healthy diet,
*  or comfortable sleep. Choose wisely, my friends. And if you wish, click the sponsor links below to
*  get a discount and to support this podcast. And now let me leave you with some words
*  from Jeffrey Eugenides. Biology gives you a brain. Life turns it into a mind.
*  Thank you for listening and hope to see you next time.

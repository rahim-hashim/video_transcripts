---
Date Generated: October 31, 2024
Transcription Model: whisper medium 20231117
Length: 7742s
Video Keywords: ['dmitry korkin', 'bioinformatics', 'biology', 'covid-19', 'artificial intelligence', 'agi', 'ai', 'ai podcast', 'artificial intelligence podcast', 'lex fridman', 'lex podcast', 'lex mit', 'lex ai', 'lex jre', 'mit ai']
Video Views: 67399
Video Rating: None
Video Description: Dmitry Korkin is a professor of bioinformatics and computational biology at Worcester Polytechnic Institute, where he specializes in bioinformatics of complex disease, computational genomics, systems biology, and biomedical data analytics. I came across Dmitry's work when in February his group used the viral genome of the COVID-19 to reconstruct the 3D structure of its major viral proteins and their interactions with human proteins, in effect creating a structural genomics map of the coronavirus and making this data open and available to researchers everywhere. We talked about the biology of COVID-19, SARS, and viruses in general, and how computational methods can help us understand their structure and function in order to develop antiviral drugs and vaccines.

Support this podcast by signing up with these sponsors:
- Cash App - use code "LexPodcast" and download:
- Cash App (App Store): https://apple.co/2sPrUHe
- Cash App (Google Play): https://bit.ly/2MlvP5w

EPISODE LINKS:
Dmitry's Website: http://korkinlab.org/
Dmitry's Twitter: https://twitter.com/dmkorkin
Dmitry's Paper that we discuss: https://bit.ly/3eKghEM

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
2:33 - Viruses are terrifying and fascinating
6:02 - How hard is it to engineer a virus?
10:48 - What makes a virus contagious?
29:52 - Figuring out the function of a protein
53:27 - Functional regions of viral proteins
1:19:09 - Biology of a coronavirus treatment
1:34:46 - Is a virus alive?
1:37:05 - Epidemiological modeling
1:55:27 - Russia
2:02:31 - Science bobbleheads
2:06:31 - Meaning of life

CONNECT:
- Subscribe to this YouTube channel
- Twitter: https://twitter.com/lexfridman
- LinkedIn: https://www.linkedin.com/in/lexfridman
- Facebook: https://www.facebook.com/LexFridmanPage
- Instagram: https://www.instagram.com/lexfridman
- Medium: https://medium.com/@lexfridman
- Support on Patreon: https://www.patreon.com/lexfridman
---

# Dmitry Korkin Computational Biology of Coronavirus  Lex Fridman Podcast #90
**Lex Fridman:** [April 22, 2020](https://www.youtube.com/watch?v=CwyOUS8TSl0)
*  The following is a conversation with Dmitriy Korkin.
*  He's a professor of bioinformatics and computational biology at WPI,
*  Worcester Polytechnic Institute, where he specializes in bioinformatics of complex diseases,
*  computational genomics, systems biology, and biomedical data analytics.
*  I came across Dmitriy's work when in February his group used the viral genome of the COVID-19
*  to reconstruct the 3D structure of its major viral proteins and their interaction with the
*  human proteins. In effect, creating a structural genomics map of the coronavirus and making this
*  data open and available to researchers everywhere. We talked about the biology of COVID-19,
*  SARS, and viruses in general, and how computational methods can help us understand
*  their structure and function in order to develop antiviral drugs and vaccines.
*  This conversation was recorded recently in the time of the coronavirus pandemic.
*  For everyone feeling the medical, psychological, and financial burden of this crisis,
*  I'm sending love your way. Stay strong. We're in this together. We'll beat this thing.
*  This is the Artificial Intelligence Podcast. If you enjoy it, subscribe on YouTube,
*  review it with 5 stars on Apple Podcasts, support it on Patreon, or simply connect with me on
*  Twitter at Lex Friedman, spelled F-R-I-D-M-A-N. This show is presented by Cash App, the number
*  one finance app in the App Store. When you get it, use code Lex Podcast. Cash App lets you send
*  money to friends, buy bitcoin, and invest in the stock market with as little as $1. Since Cash App
*  allows you to buy bitcoin, let me mention that cryptocurrency in the context of the history of
*  money is fascinating. I recommend Ascent of Money as a great book on this history. Debit and credits
*  on ledgers started around 30,000 years ago. The US dollar created over 200 years ago. And bitcoin,
*  the first decentralized cryptocurrency, released just over 10 years ago. So given that history,
*  cryptocurrency is still very much in its early days of development, but is still aiming to,
*  and just might, redefine the nature of money. So again, if you get Cash App from the App Store,
*  Google Play, and use the code Lex Podcast, you get $10, and Cash App will also donate $10 to First,
*  an organization that is helping to advance robotics and STEM education for young people
*  around the world. And now, here's my conversation with Dimitri Korkin.
*  When I think about viruses, I think about them, I mean, I imagine them as those villains that
*  do their work so perfectly well. That is impossible not to be fascinated with them.
*  LW So what do you imagine when you think about a virus? Do you imagine the individual,
*  sort of these 100 nanometer particle things? Or do you imagine the whole pandemic, like society level,
*  the, when you say the efficiency at which they do their work, do you think of viruses
*  as the millions that occupy human body or living organism, society level, like spreading as a
*  pandemic, or do you think of the individual little guy? DL Yes, this is, I think this is a unique,
*  a unique concept that allows you to move from microscale to the macroscale.
*  So the virus itself, I mean, it's not a living organism. It's a machine to me. It's a machine,
*  but it is perfected to the way that it essentially has a limited number of functions
*  it needs to do, necessary functions. And it essentially has enough information
*  just to do those functions, as well as the ability to modify itself.
*  LW So, you know, it's, it's a machine. It's an intelligent machine.
*  DL So yeah, look, maybe on that point, you're in danger of reducing the power of this thing
*  by calling it a machine, right? But you now mentioned that it's also possibly intelligent.
*  It seems that there's these elements of brilliance that a virus has, of intelligence,
*  of maximizing so many things about its behavior and to ensure its survival and its success. So
*  do you see it as intelligent? LW So, you know, I think the,
*  it's a different, I understand it differently than, you know, I think about, you know, intelligence
*  of humankind or intelligence of the, you know, of the artificial intelligence mechanisms.
*  I think the intelligence of a virus is in its simplicity. The ability to do so much
*  with so little material and information. But also, I think it's interesting. It keeps me thinking,
*  you know, it keeps me wondering whether or not it's also the, an example of
*  of the basic swarm intelligence where, you know, essentially the viruses act as the whole
*  and they're extremely efficient in that. DL So what do you attribute the incredible
*  simplicity and the efficiency to? Is it the evolutionary process? So maybe another way to
*  ask that if you look at the next hundred years, are you more worried about the natural
*  pandemics or the engineered pandemics? So how hard is it to build a virus?
*  LW Yes, it's a very, very interesting question because obviously there's a lot of conversations
*  about the, you know, whether we are capable of engineering
*  a, you know, an even worse virus. I personally expect and am mostly concerned with the
*  naturally occurring viruses simply because we keep seeing that. We keep seeing new strains of
*  influenza emerging, some of them becoming pandemic. We keep seeing new strains of
*  coronaviruses emerging. This is a natural process and I think this is why it's so powerful.
*  You know, if you ask me, you know, I've read papers about scientists trying to study
*  the capacity of the modern, you know, biotechnology to alter the viruses,
*  but I hope that, you know, it won't be our main concern in the near future.
*  CB What do you mean by hope?
*  LW Well, you know, if you look back and look at the history of the most dangerous viruses,
*  right? So the first thing that comes into mind is smallpox. So right now there is
*  perhaps a handful of places where these, you know, the strains of this virus are stored,
*  right? So this is essentially the effort of the whole society to limit the access to those
*  viruses.
*  CB You mean in the lab, in the controlled environment in order to study. And then smallpox
*  is one of the viruses for which should be stated. There's a vaccine is developed.
*  LW Yes. Yes. And that's, you know, until 70s, I mean, in my opinion, it was perhaps the most
*  dangerous thing that was there.
*  Is that a very different virus than the influenza and coronaviruses?
*  LW It is. It is different in several aspects. Biologically, it's a so-called double-stranded
*  DNA virus, but also in the way that it is much more contagious. So the R0 for so this is this is
*  the R0 is essentially an average number as person infected by the virus can spread to other people.
*  So then the average number of people that he or she can, you know, spread it to. And, you know,
*  there is still some, you know, discussion about the estimates of the current virus.
*  You know, the estimations vary between, you know, 1.5 and 3. In case of smallpox, it was 5 to 7.
*  LW And we're talking about the exponential growth, right? So that's a very big difference.
*  It's not the most contagious one. Measles, for example, it's, I think, 15 and up. So it's, you
*  know, but it's definitely, definitely more contagious that the seasonal flu than
*  the current coronavirus or SARS for that matter. So.
*  LW What makes a virus more contagious? I'm sure there's a lot of variables that come into play,
*  but is it that whole discussion of aerosol and like the size of droplets, if it's airborne,
*  or is there some other stuff that's more biology-centered? LW I mean, there are a lot
*  of components and there are biological components that there are also, you know, social components.
*  The ability of the virus to, you know, so the ways in which the virus is spread is definitely one.
*  The ability to virus to stay on the surfaces, to survive. The ability of the virus to replicate
*  fast. So, you know. LW Or once it's in the cell or whatever.
*  LW Once it's inside the host. And interestingly enough, something that I think we didn't pay
*  that much attention to is the incubation period, where, you know, hosts are symptomatic. And now
*  it turns out that another thing that we, one really needs to take into account
*  the percentage of the symptomatic population, because those people still shed this virus and
*  they still are contagious. LW I saw there's an Iceland study,
*  which I think is probably the most impressive size-wise, shows 50% asymptomatic for this virus.
*  I also recently learned the swine flu is like the, just the number of people who got infected
*  was in the billions. It was some crazy number. It was like, it was like, like 20% of the population,
*  30% of the population, something crazy like that. So the lucky thing there is the fatality
*  rate is low. But the fact that a virus can just take over an entire population so quickly,
*  it's terrifying. LW I think, I mean, this is, you know,
*  that's perhaps my favorite example of a butterfly effect. Because it's really, I mean, it's even
*  tinier than a butterfly. And look at, you know, and with, you know, if you think about it, right,
*  so it used to be in those bat species. And perhaps because of, you know, a couple of small
*  changes in the viral genome, it first had, you know, become capable of jumping from bats to
*  human. And then it became capable of jumping from human to human. Right? So this is, I mean,
*  it's not even the size of a virus, it's the size of several, you know, several atoms or so,
*  you know, a few atoms. And all of a sudden, this change has such a major impact.
*  LW So is that a mutation like on a single virus? Is that like, so if we talk about those,
*  the flap of a butterfly wing, like what's the first flap?
*  CB Well, I think this is the mutations that make, that made this virus
*  capable of jumping from bat species to human. Of course, there's, you know, the scientists are
*  still trying to find, I mean, they're still even trying to find the who was the first infected,
*  right? The patient zero. LW The first human.
*  CB The first human infected, right? I mean, the fact that there are coronaviruses,
*  different strains of coronaviruses in various bat species, I mean, we know that. So we,
*  you know, virologists observed them, they studied them, they look at their genomic sequences,
*  they're trying, of course, to understand what make these viruses to jump from bats to human.
*  There was, you know, similar to that, and, you know, in influenza, there was, I think,
*  a few years ago, there was this, you know, interesting story where several groups of
*  scientists studying influenza virus essentially, you know, made experiments to show that this virus
*  can jump from one species to another, you know, by changing, I think, just a couple of residues.
*  And, of course, it was very controversial. I think there was a moratorium on this study for a while,
*  but then the study was released, it was published.
*  LW So why was there a moratorium? Because it shows through engineering it, through modifying it,
*  you can make it jump. I personally think it is important to study this. I mean, we should be
*  informed, we should try to understand as much as possible in order to prevent it.
*  But so then the engineering aspect there is, can't you then just start searching, because there's so
*  many strands of viruses out there, can't you just search for the ones in bats that are the deadliest
*  from the virologist's perspective and then just try to engineer, try to see how to.
*  But see, there's a nice aspect to it. The really nice thing about engineering viruses,
*  it has the same problem as nuclear weapons, is it's hard for it to not lead to mutual self-destruction.
*  So you can't control a virus, it can't be used as a weapon, right?
*  CB Yeah, that's why in the beginning I said I'm hopeful, because there are definitely regulations
*  needed to be introduced. And I mean, as the scientific society is, we are in charge of
*  you know, making the right actions, making the right decisions. But I think we will benefit
*  tremendously by understanding the mechanisms by which the virus can jump, by which the virus can
*  become more dangerous to humans. Because all these answers would eventually lead to designing
*  better vaccines, hopefully universal vaccines, right? And that would be a triumph of science.
*  So what's the universal vaccine? So is that something that, how universal is universal?
*  I mean, you know, so- What's the dream, I guess,
*  because you kind of mentioned the dream of this.
*  I would be extremely happy if, you know, we designed the vaccine that is able. I mean,
*  I'll give you an example, right? So every year we do a seasonal flu shot. The reason we do it
*  is because, you know, we are in the arms race, you know, our vaccines are in the arms race with
*  constantly changing virus, right? Now, if the next pandemic, influenza pandemic will
*  occur, most likely this vaccine would not save us, right? Although it's the same virus,
*  might be different strain. So if we're able to essentially design a vaccine against, you know,
*  influenza A virus, no matter what's the strain, no matter which species did a jump from,
*  that would be, I think that would be a huge, huge progress and advancement.
*  You mentioned smallpox until the seventies might've been something that you would be
*  worried the most about. What about these days? Well, we're sitting here in the middle of a
*  COVID-19 pandemic, but these days, nevertheless, what is your biggest worry virus wise?
*  What are you keeping your eye out on?
*  And, you know, based on the past several years of the new viruses emerging, I think we're still
*  dealing with different types of influence. I mean, so the H7N9 avian flu that emerged, I think,
*  a couple of years ago in China, I think the mortality rate was incredible. I mean, it was,
*  you know, I think above 30%. So this is huge. I mean, luckily for us,
*  this strain was not pandemic, right? So it was jumping from birds to human,
*  but I don't think it was actually transmittable between the humans.
*  And, you know, this is actually a very interesting question which scientists try to understand,
*  right? So the balance, the delicate balance between the virus being very contagious, right? So
*  efficient in spreading and virus to be very pathogenic, you know, causing, you know,
*  you know, harms and deaths to the host. So it looks like that the more pathogenic the virus is,
*  the less contagious it is. Is that a property of biology or what is it?
*  What is the big... I don't have an answer to that. And I think this is still an open question.
*  But, you know, if you look at, you know, with the coronavirus, for example, if you look at,
*  you know, the deadlier relative MERS, MERS was never a pandemic virus.
*  Right. But the, you know, again, the mortality rate from MERS is far above,
*  you know, I think 20 or 30%. So.
*  So whatever is making this all happen doesn't want us dead.
*  Because it's balancing out nicely. I mean, how do you explain that we're not dead yet?
*  Like, because there's so many viruses and they're so good at what they do.
*  Why do they keep us alive? I mean, we also have, you know, a lot of protection, right? So we do
*  the immune system. And so, I mean, we do have, you know, ways to fight against those viruses.
*  And I think with the... Now we're much better equipped, right? So with the discoveries of
*  vaccines and, you know, there are vaccines against the viruses that maybe 200 years ago would
*  wipe us out completely. But because of these vaccines, we are actually, we are capable of
*  eradicating pretty much fully, as is the case with smallpox.
*  So if we could, can we go to the basics a little bit of the biology of the virus?
*  How does a virus infect the body? So I think there are some key steps
*  that the virus needs to perform. And of course, the first one, the viral particle
*  needs to get attached to the host cell. In the case of coronavirus, there's a lot of evidence that
*  it actually interacts in the same way as the SARS coronavirus. So it gets attached to AC2
*  human receptor. And so there is, I mean, as we speak, there is a growing number of papers
*  suggesting it. Moreover, most recent, I think most recent results suggest that this virus attaches
*  more efficiently to this human receptor than SARS. So just to sort of back off,
*  so there is a family of viruses, the coronaviruses, and SARS, whatever the heck for that,
*  whatever that stands for. So SARS actually stands for the disease that you get,
*  is the syndrome of acute respiratory syndrome. So SARS is the first strand, and then there's MERS.
*  And there is, yes, scientists actually know more than three strands. I mean, so there is the MHV
*  strain, which is considered to be a canonical disease model in mice. And so there is a lot
*  of work done on this virus because it's- But it hasn't jumped to humans yet?
*  No, no. Oh, interesting.
*  Yes. That's fascinating. So, and then you mentioned AC2. So when you say attach,
*  proteins are involved on both sides. Yes. So we have this infamous spike protein on the surface of
*  the virion particle, and it does look like a spike. And I mean, that's essentially because of
*  this protein, we call the coronavirus coronavirus. So that what makes corona on top of the surface.
*  So this protein, it actually, it acts, so it doesn't act alone. It actually, it makes three copies,
*  and it makes so-called trimer. So this trimer is essentially a functional unit, a single functional
*  unit that starts interacting with the AC2 receptor. So this is again, another protein that now sits on
*  the surface of a human cell, a host cell, I would say. And that's essentially in that way, the virus
*  anchors itself to the host cell, because then it needs to actually, it needs to get inside.
*  It fuses its membrane with the host membrane. It releases the key components. It releases its
*  RNA, and then essentially hijacks the machinery of the cell, because none of the viruses that we know
*  of have ribosome, the machinery that allows us to print out proteins. So in order to print out
*  proteins that are necessary for functioning of this virus, it actually needs to hijack the host
*  ribosomes. So a virus is an RNA wrapped in a bunch of proteins, one of which is this functional
*  mechanism of a spike protein that does the attachment. So yeah, so if you look at this
*  virus, there are several basic components. So we start with the spike protein. This is not the only
*  surface protein, the protein that lives on the surface of the viral particle. There is also
*  perhaps the protein with the highest number of copies is the membrane protein. So it essentially
*  forms the envelope of the viral particle and essentially helps to maintain a certain curvature,
*  helps to make a certain curvature. Then there is another protein called envelope protein or
*  E protein, and it actually occurs in far less quantities. And still there is ongoing research
*  what exactly does this protein do. So these are the three major surface proteins that make the
*  the viral envelope. And when we go inside, then we have another structural protein called
*  nuclear protein. And the purpose of this protein is to protect the viral RNA.
*  It actually binds to the viral RNA, creates a capsid. And so the rest of the viral information
*  is inside of this RNA. And if you compare the amount of the genes or proteins that are made
*  of these genes, it's significantly higher than of influenza virus, for example. Influenza virus has,
*  I think, around eight or nine proteins where this one has at least 29.
*  RG Wow, that has to do with the length of the RNA strand.
*  MP So I mean, so it affects the length of the RNA strand, right? So because you essentially need to
*  have sort of the minimum amount of information to encode those genes.
*  RG How many proteins did you say?
*  29. So this is something definitely interesting because, believe it or not, we've been studying
*  coronaviruses for over two decades. We've yet to uncover all functionalities of these proteins.
*  RG Could we maybe take a small tangent? And can you
*  say how one would try to figure out what a function of a particular protein is?
*  So you've mentioned people are still trying to figure out what the function of the envelope
*  protein might be or what's the process? MP So this is where the research that
*  computational scientists do might be of help because in the past several decades,
*  we actually have collected a pretty decent amount of knowledge about different proteins
*  in different viruses. So what we can actually try to do, and this could be our first lead
*  to a possible function, is to see whether those, say we have this genome of the coronavirus,
*  of the null coronavirus, and we identify the potential proteins. Then in order to infer the
*  function, what we can do, we can actually see whether those proteins are similar to those ones
*  that we already know. In such a way, we can, for example, clearly identify some critical components
*  that RNA polymerase or different types of proteases, these are the proteins that essentially
*  clip the protein sequences. So this works in many cases. However, in some cases, you have truly novel
*  proteins, and this is a much more difficult task.
*  CB Now as a small pause, when you say similar, what if some parts are different and some parts
*  are similar? How do you disentangle that? MP It's a big question. Of course, what bioinformatics does,
*  it does predictions. So those predictions, they have to be validated by experiments.
*  CB Functional or structural predictions?
*  MP Both. I mean, we do structural predictions, we do functional predictions, we do
*  interactions predictions.
*  CB So this is interesting. So you just generate a lot of
*  predictions, like reasonable predictions based on structure and function interaction, like you said,
*  and then here you go. That's the power of bioinformatics, is data grounded,
*  good predictions of what should happen.
*  MP So in a way, I see it. We're helping experimental scientists to streamline
*  their discovery process.
*  CB And the experimental scientists, is that what a virologist is?
*  MP So yeah, virology is one of the experimental sciences that focus on viruses.
*  They often work with other experimental scientists, for example, the molecular imaging
*  scientists. So the viruses often can be viewed and reconstructed through
*  electron microscopy techniques. But these are specialists that are not necessarily virologists.
*  They work with small particles, whether it's viruses or it's an organelle of a human cell,
*  whether it's a complex molecular machinery. So the techniques that are used are very similar
*  in their essence. So typically, we see it now, the research that is emerging and that is needed
*  involves the collaborations between virologists, biochemists, people from pharmaceutical sciences,
*  computational sciences. So we have to work together.
*  So from my perspective, just a step back, sometimes I look at this stuff,
*  how much we understand about RNA and DNA, how much we understand about protein, like your work,
*  the amount of proteins that you're exploring. Is it surprising to you that we were able,
*  we descendants of apes, were able to figure all of this out? So you're a computer scientist.
*  So for me, from a computer science perspective, I know how to write a Python program,
*  things are clear, but biology is a giant mess, it feels like to me from an outsider's perspective.
*  How surprising is it, amazing is it that we were able to figure this stuff out?
*  If you look at how computational science and computer science was evolving,
*  I think it was just a matter of time that we would approach biology. So we started from
*  applications to much more fundamental systems, physics, small chemical compounds.
*  All right, so now we are approaching the more complex biological systems.
*  And I think it's a natural evolution of the computer science, of mathematics.
*  So sure, that's the computer science side. I just meant even in higher level. So that to me is
*  surprising that computer science can offer help in this messy world. But I just mean it's incredible
*  that the biologists and the chemists can figure all this out. Or does it just sound ridiculous
*  to you that of course they would? It just seems like a very complicated set of problems. The
*  variety of the kinds of things that could be produced in the body. Just like you said,
*  29 proteins, just getting a hang of it so quickly, it just seems impossible to me.
*  I agree. I have to say we are in the very, very beginning of this journey.
*  We've yet to comprehend, not even try to understand and figure out all the details,
*  but we've yet to comprehend the complexity of the cell.
*  We know that neuroscience is not even at the beginning of understanding the human mind.
*  So where does biology sit in terms of deeply understanding the function of viruses and cells?
*  So sometimes it's easy to say when you talk about function, what you really refer to
*  is perhaps not a deep understanding, but more of an understanding sufficient to be able to mess with
*  it using a chemical to prevent some of its function. Or do you understand the function?
*  I think we are much further in terms of understanding of the complex genetic disorders,
*  such as cancer, where you have layers of complexity. In my laboratory, we're trying
*  to contribute to that research, but we're also overwhelmed with how many different layers of
*  complexity, different layers of mechanisms that can be hijacked by cancer simultaneously.
*  And so I think biology in the past 20 years, again, from the perspective of the outsider,
*  because I'm not a biologist, but I think it has advanced tremendously. And one thing that
*  where computational scientists and data scientists are now becoming very helpful
*  is coming from the fact that we are now able to generate a lot of information about the cell,
*  whether it's next-generation sequencing or transcriptomics, whether it's life imaging
*  information where it is complex interactions between proteins or between proteins and small
*  molecules such as drugs. We are becoming very efficient in generating this information.
*  And now the next step is to become equally efficient in
*  processing this information and extracting the key knowledge from that.
*  That could then be validated with experiment. So maybe then going all the way back, you said
*  the first step is seeing if we can match the new proteins you found in the virus against something
*  we've seen before to figure out its function. And then you also mentioned that, but there could be
*  cases where it's a totally new protein. Is there something bioinformatics can offer when it's a
*  totally new protein? This is where many of the methods, and you probably are aware of the case
*  of machine learning, many of these methods rely on the previous knowledge. So things where we
*  tried to do from scratch are incredibly difficult, something that we call ab initio.
*  It's not just the function. We've yet to have a robust method to predict the structures of these
*  proteins in ab initio by not using any templates of other related proteins.
*  Protein is a chain of amino acids. It's residues.
*  Residues, yeah. And then somehow, magically, maybe you can tell me, they seem to fold in incredibly
*  weird and complicated 3D shapes. Yes.
*  That's where actually the idea of protein folding, or just not the idea, but the problem of figuring
*  out how they fold into those weird shapes comes in. So that's another side of computational work.
*  Can you describe what protein folding from the computational side is, and maybe your thoughts
*  on the folding at home efforts that a lot of people know that you can use your machine to
*  do protein folding? Protein folding is one of those $1 million price
*  challenges. So the reason for that is we've yet to understand precisely
*  how the protein gets folded so efficiently to the point that in many cases where you
*  try to unfold it due to the high temperature, it actually folds back into its original state.
*  We know a lot about the mechanisms, but putting those mechanisms together
*  and making sense, it's computationally a very expensive task.
*  LR. In general, can proteins fold in an arbitrary large number of ways,
*  or do they usually fold in a very small number of ways?
*  It's typically. We tend to think that there is one canonical fold for a protein, although there
*  are many cases where the proteins upon destabilization, it can be folded into a
*  different conformation. And this is especially true when you look at proteins that include
*  more than one structural unit. So those structural units, we call them protein domains.
*  Essentially, protein domain is a single unit that typically is evolutionary preserved,
*  that typically carries out a single function, and typically has a very distinct fold,
*  3D structure organization. But it turns out that if you look at human, an average protein
*  in a human cell would have a bit of two or three such subunits, and how they are trying to
*  fold into the next level fold. And then they fold into the larger 3D structure.
*  LR. And all of that, there's some understanding of the basic mechanisms,
*  but not to put together to be able to fold it.
*  LR. We're still struggling. We're getting pretty good about folding relatively small proteins,
*  up to 100 residues, but we're still far away from folding larger proteins. And some of them are
*  notoriously difficult. For example, transmembrane proteins, proteins that sit in the membranes
*  of the cell, they're incredibly important, but they are incredibly difficult to solve.
*  LR. And so basically, there's a lot of degrees of freedom, how it folds. And so it's a combinatorial
*  problem where it just explodes. There's so many dimensions.
*  Well, it is a combinatorial problem, but it doesn't mean that we cannot approach it from the
*  not from the brute force approach. And so the machine learning approaches
*  have been emerged that try to tackle it.
*  LR. So folding at home, I don't know how familiar you are with it, but
*  is that using machine learning or is it more brute force?
*  No. So folding at home, it was originally, and I remember, it was a long time ago, I was a postdoc
*  and we learned about this game because it was originally designed as the game. And I took a
*  look at it and it's interesting because it's very transparent, very intuitive. And from what I heard
*  I've yet to introduce it to my son, but kids are actually getting very good at folding the proteins.
*  And it came to me not as a surprise, but actually as the manifest of our capacity
*  to solve these kinds of problems when a paper was published in one of these top journals
*  with the co-authors being the actual players of this game. And what happened was that they managed
*  to get better structures than the scientists themselves. It was a profound revelation that
*  problems that are so challenging for a computational science may be not that
*  challenging for a human brain. LR. Well, that's a really good,
*  that's a hopeful message always when there's the proof of existence, the existence proof that it's
*  possible. That's really interesting. But it seems, what are the best ways to do protein folding now?
*  So if you look at what DeepMind does with AlphaFold, so that's a learning approach.
*  What's your sense? I mean, your background is in machine learning, but is this a learnable problem?
*  Is this still a brute force? Are we in the Gary Kasparov Deep Blue days or are we in the Alpha Go
*  playing the game of Go days of folding? KS. Well, I think we are advancing towards
*  this direction. I mean, if you look, so there is sort of Olympic game for protein folders called CASP.
*  And it's essentially, it's a competition where different teams are given exactly the same
*  protein sequences and they try to predict their structures. And of course, there are different
*  subtasks, but in the recent competition, AlphaFold was among the top performing teams, if not the top
*  performing team. So there is definitely a benefit from the data that have been generated
*  in the past several decades, the structural data. And certainly, we are now at the capacity
*  to summarize this data, to generalize this data and to use those principles in order to predict
*  protein structures. That's one of the really cool things here is there's, maybe you can comment on
*  it. There seems to be these open data sets of protein. How did that, what the protein data bank,
*  the protein data bank. I mean, that's crazy. Is this a recent thing for just the coronavirus?
*  It's been for many, many years. I believe the first protein data bank was designed on flashcards.
*  So yes, this is a great example of the community efforts of everyone contributing. Because every
*  time you solve a protein or a protein complex, this is where you submit it. And the scientists
*  get access to it. Scientists get to test it. And we, my informaticians, use this information
*  to make predictions. So there's no culture of hoarding discoveries here. So you've released
*  a few or a bunch of proteins that are matching, whatever. We'll talk about the details a little
*  bit. But it's kind of amazing how open the culture here is.
*  It is. And I think this pandemic actually demonstrated the ability of scientific community
*  to solve this challenge collaboratively. And I think if anything, it actually moved us to a
*  brand new level of collaborations of the efficiency in which people establish new collaborations,
*  in which people offer their help to each other. Scientists offer their help to each other.
*  And publishers also. It's very interesting. We're now trying to figure out, there's a few
*  journals that are trying to sort of do the very accelerated review cycle, but so many preprints.
*  So just posting a paper going out, I think it's fundamentally changing the way we think about
*  papers. Yes. I mean, the way we think about knowledge, let's say. Because yes, I completely
*  agree. I think now the knowledge is becoming sort of the core value, not the paper or the journal
*  where this knowledge is published. And I think this is, again, we are living in the times where
*  it becomes really crystallized, the idea that the most important value is in the knowledge.
*  So maybe you can comment, what do you think the future of that knowledge sharing looks like? So
*  you have this paper that I hope we'll get a chance to talk about a little bit.
*  But it has a really nice abstract and introduction. It has all the usual, I mean,
*  probably took a long time to put together. But is that going to remain? You could have communicated
*  a lot of fundamental ideas here in a much shorter amount that's less traditionally acceptable by the
*  journal context. So the first version that we
*  posted, not even on the bio archive, because bio archive back then, it was essentially
*  overwhelmed with the number of submissions. So our submission, I think it took five or six days
*  just for it to be screened and put online. So essentially we put the first preprint
*  on our website and it started getting accessed right away.
*  So this original preprint was in a much rougher shape than this paper. But we tried, I mean,
*  we honestly tried to be as compact as possible with introducing the information that is necessary
*  to explain our results. So maybe we can dive right in if it's okay.
*  Sure. So it's a paper called Structural Genomics of SARS-CoV-2. How do you even pronounce?
*  SARS-CoV-2. By the way, COVID is such a terrible name, but it's stuck. Anyway,
*  SARS-CoV-2 indicates evolutionary conserved functional regions of viral proteins.
*  So this is looking at all kinds of proteins that are part of
*  this novel coronavirus and how they match up against the previous other kinds of coronaviruses.
*  There's a lot of beautiful figures. I was wondering if you could,
*  I mean, there's so many questions I could ask here, but maybe at the,
*  how do you get started doing this paper? So how do you start to figure out the 3D structure of
*  novel virus? Yes. So there is actually a little story behind it. And so the story actually dated
*  back in September of 2019. And you probably remember that back then we had another dangerous
*  virus, triple E virus, it's a Queen encephalitis virus. Can you maybe linger on it? I have to
*  admit I was sadly completely unaware. So that was actually a virus outbreak
*  that happened in New England only. The danger in this virus was that it actually targeted your
*  brain. So the word S from this virus, the main vector was mosquitoes. And obviously, full time
*  is the time where you have a lot of them in New England. And on one hand, people realized this
*  is actually a very dangerous thing. So it had an impact on the local economy. The schools were
*  closed past six o'clock, no activities outside for the kids because the kids were suffering
*  quite tremendously from, when infected from this virus. How do I not know about this? Was
*  universities impacted? It was in the news. I mean, it was not impacted to a high degree in Boston,
*  necessarily, but in the Metro West area and actually spread around, I think, all the way to
*  all the way to New Hampshire, Connecticut. And you mentioned affecting the brain. That's one
*  other comment we should make. So you mentioned AC2 for the coronavirus. So these viruses kind of
*  attach to something in the body. So it essentially attaches to these proteins
*  in those cells in the body where those proteins are expressed, where they actually have them
*  in abundance. So sometimes that could be in the lungs, that could be in the brain.
*  That could be. So I think what they, right now, from what I read, they have the epithelial cells
*  inside. So the cells essentially inside the cells that are covering the surface,
*  you know, so inside the nasal surfaces, the throat, the lung cells, and I believe liver as
*  a couple of other organs where they are actually expressed in abundance.
*  That's for the AC2, you said? For the AC2 receptors.
*  So, okay, so back to the story. So, yes. In the fall.
*  So now the impact of this virus is significant. However, it's a pre-local problem to the point
*  that this is something that we would call a neglected disease because it's not big enough
*  to make, you know, the drug design companies to design a new antiviral or a new vaccine.
*  It's not big enough to generate a lot of grants from the National Funding Agencies.
*  So does it mean we cannot do anything about it? And so what I did is I taught a bioinformatics
*  class in Worcester Polytechnic Institute, and we are very much a problem learning institution.
*  So I thought that that would be a perfect project for the class.
*  It's an ongoing case study.
*  So I asked, you know, so we essentially designed a study where we tried to use bioinformatics to
*  understand as much as possible about this virus. And a very substantial portion of the study was
*  to understand the structures of the proteins, to understand how they interact with each other and
*  with the host proteins, try to understand the evolution of this virus. It's obviously,
*  you know, a very important question, where it will evolve further, how it happened here.
*  So we did all these projects, and now I'm trying to put them into a paper where all these
*  undergraduate students will be co-authors. But essentially, the projects were finished
*  right about mid-December. And a couple of weeks later, I heard about this mysterious new virus
*  that was discovered and was reported in Wuhan province. And immediately I thought that, well,
*  we just did that. Can't we do the same thing with this virus? And so we started waiting for the
*  genome to be released, because that's essentially the first piece of information that is critical.
*  Once you have the genome sequence, you can start doing a lot using bioinformatics.
*  LW – When you say genome sequence, that's referring to
*  the sequence of letters that make up the RNA?
*  MP – Well, the sequence that make up the entire information encoded in the protein.
*  So that includes all 29 genes. LW – What are genes? What's the
*  encoding of information? MP – So genes is essentially a basic functional
*  unit that we can consider. So each gene in the virus would correspond to a protein. So gene
*  by itself doesn't do its function. It needs to be converted or translated into the protein
*  that will become the actual functional unit. LW – Yeah, like you said, the printer.
*  MP – So we need the printer for that. LW – We need the printer. Okay. So the first
*  step is to figure out the genome, the sequence of things that will be then used for printing the
*  protein. So, okay. MP – So then the next step. So once we have this,
*  so we use the existing information about SARS, because the SARS genomics has been done
*  in abundance. So we have different strains of SARS and actually other related coronaviruses,
*  MERS, the bat coronavirus. And we started by identifying the potential genes, because right
*  now it's just a sequence, right? So it's a sequence that is roughly, it's less than 30,000
*  nucleotide long. And… LW – Just a raw sequence.
*  MP – It's a raw sequence. LW – No other information, really.
*  MP – And we now need to define the boundaries of the genes that would then be used to identify the
*  proteins and protein structures. LW – How hard is that problem?
*  MP – It's pretty straightforward. Because we use the existing information about SARS proteins
*  and SARS genes. LW – So once again, you kind of…
*  MP – We are relying on the… Yes. And then once we get there, this is where the first more
*  traditional bioinformatics step begins. We're trying to use these protein sequences and
*  get the 3D information about those proteins. So this is where we are relying heavily
*  on the structure information, specifically from the protein data bank that we're talking about.
*  LW – And here you're looking for similar proteins.
*  MP – Yes. So the concept that we are operating when we do this kind of modeling,
*  it's called homology or template-based modeling. So essentially, using the concept that if you have
*  two sequences that are similar in terms of the letters, the structures of the sequences are
*  expected to be similar as well. LW – And this is at the micro, at the very local scale?
*  MP – At the scale of the whole protein. LW – The whole protein.
*  MP – Right. So actually, of course, the devil is in the details, and this is why we need actually
*  pre-sophisticated modeling tools to do so. Once we get the structures of the individual proteins,
*  we try to see whether or not these proteins act alone or they have to be forming protein complexes
*  in order to perform this function. And again, so this is sort of the next level of the modeling
*  because now you need to understand how proteins interact. And it could be the case that the
*  protein interacts with itself and makes sort of a multimeric complex. The same protein just repeated
*  multiple times, and we have quite a few such proteins in SARS-CoV-2. Specifically, spike protein
*  needs three copies to function. Envelope protein needs five copies to function. And there are some
*  other multimeric complexes. LW – That's what you mean by interacting with itself,
*  and you see multiple copies. So how do you make a good guess whether something's going to interact?
*  MP – Well, again, so there are two approaches. One is look at the previously solved complexes.
*  Now we're looking not at the individual structures, but the structures of the whole complex.
*  LW – Complexes of multiple proteins. MP – Yes. So it's a bunch of proteins
*  essentially glued together. LW – And when you say glued, that's the interaction.
*  MP – That's the interaction. So there are different forces, different sort of physical forces
*  behind this. LW – Sorry to keep asking dumb questions, but is the interaction fundamentally
*  structural or is it functional in the way you're thinking about it?
*  MP – That's actually a very good way to ask this question because turns out that the interaction
*  is structural, but in the way it forms the structure, it actually also carries out the function.
*  So interaction is often needed to carry out very specific functions for a protein.
*  LW – But in terms of on the reverse side, figuring out you're really starting at the structure
*  before you figure out the function. So there's a beautiful figure too in the paper
*  of all the different proteins that make up the able to figure out the make up
*  the new the novel coronavirus. What are we looking at? So these are like
*  that's this through the step two that you mentioned when you try to guess at the possible proteins,
*  that's what you're going to get is these blue cyan blobs.
*  MP – Yes. So those are the individual proteins for which we have at least some information from
*  the previous studies. So there is advantage and disadvantage of using previous studies. The biggest,
*  well, the disadvantage is that we may not necessarily have the coverage of all 29 proteins.
*  However, the biggest advantage is that the accuracy in which we can model these proteins
*  is very high, much higher compared to ab initio methods that do not use any template information.
*  LW – So, but nevertheless, this figure also has, I mean, it's such a beautiful,
*  and I love these pictures so much. It has like the pink parts, which are the parts that are
*  different. So you're highlighting, so the difference you find is on the 2D sequence,
*  and then you try to infer what that will look like on the 3D.
*  MP – Yeah. So the difference actually is on 1D sequence.
*  LW – 1D, sorry, not 2D, right. MP – And so this is one of these
*  first questions that we tried to answer is that, well, if you take this new virus
*  and you take the closest relatives, which are SARS and a couple of bad coronavirus strains,
*  they are already the closest relatives that we are aware of. Now, what are the difference
*  between this virus and its close relatives? And if you look, typically when you take a sequence,
*  those differences could be quite far away from each other. So what 3D structure makes
*  those differences to do? Very often, they tend to cluster together.
*  LW – Interesting. MP – And over sudden, the differences that may
*  look completely unrelated actually relate to each other, and sometimes they are there because they
*  correspond, they attack the functional site, right? So they are there because this is the
*  functional site that is highly mutated. LW – So that's a computational approach
*  to figuring something out. When it comes together like that, that's kind of a nice,
*  clean indication that there's something, this could be actually indicative of what's happening.
*  MP – Yes. So we need this information and the 3D structure gives us just a very intuitive way to
*  look at this information and then start asking questions such as, so this place of this protein
*  that is highly mutated, is it a functional part of the protein? So does this part of the protein
*  interact with some other proteins or maybe with some other ligands, small molecules, right? So
*  we will try now to functionally inform this 3D structure. LW – So you have a bunch of these
*  mutated parts. How many are there in the novel coronavirus when you compare to SARS? We're
*  talking about hundreds, thousands, these pink regions. MP – No, no, much less than that.
*  And it's very interesting that if you look at that, so the first thing that you start seeing,
*  you look at patterns, and the first pattern that becomes obvious is that some of the proteins
*  in the new coronavirus are pretty much intact. So they're pretty much exactly the same as SARS,
*  as the bad coronavirus, whereas some others are heavily mutated. So it looks like that the
*  evolution is not occurring uniformly across the entire viral genome, but actually target very
*  specific proteins. LW – And what do you do with that, like from the Sherlock Holmes perspective?
*  MP – Well, so one of the most interesting findings we had was the fact that the viral,
*  so the binding sites on the viral surfaces that get targeted by the known small molecules,
*  they were pretty much not affected at all. And so that means that the same small drugs or small
*  drug-like compounds can be efficient for the new coronavirus.
*  LW – Ah, so this all actually maps to the drug compounds too. So you're actually mapping out
*  what old stuff is going to work on this thing, and then possibilities for new stuff to work
*  by mapping out that things have mutated. MP – Yes. So we essentially know which parts
*  behave differently and which parts are likely to behave similar. And again, of course, all
*  our predictions need to be validated by experiments, but hopefully that sort of
*  helps us to delineate the regions of this virus that can be promising in terms of the drug
*  discovery. LW – You kind of mentioned this already, but maybe you can elaborate. So how different
*  from the structural and functional perspective does the new coronavirus appear to be relative
*  to SARS? MP – We now are trying to understand the overall structural characteristics of this virus,
*  because that's our next step, trying to model the single viral particle of this virus. So that means
*  that you have the individual proteins, like you said, you have to figure out what their interaction
*  is. Is that where this graph kind of interactome? LW – So the interactome is essentially our
*  prediction on the potential interactions, some of them that we already deciphered from the structural
*  knowledge, but some of them that essentially are deciphered from the knowledge of the existing
*  interactions that people previously obtained for SARS, for MERS or other related viruses.
*  MP – So is there kind of interactomes, am I pronouncing that correctly by the way?
*  LW – Yes, interactome. MP – Are those already
*  converged towards for SARS? LW – So I think there are a couple of papers that now investigate the
*  large-scale sets of interactions between the new SARS and its host. And so I think that's an
*  ongoing study. MP – And the success of that, the result would be an interactome.
*  And so when you say not trying to figure out the entire particle, the entire thing.
*  LW – So structure, right? So what this viral particle looks like. So as I said,
*  the surface of it is an envelope, which is essentially a so-called lipid bilayer
*  with proteins integrated into the surface. So an average particle is around 18 nanometers,
*  right? So this particle can have about 50 to 100 spike proteins. So at least we suspect it,
*  and based on the micrographs images, it's very comparable to MHV virus in mice and SARS virus.
*  MP – Micrographs are actual pictures of the actual… LW – Virus.
*  MP – Okay, so these are models. LW – These are the actual images, right?
*  MP – Sorry for the tangents, but what are these things? So when you look on the internet,
*  the models and the pictures are… And the models you have here are just gorgeous and beautiful.
*  When you actually take pictures of them with a micrograph, what do we look…
*  Well, they typically are not perfect. So most of the images that you see now
*  is the sphere with those spikes around. LW – You actually see the spikes?
*  MP – Yes, you do see the spikes. And now, our collaborators for Texas A&M University,
*  Benjamin Newman, he actually in a recent paper about SARS, he proposed, and there's some
*  actually evidence behind it, that the particle is not a sphere, but it actually is an elongated
*  ellipsoid-like particle. So that's what we are trying to incorporate into our model.
*  And if you look at the actual micrographs, you see that those particles are not symmetric.
*  So there are some of them. And of course, it could be due to the treatment of the material,
*  it could be due to some noise in the imaging. LW – Right, so there's a lot of uncertainty
*  in all this. So structurally figuring out the entire part. By the way, again, sorry for the
*  tangents, but why the term particle? Or is it just something that's stuck?
*  MP – It's a single… We call it the virion. So virion particle, it's essentially a single virus.
*  LW – Single virus. But it just feels like… Because particle to me, from the physics
*  perspective, feels like the most basic unit, because there seems to be so much going on
*  inside the virus. It doesn't feel like a particle to me.
*  MP – Yes, well, yeah, it's probably… I think virion is a good way to call it.
*  LW – So, okay, so trying to figure out the entirety of the system.
*  MP – Yes, so virion has 5200 trimer spikes. It has roughly 200 to 400
*  membrane protein dimers. And those are arranged in the very nice lattice. So you can actually see
*  it's like a carpet. LW – On the surface again.
*  MP – Exactly, on the surface. And occasionally you also see this envelope protein inside.
*  LW – Is that the one we don't know what it does?
*  MP – Exactly, exactly. The one that forms the pentamer, this very nice pentameric ring.
*  And so, this is what we're trying to put now all our knowledge together and see whether we can
*  actually generate this overall virion model with an idea to understand, well, first of all,
*  to understand how it looks like, how far it is from those images that were generated.
*  But the implications are there is a potential for the
*  nanoparticle design that will mimic this virion particle.
*  LW – Is the process of nanoparticle design meaning artificially designing something that looks similar?
*  MP – Yes. The one that can potentially compete with the actual
*  virion particles and therefore reduce the effect of the infection.
*  LW – So is this the idea of like what is a vaccine?
*  MP – So vaccine, so there are two ways of essentially treating and in the case of vaccine
*  is preventing the infection. So vaccine is a way to train our immune system. So our immune system
*  becomes aware of this new danger and therefore is capable of generating the antibodies then
*  will essentially bind to the spike proteins because that's the main target for the vaccines design
*  and block its functioning. If you have the spike with the antibody on top, it can no longer interact
*  with AC2 receptor. LW – So the process of designing a vaccine then is to
*  understand enough about the structure of the virus itself to be able to create an artificial
*  particle? MP – Well, the nanoparticle is a very exciting and new research. So there are already
*  established ways to make vaccines and there are several different ones. So there is one where
*  essentially the virus gets through the cell culture multiple times, so it becomes essentially
*  adjusted to the specific embryonic cell and as a result becomes less compatible with the host
*  human cells. Therefore, it's sort of the idea of the live vaccine where the particles
*  are there, but they are not so efficient. So they cannot replicate as rapidly as
*  before the vaccine and they can be introduced to the immune system. The immune system will learn
*  and the person who gets this vaccine won't get sick or will have mild symptoms. So then there is
*  sort of different types of the way to introduce the non-functional parts of this virus or the virus
*  where some of the information is stripped down. For example, the virus with no genetic material,
*  exactly. So it cannot replicate, it cannot essentially perform most of its functions.
*  LW – This is fascinating. What is the biggest hurdle to design one of these, to arrive at one
*  of these? Is it the work that you're doing in the fundamental understanding of this new virus or is
*  it from our perspective complicated world of experimental validation and sort of going through
*  the whole process of showing this is actually going to work with FDA approval, all that kind of stuff?
*  KS – I think it's both. I mean, our understanding of the molecular mechanisms will allow us to
*  know to design, to have more efficient designs of the vaccines.
*  However, once you design the vaccine, it needs to be tested.
*  LW – But when you look at the 18 months and the different projections,
*  it seems like an exceptionally, historically speaking, maybe you can correct me, but even
*  18 months seems like a very accelerated timeline. KS – It is. I mean, I remember reading about
*  in a book about some previous vaccines that it could take up to 10 years to design and
*  properly test a vaccine before its mass production. So yeah, everything is accelerated these days.
*  I mean, for better, for worse, but we definitely need that.
*  LW – Well, especially with the coronavirus, I mean, the scientific community is really
*  stepping up and working together. The collaborative aspect is really interesting.
*  You mentioned, so vaccine is one, and then there's antivirals, antiviral drugs.
*  KS – So antiviral drugs, so where vaccines are typically needed to prevent the infection,
*  right? But once you have an infection, what we try to do, we try to stop it. So we try to stop
*  virus from functioning. And so the antiviral drugs are designed to block some critical functioning
*  of the proteins from the virus. So there are a number of interesting candidates. And I think,
*  if you ask me, I think Remdesivir is perhaps the most promising.
*  KS – It has been shown to be an efficient and effective antiviral for SARS. Originally,
*  it was the antiviral drug developed for a completely different virus, I think, for Ebola and
*  Marburg. LW – At high level, do you know how it works?
*  KS – So it tries to mimic one of the nucleotides in RNA, and essentially that stops the replication.
*  LW – So messes, I guess that's what, so antiviral drugs mess with some aspect of this
*  process. So essentially, we try to stop certain functions of the virus. There are some other ones,
*  that are designed to inhibit the protease, the thing that clips protein sequences. There is one
*  that was originally designed for malaria, which is a bacterial disease. So…
*  KS – This is so cool. But that's exactly where your work steps in, is you're figuring out the
*  functional, the structure of these different… So like providing candidates for where drugs can
*  plug in. LW – Well, yes, because one thing that we don't know is whether or not, so let's say
*  we have a perfect drug candidate that is efficient against SARS and against MERS. Now, is it going
*  to be efficient against new SARS-CoV-2? We don't know that, and there are multiple aspects that can
*  affect this efficiency. So for instance, if the binding site, so the part of the protein where
*  this ligand gets attached, if this site is mutated, then the ligand may not be attachable to this part
*  any longer. And our work and the work of other bioinformatics groups essentially are
*  trying to understand whether or not that will be the case. And it looks like for the ligands that we
*  looked at, the ligand binding sites are pretty much intact, which is very promising.
*  If we could just zoom out for a second. Are you optimistic? So there's two, well, there's three
*  possible ends to the coronavirus pandemic. So one is there's, or drugs or vaccines get figured out
*  very quickly, probably drugs first. The other is the pandemic runs its course for this wave
*  at least. And then the third is, you know, things go much worse in some dark, bad, very bad direction.
*  Do you see, let's focus on the first two. Do you see the anti-drugs or the work you're doing
*  being relevant for us right now in stopping the pandemic, or do you hope that the pandemic will
*  run its course? So the social distancing, things like wearing masks, all those discussions that
*  people are having will be the method with which we fight coronavirus in the short term? Or do you
*  think that it'll have to be anti-viral drugs? I think anti-virals would be,
*  I would view that as the, at least the short term solution. I see more and more cases in the news
*  of those new drug candidates being administered in hospitals. And I mean, this is right now the
*  best what we have. But do we need it? In order to reopen the economy? What do you think?
*  I mean, we definitely need it. I cannot speculate on how that will affect reopening of the economy
*  because we are kind of deep into the pandemic and it's not just the states, it's also worldwide.
*  Of course, there is also the possibility of the second wave, as you mentioned. And this is why
*  we need to be super careful. We need to follow all the precautions that the doctors tell us to do.
*  Are you worried about the mutation of the virus?
*  It's of course a real possibility. Now, how, to what extent this virus can mutate,
*  it's an open question. I mean, we know that it is able to mutate, to jump from one species to another
*  and to become transmittable between humans. So let's imagine that we have the new antiviral.
*  Will this virus become eventually resistant to this antiviral? We don't know. I mean,
*  this is what needs to be studied. It's such a beautiful and terrifying process that a virus,
*  some viruses may be able to mutate to respond to the mutate around the thing we've put before it.
*  Can you explain that process? How does that happen? Is that just the way of evolution?
*  I would say so, yes. I mean, it's the evolutionary mechanisms. There is nothing imprinted
*  into this virus that makes it just the way it evolves. And actually, it's the way it co-evolves
*  with its host. It's just amazing. Especially the evolutionary mechanisms, especially amazing given
*  how simple the virus is. It's incredible that it's, I mean, it's beautiful. It's beautiful
*  because it's one of the cleanest examples of evolution working.
*  Well, I think, I mean, one of the reasons for its simplicity is because it does not require
*  all the necessary functions to be stored. So it actually can hijack
*  the majority of the necessary functions from the host cell. So the ability to do so, in my view,
*  reduces the complexity of this machine drastically. Although if you look at the most recent
*  discoveries, so the scientists discovered viruses that are as large as bacteria. So these Mimiviruses
*  and Mama viruses, actually those discoveries made scientists to reconsider the origins
*  of the virus and what are the mechanisms and how, what are the mechanisms, the evolutionary mechanisms
*  that leads to the appearance of the viruses. By the way, I mean, you did mention that viruses are,
*  I think you mentioned that they're not living. Yes, they are not living organisms.
*  So let me ask that question again. Why do you think they're not living organisms?
*  Well, because they are dependent. The majority of the functions of the virus
*  are dependent on the host. So let me do the devil's advocate. Let me be the philosophical
*  devil's advocate here and say, well, humans, which we would say are living, need our host planet
*  to survive. So you can basically take every living organism that we think of as definitively living.
*  It's always going to have some aspects of its host that it needs of its environment.
*  So is that really the key aspect of why a virus is that dependence? Because it seems to be very
*  good at doing so many things that we consider to be intelligent. It's just that dependence part.
*  LR. Well, I mean, yeah, it's difficult to answer in this way. I mean, the way I think about the
*  virus is in order for it to function, it needs to have the critical component, the critical tools
*  that it doesn't have. So I mean, in my way, it's not autonomous. That's how I separate the idea of
*  the living organism on a very high level between the living organism and...
*  LR. And you have some... I mean, these are just terms and perhaps they don't mean much,
*  but we have some kind of sense of what autonomous means and that humans are autonomous.
*  You've also done excellent work in the epidemiological modeling, the simulation
*  of these things. So the zooming out outside of the body, doing the agent-based simulation.
*  So that's where you actually simulate individual human beings and then the spread of viruses from
*  one to the other. How does, at a high level, agent-based simulation work?
*  LR. All right. So it's also one of these irony of timing. Because I mean, we've worked on this
*  project for the past five years. And the New Year's Eve, I got an email from my PGA student
*  that the last experiments were completed. And three weeks after that, we get this diamond princess
*  story and emailing each other with the same news saying...
*  LR. So the diamond princess is a cruise ship. And what was the project that you worked on?
*  LR. So the project, I mean, the code name, it started with a bunch of undergraduates.
*  The code name was zombies on a cruise ship. So they wanted to essentially model the
*  zombie apocalypses on a cruise ship. And after having some fun, we then thought about the fact
*  that if you look at the cruise ships, I mean, the infectious outbreak has been one of the biggest
*  threats to the cruise ship economy. So perhaps the most frequently occurring is the Norwalk
*  virus. And this is essentially one of these stomach flus that you have. And it can be quite
*  devastating. So occasionally there are cruise ships, they get canceled, they get returned
*  back to the origin. And so we wanted to study, and this is very different from the traditional
*  epidemiological studies where the scale is much larger. So we wanted to study this in a confined
*  environment, which is a cruise ship. It could be a school, it could be other places such as
*  this large company where people are in interaction. And the benefit of this model is we can actually
*  track that in the real time. So we can actually see the whole course of the evolution,
*  or the whole course of the interaction between the infected horse and the host and the pathogen,
*  etc. So agent-based system or multi-agent system to be more precisely
*  is a good way to approach this problem because we can introduce the behavior of the passengers,
*  of the crews. And what we did for the first time, that's where we introduced some novelty,
*  is we introduced a pathogen agent explicitly. So that allowed us to essentially model the behavior
*  on the host side as well on the pathogen side. And over sudden, we can have a flexible model
*  that allows us to integrate all the key parameters about the infections. So for example,
*  the virus, right? So the ways of transmitting the virus between the
*  horse. How long does the virus survive on the surface, the formite?
*  What is, you know, how much of the viral particles does a host shed when he or she is asymptomatic
*  versus symptomatic? And you can encode all of that into this path. And it's just for people who don't
*  know. So agent-based simulation, usually the agent represents a single human being. And then there's
*  some graphs, like contact graphs that represent the interaction between those human beings.
*  So yes, so essentially, agents are individual programs that are run in parallel. And we can
*  provide instructions for these agents how to interact with each other, how to exchange
*  information, in this case, exchange the infection. But in this case, in your case,
*  you've added a pathogen as an agent. I mean, that's kind of fascinating. It's kind of a brilliant
*  way to condense the parameters, to bring the parameters together that represent the pathogen,
*  the virus. That's fascinating, actually. So yeah, we realized that by bringing in the virus,
*  we can actually start modeling. I mean, we're no longer bounded by very specific aspects of
*  the specific virus. So we started with Norwalk virus and of course zombies. But we
*  continued to modeling Ebola virus outbreak, flu, SARS. And because I felt that we need to add a
*  little bit more excitement for our undergraduate students. So we actually modeled the virus from
*  the contagion movie, so MEV1. And unfortunately, that virus, and we tried to extract as much
*  information. Luckily, the scientific consultant was Jan Lipkin, a virologist from Columbia
*  University who is actually who provided, I think he designed this virus for this movie
*  based on Nipah virus. And I think with some ideas behind SARS of flu like airborne viruses. And
*  the movie surprisingly contained enough details for us to extract and to model it.
*  I was hoping you would like publish a paper of how this virus works.
*  Yeah, we are planning to publish.
*  I would love it if you did. But it would be nice if the origin of the virus. But you're now
*  actually being a scientist and studying the virus from that perspective.
*  But the origin of the virus, the first time actually, so this movie is assignment number one
*  in my bioinformatics class that I give. Because it tells you that bioinformatics can be of use.
*  Because if, I don't know, have you watched it?
*  A long time ago, yeah.
*  So there is approximately a week from the virus detection, we see a screenshot of scientists
*  looking at the structure of the surface protein. And this is where I tell my students that if you
*  ask an experimental biologist, they will tell you that it's impossible because it takes months,
*  maybe years to get the crystal structure of this, the structure that is represented. If you ask a
*  biopharmatician, they tell you, sure, why not? We'll just get it modeled. But it was very
*  interesting to see that there is actually, and if you do screenshots, you actually see the
*  phylogenetic tree, the evolutionary tree that relate this virus with other viruses. So it was
*  a lot of scientific thought put into the movie. And one thing that was interesting to learn is
*  that the origin of this virus was there were two animals that led to the zoonotic origin of this
*  virus were fruit bat and a pig. So this is-
*  This doesn't feel like we're, this definitely feels like we're living in a simulation. Okay,
*  maybe a big picture. Agent-based simulation now, larger scale, sort of not focused on a crucial,
*  but larger scale are used now to drive some policy. So politicians use them to tell stories
*  and narratives and try to figure out how to move forward under so much uncertainty. But
*  in your sense, are agent-based simulation useful for actually predicting the future?
*  Or are they useful mostly for relative comparison of different intervention methods?
*  Well, I think both because in the case of new coronavirus,
*  we essentially learning that the current intervention methods may not be efficient enough.
*  One thing that one important aspect that I find to be
*  so critical and yet something that was overlooked during the past pandemics is
*  the effect of the asymptomatic period. This virus is different because it has such a long
*  symptomatic period and over sudden that creates a completely new game when trying to contain this
*  virus. In terms of the dynamics of the infection. Exactly. Do you also, I don't know how close you're
*  tracking this, but do you also think that there's a different rate of infection for when you're
*  asymptomatic like that aspect or does the virus not care? So there were a couple of works.
*  One important parameter that tells us how contagious the person with asymptomatic
*  virus versus asymptomatic is looking at the number of viral particles this person sheds.
*  As a function of time. So far, what I saw is the study that tells us that the person during the
*  asymptomatic period is already contagious and the person sheds enough viruses to infect another host.
*  I think there's so many excellent papers coming out, but I think I just saw maybe a nature paper
*  that said the first week is when you're symptomatic or asymptomatic, you're the most contagious. So the
*  highest level of the plot in the 14-day period, they collected a bunch of subjects and I think
*  the first week is when it's the most contagious. Yeah, I think I'm waiting to see more populated
*  studies with higher numbers. One of my favorite studies was again, a very recent one where
*  scientists determined that tears are not contagious.
*  There is no viral shedding done through tears. So they found one moist thing that's not contagious.
*  I've personally been, because I'm on a survey paper somehow that's looking at masks.
*  There's been so much interesting debates on the efficacy of masks and there's a lot of work
*  and there's a lot of interesting work on whether this virus is airborne. It's a totally open
*  question. It's leaning one way right now, but it's a totally open question whether it can travel
*  in aerosols long distances. Do you think about this stuff? Do you track this stuff? Are you
*  focused on the informatics of it? This is a very important aspect for our epidemiology study.
*  I think it's a very simple idea, but I agree with people who say that
*  the masks work in both ways. So not only it protects you from the incoming viral particles,
*  it also makes the potentially contagious person not to spread the viral particles.
*  Who is when they're asymptomatic may not even know that they're... In fact, it seems to be there's
*  evidence that they don't... Surgical and certainly homemade masks, which is what's needed now
*  actually because there's a huge shortage of... They don't work to protect you that well.
*  They work much better to protect others. So it's a motivation for us to all wear one.
*  Exactly. About 30%, as far as I remember, at least 30% of the asymptomatic cases
*  are completely asymptomatic. So you don't really cough, you don't have any symptoms,
*  yet you shed viruses. Do you think it's possible that we'll all wear masks? I wore masks at a
*  grocery store and you get looks. I mean, this was like a week ago. Maybe it's already changed
*  because I think the CDC has said that we should be wearing masks. Like the LA, it's starting to
*  happen. But it just seems like something that this country will really struggle doing or no.
*  LR I hope not. I mean, it was interesting. I was looking through the old pictures during the
*  Spanish flu. And you could see that pretty much everyone was wearing masks with some exceptions.
*  And there were like sort of iconic photograph of the, I think it was San Francisco, this tram
*  who was refusing to let in someone without the mask. So I think, well, it's related to the fact
*  how much we are scared. So how much do we treat this problem seriously?
*  LR And, you know, my take on it is we should, because it is very serious.
*  CB Yeah, I, from a psychology perspective, just worry about the entirety, the entire big mess
*  of a psychology experiment that this is, whether masks will help it or hurt it. You know, masks
*  have a way of distancing us from others by removing the emotional expression and all that kind of
*  stuff. But at the same time, masks also signal that I care about your well-being. So it's a really
*  interesting trade-off that's just- LR Yeah, it's interesting, right, about distancing.
*  Aren't we distanced enough? CB Right, exactly. And when we try to
*  come closer together when they do reopen the economy, that's going to be a long road
*  of rebuilding trust and not all being huge germaphobes. Let me ask sort of,
*  you have a bit of a Russian accent, Russian or no Russian accent? Were you born in Russia?
*  LR Yes. And you're too kind. I have a pretty thick Russian accent.
*  What are your favorite memories of Russia? LR So I moved first to Canada and then to the United
*  States back in 99. So by that time I was 22. So whatever Russian accent I got back then,
*  it stuck with me for the rest of my life. By the time the Soviet Union collapsed, I was a kid, but
*  old enough to realize that there are changes. CB Did you want to be a scientist back then?
*  LR Oh, yes. I mean, the first sort of 10 years of my juvenile life,
*  I wanted to be a pilot of a passenger jet plane. So yes, it was like, I was getting ready
*  to go to a college to get the degree. But I've been always fascinated by science. And so
*  not just by math, of course, math was one of my favorite subjects, but biology, chemistry, physics,
*  somehow I liked those four subjects together. And yes, so essentially after a certain period of time,
*  I wanted to actually, back then it was a very popular area of science called cybernetics.
*  So it's not really computer science, but it was like computational robotics in this sense. And so
*  I really wanted to do that. But then I realized that my biggest passion was in mathematics.
*  And later when studying in Moscow State University, I also realized that I really want
*  to apply the knowledge. So I really wanted to mix the mathematical knowledge that I get
*  with real life problems. CB And that could be, you mentioned chemistry and now biology,
*  and I sort of, does it make you sad? Maybe I'm wrong on this, but it seems like
*  it's difficult to be in collaboration, to do open big science in Russia.
*  From my distant perspective in computer science, I don't, I'm not, I can go to conferences in Russia.
*  I sadly don't have many collaborators in Russia. I don't know many people doing great AI work in
*  Russia. Does that make you sad? Am I wrong in seeing it this way?
*  I have to tell you, I'm privileged to have collaborators in bioinformatics in Russia.
*  And I think this is the bioinformatics school in Russia is very strong.
*  In Moscow? In Moscow, in Novosibirsk, in St. Petersburg,
*  have great collaborators in Kazan. And so at least in terms of my area of research-
*  There's strong people there. Yeah, strong people, a lot of great ideas,
*  very open to collaborations. So I, perhaps, it's my luck, but I haven't experienced
*  any difficulties in establishing collaborations. That's bioinformatics though.
*  It could be bioinformatics too, and it could be person by person related, but I just don't
*  feel the warmth and love that I would, you know, you talk about the seminal people who
*  are French in artificial intelligence, France welcomes them with open arms in so many ways.
*  I just don't feel the love from Russia. I do on the human beings, like people in general,
*  like friends and just cool, interesting people, but from the scientific community,
*  no conferences, no big conferences. Yeah, it's actually, you know, I'm trying to think.
*  Yeah, I cannot recall any big AI conferences in Russia.
*  It has an effect on, for me, I haven't sadly been back to Russia, but my problem is it's very
*  difficult. So now I have to renounce the citizenship. Oh, is that right? I mean,
*  I'm a citizen in the United States and they make it very difficult. There's a mess now, right? So
*  I want to be able to travel like, you know, legitimately. Yeah. And it's not an obvious
*  process that will make it super easy. I mean, that's part of that. Like, you know, it should be super
*  easy for me to travel there. Well, you know, hopefully this unfortunate circumstances that
*  we are in will actually promote the remote collaborations. And I think what we are
*  experiencing right now is that you still can do science, you know, being quarantined in your own
*  homes. Especially when it comes, I mean, you know, I certainly understand there is a very
*  challenging time for experimental scientists. I mean, I have many collaborators who are, you know,
*  who are affected by that, but for computational scientists. Yeah, we're really leading into the
*  remote communication. Nevertheless, I had to force you to talk to you in person because there's
*  something that you just can't do in terms of conversation like this. I don't know why, but
*  in person is very much needed. So I really appreciate you doing it. You have a collection
*  of science bobbleheads. Yes. Which look amazing. Which bobblehead is your favorite and which
*  real world version, which scientist is your favorite? Yeah. So yeah, by the way, I was
*  trying to bring it in, but they are quarantined now in my, in my office. They sort of demonstrate
*  the social distance. So they're nicely spaced away from each other. But so, you know, it's
*  interesting. So I've been collecting those bobbleheads for the past, maybe 12 or 13 years.
*  And it, you know, interestingly enough, it started with the two bobbleheads of Watson and Creek.
*  And interestingly enough, my last bubblehead in this collection for now, and my favorite one,
*  because I felt so good when I got it, was the Rosalind Franklin. And so, so, you know, when I
*  Who's the full group? So I have Watson, Creek, Newton, Einstein, Marie Curie, Tesla,
*  of course, Charles Darwin, sorry, Charles Darwin, and Rosalind Franklin. I am definitely missing
*  quite a few of my favorite scientists. And but so, you know, if I were to add to this collection,
*  so I would add, of course, Kolmogorov. That's, you know, I've been always fascinated by
*  his, well, his dedication to science, but also his dedication to educating young people,
*  the next generation. So it's very inspiring. He's one of the, okay, yeah, he's one of the
*  Russia's greats. Yes. Yeah. So he also, you know, the school, the high school that I attended
*  was named after him. And he was great. You know, so he founded the school, and he actually taught there.
*  Is this in Moscow? Yes. So, but then, I mean, you know, other people that I would definitely
*  like to see in my collections would be Alan Turing, would be John Von Neumann.
*  Yeah, you're a little bit late on the computer scientists.
*  Yes. Well, I mean, they don't make them, you know, I still am amazed they haven't made Alan Turing
*  yet. Yes. And I would also add Linus Pauling. Linus Pauling. Who is Linus Pauling? So this is,
*  to me, is one of the greatest chemists. And the person who actually discovered the
*  the secondary structure of proteins, who was very close to solving the DNA structure.
*  And, you know, people argue, but some of them were pretty sure that if not for this, you know,
*  a photograph 51 by Rosalind Franklin that, you know,
*  Watson and Crewe got access to, he would be the one who would solve it.
*  Science is a funny race. It is. Let me ask the biggest and the most ridiculous question. So you've
*  kind of studied the human body and its defenses and these enemies that are about,
*  from a biological perspective, bioinformatics perspective, a computer scientist perspective,
*  how has that made you see your own life, sort of the meaning of it,
*  or just even seeing your, what it means to be human?
*  Well, it certainly makes me realizing how fragile the human life is.
*  If you think about this little tiny thing, it can impact the life of the whole human kind
*  to such extent. So, you know, it's something to appreciate and to
*  remember that we are fragile. We have to bond together as a society.
*  And, you know, it also gives me sort of hope that what we do as scientists is useful.
*  I don't think there's a better way to end it. Dmitry, thank you so much for talking today. It
*  was an honor. Thank you very much. Thanks for listening to this conversation with Dmitry Korkin
*  and thank you to our presenting sponsor, Cash App. Please consider supporting the podcast by
*  downloading Cash App and using code LEXPODCAST. If you enjoy this podcast, subscribe on YouTube,
*  review it with five stars on Apple Podcasts, support it on Patreon, or simply connect with me
*  on Twitter at Lex Friedman. And now, let me leave you with some words from Edward Osborne Wilson,
*  E.O. Wilson. The variety of genes on the planet and viruses exceeds or is likely to exceed
*  that in all of the rest of life combined. Thank you for listening and hope to see you next time.

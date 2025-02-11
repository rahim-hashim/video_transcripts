---
Date Generated: November 19, 2024
Transcription Model: whisper medium 20231117
Length: 4539s
Video Keywords: []
Video Views: 2620
Video Rating: None
Video Description: Patreon: https://www.patreon.com/seanmcarroll
Blog post with audio player, show notes, and transcript: https://www.preposterousuniverse.com/podcast/2024/11/18/296-brandon-ogbunu-on-fitness-seascapes-and-the-course-of-evolution/

Biological evolution via natural selection is a simple idea that becomes enormously complicated in its realization. Populations of organisms are driven toward increased "fitness," a measure of how successfully we reproduce our genetic information. But fitness is a subtle concept, changing with time and environment and interactions with other organisms around us. We talk with biologist Brandon Ogbunu about the best mathematical and conceptual tools for thinking about the messy complexities of evolution, and how technology is changing our way of thinking about it.

Brandon Ogbunu received his Ph.D. in Genetics and Microbiology from Yale University. He is currently Assistant Professor of Ecology and Evolutionary Biology at Yale, and External Faculty at the Santa Fe Institute. He has been awarded a Fullbright Fellowship and was the Martin Luther King Jr. Visiting Professor at MIT. He has contributed to a number of publications, including Wired, Undark, and Quanta.

Mindscape Podcast playlist: https://www.youtube.com/playlist?list=PLrxfgDEc2NxY_fRExpDXr87tzRbPCaA5x
Sean Carroll channel: https://www.youtube.com/c/seancarroll

#podcast #ideas #science #philosophy #culture
---

# Mindscape 296  Brandon Ogbunu on Fitness Seascapes and the Course of Evolution
**Mindscape Podcast:** [November 18, 2024](https://www.youtube.com/watch?v=4DCgYiMnaME)
*  Hello everyone, welcome to the Mindscape podcast. I'm your host Sean Carroll. I'm
*  sure many of you have heard of the idea of a fitness landscape in evolutionary
*  biology. It's a very vivid visual kind of metaphor if you want to think of it
*  that way. Introduced back in the 1930s by Sewell Wright who was a population
*  biologist, a geneticist, and the idea is that you consider a bunch of genes that
*  make up the genome of an organism or a population of organisms and you can
*  imagine changing all those genes right by mutations a little bit and so as a
*  function of the actual genes and how you might change them a population of
*  organisms will be fit, more fit or less fit depending on the environment that
*  it's in and you can sort of imagine plotting that fitness as a function of
*  what the genes are doing. There's many many genes, there's many different
*  mutations you can imagine so it's a very very high dimensional space but the
*  metaphor is nice. You climb up to the top of the fitness landscape. In the
*  course of this podcast we actually wonder whether biologists use this before
*  or after the physicists use the idea of an energy landscape so since then I
*  looked it up the physicists were first, yay physicists. Physicists turn it
*  upside down right you plot the energy of a system as a function of various
*  parameters and like a ball rolling down a hill as long as there's dissipation
*  the system will go down to the minimum of the energy landscape. This is still a
*  big idea e.g. in cosmology or string theory where we talk about the landscape
*  of possible laws of physics in string theory and things like that. Anyway the
*  metaphor is so nice, so compelling that it's one of those things you might be
*  tempted to overuse. The reality as you will not be surprised to hear is much
*  more complicated than that. For one thing it's not a landscape it's more
*  like a seascape because of course your environment which is affecting what
*  your fitness is is constantly changing in different ways. For another matter
*  it's not just you the population organisms that you are part of that
*  matters there are other organisms they have their own fitness landscapes they
*  are competing with you or they're eating you or being eaten by you and so on. So
*  this is one of the many ways in which biology is much richer and more
*  complicated than many problems in physics and that's what we're going to
*  be talking about today. Brandon Abunu is a evolutionary biologist who thinks in
*  terms of systems biology and complex systems in particular. Thinking
*  about how we can use things like big data and so forth to analyze how
*  different kinds of organisms usually for his work microorganisms pathogens in
*  diseases in particular will respond to changes in the environment to changes in
*  drugs if you're trying to fight a disease and changes in what other
*  organisms are doing. It's a fascinating problem both for very down-to-earth
*  practical reasons trying to do biology especially in an era where we can
*  collect an enormous amount of data and maybe even shape what the evolutionary
*  trajectory is either by selecting different organisms or directly by
*  changing their genomes and also a fascinating problem conceptually like
*  how do you deal with these giant dimensional spaces how do you think
*  about them mathematically practically computationally and then how does the
*  whole thing fit into the broader scope of science and as you'll see near the
*  end of the podcast even the broader scope of culture science is done by people by
*  human beings who live in a culture we live in a society and we need to take
*  that into account when we do our science so a great example here of complexity
*  science in action let's go
*  Brandon Nabunu welcome to the Mindscape podcast. Oh it's really a quite a pleasure
*  to be here thank you for having me. We're gonna cover a lot of ground I suspect
*  over the next hour but let's start with some basics we talked about evolution
*  natural selection Darwin etc the basic idea of natural selection to the
*  untutored mind like I was when I first heard about it just sounds simple and
*  obvious right of course you know there's mutations you pick the best ones you
*  move on how could it be different it seems to me that over the past few
*  decades biologists have really been complicating things the story has become
*  a lot richer that's that's right that's one way of framing it sure did take a
*  nice elegant algorithm and that's what makes kind of Darwinian reasoning so
*  beautiful that is that it is elegant and even though Darwin himself knew nothing
*  about the molecular basis right he really really did get yeah down to the
*  molecular level right a process so that's exactly right we had the simple
*  elegant thing in the last last couple decades we just learned so much that
*  it's kind of added some nuance is there yeah we'll get to it of course so don't
*  worry about having spoiler alerts or anything like is there a single most
*  intriguing to you way in which we've complicated the picture oh my I mean how
*  much time do we have I mean you know I think there's a plenty of time we'll
*  circle back there's a there's a number of things so for example right I think
*  the whole conversation around the randomness of right evolution by natural
*  selection I think what makes it powerful is that there is no formal hand guiding
*  how the variation is generated and like formally steering how selection is
*  operating that's kind of what makes it so subversive an idea but we're learning
*  is that there are elements to evolution by natural selection that very well
*  might be predictable okay and I based on the sort of information that we have
*  there might be patterns and how mutations happen are they really random
*  this is kind of a little bit of a philosophical question about what
*  randomness means and I think this manifests even at the molecular level in
*  evolution in terms of how was that random variation that selection is
*  acting upon how is that actually generated you know questions live in all
*  of those domains we you know we entirely approve of philosophical questions here
*  at the winescape as you know well you mentioned the phrase levels of
*  selection so maybe that's a good place to start getting a little bit more into
*  detail you know I've had people on the podcast philosophers and biologists
*  arguing about this question you know does selection happen at the species
*  level at the population level at the individual level at the gene level is it
*  all the above what's your take yeah now my selection is all the above I think
*  which is a very very wimpy answer but I think it is true I think the question is
*  if you think about you know the selection operating at all these levels
*  and they each are responsible for some proportion of what we see I think the
*  question is how much is it operating at one level versus another right I think
*  it's really that level of nuance now I mostly live at the molecular level and
*  it's kind of like undeniable that we see see selection happening at the protein
*  and gene network and gene level I think it gets much more controversial when you
*  talk about these social questions about how it happens and that one I have I
*  think it is happening but I'm certainly not an ardent advocate that that's
*  everything the way some others are I guess even at the individual level I've
*  long had this feeling but I guess I haven't talked to a real biologist about
*  it you know we in some sense in the Darwinian way of thinking we select on
*  traits right on phenotypical aspects of things the length of the neck of the
*  giraffe but the actual information is carried in genes which is at the
*  molecular level and I'm guessing there might not be a one-to-one map here so
*  maybe we're selecting on things that we don't pass down in the right way or
*  there's unintended consequences yeah no I mean just the basic flow of
*  information from you know DNA to RNA to protein to phenotype which is the
*  classical kind of now that information flow like you articulated you know
*  earlier asked me like what are the big questions in evolution and it is
*  precisely that there's not a very very neat mapping between what's happening at
*  the genotypic scale and what's happening at the phenotypic scale and frankly I
*  think that's the greatest existing question right in you know modern
*  evolution and evolutionary genetics I think there are multiple ways to get a
*  phenotype of interest number one right I think there are multiple ways to skin a cat
*  there are multiple ways to generate a long neck there are multiple ways to
*  generate a tall person there's more so you have that right as a profoundly
*  complicated set of questions and then the phenotypes themselves that we see
*  like you articulated very well may have been crafted by a force that has nothing
*  to do with the genotype nothing to do what you're inheriting so it creates
*  this deep complication with regards to being able to neatly map our genetic
*  information which is you know incredibly powerful and being able to tell
*  meaningful stories about organisms and humans on earth maybe elaborate more on
*  what you mean by nothing to do with what you're inheriting I guess I was pointing
*  to the idea that maybe you want a longer neck so you select for a gene that does
*  that but that gene also affects other things and then that goes along with the
*  right is that also what you were thinking about or is there more to it
*  yeah no no I mean I think I think that's that's one thing right so I think you
*  know the silly example is you know what color is your hair so the idea there is
*  the idea there is there are multiple genetic routes to get to that hair
*  combination color and we actually know a lot about kind of the evolution of hair
*  color right but there's another route which is dyeing your hair that color and
*  that has nothing to do with any sort of combination of genetic information so
*  that's an extreme example of how the environment can do the heavy lifting and
*  all the work that genetics can do and that's an extreme example to make the
*  point but something analogous is actually happening with a lot of the
*  traits that we care about they could very well be crafted by nature's hair dye
*  yeah one of the tools that we use to talk about these ideas is the idea of a
*  fitness landscape I don't know whether the physicists follow the biologists on
*  this because physicists talk about energy landscapes all the time I don't
*  know who came first there but and I understand that it's well explain to us
*  what the idea of fitness landscape is first yes yes no the fitness landscape
*  in its relationship and has absolutely been invaded by physicists the fitness
*  landscape comes from this kind of era in modern evolutionary biology called the
*  modern synthesis with many of the best thinkers ever largely statisticians and
*  mathematicians came up with analytical and mathematical descriptions of the
*  evolution process and so really what this did is it kind of like formalized
*  evolutionary biology as a quantitative field it really lived at the population
*  level and as rather than the individual level it did really really beautiful
*  things in a lot of ways for our field now one of those individuals Sewell
*  Wright one of the architects of the month came up with the notion of an
*  adaptive landscape sometimes referred to as the fitness landscape and what this
*  does is it analogizes the process of evolution as a physical surface where
*  you have kind of moving uphill and downhill and that uphill is like you are
*  climbing towards better fitness higher fitness maybe like I said a coat color a
*  bit ability to resist the drug right here and so on the x-axis here you're
*  individual mutations so it's like evolution is taking these walks up and
*  down with natural selection to do is it can change the structure of that space
*  and certainly a lot of evolution is how do you climb out of a valley so it
*  creates this mental analogy that has since become more than an analogy now
*  as a whole subfield of evolutionary theory where people like study these
*  surfaces and they basically say what is the fitness landscape for evolving
*  antibiotic resistance what is the fitness landscape for evolving height
*  right oh this is going to be rugged that means this sort of problem might be more
*  challenging to navigate and solve than another sort of problem and I think it's
*  really been a helpful profound analogy that's helped us measure and consider a
*  lot of real problems in the world it really bugs the physicists that hire on
*  the fitness landscape is where you want to go like that's not true for landscapes
*  you balls go down hill it's not no and I've actually given this talk to some
*  kind of physical chemists and somehow made it out alive because that's exactly
*  right so they were first on that regard to what degree Sewell Wright invoked the
*  original like those Boltzmann sort of thermodynamic landscapes I think is it
*  that's an empirical question that I'm sure historian of science has interrogated
*  I'm 100% sure that one of our listeners is gonna leave it in a comment so I look
*  forward to that thank thank thank you ahead of time so but I did talk about
*  fitness landscapes in my book the big picture and like a couple of people
*  pushed back a little bit they were worried about this idea that I don't
*  know whether it was mostly because they thought it was too compelling an analogy
*  and you might get lost what's really going on or apparently it can be
*  misused by creationists also but that anything can be misused by creationist
*  so that doesn't bother me too much yeah that makes sense I think what we'll
*  start with the the the reverse direction we'll go to creation is one like I think
*  what's interesting there is creationists do have this skill at seizing on any
*  sort of idea that adds real tractability and potential predictability to
*  evolution as in that being evidence that this was engineered by maker or
*  something like that so I think that makes sense I think this is a this is a
*  kind of a chat this has happened to me I published a paper on fitness landscapes
*  and I think several several creationists cited it I'm just like wait a minute I
*  think in terms of other kind of technical criticisms of the fitness
*  landscape it's really really interesting because we can think about powerful
*  analogies obviously physics has them obviously and biology has them from the
*  selfish genes the blind watchmaker to the spandrels famous spandrels there's
*  several kind of powerful analogies that we use and it's like the fitness
*  landscape can be considered a version of one of those yet it can be actually
*  mined quantitatively and theoretically you can put it in it you can put
*  equations to it and I think that's what makes it beautiful and I think perhaps
*  the critics of it are saying y'all need to chill this is supposed to be an
*  analogy you know it's really just a toy now it's a cool toy and there are
*  questions that it can answer but I think just like any analogy or frankly
*  any mathematical model frankly you have to know where its limits are it can tell
*  certain things about the world and it can do so very very beautifully but it
*  can it's not very hard to over apply it to context and circumstances and
*  biologies that it originally was not intended right I mean as I said I'm a
*  big fan of the of the metaphor but I do therefore want to sort of probe its
*  weak point so I know we're not to go overboard I mean one thing is that you
*  say the x-axis but of course there's a gajillion axes right so it's very hard
*  to actually visualize this high dimensional space of all the different
*  genes I could change no that's exactly right so that's like the the number one
*  criticism of it I guess what's interesting about that criticism is that
*  it became much more relevant technology has rendered it much more irrelevant
*  right because there was a point we actually could mutate very many things
*  in a gene and so the analogy actually mapped where we were technologically you
*  know now I mean you can take a protein and just generate I mean if techniques
*  like deep mutational scanning and now with kind of there's high throughput
*  CRISPR cas sorts of methods I can change say hemoglobin you can change like every
*  single variants of every single amino acid in large combination I mean these
*  are hundreds of thousands of various how do you actually depict that in anything
*  resembling a visual space that one isn't kind of like a neat three
*  dimensional landscape that's going to be a you know an nth dimensional landscape
*  so so I think that's exactly right I think the original landscape poses some
*  problems for actually capturing the way information is structured in the real
*  biological world I wonder if and I truly don't know whether or not anyone has
*  taken advantage of the fact that there are some simplifications mathematically
*  in very very high dimensional spaces like I'm only recently discovering this
*  stuff myself in my physics work because it's very useful you know in a very high
*  dimensional space almost all points on a sphere are on the equator almost all
*  vectors are orthogonal to each other right I mean is there do you know of any
*  work that is saying well because the fitness landscape is defined on the
*  space of genomes and that's really really big we can say this beautiful
*  mathematical fact about its structure or am I just whistling the dark no no
*  you're not I mean I think there's a there's a lot of people who ask I mean I
*  think there's the fitness landscape what's what's cool about it is that it's
*  simple enough that a bunch of different sorts of suites of mathematics or
*  physics or statistics can be used to analyze features of it so for example
*  graph theory right it had you look at a fitness landscape it has this it has
*  this graph theory like character right and so there are graph theorists who
*  have you know walked various features and mathematical tools from graph
*  theory for the questions in evolution so I'll say the good things first is that
*  is you know graph theory analytical geometry network theory which is related
*  to graph theory thinks about these sorts of problems there are people had have
*  tried to reconcile this thermodynamic it relate the relationship between
*  thermodynamics something all of these things have been brought together and I
*  think all of them have added something genetic programming also is another one
*  they've all added something but have they in some generated a unification
*  right of a mess set of mathematical tools to truly understand how evolution
*  works I would say no I mean maybe there people disagree I would say no I think
*  right now we have a bunch of different pictures of evolution using these
*  different kind of mathematical physical and statistical frameworks and they tell
*  us some interesting things about individual problems but I think that we
*  think we need to go further here good and I guess the other thing which is
*  more down to earth and I know people have thought about is the ruggedness of
*  the landscape you mentioned it already so if in our minds for the listeners
*  since there's no video here if we think about this axis going left to right as
*  changing genes from one thing to another I could easily imagine the vertical
*  axis is the fitness of it easily imagine a tiny change in a gene leads to a
*  disastrous decrease in fitness and that presumably makes it kind of hard to
*  mathematically analyze because we're used to doing you know gradient descent
*  we're used to like you know walking in the direction where things are increasing
*  but if things are wildly fluctuating that's hard to do no that's exactly
*  right and I think this is one of the arenas there are features of the way
*  fitness that topography up and down that are deeply kind of counterintuitive but
*  I think one of those forces I study quite a bit in my lab and that's this
*  idea called epistasis and epistasis basically refers to it's a kind of an old
*  concept with a really interesting history but it basically refers to you
*  have one mutation in a gene that you and you know what its effects are you have
*  another mutation and you know what its individual effects are but when you put
*  them together you got something you could not have predicted from them
*  individually yeah so what's the problem here and the problem here is this can
*  create that ruggedness this creates that confusing because if you mutation and
*  you had it in the background of another and boom you could take you downwards
*  for example you could be climbing uphill perfectly fine you're accumulating
*  mutations you're evolving resistance to a drug or something like that and then
*  you get this mutation mutation interacts epistatically we would say with the
*  other mutations and boom so I think yeah I think this throws a wrench and a lot
*  of our simplistic models for how to understand study predict how evolution's
*  working and this remains a cutting-edge problem in evolutionary genetics yeah
*  this is why we got to pay the big bucks you got to solve these hard problems
*  well you know I mean you know we're getting it yeah yeah yeah yeah yeah or at
*  least it will confidently state it has solved the problem that's something
*  that's unquestionable is it possible one complication obviously is that you
*  already alluded to the fact that the fitness landscape is not static right it
*  changes over time is there any usefulness if we have different species
*  coexisting and maybe one's a predator one's a prey or maybe they're just
*  competing with each other do they both have fitness landscapes and they're sort
*  changing in response to what the others are doing oh my yeah yeah no this is this
*  is a very very compelling question right about so number one let's go back to
*  what the you know the fitness landscape metaphor is saying it's a it's thinking
*  about a physical surface some really smart people have started to invoke the
*  notion of a fitness seascape right and the idea there is that if you actually
*  think about how evolution so again people keep adding kind of features to
*  this analogy to try to match the way you know the world works environments are
*  fluctuating yeah right I just told you know I'm like I'm wearing this sweater
*  today because it is much colder today than it was yesterday and I've no idea
*  what the weather is gonna be tomorrow simply that fluctuation in temperature
*  changes some organism probably a microbes actual fitness landscape maybe
*  on our bike microbiota meaning something that was uphill yesterday
*  maybe downhill today right so the idea is the actual problem of evolution is
*  deeply complicated because the topography of that landscape is
*  changing in which case the seascape where things are always changing is an
*  extension of that now so you know that hasn't caught on so so broadly but there
*  are people that are using that analogy a bit more now to the predator prey thing
*  so that relates to the ski scape because they're influencing each other in
*  evolutionary arms race their adaptations are gonna change as they're kind of
*  evolving or interacting through time through evolutionary time yeah that's
*  gonna change the fitness landscape I have a close colleague Martha Munoz an
*  evolutionary biologist who has this phrase you know that behavior is a
*  brake and a motor on evolution right so it's like if you're involved right so
*  the idea is and basically just talk about how behavior itself becomes
*  something that changes the fitness landscape for certain sorts of traits
*  right I just think that's a really really interesting insight so yeah no I
*  think this is what I think that probably you outlined is one of the reasons why
*  we need to think more carefully about adding bells and whistles and knobs to
*  the original fitness landscape metaphor because the problems in the real world
*  are just so much more complicated than can be captured in a simple you know
*  three-dimensional image well you use the word complicated of course that's right
*  next to the word complexity and we're both we both hang out at the Santa Fe
*  Institute and talk about these things I want to ask you the general question of
*  how complexity science plays into this but first what you just said reminded me
*  of a conversation I had on the podcast recently with Don Farmer the economist
*  another SFI guy who points to the focus on equilibria in economics as sort of a
*  limit on what they could do because the real world economies are never in
*  equilibrium this is not a good approximation I'm wondering if
*  evolutionary biologists have the same issue to confront yeah I mean yeah maybe
*  not quite sit that I mean yeah not equilibrium systems is a is a buzzword
*  in a lot of different fields in part because as you say the analytical tools
*  the original tools you know kind of rebuilt around equilibria and being in
*  fixation to get the world is kind of in flux as we described so the so just
*  bridging it to the last conversation the notion that everything is in flux
*  complicates the idea that there's a neat and clean adaptive peak let's go back to
*  that in this landscape right this idea that we've just optimized what's
*  interesting and you talk about how creation is utilized and kind of
*  weaponized even the fitness landscape that I can also see how that can work
*  because the notion that there's a neat peak for any problem and we're all just
*  trying to get there right that is one that is kind of friendly to both
*  creationist ideas of that there's an ideal and we were made perfect right and
*  and it's a kind of you know change gears a little bit to eugenic ideas that what a
*  perfect human is and there's an optimal this and an optimal that right so I think
*  even the quote-unquote scientific side of this problem is you know is you know
*  has issues when they push for equilibria and stability and optimal and that's
*  just not how the biological world is constructed for a myriad reasons so I
*  think that's that's what I would say the connection is between the equilibria
*  conversations the econ yeah okay I mean do do evolutionary biologists explicitly
*  use the language of equilibria like they try to find some happy place because I
*  know economists do and that was the yeah yeah yeah yeah I mean I think in
*  different sub for some simple questions so for example evolutionary game
*  theorists for example and absolutely they absolutely formally use the
*  mathematical understanding of equilibria right to think about how a how a you
*  know in a in a in a situation when you have a bunch of evolutionary inches it
*  was the evolutionary stable strategy for example as John Maynard Smith exactly
*  right on Nash and others would have articulated yeah so equilibria is
*  certainly used there equilibria I think like in population genetics we would say
*  fixation right that's when a it goes to fixation is fixed in a population so
*  that's an iteration of equilibria it's like you know you have an antibiotic
*  resistance gene that is better than everybody else at some point through
*  time and we have elegant math to predict when this is going to happen it will
*  like rise to fixation beat meaning virtually all the parts virtually all
*  everyone in the population has that that allele fixed so that's kind of where
*  equilibria is also invoked in evolutionary biology oh so these are all
*  very general concepts that apply to all the different levels that we were
*  talking about at the very beginning but my impression is that in your lab you're
*  looking a lot at diseases and how they resist drug treatments and things like
*  that I mean it kind of sounds like we can just take everything we've been
*  talking about import over yeah there's some some pathogens and we're fighting
*  against them and it's all dynamic etc but but what are the specific questions
*  that get raised here yeah yeah great great great thank you so I think
*  microbes and disease have all of these features that make them really really
*  great have always been some of the best systems for asking the fundamental
*  questions in evolution for various reasons number one their microbes and
*  their diseases and people care about them right I think which is very very
*  important yeah more than that part of the reason why we care about them is
*  because they are just kind of wired with all of this this biology that makes them
*  kind of fed relative fast of all first we can see them evolving fast they can
*  adapt quickly the generation time is short and now I kind of in the last half
*  spent more than half century now I mean really century we can grow these things
*  in the lab and really really elegant ways we now have their genome sequences
*  fully understood they're very very tractable system so we use it we're
*  using kind of microbes to ask fundamental questions about the way that
*  molecular evolutions happening largely at the protein scale so for example this
*  question about the fitness seascape right the fact that it changes what if I
*  have two closely related drugs that we nonetheless use interchangeably at the
*  bedside right like so you know meaning we think they're very very similar I had
*  background where I did some clinical micro so we think they're similar we're
*  looking at things like all right actually even subtle differences in the
*  chemistry of a drug very subtle changes that fitness landscape and so resistance
*  to do these two drugs actually might move differently and that did at a
*  different pace right so that's kind of highlighting the you know the relevance
*  of this fitness seascape denim to the fitness landscape metaphor because it's
*  basically saying wow it will even slight changes in an environment can profoundly
*  influence the pace and direction of evolution so we're studying two
*  questions of that sort yeah I mean we all know I guess that we fight against
*  the pathogens and the pathogens they don't fight back but they adapt back they
*  try to slip through our fingers right it how how much is the study of this sort of
*  purely empirical we try this and see what happens versus how useful is the
*  theorizing here as a theorizing caught up to the messy empirical reality what a
*  good good question I think I have a lot of thoughts about that so you know
*  number one are you know rich Richard Lenski's long-term evolution experiment
*  remains I think the greatest debt might one of the greatest demonstrations of
*  evolution by natural selection works and it continues it's now I believe with
*  Jeffrey Barrick now at the University of Texas it's one of the great examples of
*  the demonstration of evolution and action and all of its elegance and
*  beauty there's both patterns and it's completely predictable and it does all
*  these amazing things maybe sorry maybe for the audience explained the long-term
*  evolution experiment sure sure sure thank you yeah thank you so basically
*  Richard Lenski and colleagues at Michigan State gosh me now many decades
*  ago evolved a strains of E. coli this kind of it's a gut bacteria soil that
*  bacteria that we have kind of domesticated to be able to grow in the
*  laboratory very very well so it's one of the most studied organisms on earth we
*  know everything about it and we have a strain that grows very very well we have
*  strands that grow very very well in the laboratory well Lenski and colleagues
*  took this and basically generated multiple populations of them right so we
*  had multiple kind of versions of the world playing out in parallel and
*  evolved them right to various stressors sugar different sorts of sugars
*  metabolize different sorts of sugars and basically just demonstrated over the
*  course right now hundred thousand generations what happens when evolution
*  right and responding to the exact same sorts of stressors across multiple
*  populations and it's basically given us this amazing picture into how evolution
*  happens both at the genotypic meaning we know how the genome is changing and at
*  the phenotypic we see the acquisition of kind of new abilities to metabolize
*  sugars we see the gain and loss of genes we see all of these processes happening
*  right under our eyes and it's given us the one of the most detailed pictures for
*  how evolution happens this experiment has been mined by theorists and it has
*  generated new theory so to the second part of your question about has you know
*  it's there so I think those things have been in conversation experimentally and
*  a really really good way now this last point you had that question which was
*  provocative is has theory caught up oh my I mean you know there's a big joke in
*  debate within population genetics which is in which is where a lot of the
*  theorists live they call it beanbag genetics they would kind of pejorative
*  be called because it just seems too optimal it seems based on a world you
*  might have heard of Harvey Weinberg equilibria which is this this kind of
*  equation that describes it's a null model for how evolutions operating under
*  optimal conditions when you have populations that are breeding at a
*  certain kind of way and it basically reflects no reality ever you know the
*  way biology works so I'm saying to say a lot of theory still suffers from a lot
*  of that it does that problem if it does not it just does not apply to the
*  biological world as it actually exists I think the good news there and I don't
*  look at that as a bad thing I think now in that what I call the post genomic era
*  as I call it where do you know it's not just happens at a cheap pace it's no
*  longer thought it's not the rate limiting step in any scientific in
*  Denver I mean rarely there's some organisms that are hard to sequence but
*  generally speaking everyone has access to it I think we're gonna enter a golden
*  age of theory personally because we're gonna have more data than we know to do
*  with it's gonna reveal new kind of things and patterns that we could not
*  have considered and I think now we have data metadata about how the world
*  actually works so we can evolve no pun intended from being black genetics and
*  actually begin to develop theory that matches this dynamic world that we're in.
*  You know I have a historical example I always pull up when people talk about
*  this because there is this opinion out there in some circles that when we have
*  huge amounts of data we'll find patterns in them and that will be it we won't
*  have any deep understanding we'll just know the pattern and maybe that's true
*  but I harken back to Tico Brahe the astronomer who just you know had the
*  best telescopes and actually wasn't even telescopes right I mean it was just he
*  was just plotting positions of stars planets on the sky etc and on the basis
*  of that Kepler was able to say you know what it's not epicycles it's ellipses
*  and on the basis of that which was just pattern-fitting but the basis of that
*  Isaac Newton is able to invent the law of gravity which is actually
*  understanding so I'm optimistic that biology neuroscience all of these things
*  will eventually get there we're just at the first stage so it's not surprising
*  we're not there yet. I couldn't agree more and I think and I think you point
*  out something very important and that is with new data you know are gonna call
*  are gonna come associations between things that's what that's what these
*  computational tools do we'll be able to you know but that is not a mechanistic
*  theory of understanding for how a system works but I'm just I'm just but I think
*  computation can help us with theory as well I don't think you know I think
*  it can help us so that's what I'm excited about it's like okay well the
*  theory you know going back to the fitness landscape the theory from the
*  modern synthesis and the statistics from the modern synthesis you know Fisher of
*  course is one of the architects there you know everybody who does empirical
*  work of any kind is still using Fisherian statistics and and so I say
*  this to say we've done a lot of good I mean like science I mean in terms of
*  technical good not moral good and that's so good but statistical good with theory
*  that's now a century old right we've done we've done a lot of good with that
*  I really really want to see what the next generation of theory looks like
*  because it's good and should be different and I think you can use
*  computational tools to help us get there well okay back to the real world a
*  little bit do you have examples of your work in diseases in their evolution
*  adaptation where thinking about them in the right way has literally helped fight
*  a disease in some way or are we still at the sort of trying to grope towards some
*  understanding level yeah no no it's a good question so so I think it has I
*  think the you know not like you know I'm not personally taking credit for this I
*  just mean like how the field the field itself that has studied problems like
*  the evolution of drug resistance at a molecular level has unquestionably at
*  the very least most conservatively it has changed the medical conversation
*  about how and when and why to use antibiotics at the bedside and I think
*  resistance profiling is now a central part of how we think about therapies for
*  infectious diseases and cancers and I think that absolutely is a testament to
*  the fact that evolutionary understanding became part of medical
*  understanding for that problem so that's the most conservative view that there's
*  no question that we think about it and evolution that was part of drug design
*  right so think about resistance profiling up front what would resistance
*  mechanism look like this is now a conversation that's happening so there's
*  that which I think is a notable and significant application of thinking
*  about how molecular evolution can apply now more than that I think this
*  understanding if we understand what a fitness landscape looks like in these
*  environments the question is can we predict how drug resistance is gonna
*  evolve that's kind of one of the great the gold stands and these are the sorts
*  of things that we ask in our lab and colleagues of mine ask and I think the
*  goal here is a paradigm where we can cut infectious diseases off or drugs is off
*  we know where it's going to evolve and we have a suite of drugs that can
*  actually get like you have it in place before you can actually prevent
*  resistance from happening wow you have a yeah so this is so you're predicting
*  evolution not like unlike you're predicting the weather I mean the
*  mathematics and stuff is different it's more of a conceptual analogy than a
*  computational one but maybe maybe it is actually computationally maybe the tools
*  will look like that I'm saying this to say the idea is there's weather's you
*  know there's some analogies right there's there's there's some predictability
*  that because of the accumulate you know how you configure these various forces
*  that dictate how the weather works and I think in evolution there's various
*  forces that are influencing how right a a microbe is evolving in the presence of
*  some drug well if we understand what those forces are we can come up with
*  probabilities that this outcome will happen versus probably that this come
*  happen we can have drugs ready for that mm-hmm right and we can actually help
*  people you know who are infected with various pathogens that way so that's a
*  contemporary one where evolutionary theory is really and we do have drugs
*  that are on the bedside that utilize these sorts of that are being kind of
*  tested but utilize these sorts and I think you have drug companies now
*  utilizing the fitness landscape to try to identify drug targets all across the
*  fitness landscape so has this happened yet is this active now can you know the
*  search technology no but this is I think they were this is very much at the point
*  now where these sorts of sophisticated evolutionary understandings are now
*  being invoked in serious conversations about how to generate new therapies the
*  idea of predicting the course of evolution is a fascinating one I mean my
*  rough impression is that back in the day you would have said you can't predict
*  anything it's all randomness and we're gonna find different things and these
*  days we seem to be moving more toward a view where where well some things might
*  predictable because that's where the peaks of the fitness landscapes are and
*  the randomness comes in and how we find them not where we end up that's right
*  that's exactly right and I think that's what makes this current you know that's
*  that's what makes this ever so fun we now have the information again now we
*  have the data on what this fitness landscape looks like we know where the
*  peaks live we know where the valleys live we know where we are on that
*  landscape I think what we're like the things that we continue to try to
*  understand is is mutation truly random right you know as in is it really really
*  really if there's three different things if there's three four different
*  mutations is there really a 25% chance that you're gonna get each any one of
*  them well answer is no right that there are some kind of like leanings and a lot
*  of this rely leans in at the biochemistry and biophysical level like
*  there's just certain sorts of chemical modifications that are more likely to
*  happen so therefore mutation isn't like random in the sense that all things are
*  equally likely it's random in the sense that there's no particular force that is
*  picking a given site to mutate you know or and even that and I think in some
*  cases is not true so I think the evolution of mutation rate is a hugely
*  complicated field for this week it's basically saying yeah it's random by
*  some definitions and that's a debate I do not want to have with philosophers
*  but yeah it's random in sense that nobody no force is putting it there
*  actively but it's not rent it's it's non-random in the sense that there are
*  potential leanings in forces that may take evolution towards certain
*  directions so anyway just I'm just saying yeah there are with the fitness
*  landscape we now have better data audit we can understand it better but there
*  remain a lot of things we have to understand before we can truly get to
*  the point where I'm really really confident that this evolutionary outcome
*  will happen yeah I guess it's the mutations are not teleological they're
*  not oriented toward trying to make the organism more fit in fact most
*  evolutions most mutations will make it less fit right and then we sort of weed
*  them out but but yes I have learned over the course of talking to biologists on
*  the podcast that you know functional parts of the genome don't mutate nearly
*  as much as the as the junk parts you know because they're kind of protected
*  they're important and and so it's absolutely not all chances are equal no
*  no that's exactly right I mean there are absolutely parts of genomes that
*  evolve much faster and much slower than others for some of the reasons that you
*  outline and I think this relates to a concept that I'm really interested in
*  called evolvability right there you know and it kind of sounds like an interesting
*  word because it's kind of like you're a volvability it's like the capacity of an
*  or a replicator to evolve right and I think what makes it very very
*  interesting and provocative is that you think about the ability to evolve as a
*  trait that could be under selection itself so think about this can
*  evolution make one organism more likely to evolve I like that actually make
*  evolution a gene in a genome more likely to evolve right or less likely to evolve
*  and what does this mean okay and so this is a concept actually
*  Masibu Pugiuchi and actually several other kind of you know philosophers
*  have commented on and it's a really really provocative concept because it
*  really asks kind of at what levels is evolution happening does evolution
*  actually care about that can eventually actually control that if it does if you
*  do see that organism A is more evolvable evolve faster than organism B is that
*  just a byproduct of something else or did evolution actually engineer it that way
*  this is a deeply complicated idea with a lot of strong opinions I think one of
*  the things that has thrown off this discussion is just defining what it
*  actually tests I mean me and you are who's more evolvable right through
*  evolutionary history individual level do you mean at the to your original
*  question do you mean at the population level but nonetheless it's cool to think
*  about that sort of question within genes right the rate of evolution one is faster
*  than the others why is that and how do we what dictates it is it the topography
*  of the fitness landscape maybe if fitness landscape really really smooth
*  right maybe that's a feature that allows so we've asked questions like that in our
*  laboratory as well you're younger than I am you're much more
*  of all of all at least I think you know and look at what you've done and what
*  you continue to do I think it's I used to be a volvable now I'm just an old
*  buddy daddy so we mentioned complexity earlier and obviously complexity has
*  been all over what we've been talking about but I guess I have a question this
*  is always a question and I have my own answer to it but I'm always interested
*  in what other people think is the idea of complexity intrinsically a useful one
*  is thinking of some specific complex system as an example of a complex system
*  rather than the specific system that it is has that been useful to you in your
*  work what a great question I mean I think that I'm gonna hit this several
*  ways so you know I think the beauty of the complexity science you know is that
*  it is it is both a large cabinet of formal ideas and formalisms and theories
*  but it is really kind of prime for thinking about this availability concept
*  I think it's meta in the sense of complexity science is the only field that
*  recognizes that it has to change wired in the whole point is that the world is
*  complex equilibrium it's a non-equilibrium thing and we're gonna
*  fold new things in formalisms like you know math formal mathematics does that
*  and formal evolutionary body does that informally we incorporate new things but
*  that's not part of the identity of the field like we did we just kind of
*  happen to incorporate new things as they come up or it's complexity has a
*  self-awareness about it so for that reason if that reason alone even if I
*  didn't love the ideas within that cabinet I love the fact that it reinvents itself
*  like few other fields do and for that reason I think is an it is incredibly
*  useful now now think about the formalisms inside the cabinet are they
*  useful for right in terms of thinking about them across paradigms and I think
*  so I think so number one let's just kind of start more vague in general like the
*  idea that systems the formal idea that systems are constructed and the rules
*  that construct them right rely on rely on understanding kind of the interactions
*  and the nonlinear interactions between them and the emerging properties that
*  come between them yeah that one is kind of milk toast now like I think it's like
*  you know and I think everybody else is kind of incorporated in it but I think
*  that's a triumph of complexity science not a reason why it's not important right
*  I think complexity science was the one that popularized that notion and then
*  everyone else just took it and we're like oh yeah that's obvious well it wasn't
*  obvious the field championed it and that it's correct and so it became obvious so
*  yes I don't call where I talked about the nonlinear in your action between
*  mutations or they're not right yeah I don't call that come but that's not
*  formally it's epistasis that's firmly in genetics yeah I don't call that a
*  complexity science discovery I call that a genetics discovery but nonetheless the
*  the the the language for the vocabulary for in the word for it's so much easier
*  a concept to sell in various settings because I think complexity science
*  equipped us all with this vocabulary now that now let's go to the other part of
*  question is like the tools itself yeah when I said it the complexity people
*  who think about econ do I walk that directly over into thinking about
*  fitness landscapes and go oh I have a tool from the no not not so much I think
*  um and you know do I do I but conceptually I do right like I said I
*  mean I think now I think the field that I think where this work the best
*  arguably is how networks reef has completely changed how we think about
*  epidemics right like for example like that one that one I mean that was a set
*  that like I said its origins it has relatively recent origins network theory
*  of course related to graph theory but it has walked into a field of mathematical
*  epi that had a long history and really smart people already doing great work and
*  has completely been like introduced new questions and come up with new
*  strategies that have been practically helpful so the second part of the
*  question you do I think that complexity cabinet of tools and ideas and
*  mathematical tools and taking them and walking them across to different
*  problems has helped I think absolutely which is why I continue to mine this
*  cabinet you know directly or indirectly for new ways to study the natural world I
*  really love this idea of complexity science as more self aware of its being
*  a complex adaptive system itself and other fields I think that over and over
*  again in many fields maybe economics maybe evolution people look for a stable
*  foundational point certainly in philosophy right going back to day car
*  to this like I'm a little scared by change it could be good it could be bad
*  let me just find a rock to stand on right but over and over again the
*  universe is telling us actually no that's not the way it is you are a
*  surfer you are not standing on a peak you're moving on the seascape and the
*  more self aware we are about that the better off will be if you'll forgive me
*  raps it izing a little bit no this is this is totally right and I think you
*  know there's a great new volume from Santa Fe Institute on foundational
*  papers you know in complexity science which I think is a useful venture for a
*  bunch of reasons but I think it's a good answer to this question of is this a
*  field right yeah that's it has it has canon right there there is real canon to
*  it not you know it's not it doesn't have a principia or a or a you know or
*  origins of species it doesn't have those yes not yet but right not yet right but
*  it does have a canon and I think that's what really makes a difference for me
*  laughably and you know I mean sure I don't want to discredit everything I've
*  ever said by telling you that my introduction and you know to complexity
*  science was dr. Ian Malcolm from Jurassic Park of course you're not the
*  only one I was a young person then I think everything about who he was as I
*  being iconoclastic and was like wow I want to be like that I want to be like
*  that dude I think I think there's that and then for me there's the more is
*  different paper from 1972 by Anderson about kind of you know broken symmetries
*  and that's that's a foundation idea more is different it's qualitatively
*  different it's not you can't just take your deterministic tools and grow them
*  you have to actually change the rules as you add more components so those are a
*  couple of influences for me the idea of the canon is great because I'm actually
*  teaching with Jen Ismael a course in the philosophy department this year on
*  complexity where we're reading some of the classic papers and it's absolutely
*  clear that there are ideas appearing over and over again right that we build
*  on what has gone before it's exactly what you'd expect from a real field with
*  the canon expanding its purview over time yeah absolutely I think other
*  fields should kind of and I kind of have I was taking I mean yes I'm drinking the
*  Kool-Aid on complexity science I really think you know just because I'm someone who
*  life with having to explain to everyone why I'm reading multiple literatures and
*  I know you I know you can appreciate this right more than anyone but I think when I
*  found complexity science it was just like a crowd where I didn't have to do that at all
*  like nobody was gonna nobody you know when I was studying medicine when I was
*  young and I'd be reading an econ book and back then it was like Jeffrey Sachs
*  and conversations people be like why you read an econ because it's kind of
*  interesting important to understand yeah I don't have to do that in the you
*  know in the complexity community people people don't get it when I say that the
*  single best thing about Santa Fe is that at lunch you don't have to justify
*  yourself they've only brought in other people who already get it at all and you
*  know just and you know people aren't you know I mean we're fancy grumpy
*  professors but we things are not credentialist there in a way I don't
*  think anyone cares about what you know where you come from not really I'm sure
*  that's a it's elitist the way all these spaces are elitist but but if there's a
*  different set of the hierarchy is also structured there differently I feel like
*  just intellectually and I think that allows for the cross pollination you've
*  got to have to have a flat intellectual surface for complexity to work because
*  things have to be able to meet each other mm-hmm and you know they work
*  together the reason why I took physics and biology so long it's kind of like a
*  fitness landscape problem right like they're here they were fine and it
*  weren't the people people serve as the bridge and which is why I showed in
*  just what is life the such a foundational idea look look for this for
*  thinking about how physics walked into other fields okay good back to the
*  biology here because I we've left some things hanging here we talked about the
*  possibility predictive evolutionary biology which is fascinating to me but
*  then we can just imagine being the intelligent designers what about the
*  prospect of we human beings going in there and mucking with the genome and
*  designing the organisms we want yeah yeah yeah I have this you know mental
*  equation that I use it's not a firm one but it's a control equals prediction
*  plus engineering right is how I think about these sorts of things okay so the
*  idea here is you want to let me think about any system that we can control
*  it's because we know what they're going to do we have a good idea of what the
*  system is going to do with certain inputs and we have a means of inputting
*  those things that's what the engineering part is right so be it cooking right
*  like the reason why what a good chef can do is that chef knows what chef knows
*  what's gonna happen if you add oregano and the chef can't add oregano yeah
*  right like that is a means to which you can do and if you can do that you can
*  control now I'll start with the bad news the bad news is some of the kind of most
*  unscientific and worst use uses of science have come from a desire to
*  control how evolution works based on an erroneous and broken understanding of
*  prediction in biology so if the soon as we understood that evolution was a thing
*  and that genetics was a thing people were thinking about steering it this is
*  of course what eugenics was about it was the notion that you can optimize
*  populations and we don't have I mean there's a lot of people that have told
*  that history so we don't have to spend extended time there but that's the moral
*  part of course is the worst part but like right next to that adjacent is the
*  fact that it was technically completely wrong right like it does it that a very
*  poor understanding of the way human traits were constructed so some points
*  if you get prediction really really wrong you've built it on bad tools there
*  now let's flash forward today to the good news the good news is for certain
*  molecular systems we actually we have a picture of what the fitness seascape
*  looks like we know what mutations do we know that you're the distribution of
*  fitness effects how kind of with the ratio of mutations that a gene is gonna
*  get are gonna be beneficial versus deleterious we now because of people like
*  Joe Thornton and colleagues like at the biophysical scale what mutations will do
*  as in you take a protein and you add two mutations how it'll change its folding
*  how it'll change its catalysis and we have this down to the you know to the
*  physical scale now so we know so much so predictions getting stronger we
*  absolutely better than ever because of Jennifer Doudna and colleagues can
*  engineer genomes for an increasingly better resolution so we are getting the
*  tools now we can actually write we can actually steer as some of my colleagues
*  call it steer evolution towards certain things now of course Francis Arnold and
*  colleagues and awarded the Nobel Prize in 2018 for for directed evolution as in
*  I want if I want to I want a protein that kid that's more stable or that can
*  metabolize the sugar faster and that's a sort of control because you know in the
*  sense if they know what they want and they're just marching evolution towards
*  that path but that's not like full control because you're still kind of like
*  you're kind of just hoping that you get the certain evolution moving up you're
*  not actually controlling all the steps now we have the technology to actually
*  steer an engineer a better hemoglobin a better drugs better proteins that do
*  certain things we're actually getting the information now where that control
*  equals prediction plus engineering the engineering is getting better and as
*  this is where theory and experiment come in that helps with the prediction part
*  and so this paradigm is like here already and will continue to be a thing
*  so yeah Francis Arnold my former Caltech colleague and friend if I understand
*  correctly her work it was almost like breeding right I mean she was really
*  just changing external parameters and and like we do with dog species or dog
*  breeds or something like that and and like you say now we can go in and monkey
*  with the actual DNA so have there been I'm not up on it have there been big
*  breakthroughs in doing that so not just monkey with the DNA but for a particular
*  purpose designing an organism well yeah I mean I think yeah I think I mean the
*  work that that is closest to mine is colleague Jacob Scott and colleagues
*  Emily Dolson and colleagues have done stuff like actually steered evolution
*  down certain and it's like in drug resistance so similar problems like
*  however how a microbe or a cancer cell is evolving resistance to a drug yeah
*  people have tweaked parameters there is a bunch of laughs Michael Bayme and
*  colleagues have also thought about these sorts of problems where we've actually
*  steered evolution towards certain evolutionary outcomes when it's come to
*  antibiotics now I think what you're asking is something much more grander
*  than that as in do we have like a a grand molecule that we've engineered
*  from these sorts of things I think some of this just has to have happened in in
*  an industry for certain sorts of so yeah we are using evolution to build
*  molecules in the generic sense but have we yet I think what would be the ghost
*  and what would be the thing that would actually announce this as whoa right as
*  another kind of improvement I think what that would be would be we get a type of
*  molecule or protein that we thought was like impossible that has profoundly
*  important implications for life on earth and for let me give you an example
*  there's a protein called ribisco right that okay right
*  brisco is that one of the most abundant proteins on earth it lives it's
*  basically a critical component of kind of how plants basically you know in
*  photos in certain critical reactions in terms of how plants are able to
*  metabolize things it's a critical critical thing and one of the things
*  about it is according to some biophysicists it's kind of a lousy
*  protein it's actually not very good right but something about the fitness
*  landscape of this protein has made it very difficult to evolve it's actually
*  not that easy to engineer so there's a lot of people in the world my colleague
*  Matthew shoulders at MIT for example good friend are trying to always
*  engineer this thing hmm if someone can invoke a way to steer the evolution of
*  this go towards a much better kind of more efficient version you feed a lot of
*  people you feed a lot of the world you save a lot of plants so this is an
*  example of where this sort of kind of control and there's just kind of
*  features to the biophysics of it that make it tricky to work with I think
*  that's the problem right now but there's a lot of interest in investment a lot
*  of companies because this is going to be a major I mean whoever does this is rich
*  so that's an example of where this sort of approach we want to go next and I
*  think labs are working on these sorts of things now but but you and I are rich in
*  intellectual reward doesn't that count if not actually rich in money I love
*  being able to do this I think there's a lot of stress in doing that yeah so I
*  guess there's a basic thing that that for a long time I realized I don't
*  understand but you're you're putting a finger on it because you talk about
*  evolving proteins and in my brain the genetic information is in DNA and that
*  gets transcribed in the RNA and that prints out some proteins so the thing we
*  should be engineering is the DNA but can what good is it or how do we think
*  about engineering proteins directly yeah no I mean we know what the individual
*  mutations are at the DNA level we know the amino acids they encode so it's kind
*  of like what so when we're engineering the at the protein level or when things
*  are evolving at the protein level they're actually happening molecularly at
*  the DNA level got it right so it's happening so the actual engineering is
*  going on there with and then you can make you can make a lot of you make you
*  make proteins from that information and this is another great example where
*  everything matters this is why biology is so much harder than physics right
*  because it's not just the DNA instructions there are enzymes and there
*  are conditions and there are constraints and I presume that you care about
*  engineering these in a very down-to-earth way yeah I mean you know I
*  think this is really really important I think this is where I like to position
*  myself as a bit of a gadfly in that field because you know I'm all of these
*  things at once and by all the things I mean this I believe in like the many of
*  the deterministic laws that underline population genetic systems I think
*  I think they've helped us understand how evolution works I think they've added
*  rhyme and reason to it they've given us mathematical and statistical tools to be
*  able to study evolution in populations so that's I'm there but I'm also on the
*  other pole of if we want to solve any real problem in contemporary biology
*  ribisco drug resistance cancer evolution genes for depression genes for high
*  type 2 diabetes if you want to look at any problem in biology we are not going
*  to solve it with simple deterministic perspectives or tools we must must
*  rigorously incorporate these other dimensions that are influencing the way
*  that fitness landscape is structured right then influence the topography of
*  it that influence the way variation is generated right and that is right you
*  know forces like epistasis which we talked about gene by environment
*  interactions the fact that the environment is sending this escape to
*  completely different topographies all the time and you know now there's
*  epigenetics which I won't touch right now but I think it's a it's a really a
*  kind of other thing that modifies how phenotype happens pleiotropy like which
*  we refer to either the idea that a mutation that does one thing in a cell
*  is actually probably doing multiple things in a cell and so that complicates
*  the right the topography of the fitness landscape I think this is where we need
*  to live theoretically is learning how these different concepts which you know
*  complicate evolution are actually a beautiful thing to study and I think
*  we're doing that I just think we're headed to an era we can integrate these
*  things more formally into a grammar and I think then we'll be able to control
*  evolution in a much more meaningful way we'll be able to predict evolution in a
*  much more meaningful way but do I think that there's certain things within
*  biological systems that are just going to be not predictable and useful way I
*  do and I think this is where stuff like embryo selection is happening right
*  people are trying to actually pick their children and certainly for certain
*  traits right hair color and eye color we have a very good picture of how to
*  predict but I think you know you want you want a Sean Carroll in physics I
*  mean good luck with that I mean how possibly could you separate which you
*  were born with from the vagaries and the influences and the dimensions and that's
*  not a hippie concept that's a technical concept of the book the notion that this
*  is dictating who you are in a very meaningful way well look it's late in
*  the podcast this is exactly where we're allowed to broaden our scope a little
*  bit and think about the big picture I mean obviously there are ethical social
*  political considerations that come in when we start up talking about designing
*  organisms have you must have thoughts about this do we have any guidelines
*  about how to do this responsibly is it I worry that philosophy is supposed to
*  be a source of wisdom about ethics and morals and things but I I kind of think
*  it's a trailing indicator you know the philosophers wait for things to happen
*  and then go oh that was bad and we were kind of in a position where we need some
*  leading ways of thinking about things that haven't happened yet because the
*  things that could happen are maybe a little scary no what a good way of
*  putting it that you're trailing indicator and like you're right I mean we
*  think you know I can't think through the problems with anywhere near the clarity
*  that a philosopher can but what I can do is do them right away to your point and
*  not be a trailing indicator that's actually a good way to think about what
*  my job is and I think thankfully there's a generation of geneticists who are of
*  this like mine and are reading this the philosophy literature and ethical
*  literature now I think here's what's critical is that there are ethical issues
*  involved right about you know you know engineering you know embryos with
*  certain traits and what that means and how you're influencing future generations
*  and I think those are linked to the technical problems with that sort of in
*  many ways are there sometimes linked to the technical problems and that is right
*  right now we operate as if we know how the biology works and the debates are
*  only technical that's not true if you were talking about the genetics and
*  underlie type 2 diabetes for example I mean we have a lot of beautiful science
*  on that but the predictive genetics are a disaster all right our disaster and
*  it's not like the work itself is bad but that the predictive the predictions that
*  you're going to make are gonna be disastrously wrong right because that's
*  just not how the biology works we want this neat and clean picture in fact the
*  term as you know for this is physics envy I do yeah right which goes I know
*  it goes but I learned it from Gould but I think of any people have used it in
*  various ways we you know I think there's three kind of main problems that play
*  contemporary biology when it comes to prediction one is physics envy two is an
*  idea that we're encourageable categorizers and we're not critical
*  about the types of categories that we use right and three is this elegant
*  concept developed by my dear colleague doc edge a population geneticist who
*  calls it giddyness and giddyness is this notion that we're going to just solve
*  all the problems if we just keep sequencing or just to keep collecting
*  data and keep collecting data so when it comes to like the problems of
*  predictive genomics or engineering you know we just have this overconfidence
*  that we even know what we're doing these traits are deeply complicated
*  environments change them profoundly and the notion that we understand that and
*  when predicted at this moment is just wrong it's just technically wrong and so
*  that's kind of where I step in and try to be a voice to say hey you know this
*  isn't doing what you think it's doing and because of that maybe we shouldn't
*  do it right now well let me let me be a little disruptive here and mention that
*  because we've been we've been so good over the whole course of the hour but
*  as we're having this conversation we learned over the past couple days that
*  the nominee for the head of the Department of Health and Human Services
*  is Robert F Kennedy jr. who doesn't believe the vaccines work at all doesn't
*  believe that we should fluoridize our water etc there's a this is obviously
*  sort of a commonplace observation but you can't separate the science from the
*  culture right yeah there there are reasons why we've been brought to this
*  place is there there's something scientists could do I take it for granted
*  Brandon that you are on my side and thinking that vaccines do work all right
*  how should we I always struggled this myself as someone who is a scientist
*  with a sort of medium-sized public profile what are the actions to take to
*  make people get it better oh my so first thing and I'm not just saying this for
*  no reason I mean I think it's what you've decided to do with this as this
*  an example that was what you decided to do with this podcast you know I think
*  about I was reading the other night that Michael Faraday one of my scientific
*  heroes you know amongst many things you know started the Christmas Day Lectures
*  series for any started in 1827 I believe which were specifically for the public
*  they were for the public and I don't know I haven't read actually I haven't
*  read a good Faraday biography which is actually on my list of things to do I
*  don't know what the motivation came from but it had to have come from the fact
*  that Faraday himself was an outsider and was one of the people who benefit from
*  that exercise and they and they continue today but you know those those lectures
*  I'm saying this to say I say a little bit hyperbolically and I hope nobody is
*  offended that the act of getting people to understand science in the world is
*  the Manhattan Project of our time it's the thing we need we need to kind of
*  like I'm talking about generate a whole generation of people who are technically
*  trained and understand that the hardest thing to do is fit a complicated idea
*  in the head of somebody who's not as educated it's the most challenging thing
*  it is a technical exercise it's not like just a charisma exercise it's a
*  technical exercise it should be prioritized as such and I think not to
*  be again dramatic but I think this survival of science requires a movement
*  like this so that's what I try to do in my career and I think as I move up if
*  you will I hope to kind of give that movement a more of a voice more oxygen
*  well you know we can always be better at it I remember I heard you give a public
*  talk and I was struck by I mean it was great on the science but also you were
*  much more open about your biography than I would ever be and it's not what we
*  scientists are trained to do but I knew it was a conscious decision and I think
*  that it works right people want to hear those personal details I mean they love
*  hearing about Fertiger's cat and and E. coli but also the the story and my wife
*  Jennifer tells me the same thing all the time the story of how the human being
*  got there that's ultimately what is gonna affect them at a deeper level and
*  that's exactly right and it can really be a part of the scientific story right
*  the example that I used in that talk and I think it in my life is you know I
*  share half my genes with my mother from Baltimore of course of course and the
*  difference of in the difference in our life trajectory yeah I mean do you think
*  that's because of what was in my genome how could that possibly be true how could
*  I mean wait but that's what the conclusion is right the fact that she
*  unfortunately left us largely without anything and I'm able to have this
*  hyper successful career or somewhere where we predict that from what's in a
*  genome so my point is we have these technical stories in our lives you have
*  demonstrated you know typical plasticity physics in one sense philosophy and
*  another that is taking a trait the ability to think and compute and apply
*  it to multiple different like that's the concept right so I think the more we can
*  animate these concepts technically and that's not any less rigorous an
*  application in the fitness landscape was molecular evolution so I think
*  that's my thing we need to animate these personal stories they make us more
*  engaging and I think real discovery in explanatory power lives within them you
*  were kind enough to come on the podcast before you have a book out but I know
*  that you're thinking about a book so at least give you the chance to pre
*  advertise a little bit what do you what are you thinking about right in here oh
*  you're you're incredibly kind well so yes I'm writing a book and I'm not gonna
*  give a title yet because the title is still in development but what the what
*  the project is this actually relates directly to what you just said I'm
*  coming up with a series of contemporary thought experiments for complicated
*  ideas in biology think about you know think about what what the what the
*  selfish gene did for how we thought about the evolutionary process say what
*  you will about for now at the time it was incredibly important yeah right for
*  the regeneration of people think about the way that gonna reframe how we
*  thought about the process like the illusion I think there's a new wave of
*  problems in biology that require in new wave of innovative thought experiments
*  and analogies not unlike the fitness landscape right not unlike the selfish
*  gene not unlike the blind watchmaker but ones that fit the contemporary world
*  there were in and that's going to be what the project is about and is it I
*  mean how much are these cultural questions going to come in absolutely on
*  a percent because I think these are the contemporary problems that we're talking
*  about the problem of racism is composed of 15 different forces but one of them
*  is a poor understanding the way the species is structured right and our
*  propensity to put things in boxes for silly reasons that boxes themselves
*  that have leaky barriers the boxes that are artificially constructed
*  historically constructed or technologically constructed yeah now
*  we're gonna address problems like that we're gonna we're gonna address a lot
*  of contemporary debates about the way evolution works and what we can hope
*  it's a hopeful text because it's about what we hope a biology can be in the
*  future I like ending on a point of hope that's always very good so Brandon
*  Abunos thanks so much for being on the mindscape podcast thank you so much for
*  having me I had blast continued success to you

---
Date Generated: April 20, 2024
Transcription Model: whisper medium 20231117
Length: 6752s
Video Keywords: []
Video Views: 1416
Video Rating: None
---

# BI 142 Cameron Buckner: The New DoGMA
**Brain Inspired:** [July 26, 2022](https://www.youtube.com/watch?v=umMp2-6Y7Z0)
*  One of the places where I think the recent machine learning can really inform the philosophical
*  debate is by filling in some of these ellipses, you know, getting rid of this whiff of magic
*  to some of these key appeals that the empiricists have made in the past and showing how, you
*  know, vaguely brain-inspired computational mechanism could actually do some of these
*  operations. And I think that's the sense of wonder that a lot of people get. You know,
*  all the critics of deep learning almost love to then paint deep learning as being the contemporary
*  reincarnation of psychological behaviorism. And this is just totally wrong. To understand
*  how this mischaracterization started, you know, I think you have to go back to the beginning
*  of cognitive science. This is Brain Inspired. Hello, everyone. I'm Paul. On this episode,
*  my guest is Cameron Buckner, who is a philosopher and cognitive scientist at the University of
*  Houston. And today we discuss two main topics Cameron has been working on. The first centers
*  around an age-old debate in philosophy that has continued into modern questions about how to
*  understand natural intelligence and how to build AI, artificial intelligence. And Cameron is in the
*  final stages of a book all about this. And the debate goes by many names like nature versus
*  nurture, rationalism versus empiricism. But the question revolves around how much of our
*  intelligence is learned from experience versus how much is innate. Or in AI, how much should
*  deep learning models learn from scratch versus how much should we simply build in? Cameron's
*  take on this debate is roughly that we should ask, what are the handful of psychological faculties
*  that we possess? Perception, memory, different kinds of learning and so on. And importantly,
*  how might these faculties be implemented in a general and flexible enough way to work with
*  each other as interacting modules to build up to something that we would call an intelligence
*  system? Something like what Chris Elias Smith is working on with his Spawn cognitive architecture,
*  which we discussed in episode 90. So a lot of Cameron's work focuses on how to think about
*  mapping our psychological faculties onto all the different kinds of deep learning models coming out,
*  like convolutional neural networks, transformers and so on. And that we can use these deep learning
*  tools to essentially test what are the right handful of variations of architectures and
*  learning rules and so on that need to be built so as to work well together. That's what we discuss
*  in the first part of the episode. Then we switch gears a little and talk about Cameron's recent work
*  on another age-old topic, how our mental contents, our thoughts, beliefs, desires, are connected to
*  the things that they are contents about. How our mental contents are grounded in the world. So
*  without going into much detail here, Cameron proposes our mental contents are grounded by
*  our brain's predictions of what's about to happen. And more specifically about the learning that
*  predictions need to be updated due to error. So these are both huge topics and I encourage you
*  to learn more by diving deeper into his work, which I link to in the show notes at
*  braininspired.co slash podcast slash 142. On the website braininspired.co, you can also learn how
*  to support the podcast through Patreon or my online course about the intersection of neuroscience
*  and modern AI. So please check those out if you value what I'm doing. Okay, enjoy Cameron.
*  So Cameron, I can tell that you haven't been outside for the past at least I'd say 15 minutes
*  because you're not dripping in sweat from the hot, soupy Houston summer weather. You have nice
*  air conditioning. I'm actually in Cambridge right now. So we do the climate refugee thing.
*  Every summer where we try to do fellowships somewhere. So I'm doing a fellowship this summer
*  with the Center for Future for Intelligence here that's funded by Leverholm and I'm a fellow at
*  Clara Hall here. So it's been a lovely day here. It was 50 Fahrenheit when we woke up and I went
*  for a run when it was about 60 along the cams. So don't worry about me. I had a spectacular day.
*  Well thanks for joining me here. So we have potentially a ton to talk about so we'll see
*  what we get to. I know that your sort of original background is in computer science and artificial
*  intelligence but you've and you still are very interested in those and we'll talk about those
*  things. You've pivoted a lot of your work to philosophy, to issues surrounding philosophy.
*  The first thing that I want to ask you in reading your work and watching a few of your talks,
*  you know you make reference to all these old philosophers and I don't know if this is,
*  forgive me if this is a hackneyed question, but I want to know how difficult it is. So when I read
*  old philosophy it's really difficult for someone like me whose elevator might not go to the top
*  floor to interpret you know the meaning of what they're saying and I have a sense that through
*  history every modern era at every step we interpret them slightly differently. Is that true and how
*  difficult is it to go back to these original sources and interpret what they meant by their words?
*  Yeah I mean I've had courses on historical philosophers in grad school so I had a bit of
*  the training and the terminology and so on but there is kind of an initial bar to get over that's
*  just regarding the way they use language differently and the way they structure sentences and so on but
*  I'm actually struck kind of in the opposite direction by once you get past that initial sort
*  of veneer of unfamiliarity how the philosophers I talk about like Locke and Hume are really
*  grappling with the same fundamental issues that machine learning researchers are grappling with
*  today for example you know the problems of induction for example you know I wrote a paper
*  sort of about that is a question so it's just it's the same question that confronts a machine
*  learning engineer which is how do I extract some general category representations from a finite
*  amount of experience right because you want your categories to be of the right kind of abstract
*  structure so that they'll generalize to future data that's maybe slightly dissimilar to the data
*  it's seen in the past it's basically the problem of induction you know and if you go through Locke
*  and Hume's treatise or inquiry you see you know they're talking about how do I learn causal
*  relationships for example from merely sets of contingencies that I see in my past right and
*  how do I learn to do geometry you know and how do I learn about number these are the problems that
*  they they spend pages and pages talking about it's the same problems that that you know people are
*  struggling with on on the cutting edge of deep learning today so you know I think it definitely
*  is a bit daunting when you first try to jump right into it and it sort of seems like you're
*  swimming in a very unfamiliar sea but once you get past that initial hurdle and I think also
*  going through a bit of secondary literature can help too you know so finding finding a philosopher
*  who's done a bit of the interpretive work connecting the this is one of the things that I try to do in
*  my work right is to give a kind of crib sheet for the machine learning engineers who are interested
*  in you know what what Locke or Hume or William James or Ibn Sina or whoever thought about these
*  problems what proportion of AI researchers is that that are interested in those I mean I think you'd
*  be surprised so you know one of the things I do in in the first chapter of my my book manuscript
*  is I go through and I point to all the places where the machine learning researchers or the
*  classical AI people more logic rules and symbols people make direct reference to philosophers
*  you know the the Russell and Norvig textbook which is you know as close to we have is like a
*  bible in AI you go in the first chapter and five pages in they're talking about Aristotle you know
*  and they say like you know this is basically an algorithm that you can read out of Aristotle and
*  code in you know one of your programming languages and build a little rational agent model and you
*  know in the AlphaGo paper you know I don't know if I'm jumping ahead but probably everybody's
*  already heard about AlphaGo the first sentence of the abstract you know they're saying we do
*  this with a tabula AlphaZero I guess it was we do this with a tabula rasa algorithm right that's
*  a direct reference to you know not just Locke but the whole empiricist tradition back to to Aristotle
*  and if you look at the skeptics you know Gary Marcus loves to invoke the empiricist rationalist
*  debate and frequently invokes Locke and you know I don't think the most charitable interpretation
*  of Locke but is always pointing to you know this is just the kind of continuation of what Locke was
*  doing or when Judea Pearl is is talking about the need to build causal models into his into
*  computational systems you know he's he's saying this is the the machine learning radical empiricist
*  perspective that he reads out of machine learning today is kind of a continuation of Humean skepticism
*  about causality so I think it's already there all over the place in the computer science
*  you know your point is taken that you know going from those quick references to the original
*  source materials and then trying to charitably interpret what those authors were really trying
*  to say is where I think some of the speed bumps come in but you know that's one of the things I
*  try to do with my own work is point to some of the secondary literature that I think is interpreting
*  that original source material in the most useful way to connect it up to the current
*  challenges in machine learning so I hope I hope that helps a bit you're one of the first
*  of a kind of a hand well of a handful of philosophically minded I don't want to
*  just pin you as a philosopher because you're more than that so you know I was almost I was
*  about to call you a philosopher you're one of the worst one of the first philosophers you're more
*  than that but anyway of a handful of people who are connecting the modern AI and lessons that
*  we're learning from modern AI to like a rich philosophical tradition like empiricism which
*  we'll talk about and and and you often say you know it's surprising that more philosophers
*  haven't started grappling with the progress in AI and the ideas and technologies that are coming out
*  how do you think AI is is shaping or affecting you know modern philosophy of mind just in a
*  grand you know high level view is it changing things because a lot of what you do is
*  say look here's this uh an autoencoder and this is how I forget at the moment you know this is how
*  this ancient philosopher used to talk about these faculties that that you know we have mentally
*  and and you connect those two but is AI you know transforming philosophy at all as well
*  I mean that's that's my hope um I mean it's it's in one sense it's it's changing things in another
*  sense a lot of the big pieces are staying the same but one way that I think that it can uh
*  influence the debate in philosophy for the better is in empiricist philosophy of mind for example
*  there's a number of places where uh locker hume or some you know William James somebody says well
*  the mind can do this thing and it's it's vitally important to my story about how we learn abstractions
*  from experience or or make rational inferences on an empiricist framework that the mind be able
*  to do this thing and I haven't the slightest idea how it does it right you know hume hume in
*  particular is is sort of admirable in his modesty here where again and again he'll say you know he'll
*  give you the evidence he it's sort of like he's laying out a kind of empirical case on on the
*  borders that look we do this we do this we do this so clearly the mind can do this type of operation
*  but I don't have any idea how and he even despairs that we'll ever be able to uh explain certain
*  things like the faculty of imagination for example is a prime uh place where hume says you know the
*  mind can compose novel concepts and dream up these fantastical situations that we've never seen in the
*  past and I just despair that we'll ever be able to understand how it does it and his rationalist
*  critics have repeatedly just savaged him uh on these points you know saying like it looks like
*  he's just he's just assuming some solution to a problem to to plug a hole in his view uh without
*  really having any way to explain it and they diagnose a deeper problem there so one of the
*  places where I think the the recent machine learning can really inform the philosophical
*  debate is by filling in some of these ellipses uh you know getting rid of this whiff of magic
*  to some of these key appeals that the empiricists have made in the past and showing how you know
*  vaguely brain-inspired computational mechanism could actually do some of these operations and
*  I think that that's the sense of wonder that a lot of people get when they look at the recent
*  products of like uh dali 2 for example you know if you've been on twitter anywhere you can't get
*  away from this stuff where you just give it a simple prompt and there's no way it saw anything
*  exactly like that prompt in its training set and it can paint you this beautiful picture of what
*  that would look like you know and it's it's the same sort of uh fantastical uh imagery that hume
*  was talking about in the treatise and the difference is you know we can scrutinize we now
*  have a computation computational mechanism that we can scrutinize and try to understand how it
*  works we're still not completely there yet and that's one of the places where I think you know
*  philosophy can then in turn uh provide some guidance back to uh machine learning and helping
*  figure out what are the right types of questions and what are the what are the kinds of understanding
*  that we want to have about how dali 2 for example is able to fuse you know a relatively scant text
*  prompt using its latent space representations and then craft such a beautiful output that seems so
*  immediately uh coherent and plausible to us how is it able to do that and what kind of understanding
*  do we want to have of systems like that because they're vastly complicated billions and billions
*  of parameters huge training sets uh that's one place where I hope that philosophy can then
*  come back and suggest some ideas about what questions we should ask of these systems and
*  what types of understanding we should hope to have of them and and how it all fits together
*  in a more coherent picture of how the rational mind might work you know instead of just trying
*  to solve some little marketable uh trick uh you know one particular task for the next benchmark or
*  publication in the next machine learning conference you know what what does this really add up to
*  uh together with everything else that we've learned recently in machine learning
*  about how human minds work or animal minds work you know how does it add up to a bigger picture
*  I think that's a question that often machine learning engineers don't don't get enough time to
*  ask themselves is dali 2 going to be the artist for your cover art on your book when it comes out
*  I mean we'll see there we've got to figure out the copyright issues for uh for the the results
*  produced by dali 2 but yeah I mean there's some open access ones I've already I had long ago had
*  one that I made myself in some of the earlier versions of taming transformers or whatever that
*  I really liked and I've had some people make some mock-up art for me in dali 2 that what remains is
*  between uh negotiation between me the publishers and uh and opening up well so I wanted to ask you
*  but you know a lot of your early work focused on convolutional neural networks which heralded in
*  the deep learning revolution right and you talk about something called transformational abstraction
*  which I'll ask you about in just a second you know but now and then you just mentioned transformers
*  and now we have transformers uh and then next year we'll probably have something else that'll be the
*  uh the model de jour as a as a philosopher is it hard to just keep up with the the pace of progress
*  in ai because it takes you have to sit and I know it's uh in philosophy you have to kind of swim
*  in the waters and then you have to think back to who's relevant and what issues were relevant
*  but then a new model comes out and you know for like cnn's right how do they do what they do
*  what does it mean and then now no you know not that no one's using cnn's obviously but now it's all
*  transformers and right it'll next year will be is that frustrating or is it uh I mean when you're
*  trying to finish a book it's certainly frustrating um I've been rapidly updating you know all the
*  chapters with the the past six months have been uh pretty breakneck uh but on the other hand uh
*  it's it's a lot easier to keep up with it's also fascinating uh and exciting you know it's it's
*  easy to try to read 10 papers a day when uh they're all potentially interesting I mean I do as a
*  philosopher and I I still have a lot of friends in computer science and there's no way I could do
*  this without uh talking to them on a regular basis so they provide me with a lot of help
*  uh it's harder for me you know for example to sort height from uh genuine advances because I
*  would have to read a lot more carefully uh go go through the method section to see what's really
*  going on so so getting some some pointers from my friends that are still in computer science helps
*  a lot but uh you know it's it's really a joy for me it's it's also the reason why I worked in animal
*  cognition as opposed to other areas of cognitive science or philosophy because I just I it's it's
*  what keeps me going as an academic is working in areas where it feels to me like fundamental
*  philosophical issues could really be empirically uh arbitrated on a on a almost weekly basis with
*  the new findings that are coming out in a way that you don't have and you know like fundamental
*  metaphysics or basic epistemology I don't want to knock any specific areas of philosophy but
*  Come on go ahead go for it. It keeps me excited anyway and able to keep turning on the computer
*  and looking at the cursor every day. All right but then yeah you must be thinking about your next
*  book project already or you know like oh yeah as well because you're trying to trying to finish
*  that sucker. Okay well uh so one of the things that you um that I guess we're going to talk a
*  lot about um that you have pointed to is this long-standing and continued dichotomy between
*  empiricism and rationalism and we'll talk about how you um sort of dispel of that dichotomy or
*  pick a winner I suppose but could you just um for people who aren't familiar uh can you just explain
*  the dichotomy between empiricism and rationalism traditionally and then you know how it continues
*  to be a subject of much debate these days? Yeah I mean as you frame the question like I'm sure you
*  know that it's a it's very difficult even to define those two terms and and outline the scope of the
*  debate and it's in large part because there's been you know at least four or five major incarnations
*  of this debate over history you know you could you could index it to Plato versus Aristotle you
*  could index it to Locke and Hume versus Descartes and Leibniz you could index it to you know William
*  James versus some of the early introspective introspectionist psychologists you could index
*  it to the Vienna Circle versus the rest of philosophy you could index it to you know
*  rationalists in epistemology theory of knowledge today so you have to pick what you think is the
*  the most important underlying threat the way I typically start is it's a debate over the origins
*  of human knowledge where you you know the first blush as you say the rationalists want to kind of
*  unpack our innate mental endowment and the empiricists think that most knowledge comes
*  from sort of interpreting the cipher of experience right so the question is where is where is kind of
*  like the structure from which human knowledge is built to be found is it is it somehow latent
*  within our minds or is it out there in the world for us to kind of uncover
*  you know that works pretty well but then of course you can you can interpret that in the
*  half dozen different more specific debates that that come to quite different things when when the
*  rubber meets the road in the particular incarnation that we have in ai today i think you wouldn't do
*  too badly by mapping rationalist nativism to sort of classical ai or at least hybrid ai where you
*  think you need at least some rules and symbols to be manually encoded from the beginning before
*  you know genuinely human-like learning can take place whereas the empiricist side wants to either
*  minimize or completely do away with any manual pre-specification of knowledge structures
*  before learning begins so the way i try to to transmute it into a useful debate today is to
*  say that the empiricist is trying to derive all that domain specific abstraction so that could be
*  things like you know shapes or numbers or causal relations or biological categories or kinship or
*  you know whatever all the things that some people think might be innate rationalist think might be
*  innate in the mind and the rationalist thinks no you need to build at least some of that structure
*  in manually from the beginning maybe like an intuitive theory of causality or an intuitive
*  theory of what objects are or maybe even some beefier like evolutionary kind of psychology
*  inspired stuff like kin detection or facial recognition or so and you think you need some
*  sort of manual pre-wiring of knowledge structures the core knowledge of the spelky yeah so so core
*  knowledge carry and spelky is sort of like the most popular and it's really that's kind of a really
*  minimal rationalist nativism in historical context you know so if you look at you know
*  jerry fodder in philosophy and coxsife 30 years ago or 40 years ago or you look at
*  the middle incarnations of chomsky and linguistics you know you're you know fodder notoriously says
*  like every single simple concept in the mind is is innate okay he means something kind of specific
*  by that or chomsky thinks you know you have hundreds of rules and parameters that are
*  innately specified in the universal grammar that then get sort of tuned to your particular language
*  core knowledge wants just you know a few pretty general concepts to be innately pre-specified like
*  object and agent and number so i you know the way i interpret the history sort of like the
*  empiricists have already mostly won the field that we've negotiated the nativists down from sort of
*  platonic or fedorian multitudes to just a handful and i still think i still think that that debate
*  is really worth having empirically very fascinating to arbitrate really worth getting into the details
*  of the experiments that are done in developmental psychology or also you know the way that i
*  recommend machine learning research is kind of entrance to the base it's sort of like a contest
*  where we can transmute this philosophical question that goes all the way back to Plato and Aristotle
*  it's kind of an empirical contest right where you just build some systems according to the
*  rationalist principles maybe hybrid systems of the sort that like gary marcus recommends
*  and you build some systems according to empiricist principles of the sort that you know like benji or
*  lacuna recommending you just see which ones are more successful or humanly but and this is like
*  the fundamental reason i wanted to write this book i think that the the rationalists are
*  misinterpreting what the empiricists should be allowed to build into their systems from
*  the beginning and i think that you know to understand how this mischaracterization started
*  you know i think you have to go back to the beginning of cognitive science which has been an
*  interdisciplinary field with a bit of identity crisis you know since the beginning it's anytime
*  you try to bring you know computer science and philosophy and linguistics and biology and all
*  these different fields together you're always going to face this question like what are we doing such
*  that we should all be talking to each other and trying to be engaged in this common intellectual
*  endeavor all the time and you always get this bedtime story about chomsky's review of skinner's
*  verbal behavior right and how the reason we needed the cognitive revolution was that
*  behaviorism which was you know empiricism and associationism and all the stuff that you know
*  at least by label i champion now was so terribly wrong and limiting and so on that we needed to
*  just completely break with it and have a paradigm shift away to a new way of thinking and then
*  the rationalists today like gary marcus you know he does this and steven pinker does this and jerry
*  fodder loves doing this and you know all the all the critics of deep learning almost love to
*  then paint deep learning as being the contemporary reincarnation of psychological behaviorism
*  and this is just totally wrong and so what i really try to do in the book is articulate
*  exactly why that's not the the way to set up this contest i think it's absolute this this contest
*  between the empiricist spots and the rational spots is exactly the contest we should be having
*  today but it is absolutely not the reincarnation of you know bf skinner or watson versus noam
*  chomsky and the 60s you know and and what they want to say is it's it's just you know statistics
*  pattern matching simple association on sort of computational steroids right it's just a couple
*  of simple principles of association like classical and operant conditioning and then you juice it up
*  with huge data sets and huge massive amounts of computation and that's all deep learning is
*  and what i try to do in the book is go through dozens and dozens or hundreds of models and show
*  how they all do something substantially more than that and in fact what they do is exactly the kinds
*  of things that what lock or hume or william james or heaven cina i talk about sophie de grouchy adam
*  smith all these other empiricists had these wonderful ideas where they had similar ellipses
*  like the one that hume had with the imagination and you can see how the structure that's built
*  into these deep learning models is really quite similar to the more ambitious ideas that they
*  had that go beyond simple operant and classical conditioning that was in the behaviors toolkit
*  so the question you know then becomes okay so what are the constraints on what the empiricists can
*  appeal to and i think you you know there have been some rationalist nativist philosophers in particular
*  laurence and marco who've written some nice papers about this who similarly complained from the
*  nativist side about setting up the terms of the debate in this way because there just isn't anybody
*  who's an empiricist and maybe there never was right if the only innate mechanisms you're allowed
*  to appeal to in your attempt to explain how the mind works are operant and classical conditioning
*  then you know not even the classical behaviors believe that because they even they needed you
*  know attention and they needed basic drives and they needed all kinds of other innate stuff that
*  was relevant to get behaviorist learning off the ground lock and hume and the others and deep
*  learning today also appealed to a variety of other domain general procedures that i canvas
*  under the term of faculties like memory and attention and imagination and there's just no
*  way to make sense of what they were trying to do without granting them these appeals to the
*  faculties that they make and their works what is a faculty though what it like um because i'm
*  grappling with this term whether a faculty is a potential or it is the you know because you
*  could set up a system so that has some inductive bias would you call that a faculty or you know
*  like what how big is the umbrella of faculty sorry to interrupt yeah no no it's a it's a good
*  question it's a question on which a lot turns and which has been arbitrated differently let's
*  say throughout the century so the let's at least the interpreters of aerosol so aerosol was a
*  faculty psychologist right he had the same standard set of faculties that we do you know
*  perception attention memory imagination and so on so this is this is something that's very deep in
*  human thought um and the scholastics that were interpreting aerosol at least they had a kind of
*  dispositional or what we now call a functional way of interpreting the factor faculties where they
*  give it a kind of they define it in time in terms of like a dispositional power to do a certain type
*  of thing right and then anytime you wanted to explain you know how is it that i form some
*  mental imagery you would just say oh well you have a faculty that has the power to do that
*  right this is this is consistent with a kind of form of functional explanation that uh you know
*  got made fun of a lot in early modern philosophy where you like explain why why is it that opium
*  makes you sleepy because of its dormant properties right this was just another example of that
*  and loch makes almost that same argument against the scholastic approach to the faculties um in
*  his work hume i think takes a different approach i think loch does too but hume makes it even more
*  explicit and you know some of the secondary literature that i was mentioning earlier that
*  would be really useful for people to dig into here is by a guy named thomas the meter tomas
*  the meter who's written a couple of articles rebutting foders interpretation of hume
*  in particular on the faculties like the faculty of the imagination and he suggests that um the
*  way that hume thinks about the faculties is not as some kind of dispositional definition where you
*  just have this thing that has the power to do this he treats it rather like a kind of empirical
*  hypothesis where you want to define like sort of cluster of uh effects you know so you say look
*  the human mind can do this and it can do this and it can do this these three or four things they all
*  seem kind of related to one another so these are things like fusing together different concepts to
*  make a novel concept like a unicorn you know as a horse with a horn coming out of his head
*  or the ability to form mental imagery or the ability to gauge the relative probability of
*  two events by forming uh images in your head about how those two things would those two scenarios
*  would play out you might say these things all sort of seem to have something in common with one another
*  let's call the thing that does that the imagination now i'm going to be absolutely
*  explicit that i haven't explained how the imagination does that but we do have something
*  that can do those things and they seem to roughly cohere together and then i'll try to characterize
*  what that faculty is like and hume says some things like it seeks novelty and it seems to
*  want to like complete pictures you know he has this a variety of things where he kind of sketches
*  around the edges of what the imagination is like but he never defines it and he never says he's
*  explaining how it works that's where i think you know it's really interesting to plug in some of
*  these more recent neural network architectures that can actually do some of these jobs uh like
*  generative adversarial networks or generative transformers and say you know look here's a
*  physical system that does not have any innate knowledge built into it of the sort that the
*  rationalist said you would need to have and it looks like it can do some of the jobs that hume
*  says the imagination could do now i don't go so far as to say like okay so now we've created a
*  system that has a real imagination right i approach it more from a standard kind of modeling
*  perspective in philosophy of science to say no of course this is a partial model of the imagination
*  but maybe it's modeling some critical like difference making aspects of the mind or brain
*  that allow us to do these things in our head and in that sense it can teach us some of the key bits
*  that hume you know based on the neuroscience or mathematics of his day he couldn't possibly explain
*  it can fill in some of those critical ellipses that then strengthens the whole empiricist package
*  when they try to explain rational cognition so you know i prefer to you know one of the ways
*  that tamas de meter puts it is that um it's it's all hume is often interpreted as as wanting to be
*  like the newton of the minds in other words trying to do a kind of physics of the mind where you have
*  these ideas that are bouncing off against one another like billiard balls um and kind of affecting
*  one another like physical particles and he says no that's not quite right in fact hume makes
*  uh a number of appeals in the treatise and inquiry into other sciences uh more biological
*  sciences like anatomy or more chemical sciences where the fusion of two things can be more than
*  the sum of its parts and hume is better interpreted you know when talking about the faculties
*  as doing the same type of thing that like an anatomist does when they try to theorize about
*  you know how a liver works or how a heart works where you you you have you need to have something
*  that does this job and you kind of sketch its position in a kind of architecture of other
*  mental organs and then you can start trying to theorize about how it actually works and from
*  a kind of mechanistic perspective from a variety of different perspectives using behavioral work
*  maybe using modeling work maybe integrating some neuroscientific findings into the story
*  and so i think that's the better way to to approach the faculties in these cases you used
*  a as a faculty psychology i think is the phrase and yeah you know some something like imagination
*  you know there are there are people these days who think that our folk psychological concepts are
*  incorrect or outdated or we need new terms because they don't map on to you know the quote-unquote
*  mechanisms in the brain in that so so when you use a term like imagination is that in the
*  psychological domain and and then we can look at mechanisms and keep them separate or is this a way
*  to fuse the psychology with you know a more with the biological or computer mechanistic
*  implementation level accounts right of of how these things play out in other words you know
*  are we fine just using a separate language for the mental psychological constructs that are these
*  faculties or or can we fuse them you know is there can we bridge that divide in with this approach
*  i i tend to be a mechanist in these types of disputes but then some of the more subtle
*  philosophy of modeling of the last 10 years has been about abstract mechanistic explanations you
*  know you've had kathryn stinson on that's that's one of the places where i draw on her work
*  also galtiero pichinini and and a few others have been writing recently about how
*  mechanisms you know mechanistic explanations for the brain don't have to be pitched at the most
*  specific grain of detail and they can be quite general and faculties you know are almost as
*  general as they get a lot of my previous work was actually cast at an even higher level of
*  abstraction at about cognition itself you know and so i wrote about what kind of mechanism could
*  implement cognition the faculties are a little bit more specific than that but it's not like
*  you know the imagination is going to map to a particular brain region that's thinking
*  much too simplistically about the relationship between computational models and how the brain
*  works i do think that we should try to draw as close a relationship as we can between the
*  architecture and other structural details of these neural network models and the brain's
*  operations and you know all other things being equal a model that has a tighter mechanistic
*  structural correspondence is to be preferred but those tighter correspondences are often traded off
*  against other things so you know for example this is a problem that you know fmri people forget
*  about the computational models but my brain differs from your brain right so you know if
*  i'm trying to interpret fmri there's going to be some slight differences even between where
*  certain functional capacities are localized in the correlates between my brain and your brain so
*  you know even just thinking about humans not even going to other species or to artificial
*  agents you can't go too specific i do think that there's a nice story that can be told at this
*  point about the deep convolutional neural networks and i try to do that in my synthase article to say
*  that these might actually be you know we might have actually located let's put it the generic
*  mechanism in stinson's terms if anybody wants to go back and listen to that podcast too that is
*  shared between deep convolutional neural network that's instantiated in a computer and the ventral
*  stream processing in the primate brain so this is a story that like james decarlo and his lab have
*  told in a number of different publications where the idea is that you know going all the way back
*  to hubel and bissel you have this alternation in the ventral stream between what they call simple
*  cells and complex cells right where they say the simple cells are responding to a particular feature
*  in a particular orientation and then the complex cells take input from multiple simple cells that
*  are detecting the same feature but in slightly different orientations or maybe in a slightly
*  different location and they fire just if one of their inputs fires above a certain threshold
*  let's see right so the simple cells have what you know we call an a linear activation pattern
*  and the complex cells have what we call a non-linear activation pattern and then the theory is that
*  there's lots of kind of layering of these simple and complex cells throughout the ventral stream
*  and this is in fact the the neuroscientific hypothesis that inspired some of the very first
*  deep convolutional neural networks all the way back in fukushima in the 80s right he was directly
*  inspired by this neuroscientific work the neocognitron yeah right neocognitron which you
*  know didn't get as much attention maybe as it should have back in the day because we didn't
*  really know how to train such networks effectively but the the basic insights of the deep convolutional
*  neural network were were largely there and the thought is so what you're looking for is a kind of
*  an abstract kind of mechanism that could be instantiated in very different types of substrates
*  but that captures the sort of key difference makers that allow a cognitive system to solve
*  a certain type of cognitive problem like object recognition for example and the way the story goes
*  right is that by passing the input from many of these linear feature detectors to a non-linear
*  aggregator and then stacking lots of those sandwiches of linear and non-linear detectors
*  on top of one another in a deep hierarchy you sort of iteratively make the detection of objects
*  more and more resistant to what the machine learning researchers and vision researchers
*  call nuisance variation right which is what makes object detecting hard and really is what made all
*  the classical good old-fashioned ai computer vision models fail because you you just there's
*  just too much nuisance variation and input that you can't explicitly anticipate at all
*  and program for it all using manual rules and symbols so the computational benefits that you
*  get from one of these deep linear non-linear stacked hierarchies and the ability to train them
*  gradually over time is what allows the thought goes both the brain and deep convolutional neural
*  networks like alex net and later inheritors to solve these visual recognition problems so much
*  more effectively than all previous methods and the to me that's a mechanistic explanation it's just
*  a very abstract one right and it's one that's at a level of abstraction that could be shared
*  between humans and monkeys and artificial neural networks in a variety you're built in a variety
*  of different substrates and and that's the sweet stuff right that's that's the sweet spot that you
*  want between making specific empirical predictions but also being simple and abstract enough that
*  you feel like you're really understanding some kinds of deep principles about how this works
*  in the case of jim decarlo and dan yamans and now many others work on using cnn's to model the
*  ventral visual stream you know they sort of limited the model to try to map it on as well
*  as they could to the various hierarchical levels in the brain and now there's like i think it's
*  called brain score where you can see how much variance your model explains with respect to
*  neural activity that's recorded but then of course the the size of convolutional neural networks has
*  just grown and grown and grown to where it's you know not not that it really resembles brains ever
*  but so it's less so it less resembles brains and thinking about like i don't know if we've
*  used them the word the phrase domain general faculty yet but that's what you were alluding
*  to earlier is these domain general faculties that kind of fit these various things in them
*  you know when you have a giant convolutional neural network let's say
*  i guess what i want to ask is you know would that still just be the same faculty at a larger scale
*  because it's doing something superhuman or would you potentially be building new faculties as you
*  scale up for instance does that make sense yeah gosh i mean that's a really interesting question
*  i haven't thought about entirely new faculties yet i'm already sort of committed to the idea that
*  um large enough differences in sort of computational scale or power can add up to
*  qualitatively different psychological functioning because i think that's really part of the case
*  that i make about like what's different between uh contemporary deep convolutional neural networks
*  and the simple three layer networks that you had back in the 80s and 90s is you know this is a
*  result that's been proven a number of ways in the computer science as you get exponential benefits
*  and computational power by having a much deeper network because you can recursively reuse some
*  computation that's performed by an earlier node relative to the depth of the network
*  so you can now solve some you know you can say like well in principle you know a three layer
*  neural network could approximate any function yeah sure if you had like you know computation
*  for billions of years and you had the number of processors that there are atoms in the universe
*  it's not really worth talking about but now we actually have physical mechanisms that can actually
*  do these problems okay maybe a lot of them require data sets that might be a bit larger
*  than the ones that say a human child's been exposed to that's actually a point that i
*  you know think is worth a lot of uh interpretive work as well um but they can do it you know in a
*  practical time period in a way that uh some of the earlier networks can and that's a direct result of
*  them having this kind of generic uh mechanism that that we were talking about just a second ago
*  um i you're right that the one that say decarlo's lab built was kind of constrained to be shallower
*  maybe more biologically plausible in its size than a lot of the ones that people are using
*  for state-of-the-art applications today uh and i think they're very interesting and deep philosophical
*  questions this is one of the questions i raise in my nature machine intelligence paper about the
*  problems of induction is is more directed at the possibility that these systems are discovering
*  real features that are kind of like necessarily beyond human can right that you know so i think
*  this is kind of vividly raised by uh alpha fold and alpha fold two right right where you say
*  there are these microbiologists who've devoted their lives to predicting protein folds
*  and then you know on its first shot on the task alpha fold just blows them out of the water
*  how does it do that and you can talk about you know the leaven bulb paradox and the complexity
*  of an amino acid chain and how many different possible uh degrees of freedom there are for it
*  to fold and say like there's just no way that it could see some features that are letting it make
*  these but what if it can like you know what if what if that system looks at this very complex
*  and just because it's so much larger uh in its in its deep hierarchy let's say than brains
*  plausibly could be that it sees some feature there and that feature has like let's say all of the
*  nice properties of being robust uh to differences in background conditions and and being maybe even
*  causally manipulable to to bring about certain app suppose it has you know all the special
*  properties or whatever you want of a real scientific property what do we say in that
*  case you know is are there real properties out there that are necessarily beyond human
*  intelligence and it's like the front the frontier of science now going to be defined by us relying on
*  on machines to see properties that we sort of like necessarily can't understand you know that
*  we rely on you know like the web telescope now to see things very distant away but we can understand
*  the properties that we're seeing but what these might be properties that are just like necessarily
*  beyond our our comprehension what what should we do about that um as as scientists or philosophers
*  of science entirely new faculties i don't know i don't even know how we would grapple with entirely
*  new faculties you know if there was some yeah sorry go ahead new new properties are bad enough
*  from my perspective uh but it could be you know that they just start uh out thinking us in some
*  way that we we can't even figure out the way in which they're out thinking us and and then we
*  might really be in trouble well i was going to say come on you're going to turn me into a singularity
*  theorist i'm not a singularity theorist but you're going to turn me into one well right but i mean so
*  a lot of what you focus on you know thinking about these domain general faculties is you know one of
*  the questions i was going to ask you is well how many do we need right is it a handful is it a bunch
*  and but but that is geared very much toward human intelligence yeah and we all know human
*  intelligence is the highest intelligence ever in the universe but well that's that's that's actually
*  i i the way i like to look at it for both humans and this is the way i kind of presented in the
*  book the way i like to look at for both humans and machines is that the faculties are solutions to
*  computational problems right so um nuisance variation is a problem and perception is a
*  faculty that's a solution to that problem you talk then you know what does perception let you do and
*  then you do this thing i was talking about thinking about the edge of a mental organ like what is what
*  is its role in the cognitive economy and then you start to theorize about the internal structure of
*  that faculty how does it do the job that it does um imagination is a solution to a computational
*  problem right you train up a deep convolutional neural network but it has a hard time generalizing
*  to add a distribution data right this is a just standard problem that all machine learning
*  researchers worry about you say like that's great but how is it going to create you know novel
*  representations or deal with novel situations you say well what if you had a generative system
*  that could recombine its previous experience in flexible ways to think about uh you know predict
*  what would happen in different types of situations or what different types of combinations that were
*  explicitly in its training set might look like that's a solution to a computational problem
*  memory is one of the best examples right there's a very classic paper by mcclellan rumlhart and
*  o'reilly right about um or is it mcclellan mcnaughton and o'reilly i don't want to get the
*  citation on yeah yeah the 95 paper anyway um about catastrophic interference sorry
*  catastrophic so complementary learning systems i just want to say the phrase that's right
*  catastrophic interference or catastrophic forgetting it sometimes gets called right but
*  there's this problem with all neural networks that they have a tendency when you train them on a new
*  problem they tend to overwrite their previously learned adaptive solutions to other problems
*  especially if there's some kind of thematic overlap between the two subject materials
*  that's a fundamental computational problem with any system that learns the way that brains or
*  artificial neural networks do right and memory is proposed as a solution to that problem
*  by by having different memory systems one that has a faster learning rate and one that has a slower
*  learning rate and doing kind of slow interleaved memory consolidation over longer periods of time
*  you know so that's the way i look at all of the faculties in the book you know i could tell the
*  same story about attention or about empathy and social cognition they're all solutions to
*  computational problems that are going to be faced by both humans and by robots and if you look at
*  it that way it's really not it's you know it's the same story um and it from my perspective it really
*  provides another form of confirmatory evidence that neural network type approaches to the mind
*  are the right way to think about things right when you find that the brain has developed some
*  kind of faculty or system whatever you want to call it that solves this computational problem
*  that our neural artificial neural networks that lack this system struggle with that suggests that
*  we're on to me we're we're on not only on the right track by modeling the mind's operations
*  with artificial neural networks but that we're also on the right track by trying to add more
*  faculties and faculty like processing to our deep neural network architectures and i think
*  this is really something that's already well underway and i think it's a it's a perspective
*  that's certainly very friendly and familiar to the way that deep mind works and a lot of other
*  researchers that have come from psychology and neuroscience that are now in deep learning i think
*  share this type of perspective so i you know i think one of the things i do in the book you know
*  so you start from this behaviorist caricature it's all just classical and operant conditioning
*  on computational steroids and you can show no look here's like five models from deep mind or
*  or you know some other modelers where they explicitly say we were inspired to add this
*  thing to our architecture by the way that memory works in mammalian brains to solve this specific
*  computational problem or you know you can look at dozens of models that say you know look we're
*  adding an intentional mechanism to solve this problem you know the the fundamental innovation
*  of transformers being a particular type of attention we're adding this sort of to solve
*  this very particular computational problem in a way that's you know vaguely inspired by the role
*  that this faculty plays in this type of processing in human brains and so that's that that that's why
*  i use the faculties as a kind of narrative thread to try to raise familiarity and awareness with a
*  much wider range of neural network architectures than typically get invoked in these types of
*  flashpoint debates you have you don't have an exhaustive list of our of the needed domain
*  general that goes but one of the things that you appeal to is in the days of old which doesn't
*  happen much anymore and you kind of put a call out that this is what ai researchers should be
*  focusing more on and some are are cognitive architectures people like you know chrysalis
*  smith randy o'reilly they're trying to you know build these things and and you you think at the
*  time is right now to start taking these modules and putting them together and then figuring out
*  how they can work together to do more yeah right intelligent things right exactly yeah most of the
*  so that i say in the book there's been a lot of faculty models but they've mostly been one-offs
*  right so they they just say like we're adding a memory store to this model and look at what cool
*  things you can do or we're adding some imagination like component look at the cool stuff you can do
*  or adding an attentional mechanism look at the cool stuff you do but you don't yet see somebody
*  trying to release a full deep learning cognitive architecture the way that you've seen as you
*  mentioned with older previous incarnations of so many more like sorry our actor yeah those are the
*  examples i talked about in the book and i think the time is definitely right for that but this is
*  another place where i think it would be really good to look at the history of empiricist philosophy
*  and this is not you know a novel idea i came up with but the thought is that as they try to combine
*  more and more semi-independent modules in a coherent deep learning cognitive architecture
*  they're going to face more control problems and coordination problems right where you know the
*  memory module and the imagination module might conflict or the attention module might have
*  multiple things sort of vying for its processing and these are problems that i think it would be
*  best to be proactive about at this point where we're just now starting to build you know fully
*  deep learning cognitive architecture that's not sort of hybrid but really like deep learning
*  through and through are how are we going to solve these control and coordination problems before
*  they they really become unmanageable and this is this type of problem is something that all
*  of the empiricist philosophers worried about sort of exhaustively in their famous works is
*  they worried endlessly about confusing the deliverances of perception and imagination
*  and memory they had kind of detailed almost processing level stories about how they thought
*  you should solve that problem in terms of like saliency and vibrancy different different properties
*  of the mental representation that they don't give you an algorithm exactly but you know they give
*  you really rich ideas you know i was mentioning i was just in scotland the the way i think that
*  i'd like these the neural network modelers to read the philosophy is sort of the way that like a
*  scottish landscape planter would go to you know the highlands to sort of take in the scenery and
*  sort of get inspired right and get the big picture it's not going to tell you how to do the code in
*  the same way that like looking at the beautiful view doesn't tell you how to paint the picture
*  but it's sort of like it's it gives you some ideas about what to try to paint and and why it's
*  valuable to try to paint that thing right and and i'm hoping that reading you know what you know
*  humor lock had to say about these control problems where the faculties might clash with one another
*  would provide that kind of inspiration to develop the algorithms that might actually solve the
*  problems in computational mechanisms do you think that that's going to be one of the harder do you
*  think that's going to be harder than what's being done in deep learning these days like the control
*  and coordination between modules you know there are even you know trade-offs between model-based
*  and model-free reinforcement learning in our brain right we're done to see which one takes over and
*  are they in competition are they complementary and right and that's just within a very narrow
*  domain right so then you have these other somewhat distinct domain general faculties that then need
*  to coordinate it seems like a different problem but i don't know that it is than you know learning
*  weights yeah i mean so there's that's that's certainly one of the ways that i think it's
*  definitely worth approaching the solution to the problem is to think of it as just another kind of
*  meta reinforcement learning problem or whatever where you have you know this is the way that like
*  matthew bottling likes to think about it for example is you've just got sort of another
*  reinforcement learning system that's doing something like executive control
*  and you you just train it to kind of select between different policies and the different
*  sub networks and you don't have you know at least i haven't seen a model quite yet where they're
*  they're working that type of approach to you know arbitrate between like memory storage and
*  visual imagery from an imagination module or generating internal monologue from a verbal
*  transformer but that's that's like the kind of work i would like to see try and maybe it maybe
*  it's just another reinforcement learning problem i don't know but maybe it's not right maybe maybe
*  you need to think about some other dimensions of the problem that are you know described by some
*  of the empiricist philosophers sorry to ask you a very specific question because i know you don't
*  have a an exhaustive list of domain general faculties but you mentioned empathy and that's
*  you know that we think of that as like a really higher cognitive capacity or faculty and social
*  um is language its its own domain general faculty where does where does language fit
*  or is it part of a social i see have a yeah just for narrative structure in the book i
*  treat it as as part of attention um okay as being well transformers exactly right um the thought
*  being you know and that's based a little bit also on my on a lot of my background reading into
*  you know people who treat language like a faculty how is it that they think that it works
*  you know what is it the let's say approach it from the perspective what's the uniquely human
*  uh right capacity for language that's not shared with you know like nim chimpski or or some of the
*  animals that they've tried to teach language to and the thought is well only we can learn grammatical
*  structures in terms of like recursive tree building syntactic structures somewhere in
*  a particular place in the chompsky hierarchy right um and a lot of people think like sort
*  of maybe what we have in you know our left temporal areas or whatever they get associated with
*  grammatical processing is a kind of a pointer system that lets us kind of like store locations
*  in a grammatical structure as the structure gets kind of elaborated to be more and more complex
*  so that we can process particular bits of that structure recursively in the right order you can
*  understand that as a kind of attentional mechanism right maybe combined with a kind of memory
*  mechanism right where the attentional mechanism is pointing to where you need to look in the
*  hierarchy and then um helping you so it could just be a particularly sophisticated form of
*  attentional mechanism i don't think the debates about how exactly to count faculties are really
*  quite as important as saying there need to be you know what what's the real debate to be had
*  between the rationalist nativist today and the empiricist is whether the empiricist should get
*  to appeal to a bunch of other domain general innate structure that does more than just a couple
*  simple learning rules and the answer to that is obviously yes the rest of the debates about how
*  many faculties there should be and which faculties uh there are and which ones are actually distinct
*  from other ones is i think a family dispute that's totally worth you know empirically
*  arbitrating you know another really interesting example where that dispute comes up is whether
*  memory and imagination are distinct and that debate actually has a very long philosophical
*  pedigree too you know going all the way back to Hobbes and Hume and a number of other philosophers
*  who weighed in as to whether uh imagination and memory are not distinct and Felipe de Brigarde
*  a number of other philosophers recently have have weighed in on that you know the thought being that
*  because we find that memory recall seems to be a little bit more creative and reconstructive than
*  the kind of photocopy replay picture of memory suggested you might think well memory is just a
*  particular mode of the imagination or something like that you know i i have kind of a particular
*  take on that where i think it's actually worth preserving the ends of the continuum but then
*  there might be some interesting middle positions you know so uh the psychologist niser talked about
*  this category what he called episodic memory which is uh like you know i don't know if your
*  family celebrates thanksgiving uh but you might have a memory of like a typical thanksgiving
*  dinner you know or some other holiday whatever holiday your family celebrates right where it's
*  not like it was a particular event the way that episodic memory is supposed to be but it's kind
*  of like slightly abstracted it might be an amalgamation of like 10 thanksgiving dinners
*  you know where somebody's got the game on and somebody's complaining about the turkey and right
*  you know these certain things happen kind of stereotypically it's somewhere in between
*  you know kind of creatively fully abstracted events and a particular record of a particular
*  occasion and i think there's going to be lots of examples that are kind of like blends you know a
*  mental representation it's kind of a blend or cooperation between two different faculties but
*  that doesn't mean that like my memory of what i had for breakfast this morning or what i did five
*  minutes ago is like a purely imaginative act and there's no difference between you know me recalling
*  what i had for breakfast and uh me imagining what it would be like to you know ride a unicorn on the
*  rooftop over there those are those are still pretty distinct modes of my mind and i think that's how a
*  lot of these disputes about exactly how to count the faculties and exactly what the borders of the
*  faculties are going to be should should work is where you have sort of like particular models
*  of how each individual faculty when it's kind of like in its purest mode is operating and then you
*  can understand a lot of the phenomenal cases as being kind of halfway in between or involving
*  cooperation or coordination between the faculties we do celebrate thanksgiving but um it's the
*  exactly the same every year we sit around we're all uh just talking about how much we love each
*  other and just super thankful the whole time and dinner always comes out perfectly so nobody
*  complains about the turkey no one complains about the turkey but so so you know memory imagination
*  dichotomy right empiricism rationalism dichotomy i wanted to ask you this and i'm i almost skipped
*  over it is just how to go beyond dichotomous thinking i mean i think that we maybe one of
*  our domain general faculties is dichotomous thinking right yeah for sure to put you know have
*  binary a versus b but it seems that historically and and you know like what you're doing with
*  domain general faculties for instance seems to dissolve some of the that dichotomy yeah um and
*  seems fruitful is there a methodological approach that you take to dissolve dichotomies or is it just
*  swimming in the waters of each of them and trying to understand what each camp is trying to say
*  and what they're really saying and so on i mean it's it's i think just sort of really taking the
*  time to charitably interpret what each author thinks some of these big banner terms imply
*  and kind of mapping them out on a on a conceptual map you know it doesn't have to be like a single
*  dimension continuum sometimes you might need even two or three dimensions but you know i think
*  i have a couple figures like that in my book where i try to say you know look you know
*  sure these are all rationalists in some sense but that just means they're kind of on one side
*  of this long continuum and they're important inter-party differences that are relevant to
*  the dispute with the other far side of the continuum in the sense where you want to say
*  like core knowledge is much more empiricist than fodder or mid-career chomsky or play-doh is
*  in a in a totally meaningful sense and the you know like lacoon might be less empiricist than
*  you know certain like bitter lesson hardcore just throw more computation at it
*  machine learning theorists and these are these are important differences that you want to recognize
*  to avoid the kind of caricaturing and talking past that i'm trying to urge everybody to stop
*  for us to have a kind of the most useful competition that we can have in this
*  this grand engineering moment that we have but you use the word charity there and i think that
*  charity is not used as often as it could be in these debates right i mean i think it's actually
*  quite important to give a charitess as most a most charity laden interpretation as possible
*  but like you said you know when someone you know like gary marcus or or someone comes in and goes
*  straight to the to the old debates right it's it's a less charitable interpretation and i don't know
*  if we just have a tendency to do that because it's the thing that's going to support our arguments
*  the most or or if it's more nefarious i don't know what do you think i don't know i mean subtlety
*  is hard and and the yeah the the mantras i mean i talk about this in the book the mantras that
*  you get from lock and hume because the language is is different um yeah they look pretty straightforward
*  in everyday english today but you have to actually read much deeper into the book to see what they
*  really mean by it i mean i do i do think that at least in some philosophy phd programs charitable
*  interpretation these days at least is very heavily emphasized you know or at least the people who
*  raised me uh in my phd program you know jonathan weinberg was one of my teachers in each sense i
*  like you before you're allowed to criticize somebody's view you have to defend it better
*  than they explained it themselves right right right and i i have very good memories from my
*  philosophy phd where one of my first publications was a bbs commentary and i went through sort of
*  16 drafts of that bbs commentary and sending it back to jonathan and he would say you know no
*  you know carothers doesn't actually think that read that read here and then okay where does he
*  say that does he actually explicitly say this or here's five other ways to interpret the thing that
*  he does say try again you know and i think everybody should try to go through that activity before they
*  they try to attack specific especially ridiculous views on on smart people and it would everything
*  would be better if everybody tried to do that but i mean a lot everybody can write you know philosophy
*  monograph on how to subtly understand empiricists versus rationalist thinking and it's one of the
*  hardest ones because it has so much philosophical baggage from so many different incarnations i mean
*  i'm still struggling with this based from comments that i get from people you know because if somebody
*  if somebody comes from being raised you know on the vienna circle carnap and you know versus quine
*  that's a you know this is logical positivism where you're supposed to not be able to
*  what empiricists meant in that case was every term had to be explicitly defined in terms of sensory
*  observations that would make it true and that's just a totally different conception of what the
*  empiricist rationalist debate is from you know the one that lock and humer fighting are the one
*  that playdo and aristotle were fighting are the one that we're fighting today and you just have
*  to be really careful that you're not importing some some assumptions about what those terms meant
*  especially in these interdisciplinary areas like cognitive science from your previous background
*  because these terms get used everywhere you know it could happen somebody interpreting them from
*  linguistics being raised on you know chomsky versus the the anti-generativists or you know
*  in developmental psychology the nativists versus the empiricists there and they all mean slightly
*  different things so you always have to be careful especially when you're porting
*  to a different discipline that it means exactly the same thing there you feel like you're uh do
*  you feel satisfied that you're uh towing that line okay oh i mean i'm not entirely satisfied
*  no no i'm never entirely satisfied i mean if you're asking me what i revise most frequently in the
*  book it's the first chapter where i try to define exactly what uh what empiricism and rationalism
*  mean i've got a whole subsection where i say here's here's eight other things it could mean and
*  it sort of means these three things in this book and it definitely doesn't mean these four other
*  things in this book and just to just to lay it all out there and try to make sure that we're
*  all on the same page it's a great question i should have asked you and i'll probably ask
*  future guests what do you revise the most it's kind of telling yeah but before we you know if
*  you have time i want to uh get on to talk about forward-looking content and teleosemantics but
*  before we leave domain general faculties um i want to ask about i guess two things you know one a lot
*  of our brain's power computational power i suppose if everything is computation is devoted to bodily
*  processes homeostasis breathing you know all these automatic processes that our brain has to
*  keep involved i mean is that something that you think a that should be you know do we need to
*  even need to worry about those when we're building artificial systems because they do have to interact
*  you know and they do affect our other domain general faculties or other uh cognitive modules
*  etc um so i guess that's the first question and then the second question is just thinking about
*  the spectrum you know we're talking about human level ai and maybe superhuman level ai like protein
*  folding right um but then thinking about you know your background in animal cognition and thinking
*  about the different kinds of domain general faculties animals non-human organisms might possess
*  is that something that we should be paying attention to or even you know can we even discern
*  what those domain general faculties might be sorry those were two different questions to throw at you
*  yeah let me let me take the first one before i forget it you might have to remind me of the
*  second one um so the first question is is should let's say machine learning researchers worry about
*  the more let's say autonomic and and lower level uh processing that the brain does and seems to
*  occupy a lot of uh hardware space let's say in in the brain is that is that fair enough
*  construal fair enough interoception but also you know yeah yes yeah and the answer is yeah
*  absolutely um and i think looking at the empiricists again is a great way to draw this
*  to drive this point home in particular william james was someone who was you know
*  often considered a kind of father of modern psychology but also very emphatic on this point
*  that uh the kind of autonomic and interoceptive uh aspects of cognition were just vitally important
*  to understanding how mentality works and how we get around especially with emotional processing
*  so you know if there was one really weak point uh in recent deep learning achievements i would
*  say it's in the ability to model emotional responses or what hume you know might have
*  called sentiments uh and these emotional responses and sentiments play an enormous important role
*  in all throughout uh you know at least from early modern to to today empiricists theorizing about
*  how the mind works it's uh they they give us uh kind of effective appraisals of of how we should
*  respond to situations and all kinds of important information and one place where this would be
*  really useful to be able to take advantage of in deep learning is in valuation functions right so
*  you know there's there's maybe several dark arts to uh deep learning today but you know one of the
*  trickiest dark arts i think is building a good valuation function for your reinforcement learning
*  algorithm right and i think all of the modelers will be totally forthright about that that
*  uh you know when you're when you're dealing with a simple game like environment like go or you know
*  like an atari game okay you can just use score or board control or whatever as a proxy for reward
*  but if you want to actually model rational agency more generally uh you know it's it's hard you know
*  one of the points i make and this ties back to some of the earlier points i made about you know
*  anthropofabulation which is sort of assuming that the human mind is not vulnerable to some of the
*  same problems that these artificial agents are we are terrible at this too right a lot of the time
*  when we're thrown you know h-index or us news and world report scores or uh you know social media
*  likes we often use these these easy quantitative proxies for value that are actually making us
*  miserable and not leading us in the right direction so again this is a computational
*  problem that both uh both uh computational systems and human brains are faced with and i think
*  listening to the body right um in particular as a rich multi-dimensional source of valuations
*  uh is one way that we solve this problem and that we really don't know yet how to integrate into
*  deep learning and there's lots you know there's lots of people making specific versions of this
*  proposal um you know lucy cheek one of my hosts here at cambridge uh has suggested that in animal
*  cognition she's primarily an animal cognition researcher and developmental cognitive researcher
*  is that um reinforcement learning in deep learning today mostly focuses on a kind of like
*  wanting system that you might map to the maybe dopaminergic system in the brain but animals also
*  have like needing and liking systems that are more sort of like effective attachment and then
*  more of like homeostasis kind of survival need and they're kind of like different valuation
*  systems and they're always kind of competing and playing off each other and it seems like
*  sorry is that kenneth barrage but am i the i don't know she might be drawing on that
*  i first read it from lucy so i don't know sorry sorry interrupt so you know the the thought might
*  be that uh we need to build in more of these um lower level valuation whether they're sentiments
*  whether they're needing liking and wanting whether they're uh effective appraisals emotional reactions
*  to uh succeed in a lot of the places where current deep learning agents especially when
*  they're released into kind of more open-ended environments uh seem to to presently fail pretty
*  badly yet and and that's a place where i think we still maybe need a kind of technological leap
*  forward before we can make real progress we seem to still be missing something the danger is always
*  present of turning the machine's power off or something like that where they have to
*  that wants that okay so i'll remind you of the other question which was
*  about animal cognition and i'll slightly rephrase it so we tend to you know i i map up my emotions
*  my thought processes onto my dog my dog is sad my dog is my dog feels fear right you know and these
*  psychological constructs that we talk about and share through our own language and our own
*  experiences as humans and this goes back to like you know building human-like ai or human level ai
*  you know how much how much do we need to pay attention to potential domain general faculties
*  of other organisms non-human organisms whether or not we can put a name to them or say anything
*  about what the actual experience is like for them are you are you thinking again about like
*  faculties that humans don't have that animals not necessarily but well should we
*  let's say imagination right would would yeah is is imagination a domain general faculty
*  ontologically sound right is it a thing that actually exists in the universe that a squirrel
*  also has or could have or is it that the structure of a squirrel's brain yeah and the the the way that
*  the architectures interact and the the neural activity interacts between modules in a squirrel's
*  brain does it develop you know a slightly different faculty something that is not quite
*  imagination or memory but might be something else you know does that make sense it's a poorly asked
*  sort of question let me let me let me let me give a couple of examples so i i do think it could be
*  the case that you know some animals lack some faculties that we have and other animals share
*  faculties that we have you know ideally once you had the kind of abstract mechanistic understanding
*  of the structure of the of the internal structure of the faculty that allows it to
*  play the roles that it needs to play to do the computational work that it needs to do
*  you would be able to use that understanding to see whether other animals have that faculty or not
*  but looking at other you know it's it's not that it's kind of just a one direction thing that you
*  go from the computational modeling and then you go around and check other animals to see if they
*  have it looking at other animals can actually help us figure out what's the right level of
*  abstraction at which to cast the faculty's nature as well an example i often like to bring up here
*  is like echolocation and cognitive mapping right so in animal cognition there's this there's tons
*  and tons of papers like do does x species have a cognitive map you know do bees have a cognitive
*  map do rats have a cognitive map do chimpanzees have a cognitive map right and in humans there's
*  all this great neuroscience you know some won the nobel prize for showing how the dentate gyrus and
*  the hippocampus and entral hynal cortex cooperate together to allow us to build cognitive maps of
*  our environment right and based on that level of understanding we have about you know how place
*  cells and grid cells work we can look then at other organisms and see like well should they have it
*  or not but if if we didn't have that level of understanding yet you you might look at bats and
*  say like well bats can't have a cognitive map because they can't see well enough that's a case
*  right where i would think there's like a clear mistake being made akin to anthropofabulation
*  where you think like the only way you could have this faculty is by exhibiting it in the distinctively
*  human-like way you know whereas humans mostly have visual cognitive maps based on visual landmarks
*  but why couldn't an echolocating organism have you know echolocating cognitive maps based on
*  acoustic feedback landmarks you know so that's a kind of case where you can
*  you can help decide what's really core to this faculty and its ability to do its computational
*  work and what's just a kind of contingent way that it's implemented in us by looking at other
*  biological organisms and that can help you maybe decide what you should build into your artificial
*  organisms as well you have time for some forward-looking content yeah yeah and it's
*  i mean of course i think it's actually related to a lot of the other stuff we've talked about
*  yeah i was about to say other you know non-human animals or organisms don't possess language
*  although you said languages within the attention camp of course most animals have well you would
*  assume have attentional mechanisms right because they have to figure out what to pay attention to
*  in the environment top down and bottom up but but they don't have like the symbolic
*  lingual processing and we don't need to go down the whether language requires symbolic thought
*  etc but i use that as a segue thinking of symbols and the symbol grounding problem and representation
*  you've had a long interest in meaning and so we're switching gears here to talk about your account of
*  representational content so i'm i'm going to kind of throw the floor open to you because i'm aware
*  of our time and maybe we shouldn't go down and too much under the weeds but i'm one so maybe you can
*  summarize your the forward-looking content account with respect to both telio semantics which you'll
*  have to define but also just uh selfishly since i've had mark big hard on the podcast and there's
*  some overlap between his interactivism and representations as anticipations of future
*  events based on our actions and your account as well although yeah i know that your account
*  involved is is much more intertwined with learning which is really interesting
*  so that was a mouthful but what is the forward-looking content view yeah let me let me
*  motivate it a little bit so i first got interested in this topic by looking at very similar debates
*  in animal cognition okay so you know one of the debates i looked at is um do animals have a theory
*  of mind which is you know maybe you think of it like a sub faculty of social cognition right which
*  is the ability to attribute beliefs and desires to other agents and so there's a bunch of experiments
*  showing that you know chimpanzees and i worked on some experiments with ravens and a bunch of
*  other animals can attribute at least perceptual states to other organisms kind of simple theory
*  of mind and then skeptics though would look at that work and say uh no those aren't theory of
*  mind because i can come up with simple associative explanation for those results right where it's all
*  in terms of observable cues uh that the animal was seeing at the time uh and they didn't actually
*  deposit some underlying mental state uh like they had a theory of mind do you understand the basic
*  opposition yeah so as a philosopher of science the thing that i found very funny about these debates
*  is that if you sat the two sides down and you said okay so what do you think the animal can
*  actually do and you describe a series of situations they agree completely they like agree on all the
*  behavioral capacities and they agree on all the experimental data and they have a very hard time
*  coming up with a future experiment that could possibly arbitrate between the two positions
*  that the animal does or doesn't have a theory of mind and that's a place where the philosopher
*  says like maybe this is actually a philosophical disagreement right rather than an empirical one
*  or you know there's not i'm not somebody who's like there's a big sharp divide between a
*  philosophical theory i think all philosophical theories should have at least some empirical
*  content to them but you know at least there's a kind of semantic disagreement here right because
*  if i put the disagreement like you think this animal has a representation of a perceptual state
*  yes you think this animal does not have a representation of a process yes okay so that's
*  what you disagree about now let's talk about your theories of representation maybe well you know i've
*  been around enough philosophers to know that that's that's a sticky business that's deep water um so
*  i'm reluctant to put it all on the table but daniel pavinelli you know uh love him for this
*  like he's willing to put all his cards on the table and say like you know look uh i think that
*  they should have a representation that like really causally co-varies with the underlying mental
*  straight across like this very wide maybe potentially totally open-ended number of different
*  situations and that's where i want to say no that's anthropofabulation right because humans don't
*  have that ability right humans can only infer that other humans have particular mental states
*  on the basis of observable behavior like we're not psychic right so we also have to use observable
*  cues that you could tell some sufficiently sophisticated associative story about if you
*  know you had a complex enough model uh that could learn those cues and make the same predictions
*  um so there was a there's a pattern there and it's now the pattern that i also see
*  in artificial intelligence uh today between the skeptics and the proponents of kind of ambitious
*  interpretations of what deep deep learning models are doing where you see some results some
*  experimental results either from the animal or from a new deep neural network system where they
*  do some cool behavior and then the the kind of enthusiast says you know ah look you know it's
*  like object detection or it's uh you know it's it's like imagination you know like dolly twos
*  doing some creativity you know it's another word that gets thrown around right um and then the
*  skeptic says no that's just statistics or that's just pattern matching or that's just you know
*  linear algebra that's not really that thing and you have to say well what's really the criteria
*  for having that capacity and it always comes down to representations in one way or another
*  right so in the animal cognition debate it came down to what is it to have a representation
*  of a distal mental state like a perception i see some particular thing or i believe some
*  particular thing in this case right like what the skeptics want in deep learning are core
*  knowledge concepts right so it's what is it to have a concept of an object or what is it to have
*  a concept of a cause these are again debates that are ultimately cast in representational terms
*  right so it doesn't seem like you can arbitrate the dispute empirically unless the two sides agree
*  on what it is to have a representation of that concept and that's where if you ask them you see
*  that the two sides have different implicit theories of representation in particular the skeptics game
*  right is they all they think they need to do is show a few cases where the other system makes some
*  apparent mistake that they think humans wouldn't make to say aha look see i exposed the fraud
*  right they don't have that capacity but humans make all kinds of mistakes too right so if you
*  want to say like well humans have a true concept of causation that deep neural networks don't have
*  even deep neural networks that are trained to solve causal inference problems there's all these
*  famous studies that show that you know even harvard undergraduates that just finished and got a high
*  grade in a physics course when you take them out of the classroom and you ask them these simple
*  physics problems they make these very elementary correlation causation and weird like impetus
*  principle mistakes that it seems like if they've just done a few calculations on a napkin they
*  could have gotten the right answer but they they still seem to have these mistakes like very deeply
*  ingrained in them that seem more applicable to a kind of interpretable in terms of a kind of
*  statistical theory of how things are going on so it can't just be making some mistakes any mistakes
*  that the ideal reasoner wouldn't make rules you out of the realm of the agents that could have
*  this concept you know whether it's causation or a belief of them or a mental state or whatever
*  but then you actually have to do the hard work to say okay so which mistakes are disqualifying
*  and which ones aren't and that's where you need a kind of principled philosophical theory i think
*  right now if you go back into the 80s in you know the the kind of heyday of the theory of representation
*  attempts to naturalize representation from like fodder or millikin dretzky telio semantics like
*  you mentioned earlier they all start from the perspective that this simple causal theory of
*  content where to have a representation of x you have to have some neural state that perfectly
*  causally co-varies with x is false and obviously false right because we all make mistakes
*  misrepresentation in other words it's just like a basic fact of mentality there's no concept we have
*  that we have we never make a mistake with respect to it so we need some different principle
*  that determines whether we have a representation of some particular content as that doesn't require
*  perfect use in other words and all of the different telio semantic theories are an attempt
*  to pick some principle that doesn't require perfect use but still ascribes determinant contents
*  okay i used to do you have a follow-up question before i go deeper into it or are we okay so far
*  i'm okay but i know these are deep philosophical waters i know i've read your work so i'm keeping
*  up but you know who knows but uh okay so so i don't know what to ask you for clarification
*  so yeah and a lot of them for example were appealing to evolutionary theory or
*  theory of information so dretzky's theory for example which was my favorite and is called the
*  telio semantic theory uh it tries to decide okay so what's the function of the representation
*  that's how you're going to decide what is the determinant content of the representation
*  without requiring perfect use you need to figure out what its function is and the way you figure
*  out its function according to dretzky is to look at the representation's learning history
*  so he interprets learning as a function bestowing process okay so what learning does is it like picks
*  up what he calls indicators that are you know say a neural state that you know maybe in the
*  perceptual cortex or whatever that happens to be activated whenever some particular uh thing in the
*  environment happens that then at least in that particular circumstance so let's say we're in a
*  brightly lit room and i have a particular neural state that uh lights up whenever i see my water
*  bottle in this brightly lit room uh and i learned that you know that water bottle affords drinking
*  when i'm thirsty then i might recruit that neural state through learning you know dretzky talks
*  about simple operant conditioning to control my drinking movements my you know grasping and
*  drinking movements okay a rat can do that uh but then turn out the lights right and in some sense
*  the water bottle is still there but that same neural state maybe doesn't fire you know i need
*  to learn that the water bottle looks differently or i need to use haptic feedback or whatever to
*  find the water bottle in the dark but that doesn't mean i don't have a concept of a water bottle you
*  know a representation of a water bottle according to dretzky he can still say well that that
*  representation still indicates the water bottle it still means the water bottle in a sense because
*  it has the function of indicating the water bottle right because that's what it was recruited to do
*  in those previous conditions so so the representation is the function or sorry i'm
*  going to jump in when i can with the case the representation is just a neural state it has a
*  function it's it's sort of like bestowed a function by learning when that representation is recruited
*  to control some desire satisfying movements right yeah so you kind of get the the teleology from the
*  the agency aspect of it right the idea being that you're you're a system with needs that need to be
*  met and you're thrust into an environment where you don't know how to meet those needs and learning
*  is a system that picks certain perceptual brain states or whatever and bestows them with certain
*  functions through this process of recruitment to control certain movements because it was successful
*  in satisfying that need when it triggered those movements in those circumstances in the past
*  in the past is key here right because it's a historically looking way of talking about
*  what a representation is because at every moment we are our best and most perfect selves and our
*  representations are always backward looking in that respect right and that the backward looking
*  aspect is the part of it that always bothered me i thought dreadsky's story was you know brilliant
*  ingenious and if you interpret his co-variation condition in the past recruitment situation
*  strictly that is anything that causally co-variated with it in the past all and only that thing is the
*  content of the representation then it solves this indeterminacy problem which is a horribly
*  difficult problem to solve and it's one of the only views i think that actually solves this problem
*  but then it's like sorry sorry state the indeterminacy problem again or i i can maybe
*  state it and you can then correct me it's that you can't um or just correct me if i'm wrong
*  um you it's it's you can't look back and say which strand of possible historical contingencies
*  led up to this um modern in the now content of the representation yeah so i mean a standard way
*  of painting the indeterminacy picture is uh you have a frog and you you've got a frog who sticks
*  out its tongue to eat flies right so you want to say oh well the frog's uh representation means
*  flies and then you know the skeptic says oh but what if i flick little bbs in front of the flock
*  and the frog's tongue sticks out and eats those too so what is the content of the representation
*  right is it uh is it fly because that was what caused the the that particular perceptual
*  representation to control tongue guarding movements due to some evolutionary selection
*  you know some of the more evolutionary oriented teleosemantic theories might say that um is it
*  bbs because it now darts to select bbs or is it some this is the really tricky one to rule out
*  is it some more approximate construal that is shared with both uh flies and bbs like small
*  dark moving speck right so in some sense you want to say like the fly is the more teleologically
*  satisfying answer because that's what actually solves the need but anytime it indicated fly
*  right it also indicated small dark moving speck right what does what does that say about the frog
*  so it it changed i mean one of the it depends on which time slice of dretzky we're talking about
*  is one of the things so yeah so like many great philosophers you know his views kind of evolved
*  over the years um and he played with different notions of indication so there's a strict notion
*  of indication so it's only what it you know actually co-varied with in that particular
*  circumstance and there's another more open-ended notion so it's anything that sort of like could
*  have co-varied with um that had this and so that's the particular tension that i wanted my view to
*  solve where you both need so on dretzky's view let me say just to clarify how misrepresentation
*  is possible on dretzky's view it's you know it's this is the part of the story that's implausible to
*  me is you can miss you can have a representation of the water bottle even when your representation
*  later doesn't perfectly causally co-vary with the water bottle that is you make some mistakes
*  either you grab something that looks like the water bottle that's really a you know duplicate
*  or you fail to grab the water bottle when it's right in front of you because the lights are out
*  those are two types of mistakes right on dretzky's view it's okay to make those mistakes that doesn't
*  like mean you're not competent with the concept of the water bottle because it has the content
*  of indicating water bottle given its recruitment history and it's only later when you're out of
*  that same environment of recruitment that you make the mistake right so for dretzky like you
*  can't make a mistake during recruitment it's it's like logically impossible and then mistakes are
*  possible only later when you move to a different environment that has different contingencies
*  and that both aspects of that always struck me as wrong you know as ingenious as the view was
*  because we make mistakes all throughout learning you know if you watch a kid learning to do
*  something and we recognize them as mistakes while we're learning and in fact it's crucial that we
*  recognize them as mistakes while we're learning because that's how learning works right if you
*  look at the acquisition of expertise for example in any domain you see that an agent that just kind
*  of blunders along with trial and error is never going to become an expert at that subject right
*  you have to attend to the causes of your successes and failures and try to like actively diagnose
*  where you went wrong and then correct your what we might call conception of the thing that you
*  were trying to interact with as a result of the mistake that you made to sort of get closer and
*  improve your use and that's how learning works all throughout the trajectory and so i thought any of
*  you that sort of like couldn't make sense of that is just misrepresenting the way that learning works
*  as a matter of empirical fact so what i wanted was a view that would save the the parts of
*  dratsky's view that were ingenious in work but not have misrepresentation be derivative of this kind
*  of artificial construal of learning where you don't make mistakes during the recruitment history and
*  then you only make mistakes later when you're in a different environment that has a different
*  contingency structure from the environment in which you learn and so the forward-looking view
*  is supposed to help with that now you know the forward-looking story just to get make a long
*  story short is you now don't ground content descriptions in the agent's learning history
*  or evolutionary history for that matter you rather ground them in the agent's own dispositions to
*  respond to representational errors okay so you know go back to the frog the idea is if i'm in doubt
*  whether the frog's representation means fly or bb i expose the frog through some you know open-ended
*  interactions to lots of flies and lots of bb's and see what it does now if it stops responding to the
*  bb's over a long enough period of time then i want to say it treated it like a mistake to respond to
*  those bb's in the learning trajectory and so it was always aiming at something else you know maybe
*  fly if however it continues to eat babies until it you know gets a belly full of lead as i think
*  frogs actually do then this view would say well it lacks the the capacity to revise that representation
*  to better indicate flies and so it actually does mean something that encompasses both fly and bb
*  like small dart moving spell and i think some animals are like that and some animals aren't
*  right like some animals are more flexible where they can learn to better indicate the reference
*  of their concepts through further interaction with the environment maybe potentially open-ended and
*  again i like to think of expertise here where you can learn to get better and better at indicating
*  something you know for decades so it's not like there's some definitive point at which learning
*  stops but if you're ever in doubt as to what the function of this representation is in the cognitive
*  economy we should be deferring not to some magic recruitment period but rather to the agent's own
*  dispositions to detect and respond to representational errors now that's that i like that view
*  also because it suggests ways to do experiments when you're in one of these situations where
*  you're not sure whether say you know the raven experiment i talked about earlier for example
*  was inspired by this type of view whether you're not sure whether the raven has a representation
*  of another raven's perceptual state or merely some a current cue for that perceptual state like
*  gaze like direction of the the raven's head or eyes which was the the skeptics preferred
*  explanation for all the data that had come before right they'd say well the raven doesn't really
*  understand anything about seeing it's just using this simple associative cue of where the raven's
*  eyes the other raven's eyes are pointed and so it doesn't need to understand anything about mentality
*  so what it says is you need to now make a further experiment where the raven has an opportunity to
*  learn about some other cues that indicate seeing that are not gaze like and that's the that's the
*  type of experiment that we did and the ravens seem to pass so the thought would be according
*  to the forward-looking view if the raven can recruit a potentially open-ended number of other
*  cues to indicate that that same shared disposition and to which it responds in the same type of way
*  and generalize its previous behaviors to these new cues then that suggests that the raven's
*  representation was all along aimed at you know perceptual state like seeing rather than just
*  gaze which it would stop responding to if gaze stopped indicating the thing it actually cares about
*  seeing and it further suggests a way now in machine learning i think you know i don't talk
*  about this in the book because i'm worried i would scare off all the machine learning
*  researches if i started going all this theory of representation stuff but you know it suggests a
*  way to arbitrate these dispute where you know gary marcus goes on twitter and he says you know
*  look i gave dolly to the prompt you know three blue squares in front of three red squares and
*  you know look it got the squares in the wrong order it painted them the wrong color
*  well if you gave dolly to the opportunity to learn about those situations and whether it got
*  the answer right or not and you gave it that kind of training so right like a lot of people who are
*  responding this to say well this type of situation or these types of relations were just not in the
*  dolly to training so why think that it would be good because of the kind of captions that people
*  put on pictures on the internet or whatever why would you think that it would be able to succeed
*  at that if it could learn to better indicate those relations through further rounds of training
*  online training especially where it's detecting its own errors right so you know if it's all just
*  supervised learning i might be more skeptical of applying the forward-looking story and saying
*  that actually has the representation but if we build systems that have the kind of self-supervision
*  of the sort that like lacoon is has been recommending for the last few years then i
*  would start to say you know look we have now a way to ask the system what it really has a representation
*  of by seeing whether it can get better at doing this by detecting its own representational errors
*  and improving its use as a result we still don't really have that that interaction and sort of
*  unguided self-supervised learning or at least we don't have deployable state-of-the-art systems
*  doing that yet but i'm sure it's just around corn yeah but if you took a thinking about like an oracle
*  let's say you train up a machine learning model and it answers everything then you freeze its weights
*  so it can't learn and it answers you know 100 questions correctly does that have content then
*  would you say that has content because it doesn't have to doesn't even it doesn't get a chance to
*  nor does it need to improve because its predictions matched its output and then what about the
*  uh the old guy next door who you can't teach him anything he already knows everything
*  maybe old dual older people who become more brittle or more um obstinate in their opinions
*  do they have less content or are they lacking content in their representations is that what
*  i should tell old man henderson over there gosh gosh you're gonna get me in trouble but but yeah
*  i think actually wow all right probably let's go okay that's it they at least have different
*  contents uh and you do so i mean the way i look at is it's not like actual futures that matter
*  so it's not like what you're actually going to do in the next 30 years it's rather uh based on what
*  you know now and the learning dispositions that you have currently if you had an open-ended
*  exploration of this environment how would you respond or how would we predict that you would
*  respond over time that's that's what really matters for the the content description on my view um so
*  a more flexible i think this is the right answer a much more flexible learning system can have much
*  more variegated and specific contents than a much less flexible learning system you know sorry um
*  but you know in some of these cases too like it looks maybe to us like somebody's making a mistake
*  when they say like no i'm fine and like you pointed out to them like no it's fine for me
*  who are we to say they're making a mistake right like maybe that's really the content that they
*  were after right um and and again i think that's ultimately why deferring to the agent's own capacity
*  and dispositions to revise is the right answer because that's what's going to make the right
*  predictions about their future behavior right i think the content descriptions should be
*  earning their keep uh as as psychological pauses right in virtue of making empirical predictions
*  that are borne out by uh experiments or or interactions with the the agents that have
*  those contents right and so for me that that's that's again sort of what always bothered me
*  about the backward looking gamut is that you're making lots of predictions about what this agent
*  is going to do if you ascribe contents that are like too ambitious for its own learning capacities
*  you're saying like it's you're predicting it's going to eat a bunch of flies that it just like
*  can't see or you're predicting it's not going to eat a bunch of bbs that it you know repeatedly
*  is going to eat until it fills its stomach completely um whereas the forward looking
*  gamut again it makes it possible to make mistakes but the mistakes should not be systematic
*  right in the sense that they should not persist indefinitely if you make a mistake it should the
*  agent should treat it like a mistake and be less likely to do that thing again in the future in
*  the similar circumstances and i think that's ultimately why content descriptions are useful
*  to scientists not just to philosophers is because they help us make a kind of prediction that seems
*  like we couldn't make otherwise you know you can call it whatever you want but you would need to
*  invent a new type of posit to predict how a dynamic system and maybe i'm starting to sound
*  like big heart here but like how a dynamic system is going to interact with its environment over
*  time where it's it's not a static thing neither the environment nor the agent is is static
*  you need to you know i often say if you want to shoot an arrow you need to aim where the
*  target is headed not where it's been and and i think that's the way to look at content
*  descriptions and psychology and and machine learning do you see you just mentioned big
*  heart and that was part of my original question do you feel comfortable just comparing his
*  account of representations and i guess content i don't think he appeals to learning necessarily
*  although he does allow for misrepresentation in the fact that you can have like multiple different
*  anticipatory futures that you're anticipating and that is the representation and then one can be
*  wrong or right and that's how you can misrepresent and then i guess learning is implicit in that
*  that yeah maybe i don't know i'm not sure i want to do a big heart interpretation but i do list him
*  in the paper as as another type of forward-looking view that was that was inspirational he i think
*  he focuses a lot more on the structure of anticipatory mechanisms in a way that i don't
*  but i generally agree with you know i i focus on this this kind of global total agent level
*  revision mechanism because i think that's the most useful to focus on for the purposes of animal
*  cognition but i think there's also a lot of other anticipatory mechanisms and he describes them you
*  know much better than than i do all right cameron i've taken you long enough i appreciate your
*  patience with me and uh and no thanks i hope it was useful oh we've gone down a long road yeah
*  so yeah thanks for being on yeah thank you
*  brain inspired is a production of me and you i don't do advertisements you can support the
*  show through patreon for a trifling amount and get access to the full versions of all the episodes
*  plus bonus episodes that focus more on the cultural side but still have science go to
*  brandinspired.co and find the red patreon button there to get in touch with me email paul at
*  brandinspired.co the music you hear is by the new year find them at the new year dot net thank you
*  for your support see you next time
*  the covers
*  they take me

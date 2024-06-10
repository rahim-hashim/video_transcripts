---
Date Generated: June 08, 2024
Transcription Model: whisper medium 20231117
Length: 5574s
Video Keywords: ['physics', 'quantum computers']
Video Views: 35381
Video Rating: None
Video Description: Patreon: https://www.patreon.com/seanmcarroll
Blog post with audio player, show notes, and transcript: https://www.preposterousuniverse.com/podcast/2021/06/28/153-john-preskill-on-quantum-computers-and-what-theyre-good-for/

Depending on who you listen to, quantum computers are either the biggest technological change coming down the road or just another overhyped bubble. Today we’re talking with a good person to listen to: John Preskill, one of the leaders in modern quantum information science. We talk about what a quantum computer is and promising technologies for actually building them. John emphasizes that quantum computers are tailor-made for simulating the behavior of quantum systems like molecules and materials; whether they will lead to breakthroughs in cryptography or optimization problems is less clear. Then we relate the idea of quantum information back to gravity and the emergence of spacetime. (If you want to build and run your own quantum algorithm, try the IBM Quantum Experience.)

John Preskill received his Ph.D. in physics from Harvard University. He is currently the Richard P. Feynman Professor of Theoretical Physics at Caltech and the Davis Leadership Chair at the Institute for Quantum Information and Matter, as well as an Amazon Scholar at Amazon Web Services. Before moving into quantum information, he was a leading researcher in quantum field theory and black holes. He is the winner of multiple bets with Stephen Hawking.

Mindscape Podcast playlist: https://www.youtube.com/playlist?list=PLrxfgDEc2NxY_fRExpDXr87tzRbPCaA5x

#podcast #ideas #science #philosophy #culture
---

# Mindscape 153 | John Preskill on Quantum Computers and What They’re Good For
**Mindscape Podcast:** [June 28, 2021](https://www.youtube.com/watch?v=UYt4QG8iZ6U)
*  Hello everyone, welcome to the Mindscape Podcast. I'm your host, Sean Carroll. If you have not been sleeping under a rock or whatever it is in recent years and you have some interest in physics and science more broadly, you will have heard of quantum computers.
*  You all know about quantum mechanics, you all know about computers. There seems to be a new thing on the horizon where we're going to use quantum mechanics to build a new powerful, different kind of computer.
*  In fact, I sometimes speak in the future tense, it's happened. We have working quantum computers right now, but so far they're not big enough and they're not efficient enough, they're not accurate enough to really beat their classical counterparts at any particular kind of calculation that you might want to do.
*  However, the technology is improving, the theoretical understanding is improving. We're very hopeful that pretty soon quantum computers will be doing things more efficiently for certain kinds of things than classical computers do.
*  So it's a very obvious fun topic for us to discuss here on Mindscape. We brought in one of the world's top experts, my Caltech colleague John Preskill. And John, like me, started out as a theoretical particle physicist, cosmologist, gravity person.
*  And he made a very explicit choice to move into quantum information science and quantum computing, and he's since become one of the world's leaders in that project. He's also the best person to talk to about the big picture for quantum computing, because as we'll discuss in the podcast, in the conversation, though he is certainly personally extremely excited about both the intellectual adventure of quantum computing and the technological prospects for making it work, he's also the best person to talk to about the big picture for quantum computing, because as we'll discuss in the podcast, in the conversation, though he is certainly personally extremely excited about both the intellectual adventure of quantum computing and the technological prospects for making it work, he's also the best person to talk to about the big picture for quantum computing, because as we'll discuss in the podcast, in the conversation, though he is certainly personally extremely excited about both the intellectual adventure of quantum computing and the technological prospects for making it work, he's also the best person to talk to about the big picture for quantum computing, because as we'll discuss in the podcast, in
*  the conversation, though he is certainly certainly extremely excited about both the intellectual adventure of quantum computing and the technological prospects for making it work, he is also relentlessly careful not to overhype. So he's very, very specific about what he thinks quantum computers will be good for, and especially this sort of most obvious thing in the world, which is simulating quantum mechanical systems, like chemical reactions or materials or something like that. It's less clear that quantum computers are going to be very helpful for giant optimization problems, the traveling salesman problem or something like that, but maybe they will.
*  So we talk about what quantum computers are, what the best technologies are to make them happen, and the prospects for using them, where they will really be useful, what kinds of problems we'll be addressing with them, why people are so excited about it. At the end of the day, probably will not have a quantum computer in your smartphone, but they probably will be useful for various things we can't even yet anticipate. It's clear that this is a very exciting time to be thinking about this stuff. I mean, we not only talk about quantum computers, but how the ideas from quantum computers are going to be used in the future.
*  And I think that the idea of quantum information theory have radically changed our views of quantum gravity and black holes and emergent space time and some of my favorite topics along those lines. This is also an area where John is one of the world's leaders, so he's a great person to talk to about it.
*  So what do we have to do that we have resources out there for mindscape listeners? We have a whole website, preposterousuniverse.com slash podcast. You can get not only the audio files, obviously, for the different podcast episodes, but we have show notes. So there'll be links to people's web pages and their Twitter bios and things like that. And also we have full transcripts for every podcast. So if you want to find something, there is a search engine right there. If you say, well, someone was talking about that on mindscape, we have very, very good ways to do that.
*  So we have a whole series of searching the entire mindscape archive for whatever topic for whatever keywords you want to look for. So check that out preposterousuniverse.com slash podcast and let's go.
*  John Presko, welcome to the mindscape podcast. Great to be here, Sean. So you're someone who did something interesting. I mean, you've done many interesting things, but among the interesting things is you had a good career going as a pretty straightforward
*  quantum field theory, particle physicist, cosmologist, the kind of stuff that I grew up doing myself and thinking about. And somewhere you made a not very dramatic, but a noticeable shift into quantum information and quantum computing.
*  So I guess can I mix up two questions together? First is why that shift? And secondly, do you have any bigger picture thoughts about shifting one's research focus later in life? I mean, you're at an age when many physicists are thinking about retiring and in some sense, you're peaking now in terms of your contributions to a very vibrant and active field.
*  That's hard to do. That's just yet to come. That's right. Exactly. Well, so the shift you're talking about occurred about 25 years ago. And, you know, well, you were around then. This was the mid 90s. And what happened, I think, which made me more receptive to going in a new direction was the SSC got canceled.
*  Oh, yeah. You know, for my generation of particle physicists, it was that was our great hope. Right. We were a little too later. I was I'm older than you. But I got my PhD in 1980 and missed by a few years the opportunity to participate and solidifying the core theory, the standard model of particle physics.
*  So so our big hope was what comes after the standard model, the so-called, you know, beyond the standard model physics, where we thought there were a lot of big questions that we could answer. And that was what the SSC was supposed to do. The superconducting super collider.
*  They started digging a tunnel in Texas and spent a couple of billion dollars and then for complex political reasons, it got canceled. And so I started to ask myself, what now?
*  You know, it was we were going to be able to do some of that physics eventually. Yeah. But it was maybe a couple of decades away. And I think that made me more receptive to looking into new things. Now, meanwhile, while I was waiting for the SSC, I was thinking about crazy stuff like how to black holes, right?
*  Process information. And that was my excuse for digging a little bit into quantum information. And, you know, I learned about things like quantum teleportation and quantum cryptography, partly for fun and partly because I thought those ideas might be helpful for understanding information processing at a more fundamental level.
*  And then something big happened. Peter Shore discovered the factoring algorithm. That was 1994. And that was an eye opener for many people, including me. You know, it made me feel that this was a serious business, that the difference between problems we could solve with computers and the problems we can't solve because they're too hard.
*  You know that different shifts because this is a quantum world, not a classical one. And I just thought that was a really, really interesting idea. And you know how it is when when you're in the middle of a transition like that, you don't quite see it happening. It seems a little more adiabatic. But over the course of a couple of years, you know, I realized most of the things that I was excited about and thinking about had to do with quantum computing.
*  So it sounds like it's a there's a little bit of everything because I can imagine these shifts happen. Sometimes like you say adiabatically people just gradually shift. Sometimes it's an intentional reflection on what they're doing. And sometimes there's some external event that might shift things. And for you, it was all three at once.
*  Yeah, of course, you know, I imagine there's a little bit of rational reconstruction of what happened in the description I just gave you. It was a somewhat complicated time because you know, I had students and they were working on various things and some of them got excited about quantum computing and some of them didn't. And but you know, everybody turned out all right.
*  Well, and do you have then any lessons for this question more generally in academia even forget about physics? I mean, we don't really encourage or set up or provide pathways for people to make dramatic career transformations in the middle of their careers in their 40s or 50s, right? I mean, should we or you know, is the system pretty good as it is?
*  It helped that I had tenure. Yeah, you know, I didn't have to worry about that. And so I had that luxury of, you know, taking a year or so to acquaint myself with another field. It was easier then because the field was new and there wasn't as much to learn. It was small.
*  But what was really helpful and you've had this experience to probably is I taught a course. Yeah. And you know, I did that for the first time in 1997. And you know, a lot of the stuff was pretty fresh. And I really enjoy kind of synthesizing materials and try kind of distilling them to what I think is important. So that was really fun to do. But it also deepened my understanding and made me feel like I was, you know, kind of on the cutting edge of the field by the time I finished teaching. And I was really excited about that.
*  And I was really excited about that. And I think that's what I was able to do. And I think that's what I was able to do. And I think that's what I was able to do. And I think that's what I was able to do. And I think that's what I was able to do. And I think that's what I was able to do. And I think that's what I was able to do. And I think that's what I was able to do. And I think that's what I was able to do. And I think that's what I was able to do. And I think that's what I was able to do. And I think that's what I was able to do. And I think that's what I was able to do. And I think that's what I was able to do. And I think that's what I was able to do. And I think that's what I was able to do. And I think that's what I was able to do. And I think that's what I was able
*  to do. And I think that's what I was able to do. But know when the
*  research was a really interesting
*  and valuable that I was so fascinated by it. So it's a great community. And, you know, I learned a lot from from people with conferences in summer schools those first couple of years. And that was really fun to
*  too.
*  quantum information is? Well, I'll tell you what a quantum computer is not. It's
*  not just a computer like the ones we have now, but much, much faster. It really
*  processes information in a very different way. And to sort of jump past
*  the what is quantum mechanics part? Well, not really. I mean, in quantum mechanics,
*  when you have a lot of particles, the description of how those particles
*  behave that quantum mechanics uses has great extravagance. If I wanted to
*  describe in terms of ordinary information, classical bits, the way we
*  usually store and process information in ordinary life, if I wanted to describe
*  what a quantum system with many particles is doing, the number of bits I
*  would need is just inconceivably vast. Now, there's a catch though, which is, of
*  course, if I want to get information out of a quantum system, I want ordinary
*  classical information, you know, bits I can write down or put in my head. And to
*  get information out of a quantum system, well, you know, if you, qubits are what
*  we call the fundamental units, the analog bits, you have to measure them.
*  And when you measure a qubit, you just get one bit of information. So, you know,
*  if you have a few hundred qubits, a description of some typical state of a
*  few hundred qubits in terms of classical information would be something you could
*  never write down because it involves more bits than the number of atoms, the
*  visible universe. But if you want to get information out, you can't get more than
*  300 bits out of 300 qubits. So this is the tension in quantum computing that
*  somehow this extravagant quantum world, which is largely hidden from us as a
*  resource, if we can figure out how to use it. But it's not a simple thing
*  because, you know, we're our access to all that rich quantum information is very
*  limited. And so it turns out we can't use quantum computing to just speed up any
*  problem we want to solve. The problem has to have the right structure and we have
*  to be sufficiently clever to figure out how to use all that rich quantum
*  information that's, you know, behind the barrier that we only have limited
*  ability to penetrate.
*  So when you say qubit, the classical bit is zero or one, the qubit is in some
*  superposition of zero or one. Probably most mindscape listeners have heard me
*  say words like that before. And then, of course, when you have multiple qubits,
*  they're entangled with each other. And it would seem to me like just one qubit in
*  principle, that there's probably a way of thinking about why quantum computers are
*  better, which is entirely wrong, which is that even one qubit has a huge amount of
*  information, right? Because it requires a real number or even in fact a complex
*  number to specify where you are in that qubit land, whereas a classical bit is
*  just zero or one. But that's actually not the important thing. The important thing
*  is the entanglement between the qubits, right?
*  Yeah. And that's why we seem to be forced. If we want to describe in terms of
*  class, there's sort of a mismatch between information in the classical world and in
*  the quantum world because of entanglement, entanglement of when I have a system with
*  many particles, which are highly entangled. That's the word we use, you
*  know, for the characteristic correlations among the parts of a quantum system that
*  has many parts. The correlations among those are just different from correlations
*  among parts of a classical system. And what's so interesting about entanglement,
*  from my point of view, is that there's no succinct way of describing it in terms of
*  classical information.
*  And I think that some of the things, one aspect here that maybe the non-experts
*  don't appreciate as much is that entanglement really wasn't that big a deal
*  for many, many decades after we invented quantum mechanics, right? I mean,
*  Einstein, Podolsky and Rosen sort of tried to emphasize it and we had these
*  puzzles. But probably you, just like me, when we took our quantum mechanics
*  classes, there's a lot of tunneling through barriers and simple harmonic
*  oscillators and solving the Schrodinger equation. And its entanglement was kind of
*  there in the background, but not emphasized. Is that an accurate way of
*  putting it?
*  We didn't learn Bell inequalities. So Einstein, Podolsky and Rosen, that was
*  1935. And there were some thoughtful responses to that paper, which talked
*  about how these correlations in quantum systems are different from classical
*  ones. From Schrodinger, for example, who understood pretty well what it meant.
*  But not much happened for 30 years. And then Bell in the mid 60s came up with
*  this idea of Bell inequalities, which in a very visceral way indicated how these
*  correlations are different from the ones we can realize, you know, with ordinary
*  information like we encounter in everyday life. And so I could have learned
*  that when I took quantum mechanics, because I took quantum mechanics in the
*  early 70s and Bell did that in the mid 60s. But it was just it wasn't part of
*  the quantum curriculum, I guess it wasn't for you either. Now it happened,
*  though, something and maybe this also planted a seed, which partially explains
*  the answer to your first question about how I made this transition. When I was an
*  undergraduate at Princeton, you know, we were supposed to do a research project
*  when as juniors and who knows how to do that. So you have to go around and knock
*  on doors and see if anybody has any idea. And somebody suggested to me, because I
*  said, as undergraduates often do, oh, I'm interested in the interpretation of
*  quantum theory to one of the professors, he said, Oh, well, you should, you should
*  look into the EPR paradox, which I'd never heard of. But it turned out there
*  was a instructor who had just arrived at Princeton that fall, who had just done an
*  experiment for his PhD with john clauser. That was Stuart Friedman. Friedman and
*  clauser did this experiment in, you know, the early 70s, which was, oh, well, one
*  of the first to sort of convincingly show that these Bell inequalities are
*  violated in a quantum system. And so, you know, there really is a difference
*  between quantum and classical information. And so, you know, I pumped him a little
*  bit. And I wrote a little paper about EPR. So I thought about that. So, and so
*  that probably also made me more receptive to some of this quantum information
*  stuff when 20 years ago, I realized it was pretty interesting.
*  I'm excited to share the news that the great courses plus is now one dream.
*  One dream is everything we know and love about the great courses plus and so much
*  more. Wonderium provides fantastic video and audio learning experiences, tons of
*  great content to enrich our lives with mind blowing moments. And you can still
*  stream all of your favorites from the great courses. These include videos that
*  are created in partnership with National Geographic, Smithsonian history and more.
*  If you like the topic of today's podcast, for example, there's a course by Mark
*  Berkson on Wonderium called cultural literacy for religion, everything the well
*  educated person should know whether you believe or not.
*  Religion plays an important part in human history and you can learn that right there
*  on Wonderium. So sign up now through this special URL to get this great offer a 14
*  day free trial of unlimited access.
*  Go to wonderium.com slash mindscape.
*  That's W O N D R I U M dot com slash mindscape wonderium dot com slash
*  mindscape.
*  Well, that's interesting because like you say, every undergraduate wants to think
*  about the interpretation of quantum mechanics.
*  And usually that instinct is just beaten out of them.
*  But for you, at least it turned into something productive.
*  Now, years later, I take it that what one stances about the interpretation of quantum
*  mechanics doesn't really enter into your everyday life as a quantum information
*  theorist. Right. I mean, I talk about the interpretation of quantum mechanics a lot,
*  but let's just be clear to the audience.
*  The practitioners in the field kind of don't spend their time worrying about that.
*  Is that also accurate?
*  It's less accurate than it used to be, I think.
*  At least in the quantum information community.
*  Some young people, I think, are attracted to quantum information because, you know,
*  they think it is revealing concerning the foundations of quantum theory.
*  Even so, I accept your statement that it's not it's not what it's not our bread and
*  butter. Even in quantum information, there are other things that we're usually
*  thinking about unless we're listening to you or reading one of your books or
*  something. Having said that, do you have a favorite formulation of quantum
*  mechanics at the fundamental level?
*  I'm an Averettian.
*  So I think you and I are pretty aligned, actually.
*  Yeah.
*  I'm comfortable with nothing happening in the world besides unitary evolution.
*  If your audience knows what I mean by that, then measurement isn't something
*  fundamentally different.
*  And, you know, what I and people say, well, it's, you know, but it requires all
*  these worlds and stuff.
*  So that's another place where the word extravagant seems appropriate that we
*  need to have this very, very rich description of experience because we
*  include all the alternatives.
*  But I guess my question would be then, well, suppose it were true.
*  How would the world be different than we actually experience and observe it to be?
*  And so I just find that appealing.
*  It seems minimal.
*  You know, there's nothing happening but the Schrodinger equation and things are
*  evolving. And if we can reconcile that with what we observe about physics, then
*  I think that's, I mean, if you prefer another interpretation, that's fine with
*  me. I'm not going to get dogmatic about it or anything, but I'm pretty happy with
*  that.
*  That sounds good to me.
*  I'm not going to, let's just declare victory right there.
*  Yeah, exactly.
*  So we have these qubits.
*  They can be superpositions of zero or one.
*  If you measure them, you're going to get either zero or one or whatever product,
*  whatever actual physical property you're measuring of them.
*  And they're entangled.
*  So can we just be a little bit more specific to help the audience out there
*  visualize what exactly does that mean that they're entangled?
*  And how does that mean that there's more oomph to the computation of the
*  world?
*  So I think that's a good question.
*  So what does that mean?
*  Is that entangled?
*  And how does that mean that there's more oomph to the computational power?
*  Well, what it means is that even if we have a complete description of the full
*  system of all the particles and by complete, I mean, you know, the most
*  complete description that we think the laws of quantum mechanics will allow.
*  When we look at part of the system, we can't predict what we're going to see.
*  You know, we can have a complete description of the whole thing, but still
*  be very uncertain about the parts.
*  That's what entanglement is.
*  So, you know, you could imagine like you have a book and it's 100 pages long.
*  And if it's an ordinary book, you can read the pages one at a time, or you can
*  even give each page to a different friend and they all read the pages and they get
*  together and talk and they can reconstruct everything that's in the book.
*  But if it's written in qubits and the pages are highly entangled with one
*  another, you can look at the pages one at a time, but you just see random
*  gibberish. You don't get any information from it or essentially none.
*  And that's true even if you look at all the pages one at a time, you're still
*  missing almost all the information that's in that quantum book.
*  There's information there. You just can't read it that way because the information
*  isn't printed on the individual pages.
*  It's encoded almost entirely in how these pages are correlated with one another.
*  That's the entanglement.
*  And describing those correlations in terms of ordinary bits, that's what's so
*  expensive to describe that the way we usually describe and think about
*  information is completely unreasonably costly.
*  And so that's the way I would look at the reason why we can't just use the
*  computers we have today and simulate what's going on in some complex quantum
*  system. It's just too hard to do.
*  And the way that helps us with the computer is, if I think about what a
*  computer is, it has memory, it has processors, it has algorithms.
*  It's really sort of the processors that are being improved here because they can
*  sort of well, let's ask it this way.
*  There's a couple of wrong ways of saying it.
*  And let's get those out of our audience's mind.
*  One way that I know Scott Aronson always gets annoyed at is that it's not really
*  like there's a whole bunch of universes doing separate computations and eventually
*  finding the right one. Right.
*  I mean, do you agree with him that that is a bad way of thinking about quantum
*  computing?
*  It's not completely wrong, but it's very misleading because it would lead you to
*  expect that we can speed up anything with a quantum computer, any problem we
*  want to solve.
*  And the catch is what I said earlier, that, you know, in the end, you're going to
*  have to measure something and you can only get a limited amount of information
*  out, even if, you know, all these computations in some, you know, fanciful
*  description of what's going on are occurring in parallel, a vast number of
*  computations.
*  We got to eventually bring them together and read something out.
*  And so the art of making a quantum algorithm that's powerful is that when you
*  combine them all together, you get something useful.
*  And it's not so obvious that you'll be able to do that.
*  No, no, no.
*  Entanglement is very complicated to describe classically, I just claim.
*  But does that make it useful?
*  It's not so obvious.
*  So said in another way, what's obvious is that it requires a lot more information
*  to specify what's going on in an entangled quantum state than in a bunch of
*  classical qubits.
*  But it is not at all obvious that you can put a lot of information in a quantum
*  state.
*  It's not so obvious that you can put that to useful work.
*  Yeah.
*  And I think, you know, the best reason we have to think that quantum computers are
*  powerful is that we can't simulate them with ordinary classical computers.
*  Now, that doesn't tell us exactly what they're good for.
*  But it does kind of point us in the right direction.
*  You know, this was Feynman's idea 40 years ago, almost exactly 40 years ago.
*  It was in May of 1981 that he proposed that if you want to simulate quantum
*  systems, complex quantum systems with many particles on a computer, you
*  shouldn't use an ordinary computer because that'll be just too hard.
*  It should be a quantum computer.
*  And that's still the best idea we have about how to apply quantum computation
*  to something that people will care about.
*  Because simulating quantum systems is important.
*  If we can, you know, we if we could, we would simulate complex materials and
*  complex molecules on our computers now and predict how they'll behave.
*  And that would point us presumably towards new types of materials with
*  properties that we find useful or new types of catalysts or pharmaceuticals and
*  so on.
*  And to a certain extent, people do that, of course, in quantum chemistry and in
*  computational quantum physics.
*  But it's very limited what we can do with ordinary computers just because it's so
*  hard to simulate highly entangled quantum systems.
*  And that's what we have.
*  What if we have many particles and they're interacting strongly quantum
*  mechanically with one another?
*  It's really hard to simulate with a quantum computer.
*  We think we'd be able to do that efficiently.
*  And that's the from what we can currently foresee.
*  That's the application, which is most likely to have a big impact on the world.
*  Now, quantum computing is so different from the information processing we've
*  been familiar with up to now.
*  Then, you know, we probably have very limited ability to forecast what its most
*  important applications are going to be.
*  But based on what we concurrently project and have some understanding of, it's
*  those applications to simulating complex matter, many particles interacting
*  quantum mechanically, which will be the most important application.
*  Now it came as a bit of a shock.
*  And that's what caught my attention in 1994, that you could use quantum computers
*  to speed up solutions to other problems, which don't on the face of it seem to have
*  anything to do with quantum computing.
*  And, you know, Shor discovered that quantum computers would be very good at breaking
*  codes, that they could do things like finding prime factors of very large numbers.
*  And of course, that caused interest in the field to ramp up sharply because people
*  care about breaking code.
*  Some people do.
*  But in the long run, you know, I don't think that's likely to be the application
*  that's going to be a broad interest and might affect people's everyday lives.
*  Well, it was in the short run.
*  I mean, it's disruptive that quantum computers will be able to break the codes
*  that we use and which we do use in our everyday lives.
*  Whenever you're going to a website that has that little padlock next to the URL,
*  you're using some some public key crypto system and the ones that are most widespread
*  use today, quantum computers will be able to break those crypto systems are based on
*  the presumption that although by doing a hard computation, you can break the codes,
*  that those computations are just too hard.
*  So if you wanted to break RSA, which is one of the most widely used crypto systems now,
*  you'd have to be able to factor numbers that are 2000 bits long.
*  And that's still pretty far out of reach with the most powerful supercomputers we have
*  now. With quantum computers, that won't be a hard problem.
*  And then we'll have to protect our privacy a different way.
*  And what most likely is going to happen is people will switch to new public key crypto
*  systems based on problems, which we don't think quantum computers can solve efficiently.
*  And that will mean we'll all have to change our browser software or something like that.
*  But for most people, maybe it won't have such a big impact on their everyday lives.
*  It's always fun listening to you talk about this stuff because you're clearly super excited
*  about quantum computers, but also just so extremely careful about not overhyping them
*  that I can always see the battle going back and forth between you in your own mind, like
*  saying how interesting it is.
*  But you can see how people who only know a little bit about it could get carried away.
*  And you want to protect against that.
*  Well, there's a lot of the hype.
*  It's an issue.
*  I mean, you know, what's happening in the last few years seems kind of extraordinary
*  to to those of us who've been working in the field for 20 plus years because, you know,
*  it started out well from the start.
*  Well, part of what was exciting about it for me is that, you know, it had an experimental
*  side and it had a theoretical side.
*  And you might say kind of a big gap between the two.
*  But people were really trying to do quantum computing already in the in the 90s.
*  And, you know, it came along at a at an opportune time that when this factoring algorithm
*  was discovered and people started to think seriously about what other applications they
*  would there would be, the experimental physicists had just, you know, in the past decade or
*  so acquired the tools to manipulate single atoms and to, you know, manipulate single
*  electrons and things like that with a motivation which initially didn't have much to do
*  with computing. One motivation was we want we wanted better clocks and the technology
*  for making really good atomic clocks is not that different from the technology we need
*  to operate a quantum computer.
*  So, you know, it was fun that there was interaction between the theory and the experiment.
*  But it wasn't like, you know, we all were going to launch startups.
*  You know, some of you did or 20 years ago.
*  Now everybody's launching startup and, you know, there's a lot of money sloshing around
*  and they're also big companies that are making hefty investments like like Microsoft and,
*  you know, IBM and Google and Intel and actually Amazon, which I have some affiliation with
*  now. And people are excited and the excitement to a certain extent is good.
*  It optimism propels things forward.
*  It creates opportunities for young people.
*  It the investment accelerates progress.
*  But if expectations are unrealistic, you know, we'll get burned eventually.
*  And I think I do expect that quantum computing is going to have a big impact on society.
*  Well, we don't know exactly how far off that is.
*  Right. I not going to happen in five years.
*  I don't think some people think it will happen in five years or 10.
*  I think that's unlikely.
*  But that doesn't mean we shouldn't be pushing ahead and developing the technology.
*  And, you know, there are there are related technologies which might have practical impact
*  on a shorter time scale, like sensing technologies.
*  Quantum sensing has applications that are developing, you know, that better quantum
*  sensors. They have applications to fundamental physics that you and I might be interested
*  in. But also everybody needs to measure things more accurately and with higher resolution
*  and, you know, less invasively.
*  That's important in materials.
*  It's important in medicine.
*  And the technology for quantum sensing has a lot in common with the technology for quantum
*  computing. So I think, you know, the excitement to a certain extent is warranted.
*  But we we shouldn't expect everything to happen at once.
*  It's a sustained investment.
*  It's going to take a lot of effort to make quantum computing a big thing in the sense
*  that it really benefits humankind.
*  Your data is now one of the most valuable commodities in the world and protecting your
*  data has never been so important.
*  That's why I like to recommend NordVPN, a virtual private network that keeps your
*  Wi-Fi safe from intrusion.
*  NordVPN is very easy to use.
*  It's one click and you're using a different server in another country with over 5,000
*  servers that get involved.
*  It has amazing speed confirmed by the speed test.
*  NordVPN is the fastest VPN out there.
*  I like it because when I'm traveling in a cafe in an airport, you can feel secure.
*  NordVPN will protect your data from hackers and block malware sites from attacking your
*  computers. And you can have NordVPN on up to six devices, not only your laptop, but
*  your mobile phone, your smart TV and so on.
*  So go to https.
*  NordVPN.com slash Mindscape.
*  That's NordVPN.com slash Mindscape or use code Mindscape to get a two year plan plus
*  a bonus gift with a huge discount.
*  Well, I mean, I get it because we all know the technology is changing the world and is
*  advancing rapidly and everyone wants to know the next big thing.
*  And when you take computing, which everyone knows is important, and marry it with quantum,
*  which everyone knows is mysterious, it sounds like it could change the world very
*  dramatically. So I'm sure there's sort of a feedback mechanism between people who do
*  and do not understand quantum computing about getting excited about the very near term
*  prospects.
*  Well, here's how it looks to me that right now quantum computers that are at a pretty
*  interesting stage.
*  What's interesting? Well, we can build systems with 50 to 100 qubits.
*  That's interesting because that's already large enough so that it's quite hard just by
*  brute force to simulate with our most powerful classical computers what the quantum
*  computer is doing. So in that sense, it's natural to start thinking seriously about what
*  could the applications be for these near term quantum devices?
*  What kind of problems can they solve?
*  But they're really noisy. In other words, the hardware isn't very reliable.
*  So when you do quantum computation, just like with the classical one, you have to put
*  together a lot of elementary operations, you know, and then in the end you read out a
*  result. But with the best quantum hardware we have now and devices that have lots of
*  qubits, when you do the fundamental two qubit operations, you know, the entangling
*  operations on pairs of qubits, you make an error like once every couple hundred times.
*  So you can put together a circuit with, you know, more than a thousand or so gates and
*  read out a result that's useful.
*  That's a real limitation.
*  Now, we understand that even if the hardware is noisy, as long as it's not really, really
*  noisy, there's an idea called quantum error correction that we can use to control the
*  errors. But that's very, very expensive in terms of overhead, the number of physical
*  qubits that you need, particularly with the kinds of error rates we have now or, you
*  know, with the physical hardware or even if it's a little bit better than what we have
*  now. So I think it's really, really important to make better hardware, to have, you
*  know, operations with error rates which aren't, you know, 1% or half a percent, but 10
*  to the minus 5 or something like that.
*  Now, that's really hard.
*  But that's I'd like to see the focus there because that'll take us more rapidly to the
*  regime where quantum computers can can really solve things that we can't solve classically
*  and including these applications to physics and chemistry that at least, you know, people in
*  the physical sciences are are exciting and something we're impatient to realize.
*  I think if the focus is instead on, you know, well, can we find something interesting to do
*  with these kind of these very limited quantum devices that that we have now?
*  Well, I didn't get that.
*  Could you try again?
*  Siri, you see, even Siri doesn't get it.
*  Then I'm afraid we're, you know, we might wind up with nothing because it's possible.
*  Well, look, it's good to try things.
*  You got to experiment. You got this cool thing and you want to see what it can do.
*  And I think as a physics discovery tool, it's already interesting, you know, because we
*  can study the behavior of a quantum system that's strongly interacting and becomes highly
*  entangled, which we can't simulate and understanding the things they can do just from a
*  point of view of understanding physics better.
*  That I there I do see progress happening in five years.
*  But as far as a practical application that customers will want to pay for, because, you
*  know, they'll be able to improve their financial portfolio or solve some optimization problem.
*  I think we'll have to be pretty lucky to see applications like that that are really impactful
*  in, say, the next five years.
*  But that's where a lot of the focus is.
*  And I will be thinking about the longer term if we're going to make this into a real thing,
*  then we have to focus on the really hard problems of advancing the technology.
*  I've said this before out loud on the podcast, but not to you, which is the confession that
*  one of the many dumb big mistakes I've made in my physics career was I saw a paper by
*  you, I think it was in the 1990s about quantum error correction.
*  And I instantly thought to myself, like, that is the most boring thing anybody could be
*  thinking about. Obviously important if you want to build something.
*  But it doesn't seem like the sort of intellectual fun that we all like to have as theoretical
*  physicists. But I was utterly wrong.
*  Right. I mean, you know, I don't I mean, maybe you can let the audience know a little bit
*  that there is there really is a fascinating set of ideas associated with quantum error
*  correction, not just an engineering project to make the computers better.
*  I'm not an engineer.
*  And I'm a physicist.
*  And even back in the 90s.
*  What I thought was most exciting for me about quantum computing is that it gives us a
*  different way of looking at problems in basic physics, including the condensed matter
*  physics, but also, you know, in quantum field theory and in quantum gravity, the kind of
*  stuff that you and I like.
*  I think quantum error correction is as important as contribution to science as the
*  discovery that, you know, there are fast quantum algorithms, that there are some problems
*  that we can solve, because it's really an amazing thing.
*  We normally, for good reasons, think, well, quantum mechanics, that's about little things,
*  atoms, little single electrons or whatever.
*  And and big things are classical.
*  And we think that for a good reason.
*  Because of the phenomenon we call decoherence.
*  When you scale a system up, it's very hard to isolate it from the outside world.
*  Yeah, it inevitably interacts with its environment and those interactions with the
*  environment sort of cause the quantum information to leak to the outside.
*  And it doesn't behave like a quantum system anymore.
*  It behaves like something we can describe classically, essentially because information
*  about what the system is doing is is redundantly stored and everything all around it.
*  And that's not quantum anymore.
*  That becomes classical.
*  And what quantum error correction is about is that in principle, you know, we can scale
*  the system up, many particles doing very complicated quantum mechanical things and
*  keep it quantum. And we don't do that by perfectly isolating it from the environment,
*  because that's just too hard.
*  But what we do is we take the information that the quantum system is processing and
*  we make that invisible to the environment.
*  And you know how we do it with entanglement?
*  We take the information that we want to protect and we store it in the form of some very
*  highly entangled state shared by many particles.
*  And then the environment comes along and it's kicking the system and, you know, peering
*  into it and and it's looking at the particles a few at a time.
*  But because the system is so entangled, it can't see the protected information when it
*  interacts with just a few particles at a time, just like that 100 page book I was talking
*  about. You know, when you look at one page, you don't see any of the information that's
*  in the book. The information that we've cleverly encoded it in such a way that when you
*  look at just parts of the system one at a time, you don't see the encoded information at
*  all. And therefore it can be robust.
*  And we've also figured out how you can process it, even when it's encoded in that in that
*  very highly entangled form.
*  And I mean, that's a tremendous insight that we can make really complex, large quantum
*  things behave quantumly despite the effects of decoherence, which we have correctly
*  believed explains why big things are classical and little things are quantum.
*  We can outsmart decoherence.
*  That's the lesson. And this was controversial for a while, you know, back in the mid 90s, not
*  surprisingly. You know, people started talking about quantum computing and you could break
*  codes and all that. And good physicists said that'll never happen because they physicists
*  who were very experienced with decoherence, including in the lab like Serge Arosh, who
*  won a Nobel Prize for figuring out how decoherence works.
*  And, you know, he said it was the theorists dream, but the experimentalist nightmare,
*  because you can never really control the quantum system.
*  It's really hard. And, you know, we're not all the way there yet, but we're making progress and we
*  understand conceptually how to scale things up and still make a complex quantum system work.
*  And I think that's just an amazing scientific breakthrough.
*  Let me see if I can rephrase it just so I know that I understand what's going on here.
*  As you said, there's a lot of richness and complexity in the quantum system itself.
*  But when we look at it, when we measure it, in some sense, we only extract a classical result
*  with some probability, right?
*  We the qubit can be up or down, but we see only one or the other.
*  And likewise for many qubits.
*  And decoherence, in a sense, is is making a measurement of the system, right?
*  It's the environment, the outside world becoming entangled and then sort of ruining the
*  quantumness, like you said.
*  And so the quantum error correction game is putting the information into the quantum system
*  in such a way that it is not being measured away by the environment.
*  Is that is that fair?
*  Well, you said it much better than I did.
*  You should be a podcaster.
*  I should write books about this.
*  Yeah, that's exactly what I meant.
*  Good.
*  Very, very good.
*  And so then then let's make it real.
*  I know that neither one of us is an engineer, but what are your favorite ways to make qubits
*  and entangle them?
*  What are your favorite physical manifestations here that we could build into a computer?
*  Well, so you mean what what kind of hardware do I like for quantum qubits?
*  What's your favorite qubit?
*  Well, first of all, you know, I think it's important and great that there are a lot of
*  different hardware approaches that people are pursuing and trying to develop because
*  we don't have a clear understanding of what type of quantum hardware is going to have
*  the best long term prospects for scaling up to large systems.
*  Right now, the two leading technologies are superconducting circuits and atomic qubits,
*  usually ions, you know, electrically charged qubits, which can trap with electromagnetic
*  fields.
*  So what do you need if you're going to have quantum hardware?
*  What do you need?
*  Well, you need qubits.
*  You would like to have a system where you can scale it up to many qubits.
*  You want them to have long coherence times, as we say, in other words, for it to take
*  a long time for the environment to measure the qubit.
*  And then you want to be able to manipulate them quickly compared to that time scale.
*  You want to be able to get them to do something before the environment spoils it all.
*  And of course, you want to be able to read them out in the end.
*  You want to be able to measure them accurately.
*  So it's tricky to come up with a system that meets all of those desiderata.
*  But atoms are pretty good qubits.
*  You can take an atom and you can control it with lasers, for example.
*  And it could be in either its ground state, its lowest energy state, or some excited state.
*  You'd like that to be an excited state that doesn't decay back to the ground state very
*  quickly.
*  That's how you get the long coherence time.
*  So you can actually create with a laser a state which is a superposition of the ground
*  state and the excited state.
*  You can manipulate that.
*  That's good.
*  You can read it out pretty easily.
*  I mean, you do it with lasers again.
*  You can shine a laser with the right frequency on an atom.
*  And if it's in one state, like the ground state, it will absorb the light and readmit
*  it very rapidly.
*  So it glows.
*  But if it's in another state, then the light doesn't see it.
*  So it stays dark.
*  So you shine a laser and some of them shine.
*  Some of them don't.
*  Those are the zeros and ones.
*  So that all works great.
*  As with other quantum computing technologies, the hardest part is you got to get qubits
*  to interact.
*  You have to be able to perform entangling operations on pairs of qubits.
*  And that's why it's useful for them to be electrically charged.
*  Then they have Coulomb interactions.
*  You know, the repulsive interactions.
*  And you can leverage that to kind of couple together the internal states of the qubits
*  and their emotional states as they're vibrating in a trap.
*  And that's how you can get them to interact in a pretty well controlled way and do pretty
*  good entangling to qubit gates.
*  So that's a good technology.
*  Now, superconducting circuits is something really completely different.
*  But it has it satisfies all the desiderata.
*  And now what's being manipulated is the collective motion of billions of pairs of electrons.
*  OK, it's a circuit.
*  For a single qubit.
*  But it's very, very cold.
*  You know, it's at 10 or 20 millikelvin or something like that.
*  So it's a material that conducts electricity without resistance.
*  That's what we mean by a superconductor.
*  But you make it much colder than it needs to be to be a superconductor because you don't
*  want to have a lot of stray, well, essentially light, except it's microwave light at those
*  low temperatures, which could be, you know, interacting with the electron motion.
*  And now you can have this isn't this isn't the way you really do it in practice for practical
*  reasons.
*  But you can imagine you've got a loop of wire.
*  It's conducting electricity without resistance, but it could be going around either clockwise
*  or counterclockwise.
*  And those are like the two states of a qubit.
*  And you can those can also be in superposition.
*  You know, it can be a little bit of going clockwise, a little bit of going counterclockwise.
*  And you can read out these circuits.
*  I mean, the key thing is, well, actually, the way you do it is you couple it to another
*  thing, like a microwave resonator, just like a thing that a waveguide, just a photon waveguide.
*  And the frequency of that waveguide depends on whether the qubits in one state or another.
*  So you can read it out.
*  So that's all great, too.
*  Now, these are about the best technologies we have.
*  And in both cases, you can build devices with tens of qubits.
*  But again, those entangling two qubit gates have pretty high error rates, you know, like
*  at the one percent level.
*  We got to do much better than that.
*  Now, I looking forward, I do have a preference for the superconducting qubits because there
*  are there's a lot of opportunity to sort of fool around with the electrical engineering
*  of the superconducting devices.
*  Well, I wouldn't even put it that way because it's more fundamental than that.
*  You have a lot of there are a lot of tricks you can play.
*  And there are a few ideas we're pursuing that might result in having much, much better
*  performance for the gates.
*  And that will make a huge difference because it means in the in the near term, we can conduct,
*  you know, we can execute larger circuits and still get reasonable signal to noise when
*  we read up.
*  And in the longer term, it means we'll be able to do error correction with a lower cost.
*  And that'll make it less expensive to scale things up further.
*  But, you know, there are there could be big surprises and coming from from other technologies.
*  A few years ago, I wouldn't have mentioned what is now one of the most promising approaches.
*  What we call Rydberg Adams.
*  It just means an atom now is either in its ground state or it's really, really highly
*  excited with some electron in a very large orbit.
*  And those guys have a big dive dipole moment so they can interact strongly with one another.
*  That, you know, makes it well, that way they have interesting interactions and they can interact quickly.
*  You can read them out.
*  It's got a lot of great features.
*  And that's really come along rapidly in just the last couple of years.
*  And there could be other things like that, which sort of take a leap forward.
*  We're really in early days, I think, as far as the technology goes.
*  It's interesting that your favorite is the superconducting circuits, because when you
*  mention the atoms, there seems to be an obvious advantage of atoms, namely they are small.
*  So we could pack a lot of them close together.
*  But I mean, maybe our ambitions are not to have 10 to the 10 qubits, but only, you know, thousands of qubits.
*  And so we don't need to make them that small.
*  But what is the do you need space for the atoms?
*  I probably want to have millions, millions of qubits.
*  Yeah.
*  And that might be a big thing, but, you know, it's not so easy with the atoms either.
*  So if you use this trapped ion technology, remember the way you get the atoms to interact with one another is through their Coulomb interactions, the way they're vibrating in the trap.
*  And if you put in more and more ions, you get more and more normal modes of vibration.
*  And then you're going to try to drive, though.
*  They correspond to different microwave frequencies and you're driving it with lasers, which are optical.
*  But you can have differences between frequencies of different lasers, you know, which can excite different modes.
*  But it gets it gets to be a pretty thick forest of, you know, normal modes if you put in too many ions.
*  So it gets very difficult, you know, once you have more than, I don't know, 32, 64 ions, something like that.
*  OK.
*  And so then you got to it'll have to be some kind of modular design.
*  So you'll have a lot of processors.
*  Maybe each one has tens of ions and you got to get them to talk to one another.
*  So, you know, so they can share entanglement.
*  And so you need some way of designing an interconnect between traps.
*  People have ideas about how to do that, but it's hard.
*  Or otherwise, you can have a trap with with lots of zones where you have a few ions in one zone and a few ions in another.
*  But then you have to be able to move the ions between zones so you can transfer entanglement from one zone to another.
*  If you're going to get a highly entangled state with many ions and, you know, people are working on that, too.
*  But it's hard. Everything's hard. Yeah, everything's hard.
*  Nobody said it would be easy. Phonal computing is hard.
*  That's why we haven't made more progress.
*  Well, we made a lot of progress, but it's only, you know, it's been decades of improvement in the design of the qubits and the control and the fabrication and all that.
*  But we still have a long way to go.
*  And how do you get the superconducting loops to entangle with each other and interact?
*  Oh, well, the superconducting circuits, you know, they have magnetic fields and electric fields, so they can interact either capacitively.
*  That means the electric field or inductively.
*  That means the magnetic field.
*  And, you know, of course, the art is to control those things well.
*  Yeah. Yeah.
*  What should I be visualizing in terms of the geometry?
*  Are these arranged in a line or a plane or a 3D grid?
*  Well, 3D is hard, but there are two dimensional layouts.
*  Pretty much the state of the art still in superconducting quantum computers is this device that Google built a couple of years ago now, which they call Sycamore.
*  It has 53 working qubits.
*  They're in a two dimensional array.
*  You can execute entangling operations on pairs of qubits in that array, which are neighbors to one another.
*  And they are able to do a sequence of, you know, layers of such entangling gates in an experiment they did in 2019.
*  They did up to 20 layers and something like, you know, a thousand operations altogether.
*  And because of the noise that I keep talking about, then when they measured all 53 qubits at the end, you know, they get the right answer about one time out of 500.
*  So not such good signal to noise, but then they can run it millions of times in just a few minutes.
*  And the same circuit over and over again.
*  And then they get, you know, a good enough sample of the output to have something that's statistically useful.
*  And already that quantum computation is something that's really hard to simulate.
*  53 qubits is a lot.
*  And, you know, with the best classical methods that we have to simulate what Sycamore is doing in just a few minutes on a classical supercomputer takes at least days.
*  So in that sense, you know, I sometimes I say it's quantum David Verklu's classical Goliath because the classical computer is this huge system.
*  It covers to the equivalent of two tennis courts and it's burning megawatts of power.
*  Sycamore, it's just a little chip, you know, just doing its thing inside inside a dilution refrigerator.
*  And yet, in a sense, it's doing something that Goliath has a very hard time keeping up with.
*  Now, it's not doing anything useful.
*  As yet, the computation that it's doing is useful for only one purpose, to demonstrate that the quantum device can do something that's really hard for a classical device to do.
*  You mentioned that it's in a dilution refrigerator, even though it's tiny.
*  I mean, do we imagine that there will ever be a day when we will have iPhones with quantum computers inside?
*  Well, if we if we're carrying them in our pockets, they probably won't be a 20 milliket, you know, but it could be a different technology.
*  There are there are quantum technologies that work at room temperature.
*  OK. And, you know, why would you want to have it in your iPhone?
*  That's another question. It you know, you might want to have it as sort of a smart card.
*  You know, we haven't talked about quantum cryptography, but which is another intellectually interesting idea where exactly what the best use case is still a little bit murky.
*  But the great thing about quantum information from the point of view of security is that you can't eavesdrop on quantum systems without disturbing them in some detectable way.
*  You know, this is what's really different or one of the things that's really different.
*  I don't know if you've talked about entanglement, but one thing that's really different about quantum information from classical information is you can look at classical information or you can copy it and you don't have to change it.
*  But if it's quantum information and you observe it, you disturb it.
*  It's gone. Yeah.
*  And that's actually can be the basis of a kind of cryptographic scheme where you're sending quantum states.
*  And if somebody tries to eavesdrop, you can do a test to see that the state has been disturbed.
*  And you can base security then not on some assumption about the computation you would need to break the protocols too hard to do in any reasonable amount of time.
*  It's really based on the laws of physics that you can collect information without creating a disturbance.
*  So maybe you'll want to have a little quantum, I don't know, smart card that you can carry around.
*  So when you go to the ATM, I don't know if people will be going to the ATM by then, but wherever you go, you can have someone verify your card, but nobody would be able to copy it.
*  You know, I have no idea what good a quantum iPhone would be, a quantum computer inside the iPhone or smartphone would be.
*  But I am 99.99% sure that it would be incredibly useful just because even I'm old enough that I remember a day when people said, why would you ever need more than 64K of RAM in your personal computer?
*  I don't see what the usefulness of that would be.
*  And then I remember when people said, why do we need web browsers?
*  You know, we have the phone book and we have other ways to do things.
*  And so even if I can't foresee what the applications are going to be, there are different kinds of things, as you've been saying, that you can do with quantum algorithms and computers.
*  And so someone will come up with ways to put them to use, is my conviction.
*  Well, you remember when nobody could imagine why anyone would want a computer at home.
*  Yeah.
*  Usually the explanation was you can organize your recipes.
*  Yeah, my explanation why you need a web browser at the time was, well, I can order a pizza on a web page.
*  And people said, well, we have ways.
*  We have ways of doing that other ways.
*  But OK, let's get more into what exactly we can do with the quantum computers.
*  I mean, one thing that slipped by there, which because I know some people are not completely convinced of or haven't heard of yet.
*  We have quantum computers.
*  They are working, right?
*  I mean, there's the IBM quantum experience where you can go onto a web page and run a little quantum algorithm yourself.
*  So it's not like the existence of the computers is the issue.
*  It's all these scalings and error correction and decoherence is the issue.
*  Yeah.
*  There are quantum computers.
*  You can you can use them.
*  And there are several different hardware providers, you know, where you can have cloud access.
*  Actually, AWS has the system they call Bracket, where you can access an ion trap quantum computer and a superconducting quantum computer.
*  And but they're not useful yet.
*  Sure.
*  They're not able to solve problems we can't solve other ways.
*  Now, that doesn't mean people it doesn't make sense for people to be playing around with them.
*  It probably does make sense because they are going to be useful.
*  And if you're you know, if you have a company that for which solving hard computational problems is of value, then you know, you might want to have some quantum expertise on board, have some people who are familiar with what quantum computers can potentially do and can explore the potential applications, you know, to the problems they're interested in.
*  But how long it will be before quantum computers can solve problems that people really care about, say, for business reasons and solve them with a speed up relative to what the best classical computers running the best algorithms for solving the same problems.
*  How long is that? That's going to be I don't think anybody really knows that.
*  That sounds like there's a lot of interest in optimization, just because everybody wants to optimize things.
*  And there are heuristic ideas about how you can use a quantum computer to skip up.
*  Sorry to speed up optimization.
*  But we don't really have very convincing theoretical arguments that quantum computers will get big speed ups for optimization.
*  They might.
*  We know we know there is that we know they can speed up exhaustive search.
*  But that's not a spectacular speed up.
*  You know, if you're looking for the solution to the traveling salesman problem or something like that, you know, you want to find a route that visits a whole bunch of cities, which is as short as possible.
*  You can always solve that problem by trying all the routes and finding one that's shortest.
*  But, you know, that's completely inefficient.
*  Nobody can solve the problem that way for more than, you know, a few cities.
*  And.
*  Exhaustive search isn't a good way to solve it, but quantum computing can speed up exhaustive search, but it doesn't speed it up by a spectacular amount the way it speeds up factoring the time as that's assuming you had quantum hardware with the same clock speed, the same number of operations per second as your classical computer.
*  Yeah, I can solve the problem in the square root of the time it would take to solve it classically.
*  That's something, but it's probably going to be a long time before quantum computers are of high enough quality for us to be able to take advantage of that speed up.
*  So I think the the speed ups that are going to have an impact first will be the ones where we think it really is a exponential speed up a spectacular speed up solving those problems in material science and chemistry is an example.
*  But those require lots of qubits and, you know, that's probably going to be a while.
*  Now.
*  Just because we theorists can't guarantee that quantum computers are going to speed up certain problems doesn't mean, you know, that it's not going to happen.
*  It's important to experiment classically.
*  We have lots of examples where there are heuristic algorithms, which turn out to have a lot of practical value, even though the theorists can't very well explain why they're so valuable.
*  Machine learning is the most obvious example now.
*  You know, AI is having a big impact.
*  You can drive autonomous vehicles.
*  You can win it go.
*  You can recognize spaces using deep learning networks.
*  And we have very limited theoretical understanding of why for those applications, we can we can train those networks efficiently.
*  People just tried it and found out that it worked.
*  Right. So if you're an optimist, you can say, well, let's, you know, try a lot of things on these near term quantum devices and see if something works.
*  And that's a worthwhile thing to do.
*  And that's one way in which these devices that are now available on the cloud will be used and are being used.
*  But, you know, in the near term, you could say maybe the most important application for these quantum computers we have now is they can help us learn to make bigger quantum computers.
*  And, you know, this quantum error correction idea I keep harping on, we can we've gotten to the point now where we can start to try out quantum error correction on the devices we have now and try to improve it.
*  And get it to run more efficiently and lower overhead costs, come up with new ideas.
*  We have to see whether the noise in the devices we can really build has the right properties for quantum error correction to work effectively.
*  And that's I mean, that's interesting scientifically.
*  And I think also interesting from the point of view of moving the technology to the next level.
*  So that's another thing we should be doing with these computers that we have now.
*  I mean, maybe we can be a little bit more specific about what our theoretical knowledge is about the amount of quantum speed up we can either expect or hope for.
*  So my understanding is there definitely is speed up in certain well understood cases.
*  This exponential speed up, the speed up that we would really like to see.
*  What's the status there?
*  Is it that we it's possible that every problem can be exponentially sped up or do we know that there are any problems that could be exponentially sped up?
*  What do we think about that?
*  Well, I guess it depends partly on what your your standard for rigor is.
*  I would say we have we have pretty convincing arguments that quantum error correction is a very good way to do it.
*  Pretty convincing arguments that quantum computers will not be able to efficiently solve exactly the NP hard problems.
*  You know, the hard instances of the so-called NP hard problems.
*  NP means the problems where when we find a solution, we can efficiently verify that the solution is correct.
*  The traveling salesman problem that I mentioned is an example of a so-called NP hard problem.
*  That means it's in NP.
*  Once you find the route, you can check that the route has a total mileage less than some specified number.
*  It's hard to find the route.
*  And that problem has the property that if you can solve that efficiently, then you can solve a ton of other optimization problems efficiently.
*  And that would be of great interest for many applications.
*  We don't think quantum computers can find exact solutions to those problems efficiently.
*  Now, they may be able to find approximate solutions with some advantage over classical computers.
*  We don't know that for sure. That's really more of a speculation.
*  But that's, you know, something we should continue to strive for and try to clarify.
*  And that's part of what is motivating the effort to use these near-term quantum devices to see if we can speed up optimization.
*  But I mentioned factoring a couple of times.
*  So what's the deal with factoring?
*  The truth is we can't prove that factoring is hard classically.
*  It's not one of these NP-hard problems.
*  It's pretty hard, but not that hard.
*  No. Why do we think it's hard?
*  Because really, really smart people have tried very, very hard to come up with a better factoring algorithm.
*  And they've been doing it for decades and they haven't succeeded.
*  But some brilliant student may come along tomorrow and come up with a factoring algorithm.
*  That's possible.
*  But we do know, theoretically, if we have a quantum computer that operates reliably, it will be able to solve factoring efficiently.
*  So it's not exactly exponential. It's super polynomial. It's almost exponential, the speedup.
*  It's a very spectacular speedup.
*  You can solve factoring problems if you have a quantum computer with a clock speed that seems physically reasonable.
*  You can solve it in hours, even if it would take the age of the universe to solve it with the best classical computer.
*  So that's a real speedup.
*  And that's the kind of thing that gets our pulses quickening.
*  Now, as far as these applications to material science and chemistry and so on, again, I would say the best argument we have that those problems are really hard classically,
*  is nobody can figure out how to solve them.
*  Again, it's not for lack of trying.
*  Physicists and chemists have been trying for decades to come up with better algorithms.
*  They can run on classical computers for simulating the behavior of quantum systems with many particles, but still the best algorithms that we have have a runtime which rises exponentially with the number of qubits.
*  Quantum computers will be able to solve those problems efficiently.
*  Problems like simulating the dynamics of a quantum system that's evolving with time.
*  Well, with some caveats, they'd be able to solve problems like finding the low energy states, finding the ground state of a molecule, and things like that.
*  So we're thinking of things like chemistry, materials, superconductivity, stuff like that?
*  Yeah, so those are the applications where I feel pretty confident the problems really are classically hard and quantum computers will be able to solve them efficiently.
*  But, you know, efficiently is computer scientists mean something technical by those words.
*  They mean that the time it takes to solve the problem scales in a reasonable way with the size of the problem, like the number of particles in the material or the number of electrons in the molecule or something like that.
*  That doesn't necessarily mean it's really practical.
*  So we're going to have to scale up quantum computers quite a bit from where they are now before we can do simulations of materials that are too hard to do with our classical computers that might teach us something interesting.
*  One of the holy grails in computational quantum materials for decades has been trying to understand high temperature superconductors better and, you know, try to point us in the direction of discovering new high temperature superconductors, potentially of great practical interest, if we can get them to room temperature in particular.
*  And that's a really hard computational problem.
*  And already, you know, you can consider model systems with the number of particles, you know, which is of order 100 or so, where that's too hard to solve with a classical computer.
*  You should be able to solve with the quantum computer.
*  But then the real cost of running that quantum computation comes back to this issue that the quantum computers aren't perfect.
*  And we'll probably have to use quantum error correction to run those algorithms.
*  And how many physical qubits we need then is going to depend on how reliable the hardware is, you know, what the error rates are.
*  And right now, the error rates are pretty bad. So it would probably mean millions of physical qubits.
*  And what do we have now? Maybe 100 physical qubits, not quite that.
*  So it's a big, big gap to cross from where we are now to where we'll be confident quantum computers can solve problems that material scientists are interested in, which seem to be too hard to solve classically.
*  I hope it'll happen soon.
*  And these problems you mentioned, I mean, these kinds of problems are, it's easy to see why they're a natural fit for quantum computers because you're using entangled qubits to simulate literally entangled materials.
*  Does that mean that we shouldn't necessarily hold out any hope for quantum computers being especially good for simulating other complex but classical systems like economies or societies or technologies or anything like that?
*  Well, I wouldn't put it as strongly as we shouldn't hold out hope. But I would say I don't see any very persuasive argument that quantum computers will be good at problems like that.
*  Good.
*  Yeah, I think as best we currently understand, like I said, we don't expect quantum computers to dramatically speed up everything.
*  And so the class of problems for which, you know, very substantial speed ups are possible is something that's probably limited.
*  And exactly what are those problems? What are the things that are too hard to solve classically that we can solve quantumly?
*  I don't think we really know so much about that yet. You know, our understanding of it has advanced some over the last 25 years or so.
*  But still, like I said, the best idea we have, I keep coming back to it, is simulating quantum systems with quantum computers.
*  That they have these applications to cryptology came as kind of a surprise.
*  And there could well be other surprises.
*  There probably will be.
*  And for the young people in the audience, just so they know, I mean, there's no proof that there isn't a genius algorithm that uses quantum entanglement to help us solve these big simulation problems, right?
*  Well, it's really, really hard to show from first principles that a problem is hard. In fact, we're very bad at that.
*  So much, I mean, there's a whole field of complexity theory, the study of hardness of problems, which has many beautiful results.
*  But it's largely founded on unproven conjectures, the most fundamental and famous of which is the P not equals NP conjecture, you know, that they're,
*  I alluded to it in passing before that there are problems for which we can verify the solution easily once we find the solution.
*  But it's really hard to find the solution.
*  You know, we don't know for sure that you can't solve the traveling salesman problem lickety split if you find the right algorithm.
*  But most people have thought seriously about it think that's really a hard problem.
*  Now, on the other end, quantum computers can't solve that efficiently either.
*  So we really have to, you know, it's quite subtle to find this sweet spot where an important part of the topic is understanding what's hard classically.
*  To find these problems that, you know, we can solve efficiently quantumly and we can't solve efficiently classically.
*  Theorists have made only limited progress on that.
*  And, you know, once we have the quantum computers, I'm sure we'll learn a lot more just by experimenting with.
*  Let's bring it home maybe by going back to field theory and quantum gravity and black holes that you were thinking about before you made this phase transition.
*  And it turns out that you're still there like you have not completely abandoned this right.
*  These ideas from quantum information theory and quantum computing turn out to be relevant for things like the black hole information problem.
*  Is that right? Yeah.
*  And in a way, I sort of came back to it.
*  That's I would say they're two big surprises for me.
*  You know, from the perspective of the way I thought about the field when I got started, like 25 years ago, I actually believed early on that quantum information was going to be important for fundamental questions in physics.
*  And it has had an impact on, you know, understanding phase transitions and quantum matter.
*  And I thought it would be helpful for understanding black holes and quantum gravity as well, which, like I said earlier, is kind of how I got into it.
*  I thought I should study quantum information because that'll help me to understand how black holes behave.
*  But I there was kind of a transition that I didn't expect from the people who do quantum gravity for a living.
*  You know, many brilliant people who are friends of both of us were not too interested in quantum information.
*  And then suddenly they were. Yeah.
*  You know, and suddenly you could go to a quantum gravity meeting and the talks would be about quantum error correction and computational complexity and entanglement.
*  And and that I found that quite exciting.
*  And, you know, our current perspective is that space itself or space time is not truly fundamental.
*  It's sort of an emergent property from something deeper.
*  And what is the deeper thing? Well, when I talk about space, I mean, geometry, you know,
*  when one thing is close to another thing, that's a property of geometry.
*  Where things are relative to one another, that's geometry.
*  And the underlying explanation for geometry, we increasingly believe, is quantum entanglement.
*  You know, so you and I, as it happens, we're on Zoom, so we're not in the same room.
*  But, you know, if we were, we could imagine trying to break the entanglement.
*  We don't have to be in the same room to imagine this.
*  Try to break the entanglement between, you know, where I am in space and where you are in space.
*  And we think that if you did that, you would actually break space, that we would be disconnected from one another.
*  And there wouldn't be any way to travel from where you are to where I am if there weren't for that entanglement.
*  So in that sense, quantum entanglement seems to be what's gluing space together.
*  And just to be super clear, because I always get people confused by this,
*  it's not the entanglement between you and me that gives us the distance.
*  It's the entanglement between invisible degrees of freedom in the space between us, which is a little bit hard to visualize.
*  Well, part of the problem is we don't understand it as deeply as we would like to.
*  But we have lots of hints that that's what's going on.
*  And these ideas, which emerge largely through the study of quantum computing,
*  like quantum error correction, turn out to be just what we need to understand this at a deeper level.
*  It kind of makes sense that if space is going to be an emergent property, it better be pretty robust.
*  So you shouldn't be able to tickle it and make it fall apart.
*  And it's kind of a quantum error correction code that has this property that, you know, it's not so easy to, you know, break space up.
*  Just like once you have quantum error correction, it becomes harder for the environment to, you know, attack a quantum computer and make it fail.
*  I'm literally trying to understand this exact feature of immersion space time better myself right now for research, writing papers purposes.
*  So we're at the end of the podcast.
*  While I have you here, I mean, can we be a little bit more specific?
*  Can you be about, I mean, you say robustness of space that makes perfect sense.
*  But what is the relationship in an explicitly as we can be between a quantum error correcting code,
*  which seems like something you build into a computer and the nature of space itself?
*  Well, here's something that's fairly concrete, but it requires a bit of a detour.
*  If you're up for it, I am.
*  Holographic duality.
*  And so there's a particular setting in which we understand quantum gravity best at present.
*  And it gives us a handle, a tool for understanding properties of black holes that form and evaporate and so on.
*  And it is a duality between a ordinary quantum theory that doesn't involve gravity at all,
*  but which actually is an alternative way of describing gravity in which black holes form and things fall and so on.
*  There's a complicated dictionary that relates those two descriptions, one which is just ordinary quantum mechanics and the other one that involves gravity.
*  And that dictionary is actually the encoding map of a quantum error correcting code.
*  So what does that mean, for example?
*  And we can think of the dictionary in the following way that there's some geometry, you know, it's dynamical black holes are forming and they're moving around and gravitationally attracting one another and so on.
*  But this alternative description that doesn't involve gravity lives at the boundary of this space time.
*  And now you could there's all this wonderful stuff happening inside.
*  And now you can start messing around with the boundary.
*  There's some map that takes the physics on the boundary and maps it to the the physics deep inside the space time.
*  And now you state like you start removing little pieces of the geometry or hitting them with a hammer or sorry, removing little pieces of the boundary, the boundary,
*  like take away some of the qubits from the boundary or flip them or do something awful to them, but not too many of them.
*  And what's happening deep in the space time is still OK.
*  And that's because this map from the boundary to what we call the bulk, you know, where the interesting gravity is, it's very non-local.
*  So things that look local in the bulk, like a black hole, you know, right here in my room on the boundary, that actually involves lots of degrees of freedom, you know, which are entangled with one another.
*  And you can take away some of those degrees of freedom, but you don't spoil that entanglement for the most part.
*  And the what's going on with the black hole doesn't doesn't get altered.
*  So that's an example of what I mean by quantum error correction.
*  It's a great example. And I think that I'm tempted to ask.
*  So I'll just ask it. Why not?
*  In that explanation you just gave, which is beautifully clear, the role of holography is absolutely central.
*  And, you know, in this sense, we did, by the way, have Neda Engelhardt on the podcast for those who want a longer disquisition about that and Lenny's Huskin before her.
*  That does live in this context of what we call the ADS-CFT correspondence, right, where we have a space time where there is a boundary that we can identify and it's a space time itself, etc, etc.
*  And as you know, as well as I do, our world does not appear to be anti-de Sitter space.
*  Does that mean that is the holography sort of a way to answer the questions in a very simple context, but we're going to have to do more work to apply it to the real world?
*  Or is there a more direct connection there?
*  It's a toy model. It's not the real thing. Just as you said, it's not our universe.
*  It's something that's easier to understand than our than our universe.
*  So we understand it better. Yeah.
*  And eventually we need to throw away that crutch.
*  And well, I don't know if you said these words, but what I was describing applies in what we call anti-de Sitter space.
*  It's negatively curved space, and that doesn't seem to be the one we're living in.
*  It turns out that it's easier to understand because of this nice relationship between the quantum system,
*  living on the boundary and the physics going on in the bulk and I just hit her space.
*  I think the lessons are broader that the connection between entanglements and quantum error correction and geometry will extend beyond that toy example.
*  But we got a lot of work to do to elucidate that.
*  Now, you had Netta on your podcast and she told you about some of these spectacular recent developments that she's been involved in,
*  which actually teaches things about the case that's more like the real world,
*  understanding how black holes evaporate and what happens to the information in them.
*  And what she and her collaborators found, I think also has a width of quantum error correction because they said things like
*  what's going on outside the black hole is related to what's going on inside the black hole.
*  And I think that actually involves one of these kind of quantum error correcting maps as well.
*  But we need to flesh that out.
*  Sounds like it's a pretty exciting time when we can bounce back and forth between black holes evaporating and the nature of space time
*  and little circuits superconducting that will help us solve the traveling salesman problem.
*  I'm having a blast. Yeah, and so are you.
*  I am. And I hope that everyone listening is also and they catch some of the spirit that is very much alive here.
*  So, John Preskill, thanks so much for being on the Mindscape Podcast.
*  It was a pleasure, Sean.
*  Thank you.

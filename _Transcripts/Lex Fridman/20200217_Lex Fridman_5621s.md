---
Date Generated: October 31, 2024
Transcription Model: whisper medium 20231117
Length: 5621s
Video Keywords: ['scott aaronson', 'quantum computing', 'quantum mechanics', 'artificial intelligence', 'agi', 'ai', 'ai podcast', 'artificial intelligence podcast', 'lex fridman', 'lex podcast', 'lex mit', 'lex ai', 'lex jre', 'mit ai']
Video Views: 239611
Video Rating: None
Video Description: Scott Aaronson is a professor at UT Austin, director of its Quantum Information Center, and previously a professor at MIT. His research interests center around the capabilities and limits of quantum computers and computational complexity theory more generally.

This episode is presented by Cash App. Download it & use code "LexPodcast":
Cash App (App Store): https://apple.co/2sPrUHe
Cash App (Google Play): https://bit.ly/2MlvP5w

This episode is also supported by the Techmeme Ride Home podcast. 
Get it on Apple Podcasts: https://apple.co/2vIbh1k
or find it by searching "Ride Home" in your podcast app.

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
5:07 - Role of philosophy in science
29:27 - What is a quantum computer?
41:12 - Quantum decoherence (noise in quantum information)
49:22 - Quantum computer engineering challenges
51:00 - Moore's Law
56:33 - Quantum supremacy
1:12:18 - Using quantum computers to break cryptography
1:17:11 - Practical application of quantum computers
1:22:18 - Quantum machine learning, questinable claims, and cautious optimism
1:30:53 - Meaning of life

CONNECT:
- Subscribe to this YouTube channel
- Twitter: https://twitter.com/lexfridman
- LinkedIn: https://www.linkedin.com/in/lexfridman
- Facebook: https://www.facebook.com/LexFridmanPage
- Instagram: https://www.instagram.com/lexfridman
- Medium: https://medium.com/@lexfridman
- Support on Patreon: https://www.patreon.com/lexfridman
---

# Scott Aaronson Quantum Computing  Lex Fridman Podcast #72
**Lex Fridman:** [February 17, 2020](https://www.youtube.com/watch?v=uX5t8EivCaM)
*  The following is a conversation with Scott Aronson, a professor at UT Austin,
*  director of its Quantum Information Center and previously a professor at MIT.
*  His research interests center around the capabilities and limits of quantum computers
*  and computational complexity theory more generally. He is an excellent writer and one
*  of my favorite communicators of computer science in the world. We only had about an hour and a half
*  of this conversation so I decided to focus on quantum computing but I can see us talking
*  again in the future on this podcast at some point about computational complexity theory
*  and all the complexity classes that Scott catalogs in his amazing Complexity Zoo Wiki.
*  As a quick aside, based on questions and comments I've received, my goal with these conversations
*  is to try to be in the background without ego and do three things. One, let the guests shine
*  and try to discover together the most beautiful insights in their work and in their mind. Two,
*  try to play devil's advocate just enough to provide a creative tension in exploring ideas
*  through conversation. And three, to ask very basic questions about terminology, about concepts,
*  about ideas. Many of the topics we talk about in the podcast I've been studying for years
*  as a grad student, as a researcher, and generally as a curious human who loves to read.
*  But frankly, I see myself in these conversations as the main character for one of my favorite
*  novels by Dostoevsky called The Idiot. I enjoy playing dumb. Clearly, it comes naturally. But
*  the basic questions don't come from my ignorance of the subject but from an instinct that the
*  fundamentals are simple. And if we linger on them from almost a naive perspective, we can draw an
*  insightful thread from computer science to neuroscience to physics to philosophy and to
*  artificial intelligence. This is the Artificial Intelligence Podcast. If you enjoy it, subscribe
*  on YouTube, give it five stars on Apple Podcasts, support it on Patreon, or simply connect with me
*  on Twitter at Lex Friedman, spelled F-R-I-D-M-A-N. As usual, I'll do one or two minutes of ads now,
*  and never any ads in the middle that can break the flow of the conversation.
*  I hope that works for you and doesn't hurt the listening experience.
*  Quick summary of the ads. Two supporters today. First, get Cash App and use the code LexPodcast.
*  Second, listen to the Tech Meme Ride Home Podcast for tech news. Search Ride Home,
*  two words, in your podcast app. This show is presented by Cash App,
*  the number one finance app in the App Store. When you get it, use code LexPodcast. Cash App lets
*  you send money to friends, buy bitcoin, and invest in the stock market with as little as $1. Broker
*  services are provided by Cash App Investing, a subsidiary of Square, and member SIPC. Since
*  Cash App does fractional share trading, let me mention that the order execution algorithm that
*  works behind the scenes to create the abstraction of fractional orders is an algorithmic marvel.
*  Big props to the Cash App engineers for solving a hard problem that in the end provides an easy
*  interface that takes a step up to the next layer of abstraction over the stock market,
*  making trading more accessible for new investors and diversification much easier.
*  Again, if you get Cash App from the App Store or Google Play and use the code LexPodcast,
*  you'll get $10, and Cash App will also donate $10 to FIRST, one of my favorite organizations
*  that is helping to advance robotics and STEM education for young people around the world.
*  This episode is also supported by the Tech Meme Ride Home Podcast. It's a technology podcast I've
*  been listening to for a while and really enjoying. It goes straight to the point, gives you the tech
*  news you need to know, and provides minimal but essential context. It's released every day by 5
*  pm Eastern and is only about 15 to 20 minutes long. For fun, I like building apps on smartphones,
*  most on Android, so I'm always a little curious about new flagship phones that come out.
*  I saw that Samsung announced the new Galaxy S20, and of course, right away, Tech Meme Ride Home
*  has a new episode that summarizes all that I needed to know about this new device.
*  They've also started to do weekend bonus episodes with interviews of people like AWELL founder Steve
*  Case on investing and Gary Marcus on AI, who I've also interviewed on this podcast. You can find the
*  Tech Meme Ride Home Podcast if you search your podcast app for Ride Home. Two words. Then
*  subscribe, enjoy, and keep up to date with the latest tech news. And now, here's my conversation
*  with Scott Aaronson. I sometimes get criticism from a listener here and there that while having
*  a conversation with a world-class mathematician, physicist, neurobiologist, aerospace engineer, or
*  theoretical computer scientist like yourself, I waste time by asking philosophical questions
*  about free will, consciousness, mortality, love, nature of truth, super intelligence,
*  whether time travel is possible, whether space time is emergent or fundamental,
*  even the crazier questions like whether aliens exist, what their language might look like,
*  what their math might look like, whether math is invented or discovered, and of course,
*  whether we live in a simulation or not. So I try to dance back and forth from the
*  deep technical to the philosophical. So I've done that quite a bit. So you're a world-class
*  computer scientist, and yet you've written about this very point that philosophy is important for
*  experts in any technical discipline, though they somehow seem to avoid this. So I thought it'd be
*  really interesting to talk to you about this point. Why should we computer scientists,
*  mathematicians, physicists care about philosophy, do you think? Well, I would reframe the question
*  a little bit. I mean, philosophy, almost by definition, is the subject that's concerned
*  with the biggest questions that you could possibly ask. So the ones you mentioned,
*  are we living in a simulation? Are we alone in the universe? How should we even think about such
*  questions? Is the future determined? And what do we even mean by it being determined? Why are we
*  alive at the time we are and not at some other time? And when you contemplate the enormity of
*  those questions, I think you could ask, well, then why be concerned with anything else? Why not spend
*  your whole life on those questions? I think in some sense, that is the right way to phrase the
*  question. And actually, what we learned throughout history, but really starting with the scientific
*  revolution with Galileo and so on, is that there is a good reason to focus on narrower questions,
*  more technical, mathematical or empirical questions, and that is that you can actually
*  make progress on them. And you can actually often answer them. And sometimes they actually
*  tell you something about the philosophical questions that maybe motivated your curiosity
*  as a child. They don't necessarily resolve the philosophical questions, but sometimes they
*  reframe your whole understanding of them. And so for me, philosophy is just the thing that you have
*  in the background from the very beginning. These are the reasons why you went into intellectual life
*  in the first place, at least the reasons why I did. But math and science are tools that we have
*  for actually making progress and hopefully even changing our understanding of these
*  philosophical questions, sometimes even more than philosophy itself does.
*  Why do you think computer scientists avoid these questions? We'll run away from them a little bit,
*  at least in the technical scientific discourse. Well, I'm not sure if they do so more than any
*  other scientists do. Alan Turing was famously interested. One of his two most famous papers
*  was in a philosophy journal, Mind. It was the one where he proposed the Turing test. He took
*  Wittgenstein's course at Cambridge, argued with him. I just recently learned that little bit,
*  and it's actually fascinating. I was trying to look for resources in trying to understand
*  where the sources of disagreement and debates between Wittgenstein and Turing were. It's
*  interesting that these two minds have somehow met in the arc of history. Yeah, well, the transcript
*  of the course, which was in 1939, is one of the more fascinating documents that I've ever read.
*  Wittgenstein is trying to say, well, all of these formal systems are just
*  complete irrelevancies. If a formal system is irrelevant, who cares? Why does that matter in
*  real life? Turing is saying, well, look, if you use an inconsistent formal system to design a bridge,
*  the bridge may collapse. So Turing, in some sense, is thinking decades ahead,
*  I think, of where Wittgenstein is, to where the formal systems are actually going to be used
*  in computers, to actually do things in the world. It's interesting that Turing actually dropped the
*  course halfway through. Why? Because he had to go to Bletchley Park and work on something of
*  more immediate importance. That's fascinating. Take a step from philosophy to actual, the biggest
*  possible step to actual engineering with actual real impact. Yeah, and I would say more generally,
*  a lot of scientists are interested in philosophy, but they're also busy. They have a lot on their
*  plate, and there are a lot of very concrete questions that are already not answered, but
*  look like they might be answerable. So then you could say, well, then why break your brain over
*  these metaphysically unanswerable questions when there were all of these answerable ones instead?
*  I think for me, I enjoy talking about philosophy. I even go to philosophy conferences sometimes,
*  such as the FQXI conferences. I enjoy interacting with philosophers. I would not want to be a
*  professional philosopher because I like being in a field where I feel like if I get too confused
*  about the sort of eternal questions, then I can actually make progress on something.
*  Can you maybe link on that for just a little longer? What do you think is the difference?
*  The corollary of the criticism that I mentioned previously,
*  that why ask the philosophical questions of the mathematician, is if you want to ask
*  philosophical questions, then invite a real philosopher on and ask them. What's the difference
*  between the way a computer scientist or mathematician ponders a philosophical question
*  and a philosopher ponders a philosophical question? Well, a lot of it just depends on
*  the individual. It's hard to make generalizations about entire fields, but I think if we try to
*  stereotype, we would say that scientists very often will be less careful in their use of words.
*  Philosophers are really experts in sort of like when I talk to them, they will just pounce if I
*  use the wrong phrase for something. Experts is a very nice word. You could say sticklers.
*  They will sort of interrogate my word choices, let's say, to a much greater extent than scientists
*  would. Scientists will often, if you ask them about a philosophical problem like the hard
*  problem of consciousness or free will or whatever, they will try to relate it back to recent research,
*  research about neurobiology. The best of all is research that they personally are involved with.
*  Of course, they will want to talk about that and it is what they will think of. Of course,
*  you could have an argument that maybe it's all interesting as it goes, but maybe none of it
*  touches the philosophical question. Maybe a science at least, as I said, it does tell us
*  concrete things and even if a deep dive into neurobiology will not answer the hard problem
*  of consciousness, maybe it can take us about as far as we can get toward expanding our minds about
*  it, toward thinking about it in a different way. I think neurobiology can do that, but with these
*  profound philosophical questions, also art and literature do that. They're all different ways of
*  trying to approach these questions for which we don't even know really what an answer would
*  look like, and yet somehow we can't help but keep returning to the questions. You have a kind of
*  beautiful mathematical way of discussing this with the idea of Q'. You write that usually the only
*  way to make progress on the big questions like the philosophical questions we're talking about now
*  is to pick off smaller sub-questions. Ideally, sub-questions that you can attack using math,
*  empirical observation, or both. You define the idea of a Q'. Given an unanswerable philosophical
*  riddle Q, replace it with a merely in quote scientific or mathematical question Q',
*  which captures part of what people have wanted to know when they first asked Q. Then with luck,
*  one solves Q'. You describe some examples of such Q' sub-questions in your long essay titled,
*  Why Philosophers Should Care About Computational Complexity. You catalog the various Q' on which
*  theoretical computer science has made progress. Can you mention a few favorites if any pop to mind?
*  I would say some of the most famous examples in history of that sort of replacement were,
*  to go back to Alan Turing, what he did in his computing machinery and intelligence paper.
*  He explicitly started with the question, can machines think? Then he said, sorry,
*  I think that question is too meaningless, but here's a different question. Could you program
*  a computer so that you couldn't tell the difference between it and a human?
*  In the very first few sentences, he in fact just formulates the Q' question.
*  It precisely, he does precisely that. Or we could look at Gödel, where you had these
*  philosophers arguing for centuries about the limits of mathematical reasoning, the limits of
*  formal systems. Then by the early 20th century, logicians, starting with Frege, Russell, and then
*  most spectacularly Gödel managed to reframe those questions as, look, we have these formal systems,
*  they have these definite rules. Are there questions that we can phrase within the rules of
*  these systems that are not provable within the rules of the systems? Can we prove that fact?
*  That would be another example. I had this essay called The Ghost in the Quantum Turing Machine.
*  That's one of the crazier things I've written. I tried to advocate doing something similar there
*  for free will, where instead of talking about, is free will real, or we get hung up on the meaning
*  of what exactly do we mean by freedom? Or do we mean compatibilist free will, libertarian free will?
*  What do these things mean? I suggested just asking the question, how well in principle,
*  consistently with the laws of physics, could a person's behavior be predicted without,
*  so let's say, destroying the person's brain, taking it apart in the process of trying to predict them?
*  Asking that question gets you into all sorts of meaty and interesting issues,
*  issues of what is the computational substrate of the brain? Can you understand the brain
*  just at the level of the neurons, at the abstraction of a neural network? Or do you need to go deeper
*  to the molecular level and ultimately even to the quantum level? Of course, that would put
*  limits on predictability if you did. You need to reduce the mind to a computational device
*  like formalize it so then you can make predictions about whether you could predict the behavior.
*  If you were trying to predict a person, then presumably you would need some model of their
*  brain. Now the question becomes one of how accurate can such a model become? Can you make a model that
*  will be accurate enough to really seriously threaten people's sense of free will? Not just
*  metaphysically, but really, I have written in this envelope what you were going to say next.
*  Is accuracy the right term here? It's also a level of abstraction that has to be right.
*  If you're accurate at the quantum level, that may not be convincing to us at the human level.
*  The question is what accuracy at the level of the underlying mechanisms do you need in order to
*  predict the behavior? At the end of the day, the test is just can you foresee what the person is
*  going to do? In discussions of free will, it seems like both sides want to very quickly dismiss that
*  question as irrelevant. Well, to me, it's totally relevant because if someone says, oh, well, a
*  plus demon that knew the complete state of the universe could predict everything you're going
*  to do, therefore you don't have free will. It doesn't trouble me that much because I've never
*  met such a demon. We even have some reasons to think maybe it could not exist as part of our
*  world. It was only an abstraction, a thought experiment. On the other hand, if someone said,
*  I have this brain scanning machine. You step into it and then every paper that you will ever write,
*  it will write every thought that you will have even right now about the machine itself. It will
*  foresee. If you can actually demonstrate that, then I think that threatens my internal sense
*  of having free will in a much more visceral way. Now you notice that we're asking a much more
*  empirical question. We're asking, is such a machine possible or isn't it? We're asking if
*  it's not possible, then what in the laws of physics or what about the behavior of the brain
*  prevents it from existing? If you could philosophize a little bit within this empirical question,
*  where do you think would enter the... By which mechanism would enter the possibility that we
*  can't predict the outcome? There would be something that would be akin to a free will.
*  You could say the obvious possibility, which was recognized by Eddington and many others about as
*  soon as quantum mechanics was discovered in the 1920s, was that if let's say a sodium ion channel
*  in the brain, its behavior is chaotic. It's governed by these Hodgley-Huxkin equations
*  in neuroscience, which are differential equations that have a stochastic component.
*  This ultimately governs, let's say, whether a neuron will fire or not fire.
*  That's the basic chemical process or electrical process by which signals are sent in the brain.
*  Exactly. You could ask, well, where does the randomness in the process,
*  that neuroscientists, what neuroscientists would treat as randomness, where does it come from?
*  Ultimately, it's thermal noise. Where does thermal noise come from? Ultimately,
*  there were some quantum mechanical events at the molecular level that are getting
*  chaotically amplified by a butterfly effect. Even if you knew the complete quantum state of
*  someone's brain, at best you could predict the probabilities that they would do one thing or do
*  another thing. I think that part is actually relatively uncontroversial. The controversial
*  question is whether any of it matters for the philosophical questions that we care about.
*  Because you could say if all it's doing is just injecting some randomness into an otherwise
*  completely mechanistic process, well, then who cares? More concretely, if you could build a
*  machine that could just calculate even just the probabilities of all of the possible things that
*  you would do. Of all the things that said you had a 10% chance of doing, you did exactly a 10th of
*  them and so on and so on. That somehow also takes away the feeling of free will.
*  Exactly. To me, it seems essentially just as bad as if the machine deterministically predicted you.
*  It seems hardly different from that. A more subtle question is could you even learn enough
*  about someone's brain to do that? Another central fact about quantum mechanics is that
*  making a measurement on a quantum state is an inherently destructive operation.
*  Okay, so if I want to measure the position of a particle, it was well, before I measured,
*  it had a superposition over many different positions. As soon as I measure, I localize it.
*  Now I know the position, but I've also fundamentally changed the state.
*  You could say, well, maybe in trying to build a model of someone's brain that was accurate enough
*  to actually make, let's say, even well calibrated probabilistic predictions of their future
*  behavior, maybe you would have to make measurements that were just so accurate that you would just
*  fundamentally alter their brain. Or maybe not. Maybe it would suffice to just make some nanorobots
*  that just measured some much larger scale macroscopic behavior like what is this neuron
*  doing? What is that neuron doing? Maybe that would be enough. But now what I claim is that
*  we're now asking a question in which it is possible to envision what progress on it would look like.
*  Yeah, but just as you said, that question may be slightly detached from the philosophical question
*  in the sense if consciousness somehow has a role to the experience of free will.
*  Ultimately, when we're talking about free will, we're also talking about not just the predictability
*  of our actions, but somehow the experience of that predictability. Yeah. Well, a lot of philosophical
*  questions ultimately feed back to the hard problem of consciousness as much as you can try to talk
*  around it or not. There is a reason why people try to talk around it, which is that a democratist
*  talked about the hard problem of consciousness in 400 BC in terms that would be totally recognizable
*  to us today. And it's really not clear if there's been progress since or what progress could
*  possibly consist of. Is there a Q prime type of sub-question that could help us get at consciousness?
*  It's something about consciousness. Well, there is the whole question of AI. Can you build a
*  superhuman level AI? Can it work in a completely different substrate from the brain?
*  Of course, that was Alan Turing's point. Even if that was done, maybe people would still argue
*  about the hard problem of consciousness. And yet, my claim is a little different. My claim is that
*  in a world where there were human level AIs or where we'd been even overtaken by such AIs,
*  the entire discussion of the hard problem of consciousness would have a different character.
*  It would take place in different terms in such a world, even if we hadn't answered the question.
*  And my claim about free will would be similar. If this prediction machine that I was talking about
*  could actually be built, well, now the entire discussion of free will is transformed by that,
*  even if in some sense the metaphysical question hasn't been answered.
*  Yeah, exactly. It transforms it fundamentally because say that machine does tell you that it
*  can predict perfectly, and yet there is this deep experience of free will. And then that changes
*  the question completely. And it starts actually getting to the question of the AGI, the Turing
*  questions of the demonstration of free will, the demonstration of intelligence, the demonstration
*  of consciousness. Does that equal consciousness, intelligence, and free will? But see, Alex, if
*  every time I was contemplating a decision, this machine had printed out an envelope where I could
*  open it and see that it knew my decision, I think that actually would change my subjective experience
*  of making decisions. Does knowledge change your subjective experience?
*  The knowledge that this machine had predicted everything I would do, it might drive me completely
*  insane, but at any rate it would change my experience to not just discuss such a machine
*  as a thought experiment, but to actually see it. You could say at that point, why not simply call
*  this machine a second instantiation of me and be done with it? Why even privilege the original me
*  over this perfect duplicate that exists in the machine? Or there could be a religious experience
*  with it too. It's kind of what God throughout the generations is supposed to have. That God
*  kind of represents that perfect machine. I guess, actually, I don't even know what are the religious
*  interpretations of free will. So if God knows perfectly everything in religion, in the various
*  religions, where does free will fit into that? Do you know? That has been one of the big things
*  that theologians have argued about for thousands of years. I am not a theologian, so maybe I
*  shouldn't go there. There's not a clear answer in a book like... I mean, the Calvinists debated this.
*  Different religious movements have taken different positions on that question, but
*  that is how they think about it. Meanwhile, a large part of what animates theoretical computer
*  science is we are asking what are the ultimate limits of what you can know or calculate or figure
*  out by entities that you can actually build in the physical world. If I were trying to explain it
*  to a theologian, maybe I would say we are studying to what extent gods can be made manifest in the
*  physical world. I'm not sure my colleagues would like that. Let's talk about quantum computers.
*  Yeah, sure. Sure. As you've said, quantum computing, at least in the 1990s, was a profound story at the
*  intersection of computer science, physics, engineering, math, and philosophy. So there's
*  this broad and deep aspect to quantum computing that represents more than just the quantum computer.
*  But can we start at the very basics? What is quantum computing? Yeah. So it's a proposal for
*  a new type of computation, or let's say a new way to harness nature to do computation
*  that is based on the principles of quantum mechanics. Now, the principles of quantum
*  mechanics have been in place since 1926. They haven't changed. What's new is how we want to
*  use them. So what does quantum mechanics say about the world? The physicists, I think,
*  over the generations, convinced people that that is an unbelievably complicated question and just
*  give up on trying to understand it. I can let you in, not being a physicist, I can let you in on a
*  secret, which is that it becomes a lot simpler if you do what we do in quantum information theory
*  and take the physics out of it. So the way that we think about quantum mechanics is as a generalization
*  of the rules of probability themselves. So you might say there was a 30% chance that it was going
*  to snow today or something. You would never say that there was a negative 30% chance. That would
*  be nonsense. Much less would you say that there was an I% chance, a square root of minus 1% chance.
*  Now, the central discovery that quantum mechanics made is that fundamentally the world is described
*  by the possibilities for what a system could be doing are described using numbers called
*  amplitudes, which are like probabilities in some ways, but they are not probabilities.
*  They can be positive, for one thing, they can be positive or negative. In fact, they can even be
*  complex numbers. If you've heard of a quantum superposition, this just means some state of
*  affairs where you assign an amplitude, one of these complex numbers, to every possible
*  configuration that you could see a system in on measuring it. So for example, you might say that
*  an electron has some amplitude for being here and some other amplitude for being there.
*  Now, if you look to see where it is, you will localize it. You will force the amplitudes to
*  be converted into probabilities. That happens by taking their squared absolute value.
*  You can say either the electron will be here or it will be there. Knowing the amplitudes,
*  you can predict at least the probabilities that you'll see each possible outcome.
*  But while a system is isolated from the whole rest of the universe, the rest of its environment,
*  the amplitudes can change in time by rules that are different from the normal rules of probability
*  and that are alien to our everyday experience. So anytime anyone ever tells you anything about
*  the weirdness of the quantum world or assuming that they're not lying to you,
*  yet another consequence of nature being described by these amplitudes.
*  So most famously, what amplitudes can do is that they can interfere with each other.
*  In the famous double slit experiment, what happens is that you shoot a particle,
*  like an electron, let's say, at a screen with two slits in it, and you find that
*  there are, you know, on a second screen, now there are certain places where that electron will never
*  end up, you know, after it passes through the first screen. And yet, if I close off one of the
*  slits, then the electron can appear in that place. Okay? So by decreasing the number of paths that
*  the electron could take to get somewhere, you can increase the chance that it gets there. Okay? Now,
*  how is that possible? Well, it's because, you know, as we would say, now the electron has a
*  superposition state. Okay? It has some amplitude for reaching this point by going through the
*  first slit. It has some other amplitude for reaching it by going through the second slit.
*  But now if one amplitude is positive and the other one is negative, then I have to add them all up,
*  right? I have to add the amplitudes for every path that the electron could have taken to reach
*  this point. And those amplitudes, if they're pointing in different directions, they can cancel
*  each other out. That would mean the total amplitude is zero and the thing never happens at all.
*  I close off one of the possibilities, then the amplitude is positive or it's negative,
*  and now the thing can happen. Okay? So that is sort of the one trick of quantum mechanics.
*  And now I can tell you what a quantum computer is. Okay? A quantum computer is a computer that tries
*  to exploit, you know, these, exactly these phenomena, superposition, amplitudes, and
*  interference in order to solve certain problems much faster than we know how to solve them
*  otherwise. So it's the basic building block of a quantum computer is what we call a quantum bit or
*  a qubit. That just means a bit that has some amplitude for being zero and some other amplitude
*  for being one. So it's a superposition of zero and one states, right? But now the key point
*  is that if I've got, let's say, a thousand qubits, the rules of quantum mechanics are completely
*  unequivocal that I do not just need one amp, you know, I don't just need amplitudes for each qubit
*  separately. Okay? In general, I need an amplitude for every possible setting of all thousand of
*  those bits. Okay? So that what that means is two to the 1000 power amplitudes. Okay? If I had to
*  write those down, let's say in the memory of a conventional computer, if I had to write down
*  two to the 1000 complex numbers, that would not fit within the entire observable universe.
*  Okay? And yet, you know, quantum mechanics is unequivocal that if these qubits can all interact
*  with each other, and in some sense, I need two to the 1000 parameters, you know, amplitudes to
*  describe what is going on. Now, you know, now I can tell you where all the popular articles,
*  you know, about quantum computing go off the rails is that they say, you know, they sort of,
*  sort of say what I just said, and then they say, oh, so the way a quantum computer works is just
*  by trying every possible answer in parallel. You know, that sounds too good to be true. And
*  unfortunately, it kind of is too good to be true. The problem is I could make a superposition
*  over every possible answer to my problem. You know, even if there were two to the 1000 of them,
*  right? I can easily do that. The trouble is for a computer to be useful, you've got at some point,
*  you've got to look at it and see an output. Right? And if I just measure a superposition
*  over every possible answer, then the rules of quantum mechanics tell me that all I'll see will
*  be a random answer. You know, if I just wanted a random answer, well, I could have picked one
*  myself with a lot less trouble. Right? So the entire trick with quantum computing, with every
*  algorithm for a quantum computer, is that you try to choreograph a pattern of interference of
*  amplitudes. And you try to do it so that for each wrong answer, some of the paths leading to that
*  wrong answer have positive amplitudes, and others have negative amplitudes. So on the whole, they
*  cancel each other out. Okay, whereas all the paths leading to the right answer should reinforce
*  each other, you know, should have amplitudes pointing the same direction. So the design of
*  algorithms in this space is the choreography of the interferences. Precisely. That's precisely
*  what it is. Can we take a brief step back and you mentioned information. Yes. So in which part of
*  this beautiful picture that you've painted is information contained? Oh, well, information is
*  at the core of everything that we've been talking about. Right? I mean, the bit is, you know, the
*  basic unit of information since, you know, Claude Shannon's paper in 1948. You know, and, you know,
*  of course, you know, people had the concept even before that, you know, he popularized the name.
*  Right. But I mean, but a bit is zero or one. That's right. Basic. That's right. And what we would say
*  is that the basic unit of quantum information is the qubit is, you know, the object, any object that
*  can be maintained in this manipulated in a superposition of zero and one states. Now,
*  you know, sometimes people ask, well, but what is a qubit physically? Right. And there are all these
*  different, you know, proposals that are being pursued in parallel for how you implement qubits.
*  There is, you know, superconducting quantum computing that was in the news recently because
*  of Google's quantum supremacy experiment, right? Where you would have some little coils where a
*  current can flow through them in two different energy states, one representing a zero, another
*  representing a one. And if you cool these coils to just slightly above absolute zero, like a
*  hundredth of a degree, then they superconduct and then the current can actually be in a superposition
*  of the two different states. So that's one kind of qubit. Another kind would be, you know, just
*  an individual atomic nucleus, right? It has a spin. It could be spinning clockwise. It could be
*  spinning counterclockwise, or it could be in a superposition of the two spin states. That is
*  another qubit. But see, just like in the classical world, right, you could be a virtuoso programmer
*  without having any idea of what a transistor is, right, or how the bits are physically represented
*  inside the machine, even that the machine uses electricity, right? You just care about the logic.
*  It's sort of the same with quantum computing, right? Qbits could be realized by many, many
*  different quantum systems, and yet all of those systems will lead to the same logic, you know,
*  the logic of qubits and how, you know, how you measure them, how you change them over time.
*  And so, you know, the subject of, you know, how qubits behave and what you can do with qubits,
*  that is quantum information. So just to linger on that, so does the physical design implementation
*  of a qubit does not interfere with that next level of abstraction that you can program over it.
*  So it truly is, the idea of it is, is it okay? Well, to be honest with you, today they do interfere
*  with each other. That's because all the quantum computers we can build today are very noisy,
*  right? And so sort of the, you know, the qubits are very far from perfect, and so the lower level
*  sort of does affect the higher levels, and we sort of have to think about all of them at once.
*  Okay, but eventually, where we hope to get is to what are called error-corrected quantum computers,
*  where the qubits really do behave like perfect abstract qubits for as long as we want them to.
*  And in that future, you know, the, you know, a future that we can already sort of prove theorems
*  about or think about today, but in that future, the logic of it really does become decoupled from
*  the hardware. So if noise is currently like the biggest problem for quantum computing,
*  and then the dream is error-correcting quantum computers, can you just maybe describe what does
*  it mean for there to be noise in the system? Absolutely. So yeah, so the problem is even a
*  little more specific than noise, so that the fundamental problem if you're trying to actually
*  build a quantum computer, you know, of any appreciable size, is something called decoherence.
*  Okay, and this was recognized from the very beginning, you know, when people first started
*  thinking about this in the 1990s. Now, what decoherence means is sort of the unwanted
*  interaction between, you know, your qubits, you know, the state of your quantum computer
*  and the external environment. Okay, and why is that such a problem? Well, I talked before about
*  how, you know, when you measure a quantum system, so let's say if I measure a qubit that's in a
*  superposition of zero and one states to ask it, you know, are you zero or are you one? Well,
*  now I force it to make up its mind, right? And now probabilistically, it chooses one or the other,
*  and now, you know, it's no longer a superposition, there's no longer amplitudes,
*  there's just there's some probability that I get a zero and there's some that I get a one.
*  Now, the trouble is that it doesn't have to be me who's looking, okay? In fact, it doesn't have
*  to be any conscious entity. Any kind of interaction with the external world that leaks out the
*  information about whether this qubit was a zero or a one, sort of that causes the zero-ness or
*  the oneness of the qubit to be recorded in, you know, the radiation in the room, in the molecules
*  of the air, in the wires that are connected to my device, any of that. As soon as the information
*  leaks out, it is as if that qubit has been measured, okay? It is, you know, the state has now
*  collapsed. You know, another way to say it is that it's become entangled with its environment,
*  okay? But, you know, from the perspective of someone who's just looking at this qubit,
*  it is as though it has lost its quantum state. And so what this means is that if I want to do
*  a quantum computation, I have to keep the qubits sort of fanatically well isolated from their
*  environment, but then at the same time, they can't be perfectly isolated because I need to tell them
*  what to do. I need to make them interact with each other, for one thing, and not only that,
*  but in a precisely choreographed way, okay? And, you know, that is such a staggering problem, right?
*  How do I isolate these qubits from the whole universe, but then also tell them exactly what
*  to do? I mean, you know, there were distinguished physicists and computer scientists in the 90s
*  who said this is fundamentally impossible, you know? The laws of physics will just never let you
*  control qubits to the degree of accuracy that you're talking about. Now, what changed the views
*  of most of us was a profound discovery in the mid to late 90s, which was called the theory of quantum
*  error correction and quantum fault tolerance, okay? And the upshot of that theory is that if I want
*  to build a reliable quantum computer and scale it up to, you know, an arbitrary number of as many
*  qubits as I want, you know, and doing as much on them as I want, I do not actually have to get the
*  qubits perfectly isolated from their environment. It is enough to get them really, really, really
*  well isolated, okay? And even if every qubit is sort of leaking, you know, its state into the
*  environment at some rate, as long as that rate is low enough, okay, I can sort of encode the
*  information that I care about in very clever ways across the collective states of multiple qubits,
*  okay, in such a way that even if, you know, a small percentage of my qubits leak, well,
*  I'm constantly monitoring them to see if that leak happened. I can detect it and I can correct it.
*  I can recover the information I care about from the remaining qubits, okay? And so, you know,
*  you can build a reliable quantum computer even out of unreliable parts, right? Now,
*  in some sense, you know, that discovery is what set the engineering agenda for quantum computing
*  research from the 1990s until the present, okay? The goal has been, you know, engineer qubits that
*  are not perfectly reliable, but reliable enough that you can then use these error correcting codes
*  to have them simulate qubits that are even more reliable than they are, right?
*  The error correction becomes a net win rather than a net loss, right? And then once you reach that
*  sort of crossover point, then, you know, your simulated qubits could in turn simulate qubits
*  that are even more reliable and so on until you've just, you know, effectively you have arbitrarily
*  reliable qubits. So long story short, we are not at that breakeven point yet. We're a hell of a
*  lot closer than we were when people started doing this in the 90s, like orders of magnitude closer.
*  But the key ingredient there is the more qubits, the better because...
*  Ah, well, the more qubits, the larger the computation you can do, right? I mean,
*  qubits are what constitute the memory of your quantum computer, right?
*  But also for the, sorry, for the error correcting mechanism.
*  Ah, yes. So the way I would say it is that error correction imposes an overhead in the number of
*  qubits. And that is actually one of the biggest practical problems with building a scalable
*  quantum computer. If you look at the error correcting codes, at least the ones that we
*  know about today, and you look at, you know, what would it take to actually use a quantum computer to
*  hack your credit card number, which is, you know, maybe the most famous application people talk
*  about, right? Let's say to factor huge numbers and thereby break the RSA cryptosystem. Well,
*  what that would take would be thousands of several thousand logical qubits. But now with
*  the known error correcting codes, each of those logical qubits would need to be encoded itself
*  using thousands of physical qubits. So at that point, you're talking about millions of physical
*  qubits. And in some sense, that is the reason why quantum computers are not breaking cryptography
*  already. It's because of these immense overheads involved. So that overhead is additive or
*  multiplicative. Well, it's multiplicative. I mean, it's like you take the number of
*  logical qubits that you need in your abstract quantum circuit, you multiply it by a thousand
*  or so. So, you know, there's a lot of work on, you know, inventing better, trying to invent better
*  error correcting codes. Okay, that is the situation right now. In the meantime, we are now in what
*  the physicist John Preskill called the noisy intermediate scale quantum or NISQ era. And
*  this is the era you can think of it as sort of like the vacuum. You know, we're now entering
*  the very early vacuum tube era of quantum computers. The quantum computer analog of the transistor
*  has not been invented yet. Right. That would be like true error correction, right? Where, you know,
*  we are not or something else that would achieve the same effect, right? We are not there yet.
*  But where we are now, let's say as of a few months ago, you know, as of Google's announcement of
*  quantum supremacy, you know, we are now finally at the point where even with a non error corrected
*  quantum computer with, you know, these noisy devices, we can do something that is hard for
*  classical computers to simulate. Okay. So we can eke out some advantage. Now, will we in this noisy
*  era be able to do something beyond what a classical computer can do that is also useful to someone?
*  That we still don't know. People are going to be racing over the next decade to try to do that by
*  people. I mean, Google, IBM, you know, a bunch of startup companies and, you know,
*  research labs and governments and yeah. You just mentioned a million things. Well,
*  I'll backtrack for a second. Yeah, sure. Sure. So when these vacuum tube days, yeah, just entering
*  them and just entering. Wow. Okay. So yeah, how do we escape the vacuum? So how do we get to
*  how to get to where we are now with the CPU? Is this a fundamental engineering challenge? Is there
*  is there breakthroughs in on the physics side that they're needed on the computer science side?
*  What's is there an, is it a financial issue where much larger just sheer investment and excitement
*  is needed? So, you know, those are excellent questions. My guess, well, no, no, my guess
*  would be all of the above. I mean, my guess, you know, I mean, I mean, you know, you could say
*  fundamentally it is an engineering issue, right? The theory has been in place since the nineties,
*  you know, at least, you know, this is what, you know, error correction would look like, you know,
*  we do not have the hardware that is at that level. But at the same time, you know, so you could just,
*  you know, try to power through, you know, maybe even like, you know, if someone spent a trillion
*  dollars on some quantum computing Manhattan project, right, then conceivably they could just,
*  you know, build a, a, an error corrected quantum computer as it was envisioned back in the nineties.
*  Right. I think the more plausible thing to happen is that there will be further theoretical
*  breakthroughs and there will be further insights that will cut down the cost of doing this.
*  So let's take a brief step to the philosophical. I just recently talked to Jim Keller, who's
*  sort of like the famed architect in the microprocessor world. Okay. And he's
*  been told for decades every year that the Moore's law is going to die this year.
*  And he tries to argue that the Moore's law is still alive and well, and it'll be alive for
*  quite a long time to come. How long? How long did he say? Well, he's, the main point is it's still
*  alive, but he thinks there's still a thousand X improvement just on shrinking the transition.
*  That's possible. Whatever. The point is that the exponential growth we see it is actually
*  a huge number of these S curves, just constant breakthroughs at the philosophical level.
*  Why do you think we, as a descendants of apes, we're able to, to just keep coming up with these new
*  breakthroughs on the CPU side? Is this something unique to this particular endeavor or will it be
*  possible to replicate in the quantum computer space? Okay. All right. There was a lot there to,
*  to, but to, to, to break off something. I mean, I think we are in an extremely special period of
*  human history, right? I mean, it's, it is, you could say obviously special, you know, in, in,
*  in many ways, right? There are, you know, way more people alive than there, than there, than
*  there have been. And, and, you know, the, you know, the whole, you know, future of the planet is in,
*  is in question in a way that it, it hasn't been, you know, for, for the rest of human history. But,
*  but, you know, in particular, you know, we are in the era where, you know, we, we finally figured out
*  how to build, you know, universal machines, you could say, you know, the things that we call
*  computers, you know, machines that you program to simulate the behavior of, of whatever machine you
*  want. And, you know, and, and, and, and, and, and, and, and once you've sort of crossed this
*  threshold of universality, you know, you've built, you could say, you know, touring, you've
*  instantiated touring machines in the physical world. Well, then the main questions are, are
*  ones of numbers. They are, you know, ones of how many, of how much memory can you access? How fast
*  does it run? How many parallel processors, you know, at least until quantum computing, quantum
*  computing is the one thing that changes what I just said, right? But, you know, as long as it's
*  classical computing, then it's all questions of numbers. And, you know, the, the, you could say at
*  a theoretical level, the computers that we have today are the same as the ones in the fifties.
*  They're just millions of times, you know, faster and with millions of times more memory. And,
*  you know, I mean, I think there's been an immense economic pressure to, you know, get more and more
*  transistors, you know, get them smaller and smaller, get, you know, add more and more cores. And,
*  you know, and, and, and, and in, in some sense, like a huge fraction of sort of all of the
*  technological progress that there is in all of civilization has gotten concentrated just more
*  narrowly into just those problems, right? And so, you know, it has been
*  one of the biggest success stories in the history of technology, right? There's, you know, I mean,
*  it is, I am as amazed by it as, as anyone else is, right? But at the same time, you know, we also
*  know that it, you know, and I, I, I, I really do mean we know that it cannot continue indefinitely,
*  okay? Because you will reach, you know, fundamental limits on, you know, how small you can possibly
*  make a processor. And, you know, if you want a real proof, you know, that would justify my use
*  of the word, you know, we know that, you know, Moore's law has to end. I mean, ultimately,
*  you will reach the limits imposed by quantum gravity, you know, you know, if, if you were
*  doing, if you tried to build a computer that operated at 10 to the 43 Hertz, so did 10 to
*  the 43 operations per second, that computer would use so much energy that it would simply
*  collapse through a black hole. Okay. So, you know, that, you know, in, in, in reality, we're going
*  to reach the limits long before that, but, you know, that is a sufficient proof. That there's a
*  limit. Yes. Yes. But it would be interesting to try to understand the mechanism, the economic
*  pressure that you said, just like the cold war was a pressure on getting us, getting us,
*  because I'm both, my us is both the Soviet Union and the United States, but getting us,
*  the two countries to get, to hurry up, to get the space to the moon, there seems to be that same
*  kind of economic pressure that somehow created a chain of engineering breakthroughs that resulted
*  in the Moore's law. Yeah. It'd be nice to replicate. Yeah. Well, I mean, I mean, some people are sort of
*  get depressed about the fact that technological progress, you know, may seem to have slowed down
*  in, in many, many realms outside of computing, right? And there was this whole thing of, you know,
*  we wanted flying cars and we only got Twitter instead, right? And yeah, good old Peter Thiel.
*  Yeah. Yeah. Right. Right. So then jumping to another really interesting topic that you mentioned. So
*  Google announced with their work in the paper in nature with quantum supremacy. Yes. Can you
*  describe again, back to the basic, what is perhaps not so basic, what is quantum supremacy?
*  Absolutely. So quantum supremacy is a term that was coined by again, by John Preskill in 2012.
*  Not everyone likes the name, you know, but, you know, it's sort of stuck. You know, we don't,
*  we sort of haven't found a better alternative. It's technically quantum computational. Yeah.
*  Yeah. Supremacy. That's right. That's right. And, but the basic idea is actually one that goes all
*  the way back to the beginnings of quantum computing. When Richard Feynman and David
*  Deutsch, people like that were talking about it in the early eighties. And quantum supremacy
*  just refers to sort of the point in history when you can first use a quantum computer to do some
*  well-defined task much faster than any known algorithm running on any of the classical computers
*  that are available. Okay. So, you know, notice that I did not say a useful task. Okay. You know,
*  it could be something completely artificial, but it's important that the task be well-defined. So
*  in other words, you know, there is, it is something that has right and wrong answers,
*  you know, and that are knowable independently of this device, right? And we can then, you know,
*  run the device, see if it gets the right answer or not. Can you clarify a small point? You said much
*  faster than a classical implementation. What about sort of, what about the space with where the
*  class, there's no, there's not, it doesn't even exist a classical algorithm to solve the problem.
*  So maybe I should clarify everything that a quantum computer can do, a classical computer
*  can also eventually do. Okay. And the reason why we know that is that a classical computer could
*  always, you know, if it had no limits of time and memory, it could always just store the entire
*  quantum state, you know, of your, you know, of the quantum store in a list of all the amplitudes,
*  you know, in the state of the quantum computer and then just, you know, do some linear algebra
*  to just update that state. Right. And so, so anything that quantum computers can do can also
*  be done by classical computers, albeit exponentially slower. So quantum computers don't go into some
*  magical place outside of Alan Turing's definition of computation. Precisely. They do not solve the
*  halting problem. They cannot solve anything that is uncomputable in Alan Turing's sense.
*  What we think they do change is what is efficiently computable. Okay. And, you know, since the 1960s,
*  you know, the word efficiently, you know, as well as been a central word in computer science,
*  but it's sort of a code word for something technical, which is basically with polynomial
*  scaling, you know, that as you get to larger and larger inputs, you would like an algorithm
*  that uses an amount of time that scales only like the size of the input raised to some power and not
*  exponentially with the size of the input. Right. Yeah. So I do hope we get to talk again, because
*  one of the many topics that there's probably several hours worth of conversation on is complexity,
*  which we probably won't even get a chance to touch today, but you briefly mentioned it,
*  but let's, let's maybe try to continue. So you said the definition of quantum supremacy is
*  basically a design is achieving a place where much faster on a formal, that quantum computer
*  is much faster on a formal well-defined problem. That is or isn't useful. Yeah. Yeah. Yeah. Right.
*  Right. And I would say that we really want three things, right? We want first of all, the quantum
*  computer to be much faster, just in the literal sense of like number of seconds, you know,
*  at the solving this, you know, well-defined, you know, problem. Secondly, we want it to be sort of,
*  you know, for a problem where we really believe that a quantum computer has better scaling
*  behavior. Right. So it's not just an incidental, you know, matter of hardware, but it's that,
*  you know, as you went to larger and larger inputs, you know, the classical scaling would be
*  exponential and the scaling for the quantum algorithm would only be polynomial. And then
*  thirdly, we want the first thing, the actual observed speed up to only be explainable in terms
*  of the scaling behavior. Right. So, you know, I want, I want, you know, a real world, you know,
*  a real problem to get solved. Let's say by a quantum computer with 50 qubits or so, and for no
*  one to be able to explain that in any way other than, well, you know, to this, this computer
*  involved a quantum state with two to the 50th power amplitudes and, you know, a classical simulation,
*  at least any that we know today would require keeping track of two to the 50th numbers. And
*  this is the reason why it was faster. So the intuition is that then if you demonstrate on 50
*  qubits, then once you get to a hundred qubits, then it'll be even much more faster.
*  Precisely, precisely. Yeah. And, you know, and, and quantum supremacy does not require error
*  correction, right? We don't, you know, we don't have, you could say true scalability yet or true,
*  you know, error correction yet, but you could say quantum supremacy is already enough by itself
*  to refute the skeptics who said a quantum computer will never outperform a classical
*  computer for anything. But one, how do you demonstrate quantum supremacy? And two,
*  what's up with these new news articles I'm reading that Google did so? Yeah. All right. Well,
*  what did they actually do? Great, great questions. Cause now you get into actually, you know, a lot
*  of the work that I've, you know, I and my students have been doing for the last decade, which was
*  precisely about how do you demonstrate quantum supremacy using technologies that, you know,
*  we thought would be available in the near future. And so one of the main things that we realized
*  around 2011, and this was me and my student, Alex Arkhipov at MIT at the time, and independently,
*  some others, including Bremner, Joseph and Shepherd. Okay. And the realization that we came to
*  was that if you just want to prove that a quantum computer is faster, you know, and not do something
*  useful with it, then there are huge advantages to sort of switching your attention from problems
*  like factoring numbers that have a single right answer to what we call sampling problems. So these
*  are problems where the goal is just to output a sample from some probability distribution,
*  let's say over strings of 50 bits, right? So there are, you know, many, many, many possible valid
*  outputs. You know, your computer will probably never even produce the same output twice, you know,
*  if it's running as, as, uh, uh, uh, even, you know, assuming it's running perfectly. Okay. But,
*  but the key is that some outputs are supposed to be likelier than other ones. So, yeah.
*  To clarify, is there a set of outputs that are valid and set there or not? Or is it more that
*  the distribution of a particular kind of output is more, is like there's a specific distribution
*  of a particular kind of output? Yeah, there's a specific distribution that you're trying to hit,
*  right? Or, you know, that you're trying to sample from. Now, there are a lot of questions about this,
*  you know, how do you do that? Right now, now how you, how, how you do it, you know, it turns out
*  that with a quantum computer, even with the noisy quantum computers that we have now that we have
*  today, what you can do is basically just apply a randomly chosen sequence of operations, right? So
*  we, you know, we, and sometimes, you know, we, you know, that part is almost trivial, right? We just
*  sort of get the qubits to interact in some random way, although a sort of precisely specified random
*  way. So we can repeat the exact same random sequence of interactions again and get another
*  sample from that same distribution. And what this does is it basically, well, it creates a lot of
*  garbage, but, you know, very specific garbage, right? So, you know, of all of the, so if we're
*  going to talk about Google's device, there were 53 qubits there, okay? And so there are two to the
*  53 power possible outputs. Now for some of those outputs, you know, there are, there was a little
*  bit more destructive interference in their amplitude, okay? So their amplitudes were a
*  little bit smaller. And for others, there was a little more constructive interference. You know,
*  the amplitudes were a little bit more aligned with each other, you know, and so those, those that were
*  a little bit likelier, okay? All of the outputs are exponentially unlikely, but some are, let's say,
*  two times or three times, you know, unlikelier than others, okay? And so you can define, you know,
*  this sequence of operations that gives rise to this probability distribution. Okay, now,
*  the next question would be, well, how do you, you know, even if you're sampling from it,
*  how do you verify that? How do you know? And so my students and I, and also the people at Google
*  who were doing the experiment came up with statistical tests that you can apply to the
*  outputs in order to try to verify, you know, what is, you know, that at least that some hard
*  problem is being solved. The test that Google ended up using was something that they called
*  the linear cross entropy benchmark, okay? And it's basically, you know, so the drawback of this test
*  is that it requires, like, it requires you to do a two to the 53 time calculation with your classical
*  computer, okay? So it's very expensive to do the test on a classical computer. The good news is-
*  How big of a number is two to the 53?
*  It's about nine quadrillion.
*  Okay.
*  That doesn't help.
*  Well, you know, it's, you want it in like scientific notation?
*  No, no, no, what I mean is-
*  Yeah, it is-
*  It is just-
*  It's impossible to run on a-
*  Yeah, so we will come back to that. It is just barely possible to run, we think, on the largest
*  supercomputer that currently exists on earth, which is called Summit at Oak Ridge National Lab, okay?
*  Great. This is exciting.
*  That's the short answer. So ironically, for this type of experiment, we don't want a hundred qubits,
*  okay? Because with a hundred qubits, even if it works, we don't know how to verify the results,
*  okay? So we want a number of qubits that is enough that the biggest classical computers on
*  earth will have to sweat and will just barely be able to keep up with the quantum computer,
*  using much more time, but they will still be able to do it in order that we can verify the results.
*  Which is where the 53 comes from, for the number of qubits?
*  Well, I mean, that's also that sort of, you know, that's sort of where they are now in terms of
*  scaling, and then soon that point will be passed. And then when you get to larger numbers of qubits,
*  then these types of sampling experiments will no longer be so interesting because we won't even
*  be able to verify the results and we'll have to switch to other types of computation. So with
*  the sampling thing, you know, so the test that Google applied with this linear cross entropy
*  benchmark was basically just take the samples that were generated, which are, you know, a very small
*  subset of all the possible samples that there are. But for those, you calculate with your
*  classical computer the probabilities that they should have been output. And you see, are those
*  probabilities like larger than the mean? You know, so is the quantum computer biased toward outputting
*  the strings that you want it to be biased toward. And then finally, we come to a very crucial
*  question, which is supposing that it does that. Well, how do we know that a classical computer
*  could not have quickly done the same thing? How do we know that this couldn't have been spoofed
*  by a classical computer? And so, well, the first answer is we don't know for sure, because this
*  takes us into questions of complexity theory. You know, the, I mean, questions on the, of the
*  magnitude of the P versus NP question and things like that, right? We, you know, we don't know how
*  to rule out definitively that there could be fast classical algorithms for, you know, even
*  simulating quantum mechanics and for, you know, simulating experiments like these. But we can give
*  some evidence against that possibility. And that was sort of the, you know, the main thrust of a
*  lot of the work that my colleagues and I did, you know, over the last decade, which is then sort of
*  in around 2015 or so, what led to Google deciding to do this experiment. So is the kind of evidence
*  theory, first of all, the hard P equals NP problem that you mentioned and the kind of evidence that
*  you're, were looking at, is that something you come to on a sheet of paper or is this something,
*  are these empirical experiments? It's math for the most part. I mean, it, you know, it's also
*  trot, you know, we have a bunch of methods that are known for simulating quantum
*  circuits or, you know, quantum computations with classical computers. And so we have to try them
*  all out and make sure that, you know, they don't work, you know, make sure that they have exponential
*  scaling on, you know, these problems and not just theoretically, but with the actual range of
*  parameters that are actually, you know, arising in Google's experiment. Okay. So there is an
*  empirical component to it, right? But now on the theoretical side, you know, what basically, what we
*  know how to do in theoretical computer science and computational complexity is, you know, we don't
*  know how to prove that most of the problems we care about are hard, but we know how to pass the
*  blame to someone else. Okay. We know how to say, well, look, you know, I can't prove that this
*  problem is hard, but if it is easy, then all these other things that, you know, you probably were
*  much more confident or were hard, then those would be easy as well. Okay. So we can give what are
*  called reductions. This has been the basic strategy in, you know, NP completeness, right? In all of
*  theoretical computer science and cryptography since the 1970s, really. And so we were able to
*  give some reduction evidence for the hardness of simulating these sampling experiments, these
*  sampling-based quantum supremacy experiments. The reduction evidence is not as satisfactory as it
*  should be. One of the biggest open problems in this area is to make it better. But, you know,
*  we can do something, you know, certainly we can say that, you know, if there is a fast classical
*  algorithm to spoof these experiments, then it has to be very, very unlike any of the algorithms that
*  we know. Which is kind of in the same kind of space of reasoning that people say P equal, not
*  equals NP. Yeah, it's in the same spirit. Yeah, in the same spirit. Okay. So Andrew Yang, a very
*  intelligent and presidential candidate with a lot of interesting ideas in all kinds of technological
*  fields, tweeted that because of quantum computing, no code is uncrackable. Is he wrong or right?
*  He was premature, let's say. So, well, okay, wrong. Look, you know, I'm actually, you know,
*  I'm a fan of Andrew Yang. I like his ideas. I like his candidacy. I think that, you know, he may be
*  ahead of his time with, you know, the universal basic income and, you know, and so forth. And he
*  may also be ahead of his time in that tweet that you referenced. So regarding using quantum computers
*  to break cryptography. So the situation is this. Okay. So the famous discovery of Peter Shor,
*  you know, 26 years ago, that really started quantum computing, you know, as an autonomous field,
*  was that if you built a full scalable quantum computer, then you could use it to efficiently
*  find the prime factors of huge numbers and calculate discrete logarithms and solve a few
*  other problems that are very, very special in character, right? They're not NP-complete problems.
*  We're pretty sure they're not. Okay. But it so happens that most of the public key cryptography
*  that we currently use to protect the internet is based on the belief that these problems are hard.
*  What Shor showed is that once you get scalable quantum computers, then that's no longer true.
*  Okay. But now, you know, before people panic, there are two important points to understand here.
*  Okay. The first is that quantum supremacy, the milestone that Google just achieved, is very,
*  very far from the kind of scalable quantum computer that would be needed to actually
*  threaten public key cryptography. Okay. So, you know, we touched on this earlier, right? But Google's
*  device has 53 physical qubits, right? To threaten cryptography, you're talking, you know, with any
*  of the known error correction methods, you're talking millions of physical qubits. Because error
*  correction would be required to do cryptography. Yes. Yes. Yes. Yes. It certainly would, right?
*  How great will the overhead be from the error correction that we don't know yet?
*  But with the known codes, you're talking millions of physical qubits and of a much higher quality
*  than any that we have now. Okay. So, you know, I don't think that that is, you know, coming soon.
*  Although people who have secrets that, you know, need to stay secret for 20 years, you know, are
*  already worried about this, you know, for the good reason that, you know, we presume that intelligence
*  agencies are already scooping up data, you know, in the hope that eventually they'll be able to
*  decode it once quantum computers become available. Okay. So, this brings me to the second
*  point I wanted to make, which is that there are other public key cryptosystems that are known
*  that we don't know how to break even with quantum computers. Okay. And so there's a whole field
*  devoted to this now, which is called post quantum cryptography. Okay. And so there is already,
*  so we have some good candidates now, the best known being what are called lattice based cryptosystems.
*  And there is already some push to try to migrate to these cryptosystems. So NIST
*  in the US is holding a competition to create standards for post quantum cryptography,
*  which will be the first step in trying to get every web browser and every router to upgrade,
*  you know, and use, you know, something like SSL that is would be based on, you know, what we
*  think is quantum secure cryptography. But, you know, this will be a long process. But, you know,
*  it is something that people are already starting to do. And so, you know, I'm sure his algorithm
*  is sort of a dramatic discovery. You know, it could be a big deal for whatever intelligence
*  agency first gets a scalable quantum computer, if no one, at least certainly if no one else knows
*  that they have it. Right. But eventually, we think that we could migrate the internet to the
*  post quantum cryptography, and then we'd be more or less back where we started. Okay. So this is
*  sort of not the application of quantum computing, I think that's really going to change the world
*  in a sustainable way, right? The big, by the way, the biggest practical application of quantum
*  computing that we know about by far, I think is simply the simulation of quantum mechanics itself,
*  in order to, you know, learn about chemical reactions, you know, design maybe new chemical
*  processes, new materials, new drugs, new solar cells, new superconductors, all kinds of things
*  like that. What's the size of a quantum computer that would be able to simulate the, you know,
*  quantum mechanical systems themselves, that would be impactful for the real world for the kind of
*  chemical reactions and that kind of work? What scale are we talking about?
*  Now you're asking a very, very current question, a very big question. People are going to be racing
*  over the next decade to try to do useful quantum simulations, even with, you know, 100 or 200
*  qubit quantum computers of the sort that we expect to be able to build over the next decade.
*  Okay. So that might be, you know, the first application of quantum computing that we're
*  able to realize, you know, or maybe it will prove to be too difficult. And maybe even that will
*  require fault tolerance or, you know, will require error correction.
*  So that's an aggressive race to come up with the one case study, kind of like Peter Shor,
*  with the idea that would just capture the world's imagination of, look, we can actually do
*  something very useful here.
*  Right. But I think, you know, within the next decade, the best shot we have is certainly not,
*  you know, using Shor's algorithm to break cryptography, you know, just because it requires,
*  you know, too much in the way of error correction. The best shot we have is to do some
*  quantum simulation that tells the material scientists or chemists or nuclear physicists,
*  you know, something that is useful to them and that they didn't already know, you know,
*  and you might only need one or two successes in order to change some, you know, billion dollar
*  industries, right? Like, you know, the way that people make fertilizer right now is still based
*  on the Haber-Bosch process from a century ago, and it is some many-body quantum mechanics problem
*  that no one really understands, right? If you could design a better way to make fertilizer,
*  right, that's, you know, billions of dollars right there. So those are sort of the applications that
*  people are going to be aggressively racing toward over the next decade. Now, I don't know if they're
*  going to realize it or not, but, you know, it is, you know, they certainly at least have a shot.
*  So it's going to be a very, very interesting next decade.
*  Just to clarify, what's your intuition? Is if a breakthrough like that comes, is it possible
*  for that breakthrough to be on 50 to 100 qubits or is scale a fundamental thing like 500,
*  1000 plus qubits? Yeah, so I can tell you what the current studies are saying. You know, I think
*  probably better to rely on that than my intuition. But, you know, there was a group at Microsoft
*  had a study a few years ago that said even with only about 100 qubits, you know, you could already
*  learn something new about the chemical reaction that makes fertilizer, for example. The trouble
*  is they're talking about 100 qubits and about a million layers of quantum gates. Okay, so basically
*  they're talking about 100 nearly perfect qubits. So the logical qubits, as you mentioned. Yeah,
*  exactly. 100 logical qubits. And now, you know, the hard part for the next decade is going to be,
*  well, what can we do with 100 to 200 noisy qubits? Yeah. Yeah. Is there error correction
*  breakthroughs that might come without the need to do thousands or millions of physical qubits?
*  Yeah. So people are going to be pushing simultaneously on a bunch of different
*  directions. One direction, of course, is just making the qubits better, right? And, you know,
*  there is tremendous progress there. I mean, you know, the fidelities, like the accuracy of the
*  qubits has improved by several orders of magnitude, you know, in the last decade or two. Okay, the
*  second thing is designing better, or, you know, let's say lower overhead error correcting codes.
*  And even short of doing the full recursive error correction, you know, there are these error
*  mitigation strategies that you can use, you know, that may, you know, allow you to eke out
*  a useful speed up in the near term. And then the third thing is just taking the quantum algorithms
*  for simulating quantum chemistry or materials and making them more efficient. You know, and
*  those algorithms are already dramatically more efficient than they were, let's say, five years
*  ago. And so when, you know, I quoted these estimates like, you know, circuit depth of one million.
*  And so, you know, I hope that because people will care enough that these numbers are going to come
*  down. So you're one of the world class researchers in this space. There's a few groups, I can mention
*  Google and IBM working at this. There's other research labs, but you put also, you have an
*  amazing blog. You're too kind. You paid me to say it. You put a lot of efforts sort of to communicating
*  the science of this and communicating, exposing some of the BS and sort of the natural, just like
*  in the AI space, the natural charlatanism, if that's a word in this, in quantum mechanics in
*  general, but quantum computers and so on. Can you give some notes about people or ideas that people
*  like me or listeners in general from outside the field should be cautious of when they're taking in
*  news headings that Google achieved quantum supremacy? So what should we look out for?
*  Where's the charlatans in the space? Where's the BS?
*  Yeah. So good question. Unfortunately, quantum computing is a little bit like cryptocurrency
*  or deep learning. There is a core of something that is genuinely revolutionary and exciting.
*  And because of that core, it attracts this sort of vast penumbra of people making just
*  utterly ridiculous claims. And so with quantum computing, I mean, I would say that the main way
*  that people go astray is by not focusing on sort of the question of, are you getting a speed up
*  over a classical computer or not? And so people have dismissed quantum supremacy because it's not
*  useful, right? Or it's not itself, let's say, obviously useful for anything.
*  But ironically, these are some of the same people who will go and say, well, we care about useful
*  applications. We care about solving traffic routing and financial optimization and all these
*  things. And that sounds really good, but their entire spiel is sort of counting on nobody asking
*  the question, yes, but how well could a classical computer do the same thing?
*  I really mean the entire thing. They say, well, a quantum computer can do this. A quantum computer
*  can do that. And they just avoid the question, are you getting a speed up over a classical
*  computer or not? And if so, how do you know? Have you really thought carefully about classical
*  algorithms to solve the same problem? And a lot of the application areas that the
*  companies and investors are most excited about, that the popular press is most excited about
*  for quantum computers have been things like machine learning, AI, optimization. And the problem
*  with that is that since the very beginning, even if you have a perfect fault tolerant
*  scalable quantum computer, we have known of only modest speed ups that you can get for these
*  problems. So there is a famous quantum algorithm called Grover's algorithm. And what it can do is
*  it can solve many, many of the problems that arise in AI, machine learning, optimization,
*  including NP-complete problems. But it can solve them in about the square root of the number of
*  steps that a classical computer would need for the same problems. Now a square root speed up is
*  important. It's impressive. It is not an exponential speed up. So it is not the kind of game changer
*  that Shor's algorithm for factoring is, or for that matter that simulation of quantum mechanics
*  is. It is a more modest speed up. In theory, it could roughly double the size of the optimization
*  problems that you could handle. And so because people found that too boring or too unimpressive,
*  they've gone on to invent all of these heuristic algorithms where because no one really understands
*  them, you can just project your hopes onto them. That well, maybe it gets an exponential speed up.
*  You can't prove that it doesn't. And the burden is on you to prove that it doesn't get a speed up.
*  So they've done an immense amount of that kind of thing. And a really worrying amount of the case
*  for building a quantum computer has come to rest on this stuff that those of us in this field know
*  perfectly well is on extremely shaky foundations. So the fundamental question is show that there's
*  a speed up. Yes, absolutely. And in this space that you're referring to, which is actually interesting,
*  the area that a lot of people excited about is machine learning. So your sense is, do you think
*  it will, I know that there's a lot of smoke currently, but do you think there actually
*  eventually might be breakthroughs where you do get exponential speed ups in the machine learning
*  space? Absolutely, there might be. I mean, I think we know of modest speed ups that you can get for
*  these problems. I think whether you can get bigger speed ups is one of the biggest questions for
*  quantum computing theory, for people like me to be thinking about. Now, we had actually recently a
*  super exciting candidate for an exponential quantum speed up for a machine learning problem
*  that people really care about. This is basically the Netflix problem, the problem of recommending
*  products to users given some sparse data about their preferences. Karonidis and Prakash in 2016
*  had an algorithm for sampling recommendations that was exponentially faster than any known
*  classical algorithm. And so a lot of people were excited. I was excited about it. I had an 18-year-old
*  undergrad by the name of Yilin Tang, and she was obviously brilliant. She was looking for a project.
*  I gave her as a project, can you prove that this speed up is real? Can you prove that any classical
*  algorithm would need to access exponentially more data? This was a case where if that was true,
*  this was not a P versus NP type of question. This might well have been provable, but she worked on
*  it for a year. She couldn't do it. Eventually, she figured out why she couldn't do it. And the
*  reason was that that was false. There is a classical algorithm with a similar performance
*  to the quantum algorithm. So Yilin succeeded in de-quantizing that machine learning algorithm.
*  And then in the last couple of years, building on Yilin's breakthrough, a bunch of the other
*  quantum machine learning algorithms that were proposed have now also been de-quantized.
*  Yeah. That's an important backwards step. Yes. Or a forward step for science, but a step for
*  quantum machine learning that precedes the big next forward step. Right, right, right.
*  Now, some people will say, well, there's a silver lining in this cloud. They say,
*  well, thinking about quantum computing has led to the discovery of potentially useful new classical
*  algorithms. That's true. Right? And so you get these spin-off applications, but if you want a
*  quantum speed up, you really have to think carefully about that. Yilin's work was a perfect
*  illustration of why. Right? And I think that the challenge, the field is now open. Right?
*  Find a better example. Find where quantum computers are going to deliver big gains for
*  machine learning. Not only do I ardently support people thinking about that, I'm trying to think
*  about it myself and have my students and post-docs think about it. But we should not pretend that
*  those speed ups are already established. And the problem comes when so many of the companies and
*  journalists in this space are pretending that. Like all good things, like life itself, this
*  conversation must soon come to an end. Let me ask the most absurdly philosophical last question.
*  What is the meaning of life? What gives your life fulfillment, purpose, happiness,
*  and meaning? I would say number one, trying to discover new things about the world and share them
*  and communicate and learn what other people have discovered. Number two, my friends, my family,
*  my kids, my students, the people around me. Number three, trying when I can to
*  make the world better in some small ways. And it's depressing that I can't do more and that
*  the world is facing crises over the climate and over
*  resurgent authoritarianism and all these other things. But trying to stand against the
*  things that I find horrible when I can. Let me ask you one more absurd question. What makes you smile?
*  Well, yeah, I guess your question just did. I don't know.
*  I thought I tried that absurd one on you. Well, it was a huge honor to talk to you.
*  We'll probably talk to you for many more hours. Scott, thank you so much.
*  Well, thank you. Thank you. It was great.
*  Thank you for listening to this conversation with Scott Aronson. And thank you to our
*  presenting sponsor, Cash App. Download it, use code LEXPODCAST, you'll get $10, and $10 will go
*  to FIRST, an organization that inspires and educates young minds to become science and
*  technology innovators of tomorrow. If you enjoy this podcast, subscribe on YouTube, give it five
*  stars on Apple Podcasts, support it on Patreon, or simply connect with me on Twitter at Lex Friedman.
*  Now, let me leave you with some words from a funny and insightful blog post Scott wrote over 10 years
*  ago on the ever-present Malthusianisms in our daily lives. Quote, again and again, I've undergone
*  the humbling experience of first lamenting how badly something sucks, then only much later having
*  the crucial insight that it's not sucking wouldn't have been a Nash equilibrium.
*  Thank you for listening. I hope to see you next time.

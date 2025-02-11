---
Date Generated: October 31, 2024
Transcription Model: whisper medium 20231117
Length: 7232s
Video Keywords: ['matt botvinick', 'artificial intelligence', 'agi', 'ai', 'ai podcast', 'artificial intelligence podcast', 'lex fridman', 'lex podcast', 'lex mit', 'lex ai', 'lex jre', 'mit ai']
Video Views: 169809
Video Rating: None
Video Description: Matt Botvinick is the Director of Neuroscience Research at DeepMind. He is a brilliant cross-disciplinary mind navigating effortlessly between cognitive psychology, computational neuroscience, and artificial intelligence.

Support this podcast by supporting our sponsors:
- The Jordan Harbinger Show: https://www.jordanharbinger.com/lex
- Magic Spoon: https://magicspoon.com/lex and use code LEX at checkout

EPISODE LINKS:
Matt's papers: https://scholar.google.com/citations?user=eM916YMAAAAJ

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
3:29 - How much of the brain do we understand?
14:26 - Psychology
22:53 - The paradox of the human brain
32:23 - Cognition is a function of the environment
39:34 - Prefrontal cortex
53:27 - Information processing in the brain
1:00:11 - Meta-reinforcement learning
1:15:18 - Dopamine
1:19:01 - Neuroscience and AI research
1:23:37 - Human side of AI
1:39:56 - Dopamine and reinforcement learning
1:53:07 - Can we create an AI that a human can love?

CONNECT:
- Subscribe to this YouTube channel
- Twitter: https://twitter.com/lexfridman
- LinkedIn: https://www.linkedin.com/in/lexfridman
- Facebook: https://www.facebook.com/LexFridmanPage
- Instagram: https://www.instagram.com/lexfridman
- Medium: https://medium.com/@lexfridman
- Support on Patreon: https://www.patreon.com/lexfridman
---

# Matt Botvinick Neuroscience, Psychology, and AI at DeepMind  Lex Fridman Podcast #106
**Lex Fridman:** [July 03, 2020](https://www.youtube.com/watch?v=3t06ajvBtl0)
*  The following is a conversation with Matt Botmanek, Director of Neuroscience Research
*  at DeepMind. He's a brilliant cross-disciplinary mind navigating effortlessly between cognitive
*  psychology, computational neuroscience, and artificial intelligence. Quick summary of the
*  ads. Two sponsors, The Jordan Harbinger Show and Magic Spoon Cereal. Please consider supporting
*  the podcast by going to jordanharmiger.com slash Lex and also going to magicspoon.com slash Lex
*  and using code Lex at checkout after you buy all of their cereal. Click the links, buy the stuff.
*  It's the best way to support this podcast and the journey I'm on. If you enjoy this podcast,
*  subscribe on YouTube, review it with 5 stars on Apple podcast, follow on Spotify, support on
*  Patreon, or connect with me on Twitter at Lex Friedman spelled surprisingly without the E,
*  just F-R-I-D-M-A-N. As usual, I'll do a few minutes of ads now and never any ads in the middle that
*  can break the flow of the conversation. This episode is supported by The Jordan Harbinger Show.
*  Go to jordanharmiger.com slash Lex. It's how he knows I sent you. On that page, subscribe to this
*  podcast, on Apple podcast, Spotify, and you know where to look. I've been binging on his podcast.
*  Jordan is a great interviewer and even a better human being. I recently listened to his conversation
*  with Jack Barsky, former sleeper agent for the KGB in the 80s and author of Deep Undercover,
*  which is a memoir that paints yet another interesting perspective on the Cold War era.
*  I've been reading a lot about the Stalin and then Gorbachev and Putin eras of Russia,
*  but this conversation made me realize that I need to do a deep dive into the Cold War era
*  to get a complete picture of Russia's recent history. Again, go to jordanharmiger.com slash Lex.
*  Subscribe to this podcast. It's how he knows I sent you. It's awesome. You won't regret it.
*  This episode is also supported by Magic Spoon. Low carb, keto friendly, super amazingly delicious
*  cereal. I've been on a keto or very low carb diet for a long time now. It helps with my mental
*  performance. It helps with my physical performance even during this crazy push up pull up challenge
*  I'm doing, including the running. It just feels great. I used to love cereal. Obviously, I can't
*  have it now because most cereals have a crazy amount of sugar, which is terrible for you.
*  I quit it years ago, but Magic Spoon amazingly somehow is a totally different thing. Zero sugar,
*  11 grams of protein, and only three net grams of carbs. It tastes delicious. It has a lot of
*  flavors, two new ones, including peanut butter. If you know what's good for you, you'll go with
*  cocoa. My favorite flavor and the flavor of champions. Click the magic spoon.com slash
*  Lex link in the description and use code Lex at checkout for free shipping and to let them know
*  I sent you. They have agreed to sponsor this podcast for a long time. They're an amazing sponsor
*  and an even better cereal. I highly recommend it. It's delicious. It's good for you. You won't
*  regret it. Now, here's my conversation with Matt Botpenick. How much of the human brain
*  do you think we understand? I think we're at a weird moment in the history of neuroscience in
*  the sense that I feel like we understand a lot about the brain at a very high level,
*  but a very, very coarse level. When you say high level, what are you thinking? Are you thinking
*  functional? Are you thinking structurally? In other words, what is the brain for? What kinds
*  of computation does the brain do? What kinds of behaviors would we have to explain if we were
*  going to look down at the mechanistic level? At that level, I feel like we understand much,
*  much more about the brain than we did when I was in high school. It's almost like we're seeing it
*  through a fog. It's only at a very coarse level. We don't really understand what the neuronal
*  mechanisms are that underlie these computations. We've gotten better at saying what are the
*  functions that the brain is computing that we would have to understand if we were going to get
*  down to the neuronal level. At the other end of the spectrum, in the last few years, incredible
*  progress has been made in terms of technologies that allow us to actually literally see in some
*  cases what's going on at the single unit level, even the dendritic level. Then there's this
*  yawning gap in between. That's interesting. At the high level, that's almost a cognitive science
*  level. Then at the neuronal level, that's neurobiology and neuroscience, just studying
*  single neurons, the synaptic connections and all the dopamine, all the neurotransmitters.
*  One blanket statement I should probably make is that as I've gotten older, I have become more and
*  more reluctant to make a distinction between psychology and neuroscience. To me, the point
*  of neuroscience is to study what the brain is for. If you're a nephrologist and you want to
*  learn about the kidney, you start by saying, what is this thing for? Well, it seems to be for
*  taking blood on one side that has metabolites in it that shouldn't be there, sucking them out of
*  the blood while leaving the good stuff behind, and then excreting that in the form of urine.
*  That's what the kidney is for. It's obvious. The rest of the work is deciding how it does that.
*  This, it seems to me, is the right approach to take to the brain. You say, well, what is the brain
*  for? The brain, as far as I can tell, is for producing behavior. It's for going from perceptual
*  inputs to behavioral outputs, and the behavioral outputs should be adaptive. That's what psychology
*  is about. It's about understanding the structure of that function. Then the rest of neuroscience
*  is about figuring out how those operations are actually carried out at a mechanistic level.
*  That's really interesting. Unlike the kidney, the brain, the gap between the electrical signal
*  and behavior, you truly see neuroscience as the science that touches behavior, how the brain
*  generates behavior, or how the brain converts raw visual information into understanding.
*  Again, you basically see cognitive science, psychology, and neuroscience as all one science.
*  It's a personal statement. I don't mean to- Is that a hopeful or realistic statement? Certainly,
*  you will be correct in your feeling in some number of years, but that number of years could be
*  200, 300 years from now. Is that aspirational or is that pragmatic engineering feeling that you have?
*  It's both in the sense that this is what I hope and expect will bear fruit over the coming decades,
*  but it's also pragmatic in the sense that I'm not sure what we're doing in either psychology
*  or neuroscience if that's not the framing. I don't know what it means to understand
*  the brain if part of the enterprise is not about understanding the behavior that's being produced.
*  I would compare it to maybe astronomers looking at the movement of the planets and the stars
*  and without any interest of the underlying physics. I would argue that at least in the early days,
*  there is some value to just tracing the movement of the planets and the stars without thinking
*  about the physics too much because it's such a big leap to start thinking about the physics
*  before you even understand even the basic structural elements of-
*  Oh, I agree with that. I agree.
*  You're saying in the end, the goal should be to deeply understand.
*  Well, right. I thought about this a lot when I was in grad school because a lot of what I studied in
*  grad school was psychology. I found myself a little bit confused about what it meant to-
*  It seems like what we were talking about a lot of the time were virtual causal mechanisms like,
*  oh, well, attentional selection then selects some object in the environment and that is then
*  passed on to the motor. Information about that is passed on to the motor system.
*  But these are virtual mechanisms. They're metaphors. There's no reduction going on in
*  that conversation to some physical mechanism which is really what it would take to fully
*  understand how behavior is arising. The causal mechanisms are definitely neurons interacting.
*  I'm willing to say that at this point in history. In psychology, at least for me personally, there
*  was this strange insecurity about trafficking in these metaphors which were supposed to explain
*  the function of the mind. If you can't ground them in physical mechanisms, then what is the
*  explanatory validity of these explanations? I managed to soothe my own nerves by thinking about
*  the history of genetics research. I'm very far from being an expert on
*  the history of this field. I know enough to say that Mendelian genetics preceded
*  Watson and Crick. There was a significant period of time during which people were
*  productively investigating the structure of inheritance using what was essentially a metaphor,
*  the notion of a gene. Genes do this and genes do that. But we're the genes. There's an
*  explanatory thing that we made up and we ascribe to them these causal properties. There's a dominant,
*  there's a recessive, and then they recombine it. Then later, there was a kind of a
*  and then later, there was a kind of blank there that was filled in with a physical mechanism.
*  That connection was made. But it was worth having that metaphor because that gave us
*  a good sense of what kind of causal mechanism we were looking for.
*  And the fundamental metaphor of cognition, you said, is the interaction of neurons.
*  Is that, what is the metaphor? No, no, the metaphors we use in cognitive psychology are
*  things like attention, the way that memory works. I retrieve something from memory.
*  A memory retrieval occurs. What is that? That's not a physical mechanism that I can
*  examine in its own right. But it's still worth having that metaphorical level.
*  Yeah, I misunderstood actually. The higher level abstractions is the metaphor that's most useful.
*  What about, how does that connect to the idea that that arises from interaction of neurons?
*  Well, even is the interaction of neurons also not a metaphor to you? Or is it literally,
*  that's no longer a metaphor. That's already the lowest level of abstractions that could actually
*  be directly studied. Well, I'm hesitating because I think
*  what I want to say could end up being controversial. So what I want to say is, yes,
*  the interactions of neurons, that's not metaphorical. That's a physical fact.
*  That's where the causal interactions actually occur. Now, I suppose you could say, well,
*  even that is metaphorical relative to the quantum events that underlie. I don't want to go down that
*  rabbit hole. It's always turtles on top of turtles. Yeah, it's all the way down.
*  There is a reduction that you can do. You can say these psychological phenomena
*  are, can be explained through a very different kind of causal mechanism,
*  which has to do with neurotransmitter release. And so what we're really trying to do in neuroscience
*  large, as I say, which for me includes psychology, is to take these psychological phenomena
*  and map them onto neural events. I think remaining forever at the level of
*  description that is natural for psychology, for me personally would be disappointing. I
*  want to understand how mental activity arises from neural activity. But the converse is also true.
*  Studying neural activity without any sense of what you're trying to explain to me feels like
*  at best roping around at random. Now, you've kind of talked about this
*  bridging of the gap between psychology and neuroscience, but do you think it's possible?
*  My love is, I fell in love with psychology and psychiatry in general with Freud when I was
*  really young and I hoped to understand the mind. And for me, understanding the mind,
*  at least at a young age before I discovered AI and even neuroscience, was to psychology.
*  And do you think it's possible to understand the mind without getting into all the messy details of
*  neuroscience? Like you kind of mentioned to you, it's appealing to try to understand the
*  mechanisms at the lowest level, but do you think that's needed, that's required to understand how
*  the mind works? That's an important part of the whole picture, but I would be the last person on
*  earth to suggest that that reality renders psychology in its own right unproductive.
*  I trained as a psychologist. I am fond of saying that I have learned much more from
*  psychology than I have from neuroscience. To me, psychology is a hugely important discipline.
*  And one thing that warms in my heart is that
*  ways of investigating behavior that have been native to cognitive psychology since it's
*  you know, dawn in the sixties, are starting to become interesting to AI researchers for a variety
*  of reasons. And that's been exciting for me to see.
*  Can you maybe talk a little bit about what you see as beautiful aspects of psychology,
*  maybe limiting aspects of psychology? I mean, maybe just start it off as a science, as a field.
*  To me, when I understood what psychology is, analytical psychology, like the way it's actually
*  carried out, it was really disappointing to see two aspects. One is how small the N is, how small the
*  number of subjects is in the studies. And two, it was disappointing to see how controlled the entire,
*  how much it was in the lab. It wasn't studying humans in the wild. There was no mechanism for
*  studying humans in the wild. So that's where I became a little bit disillusioned to psychology.
*  And then the modern world of the internet is so exciting to me. The Twitter data or YouTube data,
*  data of human behavior on the internet becomes exciting because the N grows and then in the wild
*  grows. But that's just my narrow sense. Do you have an optimistic or pessimistic, cynical view
*  of psychology? How do you see the field broadly? When I was in graduate school, it was early
*  enough that there was still a thrill in seeing that there were ways of doing experimental science
*  that provided insight to the structure of the mind. One thing that impressed me most when I was
*  at that stage in my education was neuropsychology, looking at analyzing the behavior of populations
*  who had brain damage of different kinds and trying to understand what the specific deficits were
*  that arose from a lesion in a particular part of the brain. And the kind of experimentation that
*  was done and that's still being done to get answers in that context was so creative and it was so
*  deliberate. It was good science. An experiment answered one question but raised another and
*  somebody would do an experiment that answered that question and you really felt like you were
*  narrowing in on some kind of approximate understanding of what this part of the brain
*  was for. Do you have an example from memory of what kind of aspects of the mind could be studied
*  in this kind of way? Oh, sure. I mean, the very detailed neuropsychological studies that we did
*  very detailed neuropsychological studies of language function, looking at production and
*  reception and the relationship between visual function, reading and auditory and semantic.
*  And still are these beautiful models that came out of that kind of research that really made you
*  feel like you understood something that you hadn't understood before about how language
*  processing is organized in the brain. But having said all that, I think you are,
*  I mean, I agree with you that the cost of doing highly controlled experiments is that you,
*  by construction, miss out on the richness and complexity of the real world.
*  One thing that, so I was drawn into science by what in those days was called connectionism,
*  which is of course, what we now call deep learning. And at that point in history,
*  neural networks were primarily being used in order to model human cognition. They weren't
*  yet really useful for industrial applications. So you always found neural networks in biological
*  form beautiful. Oh, neural networks were very concretely the thing that drew me into science.
*  I was handed, are you familiar with the PDP books from the 80s? I went to medical school before I
*  went into science. Really? Interesting. Wow. I also did a graduate degree in art history. So
*  I'm kind of exploring. Well, art history, I understand. That's just a curious creative
*  mind. But medical school, what the dream of what, if we take that slight tangent,
*  did you want to be a surgeon? I actually was quite interested in surgery. I was interested
*  in surgery and psychiatry. And I thought that must be, I must be the only person
*  on the planet who had, who was torn between those two fields. And I said exactly that to my advisor
*  in medical school who turned out, I found out later to be a famous psychoanalyst. And he said
*  to me, no, no, it's actually not so uncommon to be interested in surgery and psychiatry.
*  And he conjectured that the reason that people develop these two interests is that both fields
*  are about going beneath the surface and kind of getting into the kind of secret. I mean,
*  maybe you understand this as someone who was interested in psychoanalysis at a certain stage.
*  There's sort of a, there's a cliche phrase that people use now on, like an NPR, the secret life of
*  blankity blank. And that was part of the thrill of surgery was seeing the secret activity that's
*  inside everybody's abdomen and thorax. That's a very poetic way to connect the two
*  disciplines that are very practically speaking different from each other. That's for sure.
*  That's for sure. Yes. So how do we get onto medical school?
*  So I was in medical school and I was doing a psychiatry rotation and my kind of advisor in
*  that rotation asked me what I was interested in. And I said, well, maybe psychiatry. He said,
*  why? And I said, well, I've always been interested in how the brain works.
*  I'm pretty sure that nobody's doing scientific research that addresses my interests, which are,
*  I didn't have a word for it then, but I would have said about cognition. And he said, well,
*  I'm not sure that's true. You might be interested in these books. And he pulled down the PDP
*  books from his shelf and they were still shrink wrapped. He hadn't read them, but he handed them
*  to me. He said, you feel free to borrow these. And that was, I went back to my dorm room and I just
*  read them cover to cover and what's PDP? Parallel distributed processing, which was one of the
*  original names for deep learning. And so I apologize for the romanticized question,
*  but what, what idea in the space of neuroscience in the space of the human brain is to you the
*  most beautiful, mysterious, surprising. What, what had always fascinated me, even when I was a pretty
*  young kid, I think, was the, the, the paradox that lies in the fact that the brain is so mysterious
*  and so it seems so distant. But at the same time, it's responsible for the, the, the, the full
*  transparency of everyday life. It's the brain is literally what makes everything obvious and
*  familiar. And, and, and, and there's always one in the room with you. I used to teach when I taught
*  at Princeton, I used to teach a cognitive neuroscience course. And the very last thing I would say to the
*  students was, you know, people often, when people think of scientific inspiration, the, the metaphor
*  is often, well, look to the stars, you know, the stars will inspire you to wonder at the universe
*  and, and, you know, think about your place in it and how things work. And, and I'm all for looking
*  at the stars, but I've always been much more inspired and kind of my sense of wonder comes from
*  the, not from the distant mysterious stars, but from the extremely intimately close brain.
*  Yeah. There's something just endlessly fascinating to me about that. The, like,
*  just like you said, the, the, the one is close and yet distant in, in, in terms of our understanding
*  of it. Do you, are you also captivated by the, the fact that this very conversation is happening
*  because two brains are communicating? Yes. Exactly. The, I guess what I mean is the subjective nature
*  of the experience. If it can take a small tangent into the, the mystical of it, the consciousness
*  or, or when you're saying you're captivated by the idea of the brain, you're, are you talking
*  about specifically the mechanism of cognition or are you also just like, at least for me,
*  it's almost like paralyzing the beauty and the mystery of the fact that it creates the entirety
*  of the experience, not just the reasoning capability, but the experience. Well,
*  I definitely resonate with that, that latter thought. And I, I often find
*  discussions of artificial intelligence to be disappointingly narrow. You know, speaking as
*  someone who has always had an interest in, in, in art. Right. I was just going to go there because
*  it sounds like somebody who has an interest in art. Yeah. I mean, I, there, there, there,
*  there are many layers to, you know, to full bore human experience. And, and in some ways,
*  it's not enough to say, oh, well, don't worry. You know, we, we're talking about cognition,
*  but we'll add emotion, you know, there's, there's, there's an incredible scope to what humans go
*  through in, in every moment. And, and yes, so it's, that's part of what fascinates me is that,
*  is that our brains are producing that. But at the same time, it's so mysterious to us how,
*  we literally, our brains are literally in our heads producing this experience. And yet there,
*  and yet there's, there, it's so mysterious to us. And so, and, and the scientific challenge of
*  getting at the, the, the actual explanation for that is so overwhelming. That's just, I don't know
*  that certain people have fixations on particular questions. And that's always, that's just always
*  been mine. Yeah. I would say the poetry that is fascinating. And I'm, I'm really interested in
*  natural language as well. And when you look at artificial intelligence community, it always
*  saddens me how much, when you try to create a benchmark for the community to get together
*  around how much of the magic of language is lost when you create that benchmark, that there's
*  something we talk about experience, the, the music, the language, the wit, the something that makes a
*  rich experience, something that would be required to pass the spirit of the Turing test is lost in
*  these benchmarks. And I wonder how to get it back in. Cause it's very difficult. The moment you try
*  to do like real good rigorous science, you lose some of that magic. When you try to study cognition
*  in a rigorous scientific way, it feels like you're losing some of the magic, the, the seeing
*  cognition in a mechanistic way that AI folk at this stage in our history. Well, I agree with you,
*  but at the same time, one, one thing that I found really exciting about that first wave of,
*  of deep learning models in cognition was there was the, the fact that the people who were building
*  these models were focused on the richness and complexity of human cognition. So an early debate
*  in cognitive science, which I sort of witnessed as a grad student was about something that sounds
*  very dry, which is the formation of the past tense. But there were these two camps. One said, well,
*  the mind encodes certain rules and it also has a list of exceptions because of course, you know,
*  the rule is add ED, but that's not always what you do. So you have to have a list of exceptions. And,
*  um, and then there were the connectionists who, you know, evolved into the deep learning people
*  who said, well, you know, if you look carefully at the data, if you look at actually look at
*  corpora, like language corpora, it's, it turns out to be very rich because yes, there are, there are,
*  there's a, you know, the, there are most verbs that, and you know, you just tack on ED and then
*  there are exceptions, but there are also, there's also, there are, there are rules that, you know,
*  there's the exceptions aren't just random. They, there are certain clues to which, which,
*  which verbs should be exceptional. And then there are exceptions to the exceptions. And there was a
*  word that was kind of deployed in order to capture this, which was quasi regular. In other words,
*  there are rules, but it's, it's messy and there are, there's, there are structure even among the
*  exceptions. And, and it would be, yeah, you could try to write down, you could try to write down,
*  um, the structure in some sort of closed form, but really the right way to understand how the
*  brain is handling all this, and by the way, producing all of this is to build a deep neural
*  network and trained it on this data and see how it ends up representing all of this richness. So
*  the way that deep learning was deployed in cognitive psychology was that was the spirit of it.
*  It was about that richness. Um, and that's something that I always found very, very compelling, still do.
*  Is it, is there something especially interesting and profound to you in terms of our current deep
*  learning neural network, artificial neural network approaches and the, what, whatever we do understand
*  about the biological neural networks in our brain, is there, there's some, there's quite a few
*  differences. Are some of them to you either interesting or perhaps profound in terms of,
*  uh, in terms of, uh, the gap we might want to try to close in trying to create a human level intelligence?
*  What I would say here is something that a lot of people are saying, um, which is that, uh,
*  one seeming limitation of the systems that we're building now is that they lack the kind of
*  flexibility, um, the readiness to sort of turn on a dime when this, when the context calls for it,
*  that is so characteristic of human behavior. So is that connected to you to the, like which aspect
*  of the neural networks in our brain is that connected to, is that closer to the cognitive
*  science level of, um, now again, see like my natural inclination is to separate into three
*  disciplines of, uh, of neuroscience, cognitive science and psychology. And you've already kind
*  of shut that down by saying you're kind of see them as separate, but just to look at those layers,
*  I guess, where is there something about the lowest layer of the way the neuro neurons are
*  layer of the way the neuro neurons interact that is profound to you in terms of this difference
*  to the artificial neuron that works or is all the diff the key differences at a higher level of
*  abstraction. One thing I often think about is that, um, you know, if you take an introductory
*  computer science course and they are introducing you to the notion of Turing machines, one way of,
*  uh, articulating what the significance of a Turing machine is, is that it's a machine emulator.
*  It can emulate any other machine. Um, and that, that to me, you know, that, that,
*  that way of looking at a Turing machine, you know, really sticks with me. I think of humans as
*  maybe sharing in some of that, um, character or capacity limited. We're not Turing machines,
*  obviously, but we have the ability to adapt behaviors that are, uh, very much unlike anything
*  we've done before, but there's some basic mechanism that's implemented in our brain that
*  allows us to run, run software. But you're just in that point, you mentioned a Turing machine,
*  but nevertheless, it's fundamentally our brains are just computational devices in your view. Is
*  that what you're getting at? Like is it, I, I was a little bit unclear to this line you drew. Is,
*  is, is there any magic in there or is it just basic computation?
*  I'm happy to think of it as just basic computation, but mind you, I won't be satisfied
*  until somebody explains to me how, what the basic computations are that are leading to
*  the full richness of human cognition. I mean, it's not going to be enough for me to understand what
*  the computations are that allow people to do arithmetic or play chess. I want, I want the whole,
*  the whole, you know, the whole thing. And a small tangent, because you kind of mentioned
*  coronavirus, there's group behavior. Oh, sure. Is that, is there something interesting to your
*  search of understanding the human mind where behavior of large groups or just behavior of
*  groups is interesting, you know, seeing that as a collective mind, as a collective intelligence,
*  perhaps seeing the groups of people as a single intelligent organisms, especially
*  looking at the reinforcement learning work you've done recently.
*  Well, yeah, I can't, I can't, I mean, I, I have the, I have the, the honor of working with a lot
*  of incredibly smart people and I wouldn't want to take any credit for, for leading the way on the,
*  the multi-agent work that's come out of, out of my group or DeepMind lately, but I do find it
*  fascinating. And I mean, I think they're, you know, I think it's, it can't be debated, you know,
*  human behavior arises within communities. That just seems to me self-evident.
*  But to me, it is self-evident, but that seems to be a profound aspects of something that created,
*  that was like, if you look at like 2001 space, I'll say when the, when the monkeys touched the,
*  yeah, like that's the magical moment. I think Yvah Harari argues that the, the ability of our
*  large numbers of humans to hold an idea, to converge towards idea together, like you said,
*  shaking hands versus bumping elbows somehow converge like without even like, like without,
*  you know, without being in a room altogether, just kind of this like distributed convergence
*  towards an idea over a particular period of time seems to be fundamental to, to just every aspect
*  of our cognition, of our intelligence, because humans, I will talk about reward, but it seems
*  like we don't really have a clear objective function under which we operate, but we all kind
*  of converge towards one somehow. And that, that to me has always been a mystery that I think is
*  somehow productive for also understanding AI systems. But I guess, I guess that's the next
*  step. The first step is try to understand the mind. Well, I don't know. I mean, I think there's
*  something to the argument that, that kind of bottom, like strictly bottom up approach is
*  wrong-headed. In other words, you know, there are, there are basic phenomena that, you know,
*  you know, basic aspects of human intelligence that, you know, can only be understood in,
*  in the context of groups. I, I'm perfectly open to that. I've never been particularly
*  convinced by the notion that we should be, we should consider intelligence to in here
*  at the level of communities. I, I, I don't know why I just, I'm sort of stuck on the notion that
*  the basic unit that we want to understand is individual humans. And if, if we have to
*  understand that in the context of other humans, fine. But for me, intelligence is just, I'm
*  stubbornly, I stubbornly define it as something that is, you know, an aspect of an individual
*  human. That's just my, I don't know. I'm with you, but that's, that could be the reductionist
*  dream of a scientist because you can understand a single human. It also is very possible that
*  intelligence can only arise when there's multiple intelligences, when there's multiple sort of,
*  it's a sad thing if that's true, because it's very difficult to study. But if, if it's just one human,
*  that one human will not be homo sapien would not become that intelligent. That's a real,
*  that's a possibility. I, I, I'm with you. One thing I will say along these lines is that,
*  I think, I think a serious effort to understand human intelligence,
*  and maybe to build a human like intelligence needs to pay just as much attention to the
*  structure of the environment as to the structure of the, you know, the cognizing system, whether
*  it's a brain or an AI system. That's one thing I took away actually from my early studies with
*  the pioneers of neural network research, people like Jay McClelland and John Cohen, you know,
*  the structure of cognition is really, it's only partly a function of the,
*  the, you know, the architecture of the brain and the learning algorithms that it implements.
*  What it's really a function, what it re, what really shapes it is the interaction of those
*  things with the structure of the world in which those things are embedded, right?
*  And that's especially important for, that's made most clear in reinforcement learning where
*  simulated environment is, you can only learn as much as you can simulate. And that's what made,
*  with DeepMind made very clear with the other aspect of the environment, which is the self-play
*  mechanism of the other agent of the competitive behavior, which the other agent becomes the
*  environment essentially. And that's, I mean, one of the most exciting ideas in AI is the self-play
*  mechanism that's able to learn successfully. So there you go. There's a, there's a thing where
*  competition is essential for learning, at least in that context. So if we can step back into
*  another sort of beautiful world, which is the actual mechanics, the dirty mess of it, of the
*  human brain, is there something for people who might not know? Is there something you can comment
*  on or describe the key parts of the brain that are important for intelligence or just in general?
*  What are the different parts of the brain that you're curious about, that you've studied,
*  and that are just good to know about when you're thinking about cognition?
*  Well, my area of expertise, if I have one, is prefrontal cortex. So, you know-
*  What's that? Where do we-
*  It depends on who you ask. The technical definition is anatomical. There are parts of
*  your brain that are responsible for motor behavior, and they're very easy to identify.
*  And the region of your cerebral cortex, the sort of outer crust of your brain that lies in front
*  of those is defined as the prefrontal cortex. And when you say anatomical, sorry to interrupt,
*  so that's referring to sort of the geographic region as opposed to some kind of functional
*  definition. Exactly. So this is kind of the coward's way out. I'm telling you what the
*  prefrontal cortex is just in terms of what part of the real estate it occupies. It's the thing
*  in the front of the brain. Yeah, exactly. And in fact, the early history of
*  neuroscientific investigation of what this front part of the brain does is sort of funny to read
*  because it was really World War I that started people down this road of trying to figure out
*  what different parts of the human brain do in the sense that there were a lot of people with
*  brain damage who came back from the war with brain damage. And that provided, as tragic as that was,
*  it provided an opportunity for scientists to try to identify the functions of different brain
*  regions. And that was actually incredibly productive. But one of the frustrations that
*  neuropsychologists faced was they couldn't really identify exactly what the deficit was
*  that arose from damage to these most kind of frontal parts of the brain. It was just a very
*  difficult thing to pin down. There were a couple of neuropsychologists who identified through a
*  large amount of clinical experience and close observation, they started to put their finger
*  on a syndrome that was associated with frontal damage. Actually, one of them was a Russian
*  neuropsychologist named Luria, who students of cognitive psychology still read. And what he
*  started to figure out was that the frontal cortex was somehow involved in flexibility,
*  in guiding behaviors that required someone to override a habit or to do something unusual
*  or to change what they were doing in a very flexible way from one moment to another.
*  So focused on like new experiences. So the way your brain processes and acts in new experiences.
*  Yeah. What later helped bring this function into better focus was a distinction between
*  controlled and automatic behavior. In other literatures, this is referred to as
*  habitual behavior versus goal-directed behavior. So it's very, very clear that
*  the human brain has pathways that are dedicated to habits, to things that you do all the time.
*  And they need to be automatized so that they don't require you to concentrate too much. So
*  that leaves your cognitive capacity free to do other things. Just think about the difference
*  between driving when you're learning to drive versus driving after you're fairly expert.
*  There are brain pathways that slowly absorb those frequently performed behaviors so that they can be
*  habits, so that they can be automatic. That's kind of like the purest form of learning.
*  I guess it's happening there, which is why, I mean, this is kind of jumping ahead, which is why that
*  perhaps is the most useful for us to focusing on and trying to see how artificial intelligence
*  systems can learn. Is that the way you think? It's interesting. I do think about this distinction
*  between controlled and automatic or goal-directed and habitual behavior a lot in thinking about
*  where we are in AI research. But just to finish the kind of dissertation here, the role of the
*  prefrontal cortex is generally understood these days in contradistinction to that habitual domain.
*  In other words, the prefrontal cortex is what helps you override those habits. It's what allows
*  you to say, well, what I usually do in this situation is X, but given the context, I probably
*  should do Y. I mean, the elbow bump is a great example. Reaching out and shaking hands is
*  probably a habitual behavior. It's the prefrontal cortex that allows us to
*  bear in mind that there's something unusual going on right now. In this situation, I need to not
*  do the usual thing. The kind of behaviors that Luria reported, and he built tests for detecting
*  these kinds of things, were exactly like this. In other words, when I stick out my hand,
*  I want you instead to present your elbow. A patient with frontal damage would have a great
*  deal of trouble with that. Somebody proffering their hand would elicit a handshake. The prefrontal
*  cortex is what allows us to say, hold on, that's the usual thing, but I have the ability to bear
*  in mind even very unusual contexts and to reason about what behavior is appropriate there.
*  Just to get a sense, are us humans special in the presence of the prefrontal cortex?
*  Do mice have a prefrontal cortex? Do other mammals that we can study? If no, then how do
*  they integrate new experiences? Yeah, that's a really tricky question and a very timely question
*  because we have revolutionary new technologies for monitoring, measuring, and also causally
*  influencing neural behavior in mice and fruit flies. These techniques are not fully available
*  for studying brain function in monkeys, let alone humans. It's a very urgent question whether the
*  kinds of things that we want to understand about human intelligence can be pursued in these other
*  organisms. To put it briefly, there's disagreement. People who study fruit flies will often tell you,
*  hey, fruit flies are smarter than you think. They'll point to experiments where fruit flies
*  were able to learn new behaviors, were able to generalize from one stimulus to another
*  in a way that suggests that they have abstractions that guide their generalization.
*  I've had many conversations in which I will start by recounting some observation about mouse
*  behavior where it seemed like mice were taking an awfully long time to learn a task that for a human
*  would be profoundly trivial. I will conclude from that that mice really don't have the cognitive
*  flexibility that we want to explain. Then a mouse researcher will say to me, well, hold on,
*  that experiment may not have worked because you asked a mouse to deal with stimuli and behaviors
*  that were very unnatural for the mouse. If instead you kept the logic of the experiment the same,
*  but presented the information in a way that aligns with what mice are used to dealing with
*  in their natural habitats, you might find that a mouse actually has more intelligence than you
*  think. Then they'll go on to show you videos of mice doing things in their natural habitat,
*  which seem strikingly intelligent, dealing with physical problems. I have to drag this piece of
*  food back to my lair, but there's something in my way, and how do I get rid of that thing?
*  So I think these are open questions to sum that up.
*  LW And then taking a small step back related to that, as you mentioned, we're taking a little
*  shortcut by saying it's a geographic part of the prefrontal cortex is a region of the brain.
*  What's your sense in a bigger philosophical view, prefrontal cortex and the brain in general?
*  Do you have a sense that it's a set of subsystems in the way we've implied
*  that are pretty distinct? Or to what degree is it that? Or to what degree is it a giant
*  interconnected mess where everything does everything and it's impossible to disentangle them?
*  AC I think there's overwhelming evidence that there's functional differentiation, that it's
*  clearly not the case that all parts of the brain are doing the same thing.
*  This follows immediately from the kinds of studies of brain damage that we were chatting about before.
*  It's obvious from what you see if you stick an electrode in the brain and measure what's going
*  on at the level of neural activity. Having said that, there are two other things to add,
*  which kind of, I don't know, maybe tug in the other direction. One is that
*  when you look carefully at functional differentiation in the brain, what you usually
*  end up concluding, at least this is my observation of the literature, is that the differences between
*  regions are graded rather than being discrete. It doesn't seem like it's easy to divide the brain
*  up into true modules that have clear boundaries and that have clear channels of communication
*  between them. AC And this applies to the prefrontal cortex?
*  AC Yeah, the prefrontal cortex is made up of a bunch of different subregions,
*  the functions of which are not clearly defined and the borders of which seem to be quite vague.
*  Then there's another thing that's popping up in very recent research, which involves application
*  of these new techniques. There are a number of studies that suggest that parts of the brain
*  that we would have previously thought were quite focused in their function are actually
*  carrying signals that we wouldn't have thought would be there. For example,
*  looking in the primary visual cortex, which is classically thought of as
*  basically the first cortical way station for processing visual information. Basically,
*  what it should care about is where are the edges in this scene that I'm viewing?
*  AC It turns out that if you have enough data,
*  you can recover information from primary visual cortex about all sorts of things,
*  like what behavior the animal is engaged in right now and how much reward is on offer in the task
*  that it's pursuing. It's clear that even regions whose function is pretty well defined at a coarse
*  grain are nonetheless carrying some information from very different domains.
*  The history of neuroscience is this oscillation between the two views that you articulated,
*  the modular view and then the big mush view. I guess we're going to end up somewhere in the
*  middle, which is unfortunate for our understanding because there's something about our conceptual
*  system that finds it easy to think about a modularized system and easy to think about
*  a completely undifferentiated system. Something that lies in between is confusing,
*  but we're going to have to get used to it, I think.
*  LL We can understand deeply the lower level mechanism of neuronal communication.
*  AC Yeah.
*  LL On that topic, you mentioned information. Just to get a sense, I imagine something that
*  there's still mystery and disagreement on is how does the brain carry information and signal?
*  What in your sense is the basic mechanism of communication in the brain?
*  AC Well, I guess I'm old fashioned in that I consider the networks that we use in deep
*  learning research to be a reasonable approximation to the mechanisms that carry information in the
*  brain. The usual way of articulating that is to say what really matters is a rate code. What
*  matters is how quickly is an individual neuron spiking? What's the frequency at which it's
*  spiking? Is it right? LL
*  So the timing of the spike. AC
*  Yeah. Is it firing fast or slow? Let's put a number on that, and that number is enough to
*  capture what neurons are doing. There's still uncertainty about whether that's an adequate
*  description of how information is transmitted within the brain. There are studies that suggest
*  that the precise timing of spikes matters. There are studies that suggest that there are
*  computations that go on within the dendritic tree, within a neuron, that are quite rich and
*  structured and that really don't equate to anything that we're doing in our artificial
*  neural networks. Having said that, I feel like we're getting somewhere by sticking to this high
*  level of abstraction. LL
*  Just the rate, and by the way, we're talking about the electrical signal. I remember reading some
*  vague paper somewhere recently where the mechanical signal, like the vibrations or something
*  of the neurons also communicates information. AC
*  I haven't seen that, but... LL
*  So somebody was arguing that the electrical signal, this is in a Nature paper or something
*  like that, where the electrical signal is actually a side effect of the mechanical signal. But I
*  don't think that changes the story, but it's almost an interesting idea that there could be
*  a deeper... It's always like in physics with quantum mechanics, there's always a deeper story
*  that could be underlying the whole thing. But you think it's basically the rate of spiking
*  that gets us... That's like the lowest hanging fruit that can get us really far.
*  AC This is a classical view. The only way in which this
*  stance would be controversial is in the sense that there are members of the neuroscience community
*  who are interested in alternatives, but this is really a very mainstream view. The way that
*  neurons communicate is that neurotransmitters arrive, they wash up on a neuron, the neuron has
*  receptors for those transmitters, the meeting of the transmitter with these receptors changes the
*  voltage of the neuron, and if enough voltage change occurs, then a spike occurs, one of these
*  discrete events. It's that spike that is conducted down the axon and leads to neurotransmitter
*  release. This is just like neuroscience 101. This is the way the brain is supposed to work.
*  Now, what we do when we build artificial neural networks of the kind that are now popular in the
*  AI community is that we don't worry about those individual spikes, we just worry about the frequency
*  at which those spikes are being generated. People talk about that as the activity of a neuron.
*  The activity of units in a deep learning system is broadly analogous to the spike rate of a neuron.
*  There are people who believe that there are other forms of communication in the brain. In fact,
*  I've been involved in some research recently that suggests that the voltage fluctuations that occur
*  in populations of neurons that are below the level of spike production may be important for
*  communication. I'm still pretty old school in the sense that I think that the things that we're
*  building in AI research constitute reasonable models of how a brain would work. Let me ask just
*  for fun a crazy question because I can. Do you think it's possible we're completely wrong about
*  this basic mechanism of neuronal communication that information is stored in some very different
*  kind of way in the brain? Oh, heck yes. Look, I wouldn't be a scientist if I didn't think there
*  was any chance we were wrong. If you look at the history of deep learning research as it's been
*  applied to neuroscience, of course, the vast majority of deep learning research these days
*  isn't about neuroscience. If you go back to the 1980s, there's an unbroken chain of research
*  in which a particular strategy is taken, which is, hey, let's train a deep learning system. Let's
*  train a multi-layered neural network on this task that we trained our rat on or our monkey on
*  or this human being on. Then let's look at what the units deep in the system are doing.
*  Let's ask whether what they're doing resembles what we know about what neurons deep in the brain
*  are doing. Over and over and over and over, that strategy works in the sense that the learning
*  algorithms that we have access to, which typically center on back propagation, they give rise to
*  patterns of activity, patterns of response, patterns of neuronal behavior in these artificial
*  models that look hauntingly similar to what you see in the brain. Is that a coincidence?
*  At a certain point, it starts looking like such coincidence is unlikely to not be deeply meaningful.
*  The circumstantial evidence is overwhelming.
*  But you're always open to a total flipping at the table.
*  Of course.
*  You have co-authored several recent papers that weave beautifully between the world of
*  neuroscience and artificial intelligence. Maybe if we could, can we just try to dance around and
*  talk about some of them, maybe try to pick out interesting ideas that jump to your mind
*  from memory. Maybe looking at, we're talking about the prefrontal cortex, the 2018, I believe, paper
*  called the prefrontal cortex as a meta reinforcement learning system.
*  Is there a key idea that you can speak to from that paper?
*  Yeah. The key idea is about meta-learning.
*  What is meta-learning?
*  Meta-learning is, by definition, a situation in which you have a learning algorithm
*  and the learning algorithm operates in such a way that it gives rise to another learning algorithm.
*  In the earliest applications of this idea, you had one learning algorithm adjusting the parameters
*  on another learning algorithm. But the case that we're interested in this paper is one where
*  you start with just one learning algorithm and then another learning algorithm emerges out of
*  thin air. I can say more about what I mean by that. I don't mean to be
*  conspiracy theorists, but that's the idea of meta-learning. It relates to the old idea in
*  psychology of learning to learn. Situations where you have experiences that make you better at
*  learning something new. A familiar example would be learning a foreign language. The first time you
*  learn a foreign language, it may be quite laborious and disorienting and novel. But let's
*  say you've learned two foreign languages. The third foreign language, obviously, is going to
*  be much easier to pick up. Why? Because you've learned how to learn. You know how this goes.
*  I'm going to have to learn how to conjugate. That's a simple form of meta-learning in the
*  sense that there's some slow learning mechanism that's helping you update your fast learning
*  mechanism. That makes sense. From our understanding from the psychology world, from neuroscience,
*  our understanding how meta-learning works might work in the human brain. What lessons can we
*  draw from that that we can bring into the artificial intelligence world?
*  Well, yeah. The origin of that paper was in AI work that we were doing in my group.
*  We were looking at what happens when you train a recurrent neural network using standard
*  reinforcement learning algorithms. But you train that network not just in one task, but you train
*  it in a bunch of interrelated tasks. Then you ask what happens when you give it yet another task
*  in that line of interrelated tasks. What we started to realize is that
*  a form of meta-learning spontaneously happens in recurrent neural networks.
*  The simplest way to explain it is to say a recurrent neural network has a memory
*  in its activation patterns. It's recurrent by definition in the sense that you have
*  units that connect to other units that connect to other units. You have loops of connectivity,
*  which allows activity to stick around and be updated over time. In psychology,
*  in neuroscience, we call this working memory. It's like actively holding something in mind.
*  That memory gives the recurrent neural network dynamics. The way that the activity pattern
*  evolves over time is inherent to the connectivity of the recurrent neural network.
*  That's idea number one. Now, the dynamics of that network are shaped by the connectivity,
*  by the synaptic weights. Those synaptic weights are being shaped by this reinforcement learning
*  algorithm that you're training the network with. The punchline is if you train a recurrent neural
*  network with a reinforcement learning algorithm that's adjusting its weights,
*  and you do that for long enough, the activation dynamics will become very interesting.
*  Imagine I give you a task where you have to press one button or another, left button or right button.
*  There's some probability that I'm going to give you an M&M if you press the left button,
*  and there's some probability I'll give you an M&M if you press the other button.
*  You have to figure out what those probabilities are just by trying things out.
*  As I said before, instead of just giving you one of these tasks, I give you a whole sequence.
*  I give you two buttons, and you figure out which one's best, and I go, good job, here's a new box.
*  Two new buttons, you have to figure out which one's best. Good job, here's a new box.
*  Every box has its own probabilities, and you have to figure it. If you train a recurrent neural
*  network on that kind of sequence of tasks, what happens, it seemed almost magical to us when we
*  first started realizing what was going on. The slow learning algorithm that's adjusting the
*  synaptic weights, those slow synaptic changes give rise to a network dynamics that themselves
*  turn into a learning algorithm. In other words, you can tell this is happening by just freezing
*  the synaptic weights, saying, okay, no more learning, you're done. Here's a new box.
*  Figure out which button is best, and the recurrent neural network will do this just fine.
*  It figures out which button is best. It kind of transitions from exploring the two buttons to just
*  pressing the one that it likes best in a very rational way. How is that happening? It's happening
*  because the activity dynamics of the network have been shaped by this slow learning process
*  that's occurred over many, many boxes. What's happened is that this slow learning algorithm
*  that's slowly adjusting the weights is changing the dynamics of the network, the activity dynamics,
*  into its own learning algorithm. As we were realizing that this is a thing,
*  it just so happened that the group that was working on this included a bunch of neuroscientists,
*  it started ringing a bell for us, which is to say that we thought, this sounds a lot like the
*  distinction between synaptic memory and activity-based memory in the brain.
*  It also reminded us of recurrent connectivity that's very characteristic of prefrontal function.
*  This is why it's good to have people working on AI that know a little bit about neuroscience
*  and vice versa, because we started thinking about whether we could apply this
*  principle to neuroscience. That's where the paper came from.
*  The kind of principle of the recurrence they can see in the prefrontal cortex,
*  then you start to realize that it's possible for something like an idea of a learning to learn
*  emerging from this learning process, as long as you keep varying the environment sufficiently.
*  Exactly. The kind of metaphorical transition we made to neuroscience was to think, okay,
*  well, we know that the prefrontal cortex is highly recurrent. We know that it's an important locus
*  for working memory, for activation-based memory. Maybe the prefrontal cortex supports reinforcement
*  learning. In other words, what is reinforcement learning? You take an action, you see how much
*  reward you got, you update your policy of behavior. Maybe the prefrontal cortex is doing that sort of
*  thing strictly in its activation patterns. It's keeping around a memory in its activity patterns
*  of what you did, how much reward you got, and it's using that activity-based memory as a basis for
*  updating behavior. Then the question is, well, how did the prefrontal cortex get so smart? In
*  other words, where did these activity dynamics come from? How did that program that's implemented
*  in the recurrent dynamics of the prefrontal cortex arise? One answer that became evident in this work
*  was, well, maybe the mechanisms that operate on the synaptic level, which we believe are mediated
*  by dopamine, are responsible for shaping those dynamics. This may be a silly question, but
*  because this kind of several temporal classes of learning are happening and the learning to learn
*  is emerges, can you keep building stacks of learning to learn to learn, learning to learn to
*  learn to learn to learn to learn? Because it keeps, I mean, basically abstractions of more powerful
*  abilities to generalize of learning complex rules. Is this over-stretching this kind of mechanism?
*  One of the people in AI who started thinking about meta-learning from very early on, Jürgen
*  Schmidt Huber, cheekily suggested, I think it may have been in his PhD thesis, that we should think
*  about meta-meta-meta-meta-meta-meta-learning. That's really what's going to get us to true
*  intelligence. Certainly there's a poetic aspect to it and it seems interesting and correct that
*  that kind of levels of abstraction will be powerful, but is that something you see in the brain?
*  This kind of, is it useful to think of learning in these meta-meta-meta-meta way or is it just
*  meta-learning? Well, one thing that really fascinated me about this
*  mechanism that we were starting to look at and other groups started talking about very similar
*  things at the same time and then a kind of explosion of interest in meta-learning happened
*  in the AI community shortly after that. I don't know if we had anything to do with that, but
*  I was gratified to see that a lot of people started talking about meta-learning.
*  One of the things that I like about the kind of flavor of meta-learning that we were studying
*  was that it didn't require anything special. It was just if you took a system that had some
*  form of memory that the function of which could be shaped by pick your RL algorithm,
*  then this would just happen. There are a lot of forms of, there are a lot of meta-learning
*  algorithms that have been proposed since then that are fascinating and effective in their
*  domains of application, but they're engineered. There are things that somebody had to say,
*  well, gee, if we wanted meta-learning to happen, how would we do that? Here's an algorithm that
*  would, but there's something about the kind of meta-learning that we were studying that seemed
*  to me special in the sense that it wasn't an algorithm. It was just something that automatically
*  happened if you had a system that had memory and it was trained with a reinforcement learning
*  algorithm. In that sense, it can be as meta as it wants to be. There's no limit on how abstract
*  the meta-learning can get because it's not reliant on a human engineering a particular meta-learning
*  algorithm to get there. I also, I don't know, I guess I hope that that's relevant in the brain,
*  I think there's a kind of beauty in the ability of this emergent.
*  The emergent aspect of it. Yeah, it's something that-
*  As opposed to engineered. Exactly. It's something that just,
*  it just happens in a sense. In a sense, you can't avoid this happening. If you have a system that
*  has memory and the function of that memory is shaped by reinforcement learning and this system
*  is trained in a series of interrelated tasks, this is going to happen. You can't stop it.
*  As long as you have certain properties, maybe like a recurrent structure to-
*  You have to have memory. It actually doesn't have to be a recurrent neural network. A paper
*  that I was honored to be involved with even earlier used a kind of slot-based memory.
*  Do you remember the title? Just for people to understand.
*  It was Memory Augmented Neural Networks. I think the title was
*  Meta-Learning in Memory Augmented Neural Networks. It was the same exact story.
*  If you have a system with memory, here it was a different kind of memory,
*  but the function of that memory is shaped by reinforcement learning. Here it was the reads
*  and writes that occurred on this slot-based memory. This will just happen. This brings us back to
*  something I was saying earlier about the importance of the environment. This will happen if the system
*  is being trained in a setting where there's a sequence of tasks that all share some abstract
*  structure. Sometimes we talk about task distributions. That's something that's
*  very obviously true of the world that humans inhabit. If you just think about what you do every
*  day, you never do exactly the same thing that you did the day before, but everything that you do
*  has a family resemblance. It shares a structure with something that you did before.
*  The real world is saturated with this property. It's endless variety with endless redundancy.
*  That's the setting in which this kind of meta-learning happens.
*  We're just so good at finding, just like in this emergent
*  phenomenon you described, we're really good at finding that redundancy, finding those similarities,
*  the family resemblance. Some people call it, Melanie Mitchell was talking about analogies,
*  so we're able to connect concepts together in this kind of way, in this same kind of automated,
*  emergent way. There's so many echoes here of psychology and neuroscience and obviously now
*  with reinforcement learning with recurrent neural networks at the core.
*  If we could talk a little bit about dopamine, you're a part of co-authoring a really exciting
*  recent paper, very recent, in terms of release on dopamine and temporal difference learning.
*  Can you describe the key ideas of that paper? Sure. One thing I want to pause to do is
*  acknowledge my co-authors on actually both of the papers we're talking about. This dopamine paper-
*  Just to, I'll certainly post all their names.
*  Okay, wonderful. Yeah, because I'm sort of a bashed to be the spokesperson for these papers when
*  I had such amazing collaborators on both. It's a comfort to me to know that you'll acknowledge them.
*  Yeah, this is an incredible team there, but yeah.
*  Oh yeah, it's so much fun. In the case of the dopamine paper, we also collaborate with Nauchi
*  to Harvard, who obviously a paper simply wouldn't have happened without him.
*  You were asking for a thumbnail sketch of- Yeah, thumbnail sketch or key ideas or things,
*  the insights that continue on our discussion here between neuroscience and AI.
*  Yeah, I mean, this was another, a lot of the work that we've done so far is
*  taking ideas that have bubbled up in AI and asking the question of whether the brain might
*  be doing something related, which I think on the surface sounds like something that's really mainly
*  of use to neuroscience. We see it also as a way of validating what we're doing on the AI side.
*  If we can gain some evidence that the brain is using some technique that we've been trying out
*  in our AI work, that gives us confidence that it may be a good idea, that it'll scale to
*  rich complex tasks, that it'll interface well with other mechanisms.
*  So you see it as a two-way road. Yeah, for sure.
*  Just because a particular paper is a little bit focused on from AI from neural networks to
*  neuroscience, ultimately the discussion, the thinking, the productive long-term aspect of
*  it is the two-way road nature of the whole- Yeah, I mean, we've talked about the notion of a virtuous
*  circle between AI and neuroscience. The way I see it, that's always been there since the two fields
*  jointly existed. There have been some phases in that history when AI was ahead. There are some
*  phases when neuroscience was ahead. I feel like given the burst of innovation that's happened
*  recently on the AI side, AI is ahead in the sense that there are all of these ideas for which it's
*  exciting to consider that there might be neural analogs. Neuroscience, in a sense, has been
*  focusing on approaches to studying behavior that are derived from this earlier era of cognitive
*  psychology and in some ways fail to connect with some of the issues that we're grappling with in AI,
*  how do we deal with large complex environments? I think it's inevitable that this circle will
*  keep turning and there will be a moment in the not too distant future when neuroscience is
*  pelting AI researchers with insights that may change the direction of our work.
*  Just a quick human question. You have parts of your brain, this is very meta, but they're able
*  to both think about neuroscience and AI. I don't often meet people like that. Let me ask a meta
*  plasticity question. Do you think a human being can be both good at AI and neuroscience? On the
*  deep mind, what kind of human can occupy these two realms? Is that something you see everybody
*  should be doing, can be doing, or is it a very special few can jump? Just like we talk about
*  art history, I would think it's a special person that can major in art history and also consider
*  being a surgeon. Otherwise known as a dilettante. A dilettante, yeah. Easily distracted.
*  I think it does take a special kind of person to be truly world class at both AI and neuroscience,
*  and I am not on that list. I happen to be someone whose interest in neuroscience and psychology
*  involved using the kinds of modeling techniques that are now very central in AI.
*  That sort of, I guess, bought me a ticket to be involved in all of the amazing things that are
*  going on in AI research right now. I do know a few people who I would consider pretty expert on both
*  fronts, and I won't embarrass them by naming them, but there are exceptional people out there
*  who are like this. The one thing that I find is a barrier to being truly world class on both fronts
*  is just the complexity of the technology that's involved in both disciplines now.
*  The engineering expertise that it takes to do truly front line, hands on AI research
*  is really, really considerable. The learning curve of the tools,
*  just like the specifics of just whether it's programming or the kind of tools necessary to
*  collect the data, to manage the data, to distribute, to compute, all that kind of stuff.
*  On the neuroscience side, there would be all different sets of tools.
*  Exactly, especially with the recent explosion in neuroscience methods.
*  Having said all that, I think the best scenario for both neuroscience and AI is to have people
*  who are interacting who live at every point on this spectrum from exclusively focused on neuroscience
*  to exclusively focused on the engineering side of AI. But to have those people inhabiting a community
*  where they're talking to people who live elsewhere on the spectrum. I may be someone who's very close
*  to the center in the sense that I have one foot in the neuroscience world and one foot in the AI
*  world. That central position, I will admit, prevents me, at least someone with my limited
*  cognitive capacity, from having true technical expertise in either domain. But at the same time,
*  I at least hope that it's worthwhile having people around who can see the connections.
*  Yeah, the community, the emergent intelligence of the community when it's nicely distributed
*  is useful. Okay. Exactly. Yeah. I've seen that work out well at DeepMind. There are people who,
*  I mean, even if you just focus on the AI work that happens at DeepMind, it's been a good thing to have
*  some people around doing that kind of work whose PhDs are in neuroscience or psychology.
*  Every academic discipline has its kind of blind spots and kind of unfortunate obsessions
*  and its metaphors and its reference points. And having some intellectual diversity is really
*  healthy. People get each other unstuck, I think. I see it all the time at DeepMind. And I like to
*  think that the people who bring some neuroscience background to the table are helping with that.
*  So one of my probably the deepest passions for me, what I would say, maybe we kind of spoke off,
*  Mike, a little bit about it, but that I think is a blind spot for at least robotics and AI folks,
*  is human-robot interaction, human-agent interaction. Maybe, do you have thoughts about how we reduce
*  the size of that blind spot? Do you also share the feeling that not enough folks are studying
*  this aspect of interaction? Well, I'm actually pretty intensively interested in this issue now.
*  And there are people in my group who've actually pivoted pretty hard over the last few years from
*  doing more traditional cognitive psychology and cognitive neuroscience to doing experimental work
*  on human-agent interaction. And there are a couple of reasons that I'm pretty passionately
*  interested in this. One is it's kind of the outcome of having thought for a few years now about
*  what we're up to. What are we doing? What is this AI research for? So what does it mean to make the
*  world a better place? I'm pretty sure that means making life better for humans.
*  And so how do you make life better for humans? That's a proposition that when you look at it
*  carefully and honestly is rather horrendously complicated, especially when the AI systems that
*  you're building are learning systems. You're not programming something that you then introduce to
*  the world and it just works as programmed, like Google Maps or something. We're building systems
*  that learn from experience. So that typically leads to AI safety questions. How do we keep
*  these things from getting out of control? How do we keep them from doing things that harm humans?
*  I hasten to say I consider those hugely important issues and there are large sectors of the research
*  community at DeepMind and of course elsewhere who are dedicated to thinking
*  hard all day every day about that. But there's I guess I would say a positive side to this too,
*  which is to say, well, what would it mean to make human life better? And how can we imagine learning
*  systems doing that? And in talking to my colleagues about that, we reached the initial conclusion that
*  it's not sufficient to philosophize about that. You actually have to take into account how humans
*  actually work and what humans want and the difficulties of knowing what humans want
*  and the difficulties that arise when humans want different things.
*  And so human-agent interaction has become a quite intensive focus of my group lately.
*  If for no other reason that in order to really address that issue in an adequate way,
*  you have to, I mean, psychology becomes part of the picture.
*  Yeah. And so there's a few elements there. So if you focus on solving,
*  if you focus on the robotics problem, let's say AGI, without humans in the picture,
*  is you're missing fundamentally the final step. When you do want to help human civilization,
*  you eventually have to interact with humans. And when you create a learning system, just as you said,
*  that will eventually have to interact with humans, the interaction itself has to become
*  part of the learning process. So you can't just watch, well, my sense is, it sounds like your sense
*  is you can't just watch humans to learn about humans. You have to also be part of the human
*  world. You have to interact with humans. Yeah, exactly. And I mean, then questions arise that
*  start imperceptibly, but inevitably to slip beyond the realm of engineering.
*  So questions like, if you have an agent that can do something that you can't do,
*  under what conditions do you want that agent to do it? So, you know, if I have a robot that can play
*  Beethoven sonatas better than any human, in the sense that the sensitivity, the expression is just
*  beyond what any human, do I want to listen to that? Do I want to go to a concert and hear a robot
*  play? These aren't engineering questions. These are questions about human preference and human
*  culture. Psychology bordering on philosophy. Yeah. And then you start asking, well, even if we knew
*  the answer to that, is it our place as AI engineers to build that into these agents? Probably the
*  agents should interact with humans beyond the population of AI engineers and figure out what
*  those humans want. And then, you know, when you start, I referred this the moment ago, but even
*  that becomes complicated. What if two humans want different things and you have only one agent
*  that's able to interact with them and try to satisfy their preferences? Then you're into the
*  realm of economics and social choice theory and even politics. So there's a sense in which, if you
*  kind of follow what we're doing to its logical conclusion, then it goes beyond questions of
*  engineering and technology and starts to shade in perceptibly into questions about
*  what kind of society do you want? And actually, once that dawned on me, I actually felt,
*  I don't know what the right word is, quite refreshed in my involvement in AI research. It's
*  almost like building this kind of stuff is going to lead us back to asking really fundamental
*  questions about what's the good life and who gets to decide? And bringing in viewpoints from
*  multiple sub-communities to help us shape the way that we live. It started making me feel like,
*  doing AI research in a fully responsible way could potentially lead to a kind of
*  cultural renewal. Yeah, it's the way to understand human beings at the individual,
*  at the societal level. It may become a way to answer all the silly human questions of the meaning
*  of life and all those kinds of things. Even if it doesn't give us a way of answering those
*  questions, it may force us back to thinking about them. It might restore a certain depth to,
*  or even dare I say spirituality to the world. I don't know, maybe that's too grandiose.
*  I'm with you. I think AI will be the philosophy of the 21st century,
*  the way which will open the door. I think a lot of AI researchers are afraid to open that door
*  of exploring the beautiful richness of the human-agent interaction, human-AI interaction. I'm
*  really happy that somebody like you have opened that door. One thing I often think about is,
*  you know, the usual schema for thinking about human-agent interaction is this kind of dystopian,
*  our robot overlords. Again, I hasten to say AI safety is hugely important. I'm not saying
*  we shouldn't be thinking about those risks. Totally on board for that. Having said that,
*  there's a... What often follows for me is the thought that there's another kind of narrative
*  that might be relevant, which is when we think of humans gaining more and more information about
*  human life, the narrative there is usually that they gain more and more wisdom. They get closer
*  to enlightenment and they become more benevolent. The Buddha is like... That's a totally different
*  narrative. Why isn't it the case that we imagine that the AI systems that we're creating, they're
*  going to figure out more and more about the way the world works and the way that humans interact
*  and they'll become beneficent. I'm not saying that will happen. I don't honestly expect that
*  to happen without some careful... Setting things up very carefully, but it's another way things
*  could go, right? Yeah. I would even push back on that. I personally believe that the
*  most trajectories, natural human trajectories will lead us towards progress. For me,
*  there is a kind of sense that most trajectories in AI development will lead us into trouble.
*  To me, and we over-focus on the worst case. It's like in computer science, theoretical computer
*  science, there's been this focus on worst case analysis. There's something appealing to our human
*  mind at some lowest level. We don't want to be eaten by the tiger, I guess. We want to do the
*  worst case analysis, but the reality is that shouldn't stop us from actually building out all
*  the other trajectories, which are potentially leading to all the positive worlds.
*  All the enlightenment. There's a book, Enlightenment Now with Steven Pinker and so on. This
*  is looking generally at human progress. There's so many ways that human progress can happen with
*  AIs. I think you have to do that research. You have to do that work. You have to do the,
*  not just the AI safety work of the one worst case analysis. How do we prevent that? But the
*  the glue and the mechanisms of human AI interaction that would lead to all the positive
*  interactions that can go. It's a super exciting area, right?
*  Yeah. We should be spending a lot of our time saying what can go wrong. I think it's harder
*  to see that there's work to be done to bring into focus the question of what it would look like for
*  things to go right. That's not obvious. We wouldn't be doing this if we didn't have the sense
*  there was huge potential. We're not doing this for no reason. We have a sense that AGI would be
*  a major boom to humanity, but I think it's worth starting now, even when our technology is quite
*  primitive, asking exactly what would that mean? We can start now with applications that are
*  already going to make the world a better place, like solving protein folding. I think this deep
*  mind has gotten heavy into science applications lately, which I think is a wonderful, wonderful
*  move for us to be making. But when we think about AGI, when we think about building fully
*  intelligent agents that are going to be able to innocent people, we're going to be able to
*  do whatever they want. We should start thinking about what do we want them to want? What kind of
*  world do we want to live in? That's not an easy question. I think we just need to start working
*  on it. Even on the path to AGI, it doesn't have to be AGI, but just intelligent agents that interact
*  with us and help us enrich our own existence on social networks, for example, on recommender
*  systems and various intelligence. There's so much interesting interaction that's yet to be understood
*  and studied. Twitter is struggling with this very idea of how do you create AI systems
*  that increase the quality and the health of a conversation? For sure. That's a beautiful
*  human psychology question. How do you do that without deception being involved,
*  without manipulation being involved, maximizing human autonomy? How do you make these choices
*  in a democratic way? How do we face the fact that it's a small group of people who have the
*  skill set to build these kinds of systems, but what it means to make the world a better place
*  is something that we all have to be talking about.
*  The world that we're trying to make a better place includes a huge variety of different kinds
*  of people. Yeah. How do we cope with that? This is a problem that has been discussed in gory,
*  extensive detail in social choice theory. One thing I'm really enjoying about the recent
*  direction work has taken in some parts of my team is that, yeah, we're reading the AI literature,
*  we're reading the neuroscience literature, but we've also started reading economics and,
*  as I mentioned, social choice theory, even some political theory, because it turns out that
*  it all becomes relevant. But at the same time, we've been trying not to write
*  philosophy papers. We've been trying not to write position papers. We're trying to figure out
*  ways of doing actual empirical research that take the first small steps to thinking about what it
*  really means for humans with all of their complexity and contradiction and paradox
*  to be brought into contact with these AI systems in a way that really makes the world a better
*  place. And often reinforcement learning frameworks actually allow you to do that machine learning.
*  That's the exciting thing about AI is it allows you to reduce the unsolvable problem,
*  philosophical problem into something more concrete that you can get a hold of.
*  Yeah, and it allows you to kind of define the problem in some way that allows for
*  growth in the system that's sort of, you know, you're not responsible for the details,
*  right? You say, this is generally what I want you to do. And then learning takes care of the rest.
*  Of course, the safety issues arise in that context. But I think also some of these positive
*  issues arise in that context. What would it mean for an AI system to really come to understand what
*  humans want? And, you know, with all of the subtleties of that, right? You know, humans
*  want help with certain things, but they don't want everything done for them, right? There is
*  part of the satisfaction that humans get from life is in accomplishing things. So if there were
*  devices around that did everything for me, I often think of the movie Wall-E. That's like
*  dystopian in a totally different way. It's like the machines are doing everything for us. That's
*  not what we wanted. Anyway, I find this opens up a whole landscape of research that feels affirmative.
*  To me, it's one of the most exciting and it's wide open. We have to, because it's a cool paper,
*  talk about dopamine. Oh, yeah. Okay. So I can. We were gonna, we were gonna, I was gonna give you
*  a quick summary. It's a quick summary of what's the title of the paper? I think we called it
*  a distributional code for value in dopamine-based reinforcement learning. Yes. So that's another
*  project that grew out of pure AI research. A number of people at DeepMind and a few other
*  places had started working on a new version of reinforcement learning, which was defined by
*  taking something in traditional reinforcement learning and just tweaking it. So the thing that
*  they took from traditional reinforcement learning was a value signal. So at the center of reinforcement
*  learning, at least most algorithms, is some representation of how well things are going,
*  your expected cumulative future reward. And that's usually represented as a single number.
*  So if you imagine a gambler in a casino and the gambler's thinking, well, I have this probability
*  of winning such and such an amount of money and I have this probability of losing such and such an
*  amount of money, that situation would be represented as a single number, which is like the expected,
*  weighted average of all those outcomes. And this new form of reinforcement learning said, well,
*  what if we generalize that to a distributional representation? So now we think of the gambler
*  as literally thinking, well, there's this probability that I'll win this amount of money
*  and there's this probability that I'll lose that amount of money. And we don't reduce that to a
*  single number. And it had been observed through experiments, through just trying this out,
*  that that kind of distributional representation really accelerated reinforcement learning and
*  led to better policies. What's your intuition about, so we're talking about rewards. So what's your
*  intuition why that is? Why does it? Well, it's kind of a surprising historical note, at least
*  surprised me when I learned it, that this had been tried out in a kind of heuristic way. People
*  thought, well, gee, what would happen if we tried? And then it had this empirically, it had this
*  striking effect. And it was only then that people started thinking, well, gee, why, wait, why,
*  wait, why, why is this working? And that's led to a series of studies, just trying to figure out why
*  it works, which is ongoing. But one thing that's already clear from that research is that one reason
*  that it helps is that it drives richer representation learning. So if you imagine
*  two situations that have the same expected value, the same kind of weighted average value,
*  standard deep reinforcement learning algorithms are going to take those two situations and kind
*  of in terms of the way they're represented internally, they're going to squeeze them together.
*  Because the thing that you're trying to represent, which is their expected value, is the same. So
*  all the way through the system, things are going to be mushed together. But what if those two
*  situations actually have different value distributions? They have the same average
*  value, but they have different distributions of value. In that situation, distributional
*  learning will maintain the distinction between these two things. So to make a long story short,
*  distributional learning can keep things separate in the internal representation that might
*  otherwise be conflated or squished together. And maintaining those distinctions can be useful
*  when the system is now faced with some other task where the distinction is important.
*  If we look at the optimistic and pessimistic dopamine neurons. So first of all,
*  what is dopamine? Why is this at all useful to think about in the artificial intelligence sense?
*  But what do we know about dopamine in the human brain? What is it? Why is it useful? Why is it
*  interesting? What does it have to do with the prefrontal cortex and learning in general?
*  Yeah. So, well, this is also a case where there's a lot of people who are going to be like,
*  what is this? This is also a case where there's a huge amount of detail in debate. But one
*  currently prevailing idea is that the function of this neurotransmitter dopamine resembles
*  a particular component of standard reinforcement learning algorithms, which is called the reward
*  I was talking a moment ago about these value representations. How do you learn them? How do
*  you update them based on experience? Well, if you made some prediction about a future reward,
*  and then you get more reward than you were expecting, then probably retrospectively,
*  you want to go back and increase the value representation that you attached to that earlier
*  situation. If you got less reward than you were expecting, you should probably decrement that
*  estimate. That's the process of temporal difference.
*  Exactly. This is the central mechanism of temporal difference learning, which is one of several
*  the backbone of our armamentarium in RL. This connection between the reward prediction error
*  and dopamine was made in the 1990s. There's been a huge amount of research that seems to back it
*  up. Dopamine may be doing other things, but this is clearly, at least roughly, one of the things
*  that it's doing. The usual idea was that dopamine was representing these reward prediction errors,
*  again, in this single number way, representing your surprise with a single number.
*  In distributional reinforcement learning, this new elaboration of the standard approach,
*  it's not only the value function that's represented as a single number, it's also the reward
*  prediction error. What happened was that Will Dabney, one of my collaborators, who was one of
*  the first people to work on distributional temporal difference learning, talked to a guy in my group,
*  Zeb Kurt Nelson, who's a computational neuroscientist, and said, gee, is it possible
*  that dopamine might be doing something like this distributional coding thing? They started looking
*  at what was in the literature, and then they brought me in, and we started talking to Nao Uchida.
*  We came up with some specific predictions about if the brain is using this kind of
*  distributional coding, then in the tasks that Nao has studied, you should see this, this, this,
*  and this. That's where the paper came from. We enumerated a set of predictions,
*  all of which ended up being fairly clearly confirmed, and all of which leads to at least
*  some initial indication that the brain might be doing something like this distributional coding,
*  that dopamine might be representing surprise signals in a way that is not just collapsing
*  everything to a single number, but instead is kind of respecting the variety of future outcomes,
*  if that makes sense. Yeah, so that's Ruth showing, suggesting possibly that dopamine has a really
*  interesting representation scheme in the human brain for its reward signal.
*  Exactly. That's fascinating. That's another beautiful example of AI revealing something
*  nice about neuroscience, potentially suggesting possibilities. Well, you never know. The minute
*  you publish a paper like that, the next thing you think is, I hope that replicates. I hope we see
*  that same thing in other data sets, but of course, several labs now are doing the follow-up experiments,
*  so we'll know soon. But it has been a lot of fun for us to take these ideas from AI and kind of
*  bring them into neuroscience and see how far we can get. So we kind of talked about it a little
*  bit, but where do you see the field of neuroscience and artificial intelligence heading broadly?
*  What are the possible exciting areas that you can see breakthroughs in the next, let's get crazy,
*  not just three or five years, but the next 10, 20, 30 years
*  that would make you excited and perhaps you'd be part of? On the neuroscience side,
*  there's a great deal of interest now in what's going on in AI. And at the same time,
*  I feel like neuroscience, especially the part of neuroscience that's focused on circuits and
*  systems, kind of like really mechanism focused. There's been this explosion in new technology,
*  and up until recently, the experiments that have exploited this technology have
*  not involved a lot of interesting behavior. And this is for a variety of reasons, one of which is
*  in order to employ some of these technologies, you actually have to, if you're studying a mouse,
*  you have to head fix the mouse. In other words, you have to immobilize the mouse.
*  And so it's been tricky to come up with ways of eliciting interesting behavior from a mouse
*  that's restrained in this way, but people have begun to create very interesting
*  solutions to this, like virtual reality environments where the animal can kind of
*  move a track ball. And as people have begun to explore what you can do with these technologies,
*  I feel like more and more people are asking, well, let's try to bring behavior into the picture.
*  Let's try to reintroduce behavior, which was supposed to be what this whole thing was about.
*  And I'm hoping that those two trends, the kind of growing interest in behavior and the widespread
*  interest in what's going on in AI, will come together to kind of open a new chapter in
*  neuroscience research where there's a kind of a rebirth of interest in the structure of behavior
*  and its underlying substrates, but that research is being informed by computational mechanisms
*  that we're coming to understand in AI. If we can do that, then we might be taking a step closer to
*  this utopian future that we were talking about earlier, where there's really no distinction
*  between psychology and neuroscience. Neuroscience is about studying the mechanisms that underlie
*  whatever it is the brain is for and what is the brain for? It's for behavior.
*  I feel like we could maybe take a step toward that now if people are motivated in the right way.
*  You also asked about AI. So that was a neuroscience question.
*  You said neuroscience, that's right. And especially places like DeepMind are interested
*  in both branches. So what about the engineering of intelligence systems?
*  I think one of the key challenges that a lot of people are seeing now in AI is to build systems
*  that have the kind of flexibility that humans have in two senses. One is that humans can be
*  good at many things. They're not just expert at one thing. And they're also flexible in the sense
*  that they can switch between things very easily and they can pick up new things very quickly.
*  Because they very ably see what a new task has in common with other things that they've done.
*  That's something that our AI systems blatantly do not have. There are some people who
*  like to argue that deep learning and deep RL are simply wrong for getting that kind of flexibility.
*  I don't share that belief. But the simpler fact of the matter is we're not building things yet
*  that do have that kind of flexibility. And I think the attention of a large part of the AI
*  community is starting to pivot to that question. How do we get that? That's going to lead to
*  a focus on abstraction. It's going to lead to a focus on what in psychology we call cognitive
*  control, which is the ability to switch between tasks, the ability to quickly put together a
*  program of behavior that you've never executed before, but you know makes sense for a particular
*  set of demands. It's very closely related to what the prefrontal cortex does on the neuroscience
*  side. I think it's going to be an interesting new chapter.
*  That's the reasoning side and cognition side. But let me ask the over romanticized question.
*  Do you think we'll ever engineer an AGI system that we humans would be able to love
*  and that would love us back? Have that level and depth of connection?
*  I love that question. It relates closely to things that I've been thinking about a lot lately in the
*  context of this human AI research. There's social psychology research, in particular by Susan Fisk
*  at Princeton in the department where I used to work, where she dissects human attitudes
*  toward other humans into a two-dimensional scheme. One dimension is about ability. How able,
*  how capable is this other person? But the other dimension is warmth. You can imagine
*  another person who's very skilled and capable, but is very cold.
*  You might have some reservations about that other person. There's also a kind of reservation
*  that we might have about another person who elicits in us or displays a lot of human warmth,
*  but is not good at getting things done. We reserve our greatest esteem for people who are
*  highly capable and also quite warm. That's the best of the best. This isn't a normative statement
*  I'm making. This is an empirical statement. These are the two dimensions that people seem to
*  along which people size other people up. In AI research, we really focus on this capability
*  thing. We want our agents to be able to do stuff. This thing can play Go at a superhuman level.
*  That's awesome. But that's only one dimension. What about the other dimension? What would it mean
*  for an AI system to be warm? I don't know. Maybe there are easy solutions here. We can put a face
*  on our AI systems. It's cute. It has big ears. That's probably part of it. I think it also has
*  to do with a pattern of behavior. What would it mean for an AI system to display caring,
*  compassionate behavior in a way that actually made us feel like it was for real? We didn't
*  feel like it was simulated. We didn't feel like we were being duped. To me, people talk about the
*  Turing test or some descendant of it. I feel like that's the ultimate Turing test. Is there an AI
*  system that can not only convince us that it knows how to reason and it knows how to interpret
*  language, but that we're comfortable saying, yeah, that AI system is a good guy.
*  On the warmth scale, whatever warmth is, we intuitively understand it, but we also want to
*  be able to... Yeah, we don't understand it explicitly enough yet to be able to engineer it.
*  Exactly. That's an open scientific question. You alluded to it several times in the human-AI
*  interaction. That's the question that should be studied and probably one of the most important
*  questions as we move to AGI. We humans are so good at it. It's not just that we're born warm.
*  I suppose some people are warmer than others given whatever genes they manage to inherit,
*  but there are also learned skills involved. There are ways of communicating to other people
*  that you care, that they matter to you, that you're enjoying interacting with them.
*  We learn these skills from one another and it's not out of the question that we could build
*  engineered systems. I think it's hopeless, as you say, that we could somehow hand design these sorts
*  of behaviors, but it's not out of the question that we could build systems that we instill in
*  them something that sets them out in the right direction so that they end up learning what it is
*  to interact with humans in a way that's gratifying to humans. Honestly, if that's not where we're
*  headed, I want out. I think it's exciting as a scientific problem, just as you described.
*  I honestly don't see a better way to end it than talking about warmth and love.
*  Matt, I don't think I've ever had such a wonderful conversation where my questions were so bad and
*  your answers were so beautiful. I deeply appreciate it. I really enjoyed it. It's been very fun.
*  As you can probably tell, there's something I like about thinking outside the box.
*  So it's good to have the opportunity to do that.
*  Awesome. Thanks so much for doing it.
*  Thanks for listening to this conversation with Matt Boppenick. Thank you to our sponsors,
*  The Jordan and Harbinger Show and Magic Spoon Low Carb Keto Cereal. Please consider supporting
*  this podcast by going to Jordan and Harbinger.com slash Lex and also going to magic spoon.com slash
*  Lex and using code Lex at checkout. Click the links, buy all the stuff. It's the best way to
*  support this podcast and the journey I'm on in my research and the startup. If you enjoy this thing,
*  subscribe on YouTube, review it with the five stars in our podcast, support on Patreon,
*  follow on Spotify or connect with me on Twitter at Lex Friedman, again spelled miraculously
*  without the E, just F R I D M A N. And now let me leave you with some words from neurologist
*  V S Samachandran. How can a three pound mass of jelly that you can hold in your palm,
*  imagine angels, contemplate the meaning of an infinity, even question its own place in cosmos,
*  especially awe inspiring is the fact that any single brain, including yours, is made up of
*  atoms that were forged in the hearts of countless far flung stars billions of years ago. These
*  particles drifted for eons and light years until gravity and change brought them together here,
*  now. These atoms now form a conglomerate, your brain, that cannot only ponder the very stars
*  they gave at birth, but can also think about its own ability to think and wonder about its own
*  ability to wander. With the arrival of humans, it has been said, the universe has suddenly become
*  conscious of itself. This truly is the greatest mystery of all. Thank you for listening and hope
*  to see you next time.

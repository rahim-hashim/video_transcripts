---
Date Generated: April 26, 2024
Transcription Model: whisper medium 20231117
Length: 7790s
Video Keywords: []
Video Views: 13
Video Rating: None
---

# Merging Man and Machine? The Neurotech Frontier with Dean W. Ball
**Cognitive Revolution How AI Changes Everything:** [April 26, 2024](https://www.youtube.com/watch?v=dRxolamy-NA)
*  Computers already are neural interfaces. You don't control them directly with your brain,
*  but they obviously interface with your brain, and you are using your brain via touch control
*  to manipulate them. Throughout the history of technology, one of the things we see is that
*  information technologies don't just change the way information propagates. They change the way we
*  think. The impulse that people have a lot of the time is to think, oh no, if there's an incentive
*  to use this thing, then everybody will have to use it. What about the people that don't want to
*  use it? I go there too. I have sympathy for those people. I think about the Amish, and I do think
*  that there's probably going to be forms of digital Amish in the future that we need to be thinking
*  about. At the same time, the people who want to enhance their cognition also should have the
*  liberty to do that. We should want there to be more cognition in the world, especially human
*  cognition. Hello, and welcome to the Cognitive Revolution, where we interview visionary
*  researchers, entrepreneurs, and builders working on the frontier of artificial intelligence.
*  Each week, we'll explore their revolutionary ideas, and together we'll build a picture of
*  how AI technology will transform work, life, and society in the coming years. I'm Nathan LeBenz,
*  joined by my co-host, Eric Thornburg. Hello, and welcome back to the Cognitive Revolution.
*  Today, I'm very excited to share my conversation with Dean W. Ball, research fellow at the Mercatus
*  Center and author of the Hyperdimensional Substack. Dean is a kindred spirit who shares my
*  obsession with frontier technologies and their near-term possibilities, and he's done a super
*  deep dive into the current state of brain-computer interfaces. In this wide-ranging discussion,
*  Dean explains the major approaches being pursued today, from the non-invasive techniques like EEG
*  and ultrasound stimulation to the invasive implants like those being developed by Neuralink.
*  He gives us a sense for the current state of the art across important technical dimensions,
*  such as the number of electrodes used in a given device, the spatial and temporal resolution that's
*  achievable with different technologies, and the major technical challenges that still need to be
*  overcome. Along the way, we touch on big picture questions about the dimensionality of thought,
*  the challenges of interpreting signal that's transmitted through the human skull,
*  and the ethical and societal implications of being able to increasingly read from,
*  and even write to, the human brain. Could we one day induce complex thoughts or download
*  knowledge and skills matrix-style? Will brain monitoring become a routine part of legal
*  proceedings or job interviews? How might the widespread adoption of cognitive enhancement
*  change human culture and even our biological evolution?
*  While he maintains an appropriate degree of epistemic humility throughout,
*  Dean's well-informed intuitions paint a picture of consumer devices that will soon provide powerful
*  brain reading and crude but potentially useful brain writing capabilities. More advanced
*  applications like high-bandwidth, two-way brain-computer communication will likely require
*  invasive implants, but the pieces there too are coming together faster than many realize.
*  Whether you're an AI expert looking to understand a related technology trend,
*  a policymaker grappling with the implications, or just a curious observer of the human journey,
*  this episode will give you a solid grounding in the emerging neurotech landscape. Special thanks
*  to Dean for doing all the work to make this episode possible, and definitely check out his
*  newsletter at hyperdimensional.substack.com. As always, we welcome your comments, questions,
*  and suggestions for future episodes. You can contact us via our website, cognitiverevolution.ai,
*  and if you do, you might also enjoy the chance to chat with my new AI clone, which has been
*  trained on the full history of the cognitive revolution and is powered by Delphi AI.
*  For now, I hope you enjoyed my conversation about brain-computer interfaces and the potential for a
*  man-machine merge with Dean W. Ball. Dean W. Ball, research fellow at the Mercatus Center and author
*  of the hyperdimensional.substack. Welcome to the cognitive revolution. Thank you, Nathan. Great to
*  be here. I'm really excited for this conversation. You and I are kindred spirits in that we both have
*  had our day jobs and then we've had our obsessions with different areas of technology. We connected
*  online after a couple pieces of writing that you put out that were excellent. And as I learn more
*  about you, I was fascinated to see just how much time and energy you have put into learning all
*  about the brain-computer interface space. And so today we are going to do a survey on all things
*  neuro tech. And I'm really excited to learn from you in this domain and to share that with our
*  audience. Awesome. Yeah, me too. So you want to start by just maybe introducing yourself. You've
*  got a varied set of experiences and background interests, and then we can dive into your kind of
*  high-level thesis and dig into the technologies that will take us there one by one. Yeah, as the
*  title of my sub stack suggests, I have a varied background with a lot of different friends going
*  into it. I spent most of my career in the think tank world. So about a decade working in state
*  and local economic policy for the most part, housing, infrastructure, things like that,
*  but have always maintained a very strong interest in technology. I started open source forum
*  software. If there's anyone who remembers PHP BB from way back in the day, I was doing commits to
*  that and writing technical documentation for that at a young age. And the coding bug hit me at that
*  point. And I never went into it professionally, but it's always stuck with me and just a general
*  interest in technology. And that morphed as the deep learning revolution unfolded in the last
*  decade into following the ML literature pretty closely. And once Chapshity came on the scene,
*  I realized that this was a perfect moment for me because I have a background in policy and there's
*  a lot of interest in the societal and policy implications of this technology. And at the same
*  time, I've got a pretty good ground truth, technical sense of what's actually going on,
*  which is often lacking in the policy space. So I try to bring that to everything that I do.
*  I love that. I often say that we really need to figure out what is before what ought to be done
*  about it. And there's all too much jumping to what ought to be done about it that is not based in a
*  good ground truth understanding of what technology actually exists today, what can be done with it,
*  where that's sitting in the near term and so on. So I appreciate that perspective. And I'm excited
*  to get into the details of what you think is going to happen in the big picture of the
*  possibility of a merge between man and machine. Yeah. So I'll explain a little more about how I
*  came to this particular issue. I am a long time fan of JCR Licklider, the DARPA senior researcher
*  who wrote an article back in 1960 called Man-Machine Symbiosis. It's not quite the
*  physical merge that we're going to be talking about. It anticipates the development of something
*  like AGI, as a lot of people did in the sixties, being like way easier. The thesis of that paper
*  is AGI is going to be here in the next five to 10 years. And who knows what happens after that?
*  Probably it'll become super intelligent and replace us. But in the meantime, we'll have a lot of fun.
*  That's basically the thesis of this senior government official at that time. It shows you
*  how much things really changed in terms of just approaches to technology. Although I feel like I've
*  heard similar quotes from some notable technology leaders more recently as well.
*  From the technologists for sure. But coming directly from the DOD is interesting. And it
*  shows you how Greenfield, everything felt with computing at that time. And what's exciting about
*  right now is I do feel like we're at a similar moment where a lot of things are possible. But
*  I've always thought about this issue of symbiosis and thought about it in a fairly broad way.
*  But in the last few years, is the concept of artificial super intelligence has become
*  maybe a little closer than any of us thought, possibly eminent. If you believe some people on
*  Twitter, the concept of the merge just keeps coming up. Prominent technologists, as you say, Sam Altman
*  has a famous blog post called the merge, where he essentially describes it as an inevitability.
*  Elon Musk is not just called it an inevitability, but is in fact working on technical solutions.
*  So he is probably taking this more seriously than anyone else. And just in general, in my
*  conversations with people building in the AI space at advanced levels, there is a very common sense
*  that this is something that will happen. And if artificial super intelligence is even remotely
*  eminent, then the merge must be not too far off either, if that's going to happen. And so my
*  fundamental question is, what does the technology really look like? And that's what I sought to
*  answer in some articles that I've written. And do that, I first looked at the actual scientific
*  technologies that exist right now and like, where is the literature, but also thought about it in a
*  broader sense, because in a lot of ways, computers already are neural interfaces, you don't control
*  them directly with your brain. But they obviously interface with your brain. And you are using your
*  brain via touch control to manipulate them. And throughout the history of technology, one of the
*  things we see is that information technologies don't just change the way information propagates,
*  they change the way we think. So that was my starting point of almost seeing the merge
*  as something that started a long time ago, a path that we are still on, and that will get more vivid
*  and more visceral over time, but not fundamentally new.
*  Yeah, that's interesting. Certainly, I feel like I've been through a couple waves already of
*  technology changing how I think it feels so quaint now. But there was the idea of we don't have to
*  remember anything anymore, because we can just go search for it on the internet. And certainly,
*  that is true, or even GPS, right? Just we don't have to make spatial maps of our general
*  environments, because so many of us just default to using the GPS. For me right now, I wonder if
*  you have experienced something similar with the current wave of technology. I do find myself
*  getting into some pretty deep habits, at least with how I relate to language models. Coding tasks
*  are a pretty good example of this when I reflect on how I used to code versus how I approach coding
*  tasks now. Probably making a mistake in the past, because I've never been an outstanding coder, but
*  I feel like I often used to go into the editor first, and maybe start writing some comments and
*  trying to break things down or starting to scaffold out the classes. But very often, I was jumping
*  too quickly into code. And one of the things I've learned from using language models is I'm really
*  rewarded for taking the time first to think, what do I actually want here? Can I define that
*  in conceptual terms first, before I start to diffuse as it were into the finer grained structure
*  of the code? And in general, I think that's starting to happen to me. We recently did an
*  episode with shortwave, the email client as well that has really good email AI assistant. I see an
*  evolution there too, where I used to remember keywords to navigate my vastly overflowing and
*  unmaintained inbox. And now, I don't have to be so keyword oriented anymore. I can ask questions.
*  And that's definitely very helpful for me. But also, I'm starting to feel already a little bit
*  like my keyword search ability is beginning to atrophy. So certainly, I recognize and
*  experientially feel the idea that the ways that technology have changed have been fought.
*  I don't know if you have any similar stories, and it's probably pales compared to what might
*  be ahead of us still. Yeah, no, absolutely. And it is important to think about that kind of thing.
*  For me, in a similar vein, LLMs just fundamentally changed the way I ask questions and made me much
*  better at asking questions. Oftentimes, I remember it's about a year ago, since my first experience
*  as the GPT. And 3.5 was not quite as vivid in this way. But when GPT-4 came out, I would ask
*  it a question and I would find this isn't quite what I wanted. This isn't quite what I was looking
*  for. But I know this model must be capable of giving me what I look for. So the problem must
*  be with me. And so I kind of refining my question and getting down to what is it that you're really
*  asking. And so often in fields of intellectual inquiry, that is actually the more important
*  thing, that finding the right question is 90% of the intellectual journey. And so something that
*  accelerates that, that makes us better at that, accelerates all kinds of intellectual endeavor.
*  And I am excited to see things like Claude III Opus, which it seems that the qualitative difference
*  in that model versus GPT-4 is really at the frontier of all kinds of different fields,
*  that people that are doing middle of the bell curve activities, and not even coding necessarily,
*  but just like various kinds of questions on science, history, whatever it may be, that
*  those questions, the middle of the bell curve stuff, the difference between GPT-4 and Claude
*  III Opus is not necessarily all that much. But that when you're asking things that are more at
*  the frontier, Claude III really shines vis-a-vis GPT-4. I can definitely tell you, having used
*  LLMs a lot to help me accelerate this process of researching these articles on neuroscience,
*  that's definitely been the case with Claude. It's just so much better at answering those questions
*  than GPT-4, where GPT-4 would get answers that I had enough context to know, like,
*  eh, this is kind of BS here. This is just filling in the blank. Whereas Claude III is more capable.
*  I think as the LLMs get more capable, that will continue to be very relevant. And then on another
*  level, obviously, anyone paying attention to this space is asking themselves philosophical questions
*  about what is the nature of cognition? What is the nature of intelligence? What distinguishes
*  my intelligence from the kind of intelligence that I'm seeing here exhibited on this screen?
*  And it's actually a journey that we should all go through anyway, regardless of whether LLMs exist.
*  Because asking what special value do you bring to the table? And what unique perspective do you have
*  is a question that everybody should be seriously asking themselves all the time and not enough
*  people do. And I think LLMs are kind of forcing function for a lot of people for labor market
*  concerns, just as much as anything else, to just really probe at that. So in a way, for me,
*  my experience is as I look back on the last year using advanced LLMs, it's made me more reflective
*  and just more inquisitive. And that is Excel. That has all kinds of compounding benefits.
*  And obviously, the other thing is that once so much about the history of technology is not
*  how it impacts one person or one building or one place, it is instead about the non-linear
*  compounding effects when everybody has access to that same capability. And I think we're in the
*  very early days of that. And that's part of why I find this to be such an enormously exciting time
*  to be alive. Hey, we'll continue our interview in a moment after a word from our sponsors.
*  The Brave Search API brings affordable developer access to the Brave Search index,
*  an independent index of the web with over 20 billion web pages. So what makes the Brave Search
*  index stand out? One, it's entirely independent and built from scratch.
*  That means no big tech biases or extortionate prices. Two, it's built on real page visits from
*  actual humans, collected anonymously, of course, which filters out tons of junk data. And three,
*  the index is refreshed with tens of millions of pages daily. So it always has accurate up-to-date
*  information. The Brave Search API can be used to assemble a data set to train your AI models
*  and help with retrieval augmentation at the time of inference, all while remaining affordable with
*  developer-first pricing. Integrating the Brave Search API into your workflow translates to more
*  ethical data sourcing and more human representative data sets. Try the Brave Search API for free for
*  up to 2,000 queries per month at brave.com slash API. Amna Ki uses generative AI to enable you to
*  launch hundreds of thousands of ad iterations that actually work customized across all platforms
*  with a click of a button. I believe in Amna Ki so much that I invested in it, and I recommend you
*  use it too. Use Cogrev to get a 10% discount. Yeah, it's crazy. You hit on something there
*  that I often think about as well, which is just that the future dynamics of the world at large as
*  AI starts to infuse into everything are dramatically under-theorized. When I go around
*  and talk to everybody in AI today, largely their implicit world model seems to be,
*  the world is the world, I'm applying AI here, therefore we're going to have the world plus my
*  AI intervention, and that'll be sweet because we'll get this productivity gain or whatever.
*  And that is not wrong, but it sort of misses the fact that everybody else is doing this at the same
*  time, and therefore there's going to be just a lot of, in my view, unpredictability to how all
*  these new arrangements interact with each other at a higher level. I think about that all the time,
*  and I think that we're in for just an order of magnitude complexification of the world beyond
*  what we've already seen. If you think about the world has just become denser in the last 30 years,
*  you think about what was New York City like 400 years ago, the island of Manhattan versus
*  what it is today. It's the same geographic landmass today, landfill parts of it, but basically
*  the same thing. And the difference is that it's just dramatically denser and more complex. And
*  I think that we are in for perhaps not geographical densification, but another substantial round of
*  conceptual and cognitive densification. And one of the things I worry about, and another thing that
*  attracted me to this issue area, is the question of how we're all going to keep up with that.
*  I worry now that people like you and me are already in a bubble. We're extrapolating multiple points
*  out on this LLM, on the dynamics of AI agents being all over the world. Other people haven't even
*  contemplated the idea of AI agents and have probably asked ChatGPT 3.5 one basic question
*  18 months ago and haven't thought about it really that much since. And so I worry about people being
*  shocked and left behind. And I think that maybe neural technology is our way, at least I hope,
*  for us all to just keep better pace with the complexity that I suspect is coming.
*  Yeah, there was a recent study just this week that came out that said that 30% of young people
*  are using ChatGPT for work or whatever. And it is a good reminder that that's a lot because it's only
*  been a year in change since the first version and a year in just a few days since GVD4. But
*  it's also not that many yet. And the tools are still certainly relatively basic compared to
*  where it seems quite clear that we're headed. In terms of going along for the ride, which is an
*  Elon Musk framing on this, this may be a little shocking for people that aren't aware of how much
*  progress has already been made. Because one way I think about it is like, the way we use computers
*  has, first of all, it's a bidirectional relationship, right? We put information into
*  them, they give us information back. The way in which we have entered information into the
*  computers historically has been this sort of finite action space of like, you can type on the
*  keyboard and you can click the mouse. And you can do a lot with that. But at any given time,
*  you have a finite and often quite prescribed set of actions that you can take. And outside of that,
*  just nothing happens. And that's also interesting. That's one of the reasons that
*  they cite for why the web agents historically didn't take off. They tried to do reinforcement
*  learning on the web. And the reward signal was just too sparse. Agents couldn't get anywhere.
*  And they couldn't chain enough success together to get any reward. And so the whole project went
*  nowhere for that reason. Of course, the signals that we get back have been getting richer and
*  richer over time, like higher resolution, more realistic graphics, etc, etc. Now with this
*  language moment, we have the ability to speak in natural language to the computers. And this
*  really opens up a sort of richness of communication for what they can understand in terms of our
*  mental states and desires. Ilija from OpenAI once and possibly still from OpenAI put that when he
*  said, the thing that's most incredible about this is I speak to the computer and I feel I am
*  understood. And that's a really good baseline reality check of what makes this different than
*  before. But now recalling your sub stack title hyperdimensional, we're moving around the verge
*  of potentially moving from this language mode of communication, which has just opened up for us to
*  talk to computers in our own natural language. That is obviously a richer space, much more wide
*  open space than you can click on these particular buttons within an interface. But it is still,
*  of course, the compressed form token by token that we're reducing our internal thoughts to this
*  output stream that we can encode in language. And one big way to think about the set of technologies
*  that we're going to talk about today is that it goes up yet another level in terms of the richness
*  of the dimensionality of the space in which we can communicate with computers.
*  Yeah, absolutely. So let's get into it. I think at a fundamental level, all of this,
*  the neural technologies, it's really a story of very advanced sensor fusion and signal processing,
*  which is the story of so much technological innovation over the last 100 years. We don't
*  think about it in that way. But from Bell Labs on, it's been a story of signal processing. In this
*  case, signals are the biomarkers of thought. Thought is fundamentally mediated by electricity
*  and magnetism. And so you can measure electrical and magnetic fields generated by brain activity.
*  That's the primary way that this is done, or at least it's the most straightforward way,
*  let's put it that way. There are other interesting ways that we'll get into. The most common that you
*  see for neural monitoring, monitoring brain, say not so much modifying them, but understanding what
*  a person is thinking, is called EEG, electroencephalography. And it has a closely related
*  cousin called MEG, magnetoencephalography, which is measuring the magnetic fields. So kind of same
*  idea. The difference is that EEG can be done with tiny electrodes placed on the head. Magneto
*  encephalography requires pretty substantial equipment that I don't think is going to make it
*  out of the lab anytime soon. The thing that a lot of people don't know, even in the tech space,
*  is that it's not just Neuralink in this field, shipping products. For more than a decade,
*  there have been neural technologies using EEG, especially because it's relatively cheap to do
*  all kinds of practical things. And it's obviously also been used in a lot of lab settings. The
*  difference between really a lab EEG and a consumer EEG is just the number of channels that you get.
*  So consumer EEG might be stereo, just two electrodes up to maybe at the maximum 32.
*  That would be a lot. 32 would be like a whole helmet that you're wearing. Something like 8,
*  16 is more common in the consumer setting. Lab can go all the way up to 256. And this is just
*  taking an enormous amount of data. That's something that is also not appreciated,
*  is just that the brain generates a torrent of data. A lot of EEG, you can change the sampling
*  rate, but the sample rate is usually around a thousand hertz. So a thousand samples per second.
*  Any channel EEG in a consumer headset is going to be generating 8,000 data points from your brain
*  per second. So you quickly get into millions if you're using it for any substantial period of time.
*  Fundamentally, the problem with all of these technologies really is the human skull.
*  The skull was designed to protect your brain, and it does a good job of that.
*  And it is not particularly conductive. So it tends to attenuate signal coming out of the brain and
*  going in. There's other things too. There's cerebrospinal fluid. There's other mediating
*  layers between the actual surface of the cortex and the brain and the scalp, but the skull is
*  the most important one. And so modeling that, modeling the skull, which also varies between
*  people. In thickness, density is very difficult. It also varies not just between people, but
*  cross your skull. So your skull is not homogeneous in terms of its density or thickness. And so it
*  has to be modeled in real time for an ideal reading. And that is where I think we're at the
*  frontier of these technologies. But I'll talk a little about what has been done so far,
*  particularly with EEG. EEG devices can do things like screen for signs of cognitive decline.
*  They can read, for example, Parkinson's. There are biomarkers of mental illness that can be picked
*  up in EEG devices. Generally, you don't see that on the consumer side of things. And the reason for
*  that is that it relates to FDA regulation. We can get into that later. But for consumer devices,
*  you'll often see devices to help you meditate better. The brain waves, they fall into a few
*  broad families. And it is actually kind of intuitive. Your brain, the electrical fields
*  that your brain is generating oscillate at higher frequency when you are thinking more intensely.
*  That is an intuitive relationship. So when you're in deep sleep, the frequency is very low. And when
*  you are focusing or in a panic, the frequency is very high. And so those kind of crude measures of
*  is this person sleeping? Is this person in a deep meditative state? Is this person attentive and
*  focused? Or are they scared? These are the kinds of things that can be read right now in consumer
*  devices. Still fairly crudely, but it can be done. So come with just very practical, rookie level
*  questions about exactly what we're measuring and exactly what we're doing with it here.
*  The electrodes that you put on your head to measure these electrical signals, you said that
*  the frequency with which they can take a measurement is about a thousandth of a second. A thousand
*  hertz is a thousand cycles a second. So it's a one, one thousandth of a second measurement.
*  The rate at which a neuron can fire is also roughly a thousand times a second. Is that right?
*  It can be quicker than that. Neural activations can be quicker. So I should actually just step
*  back. First of all, we're talking here about non-invasive technology. There's a whole school
*  of invasive stuff, which we can get into later, but on the non-invasive side, yeah, that's right.
*  And EEG is also useful because of that temporal resolution, as it's called in the literature,
*  is excellent for EEG. As a comparison, the kind of gold standard for spatially imaging the brain
*  is fMRI and that at its best can take one image every two seconds. So in the space that fMRI,
*  using fMRI you're in a lab because fMRI requires superconducting materials. You're not wearing that
*  on your head anytime soon. If you're wearing, for example, let's just say a 64 channel EEG,
*  then in the space that an MRI can take one image of your brain, the EEG is generated more than a
*  sample from the brain. So the temporal resolution is great. Not quite at the neural activation
*  level from a temporal perspective and far from it from a spatial perspective. So an electrode at its
*  most precise can see millions of neurons still down to a spatial resolution of centimeters or
*  millimeters in some cases. I want to understand a little bit better what the electrodes are actually
*  measuring, like what their output is and then how that gets translated into this sort of
*  spatial model of what's going on in the brain. Is it accurate to say that an electrode creates
*  one number every thousandth of a second that would represent sort of the strength of the
*  electrical field? A point in time. Yeah, exactly. And it seems like there's Fourier transform kind
*  of math that must be happening here where this is similar to like how cell phone towers work from
*  what like limited understanding I have of this branch of physics. But basically we have all of
*  these neurons firing off with these sort of spikes, right? And there's a very short duration,
*  relatively high voltage signal that is getting sent very locally. Stop me if I'm wrong about
*  this at any point because I'm really not very expert in this at all. Because that's now happening
*  in all these billions of locations concurrently throughout this whole region of the brain,
*  that then sends out this massive signal to the outside world. Much like a cell phone tower is
*  sending out a massive signal that is communicating with all of the phones in the area at once.
*  And then in a similar way, all these electrodes are receiving this sort of messy signal where
*  it's like, okay, I'm here. And this is what I feel right now. And that is the aggregate of all of the
*  signals that have been created from these individual neuron firings. And then there's like
*  a real computational challenge after that to say, okay, we've got 64 different signals because
*  we've got 64 electrodes on the head. What does that translate into? So can you tell us a little
*  bit more about how that is happening? How does that sort of 64 numbers get translated into
*  a spatial understanding of what's going on inside? Yeah, this is a great question. First of all,
*  your intuition here and what you've stretched out is basically correct. And yeah, a lot of the
*  basic analysis that's happening here is your standard Fourier transform. Just to define that,
*  that basically takes a composite signal and breaks it down into the intensity of the signal
*  at different frequencies over time. So you have some wobbly signal that you're measuring. And
*  this says, okay, how could you re-represent that signal as the sum of intensities at certain
*  frequencies throughout the frequency spectrum? Yeah, the way I think about it is almost like,
*  if your brain is playing a chord, the Fourier transform separates it into individual notes.
*  And so you can see in that way. And that's essentially what's going on with EEG signal
*  processing. I would just add that there's competing electrical signals, right? Your eyes,
*  when you blink, are generating electrical fields. All of the muscles in your face are doing the same
*  thing. The device itself that you're wearing is generating electrical fields. So there's all of
*  this competing electrical activity around the head, which is being sampled. The electrodes are
*  going to sample some of that. That's got to be processed out. And then there is what I was
*  alluding to earlier, that the electrical field itself from the brain is going to be attenuated
*  in different ways dynamically by the skull and other sort of cranial media difficulty of
*  processing that. That's where there have been a lot of traditional techniques, traditional statistical
*  analysis techniques that have been used, and older metal techniques, convolutional neural nets,
*  recurrent neural nets, all that kind of stuff that have shown some promise. Basically, everything
*  that I'll talk about actually, is really using those kind of older forms of statistical analysis
*  to break this apart and figure out what's relevant and figure out what it means. There hasn't been a
*  lot of transformer-based work and other types of things. That's why I think there's just a lot
*  of low-hanging fruit. And it's actually still an open question to me. The transformer has been
*  around for a while now. There are some papers that show EEG transformers and other types of
*  neural signal processing with transformers. But why aren't there much more? Is it the conservatism
*  of academia? My first intuition was maybe it's a data problem, but these things generate a lot
*  of data. So I really don't know. I'd love to know. If any of your listeners have insights,
*  I'd love to hear it. Yeah, I have a couple of intuitions, which may or may not be right.
*  People can correct me on this as well. But we just did an episode on the first 90 days of Mamba
*  literature. One of the things that is really interesting about this new mechanism, the
*  selective states-based mechanism, is that it does have different strengths and weaknesses compared
*  to the attention mechanism, both in terms of how much memory it consumes, where the attention
*  mechanism is quadratic and the length of the input. And that might be, by the way, one of the
*  reasons. Just as you talk about a torrent of data and a thousand samples per second, if that were
*  to be naively translated to a thousand tokens per second, then very quickly you're getting to a level
*  of tokens that we have only very recently reached with frontier grade transformers. It was only
*  with GPT-4 a year ago that the public first got to see a quality 8,000 token transformer. And before
*  that, it was just a couple of months where we had just seen the 4,000. And before that, as of 18
*  months ago, 2,000 tokens was what you could really get from the OpenAI API. So just the sheer volume
*  of data may not lend itself super well to the transformer. But also another interesting thing
*  is that when they break down these micro tasks and look at what the transformer can do and can't do,
*  one of the things it really struggles on is the hyper-noisy environment. There was an interesting
*  result in this one Mamba versus transformer comparison paper. It's more about the selective
*  state space mechanism and the attention mechanism. Those are really the two things that are more
*  dueling it out than the higher level architectures. And they're not even dueling it out because they
*  actually work best together, spoiler. But in the super-noisy environment where what actually matters
*  is quite rare in what you're signaling, then the transformer sometimes has a hard time converging.
*  And the intuition I've developed for that is because it's changing all the weights at the same
*  time across the entire range of the input, it may be that the gradient is often dominated by noise
*  and has a hard time converging on the signal. Whereas when I want to make everything about the
*  selective state space model, though I do have an obsession about this, as folks know, it is updating
*  per token. And so it seems like it has a more natural mechanism when the actual signal hits
*  to say, oh, and this is where I start to violate my no anthropomorphizing policy. But it has an
*  ability to recognize when the signal hits and update in a more focused way on that one thing
*  that really was supposed to matter. Whereas a transformer is updating everything all across,
*  it's considering everything at once. And so it seems like the signal can get lost in all that
*  noise. The recurrent nature of the selective state space mechanism allows you to kind of zero in and
*  do the gradient on the signal when you have the signal. And then of course, there's still a lot of
*  noise, but that maybe can get separated from the signal because of this bit by bit level processing
*  and updating. I'm not 100% confident in that theory, but it is consistent with all the evidence that I
*  know of so far. So we'll see how that evolves through time. Then we might be in for an exciting
*  couple of years. If that's true. Yeah, that's a great point. Very well. Hey, we'll continue our
*  interview in a moment after a word from our sponsors. Today's podcast is brought to you by Plum.
*  It's 2024. Do you really need to be a staff engineer to understand how your AI feature works?
*  Plum doesn't think so. That's why they've created a no code AI app builder that non-technical folks
*  can understand at a glance. A drag, drop and configure visual pipeline for any AI feature you
*  can imagine. Plum gives product teams a place to go from prototype to prod together. Check out
*  useplum.com. That's Plum with a B for early access. Hey all, Eric Torenberg here. I'm hearing more
*  and more that founders want to get profitable and do more with less, especially with engineering.
*  Listen, I love your 30 year old ex-fang senior software engineer as much as the next guy,
*  but honestly I can't afford them anymore. Founders everywhere are trying to turn to global talent,
*  but boy is it a hassle to do at scale from sourcing to interviewing to on the ground operations and
*  management. That's why I teamed up with Sean Lanahan, who's been building engineering teams
*  in Vietnam at a very high level for over five years to help you access global engineering without
*  the headache. SQUAD, Sean's new company, takes care of sourcing, legal compliance and local HR
*  for global talent so you don't have to. With teams across Asia and South America, we can cover you
*  no matter which time zone you operate in. Their engineers follow your process and use your tools.
*  They work with React, Next.js or your favorite front-end frameworks. And on the back end,
*  they're experts at Node, Python, Java and anything under the sun. Full disclosure, it's going to cost
*  more than the random person you found on Upwork that's doing two hours of work per week but billing
*  you for 40. But you'll get premium quality at a fraction of the typical cost. Our engineers are
*  vetted top 1% talent and actually working hard for you every day. Increase your velocity without
*  amping up burn. Head to choose squad.com and mention Turpentine to skip the wait list.
*  Maybe that. I've talked a lot about the downsides and what's hard. Once you get into this literature,
*  what ends up happening is you just admire the very, very challenging problems that there are and just
*  how complicated the brain is. But there is a lot that you can do. And what's shocking about EEG
*  is that it works as well as it does non-invasively, especially when you consider
*  that the only electrical signals really that can reach the brain or that can reach the electrodes
*  on the scalp from the brain are very much on the surface, very much cortex, maybe 1 to 3 millimeters
*  below at the most. Everything else just gets totally attenuated. So any deep brain structure,
*  there's just nothing that EEG can really read. So everything you're talking about is stuff that's
*  coming from just the surface of the brain. And that can do things like predict seizures with
*  nearly 100% accuracy up to one hour before. That was demonstrated, in fact, about eight years ago
*  in a lab setting. And there are devices that do this for people with epilepsy. So the telltale
*  signs during which the patient feels absolutely nothing. There's no external sign for the patient
*  that a seizure is coming. But there are brain patterns that can be interpreted by consumer EEG
*  hardware that can predict with almost 100% accuracy whether a seizure is going to happen.
*  Same thing with Parkinson's early onset. Parkinson's has a pretty distinct neurosignature
*  that can be read. That's something like 90 plus percent accuracy. So already, the potential of a
*  medical device. I mean, I'm wearing AirPods right now. In fact, Apple has a patent that they've
*  explored of putting electrodes on AirPods to do this exact thing. Just simply something,
*  a pair of AirPods that can monitor for important medical conditions like that, and maybe help me
*  relax. That's already something that could be quite useful and seems like it will happen within the
*  next few years. Maybe not exactly in the AirPods form factor. And when I said, you know, make you
*  relaxed, that refers to something called neurofeedback. So rather than a direct modulation
*  by hardware of your neural state, neurofeedback is basically giving you the data and allowing you
*  to change your patterns of thought in response to the data. So there are neurofeedback devices
*  that have EEG sensors on a headband that you might wear and it pairs with a phone app.
*  And the phone app will show you your neural activity in real time and maybe give you a game
*  or some other kind of cognitive stimulator to play with. And it will tell you how focused you are.
*  And you can get focused more. The idea is that you can actually train circuits in the brain to
*  become more focused. There are devices that do this for sleep without you having to do anything.
*  A lot of devices, for example, there's one called the BIA, I believe that resembles like a sleep mask
*  that you wear around your head. And I've never tried this by the way. I don't think the BIA is
*  actually shipping yet. And I'm certainly not endorsing it, just to be clear. But you can wear
*  it like a sleep mask and it will play music. And that music is dynamically tuned in response to
*  EEG signal and meant to bring you into a more relaxed state. And ultimately, I don't think
*  there's a lot of scientific literature backing this up. But there is general scientific literature
*  to support the idea that neurofeedback is a thing. Your brain will develop circuits to get into a
*  more relaxed state more easily on its own, but they're not practice at that. So that's the kind
*  of thing that we're talking about in consumer devices. There's also motor control, which is a
*  whole different interesting field that maybe you want to go into. But first, if you have any
*  questions on the first set of things. Yeah, this sort of same paradigm seems to happen all over
*  the place. There's like echoes of this going with the increasingly rich signal. Then we also have
*  these sort of increasingly meaningful states that we're able to identify, right? Within the transformer,
*  this is pretty well studied now where in these sort of late middle layers, the inputs have been
*  worked up to these rich concepts. And you can even identify the direction in activation space that
*  corresponds to justice or fairness or love or these kind of things. You're like, wow, how did this AI
*  learn to represent that when all it's doing is next token prediction? And here there's like
*  a somewhat analogous thing where as the ability to read the signal gets better and better,
*  we're able to see like, okay, it takes two electrodes on the brain to detect if you're
*  sleeping or awake. With four, you can get to, are you stressed or are you relaxed? With eight,
*  you can get to general emotional state like fear, happiness, disgust, anger. And then with 16 and
*  32, more advanced things are starting to happen. So I am actually really interested in the motor
*  thing because that seems like an interesting lens into just like how much resolution do we already
*  have in the ability to decode this stuff. And then I also wonder if you have thoughts about the limits
*  of that with this technology, of course, but we're going to discuss them on technologies too.
*  Yeah. So motor control, it really does turn out that when you think about moving something,
*  it is tantamount to sending the electrical impulses to actually move that thing. And that can be
*  translated for people that are unable to make that motion themselves. So there's demonstrations,
*  maybe it's just my algorithm, but I see this on X all the time of a person wearing a helmet,
*  controlling a robotic arm, for example. And oftentimes the motions are jerky or slow,
*  or you'll see sped up footage. And those are the signal processing issues that we have now. If you
*  see someone wearing a whole helmet, that's going to be a lot of EEG signal that they're reading.
*  But you can interpret some basic motor control from the cortex, from cortical activity. Now,
*  a lot of motor control is coming from deeper brain structures. The limits on that, at least to me,
*  as someone who's not a neuroscientist, unclear exactly. But I actually think it's important to
*  say at this point that some of the highest quality data sets for this kind of application
*  are data sets that combine EEG readings with fMRI or PET scans. Now, PET scans and fMRI, again,
*  not the kind of thing that are going to make it into consumer use cases, maybe ever, certainly
*  not anytime soon. In lab settings, you can record that. And then you have an interesting relationship,
*  because the fMRI in particular is a 3D voxel, as it's called in the literature, representation
*  of brain activity. fMRI uses blood flow to infer a blood oxygenation, to be precise,
*  to infer brain activity. And then you can connect that with the EEG signal. So all of a sudden,
*  that's an interesting AI application, because you've got a much richer, but more sparse signal
*  coming from the fMRI, and then a super noisy signal coming out of EEG. And there's an interesting
*  connection. What are subtle differences that we might not notice, subtle patterns that we might
*  not notice between different states of mind that we can easily see on the fMRI that we can't see on
*  EEG, but perhaps they can be pulled out of the data. I think that's a very rich area of research.
*  And we'll talk later about some companies that are using models exactly of that kind
*  to do interesting things. But that could really advance, especially on the motor control.
*  But non-invasive EEG based brain computer interfaces already exist. And that's to understand,
*  are they super useful? No, not really. They're for enthusiasts of this kind of thing. And they're
*  not cheap. But you can today buy a 32 channel EEG headset and pair it with software that you can
*  use to manipulate objects on the screen of your brain. It requires some calibration. You can't
*  just do that out of the box, but it can do it. It's like they have a block that you can move left and
*  right and things like that. Nothing like the cursor control that Neuralink has displayed has shown,
*  but that is possible in digital environments. And then certainly also it's possible to move robotic
*  devices. And there are prosthetics that work in this way already.
*  One question I've been pondering here is what is the kind of breakdown? We talked a little bit
*  about traditional signal processing and Fourier transforms and whatever. And then I'm also reminded
*  of Elon Musk saying on the Neuralink show and tell day a year and change ago now that turns out the
*  best thing to decode a neural net is another neural net. And so I'm wondering what parts of the
*  interpretation process you've got like a thousand numbers coming off each electrode per second.
*  And then ultimately that needs to be translated into something right. A classification of your
*  state or like a direction in motion space that you're going to try to move your robot arm or
*  whatever you're trying to do. And between there, there's you could imagine like decoding with all
*  traditional methods. You can imagine an entirely neural net thing that just like takes in these
*  wrong numbers and translates that to an output with basically no principled approach other than
*  just throw a model and a bunch of data at it and let it figure it out. Do you have a sense for what
*  the right balance is there and whether today's balance is likely to hold or are we headed for
*  another bitter lesson where just all of this gets thrown into neural nets ultimately?
*  It does feel that way. We see problem after problem falling to the unprincipled application
*  of neural nets. Obviously it's more complicated than just throwing data into architecture,
*  but basically we've seen that over and over again. And every time it happened, the experts
*  and the scientists who were specific to that field told us that will never work. It's impossible.
*  And then it works. So I've learned to be humble in this regard and I wouldn't want to hazard
*  too much of a guess. My intuition right now is that the field, frankly, is probably relying on
*  a little bit more primitive methods of doing the signal processing than it could. And that
*  sort of moving in the direction of a fully neural net is at least worth experimenting with. And I
*  think part of the reason that the scientific community doesn't do that is because you want
*  comparability with studies that have come before. There is this innate conservatism
*  in this field of science that the fresh crop of startups focusing on this will be entirely
*  uninterested in. And I think we're at the stage where we need to get this research
*  out of scientific labs and more into at least corporate R&D labs. And obviously something
*  that's important to understand here is that every one of the big tech companies
*  employs neuroscientists who work on things that are at least adjacent to this. Apple's got a lot
*  of patents in the field. Apple's exploratory design group is probably looking at this. That's
*  their kind of skunkworks operation. Meta's been more public about it. Meta's put with Greece. And
*  in fact, Mark Zuckerberg, it's worth noting in his review of the Apple Vision Pro, which we should
*  talk about, by the way, because that's like an interesting kind of upstep towards all this. But
*  Mark Zuckerberg in his review of the Apple Vision Pro said, basically something along the lines of
*  the eye tracking interface they've built is okay until we get the neural interface hooked up.
*  Basically viewing it as an inevitability. There are probably right now inside of both startups
*  and large corporate R&D labs fresher approaches to this being tried than at least what I have seen
*  in the academic literature. Though in fairness, academic literature doesn't always go into a ton
*  of detail about exactly how the signal processing is done at the statistical analysis level. But
*  yeah, that's my general sense. Availability of data also may be a real issue for some of these
*  things. It seems like the way that this has progressed in neuroscience has backfilling
*  a narrative here. But I feel like it is the brain is the ultimate black box, right? Even more messy
*  and black boxy and just hard to get into, obviously, for all sorts of medical and ethical
*  reasons as compared to a digital neural network, which you can be into with clarity and chop parts
*  off and see how it works with different permutations. So there's been just a huge
*  initial challenge of figuring out in rough terms what is going on and how does it work.
*  And so people are doing these very small sample sizes of looking at people in fMRIs and trying
*  to deduce what brain region does what and what frequency of waves seem to correspond to what.
*  And this super low data regime figuring out in general terms what's going on then seems to
*  naturally lend itself to, okay, now let's try to apply principled approaches to identify when
*  that's happening versus I can see this shifting very quickly and probably would happen in private
*  companies first, just because if nothing else, they're going to see the opportunity and really
*  invest in scaling up the data. Having the data to say what were you trying to do when we recorded
*  that brain state, what were you trying to do with your robot arm or with the cursor on the screen?
*  Like that data just has never existed. So you can't really take the better lesson approach until you
*  have the scale of recorded data to make it go. And it seems like we've only recently realized this is
*  going to work for everything and we need that scale of data and nobody has really collected it
*  globally. We just did this episode with Paul Scottie, who is the author of the MindEye2 paper.
*  They are beginning to work on a multimodal brain state interpretation model, which would
*  take in different kinds of signals and try to output different kinds of predictions.
*  And it sounds like that's really only getting underway. Like there's data is super fragmented.
*  It's all kinds of different places and forms. And that also seems like a big part of why this
*  hasn't happened yet. Would you agree? Yeah, I do. And I think we're at a very primitive state
*  when it comes to the data. I don't think we have a good sort of population level modeling
*  of the variation in neurosignatures, even things like skull thickness. Right now, it's like the
*  literature is, well, everyone's skull is different. And that's probably not true. It's probably not
*  literally true that it's like a snowflake. Right? Like my skull is, it might be unique at a very
*  granular level of detail, but you can probably model population dynamics for this sort of thing.
*  And that would make your imaging challenges substantially easier. Same thing goes for the
*  neural activity. It's definitely quite likely that high dimensional thought in particular
*  is probably pretty unique signature. My associations that I have with the concept of Flawed 3 Opus
*  or Mozart or something are very different from yours. And it's not entirely clear that we're
*  going to be able to get to the point of like, oh, Dean and Nathan are both thinking about Mozart.
*  That seems hard to be able to reach, but there's a lot lower level thought that is still interesting,
*  that it seems like you could model that's also more, that's higher level somewhere in between
*  Mozart and, you know, I'm scared of this tiger. I'm trying to run away from it. We can read that
*  pretty easily. We know what that looks like. That has a pretty common signature. That's easy to pick
*  up on. The my guy team paper actually may shed a little light on this because first of all,
*  the dataset is only from eight people that they work on. So people, it should be right before this
*  on the feed. Basically what they're doing is looking at your brain state as measured in that
*  case by fMRI and reconstructing what you were looking at. They had an earlier version of this
*  where they created a custom model for each of the eight people that are represented in this one
*  open source dataset. Each person had to spend like 30 to 40 hours in an MRI machine over presumably
*  a bunch of different sessions and they're being shown an image every few seconds. And then they
*  just had to sit there and click a button if they recognized that they had seen that image before,
*  just to kind of make sure that people are engaged in the task on an ongoing basis.
*  So the jump between MindEye1 and MindEye2 was that instead of creating a single model trained on all
*  of the 30 to 40 hours of data per individual, they were able to train a single model based on
*  seven of the eight individuals' data. By the way, each of the brains is quite different in shape.
*  They report the number of voxels per individual, voxel being roughly speaking a centimeter or a
*  two millimeter cube. The lowest number of voxels from one person is like 12. How they choose the
*  number of voxels is by the anatomy of the brain. So they're looking at basically the visual cortex,
*  segmenting that off and then just splitting it into voxels. And the resolution of the voxel is
*  constant. So how many voxels you get depends on the total space of the portion of the brain that
*  they identify as the relevant visual cortex for this purpose. So 12,000 in some is the low end
*  and the high end is over 17,000. So you have a 12,000, a couple in the 13,000 range, a couple
*  in the 14,000 range, a couple in the 15,000 range, and then one over 17, close to 18,000 is the highest.
*  So you see like a roughly 40% difference from the lowest number of voxels to the highest.
*  And that requires then a little bit of a bespoke adapter portion of the model for each person
*  because they just have literally different numbers of input. The vector that is measured is a different
*  length for each of these individuals. So the adapter to then get to the shared latent space
*  has to be a bit different for each individual. But once they create that shared latent space,
*  then they are able to do an additional person with just one hour of data. So the key finding
*  there is that they go from a previous technology, same data set, interestingly, same raw
*  information. These are the same sessions that were recorded, but they're able to go from
*  a version where it works at 30 to 40 hours, which is obviously prohibitive for most usage,
*  down to now they can get it to work with one hour of data because they're tapping into this
*  like shared latent space that they've created from other individuals. So I think that is pretty
*  interesting. I asked him a question about, can we say anything about how similarly people perceive
*  the same thing? And he said, unfortunately, in the data set that they're working with,
*  there's very little overlap between the different images that people saw.
*  So on the one hand, you would say, in some sense, that maybe suggests that there is a high level of
*  generality because they're able to get this shared latent space to work even when people mostly didn't
*  see the same images. On the other hand, it creates a limitation in terms of, can we say what the
*  inner product of my CLAWD3 conception and your CLAWD3 conception is. Unfortunately, in this study,
*  people just didn't see the same thing enough for them to be able to do that sort of analysis.
*  But I did find it quite interesting, truly profound, quite interesting is another statement.
*  It's a profound observation that you can get with only seven individuals whose brains vary in size
*  by up to 40% to a shared latent space that is general enough that you can just come plug another
*  individual onto it with basically one hour's worth of calibration data from an SMRI.
*  Yeah, no, that's wild. It really is. And I think we're just scratching the surface there.
*  Like I said, I don't know that we're going to get to my Mozart and your Mozart or whatever,
*  but I also think that there's a really wide space. There's a lot of surface area that you can reach.
*  So yeah, and anything that makes it easier to collect data is particularly appealing because
*  having to have people go through these things for 30, 40 hours is an unreasonable collection. So I
*  suspect that we will see an acceleration of all this pretty soon. It's going to happen pretty soon.
*  And I don't know that EEG will be the technology specifically. There's one other approach called
*  ESMRS, functional near infrared spectroscopy. If you almost think of it as like FMRI,
*  but that you can wear around in a consumer device, it's not going to give you the 3D
*  depth that FMRI is, but it's doing the same thing where it's blood oxygenation to measure brain
*  activity. It is actually pretty simple. It's pretty comparable to EEG in terms of what it can do
*  and in terms of its costs and things like that. So it could be that, but I think that there are
*  devices that I can imagine existing that are not the full brain computer interface that we're all
*  dreaming of or like what Neuralink is doing, but it can take you to some pretty interesting
*  directions. And by the way, it just as a side note, what Neuralink is doing is really kind of
*  just an invasive version of everything we're talking about here. So instead of putting the EEGs
*  or the electrodes on your scalp, they're putting a lot of them, very high density,
*  implanted in the brain with some silicon on board that can do some of this ML sensor processing
*  right there for latency purposes. So what you saw with the guy playing chess on a computer
*  with an implanted device is very impressive. And it's amazing to see some awareness of these issues
*  coming up. Also not shocking. You want to describe that just in case people haven't actually seen it?
*  Yeah. There I go thinking that everyone's as engaged in this as I am. So yeah, this is the
*  first patient of Neuralink is a young quadriplegic, a very sad case. He had a diving accident,
*  something like that. Doesn't have any use of his arms. And he had the Neuralink implanted and was
*  able to manipulate standard Windows computer. If you've ever used Windows, this is exactly the
*  same. It's not some special software. He's just using Windows to move the cursor around to play
*  chess. The first night that he got all this hooked up, he stayed up all night playing Civilization
*  6, which I can relate to. And yeah, so just this amazing ability to more or less fully use a computer.
*  And with devices like this implanted, typing has been demonstrated not in a way that a consumer
*  would ever want to use, but typing has been demonstrated with non-invasive technology. You
*  can do that with non-invasive EEG. But being able to just fully manipulate a computer and live at
*  least a digital life, surely with the brain, was what he was able to do. And again, amazing,
*  but not something that would come as a galloping shock to anyone who's been paying attention to
*  this. We've seen stuff like that before. And a lot of what Neuralink actually has done in kind of a
*  classic Elon Musk fashion, one of the most important innovations that they have done is the automated
*  surgery device, the robotic surgeon that can do this more or less without human intervention.
*  There's Elon Musk thinking about not just how do I bring innovative technology, but how do I change
*  the cost structure? He's thinking along those lines. So he's obviously thinking about wide scale
*  deployment or something like this. Okay. So can we summarize, or maybe there's a couple other
*  high level data points that could bring all this into focus to zoom out and give this the sort of
*  survey view of where we are in the taxonomy. So it's two directions in which information can flow.
*  We have focused on reading of the brain states, not yet the ability to change the brain states,
*  except in as much as various sort of the feedback thing of like you measure and then you show that
*  to the user, then they can get into a certain rhythm and react to the measurement that they're
*  seeing. But that neurofeedback is not direct manipulation of the brain state. And then within
*  this reading half of the equation, there's a lot of different technologies. We've got stuff that's
*  outside the skull is subject to just really noisy signal, a lot of challenges with that.
*  But with the EG, you do get high frequency of signal. Then you've got the fMRI, which is
*  a million dollar machine or whatever, certainly not something you can wear around gives you
*  a much better spatial resolution. You can really see what's going on at a finer grain level,
*  but less fast. There's some idea that these two modalities might be merged. And there could be
*  some really interesting generalization based on that. You can maybe unpack that a little bit more.
*  And then in terms of what we can do with it, it's like with just a couple of electrodes on the head,
*  you can do basic stuff like are you asleep or are you awake? With a lot of electrodes on the head,
*  you can do reasonably advanced stuff, although it's still kind of clumsy and slow. Like you can type
*  with your brain. Neuralink then is going inside the skull and that gives them a much cleaner signal
*  and gives them the ability to have higher bandwidth. That's kind of the whole value prop that
*  UNESCO is talking about over time. Are there other memorable kind of striking demos or products that
*  you think people should understand that are coming out of all this work that they could go check out
*  or watch a little demo videos of? Yeah, I would say robotic control is definitely always worth
*  looking at. And you can find if you just Google EG robotic control, they're not really devices.
*  They're not like marketing devices to do this, but you can find a lot of laboratory settings
*  where it's been done. Beyond that, there are all kinds of interesting headbands, things like that
*  that you can wear sometimes like headphones to. Over-ear headphones is very common with a band
*  over them and they integrate the EEG into the band that goes over your head. There's a lot of
*  products like that out there and they're not fantastically expensive. They're not super cheap.
*  Usually somewhere between $500 and $1000 would be roughly my estimate. In terms of the brain
*  computer interface though, the company that I know of that is furthest along in this regard is a
*  company called Emotiv. E-M-O-T-I-V. And they are the ones that I was referencing earlier. The little
*  V.I.Y. that you can buy them and use them at home and pair it with software that allows you to do some
*  very low-level manipulation of objects. You mentioned though, what might be the next
*  sort of level of generalization that we reach as we get better data and we apply better model
*  architectures. Obviously, I don't know. There's been some interesting work on this in the lab is
*  better decoding of language. So the best way to put it is mind reading. So we've seen that with
*  image. There have been a lot of, in MindEye as an example, Meta has had some research in this
*  regard. There's a lot of people that are basically decoding images that you're imagining in your
*  mind's eye into using AI into a predicted digital image. Basically doing the same thing with text
*  word by word at first, eventually getting higher bandwidth and higher latency. That seems achievable
*  and that seems very interesting, particularly when you think about it in the context of communicating
*  with an LLM, prompting an LLM with thoughts. As we were saying at the beginning of this conversation,
*  the challenge but also sort of opportunity with a frontier LLM is how good is your question?
*  And the better your question, the more precise and tailored your question, the better an answer you
*  will get out of these systems. So some people just don't have the communication capability
*  to ask exactly the question that they want to, but they can surely think of it. So can that
*  start to be translated into questions that could prompt an LLM? I don't know. Maybe. Certainly it
*  seems to me that basic motives could be. So I think about something like this device that came out
*  at CES this year, the Rabbit R1, which uses that thing that they call a large action model.
*  An LLM that translates what you want into intense, basic intents. I also think about something like
*  the iPhone and Apple devices in general have these automation layer called shortcuts, where you can
*  make little modular pieces of software to do a simple thing. Could we start to translate thought
*  into basic actions like that? Maybe not my thoughts on a painting by Picasso, a very complex
*  set of thoughts, but maybe I want to see what my schedule is for today. I want to see what the
*  weather is for today. I want to turn the bedroom lights and things like that. Can we translate that
*  and then use existing AI infrastructure, sort of automation infrastructure currently being built
*  to actually just perform that? And essentially that might feel shockingly like telepathy.
*  If you can think, I want to turn the lights downstairs off and they will turn off.
*  That might feel shockingly like telepathy. In a certain sense, the really stone cold reality of
*  where we are, but everything feels like it's converging to this point where a real qualitative
*  leap is possible. At least it seems to me like it could be in the relatively near future. But
*  to your point, to get to the brain computer interface that we all really want, you need
*  write access, not just read access. Yeah. Let's sketch out a little bit more the,
*  how does this tip over the next couple of years? It seems like the model is basically,
*  this is a bit hackneyed now in the AI space to put everything in terms of what GPT level are we at.
*  But it seems like we're at GPT-1 on this, maybe between one and two, where it's like
*  GPT-2 was just barely starting to be useful. When fine tuned, you could do some interesting
*  things with it, but you couldn't do much with it. It certainly wasn't doing much in the way
*  of reasoning. It didn't have the few shot learning ability that emerged with GPT-3.
*  So you could do classification type tasks or some sentence completion perhaps, but very limited
*  application. And it seems like we've sort of managed through mostly basic science
*  to get to the point where we've got a similar level of capability.
*  And you've got links here in the show notes that we can include so people can go check out
*  in visual form, like what these devices look like. But there's eight or so different consumer devices
*  that have seen enough there where they're like, somebody's going to want to buy this. Let's get
*  started building a company on it. And where I see this really changing is akin to robotics to
*  the amount of data that is going to be generated as the products hit the wild,
*  even with the early adopter set, it seems like it just goes vertical compared to what has existed
*  before. Keeping in mind that MindEye 2 is eight patients, a total of 200 and some hours in an MRI
*  across eight individuals. Now you've got things that are going consumer. So you've got orders of
*  magnitude more data flowing in, and you have people that are actually attempting to use them.
*  And so you're going to start to get feedback on what is working, what is not working.
*  And so the data regime is just totally changing. So there's ultimately a very simple story. It's
*  like we've gotten through enough basic science to get to the point where there's just this kernel
*  of utility, which is going to tip us into a much faster bootstrapping dynamic where we're going to
*  soar through orders of magnitude of data available. That of course, we've already got architectures
*  that can probably decode that signal. If there is enough data to learn from, the same machine
*  learning techniques are working everywhere. So unless there's some very odd reason why they
*  won't work here, the data is about to come online. And that's going to be the big unlock that's going
*  to allow for just tremendously more utility. And we might hit some limits around just how
*  good of a signal can we ultimately get. But it seems like at a minimum, we are headed for
*  this sort of stored procedure triggering that you mentioned. For image decoding is obviously
*  what you're seeing is already quite decodable. What you're thinking about in turning that into
*  verbal form seems like very achievable. And then even control seems like it likely gets refined
*  to the point where it's practically useful, if not super smooth, just based on collecting a ton
*  of data and applying known machine learning techniques to those signals. Is that basically
*  your world model or how would you refine what I just said? I think that's pretty much spot on.
*  The GPT-2 comparison is an interesting one. I recall back in my housing policy days,
*  kind of YIMBY adjacent, build more housing is what YIMBY means. Build more housing to make it
*  cheaper, to put it simply. I tried to use GPT-2 to analyze municipal zoning codes,
*  segments of municipal zoning codes, to give me just a thumbs up or down on how restrictive was it,
*  how not restrictive was it in an automated way. And the answers that you could get out of it
*  compared to now are just so simian, was like, good, bad, kind of thing. And you look at where
*  we are now. The difference, of course, is that language is a kind of ground truth that you can
*  refine your understanding of over time. And the question really is, how consistent is the language
*  of thought across people? I think that's the fundamental barrier, potential barrier, is how
*  calibrated does this have to be? And ultimately, if I have to go get an fMRI scan to make any of
*  this useful to me, then that kind of really changes it a lot. Maybe I'll do that. I feel
*  like the craziest thing in the world, actually. How long does it take to go buy an Apple Vision Pro?
*  About half an hour.
*  Demo is 27 minutes. Yeah.
*  Yes. How hard would it be to put an fMRI in the back of an Apple Store or something? I don't know,
*  but still, it changes it for sure. The level of calibration to me is really the big open question
*  here, both on the interpretation side and the imaging or the skull side. But I have to think
*  that substantial progress can be made and that it is possible to at least translate impulses,
*  desires, basic desires, and that that can be fed into various kinds of AI architectures that
*  can take actions on your VM. That just seems super possible in the near term. I would be shocked if
*  that didn't happen in the next five to 10 years. Maybe less, maybe a lot less. That basically is my
*  knowledge. Yeah. I see a parallel also between the fact that all these devices exist and the
*  current state of AI agents, broadly, where it's like everybody sees where the technology is going.
*  In the case of the agents, it's like, yeah, GBT-4 wasn't quite trained. There's this weird juxtaposition
*  where it's closing in on an expert level on things like medical diagnosis, but then it sometimes can't
*  click the right button on a very simple user interface or gets stuck. It gets into loops that
*  it sometimes can't break out of. Why is that disconnect there? Presumably it's because there
*  wasn't really the task completion mid-length episode data available to train the first version
*  of GBT-4 on. I strongly believe now that big tech leaders are investing heavily in creating that
*  mid-length episode data and that in all likelihood, I would bet reasonably confidently that the next
*  big shift is going to be that those sorts of things are going to start to work, even if the
*  MMLU score doesn't go up that much in the immediate term. To close that thread, when that happens,
*  then all these agent products start to work dramatically better all at once. I can't
*  suspect that dynamics question we talked about earlier. On the brain-computer interface side,
*  it does seem similar where people are developing all these different form factors. You've got
*  glasses, you've got helmets, you've got headbands, and they all don't work that well because there
*  wasn't enough of the right kind of data to train them on. But you also had to get these things out
*  there to get that data. I don't know that OpenAI necessarily had to have all these agent products
*  created. I think they probably could have created their own data. But in this field, you actually
*  need readings off of a lot of brains. It seems like we're in this similar space where the hardware
*  is starting to ship. It doesn't quite work, but again, it's going to collect a lot of data. Then
*  you can imagine a lot of these things turning on relatively quickly and being just a lot more
*  advanced, perhaps without even necessarily needing major upgrades to the hardware.
*  If you already have a 32-channel thing, that may well be enough for a lot of use cases
*  if you can decode the data effectively. Maybe it'll take more than 32, but it's just... Do you know
*  what is the number of electrodes that the guy from the Neuralink patient had?
*  That's a great question. I don't know exactly, but it's a lot. They're very dense. It might be
*  a thousand plus. I'm not actually a hundred percent sure of that, but it's quite a bit because of the
*  sort of fibrous way that they're doing the implant. It is very dense and fine.
*  Google both traditional search result and generative search result comes back with 1024
*  electrodes. Yeah, so it's a lot. The problem though with that, obviously, is that it's a lot
*  in a very specific place and there are long-term issues with that. Invasive is very promising in
*  terms of capabilities, but you got to have them all over the place. The EEGs, they do have the same
*  problem that the non-invasive ones have when they're implanted in this field. They can't read
*  everything in the brain. They can read in very local areas. They can read down to the neuron level
*  invasively, but they can only read locally. So same problem. And also obviously, like the idea
*  of connecting an EEG in my brain to the internet is absolutely terrifying. That's right, just from
*  a cybersecurity perspective. So there's obstacles there too. Yeah, but one other thing that I do
*  think about though is in as much as these various platforms, the problem with foundation model agents
*  is that their test environment is the real world. They don't have a baby version of the internet
*  or computing environment that they can interact in. They have to use our computing environment,
*  which is weird and has all kinds of history to it and affordances that are for us that they don't
*  necessarily need that probably ultimately serve to confuse them and complexify the environment.
*  For them, it is why I mentioned the shortcuts idea from Apple's platforms is what they have done
*  is modularize the functionality of not just their whole operating system, but developers can plug
*  into this too. So third-party apps are modularized too. And Android, I believe, has something
*  similar. It's not just Apple. That's the kind of thing that again, it could like take off pretty
*  quickly and it could actually be local. So it could be fast. You could do this inference locally
*  in theory, if you had a sufficiently powerful compute on board, but it wouldn't be like, you
*  don't need like an H100 to do this kind of thing. Yeah. And then the other shocking thing is just
*  how little compute has been applied to this problem. Yeah, there's low hanging fruit. I have no doubt
*  about it. So yeah, that takes us to the right section of this, which from a technological
*  perspective is actually pretty simple for me to explain in a narrative way, because it's the same
*  basic principle. We want to manipulate electrical and magnetic fields. The problem is that everything
*  I described in terms of getting signal out of the brain in a clean way, those problems are magnified
*  substantially for getting signal into the brain, because that's really what your scholars
*  intended to do. It's not so much to keep things in, it's to keep things out. So there's direct
*  current and alternating current stimulation. Transcranially, this is not invasive, that
*  transcranial magnetic stimulation would be the magnetic field equivalent of that. The problem is
*  that there's been some promise, there's been some stuff that's been shown in the lab, but it's either
*  very expensive hardware, it's not writing that good hardware curve like the electrodes are,
*  by the way, which are getting denser, cheaper all the time, and the signal just diffuses. So it's
*  just erratic, it's impossible to focus, and it's very varied between people. So I don't really see
*  the magnetic or electric field manipulation as being all that promising in the long term
*  for neuromodulation. Some people disagree with what's called transcranial magnetic stimulation.
*  Some people disagree and think that is going to be the path if we can just get the cost down,
*  but right now the cost is very, very, very high. So it's just not what I'm focusing on, because
*  I'm interested in things that seem like they could happen in the relative linear future.
*  There is a technology though, this really was my exclusive focus when it comes to
*  non-invasive neuromodulation, it's called transcranial focused ultrasound. It's a very
*  old technology, it goes back a hundred years, but really its rebirth is in the past 10 or 20 years.
*  What this is, firing very high frequency sound waves at the brain, far outside the range of human
*  hearing, far outside the range of the hearing of dogs and cats, though there are animals that can
*  hear it, rats, bats, I think can hear it too, but that you can fire at a sufficient frequency
*  and amplitude and pulse to target pretty precisely into the brain and deeper than anything else can.
*  You can't get to deep brain regions, you can't write to the hippocampus, which is
*  memory, with this, but you can go a few millimeters, as much as a centimeter, into the
*  brain and you can target it very precisely. So it's a few millimeters to a centimeter of depth and
*  then millimeter level resolution spatially. So it's a very promising technology, also it's cheap
*  and also much like the electrodes, ultrasonic transducers are on a good hardware curve,
*  they are getting cheaper and denser year by year. The weird thing about TFUS, as it's called, it's
*  not very well understood how it works and it's just weird in principle that firing high frequency
*  sound waves into the brain makes you, that changes your thought in any way, that's just weird, but it
*  does. There's some who theorize that it changes the electrical receptivity of brain tissue in
*  certain ways that just make electrical signal flow more readily. There's a theory that it just
*  stimulates neurotransmitter release in the targeted regions of the brain, but no one's really found
*  any safety problems with it at reasonable dosages. At high dosages, it has a thermal effect,
*  as we see with other ultrasound. At a very high dosage, it can cause brain tissue to heat in a
*  way that you probably don't want. The other thing from a safety perspective, of course, is that all
*  of these things are done one time in a lab. Nobody has modeled what the long-term effects are
*  of using this, for example, every day, but it's very promising. The FDA says it's safe below a
*  certain level and it's been shown to do some shocking things in my mind. So we've talked a
*  little bit about improving bandwidth. Maybe the single most interesting finding to me of this whole
*  chain of research that I've done is this finding that with TFUS at the somatosensory cortex,
*  fired at the specific regions of basically your tactile sensation, the part of your brain that
*  measures tactile sensation, you can perform tactile discrimination tests. So basically,
*  you cover the user's eyes and rub a pin on their hand and then rub two pins really close together.
*  If they can distinguish between the one pin and the two pins. TFUS was shown to improve that
*  when it was being fired at the brain. Also, it had some offline effect too. An offline versus
*  an online effect. An online effect is do we observe an improvement in the desired cognitive
*  activity when the treatment is actually being applied? Offline is do we observe it afterwards?
*  And 40 minutes afterwards, the discrimination attenuated a little bit but was still there.
*  So it had a long-term effect on what it would seem to me is the brain's channel bandwidth
*  to the hand. So that is very interesting. There's a lot of other things that it's done too.
*  Mood, focus, visual acuity and visual discrimination tasks in the same way that
*  I described with the tactile discrimination. You can actually induce complete changes to the visual
*  field or at least noticeable changes to the visual field by inducing these what's called
*  phosphines. If you imagine when you shut your eyes and you lightly press with your fingers on your
*  eyelids, those kind of blobby shapes you see, those are phosphines. You can induce that in
*  a person's visual field using TFUS. Auditory discrimination also goes up. Another finding
*  that interests me too is the people can discriminate between vibrations at different
*  frequencies that are very close together. They can do that discrimination not substantially
*  but marginally better with TFUS. And all of these studies for the most part are TFUS applied at
*  fairly low dosage levels, well below where that thermal effect is seen that I mentioned. So
*  there might be an interesting range of capabilities that you could obtain if you were to go beyond
*  that dosage level. And I've talked to both of the leading scientists in the world who have had the
*  top TFUS papers in the last 10 years and they've both said we are very confident that you can
*  increase dose safely at this point. That's TFUS. And can it write thoughts to the brain? Like
*  absolutely not. And I don't even want to suggest that I think that's like remotely close. I think
*  that's really hard. That's my intuition. But this idea of being able to improve not just mood
*  but things like channel bandwidth in the senses, that's really interesting to me. So yeah,
*  any questions? So you had said that the skull is a huge barrier in the most obvious way to
*  getting these signals into the brain. It seems like that's also a problem on the way out.
*  We sort of compensate for it by just like having a bunch of electrodes all around and collecting
*  the mess and then trying to clean up the mess. But on the way in where the precision really
*  matters, that becomes a big barrier. Is there an evolutionary story for why the brain would be
*  good at this? Or do you think this is just like an accident of biological history that the brain
*  blocks these electrical signals? I think it probably has to do with the fact that it's
*  probably useful for all kinds of other reasons for bone, just in general to be low conductivity.
*  And the skull is made of bone and you just benefit it there. I have no idea though. That's an
*  interesting question. I'd love to ask an evolutionary biologist that question. I will say that with TFUS,
*  the exact same imaging problems are present. Weirdly enough, in certain cases, the skull can
*  actually have a beneficial effect on getting ultrasound signal into the brain. It's the kind
*  of signal you're trying to create and the specific region of the skull is just right. It can actually
*  have a lensing effect. But in general, you still have to deal with signal processing and sort of
*  attenuate modifying your signal based on a dynamic model of the skull. You still have to do that.
*  It is crazy that this ultrasound is basically just vibration, right? Sound is vibration. This is just
*  high frequency vibration. And I don't know if you know the frequency off top of your head that this
*  operates at. Like middle A or middle C, the tuning note in the orchestra is like 440, right? So this
*  would be like, you go up several octaves, we can definitely still hear up into the range of a few
*  thousand hertz, it seems. And then I guess this would be like north of 10,000 maybe? I think it's
*  five to 10, usually in that range, five to 10,000 hertz. Yeah, it's weird, right? At a neuron level,
*  this basically amounts to shaking the neuron, right? It's like this thing can sort of fire
*  off its electrical signal a thousand-ish times a second or sometimes even faster as you said earlier.
*  Now we bring in a literal physical shaking that comes in at an even higher frequency than that.
*  And that seems to kind of wobble things loose and just, this is stimulus, right? Is there a
*  suppressive effect that can be achieved this way or is this purely a stimulus technology?
*  Most of the literature I've seen is for excitatory signals, but no, you can do inhibitory effects as
*  well. So yeah, you can block certain things too. And do you have a sense of what is the difference?
*  If I'm imagining shrinking myself down to neuron scale and sitting in this region of the brain,
*  it seems that the vibrations coming through, like how would I know whether they're supposed to make
*  me do stuff or not do stuff in my particular local area? Yeah, that's a very good question.
*  I'd love to ask one of the scientists who helped me with this research, I'd love to ask them this
*  question. That's a great practical question for them. My general sense is that most of the
*  inhibitory stuff is not that much inhibitory stuff that actually gets done. Let me actually quickly
*  pull up my notes. I'll get you an answer to that question on what specifically has been inhibited,
*  at least, because that might answer the question. Yeah, so the inhibitory TFUS, most of it has been
*  used for pain attenuation. So it's looking at the parts of the brain that are sensing pain and
*  targeting that. And that seems to work for whatever reason. I don't think that is well
*  understood at all. I don't know for sure. But that also has the side effects of reducing
*  motor time, reaction time for various kinds of motor tasks and can reduce some of the things
*  we were talking about. Yeah, it seems there's also even if it was purely stimulating activity
*  in a particular region, it's an important fact to keep in mind that the brain is self-regulating
*  in all sorts of ways. So we see this at the cellular level too. There is a gene that gets
*  expressed to suppress the expression of another gene. And at the brain level, there are regions
*  that activate to suppress other regions. And so you can imagine, even if you could only turn things
*  on in many ways, that might allow you to turn things off if you can figure out the indirect
*  pathway to get there. It doesn't sound like that's what's going on here, but
*  conception. It might well be what they're doing. That could very well be the case.
*  It is definitely inhibitory in terms of activity though. And I don't have a good model for why that
*  works. The excitatory is at least intuitive. If anything, it's a little like, well, if you
*  shake the TV set, it generally fixes the signal. There's a primitive part of us that can understand
*  how that works. But yeah, the inhibitory is a bit more of a puzzle to me as to why that works.
*  So this question of writing thoughts, I'm not sure we ever would want this exactly anyway,
*  but putting that aside, I can start to imagine how you might close the loop here. Maybe there
*  are some barriers that I'm not immediately seeing. I'm sure there are plenty of challenges that would
*  have to be overcome, and I'm not seeing any fundamental barriers. The resolution on this
*  technology was down to a couple millimeters as well, right?
*  That's right.
*  That's notably the same scale as the voxels that come out of the
*  fMRI. And so if I connect this to the MindEye paper again, and I'm like, okay, there are 12
*  to 17,000 voxels per person back in the visual cortex. And I got a mini lesson on this in that
*  episode around how much semantic information is encoded in the visual cortex. Is that just raw
*  sensory workup into lines and edges? And then the front of the brain does the sort of that's a
*  tiger type stuff. And Paul, the author of this paper, he said, no, still in the back of the brain
*  as part of the visual cortex, there is a lot of semantic information that understands what it is
*  that you actually recognize as conceptually what it is you are looking at. So from these 12 to 17,000
*  voxels, two ish millimeters cubed, they're able to extract both a general sense of the image that
*  you're looking at, like, what are the colors? And what are the regions of the image? Which part is
*  dark? Which part is light, whatever. But then also, straight from that reading, they can predict a
*  caption for the image from the brain state. And that's because there is enough semantic
*  information there that not only do you have this kind of blurry, purely visual information,
*  but you also have this conceptual information. So anyway, point there is that you could read that
*  at a two millimeter cube level. And now you're saying that you can also focus this signal down
*  to that same kind of scale. It seems like the possibility at least conceptually exists to
*  create a feedback loop where you might say, okay, I want to send some signal. How do I know that I
*  sent that signal? I also need to then read the signal back. So you can focus the signal down to
*  a couple millimeters region, but maybe you can't do that 10,000 wide, maybe you'd have to do that
*  10,000 voxels at a time to induce meaningful higher order concepts in the brain. But it does
*  seem like you at least now start to have some ability to make a perturbation and then also
*  read it on the other end. And if you have a sense for what it is you're targeting,
*  I want you to be thinking about cloud three. There seems to be at least some ability to start to be
*  like, okay, I'm going to send a signal and then decode what states arise from that. And was the
*  person thinking about cloud three? Yes or no. Then I update my network that is deciding what signal to
*  send in based on the signal that is later read out. And this seems like a leap, but given what
*  we have seen work, it doesn't seem too crazy to think that you could start to close this loop with,
*  was I able to induce what I was trying to induce? Maybe the reward is too sparse. Maybe you need to
*  have broader regions subject to receiving a signal at the same time to really get anywhere. If you
*  can only target one, two millimeter cube, maybe that just gets lost in the overall broader state
*  of the brain. But I'm starting to at least imagine how you can close a loop and begin to reliably
*  induce certain things because you can read those things. And that gives you some ability to
*  correct or to gradually learn how to do the inducement in the first place. I'm not sure
*  what other big barriers there would be to doing something like this, but it also seems like there's
*  plenty of possibility that things could just be quite odd. And maybe you don't actually need that.
*  If you really could figure out how the brain works, all these thoughts arise somewhere and
*  they presumably arise locally first. There's some trigger that ultimately propagates through
*  broader regions of the brain, but starts with some input or some signal that becomes dominant in the
*  moment and ultimately rises to the level of consciousness. It seems like it's not crazy to
*  think that maybe you could find the key levers through this process of attempting to know,
*  would we do this on humans? Maybe not, but you could definitely do it on monkeys. And I bet we're
*  similar enough to monkeys. We could even create like a shared latent space with some monkeys
*  at some point to get to the point where you could say, yeah, I'm just going to run this loop a ton.
*  I'm going to try to induce these things. I'll measure how close did I come. I'll update on that.
*  And even if I don't have the ability to stimulate that much of the brain at a single time,
*  potentially I can find the key that unlocks the lock to induce the states that I want to induce.
*  Possibly crazy, but what if anything would say that can't happen?
*  The main thing is that we don't really understand at all. As far as I know, we don't have a good
*  understanding of how information is encoded in the brain. And it can be read back when you're
*  doing things like the mind eye, the fMRI, and especially when you're pairing it, like when
*  you're looking at the visual cortex, you can kind of like extract out of it. But actually,
*  the right process, like how do you do that? Where does the right happen? Probably more than one
*  place, right? Like the thing that distinguishes brains from even the most sophisticated neural
*  networks is just how much crosstalk there is and how much weird resonance and just all sorts of
*  feedback that's constantly being conveyed. And I don't think we have a good understanding of that.
*  Would I be shocked if you were able to induce a simple thought in someone's mind
*  by firing ultrasound at V2, the visual cortex? Well, no, I would be pretty surprised if that
*  worked. It wouldn't be a galloping shock to me because of the informational aspect of that.
*  I'm not sure that high dimensional information can be, first of all, encoded in instructions to
*  ultrasound, to ultrasonic transducers, and then successfully transmitted into the parts of the
*  brain, probably several, where it would need to go in order to actually write information,
*  particularly of any... I'm thinking of the moment in The Matrix where Trinity downloads the
*  instructions for how to operate a helicopter. Thinking of that as being your North Star.
*  That seems hard to encode in all the various ways they would need to be encoded.
*  But I wouldn't rule it out. At the very least though, brain activity is possible to stimulate
*  and it is possible to change the mood of the wearer, the level of focus that they have,
*  things of that nature. All possible. We don't know how much and how high dimensional that can get.
*  Obviously, a good mood is a pretty general concept that could be refined quite a bit.
*  There's a few TFUS devices that are on the market. There's a company called Prophetic AI
*  that is based in New York. They've had a lot of buzz on X and other social media with some of
*  their various announcements. There's a couple of things that are really interesting about what
*  they're doing because it is actually kind of the convergence of a few of the things that we've
*  talked about in this discussion. First of all, they have developed what they call an ultrasonic
*  transformer, which is a transformer based system trained on EEG and fMRI data, which takes as its
*  input EEG readings from the headband that they're going to sell and outputs instructions to the
*  ultrasonic transducers also on that same headband. So it's inferring your brain state and then it's
*  turning that into instructions for neuromodulation. Their ambition is to do this with lucid dreaming.
*  It's actually a pretty easy signature. From an EEG perspective, this is not hard. You can absolutely
*  recognize that somebody is lucid dreaming while they're sleeping because the neurosimetry of sleep
*  is pretty consistent, pretty easy to recognize even for low channel EEG. Then there's a spike
*  of gamma waves in the prefrontal cortex. It recognizes that spike and then it directs the
*  transducers to just keep firing to maintain that brain state and keep you in that lucid state.
*  They might have slight corrections to that description, but the basic idea is that it
*  can keep you inside of a lucid dreaming state. They also have ambition to do quite a lot of other
*  stuff. Conscious experiences of all kinds, much higher dimensional conscious experiences. They
*  want to start with focus and a positive mood, but they have ambition to go beyond that. A lot
*  of other people that are operating in the space have ambition to go beyond that. Again, you're
*  writing a positive hard record. Just like you are with EEG. Yeah, the how high dimensional is thought
*  is it's really, I'm thinking about the representation engineering work that recently came out of
*  Case and other there's been a bunch of authors on that paper, but they identify these high order
*  concepts through clever, but honestly it's not even that crazy of a technique where they
*  create a bunch of different contrasting pairs that show like the presence and absence of the
*  positive and the negative of a concept of interest and then create enough pairs of those and then
*  run them all through and then look at these intermediate states and then take the averages
*  and are able to basically say, okay, this appears to be the general direction trying to kind of
*  let the noise cancel out that represents the direction from unfairness to fairness or the
*  direction from sadness to happiness. And then they can start to use that vector direction to
*  detect those states in further downstream inferences blind, right? Just looking at the
*  activations and saying, is this a happy state or is it an unhappy state? And then they can also
*  start to layer those in and shape behavior based on just adding it to the whatever the thing is
*  doing at a given time. If you just add on the happiness direction, then you can see that you
*  actually steer the downstream model behavior in a reasonably intuitive direction where it seems
*  like, okay, now it is actually generating happier outputs. So that is way, way easier to do in a
*  neural network than it is to do in the brain. And the dimensionality of that is pretty high.
*  So it might just be an engineering challenge that is like, at least in a non-invasive way,
*  just too crazy to get to. But it does seem like we have something pretty similar going on.
*  And you're citing all these examples where it's like, you're doing that at basically a low
*  dimensional, very crude sort of way. And as we get into these higher and higher level concepts,
*  I also think about the entropic sparse autoencoders with this, where they show that basically
*  from these high dimensional states, you want to identify these human intuitive concepts.
*  And the more space you give the sparse autoencoder, the more concepts it will find. They
*  call this feature splitting. So if you don't give it that many, if you give it like a limited number
*  of concepts that it can differentiate its activation space into, then you'll get high
*  leveled, kind of more general concepts out. And if you give it a lot more space, then the features
*  will split and you'll start to see these very granular level representations. And it seems like
*  we're just operating right now at a very, very general level. We have not yet got to the level
*  of resolution where the features can split. And so we're making these very basic modifications
*  to mood, but it seems like it's really a question of resolution more than anything else over time.
*  Yeah, resolution and it might also just be data, the same data problems that we talked about earlier.
*  And then obviously with TFUS in particular, that's even more limited of a data set. It might be some
*  combination of all those things. And yeah, but I don't know how far it can go. In principle,
*  any conscious state is inducible, but how far can that go with non-invasive? My guess would be
*  somewhere between exactly what I'm experiencing right now at the high end and being happy at the
*  low end. I would suspect you can do more than that, more than being happy, less than what I'm
*  experiencing right now. But where exactly? I think we just have to find out. It is though possible,
*  it takes some time to even get your head around what that would be like. The closest thing
*  is probably drug use. I really don't want to say that this is like using a drug,
*  because I think that this might be much more than that. And I don't even necessarily mean
*  illicit drug use. I just mean something that's meant to enhance your mood. But even then,
*  my guess would be that because of the sort of slower mechanism of action that most pharmaceutical
*  mood drugs have, it's going to feel like it's coming from inside you more. Whereas something
*  like TFUS, you will feel good or focused suddenly. I don't know exactly how long the feelings
*  persist. I would be shocked if it were like a steep drop off, like a completely like cliff,
*  but it is also probably fairly quick that it drops off. And certainly, I would guess that the
*  experience of using something like the prophetic headband to lucid dream, if you use that every
*  day, it would be like ticking LSD every single day. And you would eventually go into a Syd Barrett
*  doom loop would be my guess. But yeah, how far can you go? I have no idea. It's very early days.
*  This is very much at the frontier. At the same time, immediately gradable into consumer hardware,
*  not expensive. And FDA approved below a certain limit. I'm happy to explore this more. That might
*  be a good segue into some of the policy. I am a policy person. Before we go into policy,
*  let me just ask one more kind of technical intuition question. If I had to make a high
*  level guess this on everything we've talked about, it feels like I would put my money on we're going
*  to have pretty good brain reading in consumer devices over the next few years, because the
*  hardware is already there and the cost curve is good. And the data is about to explode. And the
*  best thing to interpret one neuron that is another neuron that on the other end of the right or the
*  modification to brain state side, it seems like resolution and just the overall ability to
*  accurately send the signal that you want to send is limited. And seems like it's probably going to
*  continue to be limited relative to the bandwidth you would actually need to create really rich
*  input signal to the brain from outside the skull anyway. And so we're probably headed for something
*  that is like fairly crude and sort of valence level, but we're not going to be invoking or
*  reducing thoughts of Cod3 opus with precision with those sort of non-invasive techniques.
*  And so if those things are to be done, it seems like they would require invasive techniques.
*  And at that level, then you can actually send the signal where you want at the obvious cost of
*  having to implant thousands or potentially many thousands of electrodes into the brain.
*  But what would the path be if there is to be a path to something like the Matrix moment where
*  you could randomly download skill sets or knowledge bases or whatever, or even just create the sort of
*  mind control to get people to act in whatever way you want them to act with the current technology
*  landscape that seems only plausibly feasible through invasive methods.
*  Yeah, I totally agree. The only thing I'll say just as a caveat is that the spatial resolution
*  of TFUS and the spatial resolution of EEG are basically the same. There might be practical
*  differences in spatial resolution that I'm not thinking of. The obvious one being that with EEG,
*  you can't differentiate between all the neural signals between individual neurons,
*  but you are picking up the collective aggregate result of their electrical activity.
*  Whereas with TFUS, maybe it is the case that you need neuron level or close to neuron level
*  targeting to create really rich experiences. But I don't know. At the same time, neural networks
*  tend to have a fair amount of redundancy. Would you say that's a fair observation?
*  There's a possibility that you don't need to get down to the level of the individual neuron
*  to do quite a bit. But in general, I agree with your intuition. That's about where I am too.
*  Cool. Then let's get to policy. And also, I wonder if you have any intuition for sort of as this
*  technology maybe follows its natural course, how does life start to change? Have you started to
*  game out dynamics at all and policy will be a part of shaping those dynamics? I used to ask
*  people all the time if the Neuralink had reached a million patients and was generally considered to
*  be safe, would you get one? And interesting for people that are like very much on the frontier
*  of AI, I got very different answers there. But some of the interesting answers that I got were
*  rooted in the idea that I'd have to, how else would I keep up? So I feel like there's some
*  game theoretic aspect to this and policy can shape the sort of game theoretic environment,
*  perhaps, and maybe can do other things too, including encouraging or discouraging the
*  development of different kinds of technologies. But I'm interested in both kind of how you think
*  this in the absence of governmental intervention, how it evolves, and then what questions government
*  can and should be asking and what maybe the most likely things are to happen in that respect.
*  Yeah, one of my favorite anecdotes, I'll go back to the 1910s for one second,
*  the interior design of the average American's house before, and you can just imagine like an
*  old house, right? Victorian house, whatever, beautiful houses in Detroit, dark red, dark green
*  walls you often think about, there's kind of like burgundy. Why? Why were all the walls dark back
*  then? That seems weird. The reason is that interior illumination was provided by kerosene lamps,
*  which stained walls. So you had dark colored walls to hide the stain. White walls are a luxury
*  enabled by electricity. My point only is that it is very hard to predict the outcomes of what
*  happens when these things are at scale. Obviously, like the things I can predict are going to pale
*  in comparison to what will actually happen. That being said, some things do seem apparent to me.
*  I always try to think about the legal system first. And this is an area that interacts with
*  the legal system, I think in really interesting ways. The concept of being under oath changes if
*  we want it to. And that's the question. And a interesting way of thinking about the next
*  20 years of technology in general is will we want to impose artificial constraints on various aspects
*  of social life and technological development? And I'm not saying that we should. I don't have a
*  strong model of that yet. But it does occur to me that if we're headed towards the Nicholas Bostrom
*  solved world, which I don't think we are, by the way, but if he's right, then one of the things
*  you will need is artificial constraints. Because my strong intuition is that a solved world quickly
*  devolves into hell. I really do believe that. Can you unpack what exactly you mean by solved
*  world? And then you're probably going there anyway, but more kind of granular specific questions. I
*  take it that you're asking, you can imagine a lot of different regimes, but would we require you to
*  wear one of these headsets to testify so we can also look at your internal brain states in addition
*  to your like spoken testimony? That's the sort of thing that you are getting at, right? Yeah, exactly.
*  The solved world is a concept from Nick Bostrom, essentially post singularity, techno utopia style
*  thinking, where every conceivable good is available in enormous abundance and humans have godlike
*  powers to assemble atoms in whatever way that they find desirable or self-themed does. Some form of
*  conscious life does. Maybe not us, but I'm not a big subscriber to any of that sort of techno
*  utopian thinking. But yeah, ultimately, it's a very different kind of society. If we can actually
*  know at a biological level whether or not you are lying, for example, right, that's just a profoundly
*  different society. Do we want that? Is a society with no deception actually a desirable thing?
*  Is an AI model with no deception actually a desirable thing? I'm not confident the answer
*  to either of those questions is yes. In fact, I'm like pretty confident that the opposite is the case.
*  I'm pretty confident some degree of deception is an important part of life. I think some degree
*  of deception is probably an important part of judicial life. In court, we assume that there
*  will be some degree of bending of the truth. And I think that thinking about court is a fascinating
*  way to think about how society will digest this. It's not the only way, but I just think it's a
*  very concrete way to think about it. What are the limits on something like a warrant or a subpoena
*  in a world where varying degrees of dimensionality into human thought is recorded and in theory
*  something that you can be examined for a court case? My instinct on that kind of a question is
*  that it's probably beneficial to a certain point, but there is an extreme where if everyone really
*  has Neuralink and really truly every thought you have can be recorded in a high resolution
*  production. You probably don't want that to be available to, certainly not for advertising
*  purposes. That's another thing I think about. Within limits, it seems fine. At the extreme,
*  it seems dangerous to have to figure that one out. And my general sense is that from a policy
*  perspective, sure, I mean, if this exists, the Europeans will regulate it, right? We know that.
*  And half of America at least will want to regulate it, whether or not they'll be able to
*  is a separate question. Actually, it's probably worth talking about just for a moment what the
*  current regulatory state of all this stuff is. So these are not considered to be high risk medical
*  devices by the FDA by and large. They fall into this category two, this mid level of risk, but
*  there is an exception to that, which allows you to evade most of the FDA's regulatory processes
*  if you are marketing a general wellness device. So I remember when the Apple watch came out with
*  its blood oxygen sensor a few years ago, it was during COVID. It was like in 2020 that watch came
*  out. Apple was extremely careful. And blood oxygen is an important measure for COVID. Apple was very
*  careful to say this has nothing to do with measuring for COVID. This is purely telling you
*  your blood oxygen level. Because if you connect the device to diagnosing or treating any specific
*  medical condition, then all of a sudden, you're in a whole different world. From a regulatory
*  perspective, neural technologies have generally gone for this general wellness exemption from the
*  FDA. The FDA has not actually been clear that that exemption applies to them. They've been asked to
*  make that clear and they have refused to do so, which is a common thing that the FDA and other
*  aspects of American bureaucracy tend to do. Anyone who knows cryptocurrency will also be familiar
*  with this, that a regulatory tactic is actually uncertainty. That is a tactic, that's a form of
*  regulation that regulators use is creating uncertainty and creating gray areas. So that's
*  where most of these neural technologies exist right now, is sitting in a gray area, they're
*  being marketed. And the reason that the FDA does that, I suspect, is maybe they don't know. Maybe
*  they don't know how they feel about it. That could be true. But also for sure, they probably want to
*  preserve the optionality to cut back on this stuff if they want to, and to remove all the general
*  wellness devices from the market in a heartbeat. But at the moment, if you could make a non-invasive
*  brain-computer interface that can induce all kinds of conscious experiences, and as long as you're
*  not trying to treat or diagnose a specific medical condition, and as long as you're staying below
*  certain thresholds of DFUS and other things, like there's certain safety guidelines, as long as you're
*  mechanically underneath those things, then you can just sell this on the general market. That's the
*  way, that's how it currently applies. And the final part of your question was about long-term
*  dynamics of adoption. And yeah, I think if these things are cognitive-enhancing devices, then there
*  will be evolutionary incentives. There are evolutionary incentives to do all sorts of things
*  right now that most people do not do. Right? Like we have enough data to know that I have
*  an evolutionary incentive to go on a jog after this podcast. Will I do that? Probably not.
*  That's the threat, or that I should only eat whatever Andrew Huberman recommends. Like all that stuff
*  is true, and yet we don't do it. Right? We don't do it all the time. We shouldn't be drinking alcohol,
*  but a lot of people drink alcohol. So, I don't know. And I see this in the AI safety community
*  in general. A lot of people think that legible Darwinian evolutionary impulses are going to
*  drive technology adoption in society. And I think it's more complicated than that. I don't think it
*  is a straight Darwinian evolutionary algorithm that's being applied here. So, that's my read on
*  that. And I also think that there's a flip side. I think the impulse that people have a lot of the
*  time is to think, oh no, if there's an incentive to use this thing, then everybody will have to use it.
*  And what about the people that don't want to use it? I go there too, right? I have sympathy for
*  those people. I think about the Amish. And I do think that there's probably going to be forms of
*  digital Amish in the future that we need to be thinking about. At the same time, the people who
*  want to enhance their cognition also should have the liberty to do that. And we should want there
*  to be more cognition in the world, especially human cognition. There's a part of me that says,
*  my God, like the idea that we would want there to be less human cognition in a world where GPT-5 is
*  right around the corner. I am not sure from what world model that impulse derives, but it is a
*  world model that I could poke holes at. Not that it's wrong, but I could certainly poke holes at
*  it. So, that's like, my mind is not at all made up on any of this, but that is how I model this
*  right now. I know you're potentially just a couple doors down the hall from Robin Hansen, who's also
*  a recent guest on the podcast. And he makes an extremely compelling case that we are in a
*  what he calls strange dream time between what are almost sure to be much longer eras, both before
*  and after us, in which evolutionary dynamics and just the practical constraints of available
*  resources are in fact the dominant drivers of how things unfold. And we're in this weird moment now
*  where we've created way more capital per capita and birth rates are down. And it seems like the
*  strangeness probably can't last in the course of evolutionary time scales. Then he also, it's funny
*  you mentioned the Amish too, because he also has a part of his near-term world model, which I think
*  is less compelling personally, but you can debate that with him over lunch perhaps, where he thinks
*  because of the lower birth rates in general, but higher among the Amish, we may be headed for a
*  period of technology stagnation and Amish domination. So, that gets a little fine grained
*  in terms of how precise the crystal ball has to be to advance a theory like that. And for me,
*  but there's definitely a couple of interesting lunch debate topics for you now at the Mercatus
*  Center with him. Well, for sure. And I think part of his point is like, not to put words in his mouth
*  at all, but we have a lot of artificial hyperparameters on the way society works. And
*  those things are called laws and policies. And that's what I study for a living. And yeah,
*  they've created all kinds of unintended effects. And that's not to say they're bad or good or
*  really any to say that they exist. And to say that things don't proceed according to mathematical
*  models of the way that history, nature has unfolded in the past for those reasons, because they didn't
*  have occupational licensing a million years ago. And that does change the way that evolution works
*  at a certain level, at least the evolution of society. And yeah, like just one other point
*  about the kind of digital Amish thing and just in general, my read on there's some polling that
*  gets put out about AI and things like that. I don't put a lot of stock in issue polling
*  personally. And I don't think they're coming from organizations that are motivated to find the truth.
*  I will just put it that way about what Americans think. I think the questions are along the lines
*  of someone's going to make how 9,000. How do you feel about that? It's coming to kill you.
*  It's gonna be here next year. What do you think? 98% of Americans are opposed to like, okay,
*  that's not that useful of a question. But issue polling is also not that useful of a field,
*  unless you do it really carefully. But I do think that these things, adoption of technology
*  is going to start to have a political valence to it. And whether that is coded as AI or whether
*  that ends up getting coded in terms of these neural technologies, or the Apple vision pro is
*  the Apple vision pro a political statement of a sort? Yeah, I see it as one already. I think a lot
*  more people will in the future. So I don't know exactly how to model that. But I do think that we
*  should expect this all to become more political, not just about who gets to control the existing
*  platforms, but about sort of whether you are interested in these technologies at all.
*  Yeah, unfortunately, I would love to see the discourse around AI and technologies like this
*  remain separated from day to day political discourse as long as possible, just because
*  it seems like everything gets worse once it gets cast through the lens of certainly partisan
*  politics. I'm not sure I agree with your view on polling in as much as I would say, like,
*  my read of a lot of those answers is that I certainly would agree that they're subject to
*  framing effects majorly. So definitely by that argument, my sense of just the people that I talk
*  to in life and they're outside of the bubble when I get outside of the bubble, their kind of
*  gut reactions to things is that it is negative by default. And arguably that has been shaped by
*  culture and fiction and the Terminator and whatever. But I do think there is something
*  quite real there that those answers are getting at. Though I also do think they're coming largely
*  from a position of ignorance, certainly when you're doing general public opinion polling.
*  So I always advise people I don't think we don't have too many chat CPT novices listening to this
*  show. But again, when I get outside the bubble and present like business leaders or whatever,
*  I'm always just like, okay, first thing you got to do, spend some actual time with the technology.
*  Like you need to develop your own experiential understanding of what this stuff is. You can't
*  just have it all be filtered through the media for you because the surface area is just so vast and
*  the range of different use cases. And it's just so big compared to what you can get in an article
*  or whatever. So you really do need to get hands on with it, feel it, mess around with it,
*  get it your data, see how it reacts to stuff that is really personal to you.
*  And if that's useful to you, and that also gives a great sense of its strengths and weaknesses in
*  doing that. Maybe in closing, I wonder if you could recommend some things that people might do
*  to start to get themselves acclimated to this merge technology tree. Again, a lot of people
*  follow this show will be very familiar with the language models. They'll have a sense for
*  where AI is and some sense of where it's headed. I would guess that most people have never worn
*  any of these devices. Even starting with an Apple vision pro, I would still guess that sub 5% of
*  the audience has even done the demo at the Apple store at this point. So what would you suggest?
*  Is it like going and watching the demo videos on the company websites that we can put links
*  to these companies in the show notes? Is it going and trying an Apple vision pro? What do people do
*  to start to orient themselves to this and start to develop their own, not just through the media,
*  not just by listening to you and me, but how do they get their own sense for how they should
*  start to feel about this technology? Yeah. First of all, I would just say in response to the polling
*  thing, I totally agree with you. People are passing this thing about this. That is a fact.
*  I think that the techno optimists like myself, we have it all the hell to fight. So I don't want to
*  suggest that the polling is like manipulating the reality. I think it's exaggerating a tendency
*  that already exists. That's how I would put it. Anyway, it's a very good question. I've never
*  thought exactly about what other people should do. I guess my somewhat myopic reaction is like the
*  path I took was useful enough for me. There's a good book about all this that came out recently
*  called the battle for your brain by Nita Farahani. She's done some great reporting almost
*  about this kind of stuff. And I would recommend reading that. I actually would recommend trying
*  on an Apple vision pro. And the reason for that is that you would be shocked how close your gaze is
*  to a kind of neural interface. And it is something we didn't talk about at all.
*  But it is probably the case that the ideal form factor for any of this kind of neural technology
*  we're talking about is probably something that wraps around the head, much as the meta quest and
*  the vision pro do. And so when you start to combine the idea of, well, we've already got
*  eye tracking, and we've got hand tracking, and now we're adding in the neural technology,
*  maybe the neural signal doesn't need to be that good to do something really interesting, right?
*  The whole different angle to approach this is a sensor fusion. So that's just one note.
*  But yeah, I would try a vision pro.
*  This is by the way, a breathtaking experience. I was really floored by just the demo. And I
*  haven't bought one yet, only because I'm not sure how much content there is and how much time I
*  would really spend in it. But it was definitely an eye opener for me in the sense that it was like
*  akin to a GPT-4 type experience where I have the Oculus 2. And when I first got the GPT-4 access,
*  I had been using a lot of GPT-3. But the step up in terms of the quality and the like, oh my God,
*  this is just an arrestingly different experience. It is a similar, you have to experience it to
*  feel the difference. I could tell you how much better GPT-4 is versus GPT-3, but the best way
*  is to get your hands on it. I would say the same thing, even if you have done like relatively
*  recent VR but not done the Apple vision pro yet, I would say you do kind of owe it to your own
*  worldview, if not necessarily to buy it, but at least to get that sense of what this thing
*  can do, how high resolution it can be, how immersive it is, just how compelling the overall
*  sensory experience of it is, because it is genuinely next level. And it absolutely feels to me like
*  a part of the future. I haven't quite figured out how to use it yet. The experience of it is
*  this is definitely going to be a thing. Yeah, no, I totally agree. And I think that
*  it's not entirely a neural interface, but it's also not not a neural interface.
*  So I would say like reading that book, trying an Apple vision pro. And beyond that,
*  unfortunately, my answer is boring, which is always try to proceed from ground truth
*  of actual empirically demonstrated knowledge and not narrative, because the narrative surrounding
*  this technology in particular is likely to be quite toxic and quite misleading in a variety
*  of different ways. So model it for yourself. That is my best advice. Don't rely on someone else's
*  model, including mine. In the future technology scouting business, it is important to maintain
*  always a high degree of epistemic humility. And I think that's a great note potentially to close on.
*  Dean W Ball, research fellow at the Mercatus Center and author of the hyperdimensional
*  sub stack. Thank you for being part of the cognitive revolution. Thank you, Nathan.
*  It is both energizing and enlightening to hear why people listen and learn what they value about the
*  show. So please don't hesitate to reach out via email at tcr at turpentine.co. Or you can
*  DM me on the social media platform of your choice.

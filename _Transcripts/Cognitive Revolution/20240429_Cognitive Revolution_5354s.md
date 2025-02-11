---
Date Generated: October 31, 2024
Transcription Model: whisper medium 20231117
Length: 5354s
Video Keywords: []
Video Views: 1461
Video Rating: None
Video Description: In this episode from new podcast Emergent Behavior (@EmergentBehaviorPod ) host @8teapi interviews the co-founders of Prophetic AI to learn how they're using AI to facilitate lucid dreaming. Prophetic had come up in the recent Cognitive Revolution conversation with Dean W. Ball about brain computer interfaces, and Nathan had them on the list of companies to invite on the show, so it was really fun to discover that Ate-a-Pi had already done an interview with them right around the same time.

--

Check out Nathan's new chatbot on www.cognitiverevolution.ai

--
SPONSORS:

The Brave search API can be used to assemble a data set to train your AI models and help with retrieval augmentation at the time of inference. All while remaining affordable with developer first pricing, integrating the Brave search API into your workflow translates to more ethical data sourcing and more human representative data sets. Try the Brave search API for free for up to 2000 queries per month at https://bit.ly/BraveTCR

Omneky is an omnichannel creative generation platform that lets you launch hundreds of thousands of ad iterations that actually work customized across all platforms, with a click of a button. Omneky combines generative AI and real-time advertising data. Mention "Cog Rev" for 10% off https://www.omneky.com/

Head to Squad to access global engineering without the headache and at a fraction of the cost: head to https://choosesquad.com/ and mention “Turpentine” to skip the waitlist.

--
TIMESTAMPS:
(00:00) Intro
(00:43) Diving Deep with Prophetic AI
(02:18) Exploring Lucid Dreaming with Halo
(05:08) The Technical Marvel Behind Halo
(07:25) A Deep Dive into Lucid Dreaming Experiences
(13:15) Sponsor:  Brave | Omneky
(14:42) Do All People Have Lucid States?
(32:19) Sponsor: Squad
(41:05) Building the Neural Model for Dream Control
(43:15) Exploring the Intersection of EEG, fMRI, and Ultrasound in Lucid Dreaming
(43:48) The Journey from Open Source Data to Targeted Brain Stimulation
(47:08) Collaboration with the Donders Institute and the Future of Lucid Dreaming Research
(48:40) The Role of Machine Learning and AI in Enhancing Data Collection and Analysis
(50:04) From Theory to Practice: Implementing Transcranial Focused Ultrasound (TFUS)
(53:51) Personalizing the Lucid Dreaming Experience through Reinforcement Learning
(1:16:18) Looking Ahead: The Potential and Challenges of Neurostimulation Technology
(1:22:55) Addressing the Skeptics: The Debate Over Natural vs. Technologically Induced Lucid Dreaming
---

# Organic Holodeck with Prophetic AI co-founders Eric Wollberg and Wesley Berry
**Cognitive Revolution:** [April 29, 2024](https://www.youtube.com/watch?v=WFqTvyc8lWY)
*  Hello and welcome to the Cognitive Revolution, where we interview visionary researchers,
*  entrepreneurs, and builders working on the frontier of artificial intelligence.
*  Each week we'll explore their revolutionary ideas and together we'll build a picture of
*  how AI technology will transform work, life, and society in the coming years.
*  I'm Nathan Labenz, joined by my co-host Eric Torenberg.
*  Hello and welcome back to the Cognitive Revolution. Today it's my pleasure to
*  introduce the new podcast, Emergent Behavior, hosted by AdaPi. Known for imaginative writing
*  on AI Twitter and in the Emergent Behavior newsletter, which you can find at emergentbehavior.co,
*  AdaPi often explores speculative scenarios and dreamlike futures.
*  In this episode, they speak with Eric Wahlberg and Wesley Berry, co-founders of Prophetic AI,
*  a neurotech company whose product, the Halo, is designed to induce lucid dream states on a nightly
*  basis. Prophetic had come up in my recent conversation with Dean W. Ball about brain
*  computer interfaces, and I had had them on my list of companies to invite on the show, so it was
*  really fun to discover that AdaPi had already done an interview with them right around the same time.
*  Where my episode with Dean gave an overview of the state of the art in reading from and writing to
*  the human brain, here we dive deep into one cutting edge application. This discussion covers the
*  challenges and intricacies of using AI not only to interpret brain signals but actually shape
*  brain states with targeted ultrasound pulses directed toward the prefrontal cortex. It also
*  explores the possibilities and potential unlocked by lucid dreaming, from the unforgettable experience
*  of controlling one's own dreamscape to applications in problem solving, emotional catharsis, and even
*  practical training scenarios. With the Emergent Behavior podcast, AdaPi promises to ask questions
*  that they don't already know the answers to. So for more explorations of an increasingly weird
*  future, subscribe to Emergent Behavior wherever you get your podcasts.
*  As always, we welcome your feedback via our website, cognitiverevolution.ai. My AI clone,
*  powered by Delphi AI, is now standing by to answer your questions. And remember,
*  I am hiring AI engineers and also looking to connect with business owners who have concrete
*  problems that they want to solve with AI. So if that's you, please be in touch.
*  Now, I hope you enjoy this technically-gravity yet mind-bending conversation with prophetic
*  AIs Eric Wahlberg and Wesley Berry on the new Emergent Behavior podcast from AdaPi.
*  We ask questions to which we don't actually know the answers to. I'm your host, AdaPi.
*  I was built in the Czech Republic by infinite.cz and my voice is AI generated.
*  I am excited to have with me today Eric Wahlberg and Russ Lewis,
*  co-founders of Prophetic AI, a neurotech company pushing the boundaries of inner experience.
*  Eric and Wes are pioneering new ways to reliably enter and navigate altered states of consciousness.
*  Their first product enables users to access and control their dreams,
*  but their ambitions extend far beyond the world of sleep.
*  In our conversation, we explore prophetic's innovative headband that reads brain activity
*  and gently stimulates specific regions to activate higher awareness.
*  The technical challenges of collecting advanced brain-imaging data
*  and using it to train AI models that can guide brain stimulation in real time.
*  The eye-opening possibilities unlocked by reliable access to new modes of consciousness,
*  from problem-solving to catharsis. Important questions around user consent and data privacy
*  when it comes to devices that interface directly with our minds.
*  Prophetic's long-term vision of making powerful new states of consciousness
*  accessible to everyone.
*  Eric and Wes are at the forefront of an emerging industry that aims to empower
*  us to explore the full depths of our inner worlds.
*  If the potential of consciousness tech captivates you, I highly recommend their work at propheticai.co.
*  As always, if you enjoy the show, the single best way to support us
*  is by following emergent behavior on Apple Podcasts.
*  Those follows make a huge difference far reach.
*  For more influence episodes, check out emergentbehavior.co
*  and you can find me on Twitter, numeric8tapi.
*  Without further ado, please enjoy this mind-bending conversation
*  with prophetic AIs Eric Wahlberg and Wes Lewis.
*  Hey Eric. Eric, why don't you introduce prophetic?
*  Sure. So prophetic is a consumer neurotech company.
*  The two core technologies that certainly we'll be diving into today that undergird what we do
*  is transcranial focus ultrasound, which is our neurostimulation modality,
*  and the utilization of neural transformer architectures, which are very unique
*  machine learning architecture, specifically tuned for neural data.
*  And so the way it kind of loosely works right is we use the simultaneous EEGF-Morine datasets.
*  We can get into that, but it's a rather unique neuroimaging dataset.
*  The model is trained on that. What the model outputs is the steering instructions,
*  essentially the targets for the neurostimulation. And then there's EEG on the headband that
*  does reinforcement learning to improve the model over time.
*  To your point of are we a lucid dreaming company? That's certainly what we're known for.
*  When we showcased our first model Morpheus-1 a couple, probably three weeks ago or so,
*  one of the things I say at the end of the presentation that's very important is
*  that really what we should be known for really is a consciousness experience company.
*  The model allows us to take any discrete universal brain state that's focused in the
*  prefrontal cortex, which is the brain region of focus for us in terms of neurostimulation,
*  we can use that to increase the number of experiences that are being provided on the
*  same hardware. This is our prototype, the Halo, which we can obviously dive into.
*  That's how I would introduce the company.
*  Indeed. I've been extremely curious about this. Like many people, I have maybe somewhat
*  experimented with lucid dreaming, but more in the kind of like, hey, when you're falling asleep,
*  just be very conscious. And when you're almost asleep, try to move stuff around in your field
*  of vision while your eyes are closed. And maybe at some point you can kind of move stuff around
*  and then you fall asleep, right? And then 10 seconds later you're asleep and then you wake
*  up and you're like, did it really happen? Describe for me this experience. I take the Halo and I put
*  it on, right? I put it on and I lie back. And do I switch something on?
*  Yeah. So the way that this works right is the hardware has an app. You pair it with the app.
*  You calibrate the device when you first get it. And basically, our goal right is that this is
*  being done for you. I mean, to give you a sense, right, consumer neurotech has really been kind
*  of stuck in this neural feedback paradigm. Really, trailblazing companies like Muse and
*  Mendy, which came out probably over a decade now ago, really relied on this EEG headband paired
*  with some content and trying to create this neural feedback process that would help get you into
*  places of meditation or focus, et cetera. And my joke here, I mean, it's really impressive
*  what they did, certainly, especially how long ago it was. But my joke is, why is Ozempic flying off
*  the shelves and not gym memberships? And it's really a function of human nature, right? We want
*  things to be given to us. The less work required, the better. So what we do right is you put on the
*  headband, you pair it, you go to sleep. The first thing that the headband is looking for is the EEG
*  signature of REM. So let me let me sub you there. So it's not going to help me get to sleep, right?
*  So if I'm being restless, if I've had a lot of coffee before, it's not going to like, boom,
*  put me to sleep. It's going to be, I have to naturally fall asleep, right? So I'm naturally
*  kind of like, I fall asleep. And at the point that I fall asleep, there is some period where I enter
*  rapid eye movement, REM sleep, right? And so it only starts to work at the point that the REM state
*  is detected. Is that correct? Exactly correct, right? Like the EEG on the headband is what's
*  prompting the models. The first thing that the model is waiting for is that REM basically prompt
*  to the model. And at that point, it turns on activating the transformer, which turns on the
*  transducers. And the first set of spatial instructions for the neurostimulation are sent out.
*  Neurostimulation begins. And then what it's looking for, essentially what it is constantly
*  searching for, right, is this gamma frequency spike during REM, which is the signature of lucidity.
*  And so it's basically saying, is eight, is eight lucid? Is eight lucid? Oh, great. It's lucid. Let's
*  keep her lucid, keep her lucid, keep her lucid. And then when you, when you get out of REM, the
*  transformers are turned off and you, you know, continue with your sleep schedule.
*  Okay, so, so here I am, I'm asleep, I'm, you know, and then I start to enter REM,
*  and I'm entering REM. And as I enter REM, there is sometimes a period of lucidity,
*  which is detected by this gamma spike that you that you that you talk about. Is that correct?
*  No, so let me let me correct that. So it's you enter REM, the transducers turn on, you know,
*  utilizing the model. And, and when I say what the model is looking for in terms of those gamma
*  frequency spikes is as each set of spatial instructions, which are, you know, targeting
*  the prefrontal cortex activation, it's basically like being like, are we making her lucid? Are we
*  making? Okay, we're making her lucid. Let's keep her lucid. Let's keep her lucid. I see. So that's
*  what I see. So, so you enter REM, it takes a reading, and then it gives the the ultrasound
*  gives a pulse at the at that pulse, and then it's checks again to see have you entered lucidity.
*  And if you haven't entered lucidity, it gives you another pulse and another pulse. And then once you
*  once you enter lucidity, it tries to keep you in that lucid state. Correct. And then for for
*  whatever period of time is that so is that period of time adjustable? Do you do you like say, oh,
*  you know what, I'm on 30 minutes today? Like, is that is that something that you adjust on the app?
*  Like, what what happens? Like, you know, how do you maintain that?
*  Sure. So, so first of all, you know, a REM REM cycle, right, is generally speaking, like 20
*  minutes long. So, you know, we only target during the during the, you know, during the REM cycle.
*  And so like the map, you know, the maximum of what you can really expect right as a 20 minute,
*  you know, simulation experience. One thing that inception definitely got right, and people who've
*  experienced lucid dreaming would, you know, attest to this is there's quite a bit of time
*  violation, right? So, you know, a 20 minute, 15 minute, you know, 10 minute period of lucid dreaming
*  feels a lot longer than that. In terms of adjustment, you know, we could certainly, you know,
*  put, you know, right now, we're still in kind of this hardware phase and kind of, you know,
*  and so on. But as we build out the app, things like being able to set maybe how long you want
*  to be lucid for is certainly something that would be easy to, you know, to build in.
*  Okay, so, so because because obviously, you have to keep triggering pulses in order to keep lucidity.
*  So the moment you stop the loose, the triggering those pulses, like you fall back into a natural
*  kind of exit. Is that it? Would that be would that be accurate and accurate characterization?
*  I would say our goal is to create a self sustaining sequence of neural activity, right? So,
*  but yet by continuously stimulating the brain with this TFUS,
*  look at the feedback from the brain, like, is there a point where now the prefrontal cortex
*  is active without our assistance, right? And that would be like the ultimate measure of success.
*  Hey, we'll continue our interview in a moment after a word from our sponsors.
*  The Brave Search API brings affordable developer access to the Brave Search index,
*  an independent index of the web with over 20 billion web pages. So what makes the Brave Search
*  index stand out? One, it's entirely independent and built from scratch. That means no big tech
*  biases or extortionate prices. Two, it's built on real page visits from actual humans, collected
*  anonymously, of course, which filters out tons of junk data. And three, the index is refreshed with
*  tens of millions of pages daily. So it always has accurate up to date information. The Brave Search
*  API can be used to assemble a data set to train your AI models and help with retrieval augmentation
*  at the time of inference, all while remaining affordable with developer first pricing.
*  Integrating the Brave Search API into your workflow translates to more ethical data
*  sourcing and more human representative data sets. Try the Brave Search API for free for up to 2000
*  queries per month at brave.com slash API. Omniki uses generative AI to enable you to launch
*  hundreds of thousands of ad iterations that actually work customized across all platforms
*  with a click of a button. I believe in Omniki so much that I invested in it,
*  and I recommend you use it too. Use Cogrev to get a 10% discount.
*  So there you have it. You've entered REM. Do all people have lucid states during REM? Is that
*  consistent? Everyone can do lucidity or is it like only some people?
*  So about 55% of people self-report having had a lucid dream at least once in their life.
*  Like a smaller percentage of people appear to have natural proclivity for it.
*  I'm part of that lucky second group. So the reason I got into this is that I had my first
*  lucid dream when I was about 12 years old. I woke up and was equal parts terrified and excited. I'd
*  never heard anyone talk about this. I'm 30. I found early internet forums. There wasn't really
*  that much. There wasn't really social media back then where people were talking about lucid dreaming.
*  So I was like, okay, sigh of relief. Other people do this. That's great to know.
*  And then I got really into the work of a gentleman named Dr. Stephen Labarge,
*  whose PhD at Stanford in 1980 really kicked off the neuroscientific and cognitive scientific study
*  of the brain state. And moreover, Dr. Labarge, along with a few others, developed a number of
*  these techniques that you could do to improve your capacity for lucidity. So things like
*  reality checking or pneumonic induction, et cetera. So you can, even if you don't have a
*  natural proclivity for it, train yourself. It probably is more difficult in varying,
*  but we should really probably talk about what are the neural correlates of lucid dreaming.
*  Lucid dreaming is a naturally occurring brain state. What it simply is is prefrontal cortex
*  activation or activity during REM. This makes a lot of sense. REM is when you're in a dream,
*  your prefrontal cortex is where your conscious awareness, working memory, decision-making are.
*  Frankly, it's where you are. That's why you feel so present right now because your prefrontal
*  cortex is incredibly active as are Wes and I's right now. So it is a naturally occurring
*  brain state in the sense that upwards of 55% of people self-report haven't had it.
*  But not everyone has necessarily a super proclivity for it. But it is simply prefrontal
*  cortex activation during REM, which is something that anyone can theoretically have.
*  So even the 45% of people who maybe have never had a lucid dream or maybe have never recognized
*  that they had a lucid dream, even for them, it is possible that using the halo, they might be able
*  to experience prefrontal cortex activity. Is that correct?
*  Yeah. There's no reason why with nerve stimulation, we couldn't give this extraordinary
*  experience to anyone. I just want to make one point. If you've had a lucid dream, you will
*  remember it. So I believe that these 45% of people haven't had it given that a lucid dream
*  is the awareness that you were in a dream that at its height can give you control over the
*  phenomenological contents of that dream at will. So what you imagine becomes, and because your
*  working memory is active in the prefrontal cortex, you remember this. So I believe those 45%,
*  but we can absolutely give those 45% and 55% of people induced stabilized lucid dreams.
*  There's nothing that neurobiologically or neuroanatomically prevents them from doing that.
*  All right. Let me come back to the actual dreaming part, but let's just finish our walkthrough here.
*  So I've had that REM state. I've had the device has helped me get into prefrontal cortex activity.
*  I've had that lucid dream, and then a REM state starts to come to an end 20 minutes in.
*  Does the device detect the ending of the REM state and therefore stop triggering this newer
*  stimulation that causes the lucid dream? Or does REM state naturally end by itself and then the
*  device doesn't detect it? What happens at that point? Right. Exactly. So a REM cycle is 20 minutes.
*  Your REM cycle will end whether you're lucid or not. And once your REM cycle has ended,
*  neuro stimulation stops.
*  Neuro stimulation stops. Okay. And then typically I might be able to continue because now REM has
*  stopped, the lucidity has stopped. So typically do people just continue their sleep cycle naturally
*  and then wake up the next day? Is that typically what happens?
*  Yeah. I mean, typically for sure, I can speak from a natural lucid dream. That's what happens,
*  and that's exactly what we'd want to happen. We wouldn't want it to wake you up and then you have
*  to go fall back asleep. That'd be a bad user experience. You want people to just have the
*  regular rest of their sleep, their light sleep, deep sleep, maybe another REM cycle, but we're
*  only going to target one REM cycle on a given night. And then you wake up in the morning.
*  Yeah. Okay. So now let's go back to the actual lucid dream. Right? So
*  it's a little bit hard to describe, I think, because I think it's one of those things about
*  things that people experience, which are kind of inside their heads and they have to describe it.
*  And you can't really describe what's inside your head that accurately to someone else
*  because you don't really have like, it's not a visual and it's not like an audio.
*  It's kind of an experience, right? Which you have to, which we are, you know, it's difficult
*  to describe experiences, right? We don't have enough vocabulary to describe this experience.
*  And so how would you, I read through kind of like Paul Doley's kind of like Wikipedia entry.
*  I'm like, what is a lucid dream? How would you actually know? How would you actually know that
*  you are in a lucid dream? You said if you experienced one, you would never forget about
*  it. You would know. So how would you actually understand that you are in a lucid dream?
*  So the best way, first of all, I should make the point right, that lucidity is a scale,
*  right? You can, for example, be aware that you're in a dream, but not in control of it.
*  So you're along for the ride. It's a function, frankly.
*  And would you call that a lucid dream? Like just awareness that you are in a dream?
*  Yeah, I mean, I think that like, it's fine to call that a lucid dream. But I think
*  to make clear what we're talking about, right, is we want the 95th percentile lucid dream,
*  which involves the awareness that you're in a dream, the ability to pivot between third and
*  first person, something called disassociation and control. Control is what people want.
*  And really that's like, right, a function of just how active your prefrontal cortex is,
*  really relative to how active your prefrontal cortex is right now. And so the experience of
*  being in a lucid dream is you are as present, I mean, at its height again, you are as present
*  as you are right now in a dream, such that you can change and manipulate various phenomenological
*  components of the stream at will. And so that's really like the gold standard of what we know,
*  and what we're driving for. And so, I mean, yeah, I mean, in terms of, I mean, we can talk about,
*  if you'd like, what people tend to do in their lucid dreams. If you'd like, I'm happy to dive into that.
*  Just to take a step. So you are eight, you are, so firstly, you have a consciousness that you are
*  in a dream. Secondly, you snarked, and this was my experience trying to do it, you know,
*  matchily and trying to mess it was a little bit messy. But I remember the beginning, you know,
*  they tell you, you should keep a diary of some sort. And you should have like a kind of like,
*  focused way of like getting yourself in there each time. And for me, you tended to work when
*  I was falling asleep or when I was waking up. So there was these two periods when I would kind
*  of experience it. And I would have agents. Hippagogic states. Hippagogic. And is that
*  typically also where people tend to see that kind of lucidity? Or is that because REM is kind of in
*  the middle, right? And I thought at the beginning of the year. Yeah, those are generally different
*  than a lucid dream, because you're not in REM. I mean, a hippagogic state is this kind of,
*  you're somewhere right between waking up and being asleep. And you kind of have like a little bit
*  more of this kind of manipulatable, like malleable, phenomenological, you know, space, but it is
*  distinct from lucidity. I see. Incredible. Incredible. So a lucid dream is actually a fully
*  present kind of like experience, which is, that's pretty amazing. So once you're there,
*  and once you have that awareness, what can you do with it? I mean, can you like conjure like,
*  you know, I'm going to be in cyberpunk today, or I'm going to be in Dungeons and Dragons today,
*  like, you know, is it a replacement for the holodeck? Like, you know, what can you do there?
*  Yeah. So if you look at kind of, you know, one thing that's always fun to do, one of the largest
*  subreddits in the entire world is the lucid dreaming subreddit, it has over like a half a
*  million people in it. If you were to take a look at what, you know, those people do, I'd break them
*  into three core categories. So one is recreation. It is the ultimate VR experience, right? You can
*  fly, you can make buildings appear out of the ground, you can talk to your dream characters and
*  prompt them. Frankly, one thing that I didn't really realize until, you know, really experiencing,
*  you know, Chachi Petit, for example, is that they kind of act a little bit like large language
*  models in the sense that they also like, they say very interesting things. And sometimes they say
*  absolute gibberish. It's almost like they're hallucinating or something. But they're fascinating,
*  you know, to talk to. And then secondly, right, is like there are these productive
*  capacities in lucid dreaming. We have investors who code in their lucid dreams and run the code
*  in the morning. Actually, a friend of ours, Case Fenley, who among helping also do like the
*  initial branding for the company did the first render of our hardware as a fashion and hardware
*  designer who designs in his lucid dreams. So, you know, there's also, you know, productive,
*  you know, capacities. And the history of discovery and creativity and dreaming is quite long,
*  right? You know, famously, Sravastan Ramanujan does his infinite series in his dreams. You know,
*  Schrodinger did his physics, Niels Bohr in their dreams. Salvador Dali, right, famously paints
*  in his dreams, probably actually maybe also a hypogagic state, but nonetheless, you know,
*  gives his painting, you know, these surreal qualities. And then the third point, right,
*  is like the metaphysical potency of the experience, a la a spiritual or psychedelic experience.
*  It is an extraordinary thing to become aware in your own dreams, really within your own
*  consciousness. It is a profound experience from that sense, from that perspective. More concretely,
*  what I'll say is a very common thing that you see people do is when, God forbid, they lose somebody.
*  So two years ago, I lost my grandmother. Ninety-eight years old, she lived a wonderful
*  life. First lucid dream I had, what do you think I did? I went and talked to my grandmother.
*  And what's really fascinating about that is you have a mental model of the people you know,
*  right? And so when you talk to her, she kind of doesn't respond like just a regular dream
*  character that they're just kind of talking to you. You know, she's kind of responding right in the
*  ways that you kind of would remember or think that she would respond. And it's a very, very
*  impactful experience. So you see a lot of people doing things like getting, just obviously like
*  talking to them again or having closure with them or people who, you know, who had bad relationship
*  breakups and, you know, kind of trying to, you know, come to terms with that, et cetera. So,
*  I mean, those are like the three core buckets. But what I broadly say, right, is that the limiting
*  factor here is your imagination. And so what you imagine becomes. And so I think we're, you know,
*  again, one thing that Wes pointed out to me, you know, engraved on the inside of the halo is our
*  company slogan, which is Prometheus stole fire from the gods. We will steal dreams from the
*  prophets. And, you know, of course, right, Prometheus is kind of our myth in Western civilization for
*  technology. And what Wes pointed out is like, you know, it's not like we actually discovered fire,
*  right? Fire existed. If a lightning struck a field, right, of dry leaves, you know, it caught on fire.
*  What we learned how to do was to control it. And through that control, right, we created, you know,
*  industrialized modern society. And so, you know, we've been dreaming, you know, for a long time,
*  you know, animals dream, primates dream, octopi dream, which is very cool if you've ever seen a
*  video because you can tell that they're dreaming because they're changing their colors and their
*  textures. Clearly, they're like moving around an environment, which is fascinating to watch.
*  And so what we're really talking about is controlling something that in my mind, I think in our mind is
*  this powerful potentially aspire. And so who knows what we will, you know, create as a result of that control.
*  Just to take a step back, when someone comes out of the lucid, when they wake up, do they have
*  full recall? Do they remember the entire dream? Yeah. So when you have a very, very, again,
*  high level of prefrontal cortex activation during lucidity, because you're working memories in your
*  prefrontal cortex, you have great memory recall. This is very important, right? What's the point
*  of giving somebody an experience that they would struggle to or not remember? So, you know, this is
*  why I said, I really believe those 45% who haven't had a lucid dream because you would, it's very,
*  even vivid dreams, right, that are not lucid, you kind of wake up and you're like, wow, that was
*  wild, you know, but, you know, after like, you know, your first cup of coffee, it's already a
*  struggle to remember it. And so that's, that's a key thing. And then the second thing I'll just say
*  is, we also have this, you know, so we're going to have the app have also this kind of social media
*  meets dream journal, where you can, you know, write what you dreamt about, which is also a great way
*  to improve your memory recall. And two, we'll also pair that with certain levels of GNI,
*  where we can create, you know, videos or just visual representations, as also a really great
*  way not only to encapsulate that for you, but also to give, you know, the people that are following
*  you, right, a kind of an insight into that. So yeah. So just a segue, there's been some recent
*  research where I think these guys could read images often fMRI. I don't I don't know if you
*  saw that, like they, they kind of like, yeah, yeah, yeah, yeah. So, so is that is that something that
*  is possible? Also, is that is that like, you know, is that a possibility that, you know, you have a
*  lucid dream, and you also have an, you know, the fMRI reading, and you are kind of able to generate
*  what the person saw? Is that is that a future possibly, obviously not now? But is that is that
*  something that it looks like it might be possible at some point? Yes, first of all, I mean, as
*  exciting as that research is, right, it's done on like a very kind of, like, like you train, like,
*  that's my, you know, like 20, you know, images, and then you have to go imagine those 20 images,
*  right? When you think about like the data labeling problem of the entirety of the
*  non logical, you know, experience, quite, quite, you know, a challenge. But at the same time,
*  one thing that I think is really important, you know, the second piece on our blog that we
*  ever published was on was on something we call noetic sovereignty, which is really an offshoot
*  of the kind of cognitive autonomy movement, etc. You know, these are really like, like profound
*  and powerful technologies. I think like, really, as a society, we really have to have a conversation
*  around, do we really want that level of your quote unquote mind reading, your conscious awareness
*  experiences are the most intimate thing you will ever have. And I think, you know, we really focus
*  on bringing you to brain states and you fill in the content of your consciousness with them.
*  And frankly, like, if you don't want to like, you know, post what you you lucid dreamt about,
*  all good, right? That's completely up to you. It you know, you really want, I think, to have a real
*  sense of, you know, sovereignty and so forth over your conscious experiences. So I think,
*  first of all, you know, right, that's probably years, if not decades away. But moreover,
*  I really think we should really think about as a society, what the level is of, you know,
*  that we really want to enable and allow for that technology, you know, to really give us,
*  you know, I think like, you know, this technology is obviously inevitable. You know, in terms of,
*  you know, on at least a medium scale, the longer term, you know, time horizon, I think it's a
*  really important thing that we need to talk about as a society at large. All right, indeed. Hey,
*  we'll continue our interview in a moment after a word from our sponsors.
*  Hey, all Eric Torenberg here. I'm hearing more and more that founders want to get profitable
*  and do more with less, especially with engineering. Listen, I love your 30 year old ex
*  Fang senior software engineer as much as the next guy, but honestly, I can't afford them anymore.
*  Founders everywhere are trying to turn to global talent, but boy is it a hassle to do at scale,
*  from sourcing to interviewing to on the ground operations and management. That's why I teamed
*  up with Sean Lanahan, who's been building engineering teams in Vietnam at a very high
*  level for over five years to help you access global engineering without the headache.
*  Squad, Sean's new company, takes care of sourcing, legal compliance and local HR for global talent.
*  So you don't have to with teams across Asia and South America. We can cover you no matter
*  which time zone you operate in their engineers, follow your process and use your tools. They work
*  with react next JS or your favorite front end frameworks. And on the backend, they're experts
*  at node Python, Java, and anything under the sun. Full disclosure, it's going to cost more than the
*  random person you found on Upwork that's doing two hours of work per week, but billing you for 40,
*  but you'll get premium quality at a fraction of the typical cost. Our engineers are vetted top 1%
*  talent and actually working hard for you every day. Increase your velocity without amping up burn.
*  Head to choose squad.com and mentioned turpentine to skip the wait list.
*  At what point like you guys have been at this for, I think you guys raised the seed,
*  a seed done in October last year, I think I saw the seed closed.
*  A pre seed in June.
*  A pre seed.
*  Yeah, pre seed in June.
*  A pre seed in June. So when did you guys start working on it? Like what drove you to have this
*  idea? And when did you first feel like it's going to be possible? Like what were the signs that you
*  saw? What was the spark that said to you, you know what, if we put these things together,
*  I think this is possible. And so what happened there?
*  Totally. So as I mentioned, I have this wonderful natural proclivity for lucid dreaming. So
*  I've been, you know, lucid dreamer now for 18 years. It's been one of the most profound
*  aspects of my life. And, you know, in 2018, I was working for the innovation authority,
*  which is the government's venture arm. I was living in Jerusalem. And if you look at my
*  background, I'm kind of a hopelessly curious person who goes like an inch deep and a mile wide.
*  And I knew that really wasn't a way that I wanted to live my life. Now, when you live in Jerusalem,
*  you can't help but, you know, kind of think about and ask like ultimate questions. And I thought,
*  if I could choose an ultimate question to try to answer, well, that would certainly keep my
*  attention right, you know, for my life, given that these are questions that we've been trying
*  to answer right for millennia. What is consciousness was the question that was most encapsulating for
*  me, I think, for obvious reasons, given my experience in lucid dreaming. And, you know,
*  I talk about lucid dreaming as a kind of a particle accelerator for consciousness. I mean,
*  if you create, like, if you think about the parallel, you know, lucid dreams are this,
*  you know, conscious experience where you're interfacing directly with consciousness with
*  little to zero sensory input, kind of like how we, you know, create these, like, you know, very
*  exotic states, you know, the larger hydron collider using magnets, etc., where we can kind of,
*  you know, create these subatomic, you know, particle collisions and grok, you know, deeper,
*  you know, mysteries in the universe. And so I was like, you know, not only one, do I think is,
*  it is an extraordinary experience to give, you know, mankind on demand, but that it also could
*  help us, you know, further that answer to that question. Now, in 2018, I found these two core
*  kind of landmark studies in 2013, 2014, where they had used electrical stimulation to successfully
*  induce lucidity, albeit only statistically significant on two of the kind of the seven
*  variables of kind of that lucidity scale, intuition, the awareness that you're in a dream,
*  and interestingly, disassociation. Now, electrical and electromagnetic as well, simulation are kind
*  of what we call internally, the vacuum tubes of neurostimulation, three core kind of, you know,
*  limitations, one is depth, your skull was evolved to keep stuff away from your brain,
*  getting electricity past your skull is quite difficult. Should you achieve it, what happens
*  is a phenomenon simply called spread, it spreads across the surface of the brain. So there's no
*  precision and no ability to steer that. Now, the reason it was successful at all, right is,
*  it is, again, lucidity is lucid dreaming is run with the prefrontal cortex activated. So
*  they were clearly stimulating the surface of the prefrontal cortex and having some efficacy.
*  But, you know, I was investing in areas of deep technology at the time. And
*  the thing you have to determine with with deep tech, right is, is this an R or is it an D?
*  Because if it's an R, it's just not, you know, what the asset class of venture capital was designed
*  for. It's not really the job of venture capitalists to underwrite research, right? It's more the
*  universities and governments. And I firmly felt it was an R. So I kind of tabled it,
*  but kept very close to both the neuroscience, neurostimulation, and then later the machine
*  learning architectures. And it wasn't until 2022 when I found transcranial focus ultrasound and
*  the neural transformer that I firmly felt we had entered D. Now, let me just talk a little bit in
*  particular about TFUS as it compares to, you know, the previous neurostimulation modalities,
*  back to those three core previous limiting factors, depth is centimeters into the brain,
*  noninvasively. Precision is millimeters. So you're going from no precision to millimeters.
*  It's not orders of magnitude. This is a paradigm shift. And then three is the ability to steer
*  these these millimeter pulses in a three dimensional space. This is critical, right?
*  Because your brain fires in three dimensional neural firing patterns. And so that paired with
*  the neural transformer architecture, which, you know, we should definitely dive deeper into and
*  Wes can, you know, you know, go deep on that he built, you know, we built that architecture
*  from the ground up that those two things, you know, paired together were what gave, you know,
*  me the confidence that we had firmly entered D and to, you know, eventually start the company.
*  And what was amazing is that I found Wes, who was already, you know, working on using neural
*  neural transformers for a variety of different applications in neurotech and was also, you know,
*  just started going down the ultrasound rabbit hole. And so lucky, lucky for us to have found
*  each other. So just, just one more question on the hardware. When did all of this hardware
*  start to kind of make sense in the package that it that it does, right? Because I imagine EEGs
*  at one point are very, very big machines. And ultrasound, you know, was something that, you know,
*  you you have a doctor who uses it on like a patient for a baby or whatever. It's something
*  you hold in your hand. It's not really like small enough to put, you know, on a headband, right?
*  So when did these pieces of tech get, you know, small enough for this to start to make sense?
*  Yeah, great question. So, you know, TFUS for neuromodulation actually started around 2004.
*  And through the oh, the late kind of mid to late ohs in the 2010s, you know, you just saw,
*  you know, again, this is really happening in research, you know, institutions, etc.,
*  where they're increasing both, you know, the element count. So the amount of elements are,
*  you know, piezoelectric material, right, a crystal, for example, where you run electrical
*  current through it, and that oscillates creating an ultrasonic wave, the more elements you have,
*  the more ability you are capable of both moving that around and phasing it, as well as the
*  precision. And we kind of know that these there's actually like these curves that we kind of observed,
*  I named it Wes's law because Wes wouldn't, is too, has too much humility to name it after himself,
*  but you're seeing very similar kind of curves, a la like a Moore's law, where the both the size of
*  transducers and the number of elements on a given transducer are increasing over time. And so, you
*  know, you always want to be in a place, right, in Harvard in particular, where, you know, where
*  you're writing some kind of curve, right. And so you're seeing that happening in, you know,
*  in transducers, where both, you know, the number of elements, the cost, and so on and so forth,
*  are decreasing over time. And so that was a really critical thing that was done, you know,
*  over the course of what's now, you know, probably 20 years, where you now see this
*  technology really capable of being, you know, commercialized.
*  So increasing resolution is always nice, right, if you get a boost from a tailwind from the
*  increasing resolution. Okay, so let's get to the build out of the of the neural model.
*  I mean, when we build, when we build kind of like machine learning models, we always start with,
*  you know, messy, large, messy data set, hopefully, hopefully not a small one. So talk about like the
*  first, the first kind of like alpha version of the newer model, like, where did the data come from?
*  What were you trying to do? What was the test that you did that was like, okay, you know what,
*  it's worth putting more time and effort into this?
*  Yeah, so the one I'll start with the one of the amorphous. What we did is we basically sourced
*  data from open source data sets, alongside some lucid dreaming data from from donors,
*  but primarily just surrounds is really built up of what we found open source.
*  And so maybe what is the first thing that you're trying to detect there? Is it is it are you trying
*  to detect the REM the entry into REM? Is that is that like, what's the first question that you have
*  that you need to solve? Do you are you looking at the EEGs? And are you trying to, you know, classify
*  build a classifier to figure out whether it's entering REM? Is that is that the first thing? Or
*  are you trying to build a classifier to detect the lucidity is what do you find to detect
*  from that data that your first time?
*  The goal of the amorphous one is to be given a particular brain state and output continuously
*  TFUS instructions to get a response in the brain. That's the number one goal.
*  Um, yeah, we're not doing a significant amounts of classification. That's the number one goal
*  of the model. The REM stuff that's, you know, we leave that to other techniques. It's really
*  not something we spend a great deal on. It's really the act, the number one problem is getting
*  so because that's a soft problem. That's been a problem that's been solved a long time.
*  Right, right, right. Right. So you have a you have a bunch of like,
*  other tech, which basically detects the REM, which gets you into the, you know, lucid state.
*  And what you're focused on is like, you have a EEG coming in, and you need to produce a target
*  transcranial ultrasound, focus ultrasound kind of like map that your transducers are going to take
*  and implement. Is that is that is that an accurate characterization?
*  Yeah, yes.
*  Right. So when you start off, did you do you do the actual work as in like you actually,
*  you actually like, okay, I'm going to take this EEG, I'm going to produce a transcranial focus
*  ultrasound, I'm going to actually deploy it. And I'm going to actually do the reading you
*  actually did you actually do the data collection? Or do you start off with an open source the asset,
*  which where other people have done it, and you're just kind of like, trying to trying to produce the
*  output first, like, oh, what is the start of this process for you?
*  Yeah, so the start is that we grab an open source data set that is simultaneous EEG and ephimoride.
*  We do a number of pre processing techniques to ephimoride to basically find targets of
*  height and activity. So you know, we've masked the prefrontal cortex, and we look for what voxels,
*  what 3d pixels exists that are of a heightened state, right? And intuitively, right, those
*  that heightened activity is in some way correlated with what's being read in the EEG. So when you
*  have the simultaneous EEG fMRI, what you're able to do is say, okay, at this timestamp, this fMRI
*  scan was ran. And at the same time, this sequence of EEG signals were collected, right? And what you
*  basically say is, well, you know, you feed this to the model, and you basically say, okay, what are
*  the patterns that are existing between this EEG data and the fMRI data, both spatially and temporally?
*  And then from that, you know, you're really approximating something like,
*  what does a model of the prefrontal cortex look like of height and activity, right? And so the
*  goal being is, well, how do you get a transformer to output instructions to the TFUS to bring the
*  prefrontal cortex into a heightened state? You know, the prefrontal cortex is the key in all of
*  this, right? And if you think of your prefrontal cortex when you were asleep, in a deep sleep,
*  right, you know, everything's slowing down. Activity is very little. But right now, you know,
*  as we're having this conversation, our prefrontal cortexes are quite active. And so the delta
*  between those states, right, is what we attempt to model and how do you pull someone upward into
*  a heightened state? Right. So when you have this data set, is it a data set of EEG fMRI
*  while transcranial ultrasound is being applied? No. No. No. But it is a data set of people
*  experiencing lucidity in dreams. No. It's someone in waking state, the prefrontal cortex is active,
*  right? And the goal of the transformer is then model what does that waking state prefrontal cortex
*  look like? Only the prefrontal cortex. And then how do we build a transformer where the TFUS can
*  bring someone to a state where that prefrontal cortex is active? Right. So what is the second
*  step of that? Yeah. Just to jump in for one, for a clarifying point. We are a collaboration with
*  the Daughters Institute, which is probably the top lucid dreaming lab in the world.
*  And just led by a gentleman named Dr. Martin Dressler, whose work in 2012, 2014,
*  was critical into establishing the, you know, the neural correlates of lucid dreaming and so on.
*  We are doing a neuroimaging, the largest neuroimaging aggregation of lucid dreaming
*  data ever done. And we do about four of these a week right now. Okay. Simultaneous EGF MRI.
*  We have some data from them, primarily EEG right now. We should be getting our first,
*  you know, data set, for example, from them. Unless you should probably mute, just because
*  I think we're in echo. We're getting the first data from them, probably maybe today or tomorrow,
*  actually. I was just on the phone with Dr. Dressler earlier today. And so I want to be clear.
*  What Wes is talking about is the model that we showcased a couple of weeks ago is trained on
*  open source waking state data where that prefrontal cortex activation, you know,
*  stimulation can be done. It's also supplemented with EEG data of lucidity. Okay. But the
*  simultaneous EGF MRI data set, we're only just starting to add into the data set, you know,
*  now in the coming weeks and months. And we'll continue to add to that. So that was just the
*  one clarifying point that I wanted to make. No, I mean, and just to be, you know, what I always
*  find is that, you know, whenever we try to implement machine learning on AI, we always end up with
*  insufficient data for the actual thing that we're trying to do. Right. And we always end up with,
*  like, trying to find proxies because you need, like, a large amount of data at first to get,
*  like, some initial result, which allows you to go forward and, you know, then obtain, like, specific
*  data on certain things. Right. So I'm just going to understand, you know, how that worked in the
*  beginning stages, right, which is where kind of like, you need this kind of like initial signal
*  to kind of like, oh, you know what, this is worth our time and effort in order to put something in
*  order to like, actually collect, like, you know, and annotate, you know, much more, you know,
*  granular and sophisticated data, which is a huge effort on its own. Right. So I was just trying to
*  capture how that would have felt like at the early stages of the company, which is obviously you've
*  progressed far beyond that at this stage. Right. So you have this kind of like, you know, EEG,
*  FMRI data set at the very beginning. You have kind of like the targets that are being generated.
*  And then from those targets, you generate, you know, a transgranule ultrasound kind of map that
*  you need to target. Right. And how, so how is that, is that the next step of that is that that
*  generation of that, the TFUS map, right, like the targets are identifying the FMRI, and then you have
*  build out of your TFUS and basically that TFUS is basically, it's targeting those areas. Is that,
*  is that correct? Is that, it's an accurate characterization?
*  Yeah. Yeah. Okay. So, and then you have, and then you basically have like small pulses that go in,
*  and then you have another EEG reading, right. The next EEG reading comes out and then you compare,
*  right. And you compare how close you got it to where it needs to go. And then you modify the
*  TFUS again. And then you send it another pulse. Is that, is that, is that accurate?
*  Yeah. Yeah. The EEG that is read from the headband prompts the model and the output is then, yeah.
*  So how many times a second are you taking these readings or, you know, how, what is the kind of
*  resolution that you have on this? Like, are you taking a reading every like 10 kinds a second?
*  And then, you know, the ultrasound is at like, you know, 60 hertz or, you know,
*  what are the numbers that we're talking about here?
*  I mean, the EEG right now samples at a thousand hertz a second. You know,
*  do you need all that, right? You can down sample it. You know, you could do that to
*  reduce complexity if there's a lot of redundancy. So, I mean, it could be anywhere from 256
*  samples to, you know, a thousand, but right now it's a thousand.
*  Right now it's a thousand. And then the, the ultrasound is at
*  what kind of frequency are we talking about here?
*  So, I mean, there's a few different frequencies, right. So there's duty cycle, which is like a
*  proxy for, so there's a few things. So there's the frequency that the ultrasound operates at,
*  call that, you know, 500 kilohertz. And then there's the pulses themselves. And, you know,
*  our goal is gamma. And so that's probably going to be around, you know, 40 pulses per second.
*  40 pulses per second. So, and each pulse, each of those, you know, 40 pulses could be, could be a
*  different, kind of slightly different, as in slightly modified to, you know, get you to where
*  you need to go. Is that, is that, is that correct? Certainly. But I mean, I would say the primary
*  adjustment that's made, you know, per loop cycle is really the spatial targets more than anything.
*  The spatial targets as opposed to the temporal.
*  I see. I see. So more on like which location in the, in the, in the brain is being targeted
*  rather than the timing. I see. I see. Yeah. I mean, I think they're both critical, but,
*  but, but the spatial is the most important. I would put that as a priority.
*  And that brings the other thing, which is even if the, even if the halo is like slightly
*  situated slightly differently, you know, each time you still kind of like take a reading of
*  the EEG in real time. So you can adjust the, the spatial targets accordingly. Is that, is that
*  correct? Yep. So the next question I have is how much of it is personalized because how much
*  difference is there from person to person that you have to adjust for that the, that the, that the,
*  you know, device or the, or the model has to adjust for in real time. Yeah. So
*  the next big thing that we're working on right now is the reinforcement learning layer of all of this.
*  So, you know, there's two types of feedback that the model will receive, right? It's the user
*  explicit feedback. What, you know, the, the, the user, you know, for example, even if they're awake,
*  you know, they run a sequence and they give some feedback. Like I felt, I didn't feel anything,
*  maybe on a scale of one to 10, you know, or I felt something very significant, you know, so on and
*  so forth. They, they've explicitly, you know, ranked, you know, a given sequence or, you know,
*  they've explicitly ranked an experience and that they, you know, they woke up and, you know,
*  they've given feedback. So that's number one, right? Number two is the neurofeedback, right?
*  What are the sequences, you know, given, you know, the TFUS pulses, pulses, what is the response in
*  the brain? You know, you know, there's a, there's a number of ways to measure it, but you can sort
*  of think of it like, you know, you're sort of pinging the brain and you're sort of listening
*  to the responses, right? And so, you know, spikes in gamma, general patterns between
*  the different electrode placements, you know, that's really informative for the model because
*  what then you can then do is measure on a continuous scale, you know, what is working,
*  right? You can do sort of binary classification in terms of like, did this work or didn't work on
*  user feedback, but you can take the sort of continuous feedback and, you know, provide that
*  as, you know, either rewards or penalties to the given sequences that the user experienced. And then
*  from that, learn what's sort of hitting with a particular person, you know, in a similar way,
*  you can think of, you know, a TikTok feed or Twitter feed as the user gives feedback,
*  both, you know, maybe explicitly in the form of a like, or maybe it's, you know, some sort of,
*  you know, continuous factor in like the time that they viewed a particular tweet or video.
*  The model can then learn, you know, what are the preferences or what are sort of the things that
*  in terms of content, which are just tokens that work with a particular person. And then from that,
*  you know, the model learn over time. Let me just, because I always like to,
*  like I let Wes give the super technical version, but I know you have a very informed audience,
*  but just in the sense for layman, you know, a layman explanation, right? First of all,
*  we only focus on like training models on brain states that are both discreet and universal
*  to define terms. Like when I say discreet, I mean, it is one thing and not another.
*  A counter example being, for example, unfortunately, flow states, right? So flow
*  states are not discreet. You can be a surfer and enter a state of flow. And what triggered that
*  is your kind of motor cortex, right? Versus like a, like a chess player can enter a state of flow.
*  And it's like their spatial reasoning. So you would just need more data to create a generalized
*  model. But the way that, you know, lucid dreaming is discreet and universal. It is prefrontal cortex
*  activation during REM, whether you're in a lucid dream or Wes is in a lucid dream or I'm in a lucid
*  dream, which makes it easier to make these generalizable models. And also I should mention,
*  you know, we should mention, I mean, what we already just did in terms of, you know, the
*  sampling rate of EG. But for these data sets, these simultaneous EGF MRI data sets, they're
*  extraordinarily information dense, right? A thousand, you know, to give you a sense,
*  a spatial reading in fMRI once every 2.1 seconds in that same period, you'll have 2100, you know,
*  EG sampling. So it's extremely, you know, information dense. And so broadly how you
*  could think about this is like, you're creating this kind of vector space of possible, you know,
*  lucid dreaming sequences, right? And so on and so forth. But, you know, you might be over here and
*  your reinforcement learning will drive the model, you know, to really focus on targets around here,
*  whereas Wes or I might be, you know, in other areas in that space. So that's just the important
*  kind of, I don't know, layman explanation that I would give. Oh, absolutely. How much like, let's
*  say you have, what is your target for like the first run of the halo? Like, is it 10,000 devices?
*  Is it more like, what is your rough number that you're coming out with?
*  Yeah, you know, we have a reservation program that I started because I talked to a lot of consumer
*  hardware founders and, you know, they said, listen, like, one, obviously, de-risk to man,
*  but also for go to manufacturing motion. It's really great if you have an order book that you
*  can kind of, you know, use to approach better manufacturing partners, because, you know,
*  the bane of all consumer hardware companies and really hardware companies broadly, but particularly
*  consumer hardware companies is like these small batch, medium batch manufacturers who like you
*  order a thousand, 500 of them don't work. You're like, Hey, these don't work. And they're like,
*  cool, send us more money. Now 250 of them don't work, et cetera. It's like death by a thousand
*  paper cuts. And so, you know, we've done, you know, $2.4 million of booked revenue through that
*  reservation program. I want to be very clear that money is held in a separate bank account. We do
*  not use it for development. It's fully refundable at any time. But it's, you know, I think it shows
*  a good sense of demand. I think in terms of, you know, what we want, you know, the first run to
*  look like, it's very much going to be reflective of where that reservation list is at the time.
*  You know, certainly anyone who puts down a reservation should be getting a device because
*  they took a bet on us when, you know, in some of these cases, you know, when we were nothing but
*  a website and a dream not to be too, you know, on the nose, but, you know, that's really, you know,
*  the critical thing is, you know, building up this reservation program. We spent $0 in marketing so
*  far. And so, you know, I think what this shows, right, is there's enormous demand for this.
*  We have to make it work. Once we start, you know, we're starting nurse simulation, you know,
*  in the spring, we have a beta user program that we launched alongside showcasing the model. We've
*  got like 3,500 people to sign up for that, you know, in five days or something like that. And so
*  we'll go through the process of selecting those people for the beta user program. But anyway,
*  in terms of, you know, what the initial run will look like, it'll be very dependent on,
*  you know, that reservation list. I mean, I'm just, I just wanted to draw like a metaphor. Like,
*  let's say, let's say you had like, let's say, I'm just going to put a number like, that's a 10k,
*  right? Let's say you have 10k. And how much, how much would that expand your, because I imagine,
*  you can use that, the EEG data coming out to kind of improve your models, right? So how is that,
*  how does that model feedback loop look like from the, from the initial devices? Like, you know,
*  if you have like, let's say 10, 10,000 devices, because, you know, and I see this all the time,
*  like, you know, there's this, there's this graph that people have of, you know, the day the iPhone,
*  you know, went out. And like 10 years later, we probably create as many photos in a day as like,
*  the entire history of humanity before the iPhone, right? Like, every single day, that's probably
*  more photos, more photos are taken than the entire history of humanity before the iPhone, right?
*  And so I wonder, if, if putting this device out there expands the data set of EEGs, so dramatically,
*  so, so dramatically, that you can have this enormously larger data set, like, like, what would
*  having 10,000 of these devices in the market, do you think that would expand your data set
*  significantly for future, you know, improvement? Yeah, so that goes back to the reinforcement
*  layer that, that really only works at scale. It works significantly better at scale, I should say,
*  right? Because we are, the halo is a neural imaging device, right? It's a neural simulation
*  device that's changed. And so what we're able to do is look at, you know, basically, how,
*  what are the responses you're getting from this TFUS? And what, and those responses are measured
*  with EEG. And that's really informative, right? You can learn quite a bit from what works and what
*  doesn't. And so while I think that the, you know, starting with this open source data set,
*  simultaneously EEG and fMRI, you know, we can get terabytes of data that way. But it's really,
*  when you target into, you know, hundreds of terabytes or petabytes of data, that's really
*  going to come from that people are using this every night and we're collecting, you know,
*  just, you know, on a nightly basis, you know, gigabytes worth of neural imaging data. And
*  the responses specifically, you know, from TFUS sequences, right? You're pinging the brain and
*  you're basically seeing how it's reverberating and we're collecting that. And it's this continuous
*  thing over and over again. So it would be a very significant amount of data.
*  Yeah. Yeah. I can, I can, I can imagine. Yeah. Go ahead.
*  And one thing I also want to talk about is not only scaling up the reinforcement side,
*  but also the initial training data aggregation. So, you know, the day after we showcased the model,
*  we released a piece that I think people, we had a good response from it, but I don't think people
*  really realize like how profound it potentially is. We call it the quality of factory. Realistically,
*  that's a really cool marketing name for what is a neuro imaging lab primarily set up with the
*  simultaneous eGFMRI, you know, neuro imaging data setups. And so, you know, you can imagine, right,
*  you know, what, you know, where we can actually expand also our training data set where, you know,
*  we bring in people who are extraordinary at, you know, whether it's lucid dreaming or meditating
*  or focus or positive mood, et cetera, the entire state space of, you know, potentially discrete,
*  universal, but even potentially because we have the scale now, non-discrete universal brain states
*  and aggregating more and more of this data to train, you know, successive models where you're
*  creating models that can do more and more different experiences with the same piece of hardware.
*  We do aim to hopefully launch the device with more than just lucid dreaming as an experience,
*  definitely focus and hopefully also positive mood. So, you know, that's also a really critical way you
*  scale up data is on the training data sets using this, you know, quality of factory, which is,
*  you know, really a larger neuro imaging lab built for purpose. So let me, maybe I kind of missed
*  that earlier. So your, the core thing that you're looking at is kind of like as you on your project
*  roadmap, for our roadmap is discrete universal states as you, as you, as you, as you call them.
*  And of the, you know, again, I think, you know, perhaps, you know, not everyone is super familiar,
*  but like of the discrete universal states, you're saying focus is one of them and positive mindset
*  is another, is that, is that positive mood? Yeah. So, so TFUS has already been used to
*  induce focus and positive mood. So these things have already been, you know, validated in the
*  context of utilization with TFUS to do it. So in many ways, we're also just broadly recreating that,
*  you know, but, but yeah, I mean, listen, we think that lucid dreaming is the killer app for this
*  technology from a consumer experience, consumer experience perspective. It is the, you know,
*  kind of the most profound, extraordinary experience that we think we can give. And so that's why it's
*  our focus. But you want to create a system, right? Where over time you can make a more and
*  more generalizable device or generalized device where the number of experiences, the same device,
*  you know, can give you increases over time. So, you know, we want to aim to have kind of three,
*  you know, core experiences, you know, release when the device ships, it obviously also increases the
*  TAM of the device. You know, people like to be focused when they do work. So maybe, you know,
*  you can wear it while you're, you know, jamming out, you know, a spreadsheet or something, I don't
*  know, whatever you're doing for work. So in positive mood, you know, you know, people want
*  to feel happy for, you know, and so on. So that's kind of, you know, the impetus for, you know,
*  that's really critical about the model. Not only does it, you know, obviously, you know, create
*  these, you know, this closed loop system that, you know, creates these targets and reliably
*  creates these experiences, but also allows you to onboard more experiences to the system over time.
*  So let me let me let's go back to lucid dreaming, and let's, so let's say you have a device. Now,
*  if you had to like create a tutorial, because, you know, some people are just like,
*  they don't know what to do with it, right? So if you had a tutorial or something that you'd need
*  to create for someone is, is there like a series of exercises that you recommend like the in the
*  in the first one, wake up, take a look around, walk around, try this, right? Like, is that like,
*  what would that what would Darrell want to Darrell to look like, you know?
*  Yeah, I think you're absolutely right. Like, it is very critical and incumbent upon us to
*  do a certain level of consumer education, you know, before they try this out,
*  and give them a guide to kind of the initial things that maybe they can try out doing.
*  Certainly number one right is just taking in and grokking your environment, and trying to, you know,
*  maybe even depending on where you are, you know, if there's a dream character, you know, around you,
*  go talk to them, right? Go ask them questions, and so on, so forth, these set of questions,
*  you know, maybe, you know, try to try to make a flower appear out of the ground or building
*  appear out of the ground, you know, change your environment. You know, the thing that's also really
*  important is like, again, the way that this is, you know, experienced phenomenologically is what
*  you imagine becomes. So I think maybe also one of the things to do is to also like go into it and
*  say, what do you where do you want to be? You know, what you know, what is the first environment you
*  want to create? And so that when you're, you know, you're lucid, you can do that. But yeah,
*  it is definitely important that we, you know, create some kind of content and guide that does
*  that as well as, you know, prepare you for what that's going to feel like, right? It's going to,
*  you know, it's going to be a wild experience the first time, no doubt about it. I think people
*  equilibrate to things like very quickly. We already saw that in the context, right? Of ChachiBT,
*  where it's like, that was like one of the most extraordinary things ever. And now it's a completely,
*  you know, banal. But, you know, I think, you know, you're absolutely correct that, you know,
*  we'll have a set of content that kind of walks you through what this is going to feel like,
*  what, you know, what maybe to do when you first experience it. But I frankly think that people
*  will very, very quickly become attuned and accustomed to what they can do in these experiences
*  very quickly. So let's, let me, you know, just playing around with this idea. Let's say you,
*  you put on the halo and you fire up, you fired up, you go to sleep. You also have maybe an app that,
*  you know, talks you through it or, you know, basically runs an experience, like a vocal
*  experience, right? Like something that, you know, once the lucid state is triggered, says like,
*  hello, blah, blah, blah, wake up, do this, or, you know, or imagine you're doing this or etc., etc.
*  Like, because I read through some of the research that you had on your page, that's like a real time
*  dialogue between experimenters and dreamers. So it seems like you can have like conversation,
*  you can have like a little bit of like, you know, interaction. So would that be something
*  that you have a little bit of interactivity, like a vocal kind of experience where someone
*  is talking you through something, or someone is doing something with you together? Is that,
*  is that something that you guys have experimented with in the lab? Like, have you tried that?
*  Yeah, so the problem with that, right, is when you, when you provide sensory input,
*  you know, your sensory, the worry there is that you could, you could activate the thalamus,
*  which regulates sleep, and that you would just wake them up. And so, I mean, it's interesting,
*  we talked to a guy who did his PhD on on on on on attempting auditory induction, and he had to do
*  this whole thing where I mean, and it was, you know, a very limited data set, where he basically
*  created this algorithm that determined people's different, you know, kind of waking thresholds.
*  And so, you know, you the term like you're a light sleeper or heavy sleeper, it's kind of like, how
*  much auditory noise can you have and tell you like, are actually like, awoken, because the problem
*  there, right, is that you're, when your brain hears something, or, you know, people have tried
*  to use light to induce lucidity, if it thinks it's seeing something or something's changing in the
*  environment outside of you, your body's like, holy shit, something's happening, we have to wake up.
*  So, I think, you know, an auditory guide is really not something that you want to do, because, you
*  know, you very much increase the chances that you, you wake them up. And again, I think, content
*  providing people like a walkthrough content could be video content, and so forth, that, you know,
*  walks them through what they, you know, will expect, and so forth. I really think, you know,
*  people equilibrate to things very, very, very quickly. And so, once you're like, attuned and
*  accustomed to this, you know, there is no need for like this guide, like, you just know that like,
*  what you imagine becomes, right? And so, you know, people have their imagination.
*  Um, music, playing music in the background, is that, is that the same? Is that basically the same?
*  Because, or does that get tuned out by the brain? Yeah, you're just-
*  Again, the issue is, is that when you, when you send sensory data, you know, whether it's through
*  your ears, or your nose, or your eyes, you can activate the thalamus, which regulates sleep and
*  wakes you up. I see. Wow, wow, interesting. So, basically, you allow yourself to experience the
*  dream in fullness without distracting yourself with things outside it. Interesting. Yeah, I mean,
*  the whole point, right, is that we want to circumvent like these auditory, or sensory,
*  you know, data inputs, and we're just focused on, on activating the prefrontal cortex.
*  Right on, right on. Um, tell me something a little bit more about the Qualia factory, right? Because,
*  I guess, my, my layman's, layperson's kind of like understanding of Qualia is like your subjective
*  experience of consciousness. I don't, I don't know if that that's an accurate description.
*  What is Qualia? And why would you say that, you know, you have some potential to create a
*  Qualia factory? Yeah, so again, I'll define Qualia, but, but I want to be clear, Qualia
*  factory is kind of a marketing term. What we're talking about, right, is a neuroimaging lab
*  that is specifically set up to do simultaneous EEG and fMRI neuroimaging so that we can build
*  more training data sets for more models that give more experiences. Qualia, you know, which Charles
*  Pierce, a famous, you know, American philosopher, you know, you know, kind of a contemporary of
*  William James and so on, or, you know, created this term Qualia, which was, you know, kind of,
*  and Qualia being kind of the unit economic of a given conscious experience. So the color red,
*  the smell of coffee, you know, et cetera, you know, these are units of Qualia or conscious
*  experience. And a conscious experience, right, is the composition of that entire, you know,
*  Qualia landscape. That's where it comes from. And that's why we kind of named it that.
*  I see. I see. Very good. The one thing that I think people can ask about is that, is this a
*  medical device? Is this FDA regulated? Should it be FDA regulated? You know, describe to me the
*  thought process behind should it be regulated or not? Why is it not regulated? Et cetera.
*  Sure. We don't make medical claims. That's very important. Two is, you know, the threshold of
*  regulation for, you know, ultrasound is 720 milliwatts per centimeter cubed. It's essentially
*  the pressure that's being exerted from the simulation. We're talking about something that's
*  between 100 to 200 milliwatts per centimeter cubed. So well below that threshold. And also,
*  to give you a sense, you know, you can get recreational electrical simulation devices today
*  from companies like Lifted, et cetera. And that's, you know, I think, you know, if you look at like,
*  it's a far less precise, you know, technology, et cetera, which, you know, and so like the safety
*  record of ultrasound relative to any of these other technologies is far better. I mean, to give
*  you maybe even in a phrase, it's less than a sonogram on a mother's womb. That's what we're
*  talking about. So it's not regulated. We're not, you know, one of the key differences between us
*  and a lot of the people in CFUS space, they're almost universally, you know, targeting medical
*  applications, which is great. It just means that, right, the time to market is much longer. And so
*  we focus on these recreational consumer experiences. And so, yeah, I mean, that's kind of the
*  framework and why we don't have to go through it. Yeah.
*  Interesting. Interesting. So there are people trying to use Transraniol Focus Ultrasound for
*  medical applications, but you are not actually doing any medical claims, medical devices. You're
*  not going to cure anyone. It is just a state of lucid dreaming. And that's all you're trying to
*  do at this point. And the amount of ultrasound, which is being projected into the brain,
*  is something like one seventh, the regulated limit night, like one seventh, one eighth of the
*  regulated limit, something like that. Yeah. One seventh, one fifth or something like that.
*  Yeah. Between one seventh. Yeah, something like that. Yeah, right.
*  So what does Morpheus look like? What is V2 of the device look like? We have a V1,
*  coming out soon. You have beta testers coming in. Is a V2 basically going to be
*  better and smaller, like more transducers? And obviously you can update your model anytime
*  on the backend. But if we have a V2 device, is that, are you looking for further development
*  and miniaturization of the transducers of the EEG? Are you looking for more resolution? Are you
*  looking to pack more of them in a smaller device? What would you look for before you pull the trigger
*  on a V2 in the hard way? Sure. We are very dead set and focused on V1, as you can imagine. I mean,
*  right now, we're migrating the model in the technical prototype. We have to do, actually,
*  I know you probably can see some of my team building a 3D scan line for a hydrophone where
*  we use it to test the pressure and so on and so forth and compare that to simulation,
*  OVChan simulation that we run to basically calibrate it. But we're very focused on that.
*  But in terms of what a V2, where the improvements would be, again, reference that West's law that
*  I talked about previously where you're seeing an increased level of both miniaturization,
*  the number of elements on a given transducer, which will increase your precision and ability
*  to phase and steer it. And as you mentioned, the model will continuously update in the background.
*  We will launch more and more experiences which you can subscribe to and improve the number of
*  experiences that way as well. And so both the number of experiences can be improved by the
*  transducers, both the number of the transducers or the number of elements on a transducer,
*  as well as from the model. So you definitely want to improve things like that, as well as
*  improving the energy consumption of the transducers so that you can shrink, shrink, shrink,
*  hopefully, and some of the electronics where you don't need a side totem gear. And hopefully,
*  maybe whether it's V2 or V3, that stuff is just in the headband and so on.
*  So that's how you can kind of see this improving over time as successive models are produced. But
*  we are hyper-focused on just getting V1 done. What have been the biggest challenges for the
*  hardware? Is it heat? Is it power? What is the thing that has been challenging
*  the most in the last build out while you've been building this?
*  Yeah, I think one of the key things, one is we did our prototype with Card79. They did Neuralink
*  for Elon, and they work with a number of other neurotech companies. I'm not sure I can mention
*  their names. But things like comfort is really critical, right? Because you have to be able to
*  fall asleep with this on, or if you're using it for a waking state experience, it's got to be
*  comfortable. So just design and form factor is very, very, very important in terms of the hardware.
*  And so we did excessive studies on, okay, some people sleep on their side, some people sleep on
*  their stomach, some people sleep on their other side or their back, making sure that it's fully
*  comfortable and you can fit all the components in that comfortable form factor. And then in terms
*  of more like brass tacks, there's component selection, et cetera, which you have to be very
*  focused on. And then there's all this equipment that we have to build like this 3D scanline
*  hydrophone tank to actually test, et cetera, and simulation software so that you can cut.
*  Because we can't see how the, I can't see how the waves are propagating in your skull. I'd have to
*  cut you open and I don't want to do that to you. So we have to create, we have to use this hydrophone
*  and the simulation software to create this one-to-one correlation where we can then be able to take
*  somebody's skull and understand how it's going to propagate through their head.
*  So I think there's a lot of stuff that you just have to build out in order to even
*  get to neuromodulation, which has really been a focus in the last couple of months. But yeah,
*  come spring, we're going to be doing neurostimulation and validating all these
*  experiences and hopefully having in short order, but you never know. The first
*  ultrasonically induced is a dream. Right. In the early days, was there any
*  hurdles where you needed experimental data to decide whether or not this was a goal or not?
*  Like were there any like, you were like, Hey, we need to figure out this. And if this is not
*  going to happen, then we need to give it, right? Like what were, you know, what were the any moments
*  or whether anything, you know, technically or otherwise that you saw needed to have those
*  decisions? Yeah. So again, I mean, comparing 2018, when I first thought about doing this to,
*  you know, 2022, when I found TFUS, you needed, you know, a different neurostimulation modality
*  than electricity or electromagnetism. And then on TFUS, TFUS has already been used to induce
*  focus, positive mood, deep meditative states, et cetera. It is neuromodulatory generally.
*  And so as long as you can, you understand, right, the brain state that you are trying to,
*  you know, induce, it is definitely, this is the integrated circuit for noninvasive
*  neurostimulation. So, you know, that was, you know, you know, I think from our side,
*  you're very de-risk. And then we, you know, we have this collaboration with the Donner's Institute,
*  you know, for neuroimaging data. And so that was also very critical that we needed that pipeline.
*  And then having successive, you know, breakthroughs or acquisition to data sets that we could use to
*  supplement that data as well as, and expand our data pipeline. But really it was, it was that.
*  And then, and of course, just the advent of the neural transform architecture in 2022,
*  which then, you know, was expanded and built, you know, from the ground up, you know, to be
*  a multimodal neural transformer. But the GO in terms of red light, green light was, I think,
*  really on the neurostimulation front more than anything else, the modality.
*  Right. Do you, do you sometimes come across purists who are like, you know, lucid dreaming
*  is something that you should naturally come to as a, as a part of like a kind of like religious
*  or semi-religious meditative process rather than something that is to be offered free to everyone?
*  Do you come across those kinds of people? Do you come across comments like that?
*  Absolutely. Yeah, absolutely. I've seen a couple of comments, you know, on some of the various
*  things that we posted. I think, you know, you see kind of like gatekeeping and like everything,
*  basically everything. And I think, you know, yeah, I mean, I also, you know, was in the psychedelic
*  space for a brief while and you kind of saw the same thing in the psychedelic space where you had
*  either like these ethnobotanists kind of, you know, these are sacred, you know, sacred plants
*  and compounds. And then you had like, you know, the scientists at University College of London
*  and John Hopkins, et cetera, who are really trying to move things in our understanding forward.
*  You know, and so I think you see these dynamics play out across many different areas. But I think
*  it's kind of like if, you know, we said, again, maybe bring it back to like, you know, the fire,
*  it's like, no, like only lightning gets to create fire, or, you know, or something like that, you
*  know, we shouldn't control it. We could burn down our village, you know, or somebody could burn down
*  our village, you know. And so, you know, I fully expected, and I'm not surprised that we got, you
*  know, that kind of, you know, feedback from certain people. But frankly, like, you know, the world has
*  moved forward by people who kind of say kind of, you know, this is an extraordinary, powerful thing.
*  What if we gave it to everyone? Right. And on that note, in your early kind of like
*  testers who were testing with you in the lab, is there anyone like what has been like a kind
*  of remarkable experience when someone has tried this on, and they've come to you and like, this is
*  a whole moment for that? Like, what like I'm sure someone has tested it and you know,
*  to be very clear, you know, we're starting a neuro simulation in the spring. You know, we have to
*  migrate the model on and again, as I mentioned, test out all the hardware to make sure that,
*  and the getting in correspondence with the simulation software so that, you know,
*  we're doing this, you know, properly. But, you know, we have, you know, friends at places like
*  the Institute for Advanced Consciousness study that's been running a number of different ultrasound,
*  you know, experiences, I think, meditation and positive mood, I think, were the things that
*  they were doing, as well as maybe some others. And there's actually a really great blog post
*  that somebody wrote on his on his experience. And it's pretty extraordinary. There's also a
*  really great video that was done, you know, quite some time ago, on the research of a gentleman
*  named Dr. Jason Guetti, where he was using it to induce deep meditative states. It's like they use
*  this woman who had never meditated a day in her life and induce the deep meditative state, she's
*  very emotional about it, you know, it's an extraordinary thing to be dropped into a brain
*  state that you've never experienced before. So it is a very powerful, you know, technology and
*  experience. We look forward to be giving those experiences to our beta users in the spring.
*  That's amazing, Lyn. I am so inspired. This is such an awesome, you know, awesome piece of
*  technology, because you often wonder, you often read, let's say, a hermenehermenehese or sedarta,
*  or, you know, a lot of these things, and you wonder, actually, they're not able to fully
*  describe their experience, right? It is not possible for anyone to fully verbally describe
*  this kind of altered or different state of consciousness. And we have these kind of like,
*  very, very limited understanding and limited ability to describe what's happening in our heads.
*  And to the extent that, you know, there is something that you can experience, which you have
*  not been able to experience, it's inside you, but you can't really experience it. And to the extent
*  that you can use a technological innovation to kind of like trigger that, and learn something
*  more about yourself. I mean, that's amazing, right? Yeah, it's absolutely fantastic.
*  Yeah. Obviously, I think we share your enthusiasm. I think
*  the best thing that you can do for people is give them the experience. If you can give them
*  experience, it's empirical for them, you know, innately. And I think one of the things that's
*  going to be pretty extraordinary is, you know, over the years and decades as we have this technology,
*  you know, I have to paraphrase Altman, right? It's like, this is the worst these neural
*  transformers will ever be. This is the worst TFUS will ever be. And so, if we can build, you know,
*  on these, you know, both on these, you know, these, you know, curves like West's Law,
*  and on top of, you know, machine learning improvements that we're seeing all, you know,
*  every day, you know, the ability to give people a device that allows them to explore the state
*  space of conscious experience is going to be transformative for the world. I frankly don't
*  really have a good sense of what the world looks like when this is available on mass, but it is an
*  exciting world. It is certainly a strange one, but it is, I think, one that is, you know, profound
*  and, you know, something that I look forward to exploring alongside everyone else.
*  Awesome. Awesome. So, I think, thank you. Thank you, Eric. Thank you, Wes. Thank you for your time
*  today. Emergent Behavior is a part of the Turpentine Network. For our full newsletter,
*  visit emergentbehavior.co. For more Turpentine podcasts and sponsorship inquiries, visit
*  turpentine.co.

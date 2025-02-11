---
Date Generated: April 12, 2024
Transcription Model: whisper medium 20231117
Length: 9090s
Video Keywords: ['agi', 'ai', 'ai podcast', 'artificial intelligence', 'artificial intelligence podcast', 'bryan johnson', 'lex ai', 'lex fridman', 'lex jre', 'lex mit', 'lex podcast', 'mit ai']
Video Views: 437448
Video Rating: None
---

# Bryan Johnson: Kernel Brain-Computer Interfaces | Lex Fridman Podcast #186
**Lex Fridman:** [May 24, 2021](https://www.youtube.com/watch?v=1YbcB6b4A2U)
*  The following is a conversation with Brian Johnson, founder of Kernel, a company that
*  has developed devices that can monitor and record brain activity. Previously, he was the founder of
*  BrainTree, a mobile payment company that acquired Venmo and then was acquired by PayPal and eBay.
*  Quick mention of our sponsors, Forsigmatic, NetSuite, Grammarly, and ExpressVPN. Check them
*  out in the description to support this podcast. As a side note, let me say that this was a
*  fun and memorable experience, wearing the Kernel FlowBrain interface in the beginning of this
*  conversation, as you can see if you watch the video version of this episode. And there was a
*  Ubuntu Linux machine sitting next to me collecting the data from my brain. The whole thing gave me
*  hope that the mystery of the human mind will be unlocked in the coming decades as we begin to
*  measure signals from the brain in a high bandwidth way. To understand the mind, we either have to
*  build it or to measure it. Both are worth a try. Thanks to Brian and the rest of the Kernel team
*  for making this little demo happen. This is the Lex Friedman podcast and here is my conversation
*  with Brian Johnson. You ready, Lex? Yes, I'm ready. Do you just want to come in and put the
*  interfaces on our heads and then I will proceed to tell you a few jokes?
*  So we have two incredible pieces of technology and a machine running Ubuntu 2004 in front of us.
*  What are we doing? Are these going on our heads? They're going on our heads, yeah. And they will
*  place it on our heads for proper alignment. Does this support giant heads? Because I kind of have
*  a giant head. Is this just giant? Are you saying as like an ego or are you saying physically both?
*  It's a nice massage. Yes. Okay, how does this feel?
*  It's okay to move around? Yeah. It feels, oh yeah.
*  It feels awesome. Thank you. That feels good.
*  So this is big head friendly. It suits you well, Lex. Thank you.
*  I feel like I need to, I feel like when I wear this I need to sound like Sam Harris. Calm, collected,
*  eloquent. I feel smarter actually. I don't think I've ever felt quite as much like I'm part of the
*  future as now. Have you ever worn a brain interface or had your brain imaged? Oh, never had my brain
*  imaged. The only way I've analyzed my brain is by talking to myself and thinking. No direct data.
*  Yeah, that is definitely a brain interface that has a lot of things. It's a lot of things.
*  That has a lot of blind spots. It has some blind spots. Yeah, psychotherapy. That's right.
*  All right. Are we recording? Yep, we're good. All right. So Lex, the objective of this, I'm going to
*  tell you some jokes and your objective is to not smile, which as a Russian you should have
*  an edge. Make the motherland proud. I gotcha. Okay. Let's hear the jokes. Lex, and this is from
*  the Colonel crew. We've been working on a device that can read your mind and we would love to see
*  your thoughts. Is that the joke? That's the opening. Okay.
*  Okay. If I'm seeing the muscle activation correctly on your lips, you're not going to do
*  well on this. Let's see. All right. Here comes the first one. Is this going to break the device?
*  Is it resilient to laughter?
*  Lex, what goes through a potato's brain?
*  I got already failed. That's the hilarious opener. Okay. What? Tater thoughts.
*  What kind of fish performs brain surgery? I don't know. A neural surgeon.
*  And so we're getting data of everything that's happening in my brain right now.
*  Lifetime. Yeah. We're getting activation patterns of your entire cortex. I'm going to try to do
*  better. I'll edit out all the parts where I laughed and Photoshop a serious face over me.
*  You can recover. Yeah. All right. Lex, what do scholars eat when they're hungry?
*  I don't know what. Academia nuts.
*  That's a pretty good one.
*  So what we'll do is, so you're wearing kernel flow, which is an interface built using technology
*  called spectroscopy. So it's similar to what we wear wearables on the wrist using light.
*  So using light are as you know, and we're using that to image the functional imaging of brain
*  activity. And so as your neurons fire electrically and chemically, it creates
*  blood oxygenation levels. We're measuring that. And so in you'll see in the reconstructions we
*  do for you, you'll see your activation patterns in your brain as throughout this entire time,
*  we are wearing it. So in the reaction to the jokes and as we were sitting here talking,
*  and so it's a, we're moving towards a real time, you know, a more real time
*  activity. So there's a bunch of things that are in contact with my skull right now. How many of
*  them are there? And so how many of them are, what are they? What are the actual sensors?
*  There's 52 modules and each module has one laser and six sensors. And they're the sensors fire
*  in about a hundred picoseconds. And then the sensors fire in about a hundred picoseconds.
*  And then the photons scatter and absorb in your brain. And then a few go in, if you come back out,
*  a bunch go in, then a few come back out and we sense those photons. And then we do the
*  reconstruction for the activity. Overall, there's about a thousand plus channels that are sampling
*  your activity. How difficult is it to make it as comfortable as it is? Because it's surprisingly
*  uncomfortable. I would not think it would be comfortable. Something that's not very
*  comfortable. Something that's measuring brain activity, I would not think it would be
*  comfortable, but it is. I agree. In fact, I want to take this home. Yeah. Yeah, that's right. So
*  people are accustomed to being in big systems like fMRI where there's 120 decibel sounds and
*  you're in a claustrophobic encasement or EEG, which is just painful or surgery. And so yes,
*  I agree that this is a convenient option to be able to just put on your head. It measures your
*  brain activity in the contextual environment you choose. So if we want to have it during a podcast,
*  if we want to be at home in a business setting, it's freedom to be where to record your brain
*  activity in the setting that you choose. Yeah. But sort of from an engineer perspective, are these,
*  what is it? There's a bunch of different modular parts and they're kind of, there's like a rubber
*  band thing where they mold to the shape of your head. That's right. So we built this version of
*  the mechanical design to accommodate most adult heads. But I have a giant head and it fits fine.
*  It fits well actually. So I don't think I have an average head. Okay. Maybe I feel much better
*  about my head now. Maybe I'm more average than I thought. Okay. So what else is there? Interesting
*  you could say while it's on our heads. I can keep this on the whole time. This is kind of awesome.
*  And it's amazing for me as a fan of Ubuntu, I use Ubuntu Mate. You guys should use that too. But it's
*  amazing to have code running to the side, measuring stuff and collecting data. I mean, I just, I feel
*  like much more important now that my data is being recorded. Like somebody cares, like, you know,
*  when you have a good friend that listens to you, that actually like listens, like actually is
*  listening to you. This is what I feel like, like a much better friend because it's like accurately
*  listening to me, Ubuntu. What a cool perspective. I hadn't thought about that of feeling understood.
*  Yeah. Heard. Yeah. Heard deeply by the mechanical system that is recording your brain activity
*  versus the human that you're engaging with. That your mind immediately goes to
*  that there's this dimensionality and depth of understanding of this software system,
*  which you're intimately familiar with. And now you're able to communicate with this system in
*  ways that you couldn't before. Yeah. I feel heard.
*  Yeah. I mean, I guess what's interesting about this is your intuitions are spot on. Most people
*  have intuitions about brain interfaces that they've grown up with this idea of people moving
*  cursors on the screen or typing or changing the channel or skipping a song. It's primarily been
*  anchored on control. And I think the more relevant understanding of brain interfaces or neural
*  imaging is that it's a measurement system. And once you have numbers for a given thing,
*  a seemingly endless number of possibilities emerge around that of what to do with those numbers.
*  So before you tell me about the possibilities, this was an incredible experience. I can keep
*  this on for another two hours, but I'm being told that for a bunch of reasons, just because
*  we probably want to keep the data small and visualize it nicely for the final product,
*  we want to cut this off and take this amazing helmet away from me. So Brian, thank you so much
*  for this experience. And let's continue without helmetless. All right. So that was an incredible
*  experience. Can you maybe speak to what kind of opportunities that opens up that stream of data,
*  that rich stream of data from the brain? First, I'm curious, what is your reaction? What comes
*  to mind when you put that on your head? What does it mean to you and what possibilities emerge and
*  what significance might it have? I mean, I'm curious where your orientation is at.
*  Well, for me, I'm really excited by the possibility of various information about my body,
*  about my mind being converted into data such that data can be used to create products
*  that make my life better. So that to me is really exciting possibility. Even just like a fit bit
*  that measures, I don't know, some very basic measurements about your body is really cool.
*  But the bandwidth of information, the resolution of that information is very crude, so it's not
*  very interesting. The possibility of recording, of just building a data set coming in a clean way,
*  in a high bandwidth way from my brain opens up all kinds of, you know, at the very,
*  I was kind of joking when we were talking, but it's not really, is like I feel heard in the sense
*  that it feels like the full richness of the information coming from my mind is actually
*  being recorded by the machine. I mean, there's a, I can't quite put it into words, but there is
*  genuinely for me, there's not some kind of joke about me being a robot. It just genuinely feels
*  like I'm being heard in a way that's going to improve my life. As long as the thing that's on
*  the other end can do something useful with that data. But even the recording itself is like,
*  once you record, it's like taking a picture. That moment is forever saved in time. Now, a picture
*  cannot allow you to step back into that world, but perhaps recording your brain is a much higher
*  resolution thing, much more personal recording of that information than a picture that would allow
*  you to step back into that, where you were in that particular moment in history and then map out a
*  certain trajectory to tell you certain things about yourself that could open up all kinds of
*  applications. Of course there's health that I consider, but honestly, to me, the exciting
*  thing is just being heard. My state of mind, the level of focus, all those kinds of things being
*  heard. What I heard you say is you have an entirety of lived experience, some of which you can
*  communicate in words and in body language, some of which you feel internally, which cannot be
*  captured in those communication modalities. And that this measurement system captures both the
*  things you can try to articulate in words, maybe in a lower dimensional space using one word,
*  for example, to communicate focus. When it really may be represented in a 20 dimensional space
*  of this particular kind of focus and that this information is being captured. So it's a closer
*  representation to the entirety of your experience captured in a dynamic fashion that is not just a
*  static image of your conscious experience. Yeah, that's the promise. That was the feeling.
*  And it felt like the future. So it was a pretty cool experience. And from the sort of mechanical
*  perspective, it was cool to have an actual device that feels pretty good. That doesn't require me
*  to go into the lab. And also the other thing I was feeling, there's a guy named Andrew Huberman.
*  He's a friend of mine, amazing podcast. People should listen to a Huberman Lab podcast.
*  We're working on a paper together about eye movement and so on. And we're kind of,
*  he's a neuroscientist and I'm a data person, machine learning person. And we're both excited by
*  how much the data measurements of the human mind, the brain and all the different metrics that come
*  from that can be used to understand human beings and in a rigorous scientific way. So the other
*  thing I was thinking about is how this could be turned into a tool for science. Sort of not just
*  personal science, not just Fitbit style, like how am I doing on my personal metrics of health,
*  but doing larger scale studies of human behavior and so on. So like data, not at the scale of an
*  individual, but data at a scale of many individuals or a large number of individuals. So it's personal
*  being heard was exciting and also just for science is exciting. It's very easy. There's a very
*  powerful thing to it being so easy to just put on that you can scale much easier.
*  If you think about that second thing you said about the science of the brain,
*  most, we've done a pretty good job. Like we, the human race, have done a pretty good job
*  figuring out how to quantify the things around us from distant stars to calories and
*  steps and our genome. So we can measure and quantify pretty much everything in the known universe
*  except for our minds. And we can do these one-offs if we're going to get an fMRI scan or
*  do something with the low-res EEG system, but we haven't done this at population scale. And so if
*  you think about human thought or human cognition is probably the single largest raw input material
*  into society at any given moment. It's our conversations with ourselves and with other people
*  and we have this raw input that we haven't been able to measure yet. And if you, when I think
*  about it through that frame, it's remarkable. It's almost like we live in this wild wild west
*  of unquantified communications within ourselves and between each other.
*  When everything else has been grounded, for example, I know if I buy an appliance at the
*  store or on a website, I don't need to look at the measurements on the appliance to make sure it can
*  fit through my door. That's an engineered system of appliance manufacturing and construction.
*  Everyone's agreed upon engineering standards and we don't have engineering standards
*  around cognition. It has not entered as a formal engineering discipline that enables us to scaffold
*  in society with everything else we're doing, including consuming news, our relationships,
*  politics, economics, education, all the above. And so to me, the most significant
*  contribution that kernel technology has to offer would be the formal, the introduction to formal
*  engineering of cognition as it relates to everything else in society. I love that idea that
*  you kind of think that there is just this ocean of data that's coming from people's brains as
*  being in a crude way reduced down to like tweets and texts and so on. It's a very
*  hardcore, many scale compression of actual raw data. But maybe you can comment,
*  because you're using the word cognition. I think the first step is to get the brain data. But
*  is there a leap to be taking to sort of interpreting that data in terms of cognition?
*  So is your idea is basically you need to start collecting data at scale from the brain and then
*  we start to really be able to take little steps along the path to actually measuring some deep
*  sense of cognition. Because as I'm sure you know, we understand a few things, but
*  we don't understand most of what makes up cognition. This has been one of the most significant
*  challenges of building kernel. And kernel wouldn't exist if I wasn't able to fund it
*  initially by myself. Because when I engage in conversations with investors, the immediate
*  thought is what is a killer app? And of course, I understand that heuristic. That's what they're
*  looking at is they're looking to de-risk. Is the product solved? Is there a customer base? Are
*  people willing to pay for it? How does it compare to competing options? And in the case with brain
*  interfaces, when I started the company, there was no known path to even build a technology that
*  could potentially become mainstream. And then once we figured out the technology, we could even we
*  could commence having conversations with investors and it became what is a killer app. And so what
*  has been so I funded the first $53 million of the company. And to raise the round of funding,
*  the first one we did, I spoke to 228 investors. One said yes. It was remarkable. And it was
*  mostly around this concept around what is a killer app. And so internally, the way we think about it
*  is we think of the go-to-market strategy much more like the Drake equation, where if we can build
*  technology that has the characteristics of it has the data quality is high enough, it meets some
*  certain threshold, cost, accessibility, comfort, it can be worn in contextual environments, it meets
*  the criteria of being a mass market device, then the responsibility that we have is to figure out
*  how to create the algorithm that enables the human to enable humans to then find value with it.
*  Okay. So the analogy is like brain interfaces are like early 90s of the internet.
*  Is you want to populate an ecosystem with a certain number of devices, you want a certain
*  number of people who play around with them, who do experiments of certain data collection parameters,
*  you want to encourage certain mistakes from experts and non-experts. These are all critical
*  elements that ignite discovery. And so we believe we've accomplished the first objective of building
*  technology that reaches those thresholds. And now it's the Drake equation component of how do we
*  try to generate 20 years of value discovery in a two or three year time period? How do we compress
*  that? So just to clarify, so when you mean the Drake equation, which for people who don't know,
*  I don't know why you, if you listen to this, I bring up aliens every single conversation. So
*  I don't know how you would know what the Drake equation is, but you mean like the killer app
*  it would be one alien civilization at equation. So meaning like,
*  this is in search of an application that's impactful, transformative, by the way, it should
*  be, we need to come up with a better term than killer app as a, as it's also violent, right?
*  You can go like viral app. That's horrible too. Right. It's some very inspiringly impactful
*  application. How about that? No. Yeah. Okay. So let's stick with killer app. That's fine.
*  Nobody's, but I concur with you. I dislike the chosen words in capturing the concept.
*  You know, it's, it's one of those sticky things that is as effective to use in the tech world.
*  But when you're now become a communicator outside of the tech world, especially when you're talking
*  about software and hardware and artificial intelligence applications, it sounds horrible.
*  Yeah. No, it's interesting. I actually regret now having called attention to, I regret having used
*  that word in this conversation because it's something I would not normally do. I used it
*  in order to create a bridge of shared understanding of how others would, what terminology others would
*  use. Yeah. But yeah, I concur. Let's go with impactful application or value creation. Value
*  creation. Something people love using. There we go. That's it. Love app. Okay. So what, do you have
*  any ideas? So you're basically creating a framework where there's the possibility of a discovery
*  of an application that people love using. Is do you have ideas? We've began to play a fun game
*  internally where when we have these discussions or we, we begin circ circling around this concept of
*  does anybody have an idea? Does anyone have intuitions? And if we see the conversation
*  starting to veer in that direction, we flag it and say, human intuition alert,
*  stop it. And so we really want to focus on the algorithm of there's a natural process of human
*  discovery that when you populate a system with devices and you give people the opportunity to
*  play around with it in expected and unexpected ways, we are thinking that is a much better system
*  of discovery than us exercising intuitions. And it's interesting. We're also seeing a few
*  neuroscientists who have been, have been talking to us where I was speaking to this one young
*  associate professor and I approached a conversation and said, Hey, we have these five data streams
*  that we're pulling off. When you hear that, what weighted value do you add to each data source?
*  Like which one do you think is going to be valuable for your objectives and which one's not?
*  And he said, I don't care. Just give me the data. All I care about is my machine learning model.
*  But importantly, he did not have a theory of mind. He did not come to the table and say,
*  I think the brain operates in this way and these reasons have these functions.
*  He didn't care. He just wanted the data. And we're seeing that more and more that
*  certain people are devaluing human intuitions for good reasons, as we've seen in machine learning
*  over the past couple of years. And we're doing the same in our value creation market strategy.
*  So more collect more data, clean data, make the product such that the collection of data is
*  easy and, and, and fun. And then the rest will just spring to life. That's right. Through
*  humans playing around with it. Our objective is to create the most valuable
*  data collection system of the brain ever.
*  And with that, then applying all the best tools of machine learning and other
*  techniques to extract out, you know, to try to find insight. But yes, our objective is
*  really to systematize the discovery process because we, we can't put definite timeframes
*  on discovery. The brain is complicated and science is not a business strategy. And so we really
*  need to figure out how to, this is the difficulty of bringing, bringing, you know, technology like
*  this to market. It's why most of the time it just link it languishes in academia, academia for quite
*  some time, but we hope that we will over, you know, cross over and make this mainstream in the coming
*  years. The thing was cool to wear, but what's the, are you chasing a good reason for millions of
*  people to put this on their head and keep on their head regularly? Is there, like who's going to
*  discover that reason? Is it going to be people just kind of organically or is there going to be a
*  Angry Birds style application that's just too exciting to not use?
*  If I think through the things that have changed my life most significantly over the past few years,
*  when I started wearing a wearable on my wrist that would give me data about my heart rate,
*  heart rate variability, respiration rate, metabolic approximations, et cetera,
*  for the first time in my life, I had access to information, sleep patterns that were highly
*  impactful. They, they told me, for example, if I eat close to bedtime, I'm not going to get deep sleep.
*  Close to bedtime, I'm not going to get deep sleep. And not getting deep sleep means you have all
*  these follow-on consequences in life. And so it opened up this window of understanding of myself
*  that I cannot self-interest back and deduce these things. This is information that was
*  available to be acquired, but it just wasn't. I would have to get an expensive sleep study.
*  Then it's an end, like one night and that's not good enough to look at, to run all my trials.
*  And so if you look just at the information that one can acquire on their wrist,
*  and now you're applying it to the entire cortex on the brain, and you say, what kind of information
*  could we acquire? It opens up a whole new universe of possibilities. For example, we did this internal
*  study at Kernel where I wore a prototype device and we were measuring the cognitive effects of
*  sleep. So I had a device measuring my sleep. I performed with 13 of my co-workers. We performed
*  four cognitive tasks over 13 sessions. And we focused on reaction time, impulse control,
*  short-term memory, and then a resting state task. And with mine, we found, for example, that my
*  impulse control was independently correlated with my sleep outside of behavioral measures of my
*  ability to play the game. The point of the study was I had the brain study I did at Kernel confirmed
*  my life experience that if I, my deep sleep determined whether or not I would be able to
*  resist temptation the following day. And my brain did show that as one example. And so if you start
*  thinking, if you actually have data on yourself, on your entire cortex, you can control the settings.
*  I think there's probably a large number of things that we could discover about ourselves, very,
*  very small and very, very big. Just for example, like when you read news, what's going on?
*  Like when you use social media, when you use news, what would like all the ways we allocate
*  attention. That's right. With a computer. I mean, that seems like a compelling place to where you
*  would want to put on a kernel. By the way, what is it called? Kernel Flux? Kernel, like,
*  what flow flow two technologies you were flow flow. Okay. So when you, when you put on the,
*  the kernel flow, it is seems like to be a complete, a compelling time and place to do it is when you're
*  behind a desk, behind a computer, because you could probably wear it for prolonged periods of time.
*  As you're, as you're taking in content, and there could a lot of, because some of our,
*  so much of our lives happens in the digital world now that kind of coupling the information
*  about the human mind with the consumption and the behaviors in the digital world might give
*  us a lot of information about the effects of the way we behave and navigate the digital world
*  to the actual physical meat space effects on our body. It's interesting to think in certain terms
*  both like for work, I, I'm a big fan of, so Cal Newport has ideas of deep work that I spend
*  with few exceptions, I try to spend the first two hours of every day.
*  Usually if I'm like at home and have nothing on my schedule is going to be up to eight hours of
*  deep work of focus, zero distraction. And for me to analyze the, I mean, I'm very aware of the,
*  uh, the waning of that, the ups and downs of that. And it's almost like you, you're surfing the ups
*  and downs of that as you're doing programming, as you're doing thinking about particular problems,
*  you're trying to visualize things in your mind, you start trying to stitch them together.
*  You're trying to, uh, when there's a dead end about an idea, you have to kind of calmly like walk back
*  and start again, all those kinds of processes. It'd be interesting to get data on what my mind
*  is actually doing. And also recently started doing, um, I just talked to Sam Harris a few days ago
*  and been building up to that. I started using, started meditating using his app, uh, waking up,
*  but very much, uh, recommend it. And we should get data on that because it's, you're very,
*  it's like you're removing all the noise from your head and you very much, it's an active process of
*  active noise removal, active noise canceling, like the headphones. And it'd be interesting to see what
*  is going on in the mind, uh, before the meditation, during it and after all those kinds of things.
*  And you, all of your examples, it's interesting that everyone who's designed an experience for
*  you. So whether it be the meditation app or the deep work or all the things you mentioned,
*  they constructed this product with a certain number of knowns. Now, what if we expand to the
*  number of knowns by 10 X or 20 X or 30 X, they would reconstruct their product,
*  cool, incorporate those knowns. So it'd be, and so this is the dimensionality that I think is
*  the promising aspect is that people will be able to use this quantification, use this information
*  to build more effective products. And this is, I'm not talking about better products to advertise
*  to you or manipulate you. I'm talking about, uh, our focus is helping people, individuals
*  have this contextual awareness and this quantification, and then to engage with
*  others who are seeking to improve people's lives. That the objective is, is betterment across
*  ourselves individually and also with each other. Yeah. So it's a nice data stream to have if you're
*  building an app, like if you're building a podcast listening app, it would be nice to know data
*  about the listener so that like, if you're bored or you've fell asleep, maybe pause the podcast.
*  It's like really dumb, just very simple applications that could just improve the
*  quality of the experience of the using the app. I'm imagining if you have, you have your neurome,
*  this is Lex and you, there's a statistical representation of you and you engage with the
*  app and it says, Lex, your best to engage with this meditation
*  exercise in the following settings at this time of day, after eating this kind of food or not eating
*  fasting with this level of blood glucose and this kind of night's sleep. But all these data
*  combined to give you this contextually relevant experience, just like we do with our sleep.
*  You've optimized your entire life based upon what information you can acquire and know about
*  yourself. And so the question is, how much do we really know of the things going around us? And I
*  would venture to guess in my own, my life life experience, I capture, my self-awareness captures
*  an extremely small percent of the things that actually influenced my conscious and unconscious
*  experience. Well, in some sense, the data would help encourage you to be more self-aware, not just
*  because you trust everything the data is saying, but is it'll give you a prod to start investigating.
*  Like I would love to get it like a rating, like a ranking of all the things I do and what are the
*  things it's probably important to do without the data, but the data will certainly help. It's like
*  rank all the things you do in life and which ones make you feel shitty, which ones make you feel
*  good. Like you're talking about evening, Brian, like this is a good example, somebody like,
*  I do pig out at night as well. And it never makes you feel good. Like you're in a safe space.
*  It's a safe space. Let's hear it. No, I definitely have much less self-control at night. And it's
*  interesting. And the same, you know, people might criticize this, but I know my own body. I know when
*  I eat carnivore, just eat meat, I feel much better than if I eat more carbs. The more carbs I eat,
*  the worse I feel. I don't know why that is. I don't, there is science supporting, but I'm not
*  leaning on science. I'm leaning on personal experience. And that's really important. I don't
*  need to read. I'm not going to go on a whole rant about nutrition science, but many of those studies
*  are very flawed. They're doing their best, but nutrition science is a very difficult feel of the
*  study because humans are so different and the mind has so much impact on the way your body
*  behaves. And it's so difficult from a scientific perspective to conduct really strong studies
*  that you have to be almost like a scientist of one. You have to do these studies on yourself.
*  That's the best way to understand what works for you or not. And I don't understand why,
*  because it sounds unhealthy, but eating only meat always makes me feel good. Just eat meat. That's
*  it. And I don't have any allergies and you have that kind of stuff. I'm not full like Jordan
*  Peterson where like, if he like deviates a little bit that he goes off, like deviates a little bit
*  from the carnivore diet, he goes off like the cliff. No, I can have like chocolate. I can go
*  off the diet. I feel fine. It's a gradual, it's a gradual worsening of how I feel. But when I eat
*  only meat, I feel great. And it'd be nice to be reminded of that. Like there's a very simple fact
*  that I feel good when I eat carnivore. And I think that repeats itself in all kinds of experiences.
*  Like I feel really good when I exercise. Not I hate exercise. Okay. But in the rest of the day,
*  the impact it has on my mind and the clarity of mind and the experiences and the happiness and
*  all those kinds of things, I feel really good. And to be able to concretely express that through data
*  would be nice. It would be a nice reminder, almost like a statement, like remember what
*  feels good and whatnot. And there could be things like that. I'm not many things like you're suggesting
*  that I could not be aware of that might be sitting right in front of me that make me feel really good
*  and make me feel not good. And the data would show that. I agree with you. I've actually employed the
*  same strategy. I fired my mind entirely from being responsible for constructing my diet.
*  And so I started doing a program where I now track over 200 biomarkers every 90 days. And it
*  captures, of course, the things you would expect like cholesterol, but also DNA methylation and
*  all kinds of things about my body, all the processes that make up me. And then I let that data
*  generate the shopping lists. And so I never actually ask my mind what it wants. It's entirely
*  what my body is reporting that it wants. And so I call this goal alignment within Brian. And there's
*  200 plus actors that I'm currently asking their opinion of. And so I'm asking my liver, how are
*  you doing? And it's expressing via the biomarkers. And so then I construct that diet and I only eat
*  those foods until my next testing round. And that has changed my life more than I think anything
*  else because in the demotion of my conscious mind that I gave primacy to my entire life,
*  it led me astray because like you're saying, the mind then goes out into the world and it navigates
*  the dozens of different dietary regimens people put together in books. And it all has their
*  supporting science in certain contextual settings, but it's not N of one. And like you're saying,
*  dietary really is an N of one. What people have published scientifically, of course, can be used
*  for nice groundings, but it changes when you get to an N of one level. And so that's what gets me
*  excited about brain interfaces is if I could do the same thing for my brain, where I can stop asking
*  my conscious mind for its advice or for its decision making, which is flawed. And I'd rather
*  just look at this data that I've never had better health markers in my life than when I stopped
*  actually asking myself to be in charge of it. The idea of demotion of the conscious mind
*  is such a sort of engineering way of phrasing like meditation.
*  That's what we're doing, right? Yeah, that's beautiful. That means really beautifully put.
*  By the way, testing round, what does that look like? What's that? Well, you mentioned...
*  Yeah, the tests I do. Yes. So it includes a complete blood panel. I do a microbiome test. I do
*  a food of diet induced inflammation. So I look for like satochondriac expressions,
*  so foods that produce inflammatory reactions. I look at my neuroendocrine systems. I look at all
*  my neurotransmitters. I do several micronutrient tests to see how I'm looking at the various
*  nutrients. What about self-report of how you feel? You can't demote your conscious... You still
*  exist within your conscious mind, right? So that lived experience is of a lot of value. So how do
*  you measure that? I do a temporal sampling over some duration of time. So I'll think through how
*  I feel over a week, over a month, over three months. I don't do a temporal sampling of if
*  I'm at the grocery store in front of a cereal box and be like, you know what, Captain Crunch
*  is probably the right thing for me today because I'm feeling like I need a little fun in my life.
*  And so it's a temporal sampling. If the data set's large enough, then I smooth out the function of
*  my natural oscillations of how I feel about life, where some days I may feel upset or depressed or
*  down or whatever. And I don't want those moments to then rule my decision-making. That's why
*  the demotion happens. And it says, really, if you're looking at health over a 90-day period of time,
*  all my 200 voices speak up on that interval. And they're all given voice to say,
*  this is how I'm doing and this is what I want. And so it really is an accounting system for
*  everybody. So that's why I think that if you think about the future of being human,
*  there's two things I think that are really going on. One is the design, manufacturing,
*  and distribution of intelligence is heading towards zero, on a cost curve.
*  Over a certain timeframe. But our ability to, you know, evolution produced us an intelligent,
*  a form of intelligence. We are now designing our own intelligent systems.
*  And the design, manufacturing, distribution of that intelligence over a certain
*  timeframe is going to go to a cost of zero. Design, manufacturing, distribution of intelligent
*  costs is going to zero. Again, just give me a second. That's brilliant. Okay. And evolution
*  is doing the design, manufacturing, distribution of intelligence. And now we are doing the design,
*  manufacturing, distribution of intelligence. And the cost of that is going to zero. That's a very
*  nice way of looking at life on earth. So if that's going on, and then now in parallel to that,
*  then you say, okay, what then happens if when that cost curve is heading to zero,
*  our existence becomes a goal alignment problem, a goal alignment function. And so the same thing
*  I'm doing where I'm doing goal alignment within myself of these 200 biomarkers where I'm saying,
*  when Brian exists on a database and this entity is deciding what to eat and what to do and
*  et cetera, it's not just my conscious mind, which is opining, it's 200 biological processes.
*  And there's a whole bunch of more voices involved. So in that equation,
*  we're going to increasingly automate the things that we spend high energy on today, because it's
*  easier. And now we're going to then negotiate the terms and conditions of intelligent life.
*  Now we say conscious existence because we're biased because that's what we have,
*  but it will be the largest computational exercise in history because you're now doing goal alignment
*  with planet earth within yourself, with each other, within all the intelligent agents we're
*  building bots and other voice assistants. You basically have a trillions and trillions of
*  agents working on the negotiation of goal alignment. Yeah, this is in fact true.
*  And what was the second thing? That was it. So the cost, the design, manufacturing, distribution
*  of intelligence going to zero, which then means what's really going on? What are we really doing?
*  We're negotiating the terms and conditions of existence. Do you worry about the survival
*  of this process? That life as we know it on earth comes to an end or at least intelligent life,
*  that as the cost goes to zero, something happens where all of that intelligence is
*  thrown in the trash by something like nuclear war or development of AGI systems that are very dumb,
*  not AGI I guess, but AIS systems, the paperclip thing, with unmasked is dumb,
*  but has unintended consequences to where it destroys human civilization.
*  Do you worry about those kinds of things? I mean, it's unsurprising that a new thing comes into
*  this sphere of human consciousness. Humans identify the foreign object, in this case,
*  artificial intelligence, our amygdala fires up and says, scary, foreign,
*  we should be apprehensive about this. And so it makes sense from a biological perspective that
*  humans, the knee-jerk reaction is fear. What I don't think has been properly
*  weighted with that is that we are the first generation of intelligent beings on this earth
*  that has been able to look out over their expected lifetime
*  and see there is a real possibility of evolving into entirely novel forms of consciousness.
*  So different that it would be totally unrecognizable to us today. We don't have
*  words for it. We can't hint at it. We can't point at it. We can't look in the sky and see that thing
*  that is shining. We're going to go up there. You cannot even create an aspirational statement about
*  it. And instead, we've had this knee-jerk reaction of fear about everything that could go wrong.
*  But in my estimation, this should be the defining aspiration of all intelligent life on earth
*  that we would aspire. Basically, every generation surveys the landscape of possibilities that are
*  afforded. Given the technological, cultural, and other contextual situation that they're in,
*  we're in this context. We haven't yet identified this and said,
*  this is unbelievable. We should carefully think this thing through, not just of mitigating the
*  things that wipe us out. We have this potential. And so we just haven't given a voice to it,
*  even though it's within the realm of possibilities.
*  So you're excited about the possibility of superintelligence systems and what the
*  opportunities that bring. I mean, this parallels to this. You think about people before the
*  internet. As the internet was coming to life, there's kind of a fog through which you can't see
*  what does the future look like. Predicting collective intelligence, which I don't think
*  we're understanding that we're living through that now, is that there's now, we've in some sense,
*  stopped being individual intelligences and become much more like collective intelligences,
*  because ideas travel much, much faster now. And they can, in a viral way,
*  sweep across the population. And so it's almost, I mean, it almost feels like a thought is had by
*  many people now, thousands or millions of people, as opposed to an individual person.
*  And that's changed everything. But to me, I don't think we're realizing how much that actually
*  changed people or societies. But to predict that before the internet would have been very difficult.
*  And in that same way, we're sitting here with the fog before us thinking, what is
*  superintelligence systems? How is that going to change the world? What is increasing the bandwidth,
*  plugging our brains into this whole thing? How is that going to change the world? And it seems like
*  it's a fog, you don't know. And it could be, it could, whatever comes to be could destroy the world.
*  That we could be the last generation, but it also could transform in ways that creates an incredibly
*  fulfilling life experience that's unlike anything we've ever experienced. And it might involve the
*  solution of ego and consciousness and so on, you're no longer one individual. It might be more,
*  you know, that might be a certain kind of death and ego death. But the experience might be really
*  exciting and enriching. Maybe we'll live in a virtual, like, it's like, it's funny to think about
*  a bunch of sort of hypothetical questions of, would it be more fulfilling to live in a virtual world?
*  Like, if you were able to plug your brain in, in a very dense way, into a video game, like, which
*  world would you want to live in? In the video game or in the physical world? For most of us, we're kind
*  of toying with the idea of the video game, but we still want to live in the physical world, have
*  friendships and relationships in the physical world. But we don't know that, again, it's a fog.
*  And maybe in 100 years, we're all living inside a video game. Hopefully not Call of Duty.
*  Hopefully more like Sims 5. Which version is it on? For you individually, though,
*  does it make you sad that your brain ends? That you die one day very soon?
*  That the whole thing, that data source just goes offline sooner than you would like?
*  That's a complicated question. I would have answered it differently in different times in my
*  life. I, you know, I had chronic depression for 10 years. And so in that 10 year time period,
*  I desperately wanted lights to be off. And the thing that made it even worse is I was in a
*  religious, I was born into a religion. It was the only reality I ever understood. And it's
*  difficult to articulate to people when you're born into that kind of reality, and it's the only
*  reality you're exposed to, you're literally blinded to the existence of other realities,
*  because it's so much the in-group out-group thing. And so in that situation, it was not only that I
*  desperately wanted lights out forever, it was that I couldn't have lights out forever. It was that
*  it was that I couldn't have lights out forever. It was that there was an afterlife.
*  And this afterlife had this system that would either penalize or reward you for your behaviors.
*  And so it was almost like this indescribable hopelessness of not only being in hopeless
*  despair of not wanting to exist, but then also being forced to exist. And so there was a duration
*  of my time of a duration of life where I'd say, yes, I have no remorse for lights being out and
*  actually want it more than anything in the entire world. There are other times where I'm looking
*  out at the future and I say, this is an opportunity for future evolving human conscious experience
*  that is beyond my ability to understand. And I jump out of bed and I race to work and I can't
*  think about anything else. But I think the reality for me is, I don't know what it's like to be in
*  your head, but in my head, when I wake up in the morning, I don't say, good morning, Brian,
*  I'm so happy to see you. I'm sure you're just going to be beautiful to me today. You're not
*  going to make a huge long list of everything you should be anxious about. You're not going to repeat
*  that list to me 400 times. You're not going to have me relive all the regrets I've made in life.
*  I'm sure you're not doing any of that. You're just going to just help me along all day long.
*  It's a brutal environment in my brain. And we've just become normalized to this environment that
*  we just accept that this is what it means to be human. But if we look at it, if we try to muster
*  as much soberness as we can about the realities of being human, it's brutal if it is for me.
*  And so am I sad that the brain may be off one day?
*  It depends on the contextual setting. At what moment are you asking me that? And my mind is
*  so fickle. And this is why, again, I don't trust my conscious mind. I have been given realities.
*  I was given a religious reality that was a video game. And then I figured out it was not a real
*  reality. And then I lived in a depressive reality, which delivered this terrible hopelessness.
*  That wasn't a real reality. Then I discovered behavioral psychology and I figured out how biased,
*  188 chronicle biases, and how my brain is distorting reality all the time.
*  I have gone from one reality to another. I don't trust reality. I don't trust realities are given
*  to me. And so to try to make a decision on what I value or not value that future state, I don't
*  trust my response. So not fully listening to the conscious mind at any one moment
*  as the ultimate truth, but allowing you to go up and down as it does, and just kind of being
*  observing it. Yes, I assume that whatever my conscious mind delivers up to my awareness
*  is wrong on pond landing. And I just need to figure out where it's wrong, how it's wrong,
*  how wrong it is, and then try to correct for it as best I can. But I assume that on impact,
*  it's mistaken in some critical ways. Is there something you could say by way of advice
*  when the mind is depressive, when the conscious mind serves up something that,
*  you know, dark thoughts, how you deal with that, like how in your own life you've overcome that,
*  and others who are experienced in that can overcome it? Two things. One, that those depressive
*  states are biochemical states. It's not you. And the suggestions that these things, that this
*  state delivers to you about suggestion of the hopelessness of life or the meaninglessness of it,
*  or that you should hit the eject button, that's a false reality. And that it's when I completely
*  understand the rational decision to commit suicide. It is not lost to me at all that that is an
*  irrational situation, but the key is when you're in that situation, those thoughts are landing,
*  to be able to say, thank you, you're not real. I know you're not real. And so I'm in a situation
*  where for whatever reason I'm having this neurochemical state, but that state can be
*  altered. And so again, it goes back to the realities of the difficulties of being human.
*  And like when I was trying to solve my depression, I tried literally, if you name it, I tried it
*  systematically and nothing would fix it. And so this is what gives me hope with brain interfaces.
*  For example, like could I have numbers on my brain? Can I see what's going on? Because I go
*  to the doctor and it's like, how do you feel? I don't know. Terrible. Like on a scale from one
*  to 10, how bad do you want to commit suicide? 10. Like, okay. At this moment. Here's his bottle.
*  How much should I take? Well, I don't know. Like just. Yeah, it's very, very crude. And this data
*  opens up the, yeah, it opens up the possibility of really helping in those dark moments to first
*  understand the ways, the ups and downs of those dark moments. On the complete flip side of that,
*  I am very conscious in my own brain and deeply, deeply grateful that what there,
*  it's almost like a chemistry thing, a biochemistry thing that I go many times throughout the day.
*  I'll look at like this cup and I'll be overcome with joy. How amazing it is to be alive.
*  Like I actually think I'm my biochemistry is such that it's not as common. Like I've talked to
*  people and I don't think that's that common. Like it's a, and it's not a rational thing at all.
*  It's like, I feel like I'm on drugs and I'll just be like, whoa.
*  And a lot of people talk about like the meditative experience will allow you to sort of, you know,
*  look at some basic things like the movement of your hand as deeply joyful because it's like,
*  that's life. But I get that from just looking at a cup. Like I'm waiting for the coffee to brew.
*  I'll just be like, fuck, life is awesome. And I'll sometimes tweet that, but then I'll like,
*  regret it later. Like, God damn it. You so ridiculous. But yeah. So, but that is purely
*  chemistry. Like there's no rational, it doesn't fit with the rest of my life. I have all this shit.
*  I'm always late to stuff. I'm always like, there's all stuff, you know, I'm super self-critical,
*  like really self-critical about everything I do. I went to the point I will almost hate everything
*  I do, but there's this engine of joy for life outside of all that. And that has to be chemistry
*  and this flip side of that is what depression probably is, is the opposite of that feeling
*  of like, cause I bet you that feeling of the cup being amazing is, would save anybody in a state
*  of depression. Like that would be like fresh, you're in a desert and it's a drink of water.
*  Shit, man. The brain is a, it would be nice to understand where that's coming from
*  to be able to understand how you hit those lows and those highs that have nothing to do with the
*  actual reality. It has to do with some very specific aspects of how you maybe see the world. Maybe
*  it could be just like basic habits you engage in and then how to walk along the line to find
*  those experiences of joy. And this goes back to the discussion we're having of human cognition
*  is in volume, the largest input of raw material into society. And it's not quantified. We have no
*  bearings on it. And so we just, you wonder, we both articulated some of the challenges we have
*  in our own mind. And it's likely that others would say, I have something similar. And you wonder,
*  when you look at society, what, how does that contribute to all the other compounder problems
*  that we're experiencing? How does that blind us to the opportunities we could be looking at?
*  And so it really, it has this potential distortion effect on reality that just makes everything worse.
*  And I hope if we can put some, if we can assign some numbers to these things,
*  just to get our bearings, so we're aware of what's going on, if we could find greater
*  stabilization in how we conduct our lives and how we build society,
*  it might be the thing that enables us to scaffold. Because we've really, again, we've done enough,
*  humans have done a fantastic job systematically scaffolding technology and science institutions.
*  It's human, it's our own selves, which we have not been able to scaffold.
*  We are the one part of this intelligence infrastructure that remains unchanged.
*  Is there something you could say about coupling this brain data with not just the basic human
*  experience, but say an experience, you mentioned sleep, but the wildest experience, which is
*  psychedelics, is there, and there's been quite a few studies now that are being approved and run,
*  which is exciting from a scientific perspective on psychedelics. Do you think,
*  what do you think happens to the brain on psychedelics?
*  And how can data about this help us understand it? And when you're on DMT, do you see elves?
*  And can we convert that into data? Can you add aliens in there?
*  Yeah, aliens, definitely. Do you actually meet aliens? And elves are the aliens. I'm asking for
*  a few Austin friends that are convinced that they've actually met the elves.
*  What are elves like? Are they friendly? Are they helpful?
*  I haven't met them personally.
*  The smurfs, they're industrious and they have different skill sets.
*  Yeah, I think they're very critical as friends.
*  They're trolls. The elves are trolls.
*  No, but they care about you. There's a bunch of different versions of trolls. There's
*  loving trolls that are harsh on you, but they want you to be better. And there's trolls that just
*  enjoy your destruction. And I think they're the ones that care for you. I think they're a criticism.
*  I haven't met them directly. It's like a friend of a friend.
*  The whole point is that on psychedelics, and certainly on DMT,
*  this is where the brain data versus word data fails, which is words can't convey the experience.
*  You can be poetic and so on, but it really does not convey the experience of what it actually
*  means to meet the elves. To me, what baselines this conversation is, imagine if we were interested
*  in the health of your heart. And we started and said, okay, Lex, self-interests, tell me how's
*  the health of your heart. And you sit there and you close your eyes and you think, feels all right,
*  like things seem, things feel okay. And then you went to the cardiologist and the cardiologist
*  like, hey, Lex, tell me how you feel. And you're like, actually, what I'd really like you to do
*  is do an EKG and a blood panel and look at arterial plaques and let's look at my cholesterol. And
*  there's like five to 10 studies you would do. They then give you this report and say, here's
*  the quantified health of your heart. Now with this data, I'm going to prescribe the following regime
*  of exercise and maybe I'll put you on a statin, like, et cetera. But the protocol is based upon
*  this data. You would think the cardiologist is out of their mind if they just gave you a bottle of
*  statins based upon you're like, well, I think something's kind of wrong. And they're just kind
*  of experiment and see what happens. But that's what we do with our mental health today.
*  So it's kind of absurd. And so if you look at psychedelics, to have, again, to be able to measure
*  the brain and get a baseline state and then to measure during a psychedelic experience and post
*  the psychedelic experience and then do it longitudinally, you now have a quantification
*  of what's going on. And so you could then pose questions, what molecule is appropriate at what
*  dosages, at what frequency, in what contextual environment, what happens when I have this diet
*  with this molecule, this experience, all the experimentation you do when you have good sleep
*  data or HRV. And so that's what I think happens. What we could potentially do with psychedelics is
*  we could add this level of sophistication that is not in the industry currently, and it may
*  improve the outcomes people experience, it may improve the safety and efficacy.
*  And so that's what I hope we are able to achieve. And it would transform mental health because we
*  would finally have numbers to work with to baseline ourselves. And then if you think about it,
*  when we talk about things related to the mind, we talk about the modality. We use words like
*  meditation or psychedelics or something else, because we can't talk about a marker in the brain.
*  We can't use a word to say, we can't talk about cholesterol. We don't talk about plaque in the
*  arteries. We don't talk about HRV. And so if we have numbers, then the solutions get mapped to
*  numbers instead of the modalities being the thing we talk about. Meditation just does good things
*  in a crude fashion. So in your blog post, Zero Principle Thinking, good title, you ponder how
*  do people come up with truly original ideas? What's your thoughts on this as a human and as
*  a person who's measuring brain data? Zero principles are building blocks. First
*  principles are understanding of system laws. So if you take, for example, like in Sherlock Holmes,
*  he's a first principles thinker. So he says, once you've eliminated the impossible,
*  anything that remains, however improbable, is true. Whereas Dirk Gently, the holistic
*  detective by Douglas Adams says, I don't like eliminating the impossible. So when someone says
*  from a first principles perspective, and they're trying to assume the fewest number of things
*  within a given timeframe. And so when I, after Braintree Venmo, I set my mind to the question of
*  what single thing can I do that would maximally increase the probability that the human race
*  thrives beyond what we can even imagine? And I found that in my conversations with others,
*  in the books I read, in my own deliberations, I had a missing piece of the puzzle. Because I didn't
*  feel like, yeah, I didn't feel like the future could be deduced from first principles thinking.
*  And that's when I read the book Zero, a biography of a dangerous idea.
*  It's a really good book, by the way.
*  I think it's my favorite book I've ever read.
*  It's also a really interesting number, zero.
*  And I wasn't aware that the number zero had to be discovered. I didn't realize that it caused a
*  revolution in philosophy and just tore up math and it tore up, I mean, it builds modern society,
*  but it wrecked everything in its way. It was an unbelievable disruptor and it was so difficult
*  for society to get their heads around it. And so zero is of course, a representation of a
*  zero principle thinking, which is it's the caliber and consequential nature of an idea.
*  And so when you talk about what kind of ideas have civilization transforming properties,
*  oftentimes they fall in the zeroth category.
*  And so in thinking this through, I was wanting to find a quantitative structure on how to think
*  about these zeroth principles. And so I came up with that to be a coupler with first principles
*  thinking. And so now it's a staple as part of how I think about the world and the future.
*  So it emphasizes trying to identify, it lands on that word impossible, like what is impossible,
*  essentially trying to identify what is impossible and what is possible and being as,
*  I mean, this is the thing is most of society tells you the range of things they say is impossible
*  is very wide. So you need to be shrinking that. I mean, that's the whole process of
*  this kind of thinking is you need to be very rigorous in trying to be,
*  trying to draw the lines of what is actually impossible because very few things are actually
*  impossible. I don't know what is actually impossible. Like it's the Joe Rogan is entirely
*  possible. I like that approach to science, to engineering, to entrepreneurship. It's entirely
*  possible, basically shrink the impossible to zero to very small set.
*  Yeah. Life constraints favor first principles thinking because it enables faster action with
*  higher probability of success. Pursuing that is a very important thing. And so I think that's
*  success. Pursuing zero with principle optionality is expensive and uncertain. And so in a society
*  constrained by resources, time and money and a desire for social status, accomplishment, et
*  it minimizes zero principle thinking. But the reason why I think the zero principle thinking
*  should be a staple of our shared cognitive infrastructure is if you look through the
*  history of past couple thousand years and let's just say we arbitrarily, we subjectively try to
*  assess what is a zero level idea. And we say how many have occurred on what time scales and what
*  were the contextual settings for it? I would argue that if you look at AlphaGo, when it played Go
*  from another dimension, with the human Go players, when it saw AlphaGo's moves, it attributed it to
*  playing with an alien, playing Go with AlphaGo being from another dimension. And so if you say
*  computational intelligence has an attribute of introducing zero-like insights, then if you say
*  what is going to be the occurrence of zeros in society going forward? And you could reasonably say
*  probably a lot more than have occurred and probably more at a faster pace. So then if you say
*  what happens if you have this computational intelligence throughout society that the
*  manufacturing design and distribution of intelligence is now going to heading toward zero,
*  you have an increased number of zeros being produced with a tight connection between humans
*  and computers. That's when I got to a point and said we cannot predict the future with first
*  principles thinking. That cannot be our imagination set. It can't be our sole anchor in this situation
*  that basically the future of our conscious existence 20, 30, 40, 50 years is probably a zero.
*  So just to clarify, when you say zero, you're referring to basically a truly revolutionary idea.
*  Yeah, something that is currently not a building block of our shared conscious existence, either in
*  the form of knowledge. It's currently not manifest in what we acknowledge.
*  So zero principles thinking is playing with ideas that are so revolutionary that we can't
*  even clearly reason about the consequences once those ideas come to be.
*  Yeah, or for example, like Einstein, that was a zero, I would categorize it as a zero principle
*  insight. You mean general relativity, spacetime. Yeah, spacetime. Basically, that's the idea of
*  building upon what Newton had done and said yes, also, and it just changed the fabric of our
*  understanding of reality. And so that was unexpected. It existed. It became part of our
*  awareness. And the moves AlphaGo made existed. It just came into our awareness. And so to your point,
*  there's this question of what do we know and what don't we know? Do we think we know 99% of all
*  things or do we think we know 0.001% of all things? And that goes back to known knowns,
*  known unknowns and unknown unknowns. And first principles and zero principle thinking gives us
*  a quantitative framework to say there's no way for us to mathematically try to create probabilities
*  for these things. Therefore, it would be helpful if they were just part of our standard thought
*  processes, because it may encourage different behaviors in what we do individually, collectively
*  as a society, what we aspire to, what we talk about, the possibility sets we imagine.
*  Yeah, I've been engaged in that kind of thinking quite a bit. And thinking about engineering of
*  consciousness, I think it's feasible. I think it's possible in the language that we're using here.
*  And it's very difficult to reason about a world when inklings of consciousness can be engineered
*  into artificial systems. Not from a philosophical perspective, but from an engineering perspective,
*  I believe a good step towards engineering consciousness is creating engineering the illusion
*  of consciousness. I'm captivated by our natural predisposition to anthropomorphize things.
*  And I think that's what we I don't want to hear from the philosophers, but
*  I think that's what we kind of do to each other. That consciousness is created socially.
*  That much of the power of consciousness is in the social interaction. I create your consciousness,
*  no, I create my consciousness by having interacted with you. And that's the display of consciousness.
*  It's the same as the display of emotion. Emotion is created through communication.
*  Language is created through its use. And then we somehow, humans, especially philosophers,
*  the heart problem of consciousness, really want to believe that we possess this thing.
*  There's an elf sitting there with a hat or nametag that says consciousness, and they're feeding
*  this subjective experience to us, as opposed to it actually being an illusion that we construct
*  to make social communication more effective. And so I think if you focus on creating the illusion
*  of consciousness, you can create some very fulfilling experiences in software. And so that,
*  to me, is a compelling space of ideas to explore. I agree with you. And I think going back to our
*  experience together with Brain Interfaces on, you could imagine if we get to a certain level
*  of maturity. So first, let's take the inverse of this. So you and I text back and forth,
*  and we're sending each other emojis. That has a certain amount of information transfer rate as
*  we're communicating with each other. And so in our communication with people via email and text and
*  whatnot, we've taken the bandwidth of human interaction, the information transfer rate,
*  and we've reduced it. We have less social cues. We have less information to work with. There's a
*  lot more opportunity for misunderstanding. So that is altering the conscious experience
*  between two individuals. And if we add Brain Interfaces to the equation, let's imagine now we
*  amplify the dimensionality of our communications. That, to me, is what you're talking about, which
*  is consciousness engineering. Perhaps I understand you with dimensions. So maybe I understand
*  when you look at the cup and you experience that happiness, you can tell me you're happy. And I
*  then do theory of mine and say, I can imagine what it might be like to be Lex and feel happy
*  about seeing this cup. But if the interface could then quantify and give me a 50 vector space model
*  and say, this is the version of happiness that Lex is experiencing as he looks at this cup,
*  then it would allow me potentially to have much greater empathy for you and understand you as a
*  human. This is how you experience joy, which is entirely unique from how I experience joy,
*  even though we assumed ahead of time that we were having some kind of similar experience.
*  But I agree with you that we do consciousness engineering today in everything we do when we
*  talk to each other, when we're building products, and that we're entering into a stage where it will
*  be much more methodical and quantitative-based and computational in how we go about doing it,
*  which to me I find encouraging because I think it creates better guardrails to create
*  ethical systems versus right now I feel like it's really wild, wild west on how these interactions
*  are happening. Yeah. And it's funny you focus on human to human, but that this kind of data
*  enables human to machine interaction, which is what we're kind of talking about when we say
*  engineering consciousness. And that will happen, of course, let's flip that on its head. Right now
*  we're putting humans as the central node. What if we gave GPT-3 a bunch of human brains and said,
*  Hey, GPT-3, learn some manners when you speak and run your algorithms on humans' brains and see how
*  they respond so you can be polite and so that you can be friendly and so that you can be
*  conversationally appropriate, but to inverse it to give our machines a training set in real time
*  with closed loop feedback so that our machines were better equipped to find their way through
*  our society in polite and kind and appropriate ways. I love that idea. Or better yet, teach it some,
*  uh, have it read the finding documents and have it visit Austin and Texas. And so that when you ask,
*  when you tell it, why don't you learn some manners, it, GPT-3 learns to say no.
*  It learns what it means to be free and a sovereign individual. So that depends. So it depends what
*  kind of version of GPT-3 you want. One that's free, one that behaves well with the social revolution.
*  You want, you want to like, you want a socialist GPT-3, you want an anarchist GPT-3, you want to
*  polite, like you take it home to visit mom and dad GPT-3 and you want like party and like Vegas
*  to a strip club GPT-3. You want all flavors. And then you've got to have goal alignment
*  between all those. Yeah. They don't want to manipulate each other for sure.
*  Uh, so that's, I mean, you kind of spoke to ethics. The, one of the concerns that people have
*  in this modern world, the digital data is that of privacy and security,
*  but privacy, you know, they're concerned that when they share data,
*  it's the same thing with you. When we're, uh, trust other human beings, uh, in being fragile
*  and revealing something that we're vulnerable about, vulnerable about, there's a, there's a
*  leap of faith. There's a leap of trust that, uh, that's going to be just between us as a privacy
*  to it. And then the challenge is when you're in the digital space, then sharing your data
*  with companies that, uh, use that data for advertisement and all those kinds of things,
*  there's a hesitancy to share that much data, to share a lot of deep personal data. And if you look
*  at brain data, that feels a whole lot like it's richly, deeply personal data. So how do you think
*  about privacy with this kind of ocean of data? I think we got off to a wrong start with the internet
*  where the basic rules of play for the, for the company that be was if you're a company,
*  you can go out and get as much information on a person as you can find without their approval.
*  And you can also do things to induce them to give you as much information and you don't need to tell
*  them what you're doing with it. You can do anything on the backside. You can make money on it,
*  but the game is who can acquire the most information and devise the most clever schemes
*  to do it. That was a bad starting place. And so we are in this period where we need to correct
*  for that. And we need to say, first of all, the individual always has control over their data.
*  It's not a free for all. It's not like a game of hungry hippo, but they can just go out and grab
*  as much as they want. So for example, when your brain data was recorded today, the first thing
*  we did in the kernel app was you have control over your data. And so it's individual consent,
*  it's individual control, and then you can build up on top of that, but it has to be based upon
*  some clear rules of play of everyone knows what's being collected. They know what's being done with
*  it and the person has control over it. So transparency and control. So everybody knows
*  what does control look like? My ability to delete the data if I want. Yeah, delete it and to know
*  who is being shared with under what terms and conditions. We haven't reached that level
*  of sophistication with our products. If you say, for example, hey, Spotify, please give me a
*  customized playlist according to my neurome, you could say you can have access to this vector space
*  model, but only for this duration of time and then you've got to delete it. We haven't gotten
*  there to that level of sophistication, but these are ideas we need to start talking about of how do
*  you actually structure permissions? Yeah. And I think it creates a much more stable set
*  for society to build where we understand the rules of play and people aren't vulnerable to
*  being taken advantage. It's not fair for an individual to be taken advantage of without
*  their awareness with some other practice that some company is doing for their sole benefit.
*  And so hopefully we are going through a process now where we're correcting for these things and
*  that it can be an economy wide shift that because really these are
*  fundamentals we need to have in place. It's kind of fun to think about like in Chrome when you
*  install an extension or like install an app, it's ask you like what permissions you're willing to
*  give and be cool if in the future it says like you can have access to my brain data.
*  I mean it's not unimaginable in the future. The big technology companies have built a business
*  based upon acquiring data about you that they can then create a model of you and sell that
*  predictability. And so it's not unimaginable that you will create with like kernel device, for example,
*  a more reliable predictor of you than they could and that they're asking you for permission to
*  complete their objectives and you're the one that gets to negotiate that with them and say sure.
*  But so it's not unimaginable that might be the case.
*  So there's a guy named D.Lan Musk and he has a company, one of the many companies called Neuralink
*  that's also excited about the brain. So it'd be interesting to hear your kind of opinions
*  about a very different approach that's invasive, that requires surgery, that implants a data
*  collection device in the brain. How do you think about the difference between kernel and Neuralink
*  in the approaches of getting that stream of brain data?
*  Elon and I spoke about this a lot early on. We met up, I had started kernel and he had an interest
*  in brain interfaces as well and we explored doing something together, him joining kernel.
*  And ultimately it wasn't the right move and so he started Neuralink and I continued building kernel.
*  But it was interesting because we were both at this very early time where
*  it wasn't certain what, if there was a path to pursue, if now was the right time to do something
*  and then the technological choice of doing that. And so we were both, our starting point was looking
*  at invasive technologies and I was building invasive technology at the time. That's ultimately
*  where he's gone. A little less than a year after Elon and I were engaged, I shifted kernel to do
*  non-invasive. And we had this neuroscientist come to kernel we were talking about. He had been doing
*  a neural search for 30 years, one of the most respected neuroscientists in the US and we brought
*  him to kernel to figure out the ins and outs of his profession. And at the very end of our three
*  hour conversation he said, you know, every 15 or so years a new technology comes along
*  that changes everything. He said it's probably already here, you just can't see it yet.
*  And my jaw dropped. I had spoken to Bob Greenberg who had built a second site,
*  first on the optical nerve and then he did an array on the optical
*  cortex. And then I also became friendly with NeuroPace who does the implants for
*  seizure detection and remediation. And I saw in their eyes what it was like to take something
*  through an implantable device through for a 15 year run. They initially thought it was seven years
*  and it ended up being 15 years and they thought it'd be 100 million, 300, 400 million.
*  And I really didn't want to build invasive technology. It was the only thing that appeared
*  to be possible. But then once I spun up an internal effort to start looking at non-invasive options,
*  we said, is there something here? Is there anything here that again has the characteristics of,
*  it has the high quality data, it could be low cost, it could be accessible. Could it make
*  brain interfaces mainstream? And so I did a bet the company move. We shifted from non-invasive to
*  invasive to non-invasive. So the answer is yes to that. There is something there. It's possible.
*  The answer is we'll see. We've now built both technologies and they're now, you experienced
*  one of them today. We're now deploying it. So we're trying to figure out what value is really there.
*  But I'd say it's really too early to express confidence. I think it's too early to
*  assess which technological choice is the right one on what time scales.
*  Yeah, time scales are really important here. Very important. Because if you look at the,
*  like on the invasive side, there's so much activity going on right now of
*  less invasive techniques to get at the neuron firings, which what Neuralink is building,
*  it's possible that in 10, 15 years when they're scaling that technology, other things have come
*  along and you'd much rather do that, that thing starts to clock again. It may not be the case.
*  It may be the case that Neuralink has properly chosen the right technology and that that's
*  exactly what they want to be. Totally possible. And it's also possible that the path we chose
*  are non-invasive fall short for a variety of reasons. It's just, it's unknown. And so right
*  now, the two technologies we chose, the analogy I'd give you to create a baseline of understanding is
*  if you think of it like the internet in the 90s, the internet became useful when people could do a
*  dial-up connection. And then as bandwidth increased, so did the utility of that connection and so did
*  the ecosystem improve. And so if you say what kernel flow is going to give you a full screen
*  is going to give you a full screen on the picture of information, but as you're going to be watching
*  a movie, but the image is going to be blurred and the audio is going to be muffled. So it has a lower
*  resolution of coverage. A kernel flux, our MEG technology is going to give you the full movie
*  and 1080p. And Neuralink is going to give you a circle on the screen of 4k.
*  And so each one has their pros and cons and it's give and take. And so the decision I made
*  with kernel was that these two technologies, flux and flow, were basically the answer for the next
*  seven years. And they would give rise to the ecosystem, which would become much more valuable
*  than the hardware itself. And that we would just continue to improve on the hardware over time.
*  And you know, it's early days. So it's kind of fascinating to think about that.
*  It's very true that you don't know both paths are promising.
*  And it's like 50 years from now, we will look back and maybe not even remember one of them.
*  And the other one might change the world. It's so cool how technology is. I mean,
*  that's what entrepreneurship is. It's like, it's the zeorth principle is like you're marching
*  ahead into the darkness, into the fog, not knowing. It's wonderful to have someone else
*  out there with us doing this. Because if you look at brain interfaces, anything that's off the shelf
*  right now is inadequate. It's had its run for a couple decades. It's still in hacker communities.
*  It hasn't gone to the mainstream. The room size machines are on their own path.
*  But there is no answer right now of bringing brain interfaces mainstream. And so both they and us,
*  we've both spent over a hundred million dollars. And that's kind of what it takes to have a go
*  at this because you need to build full stack. I mean, at Kernel, we are from the photon and the
*  atom through the machine learning. We have just under a hundred people. I think it's something
*  like 36, 37 PhDs in these specialties, these areas that there's only a few people in the world who
*  have these abilities. And that's what it takes to build next generation, to make an attempt
*  at breaking into brain interfaces. And so we'll see over that couple of years, whether it's the
*  right time or whether we were both too early or whether something else comes along in seven to
*  10 years, which is the right thing that brings it mainstream. So you see Elon as a kind of competitor
*  or a fellow traveler along the path of uncertainty or both. It's a fellow traveler.
*  It's like at the beginning of the internet is how many companies are going to be invited to
*  this new ecosystem. Like an endless number, because if you think that the hardware
*  just starts the process and so, okay, back to your initial example. If you take the Fitbit,
*  for example, you say, okay, now I can get measurements on the body. And what do we think
*  the ultimate value of this device is going to be? What is the information transfer rate?
*  And they were in the market for a certain duration of time and Google bought them for
*  two and a half billion dollars. They didn't have ancillary value add. There weren't people building
*  on top of the Fitbit device. They also didn't have increased insight with additional data streams.
*  So it's really just the device. If you look, for example, at Apple and the device they sell,
*  you have value in the device that someone buys, but also you have everyone who's building on
*  top of it. So you have this additional ecosystem value, and then you have additional data streams
*  that come in, which increase the value of the product. And so if you look at the hardware as
*  the instigator of value creation, over time, what we've built may constitute five or 10% of
*  the value of the overall ecosystem. And that's what we really care about. What we're trying to
*  do is kickstart the mainstream adoption of quantifying the brain. And the hardware just
*  opens the door to say what kind of ecosystem could exist. And that's why the examples are so
*  relevant of the things you've outlined in your life. I hope those things, the books people write,
*  the experiences people build, the conversations you have, your relationship with your AI systems,
*  I hope those all are feeding on the insights built upon this ecosystem we've created to better your
*  life. And so that's the thinking behind it. Again, with the Drake equation being the underlying
*  driver of value. And the people at Kernel have joined not because we have
*  certainty of success, but because we find it to be the most exhilarating opportunity we could ever
*  pursue in this time to be alive. You founded the payment system Braintree in 2007. That acquired
*  Venmo in 2012. And that in that same year was acquired by PayPal, which is now eBay.
*  Can you tell me the story of the vision and the challenge of building an online payment system
*  and just building a large successful business in general? I discovered payments by accident.
*  As I was when I was 21, I just returned from Ecuador, living among extreme poverty for two
*  years. And I came back to the US and I was shocked by the opulence of the United States.
*  And I just thought, I couldn't believe it. And I decided I wanted to try to spend my life
*  helping others. That was the life objective that I thought was worthwhile to pursue versus making
*  money and whatever the case may be for its own right. And so I decided in that moment that I
*  was going to try to make enough money by the age of 30 to never have to work again.
*  And then with some abundance of money, I could then choose to do things that might be beneficial
*  to others, but may not meet the criteria of being a standalone business. And so in that process,
*  I started a few companies, had some small successes, had some failures. In one of the
*  endeavors, I was up to my eyeballs in debt. Things were not going well and I needed a part-time job
*  to pay my bills. And so one day I saw in the paper in Utah where I was living, the 50 richest
*  people in Utah, and I emailed each one of their assistants and said, I'm young, I'm resourceful,
*  I'll do anything. I'm entrepreneurial. I tried to get a job that would be flexible and no one
*  responded. And then I interviewed at a few dozen places. Nobody would even give me the time of day.
*  It wouldn't want to take me seriously. And so finally, it was on monster.com that I saw this
*  job posting for credit card sales door to door. Commission. I did not know the story. This is
*  great. I love the head drop. That's exactly right. So it was the low points to which would go in life.
*  So I responded and the person made an attempt at suggesting that they had some kind of standards
*  that they would consider hiring. But it's kind of like if you could fog a mirror,
*  come and do this because it's a hundred percent commission. And so I started walking up and down
*  the street in my community selling credit card processing. And so what you learn immediately in
*  doing that is if you walk into a business, first of all, the business owner is typically there.
*  And you walk in the door and they can tell by how you're dressed or how you walk, whatever their
*  pattern recognition is. And they just hate you immediately. It's like, stop wasting my time. I
*  really am trying to get stuff done. I don't want us to a sales pitch. And so you have to overcome
*  the initial get out. And then once you engage, when you say the word credit card processing,
*  the person's like, I already hate you because I have been taken advantage of dozens of times
*  because you all are weasels. And so I had to figure out an algorithm to get past all those
*  different conditions. Cause I was still working on my other startup for the majority of my time.
*  That's doing this part time. And so I figured out that the industry really was built on
*  people, on deceit, basically people problems and things that were not reality. And so I'd walk
*  into a business and I'd say, look, I would give you a hundred dollars. I'd put a hundred dollar bill
*  and say, I'll give you a hundred dollars for three minutes of your time. If you don't say yes to what
*  I'm saying, I'll give you a hundred dollars. And then he'd usually crack a smile and say, okay,
*  what do you got for me, son? And so I'd sit down and I just opened my book and I'd say,
*  here's the credit card industry. Here's how it works. Here are the players. Here's what they do.
*  Here's how they deceive you. Here's what I am. I'm no different than anyone else. It's like,
*  you're going to process your credit card. You're going to get the money in the account. You're
*  just going to get a clean statement. You're going to have someone who answers the call when someone
*  asks and you know, just like the basic, like you're okay. And people started saying yes.
*  And then of course I went to the next business and be like, you know, Joe and Susie and whoever
*  said yes to, and so I built a social proof structure and I became the number one salesperson
*  out of 400 people nationwide doing this. And I worked, you know, half time still doing so
*  their startup. And that's a brilliant strategy, by the way. It's very well, very well strategized
*  and executed. They did it for nine months. And at the time my customer base was making,
*  was generating around, I think it was sick. If I remember correctly, $62,504 a month.
*  Where the overall revenues, I thought, wow, that's amazing. If I built that as my own company,
*  I would just make $62,000 a month of income passively with these merchants processing
*  credit cards. So I thought, hmm. And so that's when I thought I'm going to create a company.
*  And so then I started Braintree and the idea was the online world was broken because PayPal
*  had been acquired by eBay around, I think 1999 or 2000. And eBay had not innovated much with PayPal.
*  So it basically sat still for seven years as the software world moved along. And then authorized.net
*  was also a company that was relatively stagnant. So you basically had software engineers who wanted
*  modern payment tools, but there were none available for them. And so they just dealt with software
*  they didn't like. And so with Braintree, I thought the entry point is to build software that engineers
*  will love. And if we can find the entry point via software and make it easy and beautiful and
*  just a magical experience, and then provide customer service on top of that, it was easy.
*  That would be great. What I was really going after though, it was PayPal. They were the only
*  company in payments making money because they had the relationship with eBay early on.
*  People created a PayPal account. They had fund their account with their checking account versus
*  their credit cards. And then when they'd use PayPal to pay a merchant, PayPal had a cost of
*  payment of zero versus if you have coming from a credit card, you have to pay the bank the fees.
*  So PayPal's margins were 3% on a transaction versus a typical payments company, which may be a nickel
*  or a penny or a dime or something like that. And so I knew PayPal really was the model to replicate,
*  but a bunch of companies had tried to do that. They tried to come in and build a two-sided
*  marketplace to get consumers to fund the checking account and the merchants to accept it.
*  But they'd all failed because building a two-sided marketplace is very hard at the same time. So my
*  plan was I'm going to build a company and get the best merchants in the whole world to use our
*  service. Then in year five, I'm going to acquire a consumer payments company and I'm going to
*  bring the two together. So focus on the merchant side. Exactly. And then get the payments company
*  does the customer, the whatever. So the other side. Yeah. This is the plan I presented
*  when I was at the University of Chicago. And weirdly it happened exactly like that. So four
*  years in, our customer base included Uber, Airbnb, GitHub, 37 signals, not Basecamp. We had a
*  fantastic collection of companies that represented some of the fastest growing tech companies in the
*  world. And then we met up with Venmo and they had done a remarkable job in building product.
*  And then something very counterintuitive, which is make public your private financial transactions,
*  which people previously thought were something that should be hidden from others. And we acquired
*  Venmo. And at that point we now had, we replicated the model because now people could fund their
*  Venmo account with their checking account, keep money in the account, and then you could just
*  plug Venmo in as a form of payment. And so I think PayPal saw that, that we were
*  getting the best merchants in the world. We had people using Venmo. They were both the up and
*  coming millennials at the time who had so much influence online. And so they came in and offered
*  us an attractive number. And my goal was not to build the biggest payments company in the world.
*  It wasn't to try to climb the Forbes billionaire list. The objective was I want to earn enough
*  money so that I can basically dedicate my attention to doing something that could potentially be useful
*  on a society-wide scale. And more importantly, that could be considered to be valuable
*  from the vantage point of 2050, 2100, and 2500. So thinking about it on a few hundred year timescale.
*  And there was a certain amount of money I needed to do that. So I didn't require the permission of
*  anybody to do that. And so that what PayPal offered was sufficient for me to get that amount of money
*  to basically have a go. And that's when I set off to survey everything I could identify and
*  existence to say of anything in the entire world I could do, what one thing could I do that would
*  actually have the highest value potential for the species. And so it took me a little while to arrive
*  at Brain Interfaces. But you know, payments in themselves are revolutionary technologies that
*  can change the world. Let's not forget that too easily. I mean, obviously,
*  you know this, but there's quite a few lovely folks who are now fascinated with the space of
*  cryptocurrency. And payments are very much connected to this, but in general, just money.
*  And many of the folks I've spoken with, they also kind of connect that to not just purely financial
*  discussions, but philosophical and political discussions. And they see Bitcoin as a way,
*  almost as activism, almost as a way to resist the corruption of centralized, of centers of power.
*  And sort of basically in the 21st century, decentralizing control, whether that's Bitcoin
*  or other cryptocurrencies, they see that's one possible way to give power to those that live in
*  regimes that are corrupt or are not respectful of human rights and all those kinds of things.
*  What's your sense, just all your expertise with payments and seeing how that changed the world,
*  what's your sense about the lay of the land for the future of Bitcoin or other cryptocurrencies
*  in the positive impact it may have on the world? To be clear, my communication wasn't
*  suggest, wasn't meant to minimize payments or to denigrate it in any way. It was an attempted
*  communication that when I was surveying the world, it was an algorithm of what could I individually
*  do? So there are things that exist that have a lot of potential that can be done. And then there's a
*  filtering of how many people are qualified to do this given thing. And then there's a further
*  characterization that can be done of, okay, given the number of qualified people, will somebody be
*  a unique out performer of that group to make something truly impossible to be something done
*  that otherwise couldn't get done? So there's a process of assessing where can you add unique
*  value in the world. And some of that has to do with, you're being very formal and calculative
*  here, but some of that is just like, what do you sense? Like part of that equation is how much
*  passion you sense within yourself to be able to drive that through, to discover the possibilities
*  and make them possible. That's right. And so we were a brain tree. I think we were the first
*  company to integrate Coinbase into our, I think we were the first payments company to formally
*  incorporate crypto, if I'm not mistaken. For people who are not familiar, Coinbase is a place
*  where you can trade cryptocurrencies. Yeah, which was one of the only places you could. So we were
*  early in doing that. And of course, this was in the year 2013. So an attorney to go in
*  cryptocurrency land. I concur with the statement you made of the potential of
*  the principles underlying cryptocurrencies. And that many of the things that they're building
*  in the name of money and of moving value is equally applicable to the brain and equally
*  applicable to how the brain interacts with the rest of the world and how we would imagine doing
*  goal alignment with people. So to me, it's a continuous spectrum of possibility. And we're
*  taught, your question is isolated on the money. And I think it just is basically a scaffolding
*  layer for all of society. So you don't see this money as particularly distinct from-
*  I don't. I think we at Kernel, we will benefit greatly from the progress being made in
*  cryptocurrency because it will be a similar technology stack we will want to use for many
*  things we want to accomplish. And so I'm bullish on what's going on and think it could greatly
*  enhance brain interfaces and the value of the brain interface ecosystem. I mean, is there something
*  you could say about, first of all, bullish on cryptocurrency versus fiat money? So do you have
*  a sense that in 21st century, cryptocurrency will be embraced by governments and changed
*  the face of governments, the structure of governments?
*  It's the same way I think about my diet, where previously it was conscious Brian
*  in looking at foods in certain biochemical states. Am I hungry? Am I irritated? Am I depressed?
*  And then I choose based upon those momentary windows. Do I eat at night when I'm fatigued
*  and I have low willpower? Am I going to pig out on something? And the current monetary system
*  is based upon human conscious decision-making and politics and power and this whole mess of things.
*  And what I like about the building blocks of cryptocurrencies, it's methodical, it's structured,
*  it is accountable, it's transparent. And so it introduces this scaffolding, which I think,
*  again, is the right starting point for how we think about building next generation
*  institutions for society. And that's why I think it's much broader than money.
*  So I guess what you're saying is Bitcoin is the demotion of the conscious mind as well.
*  Yeah. In the same way you were talking about diet, it's like giving less priority to the
*  the ups and downs of any one particular human mind, in this case, your own,
*  and giving more power to the sort of data driven.
*  Yes. Yeah. I think that is accurate that cryptocurrency is a version of what I would call my
*  autonomous self that I'm trying to build. It is an introduction of an autonomous system
*  of value exchange and the process of value creation in society. Yes, there are similarities.
*  So I guess what you're saying is Bitcoin will somehow help me not pig out at night,
*  or the equivalent of speaking of diet, if we could just linger on that topic a little bit.
*  We already talked about your blog post of I fired myself, I fired Brian, the evening
*  Brian, who is too willing to not making good decisions for the long term well-being and
*  happiness of the entirety of the organism. Basically, you were like pigging out at night.
*  But it's interesting, because I do the same. In fact, I often eat one meal a day.
*  And like I have been this this week, actually, especially when I travel. And it's funny that
*  it never occurred to me to just basically look at the fact that I'm able to be much smarter about
*  my eating decisions in the morning and the afternoon than I am at night. So if I eat one meal a day,
*  why not eat that one meal a day in the morning? I got not. It never occurred to me.
*  This revolution? Yeah. Until you've, you've outlined that. So maybe, can you give some details in
*  what this is just you? This is one person, Brian, arrives at a particular thing that they do. But
*  it's fascinating to kind of look at this one particular case study. So what works for you
*  diet wise? What's your actual diet? What do you eat? How often do you eat?
*  My current protocol is basically the result of thousands of experiments and decision making. So
*  I do this every 90 days. I do the tests. I do the cycle throughs. Then I measure again. And then
*  I'm measuring all the time. And so what I, I of course, I'm optimizing for my biomarkers. I want
*  perfect cholesterol and I brought perfect blood glucose levels and perfect DNA methylation,
*  you know, processes. I also want perfect sleep. And so for example, recently in the past two weeks,
*  my resting heart rate has been a 42 when I sleep. And when my resting heart rate is at 42,
*  my HRV is at its highest. And I wake up in the morning feeling more energized than any other
*  configuration. And so I know from all these processes, that eating at roughly 830 in the
*  morning, right after I work out on an empty stomach, creates enough distance between that
*  completed eating and bedtime where I have no almost no digestion processes going on in my body.
*  Therefore my resting heart rate goes very low. And when my resting heart rate is very low,
*  I sleep with high quality. And so basically I've been trying to optimize the entirety of what I
*  eat to my sleep quality. And my sleep quality then of course feeds into my willpower. So it creates
*  this virtuous cycle. And so at 830, what I do is I eat what I call super veggie, which is it's a
*  pudding of 250 grams of broccoli, 150 grams of cauliflower and a whole bunch of other vegetables
*  that I eat what I call nutty pudding, which is-
*  You make the pudding yourself like a veggie mix, whatever thing, like a blender?
*  Yeah, you can be made in a high speed blender. But basically I eat the same thing every day,
*  veggie bowl as in the form of pudding and then a bowl in the form of nuts. And then I have-
*  So vegan.
*  Vegan, yes.
*  Vegan. So that's fat and that's like, that's fat and carbs and some protein and so on.
*  Then I have a third-
*  Does it taste good?
*  I love it. I love it so much I dream about it.
*  Yeah, that's awesome. This is-
*  And then I have a third dish, which is, it changes every day. Today it was kale and spinach and
*  sweet potato. And then I take about 20 supplements that hopefully constitute a perfect nutritional
*  profile. So what I'm trying to do is create the perfect diet for my body every single day.
*  Where sleep is part of the optimization.
*  That's right.
*  You're like one of the things you're really tracking. I mean, can you, well, I have a million
*  questions, but 20 supplements, like what kind are, like would you say are essential? Because I only
*  take Athletic Greens.com slash
*  I want an algorithm for perfect health that I never have to think about. And then I want that
*  system to be scalable to anybody so that they don't have to think about it. And right now it's
*  expensive for me to do it. It's time consuming for me to do it. And I have infrastructure to do it,
*  but the future of being human is not going to the grocery store and deciding what to eat.
*  It's also not reading scientific papers trying to decide this thing or that thing. It's all
*  N of one. So it's devices on the outside and inside your body, assessing real time what your
*  body needs and then creating closed loop systems for that to happen.
*  Yeah. So right now you're doing the data collection and you're being the scientist.
*  It'd be much better if you're doing just that. If you just did the data collect,
*  or it was being essentially done for you and you can outsource that to another scientist that's
*  doing the N of one study of you. That's right. Because every time I spend time thinking about
*  this or executing spending time on it, I'm spending less time thinking about building kernel
*  or the future of being human. And so we just all have the budget of our capacity on an everyday
*  basis and we will scaffold our way up out of this. And so yeah, hopefully what I'm doing is really,
*  it serves as a model that others can also build on. That's why I wrote about it is hopefully
*  people can then take it and improve upon it. I hold nothing sacred. I change my diet
*  almost every day based upon some new test results or science or something like that.
*  Can you maybe elaborate on the sleep thing? Why is sleep so important?
*  And why, presumably, what does good sleep mean to you?
*  I think sleep is a contender for being the most powerful
*  health intervention in existence. It's a contender. I mean, it's magical what it does if you're well
*  rested and what your body can do. And I mean, for example, I know when I eat close to my bedtime,
*  and I've done a systematic study for years looking at like 15 minute increments on time of day on
*  where I eat my last meal, my willpower is directly correlated to the amount of deep sleep I get.
*  So my ability to not binge eat at night when Rascal Bryan's out and about is based upon how
*  much deep sleep I got the night before. Yeah, there's a lot to that, yeah.
*  And so I've seen it manifest itself. And so I think the way I summarize this is in society,
*  we tell stories, for example, of entrepreneurship, where this person was so amazing,
*  they stayed at the office for three days and slept under their desk. And we say, wow, that's amazing.
*  That's amazing. And now I think we're headed towards a state where we'd say that's primitive
*  and really not a good idea on every level. And so the new mythology of sleep is that it's
*  the new mythology is going to be the exact opposite.
*  Yeah, by the way, just to sort of maybe push back a little bit on that idea.
*  Did you sleep under your desk, Alex?
*  Well, yeah, a lot. I'm a big believer in that, actually. I'm a big believer in
*  chaos and not giving, like giving into your passion. And sometimes doing things that are out of the
*  ordinary, they're like not trying to optimize health for certain periods of time
*  in lieu of your passions is a signal to yourself that you're throwing everything away. So
*  I think what you're referring to is how to have good performance for prolonged periods of time.
*  I think there's moments in life when you need to throw all of that away, all the plans away,
*  all the structure away. So I'm not sure I have an eloquent way of describing exactly what I'm
*  talking about, but it all depends on people. People are different, but there's a danger of
*  over optimization to where you don't just give into the madness of the way your brain flows.
*  I mean, to push back on my pushback is like, it's nice to have like where the
*  foundations of your brain are not messed with. So you have a fixed foundation where the diet is fixed,
*  where the sleep is fixed, and that all of that is optimal. And the chaos happens in the space of
*  ideas as opposed to the space of biology. But, you know, I'm not sure if there's a
*  that requires real discipline and forming habits. There's some aspect to which some of the
*  best days and weeks of my life have been, yeah, sleeping under a desk kind of thing.
*  And I don't, I'm not too willing to let go of things that empirically worked
*  for things that work in theory. And so I'm, again, I'm absolutely with you on sleep.
*  Also, I'm with you on sleep conceptually, but I'm also very humbled to understand that for
*  different people, good sleep means different things. I'm very hesitant to trust science on
*  sleep. I think you should also be a scholar of your own body. Again, the experiment of N of one.
*  I'm not so sure that a full night's sleep is great for me. There is something about that power nap
*  that I just have not fully studied yet. But that nap is something special.
*  I'm not sure I found the optimal thing. So like, there's a lot to be explored to what is exactly
*  optimal amount of sleep, optimal kind of sleep, combined with diet and all those kinds of, I mean,
*  that all maps the sort of data, at least the truth, exactly what you're referring to.
*  Here's a data point for your consideration. Yes.
*  The progress in biology over the past, say, decade has been stunning. Yes. And it now appears as if
*  we will be able to replace our organs, x-ray transplantation. And so
*  we probably have a path to replace and regenerate every organ of your body, except for your brain.
*  You can lose your hand and your arm and a leg, you can have an artificial heart.
*  You can't operate without your brain. And so when you make that trade-off decision of whether
*  you're going to sleep under the desk or not and go all out for a four-day
*  marathon, right? There's a cost-benefit trade-off of what's happening to your brain in that situation.
*  We don't know the consequences of modern day life on our brain.
*  It's the most valuable organ in our existence. And we don't know what's going on in how we're
*  treating it today with stress and with sleep and with dietary. And to me, then if you say,
*  that you're trying to optimize life for whatever things you're trying to do,
*  the game is soon, with the progress in anti-aging and biology, the game is very soon going to become
*  different than what it is right now with organ rejuvenation, organ replacement. And I would
*  conjecture that we will value the health status of our brain above all things.
*  Yeah, no, absolutely. Everything you're saying is true, but we die. We die pretty quickly. Life is
*  short. And I'm one of those people that I would rather die in battle than stay safe at home.
*  It's like, yeah, you look at kind of, there's a lot of things that you can reasonably say,
*  this is the smart thing to do that can prevent you, that becomes conservative, that can prevent
*  you from fully embracing life. I think ultimately you can be very intelligent and data-driven
*  and also embrace life. But I err on the side of embracing life. It takes a very skillful person
*  to not sort of that hovering parent that says, no, you know what? There's a 3% chance that if you go
*  out by yourself and play, you're going to die, get run over by a car, come to a slow or a sudden end.
*  I'm more a supporter of just go out there. If you die, you die. And that's a balance you have to
*  strike. I think there's a balance to strike in long-term optimization and short-term
*  freedom. For me, for a programmer, for a programming mind, I tend to over-optimize and I'm
*  very cautious and afraid of that. To not over-optimize and thereby be overly cautious,
*  suboptimally cautious about everything I do. And then the ultimate thing I'm trying to optimize
*  for is funny you said like sleep and all those kinds of things. I tend to think,
*  you're being more precise than I am, but I think I tend to want to minimize stress,
*  which everything comes into that from your sleep and all those kinds of things. But
*  I worry that whenever I'm trying to be too strict with myself, then the stress goes up
*  when I don't follow the strictness. And so you have to kind of, it's a weird, there's so much
*  variables in an objective function, it's hard to get right. And sort of not giving a damn about
*  sleep and not giving a damn about diet is a good thing to inject in there every once in a while
*  for somebody who's trying to optimize everything. But that's me just trying to, like it's exactly
*  like you said, you're just a scientist, I'm a scientist of myself, you're a scientist of
*  yourself. It'd be nice if somebody else was doing it and had much better data
*  because I don't trust my conscious mind. And I pigged out last night at some brisk
*  in LA that I regret deeply. There's no point to anything I just said.
*  What is the nature of your regret on the brisket? Do you wish you hadn't eaten it entirely? Is it
*  that you wish you hadn't eaten as much as you did? Is it that?
*  I think, well, most regret is that I didn't eat as much as I did. I think that's the
*  most regret. I mean, if we want to be specific, I drank way too much like diet soda.
*  My biggest regret is like having drank so much diet soda. That's the thing that really was the
*  problem. I had trouble sleeping because of that. Because I was like programming and then I was
*  editing. So I stayed up late at night and then I had to get up to go pee a few times and it was
*  just a mess. A mess of a night. Well, it's not really a mess, but like it's so many, it's like
*  the little things. I know if I just eat, I drink a little bit of water and that's it.
*  All of us have perfect days that we know diet wise and so on that's good to follow. You feel
*  good. I know what it takes for me to do that. I didn't fully do that and thereby, because there's
*  an avalanche effect where the other sources of stress, all the other to-do items I have pile on
*  my failure to execute on some basic things that I know make me feel good and all that combines
*  to create a mess of a day. But some of that chaos, you have to be okay with it, but some of it I
*  wish was a little bit more optimal. And your ideas about eating in the morning are quite interesting
*  as an experiment to try. Can you elaborate? Are you eating once a day? Yes. In the morning
*  and that's it. Can you maybe speak to how that... You spoke, it's funny, you spoke about the metrics
*  of sleep, but you're also, you run a business, you're incredibly intelligent. You have to,
*  mostly your happiness and success relies on you thinking clearly. So how does that affect your
*  mind and your body in terms of performance? So not just sleep, but actual like mental performance.
*  As you were explaining your objective function of, for example, in the criteria you were including,
*  you like certain neurochemical states, like you like feeling like you're living life,
*  that life has enjoyment, that sometimes you want to disregard certain rules to have a moment of
*  passion, of focus. There's this architecture of the way Lex is, which makes you happy as a story
*  you tell, as something you kind of experience. Maybe the experience is a bit more complicated,
*  in this idea you have, this is a version of you. And the reason why I maintain the schedule I do
*  is I've chosen a game to say, I would like to live a life where I care more about what
*  intelligent, what people who live in 2000, the year 2500 think of me than I do today.
*  That's the game I'm trying to play. And so therefore, the only thing I really care about
*  on this optimization is trying to see past myself, past my limitations, using zero principle thinking,
*  pull myself out of this contextual mesh we're in right now and say, what will matter 100 years
*  from now and 200 years from now? What are the big things really going on that are defining reality?
*  And I find that if I were to hang out with diet soda Lex and diet soda Brian were to play along
*  with that, and my deep sleep were to get crushed as a result, my mind would not be on what matters
*  in 100 years or 200 years or 300 years. I would be irritable. I would be in a different state.
*  You know, I'd be in a different state. And so it's just gameplay selection. It's what you and I have
*  chosen to think about. It's what we've chosen to work on. And this is why I'm saying that no
*  generation of humans have ever been afforded the opportunity to look at their lifespan and
*  contemplate that they will have the possibility of experiencing an evolved form of consciousness.
*  That is undeniable. They would fall in a zero category of potential. That to me is the most
*  exciting thing in existence. And I would not trade any momentary neurochemical state right now in
*  exchange for that. I'd be willing to deprive myself of all momentary joy in the pursuit of that goal
*  because that's what makes me happy. That's brilliant. But I'm a bit, I just looked it up.
*  I just looked up Braveheart's speech in William Wallace. I don't know if you've seen it.
*  Fight and you may die, run and you'll live at least a while. And dying in your beds many years
*  from now, would you be willing to trade all the days from this day to that for one chance,
*  just one chance, picture Mel Gibson saying this, to come back here and tell our enemies that they
*  may take our lives with growing excitement, but they'll never take our freedom. I get excited
*  every time I see that in the movie, but that's kind of how I approach life. And do you think
*  they were tracking their sleep? They were not tracking their sleep and they ate way too much
*  brisket and they were fat, unhealthy, died early and were primitive. But there's something in my
*  eight brain that's attracted to that, even though most of my life is fully aligned with the way you
*  see yours. And part of it is for comedy, of course, but part of it is like, I'm almost afraid of
*  over optimization. Really what you're saying though, if we're looking at this, let's say from a first
*  principles perspective, when you read those words, they conjure up certain life experiences, but
*  you're basically saying I experienced a certain neurotransmitter state when these things are in
*  action. That's all you're saying. So whether it's that or something else, you're just saying
*  you have a selection for how your state for your body. And so if you as an engineer of consciousness,
*  that should just be engineerable. And that's just triggering certain chemical reactions.
*  So it doesn't mean they have to be mutually exclusive. You can have that and experience
*  that and also not sacrifice long-term health. And I think that's the potential of where we're going
*  is we don't have to assume they are trade-offs that must be had. Absolutely. And so I guess from
*  my particular brain, it's useful to have the outlier experiences that also come along with the
*  illusion of free will where I chose those experiences that make me feel like it's freedom.
*  Listen, going to Texas made me realize I spent so I was, I still am, but I lived at Cambridge and MIT
*  and I never felt like home there. I felt like home in the space of ideas with the colleagues,
*  like when I was actually discussing ideas, but there is something about the constraints,
*  how cautious people are, how much they valued also kind of material success, career success.
*  When I showed up to Texas, it felt like I belong. That was very interesting, but that's my neuro
*  chemistry, whatever the hell that is, whatever, maybe probably is rooted to the fact that I grew
*  up in the Soviet Union. It was so such a constrained system that you really deeply value freedom and
*  you always want to escape the demand and the control of centralized systems. I don't know
*  what it is, but at the same time, I love strictness. I love the dogmatic authoritarianism of diet,
*  of like the same habit, exactly the habit you have. I think that's actually when bodies perform
*  optimally, my body performs optimally. So balancing those two, I think if I have the data
*  every once in a while, party with some wild people, but most of the time he wants a day,
*  perhaps in the morning, I'm going to try that. It might be very interesting, but I'd rather not
*  try it. I'd rather have the data that tells me to do it, but in general, you're able to eating once
*  a day, think deeply about stuff like this. A concern that people have is like, you know,
*  does your energy wane? All those kinds of things. Do you find that it's, especially because
*  it's unique, it's vegan as well. So you find that you're able to have a clear mind, a focus,
*  and just physically and mentally throughout? Yeah. I find like my personal experience in
*  thinking about hard things is like, oftentimes I feel like I'm looking through a telescope
*  and I come aligning two or three telescopes and you kind of have to close one eye and move it back
*  and forth a little bit and just find just the right alignment. Then you find just a sneak peek
*  at the thing you're trying to find, but it's fleeting. If you move just one little bit,
*  it's gone. And oftentimes what I feel like are the ideas I value the most are like that. They're
*  so fragile and fleeting and slippery and elusive. And it requires a sensitivity
*  to thinking and a sensitivity to maneuver through these things. If I
*  concede to a world where I'm on my phone texting, I'm also on social media. I'm also doing 15
*  things at the same time because I'm running a company and I'm also feeling terrible from the
*  last night. It all just comes crashing down and the quality of my thoughts goes to a zero. I'm
*  a functional person to respond to basic level things, but I don't feel like I'm doing anything
*  interesting. I think that's a good word, sensitivity, because that's what thinking deeply feels like,
*  is you're sensitive to the fragile thoughts and you're right. All those other distractions
*  dull your ability to be sensitive to the fragile thoughts. It's a really good word.
*  Out of all the things you've done, you've also climbed Mount Kilimanjaro. Is this true?
*  It's true.
*  Why and how and what do you take from that experience?
*  I guess the backstory is relevant because
*  in that moment, it was the darkest time in my life. I was ending a 13-year marriage,
*  I was leaving my religion, I sold Braintree and I was coming a battling depression where I was just
*  at the end. And I got invited to go to Tanzania, and I was like, I'm going to go to Tanzania.
*  And I got invited to go to Tanzania as part of a group that was raising money to build clean
*  water wells. And I had made some money from Braintree and so I was able to donate $25,000.
*  And it was the first time I had ever had money to donate outside of paying tithing in my religion.
*  And it was such a phenomenal experience to contribute something meaningful to someone
*  else in that form. And as part of this process, we were going to climb the mountain. And so
*  we went there and we saw the clean water wells we were building. We spoke to the
*  people there and it was very energizing. And then we climbed Kilimanjaro and I came down with
*  a stomach flu on day three. And I also had altitude sickness, but I became so sick that on day four,
*  we were summiting on day five, I came into the camp, base camp at 15,000 feet,
*  just going to the bathroom on myself and falling all over. I was just a disaster. I was so sick.
*  So stomach flu and altitude sickness.
*  Yeah. And I just was destroyed from the situation. And-
*  Plus psychologically one of the lowest points you've ever-
*  Yeah. And I think that was probably a big contributor. I was just smoked as a human,
*  just absolutely done. And I had three young children. And so I was trying to reconcile,
*  whether I live or not is not my decision by itself. I'm now intertwined with these three little
*  people and I have an obligation whether I like it or not, I need to be there. And so it did,
*  it felt like I was just stuck in a straight jacket. And I had to decide whether I was going to
*  summit the next day with the team. And it was a difficult decision because once you start hiking,
*  there's no way to get off the mountain. And midnight came and our guide came in and he said,
*  where are you at? And I said, I think I'm okay. I think I can try. And so we went. And so from
*  midnight to- I made it to the summit at 5 a.m. It was one of the most transformational moments
*  of my existence. And the mountain became my problem. It became everything that I was struggling with.
*  And when I started hiking, the pain got so ferocious that it was kind of like this.
*  It became so ferocious that I turned my music to Eminem. And Eminem was the only person in existence
*  that spoke to my soul. And it was something about his anger and his vibrancy and his multibentrality.
*  He's the only person who I could turn on and I could say, ah, I feel some relief. I turned on
*  Eminem and I made it to the summit after five hours. But just a hundred yards from the top,
*  I was with my guide Ike and I started getting very dizzy and I felt like I was going to fall
*  backwards off this cliff area we were on. I was like, this is dangerous. And he said, look, Brian,
*  I know where you're at. I know where you're at. And I can tell you, you've got it in you.
*  So I want you to look up, take a step, take a breath, and look up, take a breath and take a step.
*  And I did. And I made it. And so I got there and I just sat down with him at the top. I just cried
*  like a baby. Broke down. I just lost it. And so he'd let me do my thing. And then we pulled out the
*  pulse oximeter and he measured my blood oxygen levels and it was like 50 something percent. And
*  it was danger zone. So he looked at it and I think he was like really alarmed that I was in
*  this situation. And so he said, we can't get a helicopter here and we can't get you emergency
*  evacuated. You've got to go down. You've got to hike down to 15,000 feet to get base camp.
*  And so we went down the mountain. I got back down to base camp. And again, that was pretty difficult.
*  And then they put me on a stretcher, this metal stretcher with this one wheel and a team of six
*  people wheeled me down the mountain. And it was pretty tortuous. I'm very appreciative they did.
*  Also the trail is very bumpy. So they'd go over these big rocks. And so my head would just slam
*  against this metal thing for hours. And so I just felt awful. Plus I'd get my head slammed every
*  couple of seconds. So the whole experience was really a life changing moment. And that was the
*  demarcation of me basically building your life. Basically I said, I'm going to reconstruct
*  Brian, my understanding of reality, my existential realities, what I want to go after.
*  And I try, I mean, as much as that's possible as a human, but that's when I set out to
*  rebuild everything. Was it the struggle of that? I mean, there's also just like the romantic,
*  poetic, it's a fricking mountain. He's a man in pain, psychological and physical,
*  struggling up a mountain. But it's just struggle, just in the face of,
*  just pushing through in the face of hardship or nature to something much bigger than you.
*  Was that the thing that just clicked? For me, it felt like I was just locked in with reality.
*  And it was a death match. It was in that moment, one of us is going to die.
*  So you were pondering death, like not surviving.
*  Yeah. And that was the moment. And the summit to me was,
*  I'm going to come out on top and I can do this. And giving in was, it's like, I'm just done.
*  And so it did, I locked in. And that's why mountains are magical to me.
*  I didn't expect that. I didn't design that. I didn't know that was going to be the case.
*  It would not have been something I would have anticipated.
*  But you were not the same man afterwards.
*  Is there advice you can give to young people today that look at your story,
*  that's successful in many dimensions? Advice you can give to them about how to be successful
*  in their career, successful in life, whatever path they choose?
*  Mm-hmm. Yes, I would say, listen to advice and see it for what it is, a mirror of that person,
*  and then map and know that your future is going to be in a zero principle land.
*  And so what you're hearing today is a representation of what may have been the
*  right principles to build upon previously, but they're likely depreciating very fast.
*  And so I am a strong proponent that people ask for advice, but they don't take advice.
*  So how do you take advice properly?
*  It's in the careful examination of the advice. It's actually, the person makes a statement about
*  a given thing somebody should follow. The value is not doing that. The value is understanding the
*  assumption stack they built, the assumption and knowledge stack they built around that body of
*  knowledge. That's the value. It's not doing what they say. Considering the advice, but digging
*  deeper to understand the assumption stack, like the full person. I mean, this is deep empathy,
*  essentially, to understand the journey of the person that arrived at the advice. And the advice
*  is just the tip of the iceberg that ultimately is not the thing that gives you... That's right.
*  It could be the right thing to do. It could be the complete wrong thing to do, depending on the
*  assumption stack. So you need to investigate the whole thing. Are there been people in your
*  startup, in your business journey that have served that role of advice giver
*  that's been helpful? Or do you feel like your journey felt like a lonely path, or was it one
*  that was, of course, we're all born and die alone. But
*  do you fundamentally remember the experiences, one where you leaned on people at a particular
*  moment of time that changed everything? Yeah, the most significant moments of my memory,
*  for example, like on Kilimanjaro, when Ike, some person I'd never met in Tanzania,
*  was able to, in that moment, apparently see my soul when I was in this death match with reality.
*  And he gave me the instructions, look up, step. And so
*  there's magical people in my life that have done things like that. And I suspect they probably
*  don't know. I probably should be better at identifying those things. And
*  I suppose the wisdom I would aspire to is to have the awareness and the empathy
*  to be that for other people, and not a retail
*  advertiser of advice, of, you know, like, you know, like,
*  deeply meaningful and empathetic with a one-on-one context with people that
*  it really can make a difference. Yeah, I actually kind of experience, I think about that sometimes,
*  you know, you have like an 18 year old kid come up to you.
*  It's not always obvious. It's not always clear. It's not always clear.
*  I think about that sometimes, you know, you have like an 18 year old kid come up to you.
*  It's not always obvious. It's not always easy to really listen to them. Like, not the facts,
*  but like, see who that person is. I think people say that about being a parent is,
*  you know, you want to consider that you don't want to be the authority figure in a sense,
*  that you really want to consider that there's a special, unique human being there with a unique
*  brain that may be brilliant in ways that you are not understanding that you'll never be.
*  And really try to hear that. So when given advice, there's something to that. So both sides
*  should be deeply empathetic about the assumption stack. I love that terminology. What do you think
*  is the meaning of this whole thing? Of life. Why the hell are we here, Ryan Johnson? We've been
*  talking about brains and studying brains and you had this very eloquent way of describing life on
*  earth as an optimization problem of the cost of intelligence going to zero. At first through the
*  evolutionary process and then eventually through building, through our technology, building more
*  and more intelligent systems. You ever ask yourself why is doing that? Yeah, I think the
*  answer to this question, again, the information value is more in the mirror it provides of that
*  person, which is a representation of the technological, social, political context of the time.
*  So if you asked this question a hundred years ago, you would get a certain answer that reflects that
*  time period. Same thing with a thousand years ago. It's rare. It's difficult for a person to pull
*  themselves out of their contextual awareness and offer a truly original response. And so knowing
*  that I am contextually influenced by the situation, that I am a mirror for our reality, I would say
*  that in this moment, I think the real game going on is that evolution built a system of scaffolding
*  intelligence that produced us. We are now building intelligence systems that are scaffolding
*  higher dimensional intelligence. It's developing more robust systems of intelligence.
*  In doing in that process with the cost going to zero, then the meaning of life becomes
*  goal alignment, which is the negotiation of our conscious and unconscious existence.
*  And then I'd say the third thing is if we're thinking that we want to be explorers,
*  is our technological progress is getting to a point where we could aspirationally say,
*  we want to figure out what is really going on. Really going on. Because does any of this really
*  make sense? Now we may be a hundred, two hundred, five hundred, a thousand years away from being able to
*  poke our way out of whatever is going on. But it's interesting that we could even state an
*  aspiration to say, we want to poke at this question. But I'd say in this moment of time,
*  the meaning of life is that we can build a future state of existence that is more fantastic than
*  anything we could ever imagine. The striving for something more amazing.
*  And that defies expectations that we would consider bewildering and all the things that
*  that's and I guess the last thing, if there's multiple meanings of life,
*  it would be infinite games. James Kars wrote the book, finite games, infinite games.
*  The only game to play right now is to keep playing the game. And so this goes back to the algorithm
*  of the Lex algorithm of diet soda and brisket and pursuing the passion. What I'm suggesting is
*  there's a moment here where we can contemplate playing infinite games. Therefore, it may make
*  sense to err on the side of making sure one is in a situation to be playing infinite games if that
*  opportunity arises. So it's just the landscape of possibilities changing very, very fast. And
*  therefore, our old algorithms of how we might assess risk assessment and what things we might
*  pursue and why those assumptions may fall away very quickly. Well, I think I speak for a lot of
*  people when I say that the game you, Mr. Brian Johnson, have been playing is quite incredible.
*  Thank you so much for talking to me. Thanks, Lex. Thanks for listening to this conversation
*  with Brian Johnson. And thank you to Four Sigmatic, NetSuite, Grammarly and ExpressVPN.
*  Check them out in the description to support this podcast. And now let me leave you with some words
*  from Diane Ackerman. Our brain is a crowded chemistry lab, bustling with nonstop neural
*  conversations. Thank you for listening and hope to see you next time.

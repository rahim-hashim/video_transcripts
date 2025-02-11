---
Date Generated: April 14, 2024
Transcription Model: whisper medium 20231117
Length: 3464s
Video Keywords: []
Video Views: 38152
Video Rating: None
---

# Kevin Scott: Microsoft CTO | Lex Fridman Podcast #30
**Lex Fridman:** [August 01, 2019](https://www.youtube.com/watch?v=QDN6xvhAw94)
*  The following is a conversation with Kevin Scott, the CTO of Microsoft. Before that,
*  he was the Senior Vice President of Engineering and Operations at LinkedIn,
*  and before that, he oversaw mobile ads engineering at Google.
*  He also has a podcast called Behind the Tech with Kevin Scott, which I'm a fan of. This was a fun
*  and wide-ranging conversation that covered many aspects of computing. It happened over a month ago,
*  before the announcement of Microsoft's investment in OpenAI that a few people have asked me about.
*  I'm sure there'll be one or two people in the future that'll talk with me about the impact
*  of that investment. This is the Artificial Intelligence Podcast. If you enjoy it,
*  subscribe on YouTube, give it five stars on iTunes, support it on Patreon, or simply connect with me
*  on Twitter at Lex Friedman, spelled F-R-I-D-M-A-N. I'd like to give a special thank you to Tom
*  and Nalanti Bighousen for their support of the podcast on Patreon. Thanks, Tom and Nalanti. Hope
*  I didn't mess up your last name too bad. Your support means a lot and inspires me to keep this
*  series going. Now, here's my conversation with Kevin Scott. You've described yourself as a kid
*  in a candy store at Microsoft because of all the interesting projects that are going on.
*  Can you try to do the impossible task and give a brief, whirlwind view of all the spaces that
*  Microsoft is working in, both research and product? If you include research, it becomes even
*  more difficult. Broadly speaking, Microsoft's product portfolio includes everything from
*  big cloud business, a big set of SaaS services. We have some of what are among the original
*  productivity software products that everybody uses. We have an operating system business. We
*  have a hardware business where we make everything from computer mice and headphones to high-end
*  personal computers and laptops. We have a fairly broad-ranging research group where we have people
*  doing everything from economics research. There's this really smart young economist,
*  Glenn Weil, who my group works with a lot, who's doing this research on these things called radical
*  markets. He's written an entire technical book about this whole notion of radical markets.
*  The research group spans from that to human-computer interaction to artificial intelligence.
*  We have GitHub, we have LinkedIn, we have a search advertising and news business,
*  and probably a bunch of stuff that I'm embarrassingly not recounting in this list.
*  Gaming to Xbox and so on.
*  Yeah, gaming for sure. I was having a super fun conversation this morning with Phil Spencer. When
*  I was in college, there was this game that Lucas Arts made called Day of the Tentacle that my
*  friends and I played forever. We're doing some interesting collaboration now with the folks who
*  made Day of the Tentacle. I was completely nerding out with Tim Schaefer, the guy who wrote
*  Day of the Tentacle this morning, just a complete fanboy. It happens a lot. Microsoft has been doing
*  so much stuff at such breadth for such a long period of time that being CTO,
*  most of the time my job is very, very serious. Sometimes I get caught up in how
*  amazing it is to be able to have the conversations that I have with the people
*  I get to have them with.
*  You have to reach back into the sentimental. What's the radical markets and the economics?
*  The idea with radical markets is can you come up with new market-based mechanisms to...
*  I think we're having this debate right now. Does capitalism work? Do free markets work?
*  Can the incentive structures that are built into these systems produce outcomes that are
*  creating equitably distributed benefits for every member of society?
*  I think it's a reasonable set of questions to be asking. One mode of thought there,
*  if you have doubts that the markets are actually working, you can tip towards,
*  okay, let's become more socialist and have central planning and governments or some other
*  central organization is making a bunch of decisions about how work gets done and
*  where the investments and where the outputs of those investments get distributed.
*  Glenn's notion is lean more into the market-based mechanism. For instance,
*  this is one of the more radical ideas. Suppose that you had a radical pricing mechanism for
*  assets like real estate where you could be bid out of your position in your home, for instance.
*  If somebody came along and said, I can find higher economic utility for this piece of real estate
*  that you're running your business in, then you either have to bid to stay or the thing that's
*  got the higher economic utility takes over the asset, which would make it very difficult to
*  have the same rent-seeking behaviors that you've got right now. Because if you did speculative
*  bidding, you very quickly lose a whole lot of money. The prices of the assets would be
*  very closely indexed to the value that they can produce. Because you'd have this real-time
*  mechanism that would force you to mark the value of the asset to the market, then it could be taxed
*  appropriately. You couldn't sit on this thing and say, oh, this house is only worth 10,000 bucks
*  when everything around it is worth 10 million. It's an incentive structure where the prices match
*  the value much better. Glenn does a much better job than I do at selling it. I probably picked the
*  world's worst example, and it's intentionally provocative. I'm not sure whether I like this
*  notion that we could have a set of market mechanisms where I could get bid out of my property.
*  If you're thinking about something like Elizabeth Warren's wealth tax, for instance,
*  it'd be really interesting in how you would actually set the price on the assets. You might
*  have to have a mechanism like that if you put a tax like that in place. It's really interesting
*  that that kind of research, at least tangentially, is touching Microsoft research. You're really
*  thinking broadly. Maybe you can speak to ... This connects to AI. We have a candidate, Andrew Yang,
*  who talks about artificial intelligence and the concern that people have about
*  automation's impact on society. Arguably, Microsoft is at the cutting edge of innovation in all these
*  kinds of ways, and so it's pushing AI forward. Combining all our conversations together here
*  with radical markets and socialism and innovation in AI that Microsoft is doing, and then Andrew
*  Yang's worry that that will result in job loss for the lower and so on. How do you think about that?
*  I think it's one of the most important questions in technology, maybe even in society right now,
*  about how is AI going to develop over the course of the next several decades, and what's it going
*  to be used for, and what benefits will it produce, and what negative impacts will it produce, and
*  who gets to steer this whole thing? I'll say at the highest level,
*  one of the real joys of getting to do what I do at Microsoft is Microsoft has this
*  heritage as a platform company. Bill has this thing that he said a bunch of years ago where
*  the measure of a successful platform is that it produces far more economic value for the people
*  who build on top of the platform than is created for the platform owner or builder. I think we have
*  to think about AI that way. As a platform? Yeah, it has to be a platform that other people can use to
*  build businesses, to fulfill their creative objectives, to be entrepreneurs, to solve
*  problems that they have in their work and in their lives. It can't be a thing where
*  there are a handful of companies sitting in a very small handful of cities geographically who are
*  making all the decisions about what goes into the AI, and then on top of all this infrastructure,
*  then build all of the commercially valuable uses for it. I think that's bad from economics and
*  equitable distribution of value perspective, back to this whole notion of, do the markets work?
*  But I think it's also bad from an innovation perspective because I have infinite amounts of
*  faith in human beings that if you give folks powerful tools, they will go do interesting
*  things. It's more than just a few tens of thousands of people with the interesting tools. It should be
*  millions of people with the tools. It's sort of like you think about the steam engine in the
*  late 18th century. It was maybe the first large-scale substitute for human labor that
*  we've built like a machine. In the beginning, when these things are getting deployed, the folks who
*  got most of the value from the steam engines were the folks who had capital so they could afford
*  to build them. They built factories around them and businesses and the experts who knew how to
*  build and maintain them. But access to that technology democratized over time. Now,
*  an engine is not a differentiated thing. There isn't one engine company that builds all the
*  engines and all of the things that use engines are made by this company. They get all the economics
*  from all of that. Fully democratized, like they're probably, we're sitting here in this room,
*  even though they're probably things like the memes gyroscope that are in both of our phones.
*  They're like little engines sort of everywhere. They're just a component in how we build the
*  modern world. AI needs to get there. Yeah. That's a really powerful way to think.
*  If we think of AI as a platform versus a tool that Microsoft owns as a platform that enables creation
*  on top of it, that's the way to democratize it. That's really interesting actually.
*  Microsoft throughout its history has been positioned well to do that.
*  The tie back to this radical markets thing, so my team has been working with Glenn
*  on this and Jaren Lanier actually. Jaren is the father of virtual reality. He's
*  one of the most interesting human beings on the planet. He's a sweet, sweet guy.
*  Jaren and Glenn and folks in my team have been working on this notion of data as labor or
*  they call it data dignity as well. The idea is that if you, again, going back to this
*  industrial analogy, if you think about data as the raw material that is consumed by the machine of
*  AI in order to do useful things, then we're not doing a really great job right now in having
*  transparent marketplaces for valuing those data contributions. We all make them explicitly.
*  You go to LinkedIn, you set up your profile on LinkedIn. That's an explicit contribution.
*  You know exactly the information that you're putting into the system and you put it there
*  because you have some nominal notion of what value you're going to get in return. But it's
*  only nominal. You don't know exactly what value you're getting in return. Services free,
*  it's low amount of perceived debt. Then you've got all this indirect contribution that you're
*  making just by virtue of interacting with all of the technology that's in your daily life.
*  What Glenn and Jaren and this data dignity team are trying to do is can we figure out a
*  set of mechanisms that let us value those data contributions so that you could create an economy
*  and a set of controls and incentives that would allow people to maybe even in the limit
*  earn part of their living through the data that they're creating. You can see it in explicit ways
*  there are these companies like Scale AI and there are a whole bunch of them in China right now that
*  are basically data labeling companies. You're doing supervised machine learning, you need lots
*  and lots of label training data. Those people who work for those companies are getting compensated
*  for their data contributions into the system. That's easier to put a number on their
*  contribution because they're explicitly labeling data. Correct. But you're saying that we're all
*  contributing data in different kinds of ways and it's fascinating to start to explicitly try to
*  put a number on it. Do you think that's possible? I don't know, it's hard. It really is because
*  we don't have as much transparency as I think we need in how the data is getting used and it's
*  super complicated. I think as technologists appreciate some of the subtlety there. The data
*  gets created and then it gets, it's not valuable. The data exhaust that you give off or the data
*  the explicit data that I am putting into the system isn't super valuable atomically.
*  It's only valuable when you aggregate it together into large numbers. It's true even for these
*  folks who are getting compensated for labeling things. For supervised machine learning now,
*  you need lots of labels to train a model that performs well. I think that's one of the
*  challenges. It's like how do you figure out because this data is getting combined in so many ways
*  through these combinations how the value is flowing. Yeah, that's fascinating.
*  Yeah, it's fascinating that you're thinking about this and I wasn't even going to this
*  conversation expecting the breadth of research really that Microsoft broadly is thinking about.
*  You were thinking about it, Microsoft. So if we go back to 89 when Microsoft released Office or
*  1990 when they released Windows 3.0. How's the, in your view, I know you weren't there the entire,
*  you know, through its history, but how has the company changed in the 30 years since as you look
*  at it now? The good thing is it's started off as a platform company. Like it's still a platform
*  company. Like the parts of the business that are like thriving and most successful are those that
*  are building platforms. Like the mission of the company now is, the mission's changed. It's like
*  changed in a very interesting way. So, you know, back in 89, 90, like they were still on the
*  original mission, which was like put a PC on every desk and in every home. Like, and it was basically
*  about democratizing access to this new personal computing technology, which when Bill started the
*  company, integrated circuit microprocessors were a brand new thing. And like people were building,
*  you know, homebrew computers, you know, from kits, like the way people build ham radios right now.
*  And I think this is sort of the interesting thing for folks who build platforms in general.
*  Bill saw the opportunity there and what personal computers could do. And it was like,
*  it was sort of a reach. Like you just sort of imagine like where things were,
*  you know, when they started the company versus where things are now. Like in success, when you've
*  democratized a platform, it just sort of vanishes into the platform. You don't pay attention to it
*  anymore. Like operating systems aren't a thing anymore. Like they're super important, like
*  completely critical. And like, you know, when you see one, you know, fail, like you just,
*  you sort of understand, but like, you know, it's not a thing where you're not like waiting for,
*  you know, the next operating system thing in the same way that you were in 1995, right? Like in
*  1995, like, you know, we had Rolling Stones on the stage with the Windows 95 rollout. Like it was like
*  the biggest thing in the world. Everybody was like lined up for it the way that people used to line
*  up for iPhone. But like, you know, eventually, and like this isn't necessarily a bad thing.
*  Like it just sort of, you know, the success is that it's sort of, it becomes ubiquitous. It's
*  like everywhere, like human beings, when their technology becomes ubiquitous, they just sort of
*  start taking it for granted. So the mission now that Satya re-articulated five plus years ago now,
*  when he took over as CEO of the company, our mission is to empower every individual and every
*  organization in the world to be more successful. And so, you know, again, like that's a platform
*  mission. And like the way that we do it now is, is different. It's like we have a hyperscale cloud
*  that cloud or building our applications on top of like, we have a bunch of AI infrastructure that
*  people are building their AI applications on top of. We have, you know, we have a
*  productivity suite of software, like Microsoft Dynamics, which, you know, some people might not
*  think is the sexiest thing in the world, but it's like helping people figure out how to automate all
*  of their business processes and workflows and to, you know, like help those businesses using it to
*  grow and be more successful. So it's a much broader vision in a way now than it was back then. Like
*  it was sort of a very particular thing. And like now, like we live in this world where technology
*  is so powerful and it's like such a basic fact of life that it, you know, that it both exists and
*  is going to get better and better over time, or at least more and more powerful over time.
*  So like, you know, what you have to do as a platform player is just much bigger.
*  Right. There's so many directions in which you can transform. You didn't mention mixed reality,
*  too. You know, that's probably early days or it depends how you think of it. But if we think
*  on a scale of centuries, it's the early days of mixed reality. Oh, for sure. And so with
*  HoloLens, Microsoft is doing some really interesting work there. Do you touch that part of the effort?
*  What's the thinking? Do you think of mixed reality as a platform, too?
*  Oh, sure. When we look at what the platforms of the future could be,
*  it's like fairly obvious that like AI is one. Like you don't have to, I mean, like that's,
*  you know, you sort of say it to like someone and, you know, like they get it. But like we also think
*  of the like mixed reality and quantum is like these two interesting, you know, potentially
*  quantum computing. Yeah. OK, so let's get crazy then. So you're talking about some
*  futuristic things here. Well, the mixed reality, Microsoft is really not even futuristic is here.
*  It is incredible stuff. And look, and it's having it's having an impact right now. Like one of the
*  one of the more interesting things that's happened with mixed reality over the past
*  couple of years that I didn't clearly see is that it's become the computing device for
*  for folks who for doing their work, who haven't used any computing device at all to do their
*  work before. So technicians and service folks and people who are doing like machine maintenance on
*  factory floors. So like they, you know, because they're mobile and like they're out in the world
*  and they're working with their hands and, you know, sort of servicing these like very complicated
*  things. They're they don't use their mobile phone and like they don't carry a laptop with them. And
*  you know, they're not tethered to a desk. And so mixed reality, like where it's getting traction
*  right now, where HoloLens is selling a lot of a lot of units is for these sorts of applications
*  for these workers. And it's become like, I mean, like the people love it. They're like, oh my god,
*  like this is like for them, like the same sort of productivity boost that, you know, like an office
*  worker had when they got their first personal computer. Yeah, but you did mention it's certainly
*  obvious AI as a platform. But can we dig into it a little bit? How does AI begin to infuse some of
*  the products in Microsoft? So currently providing training of, for example, neural networks in the
*  cloud or providing pre-trained models or just even providing computing resources, whatever different
*  inference that you want to do using neural networks. How do you think of AI infusing
*  as a platform that Microsoft can provide? Yeah, I mean, I think it's super interesting. It's like
*  everywhere. And like we run these, we run these review meetings now where it's me and Satya and
*  members of Satya's leadership team and like a cross-functional group of folks across the
*  entire company who are working on like either AI infrastructure or like have some substantial part
*  of their product work using AI in some significant way. Now, the important thing to understand is
*  like when you think about like how the AI is going to manifest and like an experience for something
*  that's going to make it better, like I think you don't want the AI-ness to be the first order thing.
*  It's like whatever the product is and like the thing that it's trying to help you do,
*  like the AI just sort of makes it better. And this is a gross exaggeration, but like I,
*  people get super excited about like where the AI is showing up in products and I'm like,
*  do you get that excited about like where you're using a hash table like in your code?
*  Like it's just another- It's just a tool.
*  It's a very interesting programming tool, but it's sort of like it's an engineering tool.
*  And so like it shows up everywhere. So like we've got dozens and dozens of features now
*  in Office that are powered by like fairly sophisticated machine learning. Our search engine
*  wouldn't work at all if you took the machine learning out of it. The like increasingly,
*  you know, things like content moderation on our Xbox and Xcloud platform.
*  When you mean moderation, do you mean like the recommender is like showing what you want to
*  look at next? No, no, no. It's like anti-bullying stuff.
*  So the usual social network stuff that you have to deal with.
*  Yeah, correct. But it's like really it's targeted towards a gaming audience. So it's like a very
*  particular type of thing where, you know, the lime between playful banter and like legitimate
*  bullying is like a subtle one. And like you have to, it's sort of tough. Like I have-
*  I'd love to if we could dig into it, because you're also you led the engineering efforts
*  of LinkedIn. And if we look at if we look at LinkedIn as a social network, and if we look
*  at the Xbox gaming as the social components, the very different kinds of I imagine communication
*  going on on the two platforms. And the line in terms of bullying and so on is different on the
*  platforms. So how do you I mean, it's such a fascinating philosophical discussion of where
*  that line is. I don't think anyone knows the right answer. Twitter folks are under fire now,
*  Jack, Twitter for trying to find that line. Nobody knows what that line is. But how do you try to
*  find the line for, you know, trying to prevent abusive behavior and at the same time, let people
*  be playful and joke around and that kind of thing? I think in a certain way, like, you know, if you
*  have what I would call vertical social networks, it gets to be a little bit easier. So like, if you
*  have a clear notion of like what your social network should be used for, or like what you are
*  designing a community around, then you don't have as many dimensions to your sort of content safety
*  problem as you do in a general purpose platform. I mean, so like on LinkedIn,
*  like the whole social network is about connecting people with opportunity, whether it's helping
*  them find a job or to, you know, sort of find mentors or to, you know, sort of help them
*  like find their next sales lead or to just sort of allow them to broadcast their, you know,
*  professional identity to their network of peers and collaborators and, you know, sort of professional
*  community. Like that is, I mean, like in some ways, like that's very, very broad, but in other ways,
*  it's sort of, you know, it's narrow. And so like you can build AIs, like machine learning systems
*  that are, you know, capable with those boundaries of making better automated decisions about like
*  what is, you know, sort of inappropriate and offensive comments or dangerous comments or
*  illegal content when you have some constraints. You know, same thing with, same thing with like
*  the gaming social networks. So for instance, like it's about playing games, about having fun,
*  and like the thing that you don't want to have happen on the platform is why bullying is such
*  an important thing. Like bullying is not fun. So you want to do everything in your power to
*  encourage that not to happen. And yeah, but I think it's a, it's sort of a tough problem in general.
*  It's one where I think, you know, eventually we're going to have to have
*  some sort of clarification from our policymakers about what it is that we should be doing, like
*  where the lines are, because it's tough. Like you don't, like in democracy, right? Like you don't
*  want, you want some sort of democratic involvement, like people should have a say in like where the
*  lines are drawn. Like you don't want a bunch of people making like unilateral decisions. And like
*  we are in a, we're in a state right now for some of these platforms where you actually do have to
*  make unilateral decisions where the policymaking isn't going to happen fast enough in order to
*  like prevent very bad things from happening. But like we need the policymaking side of that to
*  catch up, I think is as quickly as possible because you want that whole process to be a democratic
*  thing, not a, you know, not, not some sort of weird thing where you've got a non-representative
*  group of people making decisions that have, you know, like national and global impact.
*  And it's fascinating because the digital space is different than the physical space in which nations
*  and governments were established. And so what policy looks like globally, what bullying looks
*  like globally, what healthy communication looks like globally is an open question. And we're all
*  figuring it out, figuring it out together. Which is fascinating.
*  Yeah. I mean with, with, you know, sort of fake news for instance, and...
*  Deep fakes and fake news generated by humans.
*  Yeah. So, and we can talk about deep fakes. Like I think that is another like, you know,
*  sort of very interesting level of complexity, but like if you think about just the written word,
*  right? Like we have, you know, we invented papyrus, what, 3000 years ago where we, you know,
*  you could sort of put, put word on, on paper. And then 500 years ago, like we, we get the printing
*  press, like where the word gets a little bit more ubiquitous. And then like you really,
*  really didn't get ubiquitous printed word until the end of the 19th century when the offset press
*  was invented. And then, you know, just sort of explodes and like, you know, the cross product of
*  that and the industrial revolution's need for educated citizens resulted in like this rapid
*  expansion of literacy and the rapid expansion of the word. But like we had 3000 years up to that
*  point to figure out like how to, you know, like what's, what's journalism, what's editorial
*  integrity, like what's, you know, what's scientific peer review. And so like you built all of this
*  mechanism to like try to filter through all of the noise that the technology made possible to like,
*  you know, sort of getting to something that society could cope with. And like, if you think about
*  just the piece, the PC didn't exist 50 years ago. And so in like this span of, you know,
*  like half a century, like we've gone from no digital, you know, no ubiquitous digital technology
*  to like having a device that sits in your pocket where you can sort of say whatever is on your mind
*  to like what would Mary Haven or Mary Meeker just released her new like slide deck last week. You
*  know, we've got 50% penetration of the internet to the global population. Like there are like
*  three and a half billion people who are connected now. So it's like, it's crazy, crazy, like
*  inconceivable, like how fast all of this happens. So, you know, it's not surprising that we haven't
*  figured out what to do yet. But like we gotta like, we gotta really like lean into this set
*  of problems because like we basically have three millennia worth of work to do about how to deal
*  with all of this and like probably what amounts to the next decade worth of time. So since we're on
*  the topic of tough, you know, tough, challenging problems, let's look at more on the tooling side
*  in AI that Microsoft is looking at is face recognition software. So there's a lot of
*  powerful positive use cases for face recognition, but there's some negative ones and we're seeing
*  those in different governments in the world. So how do you, how does Microsoft think about the use
*  of face recognition software as a platform in governments and companies?
*  How do we strike an ethical balance here? Yeah, I think we've articulated a clear
*  point of view. So Brad Smith wrote a blog post last fall, I believe that sort of like outlined
*  very specifically what our point of view is there. And you know, I think we believe that there are
*  certain uses to which face recognition should not be put. And we believe again, that there's a need
*  for regulation there. Like the government should like really come in and say that, you know, this
*  is where the lines are. And like we very much wanted to like figuring out where the lines are
*  should be a democratic process. But in the short term, like we've drawn some lines where,
*  you know, we push back against uses of face recognition technology. You know, like the
*  city of San Francisco, for instance, I think has completely outlawed any government agency
*  from using face recognition tech. And like that may prove to be a little bit overly broad.
*  But for like certain law enforcement things, like you really, I would personally rather be overly
*  sort of cautious in terms of restricting use of it until like we have, you know, sort of defined
*  a reasonable, you know, democratically determined regulatory framework for like where we could and
*  should use it. And you know, the other thing there is like we've got a bunch of research that we're
*  doing and a bunch of progress that we've made on bias there. And like there are all sorts of like
*  weird biases that these models can have, like all the way from like the most noteworthy one where,
*  you know, you may have underrepresented minorities who are like underrepresented in the training data
*  and then you start learning like strange things. But like they're even, you know, other weird
*  things like we've, I think we've seen in the public research, like models can learn strange things,
*  like all doctors are men, for instance. Yeah, I mean, so like, it really is a thing where
*  it's very important for everybody who is working on these things before they push publish,
*  they launch the experiment, they, you know, push the code to, you know, online,
*  or they even publish the paper that they are at least starting to think about what some of the
*  potential negative consequences are some of this stuff. I mean, this is where, you know,
*  like the deep fake stuff, I find very worrisome, just because
*  they're going to be some very good beneficial uses of like GAN generated imagery.
*  And funny enough, like one of the places where it's actually useful is we're using the technology
*  right now to generate synthetic visual data for training some of the face recognition models to
*  get rid of the bias. So like, that's one like super good use of the tech, but like,
*  you know, it's getting good enough now where, you know, it's going to sort of challenge
*  normal human beings ability to like, now you're just sort of say, like, it's very expensive for
*  someone to fabricate a photorealistic fake video. And like GANs are going to make it fantastically
*  cheap to fabricate a photorealistic fake video. And so like what you assume you can sort of trust
*  is true versus like be skeptical about is about to change. And like, we're not ready for it. I don't
*  think the nature of truth, right. That's, it's also exciting because I think both you and I probably
*  would agree that the way to solve, to take on that challenges with technology. Yeah. Right.
*  There's probably going to be ideas of ways to verify which, which kind of video is legitimate,
*  which kind is not. So to me, that's an exciting possibility. Most, most likely for just the
*  comedic genius that the internet usually creates with these kinds of videos and hopefully will not
*  result in any serious harm. Yeah. And it could be, you know, like I think we will have technology to
*  that may be able to detect whether or not something's fake or real, although
*  the fakes are pretty convincing even like when you subject them to machine scrutiny.
*  But you know, we also have these increasingly interesting social networks, you know, that are
*  under fire right now for some of the bad things that they do. Like, you know, like the internet
*  for some of the bad things that they do. Like one of the things you could choose to do with
*  a social network is like you could, you could use crypto and the networks to like have content
*  signed where you could have a like full chain of custody that accompanied every piece of content.
*  So like when you're viewing something and like you want to ask yourself like how, you know,
*  how much can I trust this? Like you can click something and like have a verified chain of
*  custody that shows like, oh, this is coming from, you know, from this source and it's like signed by
*  like someone whose identity I trust. Yeah. Yeah. I think having the, you know, having that chain
*  of custody, like being able to like say, oh, here's this video, like it may or may not have
*  been produced using some of this deep fake technology. But if you've got a verified chain
*  of custody where you can sort of trace it all the way back to an identity and you can decide whether
*  or not like I trust this identity, like, oh no, this is really from the White House or like this
*  is really from the, you know, the office of this particular presidential candidate or it's really
*  from, you know, Jeff Weiner, CEO of LinkedIn or Satya Nadella, CEO of Microsoft. Like that might,
*  that might be like one way that you can solve some of the problems. So like that's not the
*  super high tech. Like we've had all of this technology forever. Right. And I, but I think
*  you're right. Like it has to, it has to be some sort of technological thing because
*  the underlying tech that is used to create this is not going to do anything, but get better over
*  time. And the genie is sort of out of the bottle. There's no stuffing it back in. And there's a
*  social component, which I think is really healthy for a democracy where people will be skeptical
*  about the thing they watch in general. So, you know, which is good skepticism in general is good.
*  Content. So deep fakes in that sense are creating a global skepticism about can they trust what they
*  read? It encourages further research. I come from the Soviet Union, where basically nobody trusted
*  the media because you knew it was propaganda. And that encouraged that kind of skepticism,
*  encouraged further research about ideas. Yeah. It's supposed to just trusting any one source.
*  Look, I think it's one of the reasons why the, you know, the scientific method and our apparatus
*  of modern science is so good. Like, because you don't have to trust anything. Like you,
*  like the whole notion of, you know, like modern science beyond the fact that, you know, this is
*  a hypothesis and this is an experiment to test the hypothesis. And, you know, like this is a
*  peer review process for scrutinizing published results, but like stuff's also supposed to be
*  reproducible. So like, you know, it's been vetted by this process, but like you also are expected
*  to publish enough detail where, you know, if you are sufficiently skeptical of the thing, you can
*  go try to like reproduce it yourself. And like, I don't know what it is. Like, I think a lot of
*  engineers are like this, where like, you know, sort of this, like your brain is sort of wired for,
*  for skepticism. Like you don't just first order trust everything that you see and encounter. And
*  like, you're sort of curious to understand, you know, the next thing. But like, I think it's an
*  entirely healthy, healthy thing. And like, we need a little bit more of that right now.
*  So I'm not a large business owner. So I'm just, I'm just a huge fan of many of Microsoft products.
*  I mean, I still actually in terms of, I generate a lot of graphics and images and I still use
*  PowerPoint to do that. It beats Illustrator for me, even professional sort of, it's fascinating.
*  So I wonder what is the future of, let's say windows and office look like is, do you see it?
*  I mean, I remember looking forward to XP was an exciting when XP was released. Just like you said,
*  I don't remember when 95 was released, but XP for me was a big celebration. And when 10 came out,
*  I was like, okay, well, it's nice. It's a nice improvement. But so what do you see the future of
*  these products? I think there's a bunch of exciting, I mean, on the office front, there's going to be
*  this like increasing productivity wins that are coming out of some of these AI powered features
*  that are coming. Like the products are sort of get smarter and smarter and like a very subtle way.
*  Like there's not going to be this big bang moment where, you know, like Clippy is going to reemerge
*  and it's going to be- Wait a minute. Okay. Well I have to wait, wait, wait. Is Clippy coming back?
*  But quite seriously, so injection of AI, there's not much, or at least I'm not familiar, sort of
*  assistive type of stuff going on inside the office products, like a Clippy style assistant,
*  personal assistant. Do you think that there's a possibility of that in the future?
*  So I think there are a bunch of like very small ways in which like machine learning
*  powered assistive things are in the product right now. So there are a bunch of interesting things,
*  like the auto response stuff's getting better and better. And it's like getting to the point where,
*  it can auto respond with like, okay, this person's clearly trying to schedule a meeting. So it looks
*  at your calendar and it automatically tries to find a time and a space that's mutually interesting.
*  Like we have this notion of Microsoft search where it's like not just web search, but it's like
*  search across like all of your information that's sitting inside of like your Office 365 tenant and
*  like, you know, potentially in other products. And like we have this thing called the Microsoft
*  Graph that is basically an API federator that, you know, sort of like gets you hooked up across
*  the entire breadth of like all of the, you know, like what were information silos before they got
*  woven together with the graph. Like that is like getting increasing, with increasing effectiveness
*  sort of plumbed into the, into some of these auto response things where you're going to be able to
*  see the system like automatically retrieve information for you. Like if, you know, like I
*  frequently send out, you know, emails to folks where like I can't find a paper or document or
*  whatnot. There's no reason why the system won't be able to do that for you. And like, I think the,
*  it's building towards like having things that look more like a fully integrated, you know, assistant.
*  But like you'll have a bunch of steps that you will see before you, like it will not be this like
*  big bang thing where like Clippy comes back and you've got this like, you know, manifestation of,
*  you know, like a fully, fully powered assistant. So I think that's definitely coming out. Like all of
*  the, you know, collaboration, co-authoring stuff's getting better. You know, it's like really
*  interesting. Like if you look at how we use the office product portfolio at Microsoft, like more
*  and more of it is happening inside of like Teams as a canvas. And like it's this thing where, you
*  know, you've got collaboration is like at the center of the product. And like we built some
*  like really cool stuff. That's some of which is about to be open source that are sort of
*  framework level things for doing for doing co-authoring.
*  That's awesome. So in, is there a cloud component to that? So on the web or is it,
*  and forgive me if I don't already know this, but with office 365, we still, the collaboration we
*  do for doing word, we're still send the file around. So this is,
*  it, we're already a little bit better than that. And like, you know, so like the fact that you're
*  unaware of it means we've got a better job to do for like helping you discover, discover this stuff.
*  But yeah, I mean, it's already like got a huge, huge cloud component. And like part of, you know,
*  part of this framework stuff, I think we're calling it like, I, like we've been working on it for a
*  couple of years. So like, I know the, the internal code name for it, but I think when we launched it
*  a bill, it's called the fluid framework. And, but like what fluid lets you do is like, you can go
*  into a conversation that you're having in teams and like reference, like part of a spreadsheet that
*  you're working on, where somebody's like sitting in the Excel canvas, like working on the spreadsheet
*  with a chart or whatnot. And like, you can sort of embed like part of the spreadsheet in the
*  teams conversation where like you can dynamically update it and like all of the changes that you're
*  making to the, to this object are like, you know, coordinate and everything is sort of updating in,
*  in real time. So like you can be in whatever canvas is most convenient for you to get your work done.
*  So I, out of my own sort of curiosity as engineer, I know what it's like to sort of lead a team of 10,
*  15 engineers. Microsoft has, I don't know what the numbers are, maybe 50, maybe 60,000 engineers,
*  maybe 40. I don't know exactly what the number is. It's a lot. It's tens of thousands. Right. This
*  is more than 10 or 15. What, what, I mean, you've, you've led different sizes, mostly large size of
*  engineers. What does it take to lead such a large group into a continue innovation, continue
*  being highly productive and yet develop all kinds of new ideas and yet maintain like, what does it
*  take to lead such a large group of brilliant people? I think the thing that you learn as you manage
*  larger and larger scale is that there are three things that are like very, very important for
*  big engineering teams. Like one is like having some sort of forethought about what it is that
*  you're going to be building over large periods of time. Like not exactly. Like you don't need to know
*  that like, you know, I'm putting all my chips on this one product and like, this is going to be the
*  thing, but like it's useful to know like what sort of capabilities you think you're going to need to
*  have to build the products of the future. And then like invest in that infrastructure, like whether
*  and I like, I'm not just talking about storage systems or cloud APIs. It's also like, what does
*  your development process look like? What tools do you want? Like what culture do you want to
*  build around? Like how you're, you know, sort of collaborating together to like make complicated
*  technical things. And so like having an opinion and investing in that is like, it just gets more and
*  more important. And like the sooner you can get a concrete set of opinions, like the better you're
*  going to be. Like you can wing it for a while, small scales, like, you know, when you start a
*  company, like you don't have to be like super specific about it. But like the biggest miseries
*  that I've ever seen as an engineering leader are in places where you didn't have a clear enough
*  opinion about those things soon enough. And then you just sort of go create a bunch of
*  technical debt and like culture debt that is excruciatingly painful to, to clean up. So like
*  that's one bundle of things. Like the other, the other, you know, another bundle of things is
*  like, it's just really, really important to
*  like have a clear mission. That's not just some cute crap you say because like you think you
*  should have a mission, but like something that clarifies for people, like where it is that you're
*  headed together. Like I know it's like probably like a little bit too popular right now, but
*  Yuval Harari's book Sapiens, one of the central ideas in his book is that like storytelling
*  is like the quintessential thing for coordinating the activities of large groups of people. Like
*  once you get past Dunbar's number and like I've really, really seen that just managing
*  engineering teams, like you, you can, you can just brute force things when you're less than 120,
*  150 folks where you can sort of know and trust and understand what the dynamics are between all the
*  people. But like past that, like things just sort of start to catastrophically fail if you don't have
*  some sort of set of shared goals that you're marching towards. And so like, even though it
*  sounds touchy feely and you know, like a bunch of technical people will sort of balk at the idea
*  that like you need to like have a clear, like the missions, like very, very, very important.
*  Yuval's right, right? Stories, that's how our society, that's the fabric that connects us,
*  all of us is these powerful stories. And that works for companies too, right?
*  It works for everything. Like, I mean, even down to like, you know, you sort of really think about
*  like our currency, for instance, is a story. Our constitution is a story. Our laws are, I mean,
*  like we believe very, very, very strongly in them and thank God we do. But like they are,
*  they're just abstract things. Like they're just words. Like if we don't believe in them, they're
*  nothing. And in some sense, those stories are platforms and the kinds, some of which Microsoft
*  is creating, right? They have platforms on which we define the future. So last question, what do you,
*  let's get philosophical maybe, bigger than even Microsoft, what do you think the next 20, 30 plus
*  years looks like for computing, for technology, for devices? Do you have crazy ideas about the
*  future of the world? Yeah, look, I think we, you know, we're entering this time where we've got,
*  we have technology that is progressing at the fastest rate that it ever has. And you've got,
*  you get some really big social problems, like society scale problems that we have to,
*  we have to tackle. And so, you know, I think we're going to rise to the challenge and like figure out
*  how to intersect like all of the power of this technology with all of the big challenges that are
*  facing us, whether it's, you know, global warming, whether it's like the biggest remainder of the
*  population boom is in Africa for the next 50 years or so. And like global warming is going to make
*  it increasingly difficult to feed the global population in particular, like in this place
*  where you're going to have like the biggest population boom. I think we, you know, like AI is
*  going to, like if we push it in the right direction, like it can do like incredible things to
*  empower all of us to achieve our full potential and to, you know, like live better lives. But like
*  that also means focus on like some super important things, like how can you apply it to health care to
*  make sure that, you know, like our quality and cost of and sort of ubiquity of health coverage is
*  better and better over time. Like that's more and more important every day is like in the
*  United States and like the rest of the industrialized world. So Western Europe,
*  China, Japan, Korea, like you've got this population bubble of like aging, working,
*  you know, working age folks who are, you know, at some point over the next 20, 30 years, they're
*  going to be largely retired and like you're going to have more retired people than working age people.
*  And then like you've got, you know, sort of natural questions about who's going to take care of all
*  the old folks and who's going to do all the work. And the answers to like all of these sorts of
*  questions, like where you're sort of running into, you know, like constraints of the, you know, the
*  world and of society has always been like, what tech is going to like help us get around this?
*  You know, like when I was a kid in the 70s and 80s, like we talked all the time about like,
*  oh, like population boom, population boom, like we're going to, like we're not going to be able
*  to like feed the planet. And like we were like right in the middle of the green revolution where
*  like this massive technology driven increase in crop productivity like worldwide. And like some
*  of that was like taking some of the things that we knew in the West and like getting them distributed
*  to the, you know, to the developing world. And like part of it were things like, you know, just
*  smarter biology, like helping us increase. And like we don't talk about like, you know,
*  overpopulation anymore because like we can more or less, we sort of figured out how to feed the
*  world. Like that's a technology story. And so like I'm super, super hopeful about the future
*  and in the ways where we will be able to apply technology to solve some of these super challenging
*  problems. Like I've, like one of the things that I'm trying to spend my time doing right now is
*  trying to get everybody else to be hopeful as well, because, you know, back to Harare, like we
*  are the stories that we tell. Like if we, you know, if we get overly pessimistic right now about
*  like the potential future of technology, like we, you know, like we may fail to get all the things
*  in place that we need to like have our best possible future. And that kind of hopeful optimism.
*  I'm glad that you have it because you're leading large groups of engineers that are actually
*  defining, that are writing that story, that are helping build that future, which is super exciting.
*  And I agree with everything you said, except I do hope Clippy comes back.
*  We miss him. I speak for the people. So, Kellen, thank you so much for talking today.
*  Thank you so much for having me. It was a pleasure.
*  Thank you.

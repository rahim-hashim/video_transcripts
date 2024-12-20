---
Date Generated: October 31, 2024
Transcription Model: whisper medium 20231117
Length: 3074s
Video Keywords: ['jack dorsey', 'twitter', 'square', 'artificial intelligence', 'agi', 'ai', 'ai podcast', 'artificial intelligence podcast', 'lex fridman', 'lex podcast', 'lex mit', 'lex ai', 'lex jre', 'mit ai']
Video Views: 749126
Video Rating: None
Video Description: Jack Dorsey is the co-founder and CEO of Twitter and the founder and CEO of Square.

Support this podcast by signing up with these sponsors:
- MasterClass: https://masterclass.com/lex

EPISODE LINKS:
Jack's Twitter: https://twitter.com/jack
Start Small Tracker: https://bit.ly/2KxdiBL

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
2:48 - Engineering at scale
8:36 - Increasing access to the economy
13:09 - Machine learning at Square
15:18 - Future of the digital economy
17:17 - Cryptocurrency
25:31 - Artificial intelligence
27:49 - Her
29:12 - Exchange with Elon Musk about bots
32:05 - Concerns about artificial intelligence
35:40 - Andrew Yang
40:57 - Eating one meal a day
45:49 - Mortality
47:50 - Meaning of life
48:59 - Simulation

CONNECT:
- Subscribe to this YouTube channel
- Twitter: https://twitter.com/lexfridman
- LinkedIn: https://www.linkedin.com/in/lexfridman
- Facebook: https://www.facebook.com/LexFridmanPage
- Instagram: https://www.instagram.com/lexfridman
- Medium: https://medium.com/@lexfridman
- Support on Patreon: https://www.patreon.com/lexfridman
---

# Jack Dorsey Square, Cryptocurrency, and Artificial Intelligence  Lex Fridman Podcast #91
**Lex Fridman:** [April 24, 2020](https://www.youtube.com/watch?v=60KJz1BVTyU)
*  The following is a conversation with Jack Dorsey, co-founder and CEO of Twitter, and
*  founder and CEO of Square. Given the happenings at the time related to Twitter leadership and
*  the very limited time we had, we decided to focus this conversation on Square and some broader
*  philosophical topics, and to save an in-depth conversation on engineering and AI at Twitter
*  for a second appearance on this podcast. This conversation was recorded before the outbreak
*  of the pandemic. For everyone feeling the medical, psychological, and financial burden of this crisis,
*  I'm sending love your way. Stay strong, we're in this together, we'll beat this thing.
*  As an aside, let me mention that Jack moved $1 billion of Square Equity, which is 28% of his
*  wealth, to form an organization that funds COVID-19 relief. First, as Andrew Yang tweeted,
*  is a spectacular commitment. And second, it is amazing that it operates transparently
*  by posting all its donations to a single Google Doc. To me, true transparency is simple. And this
*  is as simple as it gets. This is the Artificial Intelligence Podcast. If you enjoy it, subscribe
*  on YouTube, review it with 5 stars on Apple Podcasts, support it on Patreon, or simply connect
*  with me on Twitter at Lex Friedman, spelled F-R-I-D-M-A-N. As usual, I'll do a few minutes
*  of ads now and never any ads in the middle that can break the flow of the conversation.
*  I hope that works for you and doesn't hurt the listening experience. This show is presented by
*  Masterclass. Sign up on masterclass.com slash Lex to get a discount and to support this podcast.
*  When I first heard about Masterclass, I thought it was too good to be true. For $180 a year,
*  you get an all-access pass to watch courses from to list some of my favorites.
*  Chris Hadfield on space exploration, Neil deGrasse Tyson on scientific thinking and communication,
*  Will Wright, creator of SimCity, and Sims, both one of my favorite games on game design,
*  Jane Goodall on conservation, Carlos Santana on guitar, one of my favorite guitar players,
*  Gary Kasparov on chess, Daniel Nagrano on poker, and many, many more.
*  Chris Hadfield explaining how rockets work and the experience of being launched into space alone
*  is worth the money. For me, the key is to not be overwhelmed by the abundance of choice.
*  Pick three courses you want to complete. Watch each all the way through. It's not that long,
*  but it's an experience that will stick with you for a long time. It's easily worth the money.
*  You can watch it on basically any device. Once again, sign up on masterclass.com slash Lex
*  to get a discount and to support this podcast. And now here's my conversation with Jack Dorsey.
*  You've been on several podcasts, Joe Rogan, Sam Harris, Rich Roll, others, excellent conversations,
*  but I think there's several topics that you didn't talk about that I think are fascinating
*  that I love to talk to you about, sort of machine learning, artificial intelligence,
*  both the narrow kind and the general kind, and engineering at scale. So there's a lot
*  of incredible engineering going on that you're part of. Crypto, cryptocurrency, blockchain, UBI,
*  all kinds of philosophical questions maybe we'll get to about life and death and meaning
*  and beauty. So you're involved in building some of the biggest network systems in the world,
*  sort of trillions of interactions a day. The cool thing about that is the infrastructure,
*  the engineering at scale. You started as a programmer with C.
*  A hacker.
*  On the building. Yeah. So-
*  I'm a hacker. I'm not really an engineer.
*  Not a legit software engineer. You're a hacker at heart. But to achieve scale, you have to do some,
*  unfortunately, legit large scale engineering. So how do you make that magic happen?
*  Hire people that I can learn from, number one. I mean, I'm a hacker in the sense that
*  my approach has always been do whatever it takes to make it work so that I can see and feel the
*  thing and then learn what needs to come next. And oftentimes what needs to come next is
*  a matter of being able to bring it to more people, which is scale. And there's a lot of
*  great people out there that either have experience or are extremely fast learners
*  that we've been lucky enough to find and work with for years. But I think a lot of it,
*  we benefit a ton from the open source community and just all the learnings there that are laid
*  bare in the open. All the mistakes, all the success, all the problems. It's a very slow moving
*  process usually, open source, but it's very deliberate. And you get to see because of the
*  pace, you get to see what it takes to really build something meaningful. So I learned most of
*  everything I learned about hacking and programming and engineering has been due to open source and
*  the generosity that people have given to give up their time, sacrifice their time without any
*  expectation in return, other than being a part of something much larger than themselves,
*  which I think is great. The open source movement is amazing. But if you just look at the scale,
*  Square has to take care of, is this fundamentally a software problem or hardware problem? You
*  mentioned hiring a bunch of people, but it's not maybe from our perspective, not often talked about
*  how incredible that is to sort of have a system that doesn't go down often, that is secure,
*  is able to take care of all these transactions. Like maybe I'm also a hacker at heart and it's
*  incredible to me that that kind of scale could be achieved. Is there some insight, some lessons,
*  some interesting tidbits that you can say about how to make that scale happen? Is it the hardware
*  fundamentally challenge? Is it a software challenge? Is it a social challenge of building
*  large teams of engineers that work together, that kind of thing? What's the interesting challenges there?
*  By the way, you're the best dress hacker I've met. I think the-
*  Thank you, by the way.
*  If the enumeration you just went through, I don't think there's one. You have to
*  kind of focus on all and the ability to focus on all that really comes down to how you face problems
*  and whether you can break them down into parts that you can focus on. Because I think the biggest
*  mistake is trying to solve or address too many at once or not going deep enough with the questions
*  or not being critical of the answers you find or not taking the time to form
*  credible hypotheses that you can actually test and you can see the results of. So all of those fall
*  in the face of ultimately critical thinking skills, problem-solving skills. And if there's
*  one skill I want to improve every day, it's that. That's what contributes to learning. And the only
*  way we can evolve any of these things is learning what it's currently doing and how to take it to
*  the next step. And questioning assumptions, the first principles kind of thinking seems like
*  a fundamental to this whole process.
*  Yeah. But if you get too overextended into, well, this is a hardware issue,
*  you miss all the software solutions. And vice versa, if you focus too much on the software,
*  there are hardware solutions that can 10x a thing. So I try to resist the categories of thinking and
*  look for the underlying systems that make all these things work. But those only emerge when
*  you have a skill around creative thinking, problem-solving, and
*  being able to ask critical questions and having the patience to go deep.
*  So one of the amazing things, if you look at the mission of Square, is to increase people's access
*  to the economy. Maybe you can correct me if I'm wrong, that's from my perspective. From the
*  perspective of merchants, peer-to-peer payments, even cryptocurrency, digital cryptocurrency,
*  what do you see as the major ways our society can increase participation in the economy?
*  So if we look at today, in the next 10 years, next 20 years, you go into Africa, maybe in Africa,
*  and all kinds of other places outside of North America.
*  If there was one word that I think represents what we're trying to do at Square, it is that word
*  access. One of the things we found is that we weren't expecting this at all. When we started,
*  we thought we were just building a piece of hardware to enable people to plug it into their
*  phone and swipe a credit card. And then as we talked with people who actually tried to accept
*  credit cards in the past, we found a consistent theme, which many of them weren't even enabled,
*  not enabled, but allowed to process credit cards. And we dug a little bit deeper,
*  again, asking that question. And we found that a lot of them would go to banks or
*  these merchant acquirers, and waiting for them was a credit check and looking at a FICA score.
*  And many of the businesses that we talked to, and many small businesses, they don't have
*  good credit or a credit history. They're entrepreneurs who are just getting started,
*  taking a lot of personal risk, financial risk. And it just felt ridiculous to us that
*  for the job of being able to accept money from people, you had to get your credit checked.
*  And as we dug deeper, we realized that that wasn't the intention of the financial industry,
*  but it's the only tool they had available to them to understand authenticity, intent,
*  predictor of future behavior. So that's the first thing we actually looked at. And that's where
*  we built the hardware, but the software really came in terms of risk modeling. And that's when
*  we started down the path that eventually leads to AI. We started with a very strong data science
*  discipline because we knew that our business was not necessarily about making hardware,
*  it was more about enabling more people to come into the system.
*  So the fundamental challenge there is to enable more people to come into the system, you have to
*  lower the barrier of checking that that person will be a legitimate vendor. Is that the fundamental
*  problem here? Yeah, and a different mindset. I think a lot of the financial industry had a mindset of
*  kind of distrust and just constantly looking for opportunities to
*  prove why people shouldn't get into the system. Whereas we took on a mindset of trust and then
*  verify, verify, verify, verify, verify. So we moved, when we entered the space, only about 30 to 40
*  of the people who applied to accept credit cards would actually get through the system.
*  We took that number to 99%. And that's because we reframed the problem. We built credible models.
*  And we had this mindset of, we're going to watch not at the merchant level, but we're going to
*  watch at the transaction level. So come in, perform some transactions. And as long as you're doing
*  things that feel high integrity, credible, and don't look suspicious, we'll continue to
*  serve you. If we see any interestingness in how you use our system, that will be bubbled up to
*  people to review, to figure out if there's something nefarious going on. And that's when
*  we might ask you to leave. So the change in the mindset led to the technology that we needed.
*  To enable more people to get through and to enable more people to access the system.
*  What role does machine learning play into that? In that context of, you said, first of all,
*  it's a beautiful shift. Anytime you shift your viewpoint into seeing that people are fundamentally
*  good, and then you just have to verify and catch the ones who are not, as opposed to assuming
*  everybody's bad, this is a beautiful thing. So what role does the, to you, throughout the history
*  of the company, has machine learning played in doing that verification? It was immediate. I mean,
*  we weren't calling it machine learning, but it was data science. And then as the industry evolved,
*  machine learning became more of the nomenclature. And as that evolved, it became more sophisticated
*  with deep learning. And as that continues to evolve, it'll be another thing. But they're all
*  in the same vein. But we built that discipline up within the first year of the company. Because
*  we also had, we had to partner with the bank, we had to partner with Visa MasterCard. And we had to
*  show that by bringing more people into the system, that we could do so in a responsible way, that
*  would not compromise their systems, and that they would trust us. How do you convince this
*  Upstart company with some cool machine learning tricks is able to deliver on this sort of a
*  trustworthy set of merchants? We, we staged it out in tiers. We had a bucket of, you know, 500
*  people using it, and then we showed results, and then 1000, and then 10,000, then 50,000, and then
*  the constraint was lifted. So again, it's kind of, you know, getting something tangible out there.
*  I want to show what we can do rather than talk about it. And that put a lot of pressure on us
*  to do the right things. And it also created a culture of accountability, of a little bit
*  more transparency, and I think incentivized all of our early folks and the company in the right way.
*  So what does the future look like in terms of increasing people's access? Or if you look at
*  IoT, Internet of Things, there's more and more intelligent devices, you can see there's some
*  people even talking about our personal data as a thing that we could monetize more explicitly
*  versus implicitly. Sort of everything can become part of the economy. Do you see,
*  so what is the future of Square look like in sort of giving people access in all kinds of ways to
*  being part of the economy as merchants and as consumers? I believe that the currency we use is
*  a huge part of the answer, and I believe that the Internet deserves and requires a native currency,
*  and that's why I'm such a huge believer in Bitcoin because it just, our biggest problem
*  as a company right now is we cannot act like an Internet company. Open a new market, we have to
*  have a partnership with a local bank. We have to pay attention to different regulatory onboarding
*  environments. And a digital currency like Bitcoin takes a bunch of that away where we can potentially
*  launch a product in every single market around the world because they're all using the same
*  currency. And we have consistent understanding of regulation and onboarding and what that means. So
*  I think the Internet continuing to be accessible to people is number one,
*  and then I think currency is number two. And it will just allow for a lot more innovation,
*  a lot more speed in terms of what we can build and others can build. And it's just really exciting.
*  So I mean, I want to be able to see that and feel that in my lifetime. So in this aspect and other
*  aspects, you have a deep interest in cryptocurrency and distributed ledger tech in general. I talked to
*  Vitalik Buterin yesterday on this podcast. He says hi, by the way.
*  Hey.
*  He's a brilliant, brilliant person. Talked a lot about Bitcoin and Ethereum, of course. So
*  can you maybe linger on this point? What do you find appealing about Bitcoin, about digital currency?
*  Where do you see it going in the next 10, 20 years? And what are some of the challenges
*  with respect to Square, but also just bigger for our globally, for our world, for the way we
*  think about money? I think the most beautiful thing about it is there's no one person setting
*  the direction and there's no one person on the other side that can stop it. So we have something
*  that is pretty organic in nature and very principled in its original design. And I think
*  the Bitcoin white paper is one of the most seminal works of computer science in the last
*  20, 30 years. It's poetry. I mean, it really is.
*  Yeah, it's pretty cool technology. I mean, that's not often talked about. There's so much hype around
*  digital currency about the financial impacts of it, but the actual technology is quite beautiful
*  from a computer science perspective. Yeah, and the underlying principles behind it that
*  went into it, even to the point of releasing it under a pseudonym. I think that's a very,
*  very powerful statement. The timing of when it was released is powerful. It was a total activist
*  move. I mean, it's moving the world forward in a way that I think is extremely noble and honorable
*  and enables everyone to be part of the story, which is also really cool. So you asked the
*  question around 10 years and 20 years. I mean, I think the amazing thing is no one knows.
*  And it can emerge and every person that comes into the ecosystem, whether they be a developer
*  or someone who uses it, can change its direction in small and large ways. And that's what I think it
*  should be because that's what the internet has shown is possible. Now there's complications with
*  that, of course, and there's certainly companies that own large parts of the internet and can
*  direct it more than others. And there's not equal access to every single person in the world just
*  yet, but all those problems are visible enough to speak about them. And to me, that gives confidence
*  that they're solvable in a relatively short timeframe. I think the world changes a lot
*  as we get these satellites projecting the internet down to earth because it just removes a bunch of
*  the former constraints and really levels the playing field. But a global currency, which
*  a native currency for the internet is a proxy for, is a very powerful concept. And I don't think any
*  one person on this planet truly understands the ramifications of that. I think there's a lot of
*  positives to it. There's some negatives as well. Do you think it's possible, sorry to interrupt,
*  do you think it's possible that this kind of digital currency would redefine the nature of
*  money, sort of become the main currency of the world as opposed to being tied to fiat currency
*  of different nations and sort of really push the decentralization of control of money?
*  Definitely. But I think the bigger ramification is how it affects how society works.
*  And I think there are many positive ramifications.
*  Outside of just money.
*  Just outside of just money. Money is a foundational layer that enables so much more. I was
*  meeting with an entrepreneur in Ethiopia and payments is probably the number one
*  problem to solve across the continent, both in terms of moving money across borders between
*  nations on the continent or the amount of corruption within the current system.
*  But the lack of easy ways to pay people makes starting anything really difficult. I met an
*  entrepreneur who started the Lyft slash Uber of Ethiopia and one of the biggest problems she has
*  is that it's not easy for her riders to pay the company and it's not easy for her to pay the
*  drivers. And that definitely has stunted her growth and made everything more challenging. So
*  the fact that she even has to think about payments instead of thinking about the best
*  rider experience and the best driver experience is pretty telling. So I think as we get
*  a more durable, resilient and global standard, we see a lot more innovation everywhere.
*  And I think there's no better case study for this than the various countries within Africa
*  and their entrepreneurs who are trying to start things within health or sustainability or
*  transportation or a lot of the companies that we've seen here. So the majority of companies I met
*  in November when I spent a month on the continent were payments oriented.
*  You mentioned, and this is a small tangent, you mentioned the anonymous launch of Bitcoin
*  is a sort of profound philosophical statement.
*  Pseudonymous.
*  What's that even mean? There's a pseudonym. First of all, let me ask-
*  There's an identity tied to it. It's not just anonymous. It's Nakamoto. So Nakamoto might
*  represent one person or multiple people. But-
*  Let me ask, are you Satoshi Nakamoto? Just checking.
*  No. And if I were, what would I tell you?
*  Yeah, that's true. Maybe you slip.
*  A pseudonym is constructed identity. Anonymity is just kind of this random, drop something off
*  and leave. There's no intention to build an identity around it. And while the identity being
*  built was a short time window, it was meant to stick around, I think, and to be known.
*  And it's being honored in how the community thinks about building it. The concept of
*  Satoshi's, for instance, is one such example. But I think it was smart not to do it anonymous,
*  not to do it as a real identity, but to do it as pseudonym because I think it builds
*  tangibility and a little bit of empathy that this was a human or a set of humans behind it. And
*  there's this natural identity that I can imagine. But there is also a sacrifice of ego.
*  That's a pretty powerful thing from the perspective.
*  Yeah, which is beautiful.
*  Would you do, philosophically, to ask you the question, would you do
*  all the same things you're doing now if your name wasn't attached to it?
*  If you had to sacrifice the ego? Put another way, is your ego deeply tied
*  in the decisions you've been making?
*  I hope not. I believe I would certainly attempt to do the things without my name having to be
*  attached with it. But it's hard to do that in a corporation,
*  legally. That's the issue. If I were to do more open source things, then absolutely. I don't need
*  my particular identity, my real identity associated with it. But I think the appreciation that comes
*  from doing something good and being able to see it and see people use it is pretty overwhelming
*  and powerful, more so than maybe seeing your name in the headlines.
*  Let's talk about artificial intelligence a little bit, if we could.
*  70 years ago, Alan Turing formulated the Turing test. To me, natural language is one of the most
*  interesting spaces of problems that are tackled by artificial intelligence. It's the canonical
*  problem of what it means to be intelligent. He formulated it as the Turing test. Let me ask the
*  broad question, how hard do you think it is to pass the Turing test in the space of language?
*  Just from a very practical standpoint, I think where we are now and for at least years out,
*  is one where the artificial intelligence, machine learning, the deep learning models,
*  can bubble up interestingness very, very quickly and pair that with
*  human discretion around severity, around depth, around nuance and meaning. I think for me,
*  the chasm the cross for general intelligence is to be able to explain why and the meaning
*  behind something. Behind a decision? Behind a decision or a set of data.
*  The explainability part is essential to be able to explain using natural language why the decisions
*  were made, that kind of thing. I think that's one of our biggest risks in artificial intelligence
*  going forward is we are building a lot of black boxes that can't necessarily explain why they
*  made a decision or what criteria they used to make the decision. We're trusting them more and more
*  from lending decisions to content recommendation to driving to health. A lot of us have watches
*  that tell us, do I understand? How was it deciding that? That one's pretty simple. But you can imagine
*  how complex they get. Being able to explain the reasoning behind some of those recommendations
*  seems to be an essential part. Although it's a very hard problem because sometimes even we
*  can't explain why we make decisions. That's what I was, I think we're being sometimes a little
*  bit unfair to artificial intelligence systems because we're not very good at some of these things.
*  Do you think, apologize for the ridiculous romanticized question, but on that line of
*  thought, do you think we'll ever be able to build a system like in the movie Her that you could fall
*  in love with? So have that kind of deep connection with. Hasn't that already happened? Hasn't so much
*  in Japan fallen in love with this, his AI? There's always going to be somebody that does that kind
*  of thing. I mean, at a much larger scale of actually building relationships, of being deeper
*  connections, it doesn't have to be love, but it just deeper connections with artificial intelligence
*  systems. So you mentioned explainability. That's less a function of the artificial intelligence and
*  more a function of the individual and how they find meaning and where they find meaning. Do you
*  think we humans can find meaning in technology in this kind of way? Yeah, 100%. And I don't
*  necessarily think it's a negative, but it's constantly going to evolve. So I don't know,
*  but meaning is something that's entirely subjective. And I don't think it's going to be a function of
*  finding the magic algorithm that enables everyone to love it. But maybe. But that question really
*  gets at the difference between human and machine. You had a little bit of an exchange with Elon Musk.
*  Basically, I mean, it's a trivial version of that, but I think there's a more fundamental question of
*  is it possible to tell the difference between a bot and a human? And do you think it's
*  if we look into the future, 10, 20 years out, do you think it would be possible or is it even
*  necessary to tell the difference in the digital space between a human and a robot? Can we have
*  fulfilling relationships with each or do we need to tell the difference between them?
*  I think it's certainly useful in certain problem domains to be able to tell the difference.
*  I think in others, it might not be as useful. I think it's possible for us today to tell that
*  difference. It's the reverse, the meta of the Turing test. Well, what's interesting is I think
*  the technology to create is moving much faster than the technology to detect. Do you think so?
*  So if you look at adversarial machine learning, there's a lot of systems that try to fool machine
*  learning systems. And at least for me, the hope is that the technology to defend will always be
*  right there, at least. Your sense is that- I don't know if they'll be right there. I mean,
*  it's a race, right? So the detection technologies have to be two or 10 steps ahead of the creation
*  technologies. This is a problem that I think the financial industry will face more and more because
*  a lot of our risk models, for instance, are built around identity. Payments ultimately comes down
*  to identity. And you can imagine a world where all this conversation around deepfakes goes
*  towards the direction of driver's license or passports or state identities. And people
*  construct identities in order to get through a system such as ours to start accepting credit
*  cards or into the cash app. And those technologies seem to be moving very, very quickly. Our ability
*  to detect them, I think, is probably lagging at this point. But certainly with more focus,
*  we can get ahead of it. But this is going to touch everything. So I think it's like security. We're
*  never going to be able to build a perfect detection system. We're only going to be able to-
*  what we should be focused on is the speed of evolving it and being able to take signals
*  that show correctness or errors as quickly as possible and move and to be able to build that
*  into our newer models or the self-learning models. Do you have other worries? Like some people,
*  like Elon and others, have worries of existential threats of artificial intelligence, of artificial
*  general intelligence, or if you think more narrowly about threats and concerns about
*  more narrow artificial intelligence, what are your thoughts in this domain? Do you have concerns or
*  are you more optimistic? I think Yuval, in his book 21 Lessons for the 21st Century, his last chapter
*  is around meditation. And you look at the title of the chapter and you're like, oh, it's all
*  meditation. But what was interesting about that chapter is he believes that kids being born today,
*  growing up today, Google has a stronger sense of their preferences than they do,
*  which you can easily imagine. I can easily imagine today that Google probably knows my
*  preferences more than my mother does. Maybe not me per se, but for someone growing up only knowing
*  the internet, only knowing what Google is capable of, or Facebook or Twitter or Square or any of
*  these things, the self-awareness is being offloaded to other systems and particularly these algorithms.
*  And his concern is that we lose that self-awareness because the self-awareness
*  is now outside of us and it's doing such a better job at helping us direct our decisions around
*  should I stand? Should I walk today? What doctor should I choose? Who should I date? All these
*  things we're now seeing play out very quickly. So he sees meditation as a tool to build that
*  self-awareness and to bring the focus back on why do I make these decisions? Why do I react
*  in this way? Why did I have this thought? Where did that come from? That's the way to regain control.
*  Or awareness, maybe not control, but awareness so that you can be aware that, yes, I am offloading
*  this decision to this algorithm that I don't fully understand and can't tell me why it's doing the
*  things it's doing because it's so complex. That's not to say that the algorithm can't be a good
*  thing. And to me, recommender systems, the best of what they can do is to help guide you on a journey
*  of learning new ideas of learning period. It can be a great thing, but do you know you're doing that?
*  Are you aware that you're inviting it to do that to you? I think that's the risk he identifies,
*  right? That's perfectly okay, but are you aware that you have that invitation and it's being acted
*  upon? And so that's a concern. You're kind of highlighting that without a lack of awareness,
*  you can just be floating at sea. So awareness is key in the future of these artificial intelligence
*  systems. Yeah, the movie Wall-E, which I think is one of Pixar's best movies besides Redetory.
*  Redetory was incredible. You had me until Redetory. Okay. Redetory was incredible.
*  All right, we've come to the first point where we disagree. Okay. It's the entrepreneurial story
*  in the form of a rat. I just remember just the soundtrack was really good. So excellent.
*  What are your thoughts sticking on artificial intelligence a little bit about the displacement
*  of jobs? That's another perspective that candidates like Andrew Yang talk about.
*  Yang gang forever. Yang gang. So he unfortunately, speaking of Yang gang, has recently dropped out.
*  I know it was very disappointing and depressing. Yeah, but on the positive side, he's I think
*  launching a podcast. So- Really? Cool. Yeah. He just announced that. I'm sure he'll try to talk
*  you into trying to come onto the podcast. I would love to. About Redetory?
*  Yeah. Maybe he'll be more welcoming of the Ratatouille argument. What are your thoughts
*  on his concerns of the displacement of jobs, of automation, of course, there's positive impacts
*  that could come from automation and AI, but there could also be negative impacts. And within that
*  framework, what are your thoughts about universal basic income? So these interesting new ideas of
*  how we can empower people in the economy? I think he was 100% right on almost every dimension.
*  We see this in Squares business. I mean, he identified truck drivers from Missouri,
*  and he certainly pointed to the concern and the issue that people from where I'm from
*  feel every single day that is often invisible and not talked about enough.
*  The next big one is cashiers. This is where it pertains to Squares business.
*  We are seeing more and more of the point of sale move to the individual customer's hand in the
*  form of their phone and apps and pre-order and order ahead. We're seeing more kiosks. We're seeing
*  more things like Amazon Go. And the number of workers as a cashier in retail is immense.
*  And there's no real answers on how they transform their skills and work into something else.
*  And I think that does lead to a lot of really negative ramifications.
*  And the important point that he brought up around universal basic income is given that
*  this shift is going to come and given it is going to take time to set people up with new
*  skills and new careers, they need to have a floor to be able to survive. And this $1,000 a month
*  is such a floor. It's not going to incentivize you to quit your job because it's not enough.
*  But it will enable you to not have to worry as much about just getting on day to day
*  so that you can focus on what am I going to do now and what am I going to,
*  what skills do I need to acquire. And I think a lot of people point to
*  the fact that during the industrial age, we had the same concerns around automation,
*  factory lines, and everything worked out okay. But the biggest change is just the
*  velocity and the centralization of a lot of the things that make this work, which is the data
*  and the algorithms that work on this data. I think the second biggest scary thing is just
*  around AI is just who actually owns the data and who can operate on it. And
*  are we able to share the insights from the data so that we can also build
*  algorithms that help our needs or help our business or whatnot. So that's where I think
*  regulation could play a strong and positive part. First, looking at the primitives of
*  AI and the tools we use to build these services that will ultimately touch every single aspect
*  of the human experience. And then where data is owned and how it's shared. So those are the
*  answers that as a society, as a world, we need to have better answers around, which we're currently
*  not. They're just way too centralized into a few very, very large companies. But I think it was
*  spot on with identifying the problem and proposing solutions that would actually work. At least that
*  we'd learned from that you could expand or evolve. But I mean, I think UBI is well past its due. I
*  was certainly trumpeted by Martin Luther King and even before him as well.
*  And like you said, the exact thousand dollar mark might not be the correct one, but you should take
*  the steps to try to implement these solutions and see what works. 100%.
*  So I think you and I eat similar diets. At least I was-
*  First time I've heard this. Yeah. So I was doing it-
*  First time anyone has said that to me in this case.
*  Yeah. But it's becoming more and more cool. But I was doing it before it was cool. So intermittent
*  fasting and fasting in general, I really enjoy. I love food, but I enjoy the- I also love suffering
*  because I'm Russian. So fasting kind of makes you appreciate what it is to be human somehow.
*  So, but I have a- outside the philosophical stuff, I have a more specific question. It also
*  helps me as a programmer and a deep thinker, like from the scientific perspective to sit there for
*  many hours and focus deeply. Maybe you were a hacker before you were CEO. What have you learned
*  about diet, lifestyle, mindset that helps you maximize mental performance to be able to focus
*  for- to think deeply in this world of distractions? I think I just took it for granted
*  for too long. Which aspect? Just the social structure of we eat three meals a day and
*  there's snacks in between. And I just never really asked the question why. Oh, by the way,
*  in case people don't know, I think a lot of people know, but you at least, you famously eat once a
*  day. You still eat once a day. Yep. I eat dinner. By the way, what made you decide to eat once a
*  day? Because to me, that was a huge revolution that you don't have to eat breakfast. That was
*  like, I felt like I was a rebel. Like I abandoned my parents or something and became an anarchist.
*  When you first- like the first week you start doing it, it feels like you kind of have a superpower.
*  Then you realize it's not really a superpower. But I think you realize, at least I realize,
*  just how much our mind dictates what we're possible with. And sometimes we have structures around us
*  that incentivize this three-meal-a-day thing, which was purely social structure versus necessity for
*  our health and for our bodies. And I did it just- I started doing it because I played a lot with my
*  diet when I was a kid and I was vegan for two years and just went all over the place. Just
*  because health is the most precious thing we have and none of us really understand it. So being able
*  to ask the question through experiments that I can perform on myself and learn about is compelling
*  to me. And I heard this one guy on the podcast, Wim Hof, who's famous for doing ice baths and
*  holding his breath and all these things. He said he only eats one meal a day. I'm like, wow, that
*  sounds super challenging and uncomfortable. I'm gonna do it. So I learn the most when I make myself-
*  I wouldn't say suffer, but when I make myself feel uncomfortable because everything comes to bear
*  in those moments and you really learn what you're about or what you're not.
*  So I've been doing that my whole life. When I was a kid, I could not speak. I had to go to
*  a speech therapist and it made me extremely shy. And then one day I realized I can't keep doing
*  this and I signed up for the speech club and it was the most uncomfortable thing I could imagine
*  doing, getting a topic on a note card, having five minutes to write a speech about whatever that
*  topic is, not being able to use the note card while speaking and speaking for five minutes
*  about that topic. But it gave me so much perspective around the power of communication,
*  around my own deficiencies and around if I set my mind to do something, I'll do it.
*  So it gave me a lot more confidence. So I see fasting in the same light. This is something that
*  was interesting, challenging, uncomfortable, and has given me so much learning and benefit
*  as a result. And it will lead to other things that I'll experiment with and play with. But yeah,
*  it does feel a little bit like a superpower sometimes. The most boring superpower one can
*  imagine. No, it's quite incredible. The clarity of mind is pretty interesting.
*  Speaking of suffering, you kind of talk about facing difficult ideas. You meditate. You think
*  about the broad context of life of our society. Let me apologize again for the romanticized
*  question, but do you ponder your own mortality? Do you think about death, about the finiteness
*  of human existence when you meditate, when you think about it? And if you do,
*  how do you make sense of it, that this thing ends?
*  Well, I don't try to make sense of it. I do think about it every day. I mean, it's a daily,
*  multiple times a day. Are you afraid of death?
*  No, I'm not afraid of it. I think it's a transformation. I don't know to what, but it's
*  also a tool to feel the importance of every moment. So I just use as a reminder, like,
*  I have an hour. Is this really what I'm going to spend the hour doing?
*  I only have so many more sunsets and sunrises to watch. I'm not going to get up for it.
*  I'm not going to make sure that I try to see it. So it just puts a lot into perspective,
*  and it helps me prioritize. I don't see it as something that I dread or is dreadful. It's a
*  tool that is available to every single person to use every day because it shows how precious life
*  is. And there's reminders every single day, whether it be your own health or a friend or
*  a coworker or something you see in the news. So to me, it's just a question of what we do with that
*  daily reminder. And for me, it's, am I really focused on what matters? And sometimes that
*  might be work. Sometimes that might be friendships or family or relationships or whatnot. But that's
*  the ultimate clarifier in that sense. So on the question of what matters,
*  another ridiculously big question of once you try to make sense of it, what do you think is the
*  meaning of it all? The meaning of life? What gives you purpose, happiness, meaning?
*  A lot does. Just being able to be aware of the fact that I'm alive is pretty meaningful.
*  The connections I feel with individuals, whether they're people I just meet or long lasting
*  friendships or my family is meaningful. Seeing people use something that I helped build is
*  really meaningful and powerful to me. But that sense of, I mean, I think ultimately comes down
*  in a sense of connection and just feeling like I am bigger. I am part of something that's bigger
*  than myself and like I can feel it directly in small ways or large ways. However it manifests
*  as probably it. Last question, do you think we're living in a simulation?
*  I don't know. It's a pretty fun one if we are, but also crazy and random and
*  with tons of problems. Would you have it any other way?
*  Yeah. I mean, I just think it's taken us way too long as a planet to realize we're all in this
*  together and we all are connected in very significant ways. I think we hide our connectivity
*  very well through ego, through whatever it is of the day. But that is the one thing I would want to
*  work towards changing and that's how I would have it another way. Because if we can't do that,
*  then how are we going to connect to all the other simulations? Because that's the next step is like
*  what's happening in the other simulation. Escaping this one and yeah,
*  spanning across the multiple simulations and sharing it and on the fun. I don't think there's
*  a better way to end it. Jack, thank you so much for all the work you do. There's probably other
*  ways that we've ended this in other simulations that may have been better.
*  We'll have to wait and see. Thanks so much for talking to me.
*  Thank you. Thanks for listening to this conversation with Jack Dorsey and thank you
*  to our sponsor, Masterclass. Please consider supporting this podcast by signing up to Masterclass
*  at masterclass.com slash Lex. If you enjoy this podcast, subscribe on YouTube, review it with five
*  stars on Apple podcast, support on Patreon or simply connect with me on Twitter at Lex Friedman.
*  And now let me leave you with some words about Bitcoin from Paul Graham.
*  I'm very intrigued by Bitcoin. It has all the signs of a paradigm shift.
*  Hackers love it, yet it is described as a toy, just like microcomputers.
*  Thank you for listening and hope to see you next time.
*  Bye.

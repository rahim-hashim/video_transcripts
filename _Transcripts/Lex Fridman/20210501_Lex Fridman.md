---
Date Generated: April 13, 2024
Transcription Model: whisper medium 20231117
Length: 10797s
Video Keywords: ['agi', 'ai', 'ai podcast', 'artificial intelligence', 'artificial intelligence podcast', 'lex ai', 'lex fridman', 'lex jre', 'lex mit', 'lex podcast', 'mit ai', 'sergey nazarov']
Video Views: 834391
Video Rating: None
---

# Sergey Nazarov: Chainlink, Smart Contracts, and Oracle Networks | Lex Fridman Podcast #181
**Lex Fridman:** [May 01, 2021](https://www.youtube.com/watch?v=TPXTmVdlyoc)
*  The following is a conversation with Sergey Nazarov, CEO of Chainlink, which is a decentralized
*  Oracle network that provides data to smart contracts. He and his team have done seminal
*  research and engineering in the space of smart contracts. Check out the Chainlink 2.0 white
*  paper that I found to be a great overview of their technology and vision. It's 136 pages,
*  but very accessible. Quick mention of our sponsors. Wineaccess, Athletic Greens, Magic Spoon,
*  Indeed, and BetterHelp. Check them out in the description to support this podcast.
*  As a side note, let me say that externally connected smart contracts that combine the
*  ocean of data out there with the security of the blockchain are fascinating to me,
*  both technically and philosophically. Data is knowledge, and knowledge is power. I think the
*  more reliable data sources we integrate into our decision making, especially when those decisions
*  are executed by programs, the more efficient and productive our decisions become. There are
*  interactions between humans that should not be formalized digitally, like love, for example,
*  but for all the others, there's no reason for smart contracts not to automate away the menial
*  parts of life. Making more room for good conversation over brisket and maybe some vodka
*  with old and new friends. This is the Lex Friedman podcast, and here is my conversation
*  with Sergey Nazarov. Is that Yozhyk there? So I gave away everything I owned a few times in my life,
*  and he accidentally survived. And I don't like stuffed animals. What I really liked about,
*  I got him in a thrift store. What I liked about him is because I'd never seen a stuffed animal,
*  that looks pissed off at life. Like they're usually smiling in the dumbest of ways,
*  and this guy was just pissed. Yeah, I gotta tell you, that's actually pretty funny.
*  I like this guy. If you had to live only in the digital world or the physical world,
*  which would you choose? So I think this is actually a question more about what the fidelity
*  of the digital world would be versus the physical world. I think this type of question, this whole
*  simulation thing actually comes from papers about 20, 30 years ago in the philosophical world where
*  people tried to make this thought experiment of would you be comfortable if everything that was
*  happening to you happened in a simulation? What they were trying to do is they were intuitively
*  trying to understand is there some kind of intuitive personal connection we have to something
*  being the real world, right? And then the Matrix movie actually came out of these papers, and then
*  these ideas made their way into the public consciousness. I personally think that if I
*  had the choice to be in the digital world at the same fidelity as the real world with immortality,
*  I would absolutely go with the digital world. Wait, wait, wait, wait, wait, wait. How'd you add the
*  immortality part? You don't get immortality. If you think about how we would go into the digital
*  world, our brain patterns would be mapped onto some kind of probably virtual machine, right?
*  That would mean immortality, right? Because the virtual machine has no limit to how long it can
*  exist. Don't you think there would be a versioning system? This is a soft fork versus hard fork
*  question. Whether Sergey version 2.0 would be different from Sergey version 1.0, there would
*  be an upgrade. So that's immortality. Sergey 1.0 would die in the digital world. You get a software
*  update, and then that's it. Well, yeah. When people go into the Star Trek transporter,
*  are they killed or are they transported? I don't really know. I haven't read any papers on this.
*  I haven't really thought about it too much. There's no white paper on the transporter.
*  Not at this point. What does fidelity mean exactly to you? Is it strictly... So the fidelity of the
*  physics world, the physical world is maybe now questions of physics, quantum mechanics. What is
*  at the bottom of it all? Or do you mean the fidelity of the actual experience?
*  It's just perception. It's just perception. But that's limited by human cognitive capabilities.
*  It is, but I don't really have anything else, right? I think all of these papers that brought
*  up these questions of assimilation, they were in epistemology and metaphysics. And what they
*  were trying to do, I think, was they were trying to put people through a thought experiment where
*  they would come out on the other end and say, the reality of life is really worth something.
*  And ignorance isn't bliss, which is that consistent statement in The Matrix. Ignorance
*  is bliss. That's what one of the guys says when he's doing something wrong and trying to get back
*  into The Matrix. And the question is, is ignorance bliss? And it's a different version of that.
*  I think from a perceptual point of view, if my perceptions aren't in any way different,
*  so fidelity is very good, it doesn't matter. I don't know, right? So if I don't know something,
*  it doesn't really exist. And if it doesn't exist in my perception or my consciousness,
*  then it doesn't exist, period, for me, at least. And then whether it exists in some more metaphysical
*  version of things, I personally never really got into the metaphysics stuff because I could never
*  really... I couldn't understand what the point of it was. It's one of these things where I couldn't
*  really get what the practical application of it was. And this is from those realm of questions.
*  If there was something about the world but you didn't have a capacity to perceive it,
*  would it matter to you? To me, it wouldn't matter.
*  LW Right. To me, by the way, the simulation thing is a really interesting engineering question,
*  which is how difficult is it to engineer a virtual reality, a digital world that is sufficiently
*  of high fidelity where you would want to live in it. I think that's a really testable and a fascinating
*  engineering question. Because my intuition says it's not as difficult as we think. It's not nearly
*  as difficult as having to create a quantum mechanical simulation that's large enough to
*  capture the full human experience. It might be just as simple as just a really nice quake game,
*  like with a nice engine, just creating all the basic visual elements that trick our visual cortex
*  into believing that we're actually in a physical environment. And I think that if that's true,
*  then that's quite... A high fidelity digital world is actually achievable within a century.
*  And that changes things. LW Yeah, maybe in our lifetime. I'm really
*  hoping for that. I'm hoping somebody can copy my brain waves onto a virtual machine and allow
*  that consciousness to continue to exist. Whether that's death or not, I don't know.
*  But I think it's actually going to require some serious leaps. Even the VR headsets,
*  they don't work if they go below 90 frame rates. People start getting freaked out. So you have to
*  go from one gaming screen of 60 frames per second to two screens of 90 frames per second.
*  And so people's hardware today can't even handle that. And that's for these two little screens
*  by your eyeballs, what it's going to take to completely trick my consciousness into not
*  knowing the difference in terms of all the sensory inputs. I'm keeping my fingers crossed. Whoever
*  does that and is close to doing that, they should contact me. I want to have my brain waves turned
*  into a virtual machine. LW Would you in that context, if Morpheus came to you, would you take
*  the blue pill or the red pill? Meaning, would you be happy just living in that world and not knowing
*  that you're living inside that virtual world that's running a computer? Or would you want to know the
*  truth of it? LW Well, actually, I think that's a very different question. There's actually a moral
*  ethical question there about whether you should allow a bunch of people to get manipulated and
*  killed and enslaved because in The Matrix, they're all enslaved as like a AAA battery to turn a human
*  being into the battery. So I think the moral and ethical question of that, fascinating enough,
*  isn't actually different than the moral and ethical questions we face today in modern daily life.
*  But I probably have given the choice of just completely going along or going against it. I
*  would probably go against it if I had to make this kind of binary choice because going along with it,
*  I think at that scale of scary stuff happening to people is probably something really,
*  really difficult. LW But for your individual life, it's way more fun to go along with it.
*  So you're saying you value the opposing a system that includes the suffering of others
*  versus just for yourself enjoying the ride. I mean, if there is such a binary choice,
*  why choose the opposite system? LW I think it's the nature of the ethical
*  dilemma that you face in that situation. There's kind of some, you know, this is obviously not
*  something that's happening now, right? LW We don't know this, right?
*  LW At the end of the day, at that scale of something like that happening, yeah, that scale
*  of people being manipulated and harmed, then I think pretty much almost all people have an
*  obligation to go against it. Probably that's what that looks like, in my opinion.
*  LW So you've talked about the concept of definitive truth. What is it? And in general,
*  what is the nature of truth in human civilization? And just talking about the digital age,
*  the nature of truth in the digital age. LW So the interesting thing about definitive
*  truth is that it actually exists on this, at least in my mind, on this spectrum between objective
*  truth and just, you know, somebody made something up and nobody else agrees. So what I think
*  definitive truth is, is it's somewhere in the middle on that spectrum, where if you and me
*  define what truth is, right, like if you and me have an agreement of some kind, and we say,
*  as long as the weather is sunny, or the weather isn't, there is no rain on that day, then there
*  will be an insurance policy that results. And you and me both agree that as long as three sensors
*  monitoring weather monitoring stations all say that, then the definitive truth for us and for
*  that agreement is the result of those systems coming to consensus about what happened out in
*  the real world. I think the objective truth definition from kind of the philosophical world
*  is really, really stringent and very, very hard to attain. And that's not what this is. And that's
*  actually not what commerce or the ability for people to interact about contracts needs.
*  What I think the world of commerce needs is an upgrade from someone can unilaterally decide what
*  the truth is to there can be a pre-agreed set of conditions where we define what the truth is
*  under those conditions. And then, you know, you and me basically say, if these 20 nodes or of these
*  30 data sources come to consensus within, you know, this method of consensus with this threshold
*  of agreement, then definitive truth has been achieved for you and me in our relationship
*  for this specific agreement. And the specificity and our shared agreement to that kind of truth
*  or that definitive truth being acceptable to both of us is probably what's kind of necessary and
*  sufficient for everything to move forward in a better way. In any case, much better than,
*  you know, I'm a bank or an insurance company. I'm going to unilaterally decide what happens.
*  It's definitely an upgrade from that. Do you think it's possible to define formally in this way
*  a definitive truth for many things in this world? Like you talked about, whether
*  basically defining that if three sensors of weather agree, then that we're going to agree
*  that that is a definitive useful truth for us to operate under. So how many things in this world
*  can be formalized in this way? Do you think? A huge amount. So there's actually
*  two things going on here. One thing is the amount of data that already exists,
*  right? And the pieces of data coming off of, you know, markets, IoT, shipment of goods, any number
*  of other things. Like even your YouTube channel has a certain amount of likes or a certain amount
*  of clicks or a certain amount of views, and even that's quantifiable, right? So even to a certain
*  degree, what we do here today, you and me right now can be quantified as far as the amount of views,
*  the amount of clicks, the amount of any number of other things. You, the viewer, have power of data
*  in your hands by clicking like or dislike right now, or the subscribe button or the unsubscribe
*  button, which I encourage you to do. Anyway, okay, so there's data flowing into all interactions in
*  this world. There's data. There's more and more data, right? More and more data. That data is
*  more and more accessible to everybody. And that accessibility and the fact that there's more of
*  it means we can form more definitive truth proofs. We can form more and more proofs. And as we form
*  those proofs, well, we can provide them to these blockchains and smart contract systems that consume
*  them and then they're tamper proof, right? So they can't be manipulated. And so now we've
*  combined a system that can prove things with a system that guarantees a certain outcomes.
*  And we have a better system of contracts, which is actually an unbelievably powerful tool
*  that has never existed before. Can we talk about the world of commerce and finance,
*  decentralized finance? What is it? What's its promise from both the philosophical and
*  technical perspective? If we just zoom in on that particular space of the digital world?
*  Sure. So the decentralized finance is the instantiation of a specific type of smart contract,
*  right? Or what I call hybrid smart contracts, which are these contracts that combine the on-chain
*  code together with the off-chain proofs that something happened. They're called a hybrid
*  because they basically use both of these systems, right? The blockchain and the proofs about what
*  happened. And what DeFi is, is one specific type of hybrid smart contract that is taking on the
*  contractual agreements you traditionally find in the global financial system, right? And that's
*  basically the world of lending, the world of yield generation for people giving me or giving
*  whoever their money and somebody giving back them yield back to them, which is what bonds do and
*  what treasuries do and what a lot of the global financial markets do, as well as the ability to
*  gain exposure and protection from different types of events and risks. That's a lot of what
*  derivatives do, right? Derivatives allow us to say, hey, something's going to happen and I'm
*  either going to protect myself by getting paid if it happens, or I'm going to benefit from it happening
*  by basically saying it's going to happen, putting money down on that. And that prediction will get
*  me a return. Now, that's a very large part of the global financial system, excluding all the stuff
*  for global trade and letters of credit and all the stuff that facilitates international trade. So
*  excluding that at least for now. So if we look at what decentralized finance does, it takes all of
*  those agreements about generating yield, lending, and all of these types of things you find in
*  global finance and the world of derivatives and a few other types of financial products,
*  and it basically puts them into a different format. So the format you have for centralized
*  financial agreements is that you go to a bank, even if you're a hedge fund, even if you're the
*  richest people, you go to a bank, they make a product for you and you hope that they honor
*  the product that they made for you. Or you do a deal with another hedge fund or whoever,
*  some counterparty, and you hope that that deal is honored. And then a number of very freaky things
*  start to take place. One of them is people don't have clarity about what the agreement is. So a
*  lot of people don't know exactly what the agreement is between those parties because they can't
*  actually see it. Sometimes agreements are kept very private or parts of them are kept private,
*  and that keeps other counterparties, other people in the system from understanding what's going on.
*  This is actually partly what happened with the mortgage crisis. The mortgage crisis in 2008 was
*  basically there were a lot of agreements, there were a lot of assets, but because the centralized
*  financial system worked in such an opaque way, it was so unbelievably difficult to understand what
*  was going on. And so that lack of understanding for the global financial system basically led to
*  a big boom and then correspondingly, very, very big bust, which amazingly enough had a huge impact
*  on everybody even though they didn't participate in the boom part of the equation. In any case,
*  what decentralized finance does is it takes these financial contracts that power the global
*  financial system, it puts them in this new blockchain-based format that basically at this
*  point provides three very powerful things. The first thing that it provides is complete
*  transparency over what's going on with your financial product. So this means when you use
*  a financial product in the DeFi format, you and you as a technical person actually can drill down
*  very, very, very deeply and you can understand where the collateral is, you can understand how
*  much collateral there is, you can understand what format it's in, you can understand how it's
*  changing, you can understand this on a second to second or block to block basis. So you have
*  complete transparency into what's going on in the financial protocol that you have your assets in,
*  which is because blockchains and infrastructure, all of these things are built on,
*  force that transparency. Whereas the centralized financial system is very, very good at hiding it.
*  It's very good at hiding it and packaging things in a glossy wrapper, creating a boom, then a bust.
*  The centralized finance is built on infrastructure that forces transparency such that everyone can
*  understand what the financial product does from day one and in fact escaping that property is
*  practically impossible or if someone tries to escape it, it becomes immediately obvious and
*  people don't use their financial product. So that's number one. Number two is control.
*  So if you look at what happened with Robinhood, everybody thought the system worked a certain
*  way, right? Everybody thought I have a brokerage account, I can trade things under a certain set
*  of market conditions. And then the market conditions changed within the band of what people
*  thought they could do. And everybody was fascinated to find out that, oh my God, I thought my band of
*  market conditions in which I can control my assets is X, but it is actually Y. It's actually much,
*  much smaller band. And the reason it is a much, much smaller group of market conditions is that
*  the system doesn't work the way people think it works. The system was wrapped up in a nice
*  glossy wrapper and given to them to get them to participate in the system because the system
*  requires and needs their participation. But if you actually look at how the system works underneath,
*  you will see that it does not work the way people think that it works. And this is actually another
*  reason that DeFi is so powerful because DeFi actually, and these blockchain contracts,
*  give people the version of the world they think they already have, which is why they don't beg for
*  it, right? So everybody thinks they're in a certain version of the world that works in this reliable
*  transparent way. They're not. They don't realize it. And so they're confused when you tell them,
*  I'm going to make the world work this way because they think they're already in that world.
*  But then things like Robinhood make it immediately painfully clear that that's not how the world
*  works. So that the second real property of DeFi is control, which means that you control your assets,
*  not a bank, not a broker, not a third party, you. You control your Bitcoins. You control your tokens
*  in the finance protocol. If you don't like how something's going in that protocol, you can remove
*  it. You can send it to another protocol, or you can use a feature of the protocol to do something
*  it's supposed to do. And guess what? Nobody can just say, oops, you know, that feature,
*  that isn't so good for my friends over here. You know, that feature is actually, you know,
*  we're just going to pause that feature in the critical moment when you need it to execute your
*  strategy, which is why you took all the risk to begin with. And then the final reason,
*  the final thing to know about DeFi is that DeFi is inherently global and actually right now provides
*  better yield globally. So if you go to a bank right now with the US dollar, you get 1% or less.
*  If you go to DeFi with the US dollar, you get 7% or 8%. So if we think about that,
*  in a world where there's a lot of inflation coming down the road, and we think about, well,
*  you know, a lot more systems might be failing soon, and they might be highlighting these types
*  of problems that were there for, or as a result of the type of control that you see in Robinhood,
*  and people are more and more concerned about both transparency and control, and they're looking for
*  yield to combat inflation. I think that's what DeFi is about in a practical sense. It is this
*  clarity about your risk, it is control over your assets, and amazingly, at the same time as having
*  those two unbelievably useful properties, it is actually superior yield, which just leads me to
*  the very obvious conclusion that the only reason DeFi isn't more used is because more people don't
*  know about it. And by virtue of this long kind of explanation here and elsewhere, more people will
*  know about it. And it's just such an obviously superior solution that I haven't heard a single
*  explanation as to why. No, no, don't earn 8% and take less risk and have more transparency
*  with your assets. Earn 7% less, take more risk, and give people the ability to change the rules
*  on you at their discretion. Go do that. Who's going to do that? And in general, on the first two of
*  transparency and control, first of all, I do think, maybe you can correct me, but from my perspective,
*  they're like deeply tied together in the sense that transparency gives control.
*  Transparency creates accountability, and there's this kind of game being played,
*  game theoretic game, where if I know, if you know I'm going to discover your deviation,
*  you're not going to deviate. Yes. This could be a whole other conversation, but just as a small
*  aside, on the social network side of things, which I've been thinking deeply about in the past year
*  or so of how to do it right there, how to fix our social media. And I tend to believe that
*  human beings, if they're given clear transparency about which data is being stored, how it's being
*  used, where it's being moved about, just all a clear, simple transparency of how their data
*  is being used and them having the control at the very minimal level of being able to participate
*  or to walk away. And walk away means delete everything you ever known about me.
*  That will create a much, much better world. That currently there's a complete lack of transparency
*  on the social media, how the data is being used for your own protection. I mean, there's a lot
*  of parallels to the central bank situation, and there is not a control element of being able to
*  walk away. Being able to delete all your data, delete your account on Facebook is very difficult.
*  It doesn't take a single click, which I think is what it should take. There should be a big red
*  button that says, delete everything you've ever known about me, or forget me. So I think that
*  couple together can create a very different kind of world and create an incentivization that will
*  lead to progress and innovation and just a much better social network and a really good business
*  for the future social networks. So I tend to see control as naturally being an outgrowth from the
*  transparency. It should all start at the transparency, which is why the smart contract formulation
*  is fascinating because you're formalizing in a simple, clear way any agreements that you're
*  participating in. And as a side comment also, what's really inspiring to me is that I think
*  there's a greater, I don't know if this is always the case, but it seems like from having talked to
*  people on the psychological element, there's a hunger amongst people for transparency and
*  for control. Like transparency, another word for that is authenticity. If you look at the kind of
*  stuff that people hunger for now, they want to know the reality of who you are as an individual.
*  So that means you can create businesses, you can create tools that are built on authenticity,
*  a transparency. And then the same, I'm inspired by the intelligence of people. If you give them
*  control, if you give them power, that they would make good choices. That's really exciting. Of
*  course, not everybody, but that means that decentralized power can create effective systems.
*  So a couple that there's a hunger for transparency. So we can move to a world where everyone's being
*  just like real, you know, conveying their genuine human nature. And people are sufficiently
*  intelligent that if they're given power in a distributed mass scale sense, that we're going
*  to build a better world through that as opposed to centralized supervised control, or only a small
*  percent of the population know what the hell they're doing. Everybody else is clueless sheep.
*  So those two coupled together is really, to me, inspiring.
*  Just to really quickly comment on the stuff that you just said, which I think is super,
*  super, super fascinating. I think that's all exactly right. I think everything that you said
*  is right. And I think it's actually going to be the same for social media and banking and every
*  other type of contract is that all of those systems that house people's value for them
*  and take control of either their social media value or their financial value or whatever for
*  them. All of that is going to be made available to people in like this autonomous piece of code
*  that does the same thing that the centralized entity used to do. So they get all the features,
*  but the autonomous piece of code gives them the ability to have control while getting all the
*  features. Right. So banks give you features, social media sites give you features, you know,
*  whatever other system that you use online gives you features, and then it takes your data and it
*  takes control of your assets from you in return for those features. Right. I think the whole big
*  difference here, partly in line with the definition of smart contracts and its evolution, is that
*  there's this autonomous piece of code that's giving you all those features without requiring
*  the ownership and lock-in and control and unilateral kind of ownership of your data
*  or your value or whatever it is that you're giving it. Right. And I think what this will lead to
*  fundamentally is just more of a free market dynamic among how people make, I think with the
*  social media folks, you should just make some kind of law or something where you can just export all
*  your data from them. Everyone should be able to get their data exported by another application.
*  And then the network effect of all these social media sites will kind of crumble because people
*  will just combine your Twitter data with your Facebook data with everything else into an
*  application that you control and there will just be thousands of different interfaces competing for
*  how to consume all the social media data because it isn't locked in and one centralized actor's
*  control. And so this is just the recurring pattern of what I think all of this will do,
*  is it gives people a better deal. Right. It gives them features without ownership of data,
*  without ownership of value. And that's really the difference.
*  So I think this is a good place to talk about smart contracts then. Can you tell me the history
*  of smart contracts and the basic sort of definitions of what is it?
*  Sure. So I think smart contracts as a definition has actually gone through some kind of changes
*  or small evolution. Initially, I think it was actually a conception of a digital agreement
*  that was tamper-proof and could know things about the world. Right. So it could get proof
*  and it could define that something happened and it could conclude an outcome and release payment
*  or do something else. That's actually the definition of smart contracts that I began
*  working in this industry with seven or eight years ago when I started making smart contracts.
*  That is the conception that I had of a smart contract. Then what happened was that was really
*  hard to do. Right. Building that type of tamper-proof digital agreement that could also know things
*  about the real world and release payments back to people about those events that were codified in
*  this tamper-proof format was actually a very tall order. Turns out it's consistent of three parts.
*  It's consisting of the contract, the proof about what happened and the release of value.
*  The way things have evolved so far is that the definition has now come to mean on-chain code.
*  Right. So it's come to mean the codification of contractual agreement on a blockchain. Right.
*  So there's some code somewhere on some blockchain that defines what the agreement is.
*  Now, that eliminates the part of the definition that's related to knowing things about the world
*  and it partly eliminates the definition about payments and stuff like that. But basically
*  it's on-chain code. Right. We in our recent work on a second white paper have actually
*  put out a different definition that we call hybrid smart contracts that actually tries to go back to
*  the initial definition that I started with seven or eight years ago, which basically says that
*  there's some proof somewhere that's proven to the contract and the contract can know that
*  and the contract can gain proof. Then it can use that proof to settle the agreement that's codified
*  on a blockchain. So you both need a mechanism to provide proof. You need a mechanism to codify
*  the contract in a tamper-proof way on something like a blockchain. And then as with all contracts,
*  there's a presumption that there's some kind of release of value. So I think a smart contract
*  in our industry right now means on-chain code, which limits it to whatever can be done on-chain
*  only. And then in our internal definition for us, and for us at Chainlink and for me,
*  it's hybrid smart contracts, which is actually the original definition. It's the idea that a contract
*  can both know what happened and automatically resolve to the proper outcome based on what
*  happened. So you're referring to the Chainlink 2.0 white paper, which is a paper that I recommend
*  people look. It's a very easy read and very well structured and very thorough. So I really enjoyed
*  it. Very recently released, I guess. Can you dig in deeper? What is a hybrid smart contract?
*  You mentioned sort of this idea of data or knowing about the world and on-chain and off-chain. So
*  what are the different roles in this? So hybrid, by the way, refers to the fact that it's on-chain
*  and off-chain contracts. So maybe digging deeper of what the heck is it and what does it mean to
*  know stuff about the world? Like, how do you actually achieve that? Yeah, absolutely. So the
*  on-chain part is where the agreement itself is. That's the smart contract itself. And that's where
*  you codify certain conditions such as the conditions under which an interest payment is made or the
*  conditions under which the contract pays out the full amount that it holds to someone based on a
*  derivative outcome or something like that. Now, what the on-chain code is very good at is creating
*  transparency about what the core conditions of the contract are. It's very good at taking in money
*  from other private keys that send it tokens and send it value to hold. And then it's also very good
*  at returning money or returning value back to other addresses or other private keys. It can also
*  be involved in governance. It can be involved in a few other private key signature based
*  operations. But primarily the on-chain part of a hybrid smart contract, from what I've seen so far,
*  defines the agreement, takes in value and returns value based upon the conditions codified in the
*  agreement on a blockchain. The second and equally important off-chain part is where the term
*  an oracle comes in or an oracle mechanism or a decentralized oracle network, as we describe it
*  in the paper. And this is another decentralized computational system that has a different goal.
*  So blockchains have the goal of packaging transactions into blocks and connecting them
*  in a cryptographically unique way to create security and assurance about that chain of
*  transactions. Oracles and decentralized oracle networks achieve consensus and they achieve
*  decentralization about the topic of what happened. So blockchains structure transactions. Some of
*  those transactions might be the state changes in different pieces of on-chain code. And then those
*  on-chain pieces of code require input. I think the thing that people get a little bit thrown by
*  is despite being called smart contracts, the on-chain code on a blockchain cannot actually
*  speak to any other system. So blockchains are valuable and useful as far as they're tamper
*  proof and secure. And to be tamper proof and secure, they're made this kind of walled garden
*  that is able to know and interact only with the highly reliable information that's within that
*  system, which is basically tokens and private key signatures. All the other world's information
*  is not available in a blockchain inherently. And a smart contract or a piece of on-chain code can't
*  just say, hey, I'm going to go get some data from over here because the API they would get it from
*  creates a whole bunch of security concerns for the blockchain itself and a whole bunch of
*  consensus issues about how to agree on what that API said or what the truth of the world is,
*  because it's not even agreeing on what one API said. It's more so creating a reliable form of
*  decentralized computation that can give you a definitive proof of what happened and not just
*  what one API said. So for example, some of our most widely used networks have well over 30 nodes
*  and well over 10 data sources that are all providing information about the same type of data.
*  Then there's consensus on that one piece of data, which is then written in and essentially given
*  back into the on-chain code to tell it what happened, because you can't really make an
*  agreement unless you know what happened. If you and me were to make an agreement and set some
*  contractual conditions, but our agreement could never know what happened, it would be completely
*  useless. However, if you and me made an agreement and there was another system called an oracle
*  mechanism or decentralized oracle network that proved what happened definitively, and you and
*  me pre-agreed that whatever this mechanism says is what happened, then we can achieve an entirely
*  new level of automation. We can suddenly say there's this piece of on-chain code that's highly
*  reliable. We can give it millions, billions, eventually trillions of dollars in value,
*  and it is controlled by this other system over here that's also highly reliable under this
*  configurable set of definitive truth and decentralization conditions, which we all agree
*  are sufficiently stringent to control that much value. Therefore, the combination of this
*  tamper-proof on-chain representation of a contract and this mutually agreed upon definition of a
*  trigger or a proof system combined is a hybrid smart contract, which as you can see probably
*  already does a lot more than just a contract on-chain. Can you talk about this consensus
*  mechanism, which by the way is just fascinating. So there is the on-chain consensus mechanism of
*  proof of work and proof of stake, and then there is this oracle network consensus mechanism of
*  what is true. So how do you, can you compare the two? How do you achieve that kind of consensus?
*  How do you achieve security in integrating data about the world in a way that's definitively true,
*  in a way that is usefully true such that we can rely on it in making major agreements that,
*  as you said, involve billions of trillions of dollars?
*  Right. So this is the challenging question, right? This is the challenging
*  problem that oracle networks, oracles, we at Chainlink that we work on in order to create
*  this definitive truth to trigger and create hyper automation in this more advanced form,
*  more advanced form of hybrid smart contracts. The reality I think of this problem is that it is
*  very specific to each use case. And this is actually how we've architected our system,
*  is in a very flexible way. So for example, you need an ability for an oracle network to grow
*  in the amount of nodes that it has relative to the value it secures, right? So if you have an
*  oracle network that secures $100,000 in like a beta of a financial product, maybe it can be fine
*  with only seven nodes and only two or three data sources, right? Because the risk to that
*  oracle network is relatively low based on the value it secures.
*  So the first question is actually how do you scale security relative to value
*  secured by that oracle network? Because it wouldn't be very efficient to have
*  a thousand nodes securing $100,000 worth of value. So one of the first questions is
*  how do we properly scale and how do we compose ensembles of nodes in a decentralized way where
*  we can know that, okay, we're going from seven nodes in a network to 15, to 31, to 57, to 105,
*  to 1,000, right? So that's one dimension of the problem.
*  So you have to be scaling the number of nodes relative to the value that's
*  derived from the truth integrated into those nodes.
*  Well, that's not the only problem, right? The other side of this is that you're trying to create
*  a deterministic result, a deterministic output from a set of non-deterministic disparate systems,
*  data sources, or places that prove things. Can you also just as a side, what is an oracle
*  node? What is the role of an oracle node? Sure. So an oracle node essentially exists
*  in both places. It exists in both worlds. It exists as an on-chain contract that represents
*  either an oracle network or an oracle node. So there's an on-chain interface in the form of
*  a contract that says, I exist to give you this list of inputs. You can request weather data for me.
*  You can request price data for me. You can ask me to send the payment somewhere.
*  Like an API. So it's a pointer to API that provides truth about this world.
*  By data. It's an interface. So just like an API is an interface for web 2.0 engineers,
*  oracle networks and the contracts that represent them or individual nodes are the interface of web
*  3.0's use of services. And services includes all services. Data, payment systems, messaging systems,
*  whatever web 2.0 or any kind of computing service that you can conceptualize needs an interface
*  on chain in the form of a contract that says, here are the services I can provide for you. Here
*  are the transactions you need to send me to get back this data or that computation or this result.
*  And then what you actually see is that decentralized oracle networks, because they're
*  uniquely capable of generating their own computations in a decentralized way around the
*  data that they have access to, you actually see decentralized oracle networks generating a lot of
*  these services. So for example, we have a randomness service, a verifiable randomness
*  function service that basically provides randomness on chain. And that randomness is then used in
*  lotteries and various other contracts that need randomness. But that randomness, it's not a piece
*  of data that comes from somewhere else. We don't go to another data source and get it. We generate
*  it within an oracle node that then provides it over into oracle node or oracle nodes that provide
*  it into the contracts themselves. So why do you say oracle nodes are non-deterministic?
*  Well, they are as far as they come to consensus, but they're true. See, there's this kind of
*  different problem here, right? The blockchains are very focused on generating blocks of transactions
*  within a smaller universe of transaction types, a certain block size and a certain set of conditions.
*  And then they have an economic system that says, I will perpetually generate blocks of this size,
*  with these transaction types in this kind of limited set of transaction types, whether those
*  are UTXO transactions or scripted, Solidi or whatever it is. Oracles and oracle networks,
*  we don't have a blockchain, for example. There is no chain link blockchain. Our goal is not
*  to generate a certain set of very clearly predetermined transaction types into a set
*  of transactions that are put into blocks and will infinitely be done that way. Our goal is actually
*  to create what we call a meta layer, a decentralized meta layer between the non-deterministic,
*  highly unreliable world and the highly hyper reliable world of blockchains so that the
*  unreliable world can be passed through this decentralized meta layer.
*  It can coexist with the reliable on-chain world.
*  Exactly. It can coexist and in some cases the meta layer might generate it.
*  The problem in giving you this straight answer is that there's just such a wide array of services.
*  If you were to say, well, Sergey, how do we generate randomness from a data source? Well,
*  we don't use a data source to generate the randomness. That's the type of service that
*  can be generated in an oracle network itself. There will be certain computations that oracle
*  networks themselves generate themselves to augment and improve blockchains.
*  Got it.
*  And it is actually the goal of oracles to consistently do that. If you were to think about
*  the stack in a very generic high level, you would see blockchains are databases. They're
*  basically the data structures that retain a lot of information in this transparent,
*  highly reliable form. Smart contract code is the application logic. It is the logic under which all
*  of this kind of activity occurs, storing data in the data structure in the blockchain as a database
*  in a certain conceptualization of it. And then oracles and oracle networks
*  are all the services that are used by the application code. So by analogy, let's take
*  Uber. Uber initially, some core code goes and gets the GPS API from Google Maps about the user's
*  location, sends a message to the user through Twilio, pays the driver through Stripe.
*  If those services weren't available to the people who made Uber, they wouldn't have made Uber,
*  right? Because they would have written their core code on some database and then they would
*  have had to make a geolocation company, a telecom messaging company, and the global payments company.
*  And they wouldn't have done that because it's too hard. And that's the weird scenario that a lot of
*  people in our industry are in. And that's the problem that oracles and oracle networks fix,
*  is they provide these decentralized services to take this developer ecosystem, the blockchain
*  and smart contract developer ecosystem from, hey, I can have a database and write some application
*  logic about tokenization and voting and private key signing, all of which is super useful and is a
*  critical foundation. But now if you just layer on all the world's services, whether that's market
*  data, weather data, randomness, suddenly people can build DeFi, fraud proof gaming, fraud proof
*  global trade, fraud proof ad networks. And that's why this world of decentralized services and
*  decentralized oracle networks is particularly, in my opinion, important to our industry.
*  Yeah, it's funny. And you talk about that the current sort of decentralized world,
*  DeFi, but decentralized services world is primarily just tokens. And it's basically
*  just financial transactions. And the kind of thing, the reason why it's super exciting,
*  the kind of thing you're doing with chain link and oracle networks is that you can basically
*  open up the whole world of services to this kind of decentralized smart contract world.
*  I mean, you're talking about just orders of magnitude, greater impact financially and just
*  socially and philosophically. Are there interesting near term and long term applications that excite
*  you? Yeah, there's a lot that excites me. And that is how I think about it, that it's not just about
*  we made a decentralized oracle network. It's about we made a decentralized service or collection of
*  services that's going from hundreds to thousands. And then people are able to build the hybrid
*  smart contracts, which I think will redefine what our industry is about. Because for example,
*  for the people that only learned about blockchains through the lens of NFTs,
*  they understand blockchains through NFTs, not through speculative tokens or bitcoins.
*  Right? And I think that will continue. I think the use cases that excite me, they vary between
*  the developed market, the developed world's economies and emerging markets. I think in the
*  developed world, what you will see is that transparency, creating a new level of information
*  for how markets work and the risk that is in markets and kind of the dynamics that put
*  the global financial system at systemic financial risk like 2008. And my hope is that all of this
*  infrastructure will soften the boom and bust cycles by making information immediately available
*  to all market participants, which is by the way, what all market participants want, except for the
*  very, very, very small minority that are able to game the system and their benefit and benefit
*  from booms but avoid busts because of their asymmetric access to information, which really
*  everybody should have and which this technically solves. I think in the process of doing that,
*  which is happening I think right about now, you see a polishing of the technology such that it
*  can be made available to emerging markets. And on a personal level, I feel that the emerging markets
*  will benefit much more from this technology, just like the emerging markets benefit much more from
*  the internet or from those $50 Android phones that people can have because it's such a massive shift
*  in how people's lives work. I have always had access to books and a library, which has been
*  fantastic and very important. But there are places in the world where people don't have libraries,
*  but now they have the internet and a $50 Android phone and they can watch the same Stanford lecture
*  that I watch. I mean, that's kind of mind blowing realistically, right? They just went from zero to
*  one in a very, very dramatic way. I think all of these smart contracts, and in my case, I think the
*  one that I seem to keep coming back to is crop insurance, where partly because it doesn't have a
*  tokenization component, partly because it's actually much more important than it might seem.
*  RG What is crop insurance?
*  RS Right. So this is the nature of why it's sometimes hard to see the full value of what
*  our industry does because it solves all these kinds of back end problems that we don't have.
*  Crop insurance is if I own a farm and it doesn't rain, I get an insurance payout, so I don't need
*  to close down my farm because if it didn't rain, I don't have crops. So people in the developed
*  world can get crop insurance and there's all kinds of systems that basically pay them out and then
*  they can argue with the insurance company if they don't get paid out properly and whatever.
*  And this allows people to smooth out risk. In fact, a lot of the global options markets
*  were about this. They were initially about people selling their produce or their crops
*  ahead of time so that if there was a risk of drought, they weren't impacted by it.
*  And that's where a lot of options trading and all this kind of stuff came from,
*  even though it's now turned into this kind of global casino. But in the emerging market,
*  there are literally people that if they don't have rain for two seasons, they need to close
*  down their farm and become a migrant worker of some kind. And now they have a $50 Android phone
*  where they can read Wikipedia, but they're still decades away from an insurance company coming to
*  their geography and offering them insurance because their local legal system simply doesn't
*  allow that type of thing to exist. No insurance company is going to go and create an insurance
*  entity and offer them insurance because the levels of fraud and the ability to resolve that fraud
*  through courts would just not exist. So now these people have to wait for decades to have this very
*  basic form of financial protection or something like a bank account even. And with this technology,
*  they don't. So with this technology, if I have a $50 Android phone and the smart contract has data
*  from satellites or weather stations about the weather conditions in the geography that my
*  farm is in, I can put value into the smart contract and the smart contract will automatically pay me
*  out, pay me back out at my Android phone. And guess what? I just leapfrogged past my corrupt
*  government not being able to provide a legal infrastructure to create insurance. I just
*  leapfrogged past dealing with insurance companies that will probably price gouge me and often not
*  pay out. And I leapfrogged into the world of hyper reliable, guaranteed smart contract outcomes that
*  are as good or in many cases better than what farmers in other parts of the world have.
*  And this type of dynamic for the emerging markets of creating a way for people to control
*  and manage risk in their economic life, I think extends way past insurance. It extends to them
*  having bank accounts to combat local inflation. It extends to them being able to sell their goods
*  on the global free market of global trade without middlemen. It extends to all these things that we
*  don't really care about because we're not farmers, but are unbelievably impactful for people that
*  don't have a bank account and their inflation rate in their country is double digits,
*  or their farm completely depends on rain, or their livelihood completely depends on their ability to
*  sell goods. And they can't sell those goods because there's a middleman who essentially
*  controls all the trust relationships. But now we have the internet and smart contracts and that
*  might not have to be the case in the next five or 10 years. Yeah. So that definitely has a quality
*  of life impact on the particular farmer's life, but I suspect it has a huge like down the line
*  ripple effect on the whole supply chain. So if you think about farmers, but any other
*  people that produce things that are part of a large like logistics network, like supply chain
*  network, that means when you increase reliability, you sort of increase transparency and control,
*  but like where anyone node in that supply chain network can formalize the way it operates
*  in its agreements with others, then you could just have a very like at scale transformative
*  effect on how people that down the line use the services that you provide, the products that you
*  create operate. So like, it's almost hard to imagine the possible ways it might transform the world.
*  I wonder how much friction there is in the system, I guess, currently that smart contracts might
*  remove. That's almost unknown. You can sort of hypothesize and stuff, but I wonder. I think
*  I've seen enough bureaucracy in my world, in my life to know that smart contracts in many cases
*  would remove bureaucracy. And I wonder how the world will be once you remove much of the bureaucracy
*  coming from the Soviet Union, where I just has seen the life sucked out of the innovative spirit
*  and nature by bureaucracy. I wonder, you know, the kind of amazing world that could be created
*  once bureaucracy is removed. Yeah, I think it's I think it's fascinating how the world can evolve.
*  I think this extends a lot further than people think into many, many different parts of the
*  global economy. It might start with NFTs for art, or it might start with DeFi, right, or it might
*  start with fraud proof ad networks. Next, we don't know what it's going to go to next.
*  But I think the implication of people being in a system of contracts that holds them accountable
*  and guarantees contractual outcomes, regardless of a local legal system, is something that I think
*  extends to the supply chain, you can prove that goods were sourced in an ethical way. And you
*  can prove that in a way that can't be gamed. That'll change buying power and supplier power
*  and how people produce goods that we all consume. And then on the political level,
*  I personally think that in a number of decades, we could literally be in a place where politicians
*  can commit to a certain set of smart contract, kind of budget, definitional kind of results.
*  For example, you know, we discovered oil, I promised as a politician, I'm going to take the oil
*  and I'm going to redistribute it to all of you. Well, that's wonderful. That's a great idea.
*  Sounds very nice when you're running for office. Why don't we codify that in a smart contract?
*  And why don't we put those conditions very solidly on a blockchain? And then once you've been
*  elected, we'll just turn that one on and it'll distribute the money just like you said, and
*  everything will be fine. I personally think that this new level of systems that allows trustworthy
*  collaboration between everybody, between supply chain partners, ad network users, the financial
*  system, insurance companies and farmers. All of these are just interactions that require a trusted
*  entity or in this case, a trusted piece of code to orchestrate the interaction in the way that
*  everyone agrees. Yeah. One of the things that makes the United States fascinating is the
*  founding documents. And it's fascinating to think of us moving into the new in the 21st century to a
*  digital version of that. So the constitution, a smart constitution, no offense to the paper
*  constitution, but, and I would change that would have transformative effects on politicians and
*  governments holding people accountable. Oh man. That's so, that's so exciting to think that
*  we might enforce accountability through the smart contract process.
*  Exactly. Why can't that happen? And anything that we could codify into a smart contract
*  and anything that we all agree is the way the world should work. And then anything that we
*  can get proof about, right? Anything that a system somewhere could tell us happened,
*  those are the pieces of the puzzle, right? We need a trusted piece of code. We need to have agreement
*  that that's how the world should work. And we need a system that'll tell that trusted piece of code,
*  what happened. As long as we have those three things, we can theoretically codify any set of
*  agreements about anything where those three properties take hold. I wonder if you can apply
*  that to like military conflict and so on. Recently, the Biden announced that we're going to pull off
*  from Afghanistan after 20 years in the war. I wonder, there's a lot of debacles around
*  war in Afghanistan and invasion of Iraq, all those kinds of things. I wonder if that was
*  instead formulated as a smart contract. That might have actually huge impact on the way we do
*  conflict. So you think of a smart contract as a kind of win-win situation where you're doing
*  financial transactions or something like that. But you could see that also about military conflict
*  or whenever two nations are at tension with each other, different scales of conflict,
*  that you could have conflict codified. And that would potentially resolve conflict much faster
*  because there's honesty, transparency, and control within that conflict because there's
*  conflict in this world. And again, very, very inspiring to think about the kind of effects it
*  might have on the negative kinds of contracts, on the tense, painful kinds of contracts.
*  RG I haven't thought about that as much as actually kind of scary the stuff you're
*  thinking through now with like the war contracts or something. That's not in the white paper. We
*  don't have anything about war contracts or anything. JS Again, this is the Russian,
*  we're both Russian, but I'm a little more Russian in the suffering side. Maybe I read way too much
*  Dostoevsky and military kind of ideas. But anyway, holding politicians accountable in all forms,
*  I think is really powerful. Is there something you could say as a small side on how smart contracts
*  actually work? If we look at the code, is there some nice way to say, technically, what is a smart
*  contract? What does it mean to codify these agreements, the actual process for people who
*  might not at all be familiar? RG I think you just write it into code that operates in this kind of
*  decentralized infrastructure. You usually write code that runs in a central server somewhere.
*  Now you write code that runs across a lot of different machines in this decentralized way.
*  And then after you write it, you need services. And that's where oracles come in, they provide
*  all the services. So just like you would be writing code in Web 2.0 land, running it on a
*  server somewhere and using an API. Here you'd be writing code, putting it on a decentralized
*  infrastructure like a blockchain, or a smart contract platform like Ethereum. And then you
*  would be using various services in the form of oracles. So they'll just be called oracles or
*  decentralized services instead of APIs. And you're basically composing the same type of architecture,
*  except it's hyper reliable. At the moment, it's a little bit less efficient because there's an
*  early stage to our industry. But it provides this extreme level of reliability and transparency,
*  which for certain use cases is an absolute critical component, and is completely reinventing how they
*  work. So I think people should look at what are the use cases where that trust dynamic can be so
*  heavily improved. And that's probably the ones where this is maybe initially useful.
*  RG But I mean, just to emphasize, I don't think people realize when you say code, that we're
*  talking about non obfuscated, actual program, like you can read it, you can understand it.
*  Yeah. And it's there's something about maybe this is my computer science perspective of
*  like software engineering perspective. But there's something about the formalism of programming
*  languages, which enforces simplicity, clarity and transparency. And because it's seen to everybody,
*  I mean, simplicity is enforced. There's no there's something about natural language,
*  like language, as written in the Constitution, for example, where there's so many interpretations
*  with the nice thing about programs, there's no, there's not going to be a huge number of books
*  written about what was meant by this particular line, because it's pretty clear. Like programming
*  languages have a clarity to them that natural language does not. And they don't have ambiguity,
*  which I think it's important to pause on because it's really powerful. It's really difficult to
*  think about. I think we live in a world where all the philosophers and legal minds don't know how
*  to program. So I think not all most don't. And so we don't often see the philosophical impact of
*  this kind of idea that the agreements between humans can be written in a programming language.
*  That's a really transformative idea. That I mean, yeah, it's, it's, it's an idea that's not just
*  technical. It's not just financial. It's philosophical. It's rethinking human nature
*  from a digital perspective. The like, what is human civilization, its interaction between humans.
*  And rethinking that interaction as a digital interaction that is managed by programming
*  languages, by programs, by code. I mean, that's, that's fascinating that we'll look back at this
*  time potentially as one where us little descendants of apes did not realize how, how trans, how
*  important this moment in history is. Like human beings might be totally different.
*  A century from now, because we codified the interaction between humans, that might have
*  more of an impact than anything else we do today. You think about the impact of the internet. One of
*  the cool things is digitization of data, but we have not yet integrated the tools, the mechanisms
*  fully that use that data and interact with humans yet. And that's what smart contracts do.
*  I wonder if you think about the role of artificial intelligence in all of this,
*  because your smart contracts are kind of agreements. Maybe you disagree with this,
*  but at least the way I'm thinking about it is agreements between humans or groups of humans.
*  But it seems like because everything's operating in the digital space that you can integrate
*  non-humans into this or AI systems that help out humans, managed by humans. Like, what do you think
*  about a world of hybrid smart contracts codifying agreements between hybrid intelligent being networks
*  of humans and AI systems?
*  Yeah, I think that's a great question. I think that's a great question. I think that's a great
*  hybrid intelligent being networks of humans and AI systems.
*  Yeah, I think that makes perfect sense. In terms of AI, I'm not an expert, so it might be a bit
*  simplistic or naive, my ideas in this field. I think everyone saw the Terminator movie.
*  Everybody kind of saw the Terminator movie in the 90s, and it was like, this is really scary. I
*  personally think AI is amazing. It makes perfect sense. I think it will evolve to a place where
*  people have... Just to understand, I work in the world of trust issues. I work in the world of,
*  how can technology solve trust and collaboration issues using encryption, using cryptographically
*  guaranteed systems, using decentralized infrastructure? So that's the world that
*  I've been inhabiting for many, many years now, building smart contracts for 7Rate,
*  doing stuff before that. It's kind of what I'm focused on. So I view AI through that same lens,
*  and my brain naturally asks, well, what is the trust issue that people might have with AI?
*  And my natural kind of response is, well, let's say AI continues to be built and improve. At some
*  point, I have no clue where we are on this now. I've seen different ideas that were very far from
*  this. I've seen other ideas very close to this. At a certain point, we'd arrive at a place with AI
*  where we would be a little bit worried about just how much it could do. We might be worried
*  that AI could do things we don't want it to do, but we still want to give AI a level of control
*  over our lives. So in my world, that's a trust issue. And the way that that trust issue would
*  be solved with blockchains is actually very straightforward and I think in its simplicity,
*  quite powerful. You could have an AI that has an ability to do and control key parts of your and
*  our lives, right? But then you could limit it with private keys and blockchains and create certain
*  guardrails and firm kind of walls and limits to what the AI could never go past, assuming that
*  encryption continues to work. And assuming that if it's not that AI's specialization to break
*  encryption, that it wouldn't be able to do that. So if you have an AI that controls something very
*  important, whatever it is, shipping or something in defense or something in the financial system,
*  whatever it is, but you're sitting there and you're kind of worried, hey, this thing is
*  unbelievable. It's coming up with things we wouldn't have thought of in a hundred years,
*  but maybe it's a little too unbelievable. How do you limit it? Well, if you bake in private keys
*  and you bake in these kind of blockchain-based limitations, you can create the conditions
*  beyond which an AI could never act. And those could once again be codified in the very specific,
*  unambiguous terms in which you described, which once again, in my trust issue-focused world,
*  would solve the trust issue for users and make them comfortable with using the AI or
*  ceding control to the AI, which I think in more advanced versions of AI will continue to be a
*  concern. This is fascinating. So smart contracts actually provide a mechanism for human supervision
*  of AI systems. With encryption, very encryption heavy. So it's not about like, is it smarter than
*  us? It's about will the encryption hold up? Yep. So that's based on the assumption that
*  encryption holds up. I think that's a safe assumption. We can get into that whole discussion,
*  but from quantum computing, but cracking encryption is very difficult. That's a whole
*  another discussion. I think we're safe on the safe ground for quite a long time, assuming encryption
*  holds. There's a space that is at the cutting edge of general intelligence research in the
*  AI community, which is the space of program synthesis or AI generating programs. So that's
*  different than what you're referring to is AI being able to generate smart contracts.
*  Mm-hmm. And that to me is kind of fascinating to think of, especially two AI systems between
*  each other, generating contracts, sort of almost creating a world where most of the contracts are
*  between non-human beings. I think an AI system as I think about it, and once again, this is not my
*  field. This is something I might watch a YouTube video on or just see something interesting about
*  at some point. I think if I were to just reason through it even now, I think the highly deterministic
*  and guaranteed nature of smart contracts would probably be preferable to an AI because I'm
*  guessing an AI would have a lot of problems with dealing with the human element of how contracts
*  work today. So an AI, for example, couldn't pick up the phone and call Dave at a bank to do a
*  derivative and kind of discuss with Dave and have a call with him and kind of have a conversation
*  and get him comfortable and tell him it's going to be fine and kind of smooth out all the weird
*  social cues that have to do with making certain derivatives. I'm assuming that that's a pretty
*  complicated neural map AI kind of problem. Yeah, so if I think about it, the deterministic guaranteed
*  nature of smart contracts probably would, and assuming they're accessible to AIs,
*  could actually, interestingly enough, be the format that they prefer to codify their relationship
*  with non-AI systems and very possibly other AI systems because it is very,
*  I mean, it's pretty guaranteed all the other types of contracts that an AI could go out there
*  and seek to do would require some language processing around the law.
*  And I think, I don't know if this is a term, but probably not, a smart AI or a good AI or whatever
*  the term is for a high quality AI would probably realize some of the limitations and the risks.
*  Yeah, AI definitely dislikes ambiguity or would prefer the deterministic nature of smart contracts.
*  I do wonder about this particular problem and maybe you could speak to it of how smart contracts
*  can take over certain industries in a sense, or how certain industries can convert their sets
*  of agreements into smart contracts, which is, you mentioned, so we're talking to Dave from the bank,
*  many of our laws, many of our agreements are currently through natural language, through words.
*  And so there is a process of mapping that has to occur in order to convert the legal agreements,
*  legal contracts of today to smart contracts that by the way, AI may be able to help with.
*  But by way of question, how do you think we convert the legal contracts on which many
*  industries currently function today, or not even legal contracts, but ambiguous kind of agreements,
*  they're loose sometimes into more formal deterministic agreements that are represented
*  by smart contracts? So I think there's two, maybe two sides to this. I think the first one is
*  actually not a huge problem where you have things like the is the master agreement for derivatives,
*  or you have these agreements that basically already reference a system somewhere, right?
*  Like for example, many legal agreements already accept e-signature. And so they're saying,
*  hey, I'm going to use this computing system over here around signatures, and there's laws around
*  that, and there's clauses that say e-signature is good enough for this agreement. I actually don't
*  think this is a big problem for the vast majority of legal agreements that use systems already,
*  right? So what you'll do is you'll swap out one repository or one set of system of contract
*  settlement. And you'll just say, hey, this blockchain system over here is my new system
*  of contract settlement. Whatever it says is the state of the agreement instead of the centralized
*  system over there, right? And so there's actually a huge amount of agreements that are already
*  able to do that, and I think we'll do that. I think there's another side to your question,
*  which is the amount of agreements that are very ambiguous that can be turned into smart contracts.
*  And I think the limitation there is twofold. First of all, like you said earlier,
*  the highly reliable smart contract and the lack of opaqueness and the clarity of smart contracts
*  is very high and very powerful and very clear. And it's, in my opinion, going to be much,
*  much easier to take a smart contract and turn it into a set of natural language explanations
*  and just say, hey, this is what this does, right? So I think that many contracts are,
*  and even now in decentralized finance and DeFi and in decentralized insurance, they're basically
*  being rebuilt in this format. And that rebuilding will make them clearer, like you said, and then
*  restating those in natural language and explaining to people, well, you know, whether it is this,
*  I think it'll actually be a lot simpler to explain to people what the contract is about.
*  Especially mapping smart contracts, it's a natural language. I didn't even think about that. So
*  you're saying that's doable and natural and easy to do.
*  Because there's so much clear, right? There's that forced clarity that you talked about.
*  I think the second aspect of this problem is the nuance around what contracts can be made
*  unambiguous. And I think that often comes down to proving what happened, which is where Oracle
*  networks and decentralized Oracle networks and Chainlink would come in. And our experience there
*  is quite extensive over the many years that we've worked on many different contract types.
*  I think what it fundamentally comes down to is whether there is data. So we're not going to be
*  able to make a hybrid smart contract about whether somebody painted your house the right color blue.
*  We're just not going to be doing that because there's no data feed that tells us that your
*  house was painted blue or that it was the right color of blue. You know, unless somebody sets up
*  a drone with a color analysis tool and they generate that data. Which by the way, could be
*  possible, right? If there's enough demand, then the service would be created that has drones flying
*  around that's telling you about the colors of all this kind of stuff. So if there's actual demand,
*  that that would be created. And because there'd be value to connect that data feed to the smart
*  contracts and so on. I think you have it unbelievably right because there are already
*  insurance companies that use drones to monitor construction sites from overhead and see how many
*  people are wearing hard hats. And if the percentage of people wearing hard hats isn't
*  sufficiently high, then the policy is voided. And so in that case, there is a data source and
*  that data source can be put into a hybrid smart contract. So the limitation of hybrid smart
*  contracts is, is there a data source or a set of data sources to create definitive truth,
*  to settle the contract and eliminate ambiguity? And then as you said, I think as people realize
*  that smart contracts are a format in which they can form agreement about things like that
*  insurance product around, you know, how many people are wearing hard hats. If I'm the construction
*  site owner, well, you know, I would really like a guarantee that your insurance policy is going to
*  pay me out if everyone is wearing hard hats. And in that case, there is demand for the data and
*  people will generate the data. And I actually think the insurance industry is interestingly
*  a precursor of this because they're so data driven. You already see insurance companies
*  paying IoT companies to put data into their customers' infrastructure at the cost of the
*  insurance company to generate the data that the insurance company uses to make a policy for the
*  customer. So you basically already have people who really want to price data into their agreements
*  when they're of sufficiently high value, paying for their own customers to get data sensors into
*  their infrastructure. And I think as smart contracts become more of a requested format
*  or data driven contracts become more of a format, there will be a growing demand about proving what
*  happened through data. So it'll be motivating, totally new data feeds being created. By the way,
*  the insurance industry broadly, the revolutions there will be huge. I've worked quite a bit with
*  autonomous vehicles, semi-autonomous and just vehicles in general. The insurance industry
*  there, by the way, makes a huge amount of money, but is using very crappy data feeds,
*  revolutionizing how, like not by crappy, I mean very crude. Like literally the insurance is based
*  on things like age, basic demographic information as opposed to really high resolution information
*  about you as an individual, which you may or may not want to provide. So you can choose from an
*  individual perspective to provide a data feed. And there, the power of insurance
*  to enable the individual, to empower the individual could be huge because ultimately smart contracts
*  motivate the use of data, the creation of new data feeds, but leveraging the whatever service it provides
*  in truth, as opposed to some kind of very loose notion of who you are. So that, again, not sure
*  how that would change things in terms of the fundamental experience of life, because I think
*  we all rely on insurance, not just in business, but in life. And grounding that insurance in more and
*  more accurate representation of reality might just have transformative effects on society.
*  Well, just to mention one quick thing that you said, where I noticed another trust issue,
*  you said the user might not want to share their data. So what you could actually do,
*  and what we've already worked on is you can have a smart contract that holds the data and evaluates
*  the data of the user without sharing it with the insurance companies. And the insurance company
*  knows that the smart contract will evaluate it according to the policy, so they don't need the
*  data. And the user can provide the data knowing it'll never touch the insurance company because
*  it's only provided to the smart contract. And suddenly you've solved another trust issue,
*  because an autonomous piece of code can evaluate information separately from the interests of both
*  of the counterparties. And so this is the recurring theme. I think you're seeing this recurring theme
*  where there's a trust issue, people can't use a system, they can't collaborate, they can't share
*  information that would make a better agreement for both of them. They can't solve a risk in their
*  daily life, they can't participate in a market, they can't have a bank account because nobody
*  will give it to them because they can't give it to them in that legal system. And once you have
*  an autonomous piece of code that can also know what's going on, thanks to Oracle networks and
*  that combination of the code and the Oracle network for the hybrid smart contract, the same
*  pattern just recurs. It's really the same pattern. And this is why I keep saying trust issues, it's
*  because basically almost every contractual trust issue that I see where there is a piece of data
*  to prove and settle the trust issue in a way that works for both parties, there is no reason not to
*  use an autonomous, highly reliable contract and piece of code. And I have to tell you, I've seen
*  this in a lot of different industries. I've seen it insurance, ad networks, global finance, global
*  trade, those are all multi-trillion dollar industries. And then there are other smaller
*  industries. Even one of the first smart contracts we worked on many years ago was for search engine
*  optimization firms, where they would tell you, hey, I'm going to raise your search engine ranking,
*  give me the money. And people wouldn't want to give them the money because they never knew if they
*  were going to do it. And then the search engine firm doesn't want to do any work thinking they'll
*  never get any money. So we just initially even came up with a system where you could put Bitcoin
*  into a smart contract and it would be released based on whether the search rank of a website
*  got to a certain level on Google for a certain keyword. And so the trust problem was solved.
*  But it's just the same story. It's kind of like trust issues around AI, trust issues around
*  financial products, trust issues around insurance, trust issues around social media, whatever it is.
*  I think that's what people looking at this industry really need to understand. And once
*  they do understand, they realize what this is all about. This is about redefining how everyone
*  collaborates with everyone about everything, where we can prove something through data.
*  You've mentioned confidentiality and privacy, that you don't, the parties don't need to necessarily
*  know private data in this interaction. You talk about confidentiality in the white paper for
*  Chainlink 2.0. Can you talk more about how to achieve confidentiality in this process?
*  Sure, sure. Absolutely. So I think you once again need to think of the contract as existing in two
*  parts. You have the on-chain code and then you have this off-chain system called the centralized
*  Oracle network. So the question is really what portion of the contract should live in what part
*  of these two systems? So if you want to create transparency, you should put more information
*  on chain because that's what blockchains are very good at. They're public, transparent,
*  but they don't necessarily have privacy. Well, you can see how those two things are a little bit
*  completely diametrically opposed. So I do think and I do see blockchains working on on-chain
*  encrypted smart contracts. That's very inefficient. It has a lot of nuances around it.
*  That I think will appear at some point. I think until it appears, you have an option of taking
*  a part of the computation and putting it into the centralized Oracle network. We actually did an
*  entire paper about this that we presented at Stanford in February of last year, something
*  called Mixicles, which basically talks about how you can take an Oracle network and you can put
*  a portion of the computation into the Oracle network, assuming that you're comfortable with
*  that limited set of nodes, knowing what the computation is. And you can actually provide
*  additional confidentiality through special hardware called trusted execution environments
*  that all those nodes are forced to run so they won't even know what they're operating.
*  And so at the end of the day, if you look at a hybrid smart contract as gaining functionality
*  from its on-chain code and gaining other functionality from its off-chain decentralized
*  Oracle network component, you can place the part of the computation that you would like to be private
*  in the decentralized Oracle network because you can control the set of nodes, you can control the
*  committee of nodes, and you can require that they run certain hardware to keep the information
*  private. So you could basically make a derivative or a binary option as the example used in the
*  Mixicles paper where the payout happened on chain, but it was actually impossible to tell what the
*  outcome of the contract was. So the outcome of the contract was computed in the decentralized
*  Oracle network, and then there was a switch that triggered who received the payment,
*  but from the point of view of analyzing the on-chain transactions and seeing who received
*  the payment or what the outcome of the contract was, you couldn't derive that, you couldn't
*  backward engineer what that was, but the users of that hybrid smart contract still had on-chain code
*  that guaranteed them that as long as the decentralized Oracle network found a certain
*  outcome, determined a certain outcome, that the relevant user would get paid,
*  and there was still a place to put value. So there is this kind of fundamental tension
*  between confidentiality, privacy, which is very important for many contracts, which is critical
*  to many contracts, and the public and transparent nature of blockchains, which I think eventually
*  will be solved through encrypted on-chain smart contracts. That'll take some time,
*  I think that'll take years in my opinion, and before we arrive there, I think people will put
*  the private portion into the centralized Oracle network. Once again, going back to what the
*  decentralized Oracle networks do, they seek to provide these services. So the ability to do
*  a privacy preserving computation is perhaps a service without which a certain type of contract
*  might never come into existence in the form of an on-chain hybrid smart contract. And so this is,
*  once again, what we see the centralized Oracle networks and decentralized services doing
*  is providing people these tools and building blocks to compose, like, I'm great at making
*  these derivatives contracts, but I can't make them unless I can retain the privacy of them.
*  And our goal is to provide the infrastructure that gives you as a developer and as a creator
*  of smart contracts that capability. And what we've seen is that as we provide that capability,
*  people create more, which is also really the story of the internet. The story of the internet is,
*  it was really tough to do e-commerce while everything was in HTTP and credit cards were
*  transmitted publicly. And so e-commerce was kind of tough because how am I going to send my credit
*  card over public on encrypted channels? But the second HTTPS appears, e-commerce becomes a lot
*  easier because I can put in my credit card number and it can be sent over an encrypted channel,
*  and it's not at risk. And so I can participate in e-commerce as long as I have a credit card.
*  I think those types and I'm sure that was unexpected, right? I'm sure at the time that
*  was an unexpected outcome from that technology. And so I think this is why we sometimes have this
*  focus on privacy, because in our work with contracts and their transition into this hybrid
*  smart contract form, we see a substantial amount of need for privacy as an inherent property of
*  these contracts. And it'll take a while before that's possible to create the kind of technology
*  innovation required to do that on chain. I know there's a few ideas that are being floating about,
*  but so the currently distributed Oracle networks provide that feature, which is essential to many
*  contracts. What brings to mind in this whole space, again, it might be outside of your
*  expertise, but within the world which I'm passionate about, which is machine learning,
*  and it seems like very naturally, because current machine learning systems are very data hungry,
*  and much of the value mined by companies in the digital space are from data. They often
*  want their data to maintain privacy. So you think about an autonomous vehicle space,
*  Tesla is collecting a huge amount of data, Waymo is collecting a huge amount of data.
*  It seems like it would be very beneficial to form contracts where one could use the data from
*  the other in some kind of privacy preserving way, but also where all the uses of data are
*  codified and you can exchange value cleanly, basically contracts over data, over
*  machine learning systems use of different data. I don't know, do you talk to machine learning
*  folks that use ideas as smart contracts, or is that outside of your interest? Because it seems like
*  exceptionally applicable set of... When we talk about different services that might be created
*  and revolutionized by smart, especially hybrid smart contracts, I think machine learning systems
*  comes to mind to me in all industries. I don't know if you've gotten a chance to interact with
*  those folks, with those services. I think what you're talking about is more data marketplaces.
*  In the data marketplace side of things, well, this is actually once again very applicable
*  because there's a trust issue. At the end of the day, let's say I'm trying to sell you some data.
*  You don't know the quality of the data, so you don't know what you want to pay for it.
*  And I can't give you the data for you to determine the quality because I've given you the data.
*  Guess what? We need an autonomous, impartial agent. We need an impartial, computational kind
*  of agent, an on-chain smart contract with an Oracle network to assess my data, to basically take
*  random cross-section samples of the data, assess it for quality, assess it for signal
*  from the algorithm you have, which you don't want to share with me because you don't want to know
*  the algorithm you're working on. You don't want me to know what you want the data for.
*  So now the autonomous agent takes your algorithm, keeping it private from me, and takes my data,
*  keeping it private from you, assesses it on a random cross-section sampling for quality of data,
*  returns the scoring back to you, allows you to determine a price, and now both you and me know
*  that we have arrived at a fair price for the quality of my data for what you want to do with it.
*  And that's once again, from what I've seen in the data marketplaces, which are full of people who
*  want that data for these learning models, often for financial markets, often for other reasons,
*  this is their fundamental problem, which, amazingly enough, there's a trust issue that is
*  getting solved. And I think you can see even on the face of it, once that trust issue is solved,
*  those markets can work a lot better. I don't need to know your algorithm. You don't need to
*  know my data. We both know that the autonomous agent is not under either of our control and gave
*  us a fair assessment and a fair price. And that's it. And we're all very comfortable with that.
*  I could even make conditions that your algorithm isn't analyzing the data for something I don't
*  want you to analyze it for. Or you could make conditions that the data has to have any number
*  of properties. And once again, you haven't leaked any signal to me, and I haven't leaked any data to
*  you, which is, once again, just another type of trust issue that all of this solves. So it's the
*  same pattern. If you work in this industry long enough, or if you really look at these use cases
*  long enough, you'll simply come to the question, and this is the useful question, what is the trust
*  issue this is solving? And then if you can get an answer to that question on a case-by-case basis,
*  that's when you'll understand why blockchains are relevant. And then once you do that with enough
*  use cases, it becomes a little bit mind-blowing. You've mentioned trust quite a bit.
*  You also mentioned trust minimization in the Chainlink white paper. Can we dig into trust a
*  little bit more? What is the nature of trust that you think about in these smart contracts?
*  What is trust minimization? How do we accomplish, achieve trust minimization?
*  Sure. I think it's important maybe to have a conception of what the alternative is,
*  what is highly reliable, trust-minimized, off-chain, and on-chain computation, and alternative to.
*  So this is just how I see the world in these two camps. One camp is the traditional,
*  what I call brand-based or paper guarantee camp. And this is the world, as pretty much most or all
*  people know it today. This is the world where there's a bank logo or an insurance company logo
*  or some kind of logo. There's a very big building with marble arches and columns. It's the biggest
*  building in the town. It's bigger than the church. And everybody feels very good. Everybody's, that's
*  such a nice logo. It's such a big building. Why don't I give them my money? Why don't I interact
*  with them on the basis of any kind of agreement? And that's good. And that is definitely better
*  than that not being there. And that is definitely a huge improvement for how people conduct
*  commerce, letters of credit from branded entities are very important for global trade to take place
*  in the early stages of global trade. So that's good. But it is fundamentally just a paper
*  agreement with a legal framework behind it. And if the paper agreement you have would say Robinhood
*  or somebody else suddenly has to change, well, it changes. And you can't really do anything about
*  it. You won't be able to change anything about what happened there. There's some long terms of
*  service. There's some other agreements around all this stuff. At the end of the day, that's the brand
*  based and paper guarantee world where it's all very vague and opaque. And you're kind of hoping
*  for the best because there's a nice logo. It's been around a hundred years. There's a lot of marble.
*  But a lot of big building, lots of marbles. This is why banks have such nice buildings.
*  It's not because they want to spend money on buildings. It's to create confidence in them as
*  an entity in order for people to transact through them. This is why all these kind of go to cities
*  that had gold rushes, go to cities that needed banking as a service in certain time periods,
*  they're the most beautiful buildings, at least in the United States. So this is the brand based
*  paper guarantee model for which up until now, there has never been an alternative. So up until
*  now, if you had a bad experience with a bank or insurance company or some logo somewhere,
*  you would only have one option. Your option would be to go across the road and down the block
*  to another building with another color of marble and another set of agreements that are fundamentally
*  still paper brand agreements. Now, for the first time, you have mathematical agreements.
*  You have mathematically guaranteed encryption secured, decentralized infrastructure powered
*  agreements. This is really the shift. This is really the comparison and the alternative
*  through which people should view all of this in my opinion, because there's once again,
*  this conception that everything is fine. Everything works very well. Well, it does. It
*  works fine and very well as long as nothing goes wrong. And then in the cases when things go wrong,
*  which they pretty much invariably at some point do, then you find out that, well, turns out
*  they don't have to pay me or turns out I can't trade or turns out the ATMs can be locked up and
*  only give me 66 euros per day, whether I'm a business or an individual like what happened
*  in Greece a few years ago. Right? And the reality is that once that becomes a strong enough
*  kind of realization for people, I think they will all just migrate to mathematically guaranteed
*  contracts because why wouldn't you? So in the world of mathematically guaranteed contracts,
*  kind of how do we encryptographically secured and decentralized infrastructure powered,
*  how do we evolve into that world? Well, at the end of the day, it comes down to consensus, right? It
*  comes down to a collection of independent nodes, a collection of provably independent computing
*  systems arriving at the same conclusion impartially. That conclusion might be the transaction is
*  valid between address A and address B. Address A has one Bitcoin, wants to send it to address B,
*  and address B has one Bitcoin, right? So that's one degree of validation. It has certain
*  cryptographic primitives that are used, certain levels of cryptography encryption and other
*  methods that basically provide clarity and those guarantees. But fundamentally, it's this level of
*  consensus that multiple independent computing systems came to the same conclusion, verified that
*  conclusion and created a sense of finality, created a final state that is globally considered to be
*  the state of a transaction. And that is how it's achieved, right? So it's achieved by
*  users looking at these mathematical contract systems and saying, you know, if I have money in
*  a bank, there's one single person who controls that money. That's the bank. They could choose to
*  give me my money or choose not to give me my money. And that's great, but maybe there's a percentage
*  of what I own that I want to put into another system where there's thousands of independent
*  computing systems that are promising me, you know, with the help of cryptographic primitives,
*  that I will be able to always have access to this, whatever this is, whatever this,
*  you know, token is, I will at least, or at the very least, I will always have unfettered, complete
*  control and access to it. So, you know, that's one example. Another example is, hey, we have a
*  hybrid smart contract for something like crop insurance. I, as the user, evaluate where this
*  smart contract runs. Oh, wow, the smart contract runs on Ethereum. Great. Thousands of nodes,
*  lots of computational security, hash power, so on and so on. Then I look at, oh, well, what triggers
*  the contract? Oh, there's this Oracle network. Okay, it's composed of 25 nodes or 15 nodes,
*  gets data from five different weather stations. You know, I'm comfortable with that. I have a
*  certain level of comfort with that hybrid smart contract and its ability to provide me consensus
*  about the transaction once the contract knows what's happened, and I'm comfortable with the
*  consensus around the event that controls the contract, right? Because once again, that event
*  is what determines what happens with the contract, and if the contract is super well written,
*  it doesn't matter if the event isn't reliable, right? So now I've made this determination.
*  I've gotten all this clear, transparent information about this system that combines
*  the contract code with a decentralized Oracle network, and I've made my decision to participate
*  in this decentralized insurance, kind of crop insurance policy. I've sent the Bitcoin or the
*  stablecoin or whatever I have on my Android phone, and then time goes by and let's say it doesn't
*  rain. Lo and behold, the smart contract returns the relevant amount from the policy back to me.
*  I continue my life as a farmer, and by the way, the fact that that happened contributes reputation
*  and contributes proof back to both the contract as something that can prove to other people that it
*  has settled and the Oracle network as something that can prove that it has properly assessed
*  reality or properly triggered a contract. And this is where there's one of many network effects
*  where the more that smart contracts and Oracle networks are used, they themselves generate this
*  immutable on-chain data that proves their value and reliability. And improving more and more of that
*  in more and more kind of use cases and more and more variants of the same contract, they arrive
*  at a greater body of proof that they... I am the decentralized insurance contract for crop
*  insurance used by a million users, and my failure rate is non-existent or really low.
*  And here's my Oracle network, and by the way, it's also settled a million of these.
*  And so it's not the logo, right? It's not, hey, what a nice logo you have on top of a building,
*  above a train terminal or something. It's much more, hey, there's a million people,
*  there's a million separate contracts that got settled correctly. I have all the proof
*  that I could ever need about that. And it's not something that's very easy to game, right? Because
*  real value was at stake, real value was moved around. And so I think once again, the transparency
*  aspect comes in where you're able to prove that the cryptographically enforced contracts are better.
*  That said, you can still integrate the traditional banks as long as you create a data feed on the
*  amount of marble that's included. So if that's valuable to you in terms of reputation, you can
*  still integrate the amount of marble and the size of the logo. We could still keep the banks around.
*  I think we will. I think what will happen with the banks and all the insurance companies, by the way,
*  is not that they'll all just die or something. I think it'll be just like the internet.
*  There'll be some of them that adopt this, and some of them that don't, and some of them that do it
*  faster, some of them that do it slower. And that's an economic decision that they'll make. I think
*  their whole question is, is this a foregone conclusion? I mean, I think my answer is yes,
*  this is definitely going to be happening. I think they still have a question of, is this going to
*  change my industry? But I'm seeing a definite shift in people's understanding. And I think
*  that shift is going to accelerate rapidly as one or two of their competitors throw their hat
*  in the smart contract ring and say, well, I have smart contracts. I guarantee my outcomes to you.
*  What do they do for you? It's risky. Just use mine. And the second some of them start losing
*  business because of that, they're going to move very quickly because that's what all of their
*  compensation structures and all their goal planning structures are based around. They're based around
*  what is losing us business or getting us business. Yeah, it's fascinating organizationally,
*  though, to think about banks. They're very old school, and their ability to move quickly
*  is questionable to me. I just look at basic online banking, like how good banks are creating a
*  frictionless online experience and I think they're not very good. And so that speaks to the kind of
*  people who are in leadership positions at banks, the kind of people they hire, the kind of culture
*  there is. So I do wonder if banks will from inside revolutionize themselves to include smart contracts
*  or whether totally new competitors will have to emerge that basically create new kinds of banks.
*  Whether what is the company square? I think it comes up out of nowhere really with cash app and
*  they have Bitcoin on cash app, whether they will start incorporating smart contracts and they will
*  revolutionize the whole banking industry or whether Bank of America will revolutionize themselves from
*  within. I'm skeptical on Bank of America, but you never know. In general, I'm fascinated by
*  how big organizations, whether it's Google and Microsoft or Bank of America, pivot hard in a
*  world that's quickly changing. I think that takes bold leadership and a lot of firing and a lot of
*  pain and a lot of meetings where the one asshole brings up from first principles idea that, you
*  know what, the ways we've been doing stuff in the past require, you know, we need to throw that out
*  and do stuff totally differently. I know a lot of those assholes in a lot of these different
*  industries. First of all, I think they're getting listened to more and second of all, I think all
*  of these places, as I look at it more and more, I think they have a fundamental line of business
*  that they try to protect and then everybody's compensation and everybody's metrics and goals
*  is focused around that line of business. So the second that things begin to impact that,
*  then everybody will be in a senior meeting and that asshole will be quite listened to
*  because he will have the only thoughtful explanation as to why this is happening.
*  How things will evolve from there, I actually don't know because that hasn't been the case yet,
*  but my thinking is that there will be people who don't want to cannibalize certain parts of
*  their business or don't want to change certain parts of their business and then there will be
*  people who say, look, I think this is how the world's going to work. We're going to make a very,
*  very heavy kind of set of commitments to put resources towards this. I already see that
*  with a few banks working on various blockchain-based systems, but granted, they've been
*  working on those for years. So I think all of this comes down to these kind of quarterly
*  earnings calls where somebody asks them, hey, I saw that bank over there wants the blockchain bond
*  or a smart contract derivative platform and I also saw that they made $10 billion in revenues or $10
*  billion in volume or whatever it is from that. What's your plan on the earnings call? And I
*  promise you by the next earnings call, there's a plan. And then the question on the next one is,
*  but when's the plan going to happen? And then by the next earnings call, the plan is happening.
*  And that's what these people are sensitive to. That's what these organizations are structured
*  around. It's not completely economically disconnected. They have this core business,
*  they want to protect it. I understand that idea, but I think the problem with that is sometimes it
*  requires this myopic focus, right? And that's what all the innovation stuff is about. Every time
*  somebody at a corporate entity is about innovation, they're trying to sidestep this. But once again,
*  the incentives to maintain whatever the core business is, is so strong that the innovation
*  people, even though they are there, I think they get a phone call and go like, what are we doing
*  for this? And the ones that actually did good work and got ready to do something for this
*  have done their employer and their organization a very positive service.
*  Whereas the ones that aren't ready, I mean, they'll make up something and maybe they're
*  really smart and they'll get it together. I don't know. Can we talk about tokens a little bit?
*  Generally speaking, there's been a meteoric rise of a bunch of different tokens. We could just talk
*  about Bitcoin and Ethereum as examples. Bitcoin, I think, costs $60,000 in value.
*  What are your thoughts in general on this rise? What's the future of Bitcoin? What's the future
*  of Ethereum? There's the total value locked metric that I think generalizes the different kind of
*  value of these tokens. What does the future value and impact of cryptocurrency look like
*  if we look through the lens of these tokens? I think valuing all these tokens and determining
*  that isn't something I'm particularly great at. I haven't spent a lot of time on that.
*  I've spent the vast majority of my time on building these systems and architecting them
*  and getting them to fruition and getting them to a place where they operate properly
*  on both the technical and the crypto economic and in every other sense. I think with Bitcoin,
*  there is a certain conception of non-governmental fiat money that Bitcoin is really the first
*  creator of. There's this very powerful idea called fiat money. It's basically more or less
*  a 40-year experiment. I think on August 15th of this year is maybe, I think, even the 40th
*  anniversary. A government can say, hey, I have a currency and it's worth something and here it is.
*  In terms of the way that governments have stopped that in the past is if anyone tries to make
*  another fiat currency in their country, they immediately shut it down. They immediately say,
*  hey, this is really bad. You've done something really bad. It's time for you to stop. Don't do
*  it anymore. It stops. That's been the history of non-governmental fiat currency. Bitcoin is really
*  due to its decentralized nature, the first and possibly in some cases in many people's minds,
*  it's still the only true non-governmental fiat currency. Now, how powerful is non-governmental
*  fiat currency? I have no idea. This is why it's really as powerful as the ideas that
*  people ascribe to it in art. Right. Right. Let's say people start saying,
*  right now people are saying, hey, it's internet money. It's the money of the internet.
*  Okay, great. What's that worth? I don't know. It's probably worth a lot. I have no idea what
*  it's worth, but as an idea, as a concept to underpin the fiat money, the let there be aspect
*  of fiat and of Bitcoin, you basically look at it and you say, yeah, internet money. Okay,
*  that could be worth whatever, 60,000, 600,000. Great question. Right? There are other versions
*  of the world where people say, there are countries that don't have a good fiat currency and I see a
*  lot of people using Bitcoin. So Bitcoin isn't internet money. It's countries without a good
*  currency money. So all the countries without a good currency now use Bitcoin and let there be
*  Bitcoin as this, right? As this conception of Bitcoin. What's the value of that?
*  I don't know. That's a great question. Probably a huge amount of value.
*  Then there's a further conception of Bitcoin as some digital gold. There's a scarcity dynamic.
*  There's all these other kinds of dynamics. What is a portable version of digital gold
*  with some kind of built in scarcity worth? Artificially created scarcity. What's that
*  worth? I don't know. That's a great question. I haven't done the analysis on that is the point
*  might be worth a lot. What is it all worth if all three of these things flow into the same fiat,
*  kind of let there be Bitcoin as these three things conception of Bitcoin?
*  I don't know what that's worth. I also know what that's worth, but could be worth a huge amount.
*  So I think it's not, I personally don't think it's super important what I think it's worth
*  or what many other people think it's worth. I don't think that's really that important.
*  I think what's probably important is understanding what the societal conception of Bitcoin is
*  and how does that societal conception evolve over time. That interestingly enough doesn't just depend
*  on you or me or the people who made Bitcoin or anything else. It actually depends on current
*  events. For example, if people suddenly say, I'm more and more worried about fiat currency.
*  I'm more and more worried that governmental fiat, even if it's the most reliable version of that,
*  is not as good as I thought it was. Maybe I should go on the PayPal app and maybe I should
*  get some Bitcoin just in case. What's the world where Bitcoin is a certain percentage of everyone's
*  ownership as a hedge against governmental fiat money not being so good? Having done the analysis,
*  but another example, right? Here's this conception. That's the conception. So when I look at Bitcoin,
*  what I see is a lot of these fascinating conceptions of what the fiat let there be value
*  of Bitcoin is. By the way, all of them could be true. Maybe some of them are true. Maybe some of
*  them aren't true. The fascinating thing is that I've seen this conception change. So when I started
*  in the Bitcoin space, the conception was micro payments. The cost of Bitcoin is low. We'll have
*  micro payments. Micro payments are wonderful for machine to machine transactions. Micro payments
*  are wonderful in the emerging market. And that's fine, right? And that was one conception of
*  let there be Bitcoin as micro payments platform, right? But then the value rose and things changed.
*  There was enough expansion in certain ways. And now the conception has evolved into this other
*  conception. But at the end of the day, I think governments have a very clear set of steps for
*  directing the public's conception of their fiat, right? They say our fiat is worth this for these
*  reasons. Bitcoin doesn't have that. Bitcoin doesn't have an official Bitcoin spokesperson that goes
*  out and says the non-governmental money called Bitcoin, the non-governmental fiat money called
*  Bitcoin has value on the basis of this, this, this, and this. Here's our fiscal budget. Here's
*  our future plans. Our money will continue to be safe and secure and reliable. And so what that
*  hole creates is a hole that we all fill, right? We all basically come to some vague kind of group
*  understanding that Bitcoin is worth this because it is tied to, let's say,
*  all non-governmental fiat money comes into question. Everybody doubts it, possibly due to
*  inflation. And everybody says, you know, this is nice, but I'd like to keep 10, 20% of my of my
*  wealth in non-governmental fiat just in case. You know, what, what are those numbers? I mean,
*  if that happens, you know, I'm guessing you can add a few zeros. I like how you say, I haven't done
*  the analysis as if I'm sure a lot of people have done quote unquote analysis, but it's not,
*  it's still speculation. Nobody can predict the future, especially when so much of it has to do
*  with a large number of people holding an idea in their mind as to the importance of a particular
*  technology like Bitcoin. There's a lot of excitement by its possibilities, but the number of zeros you
*  add is a, is an open question and nobody can do a perfect analysis except whoever created this
*  simulation. Let me ask you this question. Who is Satoshi Nakamoto? There's quite a few people
*  who suggest that person is you. So is it you? No. Who do you think it could be?
*  I don't know who it is. I think if I had to guess, it's probably a group of people,
*  some of which might not even be around anymore. You know, obviously I'm very grateful to,
*  if this is a singular or a group of people for kicking off this entire industry and making this
*  amazing change in the world that, you know, I have the privilege and luxury of being part of in some
*  small way in the work that I do. I think also this kind of focus on who is Satoshi or who isn't
*  Satoshi shouldn't, in my opinion, matter so much because regardless of who it is, that in my opinion
*  should have no substantial significant effect or bearing on the functioning or the value or the use
*  or the security of the Bitcoin system. Right? So I think whoever it is, they're probably better off
*  not making that public. And I think beyond that, whoever it turned out to be shouldn't matter
*  because it has nothing to do with how the system is made useful or secure or anything else.
*  And so I think that's the, you know, that's the point of view that I have.
*  Now, if you were Satoshi Nakamoto, would you tell me? Because you said they shouldn't,
*  whoever Satoshi is, you should keep that private. So would you tell it to me or no?
*  We're in some kind of weird like thought experiment here. If I was this guy, let me think about this,
*  which I'm not, by the way, I am not this person. But if you were, would you say it?
*  I think probably not. I don't see the, I think that they would cause a lot of distraction and
*  a lot of weird stuff. And so realistically, I don't think it would help anybody or even the person who
*  discloses it. But just to be clear, I am not. And whoever it is, I think they haven't said anything
*  because they don't want the attention and they don't want the distraction and they don't want
*  all the problems from this. And that's, that makes sense to me conceptually. It's fascinating to
*  think if they're still out there and part of the, the Bitcoin, the cryptocurrency community,
*  and it is inspiring to think that if they're out there, that they're not revealing their identity
*  because it would be a distraction. That's kind of inspiring that people are like that,
*  just like George Washington relinquishing powers inspiring because it's ultimately about the
*  progress of the community. And that's some kind of ego driven attention scheme. Again, very
*  inspiring. The humans at their best are inspiring. What do you think about the certainty that people
*  in the Bitcoin maximalist community have about this particular piece of technology, Bitcoin?
*  Bitcoin. Is there something interesting that you think that you might want to say
*  about this community or is it just is what it is?
*  I think at the end of the day, results speak for themselves and Bitcoin has had an amazing impact
*  on our industry and had, has had an amazing impact on the world. And I think, you know,
*  the result is still that Bitcoin is very widely adopted and driving the adoption of our industry
*  in many ways. So I think it's very difficult for people to say that Bitcoin maximalists don't have
*  something that they can latch onto and say, hey, there's something very real here.
*  I think there's been decisions made by the Bitcoin community and the people who made the Bitcoin
*  protocol to focus it on Bitcoin and to focus it on the kind of storing of the ledger of Bitcoin
*  and the information about Bitcoin and the transaction of Bitcoin and to focus on securing
*  that. And I understand why that decision was made to a certain degree, right? It was about focus.
*  It was about getting something worthwhile, right? Without adding additional features and additional
*  risk. And that decision is a decision that was made and has kind of the benefits of focus and
*  the benefits of a certain amount of security and a certain amount of guarantees around Bitcoin
*  and what that is and the value of that. And then it has certain limitations, you know,
*  as a consequence of doing less or having the system hold data that isn't related to Bitcoin or not
*  having the system hold contracts, contractual outcomes or smart contract code. So I think it's
*  just kind of a decision, right? And I understand why they're excited and I'm very excited. I started
*  in this industry going to Bitcoin meetups and I met a lot of fantastic people, libertarian
*  people that wanted to see the world work differently and shared a lot of my beliefs
*  and a lot of my points of view. And so, you know, anyone who's been in the industry as long as I have
*  has had to come from the Bitcoin ecosystem by virtue of kind of starting out that early.
*  So I have an unbelievable amount of respect and admiration and gratitude for Bitcoin and that it
*  exists and everything that it's done and that it birthed this industry. There's absolutely no
*  doubt about that. You know, at the same time, whatever design decisions people make are the
*  design decisions they make, right? And so if you've made a design decision that this ledger and this
*  thing will be about Bitcoin, it won't be about colored coins, it won't be about op return at
*  80 bytes, it won't be about these other kind of nuances that you don't want this to be about,
*  then that's fine. That's fine and that's a logical decision and that's called focus.
*  And focus has a lot of value and a lot of great technology products have focused on something
*  and done that. And then there's a lot of smart people around Bitcoin building kind of additional
*  systems that anchor their security within Bitcoin. And I think that's an interesting approach that
*  could bear fruit. I think it'll eventually require interaction with the Bitcoin protocol
*  in more advanced ways. And then there will be another question of, you know, what is the design
*  decision for Bitcoin? Is it that Bitcoin will be just about the Bitcoin ledger? Or does Bitcoin want
*  to evolve into an anchor for all these other systems and maybe create additional data,
*  you know, kind of more data on chain on the Bitcoin blockchain related to that.
*  So I'm excited to see how that evolves. But until then, kind of results speak for themselves and
*  the results that Bitcoin has achieved for our industry and for itself as, you know, kind of the
*  dominant cryptocurrency and the conception of our industry that people interact with first is
*  obviously very important and something that I think really everybody in our industry is grateful for,
*  right? Because without Bitcoin, where would our industry be? And that's obviously something that
*  we can't forget. What are your thoughts about Ethereum in this, in the chain link distributed
*  Oracle network world? Is it competition? Is it collaboration? Is it complementary technology?
*  What do you think about Ethereum? How much do you think about Ethereum? What role does it have?
*  Yeah, I think about a lot. I think it's complete. We're completely complementary.
*  So there's no competitive dynamics. In my opinion, we are completely collaborative and
*  complementary with Ethereum and all other blockchains and all other layer twos that operate
*  a contract, right? So we do not seek to operate a smart contract. We seek to augment and enable
*  smart contracts to go further in what they're able to do. In fact, Oracle networks have some value,
*  but they don't have nearly as much value in what they do. If there isn't a mission critical system
*  like a smart contract that needs their data, right? So we've made our own explicit design
*  decisions and created our own focus around guaranteeing that smart contracts can go further.
*  We've already done that, right? Decentralized finance, the rate at which we put data is to
*  a degree the rate at which certain decentralized financial markets grow. And as we put more data,
*  we see more financial products go live. Gaming, we provide VRF. So we have this kind of focus and
*  it's a very useful and valuable kind of valuable for our industry focus. At the end of the day,
*  I think that smart contract platforms like Ethereum made a different set of design decisions
*  from Bitcoin and others, and they focused on creating the smart contract capability.
*  And they kind of wanted that functionality to exist. And I think since then, there's been a
*  number of people that try to improve on that or try to make variants of that. From our point of
*  view, we want to support smart contracts in all of their variations and in all of their use cases.
*  So one of the things that I personally like about Chainlink is their ability or Chainlink's ability
*  and the Chainlink network's ability to be useful to many different chains and across many different
*  use cases. I'm personally a fan of Ethereum. Ethereum has done a huge amount for our industry
*  as well. Ethereum took us from a world where it literally took months to make a new smart contract
*  by being forced to code it into a protocol. You had to go to the protocol developers and you had
*  to say, hey, I need a DEX or I need some kind of smart contract. Put it in the protocol itself.
*  Put it in the actual blockchain mining and kind of block generation transaction generation protocol.
*  That would take months or sometimes even over a year. That was a horrible experience. And
*  obviously very few people wanted to participate in that. And so very few people made smart contracts,
*  which I was not a fan of. And then Ethereum came along and really did a lot of innovative things
*  and introduced this approach to scriptable smart contracts where you could script all of these
*  different conditions. And I found that fascinating before Ethereum. I found that fascinating once
*  Ethereum arrived. I found it fascinating after Ethereum launched. And I still find it fascinating.
*  I'm also very grateful to Vitalik and the Ethereum community and all the core developers there
*  for taking our industry a step further. So I think they absolutely deserve a huge amount of credit
*  for taking our industry from it takes months to make a really small smart contract to it takes
*  weeks to make a relatively secure, relatively advanced piece of on-chain code that anybody
*  can script and people can do audits on. And that's an unbelievable leap forward for our industry.
*  I'm genuinely grateful to them for that. I think the next step in line with our body of work is
*  how does that scriptable on-chain code become more advanced in its interaction with all of the systems
*  and events in the real world, which is in my opinion, the final missing piece of the puzzle.
*  So my body of work, the body of work that I'm involved in would not be where it is right now
*  without Bitcoin by any measure. It wouldn't even be where it is now without Ethereum and
*  the growth in smart contract development that they've created. And now what I think is going
*  to happen next is there will be a lot of different smart contract platforms, a lot of different
*  layer twos. Some of them will be private for enterprise. Some of them will be public. There
*  will be some public winners in certain geographies for maybe regulation reasons, maybe other reasons.
*  There will be other public winners, the larger internet, and there will be a number of different
*  people building smart contracts in different languages. We are excited and I am excited and
*  the chain link community is excited. And basically there's a lot of, I mean, for lack of a better
*  word, excitement in seeing our industry graduate to providing more use cases, more usable hybrid
*  smart contracts. Because once again, it's absolutely amazing that Bitcoin created
*  non-governmental fiat money. It's an unbelievable innovation and invented decentralized infrastructure
*  and birthed our industry. It's an unbelievably great achievement, an amazing achievement that
*  we now have scriptable smart contracts through something like Ethereum. Once again, monumental
*  achievement in my opinion. Once again, we still need to look to the future. We need to look to
*  how do we take the decentralized infrastructure concepts that Bitcoin initially put forward,
*  that Ethereum then improved upon and created into these scriptable smart contract formats,
*  and how do we expand that into the world of real world outcomes to change the global financial
*  industry, the global trade industry, the global data marketplace industry, and many other global
*  industries. You mentioned results speak for themselves and how design decisions have
*  consequences. The Chainlink community have come up with a lot of brilliant designs. So how do you
*  think through the design choices that you're facing where you can't predict the future,
*  but you're trying to create a better future? Is there something low level,
*  introspective advice that you can give or describe as to how you think through those decisions or
*  high level how you think about those decisions? Sure, absolutely. I think that's a great question
*  and I think that actually gets to the core of what the Chainlink network is supposed to achieve.
*  We are supposed to achieve a maximally flexible system. So once again, this is the big difference
*  between Chainlink and Oracle networks in general and blockchains in my opinion. Blockchains do not
*  seek to be maximally flexible. They say, here's my block size, here's the transaction types you can
*  put in those blocks, here's the contract language I have, here's my blockchain system,
*  here's the fee structure for those blocks, they're going to keep getting
*  composed transactions, they're going to get put into blocks, blocks will get connected,
*  and it'll continue. That's a very focused type of system and that's great and that makes sense
*  because it's focused on creating security for that category of on-chain activity which is once
*  again a critical, critical part of building a highly transparent system and something that
*  Chainlink enables and doesn't compete with and just enables to do more. Oracle networks conversely
*  have to interact with all the world's data and provide all the services that blockchains don't
*  provide. So there's kind of a spectrum. On one end of the spectrum you have blockchains that are
*  highly secure, highly reliable, highly tamper-proof, highly transparent, but are not very feature rich.
*  For example, they cannot talk to an API. Many of them can't generate randomness. They cannot do
*  some kind of privacy preserving computation. So they're very secure and there are these kind of
*  data structures and smart contract platforms to hold on-chain code that can define conditions,
*  receive value, pay value back out under conditions, and create transparency around all that,
*  which makes perfect sense. And then there's oracles and oracle networks. That is all the
*  world's data. We're talking about taking all the world's data and making it consumable for all the
*  world's use cases that have trust issues. So the amount of variability there is absolutely massive.
*  It's like the decentralized oracle network and the conditions that that decentralized oracle network
*  needs to meet is going to vary very widely from an insurance contract to a lending contract,
*  to an ad network contract, to the data sales contract that we discussed, to any number of
*  other smart contracts. So really the ability of a decentralized oracle network to flexibly address
*  all of those requirements is what's necessary. So flexibility is the goal, whereas with on-chain,
*  Bitcoin, flexibility is the enemy in the sense that you want security, you want the focus there.
*  In that kind of world, design decisions have huge consequences. And then if you look at the
*  distributed oracle network side, you want to remove the restrictions of design choices. You
*  want to provide maximal flexibility then. So it's a completely separate kind of design framework.
*  It's a slightly different problem because we're not trying to define transaction types fitting
*  into blocks on a certain timeline of those blocks being generated. We're trying to say, hey, there's
*  this world of services or this world of data that's not very deterministic, but it's unbelievably
*  useful to these smart contracts over here. And actually they needed to even exist. And we really
*  want them to exist because once they exist, it's going to completely redefine what our whole
*  industry is known for. And DeFi and NFTs are not even the tip of the iceberg. They're like the
*  snow coming off the top of the iceberg. And so our goal is to create a framework and an
*  infrastructure and a software that allows people to compose decentralized oracle networks. So
*  initially you can compose a decentralized oracle network of seven nodes that goes to three data
*  sources to trigger your contract worth a million dollars. And that's where you could start. And
*  then let's say your smart contract, your DeFi smart contract goes to a billion dollars. Well,
*  then you need to make some changes. You need to go from seven nodes to 15 or maybe 31 nodes.
*  And you need to go from three data sources to five or seven. And you maybe need to create some
*  kind of what we call circuit breakers and some other checks. And you need to make sure that the
*  decentralized oracle network comes to consensus around those checks. Because now the decentralized
*  oracle network isn't controlling a million dollars, it's controlling a billion dollars.
*  And we have decentralized oracle networks that control well over a billion dollars,
*  multiple billions of dollars. And we see them growing and getting more advanced data sources
*  and more advanced features. And then if somebody else comes and says, well, you know, I don't
*  really want to make a DeFi product. I want to make crop insurance. And I have a completely different
*  set of conditions. I want this method of consensus. And I want data to be aggregated in this way,
*  but not the way that you do for decentralized financial products. I mean, what are we supposed
*  to tell them? We're supposed to tell them, no, you know, our decentralized oracle network can't let
*  you do that. And you can go and wait another five years until somebody builds it for you.
*  That's not what we want to do. What we want to do is be able to say, absolutely. Here's an example
*  of how somebody else made a decentralized oracle network for weather insurance. Here's a template.
*  Change that template, evolve it to meet your needs. And then someone else comes and says, hey,
*  I have some other use case in gaming. I want to make NFTs related to real world sports events,
*  or I want to do whatever I want to do with some kind of sports related data.
*  Wonderful. Here's the framework. Here are your risk dynamics. Here's a collection of node
*  operators. Here's a set of pre-integrated data sources. Here's a reputation system to assess
*  the quality of your ensemble of nodes. Here's a way to scale that up as the value in your contract
*  scales. Here's all the tools that you need to build this contract. And what we actually see now,
*  as there are multiple types of computations and data sources that are provided by different
*  decentralized oracle networks, of which there are now hundreds, we now see that a single hybrid
*  smart contract might use multiple decentralized oracle networks. So there might be a hybrid smart
*  contract that uses a price data, decentralized oracle network, a proof of reserve oracle network,
*  a randomness oracle network. And I think we're going to continue to see this dynamic that more
*  and more advanced contracts compose various decentralized oracle networks into more advanced
*  use cases. And this is the dynamic that we're focused on enabling. And I think it's actually
*  a very virtuous cycle for everybody because the more of these hybrid smart contracts we enable on
*  Ethereum and other blockchains, the more our industry provides real world outcomes to the
*  larger world, which is at the end of the day, what I think everybody in our industry wants.
*  Everybody in our industry wants hybrid smart contracts to become the way that global finance
*  works, global trade works, global insurance products work, because they will inherently
*  need both a blockchain on which the contract itself lives and an oracle network that powers
*  all of the other interactions. As a developer, how would you recommend somebody listening to this,
*  but also me, to get started with smart contracts and to get started with hybrid smart contracts?
*  Well, for hybrid smart contracts, I'm going to have to do some kind of shameless promotion.
*  Please let me twist your arm.
*  Thank you. I think you can go to our YouTube. We have a number of developer tutorials.
*  Chainlink YouTube?
*  Yeah, Chainlink. I think you could just search Chainlink on YouTube. You should find it.
*  Beyond that, we recently had a hackathon where we had a huge amount of very
*  advanced hybrid smart contracts getting built.
*  To elaborate on that, you had a hackathon. Is that something that people can follow along,
*  like a video where there's web page traces of what happened, or is there future actual
*  hackathons that people could literally participate in?
*  There's plenty of more hackathons coming up. We want to enable as many developers in Web3 and
*  build hybrid smart contracts as a way to redefine our industry and make all of these smart contracts
*  come to life. There are definitely going to be more hackathons, so people should go and
*  pre-register or register on a list to get involved in that. That's a great resource where we have a
*  lot of speakers and a lot of educational tools. They happen over a course of weeks, not days,
*  so there's a long time for people to work on these things at the speed that they find comfortable.
*  Two questions. One, is there a kind of hello world entry point for
*  hybrid smart contracts? Two, on the hackathon side, what kind of stuff do you see people building
*  at first, just kind of getting their feet wet in terms of the kind of applications that can be
*  enabled? There's unbelievable things that we see people building. I think
*  how to get your feet wet, I think the hello world is probably DeFi because it's pretty
*  straightforward and there's a large amount of data sources that we already have putting data
*  on chain on testnet, which is the test environment in which people would build. So I think DeFi is
*  probably to a certain degree the most exciting for certain people and pretty expansive in terms of
*  the tutorials and the amount of contracts to see how people have already built it. I think beyond
*  that, we see people building amazing things at these hackathons. In the previous hackathon,
*  we saw somebody build a smart contract that allows someone to rent out their Tesla.
*  It allows the Tesla API to give someone else access and rent out someone's Tesla on the basis
*  of a smart contract kind of coordinating payment, which was amazing. The more recent hackathon,
*  we saw something called D-Bridge, which is a cross-chain solution that uses Oracle networks
*  to confirm data on different chains. So I think the things that people build will just become
*  expansive and varied in ways that I can't even imagine. But I think this recent hackathon saw
*  a huge, huge list of different kind of winners in different categories. And there's so many
*  different categories. We even have a GovTech category and a whole bunch of things. If people
*  want to see what's possible, they can go look at the winners. I think that's probably a good idea
*  at... Yeah, that'll be on the side of the hackathon. There's a blog related to that,
*  and we're going to have more of these. Once again, our explicit goal is to take our industry into
*  this world of hybrid smart contracts, which just benefits everybody. It makes more on-chain activity.
*  It helps provide real-world value to the average person from all of this infrastructure period.
*  And at the end of the day, I think that it just redefines what our industry is about through use
*  cases. Because if you only learn through our industry from the point of view of a single use
*  case, like the NFT use case or some other use case, that's what our industry is about. And the
*  more of these use cases that people can make available to the average person or to the fintech
*  world or to the insurance world or wherever, the faster our industry will not just be about bitcoins
*  or tokens, it will be about changing global finance, changing global insurance, changing global
*  trade. And that's the change in the world that I and a lot of other people in this industry, I think,
*  got into this for. Now, it's funny, you've mentioned about... You've had a lot of kind words to say
*  about Bitcoin and Ethereum as important technology that paved the way for the future. And you somehow
*  did not mention one of the most profound pieces of technology, which is Dogecoin.
*  What are your thoughts about this particular revolutionary technology? And what are your
*  thoughts about Dogecoin going to the moon, to Mars, and outside of the solar system?
*  I think Dogecoin is a very interesting kind of... Probably closer to a social experiment
*  than anything else. Isn't everything a social experiment?
*  Yeah, I guess that's fair to a degree. I think it's fascinating how that's evolved. I think
*  the people that made it with certain goals in mind, and then it's kind of taken on a life of
*  its own. I don't fully understand exactly why it's taken on a life of its own at this point.
*  Once again, I don't spend too much time thinking about different tokens and how they're evolving.
*  I'm much more focused on the launching and... The technology around trust and all those kinds of
*  ideas. But I think one of the fascinating things about Dogecoin is how technology that
*  leverages social dynamics, that technology's ability to utilize fun and memes to spread.
*  I think it's really interesting. I don't think it should be discounted as a...
*  I think I tweeted today something about the fundamental force field of fun.
*  That fun has an effect on the space-time. So general relativity describes how mass and energy
*  can curve space-time. I was just giving an example that when life is fun, it seems short. When life
*  is not fun, it seems very long. So fun has a very similar effect on space-time, like in curve
*  space-time. In that same sense, there is a power to the meme. I think Dogecoin illustrates that.
*  I think Elon is an example of somebody that uses Dogecoin. I don't know his philosophy in particular
*  in this aspect, but he does use it effectively to excite the world in a fun way about the
*  possibilities of future technologies like cryptocurrency. I think the Bitcoin world is
*  very serious right now. We've spoken about Bitcoin maximalists. There is very little space for fun
*  and joking in the Bitcoin world, but there's still a little bit of fun and humor left in the
*  Dogecoin world. In that sense, I think it's exceptionally powerful to inspire, to excite,
*  to be able to talk about stuff without the seriousness of financial impact that
*  now certain cryptocurrencies have like Bitcoin. I've previously mentioned that Dogecoin, I think,
*  is a fascinating piece of technology because I do think cryptocurrency is much bigger than
*  the technology that you focus on. There is also a social element that you also spoke to that's,
*  I think, not quite yet understood and it's fascinating to watch, especially as it co-evolves
*  with the different tools on the internet, the different social network mechanisms on the internet.
*  I'm a huge supporter of Dogecoin because I'm a huge supporter of fun.
*  I'm fascinated to see how it'll work out.
*  You think it'll go to the moon? You think it'll be the first cryptocurrency to land on the moon?
*  I couldn't say. I haven't done the analysis, as I've said before.
*  I haven't done the analysis. Well, yeah.
*  No matter what, I do hope we will get humans back on the moon and hopefully get humans on Mars soon.
*  Dogecoin, Bitcoin, or not. Let me ask you about books and movies. What books and movies in your
*  life long ago when you were a baby Sergey or today had an impact on you? Maybe you would
*  recommend to others and maybe what ideas you took away from those books, movies, coloring books,
*  children's books, blogs, whatever. Yeah, yeah, sure. I think one of the things that had a very
*  big impact on me were Plato's dialogues and particularly Protagoras and Gorgias as some of
*  the two initial ones. I think what Plato's dialogues do very well is they give people a clear
*  picture of what dialogue looks like and what the assessment of information
*  probably should look like and how the dissection and analysis of an idea is very important
*  and how it can actually be taken in either direction. But at the end of the day,
*  that the process of eliminating this fuzzy thinking and arriving at whether it's an
*  external dialogue or an internal dialogue about an accurate picture of reality is actually very
*  important. I think I'm very lucky to have read the dialogues when I was in my early teenage years
*  and it had a very large impact on me because it showed me that nobody knows what they're talking
*  about. I would play out dialogues in my mind and I would engage in certain dialogues with
*  different people and what the Platonic dialogue showed me was how to tell when someone has no
*  clue. And a lot of people are very good at saying they have a clue, saying like, here's how the
*  world works, here's what you should do with your life, here's what you should do with your time,
*  here's what you should do with your money, here's what you should do with your attention,
*  here's what you should do with all these things. And I think the ability to evaluate information
*  generally is something that is surprisingly under taught. I don't actually understand why there
*  isn't a course in high schools or universities that's just like, here is how you evaluate
*  information, here's how you engage in external dialogue and internal dialogue to arrive at an
*  accurate picture of reality rather than the picture of reality that other people want you to have
*  for their benefit most often. And at the end of the day, I think that put me down a path
*  to really try and understand. Beyond that, I think biographies have had a very large impact on me,
*  Plutarch's Greek and Roman lives. After I read Plato, I started reading a bunch of stuff,
*  Greek stuff. I was just like, these Greek guys, they really know how it is. They did this 2000
*  years ago and they still got it right. There's something here. It's kind of this theory of time
*  around the value of intellectual ideas. If an intellectual idea has survived the test of time,
*  it's much more valuable than the intellectual idea that I just came up with 10 minutes ago,
*  haven't told anybody and hasn't gone up against all of the kind of rebuttals.
*  What's your favorite, what would you say would be a most impactful biography that you've come across?
*  I don't think it was those Greek or Roman biographies because they were very far away
*  I think that probably one of the most impactful ones that I can remember recently is around
*  Vanderbilt. Vanderbilt was this guy who basically, without that much of an education, he would
*  invent or work with people to make these steamboats. And then he had a lot of vacuum
*  in around creating certain monopolies regardless of what was right or wasn't right. And then
*  fascinatingly enough, it all hinged on like a Supreme Court case that decided if monopolies
*  were acceptable in the form of state-created monopolies or not. And if it was deemed that
*  state-created monopolies were acceptable, he would have had a huge problem, this guy.
*  But it was deemed that state-created monopolies through these licenses for steamboat routes was
*  not acceptable. And that did two interesting things. It unseated some kind of old-time
*  landed gentry in the Americas in the 1830s and 40s. And it basically made him right and he saw
*  it before other people. So I think Vanderbilt was a very interesting personality, first of all,
*  of all the biographies that I read, is somebody who really took the situation in hand and kind of
*  took action to achieve an outcome, which I think was an amazing result. The fascinating thing,
*  by the way, is, or amazing way of looking at things, the fascinating thing, by the way,
*  is that the ferries now in New York Harbor are all run as a public good. So the fascinating thing is
*  that the guy, he focused on an industry and he worked on something that was so important that it
*  ended up becoming a public good. And I think that that's an interesting conception of how to look at
*  this industry. I think there's a lot of economics dynamics around this industry, but I think I might
*  have said this somewhere else before, but really the success of someone in this industry is whether
*  they're able to make a Linux or HTTP or an HTTPS like system that lives on for a very long time
*  and is essentially a kind of public good. It's a success of an idea, even if that idea is
*  originally sort of a capitalist idea about that's grounded in financial benefit. Success of it is
*  if it becomes a public good. It is so universal. It is so fundamental to the quality of life that
*  it's a public good. It is deemed to be so valuable that it should be a public good.
*  Yeah, I think so. I think that's a pretty good definition of success that you work on a body
*  of work and that body of work isn't just some commercial enterprise. It's a body of work that
*  whatever commercial aspects or economic incentive aspects it might have, it eventually is so
*  important that it becomes critical to how society functions. I'm personally quite
*  lucky and grateful to be, in my opinion, working on something like that with an amazing team and
*  an amazing community that seems to really very much care about this hybrid smart contract,
*  transparent world that a lot of people in our industry, realistically, I think this is why a
*  lot of them signed up. This is why I came into our industry. It wasn't because Bitcoin,
*  it was because Bitcoin was a picture of how the world could work in so many other ways.
*  That picture of how the world could work in so many other ways attracted me a very long time ago.
*  I think that all of this stuff will eventually become a public good. I think it'll become so
*  critical to how societies function internally and internationally that just like there are systems,
*  like the Federal Reserve, like global payment systems, like all these types of things,
*  I think eventually all of this technology will be baked into these
*  societally critical systems. If I and our community and the people I work with and the body
*  of work that we're working on can make some kind of contribution to that shift towards fair
*  economically fair, transparent society, from my point of view, it's a very worthwhile body of work.
*  In terms of the show, you also mentioned the show. One of the shows that I really seem to like more
*  and more for some reason is Star Trek, not the old Star Trek. I don't really get the old Star Trek,
*  the special effects aren't good enough. Star Trek, like The Next Generation and Voyager and
*  Deep Space Nine and all those. I think whenever I happen to watch a Star Trek show again,
*  I have a very simple conception in my mind that I really didn't have whenever I saw it way back when.
*  It's that this is what the world looks like if technology takes us towards a utopia.
*  I think there's this fascinating thing where technology can take us towards a utopia or
*  towards a dystopia. In my mind, those three Star Trek shows are a picture of what
*  human civilization looks like if everybody's technological ambitions successfully take us
*  towards a utopia. Because in the Star Trek universe, you're not seeking money or you're
*  not seeking safety or you're not really seeking anything for yourself. Everybody within Maslow's
*  hierarchy of needs has gotten so many things for themselves that their goal is learning and
*  discovering and or helping. I think there is this conception of human life once the baser needs are
*  satisfied. At the end of the day, I think that's what technology generally can elevate all of
*  human civilization to. It can elevate us to Star Trek world where if people want to invent,
*  they can do that all day and nothing else. If people want to explore the stars, they can explore
*  the stars and they don't have to worry about economic scarcity or any number of these other
*  conceptions. I don't know what the most impactful on me shows have been, but for some reason,
*  recently Star Trek in the newer variant, not the most new Star Trek shows, those shows are a little
*  strange. The middle Star Trek universe where everybody is doing something with a very important
*  purpose and nobody's thinking about where's my paycheck or where's my whatever. They're all
*  we have to discover the formula to this to save the planet over there. Literally every episode,
*  you're discovering a formula to save a planet of some kind or a universe or ecosystem or whatever.
*  You're looking at it, you're like, this is a pretty good place to end up. This is where we
*  might want to end up. It gives you hope. It's funny that we don't often think about the...
*  I think it's very useful to think about positive visions of the future when we're trying to design
*  technology. There's a lot of sort of in public discourse, a lot of people are thinking about
*  kind of how everything goes wrong. It's important to think about that sometimes,
*  but in moderation, I think, because there's not enough... In my little corner of artificial
*  intelligence world, people are very kind of fear monger centered. There's a lot of discussions
*  about how everything goes wrong. Important to do, but it's also really important to talk about
*  how things can go right because we ultimately want to guide the design of the systems we create
*  to make things right. I think with hope and optimism, not naiveness, but optimism,
*  you can actually create a better world. You have to think about a positive,
*  a better world as you create because then you can actually create it.
*  Yeah, I'm one of the people that thinks that having an optimistic view of the world is better
*  for design and creativity than having a pessimistic one. It's hard to design when you're in fear.
*  Do you have advice for young people speaking of being excited about and hopeful about the future
*  world? Do you have advice for young people today in computer science world, software engineering
*  world, in crypto world, but maybe in any world whatsoever for life? How to pick a career or how
*  to live life in general? I think the thing that young people should do is not any one specific
*  thing for any one specific young person. I think what they should do is what they won't be able to
*  do in the later stages of their life. The way, in my opinion, from a framework point of view,
*  to think about that is that the amount of obligations and the amount of time that a person
*  has seems to just diminish over time. The amount of free time they have. You start your job,
*  you get a bunch of responsibilities, something with your partner, spouse, more responsibilities,
*  kids, probably even more responsibilities. Soon enough, the time that you have to educate yourself,
*  to travel, to experience the world, however, create whatever creative endeavor you're interested in,
*  slowly but surely disappears. I think this is something that young people don't fully
*  realize. They assume that the world as it is now and the amount of free time that they have
*  to travel, to educate themselves, to make new friends, to do all these things will somehow
*  maybe diminish by 10%. It won't diminish by 10%. It will diminish by 90%. And the 10% that you have,
*  you'll be resting to get back to work and get things done.
*  Yeah. So what I think young people should do, and this is why it's very different for each of them,
*  I can't tell young people, hey, you should study philosophy, travel, and start your own enterprise
*  to achieve something worthwhile in the world. That might be something that's good for me with my
*  values and my kind of worldview, but for other people might be something else. I think the way
*  that they should conceptualize it is imagine if over the next 10, 12 years, the amount of choice
*  that you had about what you could do was cut down by 90%. And this is copying from this kind of
*  Jeff Bezos regret minimization framework. In that framework, it's like, what would I regret
*  not doing at 80? And that's kind of meant to create this long-term view and make these
*  decisions now that'll get you to a long-term future that you can look back on and be proud
*  of your life, right? What I think young people should do is they should say to themselves, look,
*  if I never get the chance to travel for as long as I live, assuming that after 25, after 27,
*  after 29, that's the case, how will I feel about that? If I never get to start a company
*  after 25, after I get married, after I have kids, how will I feel about that? And whatever they
*  feel the worst about is what they should do. Whatever they feel like when they say to themselves,
*  you know, if I don't travel now, I will never travel. And they feel horrible about that. They
*  just have an overwhelming fear and disgust at themselves in that type of state at 25, 27, 29.
*  That's what they should do. And they shouldn't listen to anybody else. Let me put it to you this
*  way. If you're really smart, you're going to make it anyway. There's a lot of people putting a lot
*  of pressure on you because they're afraid whether you're going to make it. If you're really smart,
*  you're going to make it anyway. If you're not really smart, you're screwed anyway.
*  Either way, just relax with it and use your time well to do the things you would most regret not
*  doing. That's really fascinating. I wouldn't say relax. I would say very much cherish the free time,
*  the discretionary time that you have from the age of 18 to maybe 25. Because at 25, everyone's going
*  to start looking at each other and asking, what have I achieved? Like my friends have achieved,
*  I haven't achieved. And then by the time you get to 30, you're going to look at each other again and
*  go, well, my friends have a family or a company or a PhD or whatever. What do I have? And the pressure
*  will just increase. And it'll increase so much that even if you want to go and do the fun thing,
*  it will not be fun because the pressure of comparing yourself to your friends at 25 or
*  your peers at 30 will be so great that it will no longer be normal for you to be in a hostel at 30
*  living it up. And this is why I also can't tell you specifically what it is. For me,
*  it was getting an education in philosophy that was rigorous and in depth. It was traveling and
*  it was starting an enterprise that I thought that was worthwhile that I directed that I could make
*  into something great. That's what it was for me. For other people, it might be something with a
*  band. It might be something with painting. It might be an education. You, by the way, also should not
*  assume that your ability to get an education will improve. All of those responsibilities
*  will take away your ability to get an education. So if you value having an education, if you value
*  being a deeply educated, well-rounded person with a wide array of knowledge on a wide array of topics,
*  capitalism will force you to specialize. That's what it's good at. It's going to take you. It's
*  going to fashion you into a very specific tool for most people, into a very specific set of tasks.
*  If you want to have an education in something, get it now. If you want to travel somewhere,
*  travel there now. If you want to do some kind of creative endeavor that you doubt whether you'll
*  have time for in the future, do it now. You won't have time for it in the future. You won't have time
*  to read philosophy books all day, unfortunately. You won't have time to fly to Italy and kind of
*  hang out with people. If you're serious about your life, you're going to get more responsibilities.
*  You're going to get more stuff to do. And so my advice to you is do not piss away this rare,
*  unique, discretionary time. And if your friends are, get new friends. Get smarter friends.
*  Get people who are using the limited time they have better. That's my advice.
*  So just to quickly comment, it's brilliant to reframe high school and
*  undergraduate college education. Sometimes people want to quickly get it over with. But
*  one thing I remember thinking, and it's very true about high school, is one of the only times
*  in your life you'll get a chance to truly get a broad education. You don't often think of it that
*  way, but it's a chance to really enjoy learning things that are outside of the specialty that
*  you'll eventually end up with. And that's how college education is. And on a more fun side,
*  I played music, I did martial arts, and we offline mentioned played video games. I find it fascinating
*  and brilliant what you said, which is the world will not give you a chance to truly enjoy many
*  of these things and truly get value from many of those things once you get older. I find it
*  exceptionally difficult to enjoy video games now. There's so much stuff to do. There's so much
*  responsibility. And at the time when I played Elder Scrolls and Baldur's Gate and Diablo 2,
*  at the time I thought maybe that was a waste of time. But now looking back, I realize,
*  because I always thought, you know, let me get the career first and then I'll have a chance to play
*  video games. That's the way I was thinking. You know, it was a waste of time because I should
*  really progress on the career and then I'll have time to play video games. No, the reality is
*  that was really fulfilling. Those are some of the happiest travel experiences of my life,
*  is me traveling to those virtual worlds and spending time in them. And it was really fulfilling
*  and they stayed with me for the rest of my life. And I get to experience echoes of that when I play
*  video games these days for an hour here, an hour there, like one hour a month or something like
*  that. But even those experiences, as silly as they are, they seem like a waste of time at the time,
*  enjoying them fully, unapologetically. And in a framework exactly as you said, would I regret
*  being the kind of person who's never played those video games? And I can for myself honestly say
*  that yes, look, when I'm on my deathbed, I'm glad I built Ballersgate too and all those arena
*  Dagger, Fall, Morrowind and all the Elder Scrolls games. And yeah, the things that don't necessarily
*  fit into this kind of storyline of what a career is supposed to be, travel and all those experiences.
*  I think I'd just like to say one final quick thing on this. I think this extends to really hard
*  things as well. It extends to the things you want to do. But one of the best pieces of advice one of
*  my mentors gave me early on in my career around this time is that it will actually become harder
*  to start a company as you get older. Once again, because you have more responsibilities,
*  you're responsible to your partner for some kind of income to create a life together. Once you have
*  kids, you're responsible for an even greater income to create a life for kids. And startups
*  do not generate income, right? They take many, many years before anything happens. People are
*  getting evicted. People are eating ramen noodles. That is a thing that happens. That will happen.
*  So I'm not saying that you should do the fun things or the enjoyable things. I'm saying the
*  things that you would regret not doing, that you can uniquely do in the time span from 18 to 25.
*  Which one of which is if you plan to have a family and start a family when you're 25,
*  you should start a company now. You should not wait until a bunch of people depend on you for
*  income to eat to start a company. The amount of pressure that will be on you at that point
*  will be monumental. You should start a company when nobody depends on you and you can sleep
*  on the floor eating ramen noodles and still have a great time and show up with a lot of enthusiasm
*  and be excited. So I just mean whatever you want to really devote yourself to and really do,
*  don't put it off. Don't go to consulting or banking or any other industry and say,
*  I'm going to do this for three years and I'll get experience. The only way you get experience
*  is by doing something. You go, you do it, you fail, you do it again and again and again and
*  again and again and then you have experience and then you can do it right. That's the only
*  way experience happens. There is no other way short of mentorship. If you're lucky to get mentorship,
*  99% of people don't get mentorship. And even though we're talking about young people,
*  I feel like you're speaking to me as somebody who's who spent the last two weeks sleeping on
*  the floor because there's no mattress and somebody who is single and somebody who's thinking about
*  doing a startup. I felt like you were speaking to me as a fellow young person. Let me ask you about
*  this whole life of ours to zoom out on the big philosophical question, the ridiculous question.
*  What do you think is the meaning of it all? Do you think about this kind of stuff as you're
*  creating all the technology, as you're thinking about this future, you ever zoom out and think
*  like, why, why, why are you surrogate striving? Why are we the human species striving for the stars?
*  So I think it comes down to, you know, whether people want to live in society. So if, if people
*  decide to be part of society, they have a certain set of conditions that they decide to take part in.
*  Right. So I think what this comes down to is a lot of really involved conversations. But if we assume
*  people have free will and choice, we just kind of make that blanket assumption, then the question
*  starts to become, well, what choices do we make? And how do we live with those choices? And I think
*  probably the most fundamental choice is whether we exist in a society or we choose to leave society.
*  And there are people that do this. There are people that go live in the woods. There are people
*  that immigrate to other societies and they make a choice. Right. And as they enter those other
*  societies or they choose to leave society and go live in the woods, they adopt a certain set of
*  values. Right. They adopt values that the society prescribes. They compromise their own values. They
*  define their own values and they create a set of values for themselves. Right. I think at the end
*  of the day, if you're going to choose to live in society, in addition to all the minimums of, you
*  know, not throwing garbage on the floor and, you know, doing nice things for people that need help
*  and doing any number of things to just be a normal human being within society, you have to ask
*  yourself, what am I doing as part of society? Right. You can always say, hey, I'm going to leave
*  society. I'm going to live in the woods. I did that. Right. I went and I lived in the woods and
*  I gave it a shot. Realized a ton of stuff, huge amount of clarity from that. But when you decide
*  to live in society, you take on, first of all, certain minimal agreements. You mold your values
*  a little bit to that society. That's another choice that people inherently make. And then there's
*  a question of, well, what am I doing here? Right. What am I doing in society? Right. So when people
*  say the meaning of life, I don't know what the meaning of life is. The meaning of life in society.
*  What's the meaning of life for the choice that you've made within society? Right. Because that's
*  maybe the first fundamental choice you made. You made a choice and you continue to make a choice
*  to be part of society and a specific society. Right. So you've made this choice. You're part
*  of a society. And now you kind of have a life and you have people around you. And then the question
*  is, in my opinion, the question is, what is the body of work that you want to make? Right.
*  I think personally that life is kind of so short and the ability to get enough resources for
*  yourself in at least the developed markets where we're lucky to be in is so relatively abundant
*  that we, you and me, have the luxury, by your pursuit of a PhD, you've had this luxury,
*  I've had this luxury through the work that I've been doing to pursue something that makes society
*  better. So this is kind of the question I would say. The question is, am I going to live in society?
*  Yes or no? Yes. Okay. Most people choose yes. I understand why to a degree. I understand why
*  some people choose no. And then what is the, I'm going to be in society. If you choose to be in
*  society, you're just choosing to abide by the rules. You're choosing to just do the minimum.
*  That's what being part of society means. People that choose to be part of society but don't want
*  to do this, it's very confusing. They should just leave. They should just go, look, I don't like this
*  deal. I'm going to go somewhere else. I'm going to live in Tibet. I'm going to live in the woods.
*  I'm going to live wherever where the rules are to my liking. Right. You've chosen to be in society.
*  Next question, kind of final question is, what is the body of work that I'm going to be involved in?
*  Because in looking at that Jeff Bezos kind of regret minimization framework thing,
*  I think that's what a lot of it really comes down to is you kind of, the framework is at 80 years
*  old, you look back over your life, what would you regret not doing? What would you regret not pursuing?
*  I think there are a number of things on a personal level each person has. But I think,
*  at least for me, and probably for many of the other people I know, there's a question of,
*  what is the body of work that I was involved in? What did I do? What happened? What was I involved
*  in? And in my opinion, you should have a good answer to that. And you mentioned the body work
*  in relation to whether it helped make a better world. And the fundamental question there is,
*  what does better mean? So it's our striving to understand what is better. What kind of world
*  would we love to exist after we're gone? And I think that's another thing, almost unanswerable
*  question, but it's one we can strive towards, is what is a better world?
*  Right. I think that's once again a very personal question. I'm not sure if there's an objective
*  moral truth that's going to suddenly give us all an answer. I think it's actually quite
*  fascinating to me when people feel they have this objective moral truth, they're so sure in
*  their opinions, this is what we do, we should go hurt them or help them or kill them or rescue them
*  or whatever. There's all these kind of very situational specific, kind of like, this is the
*  right thing to do. The objective moral truth told me that this is it. But maybe there's a definitive
*  truth that we can arrive towards a sort of a consensus of what that is within the little
*  local pocket of society that you're in. Yeah, that's the point.
*  That's what happens. People just then mislabel it and they go like objective moral truth.
*  This is not our idea. This is coming up from on high here. This is the objective moral truth
*  that I think exists in some metaphysical form somewhere. And then you build a building with
*  marble and it's big and usually what happens. And then you convince yourself that that building
*  represents a truth. I think those people actually, the people who build those buildings probably
*  understand that there is no metaphysical objective. They're just like, we're all just coming to
*  consensus. I'm going to build the biggest building and you're like me and that's what we're going to
*  do. They just look at it that way probably. I think what ends up happening with all these values is,
*  yeah, people should determine that for themselves. I agree that there's a second order question here
*  of what is the best body of work to work on. Personally, I think that's probably a mix of
*  what could you realistically achieve? Is that going to have an impact on society that you feel
*  good about? Yeah.
*  Right? So these are probably the two aspects of this question and is this going to have a good
*  impact on society that you feel good about? Obviously very subjective. Some people save
*  animals. Some people save forests. We and I are creating this system of economic fairness
*  and transparency. I feel that I'm in a good position to enable that. I feel that I have a
*  good chance of succeeding at that and I think that the impact will be quite meaningful for a large
*  number of people. And so I'm completely happy to look back once I'm 80 and see a body of work
*  that achieve that and be very proud of that, right? Because I think that's what I'll be doing
*  when I'm looking back. So. Well, I agree with you. The scale of impact
*  as a smart hybrid smart contracts, this whole idea that you're working on has a potential to
*  transform the world for the better at a scale that I can't even imagine. So speaking of which
*  means even more that you would waste so many hours of that exciting life with me. Thank you so much
*  for talking to this, Sergey. This is a really fascinating conversation, a really fascinating
*  space and I can't wait to learn more. So thank you so much for talking today. Thank you for having
*  me. It's been an absolute pleasure. Thanks for listening to this conversation with Sergey Nazarov
*  and thank you to Wine Access, Athletic Greens, Magic Spoon, Indeed and Better Help. Check them
*  out in the description to support this podcast. And now let me leave you with some words from
*  Copernicus. To know that we know what we know and to know that we do not know what we do not know,
*  that is true knowledge. Thank you for listening and hope to see you next time.

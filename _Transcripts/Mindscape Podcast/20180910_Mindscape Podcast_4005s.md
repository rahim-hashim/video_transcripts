---
Date Generated: June 10, 2024
Transcription Model: whisper medium 20231117
Length: 4005s
Video Keywords: ['bitcoin', 'blockchain', 'cryptocurrency', 'internet', 'money']
Video Views: 14585
Video Rating: None
Video Description: Blog post with show notes: https://www.preposterousuniverse.com/podcast/2018/09/10/episode-13-neha-narula-on-blockchain-cryptocurrency-and-the-future-of-the-internet/

Support on Patreon: https://www.patreon.com/seanmcarroll

For something of such obvious importance, money is kind of mysterious. It can, as Homer Simpson once memorably noted, be exchanged for goods and services. But who decides exactly how many goods/services a given unit of money can buy? And what maintains the social contract that we all agree to go along with it? Technology is changing what money is and how we use it, and Neha Narula is a leader in thinking about where money is going. One much-hyped aspect is the advent of blockchain technology, which has led to cryptocurrencies such as Bitcoin. We talk about what the blockchain really is, how it enables new kinds of currency, and from a wider perspective whether it can help restore a more individualistic, decentralized Web.

 Neha Narula is the Director of the Digital Currency Initiative at MIT. She obtained her Ph.D. in computer science from MIT, and worked at Google and Digg before joining the faculty there. She is an expert on scalable databases, secure software, cryptocurrencies, and online privacy.
---

# Episode 13: Neha Narula on Blockchain, Cryptocurrency, and the Future of the Internet
**Mindscape Podcast:** [September 10, 2018](https://www.youtube.com/watch?v=biVfTtZc9gk)
*  Hello everybody and welcome to the Mindscape Podcast. I'm your host, Sean Carroll. And
*  today we're talking about a subject that is near and dear to the hearts of most everyone
*  out there, money. We all know what money is, right? We use money, we exchange it for goods
*  and services, as Homer Simpson once pointed out. But we also get this feeling that the
*  notion of money is in flux right now. The notion of currency, the actual thing you give
*  to somebody, which used to be dollar bills, of course it's increasingly credit one way
*  or the other. And these days there's this talk of cryptocurrencies like Bitcoin and
*  Ethereum and so forth. Somehow the computer scientists have gotten their hands on money
*  and the world might never be the same. The question is, how is this new world going to
*  look? If you followed the Bitcoin situation at all, you know there's a bit of instability
*  in the system. Bitcoin was supposed to be a way that people could use it as money to
*  exchange for things on the internet, but the actual value of Bitcoins has been fluctuating
*  wildly. If you were really, really good and bought it very, very cheaply early on, you
*  could have made an enormous amount of cash, good old American dollars, if you had sold
*  it at the right time, but now it's on its way back down. This doesn't sound like something
*  that we could reliably use as money. But the hype is not from nowhere. There's reasons
*  why people are very excited about cryptocurrencies. So today's guest is Neha Nerula, and she's
*  the one to talk to you about this. Neha is the director of the Digital Currency Initiative
*  at MIT, and she's an expert on not only cryptocurrencies, but wide scale, scalable computing, online
*  security, things like that. So we're going to actually sit down and talk about what the
*  blockchain is, this technology that some of you are, I'm sure, super experts on, but
*  other of you don't quite know what's going on. So you will. By the end of this episode,
*  you'll understand the blockchain. There may be talk of hash functions. It's a crazy world
*  out there. We need to understand some new concepts, but that's okay. It will all make
*  sense after this hour, and it matters, not just for money, but for the future of the
*  internet, which affects us in a number of ways. The internet more broadly has gone from
*  this kind of wild west individualistic view that we had back in the 90s, let's say, to
*  a set of mega platforms, Facebook and Google and Amazon and Twitter, that seem to control
*  an increasing fraction of what goes on online. So the same technologies that are behind cryptocurrencies
*  might someday help bring back the situation where things were a little bit more individualistic,
*  a little bit more decentralized, and that could have crucial impacts on how we use the
*  internet a decade or two from now. So let's go.
*  Great. Neha Nerula. Welcome to the Mindscape Podcast.
*  Hello.
*  So I'm going to be even more than usual asking the dumbest, silliest, most straightforward
*  questions, because I think we're going to talk about sexy stuff, right? Cryptocurrencies,
*  Bitcoin, distributed computing on the internet and privacy and things like that. And this is
*  very important stuff, but it's also stuff where jargon gets in the way very, very quickly. So
*  I'm not going to be embarrassed. I'm going to play the village idiot and ask silliest questions.
*  So let's start with what is money? Let's just get right to it.
*  You know, honestly, I'm getting more and more convinced by the day that no one really knows
*  what money is. It's a very, very confusing topic. And the more I read about it, I think the less I
*  understand, which is not a great sign. So economists define money as having three qualities. It is a
*  unit of account. We use it to price things. We say how much things are worth in terms of money,
*  in terms of dollars, for example, as a medium of exchange. So we use money to buy things, to
*  make exchanges, to transact and have an economy. And then the third way, the third sort of property
*  that defines money is as a store of value. So we use money to store value. You know, we work and
*  get a paycheck. We put our paycheck in a savings account. That's money. So that we can use that
*  money for a rainy day. So that's sort of the technical definition of money. Now,
*  That was excellent, by the way, I didn't expect you to have quite such a very detailed answer,
*  right on the bat. But I guess as are you what I do, I know. So is there an economics angle to
*  your sort of training and interest? Or is it more great question? I am a computer scientist, right
*  background, and I did not have any economics training, but you kind of have to sort of,
*  you know, start to crib a little bit together. And so I would say I'm still very early in that
*  process. But you know, I can quote a couple things that economists might say,
*  So you've been picking it up on street corners?
*  I've been trying to, yes, learn economics on the street. That is a great way of describing it.
*  Street level economics. So, you know, you know, yeah, talking to your friendly neighborhood
*  dropout or something like that. That's what's been going on. So, so, you know, so that's like the
*  economist definition, which is one way of looking at it. Another way of looking at it is money is
*  the way I like to say, talk about it is that money is a story. So money is a story that we
*  tell ourselves. You know, I, let's say I'm pulling a $20 bill out of my pocket right now. Why does
*  this piece of paper mean anything? Why is it worth anything? It's worth something because we, we tell
*  a story to each other about why it's worth something. And we all sort of believe in that story.
*  And we interact as though that story is true. That story being that this $20 is worth, you know,
*  approximately, I don't know, maybe a nice lunch somewhere's worth of value. And, you know, if I
*  give it to you, you can go buy a nice lunch somewhere. And with that money, that person can
*  go buy something else somewhere. So, so money is a story that we tell each other. And we've all sort
*  of agreed to use certain objects or pieces of paper or ones and zeros and certain databases as
*  accounts for how much money we all have. And we use it to transact. And it's very much based on
*  sort of an absurd level of trust between people who've never met each other, right? You know,
*  walk into a store, hand a piece of plastic and walk out with stuff. Exactly. It's kind of amazing
*  when you think about it, right? You know, that I can interact with someone I've never met before,
*  might not even like, might not trust at all. And yet we can have a transaction. And, you know,
*  a transaction that would normally require a relationship, maybe weapons or something to
*  back it up. We can have a transaction because of things like money. And so it's really a very
*  powerful thing. It's something that society really needs. And it facilitates sort of the exchange of
*  value in our economies. And there is at least this one major split between the idea of using
*  something for money that has an intrinsic worth, right, like gold or silver or whatever, versus
*  using more abstract notions of money. Well, I'm going to push back on you a little bit there
*  because this intrinsic worth thing is actually a really interesting question. And, you know,
*  a lot of people do see it that way. They're like, okay, I get it. Dollar bills, those are paper.
*  They're not actually worth something. Something's printed on them. And that's why I think they're
*  valuable. But gold, gold is actually worth something. Why is gold worth anything? You know,
*  it's like, it's turtles all the way down is what I got to say. Like, you know, gold is not actually,
*  doesn't have intrinsic value, which equates to the amount that it's worth in our society today.
*  Yes, you can use gold as, you know, in some electronics. Yes, we like to wear gold rings
*  on our fingers sometimes. But really, gold is another story that we all tell ourselves.
*  We've all decided for a very, very long time that gold is going to be a measure of wealth for us,
*  that we're going to use it to store value. And so that's what it is.
*  Well, that's great. Because I think that actually a theme of many of the conversations I'm having
*  is taking ideas that you might naturally think of as very, very different and seeing that they're
*  actually kind of blurry between them, right? And you're pointing out that there isn't really any
*  cut and dried thing called intrinsic value. Different people might value even, you know,
*  bread or water very differently from each other. Yes, yes, that is very, very true. You know,
*  things have different value to different people, things like art, you know, of course, it's
*  incredibly different value to different people. We try to negotiate that using prices and value
*  and things like that. But sort of, you know, thinking about things like gold and silver and
*  whatnot, they're precious metals that have certain properties that make them convenient to use as a
*  store of value, but that doesn't make them inherently valuable. So in some sense, the very
*  idea of money has a bit of arbitrariness built into it or a bit of convention built into it.
*  And we shouldn't be afraid of that. We should figure out how to use it. Is that okay?
*  Yes, I think that we shouldn't be afraid of it. We should acknowledge it. I mean, I'm a big
*  proponent of acknowledging the truth instead of trying to ignore it. And we should acknowledge
*  it, we should note it, and we should, you know, not try to hold things like, you know, other forms
*  of money to a different standard. Right. And in fact, this morning, I have to, you know,
*  share this with the podcast audience out there, because we're at this wonderful little event
*  called Kent Presents, where we, you know, a lot of people give talks to an interested public,
*  and you made a billion dollars this morning within a few minutes. Can you tell us by what magic you
*  did that? In theory, yes, I did. I obtained a very high market capitalization. So yes, I can explain
*  how I did that. So previously, what I'd done is I'd spent about five minutes creating something
*  called a smart contract on something called a cryptocurrency called Ethereum. So I created my
*  own token out of nowhere, basically. So I decided that there were going to be a billion of them.
*  I was going to name them Neha shares, you know, the shares of me, there's a billion of them.
*  And I created them, I willed them into existence. And then they don't correspond to a billion things
*  out here in the world. You just sat down and said billion. Yes, I just sat down and said,
*  I'm making up this thing called Neha shares, and there are a billion of them. And I so I deem it to
*  be. And nothing so prosaic is actually real things, you know, that's just ridiculous.
*  So it just so happens I'm keeping track of these Neha shares somewhere on the internet. And then I
*  went in front of this audience here at Kent Presents, and I said, would any of you be willing to buy a
*  Neha share from me for $1? And lo and behold, I think there were three people who raised their hands,
*  you know, my shares weren't worth that much, but some people are willing to sort of take a chance.
*  And with those, if I made those three sales, then given the fact that there are a billion Neha shares,
*  and I just sold three of them for $3, well, that gives me a market cap of a billion dollars.
*  A billion dollars right there.
*  A billion dollars right there.
*  You attempted to cash in right away?
*  You know, I was I was going to go get some VC money, actually, and see if I could up that a bit. Yeah.
*  Well, it again, I think it's good because it helps tear down a little bit of these artificial
*  distinctions we draw. So the same thing could be said of the stock portfolio in your retirement
*  fund, right? You say you think you're worth a certain amount of money. Well, that's because
*  you think people would pay you that amount of money for those shares. And even if you just have
*  cash under the mattress, you still are trusting that it has some value in some market.
*  Exactly. The reason I like that example so much is because first of all, it pokes fun at, you know,
*  crazy high market caps of startups or cryptocurrencies or whatever, right? It's
*  the last share you sold and you multiply that times the number of outstanding shares.
*  But also, yeah, it just makes you realize that I've always thought of something I've I used to
*  always think of money as being sort of static, right? Like if I had $1,000, I had $1,000.
*  If I didn't spend it, I would have the same amount tomorrow. And in fact,
*  you know, the world is a bit of a harsh place. And it is actually very difficult to store value
*  and to really ensure that it's going to be worth the same amount tomorrow. And so, yeah,
*  your stock portfolio could crash tomorrow. You know, even if you're storing things in dollars
*  under your mattress, maybe there's some great financial calamity and the the euro dollar ratio
*  changes dramatically. And all of a sudden, you can't import that nice Swiss cheese anymore.
*  All these things are sort of floating and ephemeral, and they're very difficult to pin down.
*  It's not even unrealistic worries, right? Hyperinflation has been known to wipe out
*  fortunes. It happens. It's happening right now in different countries.
*  Yes. Yeah. So what are some of the problems with the current system when it comes to money,
*  in terms of how useful the current system of cash and credit cards and so forth is in
*  doing the exchanges we want to do around the world?
*  Yeah, so I think some of the the so there's definitely problems with payments. I think
*  that the bigger problem lies in who happens to hold most of the wealth in the world and who
*  doesn't. We live in a pretty unequal society. It's tremendously unequal. In particular,
*  about 12 really large investment banks basically kind of run things.
*  Really?
*  Move around trillions and trillions of dollars worth of value every day. And it's kind of insane
*  when you think about the fact that some people make decisions, like where to go to college,
*  right? Well, I can't afford that school, so I'm going to go to this other school that maybe isn't
*  as good for me. And we're talking maybe thousands of dollars of difference or tens of thousands into
*  an investment bank that's like a rounding error. And so when I started to really unpack what was
*  value, what was wealth, what was money, realizing that all of this was true just made me think,
*  what is going on with our financial system such that someone can graduate college with
*  hundreds of thousands of dollars in debt that they can't get rid of, that Puerto Rico is suffering
*  from this massive hurricane and owes all this money to its bondholders. The world is just a
*  really strange place and it really made me feel like we needed to kind of upend things a little
*  bit. We really needed to think about is our financial system working for us? Does it make
*  sense? Is this the way that we want it to work? And if the answer to that is no, and I think the
*  answer to that is no, then how are we going to change it? And you point specifically, I guess
*  I was a little bit surprised again, not an expert in any of these things, but to investment banks
*  rather than Amazon and Apple and Alphabet or Petrodollars or Russian oligarchs. So it's really
*  the investment banks you think where the wealth is concentrated in the current system?
*  I think that they happen to have a lot of power in the current system. Yes, I think that they do.
*  A lot of expertise as well. Yeah, I think when we're talking about, sure, we can talk about
*  Google and Apple and Facebook and all the problems with their platforms and user data,
*  and those are really big problems. Yeah, we will. Okay, good. Those are also really big problems,
*  which maybe this technology has a chance of affecting, I don't know. One thing at a time,
*  we can't fix the whole world right at once. So what do you think about, okay, so there's problems
*  with that, obviously, inequality, I completely agree with you. Also problems, I gather, you know,
*  in certain parts of the world or whatever, there's just sort of friction in the system. There's too
*  much of a barrier to using cash in the easy way that we're used to here in the US, for example.
*  Yeah, definitely. So I think there's a lot of places in the world where people just quite simply
*  don't have access to digital financial services. It just doesn't exist. One of my colleagues liked
*  to talk about a place in South America where someone had to get in a canoe and canoe really
*  far to get to a town and maybe the bank was open, maybe it wasn't open, and it was just this really
*  arduous, horrible experience to get access to financial services like loans and savings
*  accounts and digital payments and things like that. So that is definitely a huge, huge problem.
*  I think that the general statistic that's thrown around is that there are about 2 billion unbanked
*  people in the world. So that's an issue. Some people don't like to use the word unbanked
*  because it implies that people should be banked, you know, and that's not 100% clear, but the basic
*  ideas don't have access to financial services that might be helpful for them, that might help them
*  improve the quality of their lives. So that's a major, major problem. And the reason that these
*  people don't have access to these financial services is because no institution has deigned
*  to give them access, right? And there are different reasons for that. It might be incredibly expensive
*  in order to reach these people. It also might be the case that it's too confusing to understand
*  how to sort of value the credit worthiness of these people. So there are a lot of different
*  reasons, but the simple fact of the matter is no access. And I think we need to change that.
*  All right, so we've identified the problems. What are we going to do about them? You are, you know,
*  the leader of a digital currency initiative as I take it. And so maybe your answer has something
*  to do with digital currencies. Yeah, it might just have something to do with digital currencies. So
*  to be clear, and I want to state this upfront, it's not that I necessarily think that this is
*  the absolute answer to all of these problems. That is probably not true. It's more that I think it
*  might be part of an answer to these problems. And even that is to me, good enough reason to
*  work on it and to try to try to make this stuff happen. I've heard a lot of stories about people
*  who have used cryptocurrency to solve some of their problems. And the stories have been very
*  moving, actually. People who know at this point in time, most of the stories I hear are about
*  they fall into sort of one of two categories. One category is I earn money in one country and I
*  want to put it in another country. And by using something like Bitcoin, I'm able to do that much
*  more cheaply than I would otherwise. So remittances, cross border payments, that type of use case.
*  The other use case that I hear about is people from countries who, where their currency is
*  under capital controls or it's getting hyperinflated. And this offers them a means of
*  taking the wealth that they've accumulated and getting it out before it disappears.
*  So it's about wealth preservation. Do you have a specific moving story that you have in mind when
*  you're thinking about this? Great question. So in the first category, there was a gentleman who
*  lives and works in Nigeria and needs to come to Boston occasionally. And there just wasn't really
*  a great way for him to move money every month from Nigerian currency to American currency.
*  It was complicated and extremely expensive and it just didn't work. And Bitcoin was a solution for
*  him. For the wealth side of things, I have a friend who runs a cryptocurrency company called Zappo and
*  he's from Argentina. And so he went through, he saw sort of that happening in Argentina. And it was
*  really powerful for him and he really saw a lot of potential in cryptocurrency and that's why he
*  works on it today. All right. So we're at the point where you now have to tell us what a cryptocurrency
*  is, what Bitcoin is. There's something called the blockchain. We have danced around it. Tune in for
*  this. Yes, here we are. So great question. So where do we start? I like to start with Bitcoin
*  because that's how it started. And chronologically, I think is a pretty good way to try to describe it.
*  So in 2008, this shadowy figure on the internet known only as Satoshi Nakamoto sent an email to
*  a mailing list and said, hey, I have this idea. I'm calling it Bitcoin. And Satoshi Nakamoto,
*  he, she, they, we have no idea who this person or persons, who they are, then released a white paper
*  describing Bitcoin and explaining the idea behind it. And the idea behind it was peer to peer payments
*  without any bank or government or other institution facilitating those payments.
*  It's very Neil Stevenson, right? It's very science fiction novel, like some shadowy figure who no one
*  knows what they are. Stars of revolution. Such a great movie one day. I can't wait for the movie
*  version of this. Aaron Sorkin, if you're listening. Think about it. Have your people contact us.
*  So, so right. So, so then a few months later, Satoshi actually produced working code. Satoshi
*  said, Hey, I've programmed this. Here it is. I'm running it. If you would like, you can run it too.
*  And we will be part of the same network. And that will be Bitcoin. And so people on this mailing
*  list were like, Hey, this is kind of neat. Okay, fine. Oh, and by the way, if you run this, you get
*  Bitcoin by just by running it. You know, you are your computer is going to sort of spin and do a
*  try to solve a little problem. And every time it solves the problem first, it's going to get a bit
*  of Bitcoin. And so people started doing it. They started this process is called mining. They started
*  mining Bitcoin. And then, you know, this progressed for about three years or so, I would say. And then,
*  maybe it was two years anyway, a few years, right? It was just sort of this toy. It was this
*  weird thing that some people on the internet were playing with and were using and were liking. And
*  actually, this goes back to the stories, they were all telling themselves a sort of story about it,
*  right? This was a an unhackable form of money. This was money that no one could take from you.
*  It was purely based on mathematics. It was, you know, it was a very pure form of internet money.
*  And then what happened next was, and this also happened on the internet, some guys said, Hey,
*  I'm hungry. I would like to buy two pizzas. If you send me two pizzas, I will send you
*  40,000 Bitcoin. And this is what's known as the first exchange for Bitcoin for something of actual
*  value. The first time someone bought something. Two pizzas, two pizzas, 40,000 Bitcoin. Brilliant.
*  Yeah. Why am I not on these mailing lists? So, so what happened? Somebody in London sent this guy
*  two pizzas. He was in Florida and he sent him the other guy 40,000 Bitcoin, which let's not talk
*  about how much that's worth in today's amount of money, tens of millions of dollars. So, so
*  those pizzas were delicious. I think it was Papa John's. Oh, well, sorry. So, so that was the first
*  time that yeah, Bitcoin was actually exchanged for something. And that was the first time that
*  you could really say, this is how much a Bitcoin's worth, you know, take the cost of a pizza divided
*  by 40,000. And then it just sort of went on this crazy ride of gaining value and losing value. And
*  it was all about, you know, it was all about the story of Bitcoin and what's it for and what, you
*  know, how do we use it and what does it mean? And since then there's been even more cryptocurrencies.
*  I think there are thousands of them out there right now. And in part, a lot of that is about
*  experimentation, people sort of trying out different ideas, trying to see what makes these
*  things work and what makes this doesn't work, what doesn't work. But going back to sort of
*  the question about, okay, there's Bitcoin, there's cryptocurrency. What is a blockchain?
*  Well, in Satoshi's paper, Satoshi talked about a chain of blocks and underlying-
*  Now I understand.
*  Oh, yeah, totally. It's just a chain of blocks, right? Makes so much more sense now. Bitcoin,
*  coin made of bits. Done. What's so confusing about all of this? So Satoshi talked about sort
*  of the structure of this ledger. So the idea behind Bitcoin was remember, Satoshi said, hey,
*  I'm running this code. Anybody else want to run it? Here it is. Anybody could download and run
*  this code. Anybody. You could download and run it right now. It's still the case. Anybody can
*  download and run this code, join the network and start being a part of Bitcoin.
*  Sorry, the code to do what?
*  There's, well, the code to try to create blocks and to download the blocks other people have
*  created, check them to make sure they're correct and sort of facilitate the transfer of your Bitcoin.
*  And so for, is there one blockchain for each currency? So there's one blockchain for Bitcoin?
*  Kind of. So at its heart, the blockchain is a data structure. It's a ledger of transactions.
*  Bitcoin has its own blockchain. There's one blockchain for Bitcoin. However, there's something
*  called forking. Basically, someone can decide to divide the network up and basically create a copy
*  of Bitcoin, new network, new ledger. Speciation. Another blockchain. Yes. It's like a creature
*  just divides itself into two. That's basically what happens. So then there's another blockchain.
*  So then Bitcoin is, this has happened to Bitcoin several times. There's a few variants of it.
*  There's Bitcoin cash, Bitcoin gold, Bitcoin platinum, da da da, on and on. In addition to that,
*  there are other cryptocurrencies that do have their own blockchains like Ethereum is another one.
*  Litecoin is another one. Zcash is another one. And then this is where it gets really confusing.
*  There are ways of building tokens on top of other blockchains. So this is actually really common
*  with Ethereum. And this is what I did in the talk this morning at the conference where we are.
*  Ethereum is a little bit different than Bitcoin. Whereas Bitcoin is a ledger of transactions,
*  Ethereum is kind of more like a global computer. It doesn't just handle transactions,
*  which make payments. It handles something called smart contracts, which are like little programs.
*  You can write a little program and throw it on the Ethereum blockchain. And then that little
*  program will execute. And so one very, very popular type of program is one in which you can
*  create your own token. And a token is? And a token is just like those Neha shares, something that
*  someone makes up. It's digital. It doesn't exist in the real world. There's hopefully a limited
*  amount of them that are in issuance schedule that's controlled programmatically. And it's like a
*  digital credit. Sometimes they're made in a context where the idea is that they're supposed to
*  correspond to something. Right. I was going to say at some point, just like the pizzas,
*  they have to be assigned value. Yes. And so sometimes that's done by, again, the story we
*  all tell ourselves, like as it happens with money. And sometimes that's done because there's somebody
*  sort of behind it saying this token is going to be worth something. For example, Starbucks points
*  might be thought of as tokens, right? Or airline sort of frequent flyer points. Yeah, exactly.
*  So there are a lot of people these days who are developing their own networks and are creating
*  tokens to go along with those networks and sort of suggesting that people will buy tokens in order
*  to use whatever service that network provides. Okay. This is great. And I want to come back to
*  it. But I definitely want to get this blockchain stuff completely understood. So in some sense,
*  the blockchain, let's just take the particular blockchain for your favorite Bitcoin fork, right?
*  So just one blockchain. So it's a set of ones and zeros, right? It's a file. Yeah. Except it's not
*  just one file. It's a file that exists on many computers at once. Yes. Is that right? Yes. And
*  whenever any transaction happens with Bitcoin, you add that to everyone's file, right? Yes. And
*  then there's a way of sort of checking that no one's cheating. Yes, that is exactly what happens.
*  So this computer network is every computer in it, every node in the network is keeping a file,
*  just like you said. And that is an append only file. And what you do is you add transactions to
*  the end of that file. And that file is a copy of a ledger that everyone's maintaining together.
*  The reason it's called a block chain in particular is because instead of adding transactions one at
*  a time, you group them together in a set, and then you just stick the set onto the end of the file.
*  And that's called a block. It's a block of transactions. So it's just sort of like a
*  batching mechanism. You just put them together in one chunk. The reason it's a chain is because
*  each set of transactions, each block points to the one before it. So it's kind of it's like this
*  list, this it's like a linked list in computer science terminology. And what this serves to do
*  is it makes the blockchain tamper proof, right? You can't go back in time and fiddle with the
*  transactions. Because if you do, you're going to mess up all the pointers. And the pointers aren't
*  going to work out correctly anymore. And that's going to be very obvious to everyone, they're
*  going to notice. And also everyone else's, if you try to do anything to the blockchain,
*  it's just automatic that everyone's file updates? Great question. So this is where this process
*  called mining comes in. So in order in Bitcoin in particular, in order to create a new block,
*  a new set of transactions, I myself, for example, might be doing this, I'm going to gather a bunch
*  of people's transactions together, stick them in a block, and then try to solve a random numeric
*  puzzle. That's what I'm going to do. And this was Satoshi's idea, right? This was Satoshi's idea.
*  This was Satoshi's idea. He or she or they had this idea that what will happen is we'll all sit
*  there and our computers will spin trying different random numbers. And the way I like to think about
*  this problem is imagine you have, let's say you have 10 dice, okay, and you're going to throw the
*  dice. And let's say, you know, you throw the dice once, maybe a number is repeated a couple times,
*  but you know, probably you're going to get sort of a random assortment of numbers each time.
*  Now let's say I told you, if you throw those 10 dice and you get all sixes, then you win the game.
*  That's winning the game. That's kind of the puzzle that everyone's trying to solve on their
*  computer. It's like they're throwing dice, generating random numbers until that number
*  looks a certain way. And once they do that, they publish their answer and people check it to make
*  sure that they actually did this right. And that is the process by which several different things
*  happen. First of all, that set of blocks needs that special random number attached to it in order
*  to be a valid block in the blockchain. And then second, the fact that I generated that random
*  number allows me to create new Bitcoin out of nowhere according to a schedule that is set in
*  the computer program. So this is the process known as mining, Bitcoin mining.
*  Who made up the puzzle? Who knows what the right answer is? Is it unknown or is it universal?
*  So everyone knows sort of the sketch of the problem, right? And it's actually
*  something called finding the pre-image of a hash. So there are these things called hash functions
*  in cryptography. And what they do is they take a large amount of data and they map it onto a
*  fingerprint. So it's a way of sort of fingerprinting data. Now, when you do that, the fingerprint comes
*  out looking sort of random. By fingerprint, we don't mean a set of swirls on a piece of paper.
*  We don't. We mean some ones and zeros. We mean ones and zeros. We mean another little chunk of data.
*  Another chunk of data. So you take a big chunk of data like a PDF or an email or a picture and you
*  feed it through this hash function. And what comes out the other end is a short string that is sort
*  of very uniquely tied to that piece of data you put inside. And it's shorter than the original?
*  Much, much shorter. It can be much, much shorter than the original. It can be the same size as
*  the original. And so what this does is it serves to sort of like, you know, if I take a picture and
*  put it through a hash function and fingerprint it and create this sort of hash that describes
*  the picture, that summarizes it in a way, then that means if you show me a different picture,
*  I can hash it and see that the hashes will turn out different. So hash functions are used to sort
*  of uniquely identify big chunks of data. That's why I call them a fingerprint. Because a fingerprint
*  is kind of like a unique representation of me. Except, sorry to keep interrupting, but if
*  a big file gets hashed into a small file, then mustn't it follow that multiple big files would
*  give you the same small file? Yeah, now you're, now you're got to get into the details, Sean.
*  I'm a physicist, yes. Yes, this is very true. This is absolutely, absolutely true. In fact,
*  this is the case that for any sort of single hash or fingerprint, there are many, many, many, many,
*  many things that will hash to that thing. Okay. But a property of a hash function is that it is
*  extraordinarily difficult to find something. So just given the short string, the hash, the fingerprint,
*  it is very difficult for me to work backwards from that to something that will hash to that value.
*  That difficult problem is exactly what's going on with Bitcoin mining. So what's happening is
*  your computer's trying different large, different strings over and over and over again to see if
*  they produce the right kind of fingerprint. Okay. In fact, produce a short string with a lot of
*  zeros at the front. At this point in time, I think given the way Bitcoin mining works, you need about
*  like 70 zeros in the front. That's actually a really hard, hard thing to do. But someone knows
*  the hash function. The hash function, everybody knows the hash function. The hash function is
*  called SHA-256. I see, but inverting it is hard. Inverting it is extraordinary. You can know the
*  hash function and that still, you still can't invert it very easily. And this is just a miracle
*  of math. This is a really cool property of math and cryptography. Yes. And so Satoshi is the one
*  who picked SHA-256 as the particular hash function that we were going to use for Bitcoin. Good. And
*  so when someone, so the mining that we always hear about is people, it used to be individuals
*  on their little laptops, now it's gigantic farms in China and elsewhere, chugging through little
*  tiny fingerprints trying to reconstruct what they were hashing. Yes. So what's, and it's worth
*  talking about that a little bit. Yeah. So when Satoshi started, he or she, or they thought that,
*  oh, great, everyone will run this on their computers. And, and, and, you know, computers
*  are pretty powerful. You can check, check a bunch of different combinations of data to see if they
*  produce the right hash, and then we'll all run Bitcoin together on our computers. Now, what ended
*  up happening is that, you know, clever people realized that it was possible to develop specialized
*  hardware that could do this faster than people's laptops. And if they could do it faster, that
*  means that they had a better chance of finding the answer first and winning the Bitcoin that
*  comes out of this process. And so this kind of started an arms race of crazy hardware development.
*  And now there are these machines called ASICs, Application Specific Integrated Circuits, that
*  can solve this problem millions of times faster than your laptop can. And you basically, you can't
*  mine in the Bitcoin network effectively, unless you have one of these machines and different
*  cryptocurrencies actually use slightly different hash functions. So some use SHA-256, others use
*  different things. And it's very interesting because in Nvidia, a lot of people have been buying
*  GPUs to mine cryptocurrency. And so Nvidia was like, who's buying all of our GPUs? And what's
*  going on? Why is the price going up? This is the computer circuit company, right? Yeah, yeah.
*  They make the graphics processing unit that goes on your computer. It's frequently used for gaming.
*  You need to buy like a fancy GPU in order to render your video game nicely. So you can choose the bad
*  guys. And so lo and behold, cryptocurrency enthusiasts are competing with gamers and
*  driving up the prices of GPUs, which I find very funny. Two very devoted fan bases for different
*  reasons. But okay, that was extremely helpful. But let's bring it back down. So the blockchain,
*  so this is how we make, so what do we call it when we successfully mine? We got a Bitcoin?
*  You mine to block. You mine to block. Yes, yes. Okay. And what is stored on any individual
*  computer in the network is the entire blockchain, right? The whole thing, yeah. So in the spirit of
*  asking the dumb questions, doesn't it get really big? It's about 150 gigabytes right now. It's
*  pretty big. You don't actually have to store the whole thing. You just kind of need to get it and
*  verify it. And then once you catch up, you're good. You can kind of throw it away. So there's that.
*  You don't have to keep it forever. You just have to process it. Also, you know, it is entirely
*  possible. There's a thing you have to remember about this space is that it's still pretty early
*  on. We're still at the beginning. Bitcoin was the first cryptocurrency. And yes, in Bitcoin,
*  you have to keep a history of every transaction that ever existed. But there's people working on
*  really cool ideas that let you do things like keep a constant amount of space that proves that you've
*  looked at every transaction that's ever existed and verified it. So, you know, the way I like
*  to think about this, I like making an analogy to cars. So in the early 1900s, cars were very clunky,
*  very slow, used a lot of gas, horses were faster than cars. But, you know, they got better very,
*  very, very quickly. And I think cryptocurrencies are kind of the same way. Yeah, there's a lot
*  of problems right now, but we're still working on them. And I think there are I see solutions in
*  sight. And this drives home the message that we started with really. So you you've mined a Bitcoin,
*  well, you find a block and you get rewarded with some Bitcoin when that happens, right?
*  And basically, I could translate that statement into you have solved a math puzzle, your Nvidia
*  card on your computer has solved a math puzzle, and the rest of the world agrees to then
*  exchange some little information you have for money. Yeah, of course, the amount of money seems
*  to change from day to day. But that's basically it. You have this piece of information that
*  verifies that you solved this puzzle. And we'll give you hundreds of dollars for that. Well,
*  we'll give you I think right now it's 12.5 Bitcoin for that. Yes. However many dollars that is,
*  might change by the time this podcast is definitely get something. Yes. Yes. Okay. And so
*  what makes this so great? Well, yeah, there's a there's a way to for people around the world
*  to agree on some token worth some value. Why is that better than good old American dollars?
*  Great question. I think they're both pretty great. One or the other, you know. So, so first of all,
*  one thing that wasn't immediately obvious to me, but I realized later was Bitcoin was the first time
*  that people made digital payments without a bank. Without a bank. That's a crucial point. Without a
*  bank. It's like almost going back to bartering. It is. It's going back to something that's very
*  sort of peer to peer, very sort of, you know, you don't need this very highly regulated,
*  structured institution that does very specific things in the middle. You don't need that anymore.
*  You can do digital payments without a bank. So that in itself is pretty cool. Like you probably
*  want to know, well, like, so what, right? Digital payments through banks, they seem to work fine.
*  You know, we've survived this long. And I think that that's very true. In a lot of cultures and a
*  lot of different societies, digital payments through credit cards and banks are fine. The fee
*  we have to pay is kind of annoying. You know, well, actually merchants pay it and then they
*  pass it on to us. We don't think we pay fees for credit cards, but actually we're paying for it in
*  the goods that we buy. The fee around 2.7%. You know, could it be lower? I don't know. Maybe
*  cryptocurrencies could help push that fee a little lower, but that's not really groundbreaking,
*  right? Saving like a percent here and there. But, you know, I think what's really is kind
*  of groundbreaking is going back to what we were talking about earlier. There's so many people in
*  the world who just don't have access to digital financial services. And this is a way that if they
*  can get an internet connection, they have access. Bam. Done. They don't need a bank to sign them up.
*  They don't need to be KYC or AML. They don't have to have a minimum deposit size or a certain type
*  of identification. They can just start doing it, which is kind of neat and reminds me very much
*  of another piece of technology, which is sort of what we call permissionless, which is the internet.
*  It's another thing where you can kind of just start using it. And just to get the, excuse me,
*  the technical detail right here, as I understand it, if you own some cryptocurrencies and Bitcoin
*  or Ethereum or whatever, you have a number that you're supposed to not lose. And if you lose it,
*  it's lost. It's no longer yours. And the number I read on the internet was $20 billion is estimate
*  to have been misplaced by people losing their addresses. What are they called? What is the
*  phrase for these? The private key. Yeah. Yeah. Yeah. We're still figuring this all out. This
*  it's not ready for prime time. I keep trying to tell people this. You're absolutely right. So,
*  yeah. So this is called public key cryptography. And it was actually invented in the seventies.
*  And it was invented at MIT. One of my, a professor I work with occasionally named Ron Rufest was
*  pretty critical in its invention. And it actually, it's used on the internet in so many different
*  places. Public key cryptography is critical for security, for hiding information and for
*  proving the integrity of information. So the way that it's used in cryptocurrencies is as follows.
*  People have a private key and a public key and you can generate these on your computer
*  to sort of randomly kind of throw some randomness in there and you get these two numbers out
*  and they work together. So normally when I log on to a service on the internet,
*  I type in my password, right? So my password is something that I should keep secret. I'm not
*  supposed to show it to anybody, except I'm supposed to type it into a form and then send it over the
*  internet to this company. That's the way password works. A password. This is not how public key
*  cryptography works. The way that this works is I have two pieces of information. One's public and
*  one's private. The private one I never share with anybody. I never, ever, ever, I'm not supposed to
*  ever give anyone my private key. I use my private key to either digitally sign things. So like
*  producing a signature or to encrypt things, digitally encrypt things, meaning sort of like
*  mask them. And then people use the public counterpart to that, my public key, to either
*  validate that the signature came from me or to encrypt stuff for me. So actually I use my private
*  key to decrypt things. So this is how these two pieces are used together. It's a very different
*  way of thinking. It's very different. And so yeah, when you're working with a company or a website on
*  the internet, if you lose your password, no problem. You can call them up. You can click the
*  password reset button. They'll reset your account for you. You have to remember the street you grew
*  up on or whatever. Exactly. Your first cat. They have all sorts of annoying questions. They will ask
*  you to confirm it's you, but they have a way to reset your password, give you access back to your
*  account. That's because there's a company with a list of all the accounts and they can do that.
*  They can go into their database and they can just flip something around. With cryptocurrencies like
*  Bitcoin, there's no company. Everybody's computers are running these things. It's this distributed,
*  decentralized system. And so if you lose your private key, nobody's going to be able to give
*  that back to you and nobody can reset your account for you. That's kind of the point.
*  And so yeah, you're kind of out of luck if you happen to lose it or someone steals it. They can
*  steal your money, which is kind of a bummer. But like you get at, we're still in the process of
*  setting up what will be the more user-friendly interfaces for all of those. Yeah. And I think,
*  just to talk about that a little, I think it'll be layered. So yes, at the bottom layer,
*  there will be sort of this public-private key infrastructure. And if you ultimately lose,
*  sometimes you can actually use multiple keys. So you can kind of keep them in different places. So
*  like you can give your dad one and your brother another one, and then they can reconstruct it
*  for you. There's sort of techniques that you can use to make this problem a little less bad.
*  And what will happen is I think, yeah, there'll be companies that figure out how to use these
*  techniques and then they'll offer a service to users. And users will use these companies
*  to intermediate their access to the cryptocurrency. And places like Coinbase are trying to do this.
*  Yeah. Exactly. So Coinbase is probably the biggest cryptocurrency company. So you can buy and sell
*  cryptocurrencies through Coinbase. And this is a large part of what they do. They try to make it
*  easy for users. You don't have to worry about public keys and private keys. The thing is,
*  is that when you hold cryptocurrency through a company like Coinbase, you're not actually
*  holding it yourself. They're holding it. You have an account at Coinbase. It's a little bit more
*  like a bank. Like a bank. But yeah, but it's not sort of governmental currency that is ultimately
*  being owned. But it's the cryptocurrency. Yeah, exactly. And I think a lot of people
*  get confused between the difference between thinking of these cryptocurrencies as investment
*  instruments versus actual things you use to make payments. And in fact, it's still not that easy
*  to pay for things using Bitcoin or Ethereum. Oh, it's very difficult. It's kind of annoying,
*  actually. Yes. I've done it. But people invest in them and that may or may not be a good idea.
*  Yeah. Well, I think there's a few different things going on here, really is, first of all,
*  there are digital payments. And that was kind of the pitch of Bitcoin in the beginning was this is
*  a new form of making digital payments. But it's kind of a slow system for digital payments. I think
*  there's new technology coming that's going to make things a lot faster, but it's not quite here yet.
*  So, you know, still in its infancy. But then there's also this idea of, remember, we were talking
*  about Neha shares and me issuing my own token. There's kind of this notion of like, well, why
*  can't I just issue shares in myself or shares in my idea, right? Why can't I just create that out
*  of nowhere and allow you to invest in it? You get a share, you get a promise. And I think these ideas
*  are connected in a way because they're all about sort of disentangling the instruments of finance
*  from trusted institutions and the very intense regulation that goes around those institutions.
*  It's about breaking that apart and reimagining how we might do these things if we weren't so
*  encumbered, right? What I mostly want is a way to charge people 10 cents every time they listen to
*  a podcast episode. Is that something that digital currencies will help with or do we... I think so.
*  I think we're getting closer to that. Yes, there are. So one of the major problems with Bitcoin
*  is it kind of has high fees. You still have to pay fees. Yeah, exactly. So there's still friction
*  in the system even though that was the whole promise. And part of the reason for that is,
*  going back to it, remember, everyone's storing a copy of this ledger, right? So when I create
*  my one little transaction, it gets stored thousands of times around the world, which is
*  kind of a little excessive. I don't know if it needs to be stored that many times. And that's
*  costly, right? It costs money to pay for the bandwidth to move that around, to pay for the
*  disk space to store it, to pay for the CPU to validate it. And so, for good reason, it's a
*  little bit pricier to create a Bitcoin transaction. There are really interesting solutions coming down
*  the pipeline to help make all of that much, much, much, much cheaper. And I'm really excited about
*  this. And I think it will make it so that you can very easily take one-time 10-cent payments,
*  no problem. Or even maybe what you should do is you should charge people like a cent per second of
*  podcasts they listen to. So that's another idea. Oh, that'd be awesome. All right. Now you have
*  dollar signs. Yeah. Yeah. So if they're really interested, they'll keep going. They'll keep
*  paying. You can put all the juicy stuff at the end. Well, so what would you
*  say? I mean, there's been a lot of hype, right? A lot of speculation, a lot of promise about
*  these things. I can see how once things are up and running and a little bit more accessible,
*  these kinds of currencies will help people in different parts of the world get access to money
*  or even more than access to money, access to finance, right? Access to the ability to do
*  things with this kind of money. And hopefully the friction will be less. Like, hopefully the
*  transaction costs will be less. So what is the biggest way you see that this might change the
*  world if you're being in your most optimistic mood? Oh boy. Okay. Well, I mean- So we won't hold you to
*  it. Sort of, well, okay. I'll start with something abstract. So the goal that I work on and that my
*  group works on is we want to create what we call the internet of value. So what the internet did
*  for information, we want to do for the transfer of value. And so what I think in terms of platforms
*  and infrastructure, and so I want to create the platforms and infrastructure so that people can
*  build applications which move around value and sort of transform value and create contracts and
*  things like that. So I want to build the infrastructure that will let you really, really easily,
*  with a few lines of code or a service or whatever, start to take payments for your podcast, like tiny
*  little micro payments for your podcast. So I think that building that infrastructure, I don't even know
*  what people are going to do with it, but I think it could be really exciting, similarly to the ways
*  that with the internet, we didn't really know what people were going to do about it. We didn't know
*  that it was going to sort of facilitate Arab Spring or change the outcome of an election in
*  the United States or all the things that it did. I met my wife through the internet. Oh, that's great.
*  We read each other's blogs and that's how we got to know each other. Really? Yeah. Yeah. How far apart
*  were you guys? I was in Chicago and she was in Washington DC. And what was it about her blog
*  that... Well, this was the early go-go days of blogging in general and there weren't that many
*  physics blogs on the internet and most of them were written by physicists who are not very good
*  writers. So Jennifer is a professional writer and so she was writing about physics in a much more
*  charming way than most people. So I said hi and we exchanged questions about how to be a good blogger
*  and so forth. And then it turned out that we were going to appear at the same physics conference in
*  a few weeks and 12 years later happily married. That's adorable. You met on the internet. Yeah.
*  If the internet hadn't existed. I'm a big fan of the internet. I think it's good. I even like
*  Twitter. I think I'm the only one, but I think it's good. I also like Twitter. I love hate
*  relationship definitely, but lots of love there too. Yeah. So internet, bringing people together.
*  Love is one of the things that could come out of this. So abstractly, that's what I'm really
*  interested in. When it comes to sort of concrete specifics, I get a little bit more sort of,
*  I don't know, I think access is just a really big thing. Giving people access to financial services,
*  letting them build all sorts of crazy types of things with them. And there's also a very
*  dystopian view. So something I really worry about a lot are micro payments and what kinds of things
*  micro payments might facilitate. So to give you an example, right now, there's a lot of stuff that
*  we just get for free because it's not really feasible to charge for it. So sitting on a park
*  bench or a water fountain or things like that. There's a lot of sort of like public. I see where
*  this is going. Yeah. This could get bad. You want to charge a cent per second of your podcast. What
*  if someone wants to start charging who knows what, like tolls, for example, what if you paid,
*  always paid tolls and it's like every single mile you drove on whatever road and everything
*  sort of varied and it was very much like sort of this varied pricing and like the way that sort of
*  plane tickets kind of operate right now where people are charged very different prices depending
*  on time and availability. And it just feels really unfair. It feels really weird to have
*  that happen in our society. So I worry that if we create a world where taking payments and charging
*  for things, it just becomes orders of magnitude easier than what that might do. That's a little
*  scary. So you're saying that the ability to charge people to do anything has downsides.
*  Yeah. Yeah. All right. I can see that. Sometimes I think about, you know, is money really a good
*  thing? Is owning property really a good thing? I don't know. I start to get very a little crazy.
*  Yeah, that's when things start getting a little heavy. But to remedy that, maybe we can talk about,
*  you know, beyond money. There's this bigger philosophy of decentralization and on the
*  internet in particular, you know, and I know that you've thought about this a little bit.
*  Money is an example where there's a central authority who prints the money and decides what
*  the supply is. The internet was originally maybe at least in our retelling of it, sort of Wild West
*  libertarian frontier where individuals ruggedly did their thing. And now ever more, there are
*  gatekeepers. There are sort of mega platforms that rule everything. Is the blockchain technology
*  something that can move us back toward a more individualistic approach? Or should we just do
*  that anyway, regardless of the role of the blockchain? Yeah, that's a great question.
*  So the internet, yes, the internet definitely has this mythology attached to it of,
*  oh, anybody, you know, in the beginning, anyone could run a server, anyone could put their content
*  up, it was findable by anyone. Very much like that lovely story about you and your wife and how you
*  met you both, like put your content out there. You did. And you found each other, right? You didn't
*  have to be friends on Facebook. It was just you found each other through your ideas. And that was
*  sort of the promise of the internet. And now it is all mediated by these giant platforms. And we've
*  actually done quite a bit of thinking and writing about this topic, because there is a big push to
*  quote unquote, re decentralize the web. And what does that mean? That means lots of different things.
*  So first of all, people are very worried about the power that the central that the centralized
*  platforms have over our society over public discourse. There's algorithmic bias in the ways
*  that they operate their censorship. And, and people sort of feel trapped, you know, they there's
*  this feeling like, well, I don't really like Facebook, but I don't really have any other option.
*  Like, that's where exactly what am I going to do where I won't see photos of my nephew from
*  non Facebook, what it means to be monopoly. Yeah. And, and I think, really, the, when you look at
*  the way that cryptocurrencies operate, there's this it's, the protocol is very much not about
*  monopolies. It's about users, individuals owning their own data. And so people are applying those
*  ideas to the internet in general. And so there's been a big push to think about data portability.
*  What does that mean? That means, you know, I put a lot of content onto these services,
*  I should be able to get it out whenever I want at the click of a button, and I should be able to
*  move it. So if someone develops face planner, I don't know, some other competitor to Facebook,
*  right? Some new social network, I should be able to move my data out of Facebook, bam, into this
*  other thing, with the click of a button, and I should be able to, you know, another sort of next
*  step of that interoperability is even if I'm on a different social network, I should still be able
*  to interact with the people who stayed behind on the other social network. This is sounding very utopian right now
*  compared to the present. Yes, it is. It's the problem. It was the original idea behind the internet, though,
*  would use these interoperable protocols. And so everybody would be able to talk to everybody else.
*  So I think this is, you know, it does sound a little bit like a pipe dream, given the way that
*  things work right now. But people are trying to push things in this direction. And is the blockchain
*  playing a role there? Or is it simply sort of philosophically aligned? So some people will say
*  that the blockchain can play a role there. I don't, I'm not 100% convinced of that. I think it's more
*  of the inspiration. Right. But somehow the blockchain technology goes hand in hand with the idea of
*  privacy, security, being able to be ourselves, be recognized as ourselves. And that might help,
*  right? Yeah. Well, so there's a few different things at play here. So first of all, the public
*  key cryptography I was talking about is a way of me identifying myself that doesn't require any sort
*  of central registry necessarily. I can kind of like, it's a consistent sort of digital,
*  it can be a consistent digital identity. So that's- Until you lose it.
*  Yeah. Until someone steals it or you lose it. That's a whole nother conversation to start to
*  have. So that's kind of an idea of like, can I have a digital identity that is separate from
*  these services? And then another idea is this idea of decentralization. And in particular,
*  there's no central body. There's no one, you know, we're all coordinating together. We're all
*  working on this together and we're all, we're all figuring it out this, this together, because you
*  have to realize the way that cryptocurrencies like Bitcoin work is there's no, there's no like fence
*  around them. It's not the case, like with most sort of systems, when you think about protecting them,
*  you think, okay, there's going to be a firewall, a perimeter, and I'm going to keep hackers out.
*  I'm not going to let the hackers in. But if the hackers get in, if they cross the perimeter,
*  all bets are off. With Bitcoin, there's no perimeter. Anybody can get in at any time.
*  Bitcoin invites the hackers in, so to speak. The hackers are in there. They're all hanging out
*  with you, right? But it's designed in such a way that by using digital signatures, and by creating
*  this strange game of mining, the hackers won't be able to spend my money and they will be
*  incentivized to participate in a productive way instead of attacking the system.
*  So it sounds like, I mean, there was a time, very, very brief, when there were not only blogs,
*  but then there were RSS readers. Yes. So you could, I'm the only person, Jennifer and I are
*  the only people who still use RSS. You still use them. Every day. I try occasionally and just give up.
*  And for people who are too young to know what this was, you know, you would have blogs or other news
*  services, whatever, and they would have a feed and you could choose what sources to let into
*  your feed. So I can read both like my friends' blogs and the New York Times in the same platform.
*  And you could imagine a way better version of that, because the technology has not been improved
*  really for a decade, that was the equivalent of Facebook and Twitter and the New York Times and
*  your friends' pictures and whatever. And controlled by you. Right. And yet you can, you know, I think
*  that what people realize is this is not a way to make money, right? Under the present system.
*  And I think that's one thing. I think the other thing is, of course, a slight level of technological
*  sophistication is required to jump into that and navigate it effectively. And Facebook, you know,
*  for all its terribleness, made it really easy for everyone to go in and post their pictures.
*  Yep. This is a big problem with decentralized systems. They are very hard to use. And if there's
*  no giant company sitting in the middle of it making a ton of money, who's paying for the
*  UI designers and the user experience engineers and the people who are going to actually sort of make
*  this thing work? Right. And as an empirical matter, you know, you can try to crowdsource it, but those
*  are not the issues that are often most of interest to the people coding away for free in this publicly
*  sourced thing. Right. So Linux, as much as we love it, is just not as user friendly as Mac OS
*  or whatever. Yeah. Yeah. Yeah. It's a little worrisome. And another related thing before I
*  forget is you mentioned this morning, electric voting, electronic voting, right? Will these
*  kinds of technologies help make that more secure? Well, it depends on what you mean by these types of
*  technologies. So we're really meaning like I sit at my laptop and I can vote. I don't even need to go in.
*  Or like on my mobile phone or something like that. That's the dream, right? Is like I take out my
*  phone and I vote. I don't have to stand in line. I don't have to worry about sort of like who's
*  checking to make sure I register or people turning me away. So some of these technologies,
*  yes, will be extremely helpful for electronic voting, cryptography, using public private key
*  pairs and things like that. But, you know, the big push that I've heard about is applying blockchain
*  technology to voting. And I'm actually very skeptical about that right now. The thing with
*  electronic voting is that it's so important. Electronic voting is critically important.
*  And the thing with paper is that it's kind of hard to hack paper at scale. So perfected technology
*  paper. Yeah, it really is quite difficult to affect all the paper in a really big country
*  at the same time, right? You kind of have to, but it's considerably easier to electronically
*  change things even in a wide geographical area at one time. If you hack the system, if you find a
*  flaw, you find a way in. So with electronic voting, you're kind of opening up your attack
*  surface quite a bit. Now it's not just about the voting machines, it's about the phone that you're
*  voting on, the computer you're voting on, your internet connection from your house, so many
*  different things. The entire software stack of what's running. So many things that if there's a
*  bug in any one of those things, your vote could be compromised. So we really have to be very, very
*  careful about getting it right. And blockchain technology doesn't help with any of that endpoint
*  stuff. It doesn't help make sure that I didn't install some weird piece of software that's
*  sitting there fiddling with my vote. Blockchain technology doesn't do anything about that. And so
*  I just don't think it's solving the real problems. There was this brilliant XKCD cartoon, as they so
*  often are recently, that was talking to an airplane technician and they will say,
*  it seems unsafe to be an airplane, they can crash, but it's really super duper safe, way more safe.
*  You know, car technician, same thing. And then an electronic voting software developer, he's like,
*  no, don't ever use this for anything. This is incredibly subject to being exploited.
*  Exactly. And I think when you talk to the experts in the space, they will all say this, they will
*  all say, no, no, no, no, don't try to use these weird, like, first of all, a startup, do you really
*  want to start up developing like mission critical infrastructure for your country? No, no, no, no,
*  no. They've only existed for like six months. And who are these people? You know, this is not,
*  you want something super vetted and audited and really, really, really secure, looked at by like
*  everybody. So I don't understand. I know people are very frustrated with voting and they really
*  want to increase access, right? And I very much understand that problem and that question. I just,
*  I want to urge caution. Is there a worry, what about the social side of the individuality aspect?
*  If everyone controls their own feed, if everyone, you know, makes their own internet,
*  do we worry about political polarization kind of questions, hacking by bots, stuff like that? You
*  know, we just very recently had the instance where Alex Jones and various conspiracy theorists and
*  Nazis have been kicked off of certain mega platforms. Is that the good side of the mega
*  platforms that they can control that? Exactly. This is something that we've also thought about
*  and written about a little bit. So there is an alternative to Twitter called Mastodon.
*  It is a federated form of Twitter. It's very hip. I don't know. You might want to get on that.
*  I'm not that hip. Yeah, I should become more hip. Mastodon. So Mastodon. Yes, it's sort of a
*  federated Twitter. And by that, I mean different people run different Mastodon instances. And so
*  but they all interoperate. You can subscribe to people in these different instances. But the
*  idea is if somebody kicks you off of one, you can just get on another one. It's a, you know,
*  it's a bit harder to censor. Guess what? These things are breeding grounds for the type of things
*  that get kicked off of Twitter, which are not really very savory sorts of things. Mostly. Yeah.
*  Yeah. And so, so it's, it's sort of the, the counterpoint to censorship resistant technology.
*  That means that you really can't censor things that maybe even as a society, we would want
*  censored. So aside from what you think should happen or worry about what might happen, what do
*  you think will happen? I just remember, you know, in the mid 1990s, when web pages first began to
*  become a thing, right? Mosaic and Netscape and so forth. And I was very early adopter for these
*  things. And I got very excited and I could not explain to my friends why I was excited. And like,
*  I'm sure this is going to be really important. They said, well, what is it good for? And I said,
*  well, look, you can get a photograph of whether the coffee machine has coffee in it or not.
*  This is not worth what you're, what you're talking about. But of course we use the internet for a lot
*  now. Yes. Probably many of the applications are going to be unanticipated, I guess. Yes. And
*  please don't ask me to anticipate them. I feel exactly the same way that you do. Like, look,
*  I did this cool thing where I wrote this like transaction that did this weird thing. And they're
*  like, what is that? I don't need that. Yeah. And it's just the sense that there's something neat
*  here. There's something that we can do here that we couldn't do before. And I don't know how we're
*  going to do it, but it's a platform. People will build a million things on top of it. And some of
*  those things will be super amazing and cool. All right. Neha Nurula, we'll come back 10 years from
*  now and we'll have a good laugh at what we thought the internet was going to be. Thanks so much for
*  being on the podcast. Thank you.

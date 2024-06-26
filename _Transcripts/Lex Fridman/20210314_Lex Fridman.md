---
Date Generated: April 13, 2024
Transcription Model: whisper medium 20231117
Length: 6821s
Video Keywords: ['agi', 'ai', 'ai podcast', 'artificial intelligence', 'artificial intelligence podcast', 'lex ai', 'lex fridman', 'lex jre', 'lex mit', 'lex podcast', 'mit ai', 'silvio micali']
Video Views: 513315
Video Rating: None
---

# Silvio Micali: Cryptocurrency, Blockchain, Algorand, Bitcoin & Ethereum | Lex Fridman Podcast #168
**Lex Fridman:** [March 14, 2021](https://www.youtube.com/watch?v=zNdhgOk4-fE)
*  The following is a conversation with Silvio Michali, a computer scientist at MIT, winner of the Turing Award,
*  and one of the leading minds in the fields of cryptography, information security, game theory, and most recently,
*  cryptocurrency and the theoretical foundations of a fully decentralized, secure, and scalable blockchain at Algorand,
*  a company of cryptographers, engineers, and mathematicians that he founded in 2017.
*  Quick mention of our sponsors. Athletic Greens Nutrition Drink, the Information In-Depth Tech Journalism website,
*  Four Sigmatic Mushroom Coffee, and BetterHelp Online Therapy. Click the sponsor links to get a discount and to support this podcast.
*  As a side note, let me say that I will be having many conversations this year on the topic of cryptocurrency.
*  I'm reading and thinking a lot on this topic. I just recently finished reading the Bitcoin Standard.
*  A book I highly recommend. As always with this podcast, I'm approaching it with an open mind, with compassion,
*  with as little ego as possible, and yes, with love.
*  I hope you go along with me on this journey and don't judge me too harshly on any likely missteps.
*  As usual, I will play devil's advocate. I will, on purpose, sometimes, ask simple, even dumb questions,
*  all to try and explore the space of ideas here with as much grace as I can muster.
*  I have no financial interests here. I only have a simple curiosity and a love for knowledge,
*  especially about a set of technologies that may very well transform the fabric of human civilization.
*  If you enjoy this thing, subscribe on YouTube, review it on Apple Podcasts, follow on Spotify,
*  support it on Patreon, or connect with me on Twitter at Lex Friedman.
*  And now, here's my conversation with Silvio Macaulay.
*  Let's start with the big and the basic question. What is a blockchain? And why is it interesting?
*  Why is it fascinating? Why is it powerful?
*  Alright. So a blockchain, think of it, is really a common database distributed.
*  Think about it as a ledger in which everybody can write an entry in a page.
*  You can write, I can write, and everybody can read, and you have a guarantee that everybody has the same
*  copy of the ledger that is in front of you. So whatever you see on page seven, anyone else sees on page seven.
*  So what is extraordinary about this is this common knowledge thing that I think is a really a first for humanity.
*  I mean, if you look at communication, like right now, you can communicate very quickly images, thoughts, photos.
*  But do you have a certainty that whatever you have received has been received by everybody else? Not really.
*  And so this common knowledge and the certainty that everybody can write, nobody has been prevented from writing whatever they want.
*  Nobody can erase. Nobody can tear a page of a ledger. Nobody can swap page.
*  Nobody can change anything. And that is an immutable common record is extremely powerful.
*  And there's something fundamental that is decentralized about it.
*  So at least in spirit, some degree or against maybe a resistance to centralization.
*  Absolutely. If it is not decentralized, how can it be common knowledge?
*  If only one person or a few people have a ledger, the only way you don't have a ledger, you have to ask, you know, what is on page seven?
*  And how do you know that whatever they tell you is on page seven? They tell the same thing to everybody else.
*  And so this common knowledge is extremely powerful.
*  Just to give you an example, assume that you do an auction.
*  OK, you have worked very hard to build a building and now you want to auction off.
*  Makes sense because you want to auction worldwide.
*  Better yet, you want to tokenize the building and sell it in parcels.
*  Now, everybody sees the bids and you know that everybody sees the bids.
*  You and I see the same bids and so does everybody else.
*  So you know that the fair price has reached and you know who owns what and who has spent how much.
*  And if you do it instead of a wise, you know, in a centralized system, I put a bid, say, oh, congratulations, Alex, you won.
*  And your price is twelve thousand five hundred and seventy dollars.
*  I don't know. So if instead of a common knowledge is a very powerful tool for humanity.
*  So we return to it from a bunch of different perspectives, including like a technical perspective.
*  But you often talk about blockchain and some of these concepts of decentralization, scalability, security, all those kinds of things.
*  But one of the most maybe impactful, exciting things that leverage the block chain.
*  This kind of ledger idea of common knowledge is cryptocurrency.
*  So the in the financial space.
*  So is there can you say in the same kind of basic way, what is cryptocurrency in the context of this common knowledge and in the context of the block chain?
*  Great cryptocurrency is a currency that is on such a ledger.
*  So imagine that on the ledger, right.
*  Initially, you know that somehow say you and I are the only owner each one.
*  Let's give it to ourselves a billion each of whatever this unit.
*  Then I start writing on the ledger.
*  I give a hundred of these units to my sister.
*  I give this much to my aunt.
*  And then now because it's written on the ledger and everybody can see my sister can give 57 of these units she received from me to somebody else.
*  And so and that is money and that is money because you can see that somebody who tenders your payment has really the money there.
*  You don't have any more of a doubt when you want to sell an item.
*  If I write your check, is the check covered?
*  If I write or do I have the money at the moment of a transaction?
*  You really see because the ledger is always updated.
*  What you see is what I see and what the merchant sees.
*  You know that the money so is the most powerful money system there is because it is totally transparent.
*  And so you know that you have been paid and you know that the money is there.
*  You have not to second guess anything else.
*  So the common knowledge applied there is you're basically mimicking the same kind of thing you would get in the physical space,
*  which is if you give a hundred bucks or a hundred of that thing, whatever, of that cryptocurrency to your sister,
*  the actual transfer is as real as you giving like a basket of apples to your sister because that.
*  So in the case in the physical space, the common knowledge is in the physics, right?
*  Of the atoms.
*  And then it's digital space.
*  The common knowledge is in this ledger.
*  And so that transfer holds the same kind of power.
*  But now it's operating in the digital space.
*  Go ahead.
*  Again, I apologize for a set of ridiculous questions,
*  but you mentioned cryptocurrencies and money.
*  What is money?
*  Why do we have money?
*  Do you think about this kind of from this high philosophical level at times of this tool,
*  this idea that we humans have all kind of came up with and seem to be using effectively to do stuff?
*  Money is a social construct.
*  Okay.
*  In my opinion, and this has been somehow people always felt that somehow money is a way to allow us to transact,
*  even though we want to different things.
*  So I have two sheep and then you have a one cow and I want to work out, but you are looking for blankets instead.
*  So to have money is really simplifies this.
*  But at the end of it, that's why a bit was invented.
*  And you start with gold, you start to win the congee and then you start to win the check.
*  But at the end of the day, money is essentially a social construct because you know that what you receive,
*  you can actually spend with somebody else.
*  And so there is a kind of a social pact and social belief that you have.
*  At the end of the day, even a barter requires this belief that other people are going to accept the quote,
*  unquote currency you offer them.
*  Because if I'm a Mason and you ask me to build a wall in your field, and I did, and you in exchange,
*  you give me a thousand sheep, what am I going to do?
*  Eat them all?
*  No, I have to feed them.
*  And if I don't feed them, they die and my value is zero.
*  So in receiving this livestock, I must believe that somebody else will accept them in return for something else.
*  So money is this social belief, social shared belief system that makes people transact.
*  That's fascinating.
*  I didn't even think about that.
*  You have a deep network of beliefs about how society operates.
*  So the value is assigned even to sheep based on that everyone will continue operating how they were previously operating.
*  Somebody will feed the sheep.
*  I didn't even think about that.
*  That's fascinating.
*  So that directly transfers to the space of money and then to the space of digital money, cryptocurrency.
*  OK.
*  Does it bother you sort of intellectually when this money that is a social construct is not directly tied to physical goods like gold, for example?
*  Not at all, because after all, gold has some industrial value.
*  Nobody delights it.
*  It's a metal.
*  It doesn't oxidate.
*  It has some good things about it.
*  But does this industrial value really represent the value to which it now is traded?
*  No.
*  So gold is another way to express our belief.
*  I give you an answer.
*  Gold, you treat it like, oh, somebody else will want this for doing something else.
*  So it is really this notion of this money is a mental construct.
*  It's really and is shared.
*  It's a social construct, I believe.
*  And so some people feel that it's physical.
*  So therefore gold exists.
*  But then, as you know, now we countries, most sophisticated country right now, they print their own money and you believe that they are not going to exaggerate it with inflation.
*  Not everybody believes it.
*  But I'm saying there is at least not they're not going to exaggerate it blatantly.
*  And and therefore you receive it because you know that somebody else will accept it, will have a faith in the currency and so on and so forth.
*  But the way there is gold, wherever is livestock, wherever whatever it is, money is really a shared belief.
*  So there is something, you know, and I've been reading more and more about different cryptocurrencies.
*  There is a kind of belief that the scarcity of a particular resource like Bitcoin has a limited amount and it's tied to physical, you know, to to to proof of work.
*  So it's tied to physical reality in terms of how much you can mine effectively and so on that that's an important feature of money.
*  Do you think that's an important feature to be part of what the money is?
*  That is certainly a very useful part.
*  So at some point in time, you know, assume that money is something that all of a sudden we say daisies of money are the currency.
*  Then, you know, I offer you 10 daisies in payment of whatever goods and services you want to provide.
*  But at the end of the day, if you know that you can cultivate it and generate them at will, then perhaps, you know, you should not accept my payment.
*  Here is a bouquet of daisies.
*  So you need some kind of scarcity, the inability to create it suddenly out of nothing is unimportant.
*  And it's not that intrinsic necessity, but it's much easier to accept once you know that there is a fixed number of units or whatever currency there is.
*  And therefore you can mentally understand I'm getting, you know, this much of this piece of a pie.
*  And therefore I consider myself paid.
*  I understand what I'm receiving.
*  You described the goals of a block chain.
*  You have a nice presentation on this as scalability, security and decentralization.
*  And you challenged the block chain trilemma that claims you can only have two of the three.
*  So let's talk about each.
*  What is scalability in the context of block chain and cryptocurrency?
*  What does scalability mean?
*  So remember we said that the block chain is a ledger and each page receives a get stumped transaction and everybody can write in this in these pages of a ledger.
*  Nobody can be stopped for writing and everybody can read them.
*  OK, scalability means how fast can you write?
*  Just imagine that you can write an entry in this special shared ledger once every hour.
*  Well, you know, what are you going to do if you have one transaction per hour?
*  The world doesn't go around.
*  So you need to have scalability means here that you can somehow write a lot of transaction and then you can read them and everybody can validate them.
*  And that is the speed and the number of transactions per second and the fact that they are shared.
*  So you want to have this this the speed not only in writing, but in sharing and and inspection for validity.
*  This is scalability.
*  The world is big. The world wants to interact with the people, want to interact with each other.
*  And you better be prepared to have a ledger in which you can write lots and lots and lots of transactions in this special way.
*  Very, very, very quickly.
*  So maybe from a more mathematical perspective, or can we say something about how much scalability is needed for a world that is big?
*  Well, it really depends how many transactions you want.
*  But remember that I think right now you have to go into at least a thousand transactions per second.
*  Even if you look at credit cards, we are going to go from an average of 1600 to peaks of 20,000, 40,000, something like this.
*  But remember, it's not only a question of the transaction per se, but the value is that the transaction is actually being shared and visible to everybody.
*  And the certainty that that is the case.
*  I can print on my own printer way more transactions, but nobody has the time to see or to inspect.
*  That doesn't count. Right.
*  So you want scalability at this common knowledge level.
*  And that is the challenge.
*  I also meant from a perspective of like a complexity analysis.
*  So does it, you know, when you get more and more people involved, doesn't you just scale in some kind of way that?
*  Do you like to see certain kind of properties in order to say something is scalable?
*  Oh, absolutely.
*  I took a little bit implicitly that the people transacting are actually very different.
*  So if there is two people who can do thousands of transactions per second with each other, this is not so interesting.
*  What we really need is to say there are billions of people at any point in time, you know, thousands and thousands of them want to transact with each other.
*  And you want to support that.
*  So Algorand, it solves.
*  So that's the the company, the team of cryptographers and mathematicians, engineers, so on that challenge the blockchain trilemma.
*  So let's break it down in terms of achieving scalability.
*  How do we achieve scalability in the space of blockchain in the space of cryptocurrency?
*  OK, so scalability, security, remember, and decentralization.
*  So that's what they want.
*  What's the best way to approach?
*  Can we break it down?
*  Let's start with scalability and think about how do we achieve it?
*  Well, to achieve it one at a time is perhaps easy.
*  Even security.
*  If nobody transacts, nobody loses money.
*  So that is secure, but it's not scalable.
*  So let me tell you, I'm a cryptographer.
*  So I try to fight the bad guys.
*  And what do you want is that the vesselager that we discussed before cannot be tampered with.
*  So you must think of it as a special link that nobody can erase.
*  Then it has to be everybody should be able to read and not to alter the pages or the content of the pages.
*  That's OK.
*  But you know what?
*  That is actually easy cryptographically.
*  Easy cryptographically means you can use tools invented 50 years ago, which in cryptographic time is prehistory.
*  OK, we are cavemen working around and solve that problem in cryptography land.
*  But there is really a fundamental problem, which is really almost a social, seems a political problem, is to say,
*  who the hell chooses or publishes the next page of the ledger?
*  I mean, that is really the challenge.
*  This ledger, you can always add a page because more and more transactions are to be written on there.
*  And somebody has to assemble this transaction, put them on a page and add the next page.
*  Who is the somebody who chooses the page and adds it on?
*  Who can be trusted to do it?
*  Exactly.
*  Assume it is me for what I'm being, not that I want to volunteer for the job,
*  then I would have more power than any absolute monarch in history because I would have the tremendous power to say,
*  these are the transactions that the entire world should see.
*  And whatever I don't write, this transaction will never see the light of day.
*  I mean, no one had any such power in history.
*  So it's very important to do that.
*  And that is the quintessential problem in a blockchain.
*  And people have thought about it to say it's not me, it's not you.
*  But for instance, in proof of work, what people say is, okay, it's not me, it's not you.
*  You know what it is?
*  We make a very difficult, we invent a cryptographic puzzle, very hard to solve.
*  The first one to solve it has the right to add one page to the ledger on behalf of everybody else.
*  That now seems okay because sometimes I solve a puzzle before you do,
*  sometimes you solve it before I do or before somebody else solves it.
*  It's okay.
*  And presumably the effort you put in is somehow correlated with how much trust you should be given to add to the ledger.
*  Yeah.
*  So somehow you want to make sure that you need to work because you want to prevent,
*  you want to make sure that you get one solution every 10 minutes, say, like in particular example of Bitcoin.
*  So that is very rare that two pages are added at the same time.
*  Because if I solve a puzzle at the same time you do, it could happen that if it happens once or twice, we can survive it.
*  But if it happens, you know, every other page is a double page, then which of the two is the real page, it becomes a problem.
*  So that's why in Bitcoin it is important to have a substantial amount of work so that no many,
*  how many people try on Earth to solve a puzzle, you have one solution.
*  How many people are trying every 10 minutes?
*  So that you have, you distance it with pages and you have the time to propagate through the network,
*  the solution and the page attached to it.
*  And therefore there is one page at a time that is added.
*  And they say, well, why don't we do it?
*  We have a solution.
*  Well, first of all, a page every 10 minutes is not fast enough.
*  It's a question of scalability.
*  And second of all, to ensure that no matter how many people try, you get one page every 10 minutes,
*  one solution to the riddle every 10 minutes.
*  This means that the riddle becomes very, very hard.
*  And to have a chance to solve it within 10 minutes, you must have such an expensive apparatus in terms of specialized computers,
*  not one, not two, but thousands and thousands of them.
*  And they produce tons of heat, okay, dissipated like a maniac.
*  And you need to refrigerate them too.
*  And so then now you have air conditioning galore to add to the thing.
*  It becomes so expensive that fewer and fewer and fewer people can actually compete in order to add to the page.
*  And the problem becomes so crucial that in Bitcoin, depending on which day of the week you look at it,
*  you are going to have two or three mining pools are really the ones capable of controlling the chain.
*  So you're saying that's almost like least centralization.
*  Right.
*  It started being decentralized, but the expenses became higher and higher and higher.
*  When the cost becomes higher and higher, fewer and fewer people can afford them.
*  And then it becomes de facto centralized, right?
*  Yeah.
*  And a different type of approach is instead, for instance, a delegated proof of stake,
*  which is also very easy to explain.
*  Essentially boils down to say, well, look at these 21 people say, okay, don't they look honest?
*  Yes, they do.
*  In fact, I believe that they're going to remain honest for the foreseeable future.
*  So why don't we do ourselves a favor?
*  Let's entrust them to add the page on behalf of all of us to the ledger.
*  Okay.
*  Okay.
*  But now we are going to say, is this centralized or decentralized?
*  Well, 21 is better than one.
*  What I'm going to say is very little.
*  So if you look at when people rebelled to centralized power, I don't know, the French revolutions,
*  there was a monarch and the nobles.
*  Were there 21 nobles?
*  No, there were thousands of them, but there were millions and millions of disempowered citizens.
*  So one is centralized, 21 is also centralized.
*  So that's delegated proof of stake.
*  Delegated.
*  Kind of like representative democracy, I guess.
*  Yes, which is good.
*  It's working great, right?
*  It's working great.
*  Well, it's better than a monarch.
*  There's problems.
*  There are problems.
*  And so we were looking for a different, when thinking about Algorand, for a different approach.
*  And so we have an approach in that, you know, it's really, really decentralized because essentially it works as follows.
*  You have a bunch of tokens, right?
*  These are the tokens that have equal power.
*  And you have to say 10 billions of tokens distributed to the entire world.
*  And the owners, each token has a chance to add the ledger, equal probability to everybody else.
*  In fact, actually, if you want, here is how it works.
*  So think about, you know, by some magic cryptographic process, which is not magic, it's mathematics, but think of it as magic.
*  Assume that you select a thousand tokens.
*  And so sometimes a random, okay?
*  And you have a guarantee that they're randomly selected.
*  And then the owners of these 1000 tokens somehow agree on the next page.
*  They all sign it.
*  And that is the next page.
*  Okay?
*  So it is clear that nobody has the power, but once in a while, one of your tokens is selected and you are in charge of this committee to select the next page.
*  But this goes around very quickly.
*  So if you look at this, the equation really is that it's not really centralized.
*  And because for agreeing on the same page, it is important that the 1000 tokens that you randomly selected are in honest hands, the majority of them.
*  So which, if the majority of the tokens are in honest hands, that is essentially true.
*  Because if the majority of the tokens are in honest hands, if you select, say, 90% of the people are, 90% of the tokens are in honest hands.
*  So can you randomly select a thousand?
*  In this thousand, you find the 501 tokens in bad hands.
*  Very, very improbable.
*  So basically, when a large fraction of people are honest, then you can use randomness as a powerful tool to get decentralization.
*  So what does honesty mean?
*  And now we're into the social side of things, which is how do we know that the large fraction of people or participating parties are honest?
*  That is an excellent question.
*  So by the way, first of all, we should realize that the same thing is for every other system.
*  When you look at proof of work, you rely that the majority of the mining power is in honest hands.
*  When you look at delegated proof of stake, you rely that the majority of these 21 people are honest.
*  What is the difference?
*  The difference is that in these other systems, you should say the whole economy is secure if the majority of this small piece of economy are honest.
*  And that is a big question.
*  But instead, in our approach, we say the whole economy is secure if the majority of the economy is honest.
*  In other words, who can subvert Algorand?
*  It's not a majority of a small group, but it is a majority of the token holders had to conspire with each other in order to sink the very economy for which they own the majority of.
*  I think it is a bit harder to...
*  It's a self-destructive majority, essentially.
*  And you're also making me realize that basically every system that we have in the world today assumes that the majority of participants is honest.
*  Yes. The only difference is the majority of whom.
*  And in some cases, the majority of a club.
*  And in our case, it's the majority of the whole system.
*  The whole system.
*  OK. So that's that's that.
*  So through that kind of random sampling, you can achieve decentralization.
*  You can achieve.
*  So the scalability, I understand.
*  And then the security that you're referring to.
*  Basically, the security comes from the fact that the sample selected would likely include honest people.
*  So it's very difficult to.
*  By the way, the security, as you as you mentioned, you're referring to is basically security against dishonesty.
*  Right. Or manipulation or whatever.
*  Yes. Yes.
*  So essentially, when what you're going to do is to be following and say, well, Silvio, I understood what you're saying, but somebody has to randomly selected the tokens.
*  And then I believe you. So then who does this random selection?
*  And in in our ground, we do something a little bit unorthodox.
*  Essentially is the token choose themselves at random.
*  And you say, if you think about it, that seems to be a terrible idea, because if you want to say, choose yourself at random and whoever chooses himself is a thousand people committee.
*  You choose the page for the rest of us.
*  And because if I'm a bad person, I'm going to select myself over and over again because I want to be part of the committee every single time.
*  But not so fast. So what do we do in our ground? What does it mean that I select myself with each one of us?
*  In the privacy of our own computer, actually a laptop, what do you do is that you execute your own individual lottery.
*  And think about that you pull a lever of a slot machine.
*  You can only pull the lever once, not until you win, not enough comes until you win.
*  And when you pull the lever, case one, either you win in such a case, you have a winning ticket.
*  Or you lose. You don't get any winning ticket.
*  So if you don't have a winning ticket, you can say anything you want about the next page in the ledger.
*  Nobody pays attention. But if you have a winning ticket, people say, oh, wow, this is one of the 1000 winning tickets.
*  We better pay attention to what he or she says. And that's how it works.
*  And the lottery is a cryptographic lottery, which means that even if I am an entire nation, extremely powerful, with incredible computing powers,
*  I don't have the ability to improve even minimally my probability of one of my tokens winning the lottery.
*  And that's how it happens. So everybody pulls the lever.
*  The 1000 random winners say, oh, here is my winning ticket and here is my opinion up or down about the block.
*  These are the ones that count. And if you think about it, why this is distributed?
*  Because in the case of Algon, there is 10 billion tokens and you select a thousand of them, more distributed than this, you cannot get.
*  And then why is this scalable? Because what do you have to do?
*  Okay, you have to do the lottery. How long the lottery takes? It takes actually one microsecond.
*  Whether you have one token or two tokens or a billion tokens is always one microsecond of computation, which is very fast.
*  We don't hit the planet with a microsecond of computation.
*  And finally, why is this secure? Because even if I were a very evil and very, very powerful individual,
*  I'm so powerful that I can corrupt anybody I want instantaneously in the world.
*  Who would I want to corrupt? The people in the committee so that I can choose the page of the ledger.
*  But I do have a problem. I do not know whom I should corrupt.
*  Should I go after this lady in Shanghai, this other guy in Paris?
*  Because I don't know. I should. The winners are random, so I don't know whom I should corrupt.
*  But once the winner come forward and say, here is my winning ticket, and you propagate your winning ticket across the network,
*  together with your opinion about the block, now I know who they are.
*  For sure, I can corrupt all thousands of them given to my incredible powers.
*  But so what? Whatever they said, they already said, and their winning tickets and their opinions are virally propagated across the network.
*  And I do not have the power, no more than the US government or any government has the power,
*  to put back in the bottle a message virally propagated by WikiLeaks.
*  So everything you just described is kind of is fascinating.
*  A set of ideas and, you know, online I've been reading quite a bit and people are really excited about a set of ideas.
*  Nevertheless, it is not the dominating technology today.
*  So Bitcoin in terms of cryptocurrency is the most popular cryptocurrency and then Ethereum and so on.
*  So it's useful to kind of comment. We already talked about proof of work a little bit.
*  But what in your sense does Bitcoin get right? And where is it lacking?
*  OK, so the first thing that Bitcoin got right is to understand that there was the need of a cryptocurrency.
*  And that, in my opinion, they deserve all the success because they say that the time is ripe for this idea.
*  Because very often it's not enough to be right here to be right at the right time.
*  And somebody got it right there. So how to offer to Bitcoin for that.
*  And so what they got right is that it is hard to subvert and change the ledger to cancel a transaction.
*  It's not impossible. That is very hard.
*  What they did not get right is somehow that is a great store of value, currency-wise.
*  But money is not only a question that you store it and you put under the mattress.
*  Money wants to be transacted. And the transaction in Bitcoins are very little.
*  So if you want to store value, everybody needs to store value. It might as well use Bitcoin.
*  I mean, it's the plan. But if you don't look at it for a moment, at least it's a great store of value.
*  And everybody needs a store of value. But most of the time we want to transact. We want to interact.
*  We don't put the money under the mattress, right? So we want to do that.
*  They didn't get it right. That is too slow to transact. Too few transactions.
*  Just scalability.
*  Scalability issue.
*  Is it possible to build stuff on top of Bitcoin that fixes the scalability?
*  I mean, this is the thing. There's a bunch of technologies that hit the right need at the right time.
*  And they have flaws. But we build infrastructures on top of them over time to fix it, as opposed to getting it right from the beginning.
*  Or is it difficult to do?
*  Well, that is difficult to do. So you're talking to somebody that when I decided to throw my hat in the arena,
*  and I decided, first of all, as I said before, I much admire my predecessors.
*  I mean, they got it right, a lot of things. And I really admire for that.
*  But I had a choice to make. Either I patch something that has holes all over the place or I start from scratch.
*  I decided to start from scratch because sometimes it's a better way.
*  So what about Ethereum, which looks at proof of stake and a lot of different innovative ideas that kind of improve or seek to improve on some of the flaws of Bitcoin?
*  Ethereum had another great idea. So they figured out that money and payments are important as they are.
*  They are only the first level, the first stepping stone.
*  The next level are smart contracts.
*  And they were at the vision to say the people will need smart contracts, which allow me and you to somehow to transact securely without being shopper owned by a trusted third party, by a mediator.
*  By the way, because mediators are hard to find.
*  And in fact, maybe even impossible to find.
*  If you live in Thailand and I live in New Zealand, maybe we don't have a common person that we know and trust.
*  And even if we find them, guess what? They want to be paid.
*  So much so that 6% of the world GDP goes into financial friction, which is essentially third party.
*  So the headed right of the world needed that.
*  But again, the scalability is not there.
*  And the system is a smart contract in Ethereum is slow and expensive.
*  And I believe that is not enough to satisfy the appetite and the need that we have for smart contracts.
*  Well, what do you make of just as a small sort of aside in human history, perhaps it's a big one.
*  Is NFT the non-fungible tokens? Do you find those interesting technically or is it more interesting on the social side of things?
*  Well, both. I think NFTs are actually great.
*  So you have this you're an artist to create a song or it could be a piece of art.
*  He has many unique representation of a piece where there is an artifact or something dreamed up by you and as unique representation, but now you can trade.
*  And the important part is that now you have this not only the NFTs themselves, but the ability to trade them quickly, fast, securely,
*  knowing that who owns which rights and that gives a totally new opportunity for content creators to be remunerated for whatever they do.
*  So but ultimately you still have to have the scalability, security and decentralization to make it, you know, to make it work for bigger and bigger applications.
*  Correct. Yeah.
*  Yeah. I still wonder what kind of applications are yet to be like enabled by it because so much the interesting thing about NFTs.
*  You know, if you look outside of art is just like money, you can start playing with different social constructs is you can start playing with ideas.
*  You can start playing with with even like investing.
*  Somebody was talking about almost creating an economy out of like creative people or influencers.
*  Like if you start a YouTube channel or something like that, you can invest in that person and you can start trading their creations and then almost like create a market out of people's ideas,
*  out of people's creations, out of the people themselves that generate those creations.
*  And there's a lot of interesting possibilities of what you can do with that.
*  I mean, it seems ridiculous, but you're basically creating a hierarchy of value, maybe artificial in the digital world and are trading that.
*  But in so doing are inspiring people to create.
*  So maybe as a sort of our economy gets better and better and better where actual work in the physical space becomes less and less in terms of its importance,
*  maybe we'll completely be operating in a digital space where where these kinds of economies have more and more power.
*  And then you have to have this kind of blockchains to the scalability, security and decentralization and decentralization is,
*  of course, the tricky one because people in power start to get nervous.
*  Absolutely. Once in power, you're always nervous that you'll be supplanted by somebody else.
*  That is your job. Congratulations. You got the job, the top job and now everybody wants it.
*  Well, what is your sense about our time and the future hope about the decentralization of power?
*  Do you think that's something that we can actually achieve given that power corrupts and absolute power corrupts?
*  Absolutely. And it's so wonderful to be absolutely powerful.
*  Well, good question. So, first of all, I believe that, by the way, there is a complex questions, Lex, and like all the rest of your questions.
*  I'm so very sorry. It's OK. I am enjoying it.
*  So but so there are two things. First of all, power has been centralized for a variety of reasons.
*  When you want to get it is easier for somebody, even a single person to grab power.
*  But there is also some kind of a technology lack of very off that justified having in power.
*  Because in a way in a society in which even communication never mind block chain, which is common knowledge, but even simple unilateral communication is hard.
*  It is much easier to say you do as I say, because the alternative is.
*  But as so there is a little bit of a technology barrier.
*  But I think of it and now to get to this common knowledge, it is a totally different story.
*  Now we have finally the technology for doing this.
*  So that is one part. But I really believe that, you know, not by having a distributed system, not only you don't have a you have to actually much more stable and durable system.
*  Because not only for corruption, but even for things that go astray and you give it a long enough time by strange version of Murphy's law.
*  Whatever goes wrong goes wrong.
*  And so if the power is diffused, you actually are much more stable.
*  If you look at any any living complex living being is distributed.
*  I mean, I don't have somebody is OK, tell you now it's time to eat.
*  So you have millions of cells in your body. You have billions of bacteria.
*  Exactly. Help me in the guts.
*  You know, we are in a soup of it somehow.
*  It keeps us alive.
*  And so it's strange enough, however, when we design systems, we design them centralized.
*  We ourselves are distributed beings.
*  And when we plan to say, OK, I want to get an architecture.
*  How about I make a pyramid with this on the top and the power flows down.
*  And so again, it's a little bit perhaps of a technology problem.
*  But now the technology is there.
*  So that is a big challenge to rethink how we want to organize power in very large system and and distributed system, in my opinion, a much more resilient.
*  Let's put it this way.
*  There was a wine of my Italian compatriots, right?
*  Machiavelli, who looked at the time that was a big there was a bunch of a small state, a Democratic Republic of Florence, of Venice and the other thing.
*  And there was the Ottoman Empire that at the time was an empire and a southern was very centralized.
*  And he made the political observation that goes roughly to say whenever you have such a centralized thing, it's very hard to overtake that that former government is centralized.
*  But if you get it, it's so easy to keep population.
*  When instead there is other these other things are much more resilient.
*  When the power is distributed, it is much more it's going to be lasting for a much longer time.
*  And ultimately, maybe the human spirit wants that kind of resilience, wants that kind of distribution.
*  It's just that we didn't have technology throughout history.
*  Machiavelli didn't have the computer, the Internet.
*  And that is certainly part of the reason.
*  Yes.
*  You've written an interesting blog post.
*  If we take a step out of the realm of bits and into this, the realm of governance, you wrote a blog post about making Algorand governance decentralized.
*  Now, can you explain what that means?
*  The philosophy behind that?
*  You know how you decentralized basically all aspects of this kind of system?
*  Well, the philosophy and how let's start with a philosophy.
*  So I really believe that nothing fixed last very long.
*  And so I really believe that life is about intelligent adaptation.
*  Things change and we have to be nimble and adjust to change.
*  And when I see a lot of a crypto project, actually very proud to say it's fixed in stone.
*  Right?
*  You know, code is law, law is code.
*  I very far from a code that will never change.
*  Wow.
*  When I'm saying this is a recipe to me of disaster, not immediately, but soon.
*  Just imagine you take an ocean liner and you want to go, I don't know, from Lisbon to New York and you set the course.
*  Iceberg, no iceberg, tempest, no tempest.
*  It doesn't matter.
*  But it's not the way you need a teal.
*  You need to correct.
*  You need to adjust.
*  And so by the way, we design an algorithm with the idea that the code was evolving as the needs.
*  And of course, a waiver is a system in which every time there is an adjustment, you must have essentially a vote that right now is orchestrated.
*  90% of the stake.
*  They say, OK, we are ready.
*  We agree on the next version and we pick up this version.
*  So we are able to evolve without losing too many components left and right.
*  But I think without evolving any system essentially become aesthetic and is going to shrivel and die sooner or later.
*  And so that is needed.
*  And what do you want to do on the blockchain?
*  You have a perfect platform in which you can log your wishes, your votes, your things so that you have a guarantee that whatever vote you express is actually seen by everybody else.
*  So everybody sees really the outcome, call it a referendum or a change.
*  And that is, in my opinion, a system that wants to live long as to adapt.
*  There's an interesting question about leaders.
*  I've talked to Vitalik Buterin.
*  I'll probably talk to him again soon.
*  He's one of the leaders, maybe one of the faces of the Ethereum project.
*  And it's interesting.
*  You have Satoshi Nakamoto, who's the face of Bitcoin, I guess.
*  But he's faceless.
*  He, she, they.
*  It does seem like in our whatever it is, maybe it's 20th century.
*  Maybe it's Machiavellian thinking.
*  But we seek leaders.
*  Leaders have value.
*  Linus Torvald, the leader of of Linux, the open source development a lot.
*  I mean, there's no it's not it's not that the leadership is sort of dogmatic, but it's inspiring.
*  And it's also powerful in that through leaders, we propagate the vision.
*  Like the vision of the project is more stable, maybe not the details, but the vision.
*  And so do you think there's value to because there's a tension between decentralization and leadership, like visionaries.
*  What do you make of that tension?
*  OK, so I really believe that if it's a good question, I think of it.
*  I really believe in the power of emotions.
*  I think the emotional, the creative impulse of everybody else.
*  And therefore it's very easy for a leader to be a physical person, a real being.
*  And that interprets our emotions.
*  And by the way, this emotion has to resonate.
*  And what is good is that the more intimate our emotions are, the more universal they are.
*  Paradoxically, the more personal, the more everybody else somehow magically agrees and feels a bit of the same.
*  And so and it's very important to have a leader in the initial phase that generates out on nothing something that is important leadership.
*  But then the true tested leadership is to disappear after you lead the community.
*  So in my opinion, the quintessential leader, according to my vision, is George Washington.
*  He served for one term, he served for another term, and then all of a sudden he retired and became a private citizen.
*  And 200 years later, we still are with some defects, but we have done a lot of things right.
*  And we have been able to evolve.
*  That to me is success in leadership.
*  While instead you contrast our experiment with a lot of our experiment.
*  I've done so much so well that I want another four years.
*  And why shouldn't I be only a four and I have another eight?
*  Why should there be another eight?
*  Give me 16 and I will fix all your problems.
*  And then is the type, in my opinion, of failed leadership.
*  Leadership ought to be really lead, ignite, and disappear.
*  And if you don't disappear, the system is going to die with you.
*  And it's not a good idea for everybody else.
*  So we've been talking a little bit about cryptocurrency,
*  but is there spaces where this kind of blockchain ideas that you're describing, which I find fascinating,
*  do you think they can revolutionize some other aspects of our world that's not just money?
*  A lot of things are going to be revolutionized.
*  It's independent of finance.
*  By the way, I really believe that finance is an incredible form of freedom.
*  I mean, if I'm free to do anything I want, but I don't have the means to do anything, that's a bad idea.
*  So I really think financial freedom is very, very important.
*  But you know, but just again say that, you know, against, you know, censorship,
*  you write something on the chain and now nobody can take it out.
*  That is a very important way to express our view.
*  And then the transparency that you give, because everybody can see what's happening on the blockchain.
*  So transparency is not money.
*  But I believe that transparency actually is a very important ingredient also of finance.
*  Let's put it this way.
*  As much as I'm enthusiastic about blockchain and decentralized finance,
*  and we have actually our expression we're creating with the future five,
*  as much as we want to do, we must agree that the first guarantee of financial growth and prosperity are really the legal system, the courts.
*  Because we may not think about them and say, oh, the courts are kind of a bunch of boring lawyers.
*  But without them, I'm saying there is no certainty.
*  There is no notion of equality.
*  There is no notion that you can resolve your disputes.
*  Think that's what drives the commerce and things.
*  And so what I really believe that the blockchain actually makes a lot of this trust essentially automatic by making it impossible to cheat in very way.
*  You don't even need to go to court if nobody can change the ledger.
*  So essentially it's a way of you cannot solve an illegal system that uses a blockchain.
*  But what I'm saying, a big chunk of it can actually be guaranteed.
*  And there is no reason why technology should be antagonistic to legal scholarship.
*  It could be actually coexisting.
*  And one should start to doing the interesting things that the technology alone cannot do.
*  And then you go from there.
*  But I think that is essentially is a blockchain can affect all kinds of our of our behavior.
*  Yes, in some sense, the transparency, the required transparency ensures honesty prevents corruption.
*  So there's a lot of system that could use that and the legal system is one of them.
*  There is a little bit of attention that I wonder if you can speak to where this kind of transparency, there's a tension with privacy.
*  Is it possible to achieve privacy if wanted on on a blockchain?
*  Do you have do you have ideas about different technologies that can do that?
*  People have been playing with different ideas.
*  So absolutely.
*  The answer is yes.
*  And by the way, I'm a cryptographer.
*  So I really believe in privacy and I believe in and I have devoted a big chunk of my life to guarantee privacy, even when it seems almost impossible to have it.
*  And it is possible to have it in also in the blockchain, too.
*  And however, I believe in timing as well.
*  And I believe that the people have the right to understand.
*  That system believe in and right now, people can understand the blockchain to be something that is not can cannot be altered and is transparent.
*  And that is good enough.
*  And right now, anyway, toward and there is a pseudo privacy for the fact that who knows if this keys belong public key belongs to me or to you.
*  Right.
*  And I can when I want to change my money from one public key, I split it to other public keys going to figure out which one is Sylvia.
*  All of them are Sylvia, only one of Sylvia.
*  Who knows? So you get some vanilla privacy, not the one I could talk.
*  And I think it's good enough because it is important for now that we absorb this stage because the next stage, we must understand the privacy tool rather than taking on faith.
*  When the public starts saying, I believe in the scientists and whatever they say, I swear by them and therefore they tell me it's private, it's private.
*  And nobody understands that we need a much more educated about the tools we are using.
*  And so I look forward to deploying more and more privacy on the block chain.
*  But we are not I will not rush to it until the people understand and are behind whatever we have right now.
*  So you build privacy on top of the power of the block chain.
*  You have to first understand the power of the block.
*  Yes.
*  Yes. So Algorand is like one of the most exciting, technically, at least from my perspective, technologies, ideas in this whole space.
*  What's the future of Algorand look like? Is it possible for it to dominate the world?
*  Let's put this way. I certainly working very hard with a great team to give the best block chain that one can demand and enjoy.
*  And they said, I really believe that there is going to be it's not a winner takes them all.
*  So it's going to be a few block chains and each one is going to have its own brand and it's going to be great at something.
*  And sometimes it's a scalability, sometimes it's easier views, sometimes it's a thing.
*  And it's important to have a dialogue between these things.
*  And I'm sure and I'm working very hard to make sure that Algorand is one of them.
*  But I don't believe that it is even desirable to have a winner takes all because we need to express different things.
*  But the important thing is going to have enough interoperability of various systems so that you can transfer your assets where you have the best tool to service them, whatever your needs are at the time.
*  So there's an idea. I don't know. They call themselves Bitcoin maximalists, which is essentially the bet that the philosophy that Bitcoin will eat the world.
*  So you're talking about it's good to have variety.
*  Their claim is it's good to have the best technology dominate the the medium of exchange, the medium of store value, the money, the digital currency space.
*  What's your sense of the positives and the negatives of that?
*  So I feel people are smart and it's going to be very hard for anybody and to win.
*  And because people want more and more things.
*  And there is an Italian saying that goes as translates well, I think it goes of the appetite grows while eating.
*  OK, I think you understand what he means.
*  Yes. So I say I'm not hungry. OK, food. Let me try this.
*  So we want more and more and more.
*  And when you find something like Bitcoin, which I already had very good things to say, but it does something very well, but is a static.
*  I mean, store of value. Yes, I think it's a great way for the rest.
*  You know, it would be a sad world if the world in which we are so anchoring down, so on the defensive that we want to store value and hide it under the mattress.
*  I long for a world in which is open.
*  We all want to transact and interact with each other.
*  And therefore, when you want to store value, one perhaps one chain, you want to transact.
*  Maybe is another. I'm not saying that, you know, one chain cannot be stored of value or anything, but I really believe that.
*  I believe in the ingenuity of people and in the innovation that is intrinsic to the human nature.
*  We want always different things. So how can it be something invented?
*  Whatever it is decades ago is going to fulfill the needs of our future generations.
*  I'm not going to fulfill my needs, let alone my kids or their kids.
*  I use the we're going to have a different world and things will evolve.
*  So you believe. Yeah. So you believe that life, intelligent life is ultimately about adaptability and evolving.
*  So static is static loses in the end. Yes.
*  Let me ask the. Well, first, the ridiculous question.
*  Do you have any clue who who Satoshi Nakamoto is? Is that even an interesting question?
*  Well, is it your question? Very interesting.
*  So and I think so I would say, first of all, it's not me.
*  And I can prove it because, you know, if I were Satoshi Nakamoto, I would have not found an algorithm that takes totally different principles to approach to the system.
*  But the other thing with Satoshi Nakamoto, you know what the right answer is?
*  Is not him or she, her or them.
*  Satoshi Nakamoto is Bitcoin because to me is such a coherent proof of work that at the end, the creator and the creation identify themselves.
*  So he says, OK, I understand the Michelangelo.
*  OK, he did the assistant chaplain fine.
*  It did the way some Peters Dom fine.
*  He did the most of the Pietra, the statue fine.
*  But besides this, who was Michelangelo?
*  This is the wrong question.
*  Is his own work that is Michelangelo?
*  So I think that when you look at the Bitcoin is a piece of work that as it defects.
*  Yes, like anything human.
*  But he was captivated by the imaginations of millions of people as subverted by status quo.
*  And I'm saying, you know, whoever this person or people are, he's living in this piece of work.
*  I mean, it is Bitcoin.
*  The idea of the work is bigger.
*  We forget that sometimes.
*  It's something about our biology once likes to see a face and attach a face to the idea when really the idea is the thing we love.
*  The idea is the thing that impact ideas, the thing that ultimately we Steve Jobs or something like that we associate with the Mac or the iPhone with just everything he did at Apple.
*  Apple, actually, the company is Steve Jobs.
*  Steve Jobs, the man is is is a pales in comparison to the creation.
*  Correct. And the sense of aesthetics that has brought to the daily lives and very often aesthetic wins in the long in the long, long end.
*  And these are very elegant design product.
*  And when you say, oh, elegance, a very few people care about it.
*  Apparently millions and millions and millions and millions of people do because we are attracted by beauty.
*  And these are beautifully designed products.
*  And and and, you know, and they have in addition to ever the technological aspect of the other thing.
*  And I think, yes, that is.
*  Yeah, as the Stas Chesky said, beauty will save the world.
*  So I'm with you on that one. Right.
*  It currently seems like cryptocurrency, all these different technologies are gathering a lot of excitement.
*  Not just in our discourse, but in their like scale, financial impact.
*  A lot of companies are starting to invest in Bitcoin.
*  Do you think that the main method of store value and exchange of value, basically money, will soon or at some point in the century will become cryptocurrency?
*  Yes. So mind you, as I said, that the notion of cryptocurrency,
*  like any other fundamentally human notion, has to evolve.
*  But yes, so I think that he has a lot of momentum behind it.
*  And it's not only static as of this programmable money as I think smart contracts.
*  It allows a peer to peer interaction among people who don't even know each other.
*  Right. And they don't even therefore cannot even trust each other just because they never saw each other.
*  So I think it's so powerful that is going to do.
*  This said, again, a particular cryptocurrency should develop and cryptocurrency will all develop.
*  But the answer is yes, we are going towards a much more unless we have a society, a sudden crisis for different reasons,
*  which nobody hopes there's always an asteroid, there's always something nuclear war and all the existential crisis that we kind of think about, including artificial intelligence.
*  OK, it's funny you mentioned that Michelangelo and Steve Jobs, you know, set of ideas represents the person's work.
*  So we talked about Algorand, which is a super interesting set of technologies.
*  But, you know, he did also win the touring award.
*  You have a bunch of you have a bunch of ideas that are, you know, seminal ideas.
*  So can we talk about cryptography for a little bit?
*  What is the most beautiful idea in cryptography or computer science or mathematics in general?
*  Asking somebody who has explored the depths of all.
*  Well, there are a few contenders.
*  Either your work or other work.
*  Let's leave my work aside.
*  And so but one powerful idea and is both an old idea in some sense and a very, very modern one.
*  And in my opinion, is this idea of a one way function.
*  So a function that easy to evaluate.
*  So given X, you can compute f of X easily.
*  But given f of X is very hard to go back to X.
*  OK, think like breaking a glass easy reconstruct glass harder.
*  Frying an egg easy fried egg to go back to the original egg harder.
*  If you want to be extreme killings a living being, unfortunately easy.
*  The other way around very hard.
*  And so the fact that the notion of a function, which you have a recipe that is in front of your eyes to transform an X into f of X.
*  And then from f of X, even though you see the recipe to transform it, you cannot go back to X.
*  That, in my opinion, is one of the most elegant and momentous notions that there are.
*  And there is a computational notion because of the difficulties in a computational sense.
*  And it's a mathematical notion because we were talking about function.
*  And that is so fruitful because that is actually the foundation of all cryptography.
*  And let me tell you, is an old notion.
*  Because very often in any mythology that we think of, the most powerful gods or goddesses are the ones of X and the opposite.
*  X and the opposite of X, the gods of love and death.
*  And when you take opposite, they don't just erase one another.
*  You create something way more powerful.
*  And this one way function is extremely powerful because essentially becomes something that is easy for the good guys and bad for the hard for the bad guys.
*  So for instance, in pseudo random number generation, the easy part of the function corresponds.
*  You want to generate bits very quickly.
*  And hard is predicting what the next bit is.
*  It doesn't look the same.
*  One is X f of X going from X to X.
*  Hard, what does it do? Predicting bits.
*  By a magic of reductions and mathematical apparatus,
*  This simple function morphs itself into pseudo random generation.
*  This simple function morphs itself in digital signature scheme in which digital assigning should be easy and forging should be hard.
*  Again, a digital signature is not going from X to f of X.
*  But the magic and the richness of this notion is met that it is so powerful that it morphs in all kinds of incredible constructs.
*  And in both these two opposites coexist, the easy and the hard.
*  And in my opinion, it is a very, very elegant notion.
*  That simple notion ties together cryptography.
*  Like you said, pseudo random number generation.
*  You have work on pseudo random functions.
*  What are those?
*  What's the difference in those and the generators, pseudo random number generators?
*  Okay, let's go back to pseudo random number generation.
*  First of all, people think of the pseudo random generation generates random number.
*  Not true, because I don't believe that from nothing you can get something.
*  So nothing from nothing.
*  But randomness, you cannot create out of nothing.
*  But what you could do is that it can be expanded.
*  So in other words, if you give me somehow 300 random bits, truly random bits,
*  then I can give you 300,000, 300,000, 300,000, 300,000, 300,000, 400,000, as many as you want, random bits.
*  So that even though I tell you the recipe by which I produce these bits,
*  but I don't tell you the initial 300 random numbers, I keep them secret.
*  And you see all the bits I produced so far.
*  If you were to bet, given all the bits produced so far, what is the next bit in my sequence?
*  Better than 50-50.
*  Of course, 50-50, anybody can guess, right?
*  But to be in fair in something, you have to be a bit better.
*  Then the effort to do this extra bit is so enormous that it's de facto random.
*  So that is pseudo random generator, these expanders of secret randomness,
*  which goes extremely fast.
*  Okay, they said...
*  Expanders of secret randomness, beautifully put.
*  Okay, so every time somebody, if you're a programmer,
*  is using a function that's not called pseudo random, it's called random usually,
*  you know, these programming languages and it's generating different,
*  that's essentially expanding the secret randomness.
*  But they should.
*  In the past, actually, most of the libraries, they used something pre-modern cryptography, unfortunately.
*  They would be better served to take 300 real seed random number
*  and then expand them properly, as we know now.
*  But that has been a very old idea.
*  In fact, one of the best philosophers have debated whether the world was deterministic or probabilistic.
*  Very big questions, right?
*  Does God play dice?
*  Exactly. Einstein says it does, he doesn't.
*  But in fact, now we have a language that even at Albert time was not around,
*  but it was this complexity theory, modern complexity-based cryptography.
*  And now we know that in the universe as 300 random bits, whether it is random or probabilistic or deterministic,
*  it doesn't matter because you can expand this initial seed of randomness forever,
*  in which all the experiments you can do, all the inferences you can do, all the things you can do,
*  you will not be able to distinguish them from truly random.
*  So if you are not able to distinguish truly random from this super duper pseudo randomness,
*  are they really different things?
*  So many have to become really philosophical.
*  So for things to be different, but I don't have in my lifetime, in the lifetime of the universe, any method to set them aside,
*  well, I should be intellectually honest, say, well, pseudo random in this special function is as good as random.
*  Do you think true randomness is possible? And what does that mean?
*  So practically speaking, exactly as you said, if you're being honest,
*  the pseudo randomness approaches true randomness pretty quickly.
*  But is it maybe is this a philosophical question? Is there such a thing as true randomness?
*  Well, the answer is actually maybe, but if there exists, most probably it's expensive to get.
*  And in any case, if I give you one of mine, randomness, you will never tell them apart.
*  By any other shape, no matter how much you work on it.
*  So in some sense, if it exists or not, it really is a quote philosophical sense in the colloquial way to say that
*  we cannot somehow pin it down.
*  Do you ever, again, just to stay on philosophical for a bit, for a brief moment,
*  do you ever think about free will and whether that exists?
*  Because ultimately free will sort of is this experience that we have, like we're making choices,
*  even though it appears that the world is deterministic at the core.
*  I mean, that's against the debate.
*  But if it is in fact deterministic at the lowest possible level, at the physics level,
*  how do you make, if it is deterministic, how do you make sense of the difference between the experience of us
*  feeling like we're making a choice and the whole thing being deterministic?
*  So first of all, let me give you a gut reaction to the equation.
*  And the gut reaction is that it is important that we believe that there exists free will.
*  And second of all, almost by weird logic, if we believe it exists, then it does exist.
*  So it's very important for our social apparatus, for our sense of ourselves that it exists.
*  And the moment in which we so want it, we almost conjure it up in existence.
*  But again, I really feel that if you look at some point, the space of free will seems to shrink.
*  We realize how much of our genetic apparatus dictates who we are, why we prefer certain things than others,
*  and why we react to noises of music. We prefer poetry. We may explain even all this.
*  But at the end of the day, whether it exists in a philosophical sense or not is like randomness.
*  If you can, if pseudo-random is as good as random vis-a-vis lifetime of the universe, our experience, then it doesn't really matter.
*  So we're talking about randomness. I wonder if I can weave in quantum mechanics for a brief moment.
*  There's a lot of advancements on the quantum computing side.
*  So leveraging quantum mechanics to perform a new kind of computation,
*  and there's concern of that being a threat to a lot of the basic assumptions that underlie cryptography.
*  What do you think? Do you think quantum computing will challenge a lot of cryptography?
*  Will cryptography be able to defend all those kinds of things?
*  Okay, great. So first of all, for the record, not because I think it matters, but it's important to set the record,
*  there are people who continue to contend that quantum mechanics exist, but that's nothing to do with computing.
*  It's not going to accelerate it, at least in very basic kind of hard computation.
*  That is a belief that you cannot take it out. I'm a little bit more agnostic about it,
*  but I really believe going back to whatever I said about the one-way function.
*  So one-way function, what is it? That is a cryptography. So does quantum computing challenge it?
*  The one-way function.
*  Essentially, you can boil it down to does quantum computing follow one-way function?
*  What is one-way function? Easy in one direction, hard in the other.
*  Okay, but if quantum computing exists, when you define what it is easy,
*  it's not easy by a classical computer and hard by a classical computer,
*  but easy for a quantum computer, that's a bad idea.
*  But once easy means it should be easy for a quantum and hard for also quantum.
*  Then you can see that yes, it's a challenge, but you have hope, because you can absorb.
*  If one computing really realizes and becomes available according to the promises,
*  then you can use them also for the easy part.
*  And once you use it for the easy part, the choices that you have a one-way function, they multiply.
*  So, okay, so they particularly candidates of one-way function, they not be one-way anymore,
*  but quantum one-way function may continue to exist.
*  And so I really believe that for life to be meaningful, this one-way function had to exist.
*  Because just imagine that anything that becomes easy to do.
*  I mean, what kind of life is it?
*  I mean, so you need that, and if something is hard, but it's so hard to generate,
*  you'll never find something which is hard for you.
*  You want to, there is abundance, there is easy to produce, hard problem.
*  That's my opinion is why life is interesting, because hard problem pop up
*  at a really relative speed.
*  So in some sense, I almost think that I do hope they exist.
*  If they don't exist, somehow life is way less interesting than it actually is.
*  Yeah, it does. That's funny.
*  It does seem like the one-way function is fundamental to all of life,
*  which is the emergence of the complexity that we see around us seem to require the one-way function.
*  I don't know if you play with cellular automata.
*  That's just another formulation of a very simple, it's almost a very simple illustration
*  of starting out with simple rules and one way being able to generate incredible amounts of complexity.
*  But then you ask the question, can I reverse that?
*  It's just surprising how difficult it is to reverse that.
*  It's surprising even in constrained situations, it's very difficult to prove anything.
*  It almost, I mean the sad thing about it, I don't know if it's sad,
*  but it seems like we don't even have the mathematical tools to reverse engineer stuff.
*  I don't know if they exist or not, but in the space of cellular automata,
*  where you start with something simple and you create something incredibly complex,
*  can you take a small picture of that complex and reverse engineer?
*  That's kind of what we're doing as scientists.
*  You're seeing the result of the complexity and you're trying to come up with some universal law that generate all of this.
*  What is the theory of everything? What are the basic physics laws that generate this whole thing?
*  There's a hope that you should be able to do that, but it gets difficult.
*  But there is also some poetry on the fact that it's difficult,
*  because it gives us some mystery to life without which it's not so fun.
*  Life would not be less fun.
*  Can we talk about interactive proofs a little bit, zero-knowledge proofs? What are those?
*  How do they work?
*  Interactive proofs are actually a modern realization and conceptualization of something that we knew was true.
*  It's easy to go to lectures. In fact, that's my motivation.
*  We invented schools to go to lectures.
*  We don't say, oh, I'm the Minister of Education. I published this book. You read it.
*  This is a book for this year. This is a book for this year.
*  We spend a lot of our treasury in educating our kids.
*  In person, educating, go to class, interact with the teacher, own the blackboard, and chalk on my time.
*  Now we can have a whiteboard, and presumably you're going to have actually these magic pens and a display instead.
*  But the idea is that interactively you can convey truth much more efficiently.
*  We knew this psychologically. It's better to hear an explanation than just to belabor some paper.
*  Same thing.
*  Interactive proofs is a way to do the following.
*  Rather than doing some complicated, very long papers and possibly infinitely long proofs, exponentially long proofs,
*  you say the following. If this theorem is true, there is a game that is associated to the theorem.
*  If the theorem is true, this game, I have a winning strategy that I can win half of the time, no matter what you do.
*  Then you say, well, is the theorem true? You believe me. Why should I believe you?
*  Okay, let's play. If I prove that I have a strategy and I win the first time and I win the second time,
*  then I lose the third time, but I win more than half of the time or I win all the time if the theorem is true,
*  and at least at the most half of the time if the theorem is false, you statistically get convinced.
*  You can verify this quickly. And therefore, when the game typically is extremely fast,
*  so you generate a miniature game in which if the theorem is true, I win all the time, if the theorem is false,
*  I can win at most half of the time. And if I win, win, win, win, win, win, win, win, win, you can deduce either if the theorem is true,
*  which most probably is the case, so to speak, or I've been very, very unlucky because it's like if I had a hundred coin tosses
*  and I got a hundred heads. Very improbable.
*  So that is a way. And so this transformation from the formal statement of a proof into a game that can be quickly played
*  and you can draw statistics how many times you win is one of the big conquests of modern complexity theory.
*  And in fact, actually as highlighted, the notion of a proof as a really give us a new insight of what to be true means
*  and what truth is and what the proofs are.
*  So these are legitimately proofs. So what kind of mysteries can it allow us to unlock and prove? You said truth.
*  So what does it allow us? What kind of truth does that allow us to arrive at?
*  So it enlarges the real mobotism provable because in some sense of a classical way of proving things was extremely inefficient
*  from the verifier point of view. Yes. Right.
*  So, and so therefore there is so much proof that you can take. But in this way you can actually very quickly, minutes,
*  verify something that is the correctness of an assertion that otherwise would have taken a lifetime to belabor and check all the passages
*  of a very, very long proof. And you better check all of them because if you don't check one line, an error can be in that line.
*  And so you have to go linearly through all this stuff rather than bypass this. So you enlarge tremendous amount what the proof is.
*  And in addition, once you have the idea that essentially a proof system is something that allows me to convince you of a true statement,
*  but does not allow me to convince you of a false statement. And that at the end says that it's a proof.
*  Proof can be beautiful, should be elegant, but at the end says is true or false.
*  If you want to be able to differentiate, it is possible to prove the truth and it should be impossible or statistically extremely hard to prove something false.
*  And if you do this, you can prove way, way more once you understand this. And on top of it, we got some insight like in this zero-knowledge proofs
*  that is in something which you took for granted were the same knowledge and verification actually separate concepts.
*  So you can verify that an assertion is correct without having any idea of why this is so.
*  And so people felt to say, if you want to verify something, you have to have the proof. Once you have the proof, you know why it's true.
*  You have the proof itself. So somehow you can totally differentiate knowledge and verification validity.
*  So totally you can decide if something is true and still have no idea.
*  Is there a good example in your mind?
*  Oh, actually, you know, at the beginning, we labored to find the first knowledge, zero-knowledge proof.
*  Then we found a second, then we found a third. And then a few years later, actually, we proved a theorem,
*  which essentially says every theorem, no matter what about, can be explained in a zero-knowledge way.
*  Okay. So it's not a class of theorem, but all theorems. And it's a very powerful thing.
*  So we were really for thousands of years bought this identity between knowledge and verification had to be handed in together.
*  And for no reason at all. I mean, we had to develop a way of technology.
*  As you know, I'm very big in technology because it makes us more human and make us understand more things than before.
*  And I think that is a good thing.
*  So this interactive proof process, there's power in games.
*  Yes.
*  And you've recently gotten into, recently, I'm not sure you can correct me, mechanism design.
*  Yeah.
*  So it's, I mean, first of all, maybe you can explain what mechanism design is and the fascinating space of playing with games and designing games.
*  Mechanism design is that you want to, you want a certain behavior to arise, right?
*  If you want to organize a societal structure or something, you want to have some orderly behavior to arise, right?
*  Because it is important for your goals.
*  But you know that people, they don't care what my goals are. They care about maximizing their utility.
*  So putting grossly, making money, the more money, the better, so to speak.
*  I'm exaggerating.
*  Self-interest.
*  Self-interest.
*  In whatever way they...
*  So what you want to do is ideally, what you want to do is to design a game so that while people played,
*  so to maximize their self-interest, they achieve the social goal and behavior that I want.
*  That is really the best type of thing.
*  And it is a very hard science and art to design these games.
*  And it challenges us to actually come up with a solution concept for a way to analyze the games that need to be broader.
*  And I think the game theory has developed a bunch of very compelling ways to analyze the game.
*  That if the game has the best property, you can have a pretty good guarantee that it's going to be played in a given way.
*  But as it turns out, and not surprisingly, these tools have a range of action like anything else.
*  All these so-called the technical solution concept, the way to analyze the game, like dominant strategy equilibrium,
*  something comes to mind to be very meaningful, but as a limited power.
*  In some sense, the games that can be admit such a way to be analyzed...
*  There's a very specific kind of games and the rules are set, the constraints are set, the utilities are all set.
*  So if you want to reason, there is a way that you can analyze a restricted class of games this way.
*  But most games don't fall into this restricted class.
*  Then what do I do?
*  Then you need to enlarge a way what a rational player can do.
*  So for instance, in my opinion, at least in some of my...
*  I played with this for a few years and I was doing some exoteric things, I'm sure, in the space that were not exactly mainstream.
*  And then I changed my interest in blockchain.
*  But what I'm saying, for a while I was doing...
*  So for instance, to me is a way in which I designed the game and you don't have the best move for you.
*  The best move is the move that is best for you no matter what the other players are doing.
*  Sometimes a game doesn't have that, okay, it's too much to ask.
*  But I can design the game such that given the option in front of you say, oh, these are really stupid for me, take them aside.
*  But these are not stupid.
*  So if you design the game so that in any combination of non-stupid things that the player can do, I achieve what I want, I'm done.
*  I don't care to find the very unique equilibrium.
*  I don't give a damn.
*  I want to say, well, as long as you don't do stupid things and nobody else does stupid things, good social things outcome arise, I should be equally happy.
*  And so I really believe that this type of analysis is possible and has a bigger radius.
*  So it reaches more games, more classes of games.
*  And after that, we have to enlarge it again.
*  And it's going to be, we're going to have fun because human behavior can be conceptualized in many ways.
*  And it's a long game.
*  It's a long game.
*  It's a long game.
*  Do you have favorite games that you're looking at now?
*  I mean, I suppose your work with the blockchain and Algorand is the kind of game that you're basically this mechanism design, design the game such that it's scalable, secure and decentralized.
*  Right. Yes. Yes.
*  Yes. And very often you have to say and you must also design so that the incentives are.
*  And to tell you the truth, whatever little I learned from my venture in mechanism design is that incentives are very hard to design because people are very complex creatures.
*  And so and so somehow the way we design Algorand is a totally different way.
*  Essentially, we've no incentives, essentially.
*  And then and but technically speaking, there is a notion that is actually believable.
*  Right. So let's say people want to maximize their utility.
*  Yes. Up to a point.
*  Let me let me tell you assume that.
*  If you are honest, you make 100 bucks.
*  But if you are dishonest, no matter how dishonest you are, you can only make 100 bucks and one cent.
*  What are you going to be?
*  I'm saying, you know what?
*  Technically speaking, even that one, nobody bothers and say, how much am I going to make by honest?
*  If I'm devious and if I'm a criminal, 100 bucks and one cent, you know, I might as well be honest.
*  So that essentially is called the no epsilon utility equilibrium.
*  But I think it's good.
*  And and and and that's what we design essentially means that, you know, there is an even no incentives is actually a good thing
*  because prevent people from reasoning how else I'm going to gain the system.
*  But why can we achieve in our going to have known incentives and in Bitcoin instead yet to pay the miners because they do tremendous amount of work.
*  Because if you have to do a lot of work, then you demand to be paid accordingly.
*  Because you but if I'm going to say yet to add the two and two equal to four, how much you want to be paid for this?
*  If you don't give me this, I don't add the two and two.
*  I would say you can add two and two in your sleep.
*  You don't need to be paid to add the 22.
*  So the idea is that if we make the system so efficient, so that generating the next block is so damn simple, it doesn't hit the universe, let alone my computer, let alone the extra microsecond of computation.
*  I might as well not being received incentives for doing that and try to incentivize some other part of the system, but not the main consensus, which is a mechanism for generating an adding block to the chain.
*  Since you're Italian Sicilian, I also heard rumors that you are a connoisseur of food.
*  What you know, if I said today is the last day you get to be alive, I'm Russian.
*  You shouldn't have trusted me.
*  You never know the Russian whether you're going to make it out or not.
*  If you had one last meal, you can travel somewhere in the world.
*  Either you make it or somebody else makes it.
*  What's that going to look like?
*  All right.
*  This is one last meal.
*  I must say, you know, in this era of COVID, I've not been able to see my mom.
*  And my mom was a fantastic chef.
*  Okay.
*  And had the best very traditional food.
*  As you know, the very traditional food are great for a reason because they survived hundreds of years of culinary innovation.
*  So there is one very laborious thing, which is and you heard the name, which is this parmigiana.
*  But to do it is a piece of art.
*  It requires so many hours that only my mom could do it.
*  If we have one last meal, I'm on top of Parmigiana.
*  What is what's the laborious process?
*  Is that the ingredients?
*  Is it the actual process?
*  Is it the atmosphere and the humans involved?
*  The latter.
*  The ingredient like in any other in Italian cuisine believes in very few ingredients.
*  If you take say quintessential Italian recipe, very good spaghetti pesto.
*  Okay.
*  Pesto is olive oil.
*  Very good extra virgin olive oil.
*  And basil, pine nuts, pepper, clove of garlic.
*  Not too much.
*  Otherwise, you know, the power.
*  And then you have to do either two schools of thought, parmesan or pecorino or a mix of the two.
*  I mentioned six ingredients.
*  That is typical Italian.
*  That is, I understand that there are other cuisines, for instance, the French cuisine, which is extremely sophisticated and extremely combinatorial.
*  Or some Chinese cuisine, which has a lot of many more ingredients in this.
*  And yet the artist to put them together, a lot of things.
*  In Italy is really the striving for simplicity yet to find few ingredients, but the right ingredients to create something.
*  So in Parmigiana, the ingredients are eggplants, tomatoes, basil.
*  But how to put them together and the process is an act of love, labor and love.
*  Is that you can spend the entire day when I'm exaggerating, but the entire morning for sure to do it properly.
*  Yeah, as a Japanese cuisine, too, there's a mastery to the simplicity with the sushi.
*  I don't know if you've seen Georgians of sushi, but there's a mastery to that that propagated through the generations.
*  It's fascinating.
*  You know, people love it when I ask about books.
*  I don't know if books, whether fiction, nonfiction, technical or completely non-technical, had an impact in your life throughout.
*  If there's anything you would recommend or even just mention as something that gave you an insight or moved you in some way.
*  So, OK, so I don't know if I recommend it because in some sense, you almost had to be Italian or to be such a scholar.
*  But being Italian, one thing that really impressed me tremendously is the Divine Comedy.
*  It is a medieval poem, a very long poem divided in three parts, Hell, Purgatory and Paradise.
*  And that is the non-trivial story of a middleman man gets into a crisis, personal crisis.
*  And then out of this crisis, he purifies, makes a catastrophe, purifies himself more and more and more until he's become capable of actually meeting God.
*  OK, and that is actually a complex story.
*  So you have to get some very sophisticated language, maybe Latin at that point, that we are talking about 1200s Italy, right?
*  And in Florence, this guy instead, he chose his own dialect, not spoken outside his own immediate circle, right?
*  A Florentine dialect. Actually, Dante really made Italian.
*  So how can you express such a sophisticated thing?
*  And then the point is that these words that nobody actually knew because they were essentially dialect.
*  And plus a bunch of very intricate rhymes in which you had to rhyme with the things.
*  And turns out that by getting meaning from the things that you rhyme, you essentially guess what the word means.
*  And you invent Italian and you communicate by almost osmosis what you want.
*  It's a miracle of communication in a dialect, a very poor language, very unsophisticated to express a very sophisticated situation.
*  I love it. People love it. And Italians and not Italian.
*  But what I got of it is that very often limitations are our strength.
*  Because if you limit yourself at a very poor language, somehow you get out of it and you achieve even better form of communication.
*  Using a hyper sophisticated literary language with lots of resonance from the prior books that you can actually instantaneously quote.
*  He couldn't quote anything because nothing was written in Italian before him.
*  So I really felt that limitations are our strength.
*  And I think that rather than complaining about the limitations, we should embrace them.
*  Because if we embrace our limitation, limited as we are, we find very creative solutions that people with less limitation we have.
*  We would not even think about it.
*  Well, the limitations are kind of superpower. If you choose to see it that way.
*  Is there, since you speak both languages, is there something that's lost in translation to you?
*  Is there something you can express in Italian that you can't in English and vice versa?
*  Maybe is there something you could say to the musicality of the language?
*  I mean, I from I've been to Italy a few times and I'm not sure if it's the actual words, but the people are certainly very there's body language, too.
*  There's just the whole being is language.
*  So I don't know if you miss some of that when you're speaking English in this country.
*  Yes, in fact, actually, I certainly I'm I miss it.
*  And somehow it was a sacrifice that I made consciously by the time I arrived.
*  I knew that this I was not going to express myself at a better level.
*  And and it was actually sacrifice because given to have also your mother tongue is Russian.
*  So you know that you can be very expressive in your mother tongue and not very expressive in this new tongue, a new language.
*  And then what people think of you when you language because when the precise of expression of things, it generates and all it shows.
*  It shows an arm elegance or it shows, you know, knowledge or it shows as a census or it shows as a caste or education, whatever it is.
*  So all of a sudden, I found myself on the bottom.
*  Yeah, I had to fight all my way up back up.
*  And but but I'm saying I go back to passing, right?
*  Their limitations are actually our strength.
*  In fact, is a trick to limit yourself.
*  To exceed the right and you know, there are examples in history.
*  If you think about, you know, Hernan Cortez, right, goes to invade Mexico.
*  He has what a few hundred people with him and he has a hundred thousand people in arms on the other side.
*  First thing he does, he limits himself.
*  He sinks his own ship.
*  There is no return.
*  And at that point, he actually managed to come up.
*  I actually first of all, that's inspiring to me.
*  I feel like I have quite a few limitations, but more practically on the Russian side, I'm going to try to do a couple of really big and really tough interviews in Russian.
*  Once COVID lifts a little bit and traveling to Russia and I'll keep your advice in mind that the limitations is a kind of superpower.
*  We should use it to our advantage because you do feel less like you're not able to convey your wisdom in the Russian language because I moved here on us 13.
*  So you don't you know, the parts of life you live under a certain language are the parts of life you're able to communicate.
*  You know, I became I became a thoughtful, deeply thoughtful human in English.
*  But the pain from World War Two, the music of the people that was instilled with me in Russian.
*  So I can carry both of those and there's limitations in both.
*  I can't say philosophically profound stuff in Russian, but I can't in English express like that melancholy feeling of like the people.
*  And so combining those two, I'll somehow beautifully said.
*  Thanks for sharing.
*  This is great.
*  Yes, I totally understand you.
*  Yes, you've accomplished some incredible things in this space of science in a space of technology, a space of theory and engineering.
*  Do you have advice for somebody young, an undergraduate student, somebody in high school or anyone who just feels young about life or about career, about making their way in this world?
*  So I was telling before that I believe in emotion and my thing is to be true to your own emotion.
*  And that I think that if you do that, you're doing well because it's a life well spent and you are going never tire because you want to solve all these emotional notes that have always intrigued you from the beginning.
*  And I really believe that to live meaningfully, creatively and to live your emotional life.
*  So I really believe that whether you're a scientist or an artist even more, but a scientist, I think of them as artists as well.
*  If you are a human being, so you are really to live fully your emotions and to the extent possible.
*  Sometimes emotions can be overbearing and my advice is try to express them with more and more confidence.
*  Sometimes it's hard, but you are going to be much more fulfilled than by suppressing them.
*  What about love? One of the big ones. What role does that play?
*  That's the bigger part of emotions. It's a scary thing.
*  It's a lot of vulnerability that comes with love, but there is also so much energy and power and love in all senses and in the traditional sense,
*  but also in the sense of a broader sense for humanity, feeling this compassion that makes us one with other people and the suffering of other people.
*  I mean, all of this is a very scary stuff, but it's really the fabric of life.
*  Well, the sad thing is it really hurts to lose it.
*  Yes, that's why the vulnerable believer comes with it.
*  That's the thing about emotion is up and down and the down seems to come always with up, but the up only comes with the down.
*  So let me ask you about the ultimate down, which is unfortunately, we humans are mortal or appear to be for the most part.
*  Do you think about your own mortality? Do you fear death?
*  I hope so. And I do. Because without death, there is no life. So at least there is no meaningful life.
*  Death is actually in some sense our ultimate motivator to live a beautiful and meaningful life.
*  I myself felt as a young man that unless I got something that I wanted to do, I don't know why I got this idea of something to say.
*  If I'm not able to say, I would suicide. So maybe it was a way to motivate myself.
*  But you don't need to motivate it because in some sense, unfortunately, death is there.
*  So you better get up and do your thing.
*  And because that is the best motivation to to live fully.
*  Well, what do you think? What do you hope your legacy is?
*  You mentioned you have two kids.
*  Yes. And so I really feel that, you know, there is on one side is my biological legacy and that is my two kids.
*  Right. And and their kids, hopefully. And that is one fine.
*  And the other thing is this common enterprise, which is society.
*  And I really feel that my legacy would be better by providing security and privacy.
*  Actually, for me, are metaphorical to say I want to give you the ability to interact more and take more risks and and reach out to more for more people as difficult and dangerous as it may seem.
*  But my all scientific work is about to to guarantee privacy and and give you the security of interaction.
*  And not only that transactional like it would be a block chain transaction, but that is really one of the hardcore of my emotional problems.
*  And I think of it and these are the problems I want to tackle.
*  Yeah. And ultimately, privacy and security is freedom.
*  Yes. Freedom is at the core of this. It's dangerous.
*  Dangerous. Just it's like the emotion.
*  Yeah. But ultimately, that's how we create all the beautiful things around us.
*  Do you think there's meaning to it all?
*  This life, except the urgency that death provides and us anxious beings create cool stuff along the way.
*  Is there a deeper meaning? And if it is, what is it?
*  Well, meaning of life. Actually, we have three meanings of life.
*  Great.
*  That's great. One to seek to to seek and three to seek to seek what?
*  You know, I was there. No answer that has no answer to that.
*  I really think that the journey is more and more important than the destination, whatever that be.
*  And I think that is a journey and is, in my opinion, at the end of the day, I must admit, meaningful in itself.
*  And we must admit to it, maybe whatever your destination might be, I'd be hanging.
*  You know, we may never didn't get there, but hell was a great ride.
*  Well, I don't think there's a better way to end this, Silvio.
*  Thank you for joining. Thank you for wasting your extremely valuable time with me today.
*  Joining on this journey of seeking something together.
*  We found nothing, but it was very fun.
*  I really enjoyed it. Thank you so much for thank you.
*  Thanks for being really special for me to be interviewed by you.
*  Thank you for listening to this conversation with Silvio McCauley.
*  And thank you to our sponsors, Athletic Greens Nutrition Drink, the information in depth tech journalism website, Four Sigmatic Mushroom Coffee and Better Help Online Therapy.
*  Click the sponsor links to get a discount and to support this podcast.
*  And now let me leave you with some words from Henry David Thoreau.
*  Wealth is the ability to fully experience life.
*  Thank you for listening and hope to see you next time.

---
Date Generated: April 13, 2024
Transcription Model: whisper medium 20231117
Length: 6596s
Video Keywords: ['richard craib', 'artificial intelligence', 'agi', 'ai', 'ai podcast', 'artificial intelligence podcast', 'lex fridman', 'lex podcast', 'lex mit', 'lex ai', 'lex jre', 'mit ai']
Video Views: 244033
Video Rating: None
---

# Richard Craib: WallStreetBets, Numerai, and the Future of Stock Trading | Lex Fridman Podcast #159
**Lex Fridman:** [February 07, 2021](https://www.youtube.com/watch?v=ziQSpuST6Es)
*  The following is a conversation with Richard Crape, founder of Numeroi, which is a crowd-sourced hedge fund, very much in the spirit of Wall Street bets, but where the trading is done not directly by humans, but by artificial intelligence systems submitted by those humans.
*  It's a fascinating and extremely difficult machine learning competition where the incentives of everybody is aligned.
*  The code is kept and owned by the people who develop it.
*  The data, anonymized data, is very well organized and made freely available.
*  I think this kind of idea has a chance to change the nature of stock trading and even just money management in general by empowering people who are interested in trading stocks with the modern and quickly advancing tools of machine learning.
*  Quick mention of our sponsors.
*  Audible audiobooks, child labs, machine learning company, Blinkist app that summarizes books and athletic greens all in one nutrition drink.
*  Click the sponsor links to get a discount and to support this podcast.
*  As a side note, let me say that this whole set of events around GameStop and Wall Street bets has been really inspiring to me as a demonstration that a distributed system, a large number of regular people are able to coordinate and collaborate in taking on the elite centralized power structures, especially when those elites are misbehaving.
*  I believe that power in as many cases as possible should be distributed.
*  And in this case, the Internet, as it is for many cases, is the fundamental enabler of that power.
*  And at the core, what the Internet in its distributed nature represents is freedom.
*  Of course, the thing about freedom is it enables chaos or progress or sometimes both.
*  And that's kind of the point of the thing.
*  Freedom is empowering, but ultimately unpredictable.
*  And I think in the end, freedom wins.
*  If you enjoy this podcast, subscribe on YouTube, review it on Apple Podcasts, follow on Spotify, support on Patreon or connect with me on Twitter at Lex Friedman.
*  And now here's my conversation with Richard Crabe.
*  From your perspective, can you summarize the important events around this amazing saga that we've been living through of Wall Street bets, the subreddit and GameStop?
*  And in general, just what are your thoughts about it from a technical to the philosophical level?
*  I think it's amazing. It's like my favorite story ever.
*  Like when I was reading about it, I was like, this is the best.
*  And it's also connected with my company, which we can talk about.
*  But what I liked about it is like I like decentralized coordination and looking at the mechanisms that these are Wall Street bets users use to hype each other up,
*  to get excited, to prove that that they bought the stock and they're holding.
*  And and then also to see that how big of an impact that that decentralized coordination had.
*  It really was a big deal.
*  Were you impressed by the distributed coordination, the collaboration amongst like, I don't know what the numbers are.
*  I know Numerize looking at the data after all of this is over and done, it'd be interesting to see,
*  like from a large scale distributed system perspective to see how everything played out.
*  But just from your current perspective, what we know is that obvious to you that such incredible level of coordination could happen,
*  where a lot of people come together in a distributed sense, there's an emergent behavior that happens after that.
*  No, it's not at all obvious.
*  And one of the reasons is the lack of kind of like credibility to coordinate with someone.
*  You need to kind of make credible contracts or credible claims.
*  So if you have a username on our Wall Street bets, like some of them are like deep fucking value is one of that.
*  That's an actual username. By the way, we're talking about there's a website called Reddit.
*  And there's subreddits on it.
*  And a lot of people, mostly anonymous, I think for the most part, anonymous can create user accounts and then can then just talk on forum like style boards.
*  You should know what Reddit is. If you don't know what Reddit is, check it out.
*  If you don't know what Reddit is, maybe go to the awesome subreddit first.
*  A W W with cute pictures of cats and dogs.
*  That's my recommendation. Anyway.
*  Yeah, that would be a good start to read it.
*  When you when you get into it more, go to our Wall Street bets.
*  It gets dark quickly.
*  Oh, we'll probably talk about that, too.
*  So, so, yeah, so there's these users and there's no contracts, like you're saying.
*  There's no contracts. The user anonymous.
*  But there are little things that that do help.
*  So, for example, if you've posted a really good investment idea in the past, that exists on Reddit as well.
*  And it might have lots of upvotes.
*  And that's also kind of like giving credibility to your next to your next thing.
*  And then they are also putting up screenshots like this.
*  This is the these I I here's the trades I've made and here's a screenshot.
*  Now you could fake the screenshot.
*  But but but still, it seems like if you've got a lot of karma
*  and you've had a good performance on the on the community, it somehow becomes credible enough
*  for other people to be like, you know what?
*  He actually probably did put a million dollars into this.
*  And you know what? I can I can follow that trade easily.
*  And there's a bunch of people like that.
*  So you kind of integrating all that information together yourself to see like, huh,
*  there's something happening here. And then you jump onto this little boat of like behavior.
*  Like we should buy the stock or sell the stock.
*  And then another person jumps on another person jumps on.
*  And all of a sudden you have just a huge number of people behaving in the same direction.
*  It's like flock of whatever birds. Exactly.
*  What was strange with this one, it wasn't just let's all buy Tesla.
*  We love Elon. We love Tesla.
*  Let's let's all buy Tesla because that we've heard before.
*  Right. Everybody likes Tesla.
*  Now they do.
*  So what they did with this, in this case, they're buying a stock that was bad.
*  They're buying it because it was bad.
*  And that's really weird because that's a little bit
*  too galaxy brain for for a decentralized community.
*  How did they come up with it? How did they know that was the right one?
*  And the reason they liked it is because it had really, really high short interest.
*  It had been shorted more than its own float, I believe.
*  And so they figured out that if they all bought this bad stock,
*  they could short squeeze some hedge funds.
*  And those hedge funds would have to capitulate and buy the stock at really, really high prices.
*  And we should say that shorted means that these are a bunch of people.
*  When you short a stock, you're betting on the on the you're predicting
*  that the stock is going to go down and then you will make money if it does.
*  And then what's a short squeeze?
*  It's really that if you if you are a hedge fund and you take a big short position
*  in a in a company, there's a certain level at which you can't sustain holding that position.
*  There's no limit to how high a stock can go, but there is a limit to how low it can go.
*  Right. So if you short something, you have infinite loss
*  potential, and if the stock doubles overnight, like GameStop did,
*  you're putting a lot of stress on that hedge fund.
*  And that hedge fund manager might have to say, you know what?
*  I have to get out of the trade.
*  And the only way to get out is to buy the bad stock that they don't want.
*  Like they believe will go down.
*  So it's an interesting situation, particularly because it's not zero sum.
*  If you say, let's make let's all get together and make a bubble in watermelons.
*  You buy a bunch of watermelons, the price goes up, comes down again.
*  It's a it's a it's a zero sum game.
*  If someone's already shorted a stock and you can make them short squeeze,
*  it's actually a positive sum game.
*  So, yes, some redditors will make a lot of money.
*  Some will lose a lot.
*  But actually, the whole group will make money.
*  And that's really that's really why it was such a clever thing for them to do.
*  And coupled with the fact that shorting, I mean, maybe you can push back.
*  But to me, always from an outsider's perspective, seemed
*  I hope I'm not using too strong of a word, but it seemed almost unethical.
*  Maybe not unethical.
*  Maybe it's just the asshole thing to do.
*  It's OK. I'm speaking not from an economics or financial perspective.
*  I'm speaking from just somebody who loves.
*  I'm a fan of a lot of people.
*  I love celebrating the success of a lot of people.
*  And this is like the stock market equivalent of like haters.
*  I know that's not what it is.
*  I know that there's efficient.
*  You want to have an economy, efficient mechanism for punishing
*  sort of overhyped, overvalued things.
*  That's what shorting is designed for.
*  But it just always felt like these people are just because they're not
*  just betting on the loss of the company.
*  It feels like they're also using their leverage and power
*  to manipulate media or just to write articles or just to hate on you
*  on social media.
*  Then you get to see that with the Almas.
*  And so on. So so this is like the man.
*  The people like hedge funds that were shorting are like the
*  the sort of embodiment of the evil or just the bad guy,
*  the overpower for this misusing their power.
*  And here's the crowd, the people that are standing up and rising up.
*  So it's not just that they were able to collaborate on Wall Street
*  bets to sort of effectively make money for themselves.
*  It's also that this is like a symbol of the people getting together
*  and fighting the centralized elites, the powerful and that, you know,
*  I don't know what your thoughts are about that in general.
*  At this stage, it feels like that's really exciting that
*  people have power, just like regular people have power.
*  At the same time, it's scary a little bit because, you know,
*  just studying history, people could be manipulated by charismatic leaders.
*  And so like just like Elon right now is like manipulating,
*  encouraging people to buy Dogecoin or whatever the like
*  that can be good, charismatic leaders and they can be bad, charismatic leaders.
*  And so it's nerve wracking.
*  It's a little bit scary how much power subreddit can have to
*  destroy somebody because right now we're celebrating.
*  They might be attacking or destroying somebody that everybody doesn't like.
*  But what if they attack somebody that is actually good for this world?
*  So that and that's kind of the the
*  awesomeness and the price of freedom is like
*  it could destroy the world or it can save the world.
*  But at this stage, it feels like I don't know.
*  Overall, when you sit back, do you think this was just a positive wave
*  of emergent behavior?
*  Is there something negative about what happened?
*  Well, yeah, the cool thing is that they weren't doing anything.
*  The the reddit people weren't doing anything exotic.
*  It was it was a creative trade, but it wasn't exotic.
*  It wasn't it was just buying the stock.
*  OK, maybe they bought some options, too.
*  But it was the hedge fund that was doing the exotic thing.
*  So I like that it was it's hard to say, well,
*  you know, we've got together and we've put all pooled all our money together.
*  And now there's a company out there that's worth more.
*  What's wrong with that? Yeah, right.
*  But it doesn't talk about, you know, the motivations, which is
*  and then we destroyed some hedge funds in the process.
*  Is there something to be said about the the humor and
*  I don't know, the edginess, sometimes viciousness of that subreddit.
*  I haven't looked at it too much, but it feels like people can be quite
*  aggressive on there.
*  So is there.
*  What is that? Is that what is that what freedom looks like?
*  I think it does. Yeah, you definitely need to let people
*  the one of the things that people have compared it to is the Occupy Wall Street,
*  which is, let's say, you know, some very sincere
*  liberals, like 23 years old, whatever.
*  And they go out with signs and they they have some kind of case to make.
*  But this isn't sincere, really.
*  It's like a little bit more nihilistic, a little bit more YOLO
*  and therefore a little bit more scary, because who's scared of the
*  who's scared of the Wall Street Occupy Wall Street people with the signs?
*  Nobody. But these hedge funds really are scared.
*  I was scared of the of the Wall Street people.
*  I'm still scared of them.
*  Yeah. The anonymity is a bit terrifying and exciting.
*  Yeah. I mean, yeah, I don't know what to do with it.
*  You know, I've been following events in Russia, for example.
*  It's like there's a struggle between centralized power and the distributed.
*  I mean, that's the struggle of the history of human civilization. Right.
*  But this on the Internet,
*  just that you can multiply people like some of them don't have to be real.
*  Like you can probably create bots like.
*  It starts getting me me as a programmer, I start to think like, hmm, me is one person.
*  How much chaos can can I create by writing some bots?
*  Yeah. And I'm sure I'm not the only one thinking that there's
*  I'm sure there's hundreds of thousands of good developers out there
*  listening to this, thinking the same thing.
*  And then as that develops further and further in the next decade or two,
*  what impact does that have on financial markets, on just destruction of
*  reputations of just or politics?
*  You know, the bickering of left and right political discourse,
*  the dynamics of that being manipulated by, you know,
*  people talk about like Russian bots or whatever.
*  We're probably in the very early stage of that. Right. Exactly.
*  And this is a good example.
*  So do you have a sense that most of Wall Street bets folks are actually individual people?
*  Right. That's the feeling I have is there's just individual, maybe young investors
*  just doing a little bit of an investment, but just on a large scale.
*  Yeah, exactly. The reason I found out I've known about Wall Street bets for a while.
*  But the reason I found out GameStop was this.
*  I met somebody at a party who told me about it, and he was like 21 years old.
*  And he's like, it's going to go up 100 percent in the next one day.
*  We're talking about in last year.
*  This was probably no, this was, yeah, a few days ago.
*  I went out. Yeah, it was like maybe maybe two weeks ago or something.
*  So it was it was already high GameStop.
*  But it was just strange to me that there was someone telling me at a party
*  how to trade stocks, who was like 21 years old.
*  And and it started to.
*  Yeah, I started to look into it.
*  And yeah, and he did make he made it.
*  Yeah, he made 140 percent in one day.
*  He was right. And now he's supercharged.
*  He's a little bit wealthier.
*  And now he's going to look wait for the next thing.
*  And this decentralized entity is just going to get bigger and bigger.
*  And they're going to together search for the next thing.
*  So there's thousands of folks like him.
*  And they're going to probably search for the next thing to attack
*  people that have power in this world that sit there with power right now
*  in government and in finance and any kind of position
*  are probably a little bit scared right now.
*  And honestly, that's probably a little bit good.
*  It's dangerous, but it's good.
*  Yeah, it certainly makes you think twice about shorting.
*  It certainly makes you think about putting a lot of money into a short
*  like these funds put a lot into one one or two names.
*  And so it was very, very badly risk managed.
*  Do you think shorting is?
*  Can you speak at a high level just for your own as a person?
*  Is it good for the world?
*  Is it good for markets?
*  I do think that the two kinds of shorting, evil shorting
*  and chill shorting,
*  evil shorting is what Melvin Capital was doing.
*  And it's like you put a huge position down.
*  You get all your buddies to also short it and you start making press
*  and and trying to bring this company down.
*  And I don't think in some cases,
*  you go out after like fraudulent companies say this company is a fraud.
*  Maybe that's OK.
*  But but they weren't even saying games up.
*  They're just saying it's a bad company and we're going to bring it to the ground,
*  bring it to its knees.
*  A quant fund like Numeri,
*  we always have lots of positions and we never have a position
*  that's like more than one percent of our fund.
*  So we actually have right now 250 shorts.
*  I don't know any of them except for one,
*  because it was one of the meme stocks.
*  But yeah,
*  but it's we shorting them not to make them go.
*  We don't even want them to go down necessarily.
*  That doesn't sound a bit strange to say that, but we just want them to
*  to not go up as much as our longs.
*  Right. So by shorting a little bit,
*  we can actually go long more in the things we do believe in.
*  So when we were going long in Tesla, we could do it with more money than we had
*  because we borrow from banks who would lend us money
*  because we had longs and shorts, because we didn't have market exposure,
*  you know, market risk.
*  And so I think that's a good thing because that means, you know,
*  we can short the oil companies and go long, Tesla and make the future come
*  forward faster. And I do think that's not a bad thing.
*  So we talked about this incredible distributed system created by Wall Street
*  Bets. And then there's a platform, which is Robin Hood,
*  which allows investors to efficiently as far as you can correct me if I'm wrong.
*  But you know, there's those and there's others and this Numeri that allow you to
*  make it accessible for people to invest. But that said,
*  Robin Hood was in a centralized way,
*  applied its power to restrict trading on the stock that we're referring to.
*  Do you have a thoughts on actually like the things that happened?
*  I don't know how much you were paying attention to sort of the shadiness
*  around the whole thing. Do you think it was forced to do it?
*  Or was there something shady going on? What are your thoughts in general?
*  Well, I think I want to see the alternate history.
*  Like I want to see the counterfactual history of them not doing that.
*  How bad would it have gotten for hedge funds?
*  How much more damage could have been done if the momentum of these short
*  squeezes could continue?
*  What happens when there are short squeezes, even if
*  they're in a few stocks, they affect kind of all the other shorts too.
*  And suddenly brokers are saying things like, you need to put up more collateral.
*  So we had a short, it wasn't GameStop, luckily,
*  it was BlackBerry and it went up like a hundred percent in a day.
*  It was one of these meme stocks, super bad company. The AIs don't like it. Okay.
*  The AIs think it's going down.
*  What's a meme stock?
*  A meme stock is kind of a new term for these stocks that
*  catch memetic momentum on Reddit.
*  And so the meme stocks were GameStop, the biggest one,
*  GameStonk, as Elon calls it, AMC.
*  And BlackBerry was one, Nokia was one.
*  So these are high short interest stocks as well.
*  So these are targeted stocks that some people say, oh, isn't it,
*  isn't it adorable that these, these people are investing money in these
*  companies that are, you know, nostalgic.
*  It's like you go into the AMC movie theater, it's like nostalgic. It's like, no,
*  it's not why they're doing it. It's that they had love short interest.
*  That was the main thing. And so they were high chance of short squeeze.
*  In saying, I would love to see an alternate history.
*  Do you have a sense that that,
*  what is your prediction of what that history would have looked like?
*  Well, you wouldn't have needed very many more days of that kind of chaos to,
*  to hurt hedge funds.
*  I think it's underrated how, how damaging it could have been.
*  Because when your shorts go up,
*  your collateral requirements for them go up. It's similar to Robinhood.
*  Like we have a prime broker that says, said to us, you need to put up,
*  you know, like $40 per, per a hundred dollars of short exposure.
*  And then the next day they said, actually you have to put up, you know,
*  all of it, a hundred percent. And we were like, what?
*  But if that happens, that, if that happens to all the short,
*  all the commonly held hedge fund shorts,
*  because they were all kind of holding the same things.
*  If that happens, not only do you have to cover the short,
*  which means you're buying the bad companies,
*  you need to sell your good companies in order to cover the short.
*  So suddenly like all the good companies,
*  all the ones that hedge funds like are coming down and all the,
*  all the ones that the hedge funds hate are going up in a
*  cascading way.
*  So I believe that if you could have had a few more days of
*  GameStock doubling, AMC doubling,
*  you would have had more and more hedge fund deleveraging.
*  But so hedge funds, I mean, they get a lot of shit, but they,
*  do you have a sense that they do some good for the world? I mean, ultimately,
*  so, okay, first of all,
*  Wall Street bets itself is kind of distributed hedge fund and URI is a kind of
*  hedge fund. So I got, hedge fund is a very broad category. I mean,
*  like if some of those were destroyed, would that be good for the world?
*  Or is it, would there be coupled with the,
*  the destroying the evil shorting?
*  Would there be just a lot of pain in terms of investment in good companies?
*  Yeah.
*  A thing I like to tell people if they hate hedge funds is I don't think you want
*  to rerun American economic history without hedge funds.
*  So on mass they're, they're, yeah, they're good.
*  Yeah. You really wouldn't want to, because hedge funds are kind of like picking
*  up, they're making liquidity, right? In stocks.
*  And so if you'd like, if you love venture capitalists,
*  they're investing in new technology. It's so good.
*  You have to also kind of like hedge funds because they're the reason venture
*  capitalists exists because their companies can have a liquidity event when they
*  go to the public markets.
*  So it's kind of essential that we have them.
*  There are many different kinds of them.
*  I believe we could maybe get away with only having an AI hedge fund.
*  But we don't necessarily need these evil billions type hedge funds that make the
*  media and try to kill companies, but we definitely need hedge funds.
*  Maybe from your perspective,
*  because you run such an organization and Vlad,
*  the CEO of Robinhood sort of had to make decisions really quickly.
*  Probably had to wake up in the middle of the night kind of thing. You know,
*  and he also had a conversation with Elon Musk on Clubhouse,
*  which I just signed up for. It was,
*  it was a fascinating one of the great journalistic performances of our time with
*  Elon Musk. How hilarious would it be if he gets a pulse?
*  And then his Wikipedia would be like journalist and part time entrepreneur.
*  Business Magnet.
*  You know, I don't know if you can comment on any aspects of that,
*  but like if you were Vlad, how would you do things differently?
*  What are your thoughts about his interaction with Elon?
*  How he should have played it differently? Like,
*  I guess there's a lot of aspects to this interaction.
*  One is about transparency.
*  Like how much do you want to tell people about really what went down?
*  There's NDAs potentially involved.
*  Uh, how much in private do you want to push back and say,
*  no, fuck you to centralized power, whatever the phone calls you're getting,
*  which I'm sure he's getting some kind of phone calls that might not be
*  contractual. Like it's not contracts that are forcing him,
*  but he was being, uh, what do you call it?
*  Like pressured to behave in certain kinds of ways from all kinds of directions.
*  Like what, uh, what do you take from, uh, this whole situation?
*  I was very excited to see Vlad's response. I mean,
*  it's pretty cool to have him talk to Elon.
*  And one of the things that struck me in the first few seconds of Vlad speaking
*  was like, I was like, is Vlad like a boomer?
*  Like, like, but here we are,
*  like he seemed like a 55 year old man talking to a 20 year old.
*  Elon was like the 20 year old and he's like the 55 year old man.
*  You can see why Citadel are NMR buddies, right? Like you can,
*  you can see why it's like, this is a, this is a nice, it's not a bad thing.
*  It's like, he's, it's like a, he's got a, like a respectable professional attitude.
*  Well, he also tried to do like a jokey thing, like, no,
*  we're not being ageist here. Boomer, uh, but like, like, uh,
*  like a 60 year old CEO of bank of America would try to make a joke for the kids.
*  That's what Vlad's talking about. Yeah. Yeah. I was like, what is this?
*  This guy's like, what is he 30? Yeah. Uh, and I'm like, this is weird.
*  Yeah. Um, but I think,
*  and maybe that's also what I like about Elon's kind of influence on American
*  business is like, he's super like anti the professional, right? Like why,
*  why say, why say, you know, a hundred words about nothing. Uh,
*  and so I liked how he was cutting in and saying, Vlad, what do you mean?
*  Spill the beans, bro. Yeah. So you, you don't have to be courteous.
*  It's like the first principles thinking it's like, what the hell happened.
*  And let's just talk like normal people. The problem of course is,
*  uh, you know, for Elon, uh, it's cost them, what is it?
*  Tens of millions of dollars is tweeting like that,
*  but perhaps it's a worthy price to pay because ultimately there's something
*  magical about just being real and honest and just going off the cuff and making
*  the mistakes and paying for them, but just being real.
*  And then moments like this,
*  that was an opportunity for Vlad to be that. And it felt like he wasn't.
*  Do you think there, do you think we'll ever find out what really went down?
*  If there was something shady underneath it all?
*  Yeah. I mean it, it would be sad if nothing shady happened, right?
*  But his presence made it shady.
*  Sometimes I feel like that would Mark Zuckerberg, the CEO of Facebook.
*  Sometimes I feel like, yeah,
*  there's a lot of shady things that Facebook is doing,
*  but sometimes I think he makes it look worse by the way he presents himself
*  about those things.
*  Like I honestly think that a large amount of people at Facebook just have a
*  huge unstable chaotic system and they're all not all,
*  but mass are trying to do good with this chaotic system.
*  But the presentation is like,
*  it sounds like there's a lot of back room conversations that are trying to
*  manipulate people.
*  And there's,
*  there's something about the realness that Elon has that it feels like CEO should
*  have and Vlad had that opportunity.
*  I think Mark Zuckerberg had that too when he was younger,
*  younger and somebody said, you gotta be more professional, man.
*  You can't say,
*  you know,
*  lol to an interview.
*  Uh,
*  and then suddenly he became like this distance person that was hot.
*  I'd like,
*  you'd rather have him make mistakes,
*  but be honest than be like professional and never make mistakes.
*  Yeah.
*  One of the difficult tires I think is like marketing people or like PR people is
*  you have to hire people that get the fact that you can say lol on an interview
*  or like,
*  you know,
*  take risks as opposed to what the PR I thought to quite a few big CEOs and the
*  people around them are trying to constantly minimize risk of like,
*  what if he says the wrong thing?
*  What if she says the wrong thing?
*  It's like what?
*  Like be careful.
*  It's constantly like,
*  Ooh,
*  like I don't know.
*  And there's this nervous energy that builds up over time with larger,
*  larger teams where the whole thing,
*  like I visited YouTube,
*  for example,
*  everybody had talked at YouTube,
*  incredible engineering and incredible system,
*  but everybody is scared.
*  Like let's be a,
*  let's be honest about this like madness that we have going on of huge amounts of
*  video that we can't possibly ever handle.
*  There's a bunch of hate on YouTube.
*  There's this chaos of comments,
*  a bunch of conspiracy theories,
*  some of which might be true.
*  And then just like this mess that we're dealing with and it's exciting,
*  it's beautiful.
*  It's a place where like democratizes education,
*  all that kind of stuff.
*  And instead they're all like sitting in like very,
*  trying to be very polite and saying like,
*  well,
*  we're just want to improve the health of our platforms.
*  Like,
*  discussing like,
*  all right,
*  man,
*  let's just be real.
*  Let's,
*  let's,
*  let's both advertise how amazing this fricking thing is,
*  but also to say like,
*  we don't know what we're doing.
*  We have all these Nazis posting videos on YouTube.
*  We don't,
*  we don't know how to like handle it.
*  And just being real like that,
*  I suppose that's just the skill.
*  Um,
*  maybe it can't be taught,
*  but over time the,
*  whatever the dynamics of the company is,
*  it does seem like Zuckerberg and others get worn down.
*  They just get tired.
*  Yeah.
*  Uh,
*  they get tired of not being real,
*  of not being real,
*  which is,
*  uh,
*  sad.
*  So let's talk about Numeroe,
*  which is an incredible company,
*  uh,
*  system idea,
*  I think,
*  but good place to start.
*  What is Numeroe and how does it work?
*  So Numeroe is the first hedge fund that gives away all of its data.
*  So this is like probably the last thing a hedge fund would do.
*  Right.
*  Why would we give away a data?
*  It's like giving away your edge.
*  Um,
*  but the reason we do it is because we're looking for people to model our
*  data.
*  And the way we do it is by obfuscating the data.
*  So when you get,
*  when you look at numeroized data that you can download for free,
*  it just looks like like a million rows of numbers between zero and one.
*  And you have no idea what the columns mean,
*  but you do know that if you're good at machine learning or have done
*  regressions before,
*  you know that I can still find patterns in this data,
*  even though I don't know,
*  I don't know what the features mean.
*  And the data itself is time series data.
*  And even though it's obfuscated,
*  anonymized,
*  what is the source data?
*  Like approximately what are we talking about?
*  So we are buying data from lots of different data vendors.
*  Um,
*  and they would also never want us to share that data.
*  Um,
*  so we have strict contracts with them.
*  So we only,
*  we only can,
*  but it,
*  but that's the kind of data you could never buy yourself unless you had maybe a
*  million dollars a year of budget to buy data.
*  So what's happened with the hedge fund industry is you have a lot of talented
*  people who used to be able to trade and still can trade,
*  but now they have such a data disadvantage.
*  It would never make sense for them to,
*  um,
*  to,
*  to trade themselves.
*  But Numeri by giving away this obfuscated data,
*  we can give them a really,
*  really high quality data set that's,
*  that would otherwise be very expensive and they can use whatever new machine
*  learning technique they want,
*  uh,
*  to find patterns in that data that we can use in our hedge fund.
*  And so how much variety is there in underlying data?
*  We're talking about,
*  uh,
*  I apologize if I'm using the wrong terms,
*  but there's one is just like the stock price,
*  the other there's like options and all that kind of stuff.
*  Like the,
*  what are they called order books or whatever?
*  Like is there maybe other are totally unrelated to directly to the stock market
*  data,
*  like like natural language as well,
*  all that kind of stuff.
*  Yeah,
*  we were really focused on,
*  um,
*  stock data that's specific to stocks.
*  So,
*  um,
*  things like you can have like a P every stock has like a P E ratio for some
*  stocks.
*  It's not as meaningful,
*  but every stock has that every stock has one year momentum,
*  how much they went up in the last year.
*  Um,
*  but those are very common factors,
*  but we try to get lots and lots of those factors.
*  That we have for many,
*  many years,
*  like 15,
*  20 years history.
*  Um,
*  and,
*  and then the setup of the problem is commonly in quant called like
*  cross-sectional global equity.
*  You're not really trying to say,
*  I want,
*  I believe the stock will go up.
*  You're trying to say,
*  um,
*  the like relative position of this stock in feature space,
*  uh,
*  makes it not a bad buy in a,
*  in a portfolio.
*  So it captures some period of time.
*  And you're trying to find the patterns,
*  the dynamics captured by the data of that period of time in order to make short
*  term predictions about what's going to happen.
*  Yeah.
*  So our predictions also not that short.
*  We're not really,
*  um,
*  caring about things like order books and tech data,
*  not high frequency at all.
*  We're actually holding things for quite a bit longer.
*  Uh,
*  so our prediction time horizon is about one month.
*  We ended up holding stocks for maybe like three or four months.
*  So I kind of believe that's a little bit more of a,
*  so I kind of believe that's a little bit more like investing than,
*  um,
*  then kind of plumbing,
*  like to go long a stock that's mispriced on one exchange and
*  shorter on another exchange,
*  that's just arbitrage.
*  But what we're trying to do is really know,
*  know,
*  know something more about the longer term future of the stock.
*  Yeah.
*  So from the pattern from these like periods of,
*  uh,
*  time series data,
*  you're trying to understand something fundamental about the stock,
*  not like about deep value about like,
*  it's big in the context of the market is like underpriced overpriced,
*  all that kind of stuff.
*  So like this is about investing.
*  It's not about just like you said,
*  high frequency trading,
*  which I think is a fascinating open question for machine learning perspective.
*  But just to like sort of build on that.
*  So you've anonymized the data and now you're giving away the data.
*  And then now anyone can try to,
*  uh,
*  build algorithms that make investing decisions on top of that data or
*  predictions in the top of that data.
*  And so that that's,
*  um,
*  what is it?
*  So what does that look like?
*  What's the goal of that?
*  What are the underlying principles of that?
*  So the first thing is,
*  you know,
*  we could obviously model that data in house,
*  right?
*  We can make an XGBoost model on the data.
*  Um,
*  and that would be quite good too.
*  But what we're trying to do is by,
*  by,
*  uh,
*  opening it up and letting anybody participate,
*  uh,
*  we can do quite a lot better than if we modeled it ourselves.
*  And a lot better on the stock market doesn't need to be very much.
*  Like it really matters the difference between if you can make 10 and 12% in an
*  equity market,
*  neutral hedge fund,
*  because the whole,
*  usually you're charged,
*  you're charging 2% fees.
*  So if you can do 2% better,
*  that's like all your fees,
*  it's worth it.
*  So we're trying to make sure that we always have the best possible model as new
*  machine learning libraries come out,
*  new new techniques come out,
*  they get automatically synthesized.
*  Like if there's a great paper on supervised learning,
*  someone on Numeri will figure out how to use it on numerized data.
*  And is there an ensemble of,
*  uh,
*  models going on or is it always,
*  or is it more towards kind of like one or two or three,
*  like best performing models?
*  So the way we decide on how to weight all of the predictions together
*  is by how much the users are staking on them.
*  How much of the cryptocurrency that they're putting behind their models.
*  So they're saying,
*  I believe in my model,
*  you can trust me because I'm going to put skin in the game.
*  And so we can take the stake weighted predictions from all our users,
*  add those together, average those together.
*  And that's a much better model than any one model in the,
*  in the sum because ensembling a lot of models together is kind of the key thing
*  you need to do in investing too.
*  Yeah. So you're putting,
*  so there's a kind of duality from the user,
*  from the perspective of a machine learning engineer where you're,
*  is both a competition, just a really interesting,
*  difficult machine learning problem.
*  And it's a way to,
*  to invest algorithmically. So like,
*  you're and, but the,
*  the way to invest algorithmically also is a way to put skin in the game that
*  communicates to you that you're the quality of the algorithm and also forces
*  you to really be serious about the models that you build.
*  So it's like everything just works nicely together. Like,
*  I guess one way to say that is the interests are aligned.
*  Okay. So it's just like poker is not,
*  not fun when it's like for very low stakes,
*  the higher the stakes,
*  the more the dynamics of the system starts playing out correctly as like as a
*  small side note, is there something you can say about which kind,
*  looking at the big broad view of machine learning today or AI,
*  what kind of algorithms seem to do good in these kinds of competitions at this
*  time? Is there some universal thing you can say like neural networks suck,
*  recurrent neural networks suck, transformers suck, or they're awesome.
*  Like old school sort of more basic kind of classifiers are better. All the,
*  is there,
*  is there some kind of conclusions so far that you can say?
*  There is definitely something pretty nice about tree models like,
*  like XG boosts.
*  And they just seem to work pretty nicely on this type of data.
*  So out of the box,
*  if you're trying to come a hundredth in the competition or in the tournament,
*  maybe you would try it, use that.
*  But what's,
*  what's particularly interesting about the problem that not many people understand.
*  If you're familiar with machine learning,
*  this typically will surprise you when you model our data.
*  So one of the things that you look at in finance is you don't want to be too
*  exposed to any one risk.
*  Like even if the best sector in the world to invest in over the last 10 years was
*  tech, you would not, does not mean you should put all of your money into tech.
*  So the, if you train a model, it would say, put all your money into tech.
*  It's super good.
*  But what you want to do is actually be very careful of how much of this exposure
*  you have to certain features.
*  So on Numeri,
*  what a lot of people figure out is actually if you train a model on this kind of
*  data,
*  you want to somehow neutralize or minimize your exposure to these,
*  to certain features,
*  which is unusual because if,
*  if you did train a stoplight or stop street detection on computer,
*  computer vision,
*  the, your, your favorite feature,
*  let's say you could and you have an auto encoder and it's figuring out, okay,
*  it's going to be red and it's going to be white. You've,
*  that's the last thing you want to be.
*  You want to reduce your exposure to,
*  why would you reduce your exposure to the thing that's helping you,
*  your model the most?
*  And that's actually this counterintuitive thing you have to do with machine
*  learning on financial data.
*  So reducing it's reducing your exposure would help you generalize the things that
*  are so basically financial data has a large amount of patterns that appeared in
*  the past and also a large amount of patterns that have not appeared in the
*  past.
*  And so like in that sense you have to reduce the exposure to red lights,
*  to, to the color red. That's interesting,
*  but how much of this is art and how much of it is science from your perspective
*  so far in terms of as you start to climb from the hundredth position to the 90
*  fifth in the competition?
*  Yeah, well, if you do make yourself super exposed to a one or two features,
*  you can have a lot of volatility when you're playing Numerai.
*  You could maybe very rapidly rise to be high if you were getting lucky.
*  Yes.
*  And that's a bit like the stock market. Sure. Take on massive risk exposure,
*  put all your money into one stock and you might make a hundred percent,
*  but it doesn't in the long run work out very well.
*  And so the best users are,
*  are trying to stay high for as long as possible and not,
*  not necessarily try to be first for a little bit.
*  So me, a developer, machine learning researcher,
*  how do I Lex Freeman participate in this competition and how do others,
*  I'm sure there'll be a lot of others interested in participating in this
*  competition. What are, uh, let's see, there's like a million questions,
*  but like first one is how do I get started?
*  Well, you can go to numera.ai sign up,
*  download the data and on the data is pretty small.
*  In the data pack you download, there's like an example script,
*  Python scripts that just builds a XGBoost model very quickly from the data.
*  And so in a very short time you can have an example model.
*  Is that a particular structure? Like what, uh,
*  is this model then submitted somewhere?
*  So there's needs to be some kind of structure that communicates with some kind
*  of API. Like how does the whole, how does the,
*  your model once you built the ones to create a little, little baby Frankenstein,
*  how does it then live in its,
*  we want you to keep your baby Frankenstein at home and take care of it.
*  We don't want it. So we, you never upload your model to us.
*  You always, um, only giving us predictions.
*  So we never see the code that wrote your model, which is pretty cool.
*  That our whole hedge fund is built from models where we've never ever seen the
*  code. Um,
*  but it's important for the users because it's their IP,
*  they want to give it to us. So they've got it themselves,
*  but they can basically almost like license the f the predictions from that
*  product. So what some users do is they set up a,
*  a compute server and we call numera compute.
*  It's like a little AWS kind of image and you can automate this process.
*  So we can ping you, we can be like, we need more predictions now,
*  and then you send it to us.
*  Okay, cool. So that's, uh, is that described somewhere?
*  Like what the preferred is the AWS or whether another cloud platform is there,
*  I mean, is there sort of specific technical things you want to say that comes to
*  mind that, uh, is a good path for getting started. So download the data,
*  maybe play around, see if, uh, you can modify the basic,
*  uh, the algorithm provided in the example.
*  And then you, what set up a little server on the AWS that then runs this model
*  and takes pings and then makes predictions.
*  And I was like, how does your own money actually come into play doing the stake
*  of, um, cryptocurrency?
*  Yeah. So you don't have to stake. You can start without staking.
*  And many users might try for months, uh,
*  without staking anything at all to see if their model works on the real life
*  data, right. And is not overfit. Um, but then, uh,
*  you can get numeraire, uh, many different ways. You can buy it on, um,
*  you can buy some on Coinbase. You can buy some on Uniswap.
*  You can buy some on Binance. Um,
*  So what did you say this is, uh, how do you pronounce it?
*  So this is the numeraire, uh, cryptocurrency. Yeah. NMR. NMR.
*  What you just say NMR. It is, it is technically called numeraire.
*  Numerair. I like it. Yeah. But NMR is simple.
*  NMR, numeraire. Okay. So, and you could buy it, uh, you know,
*  basically anywhere. Yeah.
*  So it's a bit strange because sometimes people are like, is this like pay to play?
*  Right. And it's like, yeah,
*  you need to put some money down to show us you believe in your model, but, uh,
*  weirdly we're not selling you the cri- like you can't buy the cryptocurrency from
*  us. Right. It's like, it's also,
*  we never, if you're, if you do badly, um,
*  we destroy your cryptocurrency. Okay. That's not good, right?
*  You don't want it to be destroyed, but what's good about it is it's also not coming
*  to us. Right. So it's not like we win when you lose or, or something like that,
*  like we're the house, like we're definitely on the same team. Yes.
*  You're helping us make a hedge fund that's never been done before. Yeah.
*  So again, interests are aligned. There's no, uh, there's no tension there at all,
*  which is really fascinating. You've given away everything.
*  And then the IP is owned by the sort of the code. You never share the code.
*  That's fascinating. Um, so since I have you here and you said, uh,
*  a hundredth, I didn't ask out of how many, so we'll just,
*  but if, uh, if I then once you get started and you find this interesting,
*  uh, how do you then win or do well,
*  but also how do you potentially try to win if this is something you want to take
*  on seriously from the machine learning perspective,
*  not from a financial perspective?
*  Yeah. I think, um, the first of all, you want to talk to the community.
*  People are pretty open. Uh,
*  we give out really interesting scripts and ideas for things you might want to
*  try. Um, and, uh,
*  but you also going to need a lot of compute probably.
*  And so some of the best users are, are, you know,
*  actually the very first time someone won on Numero, I would,
*  I wrote them a personal email. It's like, you know, you've won some money.
*  We're so excited to give you $300. And then they said,
*  I spend way more on the compute. Um, but,
*  this is fundamentally a machine learning problem first. I think,
*  is this is one of the exciting things. I don't know if we'll,
*  in how many ways you can approach this, but really this is less about
*  kind of no offense, but like finance,
*  people finance minded people. They're also, I'm sure great people,
*  but it feels like from the community that I've experienced,
*  these are people who see finance as a fascinating,
*  uh, problem space, the source of data,
*  but ultimately they're machine learning people or AI people,
*  which is a very different kind of flavor of community. And, um, I mean,
*  I should say to that, uh, I'd love,
*  I'd love to participate in this and I will participate in this and I'd love to
*  hear from other people. If you're listening to this,
*  if you're a machine learning person, you should participate in it and tell me,
*  uh, give me some hints, um, how I can do well at this thing. Cause this boomer,
*  uh, I'm not sure I still got it, but cause some of it is, uh,
*  it's like a Kaggle competitions.
*  Like some of it is certainly set up ideas,
*  like research ideas, like fundamental innovation,
*  but I'm sure some of it is like deeply understanding,
*  getting like an intuition about the data.
*  And then like a lot of it will be like figuring out like what works like tricks.
*  I mean, you could argue most of deep learning research is just tricks on top of
*  tricks, but there's a,
*  that some of it is just the art of getting to know how to work in a really
*  difficult machine learning problem.
*  And I think what's important,
*  the important difference with something like a Kaggle competition where they'll
*  set up this kind of toy problem and then there will be an out of sample test,
*  like, Hey, you did well out of sample. And this is like, okay, cool. Um,
*  but what's cool with Numerize is you're, you're,
*  the out of sample is the real life stock market. We,
*  we don't even know, like we don't know the answer to the problem. We don't,
*  like you'll have to find out live.
*  And so we've had users who've,
*  who've like submitted every week for, for like four years. Um,
*  because it's kind of a interest.
*  It's a, we say it's the hardest data science problem on the planet. Right.
*  And it sounds, maybe sounds like maybe a bit too much for like a marketing thing,
*  but it's the hardest because it's the stock market. It's like,
*  literally there are like billions of dollars at stake and like,
*  no one's like letting it be inefficient on purpose.
*  So if you can find something that works on Numerize,
*  you really have something that,
*  that is like working on the real stock market.
*  Yeah. Because there's like humans involved in the stock market. I mean,
*  that's, uh, you know,
*  you could argue there might be harder data sets that may be predicting the
*  weather, all those kinds of things. But the,
*  the fundamental statement here is, which I like, I was thinking like,
*  is this really the hardest data science problem? And you,
*  you start thinking about that,
*  but ultimately it also boils down to a problem where the data is accessible.
*  It's made accessible,
*  made really easy and efficient at like submitting
*  algorithms. So it's not just, you know,
*  it's not about the data being out there, like the weather,
*  it's about making the data super accessible,
*  making the ability of community around it. Like this is what ImageNet did.
*  Exactly. Like it's not just, there's always images.
*  The point is you aggregate them together, you give it a little title,
*  this is a community and that, that was one of the hardest, right?
*  For a time, uh,
*  and most important data science problems in the world, uh,
*  because it was accessible because it was, uh, made, uh, sort of like,
*  there was a mechanisms by which like standards and mechanisms by which to judge
*  your performance, all those kinds of things and numerize.
*  I actually just step up from that.
*  Is there something more you can say about why from your perspective,
*  it's the hardest, uh, problem in the world? I mean,
*  you said it's connected to the market.
*  So if you can find a pattern in the market,
*  that's a really difficult thing to do because a lot of people are trying to do
*  it.
*  Exactly. But there's also the,
*  the biggest one is it's it's non-stationary time series.
*  We've tried to regularize the data so you can find patterns, uh,
*  by, by doing certain things to the features and the target.
*  But ultimately you're in a space where you don't,
*  there's no guarantees that the out of sample distributions will,
*  uh, conform to any of the training data. And,
*  and every single, um, era, which we call on the website,
*  like every single era in the data,
*  which is like sort of showing you the order of the time. Um,
*  it's, it's even the training data is, has the same, same dislocations.
*  And, um, so yeah, it's, and then so,
*  and then there's yeah, there's so many things that might, um,
*  might, you might want to try this, this, like,
*  there's unlimited possible number of models, right? Um, and so,
*  by, by having it, um, be open, uh,
*  we can at least search that space.
*  It's zooming back out into the philosophical. You said that Numeri is, uh,
*  very much like Wall Street pets. Uh, is, is there,
*  I think it'd be interesting to dig in why you think so.
*  I think you're speaking to the distributed nature of the two and the power of
*  the people nature of the two.
*  So maybe can you speak to the similarities and the differences and in which way
*  is numeri more powerful in which way is Wall Street bets more powerful?
*  Yeah, this is why the Wall Street bet story is so interesting to me because it's
*  like, feels like we're connected. Um, and looking at how,
*  just looking at the forum of Wall Street bets, it's,
*  I was talking earlier about how, how can you make credible claims?
*  You're anonymous. Okay. Well, maybe you can take a screenshot. How,
*  or maybe you can upvote someone. Maybe you can have karma on Reddit.
*  And those kinds of things make this emerging thing possible.
*  Numeri, it didn't work at all when we started.
*  It didn't work at all. Why? People made multiple accounts.
*  They made really random models and hope they would get lucky.
*  And some of them did.
*  Yes.
*  Staking was our like solution to, could we,
*  could we make it so that we could trust,
*  we could know which model people believed in the most and we could weight
*  models that had high stake more and effectively coordinate this group of people
*  to be like, well, actually there's no incentive to creating bot accounts anymore.
*  Either I stake my accounts, in which case I should believe in them,
*  because I could lose my stake or I don't.
*  And that's a very powerful thing that having a negative incentive and a
*  positive incentive can make, can make things a lot better.
*  And staking is like this, is this really nice,
*  like key thing about blockchain.
*  It's like something special you can do where they're not even trusting us with
*  their stake in some ways. They're trusting the blockchain, right?
*  So the incentives, like you say,
*  it's about making these perfect incentives so that you can have coordination to
*  solve one problem. And nowadays I,
*  I sleep easy because I have less money in my own hedge fund than our users are
*  staking on their models.
*  That's powerful in some sense from a human psychology perspective,
*  it's fascinating that the Wall Street bets worked at all, right?
*  That the, the amidst that chaos, emerging behavior,
*  like behavior that made sense emerged,
*  it would be fascinating to think if numeralized style staking could then be
*  transferred to places like Reddit, you know,
*  and not necessarily for financial investments, but like,
*  I wish sometimes people would, you know,
*  would have to stake something in the comments they make on the internet.
*  Yeah. Like that's, that's the problem.
*  That anonymity is like anonymity is freedom and power that you don't have to,
*  you can speak your mind, but it's too easy to just be shitty.
*  Exactly. So this, I mean,
*  you're making me realize from a profoundly philosophical aspect,
*  numeralized staking is a really clean way to solve this problem.
*  It's a really beautiful way. Of course, it only,
*  with numeralized currently works for a very particular problem, right?
*  Not for human interaction on the internet, but that's fascinating.
*  Yeah. There's nothing for it to stop people. In fact,
*  we've opened source like the code we use for staking in a protocol we call a
*  razor. And any, if Reddit wanted to,
*  they could even use that code to do have,
*  have enabled staking on our Wall Street bets.
*  And they're actually researching now they've had some Ethereum grants on how
*  could they have more crypto stuff in there in Ethereum,
*  because wouldn't that be interesting? Like, imagine you could, um,
*  instead of seeing a screenshot, like guys, I promise, I will not, uh,
*  sell my GameStop. We're just going to go huge. We're not going to sell at all.
*  Um, and here is a smart contract,
*  which no one in the world, including me can undo that says,
*  my, I have staked, um, millions against this claim.
*  Um, that's powerful. And then what could you do?
*  And of course it doesn't have to be millions.
*  It could be just very small amount,
*  but then it's just a huge number of users doing that kind of stake.
*  Exactly.
*  That, you know, that could change the internet.
*  It would change and the man Wall Street, it would, they would not,
*  they would never have been able to,
*  they would still be short squeezing one day after the next,
*  every single hedge fund collapsing.
*  If we look into the future,
*  do you think it's possible that new Morai style infrastructure where AI systems
*  backed by humans are doing the trading is what the entirety of the stock market
*  is or the entirety of the economy is run by basically this army of AI systems
*  with high level human supervision?
*  Yeah. The thing is that some of them could be, could be bad actors.
*  Um, some of the humans.
*  No, well these systems could be tricky. So actually I once met a hedge fund
*  manager and this is kind of interesting. He said, um, very famous one.
*  And he said, um, we can see,
*  sometimes we can see things in the market where we know we can make money,
*  but it will mess shit up. Yeah. We know we can make money,
*  but it will mess things up and we choose not to do those things.
*  And on the one hand, maybe this is like, Oh, you're being super arrogant.
*  Did like, of course you can't, you can't do this,
*  but maybe he can and maybe he really isn't doing things he knows he could do,
*  but would change, you know, be pretty bad.
*  Would the Reddit army have that kind of, uh,
*  morality or concern, uh, for what they're doing?
*  Probably not based on what we've seen the madness of crowds.
*  There'll be like one person that says, Hey, maybe,
*  and then they get trampled over. Uh, that's,
*  that's the terrifying thing actually. This, uh,
*  a lot of people have written about this is somehow that like little voice that's
*  human morality gets silence when we get in a groups and start chanting.
*  And that's terrifying. But like, I think, uh, maybe I misunderstood.
*  I thought that, um, you're saying AI systems can be dangerous,
*  but you just described how humans can be dangerous. So which is safer.
*  So, I mean, one thing is, uh, numera, yeah.
*  So wall street bets, these kinds of like, these kinds of attacks,
*  like it's not possible to model numera is data and then come up with the idea
*  from the model. Let's short squeeze game stop. Right.
*  It's not even framed in that way. It's not like possible to have that idea.
*  So, but it is possible for like kind of a bunch of humans.
*  So I think there's it's numera I could get very powerful, uh,
*  without it being dangerous,
*  but wall street bets needs to get a little bit more powerful and it'll be
*  pretty dangerous.
*  Yeah. Well, I mean, uh,
*  so this is a good place to kind of think about numera data today,
*  uh, numera signals and what that looks like in 10, 20, 30, 50,
*  a hundred years, you know, like right now, I guess maybe you can correct me,
*  but this, the data that we're working with is like a window. It's a, you know,
*  anonymized, obfuscated window into a particular aspect,
*  uh, time period of the market. And, you know,
*  you can expand that more and more and more and more potentially you can imagine
*  in different dimensions to where it encapsulates all the things that,
*  uh, where you could, uh,
*  include kind of human to human communication that was available for like,
*  uh, to buy GameStop, for example, on, on wall street bets.
*  So maybe the step back,
*  can you speak to what is numera I signals and,
*  uh, what are the different data sets that are involved?
*  So with numera signals, um,
*  you're still providing predictions to us. Um,
*  but you can do that from your own data sets.
*  So numera, it's all,
*  you have to model our data to come up with predictions.
*  Numerize signals is whatever data you can find out there.
*  You can turn it into a signal and give it to us.
*  So it's a way for us to import signals on data we don't yet have.
*  And, um, and that's why it's particularly valuable because it's going to be
*  signals.
*  You're only rewarded for signals that are orthogonal to our core signal.
*  So you have to be doing something uncorrelated.
*  And so strange alternative data tends to have that property.
*  There isn't too many other signals that are correlated with, um,
*  with, uh, you know, what's happening on wall street bets.
*  That's not going to be like correlated with the price to earnings ratio, right?
*  Um, and we have some users as of recently, as of like a week ago,
*  there was a user that created, I think he's in India. He created, um,
*  a signal that is scraped from wall street bets. Um,
*  and now we have that signal, uh,
*  as one of our signals in thousands that we use at Numerize.
*  And the structure of the signal is similar.
*  So it's just numbers and time series data.
*  It's the exactly. And it's just like, it's kind of a,
*  you're providing a ranking of stocks. So you just say, give it a one means,
*  you like the stock zero means you don't like the stock and you provide that for
*  5,000 stocks in the world.
*  And they somehow converted the natural language that's in the wall street.
*  Exactly. So there's then they made, they open source this Colab notebook. Uh,
*  you can go and see it and look at it. And so yeah,
*  it's taking that making a sentiment score and then turning it into a rank of
*  sentiment score. Yeah. Uh, like this stock sucks.
*  So the stock is awesome. Uh, and then converting that's, that's fast.
*  Just even looking at that data would be a fascinating. So on the signal side,
*  what's the vision this long term? What do you see that becoming?
*  So we want to manage all the money in the world.
*  That's Numerize mission and to get that we need to have all the
*  data and have all of the talent.
*  Like there's no way for the first principles.
*  If you had really good modeling and really good data that you would lose,
*  right? Um, it's just a question of how much do you need to get,
*  to get really good.
*  So Numerize already has some really nice data that we give out this year.
*  We are 10Xing that.
*  And I actually think we'll 10X the amount of data we have on Numerize every year
*  for at least the next 10 years. Wow.
*  So it's going to get very big. The data we give out and signals
*  is more data.
*  People with any other random data set can turn that into a signal and give it
*  to us.
*  And in some sense that kind of data is the edge cases, the weirdness is the,
*  so you're focused on like the bulk,
*  like the main data and then there's just like weirdness from all over the place
*  that just can enter through this back door.
*  Exactly. And the it's, it's also, um, a little bit shorter term.
*  So the signals are about a seven day time horizon
*  and the on Numerize it's like a 30 day.
*  So it's often for faster situations.
*  You've written about a master plan and you've mentioned, which I love, uh,
*  in a similar sort of style of big self thinking,
*  you would like Numerize to manage all of the world's money.
*  Uh, so how do we get there from,
*  from yesterday to several years from now? Like what's, uh,
*  what is the plan? So
*  do you have already started to allure to it? It's like,
*  get all the data and get it to all the talent humans
*  models. Exactly. I mean, the important thing to note there is what would that
*  mean? Right. And I think the biggest thing it means is like, uh,
*  if there was one hedge fund, um, you would have, uh,
*  not so much talent wasted on all the other hedge funds. Like,
*  it's super weird how the industry works.
*  It's like one hedge fund gets a data source and hires a PhD and another hedge
*  fund has to buy the same data source and hire a PhD.
*  And suddenly a third of American PhDs are working at hedge funds and we're not
*  even on Mars. And like, so in some ways, Numerize,
*  it's all about freeing up people who work at hedge funds to go work for Elon.
*  Yeah. And also the people who are working on Numerize
*  problem,
*  it feels like a lot of the knowledge there is also transferable to other
*  domains.
*  Exactly. It's our top. One of our top users is, uh,
*  he works at NASA jet propulsion lab and he's, he's like, amazing.
*  I went to go visit him there and it's like, he's got like Numerize posters and
*  he's like, it's like, it looks like, you know, the movies, like,
*  it looks like Apollo 11 or whatever. Yeah.
*  The point is he didn't quit his job to join full
*  time.
*  He's working on getting us to Jupiter's moon. That's his mission,
*  the Europa clip emission.
*  Actually literally what you're saying.
*  Literally.
*  We, he's smart enough that we really want his intelligence to reach the stock
*  market because the stock market's a good thing. Hedge funds are a good thing.
*  Our kinds of hedge funds, especially,
*  but we don't want him to quit his job so he can just do Numerize on the weekend.
*  And that's what he does.
*  He just made a model and it just automatically submits to us.
*  And he's like one of our best users.
*  You mentioned briefly that stock markets are good for my sort of
*  outsider perspective. Is there a sense,
*  do you think trading stocks is closer to gambling
*  or is it closer to investing?
*  Sometimes it feels like it's gambling as opposed to betting on
*  companies to succeed.
*  And this is maybe connected to our discussion of shorting in general,
*  but like from your sense, the way you think about it,
*  is it fundamentally still investing?
*  I do think, I mean, it's a good question.
*  I've also seen lately, like people say, this is like speculation.
*  Is there too much speculation in the market? And it's like,
*  but all the trades are speculative. Like all the trades have a horizon.
*  Like people want them to work.
*  So I would say that there's certainly a lot of
*  aspects of gambling math that
*  applies to investing.
*  Like one thing you don't do in gambling is put all your money in one bet.
*  You have bankroll management and it's a key part of it.
*  And small alterations to your bankroll management might be better than
*  improvements to your skill.
*  So there, and then there are things we care about in our fund.
*  Like we want to make a lot of independent bets. We talk about it.
*  Like we want to make a lot of independent bets because that's going to be a
*  higher sharp than if you have a lot of bets that depend on each other,
*  like all in one sector.
*  But yeah, I mean, the point is that you want the prices of the
*  stocks to be reflective of how,
*  of their value.
*  Of the underlying value of the company.
*  Yeah. You shouldn't have there be like a hedge fund that's able to say,
*  well, I've looked at some data and all of this stuff's super mispriced.
*  Like that's super bad for society. If it's, if it looks like that to someone.
*  I guess the underlying question then is, uh,
*  do you see that the market often like drifts away from the underlying value of
*  companies and it becomes a game in itself? Like would these,
*  whatever they're called, like derivatives, like the option, like, you know, um,
*  options and, uh, shorting and all that kind of stuff.
*  It's like layers of game on top of the actual, like what you said,
*  which is like the basic thing that the Wall Street bets was doing,
*  which is like just buying stocks.
*  Yeah.
*  There are a lot of games that people play that are, um,
*  in the derivatives market.
*  And I think a lot of the stuff people dislike when they look at the history of,
*  of what's happened,
*  they hate like credit default swaps or collateralized debt obligations.
*  Like these are the, these are the kind of like enemies of 2008.
*  And then the long-term capital management thing, it was like,
*  it was like that 30 times leverage or something, or something just that no one,
*  like you could just go to, um,
*  a gas station and ask anybody at the gas station,
*  is it a good idea to have 30 times leverage? And they just say no.
*  It's like common sense just like went out the window. So the,
*  yeah, I don't, I don't, I don't respect long-term capital management.
*  Okay.
*  But Numeron doesn't actually use any derivatives unless you call shorting
*  derivative. We just, we do put money into companies. We,
*  and that does help the companies we're investing in. It's just in little ways.
*  We really did buy Tesla and it, and it did, and we, you know,
*  we were not, um, we played some role in, in that's,
*  it's success super small, make no mistake.
*  But still I think that's important.
*  Can I ask you a pothead question, which is, uh,
*  what is money, man?
*  So if we just kind of zoom out and look at,
*  because I'd love to talk to you about cryptocurrency,
*  which perhaps could be the future of money in general,
*  how do you think about money? You said Numerai, the,
*  the vision, the goal is to, to run, to manage the world's money.
*  What is money in your view?
*  I don't have a good answer to that,
*  but it's definitely in my personal life,
*  it's become more and more warped. Um,
*  and you start to care about the real thing,
*  like what's really going on here. Um,
*  Elon has talks about things like this, like what's,
*  what is the company really? It's like,
*  it's a bunch of people who like kind of show up to work together and like,
*  they solve a problem and they might not be a stock out there that, that,
*  that's trading that represents that what they're doing, but it's,
*  it's not the real thing. Um, and being involved in crypto, um,
*  like I was early, I put in crowd sale of, of Ethereum and,
*  and all these other things and different crypto hedge funds and things that I
*  have invested in. And it's like, it's just, it's just kind of like,
*  it feels like how I used to think about money stuff is just,
*  it's just like totally warped. Um, because you, yeah, you kind of,
*  you stop caring about like the,
*  the price and you care about like the product.
*  So, but, but the product,
*  you mean like the different mechanisms that money has exchanged? I mean,
*  money is ultimately a kind of a little, uh, you know,
*  one is the store of wealth, but it's,
*  it's also a mechanism of exchanging wealth, but that like what,
*  what wealth means becomes a totally different thing,
*  especially with the cryptocurrency to where it's almost like these little
*  contracts, these little agreements,
*  these transactions between human beings that represent something that's bigger
*  than just like cash being exchanged at seven or when it feels like,
*  yeah, maybe I'll answer what is finance. Uh, like you,
*  it's what are you doing when you can,
*  when you have the ability to take out a loan,
*  you can bring a whole new future into being with finance.
*  Uh, if you couldn't get a student loan to get a college degree,
*  you couldn't get a college degree. Like if you didn't have the money,
*  but now like weirdly you can get it with and like, yeah,
*  all you have is this like loan, which is like, so now you can bring,
*  you can bring a different future into the world.
*  And that's how I, when I was saying earlier about if you rerun American history,
*  economic history without these, these, these things,
*  like you're not allowed to take out loans.
*  You're not allowed to have, have derivatives, you're not allowed to have money.
*  Um, it would just, it just doesn't really work. And it's a really magic thing.
*  How, how, how much you can do with finance,
*  but kind of bringing the future forward.
*  Finance is empowering. It's a, we sometimes forget this, but yeah,
*  it enables innovation.
*  It enables big risk takers and bold builders that ultimately make this world
*  better. You said you were early in on cryptocurrency.
*  Can you give your high level overview of just your thoughts about the past,
*  present and future of cryptocurrency?
*  Um, yeah. So my friends told me about Bitcoin and I,
*  I was interested in equities a lot and I was like, well,
*  it has no net present value. It has no future cash flows.
*  Bitcoin pays no dividends. Um,
*  so I really couldn't get my head around it and like that this could be valuable.
*  Um, and then I, but I did,
*  so I didn't feel like I was early in cryptocurrency in fact, cause I was like,
*  it was like 2014. It felt like a long time after Bitcoin. Um, and then,
*  but then I, I really liked some of the things that, uh, Ethereum was doing.
*  It seemed like a super visionary thing. Like I was reading something that was, um,
*  that was just going to change the world when I was reading the white paper. Um,
*  and I liked the different constructs you could have inside of Ethereum that you
*  couldn't have on Bitcoin.
*  Like smart contracts and all that.
*  Exactly. Yeah. And even the, they were, yeah, even spoke about different,
*  uh, yeah, different constructions you could have.
*  Yeah. That's the cool dance between Bitcoin and Ethereum of it's in the space of
*  ideas. It feels so young.
*  Like I wonder what cryptocurrencies will look like in the future.
*  Like if Bitcoin or Ethereum 2.0 or some version will stick around or any of
*  those, like who's going to win out or if there's even a concept of winning out at
*  all, is there a cryptocurrency that you're especially
*  find interesting that, uh, technically, financially,
*  philosophically you think is something you keep your eye on.
*  Well, I don't really, I'm not looking to like invest in cryptocurrencies anymore.
*  Um, but I, I, they are, I mean the,
*  they're and many are almost identical. I mean, there's not,
*  there wasn't too much difference, um,
*  between even Ethereum and Bitcoin in some ways, right? Uh,
*  but they are some that I like the privacy ones. I'm always like,
*  I like Zcash for it's like coolness. It's actually, um,
*  it's, it's like a different kind of invention compared to some of the other
*  things.
*  Okay. Can you speak to just briefly to privacy? What,
*  is there some mechanisms of preserving some privacy of the, so I guess everything
*  is public.
*  Yeah. Is that the problem?
*  The yeah, none of the transactions are private. Um, and so,
*  you know, even like I have some of my,
*  I have some numeraire and you can just see it. In fact,
*  you can go to a website and says like,
*  you can go to like ether scan and it'll say like numeraire founder. Uh,
*  and I'm like, how the hell do you guys know this?
*  So they can reverse in your, whatever that's called.
*  Yeah. And so they can see me move it too. They can see me, oh,
*  why is he moving it? Um, so, uh,
*  so, but yeah, Zcash, they also, when you can make private transactions,
*  you can also play different games. Um, and it's unclear.
*  It's like, what's quite cool about Zcash is I wonder what games are being played
*  there. No one will know.
*  Uh, so from a, from a deeply analytical perspective, uh,
*  can you describe why Dogecoin is going to win?
*  Which it surely will. Like it very likely will take over the world.
*  And once we expand out into the universe, we'll take over the universe. Uh,
*  or on a more serious note,
*  like what are your thoughts on the recent success of Dogecoin where you've spoken
*  to sort of the, the meme stocks, the mimetics of the whole thing.
*  It feels like the joke can become the reality.
*  Like the meme, the joke has power in this world.
*  Yeah. Fascinating. Exactly. It's, uh, it's,
*  it's like, why is it correlated with Elon tweeting about it?
*  It's not just the Elon alone tweeting, right? It's like,
*  Elon tweeting and that becomes a catalyst for everybody on the internet,
*  kind of like spreading the joke, right? Exactly. The joke of it. So it's, it's,
*  it's the initial spark of the fire for a Wall Street bets type of situation.
*  Yeah. And that's fascinating because jokes seem to spread faster than other
*  mechanisms. Like funny shit is very effective at, uh,
*  captivating the, uh, like the discourse on the internet.
*  Yeah. And I think you can have, um, like the,
*  I like the one meme like Doge. I haven't heard that name in a long time.
*  Um, like I think back to that meme often. That's like funny.
*  And every time I think back to it,
*  there's a little probability that I might buy some Dogecoin. Right.
*  And so I imagine you should have millions of people who have had all these great
*  jokes told them. And every now and then they reminisce, Oh, that was,
*  that was really funny. And then they're like, let me buy some.
*  Wouldn't that be interesting if like the entirety,
*  if we travel in time like multiple centuries where the entirety is a
*  communication of the human species is like humor,
*  like it's all just jokes.
*  Like we're high on probably some really advanced drugs and we're all just
*  laughing nonstop. It's a weird, like dystopian future of just humor.
*  Elon has made me realize, uh,
*  how like good it feels to just not take shit seriously every once in a while and
*  just relieve like the pressure of the world. At the same time,
*  the reason I don't always like when people finish their sentences with lol,
*  is like that you don't, when you don't take anything seriously,
*  when everything becomes a joke, then it feels like,
*  uh, that way of thinking feels like it will destroy the world.
*  It's like, I often think it like,
*  well memes save the world of destroy because I think both are possible
*  directions.
*  Yeah, I think this is a big problem. I mean, America,
*  I always felt that about America,
*  a lot of people are telling jokes kind of all the time and they're kind of good
*  at it. Um, and you take someone aside and American,
*  you're like, I really want to have a sincere conversation.
*  It's like hard to even keep a straight face because, um,
*  everything is so, there's so much levity. So it's complicated.
*  I like how sincere actually like your Twitter can be. You're like,
*  I am in love with the world.
*  I get so much shit for it. I'm not,
*  I'm never going to stop because I realize like,
*  do you have to be able to sometimes just be real and be positive and just be,
*  uh, say the cliche things,
*  which ultimately those things actually capture some fundamental truths about
*  life. But it's, it's a dance.
*  And I think Elon does a good job of that, uh,
*  from an engineering perspective of being able to joke, but everyone's,
*  you know what I want mostly to pull back and be like, here's real problems,
*  let's solve them and so on. And then be able to jump back to a joke. So it's,
*  uh, it's ultimately, I think, I guess a skill that we, uh,
*  have to learn. I, uh,
*  but I guess your advice is to invest everything, uh,
*  anyone listening owns into Dogecoin. That's what I heard from this.
*  Yeah. No, exactly. Yeah. Our hedge fund is unavailable.
*  Just go straight to Dogecoin.
*  You're running a successful company.
*  It's just interesting because my mind has been in that space of, uh,
*  potentially just being one of the millions of other entrepreneurs. Uh,
*  what's your advice on, uh, how to build a successful startup,
*  how to build a successful company?
*  I think that one thing I do like,
*  and it might be a particular thing about America,
*  but like there is something about like playing,
*  tell people what you really want to happen in the world. Like,
*  don't stop. It's not, it's not going to make it. Um,
*  like if you're asking someone to invest in your company, don't say, I think,
*  uh, maybe one day we might make a million dollars. Um,
*  when you actually believe something else, you actually believe,
*  you're actually more optimistic,
*  but you're toning down your optimism because you want to appear,
*  um, like low risk,
*  but actually it's super high risk if your company becomes mediocre,
*  because no one wants to work in a mediocre company.
*  No one wants to invest in a mediocre company. Um,
*  so you should play the real game. Um,
*  and obviously this doesn't apply to all businesses,
*  but if you play a venture backed startup kind of game, like play for keeps,
*  play to win, go big. Um, and it's very hard to do that.
*  I've always feel like, um, I, yeah,
*  I start, you can start narrowing, narrowing your focus because 10 people are telling
*  you, you know, you got to care about this boring thing that won't matter five
*  years from now and you should push back and do the real play the real game.
*  So be bold. So both, I mean, this is, this is an interesting duality there.
*  So there's the way you speak to other people about like your plans and what you
*  are like privately just in your own mind.
*  And maybe it's connected with what you were saying about. Yeah.
*  Sincerity as well. Like if you,
*  if you appear to be sincerely optimistic about something that's big or crazy,
*  it's putting yourself up to be kind of like ridiculed or something.
*  And so if you say my mission, my mission is to, um, yeah, go to Mars.
*  It's just so bonkers that, uh, it's hard to say.
*  It is. But, uh, uh, one powerful thing,
*  just like you said is if you say it and you believe it,
*  then actually amazing people, uh, come and work with you.
*  Exactly. It's not just skill, but the, the dreams,
*  there's something about optimism that, uh,
*  like that fire that you have when you're optimistic of actually having the hope
*  of building something totally cool, something totally new,
*  that when those people get in a room together, like they can actually do it.
*  Yeah. Uh, yeah, there's, yeah, there's, that's, uh,
*  and also makes life really fun when you're in that room. So all,
*  all of that together, uh, ultimately, I don't know,
*  that's what makes this crazy ride of a startup really look fun.
*  And Elon is an example of a person who succeeded that there's not many other
*  inspiring figures, which is sad. I used to be a Google and there's,
*  um, there's something that happens that sometimes when the company grows bigger
*  and bigger and bigger where that kind of ambition kind of quiets down a little
*  bit. You know,
*  Google had this ambition still does of making the world's information
*  accessible to everyone. And I remember, I don't know, that's beautiful.
*  I, I still love that dream of that, you know,
*  they used to scan books,
*  but just in every way possible make the world's information accessible.
*  Same with Wikipedia. Every time I open up Wikipedia, um,
*  I'm just awe inspired by how awesome humans are, man.
*  And creating this together, I don't know what the meetings are over there,
*  but they, it's just beautiful. Like what they've created is,
*  is incredible. And I'd love to be able to be part of something like that.
*  And you're right for that. You have to be bold.
*  And there's, and strange to me also,
*  I think you're right that there's how many boring companies they are. Right.
*  Something I always talk about, especially in FinTech. It's like,
*  why am I excited about this? This is so lame. Like what is,
*  this isn't even like important, even if you succeed,
*  this is going to be like terrible. This is not good. Um,
*  and it's just strange how people can kind of get fake enthusiastic about like
*  boring ideas when there's so many bigger ideas that, um,
*  yeah, I mean, you read these things like this company raises money.
*  And it's just like, that's a lot of money for the worst idea I've ever heard.
*  Some ideas are really big. So like,
*  I worked on autonomous vehicles quite a bit and there's so many ways in which
*  you can present that idea to yourself, to the team you work with, just, yeah,
*  like to yourself when you're quietly looking in the mirror in the morning,
*  uh, that's really boring or really exciting.
*  Like if you're really ambitious with autonomous vehicles, there,
*  it changes the nature of like human robot interaction is changing the nature of
*  how we move. Forget money, forget all that stuff.
*  It changes like everything about robotics and AI machine learning.
*  It changes everything about manufacturing. I mean,
*  do cars that could transportation is so fundamentally connected to cars.
*  And if that changes,
*  it changing the fabric of society of movies of everything.
*  Uh, and if you go bold and take risks and go be willing to go bankrupt,
*  with your company, uh, as opposed to cautiously, you could,
*  you could really change the world.
*  And it's so sad for me to see all these autonomous companies,
*  Thomas vehicle companies,
*  they're like really more focused about fundraising and kind of like smoke and
*  mirrors are really afraid that the entirety of their marketing is grounded in
*  fear and presenting enough smoke to where they keep raising funds so they can
*  cautiously use technology of a previous decade or previous two decades to kind
*  of test vehicles here and there as opposed to do crazy things and bold and go
*  huge at scale to huge data collection. I mean, um,
*  yeah, so that's just an example. Like the idea can be big,
*  but if you don't allow yourself to take that idea and think really big with it,
*  uh, then you're not going to make anything happen. Yeah,
*  you're absolutely right in that. There's,
*  so you've been connected in your work, uh,
*  with a bunch of amazing people.
*  How much interaction do you have with invest with investors?
*  I get that whole process is an entire mystery to me.
*  Is there some people that just have influence on the trajectory of your thinking
*  completely, or is it just this collective energy that they behind the company?
*  Yeah. I mean, I, I came here and I, I,
*  I was amazed how, yeah, people would,
*  I was only here for a few months and I met some incredible investors, uh,
*  and I almost run out of money. And, uh,
*  once they invested, I was like, I am not going to let you down.
*  And I was like, okay, I'm gonna send them like an email update every like three
*  minutes. And then they don't care at all. So they kind of want to, I don't know,
*  like, so for some, I like it when it's just like,
*  they're always available to talk, but, um,
*  a lot of building a business, especially a high tech business, um,
*  there's little for them to add, right? There's little for them to add on product.
*  There's a lot for them to add on like business development.
*  And if we are doing product research, which is for us,
*  research into the market research into how to make a great hedge fund,
*  and we do that for years,
*  there's not much to tell the investors.
*  So they're basically is like, I believe in you. There's something,
*  I like the cut of your jib. There's something in your idea,
*  in your ambition, in your plans that I like.
*  And it's almost like a pat on the back. I was like, go, go get them kid.
*  Yeah, it is a bit like that. And that's cool. That's a good way to do it.
*  I'm glad they do it that way. Um, like the one in meeting I had,
*  which was like really good with this was meeting Howard Morgan, uh,
*  who's a actually a co-founder of Renaissance technologies in the like
*  1980s and worked with Jim Simons. And, um,
*  he, he, he was in the room and I was meeting some other guy and he was in the room
*  and I was explaining, uh, how quantitative finance works.
*  I was like, so, you know, they use mathematical models. And then he was like,
*  I, yeah, I, I started Renaissance. I know a bit about this.
*  And then I was like, Oh my God. Um, so yeah, but then,
*  and then I think he kind of said, well, yeah, he said, well,
*  cause I was talking, he was working at first round capital as a partner.
*  And they kind of said, they didn't want to invest. Um,
*  and then I wrote a blog post describing the idea and I was like,
*  I really think you guys should invest. And then they ended up,
*  Oh, interesting. You convinced them on that.
*  Cause they're like, we don't really invest in hedge funds. And I was like,
*  you don't see like what I'm doing. This is so a tech company, not a hedge fund.
*  Right? Yeah. And the numera is brilliant. It's when it caught my eye,
*  there's something special there. So I really do hope you succeed in the,
*  obviously it's a risky thing. You're taking on the ambition of it,
*  the size of it, but I do hope you succeed. You mentioned Jim Simons. Um,
*  he comes up in another world of mine really often on the,
*  he's just a brilliant guy, uh, on the mathematics side as a mathematician,
*  but he's also brilliant finance hedge fund manager guy.
*  Um, have you gotten a chance to interact with him at all?
*  Have you learned anything from him on the math, on the finance,
*  on the philosophy life side things?
*  Um, I've played poker with him. It was pretty cool. It was like, um,
*  actually in the show billions,
*  they kind of do a little thing about this poker tournament thing with all the
*  hedge fund managers and that's real life thing. Um,
*  and they have a lot of like world series of bracelet,
*  what's there's poker bracelets holders, but it's kind of Jim's thing. Um,
*  and um, I met him there and uh, yeah, it was kind of brief,
*  but I was just like, he's like, oh, how do you, why are you here?
*  And I was like, oh, Howard sent me, you know, he's like, go,
*  go play this tournament, meet some of the other players. And then, um,
*  was it Texas Hold'em? Yeah, Texas Hold'em tournament. Yeah.
*  Do you play poker yourself or was it? Yeah, I do. I mean, it was crazy.
*  And the on my right was the CEO who's the current CEO of
*  Renaissance, Peter Brown, um, and Peter Mueller,
*  who's a hedge fund manager at PDT. Uh, and yeah,
*  I mean it was just like, and then, you know, just everyone,
*  and then all these brace world series, like people I know from like TV, um,
*  and Robert Mercer, who's fucking crazy. Uh,
*  he's that he's the guy who, who, who donated the most money to Trump.
*  Um, and he's just like, it's a lot of personality character. Yeah.
*  Jeez. That's crazy. Um, so it's quite cool how, yeah,
*  like the, it was really fun. And then, um,
*  I managed to knock out Peter Mueller. I have a, uh,
*  I got a little trophy for knocking him out because he was a previous champion.
*  In fact, I think he's won the most. I think he's won three times. Super smart guy.
*  Um, but, uh, but,
*  but I will say Jim outlasted me in the tournament. Um,
*  and they're all extremely good at poker. Yeah. Um, but they're also,
*  so it was a $10,000 buy-in. Um, and I was like,
*  this is kind of expensive, uh, but it all goes to charity,
*  Jim's math charity. But then the way they play,
*  they have like rebuy's and like, they all do a shit ton of rebuy's.
*  Yeah. So, um, immediately they're like going all in and I'm like,
*  man, like, so I ended up, you know, adding more as well. Uh,
*  so the state, it's like, you couldn't play at all without doing math.
*  Yeah. The stakes are high. So, but you're,
*  you're connected to a lot of these folks. They're kind of Titans of just,
*  uh, uh, of economics and tech in general.
*  Do you feel a burden from this? You're a young guy.
*  I did feel a bit out of a place there. Like, um,
*  the company was quite new and, um,
*  they also don't speak about things, right? So it's not,
*  not like going to meet in a famous rocket engineer who will tell you how to make
*  a rocket. They do not want to tell you anything about how to make a hedge fund.
*  It's like all secretive and that part I didn't like. Um,
*  and they were also kind of making fun of me a little bit. Like they would say,
*  uh, like they'd call me like, I don't know, the Bitcoin kid or,
*  um, and then they would say even things like, uh, member Peter, yeah,
*  said to me something like,
*  I don't think AI is going to have a big role in finance. Um,
*  and I was like hearing this from the CEO of Renaissance was like weird to hear
*  because I was like, of course it will. And he's like, but, but he can see,
*  he's like, I can see it having a really big impact on things like self-driving
*  cars, but finance it's too noisy and whatever.
*  And so I don't think it's like the perfect application. And I was like,
*  that was interesting to hear. Cause it's like,
*  and that I think it was that same day that, um, Libra,
*  I think it is the poker playing AI started to beat like the human.
*  So it was kind of funny hearing them like say, Oh,
*  I'm not sure I could ever get attack that problem.
*  And then that very day it's attacking the problem of the game we're playing.
*  Well, there's a kind of a magic magic to, um,
*  somebody who's exceptionally successful.
*  Looking at you, giving you respect,
*  but also saying that what you're doing is not going to succeed in a sense.
*  Like they're not really saying it,
*  but I tend to believe from my interactions with people that it's a kind of prod
*  to say, like prove me wrong. Yeah. That's ultimately, that's,
*  that's how those guys talk. They, they see good talent and they're like,
*  yeah.
*  And I think they also saying it's not going to succeed quickly in some way.
*  They're like, this is going to take a long time. Um, and maybe,
*  maybe that's good to know.
*  And certainly AI in, in trading,
*  that's one of the most, uh,
*  philosophically interesting questions about artificial intelligence and the
*  nature of money,
*  because it's like how much can you extract in terms of patterns from all of
*  these millions of humans interacting using this methodology of money?
*  It's like one of the open questions in the artificial intelligence.
*  In that sense,
*  you converting into a data set is one of like the biggest gifts to, uh,
*  the research community, to the whole, anyone who loves data science and AI,
*  this is, uh, this is kind of fascinating.
*  And I'd love to see where this goes.
*  Actually thing I say sometimes long before AGI destroys the world,
*  a narrow intelligence will win all the money in the stock market.
*  Like way, like just a narrow AI.
*  And I want to, I don't know if I'm going to be the one who invents that.
*  So I'm building Numeri to make sure that that narrow AI, you know,
*  uses our data.
*  So you're giving a platform to where millions of people can participate and,
*  uh, do build that narrow AI themselves.
*  People love it when I ask this kind of question about books, about, uh,
*  ideas and philosophers and so on.
*  I was wondering if you had books or
*  ideas, philosophers,
*  thinkers that had an influence on your life when you were growing up or just,
*  uh, today that you would recommend that people check out blog posts, uh,
*  podcasts, videos, all that kind of stuff.
*  Is there something that just kind of had an impact on you that you can't
*  recommend?
*  Uh, super kind of obvious one.
*  That, um, I really want,
*  I was reading zero to one while coming up with Numeri. It was like,
*  I was like halfway through the book. Um,
*  and I really do like a lot of the ideas there and it's,
*  it's also about kind of thinking big and, um, uh,
*  and also it's like peculiar little book. It's like, why?
*  Like there's a little picture of the hipster versus Unabomber and it's,
*  it's a weird little book. So I like, there's kind of like some depth there.
*  It turns a whole book on a, if you're thinking of doing a startup,
*  that's a good book.
*  A book I like a lot is, um,
*  maybe my favorite book is David Deutsch's beginning of infinity.
*  Um, I just found that so optimistic.
*  It puts you, everything you read in science,
*  it like makes the world feel like kind of colder cause like, it's like, you know,
*  we're just,
*  just coming from evolution and, uh, coming from nothing,
*  have nothing should be this way or whatever. And humans are not very powerful.
*  We're just like scum on the earth.
*  And the way David Deutsch sees things and argues that he argues them with the
*  same rigor that the cynics often use and then has a much better conclusion.
*  Um, that's, uh, you know, it's some of the statements of things like, you know,
*  anything that doesn't violate the laws of physics, um,
*  can be solved. Like,
*  so ultimately arriving in a hopeful, uh, like a hopeful,
*  without being like, um, a hippie.
*  You mentioned kind of advice for startups. Is there in general,
*  whether you do a startup or not, do you have advice for young people today?
*  You're like an example of somebody who's paved their own path and were,
*  I would say exceptionally successful. Is there advice,
*  somebody who was like 20 today, 18 undergrad or thinking about going to
*  college or in college and so on, um, that you would give them?
*  I think, uh, I often tell young people, don't start companies. Is it not,
*  don't start a company unless you're prepared to make it your life's work.
*  Like that's a really good way of, of, of putting it. And a lot of people think,
*  well, you know, um, this semester I'm going to take a semester off.
*  And in that one semester I'm going to start a company and sell it or whatever.
*  And it's just like, what are you talking about?
*  It doesn't really work that way. You should be like super into the idea.
*  So into it that you want to spend a really long time on it. Um,
*  is that more about psychology or actual time allocation? Like,
*  is it literally the fact that you need to give a hundred percent for potentially
*  years for it to succeed or is it more about just the mindset that that's
*  required? Yeah. I mean, I think, well, any, I think, yeah, you don't want to have,
*  certainly don't want to have a plan to sell the company, um,
*  like quickly or something. What's like,
*  or it's like a company that has a very, it's like a big fashion component.
*  Like it'll only work now. It's like an app for something. Um,
*  so yeah, I, that's, that's a big one. And then I also think
*  something I thought about recently is I had a job as a quant at a fund,
*  uh, for about two and a half years.
*  And part of me thinks if I had spent another two years there,
*  I would have learned a lot more, um,
*  and had even more knowledge to, to be where new,
*  to basically accelerate how long Numerai took.
*  So the idea that you can sit in an air conditioned room and get free
*  food or even sit at home now in your underwear and make a huge amount of money
*  and learn whatever you want and get, it's just crazy.
*  It's such a good deal.
*  Yeah. Oh, that's interesting. That's the case for,
*  I was terrified of that. Like a Google,
*  I thought I would become really comfortable in that air conditioned room.
*  And that I was afraid the quant situation is, is, I mean,
*  what you presented is really brilliant that it's exceptionally valuable.
*  The lessons you learn, cause you get to,
*  you get to get paid while you learn from others. If you see that,
*  if you see jobs in,
*  in the space of your passion that way, that it's just an education.
*  It's like the best kind of education. But of course you have,
*  from my perspective, you have to be really careful on that to get comfortable.
*  I get in a relationship, then you buy a house or whatever the hell it is.
*  And then you get, you know, and then you convince yourself like, well,
*  I have to pay these fees for the car, for the house, blah, blah, blah.
*  And then, and there's momentum.
*  And all of a sudden you're in your deathbed and there's grandchildren and you
*  drink your whiskey and complaining about kids these days. So I, you know, that,
*  I'm afraid of that momentum, but you're right.
*  Like there's something special about the education you get working at these
*  companies.
*  Yeah. And I, I remember on my desk,
*  I had the like a bunch of papers on quant finance,
*  a bunch of papers on optimization and then the paper on Ethereum just on my
*  desk as well. And the white paper. And it's like,
*  it's amazing how much, how kind of, and you can learn about.
*  So that I also thought,
*  I think this like idea of like learning about intersections of things.
*  I don't think that too many people that know like as much about crypto and
*  quant finance and machine learning as I do.
*  And that's a really nice set of three things to know stuff about.
*  And that was because I had like free time in my job.
*  Okay. Let me ask the perfectly impractical,
*  but the most important question, what's the meaning of all the things you're
*  trying to do so many amazing things? Why?
*  What's the meaning of this life of yours or ours?
*  I don't know.
*  Yeah. So I have yet had some people say,
*  asking what meaning of life is, is like asking the wrong question or something.
*  The question is wrong.
*  Yeah. No, usually people get too nervous to be able to say that.
*  Cause it's like, your question sucks. I don't think there's an answer.
*  It's like the searching for it is like sometimes asking it.
*  It's like sometimes sitting back and looking up at the stars and being like,
*  I wonder if there's aliens up there. There's, there's a useful,
*  like a palette cleanser aspect to it.
*  Cause it kind of wakes you up to like all the little busy,
*  like hurried day to day activities, all the meetings,
*  all the things you'd like a part of.
*  We're just like ants a part of a system, a part of another system. And,
*  and then when this asking this bigger question allows you to kind of zoom out
*  and think about it, but there's ultimately,
*  I think it's an impossible thing for a limited capacity,
*  like cognitive capacity to capture.
*  But it's fun to listen to somebody who's exceptionally successful,
*  exceptionally busy now, who's also young like you,
*  to ask these kinds of questions about like, uh, death, you know,
*  do you consider your own mortality kind of thing and life,
*  whether that enters your mind, because it often doesn't, it gets,
*  it kind of almost gets in the way.
*  Yeah. It's amazing how many things you can like that are trivial that could like
*  occupy a lot of your mind until something,
*  until something bad happens or something flips you.
*  And then you start thinking about the people you love that are in your life.
*  And you started thinking about like, holy shit, this ride ends.
*  Exactly. Yeah. I, I, I just had COVID.
*  And I had a quite bad, it wasn't, what wasn't really bad is just like,
*  I also got a simultaneous like lung infection.
*  So I had like almost like bronchitis or whatever. I don't even,
*  I don't understand that stuff, but it felt, I started,
*  and then you're forced to be isolated. Right.
*  And so it's actually kind of nice it, because it's very mo,
*  it's very depressing. And then I've heard stories of,
*  I think it's Sean Parker. He had like all these diseases as a child.
*  And he had to like, just stay in bed for years. And then he like made Napster.
*  It's like pretty cool. Um, so yeah,
*  I had about 15 days of this recently just last month.
*  And it feels like it did shock me into, um,
*  a new kind of, uh, energy and ambition.
*  Were there moments when you were just like terrified at the combination of
*  loneliness and like, you know,
*  the thing about COVID is like there's some degree of uncertainty. Uh, like,
*  it feels like it's a new thing, a new monster that's arrived on this earth.
*  And so, you know, dealing with it alone, a lot of people are dying.
*  It's like wondering like,
*  Yeah, you do wonder. I mean, for sure. And then these, there are even, um,
*  new strains in South Africa, which is where I was.
*  And maybe I, maybe the new strain had some interaction with my genes and I'm
*  just going to die.
*  But ultimately it was liberating.
*  I loved it. Oh, I loved, I loved that I got out of it.
*  Cause it's also affects your mind. You get,
*  you get confusion and kind of a lot of fatigue and you can't do
*  your usual tricks of psyching yourself out of it. So, you know,
*  sometimes it's like, Oh man, I feel tired. Okay,
*  I'm just going to go have coffee and then I'll be fine. It's like, now it's like,
*  I feel tired cough.
*  I don't even want to get out of bed to get coffee cause I feel so tired.
*  And then you have to confront, uh, there's no like quick fix cure.
*  And you're trapped at home.
*  But that, so now you have this little thing that happened to you.
*  That was a reminder that you're mortal and you get to carry that flag in,
*  in, uh, in, in trying to create something special in this world, right?
*  With Numeri. Listen, uh,
*  this was like one of my favorite conversation cause you were, you're,
*  the way you think about this world of money and just this world in
*  general is so clear and you're able to, uh, explain it so eloquently.
*  Richard has really fun. Really appreciate you talking to him.
*  Thank you. Thank you.
*  Thanks for listening to this conversation with Richard Craig and thank you to
*  our sponsors, audible audio books, trial labs,
*  machine learning company,
*  Blinkist app that summarizes books and athletic greens,
*  all in one nutrition drink,
*  click the sponsor links to get a discount and to support this podcast.
*  And now let me leave you with some words from Warren Buffett.
*  Games are won by players who focus on the playing field,
*  not by those whose eyes are glued to the scoreboard.
*  Thank you for listening and hope to see you next time.

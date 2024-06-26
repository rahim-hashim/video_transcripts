---
Date Generated: April 09, 2024
Transcription Model: whisper medium 20231117
Length: 8961s
Video Keywords: ['agi', 'ai', 'ai podcast', 'alphago', 'artificial intelligence', 'artificial intelligence podcast', 'chess', 'diplomacy', 'game', 'learning', 'lex ai', 'lex fridman', 'lex jre', 'lex mit', 'lex podcast', 'machine', 'mit ai', 'noam brown', 'poker', 'programming']
Video Views: 442069
Video Rating: None
---

# Noam Brown: AI vs Humans in Poker and Games of Strategic Negotiation | Lex Fridman Podcast #344
**Lex Fridman:** [December 06, 2022](https://www.youtube.com/watch?v=2oHH4aClJQs)
*  A lot of people were saying like, oh, this whole idea of game theory, it's just nonsense.
*  And if you really want to make money, you got to like look into the other person's eyes and read their soul and figure out what cards they have.
*  But what happened was where we played our bot against four top heads up, no limit hold them poker players.
*  And the bot wasn't trying to adapt to them. It wasn't trying to exploit them.
*  It wasn't trying to do these mind games. It was just trying to approximate the Nash equilibrium and it crushed them.
*  The following is a conversation with no brown research scientist at Fair Facebook, a research group at Meta AI.
*  He co-created the first AI system that achieved superhuman level performance in no limit Texas hold them both heads up and multiplayer.
*  And now recently, he co-created an AI system that can strategically out negotiate humans using natural language in a popular board game called diplomacy,
*  which is a war game that emphasizes negotiation.
*  This is a Lex Friedman podcast to support it.
*  Please check out our sponsors in the description.
*  And now, dear friends, here's no brown.
*  You've been a lead on three amazing AI projects.
*  So we've got Lebron that solved or at least achieved human level performance on no limit Texas hold them poker with two players heads up.
*  You got Pluribus that solved no limit Texas hold them poker with six players.
*  And just now you have Cicero.
*  These are all names of systems that solved or achieved human level performance on the game of diplomacy, which for people who don't know is a popular strategy board game.
*  It was loved by JFK, John F. Kennedy and Henry Kissinger and many other big famous people in the decades since.
*  So let's talk about poker and diplomacy today.
*  First poker. What is the game of no limit Texas hold them?
*  And how is it different from chess?
*  Well, no limit Texas hold them poker is the most popular variant of poker in the world.
*  So, you know, you go to a casino, you play sit down at the poker table.
*  The game that you're playing is no limit Texas hold them.
*  If you watch movies about poker like Casino Royale or Rounders, the game that they're playing is no limit Texas hold them poker.
*  Now, it's very different from limit hold them in that you can bet any amount of chips that you want.
*  And so the stakes escalate really quickly.
*  You start out with like one or two dollars in the pot.
*  And then by the end of the hand, you've got like a thousand dollars in there, maybe.
*  So the option to increase the number very aggressively and very quickly is always there.
*  Right. The no limit aspect is there's no limits to how much you can bet.
*  You know, you in limit hold them.
*  There's like two dollars in the pot.
*  You can only bet like two dollars.
*  But if you got ten thousand dollars in front of you, you're always welcome to put ten thousand dollars into the pot.
*  So I've got a chance to hang out with Phil Helmuth, who plays all these different variants of poker.
*  And correct me if I'm wrong, but it seems like no limit rewards crazy versus the other ones rewards more kind of calculated strategy or no,
*  because you're sort of looking from an from an analytic perspective.
*  Is is strategy also rewarded in no limit Texas Hold'em?
*  I think both variants reward strategy.
*  But I think what's different about no limit hold'em is it's it's much easier to get jumpy.
*  You know, you go in there thinking you're going to lose you're going to play for like a hundred dollars or something.
*  And suddenly there's like, you know, a thousand dollars in the pot.
*  A lot of people can't handle that.
*  Can you define jumpy?
*  When you're playing poker, you always want to choose the action that's going to maximize your expected value.
*  It's kind of like kind of like with investing, right?
*  Like if you're ever in a situation where you're the amount of money that's at stake is is going to have a material impact on your life, then you're going to play in a more risk averse style.
*  You know, if somebody makes a huge bet, you're going to if you're playing no limit hold'em and somebody makes a huge bet, there might come a point where you're like, this is too much money for me to handle.
*  Like I can't risk this amount.
*  And that's what throws a lot of people off.
*  So that's the big difference, I think, between no limit and limit.
*  What about on the action side when you're actually making that big bet?
*  That's what I mean by crazy.
*  I was trying to refer to the technical, the technical term of crazy, meaning use the big jump in the bet to completely throw off the other person in terms of their ability to reason optimally.
*  I think that's right.
*  I think one of the key strategies in poker is to put the other person into an uncomfortable position.
*  And if you're doing that, then you're playing poker well.
*  And there's a lot of opportunities to do that in no limit hold'em.
*  You know, you can have like $50 in there, you throw in a $1000 bet.
*  And you know, that's sometimes if you do it right, it puts the other person in a really tough spot.
*  Now, it's also possible that you make huge mistakes that way.
*  And so it's really easy to lose a lot of money in no limit hold'em if you don't know what you're doing.
*  But there's a lot of upside potential too.
*  So when you build systems, AI systems that play these games, we'll talk about poker, we'll talk about diplomacy.
*  Are you are you drawn in in part by the beauty of the game itself, AI aside?
*  Or is it to you primarily a fascinating problem set for the AI to solve?
*  I'm drawn in by the beauty of the game.
*  When I, I started playing poker when I was in high school.
*  And the idea to me that there is a correct, an objectively correct way of playing poker.
*  And if you could figure out what that is, then you're, you know, you're making unlimited money, basically.
*  That's like a really fascinating concept to me.
*  And so I was fascinated by the strategy of poker, even when I was like 16 years old.
*  It wasn't until much later that I actually worked on poker AIs.
*  So there was a sense that you can solve poker, like in the way you can solve challenges.
*  Like in the way you can solve chess, for example, or checkers.
*  I believe checkers got solved, right?
*  Yeah, checkers, checkers are completely solved.
*  Optimal strategy.
*  It's impossible to beat the AI.
*  Yeah.
*  And so in that same way, you could technically solve chess.
*  You could solve chess, you could solve poker.
*  You could solve poker.
*  So this is, this gets into the concept of a Nash equilibrium.
*  So it is a Nash equilibrium.
*  Okay.
*  So in any finite two-player zero-sum game, there is an optimal strategy that if you play it, you are guaranteed to not lose an expectation no matter what your opponent does.
*  And this is kind of a radical concept to a lot of people, but it's true in chess.
*  It's true in poker.
*  It's true in any finite two-player zero-sum game.
*  And to give some intuition for this, you can think of rock, paper, scissors.
*  In rock, paper, scissors, if you randomly choose between throwing rock, paper and scissors with equal probability,
*  then no matter what your opponent does, you are not going to lose an expectation.
*  You're not going to lose an expectation in the long run.
*  Now, the same is true for poker.
*  There exists some strategy, some really complicated strategy, that if you play that, you are guaranteed to not lose money in the long run.
*  And I should say this is for two-player poker.
*  Six-player poker is a different story.
*  Yeah.
*  It's a beautiful giant mess.
*  When you say in expectation, you're guaranteed not to lose in expectation.
*  What does in expectation mean?
*  Poker is a very high variance game.
*  So you're going to have hands where you win.
*  You're going to have hands where you lose.
*  Even if you're playing the perfect strategy, you can't guarantee you're going to win every single hand.
*  But if you play for long enough, then you are guaranteed to at least break even and in practice, probably win.
*  So that's in expectation.
*  The size of your stack, generally speaking.
*  Now, that doesn't include anything about the fact that you can go broke.
*  It doesn't include any of those kinds of normal real-world limitations.
*  You're talking in a theoretical world.
*  What about the zero-sum aspect?
*  How big of a constraint is that?
*  How big of a constraint is finite?
*  So finite is not a huge constraint.
*  So I mean, most games that you play are finite in size.
*  It's also true, actually, that there exists this perfect strategy in many infinite games as well.
*  Technically, the game has to be compact.
*  There are some edge cases where you don't have a Nash equilibrium in a two-player zero-sum game.
*  So you can think of a game where you're like, if we're playing a game where whoever names the bigger number is the winner.
*  There's no Nash equilibrium to that game.
*  17.
*  18.
*  You win again.
*  You're good at this.
*  I played a lot of games.
*  OK.
*  So that's the zero-sum aspect.
*  The zero-sum aspect.
*  So there exists a Nash equilibrium in non two-player zero-sum games as well.
*  And by the way, just to clarify what I mean by two-player zero-sum, I mean, there's two players and whatever one player wins, the other player loses.
*  So if we're playing poker and I win $50, that means that you're losing $50.
*  Now, outside of two-player zero-sum games, there still exists Nash equilibria, but they're not as meaningful because you can think of a game like Risk.
*  If everybody else on the board decides to team up against you and take you out, there's no perfect strategy you can play that's going to guarantee that you win there.
*  There's just nothing you can do.
*  So outside of two-player zero-sum games, there's no guarantee that you're going to win by playing a Nash equilibrium.
*  Have you ever tried to model in the other aspects of the game, which is like the pleasure you draw from playing the game?
*  And then if you're a professional poker player, if you're exciting, even if you lose the money you would get from the attention you get to the sponsor and all that kind of stuff, is that that would be a fun thing to model in?
*  Or does that make it super complex to include the human factor in its full complexity?
*  I think you bring up a couple of good points there.
*  So I think a lot of professional poker players, they get a huge amount of money, not from actually playing poker, but from the sponsorships and having a personality that people want to tune in and watch.
*  That's a big way to make an name for yourself in poker.
*  I just wonder from an AI perspective, if you create, and we'll talk about this more, maybe an AI system that also talks trash and all that kind of stuff, that that becomes part of the function to maximize.
*  So it's not just optimal poker play.
*  Maybe sometimes you want to be chaotic.
*  Maybe sometimes you want to be suboptimal and you lose the chaos.
*  And maybe sometimes you want to be overly aggressive because the audience loves that.
*  That'd be fascinating.
*  I think what you're getting at here is that there's a difference between making an AI that wins a game and an AI that's fun to play with.
*  Yeah. Or fun to watch.
*  So those are all different things. Fun to play with and fun to watch.
*  Yeah. And I think I've heard talks from game designers and they say people that work on AI for actual recreational games that people play, and they say, yeah, there's a big difference between trying to make an AI that actually wins.
*  And you look at a game like Civilization, the way that the AIs play is not optimal for trying to win.
*  They're playing a different game.
*  They're trying to have personalities.
*  They're trying to be fun and engaging.
*  And that makes for a better game.
*  And we also talk about NPCs.
*  I just talked to Todd Howard, who was the creator of Fallout and the Elder Scrolls series and Starfield, the new game coming out.
*  And the creator, what I think is the greatest game of all time, which is Skyrim.
*  And the NPCs there, the AI that governs that whole game is very interesting, but the NPCs also are super interesting.
*  And considering what language models might do to NPCs in an open world RPG role playing game is super exciting.
*  Yeah, honestly, I think this is one of the first applications where we're going to see real consumer interaction with large language models.
*  I guess Elder Scrolls 6 is in development now.
*  They're probably pretty close to finishing it.
*  But I would not be surprised at all if Elder Scrolls 7 was using large language models for their NPCs.
*  No, they're not. I mean, I'm not saying anything.
*  I'm not saying anything.
*  This is me speculating, not you.
*  No, but they're just releasing the Starfield game.
*  They do one game at a time.
*  And so whatever it is, whenever the date is, I don't know what the date is.
*  Calm down.
*  But it would be, I don't know, like 2024, 2025, 2026.
*  So it's actually very possible that would include language models.
*  I was listening to this talk by a gaming executive when I was in grad school.
*  And one of the questions that a person in the audience asked is, why are all these games so focused on fighting and killing?
*  And the person responded that it's just so much harder to make an AI that can talk with you and cooperate with you than it is to make an AI that can fight you.
*  And I think once this technology develops further and you can have you can reach a point where not every single line of dialogue has to be scripted, it unlocks a lot of potential for new kinds of games, like much more positive interactions that are not so focused on fighting.
*  And I'm really looking forward to that.
*  It might not be positive. It might be just drama.
*  So you'll be in a Call of Duty game.
*  And instead of doing the shooting, you'll just be hanging out and arguing with an AI about passive aggressive.
*  And then you won't be able to sleep that night.
*  You have to return and continue the argument that you were emotionally hurt.
*  I mean, yeah, I think that's actually an exciting world.
*  Whatever whatever is the drama, the chaos that we love, the push and pull of human connection, I think it's possible to do that in the video game world.
*  And I think you could be messier and make more mistakes in a video game world, which is why it would be a nice place.
*  And also, it doesn't have a deep of a as deep of a real psychological impact, because inside video games, it's kind of understood that you're in not a real world.
*  So whatever crazy stuff AI does, we have some flexibility to play.
*  Just like with the game of diplomacy.
*  It's a game. This is not real geopolitics, not real war.
*  It's a it's a game. So you could you can have a little bit of fun, a little bit of chaos.
*  OK, back to that.
*  Equilibrium. How do we find the Nash equilibrium?
*  All right. So there's different ways to find a Nash equilibrium.
*  So the way that we do it is with this process called self play.
*  Basically, we have this algorithm that starts by playing totally randomly and it learns how to play the game by playing against itself.
*  So it will start playing the game totally randomly.
*  And then if it's playing poker, it'll eventually get to the end of the end of the game and make fifty dollars.
*  And then it will review all the decisions that it made along the way and say, what would have happened if I had chosen this other action instead?
*  If I had raised here instead of called, what would the other player have done?
*  And because it's playing against a copy of itself, it's able to do that counterfactual reasoning.
*  So they can say, OK, well, if I took this action and the other person takes this action and then I take this action and eventually I make one hundred fifty dollars instead of fifty.
*  And so it updates the regret value for that action.
*  Regret is basically like how much does it regret having not played that action in the past?
*  And when it encounters that same situation again, it's going to pick actions that have higher regret with higher probability.
*  Now. It'll just keep simulating the games this way.
*  It'll keep accumulating regrets for different situations.
*  And in the long run, if you pick actions that have higher regret with higher probability in the correct way, it's proven to converge to a Nash equilibrium.
*  Even for super complex games, even for imperfect information games?
*  It's true for all games. It's true for chess. It's true for poker.
*  It's particularly useful for poker.
*  So this is the method of counterfactual regret minimization?
*  This is counterfactual regret minimization.
*  That doesn't have to do with self play. It has to do with just any.
*  If you follow this kind of process, self play or not, you will be able to arrive at an optimal set of actions.
*  So this counterfactual regret minimization is a kind of self play.
*  It's a principled kind of self play that's proven to converge to Nash equilibria, even in imperfect information games.
*  Now you can have other forms of self play and people use other forms of self play for perfect information games where you have more flexibility.
*  The algorithm doesn't have to be as theoretically sound in order to converge to that class of games because it's a simpler setting.
*  Sure. So in my brain, the word self play has mapped to neural networks, but we're speaking something bigger than just neural networks.
*  It could be anything. The self playing mechanism is just the mechanism of a system playing itself.
*  Exactly. Yeah. Self play is not tied specifically to neural nets.
*  It's a kind of reinforcement learning, basically.
*  And I would also say this process of trying to reason, oh, what would the value have been if I had taken this other action instead?
*  This is very similar to how humans learn to play a game like poker.
*  Right? Like you probably played poker before and with your friends, you probably ask, oh, would you have called me if I raised there?
*  And that's a person trying to do the same kind of learning from a counterfactual that the AI is doing.
*  OK. And if you do that at scale, you're going to be able to learn an optimal policy.
*  Yeah. Now, where the neural nets come in, I said, OK, if it's in that situation again, then it will choose the action that has high regret.
*  Now, the problem is that poker is such a huge game.
*  You know, I think at No Limits Texas Hold'em, the version that we were playing has 10 to the 161 different decision points, which is more than the number of atoms in the universe squared.
*  That's heads up. That's heads up.
*  Yeah. 10 to the 161, you said?
*  Yeah. I mean, it depends on the number of chips that you have, the stacks and everything.
*  But like the version that we were playing was 10 to the 161.
*  Which I assume would be a somewhat simplified version anyway, because I bet there's some like step function you had for like bets.
*  Oh, no, no, no. That's I'm saying like we played the full game.
*  You can bet whatever amount you want.
*  Now, the bot maybe was constrained in like what it considered for bet sizes, but the person on the other side could bet whatever they wanted.
*  Yeah. I mean, 161 plus or minus 10 doesn't matter.
*  Yeah.
*  And so the way neural nets help out here is, you know, you don't have to run into the same exact situation because that's never going to happen again.
*  The odds of you running into the same exact situation are pretty slim.
*  But if you run into a similar situation, then you can generalize from other states that you've been in that kind of look like that one.
*  And you can say like, well, these other situations, I had high regret for this action.
*  And so maybe I should play that action here as well.
*  Which is the more complex game?
*  Chess or poker or go or poker?
*  Do you know?
*  That is a controversial question.
*  OK.
*  It's like somebody's screaming on Reddit right now.
*  It depends on which subreddit you're on.
*  Is it chess or is it poker?
*  I'm sure like David Silver is going to get really angry at me.
*  Yeah.
*  I'll say I'm going to say poker, actually.
*  And I think for a couple of reasons.
*  They're not here to defend themselves.
*  So first of all, you have the imperfect information aspect.
*  And so it's it we can go into that.
*  But like once you introduce imperfect information, things get much more complicated.
*  So we should say maybe you can describe what is seen to the players, what is not seen in the game of Texas Hold'em.
*  Yeah. So Texas Hold'em, you get two cards face down that only you see.
*  And so that's the hidden information of the game.
*  The other players also all get two cards face down that only they see.
*  And so you have to kind of as you're playing, reason about like, OK, what do they think I have?
*  What do they have? What do they think I think they have?
*  That kind of stuff. And that's that's kind of where bluffing comes into play, right?
*  Because the fact that you can bluff, the fact that you can bet with a bad hand and still win is because they don't know what your cards are.
*  And that's the that's the key difference between a perfect information game like poker, sorry, like chess and go and imperfect information games like poker.
*  This is what trash talk looks like.
*  The implied statement is the game I solved is much tougher.
*  But yeah, so when you're playing, I'm just going to do random questions here.
*  So when you're playing your opponent under imperfect information.
*  Is there some degree to which you're trying to estimate the range of hands that they have?
*  Or is that not part of the algorithm?
*  What are the different approaches to the imperfect information game?
*  So the key thing to understand about why imperfect information makes things difficult is that you have to worry not just about which actions to play, but the probability that you're going to play those actions.
*  So you think about.
*  Rock, paper, scissors, for example, rock, paper, scissors is an imperfect information game.
*  Because you don't know what I'm about to throw.
*  I do, but yeah, usually not.
*  Yeah, yeah. And so you can't just say like, oh, I'm just going to throw a rock every single time because the other person is going to figure that out and notice a pattern.
*  And then suddenly you're going to start losing.
*  And so you don't just have to figure out which action to play.
*  You have to figure out the probability that you play it.
*  And really importantly, the value of an action depends on the probability that you're going to play it.
*  So if you're playing rock every single time, that value is really low.
*  But if you're never playing rock, you play rock like one percent of the time, then suddenly the other person is probably going to be throwing scissors.
*  And when you throw a rock, the value of that action is going to be really high.
*  Now, you take that to poker.
*  What that means is the value of bluffing, for example, if you're the kind of person that never bluffs and you have this reputation as somebody that never bluffs and suddenly you bluff, there's a really good chance that that bluff is going to work and you're going to make a lot of money.
*  On the other hand, if you got a reputation, like if they've seen you play for a long time and they see, oh, you're the kind of person that's bluffing all the time, when you bluff, they're not going to buy it and they're going to call you down.
*  You're going to lose a lot of money.
*  And that finding that balance of how often you should be bluffing is the key challenge of a game of poker.
*  And you contrast that with a game like chess.
*  It doesn't matter if you're opening with the Queen's Gambit 10 percent of the time or 100 percent of the time, the value, the expected value is the same.
*  So that's why we need these algorithms that understand not just we have to figure out what actions are good, but the probabilities.
*  We need to get the exact probabilities correct.
*  And that's actually when we created the bot, Lebratis, Lebratis means balanced because the algorithm that we designed was designed to find that right balance of how often it should play each action.
*  The balance of how often in the key sort of branching is the bluff or not the bluff.
*  Is that a good crude simplification of the major decision in poker?
*  It's a good simplification.
*  I think that's like the main tension.
*  But it's not just how often to bluff or not to bluff.
*  It's like how often should you bet in general?
*  How often should you?
*  What kind of bet should you make?
*  Should you bet big or should you bet small?
*  And with which hands?
*  And so this is where the idea of a range comes from.
*  Because when you're bluffing with a particular hand in a particular spot, you don't want there to be a pattern for the other person to pick up on.
*  You don't want them to figure out, oh, whenever this person is in this spot, they're always bluffing.
*  And so you have to reason about, OK, would I also bet with a good hand in this spot?
*  You want to be unpredictable.
*  So you have to think about what would I do if I had this different set of cards?
*  Is there explicit estimation of a theory of mind that the other person has about you?
*  Or is that just a emergent thing that happens?
*  The way that the bots handle it that are really successful, they have an explicit theory of mind.
*  So they're explicitly reasoning about what's the common knowledge belief?
*  What do you think I have?
*  What do I think you have?
*  What do you think I think you have?
*  It's explicitly reasoning about that.
*  Is there multiple use there?
*  So maybe that's jumping ahead to six players, but is there a stickiness to the person?
*  So it's an iterative game.
*  You're playing the same person.
*  There is there's a stickiness to that, right?
*  You're gathering information as you play.
*  It's not every every every hand is a new hand.
*  Is there a continuation in terms of estimating what kind of player I'm facing here?
*  That's a good question.
*  So you could approach the game that way.
*  The way that the bots do it, they don't end with the way that humans approach it also, expert human players,
*  the way they approach it is to basically assume that you know my strategy.
*  So I'm going to try to pick a strategy where even if I were to play it for ten thousand hands and you could figure out exactly what it was,
*  you still wouldn't be able to beat it.
*  Basically, what that means is I'm trying to approximate the Nash equilibrium.
*  I'm trying to be perfectly balanced because if if I'm playing the Nash equilibrium,
*  even if you know what my strategy is, like I said, I'm still unbeatable in expectation.
*  So so that's what that's what the bot aims for.
*  And that's actually what a lot of expert poker players aim for as well, to start by playing the Nash equilibrium.
*  And then maybe if they spot weaknesses in the way you're playing, then they can deviate a little bit to take advantage of that.
*  They aim to be unbeatable in expectation.
*  OK, so who's the greatest poker player of all time and why is it Phil Hellmuth?
*  So this is for Phil.
*  So he's known.
*  At least in part for maybe playing suboptimally, and he still wins a lot.
*  It's a bit chaotic. So maybe can you speak from an perspective about the genius of his madness or the madness of his genius?
*  So playing suboptimally, playing chaotically.
*  As a way to make you hard to pin down about what your strategy is.
*  So, OK, the thing that I should explain, first of all, with like Nash equilibrium, it doesn't mean that it's predictable.
*  The whole point of it is that you're trying to be unpredictable.
*  Now, I think when somebody like Phil Hellmuth might be really successful is not in being unpredictable, but in being able to take advantage of the other player and figure out where they're being predictable.
*  Or guiding the other player into thinking that you have certain weaknesses and then understanding how they're going to change their behavior.
*  They're going to deviate from a Nash equilibrium style of play to try to take advantage of those perceived weaknesses and then counter exploit them.
*  So you kind of get into the mind games there.
*  So you think about at least has a poker as a dance between two agents.
*  I guess you playing the cards or you playing the player?
*  So this this gets down to a big argument in the poker community and the academic community.
*  For a long time, there was this debate of like what's called GTO, Game Theory Optimal Poker or exploitative play.
*  And up until about like 2017 when we did the Labrador's match, I think actually exploitative play had the advantage.
*  A lot of people were saying like, oh, this whole idea of game theory, it's just nonsense.
*  And if you really want to make money, you got to look into the other person's eyes and read their soul and figure out what cards they have.
*  But what happened was people started adopting the Game Theory Optimal strategy and they were making good money and they weren't trying to adapt so much to the other player.
*  They were just trying to play the Nash equilibrium.
*  And then what really solidified it, I think, was the Labrador's the Labrador's match where we played our bot against four top heads up, no limit hold them poker players.
*  And the bot wasn't trying to adapt to them.
*  It wasn't trying to exploit them. It wasn't trying to do these mind games.
*  It was just trying to approximate the Nash equilibrium and it crushed them.
*  I think, you know, we were playing for $50, $100 blinds.
*  And over the course of about 120,000 hands, it made close to $2 million.
*  120,000 hands. 120,000 hands.
*  Against humans. Yeah. And this was fake money, to be clear.
*  So there was real money at stake. There was $200,000.
*  First of all, all money is fake. But that's a different conversation.
*  We give it meaning.
*  It's a phenomena that gets meaning from our complex psychology as a human civilization.
*  It's emerging from the collective intelligence of the human species.
*  But that's not what you mean. You mean like there's literally you can't buy stuff with it.
*  OK. Can you actually step back and take me through that competition?
*  Yeah. OK. So when I was in grad school, there was this thing called the annual computer poker competition,
*  where every year all the different research labs that were working on AI for poker would get together.
*  They would make a bot. They would play them against each other.
*  And we made a bot that actually won the 2014 competition, the 2016 competition.
*  And so we decided we're going to take this bot, build on it, and play against real top professional, heads up, no limit, Texas Hold'em poker players.
*  So we invited four of the world's best players in this specialty.
*  And we challenged them to one hundred twenty thousand hands of poker over the course of 20 days.
*  And we had two hundred thousand dollars, two hundred thousand dollars in prize money at stake,
*  where it would basically be divided among them depending on how well they did relative to each other.
*  So we wanted to have some incentive for them to play their best.
*  Did you have a confidence 2014, 16 that this is even possible?
*  How much doubt was there?
*  So we did a competition actually in 2015 where we also played against professional poker players
*  and the bot lost by a pretty sizable margin, actually.
*  Now, there were some big improvements from 2015 to 2017.
*  And so can you speak to the improvements?
*  Is it computational nature? Is it the algorithm, the methods?
*  It was it was really an algorithmic approach. That was the difference.
*  So 2015, it was much more focused on trying to come up with a strategy upfront,
*  like trying to solve the entire game of poker and then just have a lookup table where you're saying, like, oh, I'm in this situation.
*  What's the strategy?
*  The approach that we took in 2017 was much more search based.
*  It was trying to say, OK, well, let me in real time try to compute a much better strategy than what I had precomputed by playing against myself during self play.
*  What is the search space for poker?
*  What are you searching over?
*  What's that look like? There's different actions like raising, calling.
*  Yeah, what are the actions?
*  Is it just a search over actions?
*  So in a game like chess, the search is like, OK, I'm in this chess position and I can, like, you know, move these different pieces and see where things end up.
*  In poker, what you're searching over is the actions you can take for your hand, the probabilities that you take those actions,
*  and then also the probabilities that you take other actions with other hands that you might have.
*  And that's kind of like hard to wrap your head around.
*  Like, why are you searching over these other hands that you might have and trying to figure out what you would do with those hands?
*  And the idea is, again, you want to always be balanced and unpredictable.
*  And so if your search algorithm is saying, like, oh, I want to raise with this hand.
*  Well, in order to know whether that's a good action, like, let's say it's a bluff.
*  Let's say you have a bad hand and you're saying, like, oh, I think I should be betting here with this really bad hand and bluffing.
*  Well, that's only a good action if you're also betting with a strong hand.
*  Otherwise, it's an obvious bluff.
*  So if your action in some sense maximizes your unpredictability, so that action could be mapped by your opponent to a lot of different hands, then that's a good action.
*  Basically, what you want to do is put your opponent into a tough spot.
*  So you want them to always have some doubt, like, should I call here?
*  Should I fold here?
*  And if you are raising in the appropriate balance between bluffs and good hands, then you're putting them into that tough spot.
*  And so that's what we're trying to do.
*  We're always trying to search for a strategy that would put the opponent into a difficult position.
*  Can you give a metric that you're trying to maximize or minimize?
*  Does this have to do with the regret thing we're talking about in terms of putting your opponent in a maximally tough spot?
*  Yeah, ultimately, what you're trying to maximize is your expected winning.
*  So your expected value, the amount of money that you're going to walk away from, assuming that your opponent was playing optimally in response.
*  So you're going to assume that your opponent is also playing as well as possible a Nash equilibrium approach, because if they're not, then you're just going to make more money.
*  Like anything that deviates, like by definition, the Nash equilibrium is the strategy that does the best in expectation.
*  And so if you're deviating from that, then they're going to lose money.
*  And since it's a two-player, zero-sum game, that means you're going to make money.
*  So there's not an explicit objective function that maximizes the toughness of the spot they're put in.
*  You're always, this is from a self-play reinforcement learning perspective.
*  You're just trying to maximize winnings.
*  And the rest is implicit.
*  That's right. Yeah.
*  So what we're actually trying to maximize is the expected value, given that the opponent is playing optimally in response to us.
*  Now, in practice, what that ends up looking like is it's putting the opponent into difficult situations where there's no obvious decision to be made.
*  So the system doesn't know anything about the difficulty of the situation?
*  Not at all. It doesn't care.
*  Yeah.
*  All right. In my head, it was getting excited whenever I was making the opponent sweat.
*  OK, so you're in 2015, you didn't do as well.
*  So what's the journey from that to a system that in your mind could have a chance?
*  So 2015, we got beat pretty badly and we actually learned a lot from that competition.
*  And in particular, what became clear to me is that the way the humans were approaching the game was very different from how the bot was approaching the game.
*  The bot would not be doing search.
*  It would just be trying to compute.
*  It would do like months of self-play.
*  It would just be playing against itself for months.
*  But then when it's actually playing the game, it would just act instantly.
*  And the humans, when they're in a tough spot, they would sit there and think for sometimes even like five minutes about whether they're going to call or fold a hand.
*  And it became clear to me that there's a good chance that that's what's missing from our bot.
*  So I actually did some initial experiments to try to figure out how much of a difference this is actually make.
*  And the difference was huge.
*  As a signal to the human player, how long you took to think?
*  No, no, no. I'm not saying that there were any timing tells.
*  I was saying when the human like the bot would always act instantly, it wouldn't try to come up with a better strategy in real time over what it had pre-computed during training.
*  Whereas the human, like they have all this intuition about how to play, but they're also in real time leveraging their ability to think, to search, to plan and coming up with an even better strategy than what their intuition would say.
*  So you're saying that there is you're doing that's what you mean by you're doing search also.
*  You have an you have a intuition and search on top of that looking for a better solution.
*  Yeah, that's that's what I mean by search that instead of acting instantly, you know, a neural net usually gives you a response in like 100 milliseconds or something.
*  It depends on the size of the of the net.
*  But if you can leverage extra computational resources, you can possibly get a much better outcome.
*  And we did some experiments in small scale versions of poker.
*  And what we what we found was that if you.
*  Do a little bit of search, even just a little bit, it was the equivalent of making your, you know, your pre-computed strategy like you can kind of think of it as your neural net a thousand times bigger with just a little bit of search.
*  And it just like blew away all of the research that we had been working on and trying to like scale up this like pre-computed solution.
*  It was dwarfed by the benefit that we got from search.
*  Can you just linger on what you mean by search here?
*  You're searching over a space of actions for your hand and for other hands.
*  How are you selecting the other hands to search over?
*  So, yeah, randomly.
*  No, it's all the other hands that you could have.
*  So when you're playing no limit, Texas hold them.
*  You've got two face down cards.
*  And so that's 52 choose to 1326 different combinations.
*  Now, that's actually a little bit lower because there's face up cards in the middle and so you can eliminate those as well.
*  But you're looking at like around a thousand different possible hands that you can have.
*  And so when we're doing when the bots doing search, it's thinking explicitly there are these thousand different hands that I could have.
*  There are these thousand different hands that you could have.
*  Let me try to figure out what would it be a better strategy than what I've pre-computed for these hands and your hands.
*  OK, so that search, how do you fuse that with what the neural net is telling you or what the train system is telling you?
*  Yeah, so you kind of like where the train system comes in is the value at the end.
*  So there's you only look so far ahead.
*  You look like maybe one round ahead.
*  So if you're on the flop, you're looking to the start of the turn.
*  And at that point, you can use the pre-computed solution to figure out what are what's the value here of like of this strategy?
*  Is it of a single action?
*  Essentially, in that spot, you're getting a value or is it the value of the entire series of actions?
*  Well, it's kind of both because you're trying to maximize the value for the hand that you have.
*  But in the process, in order to maximize the value of the hand that you have, you have to figure out what would I be doing with all these other hands as well?
*  But are you in the search or was going to the end of the game?
*  In Labrador's we did.
*  So we only use search starting on the turn and then we searched all the way to the end of the game.
*  The turn, the river. Can we take it through the terminology?
*  Yeah, there's four rounds of poker.
*  So there's the pre-flop, the flop, the turn and the river.
*  And so we would start doing search halfway through the game.
*  Now, the first half of the game, that was all pre-computed.
*  It would just act instantly.
*  And then when it got to the halfway point, then it would always search to the end of the game.
*  Now, we later improved this so we don't have to search all the way to the end of the game.
*  It would actually search just a few moves ahead.
*  But that came later and that drastically reduced the amount of computational resources that we needed.
*  But the moves, because you can keep betting on top of each other.
*  That's what you mean by moves. So like that's where you don't just get one bet per turn or poker.
*  You can have multiple arbitrary number of bets, right?
*  I'm trying to think like I'm going to bet and then what are you going to do in response?
*  Are you going to raise me? Are you going to call?
*  And then if you raise, what should I do?
*  So it's reasoning about that whole process up until the end of the game in the case of Labratus.
*  So for Labratus, what's the most number of re-raises have you ever seen?
*  You probably cap out at like five or something, because at that point, you're basically all in.
*  I mean, is there like interesting patterns like that that you've seen that the game does?
*  Like you'll have like AlphaZero doing way more sacrifices than humans usually do.
*  Is there something like Labratus was constantly re-raising or something like that that you've noticed?
*  There was something really interesting that we observed with Labratus.
*  So humans, when they're playing poker, they usually size their bets relative to the size of the pot.
*  So if the pot has $100 in there, maybe you bet like $75 or somewhere around there.
*  Somewhere between like $50 and $100.
*  And with Labratus, we gave it the option to basically bet whatever it wanted.
*  It was actually really easy for us to say like, oh, if you want, you can bet like 10 times the pot.
*  And we didn't think it would actually do that.
*  It was just like, why not give it the option?
*  And then during the competition, it actually started doing this.
*  And by the way, this is like a very last minute decision on our part to add this option.
*  And so we did not think the bot would do this.
*  And I was actually kind of worried when it did start to do this.
*  Like, oh, is this a problem?
*  Like humans don't do this.
*  Is it screwing up?
*  But it would put the humans into really difficult spots when it would do that.
*  Because you could imagine you have the second best hand that's possible given the board.
*  And you're thinking like, oh, you're in a really great spot here.
*  And suddenly the bot bets $20,000 into a $1,000 pot.
*  And it's basically saying, I have the best hand or I'm bluffing.
*  And you having the second best hand, now you get a really tough choice to make.
*  And so the humans would sometimes think like five or 10 minutes about like, what do you do?
*  Should I call?
*  Should I fold?
*  And when I saw the humans really struggling with that decision, that's when I realized,
*  oh, actually, this is maybe a good thing to do after all.
*  And of course, the system doesn't know that it's making, again, like we said,
*  that it's putting them in a tough spot.
*  It's just that's part of the optimal, the game theory optimal.
*  Right. From the bot's perspective, it's just doing the thing that's going to make it the most money.
*  And the fact that it's putting the humans in a difficult spot, like that's just a side effect of that.
*  And this was, I think, the one thing, I mean, there were a few things that the humans walked away from,
*  but this was the number one thing that the humans walked away from the competition saying,
*  like, we need to start doing this.
*  And now these over bets, what are called over bets, have become really common in high level poker play.
*  Have you ever talked to somebody like Daniel Negrano about this?
*  He seems to be a student of the game.
*  I did actually have a conversation with Daniel Negrano once.
*  Yeah, I was visiting the Isle of Man to talk to PokerStars about AI.
*  And Daniel Negrano was there when we had dinner together with some other people.
*  And yeah, he was really interested in it.
*  He mentioned that he was excited about learning from these AIs.
*  So he wasn't scared. He was excited.
*  He was excited. And he honestly, he wanted to play against the bot.
*  He thought he had a decent chance of beating it.
*  I think, you know, this was several years ago when I think it was not as clear to everybody that the AIs were taking over.
*  I think now people recognize that if you're playing against a bot, there's no chance that you have in a game like poker.
*  So consistently, the bots will win.
*  The bots have heads up and in other variants too.
*  So six player Texas Hold'em, no limit Texas Hold'em, the bots win.
*  Yeah, that's the case.
*  So I think there is some debate about like, is it true for every single variant of poker?
*  I think for every single variant of poker, if somebody really put in the effort, they can make an AI that would beat all humans at it.
*  We've focused on the most popular variants.
*  So heads up, no limit Texas Hold'em.
*  And then we followed that up with six player poker as well, where we managed to make a bot that beat expert human players.
*  And I think even there now, it's pretty clear that humans don't stand a chance.
*  See, I would love to hook up an AI system that looks at EEG, like how, like actually tries to optimize the toughness of the spot it puts a human in.
*  And I would love to see how different is that from the game theory optimal.
*  So you try to maximize the heart rate of the human player, like the freaking out over a long period of time.
*  I wonder if there's going to be different strategies that emerge that are close in terms of effectiveness.
*  Because something tells me you could still achieve superhuman level performance by just making people sweat.
*  I feel like that there's a good chance that that is the case.
*  Yeah. If you're able to see like that, it's like a decent proxy for score.
*  Right. And this is actually like the common poker wisdom where they're teaching players before there were bots and they were trying to teach people how to play poker.
*  They would say like the key to the game is to put your opponent to difficult spots.
*  It's a good estimate for if you're making the right decision.
*  So what else can you say about the fundamental role of search in poker?
*  And maybe if you can also related to chess and go in these games, what's the role of search to solve in these games?
*  Yeah, I think a lot of people under this is true for the general public, and I think it's true for the community.
*  A lot of people underestimate the importance of search for these kinds of game results.
*  An example of this is TD Gammon that came out in 1992.
*  This was the first real instance of a neural net being used in a game AI.
*  It's a landmark achievement. It was actually the inspiration for AlphaZero.
*  And it used search. It used two ply search to figure out its next move.
*  You got Deep Blue there.
*  It was very heavily focused on search, looking many, many moves ahead, farther than any human could.
*  And that was key for why it won.
*  And then even with something like AlphaGo, AlphaGo is commonly hailed as a landmark achievement for neural nets.
*  And it is. But there's also this huge component of search, Monte Carlo Tree Search, to AlphaGo that was key, absolutely essential for the AI to be able to beat top humans.
*  I think a good example of this is you look at the latest versions of AlphaGo.
*  It was called AlphaZero.
*  And there's this metric called Elo rating, where you can compare different humans and you can compare bots to humans.
*  Now, a top human player is around 3,600 Elo, maybe a little bit higher now.
*  AlphaZero, the strongest version, is around 5,200 Elo.
*  But if you take out the search that's being done at test time, and by the way, what I mean by search is the planning ahead, the thinking of like,
*  Oh, if I move my, if I place this stone here and then he does this, and then you look like five moves ahead and you see what the board state looks like.
*  That's what I mean by search. If you take out the search that's done during the game, the Elo rating drops to around 3,000.
*  So even today, what, seven years after AlphaGo, if you take out the Monte Carlo Tree Search that's being done at one playing against the human, the bots are not superhuman.
*  Nobody has made a raw neural net that is superhuman in Go.
*  That's worth lingering on. That's quite profound.
*  So without search, that just means looking at the next move and saying this is the best move.
*  So having a function that estimates accurately what the best move is without search.
*  Yeah, and all these bots, they have the what's called a policy network where it will tell you this is what the neural net thinks is the next best move.
*  And it's kind of like the intuition that a human has.
*  You know, the human looks at the board and any Go or chess master will be able to tell you like, oh, instantly here's what I think the right move is.
*  And the bot is able to do the same thing.
*  But just like how a human Grandmaster can make a better decision if they have more time to think, when you add on this Monte Carlo Tree Search, the bot is able to make a better decision.
*  Yeah, I mean, of course, a human is doing something like search in their brain, but it's not.
*  I hesitate to draw a hard line, but it's not like Monte Carlo Tree Search.
*  It's more like sequential language model generation.
*  So it's like a different it's a the neural network is doing the searching.
*  And I wonder what the human brain is doing in terms of searching because you're doing that like computation, humanist computing.
*  They have intuition. They've got.
*  They have a really strong ability to estimate, you know, amongst the top players of what is good and not position without calculating all the details.
*  But they're still doing search in their head. But it's a different kind of search.
*  Have you ever thought about like, what is the difference between the human, the search that the human is performing versus what computers are doing?
*  I have thought a lot about that, and I think it's a really important question.
*  So the AI in Alpha and AlphaGo or any of these Go AIs, they're all doing Monte Carlo Tree Search, which is a particular kind of search.
*  And it's actually a symbolic tabular search.
*  It uses the neural net to guide its search, but it isn't actually like full on neural net.
*  Now, that kind of search is very successful in these kinds of like perfect information board games like chess and Go.
*  But if you take it to a game like poker, for example, it doesn't work.
*  It can't understand the concept of hidden information.
*  It doesn't understand the balance that you have to strike between like the amount that you're raising versus the amount that you're calling.
*  And in every one of these games, you see a different kind of search.
*  And the human brain is able to plan for all these different games in a very general way.
*  Now, I think that's one thing that we're missing from AI today.
*  And I think it's a really important missing piece.
*  The ability to plan and reason more generally across a wide variety of different settings.
*  In a way where the general reasoning makes you better at each one of the games, not worse.
*  Yeah, so you can kind of think of it as like neural nets today.
*  They'll give you like transformers, for example, are super general, but they'll give you it'll output an answer in like 100 milliseconds.
*  And if you tell it like, oh, you've got five minutes to give you a decision, feel free to take more time to make a better decision.
*  It's not going to know what to do with that.
*  But a human, if you're playing a game like chess, they're going to give you a very different answer depending on if you say, oh, you've got 100 milliseconds or you've got five minutes.
*  Yeah, I mean, people have started using transformers with language models in an iterative way that does improve the answer or like showing the work kind of idea.
*  Yeah, they got this thing called chain of thought reasoning.
*  And that's I think super promising.
*  Yeah, I think and I think it's a good step in the right direction.
*  I would kind of like say it's similar to Monte Carlo rollouts in a game like chess.
*  There's a kind of search that you can do where you're saying, like, I'm going to roll out my intuition and see, like, without really thinking,
*  what are the better decisions I can make farther down the path?
*  What would I do if I just acted according to intuition for the next 10 moves?
*  And that gets you an improvement.
*  But I think that there's much, much richer kinds of planning that we could do.
*  So when the broadest actually beat the poker players, what did that feel like?
*  What was that? I mean, actually, on that day, what were you feeling like?
*  Were you nervous?
*  I mean, poker was one of the games that you thought like is not going to be solvable because of the human factor.
*  So at least in the narratives we tell ourselves, the human factor is so fundamental to the game of poker.
*  Yeah, the Lebron competition was super stressful for me.
*  Also, I mean, I was working on this, like basically continuously for a year leading up to the competition.
*  I mean, for me, it became like very clear, like, OK, this is the search technique.
*  This is the approach that we need.
*  And then I spent a year working on this pretty much like nonstop.
*  Can we actually get into details like what programming language is it written in?
*  What's some interesting implementation details that are like fun slash painful?
*  Yeah, so one of the interesting things about Lebron is that we had no idea what the bar was to actually beat top humans.
*  We could play against like our prior bots, and that kind of gives us some sense of like, are we making progress?
*  Are we going in the right direction?
*  But we had no idea like what the bar actually was.
*  And so we threw a huge amount of resources at trying to make the strongest bot possible.
*  So we use C++. It was parallelized.
*  We were using, I think, like a thousand CPUs, maybe more actually.
*  And today that sounds like nothing, but for a grad student back in 2016, that was a huge amount of resources.
*  Well, it's still a lot for even any grad student today.
*  It's still tough to get or even to allow yourself to think in terms of scale at CMU, at MIT, anything like that.
*  Yeah, and talking about terabytes of memory.
*  So it was a very parallelized and it had to be very fast, too, because the more games that you could simulate, the stronger the bot would be.
*  So is there some like John Carmack style, like efficiencies you had to come up with,
*  an efficient way to represent the hand, all that kind of stuff?
*  There are all sorts of optimizations that I had to make to try to get this thing to run as fast as possible.
*  They were like, how do you minimize the latency?
*  How do you package things together so that you minimize the amount of communication between the different nodes?
*  How do you optimize the algorithms so that you can try to squeeze out more and more from the game that you're actually playing?
*  All these kinds of different decisions that I had to make.
*  Just a fun question.
*  What ID did you use for C++ at the time?
*  I think I used Visual Studio, actually.
*  OK.
*  Yeah.
*  Is that still carried through to today?
*  VS Code is what I use today.
*  It seems like it's pretty popular.
*  It's the community, basically conversion on.
*  OK, cool.
*  So you got this super optimized C++ system and then you show up to the day of competition.
*  Yeah.
*  Humans versus machine.
*  How did it feel throughout the day?
*  Super stressful.
*  I mean, I thought going into it that we had like a 50-50 chance.
*  Basically, I thought if they play in a totally normal style, I think we'll squeak out a win.
*  But there's always a chance that they can find some weakness in the bot.
*  And if they do, and we're playing like for 20 days, 120,000 hands of poker, they have a lot of time to find weaknesses in the system.
*  And if they do, we're going to get crushed.
*  And that's actually what happened in the previous competition.
*  The humans, they started out, it wasn't like they were winning from the start.
*  But then they found these weaknesses that they could take advantage of.
*  And for the next 10 days, they were just crushing the bot, stealing money from it.
*  What were the weaknesses they found?
*  Maybe overbetting was effective, that kind of stuff, so certain betting strategies worked.
*  What they found is, yeah, overbetting, like betting certain amounts, the bot would have a lot of trouble dealing with those sizes.
*  And then also, when the bot got into really difficult all-in situations, it wasn't able to, because it wasn't doing search,
*  it had to clump different hands together and it would treat them identically.
*  And so it wouldn't be able to distinguish having a king high flush versus an ace high flush.
*  And in some situations, that really matters a lot.
*  And so they could put the bot into those situations and then the bot would just bleed money.
*  Clever humans.
*  Okay, so I didn't realize it was over 20 days.
*  So what were the humans like over those 20 days?
*  And what was the bot like?
*  So we had set up the competition, like I said, there was $200,000 in prize money,
*  and they would get paid a fraction of that depending on how well they did relative to each other.
*  So I was kind of hoping that they wouldn't work together to try to find weaknesses in the bot.
*  But they entered the competition with their number one objective being to beat the bot.
*  And they didn't care about individual glory, they were like,
*  we're all going to work as a team to try to take down this bot.
*  And so they immediately started comparing notes.
*  What they would do is they would coordinate looking at different parts of the strategy
*  to try to find out weaknesses.
*  And then at the end of the day, we actually sent them a log of all the hands that were played
*  and what cards the bot had on each of those hands.
*  Oh, wow. That's gutsy.
*  Yeah, it was honestly, I'm not sure why we did that in retrospect,
*  but I mean, I'm glad we did it because we ended up winning anyway.
*  But if you've ever played poker before, that is golden information.
*  I mean, to know, usually when you play poker, you see about a third of the hands to showdown.
*  And to just hand them all the cards that the bot had on every single hand,
*  that was just a gold mine for them.
*  And so then they would review the hands and try to see, like,
*  okay, could they find patterns in the bot, weaknesses?
*  And could they then they would coordinate and study together and try to figure out,
*  okay, now this person's going to explore this part of the strategy for weaknesses.
*  This person is going to explore this part of the strategy for weaknesses.
*  It's a kind of psychological warfare showing in the hands.
*  Yeah.
*  I mean, I'm sure you didn't think of it that way, but like doing that means you're confident
*  in the possibility to win.
*  Well, that's one way of putting it. I wasn't super confident.
*  So, you know, going in, like I said, I think I had like 50-50 odds on us winning.
*  When we actually, when we announced the competition,
*  the poker community decided to gamble on who would win.
*  And their initial odds against us were like four to one.
*  They were really convinced that the humans were going to pull out a win.
*  The bot ended up winning for three days straight.
*  And even then, after three days, the betting odds were still just 50-50.
*  And then at that point, it started to look like the humans were coming back.
*  They started to like, you know, but poker is a very high variance game.
*  And I think what happened is like they thought that they spotted some weaknesses
*  that weren't actually there.
*  And then around day eight, it was just very clear that they were getting absolutely crushed.
*  And from that point, I mean, for a while there, I was super stressed out thinking like,
*  oh my God, the humans are coming back and they've found weaknesses.
*  And now we're just going to lose the whole thing.
*  But no, it ended up going in the other direction and the bot ended up like crushing them in the long run.
*  How did it feel at the end?
*  Like as a human being, what did, as a person who loves, appreciates the beauty of the game of poker
*  and as the person who appreciates the beauty of AI, is there, did you feel a certain kind of way about it?
*  I felt a lot of things, man.
*  I mean, at that point in my life, I had spent five years working on this project.
*  And it was a huge sense of accomplishment.
*  I mean, to spend five years working on something and finally see it succeed.
*  Yeah, I wouldn't trade that for anything in the world.
*  Yeah, because that's a real benchmark.
*  It's not like getting some percent accuracy on a data set.
*  This is like real.
*  This is real world.
*  It's just a game, but it's also a game that means a lot to a lot of people.
*  And this is humans doing their best to beat the machine.
*  So this is a real benchmark unlike anything else.
*  Yeah. And I mean, this is what I have been dreaming about since I was like 16 playing poker with my friends in high school.
*  The idea that you could find a strategy, approximate the Nash equilibrium, be able to beat all the poker players in the world with it.
*  So to actually see that come to fruition and be realized, that was, it's kind of magical.
*  Yeah, especially money is on the line too.
*  It's different than chess.
*  And that aspect, like people get, that's why you want to look at betting markets.
*  If you want to actually understand what people really think.
*  And in the same sense, poker, it's really high stakes because it's money.
*  And to solve that game, that's an amazing accomplishment.
*  So the leap from that to multi-way six player poker, how difficult is that jump?
*  And what are some interesting differences between heads up poker and multi-way poker?
*  Yeah, so I mentioned, you know, Nash equilibrium in two player zero sum games.
*  If you play that strategy, you are guaranteed to not lose an expectation no matter what your opponent does.
*  Now, once you go to six player poker, you're no longer playing a two player zero sum game.
*  And so there was a lot of debate among the academic community and among the poker community about how well these techniques would extend beyond just two player heads up poker.
*  Now, what I had come to realize is that the techniques actually, I thought, really would extend to six player poker because even though in theory, they don't give you these guarantees outside of two player zero sum games, in practice, it still gives you a really strong strategy.
*  Now, there were a lot of complications that would come up with six player poker besides like the game theoretic aspect.
*  I mean, for one, the game is just exponentially larger.
*  So the main thing that allowed us to go from two player to six player was the idea of depth limited search.
*  So I said before, like, you know, we would do search, we would plan out, the bot would plan out, like, what it's going to do next and for the next several moves.
*  And in the broadest, that search was done extending all the way to the end of the game.
*  So we'd have to start from the turn onwards, like looking maybe 10 moves ahead, it would have to figure out what it was doing for all those moves.
*  Now, when you get to six player poker, it can't do that exhaustive search anymore because the game is just way too large.
*  But by only having to look a few moves ahead and then stopping there and substituting a value estimate of like, how good is that strategy at that point?
*  Then we're able to do a much more scalable form of search.
*  Is there something cool looking at the paper right now?
*  Is there something cool in the paper in terms of graphics?
*  A game tree traversal via Monte Carlo?
*  I think if you go down a bit.
*  Figure one, an example of equilibrium selection problem.
*  Ooh, so yeah.
*  What do we know about equilibrium when there's multiple players?
*  So when you go outside of two players, you're a sum.
*  So a Nash equilibrium is a set of strategies, like one strategy for each player where no player has an incentive to switch to a different strategy.
*  And so you can kind of think of it as like, imagine you have a game where there's a ring.
*  That's actually the visual here.
*  You got a ring and the object of the game is to be as far away from the other players as possible.
*  There's a Nash equilibrium is for all the players to be spaced equally apart around this ring.
*  But there's infinitely many different Nash equilibria, right?
*  There's infinitely many ways to space four dots along a ring.
*  And if every single player independently computes a Nash equilibrium, then there's no guarantee that the joint strategy that they're all playing is going to result is going to be a Nash equilibrium.
*  There is going to be like random dots scattered along this ring rather than four coordinated dots being equally spaced apart.
*  Is it possible to sort of optimally do this kind of selection?
*  To do the selection of the equilibrium you're chasing.
*  So is there like a meta problem to be solved here?
*  So the meta problem is in some sense, how do you how do you understand the Nash equilibria that the other players are going to play?
*  And and even if you do that, again, there's no guarantee that you're going to win.
*  So, you know, if you're playing if you're playing risk, like I said, and all the other players decide to team up against you, you're going to lose.
*  Nash equilibrium doesn't help you there.
*  And so there is this big debate about whether Nash equilibrium and all these techniques that compute it are even useful once you go outside of two players, zero sum games.
*  Now, I think for many games, there is a valid criticism here.
*  And I think when we talk about when we go to something like diplomacy, we run into this issue that the approach of trying to approximate a Nash equilibrium doesn't really work anymore.
*  But it turns out that in six player poker, because six player poker is such an adversarial game where none of the players really try to work with each other, the techniques that were used in two player poker to try to approximate an equilibrium, those still end up working in practice in six player poker.
*  There's some deep way in which six player poker is just a bunch of heads up poker like games in one.
*  It's like it's like embedded in it.
*  So the competitiveness is more fundamental to poker than the cooperation.
*  Right. Yeah. Poker is just such an adversarial game.
*  There's no real cooperation.
*  In fact, you're not even allowed to cooperate in poker.
*  It's considered collusion.
*  It's against the rules.
*  And so for that reason, the techniques end up working really well.
*  And I think that's true more broadly in extremely adversarial games in general.
*  But that's sort of in practice versus being able to prove something.
*  That's right. Nobody has a proof that that's the case.
*  And it could be that that six player poker belongs to some class of games where approximating a Nash equilibrium through self play provably works well.
*  And there are other classes of games beyond just two players, zero sum, where this is proven to work well.
*  So there are these kinds of games called potential games, which I won't go into.
*  It's kind of like a complicated concept.
*  But there are classes of games where this approach to approximating a Nash equilibrium is proven to work well.
*  Now, six player poker is not known to belong to one of those classes, but it is possible that there is some class of games where it either provably performs well or provably performs not that badly.
*  So what are some interesting things about Pluribus that was able to achieve human level performance on this or superhuman level performance on the six player version of poker?
*  I personally I think the most interesting interesting thing about Pluribus is that it was so much cheaper than Lebronis.
*  I mean, Lebronis, if you had to put a price tag on the computational resources that went into it, I would say the final training run took about one hundred thousand dollars.
*  You go to Pluribus, the final training run would cost like less than one hundred fifty dollars on AWS.
*  Is this normalized to computational inflation?
*  So meaning, does this just does this just have to do with the fact that Pluribus was trained like a year later?
*  No, no, no, it's not. It's I mean, first of all, like, yeah, computing resources are getting cheaper every day.
*  And like, but you're not going to see a thousandfold decrease in the computational resources over two years.
*  Or even anywhere close to that.
*  The real improvement was algorithmic improvements and in particular, the ability to do depth limited search.
*  So does depth limited search also work for Lebronis?
*  Yeah, yes. So where this depth limited search came from is, you know, I developed this technique and ran it on two player poker first.
*  And that reduced the computational resources needed to make an AI that was superhuman from, you know, one hundred thousand dollars for the broadest to something you could train on your laptop.
*  What do you learn from that?
*  From that discovery?
*  What I would take away from that is that algorithmic improvements really do matter.
*  How would you describe the more general case of limited depth search?
*  So it's basically constraining the scale, temporal or in some other way of the computation you're doing in some clever way.
*  So like with like, how else can you significantly constrain computation?
*  Right.
*  Well, I think the idea is that we want to be able to leverage search as much as possible.
*  And the way that we were doing it in the broadest required us to search all the way to the end of the game.
*  Now, if you're playing a game like chess, the idea that you're going to search always to the end of the game is kind of unimaginable.
*  Right.
*  Like there's just so many situations where you just won't be able to use search in that case or the cost would be, you know, prohibitive.
*  And this technique allowed us to leverage search and without having to pay such a huge computational cost for it and be able to apply it more broadly.
*  So to what degree did you use neural nets for Lebrados and Pluribus?
*  And more generally, what role do neural nets have to play in superhuman level performance in poker?
*  So we actually did not use neural nets at all for Lebrados or Pluribus.
*  And a lot of people found this surprising back in 2017.
*  I think they found it surprising today that we were able to do this without using any neural nets.
*  And I think the reason for that, I mean, I think neural nets are incredibly powerful and the techniques that are used today, even for poker AIs, do rely quite heavily on neural nets.
*  But it wasn't the main challenge for poker.
*  Like, I think what neural nets are really good for, if you're in a situation where finding features for a value function is really difficult, then neural nets are really powerful.
*  And this was the problem in Go.
*  Right.
*  Like the problem in Go was that, or the final problem in Go, at least, was that nobody had a good way of looking at a board and figuring out who was winning or, describing through a simple algorithm who was winning or losing.
*  And so there, neural nets were super helpful because you could just feed in a ton of different board positions into this neural net and it would be able to predict then who was winning or losing.
*  But in poker, the features weren't the challenge.
*  The challenge was, how do you design a scalable algorithm that would allow you to find this balanced strategy that would understand that you have to bluff with the right probability?
*  So can that be somehow incorporated into the value function?
*  This, the complexity of poker that you've described?
*  Yeah.
*  So the way the value functions work in poker, like the latest and greatest poker AIs, they do use neural nets for the value function.
*  The way it's done is very different from how it's done in a game like chess or Go because in poker, you have to reason about beliefs.
*  And so the value of a state depends on the beliefs that players have about what the different cards are.
*  Like if you have pocket Aces, then whether that's a really, really good hand or just an OK hand depends on whether you know I have pocket Aces.
*  Right?
*  Like if you know that I have pocket Aces, then if I bet you're going to fold immediately.
*  But if you think that I have a really bad hand, then I could bet with pocket Aces and make a ton of money.
*  So the value function in poker these days takes the beliefs as an input, which is very different from how chess and Go AIs work.
*  So as a person who appreciates the game, who do you think is the greatest poker player of all time?
*  That's a tough question.
*  Can AI help answer that question?
*  Can you actually analyze the quality of play?
*  Right?
*  So the chess engines can give estimates of the quality of play.
*  Right.
*  I wonder if there's a is there an ELO rating type of system for poker?
*  I suppose you could, but there's just not enough.
*  You would have to play a lot of games, right?
*  A very large number of games, like more than you would in chess.
*  The deterministic game makes it easier to estimate ELO.
*  I think.
*  I think it is much harder to estimate something like ELO rating in poker.
*  I think it's doable.
*  The problem is that the game is very high variance.
*  So you could play, you could be profitable in poker for a year and you could actually be a bad player just because the variance is so high.
*  I mean, you've got top professional poker players that would lose for a year just because they're on a really bad, bad streak.
*  Yeah.
*  So for ELO, you have to have a nice clean way of saying if player A played player B and A beats B, that says something.
*  That's a signal.
*  In poker, it's a very noisy signal.
*  It's a very noisy signal.
*  Now there is a signal there.
*  And so you could do this, this calculation.
*  It would just be much harder.
*  But the same way that AIs have now taken over chess and, you know, all the top professional chess players train with, with AIs, the same is true for poker.
*  The game has become a very computational.
*  People train with AIs to try to find out where they're making mistakes, try to learn from the AIs to improve their strategy.
*  So now, yeah, so the game has been revolutionized in the past five years by the development of AI in this sport.
*  The skill with which you avoided the question of the greatest of all time was impressive.
*  So my feeling is that it's a difficult, it's a difficult question because just like in chess where you can't really compare Magnus Carlsen today to Garry Kasparov, because the game has evolved so much.
*  The poker players today are so far beyond the skills of like people that were playing even 10 or 20 years ago.
*  So you look at the kinds of like all stars that were on ESPN at like the height of the poker boom.
*  Pretty much all those players are actually not that good at the game today.
*  At least the strategy aspect, I mean, they might still be good at like reading the player at the other side of the table and trying to figure out like, are they bluffing or not?
*  But in terms of the actual like computational strategy of the game, a lot of them have really struggled to keep up with that development.
*  Now, so for that reason, I'll give an answer and I'm going to say Daniel Legranio, who you actually had on the podcast recently.
*  I saw it was a great episode.
*  I love this so much.
*  And Phil's going to hate this so much.
*  And I'm going to give him credit because he is one of the few like old school, really strong players that have kept up with the development of AI.
*  So he is trying to, he's constantly studying the game theory optimal way of playing.
*  Exactly. Yeah.
*  And I think a lot of the old school poker players have just kind of given up on that aspect.
*  And I got to give Daniel Legranio credit for keeping up with all the developments that are happening in the sport.
*  Yeah, it's fascinating to watch.
*  It's fascinating to watch where it's headed.
*  Yeah. So there you go.
*  Some love for Daniel.
*  Quick pause.
*  Bath and break.
*  Yeah, let's do it.
*  Let's go from poker to diplomacy.
*  What is at a high level the game of diplomacy?
*  Yeah. So I talked a lot about two players, zero sum games.
*  And what's interesting about diplomacy is that it's very different from these like adversarial games like chess, go poker, even Starcraft and Dota.
*  Diplomacy has a much bigger cooperative element to it.
*  It's a seven player game.
*  It was actually created in the 50s and it takes place before World War I.
*  It's like a map of Europe with seven great powers.
*  And they're all trying to form alliances with each other.
*  There's a lot of negotiation going on.
*  And so the whole focus of the game is on forming alliances with the other players to take on the other players.
*  England, Germany, Russia, Turkey, Austria, Hungary, Italy and France.
*  That's right.
*  Yeah. So the way the game works is on each turn, you spend about five to 15 minutes talking to the other players in privates and you make all sorts of deals with them.
*  You say like, hey, let's work together.
*  You know, let's team up against this other player, because the only way that you can make progress is by working with somebody else against the others.
*  And then after that negotiation period is done, all the players simultaneously submit their moves and they're all executed at the same time.
*  And so you can tell people like, hey, I'm going to support you this turn, but then you don't follow through with it.
*  And they're only going to figure that out once they see the moves being read off.
*  How much of it is natural language, like written actual text?
*  How much is like you're actually saying phrases that are structured?
*  So there's different ways to play the game.
*  You can play it in person and in that case, it's all natural language, free form communication.
*  There's no constraints on the kinds of deals that you can make, the kinds of things that you can discuss.
*  You can also play it online so you can send long emails back and forth.
*  You can play it like live online or over voice chat.
*  But the focus, the important thing to understand is that this is unstructured communication.
*  You can say whatever you want.
*  You can make any sorts of deals that you want.
*  And everything is done privately.
*  So it's not like you're all around the board together having a conversation.
*  You're grabbing somebody going off into a corner and conspiring behind everybody else's back about what you're planning.
*  And there's no limit in theory to the conversation you can have directly with one person.
*  That's right. You can make all sorts of...
*  You can talk about anything. You could say like, hey, let's have a long term alliance against this guy.
*  You can say like, hey, can you support me this turn in return?
*  I'll do this other thing for you next turn.
*  Or, you know, yeah, just you can talk about like what you talked about with somebody else and gossip about like what they're planning.
*  The way that I would describe the game is that it's kind of like a mix between Risk, Poker, and the TV show Survivor.
*  There's like this big element of like trying to...
*  Yeah, there's a big social element.
*  And the best way that I would describe the game is that it's really a game about people rather than the pieces.
*  So Risk, because it is a map, it's kind of war game like.
*  Poker, because there's a game theory component that's very kind of strategic.
*  So you could convert it into an artificial intelligence problem and then survive it because of the social component.
*  That's a strong social component.
*  I saw that somebody said online that the internet version of the game has this quality of that it's easier to almost to do like role playing as opposed to being yourself.
*  You can actually like be the like really imagine yourself as the leader of France or Russia and so on, like really pretend to be that person.
*  It's actually fun to really lean into being that that leader.
*  Yeah, so some players do go this route where they just like kind of view it as a strategy game, but also a role playing game where they can like act out like,
*  what would I be like if I was, you know, a leader of France in 1900?
*  Forfeit right away.
*  No, I'm just kidding.
*  And they sometimes use like the old timey language to like or how they imagine the elites would talk at that time anyway.
*  So what are the different turns of the game?
*  Like, what are the rounds?
*  Yeah, so on every turn you got like a bunch of different units that you start out with.
*  So you start out controlling like just a few units and the object of the game is to gain control of a majority of the map.
*  If you're able to if you're able to do that, then you've won the game.
*  But like I said, the only way that you're able to do that is by working with other players.
*  So on every turn you can issue a move order.
*  So for each of your units, you can move them to an adjacent territory or you can keep them where they are or you can support a move or hold of a different unit.
*  So what are the territories?
*  Well, how is the map divided up?
*  It's kind of like risk where the map is divided up into like 50 different territories.
*  Now, you can enter a territory if you're moving into that territory with more support than the person that's in there or the person that's trying to move in there.
*  So if you're moving in and there's somebody already there, then if neither of you have support, it's a one versus one and you'll bounce back and neither of you will make progress.
*  If you have a unit that's supporting that move into the territory, then it's a two versus one and you'll kick them out and they'll have to retreat somewhere.
*  What does support mean?
*  Support is like it's an action that you can issue in the game.
*  So you can say this unit, you write down this unit is supporting this other unit into this territory.
*  Are these units from opposing forces?
*  It could be.
*  They could be.
*  And this is where the interesting aspect of the game comes in, because you can support your own units into territory, but you can also support other people's units into territories.
*  And so that's what the negotiations really revolve around.
*  But you don't have to do the thing you say you're going to do.
*  And this.
*  Yeah.
*  And so you can say, I'm going to support you, but then backstab the person.
*  Yeah, that's absolutely right.
*  And that tension is core to the game.
*  That tension is absolutely core to the game.
*  The fact that you can make all sorts of promises, but you have to reason about the fact that they might not trust you if you say you're going to do something or they might be lying to you when they say they're going to support you.
*  So maybe just to jump back, what's the history of the game in general?
*  Is it true that Henry Kissinger loved the game and JFK and all those?
*  I've heard like a bunch of different people that.
*  Or is that just one of those things that the cool kids say they do, but they don't actually play?
*  So the game was created in the 50s.
*  Yeah.
*  And from what I understand, it was JFK's.
*  It was played in like the JFK White House, Henry Kissinger's favorite game.
*  I don't know if it's true, but that's definitely what I've heard.
*  It's interesting that they went with World War One when it was created after World War Two.
*  So the story that I've heard for the creation of the game is it was created by somebody that had looked at the history of the 20th century and they saw World War One as a failure of diplomacy.
*  So they saw the fact that this war broke out as like the diplomats of all these countries really failed to prevent a war.
*  And he wanted to create a game that would basically teach people about diplomacy.
*  And it's really fascinating that in his ideal version of the game of diplomacy, nobody actually wins the game.
*  Because the whole point is that if somebody is about to win, then the other players should be able to work together to stop that person from winning.
*  And so the ideal version of the game is just one where nobody actually wins.
*  And it kind of has a nice, like wholesome take home message then that war is ultimately futile.
*  And that feudal optimal could be achieved through great diplomacy.
*  So is there some asymmetry in terms of which is more powerful, Russia versus Germany versus France and so on?
*  So I think the general consensus is that France is the strongest power in the game.
*  But the beautiful thing about diplomacy is that it's self-balancing, right?
*  So the fact that France has an inherited advantage from the beginning means that the other players are less likely to work with it.
*  I saw that Russia has four units or four of something that the others have three of something.
*  That's true. Yeah. So Russia starts off with four units while all the other players start with three.
*  But Russia is also in a much more vulnerable position because they have to like they have a lot more neighbors as well.
*  Larger territory, more border to defend.
*  OK, what else is important to know about the rules?
*  So how many rounds are there? Like is this iterative game? Is it finite? Do you just keep going indefinitely?
*  Usually the game lasts, I would say about 15 or 20 turns.
*  There's in theory no limit. It could last longer.
*  But at some point, I mean, if you're playing a house game with friends, at some point you just get tired and you all agree like, OK, we're going to end the game here and call it a draw.
*  If you're playing online, there's usually like set limits on when the game will actually end.
*  And what's the end? What's the termination condition? Like this one country have to conquer everything else?
*  So if somebody is able to actually gain control of a majority of the map, then they've won the game.
*  And that is a solo victory, as it's called.
*  Now, that pretty rarely happens, especially with strong players, because, like I said, the game is designed to incentivize the other players to put a stop to that and all work together to stop the superpower.
*  Usually what ends up happening is that all the players agree to a draw and then the score, the win is divided among the remaining players.
*  There's a lot of different scoring systems.
*  The one that we used in our research basically gives a score relative to how much control you have of the map.
*  So the more that you control, the higher your score.
*  What's the history of using this game as a benchmark for research to do?
*  People use it?
*  Yeah. So people have been working on AI for diplomacy since about the 80s.
*  There was some really exciting research back then, but the approach that was taken was very different from what we see today.
*  I mean, the research in the 80s was a very rule based approach, kind of a heuristic approach.
*  It was very in line with the kind of research that was being done in the 80s, basically trying to encode human knowledge into the strategy of the AI.
*  And it's understandable.
*  I mean, the game is so incredibly different and so much more complicated than the kinds of games that people were working on, like chess and go and poker, that it was honestly even hard to start making any progress in diplomacy.
*  Can you just formulate what is the problem from an AI perspective and why is it hard?
*  Why is it a challenging game to solve?
*  So there's a lot of aspects in diplomacy that make it a huge challenge.
*  First of all, you have the natural language components.
*  And I think this really is what makes it really the most difficult game among the major benchmarks.
*  The fact that you have to it's not about moving pieces on the board.
*  Your action space is basically all the different sentences that you could communicate to somebody else in this game.
*  Can we just linger on that?
*  So is part of it like the ambiguity in the language?
*  If it was like very strict, if you narrowed the set of possible sentences, you could do it, would that simplify the game significantly?
*  The real difficulty is the breadth of things that you can talk about.
*  You could have natural language in other games, like Settlers of Catan, for example, you could have a natural language, Settlers of Catan AI.
*  But the things that you're going to talk about are basically like, am I treating you two sheep for a wood or three sheep for a wood?
*  Whereas in a game like Diplomacy, the breadth of conversations that you're going to have are like, you know, am I going to support you?
*  Are you going to support me in return?
*  Which units are going to do what?
*  What did this other person promise you?
*  They're lying because they told this other person that they're going to do this instead.
*  If you help me out this turn, then in the future, I'll do these things that will help you out.
*  The depth and breadth of these conversations is really complicated and it's all being done in natural language.
*  Now, you could approach it and we actually consider doing this, like having a simplified language to make this complexity smaller.
*  But ultimately, we thought the most impactful way of doing this research would be to address the natural language component head on and just try to go for the full game upfront.
*  Just looking at sample games and what the conversations look like.
*  Greetings England.
*  This should prove to be a fun game since all the private press is going to be made public at the end.
*  At the least, it will be interesting to see if the press changes because of that anyway.
*  Good. OK, so there's like.
*  Yeah, that's just kind of like the generic greetings at the beginning of the game.
*  I think that the meat comes a little bit later when you're starting to talk about like specific strategy and stuff.
*  I agree there are a lot of advantages to the two of us keeping in touch and our nations make strong natural allies in the middle game.
*  So that kind of stuff, making friends, making enemies.
*  Yeah, or like if you look at the next line, so the person saying like I've heard bits about a Lepanto and an octopus opening and basically telling Austria like, hey, just a heads up.
*  You know, I've heard these whispers about like what might be going on behind your back.
*  Yeah, so there's all kinds of complexities in the language of that, right?
*  Like to interpret what the heck that means.
*  It's hard for us humans, but for AI it's even harder because you have to understand like at every level the semantics of that.
*  Right. I mean, there's the complexity and understanding when somebody is saying this to me, what does that mean?
*  And then there's also the complexity of like, should I be telling this person this?
*  Like I've overheard these whispers.
*  Should I be telling this person that like, hey, you might be getting attacked by this other power?
*  OK, so what how are we supposed to think about?
*  OK, so that's the natural language.
*  How do you even begin trying to solve this game?
*  It seems like this seems like the Torrential Asteroids.
*  Yeah, and I mean, there's the natural language aspect.
*  And then even besides the natural language aspect, you also have the cooperative elements of the game.
*  And I think this is actually something that I find really interesting.
*  If you look at all the previous game breakthroughs, they've all happened in these purely adversarial games where you don't actually need to understand how humans play the game.
*  It's all just AI versus AI.
*  Right. Like you look at checkers, chess, go poker, StarCraft, Dota 2.
*  Like in some of those cases, they leveraged human data, but they never needed to.
*  They were always just trying to have a scalable algorithm that then they could throw a lot of computational resources at a lot of memory at.
*  And then eventually it would converge to an approximation of a Nash equilibrium.
*  This perfect strategy that in a two player zero sum game guarantees that they're going to be able to not lose to any opponent.
*  So you can't leverage self play to solve this game.
*  You can leverage self play, but it's no longer sufficient to beat humans.
*  So how do you integrate the human into the loop of this?
*  So what you have to do is incorporate human data and to kind of give you some intuition for why this is the case.
*  Like imagine you're playing a negotiation game like diplomacy, but you're training completely from scratch without any human data.
*  The AI is not going to suddenly like figure out how to communicate in English.
*  It's going to figure out some weird robot language that only it will understand.
*  And then when you stick that in a game with six other humans, they're going to think this person is talking gibberish and they're just going to ally with each other and team up against the bot.
*  Or not even team up against the bot, but just not work with the bot.
*  And so in order to be able to play this game with humans, it has to understand the human way of playing the game, not this machine way of playing the game.
*  Yeah, that's fascinating.
*  Right. That's a nuanced thing to understand because a chess playing program doesn't need to play like a human to beat a human.
*  Exactly.
*  But here you have to play like a human in order to beat them.
*  Or at least you have to understand how humans play the game so that you can understand how to work with them.
*  If they have certain expectations about what does it mean to be a good ally?
*  What does it mean to have like a reciprocal relationship where we're working together?
*  You have to abide by those conventions, and if you don't, they're just going to work with somebody else instead.
*  Do you think of this as a clean and some deep sense of the spirit of the touring test is formulated by Alan Turing?
*  Is it is some sense this is what the touring test actually looks like?
*  So because of open ended natural language conversation seems like very difficult to evaluate.
*  Like here at a high stakes where humans are trying to win a game, that seems like how you actually perform the touring test.
*  I think it's different from the touring test.
*  Like the way that the touring test is formulated, it's about trying to distinguish a human from a machine and seeing, oh,
*  could the machine successfully pass as a human in this adversarial setting where the where the player is trying to figure out whether it's a machine or a human?
*  Whereas in diplomacy, it's not about trying to figure out whether this player is a human or machine.
*  It's ultimately about whether I can work with this player, regardless of whether they are human or machine.
*  And can the machine do that better than a human can?
*  Yeah, I'm going to think about that, but that just feels like the implied requirement for that is for the machine to be human like.
*  I think that's I think that's true, that if you're going to play in this human game, you have to somehow adapt to the to the human surroundings and the human play style.
*  And to win, you have to adapt.
*  So you can't if you're the outsider, if you're not human like, I feel like that's a losing strategy.
*  I think that's I think that's correct. Yeah.
*  Yeah. So, OK. What are the complexities here?
*  What was your approach to it?
*  Before I get to that, one thing I should explain, like why we decided to work on diplomacy.
*  So basically what happened is in 2019, I was wrapping up the work on Six Player Poker on Pluribus and was trying to think about what to work on next.
*  And I had been seeing like all these other breakthroughs happening in AI.
*  I mean, like 2019, you have StarCraft, you have AlphaStar beating humans in StarCraft.
*  You've got the Dota 2 stuff happening at OpenAI.
*  You have GPT-2 or GPT-3. I think it was GPT-2 at the time.
*  And it became clear that AI was progressing really, really rapidly.
*  And people were throwing out these other games about what should be the next challenge for multi-agent AI.
*  And I just felt like we had to aim bigger.
*  If you look at a game like Chess or a game like Go, they took decades for researchers to ultimately reach superhuman performance at.
*  I mean, like Chess took 40 years of AI research. Go took another 20 years.
*  And we thought that diplomacy would be this incredibly difficult challenge that could easily take a decade to make an AI that could play competently.
*  But we felt like that was a goal worth aiming for.
*  And so honestly, I was kind of reluctant to work on it at first because I thought it was like too far out of the realm of possibility.
*  But I was talking to a coworker of mine, Adam Lerner, and he was basically saying, like, why not aim for it?
*  We'll learn some interesting things along the way and maybe it'll be possible.
*  And so we decided to go for it. And I think it was the right choice considering just how much progress there was in AI and that progress has continued in the years since.
*  So winning in diplomacy, what does that really look like?
*  It means talking to six other players, six other entities, agents and convincing.
*  And convincing them of stuff that you want them to be convinced of.
*  What exactly I'm trying to get like to deeply understand what the problem is.
*  Ultimately, the problem is, it's simple to to quantify, right?
*  You're going to play this game with humans and you want your score on average to be as high as possible.
*  If you can say like, I am winning more than any human alive, then you're a champion diplomacy player.
*  Now, ultimately, we didn't reach that. We got to human level performance.
*  We actually so we played about 40 games with real humans online.
*  The bot came in second out of all players that played five or more games.
*  And so not like number one, but way, way higher than what was the expertise level of the beginners, the intermediate players, advanced players.
*  So that's a great question.
*  And so I think this kind of goes into how do you measure the performance in diplomacy?
*  And I would argue that when you're measuring performance in a game like this, you don't actually want to measure it in games with all expert players.
*  It's kind of like if you're developing a self-driving car, you don't want to measure that car on the road with a bunch of expert stunt drivers.
*  You want to put it on a road of like an actual American city and see is this car crashing less often than an expert driver would.
*  So that's the metric that we've used.
*  We we're saying like we're going to stick this game, we're going to stick this bot in games with a wide variety of skill levels.
*  And then are we doing better than a strong or expert human player would in the same situation?
*  That's quite brilliant, because I played a lot of sports in my life, like I did tennis, judo, whatever.
*  And it's somehow almost easier to go against experts almost always.
*  I think they're more predictable in the quality of play that the space of strategies you're operating under is narrower against experts.
*  It's more fun. It's really frustrating to go against beginners.
*  Also, because beginners talk trash to you when they somehow do beat you.
*  So that's a human thing that they had to be worried about that.
*  But yeah, the variance in strategies is greater, especially with natural language.
*  It's just all over the place then.
*  Yeah. And honestly, when you look at what makes a good human diplomacy player, obviously they're able to handle themselves in games with other expert humans.
*  But where they really shine is when they're playing with these weak players and they know how to take advantage of the fact that they're a weak player,
*  that they won't be able to pull off a stab as well, or that they have certain tendencies and they can take them under their wing and persuade them to do things that might not even be in their interest.
*  The really good diplomacy players are able to take advantage of the fact that there are some weak players in the game.
*  OK, so if you have to incorporate human play data, how do you do that?
*  How do you do that in order to train an AI system to play diplomacy?
*  Yeah, so that's really the crux of the problem.
*  How do we leverage the benefits of self-play that have been so successful in all these other previous games while keeping the strategy as human compatible as possible?
*  And so what we did is we first trained a language model and then we made that language model controllable on a set of intents,
*  what we call intents, which are basically like an action that we want to play and an action that we would like the other player to play.
*  And so this gives us a way to generate dialogue that's not just trying to imitate the human style, whatever a human would say in the situation,
*  but to actually give it an intent, a purpose in its communication.
*  We can talk about a specific move or we can make a specific request.
*  And the determination of what that move is that we're discussing comes from a strategic reasoning model that uses reinforcement learning and planning.
*  So the computing the intents for all the players, how is that done?
*  Just as a starting point, is that with reinforcement learning or is that just optimal determining what the optimal is for intents?
*  It's a combination of reinforcement learning and planning.
*  Actually, very similar to how we approached poker and how people approached chess and Go as well.
*  We're using self-play and search to try to figure out what is an optimal move for us and what is a desirable move that we would like this other player to play.
*  Now, the difference between the way that we approached reinforcement learning and search in this game versus those previous games is that we have to keep it human compatible.
*  We have to understand how the other person is likely to play rather than just assuming that they're going to play like a machine.
*  And how language gets them to play in a way that maximizes the chance of following the intent you want them to follow.
*  OK, how do you do that? How do you connect language to intent?
*  So the way that RL and planning is done is actually not using language.
*  So we're coming up with this plan for the action that we're going to play and the other person is going to play.
*  And then we feed that action into the dialogue model that will then send a message according to those plans.
*  So the language model there is mapping action to message one word at a time.
*  Basically, one message at a time. So we'll feed into the dialogue model.
*  Like, here are the actions that you should be discussing.
*  Here's the message. Here's the content of the message that we would like you to send.
*  And then it will actually generate a message that corresponds to that.
*  OK, does this actually work?
*  It works surprisingly well.
*  OK, how? Oh, man, the number of ways it probably goes horribly.
*  I would have imagined it goes horribly wrong. So how the heck is it effective at all?
*  I mean, there are a lot of ways that this could fail.
*  So, for example, I mean, you could have a situation where you're basically like we don't tell the language model,
*  like, here are the pieces of our action or the other person's action that you should be communicating.
*  And so, like, let's say you're about to attack somebody.
*  You probably don't want to tell them that you're going to attack them.
*  But there's nothing in the language. The language model is not very smart at the end of the day.
*  So it doesn't really have a way of knowing, like, well, what should I be talking about?
*  Should I tell this person I'm about to attack them or not?
*  So we have to develop a lot of other techniques that deal with that.
*  Like, one of the things we do, for example, is we try to calculate if I'm going to send this message,
*  what would I expect the other person to do in response?
*  So if it's a message like, hey, I'm going to attack you this turn, they're probably going to attack us or defend against that attack.
*  And so we have a way of recognizing, like, hey, sending this message is a negative expected value action and we should not send this message.
*  So, yes, for particular kinds of messages, you have like an extra function that does the estimates the value of that message.
*  Yeah. So we have these kinds of filters that, like...
*  So it's a filter. So there's a good... Is that filter in your network or is it rule based?
*  That's a neural network. So we're... Well, it's a combination. It's a neural network, but it's also using planning.
*  It's trying to compute, like, what is the policy that the other players are going to play given that this message has been sent?
*  And then is that better than not sending the message?
*  I feel like that's how my brain works, too.
*  Like, there's a language model that generates random crap and then there's these other neural nets that are essentially filters.
*  At least that's when I tweet.
*  Usually my process of tweeting, I'll think of something and it's hilarious to me.
*  And then about five seconds later, the filter network comes in and says, no, no, that's not funny at all.
*  I mean, there's something interesting to that kind of process.
*  So you have a set of actions that you want.
*  You have an intent that you want to achieve, an intent that you want your opponent to achieve,
*  then you generate messages and then you evaluate if those messages will achieve the goal you want.
*  Yeah. And we're filtering for several things.
*  We're filtering, like, is this a sensible message?
*  So sometimes language models will generate messages that are just like totally nonsense.
*  And we try to filter those out.
*  We also try to filter out messages that are basically lies.
*  So diplomacy has this reputation as a game that's really about deception and lying.
*  But we try to actually minimize the amount that the bot would lie.
*  This was actually mostly a-
*  Or are you?
*  No, I'm just kidding.
*  I mean, like part of the reason for this is that we actually found that lying would make the bot perform worse in the long run.
*  It would end up with a lower score because once the bot lies, people would never trust it again.
*  And trust is a huge aspect of the game of diplomacy.
*  Taking notes here because I think this applies to life lessons too.
*  Oh, I think it's a really, yeah, really strong-
*  So like lying is a dangerous thing to do.
*  Like you want to avoid obvious lying.
*  Yeah, I mean, I think when people play diplomacy for the first time, they approach it as a game of deception and lying.
*  And they ultimately, if you talk to top diplomacy players, what they'll tell you is that diplomacy is a game about trust and being able to build trust in an environment that encourages people to not trust anyone.
*  So that's the ultimate tension in diplomacy.
*  How can this AI reason about whether you are being honest in your communication?
*  And how can the AI persuade you that it is being honest when it is telling you that, hey, I'm actually going to support you this turn?
*  Is there some sense, I don't know if you step back and think, that this process will indirectly help us study human psychology?
*  So like if trust is the ultimate goal, wouldn't that help us understand what are the fundamental aspects of forming trust between humans and between humans and AI?
*  I mean, that's a really, really important question that's much bigger than the strategy games.
*  It's how can that's fundamental to the human-robot interaction problem.
*  How do we form trust between intelligent entities?
*  So one of the things I'm really excited about with diplomacy, there's never really been a good domain to investigate these kinds of questions.
*  And diplomacy gives us a domain where trust is really at the center of it.
*  And it's not just like you've hired a bunch of mechanical turkers that are being paid and trying to get through the task as quickly as possible.
*  You have these people that are really invested in the outcome of the game, and they're really trying to do the best that they can.
*  And so I'm really excited that we're able to, we actually like have put together this, we're open sourcing all of our models, we're open sourcing all of the code,
*  and we're making the data that we've used available to researchers so that they can investigate these kinds of questions.
*  So the data of the different, the human and the AI play of diplomacy and the models that you use for the generation of the messages and the filtering?
*  Yeah, not just even the data of the AI playing with the humans, but all the training data that we had, that we used to train the AI to understand how humans play the game.
*  We're setting up a system where researchers will be able to apply to be able to gain access to that data and be able to use it in their own research.
*  We should say, what is the name of the system?
*  We're calling the bot Cicero.
*  And what's the name, like you're open sourcing, what's the name of the repository and the project?
*  Is it also just called Cicero, the big project?
*  Or are you still coming up with a name?
*  The data set comes from this website, Web Diplomacy.net, is this site that's been online for like 20 years now, and it's one of the main sites that people use to play diplomacy on it.
*  We've got like 50,000 games of diplomacy with natural language communication, over 10 million messages.
*  So it's a pretty massive data set that people can use to, we're hoping that the academic community, the research community is able to use it for all sorts of interesting research questions.
*  So to you, from having studied this game, is this a sufficiently rich problem space to explore this kind of human AI interaction?
*  Yeah, absolutely.
*  And I think it's maybe the best data set that I can think of out there to investigate these kinds of questions of negotiation, trust, persuasion.
*  I wouldn't say it's the best data set in the world for human AI interaction.
*  That's a very broad field.
*  But I think that it's definitely up there is like, if you're really interested in language models interacting with humans in a setting where their incentives are not fully aligned, this seems like an ideal data set for investigating that.
*  So you have a paper with some impressive results and just an impressive paper that taken this problem on.
*  What's the most exciting thing to you in terms of the results from the paper?
*  Well, I think there's ideas or results.
*  Yeah, I think there's a few aspects of the results that I think are really exciting.
*  So first of all, the fact that we were able to achieve such strong performance, I was surprised by and pleasantly surprised by.
*  So we played 40 games of diplomacy with real humans and the bot placed second out of all players that have played five or more games.
*  So it's about 80 players total, 19 of whom played five or more games, and the bot was ranked second out of those players.
*  And the bot was was really good in two dimensions.
*  One, being able to establish strong connections with the other players on the board, being able to persuade them to work with it, being able to coordinate with them about how it's going to work with them.
*  And then also the raw tactical and strategic aspects of the game, being able to understand what the other players are likely to do, being able to model their behavior and respond appropriately to that.
*  The bot also really excelled at.
*  What are some interesting things that the bot said?
*  By the way, you're allowed to swear in the, are there rules to what you're allowed to say and not in diplomacy?
*  You can say whatever you want.
*  I think the site will get very angry at you if you start like threatening somebody.
*  And we actually like if you threaten somebody, you're supposed to do it politely.
*  Yeah, politely, you know, keep it in character.
*  We actually had a researcher watching the bot 24 7, well, whenever we play a game, we have a bot watching it to make sure that it wouldn't go off the rails and start like threatening somebody or something like that.
*  I would just love it if the bots started like mocking, mocking everybody, like some weird, quirky strategies would emerge.
*  Have you seen anything interesting that you, huh, that's a weird, that's a behavior, either the filter or the language model that was weird to you?
*  That was yeah, there were definitely like things that the bot would would do that were not in line with like how humans would approach the game and that in a good way, the humans actually, you know, we've talked to some expert diplomacy players about these results.
*  And their takeaway is that, well, maybe humans are approaching this the wrong way.
*  And this is actually like the right way to play the game.
*  So what's required to win?
*  Like what? What does it mean to mess up or to exploit the suboptimal behavior of a player?
*  Like, is there is there optimally rational behavior and irrational behavior that you need to estimate that kind of stuff?
*  Like what what stands out to you?
*  Like, is there a crack that you can exploit?
*  Is there like a weakness that you can exploit in the game that everybody's looking for?
*  Well, I think you're asking kind of two questions there.
*  So one like modeling the irrationality and the suboptimality of humans.
*  You can't in diplomacy, you can't treat all the other players like their machines.
*  And if you do that, you're going to end up playing really poorly.
*  And so we actually ran this experiment.
*  So we we trained a bot in a two player, zero sum version of diplomacy the same way that you might approach a game like chess or poker.
*  And the bot was superhuman.
*  It would crush any competitor.
*  And then we took that same training approach and we trained a bot for the full seven player version of the game through self play without any human data.
*  And we stuck it in a game with six humans and it got destroyed.
*  Even in the version of the game where there's no explicit natural language communication, it still got destroyed because it just wouldn't be able to understand how the other players were approaching the game and be able to to work with that.
*  Can you just linger on that meaning like there's an individual there's an individual personality, each player, and you're supposed to remember that.
*  But what do you mean it's not able to understand the players?
*  Well, it would, for example, expect the human to support it in a certain way when the human would simply like, thank you like, no, I'm not supposed to support you here.
*  It's kind of like, you know, if you develop a self-driving car and it's trained completely from scratch with other self-driving cars, it might learn to drive on the left side of the road.
*  That's a totally reasonable thing to do if you're with these other self-driving cars that are also driving on the left side of the road.
*  But if you put it in an American city, it's going to crash.
*  But I guess the intuition I'm trying to build up is why does it then crush a human player heads up?
*  This is multiple.
*  This is an aspect of two players, zero sum versus games that involve cooperation.
*  So in a two player, zero sum game, you can do self play from scratch and you will arrive at the Nash equilibrium where you don't have to worry about the other player playing in a very human suboptimal style.
*  That's just going to be the only way that deviating from a Nash equilibrium would would change things is if it helped you.
*  So what's the dynamic of cooperation that's effective in diplomacy?
*  Do you always have to have one friend in the game?
*  You always want to maximize your friends and minimize your enemies.
*  Got it. And. Boy, in the line comes into play there.
*  So the more friends you have, the better.
*  Yeah, I mean, I guess you have to attack somebody or else you're not going to make progress.
*  Right. So that's the tension. But this is too real.
*  This is too close to geopolitics of actual military conflict in the world.
*  OK, that's fascinating. So that cooperation element is what makes the game really, really hard.
*  Yeah. And to give you an example of how this suboptimality and irrationality comes into play, there's a really common situation in a game of diplomacy where one player starts to win and they're like at the point where they're controlling about half the map.
*  And the remaining players who have all been fighting each other the whole game all have to work together now to stop this other player from winning or else everybody's going to lose.
*  And it's kind of like a game of Thrones.
*  Like I've seen the show where you got the others coming from the north and all the people have to start to work out the differences and stop them from taking over.
*  And the bot will do this. The bot will work with the other players to stop the superpower from winning.
*  But if it doesn't really if it's trained from scratch or it doesn't really have a good grounding in how humans approach it, it will also at the same time attack the other players with its extra units.
*  So all the units that are not necessary to stop the superpower from winning, it will use those to grab as many centers as possible from the other players.
*  And in totally rational play, the other players should just live with that.
*  They have to understand like, hey, a score of one is better than a score of zero.
*  So, so, OK, he's grabbed my centers, but I'll just deal with it.
*  But humans don't act that way.
*  The human gets really angry at the bot and ends up throwing the game because, you know, I'm going to screw you over because you did something that's not fair to me.
*  Got it. And are you supposed to model that? Is the bot supposed to model that kind of human frustration?
*  Yeah, exactly. And so that is something that seems almost impossible to model purely from scratch without any human data.
*  It's a very cultural thing. And so you need human data to be able to understand that, hey, that's how humans behave and you have to work around that.
*  It might be suboptimal, it might be irrational, but that's an aspect of humanity that you have to you have to deal with.
*  So how difficult is it to train on human data given that human data is very limited versus what a purely self-playing mechanism can generate?
*  That's actually one of the major challenges that we faced in the research that we had a good amount of human data.
*  We had about 50,000 games. What we try to do is leverage as much self-play as possible while still leveraging the human data.
*  So what we do is we do self-play very similar to how it's been done in poker and go, but we try to regularize the self-play towards the human data.
*  Basically, the way to think about it is we penalize the bot for choosing actions that are very unlikely under how under the human data set.
*  And so, you know, is there some kind of function that says this is human like and not?
*  Yeah, so we train a bot through supervised learning to model the human play as much as possible.
*  So we basically like train a neural net on those 50,000 games.
*  And that gives us an approximate that gives us a policy that resembles to some extent how humans actually play the game.
*  Now, this isn't a perfect model of human play because we don't have unlimited data.
*  We don't have unlimited neural net capacity, but it gives us some approximation.
*  Is there some data on the Internet that's useful besides just diplomacy?
*  So on the language side of things, is there some can you go to like Reddit and so sort of background model formulation that that's useful for the game of diplomacy?
*  Yeah, absolutely. And so for the language model, which is kind of like a separate question, we didn't use the language model during self-play training,
*  but we pre-trained the language model on tons of Internet data as much as possible.
*  And then we fine tuned it specifically on the diplomacy games.
*  So we are able to leverage the wider data set in order to fill in some of the gaps in how communication happens more broadly, besides just specifically in these diplomacy games.
*  OK, cool. So what are some interesting things that came to life from this work to you?
*  What are some insights about games where natural language is involved and cooperation, deep cooperation is involved?
*  Well, I think there's a few insights. So first of all, the fact that you can't rely purely or even largely on self-play,
*  that you really have to have an understanding of how humans approach the game.
*  I think that that's one of the major conclusions that I'm drawing from this work and that is, I think, applicable more broadly to a lot of different games.
*  So we've actually already taken the approaches that we've used in diplomacy and tried them on a cooperative card game called Hanabi.
*  And we've had a lot of success in that game as well.
*  On the language side, I think the fact that we were able to control the language model through this intense approach was very effective.
*  And it allowed us, instead of just imitating how humans would communicate, we're able to go beyond that and able to feed into its superhuman strategies that it can then generate messages corresponding to.
*  Is there something you could say about detecting whether a person or AI is lying or not?
*  The bot doesn't explicitly try to calculate whether somebody is lying or not.
*  But what it will do is try to predict what actions they're going to take, given the communications, given the messages that they've sent to us.
*  So given our conversation, what do I think you're going to do?
*  And implicitly, there is a calculation about whether you're lying to me in that.
*  If you're based on your messages, if I think you're going to attack me this turn, even though your messages say that you're not, then essentially the bot is predicting that you're lying.
*  But it doesn't view it as lying the same way that we would view it as lying.
*  But you could probably reformulate with all the same data and make a classifier lying or not.
*  Yeah, I think you could do that.
*  That was not something that we were focused on, but I think that it is possible that if you came up with some measurements of what does it mean to tell a lie, because there's a spectrum, right?
*  If you're withholding some information, is that a lie?
*  If you're mostly telling the truth, but you forgot to mention this one action out of 10, is that a lie?
*  It's hard to draw the line.
*  But if you're willing to do that, then you could possibly use it to...
*  This feels like an argument inside a relationship now, what constitutes a lie.
*  Depends what you mean by the definition of the word is.
*  OK, still it's fascinating because trust and lying is all intermixed into this and it's language models that are becoming more and more sophisticated.
*  It's just a fascinating space to explore.
*  What do you see as the future of this work that is inspired by the breakthrough performance that you're getting here with diplomacy?
*  I think there's a few different directions to take this work.
*  I think really what it's showing us is the potential that language models have.
*  I mean, I think a lot of people didn't think that this kind of result was possible even today, despite all the progress that's been made in language models.
*  And so it shows us how we can leverage the power of things like self-play on top of language models to get increasingly better performance.
*  And the ceiling is really much higher than what we have right now.
*  Is this transferable somehow to chatbots for the more general task of dialogue?
*  There is a kind of negotiation here, a dance between entities that are trying to cooperate and at the same time a little bit adversarial,
*  which I think maps somewhat to the general, you know, the entire process of Reddit or like internet communication.
*  You're cooperating, you're adversarial, you're having debates, you're having camaraderie, all that kind of stuff.
*  I think one of the things that's really useful about diplomacy is that we have a well-defined value function.
*  There is a well-defined score that the bot is trying to optimize.
*  And in a setting like a general chatbot setting, it would need that kind of objective in order to fully leverage the techniques that we've developed.
*  What about like what we talked about earlier with NPCs inside video games?
*  How can it be used to create for Elder Scrolls 6 more compelling NPCs that you could talk to instead of instead of committing all kinds of violence with a sword and fighting dragons,
*  just sit in a tavern and drink all day and talk to the chatbot?
*  The way that we've approached AI and diplomacy is you condition the language on an intent.
*  Now, that intent in diplomacy is an action, but it doesn't have to be.
*  And you can imagine you could have NPCs in video games or the metaverse or whatever where there's some intent or there's some objective that they're trying to maximize and you can specify what that is.
*  And then the language can correspond to that intent.
*  Now, I'm not saying that this is happening imminently, but I'm saying that this is like a future application potentially of this direction of research.
*  So what's the more general formulation of this?
*  Making self-play be able to scale the way self-play does and still maintain human-like behavior?
*  The way that we've approached self-play in diplomacy is like we're trying to come up with good intents to condition the language model on.
*  And the space of intents is actions that can be played in the game.
*  Now, there is like the potential to have a broader set of intents, things like long-term cooperation or long-term objectives or gossip about what another player was saying.
*  These are things that we're currently not conditioning the language model on.
*  And so it's not able to we're not able to control it to say, like, oh, you should be talking about this thing right now.
*  But it's quite possible that you could expand the scope of intents to be able to allow it to talk about those things.
*  Now, in the process of doing that, the self-play would become much more complicated.
*  And so that is a potential for future work.
*  OK, the increase in the number of intents.
*  I still am not quite clear how you keep the self-play integrated into the human world.
*  Yeah, I'm a little bit loose on understanding how you do that.
*  So we train in neural nets to imitate the human data as closely as possible.
*  And that's what we call the anchor policy.
*  And now we're doing self-play.
*  The problem with the anchor policy is that it's not a perfect approximation of how humans actually play because we don't have infinite data, because we don't have unlimited neural network capacity.
*  It's actually a relatively suboptimal approximation of how humans actually play.
*  And we can improve that approximation by adding planning and RL.
*  And so what we do is we get a better approximation, a better model of human play by during the self-play process.
*  We say you can deviate from this human anchor policy if there is an action that has particularly high expected value.
*  But it would have to be a really high expected value in order to deviate from this human like policy.
*  So you basically say, try to maximize your expected value while at the same time stay as close as possible to the human policy.
*  And there is a parameter that controls the relative weighting of those competing objectives.
*  So the question I have is how sophisticated can the anchor policy get?
*  So have a policy that approximates human behavior.
*  So as you increase the number of intents, as you generalize the space in which this is applicable,
*  and given that the human data is limited, try to anticipate a policy that works for in a much larger number of cases.
*  Like how difficult is the process of forming a damn good anchor policy?
*  Well, it really comes down to how much human data you have.
*  So it's all about scaling the human data.
*  I think the more human data you have, the better.
*  And I think that that's going to be the major bottleneck in scaling to more complicated domains.
*  But that said, there might be the potential, just like in the language model where we leveraged tons of data on the Internet and then specialized it for diplomacy.
*  There is the future potential that you can leverage huge amounts of data across the board and then specialize it in the data set that you have for diplomacy.
*  And in that way, you're essentially augmenting the amount of data that you have.
*  To what degree does this apply to the general, the real world diplomacy, the geopolitics?
*  You know, there's a game theory has a history of being applied to understand and to give us hope about nuclear weapons, for example.
*  The mutually assured destruction is a game theoretic concept that you can formulate.
*  Some people say it's oversimplified, but nevertheless, here we are and we somehow haven't blown ourselves up.
*  Do you see a future where this kind of this kind of system can be used to help us make decisions, geopolitical decisions in the world?
*  Well, like I said, the original motivation for the game of diplomacy was the failures of World War One, the diplomatic failures that led to war.
*  And the real take home message of diplomacy is that, you know, if people approach diplomacy the right way, then war is ultimately unsuccessful.
*  The way that I see it, war is an inherently negative sum game, right?
*  There's always a better outcome than war for all the parties involved.
*  And my hope is that, you know, as AI progresses, then maybe this technology could be used to help people make better decisions across the board and, you know, hopefully avoid negative sum outcomes like war.
*  Yeah, I mean, I just came back from Ukraine.
*  I'm going back there on deep personal levels.
*  Think a lot about how peace can be achieved.
*  And I'm a big believer in conversation, leaders getting together and having conversations and trying to understand each other.
*  Yeah, it's fascinating to think whether each one of those leaders can run a simulation ahead of time.
*  Like, if I'm an asshole, what are the possible consequences?
*  If I'm nice, what are the possible consequences?
*  My guess is that if the president of the United States got together with Vladimir Zelensky and Vladimir Putin, that there would be significant benefits to the president of the United States not having the ego of kind of playing down, of giving away a lot of chips for the future success of a world.
*  So giving a lot of power to the two presidents of the competing nations to achieve peace.
*  That's my guess. But it'd be nice to run a bunch of simulations.
*  But then you have to have human data, right?
*  You really because it's like the game of diplomacy is fundamentally different than geopolitics.
*  You need data. You need like, I guess that's the question I have.
*  Like, how transferable is this to like, I don't know, any kind of negotiation, right?
*  Like to any kind of some local, I don't know, a bunch of lawyers like arguing like a divorce, like divorce lawyers, like how transferable this all kinds of human negotiation?
*  Well, I feel like this isn't a question that's unique to diplomacy.
*  I mean, I think you look at RL breakthroughs, reinforcement learning breakthroughs in previous games as well, like, you know, AI for Starcraft, AI for Atari.
*  You haven't really seen it deployed in the real world because you have these problems of it's really hard to collect a lot of data and you don't have you don't have a well defined action space.
*  You don't have a well defined reward function.
*  These are all things that you really need for reinforcement learning and planning to be really successful today.
*  Now, there are some domains where you do have that code generation is one example theorem proving mathematics.
*  That's another example where you have a well defined action space, you have a well defined reward function.
*  And those are the kinds of domains where I can see RL in the short term being incredibly powerful.
*  But, yeah, I think that those are the barriers to deploying this at scale in the real world.
*  But the hope is that in the long run, we'll be able to get there.
*  Yeah, we see diplomacy feels like closer to the real world than does Starcraft, because it's natural language.
*  You're operating in the space of intense and in the space of natural language that feels very close to the real world.
*  And it also feels like you could get data on that from the Internet.
*  Yeah, and that's why I do think that diplomacy is taking a big step closer to the real world than anything that's came before in terms of game breakthroughs.
*  The fact that we're communicating in natural language, we're leveraging the fact that we have this general data set of dialogue and
*  communication from a breadth of the Internet.
*  That is a big step in that direction.
*  We're not 100 percent there, but we're getting closer at least.
*  So if we actually return back to poker and chess, are some of the ideas that you're learning here with diplomacy,
*  could you construct AI systems that play like humans, like make for a fun opponent in a game of chess?
*  Yeah, absolutely. We've already started looking into this direction a bit.
*  So we tried to use the techniques that we've developed for diplomacy to make chess and go AIs.
*  And what we found is that it led to much more human-like strong chess and go players.
*  The way that AIs like Stockfish today play is in a very inhuman style.
*  It's very strong, but it's very different from how humans play.
*  And so we can take the techniques that we've developed for diplomacy.
*  We do something similar in chess and go, and we end up with a bot that's both strong and human-like.
*  To elaborate on this a bit, one way to approach making a human-like AI for chess is to collect a bunch of human games,
*  like a bunch of human Grandmaster games, and just to supervise learning on those games.
*  But the problem is that if you do that, what you end up with is an AI that's substantially weaker than the human Grandmasters that you trained on.
*  Because the neural net is not able to approximate the nuance of the strategy.
*  This goes back to the planning thing that I mentioned, the search thing that I talked about before,
*  that these human Grandmasters, when they're playing, they're using search and they're using planning.
*  And the neural net alone, unless you have a massive neural net that's like a thousand times bigger than what we have right now,
*  it's not able to approximate those details very effectively.
*  And on the other hand, you can leverage search and planning very heavily.
*  But then what you end up with is an AI that plays in a very different style from how humans play the game.
*  Now, if you strike this intermediate balance by setting the regularization parameters correctly and say you can do planning,
*  but try to keep it close to the human policy, then you end up with an AI that plays in both a very human-like style
*  and a very strong style.
*  And you can actually even tune it to have a certain ELO rating.
*  So you can say play in the style of like a 2,800 ELO human.
*  I wonder if you could do specific type of humans or categories of humans.
*  So not just skill, but style.
*  Yeah, I think so.
*  And so this is where the research gets interesting.
*  Like, you know, one of the things that I was thinking about is, and this is actually already being done,
*  there's a researcher at the University of Toronto that's working on this,
*  is to make an AI that plays in the style of a particular player, like Magnus Carlsen, for example.
*  You can make an AI that plays like Magnus Carlsen.
*  And then where I think this gets interesting is like maybe you're up against Magnus Carlsen in the World Championship or something.
*  You can play against this Magnus Carlsen bot to prepare against the real Magnus Carlsen.
*  And you can try to explore strategies that he might struggle with and try to figure out,
*  like, how do you beat this player in particular?
*  On the other hand, you can also have Magnus Carlsen working with this bot to try to figure out where he's weak and where he needs to improve his strategy.
*  And so I can envision this future where data on specific chess and Go players becomes extremely valuable
*  because you can use that data to create specific models of how these particular players play.
*  So increasingly human-like behavior in bots, however, as you've mentioned, makes cheating, cheat detection much harder.
*  It does, yeah. The way that cheat detection works in a game like poker and a game like chess and Go, from what I understand,
*  is trying to see, like, is this person making moves that are very common among chess AIs, or, you know, AIs in general,
*  but very uncommon among top human players.
*  And if you have the development of these AIs that play in a very strong style, but also a very human-like style,
*  then that poses serious challenges for cheat detection.
*  And it makes you now ask yourself a hard question about what is the role of AI systems as they become more and more integrated in our society.
*  And this kind of human AI integration has some deep ethical issues that we should be aware of.
*  And also it's a kind of cybersecurity challenge, right?
*  To make, you know, one of the assumptions we have when we play games is that there's a trust that it's only humans involved.
*  And there, the better AI systems we create, which makes it super exciting,
*  human-like AI systems with different styles of humans is really exciting, but then we have to have the defenses better and better and better.
*  If we're to trust that we can enjoy human versus human game in a deeply fair way.
*  It's fascinating. It's just it's humbling.
*  Yeah, I think there is a lot of negative potential for this kind of technology.
*  But, you know, at the same time, there's a lot of upside for it as well.
*  So, you know, for example, right now, it's really hard to learn how to get better in games like chess and poker and go,
*  because the way that the AI plays is so foreign and incomprehensible.
*  But if you have these AIs that are playing, you know, you can say like, oh, I'm a 2000 Elo human.
*  How do I get to 2200?
*  Now you can have an AI that plays in the style of a 2200 Elo human, and that will help you get better.
*  Or, you know, you mentioned this problem of like, how do you know that you're actually playing with humans when you're playing like online in video games?
*  Well, now we have the potential of populating these like virtual worlds with agents, like AI agents that are actually fun to play with.
*  And you don't have to always be playing with other humans to, you know, have a fun time.
*  So, yeah, a lot of upside potential, too.
*  And I think, you know, with any sort of tool, there's the potential for a lot of greatness and a lot of downsides as well.
*  So in the paper, they got a chance to look at there's a section on ethical considerations.
*  What's in that section? What are some ethical considerations here?
*  Is it some of the stuff we already talked about?
*  There's some things that we've already talked about, I think, specific to diplomacy.
*  You know, there's also the challenge that the game is, you know, there is a deception aspect to the game.
*  And so, you know, developing language models that are capable of deception is, I think, a dicey issue and something that, you know, makes research on diplomacy particularly challenging.
*  And, you know, so those kinds of issues of like, should we even be developing AIs that are capable of lying to people?
*  That's something that we have to, you know, think carefully about.
*  That's so cool. I mean, you have to do that kind of stuff in order to figure out where the ethical lines are.
*  But I can see in the future it being illegal to have a consumer product that lies.
*  Yeah, yeah.
*  Like your personal assistant AI system is not allowed.
*  It's always have to tell the truth.
*  But if I ask it, do I do I look did I get fatter over the past month?
*  I sure as hell want that AI system to lie to me.
*  So there's a trade off between lying and being and being nice.
*  We have to somehow find where's the ethics in that?
*  And we're back to discussions inside relationships.
*  Anyway, what were you saying?
*  I was saying like, yeah, that's kind of going to the question of like, what is a lie?
*  You know, is a white lie a bad lie?
*  Is it an ethical lie?
*  You know, those kinds of questions.
*  Boy, we return time and time again to deep human questions as we design AI systems.
*  That's exactly what they do.
*  They put a mirror to humanity to help us understand ourselves.
*  There's also the issue of like, you know, in these diplomacy experiments in order to do a fair comparison.
*  You know, what we found is that there's an inherent anti AI bias in these kinds of games.
*  So we actually played a tournament in a non-language version of the game where, you know, we told the participants like, hey, in every single game, there's going to be an AI.
*  And what we found is that the humans would spend basically the entire game, like trying to figure out who the bot was.
*  And then as soon as they thought they figured it out, they would all team up and try to kill it.
*  And, you know, overcoming that inherent anti AI bias is a challenge.
*  On the flip side, I think when robots become the enemy, that's when we get to heal our human divisions and then we can become one.
*  As long as we have one enemy, it's that Reagan thing.
*  When the aliens show up, that's when we put our side, our divisions will become one human species.
*  We might have our differences, but we're at least all human.
*  At least we all hate the robots. No, no, no.
*  I think there will be actually in the future something like a civil rights movement for robots.
*  I think that's the fascinating thing about AI systems is they ask, they force us to ask about ethical questions about what is sentience?
*  How do we feel about systems that are capable of displaying suffering?
*  And how do we design products that show emotion and not?
*  How do we feel about that? Lying is another topic.
*  Are we going to allow bots to lie and not?
*  And where's the balance between being nice and telling the truth?
*  I mean, these are all fascinating human questions.
*  It's like so exciting to be in the century where we create systems that take these philosophical questions that have been asked for centuries and now we can engineer them inside systems where you really have to answer them because you'll have.
*  Transformational impact on human society, depending on what you design inside those systems.
*  It's fascinating. And like you said, I feel like diplomacy is a step towards the direction of the real world applying these are all methods towards the real world from from from all the breakthrough performances in Go and chess and StarCraft and Dota.
*  This is this feels like the real world, especially now my mind's been on war and military conflict.
*  This feels like it can give us some deep insights about human behavior at the large geopolitical scale.
*  What do you think?
*  Is the breakthrough?
*  Or.
*  The directions of work that will take us towards solving intelligence towards creating a GI systems.
*  You've been a part of creating, by the way, we should say a part of great teams that do this of creating systems that achieve breakthrough performances on before thought unsolvable problems.
*  Like poker, multiplayer poker, diplomacy.
*  We're taking steps towards that direction.
*  What do you think it takes to go all the way to create superhuman level intelligence?
*  You know, there's a lot of people trying to figure that out right now.
*  And, you know, I should say, like the amount of progress that's been made, especially in the past few years, is truly phenomenal.
*  I mean, you look at where AI was 10 years ago and the idea that you can have a eyes that can generate language and generate images the way they're doing today.
*  And able to play a game like diplomacy was just like unthinkable even even five years ago, let alone 10 years ago.
*  Now, there are aspects of AI that I think are still lacking.
*  I think there's general agreements that one of the major issues with AI today is that it's very data inefficient.
*  It's very it requires a huge number of samples of training examples to be able to train.
*  You know, you look at an AI that plays Go and it needs millions of games of Go to to learn how to play the game well.
*  Whereas a human can pick it up and like, you know, I don't know how many games as a human go player, go grandmaster playing their lifetime, probably, you know, in the thousands or tens of thousands, I guess.
*  So that's that's one issue.
*  Overcoming data efficiency.
*  Overcoming this challenge of data efficiency.
*  And this is particularly important if we want to deploy AI systems in real world settings where they're interacting with humans, because, you know, for example, with robotics, it's really hard to generate a huge number of samples.
*  It's a different story when you're working in these, you know, totally virtual games where you can play a million games and it's no big deal.
*  I was planning on just launching like a thousand of these robots in Austin.
*  I don't think it's illegal for legged robots to roam the streets and just collect data.
*  That's not a crazy idea.
*  What's the worst that could happen?
*  Yeah, I mean, that's one way to overcome the data efficiency problem.
*  It's like scale it.
*  Yeah.
*  Like I actually tried to see if there's a law against robots like legged robots just operating in the streets of a major city and there isn't I couldn't find any.
*  So I'll take it all the way to the Supreme Court.
*  Robot rights.
*  OK, anyway, sorry, you were saying so.
*  So what are the ideas for getting becoming more data efficient?
*  I mean, that's that's the trillion dollar question in AI today.
*  I mean, if you can figure out how to make AI systems more more data efficient, then that's a huge breakthrough.
*  So nobody really knows right now.
*  It could be just a gigantic background model language model.
*  And then you do the training becomes like prompting that model to to essentially do a kind of querying a search into the space of the things that's learned to customize that to whatever problem you're trying to solve.
*  So maybe if you form a large enough language model, you can go quite quite a long way that, you know, I think there's some truth to that.
*  I mean, you look at the way humans approach a game like poker.
*  They're not coming at it from scratch.
*  They're coming at it with a huge amount of background knowledge about, you know, how humans work, how the world works, the idea of money.
*  So they're able to leverage that kind of information to to pick up the game faster.
*  So it's not really a fair comparison to then compare it to an AI that's like learning from scratch.
*  And maybe one of the ways that we address this sample complexity problem is by allowing AIs to leverage that general knowledge across a ton of different domains.
*  So, like I said, you did a lot of incredible work in the space of research and actually building systems.
*  What advice would you give to let's start with beginners?
*  What advice would you give to beginners interested in machine learning?
*  Just at the very start of their journey in their in high school and college, thinking like this seems like a fascinating world.
*  What advice would you give them?
*  I would say that there are a lot of people working on similar aspects of machine learning and to not be afraid to try something a bit different.
*  My own path in AI is pretty atypical for a machine learning researcher today.
*  I mean, I started out working on game theory and then shifting more towards reinforcement learning as time went on.
*  And that actually had a lot of benefits, I think, because it allowed me to look at these problems in a very different way from the way a lot of machine learning researchers view it.
*  And that comes with drawbacks in some respects.
*  Like, I think there's definitely aspects of machine learning where I'm weaker than most of the researchers out there.
*  But I think that diversity of perspective, you know, when I'm working with my teammates, there's something that I'm bringing to the table and something that they're bringing to the table.
*  And that kind of collaboration becomes very fruitful for that reason.
*  So there could be problems like poker, like you've chosen diplomacy.
*  There could be problems like that still out there that you can just tackle, even if it seems extremely difficult.
*  I think that there's a lot of challenges left.
*  And I think having a diversity of viewpoints and backgrounds is really helpful for working together to figure out how to tackle those kinds of challenges.
*  So as a beginner, so that I would say that's that's more for like a grad student, where they already built up a base, like a complete beginner, what's a good journey.
*  So for you, that was doing some more on the math side of things, doing game theory, all that.
*  So it's basically build up a foundation in something.
*  So programming, mathematics, it could even be physics, but build that foundation.
*  Yeah, I would say build a strong foundation in math and computer science and statistics and these kinds of areas.
*  But but don't be afraid to try something that's different and learn something that's different from the thing that everybody else is doing to get into machine learning.
*  You know, there's there's value in having a different background than everybody else.
*  Yeah, so but certainly having a strong math background, especially in things like linear algebra and statistics and probability are incredibly helpful today for for learning about and understanding machine learning.
*  Do you think one day we'll be able to, since you're taking steps from poker to diplomacy, one day we'll be able to figure out how to live life optimally?
*  Well, what is it like in poker and diplomacy, you need a value function.
*  You need to have a reward system.
*  And so what does it mean to live a life that's optimal?
*  So OK, so then you can exactly like lay down a reward function being like, I want to be rich or I want to be I want to be in a happy relationship.
*  And then you'll say, well, do X.
*  Do X.
*  You know, there's there's a lot of talk today about in AI safety circles about like misspecification of, you know, reward functions.
*  So you you say like, OK, my objective is to be rich.
*  And maybe the AI tells you like, OK, well, if you want to maximize the probability that you're rich, go rob a bank.
*  Sure. And so you want to is that is that really what you want?
*  Is your objective really to be rich at all costs?
*  Or is it more nuanced than that?
*  So the unintended consequences.
*  Yeah. Yeah.
*  So yeah, that that's maybe life is more about defining the reward function that minimizes the unintended consequences than it is about the actual policy that gets you to the reward function.
*  Maybe life is just about constantly updating the reward function.
*  I think one of the challenges in life is figuring out exactly what that reward function is.
*  Sometimes it's pretty hard to specify the same way that, you know, trying to handcraft the optimal policy in a game like chess is really difficult.
*  It's not so clear cut what the reward function is for for life.
*  I think one day I will figure it out.
*  And I wonder what that would be until then.
*  I just really appreciate the kind of work you're doing.
*  And it's really fascinating taking a leap into a more and more real world like problem space and just achieving incredible results by applying reinforcement learning.
*  Now, since I saw your work on poker, you've been a constant inspiration.
*  It's an honor to get to finally talk to you.
*  And this is really fun.
*  Thanks for having me. Thanks for listening to this conversation with No Brown.
*  To support this podcast, please check out our sponsors in the description.
*  And now let me leave you with some words from Sun Tzu and the art of war.
*  The whole secret lies in confusing the enemy so that he cannot fathom our real intent.
*  Thank you for listening and hope to see you next time.

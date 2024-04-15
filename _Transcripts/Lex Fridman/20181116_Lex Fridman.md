---
Date Generated: April 14, 2024
Transcription Model: whisper medium 20231117
Length: 3242s
Video Keywords: []
Video Views: 72892
Video Rating: None
---

# Vladimir Vapnik: Statistical Learning | Lex Fridman Podcast #5
**Lex Fridman:** [November 16, 2018](https://www.youtube.com/watch?v=STFcvzoxVw4)
*  The following is a conversation with Vladimir Vapnik.
*  He's the co-inventor of the support vector machines, support vector clustering,
*  VC theory, and many foundational ideas in statistical learning.
*  He was born in the Soviet Union and worked at the Institute of Control Sciences in Moscow.
*  Then, in the United States, he worked at AT&T, NEC Labs, Facebook Research,
*  and now is a professor at Columbia University.
*  His work has been cited over 170,000 times.
*  He has some very interesting ideas about artificial intelligence and the nature of learning,
*  especially on the limits of our current approaches and the open problems in the field.
*  This conversation is part of MIT course on Artificial General Intelligence
*  and the Artificial Intelligence Podcast.
*  If you enjoy it, please subscribe on YouTube or rate it on iTunes or your podcast provider of choice,
*  or simply connect with me on Twitter or other social networks at Lex Friedman, spelled F-R-I-D.
*  And now, here's my conversation with Vladimir Vapnik.
*  Einstein famously said that God doesn't play dice.
*  Yeah.
*  You have studied the world through the eyes of statistics, so let me ask you in terms of the
*  nature of reality, fundamental nature of reality, does God play dice?
*  We don't know some factors.
*  Because we don't know some factors, which could be important.
*  It looks like God plays dice, but we should describe it.
*  In philosophy, they distinguish between two positions, positions of instrumentalism,
*  where you're creating theory for prediction, and position of realism,
*  where you're trying to understand what God did.
*  Can you describe instrumentalism and realism a little bit?
*  For example, if you have some mechanical laws, what is that?
*  Is it law which is true always and everywhere?
*  Or it is law which allows you to predict position of moving element?
*  What do you believe?
*  You believe that it is God's law, that God created the world, which obeyed to this
*  physical law?
*  Or it is just law for predictions?
*  And which one is instrumentalism?
*  For predictions.
*  If you believe that this is law of God, and it's always true everywhere,
*  that means that you're a realist.
*  You're trying to really understand the God's thought.
*  So the way you see the world is as an instrumentalist?
*  I'm working for some models, models of machine learning.
*  So in this model, we can see setting, and we try to solve, resolve the setting,
*  to solve the problem.
*  You can do it in two different ways, from the point of view of instrumentalism.
*  That's what everybody does now, because they say that the goal of machine learning
*  is to find the role for classification.
*  That is true, but it is an instrument for prediction.
*  But I can say the God of machine learning is to learn about conditional probability,
*  so how God played youth, and is he play, what is probability for one,
*  what is probability for another given situation.
*  But for prediction, I don't need this.
*  I need the role.
*  But for understanding, I need conditional probability.
*  So let me just step back a little bit first to talk about, you mentioned,
*  which I read last night, the parts of the 1960 paper by Eugene Wigner,
*  Unreasonable Effectiveness of Mathematics and Natural Sciences.
*  Such a beautiful paper, by the way.
*  Made me feel, to be honest, to confess my own work in the past few years on deep learning,
*  heavily applied, made me feel that I was missing out on some of the beauty of nature
*  in the way that math can uncover.
*  So let me just step away from the poetry of that for a second.
*  How do you see the role of math in your life?
*  Is it a tool?
*  Is it poetry?
*  Where does it sit?
*  And does math for you have limits of what it can describe?
*  Some people say that math is language which uses God.
*  So I believe…
*  Speak to God or use God?
*  Use God.
*  Use God.
*  Yeah.
*  So I believe that this article about effectiveness,
*  unreasonable effectiveness of math, is that if you're looking at mathematical structures,
*  they know something about reality.
*  And the most scientists from natural science, they're looking on equation
*  and trying to understand reality.
*  So the same in machine learning.
*  If you're trying very carefully to look on all equations which define conditional probability,
*  you can understand something about reality more than from your fantasy.
*  So math can reveal the simple underlying principles of reality perhaps?
*  You know what means simple?
*  It is very hard to discover them.
*  But then when you discover them and look at them, you see how beautiful they are.
*  And it is surprising why people did not see that before you're looking on equation
*  and derive it from equations.
*  For example, I talked yesterday about least square net.
*  And people have a lot of fantasy how to improve least square net.
*  But if you're going step by step by solving some equations, you suddenly will get some term
*  which after thinking, you understand that it describes position of observation point.
*  In least square method, we throw out a lot of information.
*  We don't look in composition of point of observations.
*  We're looking only on residuals.
*  But when you understood that, that's very simple idea.
*  But it's not too simple to understand.
*  And you can derive this just from equations.
*  So some simple algebra, a few steps will take you to something surprising that when you think about.
*  Absolutely, yes.
*  And that is proof that human intuition not to reach.
*  And very primitive.
*  And it does not see very simple situations.
*  So let me take a step back in general.
*  Yes.
*  But what about human as opposed to intuition, ingenuity, moments of brilliance?
*  So do you have to be so hard on human intuition?
*  Are there moments of brilliance in human intuition that can leap ahead of math?
*  And then the math will catch up?
*  I don't think so.
*  I think that the best human intuition, it is putting in axioms.
*  And then it is technical way.
*  See where the axioms take you.
*  Yeah.
*  But if they correctly take axioms.
*  But it axiom polished during generations of scientists.
*  And this is integral wisdom.
*  So that's beautifully put.
*  But if you maybe look at when you think of Einstein and special relativity,
*  what is the role of imagination coming first there?
*  In the moment of discovery of an idea.
*  So there's obviously a mix of math and out of the box imagination there.
*  That I don't know.
*  Whatever I did, I exclude any imagination.
*  Because whatever I saw in machine learning that come from imagination,
*  like features, like deep learning, they are not really one of the problem.
*  When you're looking very carefully from mathematical equations,
*  you're deriving very simple theory, which goes far beyond theoretically
*  than whatever people can imagine.
*  Because it is not good fantasy.
*  It is just interpretation.
*  It is just fantasy.
*  But it is not what you need.
*  You don't need any imagination to derive, say, the main principle of machine learning.
*  When you think about learning and intelligence,
*  maybe thinking about the human brain and trying to describe mathematically the process of learning,
*  that is something like what happens in the human brain.
*  Do you think we have the tools currently?
*  Do you think we will ever have the tools to try to describe that process of learning?
*  You...
*  It is not description what's going on.
*  It is interpretation.
*  It is your interpretation.
*  Your vision can be wrong.
*  You know, one guy invent microscope, Leven Guk, for the first time.
*  Only he got this instrument and nobody...
*  Or he kept secret about microscope.
*  But he wrote report in London Academy of Science.
*  And his report, when he looking at the blood, he looked everywhere, on the water, on the blood,
*  on the spleen.
*  But he described blood like fight between queen and king.
*  So he saw blood cells, red cells, and he imagined that it is army fighting each other.
*  And it was his interpretation of situation.
*  And he sent this report in Academy of Science.
*  They very carefully looked because they believed that he is right.
*  He saw something.
*  But he gave wrong interpretation.
*  And I believe the same can happen with brain.
*  With brain, yeah.
*  Because the most important part...
*  You know, I believe in human language.
*  In some proverb, is so much wisdom.
*  For example, people say that it is better than a thousand days of diligent studies one day
*  with great teacher.
*  But if I will ask you what teacher does, nobody knows.
*  And that is intelligence.
*  But we know from history and now from math and machine learning that teacher can do a lot.
*  So what, from a mathematical point of view, is the great teacher?
*  I don't know.
*  That's an open question.
*  I don't know.
*  But we can say what teacher can do.
*  He can introduce some invariants, some predicate for creating invariants.
*  How he doing it, I don't know.
*  Because teacher knows reality and can describe from this reality a predicate, invariants.
*  But he knows that when you're using invariant, he can decrease number of observations 100 times.
*  Maybe try to pull that apart a little bit.
*  I think you mentioned like a piano teacher saying to the student, play like a butterfly.
*  I played piano, I played guitar for a long time.
*  Maybe it's romantic, poetic.
*  But it feels like there's a lot of truth in that statement.
*  There is a lot of instruction in that statement.
*  And so can you pull that apart?
*  What is that?
*  The language itself may not contain this information.
*  It's not blah, blah, blah.
*  It does not blah, blah, blah.
*  It affects you.
*  It's what?
*  It affects you.
*  It affects your playing.
*  Yes, it does.
*  But it's not the language.
*  It feels like, what is the information being exchanged there?
*  What is the nature of information?
*  What is the representation of that information?
*  I believe that it is sort of predicate, but I don't know.
*  That is exactly what intelligence and machine learning should be.
*  Because the rest is just mathematical technique.
*  I think that what was discovered recently is that there is two mechanism of learning.
*  One called strong convergence mechanism and weak convergence mechanism.
*  Before people use only one convergence.
*  In weak convergence mechanism, you can use predicate.
*  That's what play like butterfly.
*  And it will immediately affect your playing.
*  You know, there is English proverb, great.
*  If it looks like a duck, swims like a duck, and quack like a duck, then it is probably duck.
*  Yes.
*  But this is exact about predicate.
*  Looks like a duck, what it means.
*  So you saw many ducks, that you're training data.
*  So you have description of how looks integral, looks ducks.
*  Yeah, the visual characteristics of a duck.
*  Yeah, but you want and you have model for recognition.
*  So you would like to the theoretical description from model coincide with empirical description,
*  which you saw on TEDx.
*  So about looks like a duck, it is general.
*  But what about swims like a duck?
*  You should know the duck swims.
*  You can't say it play chess like a duck.
*  Okay, duck doesn't play chess.
*  And it is completely legal predicate, but it is useless.
*  So half teacher can recognize not useless predicate.
*  So up to now, we don't use this predicate in existing machine learning.
*  And you think that's so exact.
*  So why we need zillions of data?
*  But in this English proverb, they use only three predicate.
*  Looks like a duck, swims like a duck, and quack like a duck.
*  So you can't deny the fact that swims like a duck and quacks like a duck has humor in it,
*  has ambiguity.
*  Let's talk about swim like a duck.
*  It doesn't say jumps like a duck.
*  Why?
*  Because it's not relevant.
*  But that means that you know ducks, you know different birds, you know animals.
*  And you derive from this that it is relevant to say swim like a duck.
*  Underneath, in order for us to understand swims like a duck,
*  it feels like we need to know millions of other little pieces of information.
*  We pick up along the way.
*  You don't think so.
*  There doesn't need to be this knowledge base.
*  In those statements carries some rich information that helps us understand the essence of duck.
*  How far are we from integrating predicates?
*  You know that when you consider complete machine learning,
*  so what it does, you have a lot of functions.
*  And then you're talking, it looks like a duck.
*  You see your training data.
*  From training data, you recognize like expected duck should look.
*  Then you remove all functions which does not look like you think it should look from training date.
*  So you decrease amount of function from which you pick up one.
*  Then you give a second predicate and again decrease the set of function.
*  And after that you pick up the best function you can.
*  Fine, it is standard machine learning.
*  So why you need not too many examples?
*  Because your predicates aren't very good?
*  That means the predicate is very good.
*  Because every predicate is invented to decrease admissible set of function.
*  So you talk about admissible set of functions and you talk about good functions.
*  So what makes a good function?
*  So admissible set of function is set of function which has small capacity or small diversity,
*  small VC dimension.
*  Which contain good function inside.
*  By the way, for people who don't know, VC, you're the V in the VC.
*  How would you describe to a layperson what VC theory is?
*  How would you describe VC?
*  When you have a machine, so machine capable to pick up one function from the admissible set of function.
*  But set of admissible function can be big.
*  Say contain all continuous functions and it's useless.
*  You don't have so many examples to pick up function.
*  But it can be small.
*  Small, we call it capacity, but maybe better called diversity.
*  So not very different function in the set.
*  Infinite set of function, but not very diverse.
*  So it is small VC dimension.
*  When VC dimension is small, you need small amount of training data.
*  So the goal is to create admissible set of functions which have small VC dimension
*  and contain good function.
*  Then you should be able to pick up the function using small amount of observations.
*  So that is the task of learning.
*  Is creating a set of admissible functions that has a small VC dimension.
*  And then you figure out a clever way of picking up.
*  That is goal of learning, which I formulated yesterday.
*  Statistical learning theory does not involve in creating admissible set of function.
*  In classical learning theory, everywhere, 100% in textbook, the set of function,
*  admissible set of function is given.
*  But this is science about nothing because the most difficult problem to create admissible
*  set of functions, given say a lot of functions, continuous set of function.
*  Create admissible set of functions, that means that it has finite VC dimension,
*  small VC dimension and contain good function.
*  So this was out of consideration.
*  What's the process of doing that?
*  I mean, it's fascinating.
*  What is the process of creating this admissible set of functions?
*  That is invariant.
*  That's invariance.
*  Can you describe invariance?
*  You're looking of properties of training data.
*  And properties means that you have some function and you just count what is
*  average value of function on training data.
*  Then you have model and what is the expectation of this function on the model.
*  And they should coincide.
*  So the problem is about how to pick up functions.
*  It can be any function.
*  In fact, it is true for all functions.
*  But because when I talking set, say, duck does not jumping, so you don't ask question,
*  jump like a duck because it is trivially does not jumping and doesn't help you to
*  recognize jump.
*  But you know something, which question to ask and you asking if it swims like a duck.
*  But looks like a duck at this general situation.
*  Looks like, say, guy who has this illness, this disease, it is legal.
*  So there is a general type of predicate looks like and specific special type of predicate,
*  which related to this specific problem.
*  And that is intelligence part of all this business.
*  And that where teachers involved.
*  Incorporating the specialized predicates.
*  What do you think about deep learning as neural networks, these arbitrary architectures
*  as helping accomplish some of the tasks you are thinking about?
*  Their effectiveness or lack thereof?
*  What are the weaknesses and what are the possible strengths?
*  You know, I think that this is fantasy.
*  Everything which like deep learning, like features.
*  Let me give you this example.
*  One of the greatest book, this Churchill book about history of second world war.
*  And he starting this book describing that in all time when war is over, so the great
*  kings, they gathered together.
*  And most all of them were relatives.
*  And they discussed what should be done, how to create peace.
*  And they came to agreement.
*  And when happens first world war, the general public came in power.
*  And they were so greedy that robbed Germany.
*  And it was clear for everybody that it is not peace.
*  That peace will last only 20 years because they was not professionals.
*  And the same I see in machine learning.
*  There are mathematicians who looking for the problem from very deep point of view,
*  mathematical point of view.
*  And there are computer scientists who mostly does not know mathematics.
*  They just have interpretation of that.
*  And they invented a lot of blah, blah, blah interpretations like deep learning.
*  Why you did deep learning?
*  Mathematic does not know deep learning.
*  Mathematic does not know neurons.
*  It is just function.
*  If you like to say piecewise linear function, say that.
*  And do in class of piecewise linear function.
*  But they invent something.
*  And then they try to prove advantage of that through interpretations, which mostly wrong.
*  And when it is not enough, they appeal to brain which they know nothing about that.
*  Nobody knows what is going on in the brain.
*  So I think that more reliable look on math.
*  This is mathematical problem.
*  Do your best to solve this problem.
*  Try to understand that there is not only one way of convergence,
*  which is strong way of convergence.
*  There is a weak way of convergence, which requires predicate.
*  And if you will go through all this stuff, you will see that you don't need deep learning.
*  Even more, I would say one of the theorem which called the representative theorem.
*  It says that optimal solution of mathematical problem, which describe learning, is on shadow network.
*  Not on deep learning.
*  And shallow network.
*  Yeah.
*  Yeah.
*  The problem is there.
*  Absolutely.
*  So in the end, what you're saying is exactly right.
*  The question is you have no value for throwing something on the table, playing with it, not math.
*  So like in your network where you said throwing something in the bucket or the biological example
*  and looking at kings and queens with the cells or the microscope.
*  You don't see value in imagining the cells or kings and queens and using that as inspiration
*  and imagination for where the math will eventually lead you.
*  You think that interpretation basically deceives you in a way that's not productive.
*  I think that if you're trying to analyze this business of learning and especially discussion
*  about deep learning, it is discussion about interpretation, not about things
*  about what you can say about things.
*  That's right.
*  But aren't you surprised by the beauty of it?
*  So not mathematical beauty, but the fact that it works at all.
*  Or are you criticizing that very beauty, our human desire to interpret,
*  to find our silly interpretations in these constructs?
*  Let me ask you this.
*  Are you surprised and does it inspire you?
*  How do you feel about the success of a system like AlphaGo at beating the game of Go?
*  Using neural networks to estimate the quality of a board and the quality of the...
*  That is your interpretation, quality of the board.
*  Yeah, yes.
*  Yes.
*  It's not our interpretation.
*  The fact is a neural network system doesn't matter.
*  A learning system that we don't, I think, mathematically understand that well,
*  beats the best human player.
*  That's something that was thought impossible.
*  That means that it's not very difficult problem.
*  We've empirically have discovered that this is not a very difficult problem.
*  It's true.
*  So maybe it can argue.
*  Even more, I would say that if they use deep learning,
*  it is not the most effective way of learning theory.
*  Usually, when people use deep learning, they're using zillions of training data.
*  Yeah, but you don't need this.
*  So I describe challenge.
*  Can we do some problems which do well?
*  Deep learning method is deep net using 100 times less training data.
*  Even more, some problems deep learning cannot solve because it's not necessary.
*  They create admissible set of function.
*  To create deep architecture means to create admissible set of functions.
*  You cannot say that you're creating good admissible set of functions.
*  You're just, it's your fantasy.
*  It does not come from us.
*  But it is possible to create admissible set of functions because you have your training data.
*  Yeah.
*  Actually, for mathematicians, when you consider invariant, you need to use law of large numbers.
*  When you're making training in existing algorithm, you need uniform law of large numbers,
*  which is much more difficult.
*  It requires VC dimension and all this stuff.
*  But nevertheless, if you use both, weak and stroke way of convergence,
*  you can decrease a lot of training data.
*  You could do the three, the swims like a duck and quacks like a duck.
*  Let's step back and think about human intelligence in general.
*  Clearly, that has evolved in a non-mathematical way.
*  It wasn't, as far as we know, God or whoever didn't come up with a model
*  in place in our brain of admissible functions.
*  It kind of evolved.
*  I don't know.
*  Maybe you have a view on this.
*  So Alan Turing in the 50s in his paper asked and rejected the question,
*  can machines think?
*  It's not a very useful question.
*  But can you briefly entertain this useless question?
*  Can machines think?
*  So talk about intelligence and your view of it.
*  I don't know that.
*  I know that Turing described imitation.
*  If computer can imitate human being, let's call it intelligent.
*  He understands that it is not thinking computer.
*  Yes.
*  He completely understands what he's doing.
*  But he's set up a problem of imitation.
*  So now we understand that the problem is not an imitation.
*  I'm not sure that intelligence is just inside of us.
*  It may be also outside of us.
*  I have several observations.
*  So when I prove some theorem, it's a very difficult theorem.
*  In a couple of years, in several places, people prove the same theorem.
*  Say Sawyer-Lemma, after us was done, then another guy proves the same theorem.
*  In the history of science, it's happened all the time.
*  For example, geometry.
*  It's happened simultaneously.
*  First did Lobachevsky and then Gauss and Boyayi and then other guys.
*  And it's approximately in 10 times period, 10 years period of time.
*  I saw a lot of examples like that.
*  Many mathematicians think that when they develop something,
*  they develop something in general which affects everybody.
*  So maybe our models of intelligence only inside of us is incorrect.
*  It's our interpretation.
*  It may be there exists some connection with world intelligence.
*  I don't know.
*  You're almost like plugging in into…
*  Yeah, exactly.
*  And contributing to this…
*  Into a big network.
*  Maybe in your own network.
*  On the flip side of that, maybe you can comment on big O complexity
*  and how you see classifying algorithms by worst-case running time
*  in relation to their input.
*  So that way of thinking about functions.
*  Do you think P equals NP?
*  Do you think that's an interesting question?
*  Yeah, it is an interesting question.
*  But let me talk about complexity in about worst-case scenario.
*  There is a mathematical setting.
*  When I came to United States in 1991, people did not know.
*  This is a theory they did not know, statistical learning.
*  So in Russia, it was published two monographs, our monographs,
*  but in America, they did not know.
*  Then they learned.
*  And somebody told me that if it's worst-case theory,
*  then they will create real-case theory.
*  But till now, it did not.
*  Because it is mathematical too.
*  You can do only what you can do using mathematics,
*  and which has a clear understanding and clear description.
*  And for this reason, we introduce complexity.
*  And we need this because using, actually, it is diversity.
*  Like this one more, you see the mention, you can prove some theorems.
*  But we also create theory for case when you know probability measure.
*  And that is the best case which can happen.
*  It is entropy theory.
*  So from a mathematical point of view, you know the best possible case
*  and the worst possible case.
*  You can derive different model in medium.
*  But it's not so interesting.
*  And you think the edges are interesting?
*  The edges are interesting because it is not so easy to get good bound, exact bound.
*  It's not many cases where you have the bound is not exact.
*  But interesting principles which discover the mass.
*  Do you think it's interesting because it's challenging
*  and reveals interesting principles that allow you to get those bounds?
*  Or do you think it's interesting because it's actually very useful
*  for understanding the essence of a function of an algorithm?
*  So it's like me judging your life as a human being
*  by the worst thing you did and the best thing you did,
*  versus all the stuff in the middle.
*  It seems not productive.
*  I don't think so because you cannot describe situation in the middle.
*  Or it will be not general.
*  So you can describe edges cases.
*  And it is clear it has some model.
*  But you cannot describe model for every new case.
*  So you will be never accurate when you're using model.
*  But from a statistical point of view, the way you've studied functions
*  and the nature of learning and the world,
*  don't you think that the real world has a very long tail?
*  That the edge cases are very far away from the mean?
*  The mean?
*  The stuff in the middle?
*  Or no?
*  I don't know that.
*  I think that...
*  From my point of view, if you will use formal statistic,
*  you need uniform law of large numbers.
*  If you will use this invariance business,
*  you will need just law of large numbers.
*  And there's a huge difference between uniform law of large numbers and large numbers.
*  Is it useful to describe that a little more?
*  Or should we just take it to...
*  For example, when I'm talking about DAC,
*  I gave three predicates and it was enough.
*  But if you will try to do formal distinguish,
*  you will need a lot of observation.
*  I got you.
*  So that means that information about looks like a DAC
*  contain a lot of bit of information, formal bits of information.
*  So we don't know that, how much bit of information
*  we don't know that how much bit of information
*  contain things from artificial, from intelligence.
*  And that is the subject of analysis.
*  Till now, all business, I don't like how people consider artificial intelligence.
*  They consider as some codes which imitate activity of human being.
*  It is not science.
*  It is applications.
*  You would like to imitate go ahead.
*  It is very useful and good problem.
*  But you need to learn something more.
*  How people try to do, how people can to develop,
*  say predicate swims like a duck or play like butterfly or something like that.
*  They're not the teacher says you how it came in his mind.
*  How he chooses this image.
*  So that process is problem of intelligence.
*  That is the problem of intelligence.
*  And you see that connected to the problem of learning?
*  Absolutely.
*  Are they?
*  Because you immediately give this predicate like specific predicate swims like a duck
*  or quack like a duck.
*  It was chosen somehow.
*  So what is the line of work would you say?
*  If you were to formulate as a set of open problems,
*  that will take us there.
*  Will it play like a butterfly?
*  Will get a system to be able to...
*  Let's separate two stories.
*  One mathematical story that if you have predicate, you can do something.
*  And another story you have to get predicate.
*  It is intelligence problem and people even did not start to understand intelligence.
*  Because to understand intelligence, first of all, try to understand what doing teachers.
*  How teacher teach.
*  Why one teacher better than another one?
*  Yeah.
*  So you think we really even haven't started on the journey of generating the predicates?
*  No.
*  We don't understand.
*  We even don't understand that this problem exists.
*  Because did you hear?
*  You do.
*  No, I just know name.
*  I want to understand why one teacher better than another.
*  And how affect teacher, student.
*  It is not because he repeating the problem which is in textbook.
*  He makes some remarks.
*  He makes some philosophy of reasoning.
*  You know, that's a beautiful...
*  So it is a formulation of a question that is the open problem.
*  Why is one teacher better than another?
*  Right.
*  What he does better.
*  Yeah.
*  Why in every level?
*  How do they get better?
*  What does it mean to be better?
*  The whole...
*  Yeah.
*  The whole...
*  Yeah.
*  From whatever model I have, one teacher can give a very good predicate.
*  One teacher can say swims like a dog and another can say jump like a dog.
*  And jump like a dog carries zero information.
*  Yeah.
*  So what is the most exciting problem in statistical learning you've ever worked on
*  or are working on now?
*  I just finished this invariant story.
*  And I'm happy that I believe that it is ultimate learning story.
*  At least I can show that there are no another mechanism, only two mechanisms.
*  But they separate statistical part from intelligent part.
*  And I know nothing about intelligent part.
*  And if we will know this intelligent part, so it will help us a lot in teaching, in learning.
*  In learning.
*  Yeah.
*  You don't well know it when we see it?
*  So for example, in my talk, the last slide was a challenge.
*  So you have, say, NIST digital recognition problem.
*  And deep learning claims that they did it very well, say 99.5% of correct answers.
*  But they use 60,000 observations.
*  Can you do the same using 100 times less?
*  But incorporating invariants, what it means, you know, digit one, two, three.
*  Yeah.
*  Just looking at that.
*  Explain me which invariant I should keep.
*  To use 100 examples or say 100 times less examples to do the same job.
*  Yeah, that last slide in, unfortunately, your talk ended quickly, but that last slide was
*  a powerful open challenge in a formulation of the essence here.
*  That is exact problem of intelligence.
*  Because everybody, when machine learning started, it was developed by mathematicians,
*  they immediately recognized that we use much more training data than humans needed.
*  But now again, we came to the same story.
*  How to decrease.
*  That is the problem of learning.
*  It is not like in deep learning, they use zillions of training data.
*  Because maybe zillions are not enough if you have a good invariant.
*  Maybe you will never collect some number of observations.
*  But now it is a question to intelligence.
*  How to do that?
*  Because statistical part is ready.
*  As soon as you supply us with predicate, we can do a good job with small amount of observations.
*  The very first challenges will know digit recognition.
*  And you know digits.
*  And please tell me invariants.
*  I think about that, I can say.
*  For digit three, I would introduce concept of horizontal symmetry.
*  So the digit three has horizontal symmetry, say more than digit two or something like that.
*  But as soon as I get the idea of horizontal symmetry, I can mathematically invent a lot of
*  measure of horizontal symmetry.
*  Or then vertical symmetry or diagonal symmetry, whatever, if I have idea of symmetry.
*  But what else?
*  Yes.
*  Looking on digit, I see that it is meta predicate, which is not shape.
*  It is something like symmetry, like how dark is whole picture, something like that.
*  Which can self-rise a predicate.
*  You think such a predicate could rise?
*  It is out of something that is not general.
*  Meaning, it feels like for me to be able to understand the difference between a two and a three.
*  I would need to have had a childhood of 10 to 15 years playing with kids, going to school,
*  being yelled by parents, all of that, walking, jumping, looking at ducks.
*  And now then I would be able to generate the right predicate for telling the difference
*  between two and a three.
*  Or do you think there's a more efficient way?
*  I don't know.
*  I know for sure that you must know something more than digits.
*  Yes.
*  And that's a powerful state.
*  And that's a powerful state.
*  Yeah.
*  But maybe there are several languages of description, these elements of digits.
*  So I'm talking about symmetry, about some properties of geometry.
*  I'm talking about something abstract.
*  I don't know that.
*  But this is a problem of intelligence.
*  So in one of our articles, it is trivial to show that every example can carry not more than one
*  bit of information in real.
*  Because when you show example and you say this is one, you can remove, say, a function which
*  does not tell you one.
*  Say it's the best strategy.
*  If you can do it perfectly, it's remove half of the functions.
*  But when you use one predicate, which looks like a duck, you can remove much more functions
*  than half.
*  And that means that it contains a lot of bit of information from a formal point of view.
*  But when you have a general picture of what you want to recognize, a general picture of
*  the world, can you invent this predicate?
*  And that predicate carries a lot of information.
*  Beautifully put.
*  Maybe just me, but in all the math you show, in your work, which is some of the most profound
*  mathematical work in the field of learning AI and just math in general, I hear a lot of poetry
*  and philosophy.
*  You really kind of talk about philosophy of science.
*  There's a poetry and music to a lot of the work you're doing and the way you're thinking
*  about it.
*  So do you, where does that come from?
*  Do you escape to poetry?
*  Do you escape to music or not?
*  I think that there exists ground truth.
*  There exists ground truth.
*  Yeah.
*  And that can be seen everywhere.
*  The smart guy, philosopher, sometimes I surprised how they deep see.
*  Sometimes I see that some of them are completely out of subject.
*  But the ground truth, I see music.
*  Music is the ground truth?
*  Yeah.
*  And in poetry, in many poets, they believe that they take dictation.
*  So what piece of music, as a piece of empirical evidence, gave you a sense that they are
*  touching something in the ground truth?
*  It is structure.
*  The structure of it.
*  Yeah, because when you're listening to Bach, you see the structure.
*  Very clear, very classic, very simple.
*  And the same in Bach, when you have axioms in geometry, you have the same feeling.
*  And in poetry, sometimes you see the same.
*  Yeah.
*  And if you look back at your childhood, you grew up in Russia.
*  You maybe were born as a researcher in Russia.
*  You've developed as a researcher in Russia.
*  You came to the United States and a few places.
*  If you look back, what were some of your happiest moments as a researcher?
*  Some of the most profound moments, not in terms of their impact on society,
*  but in terms of their impact on how damn good you feel that day and you remember that moment.
*  You know, every time when you found something, it is great.
*  And one of the things in life.
*  Every simple thing.
*  Just even...
*  My general feeling is that most of my time was wrong.
*  You should go again and again and again and try to be honest in front of yourself.
*  Not to make interpretation, but try to understand that it related to grand truth.
*  It is not my blah, blah, blah interpretation and something like that.
*  But you're allowed to get excited at the possibility of discovery.
*  Oh, yeah.
*  You'll double, you have to double check it.
*  But...
*  No, but how it related to the other grand truths?
*  Is it just temporary or it is forever?
*  You know, you always have a feeling when you found something.
*  How big is that?
*  So 20 years ago when we discovered statistical learning theory, nobody believed.
*  Except for one guy, Dudley from MIT.
*  And then in 20 years it became fashion.
*  And the same with support vector machines.
*  That is kernel machines.
*  So with support vector machines and learning theory, when you were working on it,
*  you had a sense that you had a sense of the profundity of it, how that this seems to be right.
*  This seems to be powerful.
*  Right.
*  Absolutely.
*  Immediately.
*  I recognize that it will last forever.
*  And now when I found this invariant story.
*  You feel the same?
*  I have a feeling that it is complete learning.
*  Because I have proved that there are no different mechanisms.
*  You can have some, say, cosmetic improvement you can do.
*  But in terms of invariants, you need both invariants and statistical learning.
*  And they should work together.
*  But also I'm happy that we can formulate what is intelligence from that.
*  And to separate from technical part.
*  That is completely different.
*  Absolutely.
*  Well, Vladimir, thank you so much for talking today.
*  Thank you.
*  It's an honor.

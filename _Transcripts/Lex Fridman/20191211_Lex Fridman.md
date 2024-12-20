---
Date Generated: November 01, 2024
Transcription Model: whisper medium 20231117
Length: 4981s
Video Keywords: []
Video Views: 108377
Video Rating: None
Video Description: 
---

# Judea Pearl Causal Reasoning, Counterfactuals, and the Path to AGI  Lex Fridman Podcast #56
**Lex Fridman:** [December 11, 2019](https://www.youtube.com/watch?v=pEBI0vF45ic)
*  The following is a conversation with Judea Pearl, a professor at UCLA and a winner of the Touring
*  Award that is generally recognized as the Nobel Prize of Computing. He is one of the seminal
*  figures in the field of artificial intelligence, computer science, and statistics. He has developed
*  and championed probabilistic approaches to AI, including Beijing networks, and profound ideas
*  in causality in general. These ideas are important not just to AI, but to our understanding and
*  practice of science. But in the field of AI, the idea of causality, cause and effect, to many,
*  lie at the core of what is currently missing and what must be developed in order to build truly
*  intelligent systems. For this reason, and many others, his work is worth returning to often.
*  I recommend his most recent book called Book of Why that presents key ideas from a lifetime of
*  work in a way that is accessible to the general public. This is the Artificial Intelligence
*  Podcast. If you enjoy it, subscribe on YouTube, give it five stars on Apple Podcasts, support it
*  on Patreon, or simply connect with me on Twitter at Lex Friedman, spelled F-R-I-D-M-A-N. If you
*  leave a review on Apple Podcasts especially, but also Castbox or comment on YouTube,
*  consider mentioning topics, people, ideas, questions, quotes, and science, tech, and philosophy
*  that you find interesting. And I'll read them on this podcast. I won't call out names, but I love
*  comments with kindness and thoughtfulness in them, so I thought I'd share them with you.
*  Someone on YouTube highlighted a quote from the conversation with Noam Chomsky, where he said
*  the significance of your life is something you create. I like this line as well.
*  I recently started doing ads at the end of the introduction. I'll do one or two minutes after
*  introducing the episode and never any ads in the middle that break the flow of the conversation.
*  I hope that works for you and doesn't hurt the listening experience.
*  This show is presented by Cash App, the number one finance app in the App Store.
*  I personally use Cash App to send money to friends, but you can also use it to buy, sell,
*  and deposit Bitcoin in just seconds. Cash App also has a new investing feature. You can buy
*  fractions of a stock, say $1 worth, no matter what the stock price is. Broker services are provided
*  by Cash App Investing, a subsidiary of Square, a member of SIPC. I'm excited to be working with
*  Cash App to support one of my favorite organizations called First, best known for their First Robotics
*  and Lego competitions. They educate and inspire hundreds of thousands of students in over 110
*  countries and have a perfect rating and charity navigator, which means the donated money is used
*  to the maximum effectiveness. When you get Cash App from the App Store or Google Play and use code
*  LexPodcast, you'll get $10 and Cash App will also donate $10 to First, which again is an
*  organization that I've personally seen inspire girls and boys to dream of engineering a better
*  world. And now here's my conversation with Judea Pearl. You mentioned in an interview that science
*  is not a collection of facts by constant human struggle with the mysteries of nature. What was
*  the first mystery that you can recall that hooked you? Oh, the first mystery. That's a good one.
*  Yeah, I remember that. I had a fever for three days. When I learned about Descartes
*  analytic geometry, and I found out that you can do all the construction in geometry using algebra,
*  and I couldn't get over it. I simply couldn't get out of bed.
*  What kind of world does analytic geometry unlock? Well, it connects algebra with the geometry.
*  Okay, so Descartes had the idea that geometrical construction and geometrical theorems and
*  assumptions can be articulated in the language of algebra, which means that all the proof that
*  we did in high school, trying to prove that the three bisectors meet at one point and that, okay,
*  all this can be proven by just shuffling around notation. Yeah, that was a traumatic experience.
*  Traumatic experience? For me, it was. I'm telling you.
*  It's the connection between the different mathematical disciplines that they all-
*  Not between two different languages.
*  Languages. Yeah.
*  Which mathematic discipline is most beautiful? Is geometry it for you?
*  Both are beautiful. They have almost the same power.
*  But there's a visual element to geometry being-
*  Visually, it's more transparent. But once you get over to algebra, then a linear equation is
*  a straight line. This translation is easily absorbed. To pass a tangent to a circle,
*  you have the basic theorems, and you can do it with algebra. But the transition from one to another
*  was really, I thought that Descartes was the greatest mathematician of all times.
*  You have been at the, if you think of engineering and mathematics as a spectrum,
*  you have walked casually along this spectrum throughout your life. A little bit of engineering
*  and then done a little bit of mathematics here and there.
*  Not a little bit. We got a very solid background in mathematics because our teachers were geniuses.
*  Our teachers came from Germany in the 1930s, running away from Hitler.
*  They left their careers in Heidelberg and Berlin and came to teach high school in Israel.
*  We were the beneficiary of that experiment. They taught us math in a good way.
*  What's a good way to teach math?
*  The people. The people behind the theorems. Their cousins and their nieces and their faces.
*  How they jumped from the bathtub when they screamed Eureka and ran naked in town.
*  So you're almost educated as a historian of math.
*  No, we just got a glimpse of that history together with the theorem.
*  So every exercise in math was connected with the person and the time of the person.
*  The period.
*  The period also mathematically speaking.
*  Mathematically speaking, yes. Not the politics.
*  And then in university, you have gone on to do engineering.
*  Yeah. I got a B.S. in engineering and a tech neon.
*  Right. And then I moved here for graduate work and I got to do engineering
*  in addition to physics in Rutgers. And it combined very nicely with my
*  thesis, which I did in RCA laboratories in superconductivity.
*  And then somehow thought to switch to almost computer science, software, even
*  even not switch, but long to become to get into software engineering a little bit.
*  Programming, if you can call it that in the 70s. So there's all these disciplines.
*  If you were to pick a favorite, what in terms of engineering and mathematics,
*  which path do you think has more beauty? Which path has more power?
*  It's hard to choose. I enjoy doing physics and even have a vortex named on my name.
*  So I have investment in immortality.
*  So what is a vortex? Vortex is in superconductivity.
*  In the superconductivity. If you have permanent current swirling around,
*  one way or the other, you can have a store one or zero for computer. That's what we worked on
*  in the 1960s in RCA. And I discovered a few nice phenomena with the vortices.
*  You push the move vortex. You can Google it. Right. I didn't know about it, but the physicist
*  picked up on my thesis on my PhD thesis and the, it becomes popular. I mean,
*  thin film superconductors became important for high temperature superconductors. So they call it
*  pearl vortex without my knowledge. I discovered only about 15 years ago.
*  You have footprints in all of the sciences. So let's talk about the universe a little bit.
*  Is the universe at the lowest level deterministic or stochastic in your amateur philosophy view?
*  Put another way. Does God play dice? Well, we know it is stochastic.
*  Right. Today, today we think it is stochastic. Yes. We think because we have the Heisenberg
*  uncertainty principle and we have some experiments to confirm that.
*  All we have is experiments to confirm it. We don't understand why.
*  Why is already- You wrote a book about why.
*  Why? Yeah. It's a puzzle. It's a puzzle that you have the dice flipping machine or God
*  and the result of the flipping propagated with the speed faster than the speed of light.
*  We can't explain it. Okay. So, but it's only governs microscopic phenomena.
*  So you don't think of quantum mechanics as useful for understanding the nature of reality?
*  No. Diversionary. So in your thinking, the world might as well be deterministic.
*  The world is deterministic and as far as the new one firing is concerned,
*  it is deterministic to first approximation. What about free will?
*  Free will is also a nice exercise. Free will is an illusion that we AI people are going to solve.
*  So what do you think once we solve it, that solution will look like?
*  Once we put it in the page. First of all, it will look like a machine. A machine that acts
*  as though it has free will. It communicates with other machines as though they have free will.
*  And you wouldn't be able to tell the difference between a machine that does
*  and machine that doesn't have free will. Okay. So the illusion, it propagates the
*  illusion of free will amongst the other machines. And faking it is having it.
*  Okay. That's what Turing test is all about. Faking intelligence is intelligent because it's not
*  easy to fake. It's very hard to fake and you can only fake if you have it.
*  Yeah. So that's such a beautiful statement.
*  That's yeah, you could, yeah. Yeah. You can't fake it if you don't have it. Yeah.
*  So let's begin at the beginning with probability, both philosophically and mathematically. What
*  does it mean to say the probability of something happening is 50%? What is probability?
*  It's a degree of uncertainty that an agent has about the world.
*  You're still expressing some knowledge in that statement. Of course. The probability is 90%.
*  It's absolutely a different kind of knowledge than if it is 10%.
*  But it's still not solid knowledge. It's still solid knowledge. But hey, if you tell me that
*  90% assurance smoking will give you lung cancer in five years versus 10%, it's a piece of
*  useful knowledge. So the statistical view of the universe, why is it useful? So we're
*  swimming in complete uncertainty. Most of everything. It allows you to predict things
*  with a certain probability. And computing those probabilities are very useful. That's the whole
*  idea of prediction. And you need prediction to be able to survive. If you can't predict the future,
*  then you're just crossing the street will be extremely fearful. And so you've done a lot of
*  work in causation. And so let's think about correlation. I started with the probability.
*  You started with probability. You've invented the Bayesian networks. And so we'll dance back and
*  forth between these levels of uncertainty. But what is correlation? What is it? So probability
*  is something happening, is something, but then there's a bunch of things happening.
*  And sometimes they happen together, sometimes not. They're independent or not. So how do you think
*  about correlation of things? Correlation occurs when two things vary together over a very long time
*  is one way of measuring it. Or when you have a bunch of variables that vary cohesively,
*  and then we call it, we have a correlation here. And usually when we think about correlation,
*  we really think causally. Things cannot be correlated unless there is a reason for them
*  to vary together. Why should they vary together? If they don't see each other,
*  why should they vary together? So underlying it somewhere is causation. Yes. Hidden in our intuition,
*  there is a notion of causation because we cannot grasp any other logic except causation.
*  And how does conditional probability differ from causation? So what is conditional probability?
*  Conditional probability, how things vary when one of them stays the same. Now, staying the same
*  means that I have chosen to look only at those incidents where the guy has the same value
*  as previous one. It's my choice as an experimenter. So things that are not correlated before
*  could become correlated. Like for instance, if I have two coins which are uncorrelated,
*  and I choose only those flippings experiments in which a bell rings, and a bell rings when at
*  least one of them is a tail, then suddenly I see correlation between the two coins.
*  Because I only look at the cases where the bell rang. You see, it's my design, with my ignorance
*  essentially. With my audacity to ignore certain incidents, I suddenly create
*  a correlation where it doesn't exist physically. Right. So you just outlined one of the flaws
*  of observing the world and trying to infer something from the myth about the world from
*  looking at the correlation. I don't look at it as a flaw. The world works like that.
*  But the flaws come if we try to impose causal logic on correlation, it doesn't work too well.
*  But that's exactly what we do. That has been the majority of science.
*  Majority of naive science. Statisticians know it. Statisticians know that if you
*  condition on a third variable, then you can destroy or create correlations among two other
*  variables. They know it. It's in the data. Right. Nothing surprising. That's why they all
*  dismiss the Simpson paradox. Ah, we know it. They don't know anything about it.
*  Well, there's disciplines like psychology where all the variables are hard to account for. And so
*  oftentimes there's a leap between correlation to causation. You're imposing. What do you mean,
*  leap? Who is trying to get causation from correlation? You're not proving causation,
*  but you're sort of discussing it. Implying, sort of hypothesizing with our ability to prove. Which
*  discipline you have in mind? I'll tell you if they are obsolete, or if they are outdated,
*  or they are about to get outdated. Oh, yes. Tell me which one you have. Well, psychology,
*  you know, what is SEM? No, no, I was thinking of applied psychology studying. For example,
*  we work with human behavior and semi-autonomous vehicles, how people behave and you have to
*  conduct these studies of people driving cars. Everything starts with a question. What is the
*  research question? What is the research question? The research question, do people fall asleep
*  when the car is driving itself? Do they fall asleep or do they tend to fall asleep more frequently?
*  More frequently. Then the car not driving. It's not driving itself. That's a good question. Okay.
*  And so you measure, you put people in the car because it's real world. You can't conduct an
*  experiment where you can control everything. Why can't you turn the automatic module on and off?
*  Because it's on road public. I mean, there's aspects to it that's unethical because it's
*  testing on public roads. So you can only use vehicle. They have to, the people, the drivers
*  themselves have to make that choice themselves. And so they regulate that. And so you just observe
*  when they drive it autonomously and when they don't. But maybe they turn it off when they
*  were very tired. Yeah, that kind of thing. But you don't know those variables. Okay, so that you have
*  now uncontrolled experiments. We call it observational study. And we form the correlation
*  that we have to infer causal relationship, whether it was the automatic piece that caused them to
*  fall asleep or, okay. So that is an issue that is about 120 years old. I should only go 100 years old.
*  Okay. And, oh, maybe it's not. Actually, I should say it's 2000 years old because we have this
*  experiment by Daniel, but the Babylonian king that wanted the exile, the people from Israel that were
*  taken in exile to Babylon to serve the king. He wanted to serve them king's food, which was meat.
*  And Daniel as a good Jew couldn't eat a non-kosher food. So he asked them to eat vegetarian food.
*  But the king overseer says, I'm sorry, but if the king sees that your performance falls below
*  the height of other kids, he's going to kill me. Daniel said, let's make an experiment.
*  Let's take four of us from Jerusalem. Okay. Give us vegetarian food. Let's take the other guys
*  to eat the king's food. And in about a week's time, we'll test our performance. And you know,
*  the answer, of course, he did the experiment and they were so much better than the others.
*  The kings nominated them to super position in his case. So it was the first experiment.
*  Yes. So there was a very simple, it's also the same research questions. We want to know vegetarian
*  food, assist or obstruct your mental ability. And okay, so that's the question is very old one.
*  Even the more critical said, if I could discover one cause of things, I would rather discuss one
*  cause and be a king of Persia. Okay. The task of discovering causes was in the mind of ancient
*  people from many, many years ago. But the mathematics of doing that was only developed in
*  the 1920s. So science has left us orphan. Okay. Science has not provided us with the mathematics
*  to capture the idea of X causes Y and Y does not cause X because all the equation of physics
*  are symmetrical algebraic. The equality sign goes both ways. Okay. Let's look at machine learning
*  machine learning today. If you look at deep neural networks, you can think of it as
*  kind of conditional probability estimators. Correct. Beautiful. So where did you say that?
*  Conditional probability estimators. None of the machine learning people clobbered you, attacked you.
*  Listen, most people, and this is why this today's conversation I think is interesting is
*  most people would agree with you. There's certain aspects that are just effective today,
*  but we're going to hit a wall and there's a lot of ideas. I think you're very right that we're
*  going to have to return to about causality and that it would be, let's try to explore it.
*  Let's even take a step back. You've invented Bayesian networks
*  that look awfully a lot like they express something like causation, but they don't,
*  not necessarily. So how do we turn Bayesian networks into expressing causation? How do we
*  build causal networks? This A causes B, B causes C. How do we start to infer that kind of thing?
*  We start asking ourselves questions. What are the factors that would determine the value of X?
*  X could be blood pressure, death, hunger. But these are hypotheses that we propose.
*  Hypotheses. Everything which has to do with causality comes from a theory.
*  The difference is only how you interrogate the theory in your mind.
*  So it still needs the human expert to propose.
*  Right. You need the human expert to specify the initial model. Initial model could be very
*  qualitative. Just who listens to whom? By whom listen to I mean one variable listen to the other.
*  So I say, okay, the tide is listening to the moon and not to the rustle crow.
*  This is our understanding of the world in which we live. Scientific understanding of reality.
*  We have to start there because if we don't know how to handle cause and effect relationship,
*  when we do have a model, and we certainly do not know how to handle it when we don't have a model.
*  So let's start first. In AI, slogan is representation first, discovery second.
*  If I give you all the information that you need, can you do anything useful with it?
*  That is the first representation. How do you represent it? I give you all the knowledge in the world.
*  How do you represent it? When you represent it, I ask you, can you infer X or Y or Z?
*  Can you answer certain queries? Is it complex? Is it polynomial? All the computer science exercises
*  we do once you give me a representation for my knowledge, then I give you the first representation.
*  Then you can ask me, now I understand how to represent things, how do I discover them?
*  It's a secondary thing.
*  So first of all, I should echo the statement that mathematics in the current,
*  much of the machine learning world has not considered causation that A causes B.
*  In anything, that seems like a non-obvious thing that you think we would have really acknowledged,
*  but we haven't. So we have to put that on the table. So knowledge, how hard is it to
*  create a knowledge from which to work?
*  In certain areas, it's easy because we have only four or five major variables.
*  An epidemiologist or an economist can put them down.
*  Minimum wage, unemployment, policy, X, Y, Z, and start collecting data and quantify the
*  parameters that were left unquantified with the initial knowledge. That's the
*  routine work that you find in experimental psychology, in economics, everywhere,
*  in the health science. That's a routine thing. But I should emphasize, you should start with
*  the research question. What do you want to estimate? Once you have that, you have to have
*  a language of expressing what you want to estimate. You think it's easy? No.
*  So we can talk about two things. I think one is how the science of causation is very useful for
*  answering certain questions. And then the other is how do we create intelligence systems
*  that need to reason with causation? So if my research question is how do I pick up this water
*  bottle from the table? All the knowledge is required to be able to do that. How do we construct
*  that knowledge base? Do we return back to the problem that we didn't solve in the 80s with
*  expert systems? Do we have to solve that problem of automated construction of knowledge?
*  You're talking about the task of eliciting knowledge from an expert.
*  Task of eliciting knowledge from an expert or the self-discovery of more knowledge,
*  more and more knowledge. So automating the building of knowledge as much as possible.
*  It's a different game in the causal domain because it's essentially the same thing. You have to start
*  with some knowledge and you're trying to enrich it. But you don't enrich it by asking for more
*  rules. You enrich it by asking for the data, to look at the data and quantifying and ask queries
*  that you couldn't answer when you started. You couldn't because the question is quite complex
*  and it's not within the capability of ordinary cognition, of ordinary person, ordinary expert
*  even to answer. So what kind of questions do you think we can start to answer? Even a simple one.
*  Suppose I start with the easy one. What's the effect of a drug on recovery? What is the aspirin
*  that caused my headache to be cured? Or what is the television program or the good news I received?
*  This is already a difficult question because it's find the cause from effect. The easy one is
*  find the effect from cause. That's right. So first you construct a model saying that this is an
*  important research question. This is an important question. I didn't construct a model yet. I just
*  said it's an important question. And the first exercise is express it mathematically. What do
*  you want to do? Like if I tell you what will be the effect of taking this drug? You have to say
*  that in mathematics. How do you say that? Can you write down the question? Not the answer.
*  I want to find the effect of the drug on my headache. Write it down. That's where the
*  do calculus comes in. Yes. The operator. What is the operator? The operator. That's just nice. It's
*  the difference between association and intervention. Very beautifully sort of constructed. So we have a
*  do operator. So the do calculus connected on the do operator itself connects the operation of doing
*  to something that we can see. Right. So as opposed to the purely observing, you're making
*  the choice to change a variable. That's what it expresses. And then the way that we interpret it,
*  and the mechanism by which we take your query and we translate it into something that we can work
*  with is by giving it semantics. Saying that you have a model of the world and you cut off all the
*  incoming arrow into X. And you're looking now in the modified mutilated model. You ask for the
*  probability of Y. That is interpretation of doing X. Because by doing things, you've liberated them
*  from all influences that acted upon them earlier. And you subject them to the tyranny of your muscles.
*  So you remove all the questions about causality by doing them. So you're not-
*  One level of questions. Answer questions about what will happen if you do things.
*  If you do. If you drink the coffee, if you take the aspirin. Right. So how do we get the,
*  once, how do we get the doing data? Now the question is, if we cannot run experiments,
*  right, then we have to rely on observational study. So first we could, sorry to interrupt,
*  we could run an experiment. Yeah. Where we do something, where we drink the coffee and
*  don't, and this, the operator allows you to sort of be systematic about expressing. To imagine
*  how the experiment will look like, even though we cannot physically and technologically conduct it.
*  I'll give you an example. What is the effect of blood pressure on mortality?
*  I cannot go down into your vein and change your blood pressure, but I can ask the question,
*  which means I can, if I have a model of your body, I can imagine the effect of your, how the
*  blood pressure change will affect your mortality. How I go into the model and I conduct this
*  surgery about the blood pressure, even though physically I can do, I cannot do it.
*  Let me ask the quantum mechanics question. Does the doing change the observation?
*  Meaning the surgery of changing the blood pressure is, I mean, no, the surgery is called
*  a very delicate, it's very, infinitely delicate, incisive and delicate, which means do means
*  do X means I'm going to touch only X, only X directly into X.
*  So that means that I change only things which depends on X by virtue of X changing,
*  but I don't depend things which are not dependent on X. Like I wouldn't change your sex or your age,
*  I just change your blood pressure.
*  So in the case of blood pressure, it may be difficult or impossible to construct such an experiment.
*  No, physically, yes, but hypothetically, no.
*  Hypothetically, no.
*  But hypothetically, no.
*  Hypothetically, no.
*  If we have a model, that is what the model is for. So you conduct surgeries on a model,
*  you take it apart, put it back, that's the idea of a model.
*  It's the idea of thinking counterfactually, imagining, and that's the idea of creativity.
*  So by constructing that model, you can start to infer if the blood pressure leads to mortality.
*  With increases or decreases?
*  I construct the model, I still cannot answer it. I have to see if I have enough information
*  in the model that would allow me to find out the effects of intervention from a
*  non-interventional study, from a hands-off study.
*  So what's needed?
*  You need to have assumptions about who affects whom.
*  If the graph had a certain property, the answer is yes, you can get it from observational study.
*  If the graph is too mushy, bushy, bushy, the answer is no, you cannot.
*  Then you need to find either different kinds of observation that you haven't considered,
*  or one experiment.
*  So basically, that puts a lot of pressure on you to encode wisdom into that graph.
*  Correct. But you don't have to encode more than what you know. God forbid. If you put,
*  like economists are doing this, identifying assumptions. They put assumptions, even if they
*  don't prevail in the world, they put assumptions so they can identify things.
*  But the problem is, yes, beautifully put, but the problem is you don't know what you don't know.
*  So you know what you don't know, because if you don't know, you say it's possible,
*  it's possible that X affects the traffic tomorrow.
*  It's possible. You put down an arrow which says it's possible. Every arrow in the graph
*  says it's possible.
*  So there's not a significant cost to adding arrows that...
*  The more arrow you add, the less likely you are to identify things from purely observational data.
*  So if the whole world is bushy, and everybody affects everybody else, the answer is,
*  you can answer it ahead of time. I cannot answer my query from observational data.
*  I have to go to experiments.
*  So you talk about machine learning as essentially learning by association,
*  or reasoning by association, and this due calculus is allowing for intervention.
*  I like that word, action. So you also talk about counterfactuals.
*  Yeah.
*  And trying to sort of understand the difference in counterfactuals and intervention,
*  first of all, what is counterfactuals and why are they useful?
*  Why are they especially useful as opposed to just reasoning what affect actions have?
*  But counterfactual contains what we normally call explanations.
*  Can you give an example of what kind of...
*  I tell you that acting one way affects something else. I didn't explain anything yet.
*  But if I ask you, was it the aspirin,
*  was it the aspirin that cured my headache? I'm asking for explanation. What cured my headache?
*  And putting a finger on aspirin provides explanation. It was aspirin.
*  It was responsible for your headache going away. If you didn't take the aspirin,
*  you will still have a headache.
*  So by saying, if I didn't take aspirin, I would have a headache,
*  you're thereby saying that aspirin is the thing that removes the headache.
*  But you have to have another important information. I took the aspirin and my headache is gone.
*  It's very important information. Now I'm reasoning backward. And I said, what is the aspirin?
*  Yeah. By considering what would have happened if everything else is the same,
*  but I didn't take aspirin. That's right. So you know that things took place.
*  Joe killed Shmo. And Shmo would be alive had John not used his gun.
*  So that is the counterfactual. It had a conflict here or clash between observed fact
*  that he did shoot. And the hypothetical predicate, which says, had he not shot,
*  you have a logical clash. They cannot exist together. That's the counterfactual.
*  And that is the source of our explanation of the idea of responsibility, regret, and free will.
*  Yeah. So it certainly seems that's the highest level of reasoning, right?
*  Yes. And physicists do it all the time. Who does it all the time?
*  Physicists. In every equation of physics, let's say you have a Hooke's law and you put
*  one kilogram on the spring and the spring is one meter. And you say, had this weight been two
*  kilograms, the spring would have been twice as long. It's no problem for physicists to say that,
*  except that mathematics is only in the form of equation, equating the weight, proportionality
*  constant, and the length of the string. So you don't have the asymmetry in the equation of physics,
*  although every physicist thinks counterfactually. Ask high school kids, had the weight been three
*  kilograms, what would be the length of the spring? They can answer it immediately because they do the
*  counterfactual processing in their mind and then they put it into algebraic equations and they
*  solve it. But a robot cannot do that. How do you make a robot learn these relationships?
*  Why you would learn? Suppose you tell him, can you do it? Before you go learning, you have to ask
*  yourself, suppose I give you all the information. Can the robot perform the task that I ask him to
*  perform? Can he reason and say, no, it wasn't the aspirin. It was the good news you received on the
*  phone. Right. Because well, unless the robot had a model, a causal model of the world.
*  I'm sorry I have to linger on this. But now we have to linger and we have to say, how do we do it?
*  How do we build? Yes. How do we build a causal model without a team of human experts running
*  around? Why don't you go to learning right away? You're too much involved with learning. Because
*  I like babies. Babies learn fast. I'm trying to figure out how they do it. Good. That's another
*  question. How do the babies come out with the counterfactual model of the world? And babies do
*  that. They know how to play with the, in the crib. They know which balls hits another one. And so
*  they learn it by playful manipulation of the world. Yes. They are simple world, involve only toys and
*  balls and chimes. But it's a, if you see it, it's a complex world. We take for granted. Yes. How
*  complex. And kids do it by playful manipulation plus parent guidance, pure wisdom. And hearsay.
*  Yeah. They meet each other. Can they say, you shouldn't have taken my toy. Right.
*  And they, these multiple sources of information, they're able to integrate.
*  So the challenge is about how to integrate, how to form these causal relationships from
*  different sources of data. Correct. So how, how, how much information is it to play?
*  How much causal information is required to be able to play in the crib with different objects?
*  I don't know. I haven't experimented with the crib. Okay. Not a crib. Picking up. It's a very
*  interesting. Manipulating physical objects on this very, opening the pages of a book, all the tasks,
*  physical manipulation tasks. Do you have a sense? Because my sense is the world is extremely
*  complicated. It's only complicated. I agree. And I don't know how to organize it because I've been
*  spoiled by easy problems such as cancer and death. First we have to start. No, but it's easy.
*  The reason you said that you have only 20 variables and they are just variables are not mechanics.
*  It's easy. You just put them on the graph and they, they, they speak to you.
*  And you, you're providing a methodology for, for letting them speak. Yeah. I'm working only
*  in the abstract. The abstract of knowledge in knowledge out data in between. Now can we take
*  a leap to trying to learn in this very, when it's not 20 variables, but 20 million variables,
*  trying to learn causation in this world, not learn, but somehow construct models. I mean,
*  it seems like you would only have to be able to learn because constructing it manually would be
*  too difficult. Do you have ideas of, I think it's a matter of combining simple models for many,
*  many sources for many, many disciplines and many metaphors. Metaphors are the basic sources
*  of human intelligence basis. So how do you think of about a metaphor in terms of its use in human
*  intelligence? Metaphors is an expert system. An expert, it's mapping problem with which you are
*  not familiar to a problem with which you are familiar. Like I give you a good example. The
*  Greek believed that the sky is an opaque shell. It's not really infinite space. It's an opaque
*  shell and the stars are holes poked in the shells through which you see the eternal light.
*  It was a metaphor. Why? Because they understand how you poke holes in the shells.
*  They're not, they were not familiar with infinite space. And so, and we are walking on a shell of a
*  turtle and if you get too close to the edge, you're going to fall down to Hades or whatever.
*  That's a metaphor. It's not true. But this kind of metaphor enabled Aristoteles to measure the
*  radius of the Earth. Because he said, come on, if we are walking on a turtle shell, then the ray of
*  light coming to this angle will be different. This place will be different angle that coming to this
*  place. I know the distance. I'll measure the two angles and then I have the radius of the shell of
*  the turtle. And he did. And he found his measurement very close to the measurements we
*  have today. It's what 6,700 kilometers of the Earth. That's something that would not occur
*  to a Babylonian astronomer, even though the Babylonian experiments were the machine
*  learning people of the time. They fit curves and they could predict the eclipse of the moon
*  much more accurately than the Greek because they fit curve. That's a different metaphor.
*  Something that you're familiar with, a game, a turtle shell.
*  What does it mean if you are familiar? Familiar means that answers to certain questions are
*  explicit. You don't have to derive them. And they were made explicit because somewhere in the past,
*  you've constructed a model of that. You're familiar with, so the child is familiar with
*  billiard balls. So the child could predict that if you let loose of one ball, the other one will
*  bounce off. You obtain that by familiarity. Familiarity is answering questions and you
*  store the answer explicitly. You don't have to derive them. So this is the idea of a metaphor.
*  All our life, all our intelligence is built around metaphors, mapping from the unfamiliar
*  to the familiar. But the marriage between the two is a tough thing which we haven't yet been able to
*  algorithmatize. So you think of that process of using metaphor to leap from one place to another.
*  We can call it reasoning. Is it a kind of reasoning? It is reasoning by metaphor.
*  Do you think of that as learning? So learning is a popular terminology today in a narrow sense.
*  It is. It is definitely a form of learning. It's one of the most important learnings.
*  Taking something which theoretically is derivable and store it in accessible
*  format. I'll give you an example. Chess.
*  Finding the winning starting move in chess is hard. But there is an answer.
*  Either there is a winning move for white or there isn't or there is a draw.
*  Okay, so it is the answer to that is available through the rule of the games.
*  But we don't know the answer. So what does the chess master have that we don't have?
*  He has stored explicitly an evaluation of certain complex pattern of the board. We don't have it.
*  Ordinary people like me, I don't know about you. I'm not a chess master. So for me, I have to derive.
*  Things that for him is explicit. He has seen it before or he has seen the pattern before
*  or similar pattern, you see metaphor. And he generalize and say, don't move in the dangerous move.
*  It's just that not in the game of chess, but in the game of
*  billiard balls, where humans are able to initially derive very effectively and then reason by metaphor
*  very effectively and make it look so easy that it makes one wonder how hard is it to build it in a
*  machine. So in your sense, how far away are we to be able to construct? I don't know. I'm not a
*  futurist. I can tell you is that we are making tremendous progress in the causal reasoning domain.
*  Something that I even dare to call it revolution, the causal revolution, because
*  what we have achieved in the past three decades is something that
*  dwarf everything that was derived in the entire history.
*  So there's an excitement about current machine learning methodologies. And
*  there's really important good work you're doing in causal inference.
*  Where do these worlds collide and what does that look like?
*  First, they're going to work without collisions. It's going to work in harmony.
*  Harmony.
*  Harmony.
*  Harmony.
*  Harmony.
*  Harmony.
*  Harmony.
*  Harmony.
*  The human is going to jumpstart the exercise by providing qualitative, noncommitting
*  models of how the universe works. How in reality the domain of discourse works.
*  The machine is going to take over from that point of view and derive whatever the calculus
*  can be derived, namely quantitative answer to our questions. These are complex questions.
*  I'll give you some example of complex questions that would bugle your mind if you think about it.
*  You take the result of studies in diverse population under diverse condition
*  and you infer the cause effect of a new population which doesn't even
*  resemble any of the ones studied. You do that by doing calculus. You do that by generalizing
*  from one study to another. What's common with Beto? What is different? Let's ignore the
*  differences and pull out the commonality. And you do it over maybe a hundred hospitals
*  around the world. From that you can get really mileage from big data.
*  It's not only you have many samples, you have many sources of data.
*  So that's a really powerful thing, I think, especially for medical applications. Cure cancer,
*  right? That's how from data you can cure cancer. So we're talking about causation,
*  which is the temporal relationships between things. Not only temporal. It's more structural
*  and temporal. Temporal precedents by itself cannot replace causation.
*  Is temporal precedence the arrow of time in physics? Yeah, it's important, necessary.
*  It's important. But not sufficient. Yes. Is it?
*  Yes. I never seen the cause propagate backward. But if we use the word cause,
*  but there's relationships that are timeless. I suppose that's still forward and arrow of time.
*  But are there relationships, logical relationships that fit into the structure?
*  Sure. The whole do calculus is logical relationship. That doesn't require a temporal.
*  It has just the condition that you're not traveling back in time. Yes. Correct.
*  So it's really a generalization of a powerful generalization of what-
*  Bullying logic. Yeah, bullying logic.
*  Yes. That is simply put and allows us to reason about the order of events, the source.
*  Not about, between, but not deriving the order of events. We are given cause-effects relationship.
*  They ought to be obeying the time precedence relationship. We are given that. And now that
*  we ask questions about other cause-effects relationship that could be derived from the
*  initial ones, but were not given to us explicitly. Yeah. Like the case of the firing squad I gave you
*  in the first chapter. And I ask what if rifleman A declined to shoot, would the prisoner still be dead?
*  To decline to shoot, it means that he disobey order. And the rule of the games were that he is an
*  obedient marksman. That's how you start. That's the initial order. But now you ask questions about
*  breaking the rules. What if he decided not to pull the trigger? He just became a pacifist.
*  You and I can answer that. The other rifleman would have killed him. I want the machine to do that.
*  Is it so hard to ask machine to do that? It's just a simple task. You have to have a calculus for that.
*  Yes. But the curiosity, the natural curiosity for me is that yes, you're absolutely correct and
*  important. And it's hard to believe that we haven't done this in the last few years.
*  It's hard to believe that we haven't done this seriously, extensively already a long time ago.
*  So this is really important work. But I also want to know, you know, this maybe you can philosophize
*  about how hard is it to learn? Okay, let's assume we learn it. We want to learn it. Okay. We want to
*  learn. So what do we do? We put a learning machine that watches execution trials in many countries
*  locations. Okay. All the machine can learn is to see shot or not shot. Dead, not dead.
*  Court issued an order or didn't. Okay. That's the fact. From the fact you don't know who listens to
*  whom. You don't know that the condemned person listen to the bullets, that the bullets are
*  listening to the captain. Okay. All we hear is one command, two shots, dead. Okay. A triple of
*  variable. Yes, no. Yes, no. Okay. That you can learn who listens to whom and you can answer the
*  question. No, definitively no. But don't you think you can start proposing ideas for humans to review?
*  You want machine to learn, right? You want a robot. So robot is watching trials like that.
*  200 trials. And then he has to answer the question. What if rifleman a refrain from shooting? Yeah.
*  So how do you do that? That's exactly my point. That looking at the facts don't give you the
*  strings behind the facts. Absolutely. But do you think of machine learning as currently defined
*  as only something that looks at the facts and tries right now, they only look at the facts.
*  So is there a way to modify in your sense? Playful manipulation, playful manipulation,
*  interventionist kind of thing. Intervention. But it could be at random. For instance, the
*  rifleman is sick that day, or he just vomits or whatever. So machine can observe this unexpected
*  event, which introduced noise. The noise still has to be random to be able to relate it to
*  randomized experiment. And then you have observational studies from which to infer
*  the strings behind the facts. It's doable to a certain extent. But now that we are expert
*  in what you can do, once you have a model, we can reason back and say, what kind of data you need
*  to build a model? Got it. So I know you're not a futurist, but are you excited? Have you,
*  when you look back at your life, long for the idea of creating a human level intelligence system?
*  I'm driven by that. All my life I'm driven just by one thing.
*  But I go slowly. I go from what I know to the next step incrementally.
*  So without imagining what the end goal looks like, do you imagine what an...
*  And the end goal is going to be a machine that can answer sophisticated questions,
*  counterfactuals, regret, compassion, responsibility, and free will.
*  So what is a good test? Is a touring test a reasonable test?
*  A test of free will doesn't exist yet.
*  How would you test free will?
*  So far we know only one thing. If robots can communicate with reward and punishment among
*  themselves, hitting each other on the wrist and saying, you shouldn't have done that,
*  playing better soccer because they can do that.
*  What do you mean because they can do that?
*  Because they can communicate among themselves.
*  Because of the communication they can do the soccer.
*  Because they communicate like us, reward and punishment. Yes, you didn't pass the ball the
*  right time and so forth, therefore you're going to sit on the bench for the next two.
*  If they start communicating like that, the question is, will they play better soccer?
*  As opposed to what? As opposed to what they do now?
*  Without this ability to reason about reward and punishment, responsibility.
*  So far I can only think about communication.
*  Communication is not necessarily a natural language, but just communication.
*  Just communication. That's important to have a quick and effective means of communicating
*  knowledge. If the coach tells you you should have passed the ball, pink, he conveys so much
*  knowledge to you as opposed to what? Go down and change your software. That's the alternative.
*  But the coach doesn't know your software. How can the coach tell you you should have passed the
*  ball? Our language is very effective. You should have passed the ball. You know your software.
*  You tweak the right module and next time you don't do it.
*  Now that's for playing soccer. The rules are well defined.
*  No, no, no. The rules are not well defined. When you should pass the ball.
*  It's not well defined.
*  No, it's very soft. Very noisy. You have to do it under pressure.
*  It's art. But in terms of aligning values between computers and humans,
*  do you think this cause and effect type of thinking is important to align the values?
*  Values, morals, ethics under which the machines make decisions. Is the cause effect where
*  the two can come together? Cause and effect is a necessary component
*  to build an ethical machine because the machine has to empathize to understand what's good for you
*  to build a model of you as a recipient which should be very much what is compassion.
*  They imagine that you suffer pain as much as me. As much as me. I do have already a model of myself.
*  Right? So it's very easy for me to map you to mine. I don't have to rebuild the model.
*  It's much easier to say, oh, you're like me. Okay. Therefore I would not hate you.
*  And the machine has to imagine, has to try to fake to be human essentially.
*  So you can imagine that you're like me. Right?
*  Who is me? That's the first. That's consciousness. They have a model of yourself.
*  Where do you get this model? You look at yourself as if you are a part of the environment.
*  If you build a model of yourself versus the environment, then you can say, I need to have
*  a model of myself. I have abilities. I have desires and so forth. Okay. I have a blueprint of myself.
*  Not a full detail because I cannot get the halting problem, but I have a blueprint.
*  So on that level of a blueprint, I can modify things. I can look at myself in different ways.
*  I can look at myself in the mirror and say, hmm, if I change this, tweak this model,
*  I'm going to perform differently. That is what we mean by free will.
*  And consciousness. What do you think is consciousness? Is it simply self-awareness?
*  So including yourself into the model of the world?
*  That's right. Some people tell me, no, this is only part of consciousness.
*  And then they start telling me what they really mean by consciousness. And I lose them.
*  Yeah. For me, consciousness is having a blueprint of your software.
*  Do you have concerns about the future of AI? All the different trajectories of all of our research?
*  Yes. Where's your hope? Where the movement heads were your concerns?
*  I'm concerned because I know we are building a new species that has the capability of exceeding our
*  capabilities and can breathe itself and take over the world. Absolutely. It's a new species.
*  It is uncontrolled. We don't know the degree to which we control it. We don't even understand
*  what it means to be able to control this new species. So I'm concerned. I don't have anything
*  to add to that because it's such a gray area, that's unknown. It never happened in history.
*  The only time it happened in history was evolution with human beings.
*  It wasn't very successful, was it? Some people say it was a great success.
*  For us, it was, but a few people along the way, a few creatures along the way would not agree.
*  So it's just because it's such a gray area, there's nothing else to say.
*  We have a sample of one. Sample of one.
*  That's us. But some people would look at you and say,
*  yeah, but we were looking to you to help us make sure that sample two works out okay.
*  We have more than a sample of one. We have theories. We don't need to be statisticians.
*  So sample of one doesn't mean poverty of knowledge. It's not. Sample of one plus theory,
*  conjectural theory of what could happen. That we do have. But I really feel helpless in contributing
*  to this argument because I know so little and my imagination is limited and I know how much I don't
*  know. But I'm concerned. You were born and raised in Israel.
*  Born and raised in Israel, yes. And later served in Israel military defense forces.
*  In the Israel Defense Force. Yeah.
*  What did you learn from that experience? From that experience?
*  There's a kibbutz in there as well. Yes, because I was in a nachal, which is a
*  combination of agricultural work and military service.
*  I was really idealist. I wanted to be a member of the kibbutz throughout my life
*  and to live a communal life. And so I prepared myself for that.
*  And slowly, slowly I went to greater challenge.
*  So that's a far world away. But I learned from that.
*  It was a miracle. It was a miracle that I served in the 1950s. I don't know how we survived.
*  But the country was under austerity. It tripled its population from 600,000
*  to 1,000,000.8 when I finished college. No one went hungry. Austerity, yes.
*  When you wanted to buy, to make an omelet in a restaurant, you had to bring your own egg.
*  And they imprisoned people from bringing food from the farming, from the villages to the city.
*  But no one went hungry. And I always add to it, higher education did not suffer any budget cut.
*  They still invested in me, in my wife, in our generation,
*  to get the best education that they could. So I'm really grateful for the opportunity.
*  And I'm trying to pay back now. It's a miracle that we survived the war of 1948.
*  We were so close to a second genocide. It was all planned. But we survived it by miracle.
*  And then the second miracle that not many people talk about, the next phase,
*  how no one went hungry and the country managed to triple its population. You know what it means?
*  Imagine the United States going from what, 350 million to 2 billion. Unbelievable.
*  It's a really tense part of the world. It's a complicated part of the world. Israel and all
*  around. Religion is at the core of that complexity. Religion is a strong motivating
*  cause to many, many people in the Middle East. In your view, looking back, is religion good for
*  society? That's a good question for robotics. There's echoes of that question. Equip robots
*  with religious beliefs. Suppose we find out or we agree that religion is good to you to keep you
*  in line. Should we give the robot the metaphor of a god? As a matter of fact, the robot will get it
*  without us also. Why? The robot will reason by metaphor. And what is the most primitive metaphor
*  a child grows with? Mother smile, father teaching, father image, mother image. That's god.
*  So whether you want it or not, assuming the robot is going to have a mother and a father,
*  it may only have a programmer who doesn't supply warmth and discipline. Discipline it does.
*  So the robot will have a model of the trainer and everything that happens in the world, cosmology and
*  so on, is going to be mapped into the programmer. It's god.
*  The thing that represents the origin of everything for that robot. That's the most primitive
*  relationship. So it's going to arrive there by metaphor. And so the question is if overall that
*  metaphor has served us well as humans. I really don't know. I think it did.
*  But as long as you keep in mind, it's only a metaphor.
*  So if you think we can, can we talk about your son? Yes. Can you tell his story?
*  A story? Well, Daniel's story is known. He was abducted in Pakistan by Al Qaeda driven sect.
*  And under various pretenses, I don't even pay attention to what the pretends were.
*  Originally they wanted to have the United States
*  deliver some promised airplanes. It was all made up and all these demands were bogus.
*  I don't know really, but eventually he was executed in front of a camera.
*  At the core of that is hate and intolerance.
*  At the core? Yes, absolutely. Yes. We don't really appreciate the depth of the hate at which
*  which billions of peoples are educated. We don't understand it. I just listened recently
*  to what they teach you in Mogadishu. When the water stopped in the tap,
*  we knew exactly who did it. The Jews. The Jews. We didn't know how, but we knew who did it.
*  We don't appreciate what it means to us. The Jews didn't know how, but we knew who did it.
*  We don't appreciate what it means to us. The depth is unbelievable profound.
*  Do you think all of us are capable of evil?
*  And the education, the indoctrination is really what creates evil?
*  Absolutely we are capable of evil. If you are indoctrinated sufficiently long and in depth,
*  we are capable of ISIS. We are capable of Nazism. Yes, we are. But the question is whether we,
*  after we have gone through some Western education and we learn that everything is really relative,
*  that there is no absolute God, there is only a belief in God, whether we are capable now
*  of being transformed under certain circumstances to become brutal.
*  I'm worried about it because some people say yes, given the right circumstances, given
*  bad economical crisis, you are capable of doing it too. That worries me. I want to believe it,
*  I'm not capable. Seven years after Daniel's death, you wrote an article at the Wall Street
*  Journal titled Daniel Pearl and the Normalization of Evil. What was your message back then and
*  how did it change today over the years? I lost. What was the message? The message was that
*  we are not treating terrorism as a taboo. We are treating it as a bargaining device
*  that is accepted. People have grievance and they go and bomb restaurants. It's normal. Look,
*  you're even not surprised when I tell you that. 20 years ago you say, what? For grievance you go
*  and blow a restaurant? Today it's becoming normalized, the banalization of evil.
*  We have created that to ourselves by normalizing, by making it part of
*  the political life. It's a political debate. Every terrorist yesterday becomes a freedom
*  fighter today and tomorrow becomes a terrorist again. It's switchable.
*  We should call out evil when there's evil. If we don't want to be part of it.
*  Becoming. If we want to separate good from evil, that's one of the first things that
*  in the Garden of Eden, remember the first thing that God told him was, hey,
*  you want some knowledge? Here's a tree of good and evil.
*  So this evil touched your life personally. Does your heart have anger, sadness, or is it hope?
*  Okay. I see some beautiful people coming from Pakistan. I see beautiful people everywhere,
*  but I see horrible propagation of evil in this country too. It shows you how populistic
*  slogans can catch the mind of the best intellectuals. Today is Father's Day. I didn't know that.
*  Yeah. What's a fond memory you have of Daniel? Daniel's father, Daniel.
*  Fond memory you have of Daniel. Oh, many good memories. He was my mentor. He had
*  a sense of balance that I didn't have.
*  He saw the beauty in every person. He was not as emotional as I am.
*  More looking at things in perspective. He really liked every person. He really grew up with the
*  idea that a foreigner is a reason for curiosity, not for fear. At one time we went in Berkeley
*  and a homeless came out from some dark alley and said, hey man, can you spare a dime? I
*  retreated back two feet back and Danny just hugged him and said, here's a dime. Enjoy yourself.
*  Maybe you want some money to take a bath or whatever. Where did you get it? Not for me.
*  Do you have advice for young minds today dreaming about creating, as you have dreamt, creating
*  intelligent systems? What is the best way to arrive at new breakthrough ideas and carry them
*  through the fire of criticism and past conventional ideas? Ask your questions freely. Your questions
*  are never dumb and solve them your own way. Don't take no for an answer.
*  If they are really dumb, you will find out quickly by trying an arrow to see that they are not
*  leading any place. Follow them and try to understand things your way. That is my advice. I don't know
*  if it's going to help anyone. There is a lot of inertia inside of them. They are not going to
*  inertia in science, in academia. It is slowing down science.
*  Those two words, your way, that's a powerful thing. It's against inertia potentially,
*  against the flow. Against your professor. I wrote the book of why in order to democratize common sense.
*  Yes. In order to instill rebellious spirit in students so they wouldn't wait until the professor
*  gets things right. You wrote the manifesto of the rebellion against the professor.
*  Against the professor, yes. Looking back at your life of research,
*  what ideas do you hope ripple through the next many decades? What do you hope your legacy will be?
*  I already have a tombstone carved. The fundamental law of counterfactuals.
*  That's what it's a simple equation. What counterfactual in terms of a model surgery.
*  That's it because everything follows from that. If you get that, all the rest,
*  I can die in peace and my student can derive all my knowledge by mathematical means.
*  The rest follows. Thank you so much for talking today. I really appreciate it.
*  Thank you for being so attentive and instigating.
*  We did it. The coffee helped.
*  Thanks for listening to this conversation with Judea Pearl. Thank you to our presenting sponsor,
*  Cash App. Download it, use Code Lex Podcast. You'll get $10 and $10 will go to FIRST,
*  a STEM education nonprofit that inspires hundreds of thousands of young minds to learn
*  and to dream of engineering our future. If you enjoy this podcast, subscribe on YouTube,
*  get five stars on Apple Podcast, support on Patreon, or simply connect with me on Twitter.
*  Now, let me leave you with some words of wisdom from Judea Pearl.
*  You cannot answer a question that you cannot ask, and you cannot ask a question
*  you have no words for. Thank you for listening and hope to see you next time.

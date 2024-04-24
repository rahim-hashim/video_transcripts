---
Date Generated: April 20, 2024
Transcription Model: whisper medium 20231117
Length: 3446s
Video Keywords: ['Education', 'Science', 'Technology']
Video Views: 18582
Video Rating: None
---

# BI ViDA Panel Discussion: Deep RL and Dopamine
**Brain Inspired:** [September 02, 2021](https://www.youtube.com/watch?v=ZYlwCjCjDOA)
*  This actually gives me an occasion to mention one thing that always bothers me about trying
*  to relate deep RL to biological systems, which is that there's no natural way of taking evolutionary
*  learning into account.
*  For me, the AI work gives us a language to talk about maybe particular axes of activity,
*  say across the dopamine neurons in the fly.
*  The question is how many axes are there?
*  I suppose the fact that the training process is not completely biologically realistic might
*  lead us astray.
*  But on the other hand, I think having a model that works and encompasses many of the things
*  we are looking for and expect is much better than alternative.
*  Somehow across evolution, we have meta-learned some internal landscape, homeostatic landscape,
*  which is not representing the world, but it's representing some internal states that corresponds
*  to the scarcity or presence of various dimensions of rewards in the world.
*  Hopefully, by knowing those representations, I think we will be in the position to come
*  back as neuroscientists to AI and give them some output of what we know in terms of representation
*  in the brain and maybe give something back to AI.
*  This is Brain Inspired.
*  Hi, I'm Paul Middlebrooks.
*  Welcome to Brain Inspired.
*  In this episode, you'll hear the panel discussion that I moderated recently at the virtual dopamine
*  conference.
*  So last episode, you heard Ali Mohebi and Ben Ingelhard, and we sort of introduced dopamine
*  I suppose, and got their reflections on this panel that you're about to hear and had a
*  pretty broad conversation otherwise about related topics.
*  So in this panel that I moderated, we have Matt Botvinnik, Ida Momenajad, Ashok Litwin
*  Kumar, Ilana Witten, and Armin Lack.
*  And it was co-moderated with me by Tim Krause.
*  And you'll hear more about them in a moment.
*  So that's the panel discussion.
*  So the title of the discussion, the title of the panel, is What Can Artificial Intelligence
*  Teach Us About How the Brain Uses Dopamine to Learn?
*  And I'm just going to read you the abstract because it's short and summarizes everything.
*  Recent advances in artificial intelligence have yielded novel algorithms for reinforcement
*  learning, which leverage the power of deep learning together with reward prediction error
*  signals in order to achieve unprecedented performance in the brain.
*  In the brain, reward prediction error signals are thought to be signaled by midbrain dopamine
*  neurons and support learning.
*  Can these new advances in deep reinforcement learning help us understand the role that
*  dopamine plays in learning?
*  In this panel, experts in both theoretical and experimental dopamine research will discuss
*  this question.
*  So there you have it.
*  As a reminder, I have an email list for the podcast.
*  And what I do in those emails is often before an episode, I will send out a relevant talk
*  or abstract or some relevant information for the upcoming episode.
*  And that's what I did here.
*  I sent out Matt Botvinick's talk that he gave that just preceded the discussion you're about
*  to hear.
*  So if that's something that would be of interest to you, you can go to the website and sign
*  up for the email list at braininspired.co, where you can find out more about the discussion
*  at braininspired.co, where you can also find information about the panelists that you're
*  about to hear.
*  So enjoy.
*  I will just introduce our panel of speakers here before we kind of dive into the questions
*  and discussion.
*  In no particular order, we have Ashok Litwin Kumar from Columbia University, Ida Momendazhad,
*  who is currently at Microsoft, Armin Lack at Oxford, and Ilana Witten, who runs her
*  lab at Princeton.
*  There's already multiple questions in the Q&A.
*  And I guess I'll just remind everyone that if you want to submit a question, use the
*  Q&A box down below.
*  I suppose just to get started here, just from the perspective of your own work, do you see
*  the deep reinforcement learning models as providing a way into how we currently think
*  that brains actually learn, given the various species and computational models that you
*  work on?
*  And maybe I'll just point to someone.
*  Armin, maybe I could start with you.
*  Thank you so much.
*  So I think in order to get to this question, you probably need to start thinking about
*  what we are currently trying to do in the experimental side of systems neuroscience
*  and understanding dopamine.
*  And to me, there are two things that different groups are trying to push forward, in particular
*  in case of dopamine.
*  One of them is the idea of discovering the relation between new cognitive variables,
*  which are not tested in the dopamine case, and the representation of them in the dopamine
*  field.
*  And Matt showed a lot of those examples of the kind of new variables that we were not
*  discussing, and how they can be tested and parameterized using RL.
*  That's one avenue that I think in systems neuroscience we are trying to get to, like
*  designing new experiments with new variables and trying to parameterize those in animal
*  context.
*  The second one is going to really cracking the circuit and trying to understand the exact
*  connection between neurons, the input of the neurons to the dopamine system, as well as
*  the output.
*  And on that front, I think a lot of nice experimental work has been done.
*  But when it comes to AI and it comes to reinforcement learning or deep reinforcement learning,
*  it seems that we are still quite far from connecting the two together, like bringing
*  effectively mapping these computations onto the circuit.
*  So if I want to summarize what I have been saying is that on the two sides that we are
*  pushing in systems neuroscience, cognitive variables and cracking the circuit, I think
*  so far, AI has been more useful on the side of those variables and parameterizing those
*  variables.
*  And it has been less useful on helping us to understand the secret and the connection
*  between neurons and how they work together to make those representations.
*  I wonder if Ashok is the right person to bring in here because he works partly on figuring
*  out whether we can use circuitry and use connections to deduce function, which is just
*  an infinitely difficult problem, as you might.
*  Yeah, I mean, I'm coming at this from mostly the Drosophila connectomics side and the kind
*  of first statement one makes when looking at the connectomes, everything connects to
*  everything and there's a great deal of diversity and feedback among even all of these neurons
*  that we think may be doing or mostly doing a particular function like learning to approach
*  or avoid.
*  So I think for me, the AI work gives us a language to talk about maybe particular axes
*  of activity, say across the dopamine neurons and the fly.
*  And the question is, how many axes are there?
*  Are there axes that are not encompassed by what we typically think about in AI?
*  And can we infer those from neuroscience data like the connectome or recordings?
*  So I'm just pausing to see if anyone wants to jump in.
*  And so maybe just to make sure everyone gets to speak here in the beginning, Ilana, do you want to add to the conversation?
*  Yeah, sure.
*  So I guess one thing that I would say is that I think the way you phrase the question is what does the learning,
*  how does this model the learning process itself, these deep agents?
*  And I would say, and I think Matt would probably agree that the training of the networks is pretty far from biologically realistic as currently stated,
*  but as currently performed.
*  But that doesn't mean it can't be a helpful model for the fully trained circuit.
*  So provide constraints on hypotheses for neural data or formalized intuitions.
*  So I think at least that my impression is the current state of the AI training, the deep learning training.
*  No one's taking the training of the network very seriously as a model of the biology.
*  It's only the trained agent that's taken seriously.
*  So I think that's an important distinction or clarification with the question.
*  And I do think that once you do have a trained agent, I mean, I think Matt showed beautifully examples of how it can produce the state representations
*  that can really clarify how a trained animal could potentially, a model for how trained animal can do the task and provide a framework to either test formal hypotheses or reject them.
*  And that leaves the other side, which I think thinking about more biologically realistic training protocols that might actually model the learning, the initial learning process itself,
*  which Matt also touched on seems like a big open area that seems really exciting and important for many biological questions that many of us are interested in.
*  And Ida, I'm going to let you jump in here as well.
*  Thanks. So I think it's fantastic that we have cellular representation here and we have dorsophila and rodent sort of science.
*  I work mostly in humans and I've previously worked with Matt.
*  So I think something that may be important to note is the different types of architecture, especially for higher cognition.
*  I think that deep RL methods are particularly helpful for comparing different architectures, theorizing about them and comparing different theories in terms of their behavior.
*  And also in terms of the similarity of their internal representations with the kinds of similarity we would see in what we measure in humans and maybe monkeys or sometimes rodents in higher cognitive function.
*  And I think that that's a particularly helpful part of the parallel, but I think might not be quite the end.
*  Obviously, this is a tradition that goes back to the 80s, so it's not necessarily new to deep RL, but I feel like it moves much further after a kind of a hiatus.
*  But other than the higher cognitive function, I think that the reward maximization framework might have limitations because especially if one defines a singular reward.
*  And the reason is that we have many different scales and dimensions of reward that are competing with one another.
*  And there needs to be some higher representation that kind of decides in different moments or manages their homeostasis with regard to long term and short term goals.
*  And I think that it could be a little sort of challenging to stick to just the reward maximization framework.
*  So we might need a future kind of evolution of deep RL if we want to address these sorts of more complex, long term, short term, multi scale approaches.
*  This might be a good time. Matt, you brought up the paper reward is enough or is it I don't remember the actual intriguing title is reward enough reward is everything reward is the end all.
*  So I'm curious. You said you weren't you weren't advocating it. But I mean, it is kind of an intriguing selling point.
*  And I'm curious about everyone's take. I'm not sure if you know who's read the paper and who's not.
*  So I would I would based on what I had just said, is reward enough or is that sort of a trivial question given that we can define reward as anything?
*  And we have a lot of questions coming in. So after we discuss this a little bit, we'll have some questions from the audience as well.
*  Can I can I kick that off, please? Yeah.
*  So before before Dave and Rich and doing a and September put that paper on archive, there was actually a lot of internal debate at DeepMind about this argument that they were making.
*  And I one of my colleagues, Vladney, who is the the lead author on the the Atari paper, actually his rebuttal to the argument was basically two words.
*  Architecture matters. And so this this gives me an excuse to circle back to this to the points that Armand was making about architecture.
*  I think this circuit circuit like cracking the circuit. That's a place where it really is important that most deep RL research is not computational neuroscience.
*  There are just aspects of, you know, kind of economics that are just not going to come up from AI work.
*  But I think it is I think on the other hand, there are a lot of insights that we gain from deep RL about how things play out, assuming different architectural structures.
*  I mean, convolutional neural networks are a great example of that. Of course, they were inspired by neuroscience and they're heavily used in the analyses of the biological nervous system.
*  Coming back to the question of whether reward is enough. This is also an excuse for me to emphasize the point I made at the end of my spiel, which is that deep RL does not necessarily mean end to end learning.
*  So a lot of deep RL systems now use self supervised representation learning.
*  So just trying to predict what's going to come next. That's not a reward driven learning process, but it yields representations that are useful for reward maximization.
*  So this connects with the comment that Ida was just making.
*  And it also is relevant to what Alana was saying about training, training regimes.
*  If you have a system that is trying to predict what comes next, that's a very different form of that's a very different way of using than learning from RL alone.
*  And the results that can give you much greater sample efficiency, for example, one complaint that neuroscientists often have about deep RL is that it's highly sample inefficient.
*  But it doesn't have to be if you configure things correctly.
*  So maybe we'll jump in with a couple audience questions right now.
*  This is really interesting discussion and we have one question that's asking, do you think that AI can lead neuroscientists in the wrong direction to match the model instead?
*  So misleading how the brain might compute by trying to match the models you're using.
*  I'm happy to field that one.
*  If they're sort of hesitant, maybe start us off, Matt.
*  Short answer. Yes. I mean, the minute you the minute you adopt a deep RL model as in neuroscience work, you're you're treating it as a hypothesis and hypotheses are almost always wrong.
*  Whether whether you can be misled, that to me seems just like a question of good experimental design.
*  There's nothing there's no fundamental difference between a deep RL model as a kind of computationally implemented hypothesis and any other hypothesis in neuroscience.
*  So I think you just need to be careful to design good experiments.
*  But I think maybe what the question is getting at is this airplane versus bird thing.
*  There are a lot of aspects of deep RL systems that are just wildly unbiologic.
*  And can we be distracted by that? Absolutely. Yeah, definitely.
*  Ilana, maybe you have something perspective on this because given your comment about the differences in training and needing and the environment and the way it's structured, the differences between training a reinforcement learning algorithm, you know, agent.
*  So, of course, we have, you know, very quote unquote realistic mazes and games.
*  But but that is different than the structure of the world.
*  And I don't know if you have thoughts about how that might affect the learning process and the training process, how how it could lead us astray in that sense.
*  That's a good question. I mean, I actually I suppose the fact that the training process has is not completely biologically realistic might lead us astray.
*  But on the other hand, I think having a model that works and simulates many of the encompasses many of the things we are looking for and expect is much better than alternative, which is not having a model.
*  So I wouldn't I wouldn't I guess I wouldn't use the term lead us astray.
*  I still think I think would be interesting.
*  And I definitely think the self supervised learning aspect that Matt brought up might be a really key and important part of it.
*  I think it would be very interesting to have like, you know, initial training be as biologically realistic as possible to model that part as well and see if that makes different predictions about the end function of the network.
*  That seems like an interesting and important research direction.
*  But I I wouldn't have gone so far to say that, like having the initial training being not particularly biologically realistic means that it's not a useful model at the end.
*  But it's I mean, of course, that could be the case.
*  That sounds like an important research direction.
*  Okay, I think I was also I haven't read the reward is enough paper myself.
*  So I just was curious what that paper was really saying.
*  Were they really arguing against the importance of self supervised learning and sensory sensory prediction?
*  Or what were they actually saying?
*  Because that seems like a very strong argument to make that there's no like learning about the structure of the world without reward.
*  Because even if ultimately the goal is to get reward, obviously it seems very useful to know about the structure of the world and learn it.
*  So what were they actually saying?
*  Defend your colleagues, sir.
*  I haven't read the paper, but I've talked to the authors an awful lot.
*  So I think the argument is that optimizing a reward on a reward function through through experience with the world is guaranteed to be enough to give you the representations that you need in order to maximize reward.
*  What it doesn't guarantee and which is something that's neglected in their argument, at least as they made it verbally in inside D mine is is sample efficiency.
*  Like, yes, reward like RL is enough to get any intelligent behavior given infinite experience, infinite data.
*  But it doesn't explain how you know how humans and other animals, for example, are able to learn in such a sample efficient way.
*  Of course, that's an argument like that's a point that cognitive science scientists like Josh Tenenbaum have been making for years with with great legitimacy.
*  And that's just not something that comes up in that paper.
*  There are ways of getting there.
*  The Nature Neuroscience paper that I briefly summarized in my spiel is really about meta learning.
*  And, you know, if you if you look at our paper, it's all about how pre training on a wide variety of tasks can lead to a system that can then learn in a very sample efficient way.
*  But this actually gives me an occasion to mention one thing that always bothers me about trying to relate deep RL to biological systems, which is that there's no natural way of taking evolutionary learning into account.
*  So, you know, when when Alanda does experiments with animals, not only do they have the benefit of whatever experience they've had in their lifetime, but their brains were designed by eons of evolutionary learning, which consumes data, right?
*  Like, it's not it's not sample efficient, but it it wires in certain, you know, architectural structures into the brain.
*  And I just I don't know any way to get to capture that side of the story in deep RL.
*  There are people who play with evolutionary algorithms that design architectures and so forth.
*  But it's very hard to get the analogy right.
*  I just want to echo that.
*  I think the conflation of evolutionary development within lifetime learning is one of the most difficult things when we're trying to make analogies between these agents and biological systems.
*  Yeah, you have a raised hand there.
*  Just wanted to maybe ask Matt this or anyone else.
*  Matt, do you think it would be fair to think that there are different cultures of reinforcement learning that kind of correspond to the history of cognitive science where some are closer to behaviorism?
*  Some are more akin to the cognitive turn after Tolman, which I guess you and me would be a part of it.
*  And some might be even closer to inactivism and talking about empowerment and interaction sort of learning and which is much more used in robotics where there is a body that needs to interact with an environment.
*  And these are the three sort of cultures that sort of progress through cognitive science.
*  And it seems to me that perhaps reward is not enough is akin to the behaviorist culture of RL.
*  I wonder what you think of it.
*  Yeah, I mean, it's just like any other discipline, any other human culture.
*  There are definitely different subcultures.
*  And in particular, there have been people who have been very focused on questions of sample efficiency and other people who just don't care, who figure we'll get the data we need.
*  We're not, you know, I mean, it's important to emphasize most AI researchers are not trying to model human behavior or brain function.
*  So, you know, the fact that AlphaGo takes a huge number of games to learn what it learns relative to what a human consumes is just not it doesn't matter to some of the people who do this kind of research.
*  It's not the problem that they're addressing.
*  Whereas for other researchers, often ones who come from a cognitive science background.
*  Yes, that difference is irritating, not because deep RL is necessarily being applied as a model of human learning, but just because we have a notion of what intelligence is.
*  And part of that is learning in a sample efficient way.
*  Like, that's just what intelligence that's how intelligence manifests.
*  Another another important cultural division is between people who are very focused on single task learning.
*  Like, I just want to get as good at chess as I can, versus people who are more interested in multitask learning, you know, I want to learn six Atari games and then I want the seventh to be acquired more rapidly than it would otherwise be acquired.
*  They just people have different they set up they define the problem in different ways which leads to different emphases.
*  Absolutely.
*  This might be a good time to ask a couple listener questions as well.
*  I mean, I just carrying off what you were just talking about that.
*  So, the top of the question right now is in in AI you have known problems like reward hacking.
*  Do you think those are unique AI problems or is there a biological parallel.
*  Any animal researcher has seen reward hacking in the lab.
*  Well given. Okay.
*  So, so the answer is yes I suppose I wonder if that would be satisfying to Ben, I should let other people talk.
*  If no one has anything to say there's another, there's an actual dopamine question, and this is a dopamine conference, so maybe we can move on while people think about that question more dopamine what might be the, what might the co release of GABA or glutamate with
*  So, does anyone have a response to that co release question.
*  I actually do inspired by Matt's paper, his 2018, 2018, at all. The long at all paper, the meta reinforcement learning paper. Right. Yeah, the one that you described, which is that one argument that you made was that maybe dopamine is after like maybe initial it's involved in initial learning to train the weights but then after initial learning dopamine might be just an input to the system.
*  That just like a reward that the network uses as reward input and to me that makes much more sense as a potential function for the glutamate co release. I don't know if you specifically said that in your, I don't think you split the new paper that sort of how I didn't say that that's a great idea.
*  Yeah, but it makes more sense to me because like, you know dopamine does modulate plus it just doesn't feel right for just like an input that like drives the neurons but there is this co release so it could be like a kind of computational function of that co release so that's how I read that paper.
*  I never thought of that that's fascinating. Thank you.
*  There's also the question of whether we have dopamine solved right. So a couple of the panelists here are men and Ilana specifically I know have talked about all the different co factors outside of just reward prediction error that dopamine is involved in.
*  Is involved in our men maybe maybe you can talk about this. Do you feel like that we have a good grasp on what dopamine is doing within the reinforcement learning approach or do we really need to expand and include a thousand different computational factors as well.
*  So, yeah, that's that's a really good question and it's very hard to answer. I think at some level we have some good grasp of what the what the function but one of the core function is, but that of course doesn't exclude other functions.
*  And I think we are in the beginning of even exploring those other functions.
*  And the tools that we have now will actually allow us to do so.
*  We are. I think it's only a matter of years that it's only some years that you're actually measuring dopamine with the specificity that we that we like. And that's really allowing us to to to now think about the the the variables beyond reward prediction error.
*  Which has been hard to do to examine because most of these two type of variables and my turn out to be subtle in terms of the behavioral effect that they have and therefore the neural representation that they have.
*  And which then is this subtle nature of this type of variable beyond reward prediction error could have been made it very hard to actually discover it in the in the in the limited type of recording that we have been doing previously in one neuron or indirect measurement of dopamine.
*  I think with the tools that we have and we are actually in the position to to explore and go beyond what is known in the system.
*  And some of these questions are which are at the moment a lot of groups are addressing are really going towards the idea of characterizing the responses in relation to very basic variables like the action or the motivation or the representation of a stimulus.
*  So kind of very much external inputs or a very kind of visible observable type of behavioral variable.
*  And some of the others are are really internal variables.
*  Those that we can argue arguably only recover using models using our models or similar models.
*  And I think in that front we are we are really in the beginning of understanding not only the dopamine case but also in the rest of the brain of how those representations are happening.
*  And hopefully by knowing those representation I think we will be then in the position to to to to come back from as neuroscientists to a I and give them some some output of what we know in terms of representation in the brain and maybe give give give something back to to a I.
*  I want to jump in here with another question that is somewhat related.
*  I'm going to summarize this longer one where it's asking essentially if you're starting with your models of the assumption that dopamine is encoding RPE.
*  But we also know that dopamine is involved in things like vigor, motivation, responsibility, etc.
*  How can we then test in our model that dopamine is just coding RPE?
*  And also when we know that the RPE itself is estimated from it really depends on the value function you're using or your reward function.
*  So is that assumption really hurting us?
*  Should we go about this a different way?
*  I can kick things off if that's all right.
*  I think deep RL models have exactly the same character as classical RL models that of course have been used widely in psychology neuroscience.
*  If you're yeah, if you're modeling the function of dopamine strictly in classical RPE terms, but the dopamine neurons that you're looking at don't actually they're not actually doing that, then you're going to falsify your model.
*  Like that's that's just that's just the way it is, even with a deep RL system.
*  I mean, the I mean the distribution of dopamine project that I described as a great example of that, like the dopamine neurons are definitely doing stuff that a classical RL model cannot explain.
*  There's just variants in the data that's not explained, but that is explained by quite a different kind of deep RL model.
*  There's no there's nothing.
*  There are no new principles involved in computational modeling here.
*  What what does get complicated and the question flagged this is that because there's representation learning going on, you know, there things can happen in the model that depend very much on the way that you assume the perceptual data is structured or what you assume about the reward function.
*  So I'm thinking about like Anne's talk yesterday, you know, showing that the dopamine system cares about whatever outcome was just instructed to a human participant as the goal.
*  You have to know that humans, I don't know, are sensitive to social reward.
*  They want to comply with instructions or something.
*  That's just part of our reward function as Anne's results show.
*  So if you're not assuming the right reward function, again, you're going to get a model that doesn't explain your data.
*  But fortunately, it's a model and you can disconfirm it and you'll know you're wrong.
*  And that's so it's normal science in that regard.
*  Do we so maybe Ashok, you've done work in the mushroom body of drosophila, the olfactory sensory processing area.
*  And I'm kind of wondering, thinking about the distributional reinforcement learning that Matt talked about, you know, there might just be this trend toward more and more detail.
*  And so Matt talked about it in terms of the amount of prediction, the amount of optimism and pessimism each different little circuit might have in the dopamine reward circuits.
*  You know, I'm wondering if we need to incorporate a thousand more details or how that maps on how you think that a deep reinforcement learning model might need to be adjusted architecturally and or in any other way to map on to something species specific like drosophila.
*  In the mushroom body as an example.
*  Yes.
*  In the mushroom body, there are these other axes of heterogeneity across different compartments, each of which, you know, learns with its own particular dopamine-dependent signal.
*  These include compartments that are involved in short-term memory versus long-term memory, both novelty versus reward or aversive learning.
*  And even some types of reward, sugar or something else.
*  And I really like the distributional story because it's kind of introducing one axis of variation here, but it implies it seems like there are at least, you know, three or four others axes of variations.
*  And then kind of need to think about systems that are each learning a slightly different thing and then somehow combining each of these different predictions into a co-cariot action.
*  And, you know, we have a connectome which we are beginning to correlate with these behavioral and functional heterogeneities.
*  So I think there's a lot of work to be done.
*  Does structure matter?
*  So in an AI agent structure is less important and you just kind of throw the world at a big model, right?
*  And it can learn those associations.
*  But in something like the mushroom body, the architecture is very specific.
*  Do you need specific structure in an AI model to derive experimental predictions in something that is much more architecturally specific?
*  And this is for everyone, not just Ashok.
*  Yeah, I'll just start.
*  I think one thing that's interesting about the mushroom body is at least its factory representation is among the more unstructured and applied brain.
*  It has this kind of random heterogeneous connectivity.
*  At the same time, there are these separate systems for visual input or for thermo sensory input and these reflect some kind of, you know, evolutionary optimization of exactly what kinds of information should be combined when in order to do what a fly should do.
*  So I think the answer is, yeah, we do need to think about these architectural optimizations if we're going to map onto the behavior of a particular animal.
*  Do you, Rodent experimental modelists, do you guys agree?
*  Armin, Elana?
*  Well, if I understand the question, it also kind of relates to the point that was brought up about evolutionary learning versus development learning versus task learning, which are, of course, very, very hard issues, which again makes me less excited about the whole initial learning question in the first place.
*  In the context of these deep networks, but I mean, I think it's a really important point.
*  And I do think adding more kind of anatomical constraints to models is clearly the direction the field should go in all of neuroscience.
*  I think as the connectomes becomes available in more species, that is going to be really exciting to understand what are the constraints that it gives.
*  But there's also just, I think, this bigger, deep challenge about the different levels of learning and how we can seriously think about them is pretty challenging as has already been discussed.
*  So the question here that I think Ida would probably the best to answer. It's for Ida's view that the reward maximization has limitation with the homeostatic RL.
*  Would there be any RL model with an agent's internal set point or internal state dependent modulation of value, rather than context from the environment?
*  And along those lines, how could the multidimensionality of value map or internal drive like thirst versus hunger be computed in the AI agent?
*  Excellent question. Something I am actually working on. And I just want to also acknowledge paper, two papers by Kara Mati and Goodkin, where they use the RL framework to address homeostatic learning.
*  And they indeed this sort of have this idea of an internal landscape of your homeostatic state, and they assume kind of a simple sort of surface for it.
*  But then if some internal sense of where you are compared to that ideal point, your distance would translate into drive towards action.
*  So they have a wonderful sort of theory there. However, it's still within the framework of RL.
*  So it hasn't completely moved towards using this idea of homeostatic learning as opposed to reinforcement learning to manage it.
*  So there the idea is to minimize the distance, for instance, between this internal actual state.
*  And going back to the wonderful point that Ashok was mentioning with regards to different dimensions of reward here, they consider two, but it's generalizable to multiple, which they consider, for instance, sugar and temperature.
*  And then they simulate some results from rodent data. It was first the NERDS paper and then an eLife paper.
*  And then there was another paper I recommend people to look at it. But there are other ways to consider how rewards evolve or how this internal landscape evolves over time, for instance.
*  And there, for instance, we are using this idea of meta learning, applying it to homeostatic meta learning.
*  So that's one way to go forward. Somehow across evolution, we have meta learned some internal landscape, homeostatic landscape, which is not representing the world, but it's representing some internal states that corresponds to the scarcity or presence of various dimensions of rewards in the world.
*  And so I think there is wonderful work to be done there. If I remember the entire question completely, I would love to hear also from Matt and from others what they think about these competing dimensions of reward that I think to the extent that they think
*  that I think to some extent Ashok mentioned and in some situations, for instance, if I'm dying, if my sugar is in a particular state, I need to predict how long I have to replenish it without dying so that I can go to sleep.
*  If I go to sleep and I'm going to sleep for five hours, but then my sugar is going to get depleted, I'm going to die in two hours, I shouldn't go to sleep. So even if I'm very sleepy.
*  So there are many situations where animals need to decide with these kind of competing situations by predicting their own homeostasis within a particular time given they take one or the other action.
*  It seems super complicated and I want to hear from everyone. What kind of architectures what kind of circuits they think allows for this and I guess in their software might be easier because you have all the connective and you know all the dimensions and it might be harder for
*  But I do wonder what everyone thinks about how that is sort of managed. Obviously, dopamine has been around way early in the evolution before animals like get way earlier than the species we are sort of analyzing.
*  So I wonder also what would be the role of dopamine in this, which seems to be maybe a little less dimension specific. It might be. I don't know what you guys think actually there are different dopamine for different dimensions of reward.
*  If there is a way that it kind of credit assigns to those dimensions or access as Ashok was saying to solve the problem. What is the computation that decides between them. How does it forecast into the future my homeostasis state.
*  Wonder what you all think.
*  Okay, I let me kick it off just with a high level comment about deep RL people people approaching intelligence from an AI perspective tend to have a bias toward generality like the you know there's this term.
*  AGI artificial general intelligence people want learning systems, including deeper all systems that are you know have have the least commitment to some particular problem domain and our general purpose in that way.
*  It's tricky though because you know in machine learning there's this no free lunch principle which says that in a sense it says the opposite as intelligence is sort of proportional to the degree to which you commit to a particular range of environments.
*  And of course animals do commit right like fruit flies are good at being fruit flies like their brains are designed to solve the problems that fruit flies face.
*  There's nothing general about the need to keep your glucose level up when you have a certain metabolic rate. That's a very very specific problem. So a brain that's optimized to deal with that or to solve say foraging problems is not a general purpose intelligence.
*  And this is this along with the very related evolutionary learning point that came up earlier is a major disconnect between between studying biological systems and the kind of approach that people take in AI.
*  And this is I think even true of humans. Humans are like we seem much more general purpose than say fruit flies but we're good at dealing with problems that have a particular kind of generic structure which is a kind of compositionality.
*  And we're stuck with certain representational formats. If you permuted our rods and cones we'd be blind. You know we really our brains work under a certain set of assumptions.
*  And I think that's important to keep in view and it's relevant to the kinds of issues you're raising. Ida.
*  Anyone else want to jump in and comment. I think the question from from Ida are very very interesting. It has been very hard to actually translate those experiments the homostatic experiment into a type of recording that we do in the system given the long time scale of that type of behavior.
*  And we think about those those homostatic situations they are developing over hours and days. Right.
*  And I think these are really really interesting questions to address now that we have the tools for addressing those questions to move towards the kind of the internal state of the animal and bring that into the into the studies of learning and decision making.
*  But on the role of dopamine on this I think it's it's still a very open question. So some years ago we did experiment in which we were changing the properties of reward from one type of the juice to the other type of the juice from one magnitude to the other magnitude or the probabilistic versus safe juice.
*  And in the recording that we were doing a dopamine at that time we got to the conclusion that it doesn't really matter for dopamine what exact properties those rewards have as long as anyone is liking them as long as you can see the revealed preference of the animal then the dopamine neurons are showing up.
*  But that doesn't really exclude the possibility of having subset of these neurons doing a specific computation for a specific reward and paying attention to the properties of those reward considering the internal and homostatic state of the animal.
*  Yeah, and also, at least my thinking and I think consistent with what Armin just said is, I was very struck by a paper that came out, maybe in the last couple years from the Dysrath lab where they made the animal thirsty optogenetically or just, I guess, or stated them one or the other and they got like, entire brain change representation.
*  So I think the state representation is everywhere so you don't need it in the dopamine system in any way shape or form. Not to say it's not there. It couldn't be there, but it has there hasn't been super compelling evidence so far that it is there as far as I'm aware, and certainly it's everywhere else.
*  So those two pieces together, yeah, make me lean to that view that at least the type of reward isn't dopamine neurons aren't super specialized for the type of reward but the state representation, internal state representation is part of the state representation everywhere so it's very easy to do internal state dependent reinforcement learning with that like, you know, rest of the circuit for dopamine to work on.
*  So Matt in your talks, you often talk about how you guys have been working on deep reinforcement learning system. And then you thought, huh, maybe the brain does this way. Where could it, where could it do that do it this way in the brain.
*  There's a question from the audience that I'm going to kind of morph I guess. The question is about whether a deep reinforcement learning system could come up with solutions that are just completely unrecognizable in brains that that could either change the knowledge change the nature of the way that we think about how brains do things, or we just may not have a touch point with.
*  Or is it are the deep reinforcement learning models constrained enough as they are since they're made of artificial neural networks and reinforcement learning system that they will be within the space of possible solutions that they will be able to map any solution they come up with onto some algorithmic level or computational level and or implementation level in the brain.
*  I mean, I think I think I think it's definitely possible for artificial neural networks to arrive at solutions that will be very unbrain like. But the problem is it's very hard to know when you're looking at that. I mean, there are some, the cases where the cases where things are very unbrain like are are very different from what we're used to.
*  And I think that's the problem. I think that's the problem. I think that's the problem. I think that's the problem. I think that's the problem. I think that's the problem. I think that's the problem. I think that's the problem. I think that's the problem. I think that's the problem. I think that's the problem. I think that's the problem. I think that's the problem. I think that's the problem. I think that's the problem. I think that's the problem. I think that's the problem. I think that's the problem. I think that's the problem. I think that's the problem. I think that's the problem. I think that's the problem. I think that's the problem. I think that's the problem. I think that's the problem. I think that's the problem. I think that's the problem. I think that's the problem. I think that's the problem. I think that's the problem. I think that's the problem. I think that
*  they don't really deal with the word by word. At least some of them don't deal with the one word at a time sort of causal, causal sequence. And that's just obviously not brain like. So, you know, right from the setup that you're dealing with something that doesn't really address the way that the brain handles language. On the other hand, there are a lot of cases where something cool is going on in an artificial neural network. And you're just not sure whether it's
*  brain like or not. And that those are the cases where I think these systems offer themselves as interesting like testable hypotheses. So the same this also happens in large language models. I'm sort of fascinated by these models because transformers have an architectural bias. They have a particular structure that encourages compositional computation and allows
*  deep learning systems to generalize in ways that they didn't before. And I look at that as a cognitive scientist and I think, oh, we've been wanting neural networks to do compositional computation for decades. And now we have a way of doing it. That's amazing. Maybe that has something to do with the way the brain does
*  computation. It does compositional computation because we know it does. But I don't know looking at these transformers whether the solution in those models is really the same in any even in any abstract way as the solution that the brain is finding. And that's just that's where research comes in. You just have to ask and find out.
*  I do want to ask as we are closing in on time a little bit, but there's an I don't know exactly how to ask this. I want to ask each of the panelists in your daily work as you're making models as you're thinking about the architectures and specific needs of the species that you're working with. Is there anything lingering in your minds that you think deep reinforcement learning really doesn't address this particular thing?
*  And if so, do you have insight on what you would need from a deep reinforcement learning approach? How it would need to change to address that lingering thing in your mind? I guess deep reinforcement learning has solved at all, perhaps reward is enough.
*  I can start. So I think there's two things that I think, well, three, I would say three things that I would like to see more in DL. I think that deep RL or I think that at least those are the directions that I'm working on. So maybe I'm biased. But one thing is something that Matt already mentioned and others already mentioned, which is architecture. And I do think comparing different architectures and that using that as a means of understanding the different aspects of the model.
*  So it's either of comparing, developing and comparing different architectures for cognitive cognition in biological agents, or whether it is for solving different tasks. It's a big part of it. And it's not that even in even in deep learning for AI purposes without a care for biological agents, architecture matters a lot actually, whether it's for sample efficiency, whether it's for what kind of problems are possible to solve, whether it's for can you remember how much can you remember given your memory and sample size of the events you will experience in the world are not a matter of how much you can remember.
*  There is so much to be talked about about architecture and algorithm, even in the absence of the relevance to biological creatures, but even more so for us who are cognitive neuroscientists.
*  The second thing I would say is actually something that we got accepted and it's going to be out at ICML, which was like my first paper at Microsoft Research, which we call interaction grounded learning.
*  In much of the situations biological agents do not move around the world where things have a reward tag. So and there is no programmer God who provides a reward function in the world, we really have to learn an interaction with the world and it's really noisy.
*  And so we took a first step, the first theoretical step and a sort of a basic demonstration that we hope to follow up on for interaction grounded learning. And I think that doing more work on situations where rewards are not labeled or provided can the new generations of reinforcement learning can handle that it's not an entirely different field to think about reinforcement learning without rewards, so to speak, where the agent in interaction with the world needs to ground or define its own reward somehow.
*  And the third thing that I would say is again something that I learned from Matt, which is another paper that we got at ICML, which is about human like navigation. If you compare state of the art deep learning algorithms that can solve navigation or pass a benchmark for navigation in an Xbox game that we used.
*  Not all of them look human like so we had humans in a Turing test, look at the behavior of the avatar in the game when it was played by different architectures all of which passed the benchmark, and not all of them look human like, and some looked more human like and we needed to add more architectural components for it to even behave more human like let alone have a human like representation to the next step.
*  So I guess the third part that I would say is that in many applications of the RL which are going to interface with humans we want them to behave human like even if people don't care about cognitive neuroscience I mean I do care very deeply but even for those who only want the applications, they should care about.
*  It's not just passing a benchmark but behaving the same way humans do that includes having errors or having a trajectories that are more human like. And then the next step is what, for instance, Matt was mentioning as well which is solving it in a sample efficient way with sample efficient representations like humans.
*  So I would say these three things with the what I would hope the reinforcement learning would have in the future.
*  One thing that I will add that I think hasn't yet come up that I've wondered about is for is that, as far as I know, when these deep reinforcement learning networks are fit they aren't fit.
*  I mean so they're not fit. They aren't fit to data they're not fit to the neural activity or to the behavior they're just trained to do a task. And that's different from like for supervised learning and for simpler reinforcement learning you know those are actually fit to data and
*  neural activity which makes the link many ways easier and more compelling so it does seem like thinking about ways to fill that hole seems like a major hole to really provide constrained models, literally to constrain the models based on data rather than just like produce a model and see if it matches the data.
*  I love that point, Alana. I just want to mention that there is work fitting behavior. So behavioral cloning is a major area in AI and it's aimed at finding policies that generate some target behavior.
*  Like let's say you have some motion capture data and you want an agent that does that. In fact, the soccer video that I showed was tuned with RL, you know, scoring points being the reward function, but the basic skills like kicking the ball and running were trained through behavioral cloning.
*  And you can apply this readily in neuroscience. So I showed the little model rat running around. That rat was trained with RL but you can also train a rat. You can train that same artificial rat using motion capture from a real rat.
*  And then you have a controller like a recurrent neural network that you can say, well, okay, what's going on inside this recurrent neural network? Do the unit activities resemble what we see say in striatum? And in fact, we're collaborating with Bensie Olvetsky on a project exactly of that kind.
*  While I have the floor, I'll just respond to the original question. One thing that deep RL systems aren't good at that at least humans are is continual learning. Like learning in an open ended way, like collecting knowledge gradually and adding new knowledge to a growing store of knowledge without overriding earlier learning.
*  Many people will be familiar with the problem of catastrophic interference. It's like not a solved problem. So that kind of there's a term lifelong learning that some people are starting to use in AI more and more like that's becoming a goal.
*  And it's we don't know how to do it. I just I'll shut up in a second. But I just want to say something radical, which is the question was, what do deep RL systems, what can they not do that brains can do?
*  I would flip the script and say, like what I'm really proposing is that brains are deep learning. They are deep RL systems. Brains are deep RL systems. They're natural deep RL systems. And they work differently in some ways from artificial engineered deep RL systems.
*  And so the question can be rephrased in those terms, but I'd like to make my own radical statement along those lines.
*  I suppose this is a natural ending with with Matt screaming brains are deep RL systems. So I feel like we're just getting started. But this was fun. So thanks to the panelists are men, Ilana, Ashok, Ida and Matt.
*  Brain inspired is a production of me and you. I don't do advertisements. You can support the show through Patreon for a trifling amount and get access to the full versions of all the episodes, plus bonus episodes that focus more on the cultural side but still have science.
*  Go to brain inspired dot co and find the red Patreon button there to get in touch with me email Paul at brain inspired dot co. The music you hear is by the new year. Find them at the new year dot net. Thank you for your support. See you next time.

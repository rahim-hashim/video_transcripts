---
Date Generated: April 03, 2024
Transcription Model: whisper medium 20231117
Length: 6766s
Video Keywords: []
Video Views: 1045
Video Rating: None
---

# Seeing is Believing with MIT’s Ziming Liu
**Cognitive Revolution "How AI Changes Everything":** [June 27, 2023](https://www.youtube.com/watch?v=VKxwlxb2XWw)
*  If we want neural networks to be interpretable,
*  we should in training explicitly
*  encourage them to be interpretable.
*  That's when we pose this research question,
*  like what kind of training techniques we need to
*  induce modularity in otherwise non-modular neural networks.
*  Actually, all the results I got,
*  I'm just using my Mac M1.
*  There are no GPU.
*  For the modular addition, it takes around 20 minutes.
*  For symbolic formulas, just less than one minute.
*  The existential risk is
*  a common threat to all human beings,
*  and no one can survive if we don't collaborate.
*  With this, actually this can bring together US and
*  China collaboration on this AI safety thing.
*  Hello and welcome to the Cognitive Revolution,
*  where we interview visionary researchers,
*  entrepreneurs, and builders working on
*  the frontier of artificial intelligence.
*  Each week, we'll explore their revolutionary ideas,
*  and together we'll build a picture of how AI technology will
*  transform work, life, and society in the coming years.
*  I'm Nathan LeBenz, joined by my co-host, Eric Torenberg.
*  Hello and welcome back to the Cognitive Revolution.
*  Today, my guest is Ziming Lu,
*  grad student in Physicist turned AI Safety Researcher,
*  Max Tegmark's group at MIT,
*  and first author of the recent paper,
*  Seeing is Believing,
*  Brain-inspired Modular Training for Mechanistic Interpretability.
*  This paper immediately stood out to me for three big reasons.
*  First, any work that makes deep learning neural networks easier
*  to reverse engineer and interpret is,
*  in my view, worth celebrating.
*  The infamous black box problem,
*  which in its simplest form,
*  simply means that we don't really know why AIs do what they do,
*  is one of the biggest reasons to worry about what
*  more powerful AI systems might do in the future.
*  Personally, I see mechanistic interpretability work
*  as one of the most promising paths to AI safety.
*  Second, the technique in this paper is
*  conceptually simple but nevertheless profound.
*  Taking inspiration from biology and the practical physical constraints
*  that favor local connections and
*  modular structures within animal brains,
*  Ziming devised a straightforward modification to the loss function
*  that encourages the development of similarly modular structures
*  in digital neural networks.
*  I suspect that this technique,
*  perhaps more than any other I've seen so far in 2023,
*  left many in the AI research community asking themselves,
*  why didn't I think of that?
*  Finally, as the title, Seeing is Believing, suggests,
*  this paper includes phenomenal visual aids,
*  which very quickly and intuitively communicate both the core ideas
*  and the results while also inviting deeper study.
*  Given how much I understood at a glance,
*  I was really pleased with how much more I learned by digging in
*  and exploring some of the important design decisions and trade-offs
*  that Ziming made along the way.
*  Because this work is so visual, we've taken the extra step
*  of showing the figures in the YouTube version.
*  So if it's convenient, I would encourage you to watch this one on YouTube.
*  If not, you can definitely still get the bulk of the benefit
*  by following the links in the show notes to the GitHub page,
*  which has all of the important animations,
*  to Max Tegmark's announcement tweet, and of course to the paper itself.
*  Just a couple minutes spent looking at the animations and the images
*  will do wonders for your understanding of this discussion.
*  As always, if you're finding value in the show,
*  we'd appreciate it if you'd take a moment to share it with friends
*  or leave us a review.
*  We'd also welcome your guest suggestions either by email at tcr at turpentine.co
*  or via Twitter DM where I am at Levenz.
*  Now, I hope you enjoy this illuminating conversation about neural networks
*  made sparse, modular, and interpretable by design with Ziming Liu from MIT.
*  Ziming Liu, welcome to the Cognitive Revolution.
*  Yeah, thank you for the invitation. It's my pleasure.
*  Very excited to have you. Pleasure's all mine.
*  You guys have published this really interesting work,
*  Seeing is Believing, brain-inspired modular training for mechanistic interpretability.
*  And you had me at mechanistic interpretability,
*  but especially when I saw the visual that you guys posted on Twitter,
*  it's so rare to see in AI, you know, a mechanistic work
*  that you can kind of absorb and really start to get an intuition for
*  in just a few seconds.
*  Immediately, I was like, I need to read this paper in its entirety.
*  And obviously now here we are to dive deep into it.
*  So great job, very exciting work.
*  You started off with this question,
*  what training techniques can induce modularity in otherwise non-modular networks?
*  Maybe we could just start there and you can tell us about kind of the motivation
*  and how you came into this line of research.
*  We all know that deep neural networks are successful, but hard to understand.
*  So to interpret neural networks, we kind of hope that neural networks can
*  be decomposed into different modules.
*  And like we divide and conquer.
*  Once we decompose, we divide networks into smaller parts like modules,
*  then they are more amenable to interpretability.
*  But we kind of rely on the analogy to human brains,
*  where in brains, different parts of our brains are responsible for different functions.
*  But what's different for biological versus artificial neural networks is that
*  artificial neural networks do not have incentives to become modular.
*  By contrast, biological neural networks have evolutionary reasons to become modular,
*  because modular brains are more energy efficient than non-modular brains.
*  That's why modular brains have a selective advantage in evolution.
*  And we human beings today have modular brains.
*  So the philosophy is if we want to make neural networks,
*  artificial neural networks modular, we should in training explicitly make them modular.
*  Or to even generalize beyond modularity, if we want neural networks to be interpretable,
*  we should in training explicitly encourage them to be interpretable.
*  That's when we ask this research question, we pose this research question,
*  like what kind of training techniques we need to induce modularity in otherwise non-modular
*  neural networks.
*  And also borrowing the lesson from biology, we ask why our human brains are remarkably modular
*  is because this is closely tied to locality.
*  Because our brains, of course, we all live in the three-dimensional space,
*  where you can define distances.
*  And to create neurons in your brains, you need energy to create neurons,
*  to maintain them and also transmit signals.
*  So local neural connections tend to be more energy efficient than non-local ones.
*  So the lesson we learned from our human brains is that locality gives rise to modularity.
*  And that is the key trick we used.
*  That's a key strategy we used in the BIM paper, where we explicitly embed the network into a
*  geometric space where you can define distances.
*  And we have a penalty proportional to the length of the neural connections.
*  We penalize non-local or long neural connections more than short or local connections,
*  just to mimic these evolutionary effects to some extent.
*  That's the basic idea of it.
*  You definitely want to look at some of the artifacts from this paper.
*  As the title suggests, seeing is believing.
*  So the audio-only form here almost can't possibly do this work full justice.
*  But the good news is you can probably spend five minutes looking at the key figures.
*  And then they're simple enough and striking enough that you can absorb that information
*  and keep that image in mind and then go listen to the rest in audio form,
*  if that's what you want to do.
*  So definitely do that.
*  But just to restate key ideas.
*  So obviously, we as people and as biological beings exist in space,
*  we have this three-dimensional problem to solve how do we get the most bang for our buck out of
*  a certain size skull.
*  And that naturally means there's going to be a cost imposed on having super
*  long-range connections across the brain.
*  If nothing else, it's going to just clog up space to do that.
*  But also the cell has to get bigger.
*  It seems like it might be more susceptible to damage or supply chain issues, so to speak.
*  And so it makes sense intuitively that most of the brain activity would be local.
*  And then we also see that the brain activity is modular in that there's these particular parts,
*  which seem to be fairly clearly...
*  The boundaries are fairly clearly defined between them in many cases,
*  where this part does something and this other part does something else.
*  In contrast, though, neural networks as they've generally existed just have this concept of layers,
*  but there's not any sort of spatial meaning that is given to those layers.
*  So whether two neurons or activations or positions in the network,
*  you have the same index or are very far from each other in a layer,
*  that has never really been something that has been taken into account in the process of training.
*  Whatever connections happen to form at the beginning, those are the ones that
*  continue to be built around and refined.
*  And that's why we get spaghetti-looking networks.
*  Yes. Normally, the artificial neural networks we used normally before is we treat them as
*  topological objects.
*  So sorry for being a little bit mathematical, but for topological objects, there's no numeric
*  measure to evaluate how close these two points are.
*  We only care about whether two things are connected, whether two nodes are connected by an edge or not.
*  However, if we go to geometric space, for example, the 3D Euclidean space that we live in,
*  we have the privilege to define distances.
*  So actually, the switching from normal neural networks to BIMP is just switching from a
*  topological space to a geometric space, so to speak.
*  Yeah. I thought this was a really interesting concept in that it's ultimately a pretty simple
*  and elegant one where you describe it simply there.
*  It's moving from this topological conception to a more literal spatial conception.
*  And then if I understand correctly, the modifications that you're making to the loss
*  function are also pretty simple.
*  Right? In terms of the code, we're probably talking about just not even that many characters
*  of additional code to ultimately define that there is a link and now it's going to be counted
*  against you.
*  Yes. So basically, we want to sparsify the network so there is this L1 regularization.
*  So naturally, even if we just do L1 regularization without this locality trick,
*  you would require one hyperparameter, which is the penalty strength.
*  So on top of that, we just have one additional more hyperparameter, which is how much you want
*  to encourage locality.
*  So it's simply just L1 regularization, but it's distance dependent.
*  And the only extra hyperparameter is the locality strength.
*  When you put that locality strength to zero, you recover the VELINA L1 regularization.
*  When you put A to be large, you encourage more locality.
*  That's really simple implementation code.
*  L1 regularization is, again, motivated by the same thing.
*  We want to make the network sparse.
*  We don't want to have wasteful, needless extra connections.
*  So let's just penalize, in this case, the weight itself.
*  Right?
*  We want to optimize a loss function that includes both prediction accuracy,
*  but now we're adding on to it.
*  And we also want to minimize the total weights in the network overall.
*  So all of the weights themselves get summed up into that loss function.
*  And therefore, when we take the derivative or we find the gradient,
*  they're all naturally incentivized to go down.
*  All the weights naturally tend down at every step.
*  Yes.
*  So the loss landscape would look like, for each weight, it looks like an absolute value
*  for the L1 penalty.
*  So it has this incentive to go down to zero magnitude,
*  except that the prediction loss can also drag you somewhere else,
*  but the penalty terms drag you down to zero.
*  Right.
*  So only over rounds of gradient descent, only those weights that
*  actually contribute to prediction accuracy enough to offset the weight that they,
*  no pun intended, the weight that they are carrying against the loss function
*  actually survive and everything else just gets gradually proved back to zero.
*  So that's kind of traditional L1.
*  And now you're adding on this additional parameter on top of that,
*  that is, and you're doing both, right?
*  So you're penalizing the weight itself.
*  Is it multiplied by the length?
*  I'm not the best notation guy.
*  So as I was reading the paper, I wasn't a hundred percent sure of all that.
*  It's multiplied by the distance, say for layer I and layer I plus one,
*  the closest two neurons, the closest connection are still non-zero.
*  So it's like every weight has a non-zero distance.
*  So got pruned even if it's the most local connection.
*  Gotcha.
*  So like the minimum would be one if it's the same like index in the layer from one to the next,
*  but the more distance there is across the layer.
*  And again, go look at the figures in the paper.
*  Well, I guarantee you will really help make this much, much clearer.
*  Customized across all platforms with a click of a button.
*  I believe in Omniki so much that I invested in it and I recommend you use it too.
*  Use Cogrev to get a 10% discount.
*  So basically they can get, the penalty can get stronger as the proportional to the length going up.
*  Yeah. So if you go straight, for example, if you go straight from this neuron
*  to the nearest neuron in the next layer, the penalty is like one.
*  But if you go, if you have some certain angle, then probably the penalty is two.
*  And then if you further tilted away, maybe it becomes three.
*  So the network have the incentive to make only the most local connections non-zero.
*  And then just for completeness in this regularization, there's also L2 regularization.
*  And that is just a little bit less aggressive version because instead of adding the weight
*  itself, you're adding the square of the weight and that would tend to make a smoother curve around
*  zero. So you're not kind of pulled as hard to zero. And so you get maybe a little less
*  sparsity with L2 than with L1.
*  My experience with L2 is that it will shrink the overall weight norm of all the parameters,
*  but not necessarily push down one single parameter to really close to zero so that you can really
*  ignore it, turn it away. So like they are, well, I think they're engineering tricks that if you
*  really care about pruning, you should try both. They have their own advantages and limitations.
*  L1 sometimes have optimization issues because when you really get down to zero, you bounce back and
*  forth. But with L2, as long as your step size is smaller than some threshold, you converge steadily
*  towards zero. But also for the reason I mentioned before, L2 does not encourage one single parameter,
*  really drive it to zero, but encourage all the parameters overall have a smaller weight norm.
*  So they're like this kind of trade-offs you want to try when you do engineering.
*  So you run the process with everything that we've described so far. So there's this balance between
*  all the weights are tending to zero. The weights that have a long distance on the connection
*  are particularly trending to zero. But of course, the prediction accuracy itself is
*  maintaining some weights up because you need to make good predictions. And so you run this and you
*  do indeed find and you show these images of sparse networks. But then you add this additional concept
*  of neuron swapping. And that kind of takes the outcome from like sparse to sort of sparse, but
*  also much more symmetrical, much more aesthetic, much more elegant. How did you come up with this
*  idea of swapping? And then we can get more into understanding it as well.
*  Sure. So there's an anecdote behind it. So when I first tried modular addition without swapping,
*  the networks looks a little bit like 3D DNA, the double helix, but projected to 2D.
*  So it looks something like this. It just swaps and then swaps back. So I was about to try,
*  so I was thinking if I make this neurons movable, make their embeddings trainable,
*  I should be able to avoid this so-called topological problem. But then I asked my
*  advisor Max Tecmark and he asked me to try something simpler, as simple as possible.
*  And so he suggested that I try the swapping thing. That sounds like the simplest thing we could try
*  that can solve this double helix problem. So it turned out working pretty well. So that's why we
*  end up using swapping, but potentially one could also imagine, try, make those embeddings trainable.
*  And also in hindsight, we think that sometimes your inputs and outputs do not have a natural,
*  you don't have a preferred ordering of your inputs and outputs. You want an automatic way,
*  you want your neural network to determine which kind of order you want. Perhaps you don't want
*  to pre-specify the ordering. So this is a really contrived example, but if your task is just swapping
*  two numbers, so your input is X and Y, X on the left, Y on the right, and then your output are Y and X,
*  Y on the left, X on the right, then your neural network would have two really long connections
*  which also cross each other. Well, this is okay, right? Because you can imagine, because you can
*  understand what's happening, but it's not aesthetic. We want everything to become local and modular.
*  So naturally we want to swap these two things, either the input or the output, to make them,
*  to make the connections as short as possible. Just go straight to where it should go. Yeah,
*  that's the philosophy, I think, behind swap. But for some tasks, we find that swapping does not help
*  that much. It's basically just reorganize things a little bit so that the pictures look better.
*  But for other cases, it indeed help, even help neural network training. It helps us get lower
*  training laws. Because you can imagine if without swapping, your neural network
*  gets stuck at those weird double helix structure, and so you have a large penalty.
*  A large penalty can, you know, there's a trade-off between prediction loss and your penalty.
*  A large penalty means that you need to sacrifice the prediction loss. So if you can swap this
*  neurons cleverly to get a more local connected configuration, your penalty drops down, which means
*  even the same penalty strength, you can get a better prediction loss. So there's this
*  hyperparameter like how frequently you do the swapping. I think I just tried it to be,
*  I just set it to 200 or set it to infinity. But you could imagine that maybe there's a face diagram,
*  face transitions, like as in physics, when we talk about ice, water, and gas, right? When we
*  tune these hyperparameters, maybe there are different phases that can be emergent. Yeah,
*  but right now I just set them to be something simple, but more things to be done in the future.
*  And again, just to be super explicit, the process of the swapping is basically, okay, we've been,
*  every so often, every however many steps in our training process, we add an additional step,
*  which just goes down the layers and compares, not even compares, but takes two different
*  neuron positions and essentially says, would loss go down if I just flipped the position of these,
*  where loss is already reflecting the length penalty. So you can just do a bunch of pairwise
*  comparisons and find those enhancements. And essentially it sounds like that is,
*  it's more of an aesthetic, as you said, it's also kind of helping you not get stuck in local minima.
*  Because, and I guess how those local minima would potentially form would be like,
*  you have, you reach some kind of stable place where the prediction is pretty good and the length
*  of whatever the structure has kind of settled into, the length could be shortened, but there's
*  not really a mechanism other than the swapping to shorten the length if the other weight isn't
*  helping with prediction just yet. A weight that's not active, I guess a weight that's not
*  active can basically not really be turned back on in this scenario, right? Is there a...
*  We only care about important weights in the sense that have a large value. So actually we
*  attach each neuron a significant score, an important score, and we only care about swapping
*  the top 10, say, important neurons with other neurons to see if such swapping can reduce
*  locality loss. Yeah, and also we constrain, like we only swap two neurons in the same layer,
*  such that the prediction loss remains the same, but the locality loss may change,
*  and we want the swapping that would reduce the locality loss.
*  And the prediction loss would stay the same by definition or no? Am I missing something there?
*  Oh, the prediction loss remains the same by definition. When I say I swap two neurons,
*  I actually also swap in the incoming and outgoing weights. So basically the computational graph,
*  topologically speaking, remains the same. So the function, so the whole neural network as a function
*  remains the same, but it's just geometrically speaking, it changes.
*  So that's true at that step, but within the broader optimization process, it can still help
*  achieve better end performance because you are applying less of it. You're helping it kind of
*  apply as little length penalty as it can along the way, essentially.
*  Yes, so that at single point when we do the swapping, the prediction loss remains the same,
*  but in the long term, having connections in the right place, we encourage the network to
*  decrease prediction loss. Otherwise, if the network got stuck at local, some bad local
*  minima configurations, this would have a negative effect on the prediction loss.
*  This feels like something when I saw it, I was like, why did nobody do that years ago?
*  Do you see this as something you also feel that way? Why did nobody else think of this sooner?
*  Or was there some unlock that you think made this kind of an idea whose time has come now?
*  Actually, there are literature, although when we wrote the paper, we are not aware of
*  those related papers. So like 10 years ago, Jeff Kuhn is an expert in this, but like their papers,
*  he and collaborators, their papers basically focus on the biological side. They evolve their
*  tiny networks with evolutionary algorithms just to mimic what's really happening in biological
*  evolution. Well, they have some follow-up which extended to gradient-based methods, but still for
*  like in different setups. So first of all, the previous works did not properly leverage, or at
*  that time, the machine learning or gradient-based methods are not as popular as it is now. So we're
*  integrating the current machine learning tools. Secondly, we have different focus. Our focus is
*  for doing mechanistic interpretability to understand how neural networks work internally.
*  And again, as I said, they care more about how modularity emerged from biological systems.
*  So I would not shamelessly say that this is a totally novel idea. Well, we always stand on the
*  shoulders of people before, and they're like clever minds we always learn lessons from. But
*  still, we're in this different setup. And we also integrate like these new tools available
*  only recently in the machine learning community. As long as it's a useful tool, I mean, there's no
*  harm. We rediscover things, right? Because we find it's valuable things. Only really valuable
*  things can be rediscovered and rediscovered over and over again. Yeah, that's it. I wouldn't say
*  that this is totally novel, but it still has some contribution, I guess. Everything's a remix.
*  But this had a feeling of kind of, I bet a lot of people saw it and thought, why didn't I think of
*  that? Because it just feels so once you especially when you see that animation, it's like, man, I
*  definitely should have thought of that. So maybe it's more than I'm reacting to how compellingly
*  the final result has kind of been packaged up and communicated in terms of the density of that
*  realization than anything else. But it certainly creates that feeling.
*  I see. Yeah. I myself was really shocked when I got the results when I actually see those
*  connectivity graphs. I was shocked how possibly a neural network can do this complicated thing
*  with such spars and modular networks and everything. Actually, because we are actually
*  using this locality trick. And I'm a little bit worried that locality is not exactly modularity.
*  But it works. So there's still a lot of things unexpected here. Even if I,
*  we first came up with the idea, we're still not sure whether it can work on this examples,
*  what we will end up. And when I first see that, you know, the really sparse and modular graphs
*  for those symbolic regression paths, I'm like, oh, we are really onto something. And we should
*  really dig deep into it and try a lot of examples that people already have tested in Macinturp and
*  make it a real thing. So yeah, it's a lot of surprise along the way. So a couple little
*  follow ups here, because in particular, I definitely want to dig in a little bit on the
*  distinction between locality and modularity. And then I definitely want to get into also like the
*  things you actually did and kind of understanding, you know, now what can we interpret out of all
*  this? Just one more little follow up on the swapping. Does it seem likely to you that
*  the swapping is like more valuable at the beginning of the training process? Would you
*  expect that like front loading those swaps would be more useful than like late in training swaps?
*  That's exactly the opposite of what I'm hoping for. Yeah. So right now I'm thinking of applying
*  BIMP to pre-trained large language models. So what I hope is that I can just take pre-trained
*  large language models, like at the end of the train, at the end of the pre-training
*  and apply BIMP, just, you know, do a little bit fine tuning because maybe we don't have the compute
*  to do that. So hopefully the swapping would be most valuable for, you know, at the end of the
*  training. But since you were brought up the point, I got a little bit concerned. Maybe I tend to agree
*  with you that maybe swapping is most valuable for, you know, at the beginning of the training when,
*  you know, at the beginning of the training, there are like many lotristic directions you can go
*  and swap in. It's the time that the neural network needs to decide which way you need to branch
*  which lotristicet you want to branch into. And after you branch into that basin of attraction
*  or lotristicet, so to speak, swapping becomes no longer important because you're already in that
*  basin. You only need to, you know, row down to that bottom. You don't need to select which basin.
*  So yeah, but that's just my conjecture. We'll see how it works on language models.
*  I'm sure you've looked at like the Git rebasin paper had sort of a similar concept of, I think
*  they called it kind of confusingly aligning the model and there was some sort of
*  swapping mechanism that kind of, you know, was meant to like take two, you know, same shape
*  networks, train on different things and somehow kind of align them to each other so they could be
*  merged. Yeah, I'm a bit like for the Git rebasin paper, I think there's a follow-up paper which
*  contradicts the idea of Git rebasing called mechanistic mode connectivity. So if a network
*  has multiple mechanisms to do the same thing, for example, module addition, you have many group
*  representations that can achieve the same goal, then actually you cannot make two, you know,
*  by just swapping two neurons, by swapping neurons to make them equivalent and that's also observed
*  in my code. Well, this may not be something relevant, but it's interesting to note that when
*  I run the modular addition example, I should, to make my code reproducible, I should really set
*  the precision to be double precision numbers. Even for float position numbers,
*  like the truncation errors can dominate. Like this kind of noise is large enough to
*  make you go to another basin. This is, yeah, so like there are exponentially many equivalent basins
*  there, so this is like this permutation symmetry that makes the, you know, the neural loss landscape
*  very complicated. Yeah, just a note, if you want to make the codes reproducible, you need to use
*  the double float instead of the, you know, the double precision numbers. And is that 64? How many
*  digits is in that? 64, yeah. Yeah, so if you were to round down to, you're saying even at 32 digits,
*  it still has this problem or? Yeah, that's problem specific. Like only for modular addition and
*  permutation symmetry, like for the algorithmic datasets, you need to set it to 64 digits because
*  additional to neuron permutation, you also have this, you know, representation equivalence.
*  But for other tasks like image classification or symbolic regression, there is no such problem
*  because you don't have this, you know, representation problem. But unfortunately for
*  language models, you only need to learn the token embeddings and there they have such problem. I'm
*  not sure if there is any bug in my code, but this is what I found. I need to, for trainable embedding
*  tasks like modular addition or in the future or language models, you need to start
*  use 64 bits to make sure reproducibility. Yeah, that's a little bit unfortunate, but.
*  Modularity and locality then. I was thinking about that. You know, locality obviously
*  doesn't necessarily imply like clear boundaries. I guess that's the simple way I was framing the
*  question. So if you wanted to be more encouraging of boundaries or sort of,
*  you know, separation of concerns, is there a loss that you could conjure up to do that too? Could
*  you sort of count like the number of non-zero weights coming in to a position as part of the
*  loss? I'm sure you've thought about this. Yeah, so there are a bunch of off the shelf modularity
*  measure in the literature, especially in graph theory. So the idea basically you want to detect
*  community where you want to separate the whole graph into different sub graphs where
*  intra sub graphs, the connection are quite sparse, but intra inside the sub graph, the connections
*  and against, but across different parts of the sub graph, the connection can should be sparse,
*  something like that. We already have such measures for modularity, but they again, they just defined
*  on graphs, which are topological objects. They're good, but it's hard. It's again, hard to visualize
*  them. Yeah, this is just some preliminary thought. What I'm thinking is maybe we can combine
*  the bin penalty loss with some modularity loss people use in graph theory, something like that.
*  But I'm a little skeptical of this because it's more like an engineering trick.
*  There is not, maybe we can have something more elegant than this, but it's the simplest thing
*  that writes on top of my mind. As cool as this is, we're not at the end of this line of research,
*  that's for sure. Maybe worth checking out the tiny stories project. I noticed that project. That's
*  super cool. You mentioned like the compute budget obviously is a meaningful constraint when you are
*  trying to run this research, probably in any setting these days, but certainly in an academic
*  setting can be a challenge. Their explicit goal was to create a data set that would capture the
*  sort of, I don't think this is a well-defined concept, but the full complexity, let's say,
*  or almost the full complexity of natural language, while also being like reduced vocabulary,
*  relatively simple concepts, three-year-old can understand. Then they were able to get a lot more
*  of the reasoning behavior that we see in larger language models. They were able to get it at,
*  as far as I know, the smallest scale models that I've seen because I think essentially they
*  narrowed the universe of what had to be learned while still preserving the value of learning
*  reasoning in that context. There could be something perhaps interesting.
*  Yeah, this is actually related to one paper by our group led by Eric Michaud called the
*  quantization model of neuroscaling. We have this quantization hypothesis where we conjecture that
*  a prediction task, say language modeling, can actually be decomposed into many sub-tasks
*  called quanta, as in physics. We call them energy quantum. Those quantas, they have different
*  importance. They appear with different frequency in natural language. Presumably, we can order
*  this quanta from the most significant to least significant. We have a quanta sequence.
*  We conjecture that neural network, based on its capacity, would first learn the most significant
*  quanta and then learn it in sequence with this decreasing order of importance.
*  I would imagine that to speak English coherently as a three-year child would only require,
*  say, the first 10 quanta. But to know about, to role play a physicist or say something more fancy
*  than just a three-year-old can, you need less frequent quanta that appear in the tail. That's
*  why you need a very large language model, simply because you need to memorize, so to speak, that
*  kind of facts. But to speak English coherently, you don't need that language model.
*  I just want to mention that the tiny stories also have a connected back to our quantum model.
*  That's cool. I could definitely imagine a reconvergence of these ideas, and it would
*  be really interesting to see if you could actually start to get a visual on the different...
*  I've been using this term, reasoning micro skills, to emphasize that they're, at least as I'm
*  imagining them, they're very discrete, probably very small little modules that do very specific
*  tasks and kind of ladder up to more general purpose reasoning. But it seems like what they see,
*  and I guess this makes sense given what we understand about the mechanisms of training,
*  is that super specific things like negation kind of seems to come online as a discrete skill,
*  a discrete skill in superposition, obviously with a bunch of just memorized stuff and
*  baseline priors. But it seems to kind of brock these very, very specific little skills in kind
*  of a discrete way. So yeah, fascinating. Let's get to then some of the results. So just to recap,
*  see if I can do this briefly. You say, hey, we've built neural networks, digital neural networks
*  for the last 10 years on a sort of very loose biological inspiration. But one of the biological
*  realities that we've not really taken inspiration from is the fact that the larger the distance
*  between two neurons in like a human brain, the harder it's going to be for those cells to connect
*  for very just practical physical reasons. What if we kind of take that same concept and bring it back
*  to the machine learning context that turns into an additional penalty that corresponds to the
*  length of a connection between neurons. It gets thrown into the loss function. You re-optimize
*  around that. You find that you're getting much better sparsity. But then you also realize, hey,
*  I can sometimes get stuck in these kind of local minima. So I'll add this swapping concept to come
*  along and kind of untangle and help me kind of skip out of some of those local minima. And therefore,
*  we can both get great performance and kind of aesthetic, organized, almost crystal-like
*  structures that we can visualize at the end. You start off, there's kind of a series of
*  experiments. The first one, and again, make sure you look at these things. It will help tremendously
*  to see them. The first things you're doing are these symbolic formulas where basically you're
*  taking a few variables coming in. And then it's the job of the network to predict function output
*  values based on those input values. And it's presented as symbolic functions. But I was a
*  little confused by that because to the best of my understanding, at the end of the process,
*  the network itself is just numbers in, numbers out. Is that right?
*  Right. So we synthesize the data set with symbolic functions, but we actually
*  input x and y, numeric values, and output s also in numeric values. But f is pre-computed
*  as a symbolic formula of x and y. So yeah, numbers in, numbers out. Everything numeric.
*  Again, look at the graphs. But in each case, you're kind of demonstrating this
*  conceptual sort of congruence, I guess, between the nature of the functions that the network is
*  learning and then the structure of the network that you can look at. So just to be super,
*  super concrete, there is a function or there's a network that's trained on x, one, two, three,
*  and four. So four numeric input values. And then it's trained to predict two functional output
*  values. And I was surprised that they're not like super simple. One is x2 squared plus sine of pi x4.
*  That's one prediction. And then the other prediction is x1 plus x3 squared. So in other words,
*  take two numbers, add them and square them, and then take the other two numbers,
*  square one, take the sine of the other and add that. Okay. That's kind of random. Is there any,
*  should I understand that in any deeper way other than like, you pick two random functions and
*  that's kind of that? Yeah. Yeah. Inventors is the main thing. We want to see that the network can
*  fleet into two parts, two independent parts. And for the functions, we just pick, yeah, we just
*  randomly take it like on the top of my head or like squared functions, cubic functions, sine,
*  square root, something like that, as simple as possible. Okay. So just, I feel like I didn't
*  maybe make that as clear as I could have. The independence concept is that because the two
*  output functions that you're training the network to learn and predict numerically are such that
*  one of those only depends on two of the inputs and the other one depends only on the other two
*  inputs. Then if everything is working according to our initial theory, then we should see that
*  there's just two parallel paths through the network that don't interact at all. And because
*  they don't need to, because information doesn't need to cross in that way. And indeed that is
*  what you see. So you have, presumably due to the swapping, as it's shown in the paper, X4 and X2
*  end up together on one side and they feed directly up to their output function. And then X1 and X3
*  feed directly up to their output function. I guess you probably chose it that way so that they were
*  forced to be crossing initially. And then you see that they uncross as you go.
*  Yes, we deliberately put like X1, two X4, but like the outputs, the first output depend on X1 and X3.
*  The second output depend on X2 and X4. We deliberately want to test if the swapping is
*  effective enough to swap the inputs such that they group into the correct group.
*  We are happy to see that it indeed works. And they're extremely sparse. So these are literal
*  graphs, right? There are just two layers in the network that is trained to do this task.
*  Yes, and I did do the test. So I indeed do some pruning test. One might suspect that those
*  connections you cannot see can actually contribute a lot, but that's not the case.
*  I literally plot every weights, but the thickness of that connection is proportional to the magnitude
*  of the weight. So if you don't see it, this means that the weight is too small for the naked eyes
*  to spot. And if I deliberately set those small weights to zero, the output of the network
*  is not affected at all. This means that this is not a visualization stuff that makes you feel
*  like they're small, but they're still contributing. It's not that case. They're not contributing,
*  and they're indeed zero, close to zero. That's fascinating. And I'm left feeling like
*  this is a eureka breakthrough in the sense that, oh my God, look how simple the structure is.
*  And in this particular case of x2 squared plus sine of pi x4,
*  it is really just a couple of neurons that are doing the job, right? There's the two inputs,
*  there's three active neurons in the first layer, there's two active neurons in the second layer,
*  and there's only two layers. So essentially there's only five total active neurons
*  that are needed to translate these two inputs to that functional form output. So I'm like, again,
*  that seems like eureka, but then if I could be vulnerable with you for a second,
*  I still don't really get how it's doing it. I'm looking at the graph and I'm like,
*  it's still what's not clicking into my brain is like, oh yeah, now certainly I don't feel like I
*  could diagram a five node thing and know how to predict that function. So how do you interpret
*  that now that we have that super lean, super sparse thing? Is that very meaningful to you?
*  So I can make some explanation what the neural network did. I can actually write down the
*  symbolic formulas and trying to figure out what the neural network are trying to figure out.
*  So I was really shocked when I see the results too, but in hindsight, I think it's understandable
*  in the sense that, well, just like physicists always are fascinated by the unreasonable
*  effectiveness of mathematics, here I would frame our surprise as the unreasonable effectiveness of
*  smooth activation functions. So I'm using silo or salo as activations. They're both smooth functions
*  and in applied math, we know that if we want to approximate a smooth function with Fourier basis,
*  the approximation error drops exponentially as we add more and more higher, you know,
*  higher frequency modes. And the statements can also generalize to other smooth basis functions
*  not just for remotes. So silo or salo in our case. That's well, I understand that's not a very
*  satisfying explanation, but my take is that, wow, this smooth activation functions are
*  remarkably, are unreasonably effective. Are there basically two nonlinearities? Like you have a
*  nonlinearity at each layer? Yes, it has two hidden layers. At each hidden layer, it has a nonlinearity.
*  If people know any activation function, they might know the relu function, which is zero if the value
*  is negative and then just, you know, y equals x if the value is positive. So it looks like straight
*  line and then a sharp corner at zero and then a straight line going up. And the silo function is
*  essentially a curvy approximation of that, which remains differentiable at zero for one thing.
*  Right, right. So basically you have a relu function, but you drag around zero to make
*  a well there. So silo now becomes non-monotonic, but asymptotically when x, when your input is
*  very small, negative, or very large, positive, the asymptotics are the same as relu, but it's
*  only around, it's just that around zero, it's differentiable. So if you want to use relu,
*  did you, I assume you tried relu and it doesn't work? Is that a safe assumption? That's a good
*  question. Actually, somehow I never tried relu. Yeah, it's my unreasonable craze for silo or silo.
*  When you said it's the unreasonable effectiveness of the smooth activations,
*  you're confident enough that this is the better activation function. You don't even need to try
*  the old one. Right, right. And there are papers like proving that with silo or silo, these kind
*  of smooth functions, you can construct like quadratic functions or multiply in two numbers
*  with just two or three neurons. So for example, for the squared function, if you, the silo or
*  silo function is non-monotonic, so there's a bottom. So if you tailor expand around the bottom,
*  you've got a parabola, the quadratic function. So this may sound like you only need one neuron
*  to approximate the quadratic function, which is actually true in construction. But in practice,
*  what really happens, because the chance of being initialized around the bottom is very low. So what
*  really happens in practice is that neural networks have two neurons. Both neurons have their own
*  first order terms, but somehow in the later layers, they weighted them such that their first
*  order terms cancel, but the second order terms survive in tail expansion. So that's where,
*  you know, the cube, sorry, that's where the squared function comes from. By leveraging
*  this sneaky tail expansion trick that, you know, I myself did not think about it. Neural
*  network can be this sneaky, but the networks just discover this themselves. So it's a little bit
*  shocking to me. Like in some sense, neural networks are more clever than myself.
*  Okay. I'm looking at this train network. It takes these four inputs. It predicts these two functions.
*  You know, there's this remarkably sparse structure that is able to achieve this like pretty,
*  you know, non-trivial functional form with just a few neurons. And then on that, you report the loss.
*  And the loss is on this particular thing, I guess it's actually this, it's the joint task
*  of the two predictions, but nevertheless, the loss is 7.4 E minus three or 7.4 times 10 to the
*  minus three. I guess we can jump down to the bottom, right? There you guys have some graphs in the
*  appendix that kind of show this. I was just trying to figure out like, what does that loss
*  mean in terms of, is it like really tightly fitting the functional form or is it kind of
*  loose around it? Like how close does it actually come to learning the functional form?
*  Yeah. So I have the same concern when I just look at the loss function. Yeah. That's why in
*  appendix, we also plot the scatter plots to see how well the predicted results aligned with the
*  ground trip results. And you see, basically they lie on the line and the R squared is like 0.999
*  or something. So that's pretty good. But that's still including this penalty can also still
*  degrade the performance because as I said, to approximate the quadratic function, well,
*  you can approximate a quadratic function acceptably well with just two neurons.
*  But if you include more neurons, the approximation could be better and better.
*  So there is this trade off between accuracy and sparsity. Presumably there's a Pareto frontier,
*  something like that. There's no best solution. There's a Pareto frontier of the solution trading
*  off between accuracy and sparsity and choosing lambda. I mean, choosing the penalty strength
*  actually make us move along that Pareto frontier. Maybe I said lambda to be small. I didn't try it.
*  Maybe I should. If I said lambda to be small, maybe you'll see that there are three or four
*  neurons, but the prediction loss could be better. If you turn the prediction loss up to infinity,
*  then presumably everything just goes to zero and your predictions are all terrible.
*  Right. Yeah. And then if you turn it down to no penalty, then you just are back to the beginning
*  where you have no incentive to sparse five in the first place. Yes. Yes. Yeah. It is pretty,
*  so this is figure 10 in the paper and the, you know, the scanner plot is tight to the line. I can
*  say, you know, it's basically, at least for that one, it's almost indistinguishable from the line.
*  And a couple of these others, you can see a little bit of wobble around the line, but it's still,
*  you know, very close. Do you have any sense for how this works when it comes to, like all of
*  these inputs are on the, on the interval minus one to one, right? Did you look at what would happen
*  if you just started to go a little outside of domain on the input? Could you like just,
*  would that like ruin everything? Yeah. Good question. I honestly, I didn't try that. I
*  would imagine it will fail. Like, I don't believe in like, I don't think in this problem there,
*  like systematic generalization. It's not, it's like, we have no information about the outside.
*  So the network at most can, you know, just do interpolation in, in the range we trained on.
*  So that's my guess. That's maybe a good bridge to start to move into,
*  you know, cause we're still kind of climbing the ladder of complexity in these
*  experiments, right? The first one is purely, it's, you know, synthetic data set derived by these
*  symbolic functional forms, but the network itself is just taking numbers from some narrow interval
*  predicting essentially the curve. We see that amazingly it can learn to do that with just very
*  few active neurons. And we attribute that to the unreasonable effectiveness of the smooth activation
*  curve. But then we could still ask like, okay, we're seeing these kind of conceptual notions
*  that we designed into the problem reflected back to us. We're like, you know, when we set one up,
*  so that in theory we could have two completely distinct sub graphs, indeed, that's what we get.
*  And when we set one up with feature sharing where like, you know, one of the outputs only depends on
*  one of the inputs and the next one depends on two and the next one depends on three.
*  Again, we see like the right information flow that, you know, aligns to our expectations.
*  And then you've got the third one, which is compositionality, which, you know, starts to
*  look a little bit, you know, even more tangled, but like, you know, clearly has some parts that
*  I see as kind of interpretable where like, it appears to me that like a square root function,
*  you know, it kind of consists of like, much like a square function consists of like one neuron
*  going to two and then back to one. So we see these like little moments where we're like,
*  so we see these like little motifs that kind of pop up. And that's all super interesting.
*  But then you could still ask, has this grok anything, you know, that's kind of,
*  can, you know, more conceptual than learning, you know, the explicit shape of a curve?
*  And your expectation is no, but maybe in some of the later experiments that starts to
*  become more relevant, right? So,
*  I mean, even if you cannot generalize outside the training data, it's still interesting to
*  understand like, so I guess what physicists believe that's all the theories we have are
*  effective theories. It's only valuable. It's only valid within, you know, in certain energy
*  scales, so to speak. Yeah. Even if we cannot generalize, there's still a lot of interesting
*  things we can say about at least for the task. Cool. So the next one,
*  I think again, is a really nice little visual, the two moon classification problem. You've got a
*  bunch of points in a 2D space. They're color coded for the viewers, help in interpreting them.
*  The model itself doesn't get that in, it only knows like the position, right? And then has to
*  use the position ultimately to make a prediction of which class the data point belongs to. And it
*  has to learn this kind of curve that separates these two, you know, almost overlapping, but not
*  quite overlapping shapes. And so indeed it does that. And again, you see like a pretty sparse
*  result. I was a little bit just struggling to interpret the last graph there where there's two
*  numbers in, right? The XY coordinate, and then there's the out of like, but it seems like all
*  the nodes are going to class one and like class two has been sort of left. Yeah. That's a very
*  interesting observation. I was surprised by how clever neural networks can be.
*  When I saw the connectivity graph. So for binary classification, what really matters is like the
*  difference of the logistic classes. That is the relative magnitude, but not the absolute magnitude.
*  So an efficient strategy for neural classifiers is to simply set class A to always have
*  zero logics while only learning the logic function for another class B. And a positive
*  logic for class B means that the classification is B and a negative logic for class B means that
*  the classification result is class A. So if we also look at the evolution of the whole thing,
*  the evolution dynamics is actually very interesting. There is this intermediate phase
*  where you see that both classes have output logics. They have network connections to the outputs
*  and they're almost symmetric. But as training goes on and the pruning, and when more weights
*  are got pruned, you see that the network learns to be, to transit from this symmetric phase to
*  the asymmetric phase, because the asymmetric phase is more energy efficient, requiring
*  fewer neuron connections. Yeah. So it's very interesting to see that there's actually this
*  phase transition. At first, it's messy, everything fully connected, and then in the meter state,
*  they're like this sparse network and also symmetric for the two classes. And finally, the network
*  realizes that it only needs to predict the logics for one class while pruning away totally for the
*  other class. So it's a very clever strategy that I learned from my neural networks.
*  I'm studying that final visual and that definitely jumps out. It's basically reduced the dimensionality
*  of the problem on its own to just having now to choose, make one prediction instead of two,
*  effectively. I don't have any other immediate intuitions for the shape of what I'm looking at.
*  Is there anything else you could say about that? So they're sparse. What's good about sparsity is
*  that now you know that there are just seven, if I remember correctly, weights in a graph. So you
*  can just intervene any important weights or neurons to see what it did to the prediction results.
*  I'm guessing because the problem is too simple, it does not have any meaningful structure to emerge.
*  Maybe the whole thing itself is a module. So that's why we don't have very good explanation
*  for it because itself, the whole thing is a module and we don't expect to have a good explanation
*  for internal activations inside modules. Yeah, especially for something as arbitrary as
*  learn to separate two arbitrary shapes. Right. But in pandemics, we did intervention
*  experiments. You can see what each weights and neurons are doing to the...
*  Yeah, that's amazing. There's only six active neurons across the two layers,
*  four in the first, two in the second. Oh, you're actually eliminating connections in this case.
*  Is that right? Yeah, I'm neutralizing individual weight, but yeah, but one in principle can
*  neutralizing the neurons. Yeah. And also, one thing to notice that, well, if you change random
*  seeds, the graph would look completely different. That's another sign that there's no consistent
*  modularity. But if we move on to the modular addition case in the next example, you will see
*  that no matter random seed you have, you almost always have three parallel modules emergence.
*  So this is a more consistent thing you can say about the task. Yeah, random seed also
*  play a huge role here, but my take is that if there's a consistent structure in the task,
*  no matter what your random seed is, you should, for the most time, you should be able to find it.
*  And in the most difficult case where only some of the random seed can find the structure,
*  that's also fine. You can just select the most interpretable. You can just run 100
*  models with different random seeds in parallel, and then select the one that you think you feel
*  most interpretable to you, and you go from there to do MAPInterf. It seems like we probably could
*  graph maybe even in just closed form. Again, I'm not amazing with all the linear algebra notation,
*  but either in closed form or at worst, with just a mesh of points, you could graph
*  the value of class one as a z-axis over the two inputs and get a visualization for like,
*  oh, essentially you're learning a sort of elevation landscape.
*  Yeah, that's correct. So in appendix, we write down the symbolic formulas explicitly. Well,
*  basically just to extract those weights and the biases and write them down into a symbolic formula.
*  So yeah, as you said, in principle, you can plot the 3D surface plot like that.
*  That may be more intuitive to see, but this can all, in principle, one can do that.
*  So yeah, it makes sense then that there's not any super interpretable,
*  there's not like a two sentence summary of this because it's an arbitrary shape. It's almost like
*  you just kind of sprinkled some stuff out there and it had to kind of learn this particular shape,
*  but that's not like a super principle problem in the first place.
*  Yeah, or using the language of the quantization model I mentioned before,
*  the task itself has only one subtask. So there's no need to modularize itself.
*  If we're dealing with some compositional tasks, like language modeling actually involves many
*  subtasks, then there you have the incentive to grow these modules for different abilities.
*  But this two moon classification or later, the transformer example on linear regression,
*  they're just one single task. At least I myself cannot imagine their subtasks that underneath this
*  whole task. So that's why the graphs look a little bit, you know, look less interpretable,
*  look less modular, but that's because the whole network is presumably modules,
*  it's probably a module and they're like this degree of freedom kind of thing that makes the
*  graph look messy. If you were to add a third moon to this or, you know, a third region,
*  would you expect that that would then create some sort of subtask that you could see reflected in
*  modularity? Yeah, maybe we can look at the amnest figures. There, I'm not sure if I can say
*  confidently there, I see something modular, but there's something like this pattern mismatching
*  thing emerging that also interesting, but I can't say for sure that they are meaningful modularity
*  there. But that's a reasonable conjecture. Maybe like classifying between Y and 2 is a subtask,
*  and then 2 and 3 is another subtask, and yeah, and then you can do the, you know,
*  classifying three things by combining this binary classification task. I think that's a reasonable
*  conjecture, but it still needs to be tested. So next, modular addition, one of my favorite
*  problems in the world due to all of the mechanistic interpretability focus on it.
*  The big questions I had on this one were, is this doing the same thing that we've seen kind of prior
*  interpretability work demonstrate that, you know, a grok network is doing? Is it solving the problem
*  in the same way? That's a very good question. Actually, we have a follow-up work that's still
*  not, we're still working on it. So the short answer is yes and no. But yes, I mean, the circles,
*  the embeddings of those numbers are still a four-way basis. That's the same thing as in previous
*  Macintosh works. But by no, I mean that the model, the internal computations are different.
*  We actually find a new, a different algorithm than what Neo and collaborators paper described.
*  So we call Neo's algorithm the clock algorithm. And while we discovered a new algorithm called
*  the pizza algorithm, which algorithm the neural network ends up learning depends on architectures
*  and hyperparameters. And this can be very subtle. And there could be phase transitions from clock
*  to pizza and also pizza to clock. So this is really funny to say out of context, but
*  this is doing ongoing work with my MIT colleagues, Ziqian Zhong, Jacob Andreas and Max Tecma.
*  We'll post the preprint to archive soon, but like this is for, so we discovered clock and
*  pizza algorithm and we test the algorithm, the network we got with BIMT and we find that BIMT
*  actually ends up getting pizza algorithms. The new algorithm we discovered, not what Nanda and
*  collaborators described as the clock algorithm. But no one is wrong. It's simply that, you know,
*  Macintosh can be much more subtle than we could imagine. It's very subtle depending on the
*  architectures and also hyperparameters or kinds of stuff. So the lesson here is there's a lot of
*  possible mechanisms to interpret and which one you end up needing to interpret is kind of cast
*  in the upstream decisions of exactly how you lay out your network and training process. And in this
*  case, localization incentive as well. Right. Yes. Yes. Yeah. Yeah. In short, the clock
*  algorithm is more accurate, but it requires more resources. By contrast, the pizza algorithm is
*  less accurate, but it takes fewer resources. So that's why we see in our BIMT paper, there's
*  three shapes. Maybe I can explain more later because each shape, each parallel module is an
*  imperfect pizza algorithm. So the network needs to come up with some kind of error correction
*  to make each imperfect algorithm to become a perfect one, to aggregate the results from
*  each imperfect algorithm to aggregate them cleverly such that the final outputs are perfect.
*  So that's the takeaway. We hope to post a preprint to archive soon. And
*  is there a simple... So I mean, the clock algorithm is you're doing modular addition,
*  you take advantage of the cyclicality of the modular math. And so you sort of say,
*  okay, I'm going to rotate some and then rotate some more. And then if I get past the origin,
*  I'm naturally kind of the position that I'm at. It doesn't matter how many times I went around,
*  it's just kind of the final position that I need to look at.
*  Right, right, right. But by contrast, the pizza algorithm adds two numbers. So the final prediction
*  is more like slicing pizza and determining which pizza slice the outcome lies on. So the
*  frequency of the pizza algorithm is doubling the frequency of the clock algorithm. Or the other way
*  around, I can't remember exactly, but there's this tiny detail there that actually distinguish
*  between clock and pizza. If you don't look carefully enough, for example, if we use the metric
*  Nanda and collaborators used in their paper, we cannot distinguish clock and pizza algorithm.
*  We came up other metrics that can distinguish between these two algorithms. So there are still
*  these kind of metrics. Each metric is a coarse-grained or drop some information of
*  the whole system. So even if two things are different, but you coarse-grained too much,
*  you end up getting the same thing, you cannot distinguish two things. So my takeaway from this,
*  there's still a lot to be done in Mackintosh. At least we ended up with more metrics to really
*  distinguish those algorithms. Yeah. I'd say we are just scratching the surface. So that's really
*  interesting. When you say it is less accurate, is that a matter of like getting problems wrong,
*  or is it a matter of being less confident with the right answer? So you're in loss higher, but
*  you're still getting all the answers right. So when I say clock algorithm and pizza algorithm,
*  both algorithms have their perfect versions and imperfect versions. So what we end up getting
*  in experiments are their imperfect versions. And the imperfect versions can make wrong answers
*  on some samples, but it can be supplemented by and complemented by another
*  imperfect algorithm, which make wrong answers on another subset of samples. If you have enough
*  number of sufficient number of imperfect copies, at least one copy would give the right answer
*  on every sample. So by aggregating the results, finally, the final aggregated result would make
*  the correct prediction on every sample. But for one head or one parallel module, it can only make
*  prediction correct on some subset of all the samples. So you essentially train
*  in copies of this tiny little network. And then you find that, I guess, due to random seeds,
*  they sort of cohere in different ways. Each one represents an imperfect approximation of the ideal
*  algorithm. And then in aggregating them, you can kind of get good performance, even if they have
*  their individual weaknesses. I mean, we don't explicitly have this end copies. We just have a
*  whole network. But we can somehow disentangle and find that automatically their end copies emerge
*  from training, which is really fascinating. And this is, again, an example of where I think,
*  oh, maybe your network is more clever than myself. It leverages kind of our question.
*  Is that what is meant by voting? Yes, exactly. Okay. So as we're looking at this graph, and again,
*  it's not that big, right? We're talking about two hidden layers. So that is to say,
*  inputs, two hidden layers, again, I assume each with nonlinearity as part of that layer,
*  and then outputs. There's not really that much room to do the work here. I've always kind of,
*  through every graph in this paper, leaves me feeling the same way about that. And then each of these,
*  as you look at it, it's just clear that there are like three distinct modules that go from the
*  inputs up to layer two. And then at layer two, it's basically all kind of fully connected,
*  it looks like again, to the output. But those three distinct sections are, you're saying,
*  now I'm understanding these shapes more deeply. So each of those is an approximation. And I guess
*  you can see that because you can do the ablation here still like... Yes. So each copy is an algorithm
*  that tries to perfectly do the modular addition, but fails. So somehow the neural net,
*  at some points, the neural net figures out that, oh, it's more expensive to form one perfect copy of
*  a single algorithm. So instead, I resort, I form like three copies of imperfect algorithms,
*  and somehow aggregate some sort of majority voting to get the end results.
*  And how literally do you understand that concept of voting? I always push really hard on analogies,
*  because I find I confuse myself as often as I clarify things for myself.
*  Yeah. So the terminology voting actually comes from... So we borrow the term from error correction
*  as in information theory. So let's say you want to communicate a classical bit,
*  0 or 1, over some channel. The channel is imperfect. It can randomly flip the bit
*  with some probability. So to achieve better accuracy, there's something called the repetition
*  code, which basically you repeat the bit for three times or five times or even more.
*  So then the receiver then can infer the bit by doing a majority voting of the three bits.
*  The probability of making that error reduces exponentially as the repetition times grows larger.
*  So this analogy of repetition code also applies to module addition here. Each shape or each module
*  is an imperfect algorithm of module addition. One module alone can make mistakes on some examples,
*  but by aggregating these three modules together, or when I say vote, I actually mean aggregating.
*  Just the last linear layer aggregates the results, but just by aggregating or voting their
*  results, they can end up with perfect classification results.
*  In the bit level example from the information theory, you basically repeat the signal three
*  times and you trust that it's unlikely that two out of three get degraded, so I can trust two
*  out of three. That's the basic intuition. Yes. And also there is this independent voter,
*  the flipping thing are independent. So I'm trying to map that concept onto
*  the data that I see here. And it's like, I would expect, and I'm being very literal,
*  so I guess my approach in this is trying to be very literal and see if I get confused.
*  And I am getting a little confused because I guess if I was thinking of it in a strict analogy and I
*  said, let's imagine that I'm using this voting approach, but then I just eliminate one of my
*  inputs. Now I've got two inputs. Now if they agree, great. If they disagree, I'm at 50-50 chance.
*  But what it seems here is you knock out one and your performance is much more degraded than 50-50.
*  Yeah. So I think the majority voting thing is more like a metaphor. What really happens is the
*  linear aggregation of the outputs. And it's more like cooperation. So in majority voting,
*  we assume the voters to be independent to each other. But here we sort of like,
*  since we're adding this kind of penalty to the network, the three modules really need to
*  cooperate with each other. So they rely on each other. Somehow they talk to each other in training.
*  So for example, the first module say, I take sample A. And then the second module say, I take,
*  then I will take sample B. Something like that. But even more complicated because it's a linear
*  combination of things. We cannot partition things that clearly. In principle, we can understand,
*  we can try to understand the structure more clearly. But I haven't done that. But I think
*  it's something to investigate in details. So the major basis, I guess, then for the
*  kind of notion of voting metaphor or the reason that you're saying that you interpret these three
*  modules as kind of each an independent approximation is more anchored to those shapes, I guess? You
*  show kind of the spatial representation and that definitely looks like something.
*  Yes. Yes. I think it's more anchored on the shapes. And it's surprising to me,
*  at least to see that three modules emerge. And finally, I understand that, oh, there's
*  this error correction mechanism that we didn't think about. Yeah, it's amazing. We learned
*  something from newer networks. I think when I looked at the next problem around permutations,
*  anything you want to say on that that kind of jumps out as the most important takeaway for you?
*  So the best part I love about the permutation example is that Neo and the collaborators
*  found that the network can automatically learn the group representations. And for
*  S4 permutation group, it has a nine-dimensional representation. But they still need to probe
*  and find where to look at. But this nine-dimensional representation just naturally
*  emerge on privileged basis, like aligned with the neurons after training. And there are exactly
*  nine active neurons and there are exactly one sine neuron, the magic 22nd neuron, corresponding
*  to the sine of the representation. And all the other neurons, we can also explain them based on
*  calligraphy. And it tells us that the neural network indeed leverages the structure of the
*  group data sets. So I think the main takeaway is that, well, with BIMT, you can clearly know
*  where you should be looking at by just looking at the graph. But with other methods like probing
*  or intervention, at first you have no idea where to look at, or you need to really understand your
*  problem so that you know where to look at. But BIMT, you don't need to know anything about the
*  task. You just look at the graph and you can say something useful about it.
*  Yeah, I have this visualization sometimes in my mind of like shrink wrapping conceptual reality.
*  And I don't know how, there's probably a lot of, that's kind of an analogy. So,
*  my analogy detector goes off, but it does feel like you've kind of created another
*  way to create additional kind of negative pressure to like suck all of the extraneous activity
*  out of the network and then kind of snaps or coheres right into the appropriate dimension.
*  So the paper, we only have those static images, but if you look at the videos I posted on Twitter
*  and also on GitHub, this is exactly what you described. You seem to have some kind of pressure
*  that push inwards and the shrink prune, the whole thing. Yeah, really amazing. I encourage everyone
*  to watch the videos. Okay, so we're getting into the homestretch. So the next thing you do is then
*  extend this to the transformers. Everything we've talked about so far, I wanted to ask too,
*  like how long does it take to train these really simple networks? Like if you were to set up
*  one run to train the modular addition network and it goes through how many steps?
*  To 20,000, I guess. So how long does that actually take just on a fairly standard issue computer?
*  Yeah, so actually all the results I got, I'm just using my Mac M1. There are no GPU.
*  So for the modular addition, it takes around 20 minutes. For symbolic formulas, just less than
*  one minute. The transformer example is the most time-consuming one, ranging from one hour to two
*  hours, but hours at most. So if you want to play with BIM, I encourage you to start playing with
*  the symbolic regression example. You can even make modifications to the code. It's a very fast
*  iteration because to get the results, it only takes less than one minute to get the results.
*  So it's a good point to start. So it basically can feel with these later projects, not quite,
*  but with the simplest cases, it's almost like kind of real-time. I presume you could even just kind
*  of, although yeah, I guess if you don't go all the steps, you don't see all the sparsity. So you do
*  kind of have to run it to some sort of completion. You mentioned the transformer portion. It wasn't
*  entirely clear to me. Are you modifying the attention mechanism as well as the fully connected
*  portion of the transformer? Yeah, that's a very good question. So think about attention layers.
*  If we put aside the softmax part of the attention layer, so the attention layer is just three
*  linear, just three matrix multiplication, the key, query, and value. So this linear matrix,
*  we can understand them as a linear layer with zero bias. So we apply the same trick we used in MLP,
*  just treat it as a linear layer. So attention layer, the softmax has no parameters, so we don't
*  have to worry about that. We just need to deal with this linear matrix as in MLPs.
*  So the representation of this then for kind of purposes of the loss function is in the
*  fully expanded form. You have this sort of three multiplications, but you're treating those as
*  essentially one giant. That's a good question. So there are three matrices. I overlapped them.
*  I stacked them along a third dimension. I actually did not plot. And the shift along the third
*  dimension is very small just to visualize it. But because query, key, and value, they're actually
*  in some sense they're equivalent. So there's no sense to separate them in space. So they're
*  overlapping each other. But visually, you can think of them separated by small amounts
*  along the third dimension. Would this have a, for kind of scaling up purposes,
*  I'm not great with this sort of optimization of this, but I definitely followed Neil Nanda's work
*  quite a bit. And what I understand from, I think, taking away from some of his YouTube tutorials is
*  that there's a divergence between the representation of the attention mechanism that is most compute
*  efficient and therefore actually gets used in code from a more purely analytical,
*  purely analytical representation that's easier to interpret. And if I understand correctly,
*  you're applying the penalty in a way that works on that more analytically sound, not separated,
*  but maybe less compute efficient representation. Do I have that right? Or am I going off track
*  somewhere? Sorry, what do you mean by low compute representation here?
*  So you had said a second ago that the sort of multiple matrix operations that constitute the
*  transformer mechanism in analytical terms are not really separable, but they are in practice,
*  they are sort of coded separately, as I understand it, for efficiency reasons.
*  I see. So I treat them independently.
*  So the penalty is added in and calculated in such a way that the process of calculating that penalty
*  would scale, the whole process would still scale just like a normal transformer scales?
*  Yeah, exactly. There's no additional overhaveness.
*  Can you maybe just help develop a little bit more of the intuition of
*  how exactly should I understand the locality penalty in the context of attention? In the above
*  simple graphs, it makes total sense. It's just okay, 2D space, boom, I got it. Is there anything
*  more that I should kind of be intuiting for the attention version? Yeah, so that's a very good
*  question. Actually, it takes a lot of, it takes at least some sort of modifications to make it work,
*  to make BIM work on transformers. I don't have an intuitive picture for that, but
*  like the modifications are, you need to consider the head, the multi-headed attention.
*  And that affects swapping. We cannot just swap in two neurons in the same layer. We can only swap
*  the two neurons in the same layer and also in the same head. But we can also swap two heads
*  as a whole. We can always swap two heads. And the residual stream is another pain in the ass.
*  Because with the residual stream, the neurons got aligned. So the permutation in,
*  although the residual stream are in some sense locked. So their permutations are not independent.
*  The residual stream in different layers, they share the same permutation.
*  They share the same permutation. That may also be one thing that makes the network
*  less interpretable or less local. And that's kind of presumably related to like
*  superposition or not, not really, I guess. Basically, the idea is that there, you would
*  have to untangle. If you're going to swap, you'd have to swap at every layer of the residual stream.
*  Yes. If you swap, you need to swap every layer of the residual stream. So that sounds to me like
*  a constraint. I think it's undesirable because if you have this constraint,
*  you have to consider across all the layers. So you cannot untangle some non-local connections
*  in some certain layer because you need to consider everything globally. Maybe there are
*  better ways to do this. So again, I think there's still a lot of things to be done to improve BIMT.
*  And also another pain in the ass is layer norm. So I think Ampropic published their
*  results also arguing that layer norm did something sneaky. So in our case, we also
*  dropped, so they didn't drop layer norm. They just say, oh, layer norm is a pain in the ass.
*  But I dropped layer norm entirely because it's normalized things. Sometimes even it has a small
*  input, it still normalizes it to zero to one range. And that's something we don't want with sparse
*  neural networks. Yeah. So again, so there are still engineering tricks that we
*  need to incorporate to make BIMT work on transformers. This is just the first step
*  that I want to show that while in principle, BIMT is a high level idea that you can apply to any
*  architectures as long as you value architecture in a geometric space. And this is just a prototype
*  example, but a lot of things can be done in the future. That brings us, I think, to the last
*  experiment in the last visualization, which is applying this to 3D space instead of 2D space.
*  And here you're using the classic MNIST handwritten data sets, handwritten digit data set.
*  And of all the visualizations, I don't know, there's some good ones, but this one might be
*  the best because you see at the beginning just a massive 3D tangle of intersecting weights.
*  And then over the course of all the steps, it gets just much more, first of all, kind of cropped in
*  to the actual space where the images actually are. And then just obviously a lot more sparse.
*  It seems like in this one, again, what is it really doing is sort of limited. So we still need the
*  kind of, we still need the Neil Nand to break down, but you've kind of run the first leg of
*  the relay in that you have, by sparsifying things, made it pretty clear where to look, as you say.
*  And then next step is for somebody to kind of figure out to what degree can we kind of
*  assign any meaning to this. And maybe not, I guess. It could just be that this is like a super tight
*  module that does this really weird task and the shape of the numerals themselves is kind of a,
*  especially as played out across a ton of handwritten versions, is just weird and
*  there's not necessarily more to say about it. Yeah, that's a reasonable conjecture. It could
*  be that the task could be just too simple. The whole thing, due by the network, is just a whole
*  task. There's no subtasks. Like even linear classifiers can get above 90% accuracy on this.
*  It could also be that vision tasks, at least for image classification,
*  demonstrates less modularity than language tasks. As I imagine, the language tasks presumably have
*  many quanta, have many subtasks, and also the chain of thought reasoning thing in language
*  models might be related to modularity. You need each step you have a concrete reasoning step.
*  So I personally think that maybe BIM's ability to make language models more modular,
*  more than vision models. That's where I'm imagining. So about next step, I think I will try
*  BIM's on language models, but also I think it's important to, like lately, AI for Science,
*  try all kinds of scientific problems where interpretability, people also care a lot about
*  interpretability in scientific problems. So I think that's where BIM can also play a huge role.
*  So my next step would be language model and scientific problems.
*  Cool. Do you want to comment just for a second on the pattern anti-matching, followed by pattern
*  matching? And so it's kind of like, from there's the input layer, and then in kind of the, there's
*  again just two hidden layers, right? Between the first and the second hidden layers looks like
*  basically all the weights are negative. And then from the second layer to the output, all the weights
*  are positive. And you're interpreting that as pattern anti-matching. I guess my answer is
*  probably going to be the non-linearity, because I was initially thinking, if we just change the sign
*  of all the weights, would it still just work? But the answer, I guess, is no, because of the
*  non-linearity. Yeah. I think non-linearity also plays a role here. So in appendix, we also tried
*  one hidden layer and three hidden layer. We find this anti-pattern mismatching thing are consistent.
*  No matter how deep your neural networks are, at least for one or two or three hidden layers,
*  they're consistent. So I'm guessing there's something deep or fundamental about it, like
*  this kind of strategy is more biologically or energy efficient than what we would imagine.
*  Like how we classify, how we do image recognition, we would... So previously, we would imagine that
*  we want to do pattern matching. We have a template of things. Say we have a dog feature,
*  and we scan over the whole image and try to max polling to see if there is a dog on the image.
*  But it seems like by having this beamed strategy, you end up doing something opposite.
*  Like you want to tell, oh, this image does not have a dog. So it's more likely to a cat,
*  something like that. So I can't say that I have fully understand this. There's still
*  things to be understood. Anything that you would add, just to kind of wrap things up on
*  the paper front before just asking a few more general questions? Yeah. So one thing I still
*  want to know is that about the next direction, you mentioned tiny stories. So that's one direction
*  I'm looking to lately. One thing I'm hoping that BEAMD can achieve on tiny stories,
*  which is already achieved for module addition, is that the learnable token embeddings have
*  privileged basis or a better line with coordinate basis. For example, there's presumably a direction
*  in the embedding space corresponding to color. Say with unprivileged basis, you need to try really
*  hard to search for that color direction and then project token embeddings to that direction. But
*  there are actually infinitely many possible directions. But with privileged basis or with
*  BEAMD, very likely there's just one dimension of the token embeddings corresponds to the color
*  dimension. So you can just obtain that direction by enumerating the finite number of the embedding
*  dimensions. But yeah, one thing I'm thinking about whether it can scale, whether BEAMD can scale to
*  large networks. So my only concern so far is that it might be harder to visualize the whole network.
*  This is apparent difficulty. But other than that, the way I'm seeing it, I don't see any
*  deal breaker here. I don't necessarily see any factor that blocking it from scaling.
*  I'm actually doing another interview with one of the authors of the Megabyte paper that has kind of
*  the hierarchical approach. This seems like it could sort of play nicely with that as well, perhaps,
*  although I don't quite know how. But it has these sort of a global model and then a bunch of these
*  local models. And I don't know, have you thought about any sort of trying to apply this to any sort
*  of more hierarchical structure such that modules could naturally cohere in different places?
*  Yeah, that's a good question. Actually, like I mentioned, an outstanding researcher, Jeff Kuhn,
*  on connection cost thing like 10 years ago, but in biology, right? They discovered that
*  by imposing this connection cost thing, you not only induce modularity, you also induce
*  hierarchy and also allows you to do lifelong learning or continual learning. So a lot of
*  promising directions. But the regularity thing, as you said, like, is it possible to have one module
*  that can be copied all over the network? For example, there's a basic unit that you need
*  to record it multiple times. Unfortunately, this kind of connection cost techniques itself
*  cannot induce this kind of repetition or regularity. And you need some. So this is another thing I'm
*  thinking about lately. I want to draw inspiration from biology and some kind of stuff. And there's
*  some literature like trying hyper networks or some compositional producing networks,
*  something like that, to make sure the regularity or the repetition of the mod to reuse the modules.
*  But that's something orthogonal to modularity and hierarchy. I think there are many traits. I'm
*  all very interested in modularity, hierarchy, locality, module reusability. Maybe they're
*  connected somehow, but at least BIMP cannot solve the last one, cannot solve module reusability.
*  That's one thing I'm thinking. Maybe I can improve, integrate some kind of hyper network
*  technique into BIMP to make it also leverage this kind of module reusability structure. And also,
*  this is for better efficiency. If we can decompose a network into different motifs,
*  we only need to restore those motifs and how these motifs connected to each other. We don't need to
*  store the same motifs for thousands of times. So that's also for more efficient storage and
*  more efficient inference, especially for large scale models. If we can downsize large scale models
*  in this way, decomposing them into motifs, that would be awesome. And the inference time efficiency
*  gains, at least on these toy models, are pretty huge. If you run the fully connected version
*  versus the... Say you take the sparse version and actually prune it and you just only have the
*  fewer weights at the end, presumably it's like under 10% the compute cost at inference time.
*  So if we explicitly sparsify the network after training, the inference time would be
*  very much reduced. Like in the modular addition example, there's three parallel modules emerge
*  from training. We don't know a prior that there are three parallel modules, but they just emerge.
*  With that, we can make them parallelizable. For example, we can run these three modules in parallel
*  and then use one machine in principle, and then use one machine to aggregate the whole results.
*  If this kind of parallelization can also generalize to language models, that would be fascinating
*  because then the inference time can be saved. You can leverage all sorts of
*  multi-fretting or parallelization techniques we have at hand to make sure that the
*  inference time and the inference memory can be saved by a large margin.
*  That seems extremely compelling actually. Max Tegmark is your advisor. He has not,
*  for most of his career, has not been in AI. Did he already make the switch into AI and then you
*  joined the group after that switch? Tell me the story of working with somebody who's
*  obviously got some special ability but is new to AI.
*  I cannot recall the exact year Max switched to AI, but I joined the group after Max switched to AI.
*  When I joined the group, we were still focusing on AI for physics because Max used to be a
*  cosmologist. I have a strong background in physics. He has a position in the Department of Physics.
*  I also got admitted to the Department of Physics at MIT.
*  I did research on AI for physics with Max for two or three years. I'm in my third year right now.
*  Then Max decided to switch entirely the focus to AI safety, Mac and Terp specifically, because
*  trained as physicists, we think that we need to first fully understand something so that we can
*  fully control it. We can fully keep AI systems under control. It did no harm to our human beings.
*  But the first step is to basically to understand it.
*  I've been an admirer of his work for a number of years and it's been cool to see that he's been so
*  flexible and adaptable and has been able to attract some bright minds to the group
*  to do some exciting work. I'm struck by the fact that from what I understand just on your website
*  and briefly looking at your background, you grew up in China, went to university in China and then
*  came here after university, is that right? Yes, I went to Peking University in the physics
*  school of physics. Then Max hired me as his PhD student. I've been here in the US for two years.
*  Does the general broader context of US-China tension and the increasingly center stage that
*  AI has in that broader debate, is that relevant to you personally? Do you just try to stay out of it?
*  How do you engage with that subject, if at all? I agree with Max on this point. The existential
*  risk is a common threat to all human beings. If we see this as an extinction risk and no one can
*  survive if we don't collaborate. With this, actually this can bring together US and China
*  collaboration on this AI safety thing. I think collaboration is the right way, not opposing each
*  other. Yeah, totally. I try to highlight any instance of positive US-China relationship
*  and collaboration that I can. Your time here and work on this project is a great example of that.
*  I'm really appreciative that you've spent so much time walking through it with us. Keep up the great
*  work, whether it's here or whether it's one day back in China. Hopefully, you can continue to span
*  the two indefinitely. We certainly need a lot more of this ability to understand because,
*  as I think you guys put it very well, understanding is usually a precondition for control.
*  And everybody has a shared interest in figuring out how to control these systems so we can get
*  the best from them and avoid the worst. Yeah, sure. Thank you so much for the invitation.
*  Yeah, it was great speaking to you and have fun with your family. Thank you very much.
*  Thank you for being part of the cognitive revolution. Omniki uses generative AI to
*  enable you to launch hundreds of thousands of ad iterations that actually work customized across
*  all platforms with a click of a button. I believe in Omniki so much that I invested in it and I
*  recommend you use it too. Use Cogrev to get a 10% discount.
